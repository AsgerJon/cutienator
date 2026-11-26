//  Written by dev_tooling.RitualGenerator from the records of
//  QtScxmlQml/6.12.0/QtScxmlQml/private/invokedservices_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtScxmlQml/6.12.0/QtScxmlQml/private/qscxmlqmlglobals_p.h>
#include <QtScxmlQml/QtScxmlQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtScxmlQml/6.12.0/QtScxmlQml/private/invokedservices_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#include <QtCore/QBindable>
#include <QtCore/QVariantMap>
#include <QtScxml/QScxmlStateMachine>
#include <QtQml/QQmlListProperty>
#include <QtCore/QObject>

//  const QMetaObject *QScxmlInvokedServices::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21QScxmlInvokedServices10metaObjectEv(
    const QScxmlInvokedServices *self) {
  return self->metaObject();
}

//  void *QScxmlInvokedServices::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN21QScxmlInvokedServices11qt_metacastEPKc(
    QScxmlInvokedServices *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QScxmlInvokedServices::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN21QScxmlInvokedServices11qt_metacallEN11QMetaObject4CallEiPPv(
    QScxmlInvokedServices *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QScxmlInvokedServices::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN21QScxmlInvokedServices2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QScxmlInvokedServices::tr(s, c, n));
}

//  QScxmlInvokedServices::QScxmlInvokedServices(QObject *parent)
extern "C" Q_DECL_EXPORT
QScxmlInvokedServices *ritual_ZN21QScxmlInvokedServicesC1EP7QObject(
    QObject *parent) {
  return new QScxmlInvokedServices(parent);
}

//  QVariantMap QScxmlInvokedServices::children()
extern "C" Q_DECL_EXPORT
QMap<QString, QVariant> *ritual_ZN21QScxmlInvokedServices8childrenEv(
    QScxmlInvokedServices *self) {
  return new QMap<QString, QVariant>(self->children());
}

//  QBindable<QVariantMap> QScxmlInvokedServices::bindableChildren()
extern "C" Q_DECL_EXPORT
QBindable<QVariantMap> *ritual_ZN21QScxmlInvokedServices16bindableChildrenEv(
    QScxmlInvokedServices *self) {
  return new QBindable<QVariantMap>(self->bindableChildren());
}

//  QScxmlStateMachine *QScxmlInvokedServices::stateMachine() const
extern "C" Q_DECL_EXPORT
QScxmlStateMachine *ritual_ZNK21QScxmlInvokedServices12stateMachineEv(
    const QScxmlInvokedServices *self) {
  return self->stateMachine();
}

//  void QScxmlInvokedServices::setStateMachine(QScxmlStateMachine
//      *stateMachine)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QScxmlInvokedServices15setStateMachineEP18QScxmlStateMachine(
    QScxmlInvokedServices *self,
    QScxmlStateMachine *stateMachine) {
  self->setStateMachine(stateMachine);
}

//  QBindable<QScxmlStateMachine *>
//      QScxmlInvokedServices::bindableStateMachine()
extern "C" Q_DECL_EXPORT
QBindable<QScxmlStateMachine *> *ritual_ZN21QScxmlInvokedServices20bindableStateMachineEv(
    QScxmlInvokedServices *self) {
  return new QBindable<QScxmlStateMachine *>(self->bindableStateMachine());
}

//  QQmlListProperty<QObject> QScxmlInvokedServices::qmlChildren()
extern "C" Q_DECL_EXPORT
QQmlListProperty<QObject> *ritual_ZN21QScxmlInvokedServices11qmlChildrenEv(
    QScxmlInvokedServices *self) {
  return new QQmlListProperty<QObject>(self->qmlChildren());
}

//  void QScxmlInvokedServices::childrenChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QScxmlInvokedServices15childrenChangedEv(
    QScxmlInvokedServices *self) {
  self->childrenChanged();
}

//  void QScxmlInvokedServices::stateMachineChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QScxmlInvokedServices19stateMachineChangedEv(
    QScxmlInvokedServices *self) {
  self->stateMachineChanged();
}

//  void QScxmlInvokedServices::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QScxmlInvokedServices10classBeginEv(
    QScxmlInvokedServices *self) {
  self->classBegin();
}

//  void QScxmlInvokedServices::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QScxmlInvokedServices17componentCompleteEv(
    QScxmlInvokedServices *self) {
  self->componentComplete();
}

//  QVariantMap QScxmlInvokedServices::childrenActualCalculation() const
extern "C" Q_DECL_EXPORT
QMap<QString, QVariant> *ritual_ZNK21QScxmlInvokedServices25childrenActualCalculationEv(
    const QScxmlInvokedServices *self) {
  return new QMap<QString, QVariant>(self->childrenActualCalculation());
}

//  size_t QScxmlInvokedServices::_qt_property_m_stateMachine_offset()
extern "C" Q_DECL_EXPORT
size_t ritual_ZN21QScxmlInvokedServices34_qt_property_m_stateMachine_offsetEv() {
  return QScxmlInvokedServices::_qt_property_m_stateMachine_offset();
}

//  size_t QScxmlInvokedServices::_qt_property_m_children_offset()
extern "C" Q_DECL_EXPORT
size_t ritual_ZN21QScxmlInvokedServices30_qt_property_m_children_offsetEv() {
  return QScxmlInvokedServices::_qt_property_m_children_offset();
}

//  QScxmlInvokedServices as the QQmlParserStatus it is built on
extern "C" Q_DECL_EXPORT
QQmlParserStatus *ritual_cast_QScxmlInvokedServices_QQmlParserStatus(
    QScxmlInvokedServices *self) {
  return static_cast<QQmlParserStatus *>(self);
}

//  void QScxmlInvokedServices::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QScxmlInvokedServices10classBeginEv(
    QScxmlInvokedServices *self) {
  self->QScxmlInvokedServices::classBegin();
}

//  void QScxmlInvokedServices::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QScxmlInvokedServices17componentCompleteEv(
    QScxmlInvokedServices *self) {
  self->QScxmlInvokedServices::componentComplete();
}

//  a QBindable<QVariantMap> a ritual of QScxmlInvokedServices gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QScxmlInvokedServices__QBindable_QVariantMap(
    QBindable<QVariantMap> *self) {
  delete self;
}

//  a QBindable<QScxmlStateMachine *> a ritual of QScxmlInvokedServices gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QScxmlInvokedServices__QBindable_QScxmlStateMachine(
    QBindable<QScxmlStateMachine *> *self) {
  delete self;
}

//  a QQmlListProperty<QObject> a ritual of QScxmlInvokedServices gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QScxmlInvokedServices__QQmlListProperty_QObject(
    QQmlListProperty<QObject> *self) {
  delete self;
}
