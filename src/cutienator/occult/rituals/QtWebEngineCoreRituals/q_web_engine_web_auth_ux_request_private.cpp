//  Written by dev_tooling.RitualGenerator from the records of QtWebEngineCor
//  e/6.12.0/QtWebEngineCore/private/qwebenginewebauthuxrequest_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtWebEngineCore/6.12.0/QtWebEngineCore/private/qtwebenginecoreglobal_p.h>
#include <QtWebEngineCore/QtWebEngineCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWebEngineCore/6.12.0/QtWebEngineCore/private/qwebenginewebauthuxrequest_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QWebEngineWebAuthUxRequestPrivate::QWebEngineWebAuthUxRequestPrivate(QtWe
//      bEngineCore::AuthenticatorRequestDialogController *controller)
extern "C" Q_DECL_EXPORT
QWebEngineWebAuthUxRequestPrivate *ritual_ZN33QWebEngineWebAuthUxRequestPrivateC1EPN15QtWebEngineCore36AuthenticatorRequestDialogControllerE(
    QtWebEngineCore::AuthenticatorRequestDialogController *controller) {
  return new QWebEngineWebAuthUxRequestPrivate(controller);
}

//  QWebEngineWebAuthUxRequestPrivate::~QWebEngineWebAuthUxRequestPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN33QWebEngineWebAuthUxRequestPrivateD1Ev(
    QWebEngineWebAuthUxRequestPrivate *self) {
  delete self;
}
