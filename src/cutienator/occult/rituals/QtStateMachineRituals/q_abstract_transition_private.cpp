//  Written by hand on 2026-11-25 from
//  QtStateMachine/6.12.0/QtStateMachine/private/qabstracttransition_p.h,
//  Qt 6.12.0, as the Qt of macOS and of Windows install it, and that
//  of Linux alike. Kept as it is when the generator runs again.
#include <QtStateMachine/qstatemachineglobal.h>
#include <QtStateMachine/6.12.0/QtStateMachine/private/qstatemachineglobal_p.h>
#if QT_CONFIG(statemachine)
#include <QtStateMachine/qabstracttransition.h>
#include <QtStateMachine/6.12.0/QtStateMachine/private/qabstracttransition_p.h>
#include <cstring>

//  A QAbstractTransitionPrivate that Python can take functions over in. Every
//  QAbstractTransitionPrivate Python makes is one. Each function below asks the
//  Python function handed over for it, and runs Qt's own without
//  one.
typedef void (*CuteQAbstractTransitionPrivateCall0)(const void *, QEvent *, int *);
class CuteQAbstractTransitionPrivate : public QAbstractTransitionPrivate {
public:
  using QAbstractTransitionPrivate::QAbstractTransitionPrivate;
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
      CuteQAbstractTransitionPrivateCall0 call = reinterpret_cast<CuteQAbstractTransitionPrivateCall0>(taken[0]);
      call(this, e, &handled);
      if (handled) return;
    }
    QAbstractTransitionPrivate::callOnTransition(e);
  }
};

//  QAbstractTransitionPrivate::QAbstractTransitionPrivate()
extern "C" Q_DECL_EXPORT
QAbstractTransitionPrivate *ritual_ZN26QAbstractTransitionPrivateC1Ev() {
  return new CuteQAbstractTransitionPrivate();
}

//  QAbstractTransitionPrivate
//      *QAbstractTransitionPrivate::get(QAbstractTransition *q)
extern "C" Q_DECL_EXPORT
QAbstractTransitionPrivate *ritual_ZN26QAbstractTransitionPrivate3getEP19QAbstractTransition(
    QAbstractTransition *q) {
  return QAbstractTransitionPrivate::get(q);
}

//  bool QAbstractTransitionPrivate::callEventTest(QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_ZN26QAbstractTransitionPrivate13callEventTestEP6QEvent(
    QAbstractTransitionPrivate *self,
    QEvent *e) {
  return self->callEventTest(e);
}

//  void QAbstractTransitionPrivate::callOnTransition(QEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QAbstractTransitionPrivate16callOnTransitionEP6QEvent(
    QAbstractTransitionPrivate *self,
    QEvent *e) {
  self->callOnTransition(e);
}

//  QState *QAbstractTransitionPrivate::sourceState() const
extern "C" Q_DECL_EXPORT
QState *ritual_ZNK26QAbstractTransitionPrivate11sourceStateEv(
    const QAbstractTransitionPrivate *self) {
  return self->sourceState();
}

//  QStateMachine *QAbstractTransitionPrivate::machine() const
extern "C" Q_DECL_EXPORT
QStateMachine *ritual_ZNK26QAbstractTransitionPrivate7machineEv(
    const QAbstractTransitionPrivate *self) {
  return self->machine();
}

//  void QAbstractTransitionPrivate::emitTriggered()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QAbstractTransitionPrivate13emitTriggeredEv(
    QAbstractTransitionPrivate *self) {
  self->emitTriggered();
}

//  QAbstractTransition *QAbstractTransitionPrivate::q_func()
extern "C" Q_DECL_EXPORT
QAbstractTransition *ritual_ZN26QAbstractTransitionPrivate6q_funcEv(
    QAbstractTransitionPrivate *self) {
  return self->q_func();
}

//  const QAbstractTransition *QAbstractTransitionPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QAbstractTransition *ritual_ZNK26QAbstractTransitionPrivate6q_funcEv(
    const QAbstractTransitionPrivate *self) {
  return self->q_func();
}

//  a Python function taken by a CuteQAbstractTransitionPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAbstractTransitionPrivate(
    QAbstractTransitionPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAbstractTransitionPrivate *>(self)->take(key, call);
}

//  void QAbstractTransitionPrivate::callOnTransition(QEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN26QAbstractTransitionPrivate16callOnTransitionEP6QEvent(
    QAbstractTransitionPrivate *self,
    QEvent *e) {
  self->QAbstractTransitionPrivate::callOnTransition(e);
}

#endif  // QT_CONFIG(statemachine)
