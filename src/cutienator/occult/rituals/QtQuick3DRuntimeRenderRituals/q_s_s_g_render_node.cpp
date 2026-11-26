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
#include <QtQuick3DUtils/QtQuick3DUtils>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qssgbounds3_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

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

//  void QSSGRenderNode::addChild(QSSGRenderNode &inChild)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSSGRenderNode8addChildERS_(
    QSSGRenderNode *self,
    QSSGRenderNode *inChild) {
  self->addChild(*inChild);
}

//  void QSSGRenderNode::removeChild(QSSGRenderNode &inChild)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSSGRenderNode11removeChildERS_(
    QSSGRenderNode *self,
    QSSGRenderNode *inChild) {
  self->removeChild(*inChild);
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

//  QSSGBounds3 QSSGRenderNode::getBounds(QSSGBufferManager &inManager, bool
//      inIncludeChildren) const
extern "C" Q_DECL_EXPORT
QSSGBounds3 *ritual_ZNK14QSSGRenderNode9getBoundsER17QSSGBufferManagerb(
    const QSSGRenderNode *self,
    QSSGBufferManager *inManager,
    bool inIncludeChildren) {
  return new QSSGBounds3(self->getBounds(*inManager, inIncludeChildren));
}

//  QSSGBounds3 QSSGRenderNode::getChildBounds(QSSGBufferManager &inManager)
//      const
extern "C" Q_DECL_EXPORT
QSSGBounds3 *ritual_ZNK14QSSGRenderNode14getChildBoundsER17QSSGBufferManager(
    const QSSGRenderNode *self,
    QSSGBufferManager *inManager) {
  return new QSSGBounds3(self->getChildBounds(*inManager));
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

//  void QSSGRenderNode::calculateMVP(const QMatrix4x4 &globalTransform,
//      const QMatrix4x4 &inViewProjection, QMatrix4x4 &outMVP)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSSGRenderNode12calculateMVPERK10QMatrix4x4S2_RS0_(
    const QMatrix4x4 *globalTransform,
    const QMatrix4x4 *inViewProjection,
    QMatrix4x4 *outMVP) {
  QSSGRenderNode::calculateMVP(*globalTransform, *inViewProjection, *outMVP);
}

//  void QSSGRenderNode::calculateNormalMatrix(const QMatrix4x4
//      &globalTransform, QMatrix3x3 &outNormalMatrix)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSSGRenderNode21calculateNormalMatrixERK10QMatrix4x4R14QGenericMatrixILi3ELi3EfE(
    const QMatrix4x4 *globalTransform,
    QMatrix3x3 *outNormalMatrix) {
  QSSGRenderNode::calculateNormalMatrix(*globalTransform, *outNormalMatrix);
}

//  void QSSGRenderNode::calculateMVPAndNormalMatrix(const QMatrix4x4
//      &globalTransfor, const QMatrix4x4 &inViewProjection, QMatrix4x4
//      &outMVP, QMatrix3x3 &outNormalMatrix)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSSGRenderNode27calculateMVPAndNormalMatrixERK10QMatrix4x4S2_RS0_R14QGenericMatrixILi3ELi3EfE(
    const QMatrix4x4 *globalTransfor,
    const QMatrix4x4 *inViewProjection,
    QMatrix4x4 *outMVP,
    QMatrix3x3 *outNormalMatrix) {
  QSSGRenderNode::calculateMVPAndNormalMatrix(
      *globalTransfor,
      *inViewProjection,
      *outMVP,
      *outNormalMatrix);
}

//  float QSSGRenderNode::signedSquared(float val)
extern "C" Q_DECL_EXPORT
float ritual_ZN14QSSGRenderNode13signedSquaredEf(float val) {
  return QSSGRenderNode::signedSquared(val);
}
