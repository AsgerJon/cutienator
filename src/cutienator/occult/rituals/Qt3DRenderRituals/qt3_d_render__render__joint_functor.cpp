//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/joint_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/joint_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/qnodeid.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/private/joint_p.h>
#include <Qt3DRender/private/managers_p.h>
#include <Qt3DCore/QJoint>
#include <Qt3DCore/private/qjoint_p.h>
#include <algorithm>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/render/geometry/joint.cpp, line 85, as _ZN10Qt3DRender6Render12JointFunctorC1EPNS0_16AbstractRendererEPNS0_12JointManagerEPNS0_15SkeletonManagerE
namespace Qt3DRender::Render {
using namespace Qt3DCore;
inline JointFunctor::JointFunctor(AbstractRenderer *renderer,
                           JointManager *jointManager,
                           SkeletonManager *skeletonManager)
    : m_renderer(renderer)
    , m_jointManager(jointManager)
    , m_skeletonManager(skeletonManager)
{
}
}  // namespace Qt3DRender::Render

//  from ../qt3d/src/render/geometry/joint.cpp, line 94, as _ZNK10Qt3DRender6Render12JointFunctor6createEN8Qt3DCore7QNodeIdE
namespace Qt3DRender::Render {
using namespace Qt3DCore;
inline Qt3DCore::QBackendNode *JointFunctor::create(Qt3DCore::QNodeId id) const
{
    Joint *backend = m_jointManager->getOrCreateResource(id);
    backend->setRenderer(m_renderer);
    backend->setJointManager(m_jointManager);
    backend->setSkeletonManager(m_skeletonManager);
    return backend;
}
}  // namespace Qt3DRender::Render

//  from ../qt3d/src/render/geometry/joint.cpp, line 103, as _ZNK10Qt3DRender6Render12JointFunctor3getEN8Qt3DCore7QNodeIdE
namespace Qt3DRender::Render {
using namespace Qt3DCore;
inline Qt3DCore::QBackendNode *JointFunctor::get(Qt3DCore::QNodeId id) const
{
    return m_jointManager->lookupResource(id);
}
}  // namespace Qt3DRender::Render

//  from ../qt3d/src/render/geometry/joint.cpp, line 108, as _ZNK10Qt3DRender6Render12JointFunctor7destroyEN8Qt3DCore7QNodeIdE
namespace Qt3DRender::Render {
using namespace Qt3DCore;
inline void JointFunctor::destroy(Qt3DCore::QNodeId id) const
{
    m_jointManager->removeDirtyJoint(id);
    m_jointManager->releaseResource(id);
}
}  // namespace Qt3DRender::Render
//  -----------------------------------------------------------------------

//  Qt3DRender::Render::JointFunctor::JointFunctor(AbstractRenderer
//      *renderer, JointManager *jointManager, SkeletonManager
//      *skeletonManager)
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::JointFunctor *ritual_ZN10Qt3DRender6Render12JointFunctorC1EPNS0_16AbstractRendererEPNS0_12JointManagerEPNS0_15SkeletonManagerE(
    Qt3DRender::Render::AbstractRenderer *renderer,
    Qt3DRender::Render::JointManager *jointManager,
    Qt3DRender::Render::SkeletonManager *skeletonManager) {
  return new Qt3DRender::Render::JointFunctor(
      renderer,
      jointManager,
      skeletonManager);
}

//  Qt3DCore::QBackendNode
//      *Qt3DRender::Render::JointFunctor::create(Qt3DCore::QNodeId id) const
extern "C" Q_DECL_EXPORT
Qt3DCore::QBackendNode *ritual_ZNK10Qt3DRender6Render12JointFunctor6createEN8Qt3DCore7QNodeIdE(
    const Qt3DRender::Render::JointFunctor *self,
    const Qt3DCore::QNodeId *id) {
  return self->create(*id);
}

//  Qt3DCore::QBackendNode
//      *Qt3DRender::Render::JointFunctor::get(Qt3DCore::QNodeId id) const
extern "C" Q_DECL_EXPORT
Qt3DCore::QBackendNode *ritual_ZNK10Qt3DRender6Render12JointFunctor3getEN8Qt3DCore7QNodeIdE(
    const Qt3DRender::Render::JointFunctor *self,
    const Qt3DCore::QNodeId *id) {
  return self->get(*id);
}

//  void Qt3DRender::Render::JointFunctor::destroy(Qt3DCore::QNodeId id)
//      const
extern "C" Q_DECL_EXPORT
void ritual_ZNK10Qt3DRender6Render12JointFunctor7destroyEN8Qt3DCore7QNodeIdE(
    const Qt3DRender::Render::JointFunctor *self,
    const Qt3DCore::QNodeId *id) {
  self->destroy(*id);
}

//  Qt3DRender::Render::JointFunctor::~JointFunctor()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render12JointFunctorD1Ev(
    Qt3DRender::Render::JointFunctor *self) {
  delete self;
}
