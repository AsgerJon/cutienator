//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/buffer_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/buffer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/qnodeid.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/private/buffer_p.h>
#include <Qt3DCore/private/qbuffer_p.h>
#include <Qt3DRender/private/buffermanager_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/render/geometry/buffer.cpp, line 119, as _ZN10Qt3DRender6Render13BufferFunctorC1EPNS0_16AbstractRendererEPNS0_13BufferManagerE
namespace Qt3DRender::Render {
inline BufferFunctor::BufferFunctor(AbstractRenderer *renderer, BufferManager *manager)
    : m_manager(manager)
    , m_renderer(renderer)
{
}
}  // namespace Qt3DRender::Render

//  from ../qt3d/src/render/geometry/buffer.cpp, line 125, as _ZNK10Qt3DRender6Render13BufferFunctor6createEN8Qt3DCore7QNodeIdE
namespace Qt3DRender::Render {
inline Qt3DCore::QBackendNode *BufferFunctor::create(Qt3DCore::QNodeId id) const
{
    Buffer *buffer = m_manager->getOrCreateResource(id);
    buffer->setManager(m_manager);
    buffer->setRenderer(m_renderer);
    return buffer;
}
}  // namespace Qt3DRender::Render

//  from ../qt3d/src/render/geometry/buffer.cpp, line 133, as _ZNK10Qt3DRender6Render13BufferFunctor3getEN8Qt3DCore7QNodeIdE
namespace Qt3DRender::Render {
inline Qt3DCore::QBackendNode *BufferFunctor::get(Qt3DCore::QNodeId id) const
{
    return m_manager->lookupResource(id);
}
}  // namespace Qt3DRender::Render

//  from ../qt3d/src/render/geometry/buffer.cpp, line 138, as _ZNK10Qt3DRender6Render13BufferFunctor7destroyEN8Qt3DCore7QNodeIdE
namespace Qt3DRender::Render {
inline void BufferFunctor::destroy(Qt3DCore::QNodeId id) const
{
    if (m_manager->contains(id)) {
        m_manager->removeBufferReference(id);
        m_manager->releaseResource(id);
    }
}
}  // namespace Qt3DRender::Render
//  -----------------------------------------------------------------------

//  Qt3DRender::Render::BufferFunctor::BufferFunctor(AbstractRenderer
//      *renderer, BufferManager *manager)
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::BufferFunctor *ritual_ZN10Qt3DRender6Render13BufferFunctorC1EPNS0_16AbstractRendererEPNS0_13BufferManagerE(
    Qt3DRender::Render::AbstractRenderer *renderer,
    Qt3DRender::Render::BufferManager *manager) {
  return new Qt3DRender::Render::BufferFunctor(renderer, manager);
}

//  Qt3DCore::QBackendNode
//      *Qt3DRender::Render::BufferFunctor::create(Qt3DCore::QNodeId id)
//      const
extern "C" Q_DECL_EXPORT
Qt3DCore::QBackendNode *ritual_ZNK10Qt3DRender6Render13BufferFunctor6createEN8Qt3DCore7QNodeIdE(
    const Qt3DRender::Render::BufferFunctor *self,
    const Qt3DCore::QNodeId *id) {
  return self->create(*id);
}

//  Qt3DCore::QBackendNode
//      *Qt3DRender::Render::BufferFunctor::get(Qt3DCore::QNodeId id) const
extern "C" Q_DECL_EXPORT
Qt3DCore::QBackendNode *ritual_ZNK10Qt3DRender6Render13BufferFunctor3getEN8Qt3DCore7QNodeIdE(
    const Qt3DRender::Render::BufferFunctor *self,
    const Qt3DCore::QNodeId *id) {
  return self->get(*id);
}

//  void Qt3DRender::Render::BufferFunctor::destroy(Qt3DCore::QNodeId id)
//      const
extern "C" Q_DECL_EXPORT
void ritual_ZNK10Qt3DRender6Render13BufferFunctor7destroyEN8Qt3DCore7QNodeIdE(
    const Qt3DRender::Render::BufferFunctor *self,
    const Qt3DCore::QNodeId *id) {
  self->destroy(*id);
}

//  Qt3DRender::Render::BufferFunctor::~BufferFunctor()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render13BufferFunctorD1Ev(
    Qt3DRender::Render::BufferFunctor *self) {
  delete self;
}

//  Qt3DCore::QBackendNode
//      *Qt3DRender::Render::BufferFunctor::create(Qt3DCore::QNodeId id)
//      const
extern "C" Q_DECL_EXPORT
Qt3DCore::QBackendNode *ritual_own_ZNK10Qt3DRender6Render13BufferFunctor6createEN8Qt3DCore7QNodeIdE(
    const Qt3DRender::Render::BufferFunctor *self,
    const Qt3DCore::QNodeId *id) {
  return self->Qt3DRender::Render::BufferFunctor::create(*id);
}

//  Qt3DCore::QBackendNode
//      *Qt3DRender::Render::BufferFunctor::get(Qt3DCore::QNodeId id) const
extern "C" Q_DECL_EXPORT
Qt3DCore::QBackendNode *ritual_own_ZNK10Qt3DRender6Render13BufferFunctor3getEN8Qt3DCore7QNodeIdE(
    const Qt3DRender::Render::BufferFunctor *self,
    const Qt3DCore::QNodeId *id) {
  return self->Qt3DRender::Render::BufferFunctor::get(*id);
}

//  void Qt3DRender::Render::BufferFunctor::destroy(Qt3DCore::QNodeId id)
//      const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK10Qt3DRender6Render13BufferFunctor7destroyEN8Qt3DCore7QNodeIdE(
    const Qt3DRender::Render::BufferFunctor *self,
    const Qt3DCore::QNodeId *id) {
  self->Qt3DRender::Render::BufferFunctor::destroy(*id);
}
