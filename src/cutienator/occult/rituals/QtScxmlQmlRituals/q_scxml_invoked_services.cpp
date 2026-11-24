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

//  const QMetaObject *QScxmlInvokedServices::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21QScxmlInvokedServices10metaObjectEv(
    const QScxmlInvokedServices *self) {
  return self->metaObject();
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
