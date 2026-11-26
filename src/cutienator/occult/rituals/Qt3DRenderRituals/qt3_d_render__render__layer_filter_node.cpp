//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/layerfilternode_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/layerfilternode_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/Qt3DCore>

//  Qt3DRender::Render::LayerFilterNode::LayerFilterNode()
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::LayerFilterNode *ritual_ZN10Qt3DRender6Render15LayerFilterNodeC1Ev() {
  return new Qt3DRender::Render::LayerFilterNode();
}

//  void Qt3DRender::Render::LayerFilterNode::syncFromFrontEnd(const
//      Qt3DCore::QNode *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render15LayerFilterNode16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DRender::Render::LayerFilterNode *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->syncFromFrontEnd(frontEnd, firstTime);
}

//  Qt3DCore::QNodeIdVector Qt3DRender::Render::LayerFilterNode::layerIds()
//      const
extern "C" Q_DECL_EXPORT
Qt3DCore::QNodeIdVector *ritual_ZNK10Qt3DRender6Render15LayerFilterNode8layerIdsEv(
    const Qt3DRender::Render::LayerFilterNode *self) {
  return new Qt3DCore::QNodeIdVector(self->layerIds());
}

//  void Qt3DRender::Render::LayerFilterNode::setLayerIds(const
//      Qt3DCore::QNodeIdVector &list)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render15LayerFilterNode11setLayerIdsERK5QListIN8Qt3DCore7QNodeIdEE(
    Qt3DRender::Render::LayerFilterNode *self,
    const Qt3DCore::QNodeIdVector *list) {
  self->setLayerIds(*list);
}

//  QLayerFilter::FilterMode
//      Qt3DRender::Render::LayerFilterNode::filterMode() const
extern "C" Q_DECL_EXPORT
Qt3DRender::QLayerFilter::FilterMode ritual_ZNK10Qt3DRender6Render15LayerFilterNode10filterModeEv(
    const Qt3DRender::Render::LayerFilterNode *self) {
  return self->filterMode();
}

//  void Qt3DRender::Render::LayerFilterNode::syncFromFrontEnd(const
//      Qt3DCore::QNode *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10Qt3DRender6Render15LayerFilterNode16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DRender::Render::LayerFilterNode *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->Qt3DRender::Render::LayerFilterNode::syncFromFrontEnd(
      frontEnd,
      firstTime);
}

//  a Qt3DCore::QNodeIdVector a ritual of Qt3DRender::Render::LayerFilterNode
//      gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DRender_Render_LayerFilterNode__Qt3DCore_QNodeIdVector(
    Qt3DCore::QNodeIdVector *self) {
  delete self;
}
