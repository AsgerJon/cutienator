//  Written by hand on 2026-11-25 from
//  QtStateMachine/6.12.0/QtStateMachine/private/qhistorystate_p.h,
//  Qt 6.12.0, as the Qt of macOS and of Windows install it, and that
//  of Linux alike. Kept as it is when the generator runs again.
//  Qt's library offers nothing of this class by name: only what its
//  header writes out is called.
//  Not written: the constructor, which Qt's library offers not.
#include <QtStateMachine/qstatemachineglobal.h>
#include <QtStateMachine/6.12.0/QtStateMachine/private/qstatemachineglobal_p.h>
#if QT_CONFIG(statemachine)
#include <QtStateMachine/qhistorystate.h>
#include <QtStateMachine/6.12.0/QtStateMachine/private/qhistorystate_p.h>

//  QHistoryStatePrivate *QHistoryStatePrivate::get(QHistoryState *q)
extern "C" Q_DECL_EXPORT
QHistoryStatePrivate *ritual_ZN20QHistoryStatePrivate3getEP13QHistoryState(
    QHistoryState *q) {
  return QHistoryStatePrivate::get(q);
}

//  void QHistoryStatePrivate::setDefaultTransition(QAbstractTransition
//      *transition)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QHistoryStatePrivate20setDefaultTransitionEP19QAbstractTransition(
    QHistoryStatePrivate *self,
    QAbstractTransition *transition) {
  self->setDefaultTransition(transition);
}

//  void QHistoryStatePrivate::historyTypeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QHistoryStatePrivate18historyTypeChangedEv(
    QHistoryStatePrivate *self) {
  self->historyTypeChanged();
}

//  QHistoryState *QHistoryStatePrivate::q_func()
extern "C" Q_DECL_EXPORT
QHistoryState *ritual_ZN20QHistoryStatePrivate6q_funcEv(
    QHistoryStatePrivate *self) {
  return self->q_func();
}

//  const QHistoryState *QHistoryStatePrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QHistoryState *ritual_ZNK20QHistoryStatePrivate6q_funcEv(
    const QHistoryStatePrivate *self) {
  return self->q_func();
}

#endif  // QT_CONFIG(statemachine)
