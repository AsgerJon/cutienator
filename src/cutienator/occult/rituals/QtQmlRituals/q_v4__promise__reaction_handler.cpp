//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4promiseobject_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4promiseobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/QCoreApplication>
#include <QtQml/private/qv4promiseobject_p.h>
#include <QtQml/private/qv4symbol_p.h>
#include <QtQml/private/qv4jscall_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/jsruntime/qv4promiseobject.cpp, line 54, as local:qv4promiseobject.cpp:PROMISE_REACTION_EVENT
namespace QV4::Promise {
using namespace QV4;
const int PROMISE_REACTION_EVENT = QEvent::registerEventType();
}  // namespace QV4::Promise

//  from ../qtdeclarative/src/qml/jsruntime/qv4promiseobject.cpp, line 55, as local:qv4promiseobject.cpp:PROMISE_RESOLVE_THENABLE_EVENT
namespace QV4::Promise {
using namespace QV4;
const int PROMISE_RESOLVE_THENABLE_EVENT = QEvent::registerEventType();
}  // namespace QV4::Promise

//  from ../qtdeclarative/src/qml/jsruntime/qv4promiseobject.cpp, line 57, as local:qv4promiseobject.cpp:ReactionEvent
namespace QV4::Promise {
using namespace QV4;
struct ReactionEvent : public QEvent
{
    ReactionEvent(ExecutionEngine *e, const Value *reaction_, const Value *resolution_)
            : QEvent(QEvent::Type(PROMISE_REACTION_EVENT)),
              reaction{e, *reaction_},
              resolution{e, *resolution_}
    {}

    QV4::PersistentValue reaction;
    QV4::PersistentValue resolution;
};
}  // namespace QV4::Promise

//  from ../qtdeclarative/src/qml/jsruntime/qv4promiseobject.cpp, line 69, as local:qv4promiseobject.cpp:ResolveThenableEvent
namespace QV4::Promise {
using namespace QV4;
struct ResolveThenableEvent : public QEvent
{
    ResolveThenableEvent(ExecutionEngine *e, const PromiseObject *promise_, const Object *thenable_, const FunctionObject *then_)
        : QEvent(QEvent::Type(PROMISE_RESOLVE_THENABLE_EVENT)), promise(e, *promise_), thenable(e, *thenable_), then(e, *then_)
    {}

    QV4::PersistentValue promise;
    QV4::PersistentValue thenable;
    QV4::PersistentValue then;
};
}  // namespace QV4::Promise

//  from ../qtdeclarative/src/qml/jsruntime/qv4promiseobject.cpp, line 101, as _ZN3QV47Promise15ReactionHandler11customEventEP6QEvent
namespace QV4::Promise {
using namespace QV4;
inline void ReactionHandler::customEvent(QEvent *event)
{
    if (event)
    {
        const int type = event->type();
        if (type == PROMISE_REACTION_EVENT)
            executeReaction(static_cast<ReactionEvent*>(event));

        if (type == PROMISE_RESOLVE_THENABLE_EVENT)
            executeResolveThenable(static_cast<ResolveThenableEvent*>(event));
    }
}
}  // namespace QV4::Promise

//  from ../qtdeclarative/src/qml/jsruntime/qv4promiseobject.cpp, line 114, as _ZN3QV47Promise15ReactionHandler15executeReactionEPNS0_13ReactionEventE
namespace QV4::Promise {
using namespace QV4;
inline void ReactionHandler::executeReaction(ReactionEvent *event)
{
    Scope scope(event->reaction.engine());

    Scoped<QV4::PromiseReaction> ro(scope, event->reaction.as<QV4::PromiseReaction>());
    Scoped<QV4::PromiseCapability> capability(scope, ro->d()->capability);

    ScopedValue resolution(scope, event->resolution.value());
    ScopedValue promise(scope, capability->d()->promise);

    if (ro->d()->type == Heap::PromiseReaction::Function) {
        ScopedFunctionObject handler(scope, ro->d()->handler.as<QV4::FunctionObject>());
        ScopedValue result(scope, handler->call(promise, resolution, 1));

        ScopedFunctionObject reaction(scope);
        if (scope.hasException()) {
            reaction = capability->d()->reject.as<QV4::FunctionObject>();
            result = scope.engine->catchException();
        } else {
            reaction = capability->d()->resolve.as<QV4::FunctionObject>();
        }

        reaction->call(promise, result, 1);
    } else {
        ScopedFunctionObject reaction(scope);
        if (ro->d()->type == Heap::PromiseReaction::Identity) {
            reaction = capability->d()->resolve.as<QV4::FunctionObject>();
        } else {
            reaction = capability->d()->reject.as<QV4::FunctionObject>();
        }

        reaction->call(promise, resolution, 1);
    }
}
}  // namespace QV4::Promise

//  from ../qtdeclarative/src/qml/jsruntime/qv4promiseobject.cpp, line 91, as _ZN3QV47Promise15ReactionHandler11addReactionEPNS_15ExecutionEngineEPKNS_5ValueES6_
namespace QV4::Promise {
using namespace QV4;
inline void ReactionHandler::addReaction(ExecutionEngine *e, const Value *reaction, const Value *value)
{
    QCoreApplication::postEvent(this, new ReactionEvent(e, reaction, value));
}
}  // namespace QV4::Promise

//  from ../qtdeclarative/src/qml/jsruntime/qv4promiseobject.cpp, line 96, as _ZN3QV47Promise15ReactionHandler18addResolveThenableEPNS_15ExecutionEngineEPKNS_13PromiseObjectEPKNS_6ObjectEPKNS_14FunctionObjectE
namespace QV4::Promise {
using namespace QV4;
inline void ReactionHandler::addResolveThenable(ExecutionEngine *e, const PromiseObject *promise, const Object *thenable, const FunctionObject *then)
{
    QCoreApplication::postEvent(this, new ResolveThenableEvent(e, promise, thenable, then));
}
}  // namespace QV4::Promise
//  -----------------------------------------------------------------------

//  A QV4::Promise::ReactionHandler that Python can take functions over in. Every QV4::Promise::ReactionHandler
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQV4_Promise_ReactionHandlerCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQV4_Promise_ReactionHandlerCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQV4_Promise_ReactionHandlerCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQV4_Promise_ReactionHandlerCall3)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQV4_Promise_ReactionHandlerCall4)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQV4_Promise_ReactionHandlerCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQV4_Promise_ReactionHandlerCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQV4_Promise_ReactionHandler : public QV4::Promise::ReactionHandler {
public:
  using QV4::Promise::ReactionHandler::ReactionHandler;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
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
  //  void QV4::Promise::ReactionHandler::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQV4_Promise_ReactionHandlerCall0 call = reinterpret_cast<CuteQV4_Promise_ReactionHandlerCall0>(taken[0]);
      call(this, event, &handled);
      if (handled) return;
    }
    QV4::Promise::ReactionHandler::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQV4_Promise_ReactionHandlerCall1 call = reinterpret_cast<CuteQV4_Promise_ReactionHandlerCall1>(taken[1]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQV4_Promise_ReactionHandlerCall2 call = reinterpret_cast<CuteQV4_Promise_ReactionHandlerCall2>(taken[2]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQV4_Promise_ReactionHandlerCall3 call = reinterpret_cast<CuteQV4_Promise_ReactionHandlerCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQV4_Promise_ReactionHandlerCall4 call = reinterpret_cast<CuteQV4_Promise_ReactionHandlerCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteQV4_Promise_ReactionHandlerCall5 call = reinterpret_cast<CuteQV4_Promise_ReactionHandlerCall5>(taken[5]);
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
      CuteQV4_Promise_ReactionHandlerCall6 call = reinterpret_cast<CuteQV4_Promise_ReactionHandlerCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QV4::Promise::ReactionHandler::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK3QV47Promise15ReactionHandler10metaObjectEv(
    const QV4::Promise::ReactionHandler *self) {
  return self->metaObject();
}

//  void *QV4::Promise::ReactionHandler::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN3QV47Promise15ReactionHandler11qt_metacastEPKc(
    QV4::Promise::ReactionHandler *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QV4::Promise::ReactionHandler::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN3QV47Promise15ReactionHandler11qt_metacallEN11QMetaObject4CallEiPPv(
    QV4::Promise::ReactionHandler *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QV4::Promise::ReactionHandler::~ReactionHandler()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV47Promise15ReactionHandlerD1Ev(
    QV4::Promise::ReactionHandler *self) {
  delete self;
}

//  void QV4::Promise::ReactionHandler::addReaction(ExecutionEngine *e, const
//      Value *reaction, const Value *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV47Promise15ReactionHandler11addReactionEPNS_15ExecutionEngineEPKNS_5ValueES6_(
    QV4::Promise::ReactionHandler *self,
    QV4::ExecutionEngine *e,
    const QV4::Value *reaction,
    const QV4::Value *value) {
  self->addReaction(e, reaction, value);
}

//  void QV4::Promise::ReactionHandler::addResolveThenable(ExecutionEngine
//      *e, const PromiseObject *promise, const Object *thenable, const
//      FunctionObject *then)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV47Promise15ReactionHandler18addResolveThenableEPNS_15ExecutionEngineEPKNS_13PromiseObjectEPKNS_6ObjectEPKNS_14FunctionObjectE(
    QV4::Promise::ReactionHandler *self,
    QV4::ExecutionEngine *e,
    const QV4::PromiseObject *promise,
    const QV4::Object *thenable,
    const QV4::FunctionObject *then) {
  self->addResolveThenable(e, promise, thenable, then);
}

//  void QV4::Promise::ReactionHandler::customEvent(QEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV47Promise15ReactionHandler11customEventEP6QEvent(
    QV4::Promise::ReactionHandler *self,
    QEvent *event) {
  self->customEvent(event);
}

//  a Python function taken by a CuteQV4_Promise_ReactionHandler, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QV4_Promise_ReactionHandler(
    QV4::Promise::ReactionHandler *self,
    const char *key,
    void *call) {
  return static_cast<CuteQV4_Promise_ReactionHandler *>(self)->take(key, call);
}
