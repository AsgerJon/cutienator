//  Written by dev_tooling.RitualGenerator from the records of
//  QtHttpServer/qhttpserverconfiguration.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtHttpServer/qhttpserverconfiguration.h>

//  QHttpServerConfiguration::QHttpServerConfiguration()
extern "C" Q_DECL_EXPORT
QHttpServerConfiguration *ritual_ZN24QHttpServerConfigurationC1Ev() {
  return new QHttpServerConfiguration();
}

//  QHttpServerConfiguration::QHttpServerConfiguration(const
//      QHttpServerConfiguration &other)
extern "C" Q_DECL_EXPORT
QHttpServerConfiguration *ritual_ZN24QHttpServerConfigurationC1ERKS_(
    const QHttpServerConfiguration *other) {
  return new QHttpServerConfiguration(*other);
}

//  QHttpServerConfiguration::~QHttpServerConfiguration()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QHttpServerConfigurationD1Ev(
    QHttpServerConfiguration *self) {
  delete self;
}

//  void QHttpServerConfiguration::setRateLimitPerSecond(quint32 maxRequests)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QHttpServerConfiguration21setRateLimitPerSecondEj(
    QHttpServerConfiguration *self,
    quint32 maxRequests) {
  self->setRateLimitPerSecond(maxRequests);
}

//  quint32 QHttpServerConfiguration::rateLimitPerSecond() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK24QHttpServerConfiguration18rateLimitPerSecondEv(
    const QHttpServerConfiguration *self) {
  return self->rateLimitPerSecond();
}

//  void QHttpServerConfiguration::setMaximumConnectionsPerHost(quint32
//      maxPerHost)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QHttpServerConfiguration28setMaximumConnectionsPerHostEj(
    QHttpServerConfiguration *self,
    quint32 maxPerHost) {
  self->setMaximumConnectionsPerHost(maxPerHost);
}

//  quint32 QHttpServerConfiguration::maximumConnectionsPerHost() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK24QHttpServerConfiguration25maximumConnectionsPerHostEv(
    const QHttpServerConfiguration *self) {
  return self->maximumConnectionsPerHost();
}

//  void QHttpServerConfiguration::setMaximumConnections(quint32
//      maxConnections)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QHttpServerConfiguration21setMaximumConnectionsEj(
    QHttpServerConfiguration *self,
    quint32 maxConnections) {
  self->setMaximumConnections(maxConnections);
}

//  quint32 QHttpServerConfiguration::maximumConnections() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK24QHttpServerConfiguration18maximumConnectionsEv(
    const QHttpServerConfiguration *self) {
  return self->maximumConnections();
}

//  void QHttpServerConfiguration::setMaximumUrlSize(qint64 maxUrlSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QHttpServerConfiguration17setMaximumUrlSizeEx(
    QHttpServerConfiguration *self,
    qint64 maxUrlSize) {
  self->setMaximumUrlSize(maxUrlSize);
}

//  qint64 QHttpServerConfiguration::maximumUrlSize() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK24QHttpServerConfiguration14maximumUrlSizeEv(
    const QHttpServerConfiguration *self) {
  return self->maximumUrlSize();
}

//  void QHttpServerConfiguration::setMaximumTotalHeaderSize(qint64
//      maxTotalHeadersSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QHttpServerConfiguration25setMaximumTotalHeaderSizeEx(
    QHttpServerConfiguration *self,
    qint64 maxTotalHeadersSize) {
  self->setMaximumTotalHeaderSize(maxTotalHeadersSize);
}

//  qint64 QHttpServerConfiguration::maximumTotalHeaderSize() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK24QHttpServerConfiguration22maximumTotalHeaderSizeEv(
    const QHttpServerConfiguration *self) {
  return self->maximumTotalHeaderSize();
}

//  void QHttpServerConfiguration::setMaximumHeaderFieldSize(qint64
//      maxSingleHeaderSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QHttpServerConfiguration25setMaximumHeaderFieldSizeEx(
    QHttpServerConfiguration *self,
    qint64 maxSingleHeaderSize) {
  self->setMaximumHeaderFieldSize(maxSingleHeaderSize);
}

//  qint64 QHttpServerConfiguration::maximumHeaderFieldSize() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK24QHttpServerConfiguration22maximumHeaderFieldSizeEv(
    const QHttpServerConfiguration *self) {
  return self->maximumHeaderFieldSize();
}

//  void QHttpServerConfiguration::setMaximumHeaderFieldCount(qint64
//      maxNumberOfHeaders)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QHttpServerConfiguration26setMaximumHeaderFieldCountEx(
    QHttpServerConfiguration *self,
    qint64 maxNumberOfHeaders) {
  self->setMaximumHeaderFieldCount(maxNumberOfHeaders);
}

//  qint64 QHttpServerConfiguration::maximumHeaderFieldCount() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK24QHttpServerConfiguration23maximumHeaderFieldCountEv(
    const QHttpServerConfiguration *self) {
  return self->maximumHeaderFieldCount();
}

//  void QHttpServerConfiguration::setMaximumBodySize(qint64 maxBodySize)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QHttpServerConfiguration18setMaximumBodySizeEx(
    QHttpServerConfiguration *self,
    qint64 maxBodySize) {
  self->setMaximumBodySize(maxBodySize);
}

//  qint64 QHttpServerConfiguration::maximumBodySize() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK24QHttpServerConfiguration15maximumBodySizeEv(
    const QHttpServerConfiguration *self) {
  return self->maximumBodySize();
}

//  bool operator==(const QHttpServerConfiguration &lhs, const
//      QHttpServerConfiguration &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK24QHttpServerConfigurationS1_(
    const QHttpServerConfiguration *lhs,
    const QHttpServerConfiguration *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QHttpServerConfiguration &lhs, const
//      QHttpServerConfiguration &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK24QHttpServerConfigurationS1_(
    const QHttpServerConfiguration *lhs,
    const QHttpServerConfiguration *rhs) {
  return operator!=(*lhs, *rhs);
}
