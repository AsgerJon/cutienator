//  Written by dev_tooling.RitualGenerator from the records of
//  QtStateMachineQml/6.12.0/QtStateMachineQml/private/statemachine_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtStateMachineQml/6.12.0/QtStateMachineQml/private/qstatemachineqmlglobals_p.h>
#include <QtStateMachineQml/QtStateMachineQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtStateMachineQml/6.12.0/QtStateMachineQml/private/statemachine_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtQml/QQmlListProperty>
#include <QtCore/QObject>
#include <QtCore/QBindable>

//  const QMetaObject *StateMachine::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK12StateMachine10metaObjectEv(
    const StateMachine *self) {
  return self->metaObject();
}

//  void *StateMachine::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN12StateMachine11qt_metacastEPKc(
    StateMachine *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int StateMachine::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN12StateMachine11qt_metacallEN11QMetaObject4CallEiPPv(
    StateMachine *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
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

//  QQmlListProperty<QObject> StateMachine::children()
extern "C" Q_DECL_EXPORT
QQmlListProperty<QObject> *ritual_ZN12StateMachine8childrenEv(
    StateMachine *self) {
  return new QQmlListProperty<QObject>(self->children());
}

//  QBindable<QQmlListProperty<QObject>> StateMachine::bindableChildren()
//      const
extern "C" Q_DECL_EXPORT
QBindable<QQmlListProperty<QObject>> *ritual_ZNK12StateMachine16bindableChildrenEv(
    const StateMachine *self) {
  return new QBindable<QQmlListProperty<QObject>>(self->bindableChildren());
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

//  void StateMachine::childrenChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN12StateMachine15childrenChangedEv(StateMachine *self) {
  self->childrenChanged();
}

//  void StateMachine::qmlRunningChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN12StateMachine17qmlRunningChangedEv(StateMachine *self) {
  self->qmlRunningChanged();
}

//  void StateMachine::childrenContentChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN12StateMachine22childrenContentChangedEv(StateMachine *self) {
  self->childrenContentChanged();
}

//  QQmlListProperty<QObject> StateMachine::childrenActualCalculation() const
extern "C" Q_DECL_EXPORT
QQmlListProperty<QObject> *ritual_ZNK12StateMachine25childrenActualCalculationEv(
    const StateMachine *self) {
  return new QQmlListProperty<QObject>(self->childrenActualCalculation());
}

//  size_t StateMachine::_qt_property_m_childrenComputedProperty_offset()
extern "C" Q_DECL_EXPORT
size_t ritual_ZN12StateMachine46_qt_property_m_childrenComputedProperty_offsetEv() {
  return StateMachine::_qt_property_m_childrenComputedProperty_offset();
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

//  a QQmlListProperty<QObject> a ritual of StateMachine gave
extern "C" Q_DECL_EXPORT
void ritual_drop_StateMachine__QQmlListProperty_QObject(
    QQmlListProperty<QObject> *self) {
  delete self;
}

//  a QBindable<QQmlListProperty<QObject>> a ritual of StateMachine gave
extern "C" Q_DECL_EXPORT
void ritual_drop_StateMachine__QBindable_QQmlListProperty_QObject(
    QBindable<QQmlListProperty<QObject>> *self) {
  delete self;
}
