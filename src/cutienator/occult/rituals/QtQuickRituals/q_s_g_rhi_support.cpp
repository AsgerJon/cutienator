//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgrhisupport_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgrhisupport_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qimage.h>
#include <QtCore/qstring.h>
#include <QtQuick/qquickgraphicsconfiguration.h>

//  QSGRhiSupport *QSGRhiSupport::instance_internal()
extern "C" Q_DECL_EXPORT
QSGRhiSupport *ritual_ZN13QSGRhiSupport17instance_internalEv() {
  return QSGRhiSupport::instance_internal();
}

//  QSGRhiSupport *QSGRhiSupport::instance()
extern "C" Q_DECL_EXPORT
QSGRhiSupport *ritual_ZN13QSGRhiSupport8instanceEv() {
  return QSGRhiSupport::instance();
}

//  int QSGRhiSupport::chooseSampleCount(int samples, QRhi *rhi)
extern "C" Q_DECL_EXPORT
int ritual_ZN13QSGRhiSupport17chooseSampleCountEiP4QRhi(
    int samples,
    QRhi *rhi) {
  return QSGRhiSupport::chooseSampleCount(samples, rhi);
}

//  int QSGRhiSupport::chooseSampleCountForWindowWithRhi(QWindow *window,
//      QRhi *rhi)
extern "C" Q_DECL_EXPORT
int ritual_ZN13QSGRhiSupport33chooseSampleCountForWindowWithRhiEP7QWindowP4QRhi(
    QWindow *window,
    QRhi *rhi) {
  return QSGRhiSupport::chooseSampleCountForWindowWithRhi(window, rhi);
}

//  QImage QSGRhiSupport::grabAndBlockInCurrentFrame(QRhi *rhi,
//      QRhiCommandBuffer *cb, QRhiTexture *src)
extern "C" Q_DECL_EXPORT
QImage *ritual_ZN13QSGRhiSupport26grabAndBlockInCurrentFrameEP4QRhiP17QRhiCommandBufferP11QRhiTexture(
    QRhi *rhi,
    QRhiCommandBuffer *cb,
    QRhiTexture *src) {
  return new QImage(QSGRhiSupport::grabAndBlockInCurrentFrame(rhi, cb, src));
}

//  void QSGRhiSupport::checkEnvQSgInfo()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSGRhiSupport15checkEnvQSgInfoEv() {
  QSGRhiSupport::checkEnvQSgInfo();
}

//  void QSGRhiSupport::configure(QSGRendererInterface::GraphicsApi api)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSGRhiSupport9configureEN20QSGRendererInterface11GraphicsApiE(
    QSGRhiSupport *self,
    QSGRendererInterface::GraphicsApi api) {
  self->configure(api);
}

//  QRhi::Implementation QSGRhiSupport::rhiBackend() const
extern "C" Q_DECL_EXPORT
QRhi::Implementation ritual_ZNK13QSGRhiSupport10rhiBackendEv(
    const QSGRhiSupport *self) {
  return self->rhiBackend();
}

//  QString QSGRhiSupport::rhiBackendName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13QSGRhiSupport14rhiBackendNameEv(
    const QSGRhiSupport *self) {
  return new QString(self->rhiBackendName());
}

//  QSGRendererInterface::GraphicsApi QSGRhiSupport::graphicsApi() const
extern "C" Q_DECL_EXPORT
QSGRendererInterface::GraphicsApi ritual_ZNK13QSGRhiSupport11graphicsApiEv(
    const QSGRhiSupport *self) {
  return self->graphicsApi();
}

//  QSurface::SurfaceType QSGRhiSupport::windowSurfaceType() const
extern "C" Q_DECL_EXPORT
QSurface::SurfaceType ritual_ZNK13QSGRhiSupport17windowSurfaceTypeEv(
    const QSGRhiSupport *self) {
  return self->windowSurfaceType();
}

//  QOffscreenSurface *QSGRhiSupport::maybeCreateOffscreenSurface(QWindow
//      *window)
extern "C" Q_DECL_EXPORT
QOffscreenSurface *ritual_ZN13QSGRhiSupport27maybeCreateOffscreenSurfaceEP7QWindow(
    QSGRhiSupport *self,
    QWindow *window) {
  return self->maybeCreateOffscreenSurface(window);
}

//  RhiCreateResult QSGRhiSupport::createRhi(QQuickWindow *window, QSurface
//      *offscreenSurface, bool forcePreferSwRenderer)
extern "C" Q_DECL_EXPORT
QSGRhiSupport::RhiCreateResult *ritual_ZN13QSGRhiSupport9createRhiEP12QQuickWindowP8QSurfaceb(
    QSGRhiSupport *self,
    QQuickWindow *window,
    QSurface *offscreenSurface,
    bool forcePreferSwRenderer) {
  return new QSGRhiSupport::RhiCreateResult(
      self->createRhi(
          window,
          offscreenSurface,
          forcePreferSwRenderer));
}

//  void QSGRhiSupport::destroyRhi(QRhi *rhi, const
//      QQuickGraphicsConfiguration &config)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSGRhiSupport10destroyRhiEP4QRhiRK27QQuickGraphicsConfiguration(
    QSGRhiSupport *self,
    QRhi *rhi,
    const QQuickGraphicsConfiguration *config) {
  self->destroyRhi(rhi, *config);
}

//  void QSGRhiSupport::prepareWindowForRhi(QQuickWindow *window)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSGRhiSupport19prepareWindowForRhiEP12QQuickWindow(
    QSGRhiSupport *self,
    QQuickWindow *window) {
  self->prepareWindowForRhi(window);
}

//  QImage QSGRhiSupport::grabOffscreen(QQuickWindow *window)
extern "C" Q_DECL_EXPORT
QImage *ritual_ZN13QSGRhiSupport13grabOffscreenEP12QQuickWindow(
    QSGRhiSupport *self,
    QQuickWindow *window) {
  return new QImage(self->grabOffscreen(window));
}

//  void QSGRhiSupport::applySwapChainFormat(QRhiSwapChain *scWithWindowSet,
//      QQuickWindow *window)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSGRhiSupport20applySwapChainFormatEP13QRhiSwapChainP12QQuickWindow(
    QSGRhiSupport *self,
    QRhiSwapChain *scWithWindowSet,
    QQuickWindow *window) {
  self->applySwapChainFormat(scWithWindowSet, window);
}

//  bool QSGRhiSupport::attemptReinitWithSwRastUponFail() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QSGRhiSupport31attemptReinitWithSwRastUponFailEv(
    const QSGRhiSupport *self) {
  return self->attemptReinitWithSwRastUponFail();
}

//  QSGRhiSupport::QSGRhiSupport()
extern "C" Q_DECL_EXPORT
QSGRhiSupport *ritual_ZN13QSGRhiSupportC1Ev() {
  return new QSGRhiSupport();
}

//  void QSGRhiSupport::applySettings()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSGRhiSupport13applySettingsEv(QSGRhiSupport *self) {
  self->applySettings();
}

//  void QSGRhiSupport::adjustToPlatformQuirks()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSGRhiSupport22adjustToPlatformQuirksEv(
    QSGRhiSupport *self) {
  self->adjustToPlatformQuirks();
}

//  void QSGRhiSupport::preparePipelineCache(QRhi *rhi, QQuickWindow *window)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSGRhiSupport20preparePipelineCacheEP4QRhiP12QQuickWindow(
    QSGRhiSupport *self,
    QRhi *rhi,
    QQuickWindow *window) {
  self->preparePipelineCache(rhi, window);
}

//  void QSGRhiSupport::finalizePipelineCache(QRhi *rhi, const
//      QQuickGraphicsConfiguration &config)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSGRhiSupport21finalizePipelineCacheEP4QRhiRK27QQuickGraphicsConfiguration(
    QSGRhiSupport *self,
    QRhi *rhi,
    const QQuickGraphicsConfiguration *config) {
  self->finalizePipelineCache(rhi, *config);
}

//  QSGRhiSupport::~QSGRhiSupport()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSGRhiSupportD1Ev(QSGRhiSupport *self) {
  delete self;
}
