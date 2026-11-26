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
#include <QtCore/QList>

//  const QMetaObject *QScxmlStateMachineInfo::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK22QScxmlStateMachineInfo10metaObjectEv(
    const QScxmlStateMachineInfo *self) {
  return self->metaObject();
}

//  void *QScxmlStateMachineInfo::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN22QScxmlStateMachineInfo11qt_metacastEPKc(
    QScxmlStateMachineInfo *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QScxmlStateMachineInfo::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN22QScxmlStateMachineInfo11qt_metacallEN11QMetaObject4CallEiPPv(
    QScxmlStateMachineInfo *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
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

//  QList<StateId> QScxmlStateMachineInfo::allStates() const
extern "C" Q_DECL_EXPORT
QList<QScxmlStateMachineInfo::StateId> *ritual_ZNK22QScxmlStateMachineInfo9allStatesEv(
    const QScxmlStateMachineInfo *self) {
  return new QList<QScxmlStateMachineInfo::StateId>(self->allStates());
}

//  QList<TransitionId> QScxmlStateMachineInfo::allTransitions() const
extern "C" Q_DECL_EXPORT
QList<QScxmlStateMachineInfo::TransitionId> *ritual_ZNK22QScxmlStateMachineInfo14allTransitionsEv(
    const QScxmlStateMachineInfo *self) {
  return new QList<QScxmlStateMachineInfo::TransitionId>(
      self->allTransitions());
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

//  QList<StateId> QScxmlStateMachineInfo::stateChildren(StateId stateId)
//      const
extern "C" Q_DECL_EXPORT
QList<QScxmlStateMachineInfo::StateId> *ritual_ZNK22QScxmlStateMachineInfo13stateChildrenEi(
    const QScxmlStateMachineInfo *self,
    QScxmlStateMachineInfo::StateId stateId) {
  return new QList<QScxmlStateMachineInfo::StateId>(
      self->stateChildren(
          stateId));
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

//  QList<StateId> QScxmlStateMachineInfo::transitionTargets(TransitionId
//      transitionId) const
extern "C" Q_DECL_EXPORT
QList<QScxmlStateMachineInfo::StateId> *ritual_ZNK22QScxmlStateMachineInfo17transitionTargetsEi(
    const QScxmlStateMachineInfo *self,
    QScxmlStateMachineInfo::TransitionId transitionId) {
  return new QList<QScxmlStateMachineInfo::StateId>(
      self->transitionTargets(
          transitionId));
}

//  QList<QString> QScxmlStateMachineInfo::transitionEvents(TransitionId
//      transitionId) const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK22QScxmlStateMachineInfo16transitionEventsEi(
    const QScxmlStateMachineInfo *self,
    QScxmlStateMachineInfo::TransitionId transitionId) {
  return new QList<QString>(self->transitionEvents(transitionId));
}

//  QList<StateId> QScxmlStateMachineInfo::configuration() const
extern "C" Q_DECL_EXPORT
QList<QScxmlStateMachineInfo::StateId> *ritual_ZNK22QScxmlStateMachineInfo13configurationEv(
    const QScxmlStateMachineInfo *self) {
  return new QList<QScxmlStateMachineInfo::StateId>(self->configuration());
}

//  void QScxmlStateMachineInfo::statesEntered(const
//      QList<QScxmlStateMachineInfo::StateId> &states)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QScxmlStateMachineInfo13statesEnteredERK5QListIiE(
    QScxmlStateMachineInfo *self,
    const QList<QScxmlStateMachineInfo::StateId> *states) {
  self->statesEntered(*states);
}

//  void QScxmlStateMachineInfo::statesExited(const
//      QList<QScxmlStateMachineInfo::StateId> &states)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QScxmlStateMachineInfo12statesExitedERK5QListIiE(
    QScxmlStateMachineInfo *self,
    const QList<QScxmlStateMachineInfo::StateId> *states) {
  self->statesExited(*states);
}

//  void QScxmlStateMachineInfo::transitionsTriggered(const
//      QList<QScxmlStateMachineInfo::TransitionId> &transitions)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QScxmlStateMachineInfo20transitionsTriggeredERK5QListIiE(
    QScxmlStateMachineInfo *self,
    const QList<QScxmlStateMachineInfo::TransitionId> *transitions) {
  self->transitionsTriggered(*transitions);
}

//  QScxmlStateMachineInfoPrivate *QScxmlStateMachineInfo::d_func()
extern "C" Q_DECL_EXPORT
QScxmlStateMachineInfoPrivate *ritual_ZN22QScxmlStateMachineInfo6d_funcEv(
    QScxmlStateMachineInfo *self) {
  return self->d_func();
}

//  const QScxmlStateMachineInfoPrivate *QScxmlStateMachineInfo::d_func()
//      const
extern "C" Q_DECL_EXPORT
const QScxmlStateMachineInfoPrivate *ritual_ZNK22QScxmlStateMachineInfo6d_funcEv(
    const QScxmlStateMachineInfo *self) {
  return self->d_func();
}

//  a QList<QScxmlStateMachineInfo::StateId> a ritual of
//      QScxmlStateMachineInfo gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QScxmlStateMachineInfo__QList_QScxmlStateMachineInfo_StateId(
    QList<QScxmlStateMachineInfo::StateId> *self) {
  delete self;
}

//  a QList<QScxmlStateMachineInfo::TransitionId> a ritual of
//      QScxmlStateMachineInfo gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QScxmlStateMachineInfo__QList_QScxmlStateMachineInfo_TransitionId(
    QList<QScxmlStateMachineInfo::TransitionId> *self) {
  delete self;
}
