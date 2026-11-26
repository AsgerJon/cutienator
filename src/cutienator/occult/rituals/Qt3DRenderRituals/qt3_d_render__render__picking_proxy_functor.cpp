//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/pickingproxy_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/pickingproxy_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/qnodeid.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/private/pickingproxy_p.h>
#include <Qt3DRender/private/managers_p.h>
#include <Qt3DRender/private/qpickingproxy_p.h>
#include <Qt3DCore/private/qgeometryview_p.h>
#include <Qt3DCore/private/qnode_p.h>
#include <memory>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/render/geometry/pickingproxy.cpp, line 115, as _ZN10Qt3DRender6Render19PickingProxyFunctorC1EPNS0_16AbstractRendererEPNS0_19PickingProxyManagerE
namespace Qt3DRender::Render {
using namespace Qt3DCore;
inline PickingProxyFunctor::PickingProxyFunctor(AbstractRenderer *renderer, PickingProxyManager *manager)
    : m_manager(manager)
    , m_renderer(renderer)
{
}
}  // namespace Qt3DRender::Render

//  from ../qt3d/src/render/geometry/pickingproxy.cpp, line 121, as _ZNK10Qt3DRender6Render19PickingProxyFunctor6createEN8Qt3DCore7QNodeIdE
namespace Qt3DRender::Render {
using namespace Qt3DCore;
inline Qt3DCore::QBackendNode *PickingProxyFunctor::create(Qt3DCore::QNodeId id) const
{
    PickingProxy *node = m_manager->getOrCreateResource(id);
    node->setManager(m_manager);
    node->setRenderer(m_renderer);
    return node;
}
}  // namespace Qt3DRender::Render

//  from ../qt3d/src/render/geometry/pickingproxy.cpp, line 129, as _ZNK10Qt3DRender6Render19PickingProxyFunctor3getEN8Qt3DCore7QNodeIdE
namespace Qt3DRender::Render {
using namespace Qt3DCore;
inline Qt3DCore::QBackendNode *PickingProxyFunctor::get(Qt3DCore::QNodeId id) const
{
    return m_manager->lookupResource(id);
}
}  // namespace Qt3DRender::Render

//  from ../qt3d/src/render/geometry/pickingproxy.cpp, line 134, as _ZNK10Qt3DRender6Render19PickingProxyFunctor7destroyEN8Qt3DCore7QNodeIdE
namespace Qt3DRender::Render {
using namespace Qt3DCore;
inline void PickingProxyFunctor::destroy(Qt3DCore::QNodeId id) const
{
    m_manager->releaseResource(id);
}
}  // namespace Qt3DRender::Render
//  -----------------------------------------------------------------------

//  Qt3DRender::Render::PickingProxyFunctor::PickingProxyFunctor(AbstractRend
//      erer *renderer, PickingProxyManager *manager)
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::PickingProxyFunctor *ritual_ZN10Qt3DRender6Render19PickingProxyFunctorC1EPNS0_16AbstractRendererEPNS0_19PickingProxyManagerE(
    Qt3DRender::Render::AbstractRenderer *renderer,
    Qt3DRender::Render::PickingProxyManager *manager) {
  return new Qt3DRender::Render::PickingProxyFunctor(renderer, manager);
}

//  Qt3DCore::QBackendNode
//      *Qt3DRender::Render::PickingProxyFunctor::create(Qt3DCore::QNodeId
//      id) const
extern "C" Q_DECL_EXPORT
Qt3DCore::QBackendNode *ritual_ZNK10Qt3DRender6Render19PickingProxyFunctor6createEN8Qt3DCore7QNodeIdE(
    const Qt3DRender::Render::PickingProxyFunctor *self,
    const Qt3DCore::QNodeId *id) {
  return self->create(*id);
}

//  Qt3DCore::QBackendNode
//      *Qt3DRender::Render::PickingProxyFunctor::get(Qt3DCore::QNodeId id)
//      const
extern "C" Q_DECL_EXPORT
Qt3DCore::QBackendNode *ritual_ZNK10Qt3DRender6Render19PickingProxyFunctor3getEN8Qt3DCore7QNodeIdE(
    const Qt3DRender::Render::PickingProxyFunctor *self,
    const Qt3DCore::QNodeId *id) {
  return self->get(*id);
}

//  void Qt3DRender::Render::PickingProxyFunctor::destroy(Qt3DCore::QNodeId
//      id) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK10Qt3DRender6Render19PickingProxyFunctor7destroyEN8Qt3DCore7QNodeIdE(
    const Qt3DRender::Render::PickingProxyFunctor *self,
    const Qt3DCore::QNodeId *id) {
  self->destroy(*id);
}

//  Qt3DRender::Render::PickingProxyFunctor::~PickingProxyFunctor()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render19PickingProxyFunctorD1Ev(
    Qt3DRender::Render::PickingProxyFunctor *self) {
  delete self;
}

//  Qt3DCore::QBackendNode
//      *Qt3DRender::Render::PickingProxyFunctor::create(Qt3DCore::QNodeId
//      id) const
extern "C" Q_DECL_EXPORT
Qt3DCore::QBackendNode *ritual_own_ZNK10Qt3DRender6Render19PickingProxyFunctor6createEN8Qt3DCore7QNodeIdE(
    const Qt3DRender::Render::PickingProxyFunctor *self,
    const Qt3DCore::QNodeId *id) {
  return self->Qt3DRender::Render::PickingProxyFunctor::create(*id);
}

//  Qt3DCore::QBackendNode
//      *Qt3DRender::Render::PickingProxyFunctor::get(Qt3DCore::QNodeId id)
//      const
extern "C" Q_DECL_EXPORT
Qt3DCore::QBackendNode *ritual_own_ZNK10Qt3DRender6Render19PickingProxyFunctor3getEN8Qt3DCore7QNodeIdE(
    const Qt3DRender::Render::PickingProxyFunctor *self,
    const Qt3DCore::QNodeId *id) {
  return self->Qt3DRender::Render::PickingProxyFunctor::get(*id);
}

//  void Qt3DRender::Render::PickingProxyFunctor::destroy(Qt3DCore::QNodeId
//      id) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK10Qt3DRender6Render19PickingProxyFunctor7destroyEN8Qt3DCore7QNodeIdE(
    const Qt3DRender::Render::PickingProxyFunctor *self,
    const Qt3DCore::QNodeId *id) {
  self->Qt3DRender::Render::PickingProxyFunctor::destroy(*id);
}
