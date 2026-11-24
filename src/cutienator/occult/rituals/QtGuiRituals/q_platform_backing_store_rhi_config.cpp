//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/qpa/qplatformbackingstore.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qplatformbackingstore.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QPlatformBackingStoreRhiConfig::QPlatformBackingStoreRhiConfig()
extern "C" Q_DECL_EXPORT
QPlatformBackingStoreRhiConfig *ritual_ZN30QPlatformBackingStoreRhiConfigC1Ev() {
  return new QPlatformBackingStoreRhiConfig();
}

//  QPlatformBackingStoreRhiConfig::QPlatformBackingStoreRhiConfig(Api api)
extern "C" Q_DECL_EXPORT
QPlatformBackingStoreRhiConfig *ritual_ZN30QPlatformBackingStoreRhiConfigC1ENS_3ApiE(
    QPlatformBackingStoreRhiConfig::Api api) {
  return new QPlatformBackingStoreRhiConfig(api);
}

//  bool QPlatformBackingStoreRhiConfig::isEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK30QPlatformBackingStoreRhiConfig9isEnabledEv(
    const QPlatformBackingStoreRhiConfig *self) {
  return self->isEnabled();
}

//  void QPlatformBackingStoreRhiConfig::setEnabled(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QPlatformBackingStoreRhiConfig10setEnabledEb(
    QPlatformBackingStoreRhiConfig *self,
    bool enable) {
  self->setEnabled(enable);
}

//  Api QPlatformBackingStoreRhiConfig::api() const
extern "C" Q_DECL_EXPORT
QPlatformBackingStoreRhiConfig::Api ritual_ZNK30QPlatformBackingStoreRhiConfig3apiEv(
    const QPlatformBackingStoreRhiConfig *self) {
  return self->api();
}

//  void QPlatformBackingStoreRhiConfig::setApi(Api api)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QPlatformBackingStoreRhiConfig6setApiENS_3ApiE(
    QPlatformBackingStoreRhiConfig *self,
    QPlatformBackingStoreRhiConfig::Api api) {
  self->setApi(api);
}

//  bool QPlatformBackingStoreRhiConfig::isDebugLayerEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK30QPlatformBackingStoreRhiConfig19isDebugLayerEnabledEv(
    const QPlatformBackingStoreRhiConfig *self) {
  return self->isDebugLayerEnabled();
}

//  void QPlatformBackingStoreRhiConfig::setDebugLayer(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QPlatformBackingStoreRhiConfig13setDebugLayerEb(
    QPlatformBackingStoreRhiConfig *self,
    bool enable) {
  self->setDebugLayer(enable);
}

//  bool operator==(const QPlatformBackingStoreRhiConfig &a, const
//      QPlatformBackingStoreRhiConfig &b)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK30QPlatformBackingStoreRhiConfigS1_(
    const QPlatformBackingStoreRhiConfig *a,
    const QPlatformBackingStoreRhiConfig *b) {
  return operator==(*a, *b);
}

//  QPlatformBackingStoreRhiConfig::~QPlatformBackingStoreRhiConfig()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QPlatformBackingStoreRhiConfigD1Ev(
    QPlatformBackingStoreRhiConfig *self) {
  delete self;
}
