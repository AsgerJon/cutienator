//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DAnimation/6.12.0/Qt3DAnimation/private/backendnode_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DAnimation/6.12.0/Qt3DAnimation/private/qt3danimation_global_p.h>
#include <Qt3DAnimation/Qt3DAnimation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DAnimation/6.12.0/Qt3DAnimation/private/backendnode_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DAnimation/private/handler_p.h>
#include <Qt3DAnimation/private/managers_p.h>
#include <Qt3DAnimation/private/loadanimationclipjob_p.h>
#include <Qt3DAnimation/private/findrunningclipanimatorsjob_p.h>
#include <Qt3DAnimation/private/evaluateclipanimatorjob_p.h>
#include <Qt3DAnimation/private/buildblendtreesjob_p.h>
#include <Qt3DAnimation/private/evaluateblendclipanimatorjob_p.h>
#include <Qt3DAnimation/private/animationlogging_p.h>
#include <Qt3DAnimation/private/buildblendtreesjob_p.h>
#include <Qt3DAnimation/private/evaluateblendclipanimatorjob_p.h>
#include <Qt3DCore/private/qaspectjob_p.h>
#include <Qt3DCore/private/vector_helper_p.h>
#include <Qt3DAnimation/private/backendnode_p.h>
#include <Qt3DCore/qnode.h>
#include <Qt3DCore/private/qbackendnode_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/animation/backend/handler.cpp, line 45, as _ZN13Qt3DAnimation9Animation7Handler8setDirtyENS1_9DirtyFlagEN8Qt3DCore7QNodeIdE
namespace Qt3DAnimation::Animation {
inline void Handler::setDirty(DirtyFlag flag, Qt3DCore::QNodeId nodeId)
{
    switch (flag) {
    case AnimationClipDirty: {
        QMutexLocker lock(&m_mutex);
        const auto handle = m_animationClipLoaderManager->lookupHandle(nodeId);
        if (!m_dirtyAnimationClips.contains(handle))
            m_dirtyAnimationClips.push_back(handle);
        break;
    }

    case ChannelMappingsDirty: {
        break;
    }

    case ClipAnimatorDirty: {
        QMutexLocker lock(&m_mutex);
        const auto handle = m_clipAnimatorManager->lookupHandle(nodeId);
        if (!m_dirtyClipAnimators.contains(handle))
            m_dirtyClipAnimators.push_back(handle);
        break;
    }

    case BlendedClipAnimatorDirty: {
        QMutexLocker lock(&m_mutex);
        const HBlendedClipAnimator handle = m_blendedClipAnimatorManager->lookupHandle(nodeId);
        if (!m_dirtyBlendedAnimators.contains(handle))
            m_dirtyBlendedAnimators.push_back(handle);
        break;
    }
    }
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/backendnode.cpp, line 13, as _ZN13Qt3DAnimation9Animation11BackendNodeC1EN8Qt3DCore12QBackendNode4ModeE
namespace Qt3DAnimation::Animation {
inline BackendNode::BackendNode(Mode mode)
    : Qt3DCore::QBackendNode(mode)
    , m_handler(nullptr)
{
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/backendnode.cpp, line 19, as _ZN13Qt3DAnimation9Animation11BackendNodeD1Ev
namespace Qt3DAnimation::Animation {
inline BackendNode::~BackendNode()
{
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/backendnode.cpp, line 23, as _ZN13Qt3DAnimation9Animation11BackendNode10setHandlerEPNS0_7HandlerE
namespace Qt3DAnimation::Animation {
inline void BackendNode::setHandler(Handler *handler)
{
    m_handler = handler;
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/backendnode.cpp, line 34, as _ZN13Qt3DAnimation9Animation11BackendNode16syncFromFrontEndEPKN8Qt3DCore5QNodeEb
namespace Qt3DAnimation::Animation {
inline void BackendNode::syncFromFrontEnd(const Qt3DCore::QNode *frontEnd, bool firstTime)
{
    Q_UNUSED(firstTime);

    d_ptr->setEnabled(frontEnd->isEnabled());
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/backendnode.cpp, line 28, as _ZN13Qt3DAnimation9Animation11BackendNode8setDirtyENS0_7Handler9DirtyFlagE
namespace Qt3DAnimation::Animation {
inline void BackendNode::setDirty(Handler::DirtyFlag flag)
{
    Q_ASSERT(m_handler);
    m_handler->setDirty(flag, peerId());
}
}  // namespace Qt3DAnimation::Animation
//  -----------------------------------------------------------------------

//  A Qt3DAnimation::Animation::BackendNode that Python can take functions over in. Every Qt3DAnimation::Animation::BackendNode
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DAnimation_Animation_BackendNodeCall0)(const void *, const Qt3DCore::QNode *, bool, int *);
class CuteQt3DAnimation_Animation_BackendNode : public Qt3DAnimation::Animation::BackendNode {
public:
  using Qt3DAnimation::Animation::BackendNode::BackendNode;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN8Qt3DCore12QBackendNode16syncFromFrontEndEPKNS_5QNodeEb")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  void Qt3DAnimation::Animation::BackendNode::syncFromFrontEnd(const
  //      Qt3DCore::QNode *frontEnd, bool firstTime)
  void syncFromFrontEnd(
      const Qt3DCore::QNode *frontEnd,
      bool firstTime) override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DAnimation_Animation_BackendNodeCall0 call = reinterpret_cast<CuteQt3DAnimation_Animation_BackendNodeCall0>(taken[0]);
      call(this, frontEnd, firstTime, &handled);
      if (handled) return;
    }
    Qt3DAnimation::Animation::BackendNode::syncFromFrontEnd(frontEnd, firstTime);
  }
};

//  Qt3DAnimation::Animation::BackendNode::BackendNode(Qt3DCore::QBackendNode
//      ::Mode mode)
extern "C" Q_DECL_EXPORT
Qt3DAnimation::Animation::BackendNode *ritual_ZN13Qt3DAnimation9Animation11BackendNodeC1EN8Qt3DCore12QBackendNode4ModeE(
    Qt3DCore::QBackendNode::Mode mode) {
  return new CuteQt3DAnimation_Animation_BackendNode(mode);
}

//  Qt3DAnimation::Animation::BackendNode::~BackendNode()
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation11BackendNodeD1Ev(
    Qt3DAnimation::Animation::BackendNode *self) {
  delete self;
}

//  void Qt3DAnimation::Animation::BackendNode::setHandler(Handler *handler)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation11BackendNode10setHandlerEPNS0_7HandlerE(
    Qt3DAnimation::Animation::BackendNode *self,
    Qt3DAnimation::Animation::Handler *handler) {
  self->setHandler(handler);
}

//  void Qt3DAnimation::Animation::BackendNode::syncFromFrontEnd(const
//      Qt3DCore::QNode *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation11BackendNode16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DAnimation::Animation::BackendNode *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->syncFromFrontEnd(frontEnd, firstTime);
}

//  void Qt3DAnimation::Animation::BackendNode::setDirty(Handler::DirtyFlag
//      flag)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation11BackendNode8setDirtyENS0_7Handler9DirtyFlagE(
    Qt3DAnimation::Animation::BackendNode *self,
    Qt3DAnimation::Animation::Handler::DirtyFlag flag) {
  self->setDirty(flag);
}

//  a Python function taken by a CuteQt3DAnimation_Animation_BackendNode, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DAnimation_Animation_BackendNode(
    Qt3DAnimation::Animation::BackendNode *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DAnimation_Animation_BackendNode *>(self)->take(key, call);
}

//  void Qt3DAnimation::Animation::BackendNode::syncFromFrontEnd(const
//      Qt3DCore::QNode *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13Qt3DAnimation9Animation11BackendNode16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DAnimation::Animation::BackendNode *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->Qt3DAnimation::Animation::BackendNode::syncFromFrontEnd(
      frontEnd,
      firstTime);
}
