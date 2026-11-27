//  Written by dev_tooling.RitualGenerator from the records of QtWebEngineCor
//  e/6.12.0/QtWebEngineCore/private/qwebengineextensioninfo_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtWebEngineCore/qtwebenginecoreglobal.h>
#include <QtWebEngineCore/6.12.0/QtWebEngineCore/private/qtwebenginecoreglobal_p.h>
#if QT_CONFIG(webengine_extensions)
#include <QtWebEngineCore/6.12.0/QtWebEngineCore/private/qtwebenginecoreglobal_p.h>
#include <QtWebEngineCore/QtWebEngineCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWebEngineCore/6.12.0/QtWebEngineCore/private/qwebengineextensioninfo_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QWebEngineExtensionInfoPrivate::ExtensionData::~ExtensionData()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QWebEngineExtensionInfoPrivate13ExtensionDataD1Ev(
    QWebEngineExtensionInfoPrivate::ExtensionData *self) {
  delete self;
}

#endif  // QT_CONFIG(webengine_extensions)
