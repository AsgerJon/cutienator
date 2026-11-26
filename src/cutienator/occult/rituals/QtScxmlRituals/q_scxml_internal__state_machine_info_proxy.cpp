//  Written by dev_tooling.RitualGenerator from the records of
//  QtScxml/6.12.0/QtScxml/private/qscxmlstatemachine_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtScxml/6.12.0/QtScxml/private/qscxmlglobals_p.h>
#include <QtScxml/QtScxml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtScxml/6.12.0/QtScxml/private/qscxmlstatemachine_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QScxmlInternal::StateMachineInfoProxy that Python can take functions over in. Every QScxmlInternal::StateMachineInfoProxy
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQScxmlInternal_StateMachineInfoProxyCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQScxmlInternal_StateMachineInfoProxyCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQScxmlInternal_StateMachineInfoProxyCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQScxmlInternal_StateMachineInfoProxyCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQScxmlInternal_StateMachineInfoProxyCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQScxmlInternal_StateMachineInfoProxyCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQScxmlInternal_StateMachineInfoProxyCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQScxmlInternal_StateMachineInfoProxy : public QScxmlInternal::StateMachineInfoProxy {
public:
  using QScxmlInternal::StateMachineInfoProxy::StateMachineInfoProxy;
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
      CuteQScxmlInternal_StateMachineInfoProxyCall0 call = reinterpret_cast<CuteQScxmlInternal_StateMachineInfoProxyCall0>(taken[0]);
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
      CuteQScxmlInternal_StateMachineInfoProxyCall1 call = reinterpret_cast<CuteQScxmlInternal_StateMachineInfoProxyCall1>(taken[1]);
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
      CuteQScxmlInternal_StateMachineInfoProxyCall2 call = reinterpret_cast<CuteQScxmlInternal_StateMachineInfoProxyCall2>(taken[2]);
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
      CuteQScxmlInternal_StateMachineInfoProxyCall3 call = reinterpret_cast<CuteQScxmlInternal_StateMachineInfoProxyCall3>(taken[3]);
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
      CuteQScxmlInternal_StateMachineInfoProxyCall4 call = reinterpret_cast<CuteQScxmlInternal_StateMachineInfoProxyCall4>(taken[4]);
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
      CuteQScxmlInternal_StateMachineInfoProxyCall5 call = reinterpret_cast<CuteQScxmlInternal_StateMachineInfoProxyCall5>(taken[5]);
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
      CuteQScxmlInternal_StateMachineInfoProxyCall6 call = reinterpret_cast<CuteQScxmlInternal_StateMachineInfoProxyCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QScxmlInternal::StateMachineInfoProxy::metaObject()
//      const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14QScxmlInternal21StateMachineInfoProxy10metaObjectEv(
    const QScxmlInternal::StateMachineInfoProxy *self) {
  return self->metaObject();
}

//  void *QScxmlInternal::StateMachineInfoProxy::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN14QScxmlInternal21StateMachineInfoProxy11qt_metacastEPKc(
    QScxmlInternal::StateMachineInfoProxy *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QScxmlInternal::StateMachineInfoProxy::qt_metacall(QMetaObject::Call
//      a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN14QScxmlInternal21StateMachineInfoProxy11qt_metacallEN11QMetaObject4CallEiPPv(
    QScxmlInternal::StateMachineInfoProxy *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  void QScxmlInternal::StateMachineInfoProxy::statesEntered(const
//      QList<QScxmlStateMachineInfo::StateId> &states)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QScxmlInternal21StateMachineInfoProxy13statesEnteredERK5QListIiE(
    QScxmlInternal::StateMachineInfoProxy *self,
    const QList<QScxmlStateMachineInfo::StateId> *states) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QScxmlInternal::StateMachineInfoProxy")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "statesEntered(const QList<QScxmlStateMachineInfo::StateId> &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "statesEntered(const QList<QScxmlStateMachineInfo::StateId> &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(states)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QScxmlInternal::StateMachineInfoProxy::statesExited(const
//      QList<QScxmlStateMachineInfo::StateId> &states)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QScxmlInternal21StateMachineInfoProxy12statesExitedERK5QListIiE(
    QScxmlInternal::StateMachineInfoProxy *self,
    const QList<QScxmlStateMachineInfo::StateId> *states) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QScxmlInternal::StateMachineInfoProxy")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "statesExited(const QList<QScxmlStateMachineInfo::StateId> &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "statesExited(const QList<QScxmlStateMachineInfo::StateId> &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(states)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QScxmlInternal::StateMachineInfoProxy::transitionsTriggered(const
//      QList<QScxmlStateMachineInfo::TransitionId> &transitions)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QScxmlInternal21StateMachineInfoProxy20transitionsTriggeredERK5QListIiE(
    QScxmlInternal::StateMachineInfoProxy *self,
    const QList<QScxmlStateMachineInfo::TransitionId> *transitions) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QScxmlInternal::StateMachineInfoProxy")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "transitionsTriggered(const QList<QScxmlStateMachineInfo::TransitionId> &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "transitionsTriggered(const QList<QScxmlStateMachineInfo::TransitionId> &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(transitions)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  a Python function taken by a CuteQScxmlInternal_StateMachineInfoProxy,
//      for the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QScxmlInternal_StateMachineInfoProxy(
    QScxmlInternal::StateMachineInfoProxy *self,
    const char *key,
    void *call) {
  return static_cast<CuteQScxmlInternal_StateMachineInfoProxy *>(self)->take(key, call);
}
