//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/skeleton_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/skeleton_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/qnodeid.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/private/skeleton_p.h>
#include <QtCore/QCoreApplication>
#include <QtCore/QFile>
#include <QtCore/QFileInfo>
#include <Qt3DCore/qjoint.h>
#include <Qt3DRender/private/abstractrenderer_p.h>
#include <Qt3DRender/private/managers_p.h>
#include <Qt3DRender/private/nodemanagers_p.h>
#include <Qt3DRender/private/renderlogging_p.h>
#include <Qt3DCore/private/qskeleton_p.h>
#include <Qt3DCore/private/qskeletonloader_p.h>
#include <Qt3DCore/private/qmath3d_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/render/geometry/skeleton.cpp, line 161, as _ZN10Qt3DRender6Render15SkeletonFunctorC1EPNS0_16AbstractRendererEPNS0_15SkeletonManagerEPNS0_12JointManagerE
namespace Qt3DRender::Render {
using namespace Qt3DCore;
inline SkeletonFunctor::SkeletonFunctor(AbstractRenderer *renderer,
                                 SkeletonManager *skeletonManager,
                                 JointManager *jointManager)
    : m_renderer(renderer)
    , m_skeletonManager(skeletonManager)
    , m_jointManager(jointManager)
{
}
}  // namespace Qt3DRender::Render

//  from ../qt3d/src/render/geometry/skeleton.cpp, line 170, as _ZNK10Qt3DRender6Render15SkeletonFunctor6createEN8Qt3DCore7QNodeIdE
namespace Qt3DRender::Render {
using namespace Qt3DCore;
inline Qt3DCore::QBackendNode *SkeletonFunctor::create(Qt3DCore::QNodeId id) const
{
    Skeleton *backend = m_skeletonManager->getOrCreateResource(id);
    backend->setRenderer(m_renderer);
    backend->setSkeletonManager(m_skeletonManager);
    backend->setJointManager(m_jointManager);
    return backend;
}
}  // namespace Qt3DRender::Render

//  from ../qt3d/src/render/geometry/skeleton.cpp, line 179, as _ZNK10Qt3DRender6Render15SkeletonFunctor3getEN8Qt3DCore7QNodeIdE
namespace Qt3DRender::Render {
using namespace Qt3DCore;
inline Qt3DCore::QBackendNode *SkeletonFunctor::get(Qt3DCore::QNodeId id) const
{
    return m_skeletonManager->lookupResource(id);
}
}  // namespace Qt3DRender::Render

//  from ../qt3d/src/render/geometry/skeleton.cpp, line 184, as _ZNK10Qt3DRender6Render15SkeletonFunctor7destroyEN8Qt3DCore7QNodeIdE
namespace Qt3DRender::Render {
using namespace Qt3DCore;
inline void SkeletonFunctor::destroy(Qt3DCore::QNodeId id) const
{
    m_skeletonManager->releaseResource(id);
}
}  // namespace Qt3DRender::Render
//  -----------------------------------------------------------------------

//  Qt3DRender::Render::SkeletonFunctor::SkeletonFunctor(AbstractRenderer
//      *renderer, SkeletonManager *skeletonManager, JointManager
//      *jointManager)
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::SkeletonFunctor *ritual_ZN10Qt3DRender6Render15SkeletonFunctorC1EPNS0_16AbstractRendererEPNS0_15SkeletonManagerEPNS0_12JointManagerE(
    Qt3DRender::Render::AbstractRenderer *renderer,
    Qt3DRender::Render::SkeletonManager *skeletonManager,
    Qt3DRender::Render::JointManager *jointManager) {
  return new Qt3DRender::Render::SkeletonFunctor(
      renderer,
      skeletonManager,
      jointManager);
}

//  Qt3DCore::QBackendNode
//      *Qt3DRender::Render::SkeletonFunctor::create(Qt3DCore::QNodeId id)
//      const
extern "C" Q_DECL_EXPORT
Qt3DCore::QBackendNode *ritual_ZNK10Qt3DRender6Render15SkeletonFunctor6createEN8Qt3DCore7QNodeIdE(
    const Qt3DRender::Render::SkeletonFunctor *self,
    const Qt3DCore::QNodeId *id) {
  return self->create(*id);
}

//  Qt3DCore::QBackendNode
//      *Qt3DRender::Render::SkeletonFunctor::get(Qt3DCore::QNodeId id) const
extern "C" Q_DECL_EXPORT
Qt3DCore::QBackendNode *ritual_ZNK10Qt3DRender6Render15SkeletonFunctor3getEN8Qt3DCore7QNodeIdE(
    const Qt3DRender::Render::SkeletonFunctor *self,
    const Qt3DCore::QNodeId *id) {
  return self->get(*id);
}

//  void Qt3DRender::Render::SkeletonFunctor::destroy(Qt3DCore::QNodeId id)
//      const
extern "C" Q_DECL_EXPORT
void ritual_ZNK10Qt3DRender6Render15SkeletonFunctor7destroyEN8Qt3DCore7QNodeIdE(
    const Qt3DRender::Render::SkeletonFunctor *self,
    const Qt3DCore::QNodeId *id) {
  self->destroy(*id);
}

//  Qt3DRender::Render::SkeletonFunctor::~SkeletonFunctor()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render15SkeletonFunctorD1Ev(
    Qt3DRender::Render::SkeletonFunctor *self) {
  delete self;
}
