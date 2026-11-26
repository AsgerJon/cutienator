//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/qnetworkproxy.h, Qt 6.12.0. Changes made here are lost.
#include <QtNetwork/qtnetworkglobal.h>
#if !defined(QT_NO_NETWORKPROXY)
#include <QtNetwork/qnetworkproxy.h>
#include <QtCore/qurl.h>
#include <QtCore/qstring.h>

//  QNetworkProxyQuery::QNetworkProxyQuery()
extern "C" Q_DECL_EXPORT
QNetworkProxyQuery *ritual_ZN18QNetworkProxyQueryC1Ev() {
  return new QNetworkProxyQuery();
}

//  QNetworkProxyQuery::QNetworkProxyQuery(const QUrl &requestUrl, QueryType
//      queryType)
extern "C" Q_DECL_EXPORT
QNetworkProxyQuery *ritual_ZN18QNetworkProxyQueryC1ERK4QUrlNS_9QueryTypeE(
    const QUrl *requestUrl,
    QNetworkProxyQuery::QueryType queryType) {
  return new QNetworkProxyQuery(*requestUrl, queryType);
}

//  QNetworkProxyQuery::QNetworkProxyQuery(const QString &hostname, int port,
//      const QString &protocolTag, QueryType queryType)
extern "C" Q_DECL_EXPORT
QNetworkProxyQuery *ritual_ZN18QNetworkProxyQueryC1ERK7QStringiS2_NS_9QueryTypeE(
    const QString *hostname,
    int port,
    const QString *protocolTag,
    QNetworkProxyQuery::QueryType queryType) {
  return new QNetworkProxyQuery(*hostname, port, *protocolTag, queryType);
}

//  QNetworkProxyQuery::QNetworkProxyQuery(quint16 bindPort, const QString
//      &protocolTag, QueryType queryType)
extern "C" Q_DECL_EXPORT
QNetworkProxyQuery *ritual_ZN18QNetworkProxyQueryC1EtRK7QStringNS_9QueryTypeE(
    quint16 bindPort,
    const QString *protocolTag,
    QNetworkProxyQuery::QueryType queryType) {
  return new QNetworkProxyQuery(bindPort, *protocolTag, queryType);
}

//  QNetworkProxyQuery::QNetworkProxyQuery(const QNetworkProxyQuery &other)
extern "C" Q_DECL_EXPORT
QNetworkProxyQuery *ritual_ZN18QNetworkProxyQueryC1ERKS_(
    const QNetworkProxyQuery *other) {
  return new QNetworkProxyQuery(*other);
}

//  QNetworkProxyQuery &QNetworkProxyQuery::operator=(QNetworkProxyQuery
//      &&other)
extern "C" Q_DECL_EXPORT
QNetworkProxyQuery *ritual_ZN18QNetworkProxyQueryaSEOS_(
    QNetworkProxyQuery *self,
    QNetworkProxyQuery *other) {
  return &(self->operator=(std::move(*other)));
}

//  QNetworkProxyQuery &QNetworkProxyQuery::operator=(const
//      QNetworkProxyQuery &other)
extern "C" Q_DECL_EXPORT
QNetworkProxyQuery *ritual_ZN18QNetworkProxyQueryaSERKS_(
    QNetworkProxyQuery *self,
    const QNetworkProxyQuery *other) {
  return &(self->operator=(*other));
}

//  QNetworkProxyQuery::~QNetworkProxyQuery()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QNetworkProxyQueryD1Ev(QNetworkProxyQuery *self) {
  delete self;
}

//  void QNetworkProxyQuery::swap(QNetworkProxyQuery &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QNetworkProxyQuery4swapERS_(
    QNetworkProxyQuery *self,
    QNetworkProxyQuery *other) {
  self->swap(*other);
}

//  bool QNetworkProxyQuery::operator==(const QNetworkProxyQuery &other)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QNetworkProxyQueryeqERKS_(
    const QNetworkProxyQuery *self,
    const QNetworkProxyQuery *other) {
  return self->operator==(*other);
}

//  bool QNetworkProxyQuery::operator!=(const QNetworkProxyQuery &other)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QNetworkProxyQueryneERKS_(
    const QNetworkProxyQuery *self,
    const QNetworkProxyQuery *other) {
  return self->operator!=(*other);
}

//  QueryType QNetworkProxyQuery::queryType() const
extern "C" Q_DECL_EXPORT
QNetworkProxyQuery::QueryType ritual_ZNK18QNetworkProxyQuery9queryTypeEv(
    const QNetworkProxyQuery *self) {
  return self->queryType();
}

//  void QNetworkProxyQuery::setQueryType(QueryType type)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QNetworkProxyQuery12setQueryTypeENS_9QueryTypeE(
    QNetworkProxyQuery *self,
    QNetworkProxyQuery::QueryType type) {
  self->setQueryType(type);
}

//  int QNetworkProxyQuery::peerPort() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QNetworkProxyQuery8peerPortEv(
    const QNetworkProxyQuery *self) {
  return self->peerPort();
}

//  void QNetworkProxyQuery::setPeerPort(int port)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QNetworkProxyQuery11setPeerPortEi(
    QNetworkProxyQuery *self,
    int port) {
  self->setPeerPort(port);
}

//  QString QNetworkProxyQuery::peerHostName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QNetworkProxyQuery12peerHostNameEv(
    const QNetworkProxyQuery *self) {
  return new QString(self->peerHostName());
}

//  void QNetworkProxyQuery::setPeerHostName(const QString &hostname)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QNetworkProxyQuery15setPeerHostNameERK7QString(
    QNetworkProxyQuery *self,
    const QString *hostname) {
  self->setPeerHostName(*hostname);
}

//  int QNetworkProxyQuery::localPort() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QNetworkProxyQuery9localPortEv(
    const QNetworkProxyQuery *self) {
  return self->localPort();
}

//  void QNetworkProxyQuery::setLocalPort(int port)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QNetworkProxyQuery12setLocalPortEi(
    QNetworkProxyQuery *self,
    int port) {
  self->setLocalPort(port);
}

//  QString QNetworkProxyQuery::protocolTag() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QNetworkProxyQuery11protocolTagEv(
    const QNetworkProxyQuery *self) {
  return new QString(self->protocolTag());
}

//  void QNetworkProxyQuery::setProtocolTag(const QString &protocolTag)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QNetworkProxyQuery14setProtocolTagERK7QString(
    QNetworkProxyQuery *self,
    const QString *protocolTag) {
  self->setProtocolTag(*protocolTag);
}

//  QUrl QNetworkProxyQuery::url() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK18QNetworkProxyQuery3urlEv(const QNetworkProxyQuery *self) {
  return new QUrl(self->url());
}

//  void QNetworkProxyQuery::setUrl(const QUrl &url)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QNetworkProxyQuery6setUrlERK4QUrl(
    QNetworkProxyQuery *self,
    const QUrl *url) {
  self->setUrl(*url);
}

#endif  // !defined(QT_NO_NETWORKPROXY)
