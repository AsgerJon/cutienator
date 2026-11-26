//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DAnimation/6.12.0/Qt3DAnimation/private/clock_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <Qt3DAnimation/6.12.0/Qt3DAnimation/private/qt3danimation_global_p.h>
#include <Qt3DAnimation/Qt3DAnimation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DAnimation/6.12.0/Qt3DAnimation/private/clock_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DAnimation/private/backendnode_p.h>
#include <Qt3DCore/qnode.h>
#include <Qt3DCore/private/qbackendnode_p.h>
#include <Qt3DAnimation/private/clock_p.h>
#include <Qt3DAnimation/qclock.h>
#include <Qt3DAnimation/private/qclock_p.h>
#include <Qt3DAnimation/private/animationutils_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/animation/backend/backendnode.cpp, line 13, as _ZN13Qt3DAnimation9Animation11BackendNodeC2EN8Qt3DCore12QBackendNode4ModeE
namespace Qt3DAnimation::Animation {
inline BackendNode::BackendNode(Mode mode)
    : Qt3DCore::QBackendNode(mode)
    , m_handler(nullptr)
{
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/clock.cpp, line 20, as _ZN13Qt3DAnimation9Animation5Clock16syncFromFrontEndEPKN8Qt3DCore5QNodeEb
namespace Qt3DAnimation::Animation {
inline void Clock::syncFromFrontEnd(const Qt3DCore::QNode *frontEnd, bool firstTime)
{
    BackendNode::syncFromFrontEnd(frontEnd, firstTime);
    const QClock *node = qobject_cast<const QClock *>(frontEnd);
    if (!node)
        return;

    if (!qFuzzyCompare(m_playbackRate, node->playbackRate())) {
        m_playbackRate = node->playbackRate();
    }
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

//  from ../qt3d/src/animation/backend/backendnode.cpp, line 19, as _ZN13Qt3DAnimation9Animation11BackendNodeD2Ev
namespace Qt3DAnimation::Animation {
inline BackendNode::~BackendNode()
{
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/clock.cpp, line 32, as _ZN13Qt3DAnimation9Animation5Clock7cleanupEv
namespace Qt3DAnimation::Animation {
inline void Clock::cleanup()
{
    m_playbackRate = 1.f;
}
}  // namespace Qt3DAnimation::Animation
//  -----------------------------------------------------------------------

//  void Qt3DAnimation::Animation::Clock::syncFromFrontEnd(const
//      Qt3DCore::QNode *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation5Clock16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DAnimation::Animation::Clock *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->syncFromFrontEnd(frontEnd, firstTime);
}

//  void Qt3DAnimation::Animation::Clock::cleanup()
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation5Clock7cleanupEv(
    Qt3DAnimation::Animation::Clock *self) {
  self->cleanup();
}

//  void Qt3DAnimation::Animation::Clock::setPlaybackRate(double
//      playbackRate)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation5Clock15setPlaybackRateEd(
    Qt3DAnimation::Animation::Clock *self,
    double playbackRate) {
  self->setPlaybackRate(playbackRate);
}

//  double Qt3DAnimation::Animation::Clock::playbackRate() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK13Qt3DAnimation9Animation5Clock12playbackRateEv(
    const Qt3DAnimation::Animation::Clock *self) {
  return self->playbackRate();
}

//  void Qt3DAnimation::Animation::Clock::syncFromFrontEnd(const
//      Qt3DCore::QNode *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13Qt3DAnimation9Animation5Clock16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DAnimation::Animation::Clock *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->Qt3DAnimation::Animation::Clock::syncFromFrontEnd(
      frontEnd,
      firstTime);
}
