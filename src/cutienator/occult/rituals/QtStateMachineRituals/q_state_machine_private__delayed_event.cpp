//  Written by hand on 2026-11-25 from
//  QtStateMachine/6.12.0/QtStateMachine/private/qstatemachine_p.h,
//  Qt 6.12.0, as the Qt of macOS and of Windows install it, and that
//  of Linux alike. Kept as it is when the generator runs again.
//  Qt's library offers nothing of this class by name: only what its
//  header writes out is called.
#include <QtStateMachine/qstatemachineglobal.h>
#include <QtStateMachine/6.12.0/QtStateMachine/private/qstatemachineglobal_p.h>
#if QT_CONFIG(statemachine)
#include <QtStateMachine/qstatemachine.h>
#include <QtStateMachine/6.12.0/QtStateMachine/private/qstatemachine_p.h>

//  QStateMachinePrivate::DelayedEvent::DelayedEvent(QEvent *e, int tid)
extern "C" Q_DECL_EXPORT
QStateMachinePrivate::DelayedEvent *ritual_ZN20QStateMachinePrivate12DelayedEventC1EP6QEventi(
    QEvent *e,
    int tid) {
  return new QStateMachinePrivate::DelayedEvent(e, tid);
}

//  QStateMachinePrivate::DelayedEvent::DelayedEvent()
extern "C" Q_DECL_EXPORT
QStateMachinePrivate::DelayedEvent *ritual_ZN20QStateMachinePrivate12DelayedEventC1Ev() {
  return new QStateMachinePrivate::DelayedEvent();
}

//  QStateMachinePrivate::DelayedEvent::~DelayedEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QStateMachinePrivate12DelayedEventD1Ev(
    QStateMachinePrivate::DelayedEvent *self) {
  delete self;
}

#endif  // QT_CONFIG(statemachine)
