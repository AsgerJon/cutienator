//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendermotionvectormap_
//  p.h, Qt 6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendermotionvectormap_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qmatrix4x4.h>
#include <QtCore/qsize.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderimagetexture_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QSSGRenderMotionVectorMap::QSSGRenderMotionVectorMap(const
//      QSSGRenderContextInterface &inContext)
extern "C" Q_DECL_EXPORT
QSSGRenderMotionVectorMap *ritual_ZN25QSSGRenderMotionVectorMapC1ERK26QSSGRenderContextInterface(
    const QSSGRenderContextInterface *inContext) {
  return new QSSGRenderMotionVectorMap(*inContext);
}

//  QSSGRenderMotionVectorMap::~QSSGRenderMotionVectorMap()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QSSGRenderMotionVectorMapD1Ev(
    QSSGRenderMotionVectorMap *self) {
  delete self;
}

//  void QSSGRenderMotionVectorMap::endFrame()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QSSGRenderMotionVectorMap8endFrameEv(
    QSSGRenderMotionVectorMap *self) {
  self->endFrame();
}

//  MotionResultData QSSGRenderMotionVectorMap::trackMotionData(const void
//      *modelKey, const QMatrix4x4 &currentModelViewProjection, const
//      QMatrix4x4 &currentInstanceLocal, const QMatrix4x4
//      &currentInstanceGlobal, QSSGRenderTextureData
//      *currentBoneTextureData, QSSGRenderInstanceTable
//      *currentInstanceTable, const QVector<float> &currentMorphWeights)
extern "C" Q_DECL_EXPORT
QSSGRenderMotionVectorMap::MotionResultData *ritual_ZN25QSSGRenderMotionVectorMap15trackMotionDataEPKvRK10QMatrix4x4S4_S4_P21QSSGRenderTextureDataP23QSSGRenderInstanceTableRK5QListIfE(
    QSSGRenderMotionVectorMap *self,
    const void *modelKey,
    const QMatrix4x4 *currentModelViewProjection,
    const QMatrix4x4 *currentInstanceLocal,
    const QMatrix4x4 *currentInstanceGlobal,
    QSSGRenderTextureData *currentBoneTextureData,
    QSSGRenderInstanceTable *currentInstanceTable,
    const QVector<float> *currentMorphWeights) {
  return new QSSGRenderMotionVectorMap::MotionResultData(
      self->trackMotionData(
          modelKey,
          *currentModelViewProjection,
          *currentInstanceLocal,
          *currentInstanceGlobal,
          currentBoneTextureData,
          currentInstanceTable,
          *currentMorphWeights));
}

//  void QSSGRenderMotionVectorMap::releaseCachedResources()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QSSGRenderMotionVectorMap22releaseCachedResourcesEv(
    QSSGRenderMotionVectorMap *self) {
  self->releaseCachedResources();
}

//  void QSSGRenderMotionVectorMap::cleanupStaleEntries()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QSSGRenderMotionVectorMap19cleanupStaleEntriesEv(
    QSSGRenderMotionVectorMap *self) {
  self->cleanupStaleEntries();
}

//  void QSSGRenderMotionVectorMap::releaseEntryResources(MotionStoreData
//      &entry)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QSSGRenderMotionVectorMap21releaseEntryResourcesERNS_15MotionStoreDataE(
    QSSGRenderMotionVectorMap *self,
    QSSGRenderMotionVectorMap::MotionStoreData *entry) {
  self->releaseEntryResources(*entry);
}

//  QSSGRenderImageTexture
//      QSSGRenderMotionVectorMap::loadAndReleaseIfNeeded(const
//      std::shared_ptr<QSSGRenderTextureData> &textureData, QSize lastSize)
extern "C" Q_DECL_EXPORT
QSSGRenderImageTexture *ritual_ZN25QSSGRenderMotionVectorMap22loadAndReleaseIfNeededERKSt10shared_ptrI21QSSGRenderTextureDataE5QSize(
    QSSGRenderMotionVectorMap *self,
    const std::shared_ptr<QSSGRenderTextureData> *textureData,
    const QSize *lastSize) {
  return new QSSGRenderImageTexture(
      self->loadAndReleaseIfNeeded(
          *textureData,
          *lastSize));
}
