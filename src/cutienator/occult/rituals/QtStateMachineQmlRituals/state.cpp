//  Written by dev_tooling.RitualGenerator from the records of
//  QtStateMachineQml/6.12.0/QtStateMachineQml/private/state_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtStateMachineQml/6.12.0/QtStateMachineQml/private/qstatemachineqmlglobals_p.h>
#include <QtStateMachineQml/QtStateMachineQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtStateMachineQml/6.12.0/QtStateMachineQml/private/state_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  const QMetaObject *State::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK5State10metaObjectEv(const State *self) {
  return self->metaObject();
}

//  QString State::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN5State2trEPKcS1_i(const char *s, const char *c, int n) {
  return new QString(State::tr(s, c, n));
}

//  State::State(QState *parent)
extern "C" Q_DECL_EXPORT
State *ritual_ZN5StateC1EP6QState(QState *parent) {
  return new State(parent);
}

//  void State::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN5State10classBeginEv(State *self) {
  self->classBegin();
}

//  void State::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN5State17componentCompleteEv(State *self) {
  self->componentComplete();
}

//  void State::childrenContentChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN5State22childrenContentChangedEv(State *self) {
  self->childrenContentChanged();
}

//  State as the QQmlParserStatus it is built on
extern "C" Q_DECL_EXPORT
QQmlParserStatus *ritual_cast_State_QQmlParserStatus(State *self) {
  return static_cast<QQmlParserStatus *>(self);
}

//  void State::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN5State10classBeginEv(State *self) {
  self->State::classBegin();
}

//  void State::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN5State17componentCompleteEv(State *self) {
  self->State::componentComplete();
}
