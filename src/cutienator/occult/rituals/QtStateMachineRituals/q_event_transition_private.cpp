//  Written by hand on 2026-11-25 from
//  QtStateMachine/6.12.0/QtStateMachine/private/qeventtransition_p.h,
//  Qt 6.12.0, as the Qt of macOS and of Windows install it, and that
//  of Linux alike. Kept as it is when the generator runs again.
#include <QtStateMachine/qstatemachineglobal.h>
#include <QtStateMachine/6.12.0/QtStateMachine/private/qstatemachineglobal_p.h>
#if QT_CONFIG(qeventtransition)
#include <QtStateMachine/qeventtransition.h>
#include <QtStateMachine/6.12.0/QtStateMachine/private/qeventtransition_p.h>
#include <cstring>

//  A QEventTransitionPrivate that Python can take functions over in. Every
//  QEventTransitionPrivate Python makes is one. Each function below asks the
//  Python function handed over for it, and runs Qt's own without
//  one.
typedef void (*CuteQEventTransitionPrivateCall0)(const void *, QEvent *, int *);
class CuteQEventTransitionPrivate : public QEventTransitionPrivate {
public:
  using QEventTransitionPrivate::QEventTransitionPrivate;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN26QAbstractTransitionPrivate16callOnTransitionEP6QEvent")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  void QAbstractTransitionPrivate::callOnTransition(QEvent *e)
  void callOnTransition(QEvent *e) override {
    if (taken[0]) {
      int handled = 0;
      CuteQEventTransitionPrivateCall0 call = reinterpret_cast<CuteQEventTransitionPrivateCall0>(taken[0]);
      call(this, e, &handled);
      if (handled) return;
    }
    QAbstractTransitionPrivate::callOnTransition(e);
  }
};

//  QEventTransitionPrivate::QEventTransitionPrivate()
extern "C" Q_DECL_EXPORT
QEventTransitionPrivate *ritual_ZN23QEventTransitionPrivateC1Ev() {
  return new CuteQEventTransitionPrivate();
}

//  QEventTransitionPrivate::~QEventTransitionPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QEventTransitionPrivateD1Ev(QEventTransitionPrivate *self) {
  delete self;
}

//  QEventTransitionPrivate *QEventTransitionPrivate::get(QEventTransition
//      *q)
extern "C" Q_DECL_EXPORT
QEventTransitionPrivate *ritual_ZN23QEventTransitionPrivate3getEP16QEventTransition(
    QEventTransition *q) {
  return QEventTransitionPrivate::get(q);
}

//  void QEventTransitionPrivate::unregister()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QEventTransitionPrivate10unregisterEv(
    QEventTransitionPrivate *self) {
  self->unregister();
}

//  void QEventTransitionPrivate::maybeRegister()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QEventTransitionPrivate13maybeRegisterEv(
    QEventTransitionPrivate *self) {
  self->maybeRegister();
}

//  void QEventTransitionPrivate::setEventSource(QObject *eventSource)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QEventTransitionPrivate14setEventSourceEP7QObject(
    QEventTransitionPrivate *self,
    QObject *eventSource) {
  self->setEventSource(eventSource);
}

//  void QEventTransitionPrivate::setEventType(QEvent::Type eventType)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QEventTransitionPrivate12setEventTypeEN6QEvent4TypeE(
    QEventTransitionPrivate *self,
    QEvent::Type eventType) {
  self->setEventType(eventType);
}

//  QEventTransition *QEventTransitionPrivate::q_func()
extern "C" Q_DECL_EXPORT
QEventTransition *ritual_ZN23QEventTransitionPrivate6q_funcEv(
    QEventTransitionPrivate *self) {
  return self->q_func();
}

//  const QEventTransition *QEventTransitionPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QEventTransition *ritual_ZNK23QEventTransitionPrivate6q_funcEv(
    const QEventTransitionPrivate *self) {
  return self->q_func();
}

//  a Python function taken by a CuteQEventTransitionPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QEventTransitionPrivate(
    QEventTransitionPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQEventTransitionPrivate *>(self)->take(key, call);
}

#endif  // QT_CONFIG(qeventtransition)
