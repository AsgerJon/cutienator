//  Written by hand on 2026-11-25 from
//  QtStateMachine/6.12.0/QtStateMachine/private/qstatemachine_p.h,
//  Qt 6.12.0, as the Qt of macOS and of Windows install it, and that
//  of Linux alike. Kept as it is when the generator runs again.
//  Qt's library offers nothing of this class by name: only what its
//  header writes out is called.
//  Not written: 'qHash', a helper of Qt's own.
#include <QtStateMachine/qstatemachineglobal.h>
#include <QtStateMachine/6.12.0/QtStateMachine/private/qstatemachineglobal_p.h>
#if QT_CONFIG(statemachine) && !defined(QT_NO_PROPERTIES)
#include <QtStateMachine/qstatemachine.h>
#include <QtStateMachine/6.12.0/QtStateMachine/private/qstatemachine_p.h>
#include <QtCore/qbytearray.h>

//  QStateMachinePrivate::RestorableId::RestorableId(QObject *o, QByteArray
//      p)
extern "C" Q_DECL_EXPORT
QStateMachinePrivate::RestorableId *ritual_ZN20QStateMachinePrivate12RestorableIdC1EP7QObject10QByteArray(
    QObject *o,
    const QByteArray *p) {
  return new QStateMachinePrivate::RestorableId(o, *p);
}

//  QObject *QStateMachinePrivate::RestorableId::object() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK20QStateMachinePrivate12RestorableId6objectEv(
    const QStateMachinePrivate::RestorableId *self) {
  return self->object();
}

//  QByteArray QStateMachinePrivate::RestorableId::propertyName() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK20QStateMachinePrivate12RestorableId12propertyNameEv(
    const QStateMachinePrivate::RestorableId *self) {
  return new QByteArray(self->propertyName());
}

//  bool operator==(const QStateMachinePrivate::RestorableId &lhs, const
//      QStateMachinePrivate::RestorableId &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRKN20QStateMachinePrivate12RestorableIdES2_(
    const QStateMachinePrivate::RestorableId *lhs,
    const QStateMachinePrivate::RestorableId *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QStateMachinePrivate::RestorableId &lhs, const
//      QStateMachinePrivate::RestorableId &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRKN20QStateMachinePrivate12RestorableIdES2_(
    const QStateMachinePrivate::RestorableId *lhs,
    const QStateMachinePrivate::RestorableId *rhs) {
  return operator!=(*lhs, *rhs);
}

//  QStateMachinePrivate::RestorableId::~RestorableId()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QStateMachinePrivate12RestorableIdD1Ev(
    QStateMachinePrivate::RestorableId *self) {
  delete self;
}

#endif  // QT_CONFIG(statemachine) && !defined(QT_NO_PROPERTIES)
