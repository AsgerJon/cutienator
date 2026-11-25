//  Written by hand on 2026-11-25 from
//  QtStateMachine/6.12.0/QtStateMachine/private/qfinalstate_p.h,
//  Qt 6.12.0, as the Qt of macOS and of Windows install it, and that
//  of Linux alike. Kept as it is when the generator runs again.
#include <QtStateMachine/qstatemachineglobal.h>
#include <QtStateMachine/6.12.0/QtStateMachine/private/qstatemachineglobal_p.h>
#if QT_CONFIG(statemachine)
#include <QtStateMachine/qfinalstate.h>
#include <QtStateMachine/6.12.0/QtStateMachine/private/qfinalstate_p.h>

//  QFinalStatePrivate::QFinalStatePrivate()
extern "C" Q_DECL_EXPORT
QFinalStatePrivate *ritual_ZN18QFinalStatePrivateC1Ev() {
  return new QFinalStatePrivate();
}

//  QFinalStatePrivate::~QFinalStatePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFinalStatePrivateD1Ev(QFinalStatePrivate *self) {
  delete self;
}

//  QFinalState *QFinalStatePrivate::q_func()
extern "C" Q_DECL_EXPORT
QFinalState *ritual_ZN18QFinalStatePrivate6q_funcEv(
    QFinalStatePrivate *self) {
  return self->q_func();
}

//  const QFinalState *QFinalStatePrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QFinalState *ritual_ZNK18QFinalStatePrivate6q_funcEv(
    const QFinalStatePrivate *self) {
  return self->q_func();
}

#endif  // QT_CONFIG(statemachine)
