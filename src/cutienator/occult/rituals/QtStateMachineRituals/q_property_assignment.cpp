//  Written by hand on 2026-11-25 from
//  QtStateMachine/6.12.0/QtStateMachine/private/qstate_p.h,
//  Qt 6.12.0, as the Qt of macOS and of Windows install it, and that
//  of Linux alike. Kept as it is when the generator runs again.
//  Qt's library offers nothing of this class by name: only what its
//  header writes out is called.
#include <QtStateMachine/qstatemachineglobal.h>
#include <QtStateMachine/6.12.0/QtStateMachine/private/qstatemachineglobal_p.h>
#if QT_CONFIG(statemachine) && !defined(QT_NO_PROPERTIES)
#include <QtStateMachine/qstate.h>
#include <QtStateMachine/6.12.0/QtStateMachine/private/qstate_p.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qvariant.h>

//  QPropertyAssignment::QPropertyAssignment()
extern "C" Q_DECL_EXPORT
QPropertyAssignment *ritual_ZN19QPropertyAssignmentC1Ev() {
  return new QPropertyAssignment();
}

//  QPropertyAssignment::QPropertyAssignment(QObject *o, const QByteArray &n,
//      const QVariant &v, bool es)
extern "C" Q_DECL_EXPORT
QPropertyAssignment *ritual_ZN19QPropertyAssignmentC1EP7QObjectRK10QByteArrayRK8QVariantb(
    QObject *o,
    const QByteArray *n,
    const QVariant *v,
    bool es) {
  return new QPropertyAssignment(o, *n, *v, es);
}

//  bool QPropertyAssignment::objectDeleted() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QPropertyAssignment13objectDeletedEv(
    const QPropertyAssignment *self) {
  return self->objectDeleted();
}

//  void QPropertyAssignment::write() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK19QPropertyAssignment5writeEv(
    const QPropertyAssignment *self) {
  self->write();
}

//  bool QPropertyAssignment::hasTarget(QObject *o, const QByteArray &pn)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QPropertyAssignment9hasTargetEP7QObjectRK10QByteArray(
    const QPropertyAssignment *self,
    QObject *o,
    const QByteArray *pn) {
  return self->hasTarget(o, *pn);
}

//  QPropertyAssignment::~QPropertyAssignment()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QPropertyAssignmentD1Ev(QPropertyAssignment *self) {
  delete self;
}

#endif  // QT_CONFIG(statemachine) && !defined(QT_NO_PROPERTIES)
