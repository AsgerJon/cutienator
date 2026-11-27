//  Written by dev_tooling.RitualGenerator from the records of
//  QtWebEngineCore/qwebengineloadinginfo.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtWebEngineCore/qwebengineloadinginfo.h>
#include <QtCore/qurl.h>
#include <QtCore/qstring.h>
#include <QtCore/QMultiMap>
#include <QtCore/QByteArray>

//  QWebEngineLoadingInfo::QWebEngineLoadingInfo()
extern "C" Q_DECL_EXPORT
QWebEngineLoadingInfo *ritual_ZN21QWebEngineLoadingInfoC1Ev() {
  return new QWebEngineLoadingInfo();
}

//  QWebEngineLoadingInfo::QWebEngineLoadingInfo(const QWebEngineLoadingInfo
//      &other)
extern "C" Q_DECL_EXPORT
QWebEngineLoadingInfo *ritual_ZN21QWebEngineLoadingInfoC1ERKS_(
    const QWebEngineLoadingInfo *other) {
  return new QWebEngineLoadingInfo(*other);
}

//  QWebEngineLoadingInfo &QWebEngineLoadingInfo::operator=(const
//      QWebEngineLoadingInfo &other)
extern "C" Q_DECL_EXPORT
QWebEngineLoadingInfo *ritual_ZN21QWebEngineLoadingInfoaSERKS_(
    QWebEngineLoadingInfo *self,
    const QWebEngineLoadingInfo *other) {
  return &(self->operator=(*other));
}

//  QWebEngineLoadingInfo::QWebEngineLoadingInfo(QWebEngineLoadingInfo
//      &&other)
extern "C" Q_DECL_EXPORT
QWebEngineLoadingInfo *ritual_ZN21QWebEngineLoadingInfoC1EOS_(
    QWebEngineLoadingInfo *other) {
  return new QWebEngineLoadingInfo(std::move(*other));
}

//  QWebEngineLoadingInfo
//      &QWebEngineLoadingInfo::operator=(QWebEngineLoadingInfo &&other)
extern "C" Q_DECL_EXPORT
QWebEngineLoadingInfo *ritual_ZN21QWebEngineLoadingInfoaSEOS_(
    QWebEngineLoadingInfo *self,
    QWebEngineLoadingInfo *other) {
  return &(self->operator=(std::move(*other)));
}

//  QWebEngineLoadingInfo::~QWebEngineLoadingInfo()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QWebEngineLoadingInfoD1Ev(QWebEngineLoadingInfo *self) {
  delete self;
}

//  QUrl QWebEngineLoadingInfo::url() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK21QWebEngineLoadingInfo3urlEv(
    const QWebEngineLoadingInfo *self) {
  return new QUrl(self->url());
}

//  bool QWebEngineLoadingInfo::isErrorPage() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QWebEngineLoadingInfo11isErrorPageEv(
    const QWebEngineLoadingInfo *self) {
  return self->isErrorPage();
}

//  LoadStatus QWebEngineLoadingInfo::status() const
extern "C" Q_DECL_EXPORT
QWebEngineLoadingInfo::LoadStatus ritual_ZNK21QWebEngineLoadingInfo6statusEv(
    const QWebEngineLoadingInfo *self) {
  return self->status();
}

//  QString QWebEngineLoadingInfo::errorString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK21QWebEngineLoadingInfo11errorStringEv(
    const QWebEngineLoadingInfo *self) {
  return new QString(self->errorString());
}

//  ErrorDomain QWebEngineLoadingInfo::errorDomain() const
extern "C" Q_DECL_EXPORT
QWebEngineLoadingInfo::ErrorDomain ritual_ZNK21QWebEngineLoadingInfo11errorDomainEv(
    const QWebEngineLoadingInfo *self) {
  return self->errorDomain();
}

//  int QWebEngineLoadingInfo::errorCode() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QWebEngineLoadingInfo9errorCodeEv(
    const QWebEngineLoadingInfo *self) {
  return self->errorCode();
}

//  QMultiMap<QByteArray, QByteArray>
//      QWebEngineLoadingInfo::responseHeaders() const
extern "C" Q_DECL_EXPORT
QMultiMap<QByteArray, QByteArray> *ritual_ZNK21QWebEngineLoadingInfo15responseHeadersEv(
    const QWebEngineLoadingInfo *self) {
  return new QMultiMap<QByteArray, QByteArray>(self->responseHeaders());
}

//  bool QWebEngineLoadingInfo::isDownload() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QWebEngineLoadingInfo10isDownloadEv(
    const QWebEngineLoadingInfo *self) {
  return self->isDownload();
}

//  QWebEngineLoadingInfo::QWebEngineLoadingInfo(const QUrl &url, LoadStatus
//      status, bool isErrorPage, const QString &errorString, int errorCode,
//      ErrorDomain errorDomain, const QMultiMap<QByteArray, QByteArray>
//      &responseHeaders, bool isDownload)
extern "C" Q_DECL_EXPORT
QWebEngineLoadingInfo *ritual_ZN21QWebEngineLoadingInfoC1ERK4QUrlNS_10LoadStatusEbRK7QStringiNS_11ErrorDomainERK9QMultiMapI10QByteArrayS9_Eb(
    const QUrl *url,
    QWebEngineLoadingInfo::LoadStatus status,
    bool isErrorPage,
    const QString *errorString,
    int errorCode,
    QWebEngineLoadingInfo::ErrorDomain errorDomain,
    const QMultiMap<QByteArray, QByteArray> *responseHeaders,
    bool isDownload) {
  return new QWebEngineLoadingInfo(
      *url,
      status,
      isErrorPage,
      *errorString,
      errorCode,
      errorDomain,
      *responseHeaders,
      isDownload);
}

//  a QMultiMap<QByteArray, QByteArray> a ritual of QWebEngineLoadingInfo
//      gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QWebEngineLoadingInfo__QMultiMap_QByteArray_QByteArray(
    QMultiMap<QByteArray, QByteArray> *self) {
  delete self;
}
