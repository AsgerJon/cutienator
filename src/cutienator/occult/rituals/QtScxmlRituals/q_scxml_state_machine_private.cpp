//  Written by hand on 2026-11-25 from
//  QtScxml/6.12.0/QtScxml/private/qscxmlstatemachine_p.h,
//  Qt 6.12.0, from Qt's source. Kept as it is when the generator runs
//  again.
//  Qt's StateTable is a typedef of the class, so its Array is written
//  QScxmlStateMachinePrivate::StateTable::Array. Not written: the
//  functions taking or giving a std::vector ('stateNames',
//  'historyStates', 'selectTransitions', 'getProperAncestors',
//  'getChildStates', 'allInFinalStates', 'someInFinalStates').
//  'invokedServicesActualCalculation' gives a QList, written as a new
//  list given as an address.
#include <QtScxml/6.12.0/QtScxml/private/qscxmlglobals_p.h>
#include <QtScxml/6.12.0/QtScxml/private/qscxmlstatemachine_p.h>
#include <QtScxml/qscxmlinvokableservice.h>
#include <QtCore/qstring.h>
#include <utility>

//  QScxmlStateMachine *QScxmlStateMachinePrivate::q_func()
extern "C" Q_DECL_EXPORT
QScxmlStateMachine *ritual_ZN25QScxmlStateMachinePrivate6q_funcEv(
    QScxmlStateMachinePrivate *self) {
  return self->q_func();
}

//  const QScxmlStateMachine *QScxmlStateMachinePrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QScxmlStateMachine *ritual_ZNK25QScxmlStateMachinePrivate6q_funcEv(
    const QScxmlStateMachinePrivate *self) {
  return self->q_func();
}

//  QScxmlStateMachinePrivate::QScxmlStateMachinePrivate(const QMetaObject
//      *qMetaObject)
extern "C" Q_DECL_EXPORT
QScxmlStateMachinePrivate *ritual_ZN25QScxmlStateMachinePrivateC1EPK11QMetaObject(
    const QMetaObject *qMetaObject) {
  return new QScxmlStateMachinePrivate(qMetaObject);
}

//  QScxmlStateMachinePrivate::~QScxmlStateMachinePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QScxmlStateMachinePrivateD1Ev(
    QScxmlStateMachinePrivate *self) {
  delete self;
}

//  QScxmlStateMachinePrivate
//      *QScxmlStateMachinePrivate::get(QScxmlStateMachine *t)
extern "C" Q_DECL_EXPORT
QScxmlStateMachinePrivate *ritual_ZN25QScxmlStateMachinePrivate3getEP18QScxmlStateMachine(
    QScxmlStateMachine *t) {
  return QScxmlStateMachinePrivate::get(t);
}

//  QString QScxmlStateMachinePrivate::generateSessionId(const QString
//      &prefix)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN25QScxmlStateMachinePrivate17generateSessionIdERK7QString(
    const QString *prefix) {
  return new QString(QScxmlStateMachinePrivate::generateSessionId(*prefix));
}

//  ParserData *QScxmlStateMachinePrivate::parserData()
extern "C" Q_DECL_EXPORT
QScxmlStateMachinePrivate::ParserData *ritual_ZN25QScxmlStateMachinePrivate10parserDataEv(
    QScxmlStateMachinePrivate *self) {
  return self->parserData();
}

//  void QScxmlStateMachinePrivate::setIsInvoked(bool invoked)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QScxmlStateMachinePrivate12setIsInvokedEb(
    QScxmlStateMachinePrivate *self,
    bool invoked) {
  self->setIsInvoked(invoked);
}

//  void QScxmlStateMachinePrivate::addService(int invokingState)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QScxmlStateMachinePrivate10addServiceEi(
    QScxmlStateMachinePrivate *self,
    int invokingState) {
  self->addService(invokingState);
}

//  void QScxmlStateMachinePrivate::removeService(int invokingState)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QScxmlStateMachinePrivate13removeServiceEi(
    QScxmlStateMachinePrivate *self,
    int invokingState) {
  self->removeService(invokingState);
}

//  QScxmlInvokableServiceFactory
//      *QScxmlStateMachinePrivate::serviceFactory(int id)
extern "C" Q_DECL_EXPORT
QScxmlInvokableServiceFactory *ritual_ZN25QScxmlStateMachinePrivate14serviceFactoryEi(
    QScxmlStateMachinePrivate *self,
    int id) {
  return self->serviceFactory(id);
}

//  bool QScxmlStateMachinePrivate::executeInitialSetup()
extern "C" Q_DECL_EXPORT
bool ritual_ZN25QScxmlStateMachinePrivate19executeInitialSetupEv(
    QScxmlStateMachinePrivate *self) {
  return self->executeInitialSetup();
}

//  void QScxmlStateMachinePrivate::routeEvent(QScxmlEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QScxmlStateMachinePrivate10routeEventEP11QScxmlEvent(
    QScxmlStateMachinePrivate *self,
    QScxmlEvent *event) {
  self->routeEvent(event);
}

//  void QScxmlStateMachinePrivate::postEvent(QScxmlEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QScxmlStateMachinePrivate9postEventEP11QScxmlEvent(
    QScxmlStateMachinePrivate *self,
    QScxmlEvent *event) {
  self->postEvent(event);
}

//  void QScxmlStateMachinePrivate::submitDelayedEvent(QScxmlEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QScxmlStateMachinePrivate18submitDelayedEventEP11QScxmlEvent(
    QScxmlStateMachinePrivate *self,
    QScxmlEvent *event) {
  self->submitDelayedEvent(event);
}

//  void QScxmlStateMachinePrivate::submitError(const QString &type, const
//      QString &msg, const QString &sendid)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QScxmlStateMachinePrivate11submitErrorERK7QStringS2_S2_(
    QScxmlStateMachinePrivate *self,
    const QString *type,
    const QString *msg,
    const QString *sendid) {
  self->submitError(*type, *msg, *sendid);
}

//  void QScxmlStateMachinePrivate::start()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QScxmlStateMachinePrivate5startEv(
    QScxmlStateMachinePrivate *self) {
  self->start();
}

//  void QScxmlStateMachinePrivate::pause()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QScxmlStateMachinePrivate5pauseEv(
    QScxmlStateMachinePrivate *self) {
  self->pause();
}

//  void QScxmlStateMachinePrivate::processEvents()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QScxmlStateMachinePrivate13processEventsEv(
    QScxmlStateMachinePrivate *self) {
  self->processEvents();
}

//  void QScxmlStateMachinePrivate::setEvent(QScxmlEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QScxmlStateMachinePrivate8setEventEP11QScxmlEvent(
    QScxmlStateMachinePrivate *self,
    QScxmlEvent *event) {
  self->setEvent(event);
}

//  void QScxmlStateMachinePrivate::resetEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QScxmlStateMachinePrivate10resetEventEv(
    QScxmlStateMachinePrivate *self) {
  self->resetEvent();
}

//  void QScxmlStateMachinePrivate::emitStateActive(int stateIndex, bool
//      active)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QScxmlStateMachinePrivate15emitStateActiveEib(
    QScxmlStateMachinePrivate *self,
    int stateIndex,
    bool active) {
  self->emitStateActive(stateIndex, active);
}

//  void QScxmlStateMachinePrivate::emitInvokedServicesChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QScxmlStateMachinePrivate26emitInvokedServicesChangedEv(
    QScxmlStateMachinePrivate *self) {
  self->emitInvokedServicesChanged();
}

//  void QScxmlStateMachinePrivate::attach(QScxmlStateMachineInfo *info)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QScxmlStateMachinePrivate6attachEP22QScxmlStateMachineInfo(
    QScxmlStateMachinePrivate *self,
    QScxmlStateMachineInfo *info) {
  self->attach(info);
}

//  const OrderedSet &QScxmlStateMachinePrivate::configuration() const
extern "C" Q_DECL_EXPORT
const QScxmlStateMachinePrivate::OrderedSet *ritual_ZNK25QScxmlStateMachinePrivate13configurationEv(
    const QScxmlStateMachinePrivate *self) {
  return &(self->configuration());
}

//  void QScxmlStateMachinePrivate::updateMetaCache()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QScxmlStateMachinePrivate15updateMetaCacheEv(
    QScxmlStateMachinePrivate *self) {
  self->updateMetaCache();
}

//  void QScxmlStateMachinePrivate::exitInterpreter()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QScxmlStateMachinePrivate15exitInterpreterEv(
    QScxmlStateMachinePrivate *self) {
  self->exitInterpreter();
}

//  void QScxmlStateMachinePrivate::returnDoneEvent(QScxmlExecutableContent::
//      ContainerId doneData)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QScxmlStateMachinePrivate15returnDoneEventEi(
    QScxmlStateMachinePrivate *self,
    QScxmlExecutableContent::ContainerId doneData) {
  self->returnDoneEvent(doneData);
}

//  bool QScxmlStateMachinePrivate::nameMatch(const StateTable::Array
//      &patterns, QScxmlEvent *event) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QScxmlStateMachinePrivate9nameMatchERKN23QScxmlExecutableContent10StateTable5ArrayEP11QScxmlEvent(
    const QScxmlStateMachinePrivate *self,
    const QScxmlStateMachinePrivate::StateTable::Array *patterns,
    QScxmlEvent *event) {
  return self->nameMatch(*patterns, event);
}

//  void QScxmlStateMachinePrivate::removeConflictingTransitions(OrderedSet
//      *enabledTransitions) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK25QScxmlStateMachinePrivate28removeConflictingTransitionsEPNS_10OrderedSetE(
    const QScxmlStateMachinePrivate *self,
    QScxmlStateMachinePrivate::OrderedSet *enabledTransitions) {
  self->removeConflictingTransitions(enabledTransitions);
}

//  void QScxmlStateMachinePrivate::microstep(const OrderedSet
//      &enabledTransitions)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QScxmlStateMachinePrivate9microstepERKNS_10OrderedSetE(
    QScxmlStateMachinePrivate *self,
    const QScxmlStateMachinePrivate::OrderedSet *enabledTransitions) {
  self->microstep(*enabledTransitions);
}

//  void QScxmlStateMachinePrivate::exitStates(const OrderedSet
//      &enabledTransitions)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QScxmlStateMachinePrivate10exitStatesERKNS_10OrderedSetE(
    QScxmlStateMachinePrivate *self,
    const QScxmlStateMachinePrivate::OrderedSet *enabledTransitions) {
  self->exitStates(*enabledTransitions);
}

//  void QScxmlStateMachinePrivate::computeExitSet(const OrderedSet
//      &enabledTransitions, OrderedSet &statesToExit) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK25QScxmlStateMachinePrivate14computeExitSetERKNS_10OrderedSetERS0_(
    const QScxmlStateMachinePrivate *self,
    const QScxmlStateMachinePrivate::OrderedSet *enabledTransitions,
    QScxmlStateMachinePrivate::OrderedSet *statesToExit) {
  self->computeExitSet(*enabledTransitions, *statesToExit);
}

//  void QScxmlStateMachinePrivate::executeTransitionContent(const OrderedSet
//      &enabledTransitions)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QScxmlStateMachinePrivate24executeTransitionContentERKNS_10OrderedSetE(
    QScxmlStateMachinePrivate *self,
    const QScxmlStateMachinePrivate::OrderedSet *enabledTransitions) {
  self->executeTransitionContent(*enabledTransitions);
}

//  void QScxmlStateMachinePrivate::enterStates(const OrderedSet
//      &enabledTransitions)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QScxmlStateMachinePrivate11enterStatesERKNS_10OrderedSetE(
    QScxmlStateMachinePrivate *self,
    const QScxmlStateMachinePrivate::OrderedSet *enabledTransitions) {
  self->enterStates(*enabledTransitions);
}

//  void QScxmlStateMachinePrivate::computeEntrySet(const OrderedSet
//      &enabledTransitions, OrderedSet *statesToEnter, OrderedSet
//      *statesForDefaultEntry, HistoryContent *defaultHistoryContent) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK25QScxmlStateMachinePrivate15computeEntrySetERKNS_10OrderedSetEPS0_S3_PNS_14HistoryContentE(
    const QScxmlStateMachinePrivate *self,
    const QScxmlStateMachinePrivate::OrderedSet *enabledTransitions,
    QScxmlStateMachinePrivate::OrderedSet *statesToEnter,
    QScxmlStateMachinePrivate::OrderedSet *statesForDefaultEntry,
    QScxmlStateMachinePrivate::HistoryContent *defaultHistoryContent) {
  self->computeEntrySet(
      *enabledTransitions,
      statesToEnter,
      statesForDefaultEntry,
      defaultHistoryContent);
}

//  void QScxmlStateMachinePrivate::addDescendantStatesToEnter(int
//      stateIndex, OrderedSet *statesToEnter, OrderedSet
//      *statesForDefaultEntry, HistoryContent *defaultHistoryContent) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK25QScxmlStateMachinePrivate26addDescendantStatesToEnterEiPNS_10OrderedSetES1_PNS_14HistoryContentE(
    const QScxmlStateMachinePrivate *self,
    int stateIndex,
    QScxmlStateMachinePrivate::OrderedSet *statesToEnter,
    QScxmlStateMachinePrivate::OrderedSet *statesForDefaultEntry,
    QScxmlStateMachinePrivate::HistoryContent *defaultHistoryContent) {
  self->addDescendantStatesToEnter(
      stateIndex,
      statesToEnter,
      statesForDefaultEntry,
      defaultHistoryContent);
}

//  void QScxmlStateMachinePrivate::addAncestorStatesToEnter(int stateIndex,
//      int ancestorIndex, OrderedSet *statesToEnter, OrderedSet
//      *statesForDefaultEntry, HistoryContent *defaultHistoryContent) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK25QScxmlStateMachinePrivate24addAncestorStatesToEnterEiiPNS_10OrderedSetES1_PNS_14HistoryContentE(
    const QScxmlStateMachinePrivate *self,
    int stateIndex,
    int ancestorIndex,
    QScxmlStateMachinePrivate::OrderedSet *statesToEnter,
    QScxmlStateMachinePrivate::OrderedSet *statesForDefaultEntry,
    QScxmlStateMachinePrivate::HistoryContent *defaultHistoryContent) {
  self->addAncestorStatesToEnter(
      stateIndex,
      ancestorIndex,
      statesToEnter,
      statesForDefaultEntry,
      defaultHistoryContent);
}

//  bool QScxmlStateMachinePrivate::hasDescendant(const OrderedSet
//      &statesToEnter, int childIdx) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QScxmlStateMachinePrivate13hasDescendantERKNS_10OrderedSetEi(
    const QScxmlStateMachinePrivate *self,
    const QScxmlStateMachinePrivate::OrderedSet *statesToEnter,
    int childIdx) {
  return self->hasDescendant(*statesToEnter, childIdx);
}

//  bool QScxmlStateMachinePrivate::allDescendants(const OrderedSet
//      &statesToEnter, int childdx) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QScxmlStateMachinePrivate14allDescendantsERKNS_10OrderedSetEi(
    const QScxmlStateMachinePrivate *self,
    const QScxmlStateMachinePrivate::OrderedSet *statesToEnter,
    int childdx) {
  return self->allDescendants(*statesToEnter, childdx);
}

//  bool QScxmlStateMachinePrivate::isDescendant(int state1, int state2)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QScxmlStateMachinePrivate12isDescendantEii(
    const QScxmlStateMachinePrivate *self,
    int state1,
    int state2) {
  return self->isDescendant(state1, state2);
}

//  bool QScxmlStateMachinePrivate::isInFinalState(int stateIndex) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QScxmlStateMachinePrivate14isInFinalStateEi(
    const QScxmlStateMachinePrivate *self,
    int stateIndex) {
  return self->isInFinalState(stateIndex);
}

//  int QScxmlStateMachinePrivate::getTransitionDomain(int transitionIndex)
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK25QScxmlStateMachinePrivate19getTransitionDomainEi(
    const QScxmlStateMachinePrivate *self,
    int transitionIndex) {
  return self->getTransitionDomain(transitionIndex);
}

//  int QScxmlStateMachinePrivate::findLCCA(OrderedSet &&states) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK25QScxmlStateMachinePrivate8findLCCAEONS_10OrderedSetE(
    const QScxmlStateMachinePrivate *self,
    QScxmlStateMachinePrivate::OrderedSet *states) {
  return self->findLCCA(std::move(*states));
}

//  void QScxmlStateMachinePrivate::getEffectiveTargetStates(OrderedSet
//      *targets, int transitionIndex) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK25QScxmlStateMachinePrivate24getEffectiveTargetStatesEPNS_10OrderedSetEi(
    const QScxmlStateMachinePrivate *self,
    QScxmlStateMachinePrivate::OrderedSet *targets,
    int transitionIndex) {
  self->getEffectiveTargetStates(targets, transitionIndex);
}

//  void QScxmlStateMachinePrivate::isInitializedChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QScxmlStateMachinePrivate20isInitializedChangedEv(
    QScxmlStateMachinePrivate *self) {
  self->isInitializedChanged();
}

//  void QScxmlStateMachinePrivate::initialValuesChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QScxmlStateMachinePrivate20initialValuesChangedEv(
    QScxmlStateMachinePrivate *self) {
  self->initialValuesChanged();
}

//  void QScxmlStateMachinePrivate::loaderChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QScxmlStateMachinePrivate13loaderChangedEv(
    QScxmlStateMachinePrivate *self) {
  self->loaderChanged();
}

//  void QScxmlStateMachinePrivate::setDataModel(QScxmlDataModel *loader)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QScxmlStateMachinePrivate12setDataModelEP15QScxmlDataModel(
    QScxmlStateMachinePrivate *self,
    QScxmlDataModel *loader) {
  self->setDataModel(loader);
}

//  void QScxmlStateMachinePrivate::setTableData(QScxmlTableData *tableData)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QScxmlStateMachinePrivate12setTableDataEP15QScxmlTableData(
    QScxmlStateMachinePrivate *self,
    QScxmlTableData *tableData) {
  self->setTableData(tableData);
}

//  bool QScxmlStateMachinePrivate::isRunnable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QScxmlStateMachinePrivate10isRunnableEv(
    const QScxmlStateMachinePrivate *self) {
  return self->isRunnable();
}

//  bool QScxmlStateMachinePrivate::isPaused() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QScxmlStateMachinePrivate8isPausedEv(
    const QScxmlStateMachinePrivate *self) {
  return self->isPaused();
}

//  bool QScxmlStateMachinePrivate::isFinished() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QScxmlStateMachinePrivate10isFinishedEv(
    const QScxmlStateMachinePrivate *self) {
  return self->isFinished();
}

//  QList<QScxmlInvokableService*>
//      QScxmlStateMachinePrivate::invokedServicesActualCalculation() const
extern "C" Q_DECL_EXPORT
QList<QScxmlInvokableService *> *ritual_ZNK25QScxmlStateMachinePrivate32invokedServicesActualCalculationEv(
    const QScxmlStateMachinePrivate *self) {
  return new QList<QScxmlInvokableService *>(
      self->invokedServicesActualCalculation());
}
