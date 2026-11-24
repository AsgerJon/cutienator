//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/qhttp2configuration_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qhttp2configuration_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/qhttp2configuration.h>

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
