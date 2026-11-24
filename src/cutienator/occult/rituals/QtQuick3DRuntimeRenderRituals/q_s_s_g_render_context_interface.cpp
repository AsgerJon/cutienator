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
