//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qpropertyprivate.h, Qt 6.12.0. Edited by hand on 2026-11-25: added
//  by hand, rituals for functions the generator leaves out: 1. Kept as it is
//  when the generator runs again.
#include <QtCore/qpropertyprivate.h>
#include <QtCore/qproperty.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qproperty_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QtPrivate::QPropertyBindingData::QPropertyBindingData()
extern "C" Q_DECL_EXPORT
QtPrivate::QPropertyBindingData *ritual_ZN9QtPrivate20QPropertyBindingDataC1Ev() {
  return new QtPrivate::QPropertyBindingData();
}

//  QtPrivate::QPropertyBindingData::QPropertyBindingData(QPropertyBindingDat
//      a &&other)
extern "C" Q_DECL_EXPORT
QtPrivate::QPropertyBindingData *ritual_ZN9QtPrivate20QPropertyBindingDataC1EOS0_(
    QtPrivate::QPropertyBindingData *other) {
  return new QtPrivate::QPropertyBindingData(std::move(*other));
}

//  QtPrivate::QPropertyBindingData::~QPropertyBindingData()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtPrivate20QPropertyBindingDataD1Ev(
    QtPrivate::QPropertyBindingData *self) {
  delete self;
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

//  QUntypedPropertyBinding QtPrivate::QPropertyBindingData::setBinding(const
//      QUntypedPropertyBinding &newBinding, QUntypedPropertyData
//      *propertyDataPtr, QPropertyObserverCallback staticObserverCallback,
//      QPropertyBindingWrapper bindingWrapper)
extern "C" Q_DECL_EXPORT
QUntypedPropertyBinding *ritual_ZN9QtPrivate20QPropertyBindingData10setBindingERK23QUntypedPropertyBindingP20QUntypedPropertyDataPFvS5_EPFb9QMetaTypeS5_NS_24QPropertyBindingFunctionEE(
    QtPrivate::QPropertyBindingData *self,
    const QUntypedPropertyBinding *newBinding,
    QUntypedPropertyData *propertyDataPtr,
    void *staticObserverCallback,
    void *bindingWrapper) {
  return new QUntypedPropertyBinding(
      self->setBinding(
          *newBinding,
          propertyDataPtr,
          reinterpret_cast<QtPrivate::QPropertyObserverCallback>(staticObserverCallback),
          reinterpret_cast<QtPrivate::QPropertyBindingWrapper>(bindingWrapper)));
}

//  QPropertyBindingPrivate *QtPrivate::QPropertyBindingData::binding() const
extern "C" Q_DECL_EXPORT
QPropertyBindingPrivate *ritual_ZNK9QtPrivate20QPropertyBindingData7bindingEv(
    const QtPrivate::QPropertyBindingData *self) {
  return self->binding();
}

//  void QtPrivate::QPropertyBindingData::evaluateIfDirty(const
//      QUntypedPropertyData *a0) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK9QtPrivate20QPropertyBindingData15evaluateIfDirtyEPK20QUntypedPropertyData(
    const QtPrivate::QPropertyBindingData *self,
    const QUntypedPropertyData *a0) {
  self->evaluateIfDirty(a0);
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

//  void
//      QtPrivate::QPropertyBindingData::registerWithCurrentlyEvaluatingBindi
//      ng() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK9QtPrivate20QPropertyBindingData38registerWithCurrentlyEvaluatingBindingEv(
    const QtPrivate::QPropertyBindingData *self) {
  self->registerWithCurrentlyEvaluatingBinding();
}

//  void
//      QtPrivate::QPropertyBindingData::notifyObservers(QUntypedPropertyData
//      *propertyDataPtr) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK9QtPrivate20QPropertyBindingData15notifyObserversEP20QUntypedPropertyData(
    const QtPrivate::QPropertyBindingData *self,
    QUntypedPropertyData *propertyDataPtr) {
  self->notifyObservers(propertyDataPtr);
}

//  void
//      QtPrivate::QPropertyBindingData::notifyObservers(QUntypedPropertyData
//      *propertyDataPtr, QBindingStorage *storage) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK9QtPrivate20QPropertyBindingData15notifyObserversEP20QUntypedPropertyDataP15QBindingStorage(
    const QtPrivate::QPropertyBindingData *self,
    QUntypedPropertyData *propertyDataPtr,
    QBindingStorage *storage) {
  self->notifyObservers(propertyDataPtr, storage);
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

//  void QtPrivate::QPropertyBindingData::registerWithCurrentlyEvaluatingBind
//      ing_helper(BindingEvaluationState *currentBinding) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK9QtPrivate20QPropertyBindingData45registerWithCurrentlyEvaluatingBinding_helperEPNS_22BindingEvaluationStateE(
    const QtPrivate::QPropertyBindingData *self,
    QtPrivate::BindingEvaluationState *currentBinding) {
  self->registerWithCurrentlyEvaluatingBinding_helper(currentBinding);
}

//  void QtPrivate::QPropertyBindingData::removeBinding_helper()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtPrivate20QPropertyBindingData20removeBinding_helperEv(
    QtPrivate::QPropertyBindingData *self) {
  self->removeBinding_helper();
}

//  NotificationResult QtPrivate::QPropertyBindingData::notifyObserver_helper
//      (QUntypedPropertyData *propertyDataPtr, QBindingStorage *storage,
//      QPropertyObserverPointer observer, PendingBindingObserverList
//      &bindingObservers) const
extern "C" Q_DECL_EXPORT
QtPrivate::QPropertyBindingData::NotificationResult ritual_ZNK9QtPrivate20QPropertyBindingData21notifyObserver_helperEP20QUntypedPropertyDataP15QBindingStorage24QPropertyObserverPointerR15QVarLengthArrayI26QPropertyBindingPrivatePtrLx256EE(
    const QtPrivate::QPropertyBindingData *self,
    QUntypedPropertyData *propertyDataPtr,
    QBindingStorage *storage,
    const QPropertyObserverPointer *observer,
    PendingBindingObserverList *bindingObservers) {
  return self->notifyObserver_helper(
      propertyDataPtr,
      storage,
      *observer,
      *bindingObservers);
}

//  quintptr &QtPrivate::QPropertyBindingData::d_ref() const
extern "C" Q_DECL_EXPORT
quintptr *ritual_ZNK9QtPrivate20QPropertyBindingData5d_refEv(
    const QtPrivate::QPropertyBindingData *self) {
  return &(self->d_ref());
}
