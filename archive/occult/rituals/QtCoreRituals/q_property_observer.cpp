//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qproperty.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qproperty.h>

//  QPropertyObserver::QPropertyObserver()
extern "C" Q_DECL_EXPORT
QPropertyObserver *ritual_ZN17QPropertyObserverC1Ev() {
  return new QPropertyObserver();
}

//  QPropertyObserver::~QPropertyObserver()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QPropertyObserverD1Ev(QPropertyObserver *self) {
  delete self;
}

//  QPropertyObserver::QPropertyObserver(QUntypedPropertyData
//      *aliasedPropertyPtr)
extern "C" Q_DECL_EXPORT
QPropertyObserver *ritual_ZN17QPropertyObserverC1EP20QUntypedPropertyData(
    QUntypedPropertyData *aliasedPropertyPtr) {
  return new QPropertyObserver(aliasedPropertyPtr);
}

//  QUntypedPropertyData *QPropertyObserver::aliasedProperty() const
extern "C" Q_DECL_EXPORT
QUntypedPropertyData *ritual_ZNK17QPropertyObserver15aliasedPropertyEv(
    const QPropertyObserver *self) {
  return self->aliasedProperty();
}
