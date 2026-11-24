//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qproperty_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qproperty_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QPropertyBindingPrivate *QPropertyBindingDataPointer::binding() const
extern "C" Q_DECL_EXPORT
QPropertyBindingPrivate *ritual_ZNK27QPropertyBindingDataPointer7bindingEv(
    const QPropertyBindingDataPointer *self) {
  return self->binding();
}

//  void QPropertyBindingDataPointer::setObservers(QPropertyObserver
//      *observer)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QPropertyBindingDataPointer12setObserversEP17QPropertyObserver(
    QPropertyBindingDataPointer *self,
    QPropertyObserver *observer) {
  self->setObservers(observer);
}

//  void QPropertyBindingDataPointer::fixupAfterMove(QtPrivate::QPropertyBind
//      ingData *ptr)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QPropertyBindingDataPointer14fixupAfterMoveEPN9QtPrivate20QPropertyBindingDataE(
    QtPrivate::QPropertyBindingData *ptr) {
  QPropertyBindingDataPointer::fixupAfterMove(ptr);
}

//  void QPropertyBindingDataPointer::setFirstObserver(QPropertyObserver
//      *observer)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QPropertyBindingDataPointer16setFirstObserverEP17QPropertyObserver(
    QPropertyBindingDataPointer *self,
    QPropertyObserver *observer) {
  self->setFirstObserver(observer);
}

//  QPropertyObserverPointer QPropertyBindingDataPointer::firstObserver()
//      const
extern "C" Q_DECL_EXPORT
QPropertyObserverPointer *ritual_ZNK27QPropertyBindingDataPointer13firstObserverEv(
    const QPropertyBindingDataPointer *self) {
  return new QPropertyObserverPointer(self->firstObserver());
}

//  QPropertyProxyBindingData
//      *QPropertyBindingDataPointer::proxyData(QtPrivate::QPropertyBindingDa
//      ta *ptr)
extern "C" Q_DECL_EXPORT
QPropertyProxyBindingData *ritual_ZN27QPropertyBindingDataPointer9proxyDataEPN9QtPrivate20QPropertyBindingDataE(
    QtPrivate::QPropertyBindingData *ptr) {
  return QPropertyBindingDataPointer::proxyData(ptr);
}

//  int QPropertyBindingDataPointer::observerCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK27QPropertyBindingDataPointer13observerCountEv(
    const QPropertyBindingDataPointer *self) {
  return self->observerCount();
}

//  QPropertyBindingDataPointer::~QPropertyBindingDataPointer()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QPropertyBindingDataPointerD1Ev(
    QPropertyBindingDataPointer *self) {
  delete self;
}
