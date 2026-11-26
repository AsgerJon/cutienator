//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderdata_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderdata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qmatrix4x4.h>
#include <QtGui/QMatrix4x4>

//  QSSGGlobalRenderNodeData::QSSGGlobalRenderNodeData(QSSGRenderRoot *root)
extern "C" Q_DECL_EXPORT
QSSGGlobalRenderNodeData *ritual_ZN24QSSGGlobalRenderNodeDataC1EP14QSSGRenderRoot(
    QSSGRenderRoot *root) {
  return new QSSGGlobalRenderNodeData(root);
}

//  QSSGGlobalRenderNodeData::~QSSGGlobalRenderNodeData()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QSSGGlobalRenderNodeDataD1Ev(
    QSSGGlobalRenderNodeData *self) {
  delete self;
}

//  void QSSGGlobalRenderNodeData::reindex()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QSSGGlobalRenderNodeData7reindexEv(
    QSSGGlobalRenderNodeData *self) {
  self->reindex();
}

//  void QSSGGlobalRenderNodeData::invalidate()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QSSGGlobalRenderNodeData10invalidateEv(
    QSSGGlobalRenderNodeData *self) {
  self->invalidate();
}

//  VersionType QSSGGlobalRenderNodeData::version() const
extern "C" Q_DECL_EXPORT
QSSGGlobalRenderNodeData::VersionType ritual_ZNK24QSSGGlobalRenderNodeData7versionEv(
    const QSSGGlobalRenderNodeData *self) {
  return self->version();
}

//  VersionType QSSGGlobalRenderNodeData::stateGeneration() const
extern "C" Q_DECL_EXPORT
QSSGGlobalRenderNodeData::VersionType ritual_ZNK24QSSGGlobalRenderNodeData15stateGenerationEv(
    const QSSGGlobalRenderNodeData *self) {
  return self->stateGeneration();
}

//  void QSSGGlobalRenderNodeData::bumpStateGeneration()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QSSGGlobalRenderNodeData19bumpStateGenerationEv(
    QSSGGlobalRenderNodeData *self) {
  self->bumpStateGeneration();
}

//  size_t QSSGGlobalRenderNodeData::nodeCount() const
extern "C" Q_DECL_EXPORT
size_t ritual_ZNK24QSSGGlobalRenderNodeData9nodeCountEv(
    const QSSGGlobalRenderNodeData *self) {
  return self->nodeCount();
}

//  size_t QSSGGlobalRenderNodeData::storageSize() const
extern "C" Q_DECL_EXPORT
size_t ritual_ZNK24QSSGGlobalRenderNodeData11storageSizeEv(
    const QSSGGlobalRenderNodeData *self) {
  return self->storageSize();
}

//  QMatrix4x4
//      QSSGGlobalRenderNodeData::getGlobalTransform(QSSGRenderNodeHandle h,
//      const QMatrix4x4 &defaultValue) const
extern "C" Q_DECL_EXPORT
QMatrix4x4 *ritual_ZNK24QSSGGlobalRenderNodeData18getGlobalTransformE23QSSGRenderStorageHandleIL10HandleType1EERK10QMatrix4x4(
    const QSSGGlobalRenderNodeData *self,
    const QSSGRenderNodeHandle *h,
    const QMatrix4x4 *defaultValue) {
  return new QMatrix4x4(self->getGlobalTransform(*h, *defaultValue));
}

//  QMatrix4x4
//      QSSGGlobalRenderNodeData::getGlobalTransform(QSSGRenderNodeHandle h)
//      const
extern "C" Q_DECL_EXPORT
QMatrix4x4 *ritual_ZNK24QSSGGlobalRenderNodeData18getGlobalTransformE23QSSGRenderStorageHandleIL10HandleType1EE(
    const QSSGGlobalRenderNodeData *self,
    const QSSGRenderNodeHandle *h) {
  return new QMatrix4x4(self->getGlobalTransform(*h));
}

//  QMatrix4x4 QSSGGlobalRenderNodeData::getGlobalTransform(const
//      QSSGRenderNode &node) const
extern "C" Q_DECL_EXPORT
QMatrix4x4 *ritual_ZNK24QSSGGlobalRenderNodeData18getGlobalTransformERK14QSSGRenderNode(
    const QSSGGlobalRenderNodeData *self,
    const QSSGRenderNode *node) {
  return new QMatrix4x4(self->getGlobalTransform(*node));
}

//  float QSSGGlobalRenderNodeData::getGlobalOpacity(QSSGRenderNodeHandle h,
//      float defaultValue) const
extern "C" Q_DECL_EXPORT
float ritual_ZNK24QSSGGlobalRenderNodeData16getGlobalOpacityE23QSSGRenderStorageHandleIL10HandleType1EEf(
    const QSSGGlobalRenderNodeData *self,
    const QSSGRenderNodeHandle *h,
    float defaultValue) {
  return self->getGlobalOpacity(*h, defaultValue);
}

//  float QSSGGlobalRenderNodeData::getGlobalOpacity(const QSSGRenderNode
//      &node) const
extern "C" Q_DECL_EXPORT
float ritual_ZNK24QSSGGlobalRenderNodeData16getGlobalOpacityERK14QSSGRenderNode(
    const QSSGGlobalRenderNodeData *self,
    const QSSGRenderNode *node) {
  return self->getGlobalOpacity(*node);
}

//  InstanceTransforms
//      QSSGGlobalRenderNodeData::getInstanceTransforms(QSSGRenderNodeHandle
//      h) const
extern "C" Q_DECL_EXPORT
QSSGGlobalRenderNodeData::InstanceTransforms *ritual_ZNK24QSSGGlobalRenderNodeData21getInstanceTransformsE23QSSGRenderStorageHandleIL10HandleType1EE(
    const QSSGGlobalRenderNodeData *self,
    const QSSGRenderNodeHandle *h) {
  return new QSSGGlobalRenderNodeData::InstanceTransforms(
      self->getInstanceTransforms(
          *h));
}

//  InstanceTransforms QSSGGlobalRenderNodeData::getInstanceTransforms(const
//      QSSGRenderNode &node) const
extern "C" Q_DECL_EXPORT
QSSGGlobalRenderNodeData::InstanceTransforms *ritual_ZNK24QSSGGlobalRenderNodeData21getInstanceTransformsERK14QSSGRenderNode(
    const QSSGGlobalRenderNodeData *self,
    const QSSGRenderNode *node) {
  return new QSSGGlobalRenderNodeData::InstanceTransforms(
      self->getInstanceTransforms(
          *node));
}

//  LayerNodeView
//      QSSGGlobalRenderNodeData::getLayerNodeView(QSSGRenderLayerHandle h)
//      const
extern "C" Q_DECL_EXPORT
QSSGGlobalRenderNodeData::LayerNodeView *ritual_ZNK24QSSGGlobalRenderNodeData16getLayerNodeViewE23QSSGRenderStorageHandleIL10HandleType0EE(
    const QSSGGlobalRenderNodeData *self,
    const QSSGRenderLayerHandle *h) {
  return new QSSGGlobalRenderNodeData::LayerNodeView(
      self->getLayerNodeView(
          *h));
}

//  LayerNodeView QSSGGlobalRenderNodeData::getLayerNodeView(const
//      QSSGRenderLayer &layer) const
extern "C" Q_DECL_EXPORT
QSSGGlobalRenderNodeData::LayerNodeView *ritual_ZNK24QSSGGlobalRenderNodeData16getLayerNodeViewERK15QSSGRenderLayer(
    const QSSGGlobalRenderNodeData *self,
    const QSSGRenderLayer *layer) {
  return new QSSGGlobalRenderNodeData::LayerNodeView(
      self->getLayerNodeView(
          *layer));
}

#if QT_CONFIG(thread)
//  QThreadPool *QSSGGlobalRenderNodeData::threadPool() const
extern "C" Q_DECL_EXPORT
QThreadPool *ritual_ZNK24QSSGGlobalRenderNodeData10threadPoolEv(
    const QSSGGlobalRenderNodeData *self) {
  return self->threadPool();
}
#endif  // QT_CONFIG(thread)

//  void QSSGGlobalRenderNodeData::collectNodes(QSSGRenderRoot *rootNode)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QSSGGlobalRenderNodeData12collectNodesEP14QSSGRenderRoot(
    QSSGGlobalRenderNodeData *self,
    QSSGRenderRoot *rootNode) {
  self->collectNodes(rootNode);
}

//  void QSSGGlobalRenderNodeData::updateGlobalState()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QSSGGlobalRenderNodeData17updateGlobalStateEv(
    QSSGGlobalRenderNodeData *self) {
  self->updateGlobalState();
}

//  a QSSGGlobalRenderNodeData::LayerNodeView a ritual of
//      QSSGGlobalRenderNodeData gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QSSGGlobalRenderNodeData__QSSGGlobalRenderNodeData_LayerNodeView(
    QSSGGlobalRenderNodeData::LayerNodeView *self) {
  delete self;
}
