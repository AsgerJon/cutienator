//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qpropertyprivate.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qpropertyprivate.h>

//  QtPrivate::QPropertyBindingData::QPropertyBindingData()
extern "C" Q_DECL_EXPORT
QtPrivate::QPropertyBindingData *ritual_ZN9QtPrivate20QPropertyBindingDataC1Ev() {
  return new QtPrivate::QPropertyBindingData();
}

//  bool QtPrivate::QPropertyBindingData::hasBinding() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QtPrivate20QPropertyBindingData10hasBindingEv(
    const QtPrivate::QPropertyBindingData *self) {
  return self->hasBinding();
}

//  bool QtPrivate::QPropertyBindingData::isNotificationDelayed() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QtPrivate20QPropertyBindingData21isNotificationDelayedEv(
    const QtPrivate::QPropertyBindingData *self) {
  return self->isNotificationDelayed();
}

//  QPropertyBindingPrivate *QtPrivate::QPropertyBindingData::binding() const
extern "C" Q_DECL_EXPORT
QPropertyBindingPrivate *ritual_ZNK9QtPrivate20QPropertyBindingData7bindingEv(
    const QtPrivate::QPropertyBindingData *self) {
  return self->binding();
}

//  void QtPrivate::QPropertyBindingData::removeBinding()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtPrivate20QPropertyBindingData13removeBindingEv(
    QtPrivate::QPropertyBindingData *self) {
  self->removeBinding();
}

//  void QtPrivate::QPropertyBindingData::registerWithCurrentlyEvaluatingBind
//      ing(QtPrivate::BindingEvaluationState *currentBinding) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK9QtPrivate20QPropertyBindingData38registerWithCurrentlyEvaluatingBindingEPNS_22BindingEvaluationStateE(
    const QtPrivate::QPropertyBindingData *self,
    QtPrivate::BindingEvaluationState *currentBinding) {
  self->registerWithCurrentlyEvaluatingBinding(currentBinding);
}

//  quintptr QtPrivate::QPropertyBindingData::d() const
extern "C" Q_DECL_EXPORT
quintptr ritual_ZNK9QtPrivate20QPropertyBindingData1dEv(
    const QtPrivate::QPropertyBindingData *self) {
  return self->d();
}

//  QPropertyProxyBindingData *QtPrivate::QPropertyBindingData::proxyData()
//      const
extern "C" Q_DECL_EXPORT
QPropertyProxyBindingData *ritual_ZNK9QtPrivate20QPropertyBindingData9proxyDataEv(
    const QtPrivate::QPropertyBindingData *self) {
  return self->proxyData();
}
