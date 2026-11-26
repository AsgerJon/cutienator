//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmldelayedcallqueue_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmldelayedcallqueue_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qqmldelayedcallqueue_p.h>
#include <QtQml/private/qqmlengine_p.h>
#include <QtQml/private/qqmljavascriptexpression_p.h>
#include <QtQml/private/qv4value_p.h>
#include <QtQml/private/qv4jscall_p.h>
#include <QtQml/private/qv4qobjectwrapper_p.h>
#include <QtQml/private/qv4qmlcontext_p.h>
#include <QtQml/QQmlError>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/qml/qqmldelayedcallqueue.cpp, line 21, as _ZNK20QQmlDelayedCallQueue19DelayedFunctionCall7executeEPN3QV415ExecutionEngineE
inline void QQmlDelayedCallQueue::DelayedFunctionCall::execute(QV4::ExecutionEngine *engine) const
{
    if (!m_guarded ||
            (!m_objectGuard.isNull() &&
             !QQmlData::wasDeleted(m_objectGuard) &&
             QQmlData::get(m_objectGuard) &&
             !QQmlData::get(m_objectGuard)->isQueuedForDeletion)) {

        QV4::Scope scope(engine);

        QV4::ArrayObject *array = m_args.as<QV4::ArrayObject>();
        const QV4::FunctionObject *callback = m_function.as<QV4::FunctionObject>();
        Q_ASSERT(callback);
        const int argCount = array ? array->getLength() : 0;
        QV4::JSCallArguments jsCallData(scope, argCount);
        *jsCallData.thisObject = QV4::Encode::undefined();

        for (int i = 0; i < argCount; i++) {
            jsCallData.args[i] = array->get(i);
        }

        callback->call(jsCallData);

        if (scope.hasException()) {
            QQmlError error = scope.engine->catchExceptionAsQmlError();
            error.setDescription(error.description() + QLatin1String(" (exception occurred during delayed function evaluation)"));
            QQmlEnginePrivate::warning(QQmlEnginePrivate::get(scope.engine->qmlEngine()), error);
        }
    }
}

//  from ../qtdeclarative/src/qml/qml/qqmldelayedcallqueue.cpp, line 74, as _ZN20QQmlDelayedCallQueue26addUniquelyAndExecuteLaterEPN3QV415ExecutionEngineEP14QQmlV4Function
inline QV4::ReturnedValue QQmlDelayedCallQueue::addUniquelyAndExecuteLater(QV4::ExecutionEngine *engine, QQmlV4FunctionPtr args)
{
    QQmlDelayedCallQueue *self = engine->delayedCallQueue();

    QV4::Scope scope(engine);
    if (args->length() == 0)
        THROW_GENERIC_ERROR("Qt.callLater: no arguments given");

    QV4::ScopedValue firstArgument(scope, (*args)[0]);

    const QV4::FunctionObject *func = firstArgument->as<QV4::FunctionObject>();

    if (!func)
        THROW_GENERIC_ERROR("Qt.callLater: first argument not a function or signal");

    std::pair<QObject *, int> functionData = QV4::QObjectMethod::extractQtMethod(func);

    QList<DelayedFunctionCall>::Iterator iter;
    if (functionData.second != -1) {
        // This is a QObject function wrapper
        iter = self->m_delayedFunctionCalls.begin();
        while (iter != self->m_delayedFunctionCalls.end()) {
            DelayedFunctionCall& dfc = *iter;
            std::pair<QObject *, int> storedFunctionData = QV4::QObjectMethod::extractQtMethod(dfc.m_function.as<QV4::FunctionObject>());
            if (storedFunctionData == functionData) {
                break; // Already stored!
            }
            ++iter;
        }
    } else {
        // This is a JavaScript function (dynamic slot on VMEMO)
        iter = self->m_delayedFunctionCalls.begin();
        while (iter != self->m_delayedFunctionCalls.end()) {
            DelayedFunctionCall& dfc = *iter;
            if (firstArgument->asReturnedValue() == dfc.m_function.value()) {
                break; // Already stored!
            }
            ++iter;
        }
    }

    const bool functionAlreadyStored = (iter != self->m_delayedFunctionCalls.end());
    if (functionAlreadyStored) {
        DelayedFunctionCall dfc = *iter;
        self->m_delayedFunctionCalls.erase(iter);
        self->m_delayedFunctionCalls.append(dfc);
    } else {
        self->m_delayedFunctionCalls.append(QV4::PersistentValue(engine, firstArgument));
    }

    DelayedFunctionCall& dfc = self->m_delayedFunctionCalls.last();
    if (dfc.m_objectGuard.isNull()) {
        if (functionData.second != -1) {
            // if it's a qobject function wrapper, guard against qobject deletion
            dfc.m_objectGuard = QQmlGuard<QObject>(functionData.first);
            dfc.m_guarded = true;
        } else if (const auto *js = func->as<QV4::JavaScriptFunctionObject>();
                   js && js->scope()->type == QV4::Heap::ExecutionContext::Type_QmlContext) {
            QV4::QmlContext::Data *g = static_cast<QV4::QmlContext::Data *>(js->scope());
            Q_ASSERT(g->qml()->scopeObject);
            dfc.m_objectGuard = QQmlGuard<QObject>(g->qml()->scopeObject);
            dfc.m_guarded = true;
        }
    }
    self->storeAnyArguments(dfc, args, 1, engine);

    if (!self->m_callbackOutstanding) {
        self->m_tickedMethod.invoke(self, Qt::QueuedConnection);
        self->m_callbackOutstanding = true;
    }
    return QV4::Encode::undefined();
}

//  from ../qtdeclarative/src/qml/qml/qqmldelayedcallqueue.cpp, line 147, as _ZN20QQmlDelayedCallQueue17storeAnyArgumentsERNS_19DelayedFunctionCallEP14QQmlV4FunctioniPN3QV415ExecutionEngineE
inline void QQmlDelayedCallQueue::storeAnyArguments(DelayedFunctionCall &dfc, QQmlV4FunctionPtr args, int offset, QV4::ExecutionEngine *engine)
{
    const int length = args->length() - offset;
    if (length == 0) {
        dfc.m_args.clear();
        return;
    }
    QV4::Scope scope(engine);
    QV4::ScopedArrayObject array(scope, engine->newArrayObject(length));
    uint i = 0;
    for (int j = offset, ej = args->length(); j < ej; ++i, ++j)
        // fromReturnedValue is safe, args should already ensure marking
        array->put(i, QV4::Value::fromReturnedValue((*args)[j]));
    dfc.m_args.set(engine, array);
}

//  from ../qtdeclarative/src/qml/qml/qqmldelayedcallqueue.cpp, line 163, as _ZN20QQmlDelayedCallQueue23executeAllExpired_LaterEv
inline void QQmlDelayedCallQueue::executeAllExpired_Later()
{
    // Make a local copy of the list and clear m_delayedFunctionCalls
    // This ensures correct behavior in the case of recursive calls to Qt.callLater()
    QList<DelayedFunctionCall> delayedCalls = m_delayedFunctionCalls;
    m_delayedFunctionCalls.clear();

    QList<DelayedFunctionCall>::Iterator iter = delayedCalls.begin();
    while (iter != delayedCalls.end()) {
        DelayedFunctionCall& dfc = *iter;
        dfc.execute(m_engine);
        ++iter;
    }
}
//  -----------------------------------------------------------------------

//  A QQmlDelayedCallQueue that Python can take functions over in. Every QQmlDelayedCallQueue
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlDelayedCallQueueCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlDelayedCallQueueCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlDelayedCallQueueCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlDelayedCallQueueCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlDelayedCallQueueCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlDelayedCallQueueCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlDelayedCallQueueCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQmlDelayedCallQueue : public QQmlDelayedCallQueue {
public:
  using QQmlDelayedCallQueue::QQmlDelayedCallQueue;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQmlDelayedCallQueueCall0 call = reinterpret_cast<CuteQQmlDelayedCallQueueCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQmlDelayedCallQueueCall1 call = reinterpret_cast<CuteQQmlDelayedCallQueueCall1>(taken[1]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQmlDelayedCallQueueCall2 call = reinterpret_cast<CuteQQmlDelayedCallQueueCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQmlDelayedCallQueueCall3 call = reinterpret_cast<CuteQQmlDelayedCallQueueCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQmlDelayedCallQueueCall4 call = reinterpret_cast<CuteQQmlDelayedCallQueueCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQmlDelayedCallQueueCall5 call = reinterpret_cast<CuteQQmlDelayedCallQueueCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQmlDelayedCallQueueCall6 call = reinterpret_cast<CuteQQmlDelayedCallQueueCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQmlDelayedCallQueue::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20QQmlDelayedCallQueue10metaObjectEv(
    const QQmlDelayedCallQueue *self) {
  return self->metaObject();
}

//  void *QQmlDelayedCallQueue::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN20QQmlDelayedCallQueue11qt_metacastEPKc(
    QQmlDelayedCallQueue *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQmlDelayedCallQueue::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN20QQmlDelayedCallQueue11qt_metacallEN11QMetaObject4CallEiPPv(
    QQmlDelayedCallQueue *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QQmlDelayedCallQueue::~QQmlDelayedCallQueue()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlDelayedCallQueueD1Ev(QQmlDelayedCallQueue *self) {
  delete self;
}

//  QV4::ReturnedValue
//      QQmlDelayedCallQueue::addUniquelyAndExecuteLater(QV4::ExecutionEngine
//      *engine, QQmlV4FunctionPtr args)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN20QQmlDelayedCallQueue26addUniquelyAndExecuteLaterEPN3QV415ExecutionEngineEP14QQmlV4Function(
    QV4::ExecutionEngine *engine,
    QQmlV4FunctionPtr args) {
  return QQmlDelayedCallQueue::addUniquelyAndExecuteLater(engine, args);
}

//  void QQmlDelayedCallQueue::ticked()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlDelayedCallQueue6tickedEv(QQmlDelayedCallQueue *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQmlDelayedCallQueue")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "ticked()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "ticked()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQmlDelayedCallQueue::storeAnyArguments(DelayedFunctionCall &dfc,
//      QQmlV4FunctionPtr args, int offset, QV4::ExecutionEngine *engine)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlDelayedCallQueue17storeAnyArgumentsERNS_19DelayedFunctionCallEP14QQmlV4FunctioniPN3QV415ExecutionEngineE(
    QQmlDelayedCallQueue *self,
    QQmlDelayedCallQueue::DelayedFunctionCall *dfc,
    QQmlV4FunctionPtr args,
    int offset,
    QV4::ExecutionEngine *engine) {
  self->storeAnyArguments(*dfc, args, offset, engine);
}

//  void QQmlDelayedCallQueue::executeAllExpired_Later()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlDelayedCallQueue23executeAllExpired_LaterEv(
    QQmlDelayedCallQueue *self) {
  self->executeAllExpired_Later();
}

//  a Python function taken by a CuteQQmlDelayedCallQueue, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlDelayedCallQueue(
    QQmlDelayedCallQueue *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlDelayedCallQueue *>(self)->take(key, call);
}
