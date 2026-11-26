//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/light_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/light_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/qnodeid.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/private/light_p.h>
#include <Qt3DRender/qabstractlight.h>
#include <Qt3DRender/private/qabstractlight_p.h>
#include <Qt3DRender/private/abstractrenderer_p.h>
#include <Qt3DRender/private/nodemanagers_p.h>
#include <Qt3DCore/private/qbackendnode_p.h>
#include <Qt3DRender/private/managers_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/render/lights/light.cpp, line 38, as _ZN10Qt3DRender6Render18RenderLightFunctorC1EPNS0_16AbstractRendererEPNS0_12NodeManagersE
namespace Qt3DRender::Render {
using namespace Qt3DCore;
inline RenderLightFunctor::RenderLightFunctor(AbstractRenderer *renderer, NodeManagers *managers)
    : m_managers(managers)
    , m_renderer(renderer)
{
}
}  // namespace Qt3DRender::Render

//  from ../qt3d/src/render/lights/light.cpp, line 44, as _ZNK10Qt3DRender6Render18RenderLightFunctor6createEN8Qt3DCore7QNodeIdE
namespace Qt3DRender::Render {
using namespace Qt3DCore;
inline Qt3DCore::QBackendNode *RenderLightFunctor::create(Qt3DCore::QNodeId id) const
{
    Light *backend = m_managers->lightManager()->getOrCreateResource(id);
    backend->setRenderer(m_renderer);
    return backend;
}
}  // namespace Qt3DRender::Render

//  from ../qt3d/src/render/lights/light.cpp, line 51, as _ZNK10Qt3DRender6Render18RenderLightFunctor3getEN8Qt3DCore7QNodeIdE
namespace Qt3DRender::Render {
using namespace Qt3DCore;
inline Qt3DCore::QBackendNode *RenderLightFunctor::get(Qt3DCore::QNodeId id) const
{
    return m_managers->lightManager()->lookupResource(id);
}
}  // namespace Qt3DRender::Render

//  from ../qt3d/src/render/lights/light.cpp, line 56, as _ZNK10Qt3DRender6Render18RenderLightFunctor7destroyEN8Qt3DCore7QNodeIdE
namespace Qt3DRender::Render {
using namespace Qt3DCore;
inline void RenderLightFunctor::destroy(Qt3DCore::QNodeId id) const
{
    Light *backend = m_managers->lightManager()->getOrCreateResource(id);
    m_renderer->markDirty(AbstractRenderer::LightsDirty, backend);
    m_managers->lightManager()->releaseResource(id);
}
}  // namespace Qt3DRender::Render
//  -----------------------------------------------------------------------

//  Qt3DRender::Render::RenderLightFunctor::RenderLightFunctor(AbstractRender
//      er *renderer, NodeManagers *managers)
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::RenderLightFunctor *ritual_ZN10Qt3DRender6Render18RenderLightFunctorC1EPNS0_16AbstractRendererEPNS0_12NodeManagersE(
    Qt3DRender::Render::AbstractRenderer *renderer,
    Qt3DRender::Render::NodeManagers *managers) {
  return new Qt3DRender::Render::RenderLightFunctor(renderer, managers);
}

//  Qt3DCore::QBackendNode
//      *Qt3DRender::Render::RenderLightFunctor::create(Qt3DCore::QNodeId id)
//      const
extern "C" Q_DECL_EXPORT
Qt3DCore::QBackendNode *ritual_ZNK10Qt3DRender6Render18RenderLightFunctor6createEN8Qt3DCore7QNodeIdE(
    const Qt3DRender::Render::RenderLightFunctor *self,
    const Qt3DCore::QNodeId *id) {
  return self->create(*id);
}

//  Qt3DCore::QBackendNode
//      *Qt3DRender::Render::RenderLightFunctor::get(Qt3DCore::QNodeId id)
//      const
extern "C" Q_DECL_EXPORT
Qt3DCore::QBackendNode *ritual_ZNK10Qt3DRender6Render18RenderLightFunctor3getEN8Qt3DCore7QNodeIdE(
    const Qt3DRender::Render::RenderLightFunctor *self,
    const Qt3DCore::QNodeId *id) {
  return self->get(*id);
}

//  void Qt3DRender::Render::RenderLightFunctor::destroy(Qt3DCore::QNodeId
//      id) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK10Qt3DRender6Render18RenderLightFunctor7destroyEN8Qt3DCore7QNodeIdE(
    const Qt3DRender::Render::RenderLightFunctor *self,
    const Qt3DCore::QNodeId *id) {
  self->destroy(*id);
}

//  Qt3DRender::Render::RenderLightFunctor::~RenderLightFunctor()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render18RenderLightFunctorD1Ev(
    Qt3DRender::Render::RenderLightFunctor *self) {
  delete self;
}

//  Qt3DCore::QBackendNode
//      *Qt3DRender::Render::RenderLightFunctor::create(Qt3DCore::QNodeId id)
//      const
extern "C" Q_DECL_EXPORT
Qt3DCore::QBackendNode *ritual_own_ZNK10Qt3DRender6Render18RenderLightFunctor6createEN8Qt3DCore7QNodeIdE(
    const Qt3DRender::Render::RenderLightFunctor *self,
    const Qt3DCore::QNodeId *id) {
  return self->Qt3DRender::Render::RenderLightFunctor::create(*id);
}
