//  Written by hand on 2026-11-25 from
//  QtStateMachine/6.12.0/QtStateMachine/private/qabstractstate_p.h,
//  Qt 6.12.0, as the Qt of macOS and of Windows install it, and that
//  of Linux alike. Kept as it is when the generator runs again.
//  Qt's library offers nothing of this class by name: only what its
//  header writes out is called.
//  Not written: the constructor, 'machine', 'callOnEntry',
//  'callOnExit', 'emitEntered' and 'emitExited', which Qt's
//  library offers not.
#include <QtStateMachine/qstatemachineglobal.h>
#include <QtStateMachine/6.12.0/QtStateMachine/private/qstatemachineglobal_p.h>
#if QT_CONFIG(statemachine)
#include <QtStateMachine/qabstractstate.h>
#include <QtStateMachine/6.12.0/QtStateMachine/private/qabstractstate_p.h>

//  QAbstractStatePrivate *QAbstractStatePrivate::get(QAbstractState *q)
extern "C" Q_DECL_EXPORT
QAbstractStatePrivate *ritual_ZN21QAbstractStatePrivate3getEP14QAbstractState(
    QAbstractState *q) {
  return QAbstractStatePrivate::get(q);
}

//  const QAbstractStatePrivate *QAbstractStatePrivate::get(const
//      QAbstractState *q)
extern "C" Q_DECL_EXPORT
const QAbstractStatePrivate *ritual_ZN21QAbstractStatePrivate3getEPK14QAbstractState(
    const QAbstractState *q) {
  return QAbstractStatePrivate::get(q);
}

//  void QAbstractStatePrivate::activeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QAbstractStatePrivate13activeChangedEv(
    QAbstractStatePrivate *self) {
  self->activeChanged();
}

//  QAbstractState *QAbstractStatePrivate::q_func()
extern "C" Q_DECL_EXPORT
QAbstractState *ritual_ZN21QAbstractStatePrivate6q_funcEv(
    QAbstractStatePrivate *self) {
  return self->q_func();
}

//  const QAbstractState *QAbstractStatePrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QAbstractState *ritual_ZNK21QAbstractStatePrivate6q_funcEv(
    const QAbstractStatePrivate *self) {
  return self->q_func();
}

#endif  // QT_CONFIG(statemachine)
