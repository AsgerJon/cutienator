//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/geometryrenderer_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/geometryrenderer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/qnodeid.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/private/geometryrenderer_p.h>
#include <Qt3DRender/private/geometryrenderermanager_p.h>
#include <Qt3DRender/private/qboundingvolume_p.h>
#include <Qt3DRender/private/qgeometryrenderer_p.h>
#include <Qt3DRender/private/qmesh_p.h>
#include <Qt3DCore/private/qnode_p.h>
#include <Qt3DCore/private/qservicelocator_p.h>
#include <QtCore/qcoreapplication.h>
#include <memory>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/render/geometry/geometryrenderer.cpp, line 184, as _ZN10Qt3DRender6Render23GeometryRendererFunctorC1EPNS0_16AbstractRendererEPNS0_23GeometryRendererManagerE
namespace Qt3DRender::Render {
using namespace Qt3DCore;
inline GeometryRendererFunctor::GeometryRendererFunctor(AbstractRenderer *renderer, GeometryRendererManager *manager)
    : m_manager(manager)
    , m_renderer(renderer)
{
}
}  // namespace Qt3DRender::Render

//  from ../qt3d/src/render/geometry/geometryrenderer.cpp, line 190, as _ZNK10Qt3DRender6Render23GeometryRendererFunctor6createEN8Qt3DCore7QNodeIdE
namespace Qt3DRender::Render {
using namespace Qt3DCore;
inline Qt3DCore::QBackendNode *GeometryRendererFunctor::create(Qt3DCore::QNodeId id) const
{
    GeometryRenderer *geometryRenderer = m_manager->getOrCreateResource(id);
    geometryRenderer->setManager(m_manager);
    geometryRenderer->setRenderer(m_renderer);
    return geometryRenderer;
}
}  // namespace Qt3DRender::Render

//  from ../qt3d/src/render/geometry/geometryrenderer.cpp, line 198, as _ZNK10Qt3DRender6Render23GeometryRendererFunctor3getEN8Qt3DCore7QNodeIdE
namespace Qt3DRender::Render {
using namespace Qt3DCore;
inline Qt3DCore::QBackendNode *GeometryRendererFunctor::get(Qt3DCore::QNodeId id) const
{
    return m_manager->lookupResource(id);
}
}  // namespace Qt3DRender::Render

//  from ../qt3d/src/render/geometry/geometryrenderer.cpp, line 203, as _ZNK10Qt3DRender6Render23GeometryRendererFunctor7destroyEN8Qt3DCore7QNodeIdE
namespace Qt3DRender::Render {
using namespace Qt3DCore;
inline void GeometryRendererFunctor::destroy(Qt3DCore::QNodeId id) const
{
    m_manager->releaseResource(id);
}
}  // namespace Qt3DRender::Render
//  -----------------------------------------------------------------------

//  Qt3DRender::Render::GeometryRendererFunctor::GeometryRendererFunctor(Abst
//      ractRenderer *renderer, GeometryRendererManager *manager)
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::GeometryRendererFunctor *ritual_ZN10Qt3DRender6Render23GeometryRendererFunctorC1EPNS0_16AbstractRendererEPNS0_23GeometryRendererManagerE(
    Qt3DRender::Render::AbstractRenderer *renderer,
    Qt3DRender::Render::GeometryRendererManager *manager) {
  return new Qt3DRender::Render::GeometryRendererFunctor(renderer, manager);
}

//  Qt3DCore::QBackendNode
//      *Qt3DRender::Render::GeometryRendererFunctor::create(Qt3DCore::QNodeI
//      d id) const
extern "C" Q_DECL_EXPORT
Qt3DCore::QBackendNode *ritual_ZNK10Qt3DRender6Render23GeometryRendererFunctor6createEN8Qt3DCore7QNodeIdE(
    const Qt3DRender::Render::GeometryRendererFunctor *self,
    const Qt3DCore::QNodeId *id) {
  return self->create(*id);
}

//  Qt3DCore::QBackendNode
//      *Qt3DRender::Render::GeometryRendererFunctor::get(Qt3DCore::QNodeId
//      id) const
extern "C" Q_DECL_EXPORT
Qt3DCore::QBackendNode *ritual_ZNK10Qt3DRender6Render23GeometryRendererFunctor3getEN8Qt3DCore7QNodeIdE(
    const Qt3DRender::Render::GeometryRendererFunctor *self,
    const Qt3DCore::QNodeId *id) {
  return self->get(*id);
}

//  void
//      Qt3DRender::Render::GeometryRendererFunctor::destroy(Qt3DCore::QNodeI
//      d id) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK10Qt3DRender6Render23GeometryRendererFunctor7destroyEN8Qt3DCore7QNodeIdE(
    const Qt3DRender::Render::GeometryRendererFunctor *self,
    const Qt3DCore::QNodeId *id) {
  self->destroy(*id);
}

//  Qt3DRender::Render::GeometryRendererFunctor::~GeometryRendererFunctor()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render23GeometryRendererFunctorD1Ev(
    Qt3DRender::Render::GeometryRendererFunctor *self) {
  delete self;
}

//  Qt3DCore::QBackendNode
//      *Qt3DRender::Render::GeometryRendererFunctor::create(Qt3DCore::QNodeI
//      d id) const
extern "C" Q_DECL_EXPORT
Qt3DCore::QBackendNode *ritual_own_ZNK10Qt3DRender6Render23GeometryRendererFunctor6createEN8Qt3DCore7QNodeIdE(
    const Qt3DRender::Render::GeometryRendererFunctor *self,
    const Qt3DCore::QNodeId *id) {
  return self->Qt3DRender::Render::GeometryRendererFunctor::create(*id);
}

//  Qt3DCore::QBackendNode
//      *Qt3DRender::Render::GeometryRendererFunctor::get(Qt3DCore::QNodeId
//      id) const
extern "C" Q_DECL_EXPORT
Qt3DCore::QBackendNode *ritual_own_ZNK10Qt3DRender6Render23GeometryRendererFunctor3getEN8Qt3DCore7QNodeIdE(
    const Qt3DRender::Render::GeometryRendererFunctor *self,
    const Qt3DCore::QNodeId *id) {
  return self->Qt3DRender::Render::GeometryRendererFunctor::get(*id);
}

//  void
//      Qt3DRender::Render::GeometryRendererFunctor::destroy(Qt3DCore::QNodeI
//      d id) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK10Qt3DRender6Render23GeometryRendererFunctor7destroyEN8Qt3DCore7QNodeIdE(
    const Qt3DRender::Render::GeometryRendererFunctor *self,
    const Qt3DCore::QNodeId *id) {
  self->Qt3DRender::Render::GeometryRendererFunctor::destroy(*id);
}
