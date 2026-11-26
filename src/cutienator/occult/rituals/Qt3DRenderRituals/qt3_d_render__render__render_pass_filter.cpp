//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/renderpassfilternode_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/renderpassfilternode_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/qnodeid.h>
#include <QtCore/QList>
#include <Qt3DCore/Qt3DCore>

//  Qt3DRender::Render::RenderPassFilter::RenderPassFilter()
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::RenderPassFilter *ritual_ZN10Qt3DRender6Render16RenderPassFilterC1Ev() {
  return new Qt3DRender::Render::RenderPassFilter();
}

//  QList<Qt3DCore::QNodeId> Qt3DRender::Render::RenderPassFilter::filters()
//      const
extern "C" Q_DECL_EXPORT
QList<Qt3DCore::QNodeId> *ritual_ZNK10Qt3DRender6Render16RenderPassFilter7filtersEv(
    const Qt3DRender::Render::RenderPassFilter *self) {
  return new QList<Qt3DCore::QNodeId>(self->filters());
}

//  QList<Qt3DCore::QNodeId>
//      Qt3DRender::Render::RenderPassFilter::parameters() const
extern "C" Q_DECL_EXPORT
QList<Qt3DCore::QNodeId> *ritual_ZNK10Qt3DRender6Render16RenderPassFilter10parametersEv(
    const Qt3DRender::Render::RenderPassFilter *self) {
  return new QList<Qt3DCore::QNodeId>(self->parameters());
}

//  void Qt3DRender::Render::RenderPassFilter::appendFilter(Qt3DCore::QNodeId
//      criterionId)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render16RenderPassFilter12appendFilterEN8Qt3DCore7QNodeIdE(
    Qt3DRender::Render::RenderPassFilter *self,
    const Qt3DCore::QNodeId *criterionId) {
  self->appendFilter(*criterionId);
}

//  void Qt3DRender::Render::RenderPassFilter::removeFilter(Qt3DCore::QNodeId
//      criterionId)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render16RenderPassFilter12removeFilterEN8Qt3DCore7QNodeIdE(
    Qt3DRender::Render::RenderPassFilter *self,
    const Qt3DCore::QNodeId *criterionId) {
  self->removeFilter(*criterionId);
}

//  void Qt3DRender::Render::RenderPassFilter::syncFromFrontEnd(const
//      Qt3DCore::QNode *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render16RenderPassFilter16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DRender::Render::RenderPassFilter *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->syncFromFrontEnd(frontEnd, firstTime);
}

//  void Qt3DRender::Render::RenderPassFilter::syncFromFrontEnd(const
//      Qt3DCore::QNode *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10Qt3DRender6Render16RenderPassFilter16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DRender::Render::RenderPassFilter *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->Qt3DRender::Render::RenderPassFilter::syncFromFrontEnd(
      frontEnd,
      firstTime);
}

//  a QList<Qt3DCore::QNodeId> a ritual of
//      Qt3DRender::Render::RenderPassFilter gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DRender_Render_RenderPassFilter__QList_Qt3DCore_QNodeId(
    QList<Qt3DCore::QNodeId> *self) {
  delete self;
}
