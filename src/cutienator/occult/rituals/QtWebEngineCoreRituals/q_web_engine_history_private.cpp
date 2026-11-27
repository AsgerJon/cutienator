//  Written by dev_tooling.RitualGenerator from the records of
//  QtWebEngineCore/6.12.0/QtWebEngineCore/private/qwebenginehistory_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtWebEngineCore/6.12.0/QtWebEngineCore/private/qtwebenginecoreglobal_p.h>
#include <QtWebEngineCore/QtWebEngineCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWebEngineCore/6.12.0/QtWebEngineCore/private/qwebenginehistory_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qurl.h>

//  QWebEngineHistoryPrivate::QWebEngineHistoryPrivate(QtWebEngineCore::WebCo
//      ntentsAdapterClient *client, const ImageProviderUrl
//      &imageProviderUrl)
extern "C" Q_DECL_EXPORT
QWebEngineHistoryPrivate *ritual_ZN24QWebEngineHistoryPrivateC1EPN15QtWebEngineCore24WebContentsAdapterClientERKSt8functionIF4QUrlRKS4_EE(
    QtWebEngineCore::WebContentsAdapterClient *client,
    const QWebEngineHistoryPrivate::ImageProviderUrl *imageProviderUrl) {
  return new QWebEngineHistoryPrivate(client, *imageProviderUrl);
}

//  QWebEngineHistoryPrivate::~QWebEngineHistoryPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QWebEngineHistoryPrivateD1Ev(
    QWebEngineHistoryPrivate *self) {
  delete self;
}

//  void QWebEngineHistoryPrivate::updateItems() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK24QWebEngineHistoryPrivate11updateItemsEv(
    const QWebEngineHistoryPrivate *self) {
  self->updateItems();
}

//  QtWebEngineCore::WebContentsAdapter *QWebEngineHistoryPrivate::adapter()
//      const
extern "C" Q_DECL_EXPORT
QtWebEngineCore::WebContentsAdapter *ritual_ZNK24QWebEngineHistoryPrivate7adapterEv(
    const QWebEngineHistoryPrivate *self) {
  return self->adapter();
}

//  QUrl QWebEngineHistoryPrivate::urlOrImageProviderUrl(const QUrl &url)
//      const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK24QWebEngineHistoryPrivate21urlOrImageProviderUrlERK4QUrl(
    const QWebEngineHistoryPrivate *self,
    const QUrl *url) {
  return new QUrl(self->urlOrImageProviderUrl(*url));
}
