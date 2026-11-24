//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlincubator_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlincubator_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QQmlIncubatorPrivate::QQmlIncubatorPrivate(QQmlIncubator *q,
//      QQmlIncubator::IncubationMode m)
extern "C" Q_DECL_EXPORT
QQmlIncubatorPrivate *ritual_ZN20QQmlIncubatorPrivateC1EP13QQmlIncubatorNS0_14IncubationModeE(
    QQmlIncubator *q,
    QQmlIncubator::IncubationMode m) {
  return new QQmlIncubatorPrivate(q, m);
}

//  QQmlIncubatorPrivate::~QQmlIncubatorPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlIncubatorPrivateD1Ev(QQmlIncubatorPrivate *self) {
  delete self;
}

//  QQmlIncubatorPrivate *QQmlIncubatorPrivate::get(QQmlIncubator *incubator)
extern "C" Q_DECL_EXPORT
QQmlIncubatorPrivate *ritual_ZN20QQmlIncubatorPrivate3getEP13QQmlIncubator(
    QQmlIncubator *incubator) {
  return QQmlIncubatorPrivate::get(incubator);
}

//  QQmlIncubator::Status QQmlIncubatorPrivate::calculateStatus() const
extern "C" Q_DECL_EXPORT
QQmlIncubator::Status ritual_ZNK20QQmlIncubatorPrivate15calculateStatusEv(
    const QQmlIncubatorPrivate *self) {
  return self->calculateStatus();
}

//  void QQmlIncubatorPrivate::changeStatus(QQmlIncubator::Status a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlIncubatorPrivate12changeStatusEN13QQmlIncubator6StatusE(
    QQmlIncubatorPrivate *self,
    QQmlIncubator::Status a0) {
  self->changeStatus(a0);
}

//  void QQmlIncubatorPrivate::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlIncubatorPrivate5clearEv(QQmlIncubatorPrivate *self) {
  self->clear();
}

//  void QQmlIncubatorPrivate::incubateCppBasedComponent(QQmlComponent
//      *component, QQmlContext *context)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlIncubatorPrivate25incubateCppBasedComponentEP13QQmlComponentP11QQmlContext(
    QQmlIncubatorPrivate *self,
    QQmlComponent *component,
    QQmlContext *context) {
  self->incubateCppBasedComponent(component, context);
}

//  RequiredProperties *QQmlIncubatorPrivate::requiredProperties()
extern "C" Q_DECL_EXPORT
RequiredProperties *ritual_ZN20QQmlIncubatorPrivate18requiredPropertiesEv(
    QQmlIncubatorPrivate *self) {
  return self->requiredProperties();
}

//  bool QQmlIncubatorPrivate::hadTopLevelRequiredProperties() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QQmlIncubatorPrivate29hadTopLevelRequiredPropertiesEv(
    const QQmlIncubatorPrivate *self) {
  return self->hadTopLevelRequiredProperties();
}

//  QQmlIncubatorPrivate as the QSharedData it is built on
extern "C" Q_DECL_EXPORT
QSharedData *ritual_cast_QQmlIncubatorPrivate_QSharedData(
    QQmlIncubatorPrivate *self) {
  return static_cast<QSharedData *>(self);
}
