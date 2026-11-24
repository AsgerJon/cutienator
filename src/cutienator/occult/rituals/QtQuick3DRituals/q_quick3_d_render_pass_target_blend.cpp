//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3D/6.12.0/QtQuick3D/private/qquick3dshaderutils_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick3D/6.12.0/QtQuick3D/private/qtquick3dglobal_p.h>
#include <QtQuick3D/QtQuick3D>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3D/6.12.0/QtQuick3D/private/qquick3dshaderutils_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/rhi/qrhi.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  bool QQuick3DRenderPassTargetBlend::operator==(const
//      QQuick3DRenderPassTargetBlend &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK29QQuick3DRenderPassTargetBlendeqERKS_(
    const QQuick3DRenderPassTargetBlend *self,
    const QQuick3DRenderPassTargetBlend *other) {
  return self->operator==(*other);
}

//  QQuick3DRenderPassTargetBlend::QQuick3DRenderPassTargetBlend()
extern "C" Q_DECL_EXPORT
QQuick3DRenderPassTargetBlend *ritual_ZN29QQuick3DRenderPassTargetBlendC1Ev() {
  return new QQuick3DRenderPassTargetBlend();
}

//  QQuick3DRenderPassTargetBlend::QQuick3DRenderPassTargetBlend(QRhiGraphics
//      Pipeline::TargetBlend targetBlend)
extern "C" Q_DECL_EXPORT
QQuick3DRenderPassTargetBlend *ritual_ZN29QQuick3DRenderPassTargetBlendC1EN20QRhiGraphicsPipeline11TargetBlendE(
    const QRhiGraphicsPipeline::TargetBlend *targetBlend) {
  return new QQuick3DRenderPassTargetBlend(*targetBlend);
}

//  QRhiGraphicsPipeline::TargetBlend
//      QQuick3DRenderPassTargetBlend::toRhiTargetBlend() const
extern "C" Q_DECL_EXPORT
QRhiGraphicsPipeline::TargetBlend *ritual_ZNK29QQuick3DRenderPassTargetBlend16toRhiTargetBlendEv(
    const QQuick3DRenderPassTargetBlend *self) {
  return new QRhiGraphicsPipeline::TargetBlend(self->toRhiTargetBlend());
}

//  QQuick3DRenderPassTargetBlend::~QQuick3DRenderPassTargetBlend()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QQuick3DRenderPassTargetBlendD1Ev(
    QQuick3DRenderPassTargetBlend *self) {
  delete self;
}
