//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/scene_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/scene_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qurl.h>

//  Qt3DRender::Render::Scene::Scene()
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::Scene *ritual_ZN10Qt3DRender6Render5SceneC1Ev() {
  return new Qt3DRender::Render::Scene();
}

//  void Qt3DRender::Render::Scene::syncFromFrontEnd(const Qt3DCore::QNode
//      *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render5Scene16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DRender::Render::Scene *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->syncFromFrontEnd(frontEnd, firstTime);
}

//  QUrl Qt3DRender::Render::Scene::source() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK10Qt3DRender6Render5Scene6sourceEv(
    const Qt3DRender::Render::Scene *self) {
  return new QUrl(self->source());
}

//  void Qt3DRender::Render::Scene::setSceneManager(SceneManager *manager)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render5Scene15setSceneManagerEPNS0_12SceneManagerE(
    Qt3DRender::Render::Scene *self,
    Qt3DRender::Render::SceneManager *manager) {
  self->setSceneManager(manager);
}

//  void Qt3DRender::Render::Scene::cleanup()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render5Scene7cleanupEv(
    Qt3DRender::Render::Scene *self) {
  self->cleanup();
}

//  void Qt3DRender::Render::Scene::syncFromFrontEnd(const Qt3DCore::QNode
//      *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10Qt3DRender6Render5Scene16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DRender::Render::Scene *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->Qt3DRender::Render::Scene::syncFromFrontEnd(frontEnd, firstTime);
}
