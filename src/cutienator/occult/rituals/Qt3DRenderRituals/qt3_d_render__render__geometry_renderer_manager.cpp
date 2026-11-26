//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/geometryrenderermanager_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/geometryrenderermanager_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/qnodeid.h>
#include <QtCore/QList>
#include <Qt3DCore/Qt3DCore>

//  Qt3DRender::Render::GeometryRendererManager::GeometryRendererManager()
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::GeometryRendererManager *ritual_ZN10Qt3DRender6Render23GeometryRendererManagerC1Ev() {
  return new Qt3DRender::Render::GeometryRendererManager();
}

//  Qt3DRender::Render::GeometryRendererManager::~GeometryRendererManager()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render23GeometryRendererManagerD1Ev(
    Qt3DRender::Render::GeometryRendererManager *self) {
  delete self;
}

//  void Qt3DRender::Render::GeometryRendererManager::addDirtyGeometryRendere
//      r(Qt3DCore::QNodeId bufferId)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render23GeometryRendererManager24addDirtyGeometryRendererEN8Qt3DCore7QNodeIdE(
    Qt3DRender::Render::GeometryRendererManager *self,
    const Qt3DCore::QNodeId *bufferId) {
  self->addDirtyGeometryRenderer(*bufferId);
}

//  QList<Qt3DCore::QNodeId>
//      Qt3DRender::Render::GeometryRendererManager::dirtyGeometryRenderers()
extern "C" Q_DECL_EXPORT
QList<Qt3DCore::QNodeId> *ritual_ZN10Qt3DRender6Render23GeometryRendererManager22dirtyGeometryRenderersEv(
    Qt3DRender::Render::GeometryRendererManager *self) {
  return new QList<Qt3DCore::QNodeId>(self->dirtyGeometryRenderers());
}

//  a QList<Qt3DCore::QNodeId> a ritual of
//      Qt3DRender::Render::GeometryRendererManager gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DRender_Render_GeometryRendererManager__QList_Qt3DCore_QNodeId(
    QList<Qt3DCore::QNodeId> *self) {
  delete self;
}
