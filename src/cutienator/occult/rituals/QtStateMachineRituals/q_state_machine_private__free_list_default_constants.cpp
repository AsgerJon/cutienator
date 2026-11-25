//  Written by hand on 2026-11-25 from
//  QtStateMachine/6.12.0/QtStateMachine/private/qstatemachine_p.h,
//  Qt 6.12.0, as the Qt of macOS and of Windows install it, and that
//  of Linux alike. Kept as it is when the generator runs again.
//  Qt's library offers nothing of this class by name: only what its
//  header writes out is called.
//  It holds an enum and a table of numbers, and nothing to call.
#include <QtStateMachine/qstatemachineglobal.h>
#include <QtStateMachine/6.12.0/QtStateMachine/private/qstatemachineglobal_p.h>
#if QT_CONFIG(statemachine)
#include <QtStateMachine/qstatemachine.h>
#include <QtStateMachine/6.12.0/QtStateMachine/private/qstatemachine_p.h>

//  QStateMachinePrivate::FreeListDefaultConstants::~FreeListDefaultConstants
//      ()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QStateMachinePrivate24FreeListDefaultConstantsD1Ev(
    QStateMachinePrivate::FreeListDefaultConstants *self) {
  delete self;
}

#endif  // QT_CONFIG(statemachine)
