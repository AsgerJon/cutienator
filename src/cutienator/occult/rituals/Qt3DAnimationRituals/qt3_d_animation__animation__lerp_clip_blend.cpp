//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DAnimation/6.12.0/Qt3DAnimation/private/lerpclipblend_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DAnimation/6.12.0/Qt3DAnimation/private/qt3danimation_global_p.h>
#include <Qt3DAnimation/Qt3DAnimation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DAnimation/6.12.0/Qt3DAnimation/private/lerpclipblend_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/qnodeid.h>
#include <cstring>
#include <QtCore/QList>
#include <Qt3DCore/Qt3DCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DAnimation/private/backendnode_p.h>
#include <Qt3DCore/qnode.h>
#include <Qt3DCore/private/qbackendnode_p.h>
#include <Qt3DAnimation/private/clipblendnode_p.h>
#include <Qt3DAnimation/qabstractanimationclip.h>
#include <Qt3DAnimation/private/lerpclipblend_p.h>
#include <Qt3DAnimation/qlerpclipblend.h>
#include <Qt3DAnimation/private/qlerpclipblend_p.h>
#include <Qt3DAnimation/private/managers_p.h>
#include <Qt3DAnimation/private/clipblendnode_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/animation/backend/backendnode.cpp, line 34, as _ZN13Qt3DAnimation9Animation11BackendNode16syncFromFrontEndEPKN8Qt3DCore5QNodeEb
namespace Qt3DAnimation::Animation {
inline void BackendNode::syncFromFrontEnd(const Qt3DCore::QNode *frontEnd, bool firstTime)
{
    Q_UNUSED(firstTime);

    d_ptr->setEnabled(frontEnd->isEnabled());
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/clipblendnode.cpp, line 13, as _ZN13Qt3DAnimation9Animation13ClipBlendNodeC2ENS1_9BlendTypeE
namespace Qt3DAnimation::Animation {
inline ClipBlendNode::ClipBlendNode(BlendType blendType)
    : BackendNode(ReadOnly) // Makes sense for now at least
    , m_manager(nullptr)
    , m_blendType(blendType)
{
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/clipblendnode.cpp, line 20, as _ZN13Qt3DAnimation9Animation13ClipBlendNodeD2Ev
namespace Qt3DAnimation::Animation {
inline ClipBlendNode::~ClipBlendNode()
{
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/lerpclipblend.cpp, line 51, as _ZNK13Qt3DAnimation9Animation13LerpClipBlend8durationEv
namespace Qt3DAnimation::Animation {
inline double LerpClipBlend::duration() const
{
    ClipBlendNode *startNode = clipBlendNodeManager()->lookupNode(m_startClipId);
    const double startNodeDuration = startNode ? startNode->duration() : 0.0;

    ClipBlendNode *endNode = clipBlendNodeManager()->lookupNode(m_endClipId);
    const double endNodeDuration = endNode ? endNode->duration() : 0.0;

    return (1.0 - static_cast<double>(m_blendFactor)) * startNodeDuration + static_cast<double>(m_blendFactor) * endNodeDuration;
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/backendnode.cpp, line 13, as _ZN13Qt3DAnimation9Animation11BackendNodeC2EN8Qt3DCore12QBackendNode4ModeE
namespace Qt3DAnimation::Animation {
inline BackendNode::BackendNode(Mode mode)
    : Qt3DCore::QBackendNode(mode)
    , m_handler(nullptr)
{
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/backendnode.cpp, line 19, as _ZN13Qt3DAnimation9Animation11BackendNodeD2Ev
namespace Qt3DAnimation::Animation {
inline BackendNode::~BackendNode()
{
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/managers.cpp, line 31, as _ZNK13Qt3DAnimation9Animation20ClipBlendNodeManager10lookupNodeEN8Qt3DCore7QNodeIdE
namespace Qt3DAnimation::Animation {
inline ClipBlendNode *ClipBlendNodeManager::lookupNode(Qt3DCore::QNodeId id) const
{
    return m_nodes.value(id, nullptr);
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/lerpclipblend.cpp, line 14, as _ZN13Qt3DAnimation9Animation13LerpClipBlendC1Ev
namespace Qt3DAnimation::Animation {
inline LerpClipBlend::LerpClipBlend()
    : ClipBlendNode(ClipBlendNode::LerpBlendType)
    , m_startClipId()
    , m_endClipId()
    , m_blendFactor(0.0f)
{
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/lerpclipblend.cpp, line 22, as _ZN13Qt3DAnimation9Animation13LerpClipBlendD1Ev
namespace Qt3DAnimation::Animation {
inline LerpClipBlend::~LerpClipBlend()
{
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/lerpclipblend.cpp, line 26, as _ZN13Qt3DAnimation9Animation13LerpClipBlend16syncFromFrontEndEPKN8Qt3DCore5QNodeEb
namespace Qt3DAnimation::Animation {
inline void LerpClipBlend::syncFromFrontEnd(const Qt3DCore::QNode *frontEnd, bool firstTime)
{
    BackendNode::syncFromFrontEnd(frontEnd, firstTime);
    const QLerpClipBlend *node = qobject_cast<const QLerpClipBlend *>(frontEnd);
    if (!node)
        return;

    m_blendFactor = node->blendFactor();
    m_startClipId = Qt3DCore::qIdForNode(node->startClip());
    m_endClipId = Qt3DCore::qIdForNode(node->endClip());
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/lerpclipblend.cpp, line 38, as _ZNK13Qt3DAnimation9Animation13LerpClipBlend7doBlendERK5QListIS2_IfEE
namespace Qt3DAnimation::Animation {
inline ClipResults LerpClipBlend::doBlend(const QList<ClipResults> &blendData) const
{
    Q_ASSERT(blendData.size() == 2);
    Q_ASSERT(blendData[0].size() == blendData[1].size());
    const qsizetype elementCount = blendData.first().size();
    ClipResults blendResults(elementCount);

    for (qsizetype i = 0; i < elementCount; ++i)
        blendResults[i] = (1.0f - m_blendFactor) * blendData[0][i] + (m_blendFactor * blendData[1][i]);

    return blendResults;
}
}  // namespace Qt3DAnimation::Animation
//  -----------------------------------------------------------------------

//  A Qt3DAnimation::Animation::LerpClipBlend that Python can take functions over in. Every Qt3DAnimation::Animation::LerpClipBlend
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef double (*CuteQt3DAnimation_Animation_LerpClipBlendCall0)(const void *, int *);
class CuteQt3DAnimation_Animation_LerpClipBlend : public Qt3DAnimation::Animation::LerpClipBlend {
public:
  using Qt3DAnimation::Animation::LerpClipBlend::LerpClipBlend;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK13Qt3DAnimation9Animation13ClipBlendNode8durationEv")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  double Qt3DAnimation::Animation::LerpClipBlend::duration() const
  double duration() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DAnimation_Animation_LerpClipBlendCall0 call = reinterpret_cast<CuteQt3DAnimation_Animation_LerpClipBlendCall0>(taken[0]);
      double given = call(this, &handled);
      if (handled) return given;
    }
    return Qt3DAnimation::Animation::LerpClipBlend::duration();
  }
};

//  Qt3DAnimation::Animation::LerpClipBlend::LerpClipBlend()
extern "C" Q_DECL_EXPORT
Qt3DAnimation::Animation::LerpClipBlend *ritual_ZN13Qt3DAnimation9Animation13LerpClipBlendC1Ev() {
  return new CuteQt3DAnimation_Animation_LerpClipBlend();
}

//  Qt3DAnimation::Animation::LerpClipBlend::~LerpClipBlend()
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation13LerpClipBlendD1Ev(
    Qt3DAnimation::Animation::LerpClipBlend *self) {
  delete self;
}

//  float Qt3DAnimation::Animation::LerpClipBlend::blendFactor() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK13Qt3DAnimation9Animation13LerpClipBlend11blendFactorEv(
    const Qt3DAnimation::Animation::LerpClipBlend *self) {
  return self->blendFactor();
}

//  void Qt3DAnimation::Animation::LerpClipBlend::setBlendFactor(float
//      blendFactor)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation13LerpClipBlend14setBlendFactorEf(
    Qt3DAnimation::Animation::LerpClipBlend *self,
    float blendFactor) {
  self->setBlendFactor(blendFactor);
}

//  Qt3DCore::QNodeId Qt3DAnimation::Animation::LerpClipBlend::startClipId()
//      const
extern "C" Q_DECL_EXPORT
Qt3DCore::QNodeId *ritual_ZNK13Qt3DAnimation9Animation13LerpClipBlend11startClipIdEv(
    const Qt3DAnimation::Animation::LerpClipBlend *self) {
  return new Qt3DCore::QNodeId(self->startClipId());
}

//  void
//      Qt3DAnimation::Animation::LerpClipBlend::setStartClipId(Qt3DCore::QNo
//      deId startClipId)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation13LerpClipBlend14setStartClipIdEN8Qt3DCore7QNodeIdE(
    Qt3DAnimation::Animation::LerpClipBlend *self,
    const Qt3DCore::QNodeId *startClipId) {
  self->setStartClipId(*startClipId);
}

//  Qt3DCore::QNodeId Qt3DAnimation::Animation::LerpClipBlend::endClipId()
//      const
extern "C" Q_DECL_EXPORT
Qt3DCore::QNodeId *ritual_ZNK13Qt3DAnimation9Animation13LerpClipBlend9endClipIdEv(
    const Qt3DAnimation::Animation::LerpClipBlend *self) {
  return new Qt3DCore::QNodeId(self->endClipId());
}

//  void
//      Qt3DAnimation::Animation::LerpClipBlend::setEndClipId(Qt3DCore::QNode
//      Id endClipId)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation13LerpClipBlend12setEndClipIdEN8Qt3DCore7QNodeIdE(
    Qt3DAnimation::Animation::LerpClipBlend *self,
    const Qt3DCore::QNodeId *endClipId) {
  self->setEndClipId(*endClipId);
}

//  void Qt3DAnimation::Animation::LerpClipBlend::syncFromFrontEnd(const
//      Qt3DCore::QNode *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation13LerpClipBlend16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DAnimation::Animation::LerpClipBlend *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->syncFromFrontEnd(frontEnd, firstTime);
}

//  QList<Qt3DCore::QNodeId>
//      Qt3DAnimation::Animation::LerpClipBlend::allDependencyIds() const
extern "C" Q_DECL_EXPORT
QList<Qt3DCore::QNodeId> *ritual_ZNK13Qt3DAnimation9Animation13LerpClipBlend16allDependencyIdsEv(
    const Qt3DAnimation::Animation::LerpClipBlend *self) {
  return new QList<Qt3DCore::QNodeId>(self->allDependencyIds());
}

//  QList<Qt3DCore::QNodeId>
//      Qt3DAnimation::Animation::LerpClipBlend::currentDependencyIds() const
extern "C" Q_DECL_EXPORT
QList<Qt3DCore::QNodeId> *ritual_ZNK13Qt3DAnimation9Animation13LerpClipBlend20currentDependencyIdsEv(
    const Qt3DAnimation::Animation::LerpClipBlend *self) {
  return new QList<Qt3DCore::QNodeId>(self->currentDependencyIds());
}

//  double Qt3DAnimation::Animation::LerpClipBlend::duration() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK13Qt3DAnimation9Animation13LerpClipBlend8durationEv(
    const Qt3DAnimation::Animation::LerpClipBlend *self) {
  return self->duration();
}

//  ClipResults Qt3DAnimation::Animation::LerpClipBlend::doBlend(const
//      QList<ClipResults> &blendData) const
extern "C" Q_DECL_EXPORT
Qt3DAnimation::Animation::ClipResults *ritual_ZNK13Qt3DAnimation9Animation13LerpClipBlend7doBlendERK5QListIS2_IfEE(
    const Qt3DAnimation::Animation::LerpClipBlend *self,
    const QList<Qt3DAnimation::Animation::ClipResults> *blendData) {
  return new Qt3DAnimation::Animation::ClipResults(
      self->doBlend(
          *blendData));
}

//  a Python function taken by a CuteQt3DAnimation_Animation_LerpClipBlend,
//      for the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DAnimation_Animation_LerpClipBlend(
    Qt3DAnimation::Animation::LerpClipBlend *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DAnimation_Animation_LerpClipBlend *>(self)->take(key, call);
}

//  double Qt3DAnimation::Animation::LerpClipBlend::duration() const
extern "C" Q_DECL_EXPORT
double ritual_own_ZNK13Qt3DAnimation9Animation13LerpClipBlend8durationEv(
    const Qt3DAnimation::Animation::LerpClipBlend *self) {
  return self->Qt3DAnimation::Animation::LerpClipBlend::duration();
}

//  a QList<Qt3DCore::QNodeId> a ritual of
//      Qt3DAnimation::Animation::LerpClipBlend gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DAnimation_Animation_LerpClipBlend__QList_Qt3DCore_QNodeId(
    QList<Qt3DCore::QNodeId> *self) {
  delete self;
}

//  a Qt3DAnimation::Animation::ClipResults a ritual of
//      Qt3DAnimation::Animation::LerpClipBlend gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DAnimation_Animation_LerpClipBlend__Qt3DAnimation_Animation_ClipResults(
    Qt3DAnimation::Animation::ClipResults *self) {
  delete self;
}
