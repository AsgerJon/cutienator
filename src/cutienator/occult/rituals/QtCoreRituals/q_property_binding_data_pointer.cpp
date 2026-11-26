//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qproperty_p.h, Qt 6.12.0. Edited by hand on
//  2026-11-25: added by hand, instances of templates of the class: 5. Kept
//  as it is when the generator runs again.
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

//  static QPropertyBindingDataPointer
//      QPropertyBindingDataPointer::get<int>(QProperty<int> &property)
extern "C" Q_DECL_EXPORT
QPropertyBindingDataPointer * ritual_ZN27QPropertyBindingDataPointer3getIiEES_R9QPropertyIT_E(
    QProperty<int> *property) {
  return new QPropertyBindingDataPointer(
      QPropertyBindingDataPointer::get<int>(*property));
}

//  static QPropertyBindingDataPointer
//      QPropertyBindingDataPointer::get<double>(QProperty<double> &property)
extern "C" Q_DECL_EXPORT
QPropertyBindingDataPointer * ritual_ZN27QPropertyBindingDataPointer3getIdEES_R9QPropertyIT_E(
    QProperty<double> *property) {
  return new QPropertyBindingDataPointer(
      QPropertyBindingDataPointer::get<double>(*property));
}

//  static QPropertyBindingDataPointer
//      QPropertyBindingDataPointer::get<bool>(QProperty<bool> &property)
extern "C" Q_DECL_EXPORT
QPropertyBindingDataPointer * ritual_ZN27QPropertyBindingDataPointer3getIbEES_R9QPropertyIT_E(
    QProperty<bool> *property) {
  return new QPropertyBindingDataPointer(
      QPropertyBindingDataPointer::get<bool>(*property));
}

//  static QPropertyBindingDataPointer
//      QPropertyBindingDataPointer::get<QString>(QProperty<QString>
//      &property)
extern "C" Q_DECL_EXPORT
QPropertyBindingDataPointer * ritual_ZN27QPropertyBindingDataPointer3getI7QStringEES_R9QPropertyIT_E(
    QProperty<QString> *property) {
  return new QPropertyBindingDataPointer(
      QPropertyBindingDataPointer::get<QString>(*property));
}

//  static QPropertyBindingDataPointer
//      QPropertyBindingDataPointer::get<QVariant>(QProperty<QVariant>
//      &property)
extern "C" Q_DECL_EXPORT
QPropertyBindingDataPointer * ritual_ZN27QPropertyBindingDataPointer3getI8QVariantEES_R9QPropertyIT_E(
    QProperty<QVariant> *property) {
  return new QPropertyBindingDataPointer(
      QPropertyBindingDataPointer::get<QVariant>(*property));
}
