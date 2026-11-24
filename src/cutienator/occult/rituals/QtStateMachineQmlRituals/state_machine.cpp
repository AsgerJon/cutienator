//  Written by dev_tooling.RitualGenerator from the records of
//  QtStateMachineQml/6.12.0/QtStateMachineQml/private/statemachine_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtStateMachineQml/6.12.0/QtStateMachineQml/private/qstatemachineqmlglobals_p.h>
#include <QtStateMachineQml/QtStateMachineQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtStateMachineQml/6.12.0/QtStateMachineQml/private/statemachine_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  const QMetaObject *StateMachine::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK12StateMachine10metaObjectEv(
    const StateMachine *self) {
  return self->metaObject();
}

//  QString StateMachine::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN12StateMachine2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(StateMachine::tr(s, c, n));
}

//  StateMachine::StateMachine(QObject *parent)
extern "C" Q_DECL_EXPORT
StateMachine *ritual_ZN12StateMachineC1EP7QObject(QObject *parent) {
  return new StateMachine(parent);
}

//  void StateMachine::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN12StateMachine10classBeginEv(StateMachine *self) {
  self->classBegin();
}

//  void StateMachine::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN12StateMachine17componentCompleteEv(StateMachine *self) {
  self->componentComplete();
}

//  bool StateMachine::isRunning() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12StateMachine9isRunningEv(const StateMachine *self) {
  return self->isRunning();
}

//  void StateMachine::setRunning(bool running)
extern "C" Q_DECL_EXPORT
void ritual_ZN12StateMachine10setRunningEb(
    StateMachine *self,
    bool running) {
  self->setRunning(running);
}

//  void StateMachine::checkChildMode()
extern "C" Q_DECL_EXPORT
void ritual_ZN12StateMachine14checkChildModeEv(StateMachine *self) {
  self->checkChildMode();
}

//  void StateMachine::childrenContentChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN12StateMachine22childrenContentChangedEv(StateMachine *self) {
  self->childrenContentChanged();
}

//  StateMachine as the QQmlParserStatus it is built on
extern "C" Q_DECL_EXPORT
QQmlParserStatus *ritual_cast_StateMachine_QQmlParserStatus(
    StateMachine *self) {
  return static_cast<QQmlParserStatus *>(self);
}

//  void StateMachine::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12StateMachine10classBeginEv(StateMachine *self) {
  self->StateMachine::classBegin();
}

//  void StateMachine::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12StateMachine17componentCompleteEv(StateMachine *self) {
  self->StateMachine::componentComplete();
}
