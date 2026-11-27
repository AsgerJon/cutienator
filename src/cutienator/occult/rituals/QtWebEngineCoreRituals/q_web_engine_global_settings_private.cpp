//  Written by dev_tooling.RitualGenerator from the records of QtWebEngineCor
//  e/6.12.0/QtWebEngineCore/private/qwebengineglobalsettings_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtWebEngineCore/6.12.0/QtWebEngineCore/private/qtwebenginecoreglobal_p.h>
#include <QtWebEngineCore/QtWebEngineCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWebEngineCore/6.12.0/QtWebEngineCore/private/qwebengineglobalsettings_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QWebEngineGlobalSettingsPrivate::QWebEngineGlobalSettingsPrivate()
extern "C" Q_DECL_EXPORT
QWebEngineGlobalSettingsPrivate *ritual_ZN31QWebEngineGlobalSettingsPrivateC1Ev() {
  return new QWebEngineGlobalSettingsPrivate();
}

//  QWebEngineGlobalSettingsPrivate
//      *QWebEngineGlobalSettingsPrivate::instance()
extern "C" Q_DECL_EXPORT
QWebEngineGlobalSettingsPrivate *ritual_ZN31QWebEngineGlobalSettingsPrivate8instanceEv() {
  return QWebEngineGlobalSettingsPrivate::instance();
}

//  void QWebEngineGlobalSettingsPrivate::configureStubHostResolver()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QWebEngineGlobalSettingsPrivate25configureStubHostResolverEv(
    QWebEngineGlobalSettingsPrivate *self) {
  self->configureStubHostResolver();
}

//  QWebEngineGlobalSettingsPrivate::~QWebEngineGlobalSettingsPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QWebEngineGlobalSettingsPrivateD1Ev(
    QWebEngineGlobalSettingsPrivate *self) {
  delete self;
}
