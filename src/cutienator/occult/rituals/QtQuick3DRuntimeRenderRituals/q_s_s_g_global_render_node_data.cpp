//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderdata_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderdata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

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
