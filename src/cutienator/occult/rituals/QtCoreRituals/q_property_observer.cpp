//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qproperty.h, Qt 6.12.0. Edited by hand on 2026-11-25, mended on
//  2026-11-26: added by hand, instances of templates of the class: 5. Kept
//  as it is when the generator runs again.
#include <QtCore/qvariant.h>
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

//  void QPropertyObserver::setSource<QProperty<int>>(const QProperty<int>
//      &property)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QPropertyObserver9setSourceI9QPropertyIiELb1EEvRKT_(
    QPropertyObserver *self,
    const QProperty<int> *property) {
  self->setSource<QProperty<int>>(*property);
}

//  void QPropertyObserver::setSource<QProperty<double>>(const
//      QProperty<double> &property)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QPropertyObserver9setSourceI9QPropertyIdELb1EEvRKT_(
    QPropertyObserver *self,
    const QProperty<double> *property) {
  self->setSource<QProperty<double>>(*property);
}

//  void QPropertyObserver::setSource<QProperty<bool>>(const QProperty<bool>
//      &property)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QPropertyObserver9setSourceI9QPropertyIbELb1EEvRKT_(
    QPropertyObserver *self,
    const QProperty<bool> *property) {
  self->setSource<QProperty<bool>>(*property);
}

//  void QPropertyObserver::setSource<QProperty<QString>>(const
//      QProperty<QString> &property)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QPropertyObserver9setSourceI9QPropertyI7QStringELb1EEvRKT_(
    QPropertyObserver *self,
    const QProperty<QString> *property) {
  self->setSource<QProperty<QString>>(*property);
}

//  void QPropertyObserver::setSource<QProperty<QVariant>>(const
//      QProperty<QVariant> &property)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QPropertyObserver9setSourceI9QPropertyI8QVariantELb1EEvRKT_(
    QPropertyObserver *self,
    const QProperty<QVariant> *property) {
  self->setSource<QProperty<QVariant>>(*property);
}
