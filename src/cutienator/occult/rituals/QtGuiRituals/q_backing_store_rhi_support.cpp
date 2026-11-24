//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qbackingstorerhisupport_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qbackingstorerhisupport_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qsurfaceformat.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qplatformbackingstore.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QBackingStoreRhiSupport::~QBackingStoreRhiSupport()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QBackingStoreRhiSupportD1Ev(QBackingStoreRhiSupport *self) {
  delete self;
}

//  void QBackingStoreRhiSupport::reset()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QBackingStoreRhiSupport5resetEv(
    QBackingStoreRhiSupport *self) {
  self->reset();
}

//  void QBackingStoreRhiSupport::setFormat(const QSurfaceFormat &format)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QBackingStoreRhiSupport9setFormatERK14QSurfaceFormat(
    QBackingStoreRhiSupport *self,
    const QSurfaceFormat *format) {
  self->setFormat(*format);
}

//  void QBackingStoreRhiSupport::setWindow(QWindow *window)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QBackingStoreRhiSupport9setWindowEP7QWindow(
    QBackingStoreRhiSupport *self,
    QWindow *window) {
  self->setWindow(window);
}

//  void QBackingStoreRhiSupport::setConfig(const
//      QPlatformBackingStoreRhiConfig &config)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QBackingStoreRhiSupport9setConfigERK30QPlatformBackingStoreRhiConfig(
    QBackingStoreRhiSupport *self,
    const QPlatformBackingStoreRhiConfig *config) {
  self->setConfig(*config);
}

//  bool QBackingStoreRhiSupport::create()
extern "C" Q_DECL_EXPORT
bool ritual_ZN23QBackingStoreRhiSupport6createEv(
    QBackingStoreRhiSupport *self) {
  return self->create();
}

//  QRhiSwapChain *QBackingStoreRhiSupport::swapChainForWindow(QWindow
//      *window)
extern "C" Q_DECL_EXPORT
QRhiSwapChain *ritual_ZN23QBackingStoreRhiSupport18swapChainForWindowEP7QWindow(
    QBackingStoreRhiSupport *self,
    QWindow *window) {
  return self->swapChainForWindow(window);
}

//  QSurface::SurfaceType QBackingStoreRhiSupport::surfaceTypeForConfig(const
//      QPlatformBackingStoreRhiConfig &config)
extern "C" Q_DECL_EXPORT
QSurface::SurfaceType ritual_ZN23QBackingStoreRhiSupport20surfaceTypeForConfigERK30QPlatformBackingStoreRhiConfig(
    const QPlatformBackingStoreRhiConfig *config) {
  return QBackingStoreRhiSupport::surfaceTypeForConfig(*config);
}

//  QRhi::Implementation QBackingStoreRhiSupport::apiToRhiBackend(QPlatformBa
//      ckingStoreRhiConfig::Api api)
extern "C" Q_DECL_EXPORT
QRhi::Implementation ritual_ZN23QBackingStoreRhiSupport15apiToRhiBackendEN30QPlatformBackingStoreRhiConfig3ApiE(
    QPlatformBackingStoreRhiConfig::Api api) {
  return QBackingStoreRhiSupport::apiToRhiBackend(api);
}

//  QRhi *QBackingStoreRhiSupport::rhi() const
extern "C" Q_DECL_EXPORT
QRhi *ritual_ZNK23QBackingStoreRhiSupport3rhiEv(
    const QBackingStoreRhiSupport *self) {
  return self->rhi();
}
