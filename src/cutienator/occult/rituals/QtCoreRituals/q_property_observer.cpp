//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qproperty.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qproperty.h>

//  QPropertyObserver::QPropertyObserver()
extern "C" Q_DECL_EXPORT
QPropertyObserver *ritual_ZN17QPropertyObserverC1Ev() {
  return new QPropertyObserver();
}

//  QPropertyObserver::QPropertyObserver(QPropertyObserver &&other)
extern "C" Q_DECL_EXPORT
QPropertyObserver *ritual_ZN17QPropertyObserverC1EOS_(
    QPropertyObserver *other) {
  return new QPropertyObserver(std::move(*other));
}

//  QPropertyObserver &QPropertyObserver::operator=(QPropertyObserver
//      &&other)
extern "C" Q_DECL_EXPORT
QPropertyObserver *ritual_ZN17QPropertyObserveraSEOS_(
    QPropertyObserver *self,
    QPropertyObserver *other) {
  return &(self->operator=(std::move(*other)));
}

//  QPropertyObserver::~QPropertyObserver()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QPropertyObserverD1Ev(QPropertyObserver *self) {
  delete self;
}

//  void QPropertyObserver::setSource(const QtPrivate::QPropertyBindingData
//      &property)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QPropertyObserver9setSourceERKN9QtPrivate20QPropertyBindingDataE(
    QPropertyObserver *self,
    const QtPrivate::QPropertyBindingData *property) {
  self->setSource(*property);
}

//  QPropertyObserver::QPropertyObserver(ChangeHandler changeHandler)
extern "C" Q_DECL_EXPORT
QPropertyObserver *ritual_ZN17QPropertyObserverC1EPFvPS_P20QUntypedPropertyDataE(
    void *changeHandler) {
  return new QPropertyObserver(
      reinterpret_cast<QPropertyObserverBase::ChangeHandler>(changeHandler));
}

#if QT_DEPRECATED_SINCE(6, 6)
//  QPropertyObserver::QPropertyObserver(QUntypedPropertyData
//      *aliasedPropertyPtr)
extern "C" Q_DECL_EXPORT
QPropertyObserver *ritual_ZN17QPropertyObserverC1EP20QUntypedPropertyData(
    QUntypedPropertyData *aliasedPropertyPtr) {
  return new QPropertyObserver(aliasedPropertyPtr);
}
#endif  // QT_DEPRECATED_SINCE(6, 6)

//  QUntypedPropertyData *QPropertyObserver::aliasedProperty() const
extern "C" Q_DECL_EXPORT
QUntypedPropertyData *ritual_ZNK17QPropertyObserver15aliasedPropertyEv(
    const QPropertyObserver *self) {
  return self->aliasedProperty();
}
