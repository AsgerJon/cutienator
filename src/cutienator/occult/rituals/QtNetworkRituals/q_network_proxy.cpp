//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/qnetworkproxy.h, Qt 6.12.0. Changes made here are lost.
#include <QtNetwork/qtnetworkglobal.h>
#if !defined(QT_NO_NETWORKPROXY)
#include <QtNetwork/qnetworkproxy.h>
#include <QtCore/qstring.h>
#include <QtNetwork/qhttpheaders.h>
#include <QtCore/qvariant.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qlist.h>

//  QNetworkProxy::QNetworkProxy()
extern "C" Q_DECL_EXPORT
QNetworkProxy *ritual_ZN13QNetworkProxyC1Ev() {
  return new QNetworkProxy();
}

//  QNetworkProxy::QNetworkProxy(ProxyType type, const QString &hostName,
//      quint16 port, const QString &user, const QString &password)
extern "C" Q_DECL_EXPORT
QNetworkProxy *ritual_ZN13QNetworkProxyC1ENS_9ProxyTypeERK7QStringtS3_S3_(
    QNetworkProxy::ProxyType type,
    const QString *hostName,
    quint16 port,
    const QString *user,
    const QString *password) {
  return new QNetworkProxy(type, *hostName, port, *user, *password);
}

//  QNetworkProxy::QNetworkProxy(const QNetworkProxy &other)
extern "C" Q_DECL_EXPORT
QNetworkProxy *ritual_ZN13QNetworkProxyC1ERKS_(const QNetworkProxy *other) {
  return new QNetworkProxy(*other);
}

//  QNetworkProxy &QNetworkProxy::operator=(QNetworkProxy &&other)
extern "C" Q_DECL_EXPORT
QNetworkProxy *ritual_ZN13QNetworkProxyaSEOS_(
    QNetworkProxy *self,
    QNetworkProxy *other) {
  return &(self->operator=(std::move(*other)));
}

//  QNetworkProxy &QNetworkProxy::operator=(const QNetworkProxy &other)
extern "C" Q_DECL_EXPORT
QNetworkProxy *ritual_ZN13QNetworkProxyaSERKS_(
    QNetworkProxy *self,
    const QNetworkProxy *other) {
  return &(self->operator=(*other));
}

//  QNetworkProxy::~QNetworkProxy()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QNetworkProxyD1Ev(QNetworkProxy *self) {
  delete self;
}

//  void QNetworkProxy::swap(QNetworkProxy &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QNetworkProxy4swapERS_(
    QNetworkProxy *self,
    QNetworkProxy *other) {
  self->swap(*other);
}

//  bool QNetworkProxy::operator==(const QNetworkProxy &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QNetworkProxyeqERKS_(
    const QNetworkProxy *self,
    const QNetworkProxy *other) {
  return self->operator==(*other);
}

//  bool QNetworkProxy::operator!=(const QNetworkProxy &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QNetworkProxyneERKS_(
    const QNetworkProxy *self,
    const QNetworkProxy *other) {
  return self->operator!=(*other);
}

//  void QNetworkProxy::setType(QNetworkProxy::ProxyType type)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QNetworkProxy7setTypeENS_9ProxyTypeE(
    QNetworkProxy *self,
    QNetworkProxy::ProxyType type) {
  self->setType(type);
}

//  QNetworkProxy::ProxyType QNetworkProxy::type() const
extern "C" Q_DECL_EXPORT
QNetworkProxy::ProxyType ritual_ZNK13QNetworkProxy4typeEv(
    const QNetworkProxy *self) {
  return self->type();
}

//  void QNetworkProxy::setCapabilities(Capabilities capab)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QNetworkProxy15setCapabilitiesE6QFlagsINS_10CapabilityEE(
    QNetworkProxy *self,
    int capab) {
  self->setCapabilities(QFlags<QNetworkProxy::Capability>::fromInt(capab));
}

//  Capabilities QNetworkProxy::capabilities() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QNetworkProxy12capabilitiesEv(const QNetworkProxy *self) {
  return static_cast<int>(self->capabilities().toInt());
}

//  bool QNetworkProxy::isCachingProxy() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QNetworkProxy14isCachingProxyEv(const QNetworkProxy *self) {
  return self->isCachingProxy();
}

//  bool QNetworkProxy::isTransparentProxy() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QNetworkProxy18isTransparentProxyEv(
    const QNetworkProxy *self) {
  return self->isTransparentProxy();
}

//  void QNetworkProxy::setUser(const QString &userName)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QNetworkProxy7setUserERK7QString(
    QNetworkProxy *self,
    const QString *userName) {
  self->setUser(*userName);
}

//  QString QNetworkProxy::user() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13QNetworkProxy4userEv(const QNetworkProxy *self) {
  return new QString(self->user());
}

//  void QNetworkProxy::setPassword(const QString &password)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QNetworkProxy11setPasswordERK7QString(
    QNetworkProxy *self,
    const QString *password) {
  self->setPassword(*password);
}

//  QString QNetworkProxy::password() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13QNetworkProxy8passwordEv(const QNetworkProxy *self) {
  return new QString(self->password());
}

//  void QNetworkProxy::setHostName(const QString &hostName)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QNetworkProxy11setHostNameERK7QString(
    QNetworkProxy *self,
    const QString *hostName) {
  self->setHostName(*hostName);
}

//  QString QNetworkProxy::hostName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13QNetworkProxy8hostNameEv(const QNetworkProxy *self) {
  return new QString(self->hostName());
}

//  void QNetworkProxy::setPort(quint16 port)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QNetworkProxy7setPortEt(QNetworkProxy *self, quint16 port) {
  self->setPort(port);
}

//  quint16 QNetworkProxy::port() const
extern "C" Q_DECL_EXPORT
quint16 ritual_ZNK13QNetworkProxy4portEv(const QNetworkProxy *self) {
  return self->port();
}

//  void QNetworkProxy::setApplicationProxy(const QNetworkProxy &proxy)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QNetworkProxy19setApplicationProxyERKS_(
    const QNetworkProxy *proxy) {
  QNetworkProxy::setApplicationProxy(*proxy);
}

//  QNetworkProxy QNetworkProxy::applicationProxy()
extern "C" Q_DECL_EXPORT
QNetworkProxy *ritual_ZN13QNetworkProxy16applicationProxyEv() {
  return new QNetworkProxy(QNetworkProxy::applicationProxy());
}

//  QHttpHeaders QNetworkProxy::headers() const
extern "C" Q_DECL_EXPORT
QHttpHeaders *ritual_ZNK13QNetworkProxy7headersEv(
    const QNetworkProxy *self) {
  return new QHttpHeaders(self->headers());
}

//  void QNetworkProxy::setHeaders(const QHttpHeaders &newHeaders)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QNetworkProxy10setHeadersERK12QHttpHeaders(
    QNetworkProxy *self,
    const QHttpHeaders *newHeaders) {
  self->setHeaders(*newHeaders);
}

//  void QNetworkProxy::setHeaders(QHttpHeaders &&newHeaders)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QNetworkProxy10setHeadersEO12QHttpHeaders(
    QNetworkProxy *self,
    QHttpHeaders *newHeaders) {
  self->setHeaders(std::move(*newHeaders));
}

//  QVariant QNetworkProxy::header(QNetworkRequest::KnownHeaders header)
//      const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK13QNetworkProxy6headerEN15QNetworkRequest12KnownHeadersE(
    const QNetworkProxy *self,
    QNetworkRequest::KnownHeaders header) {
  return new QVariant(self->header(header));
}

//  void QNetworkProxy::setHeader(QNetworkRequest::KnownHeaders header, const
//      QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QNetworkProxy9setHeaderEN15QNetworkRequest12KnownHeadersERK8QVariant(
    QNetworkProxy *self,
    QNetworkRequest::KnownHeaders header,
    const QVariant *value) {
  self->setHeader(header, *value);
}

//  bool QNetworkProxy::hasRawHeader(const QByteArray &headerName) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QNetworkProxy12hasRawHeaderERK10QByteArray(
    const QNetworkProxy *self,
    const QByteArray *headerName) {
  return self->hasRawHeader(*headerName);
}

//  QList<QByteArray> QNetworkProxy::rawHeaderList() const
extern "C" Q_DECL_EXPORT
QList<QByteArray> *ritual_ZNK13QNetworkProxy13rawHeaderListEv(
    const QNetworkProxy *self) {
  return new QList<QByteArray>(self->rawHeaderList());
}

//  QByteArray QNetworkProxy::rawHeader(const QByteArray &headerName) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK13QNetworkProxy9rawHeaderERK10QByteArray(
    const QNetworkProxy *self,
    const QByteArray *headerName) {
  return new QByteArray(self->rawHeader(*headerName));
}

//  void QNetworkProxy::setRawHeader(const QByteArray &headerName, const
//      QByteArray &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QNetworkProxy12setRawHeaderERK10QByteArrayS2_(
    QNetworkProxy *self,
    const QByteArray *headerName,
    const QByteArray *value) {
  self->setRawHeader(*headerName, *value);
}

//  QList<QNetworkProxy>::QList()
extern "C" Q_DECL_EXPORT
QList<QNetworkProxy> *ritual_list_make_QNetworkProxy() {
  return new QList<QNetworkProxy>();
}

//  void QList<QNetworkProxy>::append(const QNetworkProxy &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QNetworkProxy(
    QList<QNetworkProxy> *self,
    const QNetworkProxy *element) {
  self->append(*element);
}

//  qsizetype QList<QNetworkProxy>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QNetworkProxy(const QList<QNetworkProxy> *self) {
  return self->size();
}

//  const QNetworkProxy &QList<QNetworkProxy>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QNetworkProxy *ritual_list_at_QNetworkProxy(
    const QList<QNetworkProxy> *self,
    long long index) {
  return new QNetworkProxy(self->at(index));
}

//  QList<QNetworkProxy>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QNetworkProxy(QList<QNetworkProxy> *self) {
  delete self;
}

#endif  // !defined(QT_NO_NETWORKPROXY)
