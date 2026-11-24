//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qproperty_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qproperty_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QPropertyObserverNodeProtector::QPropertyObserverNodeProtector(QPropertyO
//      bserver *observer)
extern "C" Q_DECL_EXPORT
QPropertyObserverNodeProtector *ritual_ZN30QPropertyObserverNodeProtectorC1EP17QPropertyObserver(
    QPropertyObserver *observer) {
  return new QPropertyObserverNodeProtector(observer);
}

//  QPropertyObserver *QPropertyObserverNodeProtector::next() const
extern "C" Q_DECL_EXPORT
QPropertyObserver *ritual_ZNK30QPropertyObserverNodeProtector4nextEv(
    const QPropertyObserverNodeProtector *self) {
  return self->next();
}

//  QPropertyObserverNodeProtector::~QPropertyObserverNodeProtector()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QPropertyObserverNodeProtectorD1Ev(
    QPropertyObserverNodeProtector *self) {
  delete self;
}
