//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/ssg/qssgrendercontextcore.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/ssg/qssgrendercontextcore.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QSSGRenderContextInterface::QSSGRenderContextInterface(QRhi *rhi)
extern "C" Q_DECL_EXPORT
QSSGRenderContextInterface *ritual_ZN26QSSGRenderContextInterfaceC1EP4QRhi(
    QRhi *rhi) {
  return new QSSGRenderContextInterface(rhi);
}

//  QSSGRenderContextInterface::~QSSGRenderContextInterface()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QSSGRenderContextInterfaceD1Ev(
    QSSGRenderContextInterface *self) {
  delete self;
}

//  const std::unique_ptr<QSSGRenderer>
//      &QSSGRenderContextInterface::renderer() const
extern "C" Q_DECL_EXPORT
const std::unique_ptr<QSSGRenderer> *ritual_ZNK26QSSGRenderContextInterface8rendererEv(
    const QSSGRenderContextInterface *self) {
  return &(self->renderer());
}

//  const std::unique_ptr<QSSGBufferManager>
//      &QSSGRenderContextInterface::bufferManager() const
extern "C" Q_DECL_EXPORT
const std::unique_ptr<QSSGBufferManager> *ritual_ZNK26QSSGRenderContextInterface13bufferManagerEv(
    const QSSGRenderContextInterface *self) {
  return &(self->bufferManager());
}

//  const std::unique_ptr<QSSGRhiContext>
//      &QSSGRenderContextInterface::rhiContext() const
extern "C" Q_DECL_EXPORT
const std::unique_ptr<QSSGRhiContext> *ritual_ZNK26QSSGRenderContextInterface10rhiContextEv(
    const QSSGRenderContextInterface *self) {
  return &(self->rhiContext());
}

//  const std::unique_ptr<QSSGShaderCache>
//      &QSSGRenderContextInterface::shaderCache() const
extern "C" Q_DECL_EXPORT
const std::unique_ptr<QSSGShaderCache> *ritual_ZNK26QSSGRenderContextInterface11shaderCacheEv(
    const QSSGRenderContextInterface *self) {
  return &(self->shaderCache());
}

//  const std::shared_ptr<QSSGShaderLibraryManager>
//      &QSSGRenderContextInterface::shaderLibraryManager() const
extern "C" Q_DECL_EXPORT
const std::shared_ptr<QSSGShaderLibraryManager> *ritual_ZNK26QSSGRenderContextInterface20shaderLibraryManagerEv(
    const QSSGRenderContextInterface *self) {
  return &(self->shaderLibraryManager());
}

//  const std::unique_ptr<QSSGCustomMaterialSystem>
//      &QSSGRenderContextInterface::customMaterialSystem() const
extern "C" Q_DECL_EXPORT
const std::unique_ptr<QSSGCustomMaterialSystem> *ritual_ZNK26QSSGRenderContextInterface20customMaterialSystemEv(
    const QSSGRenderContextInterface *self) {
  return &(self->customMaterialSystem());
}

//  const std::unique_ptr<QSSGProgramGenerator>
//      &QSSGRenderContextInterface::shaderProgramGenerator() const
extern "C" Q_DECL_EXPORT
const std::unique_ptr<QSSGProgramGenerator> *ritual_ZNK26QSSGRenderContextInterface22shaderProgramGeneratorEv(
    const QSSGRenderContextInterface *self) {
  return &(self->shaderProgramGenerator());
}

//  const std::unique_ptr<QSSGDebugDrawSystem>
//      &QSSGRenderContextInterface::debugDrawSystem() const
extern "C" Q_DECL_EXPORT
const std::unique_ptr<QSSGDebugDrawSystem> *ritual_ZNK26QSSGRenderContextInterface15debugDrawSystemEv(
    const QSSGRenderContextInterface *self) {
  return &(self->debugDrawSystem());
}

//  QRhi *QSSGRenderContextInterface::rhi() const
extern "C" Q_DECL_EXPORT
QRhi *ritual_ZNK26QSSGRenderContextInterface3rhiEv(
    const QSSGRenderContextInterface *self) {
  return self->rhi();
}

//  void QSSGRenderContextInterface::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QSSGRenderContextInterface4initEv(
    QSSGRenderContextInterface *self) {
  self->init();
}

//  void QSSGRenderContextInterface::releaseCachedResources()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QSSGRenderContextInterface22releaseCachedResourcesEv(
    QSSGRenderContextInterface *self) {
  self->releaseCachedResources();
}

//  const std::unique_ptr<QSSGPerFrameAllocator>
//      &QSSGRenderContextInterface::perFrameAllocator() const
extern "C" Q_DECL_EXPORT
const std::unique_ptr<QSSGPerFrameAllocator> *ritual_ZNK26QSSGRenderContextInterface17perFrameAllocatorEv(
    const QSSGRenderContextInterface *self) {
  return &(self->perFrameAllocator());
}
