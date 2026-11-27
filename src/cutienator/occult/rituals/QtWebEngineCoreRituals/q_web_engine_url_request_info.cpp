//  Written by dev_tooling.RitualGenerator from the records of
//  QtWebEngineCore/qwebengineurlrequestinfo.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtWebEngineCore/qwebengineurlrequestinfo.h>
#include <QtCore/qurl.h>
#include <QtCore/qbytearray.h>
#include <QtCore/QHash>
#include <QtCore/QByteArray>

//  ResourceType QWebEngineUrlRequestInfo::resourceType() const
extern "C" Q_DECL_EXPORT
QWebEngineUrlRequestInfo::ResourceType ritual_ZNK24QWebEngineUrlRequestInfo12resourceTypeEv(
    const QWebEngineUrlRequestInfo *self) {
  return self->resourceType();
}

//  NavigationType QWebEngineUrlRequestInfo::navigationType() const
extern "C" Q_DECL_EXPORT
QWebEngineUrlRequestInfo::NavigationType ritual_ZNK24QWebEngineUrlRequestInfo14navigationTypeEv(
    const QWebEngineUrlRequestInfo *self) {
  return self->navigationType();
}

//  QUrl QWebEngineUrlRequestInfo::requestUrl() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK24QWebEngineUrlRequestInfo10requestUrlEv(
    const QWebEngineUrlRequestInfo *self) {
  return new QUrl(self->requestUrl());
}

//  QUrl QWebEngineUrlRequestInfo::firstPartyUrl() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK24QWebEngineUrlRequestInfo13firstPartyUrlEv(
    const QWebEngineUrlRequestInfo *self) {
  return new QUrl(self->firstPartyUrl());
}

//  QUrl QWebEngineUrlRequestInfo::initiator() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK24QWebEngineUrlRequestInfo9initiatorEv(
    const QWebEngineUrlRequestInfo *self) {
  return new QUrl(self->initiator());
}

//  QByteArray QWebEngineUrlRequestInfo::requestMethod() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK24QWebEngineUrlRequestInfo13requestMethodEv(
    const QWebEngineUrlRequestInfo *self) {
  return new QByteArray(self->requestMethod());
}

//  QIODevice *QWebEngineUrlRequestInfo::requestBody() const
extern "C" Q_DECL_EXPORT
QIODevice *ritual_ZNK24QWebEngineUrlRequestInfo11requestBodyEv(
    const QWebEngineUrlRequestInfo *self) {
  return self->requestBody();
}

//  bool QWebEngineUrlRequestInfo::changed() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QWebEngineUrlRequestInfo7changedEv(
    const QWebEngineUrlRequestInfo *self) {
  return self->changed();
}

//  bool QWebEngineUrlRequestInfo::isDownload() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QWebEngineUrlRequestInfo10isDownloadEv(
    const QWebEngineUrlRequestInfo *self) {
  return self->isDownload();
}

//  void QWebEngineUrlRequestInfo::block(bool shouldBlock)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QWebEngineUrlRequestInfo5blockEb(
    QWebEngineUrlRequestInfo *self,
    bool shouldBlock) {
  self->block(shouldBlock);
}

//  void QWebEngineUrlRequestInfo::redirect(const QUrl &url)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QWebEngineUrlRequestInfo8redirectERK4QUrl(
    QWebEngineUrlRequestInfo *self,
    const QUrl *url) {
  self->redirect(*url);
}

//  void QWebEngineUrlRequestInfo::setHttpHeader(const QByteArray &name,
//      const QByteArray &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QWebEngineUrlRequestInfo13setHttpHeaderERK10QByteArrayS2_(
    QWebEngineUrlRequestInfo *self,
    const QByteArray *name,
    const QByteArray *value) {
  self->setHttpHeader(*name, *value);
}

//  QHash<QByteArray, QByteArray> QWebEngineUrlRequestInfo::httpHeaders()
//      const
extern "C" Q_DECL_EXPORT
QHash<QByteArray, QByteArray> *ritual_ZNK24QWebEngineUrlRequestInfo11httpHeadersEv(
    const QWebEngineUrlRequestInfo *self) {
  return new QHash<QByteArray, QByteArray>(self->httpHeaders());
}

//  QWebEngineUrlRequestInfoPrivate *QWebEngineUrlRequestInfo::d_func()
extern "C" Q_DECL_EXPORT
QWebEngineUrlRequestInfoPrivate *ritual_ZN24QWebEngineUrlRequestInfo6d_funcEv(
    QWebEngineUrlRequestInfo *self) {
  return self->d_func();
}

//  const QWebEngineUrlRequestInfoPrivate *QWebEngineUrlRequestInfo::d_func()
//      const
extern "C" Q_DECL_EXPORT
const QWebEngineUrlRequestInfoPrivate *ritual_ZNK24QWebEngineUrlRequestInfo6d_funcEv(
    const QWebEngineUrlRequestInfo *self) {
  return self->d_func();
}

//  void QWebEngineUrlRequestInfo::resetChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QWebEngineUrlRequestInfo12resetChangedEv(
    QWebEngineUrlRequestInfo *self) {
  self->resetChanged();
}

//  QWebEngineUrlRequestInfo::QWebEngineUrlRequestInfo()
extern "C" Q_DECL_EXPORT
QWebEngineUrlRequestInfo *ritual_ZN24QWebEngineUrlRequestInfoC1Ev() {
  return new QWebEngineUrlRequestInfo();
}

//  QWebEngineUrlRequestInfo::QWebEngineUrlRequestInfo(QWebEngineUrlRequestIn
//      foPrivate *p)
extern "C" Q_DECL_EXPORT
QWebEngineUrlRequestInfo *ritual_ZN24QWebEngineUrlRequestInfoC1EP31QWebEngineUrlRequestInfoPrivate(
    QWebEngineUrlRequestInfoPrivate *p) {
  return new QWebEngineUrlRequestInfo(p);
}

//  QWebEngineUrlRequestInfo::QWebEngineUrlRequestInfo(QWebEngineUrlRequestIn
//      fo &&p)
extern "C" Q_DECL_EXPORT
QWebEngineUrlRequestInfo *ritual_ZN24QWebEngineUrlRequestInfoC1EOS_(
    QWebEngineUrlRequestInfo *p) {
  return new QWebEngineUrlRequestInfo(std::move(*p));
}

//  QWebEngineUrlRequestInfo
//      &QWebEngineUrlRequestInfo::operator=(QWebEngineUrlRequestInfo &&p)
extern "C" Q_DECL_EXPORT
QWebEngineUrlRequestInfo *ritual_ZN24QWebEngineUrlRequestInfoaSEOS_(
    QWebEngineUrlRequestInfo *self,
    QWebEngineUrlRequestInfo *p) {
  return &(self->operator=(std::move(*p)));
}

//  QWebEngineUrlRequestInfo::~QWebEngineUrlRequestInfo()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QWebEngineUrlRequestInfoD1Ev(
    QWebEngineUrlRequestInfo *self) {
  delete self;
}

//  a QHash<QByteArray, QByteArray> a ritual of QWebEngineUrlRequestInfo gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QWebEngineUrlRequestInfo__QHash_QByteArray_QByteArray(
    QHash<QByteArray, QByteArray> *self) {
  delete self;
}
