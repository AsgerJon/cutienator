//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/rendertarget_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/rendertarget_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/qnodeid.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/private/rendertarget_p.h>
#include <Qt3DRender/qrendertarget.h>
#include <Qt3DRender/private/qrendertarget_p.h>
#include <Qt3DRender/qrendertargetoutput.h>
#include <Qt3DRender/private/managers_p.h>
#include <QtCore/QVariant>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/render/backend/rendertarget.cpp, line 65, as _ZN10Qt3DRender6Render19RenderTargetFunctorC1EPNS0_16AbstractRendererEPNS0_19RenderTargetManagerE
namespace Qt3DRender::Render {
using namespace Qt3DCore;
inline RenderTargetFunctor::RenderTargetFunctor(AbstractRenderer *renderer, RenderTargetManager *manager)
    : m_renderer(renderer)
    , m_renderTargetManager(manager)
{
}
}  // namespace Qt3DRender::Render

//  from ../qt3d/src/render/backend/rendertarget.cpp, line 71, as _ZNK10Qt3DRender6Render19RenderTargetFunctor6createEN8Qt3DCore7QNodeIdE
namespace Qt3DRender::Render {
using namespace Qt3DCore;
inline QBackendNode *RenderTargetFunctor::create(QNodeId id) const
{
    RenderTarget *backend = m_renderTargetManager->getOrCreateResource(id);
    // Remove from the list of ids to destroy in case we were added to it
    m_renderTargetManager->removeRenderTargetToCleanup(id);
    backend->setRenderer(m_renderer);
    return backend;
}
}  // namespace Qt3DRender::Render

//  from ../qt3d/src/render/backend/rendertarget.cpp, line 80, as _ZNK10Qt3DRender6Render19RenderTargetFunctor3getEN8Qt3DCore7QNodeIdE
namespace Qt3DRender::Render {
using namespace Qt3DCore;
inline QBackendNode *RenderTargetFunctor::get(QNodeId id) const
{
    return m_renderTargetManager->lookupResource(id);
}
}  // namespace Qt3DRender::Render

//  from ../qt3d/src/render/backend/rendertarget.cpp, line 85, as _ZNK10Qt3DRender6Render19RenderTargetFunctor7destroyEN8Qt3DCore7QNodeIdE
namespace Qt3DRender::Render {
using namespace Qt3DCore;
inline void RenderTargetFunctor::destroy(QNodeId id) const
{
    // We add ourselves to the dirty list to tell the renderer that this rendertarget has been destroyed
    m_renderTargetManager->addRenderTargetIdToCleanup(id);
    m_renderTargetManager->releaseResource(id);
}
}  // namespace Qt3DRender::Render
//  -----------------------------------------------------------------------

//  Qt3DRender::Render::RenderTargetFunctor::RenderTargetFunctor(AbstractRend
//      erer *renderer, RenderTargetManager *manager)
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::RenderTargetFunctor *ritual_ZN10Qt3DRender6Render19RenderTargetFunctorC1EPNS0_16AbstractRendererEPNS0_19RenderTargetManagerE(
    Qt3DRender::Render::AbstractRenderer *renderer,
    Qt3DRender::Render::RenderTargetManager *manager) {
  return new Qt3DRender::Render::RenderTargetFunctor(renderer, manager);
}

//  Qt3DCore::QBackendNode
//      *Qt3DRender::Render::RenderTargetFunctor::create(Qt3DCore::QNodeId
//      id) const
extern "C" Q_DECL_EXPORT
Qt3DCore::QBackendNode *ritual_ZNK10Qt3DRender6Render19RenderTargetFunctor6createEN8Qt3DCore7QNodeIdE(
    const Qt3DRender::Render::RenderTargetFunctor *self,
    const Qt3DCore::QNodeId *id) {
  return self->create(*id);
}

//  Qt3DCore::QBackendNode
//      *Qt3DRender::Render::RenderTargetFunctor::get(Qt3DCore::QNodeId id)
//      const
extern "C" Q_DECL_EXPORT
Qt3DCore::QBackendNode *ritual_ZNK10Qt3DRender6Render19RenderTargetFunctor3getEN8Qt3DCore7QNodeIdE(
    const Qt3DRender::Render::RenderTargetFunctor *self,
    const Qt3DCore::QNodeId *id) {
  return self->get(*id);
}

//  void Qt3DRender::Render::RenderTargetFunctor::destroy(Qt3DCore::QNodeId
//      id) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK10Qt3DRender6Render19RenderTargetFunctor7destroyEN8Qt3DCore7QNodeIdE(
    const Qt3DRender::Render::RenderTargetFunctor *self,
    const Qt3DCore::QNodeId *id) {
  self->destroy(*id);
}

//  Qt3DRender::Render::RenderTargetFunctor::~RenderTargetFunctor()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render19RenderTargetFunctorD1Ev(
    Qt3DRender::Render::RenderTargetFunctor *self) {
  delete self;
}
