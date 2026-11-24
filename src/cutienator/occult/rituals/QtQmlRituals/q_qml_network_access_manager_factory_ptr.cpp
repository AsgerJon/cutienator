//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmltypeloaderdata_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQml/qtqmlglobal.h>
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#if QT_CONFIG(qml_network)
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmltypeloaderdata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QQmlNetworkAccessManagerFactoryPtr::QQmlNetworkAccessManagerFactoryPtr(QQ
//      mlTypeLoaderLockedData *lockedData)
extern "C" Q_DECL_EXPORT
QQmlNetworkAccessManagerFactoryPtr *ritual_ZN34QQmlNetworkAccessManagerFactoryPtrC1EP24QQmlTypeLoaderLockedData(
    QQmlTypeLoaderLockedData *lockedData) {
  return new QQmlNetworkAccessManagerFactoryPtr(lockedData);
}

//  void
//      QQmlNetworkAccessManagerFactoryPtr::reset(QQmlNetworkAccessManagerFac
//      tory *factory)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QQmlNetworkAccessManagerFactoryPtr5resetEP31QQmlNetworkAccessManagerFactory(
    QQmlNetworkAccessManagerFactoryPtr *self,
    QQmlNetworkAccessManagerFactory *factory) {
  self->reset(factory);
}

#endif  // QT_CONFIG(qml_network)
