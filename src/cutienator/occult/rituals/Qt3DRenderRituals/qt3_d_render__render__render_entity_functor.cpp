//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/entity_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/entity_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/qnodeid.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/private/entity_p.h>
#include <Qt3DRender/private/entity_p_p.h>
#include <Qt3DRender/private/managers_p.h>
#include <Qt3DRender/private/nodemanagers_p.h>
#include <Qt3DRender/qabstractlight.h>
#include <Qt3DRender/qenvironmentlight.h>
#include <Qt3DRender/qlayer.h>
#include <Qt3DRender/qlevelofdetail.h>
#include <Qt3DRender/qraycaster.h>
#include <Qt3DRender/qscreenraycaster.h>
#include <Qt3DRender/qmaterial.h>
#include <Qt3DRender/qmesh.h>
#include <Qt3DRender/private/renderlogging_p.h>
#include <Qt3DRender/private/sphere_p.h>
#include <Qt3DRender/qshaderdata.h>
#include <Qt3DRender/qgeometryrenderer.h>
#include <Qt3DRender/qpickingproxy.h>
#include <Qt3DRender/qobjectpicker.h>
#include <Qt3DRender/qcomputecommand.h>
#include <Qt3DRender/private/geometryrenderermanager_p.h>
#include <Qt3DRender/private/armature_p.h>
#include <Qt3DRender/qcameralens.h>
#include <Qt3DCore/qarmature.h>
#include <Qt3DCore/qentity.h>
#include <Qt3DCore/qtransform.h>
#include <Qt3DCore/private/qentity_p.h>
#include <QtGui/QMatrix4x4>
#include <QtCore/QString>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/render/backend/entity.cpp, line 396, as _ZN10Qt3DRender6Render19RenderEntityFunctorC1EPNS0_16AbstractRendererEPNS0_12NodeManagersE
namespace Qt3DRender::Render {
using namespace Qt3DCore;
inline RenderEntityFunctor::RenderEntityFunctor(AbstractRenderer *renderer, NodeManagers *manager)
    : m_nodeManagers(manager)
    , m_renderer(renderer)
{
}
}  // namespace Qt3DRender::Render

//  from ../qt3d/src/render/backend/entity.cpp, line 402, as _ZNK10Qt3DRender6Render19RenderEntityFunctor6createEN8Qt3DCore7QNodeIdE
namespace Qt3DRender::Render {
using namespace Qt3DCore;
inline Qt3DCore::QBackendNode *RenderEntityFunctor::create(Qt3DCore::QNodeId id) const
{
    HEntity renderNodeHandle = m_nodeManagers->renderNodesManager()->getOrAcquireHandle(id);
    Entity *entity = m_nodeManagers->renderNodesManager()->data(renderNodeHandle);
    entity->setNodeManagers(m_nodeManagers);
    entity->setHandle(renderNodeHandle);
    entity->setRenderer(m_renderer);
    return entity;
}
}  // namespace Qt3DRender::Render

//  from ../qt3d/src/render/backend/entity.cpp, line 412, as _ZNK10Qt3DRender6Render19RenderEntityFunctor3getEN8Qt3DCore7QNodeIdE
namespace Qt3DRender::Render {
using namespace Qt3DCore;
inline Qt3DCore::QBackendNode *RenderEntityFunctor::get(Qt3DCore::QNodeId id) const
{
    return m_nodeManagers->renderNodesManager()->lookupResource(id);
}
}  // namespace Qt3DRender::Render

//  from ../qt3d/src/render/backend/entity.cpp, line 417, as _ZNK10Qt3DRender6Render19RenderEntityFunctor7destroyEN8Qt3DCore7QNodeIdE
namespace Qt3DRender::Render {
using namespace Qt3DCore;
inline void RenderEntityFunctor::destroy(Qt3DCore::QNodeId id) const
{
    m_nodeManagers->renderNodesManager()->releaseResource(id);
}
}  // namespace Qt3DRender::Render
//  -----------------------------------------------------------------------

//  Qt3DRender::Render::RenderEntityFunctor::RenderEntityFunctor(AbstractRend
//      erer *renderer, NodeManagers *manager)
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::RenderEntityFunctor *ritual_ZN10Qt3DRender6Render19RenderEntityFunctorC1EPNS0_16AbstractRendererEPNS0_12NodeManagersE(
    Qt3DRender::Render::AbstractRenderer *renderer,
    Qt3DRender::Render::NodeManagers *manager) {
  return new Qt3DRender::Render::RenderEntityFunctor(renderer, manager);
}

//  Qt3DCore::QBackendNode
//      *Qt3DRender::Render::RenderEntityFunctor::create(Qt3DCore::QNodeId
//      id) const
extern "C" Q_DECL_EXPORT
Qt3DCore::QBackendNode *ritual_ZNK10Qt3DRender6Render19RenderEntityFunctor6createEN8Qt3DCore7QNodeIdE(
    const Qt3DRender::Render::RenderEntityFunctor *self,
    const Qt3DCore::QNodeId *id) {
  return self->create(*id);
}

//  Qt3DCore::QBackendNode
//      *Qt3DRender::Render::RenderEntityFunctor::get(Qt3DCore::QNodeId id)
//      const
extern "C" Q_DECL_EXPORT
Qt3DCore::QBackendNode *ritual_ZNK10Qt3DRender6Render19RenderEntityFunctor3getEN8Qt3DCore7QNodeIdE(
    const Qt3DRender::Render::RenderEntityFunctor *self,
    const Qt3DCore::QNodeId *id) {
  return self->get(*id);
}

//  void Qt3DRender::Render::RenderEntityFunctor::destroy(Qt3DCore::QNodeId
//      id) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK10Qt3DRender6Render19RenderEntityFunctor7destroyEN8Qt3DCore7QNodeIdE(
    const Qt3DRender::Render::RenderEntityFunctor *self,
    const Qt3DCore::QNodeId *id) {
  self->destroy(*id);
}

//  Qt3DRender::Render::RenderEntityFunctor::~RenderEntityFunctor()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render19RenderEntityFunctorD1Ev(
    Qt3DRender::Render::RenderEntityFunctor *self) {
  delete self;
}

//  Qt3DCore::QBackendNode
//      *Qt3DRender::Render::RenderEntityFunctor::create(Qt3DCore::QNodeId
//      id) const
extern "C" Q_DECL_EXPORT
Qt3DCore::QBackendNode *ritual_own_ZNK10Qt3DRender6Render19RenderEntityFunctor6createEN8Qt3DCore7QNodeIdE(
    const Qt3DRender::Render::RenderEntityFunctor *self,
    const Qt3DCore::QNodeId *id) {
  return self->Qt3DRender::Render::RenderEntityFunctor::create(*id);
}

//  Qt3DCore::QBackendNode
//      *Qt3DRender::Render::RenderEntityFunctor::get(Qt3DCore::QNodeId id)
//      const
extern "C" Q_DECL_EXPORT
Qt3DCore::QBackendNode *ritual_own_ZNK10Qt3DRender6Render19RenderEntityFunctor3getEN8Qt3DCore7QNodeIdE(
    const Qt3DRender::Render::RenderEntityFunctor *self,
    const Qt3DCore::QNodeId *id) {
  return self->Qt3DRender::Render::RenderEntityFunctor::get(*id);
}

//  void Qt3DRender::Render::RenderEntityFunctor::destroy(Qt3DCore::QNodeId
//      id) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK10Qt3DRender6Render19RenderEntityFunctor7destroyEN8Qt3DCore7QNodeIdE(
    const Qt3DRender::Render::RenderEntityFunctor *self,
    const Qt3DCore::QNodeId *id) {
  self->Qt3DRender::Render::RenderEntityFunctor::destroy(*id);
}
