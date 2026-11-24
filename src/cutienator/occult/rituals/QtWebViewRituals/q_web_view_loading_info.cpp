//  Written by dev_tooling.RitualGenerator from the records of
//  QtWebView/qwebviewloadinginfo.h, Qt 6.12.0. Changes made here are lost.
#include <QtWebView/qwebviewloadinginfo.h>
#include <QtCore/qurl.h>
#include <QtCore/qstring.h>
#include <QtCore/qdebug.h>

//  QWebViewLoadingInfo::QWebViewLoadingInfo()
extern "C" Q_DECL_EXPORT
QWebViewLoadingInfo *ritual_ZN19QWebViewLoadingInfoC1Ev() {
  return new QWebViewLoadingInfo();
}

//  QWebViewLoadingInfo::QWebViewLoadingInfo(const QWebViewLoadingInfo
//      &other)
extern "C" Q_DECL_EXPORT
QWebViewLoadingInfo *ritual_ZN19QWebViewLoadingInfoC1ERKS_(
    const QWebViewLoadingInfo *other) {
  return new QWebViewLoadingInfo(*other);
}

//  QWebViewLoadingInfo::~QWebViewLoadingInfo()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QWebViewLoadingInfoD1Ev(QWebViewLoadingInfo *self) {
  delete self;
}

//  QUrl QWebViewLoadingInfo::url() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK19QWebViewLoadingInfo3urlEv(
    const QWebViewLoadingInfo *self) {
  return new QUrl(self->url());
}

//  LoadStatus QWebViewLoadingInfo::status() const
extern "C" Q_DECL_EXPORT
QWebViewLoadingInfo::LoadStatus ritual_ZNK19QWebViewLoadingInfo6statusEv(
    const QWebViewLoadingInfo *self) {
  return self->status();
}

//  QString QWebViewLoadingInfo::errorString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QWebViewLoadingInfo11errorStringEv(
    const QWebViewLoadingInfo *self) {
  return new QString(self->errorString());
}

#if !defined(QT_NO_DEBUG_STREAM)
//  QDebug operator<<(QDebug ds, const QWebViewLoadingInfo &info)
extern "C" Q_DECL_EXPORT
QDebug *ritual_Zls6QDebugRK19QWebViewLoadingInfo(
    const QDebug *ds,
    const QWebViewLoadingInfo *info) {
  return new QDebug(operator<<(*ds, *info));
}
#endif  // !defined(QT_NO_DEBUG_STREAM)

//  QWebViewLoadingInfo::QWebViewLoadingInfo(const QUrl &url, LoadStatus
//      status, const QString &errorString)
extern "C" Q_DECL_EXPORT
QWebViewLoadingInfo *ritual_ZN19QWebViewLoadingInfoC1ERK4QUrlNS_10LoadStatusERK7QString(
    const QUrl *url,
    QWebViewLoadingInfo::LoadStatus status,
    const QString *errorString) {
  return new QWebViewLoadingInfo(*url, status, *errorString);
}
