//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DAnimation/6.12.0/Qt3DAnimation/private/additiveclipblend_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <Qt3DAnimation/6.12.0/Qt3DAnimation/private/qt3danimation_global_p.h>
#include <Qt3DAnimation/Qt3DAnimation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DAnimation/6.12.0/Qt3DAnimation/private/additiveclipblend_p.h>
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
#include <Qt3DAnimation/private/managers_p.h>
#include <Qt3DAnimation/private/clipblendnode_p.h>
#include <Qt3DAnimation/private/additiveclipblend_p.h>
#include <Qt3DAnimation/qadditiveclipblend.h>
#include <Qt3DAnimation/private/qadditiveclipblend_p.h>
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

//  from ../qt3d/src/animation/backend/managers.cpp, line 31, as _ZNK13Qt3DAnimation9Animation20ClipBlendNodeManager10lookupNodeEN8Qt3DCore7QNodeIdE
namespace Qt3DAnimation::Animation {
inline ClipBlendNode *ClipBlendNodeManager::lookupNode(Qt3DCore::QNodeId id) const
{
    return m_nodes.value(id, nullptr);
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

//  from ../qt3d/src/animation/backend/additiveclipblend.cpp, line 14, as _ZN13Qt3DAnimation9Animation17AdditiveClipBlendC1Ev
namespace Qt3DAnimation::Animation {
inline AdditiveClipBlend::AdditiveClipBlend()
    : ClipBlendNode(ClipBlendNode::AdditiveBlendType)
    , m_baseClipId()
    , m_additiveClipId()
    , m_additiveFactor(0.0f)
{
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/additiveclipblend.cpp, line 22, as _ZN13Qt3DAnimation9Animation17AdditiveClipBlendD1Ev
namespace Qt3DAnimation::Animation {
inline AdditiveClipBlend::~AdditiveClipBlend()
{
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/additiveclipblend.cpp, line 26, as _ZN13Qt3DAnimation9Animation17AdditiveClipBlend16syncFromFrontEndEPKN8Qt3DCore5QNodeEb
namespace Qt3DAnimation::Animation {
inline void AdditiveClipBlend::syncFromFrontEnd(const Qt3DCore::QNode *frontEnd, bool firstTime)
{
    BackendNode::syncFromFrontEnd(frontEnd, firstTime);
    const QAdditiveClipBlend *node = qobject_cast<const QAdditiveClipBlend *>(frontEnd);
    if (!node)
        return;

    m_additiveFactor = node->additiveFactor();
    m_baseClipId = Qt3DCore::qIdForNode(node->baseClip());
    m_additiveClipId = Qt3DCore::qIdForNode(node->additiveClip());
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/additiveclipblend.cpp, line 38, as _ZNK13Qt3DAnimation9Animation17AdditiveClipBlend7doBlendERK5QListIS2_IfEE
namespace Qt3DAnimation::Animation {
inline ClipResults AdditiveClipBlend::doBlend(const QList<ClipResults> &blendData) const
{
    Q_ASSERT(blendData.size() == 2);
    Q_ASSERT(blendData[0].size() == blendData[1].size());
    const qsizetype elementCount = blendData.first().size();
    ClipResults blendResults(elementCount);

    for (qsizetype i = 0; i < elementCount; ++i)
        blendResults[i] = blendData[0][i] + m_additiveFactor * blendData[1][i];

    return blendResults;
}
}  // namespace Qt3DAnimation::Animation
//  -----------------------------------------------------------------------

//  A Qt3DAnimation::Animation::AdditiveClipBlend that Python can take functions over in. Every Qt3DAnimation::Animation::AdditiveClipBlend
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef double (*CuteQt3DAnimation_Animation_AdditiveClipBlendCall0)(const void *, int *);
class CuteQt3DAnimation_Animation_AdditiveClipBlend : public Qt3DAnimation::Animation::AdditiveClipBlend {
public:
  using Qt3DAnimation::Animation::AdditiveClipBlend::AdditiveClipBlend;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK13Qt3DAnimation9Animation13ClipBlendNode8durationEv")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  double Qt3DAnimation::Animation::AdditiveClipBlend::duration() const
  double duration() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DAnimation_Animation_AdditiveClipBlendCall0 call = reinterpret_cast<CuteQt3DAnimation_Animation_AdditiveClipBlendCall0>(taken[0]);
      double given = call(this, &handled);
      if (handled) return given;
    }
    return Qt3DAnimation::Animation::AdditiveClipBlend::duration();
  }
};

//  Qt3DAnimation::Animation::AdditiveClipBlend::AdditiveClipBlend()
extern "C" Q_DECL_EXPORT
Qt3DAnimation::Animation::AdditiveClipBlend *ritual_ZN13Qt3DAnimation9Animation17AdditiveClipBlendC1Ev() {
  return new CuteQt3DAnimation_Animation_AdditiveClipBlend();
}

//  Qt3DAnimation::Animation::AdditiveClipBlend::~AdditiveClipBlend()
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation17AdditiveClipBlendD1Ev(
    Qt3DAnimation::Animation::AdditiveClipBlend *self) {
  delete self;
}

//  Qt3DCore::QNodeId
//      Qt3DAnimation::Animation::AdditiveClipBlend::baseClipId() const
extern "C" Q_DECL_EXPORT
Qt3DCore::QNodeId *ritual_ZNK13Qt3DAnimation9Animation17AdditiveClipBlend10baseClipIdEv(
    const Qt3DAnimation::Animation::AdditiveClipBlend *self) {
  return new Qt3DCore::QNodeId(self->baseClipId());
}

//  void Qt3DAnimation::Animation::AdditiveClipBlend::setBaseClipId(Qt3DCore:
//      :QNodeId baseClipId)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation17AdditiveClipBlend13setBaseClipIdEN8Qt3DCore7QNodeIdE(
    Qt3DAnimation::Animation::AdditiveClipBlend *self,
    const Qt3DCore::QNodeId *baseClipId) {
  self->setBaseClipId(*baseClipId);
}

//  Qt3DCore::QNodeId
//      Qt3DAnimation::Animation::AdditiveClipBlend::additiveClipId() const
extern "C" Q_DECL_EXPORT
Qt3DCore::QNodeId *ritual_ZNK13Qt3DAnimation9Animation17AdditiveClipBlend14additiveClipIdEv(
    const Qt3DAnimation::Animation::AdditiveClipBlend *self) {
  return new Qt3DCore::QNodeId(self->additiveClipId());
}

//  void Qt3DAnimation::Animation::AdditiveClipBlend::setAdditiveClipId(Qt3DC
//      ore::QNodeId additiveClipId)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation17AdditiveClipBlend17setAdditiveClipIdEN8Qt3DCore7QNodeIdE(
    Qt3DAnimation::Animation::AdditiveClipBlend *self,
    const Qt3DCore::QNodeId *additiveClipId) {
  self->setAdditiveClipId(*additiveClipId);
}

//  float Qt3DAnimation::Animation::AdditiveClipBlend::additiveFactor() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK13Qt3DAnimation9Animation17AdditiveClipBlend14additiveFactorEv(
    const Qt3DAnimation::Animation::AdditiveClipBlend *self) {
  return self->additiveFactor();
}

//  void Qt3DAnimation::Animation::AdditiveClipBlend::setAdditiveFactor(float
//      additiveFactor)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation17AdditiveClipBlend17setAdditiveFactorEf(
    Qt3DAnimation::Animation::AdditiveClipBlend *self,
    float additiveFactor) {
  self->setAdditiveFactor(additiveFactor);
}

//  void Qt3DAnimation::Animation::AdditiveClipBlend::syncFromFrontEnd(const
//      Qt3DCore::QNode *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation17AdditiveClipBlend16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DAnimation::Animation::AdditiveClipBlend *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->syncFromFrontEnd(frontEnd, firstTime);
}

//  QList<Qt3DCore::QNodeId>
//      Qt3DAnimation::Animation::AdditiveClipBlend::allDependencyIds() const
extern "C" Q_DECL_EXPORT
QList<Qt3DCore::QNodeId> *ritual_ZNK13Qt3DAnimation9Animation17AdditiveClipBlend16allDependencyIdsEv(
    const Qt3DAnimation::Animation::AdditiveClipBlend *self) {
  return new QList<Qt3DCore::QNodeId>(self->allDependencyIds());
}

//  QList<Qt3DCore::QNodeId>
//      Qt3DAnimation::Animation::AdditiveClipBlend::currentDependencyIds()
//      const
extern "C" Q_DECL_EXPORT
QList<Qt3DCore::QNodeId> *ritual_ZNK13Qt3DAnimation9Animation17AdditiveClipBlend20currentDependencyIdsEv(
    const Qt3DAnimation::Animation::AdditiveClipBlend *self) {
  return new QList<Qt3DCore::QNodeId>(self->currentDependencyIds());
}

//  double Qt3DAnimation::Animation::AdditiveClipBlend::duration() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK13Qt3DAnimation9Animation17AdditiveClipBlend8durationEv(
    const Qt3DAnimation::Animation::AdditiveClipBlend *self) {
  return self->duration();
}

//  ClipResults Qt3DAnimation::Animation::AdditiveClipBlend::doBlend(const
//      QList<ClipResults> &blendData) const
extern "C" Q_DECL_EXPORT
Qt3DAnimation::Animation::ClipResults *ritual_ZNK13Qt3DAnimation9Animation17AdditiveClipBlend7doBlendERK5QListIS2_IfEE(
    const Qt3DAnimation::Animation::AdditiveClipBlend *self,
    const QList<Qt3DAnimation::Animation::ClipResults> *blendData) {
  return new Qt3DAnimation::Animation::ClipResults(
      self->doBlend(
          *blendData));
}

//  a Python function taken by a
//      CuteQt3DAnimation_Animation_AdditiveClipBlend, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DAnimation_Animation_AdditiveClipBlend(
    Qt3DAnimation::Animation::AdditiveClipBlend *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DAnimation_Animation_AdditiveClipBlend *>(self)->take(key, call);
}

//  double Qt3DAnimation::Animation::AdditiveClipBlend::duration() const
extern "C" Q_DECL_EXPORT
double ritual_own_ZNK13Qt3DAnimation9Animation17AdditiveClipBlend8durationEv(
    const Qt3DAnimation::Animation::AdditiveClipBlend *self) {
  return self->Qt3DAnimation::Animation::AdditiveClipBlend::duration();
}

//  a QList<Qt3DCore::QNodeId> a ritual of
//      Qt3DAnimation::Animation::AdditiveClipBlend gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DAnimation_Animation_AdditiveClipBlend__QList_Qt3DCore_QNodeId(
    QList<Qt3DCore::QNodeId> *self) {
  delete self;
}

//  a Qt3DAnimation::Animation::ClipResults a ritual of
//      Qt3DAnimation::Animation::AdditiveClipBlend gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DAnimation_Animation_AdditiveClipBlend__Qt3DAnimation_Animation_ClipResults(
    Qt3DAnimation::Animation::ClipResults *self) {
  delete self;
}
