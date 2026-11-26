//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DAnimation/6.12.0/Qt3DAnimation/private/clipblendnode_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DAnimation/6.12.0/Qt3DAnimation/private/qt3danimation_global_p.h>
#include <Qt3DAnimation/Qt3DAnimation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DAnimation/6.12.0/Qt3DAnimation/private/clipblendnode_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/qnodeid.h>
#include <cstring>
#include <Qt3DCore/Qt3DCore>
#include <QtCore/QList>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DAnimation/private/managers_p.h>
#include <Qt3DAnimation/private/clipblendnode_p.h>
#include <Qt3DAnimation/private/clipblendnode_p.h>
#include <Qt3DAnimation/qabstractanimationclip.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/animation/backend/managers.cpp, line 31, as _ZNK13Qt3DAnimation9Animation20ClipBlendNodeManager10lookupNodeEN8Qt3DCore7QNodeIdE
namespace Qt3DAnimation::Animation {
inline ClipBlendNode *ClipBlendNodeManager::lookupNode(Qt3DCore::QNodeId id) const
{
    return m_nodes.value(id, nullptr);
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/clipblendnode.cpp, line 20, as _ZN13Qt3DAnimation9Animation13ClipBlendNodeD1Ev
namespace Qt3DAnimation::Animation {
inline ClipBlendNode::~ClipBlendNode()
{
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/clipblendnode.cpp, line 24, as _ZN13Qt3DAnimation9Animation13ClipBlendNode23setClipBlendNodeManagerEPNS0_20ClipBlendNodeManagerE
namespace Qt3DAnimation::Animation {
inline void ClipBlendNode::setClipBlendNodeManager(ClipBlendNodeManager *manager)
{
    m_manager = manager;
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/clipblendnode.cpp, line 97, as _ZN13Qt3DAnimation9Animation13ClipBlendNode5blendEN8Qt3DCore7QNodeIdE
namespace Qt3DAnimation::Animation {
inline void ClipBlendNode::blend(Qt3DCore::QNodeId animatorId)
{
    // Obtain the clip results from each of the dependencies
    const QList<Qt3DCore::QNodeId> dependencyNodeIds = currentDependencyIds();
    const qsizetype dependencyCount = dependencyNodeIds.size();
    QList<ClipResults> blendData;
    blendData.reserve(dependencyCount);
    for (const auto &dependencyId : dependencyNodeIds) {
        ClipBlendNode *dependencyNode = clipBlendNodeManager()->lookupNode(dependencyId);
        ClipResults blendDataElement = dependencyNode->clipResults(animatorId);
        blendData.push_back(blendDataElement);
    }

    // Ask the blend node to perform the actual blend operation on the data
    // from the dependencies
    ClipResults blendedResults = doBlend(blendData);
    setClipResults(animatorId, blendedResults);
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/clipblendnode.cpp, line 34, as _ZN13Qt3DAnimation9Animation13ClipBlendNode14setClipResultsEN8Qt3DCore7QNodeIdERK5QListIfE
namespace Qt3DAnimation::Animation {
inline void ClipBlendNode::setClipResults(Qt3DCore::QNodeId animatorId, const ClipResults &clipResults)
{
    // Do we already have an entry for this animator?
    const qsizetype animatorIndex = m_animatorIds.indexOf(animatorId);
    if (animatorIndex == -1) {
        // Nope, add it
        m_animatorIds.push_back(animatorId);
        m_clipResults.push_back(clipResults);
    } else {
        m_clipResults[animatorIndex] = clipResults;
    }
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/clipblendnode.cpp, line 47, as _ZNK13Qt3DAnimation9Animation13ClipBlendNode11clipResultsEN8Qt3DCore7QNodeIdE
namespace Qt3DAnimation::Animation {
inline ClipResults ClipBlendNode::clipResults(Qt3DCore::QNodeId animatorId) const
{
    const qsizetype animatorIndex = m_animatorIds.indexOf(animatorId);
    if (animatorIndex != -1)
        return m_clipResults[animatorIndex];
    return ClipResults();
}
}  // namespace Qt3DAnimation::Animation
//  -----------------------------------------------------------------------

//  A Qt3DAnimation::Animation::ClipBlendNode that Python can take functions over in. Every Qt3DAnimation::Animation::ClipBlendNode
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef double (*CuteQt3DAnimation_Animation_ClipBlendNodeCall0)(const void *, int *);
typedef void (*CuteQt3DAnimation_Animation_ClipBlendNodeCall1)(const void *, const Qt3DCore::QNode *, bool, int *);
class CuteQt3DAnimation_Animation_ClipBlendNode : public Qt3DAnimation::Animation::ClipBlendNode {
public:
  using Qt3DAnimation::Animation::ClipBlendNode::ClipBlendNode;
  void *taken[2] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK13Qt3DAnimation9Animation13ClipBlendNode8durationEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8Qt3DCore12QBackendNode16syncFromFrontEndEPKNS_5QNodeEb")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

  //  double Qt3DAnimation::Animation::ClipBlendNode::duration() const
  double duration() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DAnimation_Animation_ClipBlendNodeCall0 call = reinterpret_cast<CuteQt3DAnimation_Animation_ClipBlendNodeCall0>(taken[0]);
      double given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void Qt3DAnimation::Animation::BackendNode::syncFromFrontEnd(const
  //      Qt3DCore::QNode *frontEnd, bool firstTime)
  void syncFromFrontEnd(
      const Qt3DCore::QNode *frontEnd,
      bool firstTime) override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DAnimation_Animation_ClipBlendNodeCall1 call = reinterpret_cast<CuteQt3DAnimation_Animation_ClipBlendNodeCall1>(taken[1]);
      call(this, frontEnd, firstTime, &handled);
      if (handled) return;
    }
    Qt3DAnimation::Animation::BackendNode::syncFromFrontEnd(frontEnd, firstTime);
  }
};

//  Qt3DAnimation::Animation::ClipBlendNode::~ClipBlendNode()
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation13ClipBlendNodeD1Ev(
    Qt3DAnimation::Animation::ClipBlendNode *self) {
  delete self;
}

//  void Qt3DAnimation::Animation::ClipBlendNode::setClipBlendNodeManager(Cli
//      pBlendNodeManager *manager)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation13ClipBlendNode23setClipBlendNodeManagerEPNS0_20ClipBlendNodeManagerE(
    Qt3DAnimation::Animation::ClipBlendNode *self,
    Qt3DAnimation::Animation::ClipBlendNodeManager *manager) {
  self->setClipBlendNodeManager(manager);
}

//  ClipBlendNodeManager
//      *Qt3DAnimation::Animation::ClipBlendNode::clipBlendNodeManager()
//      const
extern "C" Q_DECL_EXPORT
Qt3DAnimation::Animation::ClipBlendNodeManager *ritual_ZNK13Qt3DAnimation9Animation13ClipBlendNode20clipBlendNodeManagerEv(
    const Qt3DAnimation::Animation::ClipBlendNode *self) {
  return self->clipBlendNodeManager();
}

//  void Qt3DAnimation::Animation::ClipBlendNode::blend(Qt3DCore::QNodeId
//      animatorId)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation13ClipBlendNode5blendEN8Qt3DCore7QNodeIdE(
    Qt3DAnimation::Animation::ClipBlendNode *self,
    const Qt3DCore::QNodeId *animatorId) {
  self->blend(*animatorId);
}

//  void
//      Qt3DAnimation::Animation::ClipBlendNode::setClipResults(Qt3DCore::QNo
//      deId animatorId, const ClipResults &clipResults)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation13ClipBlendNode14setClipResultsEN8Qt3DCore7QNodeIdERK5QListIfE(
    Qt3DAnimation::Animation::ClipBlendNode *self,
    const Qt3DCore::QNodeId *animatorId,
    const Qt3DAnimation::Animation::ClipResults *clipResults) {
  self->setClipResults(*animatorId, *clipResults);
}

//  ClipResults
//      Qt3DAnimation::Animation::ClipBlendNode::clipResults(Qt3DCore::QNodeI
//      d animatorId) const
extern "C" Q_DECL_EXPORT
Qt3DAnimation::Animation::ClipResults *ritual_ZNK13Qt3DAnimation9Animation13ClipBlendNode11clipResultsEN8Qt3DCore7QNodeIdE(
    const Qt3DAnimation::Animation::ClipBlendNode *self,
    const Qt3DCore::QNodeId *animatorId) {
  return new Qt3DAnimation::Animation::ClipResults(
      self->clipResults(
          *animatorId));
}

//  QList<Qt3DCore::QNodeId>
//      Qt3DAnimation::Animation::ClipBlendNode::allDependencyIds() const
extern "C" Q_DECL_EXPORT
QList<Qt3DCore::QNodeId> *ritual_ZNK13Qt3DAnimation9Animation13ClipBlendNode16allDependencyIdsEv(
    const Qt3DAnimation::Animation::ClipBlendNode *self) {
  return new QList<Qt3DCore::QNodeId>(self->allDependencyIds());
}

//  QList<Qt3DCore::QNodeId>
//      Qt3DAnimation::Animation::ClipBlendNode::currentDependencyIds() const
extern "C" Q_DECL_EXPORT
QList<Qt3DCore::QNodeId> *ritual_ZNK13Qt3DAnimation9Animation13ClipBlendNode20currentDependencyIdsEv(
    const Qt3DAnimation::Animation::ClipBlendNode *self) {
  return new QList<Qt3DCore::QNodeId>(self->currentDependencyIds());
}

//  double Qt3DAnimation::Animation::ClipBlendNode::duration() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK13Qt3DAnimation9Animation13ClipBlendNode8durationEv(
    const Qt3DAnimation::Animation::ClipBlendNode *self) {
  return self->duration();
}

//  ClipResults Qt3DAnimation::Animation::ClipBlendNode::doBlend(const
//      QList<ClipResults> &blendData) const
extern "C" Q_DECL_EXPORT
Qt3DAnimation::Animation::ClipResults *ritual_ZNK13Qt3DAnimation9Animation13ClipBlendNode7doBlendERK5QListIS2_IfEE(
    const Qt3DAnimation::Animation::ClipBlendNode *self,
    const QList<Qt3DAnimation::Animation::ClipResults> *blendData) {
  return new Qt3DAnimation::Animation::ClipResults(
      self->doBlend(
          *blendData));
}

//  a Python function taken by a CuteQt3DAnimation_Animation_ClipBlendNode,
//      for the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DAnimation_Animation_ClipBlendNode(
    Qt3DAnimation::Animation::ClipBlendNode *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DAnimation_Animation_ClipBlendNode *>(self)->take(key, call);
}

//  a Qt3DAnimation::Animation::ClipResults a ritual of
//      Qt3DAnimation::Animation::ClipBlendNode gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DAnimation_Animation_ClipBlendNode__Qt3DAnimation_Animation_ClipResults(
    Qt3DAnimation::Animation::ClipResults *self) {
  delete self;
}

//  a QList<Qt3DCore::QNodeId> a ritual of
//      Qt3DAnimation::Animation::ClipBlendNode gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DAnimation_Animation_ClipBlendNode__QList_Qt3DCore_QNodeId(
    QList<Qt3DCore::QNodeId> *self) {
  delete self;
}
