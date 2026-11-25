//  Written by hand on 2026-11-25 from
//  QtStateMachine/6.12.0/QtStateMachine/private/qstatemachine_p.h,
//  Qt 6.12.0, as the Qt of macOS and of Windows install it, and that
//  of Linux alike. Kept as it is when the generator runs again.
//  Qt's library offers nothing of this class by name: only what its
//  header writes out is called.
//  Not written: 'swap', which changes the object handed to it.
#include <QtStateMachine/qstatemachineglobal.h>
#include <QtStateMachine/6.12.0/QtStateMachine/private/qstatemachineglobal_p.h>
#if QT_CONFIG(statemachine) && QT_CONFIG(animation)
#include <QtStateMachine/qstatemachine.h>
#include <QtStateMachine/6.12.0/QtStateMachine/private/qstatemachine_p.h>

//  QStateMachinePrivate::InitializeAnimationResult::~InitializeAnimationResu
//      lt()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QStateMachinePrivate25InitializeAnimationResultD1Ev(
    QStateMachinePrivate::InitializeAnimationResult *self) {
  delete self;
}

#endif  // QT_CONFIG(statemachine) && QT_CONFIG(animation)
