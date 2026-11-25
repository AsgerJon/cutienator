//  Written by hand on 2026-11-25 from
//  QtStateMachine/6.12.0/QtStateMachine/private/qsignaltransition_p.h,
//  Qt 6.12.0, as the Qt of macOS and of Windows install it, and that
//  of Linux alike. Kept as it is when the generator runs again.
//  Qt's library offers nothing of this class by name: only its
//  virtual functions are called, through the object, and what its
//  header writes out.
//  Not written: the constructor, 'unregister' and 'maybeRegister',
//  which Qt's library offers not.
#include <QtStateMachine/qstatemachineglobal.h>
#include <QtStateMachine/6.12.0/QtStateMachine/private/qstatemachineglobal_p.h>
#if QT_CONFIG(statemachine)
#include <QtStateMachine/qsignaltransition.h>
#include <QtStateMachine/6.12.0/QtStateMachine/private/qsignaltransition_p.h>
#include <QtCore/qbytearray.h>

//  QSignalTransitionPrivate *QSignalTransitionPrivate::get(QSignalTransition
//      *q)
extern "C" Q_DECL_EXPORT
QSignalTransitionPrivate *ritual_ZN24QSignalTransitionPrivate3getEP17QSignalTransition(
    QSignalTransition *q) {
  return QSignalTransitionPrivate::get(q);
}

//  void QSignalTransitionPrivate::callOnTransition(QEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QSignalTransitionPrivate16callOnTransitionEP6QEvent(
    QSignalTransitionPrivate *self,
    QEvent *e) {
  self->callOnTransition(e);
}

//  void QSignalTransitionPrivate::setSenderObject(const QObject *sender)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QSignalTransitionPrivate15setSenderObjectEPK7QObject(
    QSignalTransitionPrivate *self,
    const QObject *sender) {
  self->setSenderObject(sender);
}

//  void QSignalTransitionPrivate::setSignal(const QByteArray &signal)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QSignalTransitionPrivate9setSignalERK10QByteArray(
    QSignalTransitionPrivate *self,
    const QByteArray *signal) {
  self->setSignal(*signal);
}

//  QSignalTransition *QSignalTransitionPrivate::q_func()
extern "C" Q_DECL_EXPORT
QSignalTransition *ritual_ZN24QSignalTransitionPrivate6q_funcEv(
    QSignalTransitionPrivate *self) {
  return self->q_func();
}

//  const QSignalTransition *QSignalTransitionPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QSignalTransition *ritual_ZNK24QSignalTransitionPrivate6q_funcEv(
    const QSignalTransitionPrivate *self) {
  return self->q_func();
}

#endif  // QT_CONFIG(statemachine)
