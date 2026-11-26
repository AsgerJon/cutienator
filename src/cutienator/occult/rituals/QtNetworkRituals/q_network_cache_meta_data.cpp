//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/qabstractnetworkcache.h, Qt 6.12.0. Changes made here are lost.
#include <QtNetwork/qabstractnetworkcache.h>
#include <QtCore/qurl.h>
#include <QtNetwork/qhttpheaders.h>
#include <QtCore/qdatetime.h>
#include <QtNetwork/QNetworkCacheMetaData>

//  QNetworkCacheMetaData::QNetworkCacheMetaData()
extern "C" Q_DECL_EXPORT
QNetworkCacheMetaData *ritual_ZN21QNetworkCacheMetaDataC1Ev() {
  return new QNetworkCacheMetaData();
}

//  QNetworkCacheMetaData::QNetworkCacheMetaData(const QNetworkCacheMetaData
//      &other)
extern "C" Q_DECL_EXPORT
QNetworkCacheMetaData *ritual_ZN21QNetworkCacheMetaDataC1ERKS_(
    const QNetworkCacheMetaData *other) {
  return new QNetworkCacheMetaData(*other);
}

//  QNetworkCacheMetaData::~QNetworkCacheMetaData()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QNetworkCacheMetaDataD1Ev(QNetworkCacheMetaData *self) {
  delete self;
}

//  QNetworkCacheMetaData
//      &QNetworkCacheMetaData::operator=(QNetworkCacheMetaData &&other)
extern "C" Q_DECL_EXPORT
QNetworkCacheMetaData *ritual_ZN21QNetworkCacheMetaDataaSEOS_(
    QNetworkCacheMetaData *self,
    QNetworkCacheMetaData *other) {
  return &(self->operator=(std::move(*other)));
}

//  QNetworkCacheMetaData &QNetworkCacheMetaData::operator=(const
//      QNetworkCacheMetaData &other)
extern "C" Q_DECL_EXPORT
QNetworkCacheMetaData *ritual_ZN21QNetworkCacheMetaDataaSERKS_(
    QNetworkCacheMetaData *self,
    const QNetworkCacheMetaData *other) {
  return &(self->operator=(*other));
}

//  void QNetworkCacheMetaData::swap(QNetworkCacheMetaData &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QNetworkCacheMetaData4swapERS_(
    QNetworkCacheMetaData *self,
    QNetworkCacheMetaData *other) {
  self->swap(*other);
}

//  bool QNetworkCacheMetaData::operator==(const QNetworkCacheMetaData
//      &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QNetworkCacheMetaDataeqERKS_(
    const QNetworkCacheMetaData *self,
    const QNetworkCacheMetaData *other) {
  return self->operator==(*other);
}

//  bool QNetworkCacheMetaData::operator!=(const QNetworkCacheMetaData
//      &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QNetworkCacheMetaDataneERKS_(
    const QNetworkCacheMetaData *self,
    const QNetworkCacheMetaData *other) {
  return self->operator!=(*other);
}

//  bool QNetworkCacheMetaData::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QNetworkCacheMetaData7isValidEv(
    const QNetworkCacheMetaData *self) {
  return self->isValid();
}

//  QUrl QNetworkCacheMetaData::url() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK21QNetworkCacheMetaData3urlEv(
    const QNetworkCacheMetaData *self) {
  return new QUrl(self->url());
}

//  void QNetworkCacheMetaData::setUrl(const QUrl &url)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QNetworkCacheMetaData6setUrlERK4QUrl(
    QNetworkCacheMetaData *self,
    const QUrl *url) {
  self->setUrl(*url);
}

//  RawHeaderList QNetworkCacheMetaData::rawHeaders() const
extern "C" Q_DECL_EXPORT
QNetworkCacheMetaData::RawHeaderList *ritual_ZNK21QNetworkCacheMetaData10rawHeadersEv(
    const QNetworkCacheMetaData *self) {
  return new QNetworkCacheMetaData::RawHeaderList(self->rawHeaders());
}

//  void QNetworkCacheMetaData::setRawHeaders(const RawHeaderList &headers)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QNetworkCacheMetaData13setRawHeadersERK5QListISt4pairI10QByteArrayS2_EE(
    QNetworkCacheMetaData *self,
    const QNetworkCacheMetaData::RawHeaderList *headers) {
  self->setRawHeaders(*headers);
}

//  QHttpHeaders QNetworkCacheMetaData::headers() const
extern "C" Q_DECL_EXPORT
QHttpHeaders *ritual_ZNK21QNetworkCacheMetaData7headersEv(
    const QNetworkCacheMetaData *self) {
  return new QHttpHeaders(self->headers());
}

//  void QNetworkCacheMetaData::setHeaders(const QHttpHeaders &headers)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QNetworkCacheMetaData10setHeadersERK12QHttpHeaders(
    QNetworkCacheMetaData *self,
    const QHttpHeaders *headers) {
  self->setHeaders(*headers);
}

//  QDateTime QNetworkCacheMetaData::lastModified() const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK21QNetworkCacheMetaData12lastModifiedEv(
    const QNetworkCacheMetaData *self) {
  return new QDateTime(self->lastModified());
}

//  void QNetworkCacheMetaData::setLastModified(const QDateTime &dateTime)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QNetworkCacheMetaData15setLastModifiedERK9QDateTime(
    QNetworkCacheMetaData *self,
    const QDateTime *dateTime) {
  self->setLastModified(*dateTime);
}

//  QDateTime QNetworkCacheMetaData::expirationDate() const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK21QNetworkCacheMetaData14expirationDateEv(
    const QNetworkCacheMetaData *self) {
  return new QDateTime(self->expirationDate());
}

//  void QNetworkCacheMetaData::setExpirationDate(const QDateTime &dateTime)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QNetworkCacheMetaData17setExpirationDateERK9QDateTime(
    QNetworkCacheMetaData *self,
    const QDateTime *dateTime) {
  self->setExpirationDate(*dateTime);
}

//  bool QNetworkCacheMetaData::saveToDisk() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QNetworkCacheMetaData10saveToDiskEv(
    const QNetworkCacheMetaData *self) {
  return self->saveToDisk();
}

//  void QNetworkCacheMetaData::setSaveToDisk(bool allow)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QNetworkCacheMetaData13setSaveToDiskEb(
    QNetworkCacheMetaData *self,
    bool allow) {
  self->setSaveToDisk(allow);
}

//  AttributesMap QNetworkCacheMetaData::attributes() const
extern "C" Q_DECL_EXPORT
QNetworkCacheMetaData::AttributesMap *ritual_ZNK21QNetworkCacheMetaData10attributesEv(
    const QNetworkCacheMetaData *self) {
  return new QNetworkCacheMetaData::AttributesMap(self->attributes());
}

//  void QNetworkCacheMetaData::setAttributes(const AttributesMap
//      &attributes)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QNetworkCacheMetaData13setAttributesERK5QHashIN15QNetworkRequest9AttributeE8QVariantE(
    QNetworkCacheMetaData *self,
    const QNetworkCacheMetaData::AttributesMap *attributes) {
  self->setAttributes(*attributes);
}

//  a QNetworkCacheMetaData::RawHeaderList a ritual of QNetworkCacheMetaData
//      gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QNetworkCacheMetaData__QNetworkCacheMetaData_RawHeaderList(
    QNetworkCacheMetaData::RawHeaderList *self) {
  delete self;
}

//  a QNetworkCacheMetaData::AttributesMap a ritual of QNetworkCacheMetaData
//      gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QNetworkCacheMetaData__QNetworkCacheMetaData_AttributesMap(
    QNetworkCacheMetaData::AttributesMap *self) {
  delete self;
}
