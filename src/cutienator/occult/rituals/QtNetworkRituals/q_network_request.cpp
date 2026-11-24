//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/qnetworkrequest.h, Qt 6.12.0. Changes made here are lost.
#include <QtNetwork/qnetworkrequest.h>
#include <QtCore/qurl.h>
#include <QtNetwork/qhttpheaders.h>
#include <QtCore/qvariant.h>
#include <QtCore/qanystringview.h>
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <QtNetwork/qsslconfiguration.h>
#include <QtNetwork/qhttp1configuration.h>
#include <QtNetwork/qhttp2configuration.h>
#include <QtCore/qlist.h>

//  QNetworkRequest::QNetworkRequest()
extern "C" Q_DECL_EXPORT
QNetworkRequest *ritual_ZN15QNetworkRequestC1Ev() {
  return new QNetworkRequest();
}

//  QNetworkRequest::QNetworkRequest(const QUrl &url)
extern "C" Q_DECL_EXPORT
QNetworkRequest *ritual_ZN15QNetworkRequestC1ERK4QUrl(const QUrl *url) {
  return new QNetworkRequest(*url);
}

//  QNetworkRequest::QNetworkRequest(const QNetworkRequest &other)
extern "C" Q_DECL_EXPORT
QNetworkRequest *ritual_ZN15QNetworkRequestC1ERKS_(
    const QNetworkRequest *other) {
  return new QNetworkRequest(*other);
}

//  QNetworkRequest::~QNetworkRequest()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QNetworkRequestD1Ev(QNetworkRequest *self) {
  delete self;
}

//  bool QNetworkRequest::operator==(const QNetworkRequest &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QNetworkRequesteqERKS_(
    const QNetworkRequest *self,
    const QNetworkRequest *other) {
  return self->operator==(*other);
}

//  bool QNetworkRequest::operator!=(const QNetworkRequest &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QNetworkRequestneERKS_(
    const QNetworkRequest *self,
    const QNetworkRequest *other) {
  return self->operator!=(*other);
}

//  QUrl QNetworkRequest::url() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK15QNetworkRequest3urlEv(const QNetworkRequest *self) {
  return new QUrl(self->url());
}

//  void QNetworkRequest::setUrl(const QUrl &url)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QNetworkRequest6setUrlERK4QUrl(
    QNetworkRequest *self,
    const QUrl *url) {
  self->setUrl(*url);
}

//  QHttpHeaders QNetworkRequest::headers() const
extern "C" Q_DECL_EXPORT
QHttpHeaders *ritual_ZNK15QNetworkRequest7headersEv(
    const QNetworkRequest *self) {
  return new QHttpHeaders(self->headers());
}

//  void QNetworkRequest::setHeaders(const QHttpHeaders &newHeaders)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QNetworkRequest10setHeadersERK12QHttpHeaders(
    QNetworkRequest *self,
    const QHttpHeaders *newHeaders) {
  self->setHeaders(*newHeaders);
}

//  QVariant QNetworkRequest::header(KnownHeaders header) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK15QNetworkRequest6headerENS_12KnownHeadersE(
    const QNetworkRequest *self,
    QNetworkRequest::KnownHeaders header) {
  return new QVariant(self->header(header));
}

//  void QNetworkRequest::setHeader(KnownHeaders header, const QVariant
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QNetworkRequest9setHeaderENS_12KnownHeadersERK8QVariant(
    QNetworkRequest *self,
    QNetworkRequest::KnownHeaders header,
    const QVariant *value) {
  self->setHeader(header, *value);
}

//  bool QNetworkRequest::hasRawHeader(QAnyStringView headerName) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QNetworkRequest12hasRawHeaderE14QAnyStringView(
    const QNetworkRequest *self,
    const QString *headerName) {
  return self->hasRawHeader(QAnyStringView(*headerName));
}

//  QList<QByteArray> QNetworkRequest::rawHeaderList() const
extern "C" Q_DECL_EXPORT
QList<QByteArray> *ritual_ZNK15QNetworkRequest13rawHeaderListEv(
    const QNetworkRequest *self) {
  return new QList<QByteArray>(self->rawHeaderList());
}

//  QByteArray QNetworkRequest::rawHeader(QAnyStringView headerName) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK15QNetworkRequest9rawHeaderE14QAnyStringView(
    const QNetworkRequest *self,
    const QString *headerName) {
  return new QByteArray(self->rawHeader(QAnyStringView(*headerName)));
}

//  void QNetworkRequest::setRawHeader(const QByteArray &headerName, const
//      QByteArray &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QNetworkRequest12setRawHeaderERK10QByteArrayS2_(
    QNetworkRequest *self,
    const QByteArray *headerName,
    const QByteArray *value) {
  self->setRawHeader(*headerName, *value);
}

//  QVariant QNetworkRequest::attribute(Attribute code, const QVariant
//      &defaultValue) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK15QNetworkRequest9attributeENS_9AttributeERK8QVariant(
    const QNetworkRequest *self,
    QNetworkRequest::Attribute code,
    const QVariant *defaultValue) {
  return new QVariant(self->attribute(code, *defaultValue));
}

//  void QNetworkRequest::setAttribute(Attribute code, const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QNetworkRequest12setAttributeENS_9AttributeERK8QVariant(
    QNetworkRequest *self,
    QNetworkRequest::Attribute code,
    const QVariant *value) {
  self->setAttribute(code, *value);
}

#if !defined(QT_NO_SSL)
//  QSslConfiguration QNetworkRequest::sslConfiguration() const
extern "C" Q_DECL_EXPORT
QSslConfiguration *ritual_ZNK15QNetworkRequest16sslConfigurationEv(
    const QNetworkRequest *self) {
  return new QSslConfiguration(self->sslConfiguration());
}
#endif  // !defined(QT_NO_SSL)

#if !defined(QT_NO_SSL)
//  void QNetworkRequest::setSslConfiguration(const QSslConfiguration
//      &configuration)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QNetworkRequest19setSslConfigurationERK17QSslConfiguration(
    QNetworkRequest *self,
    const QSslConfiguration *configuration) {
  self->setSslConfiguration(*configuration);
}
#endif  // !defined(QT_NO_SSL)

//  void QNetworkRequest::setOriginatingObject(QObject *object)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QNetworkRequest20setOriginatingObjectEP7QObject(
    QNetworkRequest *self,
    QObject *object) {
  self->setOriginatingObject(object);
}

//  QObject *QNetworkRequest::originatingObject() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK15QNetworkRequest17originatingObjectEv(
    const QNetworkRequest *self) {
  return self->originatingObject();
}

//  Priority QNetworkRequest::priority() const
extern "C" Q_DECL_EXPORT
QNetworkRequest::Priority ritual_ZNK15QNetworkRequest8priorityEv(
    const QNetworkRequest *self) {
  return self->priority();
}

//  void QNetworkRequest::setPriority(Priority priority)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QNetworkRequest11setPriorityENS_8PriorityE(
    QNetworkRequest *self,
    QNetworkRequest::Priority priority) {
  self->setPriority(priority);
}

//  int QNetworkRequest::maximumRedirectsAllowed() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QNetworkRequest23maximumRedirectsAllowedEv(
    const QNetworkRequest *self) {
  return self->maximumRedirectsAllowed();
}

//  void QNetworkRequest::setMaximumRedirectsAllowed(int
//      maximumRedirectsAllowed)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QNetworkRequest26setMaximumRedirectsAllowedEi(
    QNetworkRequest *self,
    int maximumRedirectsAllowed) {
  self->setMaximumRedirectsAllowed(maximumRedirectsAllowed);
}

//  QString QNetworkRequest::peerVerifyName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QNetworkRequest14peerVerifyNameEv(
    const QNetworkRequest *self) {
  return new QString(self->peerVerifyName());
}

//  void QNetworkRequest::setPeerVerifyName(const QString &peerName)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QNetworkRequest17setPeerVerifyNameERK7QString(
    QNetworkRequest *self,
    const QString *peerName) {
  self->setPeerVerifyName(*peerName);
}

#if QT_CONFIG(http)
//  QHttp1Configuration QNetworkRequest::http1Configuration() const
extern "C" Q_DECL_EXPORT
QHttp1Configuration *ritual_ZNK15QNetworkRequest18http1ConfigurationEv(
    const QNetworkRequest *self) {
  return new QHttp1Configuration(self->http1Configuration());
}
#endif  // QT_CONFIG(http)

#if QT_CONFIG(http)
//  void QNetworkRequest::setHttp1Configuration(const QHttp1Configuration
//      &configuration)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QNetworkRequest21setHttp1ConfigurationERK19QHttp1Configuration(
    QNetworkRequest *self,
    const QHttp1Configuration *configuration) {
  self->setHttp1Configuration(*configuration);
}
#endif  // QT_CONFIG(http)

#if QT_CONFIG(http)
//  QHttp2Configuration QNetworkRequest::http2Configuration() const
extern "C" Q_DECL_EXPORT
QHttp2Configuration *ritual_ZNK15QNetworkRequest18http2ConfigurationEv(
    const QNetworkRequest *self) {
  return new QHttp2Configuration(self->http2Configuration());
}
#endif  // QT_CONFIG(http)

#if QT_CONFIG(http)
//  void QNetworkRequest::setHttp2Configuration(const QHttp2Configuration
//      &configuration)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QNetworkRequest21setHttp2ConfigurationERK19QHttp2Configuration(
    QNetworkRequest *self,
    const QHttp2Configuration *configuration) {
  self->setHttp2Configuration(*configuration);
}
#endif  // QT_CONFIG(http)

#if QT_CONFIG(http)
//  qint64 QNetworkRequest::decompressedSafetyCheckThreshold() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK15QNetworkRequest32decompressedSafetyCheckThresholdEv(
    const QNetworkRequest *self) {
  return self->decompressedSafetyCheckThreshold();
}
#endif  // QT_CONFIG(http)

#if QT_CONFIG(http)
//  void QNetworkRequest::setDecompressedSafetyCheckThreshold(qint64
//      threshold)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QNetworkRequest35setDecompressedSafetyCheckThresholdEx(
    QNetworkRequest *self,
    qint64 threshold) {
  self->setDecompressedSafetyCheckThreshold(threshold);
}
#endif  // QT_CONFIG(http)

//  int QNetworkRequest::tcpKeepAliveProbeCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QNetworkRequest22tcpKeepAliveProbeCountEv(
    const QNetworkRequest *self) {
  return self->tcpKeepAliveProbeCount();
}

//  void QNetworkRequest::setTcpKeepAliveProbeCount(int probes)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QNetworkRequest25setTcpKeepAliveProbeCountEi(
    QNetworkRequest *self,
    int probes) {
  self->setTcpKeepAliveProbeCount(probes);
}

#if QT_CONFIG(http) || defined (Q_OS_WASM)
//  int QNetworkRequest::transferTimeout() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QNetworkRequest15transferTimeoutEv(
    const QNetworkRequest *self) {
  return self->transferTimeout();
}
#endif  // QT_CONFIG(http) || defined (Q_OS_WASM)

#if QT_CONFIG(http) || defined (Q_OS_WASM)
//  void QNetworkRequest::setTransferTimeout(int timeout)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QNetworkRequest18setTransferTimeoutEi(
    QNetworkRequest *self,
    int timeout) {
  self->setTransferTimeout(timeout);
}
#endif  // QT_CONFIG(http) || defined (Q_OS_WASM)
