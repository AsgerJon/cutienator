//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/scene_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/scene_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/qnodeid.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/private/scene_p.h>
#include <Qt3DCore/qentity.h>
#include <Qt3DCore/private/qnode_p.h>
#include <Qt3DCore/private/qscene_p.h>
#include <Qt3DCore/private/qdownloadhelperservice_p.h>
#include <Qt3DRender/qsceneloader.h>
#include <Qt3DRender/private/qsceneloader_p.h>
#include <Qt3DRender/private/scenemanager_p.h>
#include <QtCore/qcoreapplication.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/render/io/scene.cpp, line 64, as _ZN10Qt3DRender6Render18RenderSceneFunctorC1EPNS0_16AbstractRendererEPNS0_12SceneManagerE
namespace Qt3DRender::Render {
using namespace Qt3DCore;
inline RenderSceneFunctor::RenderSceneFunctor(AbstractRenderer *renderer, SceneManager *sceneManager)
    : m_sceneManager(sceneManager)
    , m_renderer(renderer)
{
}
}  // namespace Qt3DRender::Render

//  from ../qt3d/src/render/io/scene.cpp, line 70, as _ZNK10Qt3DRender6Render18RenderSceneFunctor6createEN8Qt3DCore7QNodeIdE
namespace Qt3DRender::Render {
using namespace Qt3DCore;
inline Qt3DCore::QBackendNode *RenderSceneFunctor::create(Qt3DCore::QNodeId id) const
{
    Scene *scene = m_sceneManager->getOrCreateResource(id);
    scene->setSceneManager(m_sceneManager);
    scene->setRenderer(m_renderer);
    return scene;
}
}  // namespace Qt3DRender::Render

//  from ../qt3d/src/render/io/scene.cpp, line 78, as _ZNK10Qt3DRender6Render18RenderSceneFunctor3getEN8Qt3DCore7QNodeIdE
namespace Qt3DRender::Render {
using namespace Qt3DCore;
inline Qt3DCore::QBackendNode *RenderSceneFunctor::get(Qt3DCore::QNodeId id) const
{
    return m_sceneManager->lookupResource(id);
}
}  // namespace Qt3DRender::Render

//  from ../qt3d/src/render/io/scene.cpp, line 83, as _ZNK10Qt3DRender6Render18RenderSceneFunctor7destroyEN8Qt3DCore7QNodeIdE
namespace Qt3DRender::Render {
using namespace Qt3DCore;
inline void RenderSceneFunctor::destroy(Qt3DCore::QNodeId id) const
{
    m_sceneManager->releaseResource(id);
}
}  // namespace Qt3DRender::Render
//  -----------------------------------------------------------------------

//  Qt3DRender::Render::RenderSceneFunctor::RenderSceneFunctor(AbstractRender
//      er *renderer, SceneManager *sceneManager)
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::RenderSceneFunctor *ritual_ZN10Qt3DRender6Render18RenderSceneFunctorC1EPNS0_16AbstractRendererEPNS0_12SceneManagerE(
    Qt3DRender::Render::AbstractRenderer *renderer,
    Qt3DRender::Render::SceneManager *sceneManager) {
  return new Qt3DRender::Render::RenderSceneFunctor(renderer, sceneManager);
}

//  Qt3DCore::QBackendNode
//      *Qt3DRender::Render::RenderSceneFunctor::create(Qt3DCore::QNodeId id)
//      const
extern "C" Q_DECL_EXPORT
Qt3DCore::QBackendNode *ritual_ZNK10Qt3DRender6Render18RenderSceneFunctor6createEN8Qt3DCore7QNodeIdE(
    const Qt3DRender::Render::RenderSceneFunctor *self,
    const Qt3DCore::QNodeId *id) {
  return self->create(*id);
}

//  Qt3DCore::QBackendNode
//      *Qt3DRender::Render::RenderSceneFunctor::get(Qt3DCore::QNodeId id)
//      const
extern "C" Q_DECL_EXPORT
Qt3DCore::QBackendNode *ritual_ZNK10Qt3DRender6Render18RenderSceneFunctor3getEN8Qt3DCore7QNodeIdE(
    const Qt3DRender::Render::RenderSceneFunctor *self,
    const Qt3DCore::QNodeId *id) {
  return self->get(*id);
}

//  void Qt3DRender::Render::RenderSceneFunctor::destroy(Qt3DCore::QNodeId
//      id) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK10Qt3DRender6Render18RenderSceneFunctor7destroyEN8Qt3DCore7QNodeIdE(
    const Qt3DRender::Render::RenderSceneFunctor *self,
    const Qt3DCore::QNodeId *id) {
  self->destroy(*id);
}

//  Qt3DRender::Render::RenderSceneFunctor::~RenderSceneFunctor()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render18RenderSceneFunctorD1Ev(
    Qt3DRender::Render::RenderSceneFunctor *self) {
  delete self;
}

//  Qt3DCore::QBackendNode
//      *Qt3DRender::Render::RenderSceneFunctor::create(Qt3DCore::QNodeId id)
//      const
extern "C" Q_DECL_EXPORT
Qt3DCore::QBackendNode *ritual_own_ZNK10Qt3DRender6Render18RenderSceneFunctor6createEN8Qt3DCore7QNodeIdE(
    const Qt3DRender::Render::RenderSceneFunctor *self,
    const Qt3DCore::QNodeId *id) {
  return self->Qt3DRender::Render::RenderSceneFunctor::create(*id);
}

//  Qt3DCore::QBackendNode
//      *Qt3DRender::Render::RenderSceneFunctor::get(Qt3DCore::QNodeId id)
//      const
extern "C" Q_DECL_EXPORT
Qt3DCore::QBackendNode *ritual_own_ZNK10Qt3DRender6Render18RenderSceneFunctor3getEN8Qt3DCore7QNodeIdE(
    const Qt3DRender::Render::RenderSceneFunctor *self,
    const Qt3DCore::QNodeId *id) {
  return self->Qt3DRender::Render::RenderSceneFunctor::get(*id);
}

//  void Qt3DRender::Render::RenderSceneFunctor::destroy(Qt3DCore::QNodeId
//      id) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK10Qt3DRender6Render18RenderSceneFunctor7destroyEN8Qt3DCore7QNodeIdE(
    const Qt3DRender::Render::RenderSceneFunctor *self,
    const Qt3DCore::QNodeId *id) {
  self->Qt3DRender::Render::RenderSceneFunctor::destroy(*id);
}
