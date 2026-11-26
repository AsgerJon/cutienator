//  Written by dev_tooling.RitualGenerator from the records of
//  QtStateMachineQml/6.12.0/QtStateMachineQml/private/state_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtStateMachineQml/6.12.0/QtStateMachineQml/private/qstatemachineqmlglobals_p.h>
#include <QtStateMachineQml/QtStateMachineQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtStateMachineQml/6.12.0/QtStateMachineQml/private/state_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtQml/QQmlListProperty>
#include <QtCore/QObject>
#include <QtCore/QBindable>

//  const QMetaObject *State::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK5State10metaObjectEv(const State *self) {
  return self->metaObject();
}

//  void *State::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN5State11qt_metacastEPKc(State *self, const char *a0) {
  return self->qt_metacast(a0);
}

//  int State::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN5State11qt_metacallEN11QMetaObject4CallEiPPv(
    State *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
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

//  QQmlListProperty<QObject> State::children()
extern "C" Q_DECL_EXPORT
QQmlListProperty<QObject> *ritual_ZN5State8childrenEv(State *self) {
  return new QQmlListProperty<QObject>(self->children());
}

//  QBindable<QQmlListProperty<QObject>> State::bindableChildren() const
extern "C" Q_DECL_EXPORT
QBindable<QQmlListProperty<QObject>> *ritual_ZNK5State16bindableChildrenEv(
    const State *self) {
  return new QBindable<QQmlListProperty<QObject>>(self->bindableChildren());
}

//  void State::childrenChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN5State15childrenChangedEv(State *self) {
  self->childrenChanged();
}

//  void State::childrenContentChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN5State22childrenContentChangedEv(State *self) {
  self->childrenContentChanged();
}

//  QQmlListProperty<QObject> State::childrenActualCalculation() const
extern "C" Q_DECL_EXPORT
QQmlListProperty<QObject> *ritual_ZNK5State25childrenActualCalculationEv(
    const State *self) {
  return new QQmlListProperty<QObject>(self->childrenActualCalculation());
}

//  size_t State::_qt_property_m_childrenComputedProperty_offset()
extern "C" Q_DECL_EXPORT
size_t ritual_ZN5State46_qt_property_m_childrenComputedProperty_offsetEv() {
  return State::_qt_property_m_childrenComputedProperty_offset();
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

//  a QQmlListProperty<QObject> a ritual of State gave
extern "C" Q_DECL_EXPORT
void ritual_drop_State__QQmlListProperty_QObject(
    QQmlListProperty<QObject> *self) {
  delete self;
}

//  a QBindable<QQmlListProperty<QObject>> a ritual of State gave
extern "C" Q_DECL_EXPORT
void ritual_drop_State__QBindable_QQmlListProperty_QObject(
    QBindable<QQmlListProperty<QObject>> *self) {
  delete self;
}
