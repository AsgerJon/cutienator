//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DAnimation/6.12.0/Qt3DAnimation/private/blendedclipanimator_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <Qt3DAnimation/6.12.0/Qt3DAnimation/private/qt3danimation_global_p.h>
#include <Qt3DAnimation/Qt3DAnimation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DAnimation/6.12.0/Qt3DAnimation/private/blendedclipanimator_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/qnodeid.h>
#include <QtCore/QVector>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DAnimation/private/backendnode_p.h>
#include <Qt3DCore/qnode.h>
#include <Qt3DCore/private/qbackendnode_p.h>
#include <Qt3DAnimation/private/blendedclipanimator_p.h>
#include <Qt3DAnimation/qblendedclipanimator.h>
#include <Qt3DAnimation/qchannelmapper.h>
#include <Qt3DAnimation/qclock.h>
#include <Qt3DAnimation/qabstractclipblendnode.h>
#include <Qt3DAnimation/private/qblendedclipanimator_p.h>
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
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/animation/backend/backendnode.cpp, line 13, as _ZN13Qt3DAnimation9Animation11BackendNodeC2EN8Qt3DCore12QBackendNode4ModeE
namespace Qt3DAnimation::Animation {
inline BackendNode::BackendNode(Mode mode)
    : Qt3DCore::QBackendNode(mode)
    , m_handler(nullptr)
{
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/blendedclipanimator.cpp, line 104, as _ZN13Qt3DAnimation9Animation19BlendedClipAnimator16syncFromFrontEndEPKN8Qt3DCore5QNodeEb
namespace Qt3DAnimation::Animation {
inline void BlendedClipAnimator::syncFromFrontEnd(const Qt3DCore::QNode *frontEnd, bool firstTime)
{
    BackendNode::syncFromFrontEnd(frontEnd, firstTime);
    const QBlendedClipAnimator *node = qobject_cast<const QBlendedClipAnimator *>(frontEnd);
    if (!node)
        return;

    auto id = Qt3DCore::qIdForNode(node->blendTree());
    if (id != m_blendTreeRootId)
        setBlendTreeRootId(id);
    id = Qt3DCore::qIdForNode(node->channelMapper());
    if (m_mapperId != id)
        setMapperId(id);
    id = Qt3DCore::qIdForNode(node->clock());
    if (m_clockId != id)
        setClockId(id);

    if (m_running != node->isRunning())
        setRunning(node->isRunning());
    if (m_loops != node->loopCount())
        m_loops = node->loopCount();
    if (!qFuzzyCompare(m_normalizedLocalTime, node->normalizedTime()))
        setNormalizedLocalTime(node->normalizedTime());

    if (firstTime)
        setDirty(Handler::BlendedClipAnimatorDirty);
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

//  from ../qt3d/src/animation/backend/blendedclipanimator.cpp, line 16, as _ZN13Qt3DAnimation9Animation19BlendedClipAnimatorC1Ev
namespace Qt3DAnimation::Animation {
inline BlendedClipAnimator::BlendedClipAnimator()
    : BackendNode(ReadWrite)
    , m_running(false)
    , m_lastGlobalTimeNS(0)
    , m_lastLocalTime(0.0)
    , m_currentLoop(0)
    , m_loops(1)
    , m_normalizedLocalTime(-1.0f)
    , m_lastNormalizedLocalTime(-1.0)
{
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/blendedclipanimator.cpp, line 53, as _ZN13Qt3DAnimation9Animation19BlendedClipAnimator7cleanupEv
namespace Qt3DAnimation::Animation {
inline void BlendedClipAnimator::cleanup()
{
    setEnabled(false);
    m_handler = nullptr;
    m_blendTreeRootId = Qt3DCore::QNodeId();
    m_mapperId = Qt3DCore::QNodeId();
    m_clockId = Qt3DCore::QNodeId();
    m_running = false;
    m_lastGlobalTimeNS = 0;
    m_lastLocalTime = 0.0;
    m_currentLoop = 0;
    m_loops = 1;
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/blendedclipanimator.cpp, line 92, as _ZNK13Qt3DAnimation9Animation19BlendedClipAnimator15blendTreeRootIdEv
namespace Qt3DAnimation::Animation {
inline Qt3DCore::QNodeId BlendedClipAnimator::blendTreeRootId() const
{
    return m_blendTreeRootId;
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/blendedclipanimator.cpp, line 97, as _ZN13Qt3DAnimation9Animation19BlendedClipAnimator22setNormalizedLocalTimeEfb
namespace Qt3DAnimation::Animation {
inline void BlendedClipAnimator::setNormalizedLocalTime(float normalizedTime, bool allowMarkDirty)
{
    m_normalizedLocalTime = normalizedTime;
    if (isValidNormalizedTime(m_normalizedLocalTime) && allowMarkDirty)
        setDirty(Handler::BlendedClipAnimatorDirty);
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/blendedclipanimator.cpp, line 67, as _ZN13Qt3DAnimation9Animation19BlendedClipAnimator18setBlendTreeRootIdEN8Qt3DCore7QNodeIdE
namespace Qt3DAnimation::Animation {
inline void BlendedClipAnimator::setBlendTreeRootId(Qt3DCore::QNodeId blendTreeId)
{
    m_blendTreeRootId = blendTreeId;
    setDirty(Handler::BlendedClipAnimatorDirty);
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/blendedclipanimator.cpp, line 73, as _ZN13Qt3DAnimation9Animation19BlendedClipAnimator11setMapperIdEN8Qt3DCore7QNodeIdE
namespace Qt3DAnimation::Animation {
inline void BlendedClipAnimator::setMapperId(Qt3DCore::QNodeId mapperId)
{
    m_mapperId = mapperId;
    setDirty(Handler::BlendedClipAnimatorDirty);
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/blendedclipanimator.cpp, line 79, as _ZN13Qt3DAnimation9Animation19BlendedClipAnimator10setClockIdEN8Qt3DCore7QNodeIdE
namespace Qt3DAnimation::Animation {
inline void BlendedClipAnimator::setClockId(Qt3DCore::QNodeId clockId)
{
    m_clockId = clockId;
    setDirty(Handler::BlendedClipAnimatorDirty);
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/blendedclipanimator.cpp, line 85, as _ZN13Qt3DAnimation9Animation19BlendedClipAnimator10setRunningEb
namespace Qt3DAnimation::Animation {
inline void BlendedClipAnimator::setRunning(bool running)
{
    m_running = running;
    setDirty(Handler::BlendedClipAnimatorDirty);
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/blendedclipanimator.cpp, line 48, as _ZN13Qt3DAnimation9Animation19BlendedClipAnimator20nsSincePreviousFrameEx
namespace Qt3DAnimation::Animation {
inline qint64 BlendedClipAnimator::nsSincePreviousFrame(qint64 currentGlobalTimeNS)
{
    return currentGlobalTimeNS - m_lastGlobalTimeNS;
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/blendedclipanimator.cpp, line 43, as _ZN13Qt3DAnimation9Animation19BlendedClipAnimator19setLastGlobalTimeNSERKx
namespace Qt3DAnimation::Animation {
inline void BlendedClipAnimator::setLastGlobalTimeNS(const qint64 &lastGlobalTimeNS)
{
    m_lastGlobalTimeNS = lastGlobalTimeNS;
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/blendedclipanimator.cpp, line 28, as _ZNK13Qt3DAnimation9Animation19BlendedClipAnimator13lastLocalTimeEv
namespace Qt3DAnimation::Animation {
inline double BlendedClipAnimator::lastLocalTime() const
{
    return m_lastLocalTime;
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/blendedclipanimator.cpp, line 33, as _ZN13Qt3DAnimation9Animation19BlendedClipAnimator16setLastLocalTimeEd
namespace Qt3DAnimation::Animation {
inline void BlendedClipAnimator::setLastLocalTime(double lastLocalTime)
{
    m_lastLocalTime = lastLocalTime;
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/blendedclipanimator.cpp, line 38, as _ZN13Qt3DAnimation9Animation19BlendedClipAnimator26setLastNormalizedLocalTimeEf
namespace Qt3DAnimation::Animation {
inline void BlendedClipAnimator::setLastNormalizedLocalTime(float normalizedTime)
{
    m_lastNormalizedLocalTime = normalizedTime;
}
}  // namespace Qt3DAnimation::Animation
//  -----------------------------------------------------------------------

//  Qt3DAnimation::Animation::BlendedClipAnimator::BlendedClipAnimator()
extern "C" Q_DECL_EXPORT
Qt3DAnimation::Animation::BlendedClipAnimator *ritual_ZN13Qt3DAnimation9Animation19BlendedClipAnimatorC1Ev() {
  return new Qt3DAnimation::Animation::BlendedClipAnimator();
}

//  void Qt3DAnimation::Animation::BlendedClipAnimator::cleanup()
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation19BlendedClipAnimator7cleanupEv(
    Qt3DAnimation::Animation::BlendedClipAnimator *self) {
  self->cleanup();
}

//  void
//      Qt3DAnimation::Animation::BlendedClipAnimator::syncFromFrontEnd(const
//      Qt3DCore::QNode *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation19BlendedClipAnimator16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DAnimation::Animation::BlendedClipAnimator *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->syncFromFrontEnd(frontEnd, firstTime);
}

//  Qt3DCore::QNodeId
//      Qt3DAnimation::Animation::BlendedClipAnimator::blendTreeRootId()
//      const
extern "C" Q_DECL_EXPORT
Qt3DCore::QNodeId *ritual_ZNK13Qt3DAnimation9Animation19BlendedClipAnimator15blendTreeRootIdEv(
    const Qt3DAnimation::Animation::BlendedClipAnimator *self) {
  return new Qt3DCore::QNodeId(self->blendTreeRootId());
}

//  Qt3DCore::QNodeId
//      Qt3DAnimation::Animation::BlendedClipAnimator::mapperId() const
extern "C" Q_DECL_EXPORT
Qt3DCore::QNodeId *ritual_ZNK13Qt3DAnimation9Animation19BlendedClipAnimator8mapperIdEv(
    const Qt3DAnimation::Animation::BlendedClipAnimator *self) {
  return new Qt3DCore::QNodeId(self->mapperId());
}

//  Qt3DCore::QNodeId
//      Qt3DAnimation::Animation::BlendedClipAnimator::clockId() const
extern "C" Q_DECL_EXPORT
Qt3DCore::QNodeId *ritual_ZNK13Qt3DAnimation9Animation19BlendedClipAnimator7clockIdEv(
    const Qt3DAnimation::Animation::BlendedClipAnimator *self) {
  return new Qt3DCore::QNodeId(self->clockId());
}

//  bool Qt3DAnimation::Animation::BlendedClipAnimator::isRunning() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13Qt3DAnimation9Animation19BlendedClipAnimator9isRunningEv(
    const Qt3DAnimation::Animation::BlendedClipAnimator *self) {
  return self->isRunning();
}

//  void Qt3DAnimation::Animation::BlendedClipAnimator::setNormalizedLocalTim
//      e(float normalizedTime, bool allowMarkDirty)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation19BlendedClipAnimator22setNormalizedLocalTimeEfb(
    Qt3DAnimation::Animation::BlendedClipAnimator *self,
    float normalizedTime,
    bool allowMarkDirty) {
  self->setNormalizedLocalTime(normalizedTime, allowMarkDirty);
}

//  float
//      Qt3DAnimation::Animation::BlendedClipAnimator::normalizedLocalTime()
//      const
extern "C" Q_DECL_EXPORT
float ritual_ZNK13Qt3DAnimation9Animation19BlendedClipAnimator19normalizedLocalTimeEv(
    const Qt3DAnimation::Animation::BlendedClipAnimator *self) {
  return self->normalizedLocalTime();
}

//  bool Qt3DAnimation::Animation::BlendedClipAnimator::canRun() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13Qt3DAnimation9Animation19BlendedClipAnimator6canRunEv(
    const Qt3DAnimation::Animation::BlendedClipAnimator *self) {
  return self->canRun();
}

//  void Qt3DAnimation::Animation::BlendedClipAnimator::setBlendTreeRootId(Qt
//      3DCore::QNodeId blendTreeRootId)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation19BlendedClipAnimator18setBlendTreeRootIdEN8Qt3DCore7QNodeIdE(
    Qt3DAnimation::Animation::BlendedClipAnimator *self,
    const Qt3DCore::QNodeId *blendTreeRootId) {
  self->setBlendTreeRootId(*blendTreeRootId);
}

//  void Qt3DAnimation::Animation::BlendedClipAnimator::setMapperId(Qt3DCore:
//      :QNodeId mapperId)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation19BlendedClipAnimator11setMapperIdEN8Qt3DCore7QNodeIdE(
    Qt3DAnimation::Animation::BlendedClipAnimator *self,
    const Qt3DCore::QNodeId *mapperId) {
  self->setMapperId(*mapperId);
}

//  void Qt3DAnimation::Animation::BlendedClipAnimator::setClockId(Qt3DCore::
//      QNodeId clockId)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation19BlendedClipAnimator10setClockIdEN8Qt3DCore7QNodeIdE(
    Qt3DAnimation::Animation::BlendedClipAnimator *self,
    const Qt3DCore::QNodeId *clockId) {
  self->setClockId(*clockId);
}

//  void Qt3DAnimation::Animation::BlendedClipAnimator::setRunning(bool
//      running)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation19BlendedClipAnimator10setRunningEb(
    Qt3DAnimation::Animation::BlendedClipAnimator *self,
    bool running) {
  self->setRunning(running);
}

//  void Qt3DAnimation::Animation::BlendedClipAnimator::setStartTime(qint64
//      globalTime)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation19BlendedClipAnimator12setStartTimeEx(
    Qt3DAnimation::Animation::BlendedClipAnimator *self,
    qint64 globalTime) {
  self->setStartTime(globalTime);
}

//  void Qt3DAnimation::Animation::BlendedClipAnimator::setLoops(int loops)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation19BlendedClipAnimator8setLoopsEi(
    Qt3DAnimation::Animation::BlendedClipAnimator *self,
    int loops) {
  self->setLoops(loops);
}

//  int Qt3DAnimation::Animation::BlendedClipAnimator::loops() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13Qt3DAnimation9Animation19BlendedClipAnimator5loopsEv(
    const Qt3DAnimation::Animation::BlendedClipAnimator *self) {
  return self->loops();
}

//  int Qt3DAnimation::Animation::BlendedClipAnimator::currentLoop() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13Qt3DAnimation9Animation19BlendedClipAnimator11currentLoopEv(
    const Qt3DAnimation::Animation::BlendedClipAnimator *self) {
  return self->currentLoop();
}

//  void Qt3DAnimation::Animation::BlendedClipAnimator::setCurrentLoop(int
//      currentLoop)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation19BlendedClipAnimator14setCurrentLoopEi(
    Qt3DAnimation::Animation::BlendedClipAnimator *self,
    int currentLoop) {
  self->setCurrentLoop(currentLoop);
}

//  void Qt3DAnimation::Animation::BlendedClipAnimator::setMappingData(const
//      QVector<MappingData> &mappingData)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation19BlendedClipAnimator14setMappingDataERK5QListINS0_11MappingDataEE(
    Qt3DAnimation::Animation::BlendedClipAnimator *self,
    const QVector<Qt3DAnimation::Animation::MappingData> *mappingData) {
  self->setMappingData(*mappingData);
}

//  QVector<MappingData>
//      Qt3DAnimation::Animation::BlendedClipAnimator::mappingData() const
extern "C" Q_DECL_EXPORT
QVector<Qt3DAnimation::Animation::MappingData> *ritual_ZNK13Qt3DAnimation9Animation19BlendedClipAnimator11mappingDataEv(
    const Qt3DAnimation::Animation::BlendedClipAnimator *self) {
  return new QVector<Qt3DAnimation::Animation::MappingData>(
      self->mappingData());
}

//  void
//      Qt3DAnimation::Animation::BlendedClipAnimator::animationClipMarkedDir
//      ty()
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation19BlendedClipAnimator24animationClipMarkedDirtyEv(
    Qt3DAnimation::Animation::BlendedClipAnimator *self) {
  self->animationClipMarkedDirty();
}

//  qint64 Qt3DAnimation::Animation::BlendedClipAnimator::nsSincePreviousFram
//      e(qint64 currentGlobalTimeNS)
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN13Qt3DAnimation9Animation19BlendedClipAnimator20nsSincePreviousFrameEx(
    Qt3DAnimation::Animation::BlendedClipAnimator *self,
    qint64 currentGlobalTimeNS) {
  return self->nsSincePreviousFrame(currentGlobalTimeNS);
}

//  void
//      Qt3DAnimation::Animation::BlendedClipAnimator::setLastGlobalTimeNS(co
//      nst qint64 &lastGlobalTimeNS)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation19BlendedClipAnimator19setLastGlobalTimeNSERKx(
    Qt3DAnimation::Animation::BlendedClipAnimator *self,
    qint64 lastGlobalTimeNS) {
  self->setLastGlobalTimeNS(lastGlobalTimeNS);
}

//  double Qt3DAnimation::Animation::BlendedClipAnimator::lastLocalTime()
//      const
extern "C" Q_DECL_EXPORT
double ritual_ZNK13Qt3DAnimation9Animation19BlendedClipAnimator13lastLocalTimeEv(
    const Qt3DAnimation::Animation::BlendedClipAnimator *self) {
  return self->lastLocalTime();
}

//  void
//      Qt3DAnimation::Animation::BlendedClipAnimator::setLastLocalTime(doubl
//      e lastLocalTime)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation19BlendedClipAnimator16setLastLocalTimeEd(
    Qt3DAnimation::Animation::BlendedClipAnimator *self,
    double lastLocalTime) {
  self->setLastLocalTime(lastLocalTime);
}

//  float
//      Qt3DAnimation::Animation::BlendedClipAnimator::lastNormalizedLocalTim
//      e()
extern "C" Q_DECL_EXPORT
float ritual_ZN13Qt3DAnimation9Animation19BlendedClipAnimator23lastNormalizedLocalTimeEv(
    Qt3DAnimation::Animation::BlendedClipAnimator *self) {
  return self->lastNormalizedLocalTime();
}

//  void Qt3DAnimation::Animation::BlendedClipAnimator::setLastNormalizedLoca
//      lTime(float normalizedTime)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation19BlendedClipAnimator26setLastNormalizedLocalTimeEf(
    Qt3DAnimation::Animation::BlendedClipAnimator *self,
    float normalizedTime) {
  self->setLastNormalizedLocalTime(normalizedTime);
}

//  bool Qt3DAnimation::Animation::BlendedClipAnimator::isSeeking() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13Qt3DAnimation9Animation19BlendedClipAnimator9isSeekingEv(
    const Qt3DAnimation::Animation::BlendedClipAnimator *self) {
  return self->isSeeking();
}

//  void
//      Qt3DAnimation::Animation::BlendedClipAnimator::syncFromFrontEnd(const
//      Qt3DCore::QNode *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13Qt3DAnimation9Animation19BlendedClipAnimator16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DAnimation::Animation::BlendedClipAnimator *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->Qt3DAnimation::Animation::BlendedClipAnimator::syncFromFrontEnd(
      frontEnd,
      firstTime);
}

//  a QVector<Qt3DAnimation::Animation::MappingData> a ritual of
//      Qt3DAnimation::Animation::BlendedClipAnimator gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DAnimation_Animation_BlendedClipAnimator__QVector_Qt3DAnimation_Animation_MappingData(
    QVector<Qt3DAnimation::Animation::MappingData> *self) {
  delete self;
}
