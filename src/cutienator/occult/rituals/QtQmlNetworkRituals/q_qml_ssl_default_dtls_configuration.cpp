//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlNetwork/6.12.0/QtQmlNetwork/private/qqmlsslconfiguration_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQml/qtqmlglobal.h>
#include <QtQmlNetwork/qtqmlnetworkexports.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(qml_ssl)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtQmlNetwork/QtQmlNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlNetwork/6.12.0/QtQmlNetwork/private/qqmlsslconfiguration_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QQmlSslDefaultDtlsConfiguration::QQmlSslDefaultDtlsConfiguration()
extern "C" Q_DECL_EXPORT
QQmlSslDefaultDtlsConfiguration *ritual_ZN31QQmlSslDefaultDtlsConfigurationC1Ev() {
  return new QQmlSslDefaultDtlsConfiguration();
}

//  QQmlSslDefaultDtlsConfiguration::~QQmlSslDefaultDtlsConfiguration()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQmlSslDefaultDtlsConfigurationD1Ev(
    QQmlSslDefaultDtlsConfiguration *self) {
  delete self;
}

#endif  // QT_CONFIG(qml_ssl)
