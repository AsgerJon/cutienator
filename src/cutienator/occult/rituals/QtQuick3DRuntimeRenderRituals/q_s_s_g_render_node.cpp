//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendernode_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendernode_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qvectornd.h>
#include <QtGui/qquaternion.h>
#include <QtGui/qmatrix4x4.h>

//  QSSGRenderNode::QSSGRenderNode()
extern "C" Q_DECL_EXPORT
QSSGRenderNode *ritual_ZN14QSSGRenderNodeC1Ev() {
  return new QSSGRenderNode();
}

//  QSSGRenderNode::QSSGRenderNode(Type type, FlagT flags)
extern "C" Q_DECL_EXPORT
QSSGRenderNode *ritual_ZN14QSSGRenderNodeC1EN21QSSGRenderGraphObject4TypeEj(
    QSSGRenderGraphObject::Type type,
    QSSGRenderNode::FlagT flags) {
  return new QSSGRenderNode(type, flags);
}

//  QSSGRenderNode::~QSSGRenderNode()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSSGRenderNodeD1Ev(QSSGRenderNode *self) {
  delete self;
}

//  void QSSGRenderNode::markDirty(DirtyFlag dirtyFlag)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSSGRenderNode9markDirtyENS_9DirtyFlagE(
    QSSGRenderNode *self,
    QSSGRenderNode::DirtyFlag dirtyFlag) {
  self->markDirty(dirtyFlag);
}

//  void QSSGRenderNode::clearDirty(DirtyFlag dirtyFlag)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSSGRenderNode10clearDirtyENS_9DirtyFlagE(
    QSSGRenderNode *self,
    QSSGRenderNode::DirtyFlag dirtyFlag) {
  self->clearDirty(dirtyFlag);
}

//  bool QSSGRenderNode::isDirty(DirtyFlag dirtyFlag) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QSSGRenderNode7isDirtyENS_9DirtyFlagE(
    const QSSGRenderNode *self,
    QSSGRenderNode::DirtyFlag dirtyFlag) {
  return self->isDirty(dirtyFlag);
}

//  void QSSGRenderNode::setState(LocalState state, bool on)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSSGRenderNode8setStateENS_10LocalStateEb(
    QSSGRenderNode *self,
    QSSGRenderNode::LocalState state,
    bool on) {
  self->setState(state, on);
}

//  bool QSSGRenderNode::getLocalState(LocalState stateFlag) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QSSGRenderNode13getLocalStateENS_10LocalStateE(
    const QSSGRenderNode *self,
    QSSGRenderNode::LocalState stateFlag) {
  return self->getLocalState(stateFlag);
}

//  bool QSSGRenderNode::getGlobalState(GlobalState stateFlag) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QSSGRenderNode14getGlobalStateENS_11GlobalStateE(
    const QSSGRenderNode *self,
    QSSGRenderNode::GlobalState stateFlag) {
  return self->getGlobalState(stateFlag);
}

//  void QSSGRenderNode::removeFromGraph()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSSGRenderNode15removeFromGraphEv(QSSGRenderNode *self) {
  self->removeFromGraph();
}

//  QMatrix4x4 QSSGRenderNode::calculateTransformMatrix(QVector3D position,
//      QVector3D scale, QVector3D pivot, QQuaternion rotation)
extern "C" Q_DECL_EXPORT
QMatrix4x4 *ritual_ZN14QSSGRenderNode24calculateTransformMatrixE9QVector3DS0_S0_11QQuaternion(
    const QVector3D *position,
    const QVector3D *scale,
    const QVector3D *pivot,
    const QQuaternion *rotation) {
  return new QMatrix4x4(
      QSSGRenderNode::calculateTransformMatrix(
          *position,
          *scale,
          *pivot,
          *rotation));
}

//  QVector3D QSSGRenderNode::getGlobalPos(const QMatrix4x4 &globalTransform)
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZN14QSSGRenderNode12getGlobalPosERK10QMatrix4x4(
    const QMatrix4x4 *globalTransform) {
  return new QVector3D(QSSGRenderNode::getGlobalPos(*globalTransform));
}

//  QVector3D QSSGRenderNode::getDirection(const QMatrix4x4 &globalTransform)
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZN14QSSGRenderNode12getDirectionERK10QMatrix4x4(
    const QMatrix4x4 *globalTransform) {
  return new QVector3D(QSSGRenderNode::getDirection(*globalTransform));
}

//  QVector3D QSSGRenderNode::getScalingCorrectDirection(const QMatrix4x4
//      &globalTransform)
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZN14QSSGRenderNode26getScalingCorrectDirectionERK10QMatrix4x4(
    const QMatrix4x4 *globalTransform) {
  return new QVector3D(
      QSSGRenderNode::getScalingCorrectDirection(
          *globalTransform));
}

//  float QSSGRenderNode::signedSquared(float val)
extern "C" Q_DECL_EXPORT
float ritual_ZN14QSSGRenderNode13signedSquaredEf(float val) {
  return QSSGRenderNode::signedSquared(val);
}
