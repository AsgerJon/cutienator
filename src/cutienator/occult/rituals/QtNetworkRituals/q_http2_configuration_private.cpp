//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/qhttp2configuration_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtNetwork/qtnetworkglobal.h>
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#if QT_CONFIG(http)
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qhttp2configuration_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#if QT_CONFIG(http)
#include <QtNetwork/qhttp2configuration.h>
#endif

//  QHttp2ConfigurationPrivate
//      *QHttp2ConfigurationPrivate::get(QHttp2Configuration &config)
extern "C" Q_DECL_EXPORT
QHttp2ConfigurationPrivate *ritual_ZN26QHttp2ConfigurationPrivate3getER19QHttp2Configuration(
    QHttp2Configuration *config) {
  return QHttp2ConfigurationPrivate::get(*config);
}

//  const QHttp2ConfigurationPrivate *QHttp2ConfigurationPrivate::get(const
//      QHttp2Configuration &config)
extern "C" Q_DECL_EXPORT
const QHttp2ConfigurationPrivate *ritual_ZN26QHttp2ConfigurationPrivate3getERK19QHttp2Configuration(
    const QHttp2Configuration *config) {
  return QHttp2ConfigurationPrivate::get(*config);
}

//  QHttp2ConfigurationPrivate::~QHttp2ConfigurationPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QHttp2ConfigurationPrivateD1Ev(
    QHttp2ConfigurationPrivate *self) {
  delete self;
}

#endif  // QT_CONFIG(http)
