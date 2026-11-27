//  Written by dev_tooling.RitualGenerator from the records of
//  QtWebEngineCore/6.12.0/QtWebEngineCore/private/qwebenginecookiestore_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtWebEngineCore/6.12.0/QtWebEngineCore/private/qtwebenginecoreglobal_p.h>
#include <QtWebEngineCore/qwebenginecookiestore.h>
#include <QtWebEngineCore/QtWebEngineCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWebEngineCore/6.12.0/QtWebEngineCore/private/qwebenginecookiestore_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/qnetworkcookie.h>
#include <QtCore/qurl.h>

//  QWebEngineCookieStore *QWebEngineCookieStorePrivate::q_func()
extern "C" Q_DECL_EXPORT
QWebEngineCookieStore *ritual_ZN28QWebEngineCookieStorePrivate6q_funcEv(
    QWebEngineCookieStorePrivate *self) {
  return self->q_func();
}

//  const QWebEngineCookieStore *QWebEngineCookieStorePrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QWebEngineCookieStore *ritual_ZNK28QWebEngineCookieStorePrivate6q_funcEv(
    const QWebEngineCookieStorePrivate *self) {
  return self->q_func();
}

//  QWebEngineCookieStorePrivate::QWebEngineCookieStorePrivate(QWebEngineCook
//      ieStore *q)
extern "C" Q_DECL_EXPORT
QWebEngineCookieStorePrivate *ritual_ZN28QWebEngineCookieStorePrivateC1EP21QWebEngineCookieStore(
    QWebEngineCookieStore *q) {
  return new QWebEngineCookieStorePrivate(q);
}

//  void QWebEngineCookieStorePrivate::processPendingUserCookies()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QWebEngineCookieStorePrivate25processPendingUserCookiesEv(
    QWebEngineCookieStorePrivate *self) {
  self->processPendingUserCookies();
}

//  void QWebEngineCookieStorePrivate::rejectPendingUserCookies()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QWebEngineCookieStorePrivate24rejectPendingUserCookiesEv(
    QWebEngineCookieStorePrivate *self) {
  self->rejectPendingUserCookies();
}

//  void QWebEngineCookieStorePrivate::setCookie(const QNetworkCookie
//      &cookie, const QUrl &origin)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QWebEngineCookieStorePrivate9setCookieERK14QNetworkCookieRK4QUrl(
    QWebEngineCookieStorePrivate *self,
    const QNetworkCookie *cookie,
    const QUrl *origin) {
  self->setCookie(*cookie, *origin);
}

//  void QWebEngineCookieStorePrivate::deleteCookie(const QNetworkCookie
//      &cookie, const QUrl &url)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QWebEngineCookieStorePrivate12deleteCookieERK14QNetworkCookieRK4QUrl(
    QWebEngineCookieStorePrivate *self,
    const QNetworkCookie *cookie,
    const QUrl *url) {
  self->deleteCookie(*cookie, *url);
}

//  void QWebEngineCookieStorePrivate::deleteSessionCookies()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QWebEngineCookieStorePrivate20deleteSessionCookiesEv(
    QWebEngineCookieStorePrivate *self) {
  self->deleteSessionCookies();
}

//  void QWebEngineCookieStorePrivate::deleteAllCookies()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QWebEngineCookieStorePrivate16deleteAllCookiesEv(
    QWebEngineCookieStorePrivate *self) {
  self->deleteAllCookies();
}

//  void QWebEngineCookieStorePrivate::getAllCookies()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QWebEngineCookieStorePrivate13getAllCookiesEv(
    QWebEngineCookieStorePrivate *self) {
  self->getAllCookies();
}

//  bool QWebEngineCookieStorePrivate::canAccessCookies(const QUrl
//      &firstPartyUrl, const QUrl &url) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK28QWebEngineCookieStorePrivate16canAccessCookiesERK4QUrlS2_(
    const QWebEngineCookieStorePrivate *self,
    const QUrl *firstPartyUrl,
    const QUrl *url) {
  return self->canAccessCookies(*firstPartyUrl, *url);
}

//  void QWebEngineCookieStorePrivate::onCookieChanged(const QNetworkCookie
//      &cookie, bool removed)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QWebEngineCookieStorePrivate15onCookieChangedERK14QNetworkCookieb(
    QWebEngineCookieStorePrivate *self,
    const QNetworkCookie *cookie,
    bool removed) {
  self->onCookieChanged(*cookie, removed);
}

//  QWebEngineCookieStorePrivate::~QWebEngineCookieStorePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QWebEngineCookieStorePrivateD1Ev(
    QWebEngineCookieStorePrivate *self) {
  delete self;
}
