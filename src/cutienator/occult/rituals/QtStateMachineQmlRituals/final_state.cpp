//  Written by dev_tooling.RitualGenerator from the records of
//  QtStateMachineQml/6.12.0/QtStateMachineQml/private/finalstate_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtStateMachineQml/6.12.0/QtStateMachineQml/private/qstatemachineqmlglobals_p.h>
#include <QtStateMachineQml/QtStateMachineQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtStateMachineQml/6.12.0/QtStateMachineQml/private/finalstate_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtQml/QQmlListProperty>
#include <QtCore/QObject>
#include <QtCore/QBindable>

//  const QMetaObject *FinalState::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10FinalState10metaObjectEv(
    const FinalState *self) {
  return self->metaObject();
}

//  void *FinalState::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10FinalState11qt_metacastEPKc(
    FinalState *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int FinalState::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10FinalState11qt_metacallEN11QMetaObject4CallEiPPv(
    FinalState *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString FinalState::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10FinalState2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(FinalState::tr(s, c, n));
}

//  FinalState::FinalState(QState *parent)
extern "C" Q_DECL_EXPORT
FinalState *ritual_ZN10FinalStateC1EP6QState(QState *parent) {
  return new FinalState(parent);
}

//  QQmlListProperty<QObject> FinalState::children()
extern "C" Q_DECL_EXPORT
QQmlListProperty<QObject> *ritual_ZN10FinalState8childrenEv(
    FinalState *self) {
  return new QQmlListProperty<QObject>(self->children());
}

//  QBindable<QQmlListProperty<QObject>> FinalState::bindableChildren() const
extern "C" Q_DECL_EXPORT
QBindable<QQmlListProperty<QObject>> *ritual_ZNK10FinalState16bindableChildrenEv(
    const FinalState *self) {
  return new QBindable<QQmlListProperty<QObject>>(self->bindableChildren());
}

//  void FinalState::childrenChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN10FinalState15childrenChangedEv(FinalState *self) {
  self->childrenChanged();
}

//  void FinalState::childrenContentChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN10FinalState22childrenContentChangedEv(FinalState *self) {
  self->childrenContentChanged();
}

//  QQmlListProperty<QObject> FinalState::childrenActualCalculation() const
extern "C" Q_DECL_EXPORT
QQmlListProperty<QObject> *ritual_ZNK10FinalState25childrenActualCalculationEv(
    const FinalState *self) {
  return new QQmlListProperty<QObject>(self->childrenActualCalculation());
}

//  size_t FinalState::_qt_property_m_childrenComputedProperty_offset()
extern "C" Q_DECL_EXPORT
size_t ritual_ZN10FinalState46_qt_property_m_childrenComputedProperty_offsetEv() {
  return FinalState::_qt_property_m_childrenComputedProperty_offset();
}

//  a QQmlListProperty<QObject> a ritual of FinalState gave
extern "C" Q_DECL_EXPORT
void ritual_drop_FinalState__QQmlListProperty_QObject(
    QQmlListProperty<QObject> *self) {
  delete self;
}

//  a QBindable<QQmlListProperty<QObject>> a ritual of FinalState gave
extern "C" Q_DECL_EXPORT
void ritual_drop_FinalState__QBindable_QQmlListProperty_QObject(
    QBindable<QQmlListProperty<QObject>> *self) {
  delete self;
}
