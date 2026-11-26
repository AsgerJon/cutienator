//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DAnimation/6.12.0/Qt3DAnimation/private/clipblendvalue_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DAnimation/6.12.0/Qt3DAnimation/private/qt3danimation_global_p.h>
#include <Qt3DAnimation/Qt3DAnimation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DAnimation/6.12.0/Qt3DAnimation/private/clipblendvalue_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/qnodeid.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DAnimation/6.12.0/Qt3DAnimation/private/animationutils_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#include <QtCore/QList>
#include <Qt3DCore/Qt3DCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DAnimation/private/clipblendnode_p.h>
#include <Qt3DAnimation/qabstractanimationclip.h>
#include <Qt3DAnimation/private/clipblendvalue_p.h>
#include <Qt3DAnimation/qclipblendvalue.h>
#include <Qt3DAnimation/private/qclipblendvalue_p.h>
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

//  from ../qt3d/src/animation/backend/clipblendvalue.cpp, line 22, as _ZN13Qt3DAnimation9Animation14ClipBlendValue16syncFromFrontEndEPKN8Qt3DCore5QNodeEb
namespace Qt3DAnimation::Animation {
inline void ClipBlendValue::syncFromFrontEnd(const Qt3DCore::QNode *frontEnd, bool firstTime)
{
    BackendNode::syncFromFrontEnd(frontEnd, firstTime);
    const QClipBlendValue *node = qobject_cast<const QClipBlendValue *>(frontEnd);
    if (!node)
        return;

    m_clipId = Qt3DCore::qIdForNode(node->clip());
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/clipblendvalue.cpp, line 32, as _ZNK13Qt3DAnimation9Animation14ClipBlendValue7doBlendERK5QListIS2_IfEE
namespace Qt3DAnimation::Animation {
inline ClipResults ClipBlendValue::doBlend(const QList<ClipResults> &blendData) const
{
    // Should never be called for the value node
    Q_UNUSED(blendData);
    Q_UNREACHABLE_RETURN(ClipResults());
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/clipblendvalue.cpp, line 39, as _ZNK13Qt3DAnimation9Animation14ClipBlendValue8durationEv
namespace Qt3DAnimation::Animation {
inline double ClipBlendValue::duration() const
{
    if (m_clipId.isNull())
        return 0.0;
    AnimationClip *clip = m_handler->animationClipLoaderManager()->lookupResource(m_clipId);
    Q_ASSERT(clip);
    return clip->duration();
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

//  from ../qt3d/src/animation/backend/clipblendvalue.cpp, line 13, as _ZN13Qt3DAnimation9Animation14ClipBlendValueC1Ev
namespace Qt3DAnimation::Animation {
inline ClipBlendValue::ClipBlendValue()
    : ClipBlendNode(ValueType)
{
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/clipblendvalue.cpp, line 18, as _ZN13Qt3DAnimation9Animation14ClipBlendValueD1Ev
namespace Qt3DAnimation::Animation {
inline ClipBlendValue::~ClipBlendValue()
{
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/clipblendvalue.cpp, line 48, as _ZN13Qt3DAnimation9Animation14ClipBlendValue13setClipFormatEN8Qt3DCore7QNodeIdERKNS0_10ClipFormatE
namespace Qt3DAnimation::Animation {
inline void ClipBlendValue::setClipFormat(Qt3DCore::QNodeId animatorId, const ClipFormat &formatIndices)
{
    // Do we already have an entry for this animator?
    const int animatorIndex = m_animatorIds.indexOf(animatorId);
    if (animatorIndex == -1) {
        // Nope, add it
        m_animatorIds.push_back(animatorId);
        m_clipFormats.push_back(formatIndices);
    } else {
        m_clipFormats[animatorIndex] = formatIndices;
    }
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/clipblendvalue.cpp, line 61, as _ZN13Qt3DAnimation9Animation14ClipBlendValue10clipFormatEN8Qt3DCore7QNodeIdE
namespace Qt3DAnimation::Animation {
inline ClipFormat &ClipBlendValue::clipFormat(Qt3DCore::QNodeId animatorId)
{
    const int animatorIndex = m_animatorIds.indexOf(animatorId);
    return m_clipFormats[animatorIndex];
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/clipblendvalue.cpp, line 67, as _ZNK13Qt3DAnimation9Animation14ClipBlendValue10clipFormatEN8Qt3DCore7QNodeIdE
namespace Qt3DAnimation::Animation {
inline const ClipFormat &ClipBlendValue::clipFormat(Qt3DCore::QNodeId animatorId) const
{
    const int animatorIndex = m_animatorIds.indexOf(animatorId);
    return m_clipFormats[animatorIndex];
}
}  // namespace Qt3DAnimation::Animation
//  -----------------------------------------------------------------------

//  A Qt3DAnimation::Animation::ClipBlendValue that Python can take functions over in. Every Qt3DAnimation::Animation::ClipBlendValue
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DAnimation_Animation_ClipBlendValueCall0)(const void *, const Qt3DCore::QNode *, bool, int *);
typedef double (*CuteQt3DAnimation_Animation_ClipBlendValueCall1)(const void *, int *);
class CuteQt3DAnimation_Animation_ClipBlendValue : public Qt3DAnimation::Animation::ClipBlendValue {
public:
  using Qt3DAnimation::Animation::ClipBlendValue::ClipBlendValue;
  void *taken[2] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN8Qt3DCore12QBackendNode16syncFromFrontEndEPKNS_5QNodeEb")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK13Qt3DAnimation9Animation13ClipBlendNode8durationEv")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

  //  void Qt3DAnimation::Animation::ClipBlendValue::syncFromFrontEnd(const
  //      Qt3DCore::QNode *frontEnd, bool firstTime)
  void syncFromFrontEnd(
      const Qt3DCore::QNode *frontEnd,
      bool firstTime) override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DAnimation_Animation_ClipBlendValueCall0 call = reinterpret_cast<CuteQt3DAnimation_Animation_ClipBlendValueCall0>(taken[0]);
      call(this, frontEnd, firstTime, &handled);
      if (handled) return;
    }
    Qt3DAnimation::Animation::ClipBlendValue::syncFromFrontEnd(frontEnd, firstTime);
  }

  //  double Qt3DAnimation::Animation::ClipBlendValue::duration() const
  double duration() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DAnimation_Animation_ClipBlendValueCall1 call = reinterpret_cast<CuteQt3DAnimation_Animation_ClipBlendValueCall1>(taken[1]);
      double given = call(this, &handled);
      if (handled) return given;
    }
    return Qt3DAnimation::Animation::ClipBlendValue::duration();
  }
};

//  Qt3DAnimation::Animation::ClipBlendValue::ClipBlendValue()
extern "C" Q_DECL_EXPORT
Qt3DAnimation::Animation::ClipBlendValue *ritual_ZN13Qt3DAnimation9Animation14ClipBlendValueC1Ev() {
  return new CuteQt3DAnimation_Animation_ClipBlendValue();
}

//  Qt3DAnimation::Animation::ClipBlendValue::~ClipBlendValue()
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation14ClipBlendValueD1Ev(
    Qt3DAnimation::Animation::ClipBlendValue *self) {
  delete self;
}

//  Qt3DCore::QNodeId Qt3DAnimation::Animation::ClipBlendValue::clipId()
//      const
extern "C" Q_DECL_EXPORT
Qt3DCore::QNodeId *ritual_ZNK13Qt3DAnimation9Animation14ClipBlendValue6clipIdEv(
    const Qt3DAnimation::Animation::ClipBlendValue *self) {
  return new Qt3DCore::QNodeId(self->clipId());
}

//  void
//      Qt3DAnimation::Animation::ClipBlendValue::setClipId(Qt3DCore::QNodeId
//      clipId)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation14ClipBlendValue9setClipIdEN8Qt3DCore7QNodeIdE(
    Qt3DAnimation::Animation::ClipBlendValue *self,
    const Qt3DCore::QNodeId *clipId) {
  self->setClipId(*clipId);
}

//  void Qt3DAnimation::Animation::ClipBlendValue::syncFromFrontEnd(const
//      Qt3DCore::QNode *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation14ClipBlendValue16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DAnimation::Animation::ClipBlendValue *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->syncFromFrontEnd(frontEnd, firstTime);
}

//  QList<Qt3DCore::QNodeId>
//      Qt3DAnimation::Animation::ClipBlendValue::allDependencyIds() const
extern "C" Q_DECL_EXPORT
QList<Qt3DCore::QNodeId> *ritual_ZNK13Qt3DAnimation9Animation14ClipBlendValue16allDependencyIdsEv(
    const Qt3DAnimation::Animation::ClipBlendValue *self) {
  return new QList<Qt3DCore::QNodeId>(self->allDependencyIds());
}

//  QList<Qt3DCore::QNodeId>
//      Qt3DAnimation::Animation::ClipBlendValue::currentDependencyIds()
//      const
extern "C" Q_DECL_EXPORT
QList<Qt3DCore::QNodeId> *ritual_ZNK13Qt3DAnimation9Animation14ClipBlendValue20currentDependencyIdsEv(
    const Qt3DAnimation::Animation::ClipBlendValue *self) {
  return new QList<Qt3DCore::QNodeId>(self->currentDependencyIds());
}

//  double Qt3DAnimation::Animation::ClipBlendValue::duration() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK13Qt3DAnimation9Animation14ClipBlendValue8durationEv(
    const Qt3DAnimation::Animation::ClipBlendValue *self) {
  return self->duration();
}

//  void
//      Qt3DAnimation::Animation::ClipBlendValue::setClipFormat(Qt3DCore::QNo
//      deId animatorId, const ClipFormat &formatIndices)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation14ClipBlendValue13setClipFormatEN8Qt3DCore7QNodeIdERKNS0_10ClipFormatE(
    Qt3DAnimation::Animation::ClipBlendValue *self,
    const Qt3DCore::QNodeId *animatorId,
    const Qt3DAnimation::Animation::ClipFormat *formatIndices) {
  self->setClipFormat(*animatorId, *formatIndices);
}

//  ClipFormat
//      &Qt3DAnimation::Animation::ClipBlendValue::clipFormat(Qt3DCore::QNode
//      Id animatorId)
extern "C" Q_DECL_EXPORT
Qt3DAnimation::Animation::ClipFormat *ritual_ZN13Qt3DAnimation9Animation14ClipBlendValue10clipFormatEN8Qt3DCore7QNodeIdE(
    Qt3DAnimation::Animation::ClipBlendValue *self,
    const Qt3DCore::QNodeId *animatorId) {
  return &(self->clipFormat(*animatorId));
}

//  const ClipFormat
//      &Qt3DAnimation::Animation::ClipBlendValue::clipFormat(Qt3DCore::QNode
//      Id animatorId) const
extern "C" Q_DECL_EXPORT
Qt3DAnimation::Animation::ClipFormat *ritual_ZNK13Qt3DAnimation9Animation14ClipBlendValue10clipFormatEN8Qt3DCore7QNodeIdE(
    const Qt3DAnimation::Animation::ClipBlendValue *self,
    const Qt3DCore::QNodeId *animatorId) {
  return new Qt3DAnimation::Animation::ClipFormat(
      self->clipFormat(
          *animatorId));
}

//  ClipResults Qt3DAnimation::Animation::ClipBlendValue::doBlend(const
//      QList<ClipResults> &blendData) const
extern "C" Q_DECL_EXPORT
Qt3DAnimation::Animation::ClipResults *ritual_ZNK13Qt3DAnimation9Animation14ClipBlendValue7doBlendERK5QListIS2_IfEE(
    const Qt3DAnimation::Animation::ClipBlendValue *self,
    const QList<Qt3DAnimation::Animation::ClipResults> *blendData) {
  return new Qt3DAnimation::Animation::ClipResults(
      self->doBlend(
          *blendData));
}

//  a Python function taken by a CuteQt3DAnimation_Animation_ClipBlendValue,
//      for the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DAnimation_Animation_ClipBlendValue(
    Qt3DAnimation::Animation::ClipBlendValue *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DAnimation_Animation_ClipBlendValue *>(self)->take(key, call);
}

//  void Qt3DAnimation::Animation::ClipBlendValue::syncFromFrontEnd(const
//      Qt3DCore::QNode *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13Qt3DAnimation9Animation14ClipBlendValue16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DAnimation::Animation::ClipBlendValue *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->Qt3DAnimation::Animation::ClipBlendValue::syncFromFrontEnd(
      frontEnd,
      firstTime);
}

//  double Qt3DAnimation::Animation::ClipBlendValue::duration() const
extern "C" Q_DECL_EXPORT
double ritual_own_ZNK13Qt3DAnimation9Animation14ClipBlendValue8durationEv(
    const Qt3DAnimation::Animation::ClipBlendValue *self) {
  return self->Qt3DAnimation::Animation::ClipBlendValue::duration();
}

//  a QList<Qt3DCore::QNodeId> a ritual of
//      Qt3DAnimation::Animation::ClipBlendValue gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DAnimation_Animation_ClipBlendValue__QList_Qt3DCore_QNodeId(
    QList<Qt3DCore::QNodeId> *self) {
  delete self;
}

//  a Qt3DAnimation::Animation::ClipResults a ritual of
//      Qt3DAnimation::Animation::ClipBlendValue gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DAnimation_Animation_ClipBlendValue__Qt3DAnimation_Animation_ClipResults(
    Qt3DAnimation::Animation::ClipResults *self) {
  delete self;
}
