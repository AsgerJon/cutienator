//  Written by dev_tooling.RitualGenerator from the records of QtWebEngineQui
//  ck/6.12.0/QtWebEngineQuick/private/qquickwebengineforeigntypes_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtWebEngineCore/qtwebenginecoreglobal.h>
#include <QtWebEngineQuick/qtwebenginequickglobal.h>
#include <QtWebEngineQuick/6.12.0/QtWebEngineQuick/private/qtwebenginequickglobal_p.h>
#if QT_CONFIG(webengine_extensions)
#include <QtWebEngineQuick/6.12.0/QtWebEngineQuick/private/qtwebenginequickglobal_p.h>
#include <QtWebEngineQuick/QtWebEngineQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWebEngineQuick/6.12.0/QtWebEngineQuick/private/qquickwebengineforeigntypes_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void ForeignWebEngineExtensionManager::qt_qmlMarker_foreign()
extern "C" Q_DECL_EXPORT
void ritual_ZN32ForeignWebEngineExtensionManager20qt_qmlMarker_foreignEv(
    ForeignWebEngineExtensionManager *self) {
  self->qt_qmlMarker_foreign();
}

//  void ForeignWebEngineExtensionManager::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN32ForeignWebEngineExtensionManager24qt_qmlMarker_uncreatableEv(
    ForeignWebEngineExtensionManager *self) {
  self->qt_qmlMarker_uncreatable();
}

//  ForeignWebEngineExtensionManager::~ForeignWebEngineExtensionManager()
extern "C" Q_DECL_EXPORT
void ritual_ZN32ForeignWebEngineExtensionManagerD1Ev(
    ForeignWebEngineExtensionManager *self) {
  delete self;
}

#endif  // QT_CONFIG(webengine_extensions)
