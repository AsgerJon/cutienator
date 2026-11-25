//  Written by hand on 2026-11-25 from
//  QtStateMachine/6.12.0/QtStateMachine/private/qsignaleventgenerator_p.h,
//  Qt 6.12.0, as the Qt of macOS and of Windows install it, and that
//  of Linux alike. Kept as it is when the generator runs again.
//  Qt's library offers nothing of this class by name: only its
//  virtual functions are called, through the object, and what its
//  header writes out.
//  Not written: the constructor, 'tr' and the slot 'execute'.
#include <QtStateMachine/qstatemachineglobal.h>
#include <QtStateMachine/6.12.0/QtStateMachine/private/qstatemachineglobal_p.h>
#if QT_CONFIG(statemachine)
#include <QtStateMachine/6.12.0/QtStateMachine/private/qsignaleventgenerator_p.h>

//  const QMetaObject *QSignalEventGenerator::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21QSignalEventGenerator10metaObjectEv(
    const QSignalEventGenerator *self) {
  return self->metaObject();
}

#endif  // QT_CONFIG(statemachine)
