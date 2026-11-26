//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DAnimation/6.12.0/Qt3DAnimation/private/clipanimator_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DAnimation/6.12.0/Qt3DAnimation/private/qt3danimation_global_p.h>
#include <Qt3DAnimation/Qt3DAnimation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DAnimation/6.12.0/Qt3DAnimation/private/clipanimator_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/qnodeid.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DAnimation/6.12.0/Qt3DAnimation/private/animationutils_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/QVector>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DAnimation/private/backendnode_p.h>
#include <Qt3DCore/qnode.h>
#include <Qt3DCore/private/qbackendnode_p.h>
#include <Qt3DAnimation/private/clipanimator_p.h>
#include <Qt3DAnimation/qclipanimator.h>
#include <Qt3DAnimation/qchannelmapper.h>
#include <Qt3DAnimation/qclock.h>
#include <Qt3DAnimation/private/qclipanimator_p.h>
#include <Qt3DAnimation/private/animationclip_p.h>
#include <Qt3DAnimation/private/managers_p.h>
#include <Qt3DAnimation/private/animationlogging_p.h>
#include <Qt3DAnimation/private/animationclip_p.h>
#include <Qt3DAnimation/qanimationclip.h>
#include <Qt3DAnimation/qanimationcliploader.h>
#include <Qt3DAnimation/private/qanimationclip_p.h>
#include <Qt3DAnimation/private/qanimationcliploader_p.h>
#include <Qt3DAnimation/private/animationlogging_p.h>
#include <Qt3DAnimation/private/managers_p.h>
#include <Qt3DAnimation/private/gltfimporter_p.h>
#include <Qt3DCore/private/qurlhelper_p.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qfile.h>
#include <QtCore/qjsonarray.h>
#include <QtCore/qjsondocument.h>
#include <QtCore/qjsonobject.h>
#include <QtCore/qurlquery.h>
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

//  from ../qt3d/src/animation/backend/clipanimator.cpp, line 86, as _ZN13Qt3DAnimation9Animation12ClipAnimator16syncFromFrontEndEPKN8Qt3DCore5QNodeEb
namespace Qt3DAnimation::Animation {
inline void ClipAnimator::syncFromFrontEnd(const Qt3DCore::QNode *frontEnd, bool firstTime)
{
    BackendNode::syncFromFrontEnd(frontEnd, firstTime);
    const QClipAnimator *node = qobject_cast<const QClipAnimator *>(frontEnd);
    if (!node)
        return;

    auto id = Qt3DCore::qIdForNode(node->clip());
    if (m_clipId != id)
        setClipId(id);
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
        setDirty(Handler::ClipAnimatorDirty);
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

//  from ../qt3d/src/animation/backend/animationclip.cpp, line 265, as _ZN13Qt3DAnimation9Animation13AnimationClip24addDependingClipAnimatorERKN8Qt3DCore7QNodeIdE
namespace Qt3DAnimation::Animation {
inline void AnimationClip::addDependingClipAnimator(const Qt3DCore::QNodeId &id)
{
    QMutexLocker lock(&m_mutex);
    m_dependingAnimators.push_back(id);
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

//  from ../qt3d/src/animation/backend/clipanimator.cpp, line 18, as _ZN13Qt3DAnimation9Animation12ClipAnimatorC1Ev
namespace Qt3DAnimation::Animation {
inline ClipAnimator::ClipAnimator()
    : BackendNode(ReadWrite)
    , m_clipId()
    , m_mapperId()
    , m_clockId()
    , m_running(false)
    , m_loops(1)
    , m_lastGlobalTimeNS(0)
    , m_lastLocalTime(0.0)
    , m_mappingData()
    , m_currentLoop(0)
    , m_normalizedLocalTime(-1.0f)
    , m_lastNormalizedLocalTime(-1.0f)
{
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/clipanimator.cpp, line 72, as _ZN13Qt3DAnimation9Animation12ClipAnimator7cleanupEv
namespace Qt3DAnimation::Animation {
inline void ClipAnimator::cleanup()
{
    setEnabled(false);
    m_handler = nullptr;
    m_clipId = Qt3DCore::QNodeId();
    m_mapperId = Qt3DCore::QNodeId();
    m_clockId = Qt3DCore::QNodeId();
    m_running = false;
    m_loops = 1;
    m_clipFormat = ClipFormat();
    m_currentLoop = 0;
    m_normalizedLocalTime = m_lastNormalizedLocalTime = -1.0f;
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/clipanimator.cpp, line 34, as _ZN13Qt3DAnimation9Animation12ClipAnimator9setClipIdEN8Qt3DCore7QNodeIdE
namespace Qt3DAnimation::Animation {
inline void ClipAnimator::setClipId(Qt3DCore::QNodeId clipId)
{
    m_clipId = clipId;
    setDirty(Handler::ClipAnimatorDirty);

    // register at the clip to make sure we are marked dirty when the clip finished loading
    AnimationClip *clip = m_handler->animationClipLoaderManager()->lookupResource(clipId);
    if (clip)
        clip->addDependingClipAnimator(peerId());
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/clipanimator.cpp, line 45, as _ZN13Qt3DAnimation9Animation12ClipAnimator11setMapperIdEN8Qt3DCore7QNodeIdE
namespace Qt3DAnimation::Animation {
inline void ClipAnimator::setMapperId(Qt3DCore::QNodeId mapperId)
{
    m_mapperId = mapperId;
    setDirty(Handler::ClipAnimatorDirty);
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/clipanimator.cpp, line 51, as _ZN13Qt3DAnimation9Animation12ClipAnimator10setClockIdEN8Qt3DCore7QNodeIdE
namespace Qt3DAnimation::Animation {
inline void ClipAnimator::setClockId(Qt3DCore::QNodeId clockId)
{
    m_clockId = clockId;
    setDirty(Handler::ClipAnimatorDirty);
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/clipanimator.cpp, line 57, as _ZN13Qt3DAnimation9Animation12ClipAnimator10setRunningEb
namespace Qt3DAnimation::Animation {
inline void ClipAnimator::setRunning(bool running)
{
    m_running = running;
    if (!running)
        m_currentLoop = 0;
    setDirty(Handler::ClipAnimatorDirty);
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/clipanimator.cpp, line 65, as _ZN13Qt3DAnimation9Animation12ClipAnimator22setNormalizedLocalTimeEfb
namespace Qt3DAnimation::Animation {
inline void ClipAnimator::setNormalizedLocalTime(float normalizedTime, bool allowMarkDirty)
{
    m_normalizedLocalTime = normalizedTime;
    if (isValidNormalizedTime(normalizedTime) && allowMarkDirty)
        setDirty(Handler::ClipAnimatorDirty);
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/clipanimator.cpp, line 114, as _ZN13Qt3DAnimation9Animation12ClipAnimator20nsSincePreviousFrameEx
namespace Qt3DAnimation::Animation {
inline qint64 ClipAnimator::nsSincePreviousFrame(qint64 currentGlobalTimeNS)
{
    return currentGlobalTimeNS - m_lastGlobalTimeNS;
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/clipanimator.cpp, line 119, as _ZN13Qt3DAnimation9Animation12ClipAnimator19setLastGlobalTimeNSEx
namespace Qt3DAnimation::Animation {
inline void ClipAnimator::setLastGlobalTimeNS(qint64 lastGlobalTimeNS)
{
    m_lastGlobalTimeNS = lastGlobalTimeNS;
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/clipanimator.cpp, line 124, as _ZNK13Qt3DAnimation9Animation12ClipAnimator13lastLocalTimeEv
namespace Qt3DAnimation::Animation {
inline double ClipAnimator::lastLocalTime() const
{
    return m_lastLocalTime;
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/clipanimator.cpp, line 129, as _ZN13Qt3DAnimation9Animation12ClipAnimator16setLastLocalTimeEd
namespace Qt3DAnimation::Animation {
inline void ClipAnimator::setLastLocalTime(double lastLocalTime)
{
    m_lastLocalTime = lastLocalTime;
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/clipanimator.cpp, line 134, as _ZN13Qt3DAnimation9Animation12ClipAnimator26setLastNormalizedLocalTimeEf
namespace Qt3DAnimation::Animation {
inline void ClipAnimator::setLastNormalizedLocalTime(float normalizedTime)
{
    m_lastNormalizedLocalTime = normalizedTime;
}
}  // namespace Qt3DAnimation::Animation
//  -----------------------------------------------------------------------

//  Qt3DAnimation::Animation::ClipAnimator::ClipAnimator()
extern "C" Q_DECL_EXPORT
Qt3DAnimation::Animation::ClipAnimator *ritual_ZN13Qt3DAnimation9Animation12ClipAnimatorC1Ev() {
  return new Qt3DAnimation::Animation::ClipAnimator();
}

//  void Qt3DAnimation::Animation::ClipAnimator::cleanup()
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation12ClipAnimator7cleanupEv(
    Qt3DAnimation::Animation::ClipAnimator *self) {
  self->cleanup();
}

//  void Qt3DAnimation::Animation::ClipAnimator::setClipId(Qt3DCore::QNodeId
//      clipId)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation12ClipAnimator9setClipIdEN8Qt3DCore7QNodeIdE(
    Qt3DAnimation::Animation::ClipAnimator *self,
    const Qt3DCore::QNodeId *clipId) {
  self->setClipId(*clipId);
}

//  Qt3DCore::QNodeId Qt3DAnimation::Animation::ClipAnimator::clipId() const
extern "C" Q_DECL_EXPORT
Qt3DCore::QNodeId *ritual_ZNK13Qt3DAnimation9Animation12ClipAnimator6clipIdEv(
    const Qt3DAnimation::Animation::ClipAnimator *self) {
  return new Qt3DCore::QNodeId(self->clipId());
}

//  void
//      Qt3DAnimation::Animation::ClipAnimator::setMapperId(Qt3DCore::QNodeId
//      mapperId)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation12ClipAnimator11setMapperIdEN8Qt3DCore7QNodeIdE(
    Qt3DAnimation::Animation::ClipAnimator *self,
    const Qt3DCore::QNodeId *mapperId) {
  self->setMapperId(*mapperId);
}

//  Qt3DCore::QNodeId Qt3DAnimation::Animation::ClipAnimator::mapperId()
//      const
extern "C" Q_DECL_EXPORT
Qt3DCore::QNodeId *ritual_ZNK13Qt3DAnimation9Animation12ClipAnimator8mapperIdEv(
    const Qt3DAnimation::Animation::ClipAnimator *self) {
  return new Qt3DCore::QNodeId(self->mapperId());
}

//  void Qt3DAnimation::Animation::ClipAnimator::setClockId(Qt3DCore::QNodeId
//      clockId)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation12ClipAnimator10setClockIdEN8Qt3DCore7QNodeIdE(
    Qt3DAnimation::Animation::ClipAnimator *self,
    const Qt3DCore::QNodeId *clockId) {
  self->setClockId(*clockId);
}

//  Qt3DCore::QNodeId Qt3DAnimation::Animation::ClipAnimator::clockId() const
extern "C" Q_DECL_EXPORT
Qt3DCore::QNodeId *ritual_ZNK13Qt3DAnimation9Animation12ClipAnimator7clockIdEv(
    const Qt3DAnimation::Animation::ClipAnimator *self) {
  return new Qt3DCore::QNodeId(self->clockId());
}

//  void Qt3DAnimation::Animation::ClipAnimator::setRunning(bool running)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation12ClipAnimator10setRunningEb(
    Qt3DAnimation::Animation::ClipAnimator *self,
    bool running) {
  self->setRunning(running);
}

//  bool Qt3DAnimation::Animation::ClipAnimator::isRunning() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13Qt3DAnimation9Animation12ClipAnimator9isRunningEv(
    const Qt3DAnimation::Animation::ClipAnimator *self) {
  return self->isRunning();
}

//  void Qt3DAnimation::Animation::ClipAnimator::setLoops(int loops)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation12ClipAnimator8setLoopsEi(
    Qt3DAnimation::Animation::ClipAnimator *self,
    int loops) {
  self->setLoops(loops);
}

//  int Qt3DAnimation::Animation::ClipAnimator::loops() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13Qt3DAnimation9Animation12ClipAnimator5loopsEv(
    const Qt3DAnimation::Animation::ClipAnimator *self) {
  return self->loops();
}

//  void Qt3DAnimation::Animation::ClipAnimator::setNormalizedLocalTime(float
//      normalizedLocalTime, bool allowMarkDirty)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation12ClipAnimator22setNormalizedLocalTimeEfb(
    Qt3DAnimation::Animation::ClipAnimator *self,
    float normalizedLocalTime,
    bool allowMarkDirty) {
  self->setNormalizedLocalTime(normalizedLocalTime, allowMarkDirty);
}

//  float Qt3DAnimation::Animation::ClipAnimator::normalizedLocalTime() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK13Qt3DAnimation9Animation12ClipAnimator19normalizedLocalTimeEv(
    const Qt3DAnimation::Animation::ClipAnimator *self) {
  return self->normalizedLocalTime();
}

//  void Qt3DAnimation::Animation::ClipAnimator::syncFromFrontEnd(const
//      Qt3DCore::QNode *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation12ClipAnimator16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DAnimation::Animation::ClipAnimator *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->syncFromFrontEnd(frontEnd, firstTime);
}

//  void Qt3DAnimation::Animation::ClipAnimator::setHandler(Handler *handler)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation12ClipAnimator10setHandlerEPNS0_7HandlerE(
    Qt3DAnimation::Animation::ClipAnimator *self,
    Qt3DAnimation::Animation::Handler *handler) {
  self->setHandler(handler);
}

//  bool Qt3DAnimation::Animation::ClipAnimator::canRun() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13Qt3DAnimation9Animation12ClipAnimator6canRunEv(
    const Qt3DAnimation::Animation::ClipAnimator *self) {
  return self->canRun();
}

//  void Qt3DAnimation::Animation::ClipAnimator::setMappingData(const
//      QVector<MappingData> &mappingData)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation12ClipAnimator14setMappingDataERK5QListINS0_11MappingDataEE(
    Qt3DAnimation::Animation::ClipAnimator *self,
    const QVector<Qt3DAnimation::Animation::MappingData> *mappingData) {
  self->setMappingData(*mappingData);
}

//  QVector<MappingData>
//      Qt3DAnimation::Animation::ClipAnimator::mappingData() const
extern "C" Q_DECL_EXPORT
QVector<Qt3DAnimation::Animation::MappingData> *ritual_ZNK13Qt3DAnimation9Animation12ClipAnimator11mappingDataEv(
    const Qt3DAnimation::Animation::ClipAnimator *self) {
  return new QVector<Qt3DAnimation::Animation::MappingData>(
      self->mappingData());
}

//  void Qt3DAnimation::Animation::ClipAnimator::setStartTime(qint64
//      globalTime)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation12ClipAnimator12setStartTimeEx(
    Qt3DAnimation::Animation::ClipAnimator *self,
    qint64 globalTime) {
  self->setStartTime(globalTime);
}

//  int Qt3DAnimation::Animation::ClipAnimator::currentLoop() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13Qt3DAnimation9Animation12ClipAnimator11currentLoopEv(
    const Qt3DAnimation::Animation::ClipAnimator *self) {
  return self->currentLoop();
}

//  void Qt3DAnimation::Animation::ClipAnimator::setCurrentLoop(int
//      currentLoop)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation12ClipAnimator14setCurrentLoopEi(
    Qt3DAnimation::Animation::ClipAnimator *self,
    int currentLoop) {
  self->setCurrentLoop(currentLoop);
}

//  void Qt3DAnimation::Animation::ClipAnimator::animationClipMarkedDirty()
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation12ClipAnimator24animationClipMarkedDirtyEv(
    Qt3DAnimation::Animation::ClipAnimator *self) {
  self->animationClipMarkedDirty();
}

//  void Qt3DAnimation::Animation::ClipAnimator::setClipFormat(const
//      ClipFormat &clipFormat)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation12ClipAnimator13setClipFormatERKNS0_10ClipFormatE(
    Qt3DAnimation::Animation::ClipAnimator *self,
    const Qt3DAnimation::Animation::ClipFormat *clipFormat) {
  self->setClipFormat(*clipFormat);
}

//  ClipFormat Qt3DAnimation::Animation::ClipAnimator::clipFormat() const
extern "C" Q_DECL_EXPORT
Qt3DAnimation::Animation::ClipFormat *ritual_ZNK13Qt3DAnimation9Animation12ClipAnimator10clipFormatEv(
    const Qt3DAnimation::Animation::ClipAnimator *self) {
  return new Qt3DAnimation::Animation::ClipFormat(self->clipFormat());
}

//  qint64
//      Qt3DAnimation::Animation::ClipAnimator::nsSincePreviousFrame(qint64
//      currentGlobalTimeNS)
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN13Qt3DAnimation9Animation12ClipAnimator20nsSincePreviousFrameEx(
    Qt3DAnimation::Animation::ClipAnimator *self,
    qint64 currentGlobalTimeNS) {
  return self->nsSincePreviousFrame(currentGlobalTimeNS);
}

//  void Qt3DAnimation::Animation::ClipAnimator::setLastGlobalTimeNS(qint64
//      lastGlobalTimeNS)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation12ClipAnimator19setLastGlobalTimeNSEx(
    Qt3DAnimation::Animation::ClipAnimator *self,
    qint64 lastGlobalTimeNS) {
  self->setLastGlobalTimeNS(lastGlobalTimeNS);
}

//  double Qt3DAnimation::Animation::ClipAnimator::lastLocalTime() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK13Qt3DAnimation9Animation12ClipAnimator13lastLocalTimeEv(
    const Qt3DAnimation::Animation::ClipAnimator *self) {
  return self->lastLocalTime();
}

//  void Qt3DAnimation::Animation::ClipAnimator::setLastLocalTime(double
//      lastLocalTime)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation12ClipAnimator16setLastLocalTimeEd(
    Qt3DAnimation::Animation::ClipAnimator *self,
    double lastLocalTime) {
  self->setLastLocalTime(lastLocalTime);
}

//  float Qt3DAnimation::Animation::ClipAnimator::lastNormalizedLocalTime()
extern "C" Q_DECL_EXPORT
float ritual_ZN13Qt3DAnimation9Animation12ClipAnimator23lastNormalizedLocalTimeEv(
    Qt3DAnimation::Animation::ClipAnimator *self) {
  return self->lastNormalizedLocalTime();
}

//  void
//      Qt3DAnimation::Animation::ClipAnimator::setLastNormalizedLocalTime(fl
//      oat normalizedLocalTime)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation12ClipAnimator26setLastNormalizedLocalTimeEf(
    Qt3DAnimation::Animation::ClipAnimator *self,
    float normalizedLocalTime) {
  self->setLastNormalizedLocalTime(normalizedLocalTime);
}

//  bool Qt3DAnimation::Animation::ClipAnimator::isSeeking() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13Qt3DAnimation9Animation12ClipAnimator9isSeekingEv(
    const Qt3DAnimation::Animation::ClipAnimator *self) {
  return self->isSeeking();
}

//  void Qt3DAnimation::Animation::ClipAnimator::syncFromFrontEnd(const
//      Qt3DCore::QNode *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13Qt3DAnimation9Animation12ClipAnimator16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DAnimation::Animation::ClipAnimator *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->Qt3DAnimation::Animation::ClipAnimator::syncFromFrontEnd(
      frontEnd,
      firstTime);
}

//  a QVector<Qt3DAnimation::Animation::MappingData> a ritual of
//      Qt3DAnimation::Animation::ClipAnimator gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DAnimation_Animation_ClipAnimator__QVector_Qt3DAnimation_Animation_MappingData(
    QVector<Qt3DAnimation::Animation::MappingData> *self) {
  delete self;
}
