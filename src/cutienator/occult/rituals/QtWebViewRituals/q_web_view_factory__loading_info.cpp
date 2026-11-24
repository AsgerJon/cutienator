//  Written by dev_tooling.RitualGenerator from the records of
//  QtWebView/6.12.0/QtWebView/private/qwebviewfactory_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtWebView/QtWebView>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWebView/6.12.0/QtWebView/private/qwebviewfactory_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qurl.h>
#include <QtCore/qstring.h>
#include <QtWebView/qwebviewloadinginfo.h>

//  QWebViewLoadingInfo QWebViewFactory::LoadingInfo::create(const QUrl &url,
//      QWebViewLoadingInfo::LoadStatus status, const QString &errorString)
extern "C" Q_DECL_EXPORT
QWebViewLoadingInfo *ritual_ZN15QWebViewFactory11LoadingInfo6createERK4QUrlN19QWebViewLoadingInfo10LoadStatusERK7QString(
    const QUrl *url,
    QWebViewLoadingInfo::LoadStatus status,
    const QString *errorString) {
  return new QWebViewLoadingInfo(
      QWebViewFactory::LoadingInfo::create(
          *url,
          status,
          *errorString));
}

//  QWebViewFactory::LoadingInfo::~LoadingInfo()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QWebViewFactory11LoadingInfoD1Ev(
    QWebViewFactory::LoadingInfo *self) {
  delete self;
}
