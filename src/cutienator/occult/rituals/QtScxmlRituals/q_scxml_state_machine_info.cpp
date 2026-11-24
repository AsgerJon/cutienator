//  Written by dev_tooling.RitualGenerator from the records of
//  QtScxml/6.12.0/QtScxml/private/qscxmlstatemachineinfo_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtScxml/6.12.0/QtScxml/private/qscxmlglobals_p.h>
#include <QtScxml/QtScxml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtScxml/6.12.0/QtScxml/private/qscxmlstatemachineinfo_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>

//  const QMetaObject *QScxmlStateMachineInfo::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK22QScxmlStateMachineInfo10metaObjectEv(
    const QScxmlStateMachineInfo *self) {
  return self->metaObject();
}

//  QString QScxmlStateMachineInfo::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN22QScxmlStateMachineInfo2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QScxmlStateMachineInfo::tr(s, c, n));
}

//  QScxmlStateMachineInfo::QScxmlStateMachineInfo(QScxmlStateMachine
//      *stateMachine)
extern "C" Q_DECL_EXPORT
QScxmlStateMachineInfo *ritual_ZN22QScxmlStateMachineInfoC1EP18QScxmlStateMachine(
    QScxmlStateMachine *stateMachine) {
  return new QScxmlStateMachineInfo(stateMachine);
}

//  QScxmlStateMachine *QScxmlStateMachineInfo::stateMachine() const
extern "C" Q_DECL_EXPORT
QScxmlStateMachine *ritual_ZNK22QScxmlStateMachineInfo12stateMachineEv(
    const QScxmlStateMachineInfo *self) {
  return self->stateMachine();
}

//  QString QScxmlStateMachineInfo::stateName(int stateId) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK22QScxmlStateMachineInfo9stateNameEi(
    const QScxmlStateMachineInfo *self,
    int stateId) {
  return new QString(self->stateName(stateId));
}

//  StateId QScxmlStateMachineInfo::stateParent(StateId stateId) const
extern "C" Q_DECL_EXPORT
QScxmlStateMachineInfo::StateId ritual_ZNK22QScxmlStateMachineInfo11stateParentEi(
    const QScxmlStateMachineInfo *self,
    QScxmlStateMachineInfo::StateId stateId) {
  return self->stateParent(stateId);
}

//  StateType QScxmlStateMachineInfo::stateType(int stateId) const
extern "C" Q_DECL_EXPORT
QScxmlStateMachineInfo::StateType ritual_ZNK22QScxmlStateMachineInfo9stateTypeEi(
    const QScxmlStateMachineInfo *self,
    int stateId) {
  return self->stateType(stateId);
}

//  TransitionId QScxmlStateMachineInfo::initialTransition(StateId stateId)
//      const
extern "C" Q_DECL_EXPORT
QScxmlStateMachineInfo::TransitionId ritual_ZNK22QScxmlStateMachineInfo17initialTransitionEi(
    const QScxmlStateMachineInfo *self,
    QScxmlStateMachineInfo::StateId stateId) {
  return self->initialTransition(stateId);
}

//  TransitionType QScxmlStateMachineInfo::transitionType(TransitionId
//      transitionId) const
extern "C" Q_DECL_EXPORT
QScxmlStateMachineInfo::TransitionType ritual_ZNK22QScxmlStateMachineInfo14transitionTypeEi(
    const QScxmlStateMachineInfo *self,
    QScxmlStateMachineInfo::TransitionId transitionId) {
  return self->transitionType(transitionId);
}

//  StateId QScxmlStateMachineInfo::transitionSource(TransitionId
//      transitionId) const
extern "C" Q_DECL_EXPORT
QScxmlStateMachineInfo::StateId ritual_ZNK22QScxmlStateMachineInfo16transitionSourceEi(
    const QScxmlStateMachineInfo *self,
    QScxmlStateMachineInfo::TransitionId transitionId) {
  return self->transitionSource(transitionId);
}

//  QList<QString> QScxmlStateMachineInfo::transitionEvents(TransitionId
//      transitionId) const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK22QScxmlStateMachineInfo16transitionEventsEi(
    const QScxmlStateMachineInfo *self,
    QScxmlStateMachineInfo::TransitionId transitionId) {
  return new QList<QString>(self->transitionEvents(transitionId));
}
