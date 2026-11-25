//  Written by hand on 2026-11-25 from
//  QtStateMachine/6.12.0/QtStateMachine/private/qstate_p.h,
//  Qt 6.12.0, as the Qt of macOS and of Windows install it, and that
//  of Linux alike. Kept as it is when the generator runs again.
//  Not written: 'historyStates', which gives a
//  'QList<QHistoryState *>', a list QtStateMachine has no rituals for.
#include <QtStateMachine/qstatemachineglobal.h>
#include <QtStateMachine/6.12.0/QtStateMachine/private/qstatemachineglobal_p.h>
#if QT_CONFIG(statemachine)
#include <QtStateMachine/qstate.h>
#include <QtStateMachine/6.12.0/QtStateMachine/private/qstate_p.h>
#include <QtCore/qlist.h>

//  QStatePrivate::QStatePrivate()
extern "C" Q_DECL_EXPORT
QStatePrivate *ritual_ZN13QStatePrivateC1Ev() {
  return new QStatePrivate();
}

//  QStatePrivate::~QStatePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QStatePrivateD1Ev(QStatePrivate *self) {
  delete self;
}

//  QStatePrivate *QStatePrivate::get(QState *q)
extern "C" Q_DECL_EXPORT
QStatePrivate *ritual_ZN13QStatePrivate3getEP6QState(QState *q) {
  return QStatePrivate::get(q);
}

//  const QStatePrivate *QStatePrivate::get(const QState *q)
extern "C" Q_DECL_EXPORT
const QStatePrivate *ritual_ZN13QStatePrivate3getEPK6QState(
    const QState *q) {
  return QStatePrivate::get(q);
}

//  QList<QAbstractState *> QStatePrivate::childStates() const
extern "C" Q_DECL_EXPORT
QList<QAbstractState *> *ritual_ZNK13QStatePrivate11childStatesEv(
    const QStatePrivate *self) {
  return new QList<QAbstractState *>(self->childStates());
}

//  QList<QAbstractTransition *> QStatePrivate::transitions() const
extern "C" Q_DECL_EXPORT
QList<QAbstractTransition *> *ritual_ZNK13QStatePrivate11transitionsEv(
    const QStatePrivate *self) {
  return new QList<QAbstractTransition *>(self->transitions());
}

//  void QStatePrivate::emitFinished()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QStatePrivate12emitFinishedEv(QStatePrivate *self) {
  self->emitFinished();
}

//  void QStatePrivate::emitPropertiesAssigned()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QStatePrivate22emitPropertiesAssignedEv(
    QStatePrivate *self) {
  self->emitPropertiesAssigned();
}

//  void QStatePrivate::initialStateChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QStatePrivate19initialStateChangedEv(QStatePrivate *self) {
  self->initialStateChanged();
}

//  void QStatePrivate::errorStateChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QStatePrivate17errorStateChangedEv(QStatePrivate *self) {
  self->errorStateChanged();
}

//  void QStatePrivate::childModeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QStatePrivate16childModeChangedEv(QStatePrivate *self) {
  self->childModeChanged();
}

//  QState *QStatePrivate::q_func()
extern "C" Q_DECL_EXPORT
QState *ritual_ZN13QStatePrivate6q_funcEv(QStatePrivate *self) {
  return self->q_func();
}

//  const QState *QStatePrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QState *ritual_ZNK13QStatePrivate6q_funcEv(const QStatePrivate *self) {
  return self->q_func();
}

#endif  // QT_CONFIG(statemachine)
