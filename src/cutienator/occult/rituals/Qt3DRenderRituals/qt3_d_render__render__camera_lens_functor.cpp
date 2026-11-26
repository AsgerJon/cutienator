//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/cameralens_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/cameralens_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/qnodeid.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/private/cameralens_p.h>
#include <Qt3DRender/qcameralens.h>
#include <Qt3DRender/qrenderaspect.h>
#include <Qt3DRender/private/nodemanagers_p.h>
#include <Qt3DRender/private/managers_p.h>
#include <Qt3DRender/private/renderlogging_p.h>
#include <Qt3DRender/private/abstractrenderer_p.h>
#include <Qt3DRender/private/entity_p.h>
#include <Qt3DRender/private/sphere_p.h>
#include <Qt3DRender/private/computefilteredboundingvolumejob_p.h>
#include <Qt3DRender/private/renderlogging_p.h>
#include <Qt3DRender/private/qrenderaspect_p.h>
#include <Qt3DCore/qentity.h>
#include <Qt3DCore/qtransform.h>
#include <Qt3DCore/private/qaspectmanager_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/render/backend/cameralens.cpp, line 186, as _ZNK10Qt3DRender6Render17CameraLensFunctor6createEN8Qt3DCore7QNodeIdE
namespace Qt3DRender::Render {
using namespace Qt3DCore;
inline QBackendNode *CameraLensFunctor::create(const QNodeId id) const
{
    CameraLens *backend = m_manager->getOrCreateResource(id);
    backend->setRenderer(m_renderer);
    backend->setRenderAspect(m_renderAspect);
    return backend;
}
}  // namespace Qt3DRender::Render

//  from ../qt3d/src/render/backend/cameralens.cpp, line 194, as _ZNK10Qt3DRender6Render17CameraLensFunctor3getEN8Qt3DCore7QNodeIdE
namespace Qt3DRender::Render {
using namespace Qt3DCore;
inline QBackendNode *CameraLensFunctor::get(QNodeId id) const
{
    return m_manager->lookupResource(id);
}
}  // namespace Qt3DRender::Render

//  from ../qt3d/src/render/backend/cameralens.cpp, line 199, as _ZNK10Qt3DRender6Render17CameraLensFunctor7destroyEN8Qt3DCore7QNodeIdE
namespace Qt3DRender::Render {
using namespace Qt3DCore;
inline void CameraLensFunctor::destroy(QNodeId id) const
{
    m_manager->releaseResource(id);
}
}  // namespace Qt3DRender::Render
//  -----------------------------------------------------------------------

//  Qt3DCore::QBackendNode
//      *Qt3DRender::Render::CameraLensFunctor::create(Qt3DCore::QNodeId id)
//      const
extern "C" Q_DECL_EXPORT
Qt3DCore::QBackendNode *ritual_ZNK10Qt3DRender6Render17CameraLensFunctor6createEN8Qt3DCore7QNodeIdE(
    const Qt3DRender::Render::CameraLensFunctor *self,
    const Qt3DCore::QNodeId *id) {
  return self->create(*id);
}

//  Qt3DCore::QBackendNode
//      *Qt3DRender::Render::CameraLensFunctor::get(Qt3DCore::QNodeId id)
//      const
extern "C" Q_DECL_EXPORT
Qt3DCore::QBackendNode *ritual_ZNK10Qt3DRender6Render17CameraLensFunctor3getEN8Qt3DCore7QNodeIdE(
    const Qt3DRender::Render::CameraLensFunctor *self,
    const Qt3DCore::QNodeId *id) {
  return self->get(*id);
}

//  void Qt3DRender::Render::CameraLensFunctor::destroy(Qt3DCore::QNodeId id)
//      const
extern "C" Q_DECL_EXPORT
void ritual_ZNK10Qt3DRender6Render17CameraLensFunctor7destroyEN8Qt3DCore7QNodeIdE(
    const Qt3DRender::Render::CameraLensFunctor *self,
    const Qt3DCore::QNodeId *id) {
  self->destroy(*id);
}

//  Qt3DRender::Render::CameraLensFunctor::~CameraLensFunctor()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render17CameraLensFunctorD1Ev(
    Qt3DRender::Render::CameraLensFunctor *self) {
  delete self;
}

//  Qt3DCore::QBackendNode
//      *Qt3DRender::Render::CameraLensFunctor::create(Qt3DCore::QNodeId id)
//      const
extern "C" Q_DECL_EXPORT
Qt3DCore::QBackendNode *ritual_own_ZNK10Qt3DRender6Render17CameraLensFunctor6createEN8Qt3DCore7QNodeIdE(
    const Qt3DRender::Render::CameraLensFunctor *self,
    const Qt3DCore::QNodeId *id) {
  return self->Qt3DRender::Render::CameraLensFunctor::create(*id);
}

//  Qt3DCore::QBackendNode
//      *Qt3DRender::Render::CameraLensFunctor::get(Qt3DCore::QNodeId id)
//      const
extern "C" Q_DECL_EXPORT
Qt3DCore::QBackendNode *ritual_own_ZNK10Qt3DRender6Render17CameraLensFunctor3getEN8Qt3DCore7QNodeIdE(
    const Qt3DRender::Render::CameraLensFunctor *self,
    const Qt3DCore::QNodeId *id) {
  return self->Qt3DRender::Render::CameraLensFunctor::get(*id);
}

//  void Qt3DRender::Render::CameraLensFunctor::destroy(Qt3DCore::QNodeId id)
//      const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK10Qt3DRender6Render17CameraLensFunctor7destroyEN8Qt3DCore7QNodeIdE(
    const Qt3DRender::Render::CameraLensFunctor *self,
    const Qt3DCore::QNodeId *id) {
  self->Qt3DRender::Render::CameraLensFunctor::destroy(*id);
}
