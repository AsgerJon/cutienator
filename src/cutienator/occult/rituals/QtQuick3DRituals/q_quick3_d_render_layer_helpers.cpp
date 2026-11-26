//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3D/6.12.0/QtQuick3D/private/qquick3dscenerenderer_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick3D/6.12.0/QtQuick3D/private/qtquick3dglobal_p.h>
#include <QtQuick3D/QtQuick3D>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3D/6.12.0/QtQuick3D/private/qquick3dscenerenderer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void QQuick3DRenderLayerHelpers::updateLayerNodeHelper(const
//      QQuick3DViewport &view3D, const
//      std::shared_ptr<QSSGRenderContextInterface> &rci, QSSGRenderLayer
//      &layerNode, bool &aaIsDirty, bool &temporalIsDirty)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuick3DRenderLayerHelpers21updateLayerNodeHelperERK16QQuick3DViewportRKSt10shared_ptrI26QSSGRenderContextInterfaceER15QSSGRenderLayerRbSA_(
    const QQuick3DViewport *view3D,
    const std::shared_ptr<QSSGRenderContextInterface> *rci,
    QSSGRenderLayer *layerNode,
    bool *aaIsDirty,
    bool *temporalIsDirty) {
  QQuick3DRenderLayerHelpers::updateLayerNodeHelper(
      *view3D,
      *rci,
      *layerNode,
      *aaIsDirty,
      *temporalIsDirty);
}

//  QQuick3DRenderLayerHelpers::~QQuick3DRenderLayerHelpers()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuick3DRenderLayerHelpersD1Ev(
    QQuick3DRenderLayerHelpers *self) {
  delete self;
}
