//  Written by dev_tooling.RitualGenerator from the records of
//  QtHttpServer/qhttpserverrequest.h, Qt 6.12.0. Changes made here are lost.
#include <QtNetwork/qtnetworkglobal.h>
#include <QtHttpServer/qhttpserverrequest.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qurl.h>
#include <QtCore/qurlquery.h>
#include <QtNetwork/qhttpheaders.h>
#include <QtNetwork/qhostaddress.h>
#include <QtNetwork/qsslconfiguration.h>
#include <QtCore/qdebug.h>
#include <QtHttpServer/QtHttpServer>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtHttpServer/6.12.0/QtHttpServer/private/qhttpserverparser_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QHttpServerRequest::QHttpServerRequest()
extern "C" Q_DECL_EXPORT
QHttpServerRequest *ritual_ZN18QHttpServerRequestC1Ev() {
  return new QHttpServerRequest();
}

//  QHttpServerRequest::QHttpServerRequest(const QHttpServerRequest &other)
extern "C" Q_DECL_EXPORT
QHttpServerRequest *ritual_ZN18QHttpServerRequestC1ERKS_(
    const QHttpServerRequest *other) {
  return new QHttpServerRequest(*other);
}

//  QHttpServerRequest &QHttpServerRequest::operator=(const
//      QHttpServerRequest &other)
extern "C" Q_DECL_EXPORT
QHttpServerRequest *ritual_ZN18QHttpServerRequestaSERKS_(
    QHttpServerRequest *self,
    const QHttpServerRequest *other) {
  return &(self->operator=(*other));
}

//  QHttpServerRequest::QHttpServerRequest(QHttpServerRequest &&other)
extern "C" Q_DECL_EXPORT
QHttpServerRequest *ritual_ZN18QHttpServerRequestC1EOS_(
    QHttpServerRequest *other) {
  return new QHttpServerRequest(std::move(*other));
}

//  QHttpServerRequest &QHttpServerRequest::operator=(QHttpServerRequest
//      &&other)
extern "C" Q_DECL_EXPORT
QHttpServerRequest *ritual_ZN18QHttpServerRequestaSEOS_(
    QHttpServerRequest *self,
    QHttpServerRequest *other) {
  return &(self->operator=(std::move(*other)));
}

//  QHttpServerRequest::~QHttpServerRequest()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QHttpServerRequestD1Ev(QHttpServerRequest *self) {
  delete self;
}

//  void QHttpServerRequest::swap(QHttpServerRequest &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QHttpServerRequest4swapERS_(
    QHttpServerRequest *self,
    QHttpServerRequest *other) {
  self->swap(*other);
}

//  QByteArray QHttpServerRequest::value(const QByteArray &key) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK18QHttpServerRequest5valueERK10QByteArray(
    const QHttpServerRequest *self,
    const QByteArray *key) {
  return new QByteArray(self->value(*key));
}

//  QUrl QHttpServerRequest::url() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK18QHttpServerRequest3urlEv(const QHttpServerRequest *self) {
  return new QUrl(self->url());
}

//  QUrlQuery QHttpServerRequest::query() const
extern "C" Q_DECL_EXPORT
QUrlQuery *ritual_ZNK18QHttpServerRequest5queryEv(
    const QHttpServerRequest *self) {
  return new QUrlQuery(self->query());
}

//  Method QHttpServerRequest::method() const
extern "C" Q_DECL_EXPORT
QHttpServerRequest::Method ritual_ZNK18QHttpServerRequest6methodEv(
    const QHttpServerRequest *self) {
  return self->method();
}

//  const QHttpHeaders &QHttpServerRequest::headers() const
extern "C" Q_DECL_EXPORT
QHttpHeaders *ritual_ZNKR18QHttpServerRequest7headersEv(
    const QHttpServerRequest *self) {
  return new QHttpHeaders(self->headers());
}

//  QByteArray QHttpServerRequest::body() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK18QHttpServerRequest4bodyEv(
    const QHttpServerRequest *self) {
  return new QByteArray(self->body());
}

//  QHostAddress QHttpServerRequest::remoteAddress() const
extern "C" Q_DECL_EXPORT
QHostAddress *ritual_ZNK18QHttpServerRequest13remoteAddressEv(
    const QHttpServerRequest *self) {
  return new QHostAddress(self->remoteAddress());
}

//  quint16 QHttpServerRequest::remotePort() const
extern "C" Q_DECL_EXPORT
quint16 ritual_ZNK18QHttpServerRequest10remotePortEv(
    const QHttpServerRequest *self) {
  return self->remotePort();
}

//  QHostAddress QHttpServerRequest::localAddress() const
extern "C" Q_DECL_EXPORT
QHostAddress *ritual_ZNK18QHttpServerRequest12localAddressEv(
    const QHttpServerRequest *self) {
  return new QHostAddress(self->localAddress());
}

//  quint16 QHttpServerRequest::localPort() const
extern "C" Q_DECL_EXPORT
quint16 ritual_ZNK18QHttpServerRequest9localPortEv(
    const QHttpServerRequest *self) {
  return self->localPort();
}

#if QT_CONFIG(ssl)
//  QSslConfiguration QHttpServerRequest::sslConfiguration() const
extern "C" Q_DECL_EXPORT
QSslConfiguration *ritual_ZNK18QHttpServerRequest16sslConfigurationEv(
    const QHttpServerRequest *self) {
  return new QSslConfiguration(self->sslConfiguration());
}
#endif  // QT_CONFIG(ssl)

#if !defined(QT_NO_DEBUG_STREAM)
//  QDebug operator<<(QDebug debug, const QHttpServerRequest &request)
extern "C" Q_DECL_EXPORT
QDebug *ritual_Zls6QDebugRK18QHttpServerRequest(
    const QDebug *debug,
    const QHttpServerRequest *request) {
  return new QDebug(operator<<(*debug, *request));
}
#endif  // !defined(QT_NO_DEBUG_STREAM)

//  QHttpServerRequest QHttpServerRequest::create(const QHttpServerParser
//      &parser)
extern "C" Q_DECL_EXPORT
QHttpServerRequest *ritual_ZN18QHttpServerRequest6createERK17QHttpServerParser(
    const QHttpServerParser *parser) {
  return new QHttpServerRequest(QHttpServerRequest::create(*parser));
}

#if QT_CONFIG(ssl)
//  QHttpServerRequest QHttpServerRequest::create(const QHttpServerParser
//      &parser, const QSslConfiguration &configuration)
extern "C" Q_DECL_EXPORT
QHttpServerRequest *ritual_ZN18QHttpServerRequest6createERK17QHttpServerParserRK17QSslConfiguration(
    const QHttpServerParser *parser,
    const QSslConfiguration *configuration) {
  return new QHttpServerRequest(
      QHttpServerRequest::create(
          *parser,
          *configuration));
}
#endif  // QT_CONFIG(ssl)

//  QHttpServerRequest::QHttpServerRequest(const QHostAddress &remoteAddress,
//      quint16 remotePort, const QHostAddress &localAddress, quint16
//      localPort)
extern "C" Q_DECL_EXPORT
QHttpServerRequest *ritual_ZN18QHttpServerRequestC1ERK12QHostAddresstS2_t(
    const QHostAddress *remoteAddress,
    quint16 remotePort,
    const QHostAddress *localAddress,
    quint16 localPort) {
  return new QHttpServerRequest(
      *remoteAddress,
      remotePort,
      *localAddress,
      localPort);
}

#if QT_CONFIG(ssl)
//  QHttpServerRequest::QHttpServerRequest(const QHostAddress &remoteAddress,
//      quint16 remotePort, const QHostAddress &localAddress, quint16
//      localPort, const QSslConfiguration &sslConfiguration)
extern "C" Q_DECL_EXPORT
QHttpServerRequest *ritual_ZN18QHttpServerRequestC1ERK12QHostAddresstS2_tRK17QSslConfiguration(
    const QHostAddress *remoteAddress,
    quint16 remotePort,
    const QHostAddress *localAddress,
    quint16 localPort,
    const QSslConfiguration *sslConfiguration) {
  return new QHttpServerRequest(
      *remoteAddress,
      remotePort,
      *localAddress,
      localPort,
      *sslConfiguration);
}
#endif  // QT_CONFIG(ssl)
