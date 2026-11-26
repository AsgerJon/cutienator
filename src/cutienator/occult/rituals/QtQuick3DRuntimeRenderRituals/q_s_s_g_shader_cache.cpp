//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendershadercache_p.h,
//  Qt 6.12.0. Edited by hand on 2026-11-25: added by hand, rituals for
//  functions the generator leaves out: 1. Kept as it is when the generator
//  runs again.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendershadercache_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtQuick3DUtils/QtQuick3DUtils>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qqsbcollection_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/QByteArray>
#include <QtCore/QFlags>

//  QSSGRhiShaderPipelinePtr QSSGShaderCache::loadBuiltinUncached(const
//      QByteArray &inKey, int viewCount, QSSGRhiShaderPipeline::StageFlags
//      vertexStageFlags)
extern "C" Q_DECL_EXPORT
QSSGRhiShaderPipelinePtr *ritual_ZN15QSSGShaderCache19loadBuiltinUncachedERK10QByteArrayi6QFlagsIN21QSSGRhiShaderPipeline9StageFlagEE(
    QSSGShaderCache *self,
    const QByteArray *inKey,
    int viewCount,
    int vertexStageFlags) {
  return new QSSGRhiShaderPipelinePtr(
      self->loadBuiltinUncached(
          *inKey,
          viewCount,
          QFlags<QSSGRhiShaderPipeline::StageFlag>::fromInt(vertexStageFlags)));
}

//  void QSSGShaderCache::addShaderPreprocessor(QByteArray &str, const
//      QByteArray &inKey, ShaderType shaderType, const QSSGShaderFeatures
//      &inFeatures, const QSSGUserShaderAugmentation &shaderAugmentation,
//      int viewCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSSGShaderCache21addShaderPreprocessorER10QByteArrayRKS0_NS_10ShaderTypeERK18QSSGShaderFeaturesRK26QSSGUserShaderAugmentationi(
    QSSGShaderCache *self,
    QByteArray *str,
    const QByteArray *inKey,
    QSSGShaderCache::ShaderType shaderType,
    const QSSGShaderFeatures *inFeatures,
    const QSSGUserShaderAugmentation *shaderAugmentation,
    int viewCount) {
  self->addShaderPreprocessor(
      *str,
      *inKey,
      shaderType,
      *inFeatures,
      *shaderAugmentation,
      viewCount);
}

//  QSSGShaderCache::~QSSGShaderCache()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSSGShaderCacheD1Ev(QSSGShaderCache *self) {
  delete self;
}

//  QSSGRhiContext &QSSGShaderCache::rhiContext()
extern "C" Q_DECL_EXPORT
QSSGRhiContext *ritual_ZN15QSSGShaderCache10rhiContextEv(
    QSSGShaderCache *self) {
  return &(self->rhiContext());
}

//  void QSSGShaderCache::releaseCachedResources()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSSGShaderCache22releaseCachedResourcesEv(
    QSSGShaderCache *self) {
  self->releaseCachedResources();
}

//  QQsbInMemoryCollection &QSSGShaderCache::persistentShaderBakingCache()
extern "C" Q_DECL_EXPORT
QQsbInMemoryCollection *ritual_ZN15QSSGShaderCache27persistentShaderBakingCacheEv(
    QSSGShaderCache *self) {
  return &(self->persistentShaderBakingCache());
}

//  QSSGRhiShaderPipelinePtr QSSGShaderCache::tryGetRhiShaderPipeline(const
//      QByteArray &inKey, const QSSGShaderFeatures &inFeatures)
extern "C" Q_DECL_EXPORT
QSSGRhiShaderPipelinePtr *ritual_ZN15QSSGShaderCache23tryGetRhiShaderPipelineERK10QByteArrayRK18QSSGShaderFeatures(
    QSSGShaderCache *self,
    const QByteArray *inKey,
    const QSSGShaderFeatures *inFeatures) {
  return new QSSGRhiShaderPipelinePtr(
      self->tryGetRhiShaderPipeline(
          *inKey,
          *inFeatures));
}

//  QSSGRhiShaderPipelinePtr
//      QSSGShaderCache::tryNewPipelineFromPersistentCache(const QByteArray
//      &qsbcKey, const QByteArray &inKey, const QSSGShaderFeatures
//      &inFeatures, QSSGRhiShaderPipeline::StageFlags stageFlags)
extern "C" Q_DECL_EXPORT
QSSGRhiShaderPipelinePtr *ritual_ZN15QSSGShaderCache33tryNewPipelineFromPersistentCacheERK10QByteArrayS2_RK18QSSGShaderFeatures6QFlagsIN21QSSGRhiShaderPipeline9StageFlagEE(
    QSSGShaderCache *self,
    const QByteArray *qsbcKey,
    const QByteArray *inKey,
    const QSSGShaderFeatures *inFeatures,
    int stageFlags) {
  return new QSSGRhiShaderPipelinePtr(
      self->tryNewPipelineFromPersistentCache(
          *qsbcKey,
          *inKey,
          *inFeatures,
          QFlags<QSSGRhiShaderPipeline::StageFlag>::fromInt(stageFlags)));
}

//  QSSGRhiShaderPipelinePtr
//      QSSGShaderCache::newPipelineFromPregenerated(const QByteArray &inKey,
//      const QSSGShaderFeatures &inFeatures, QQsbCollection::Entry entry,
//      const QSSGRenderGraphObject &obj, QSSGRhiShaderPipeline::StageFlags
//      stageFlags)
extern "C" Q_DECL_EXPORT
QSSGRhiShaderPipelinePtr *ritual_ZN15QSSGShaderCache27newPipelineFromPregeneratedERK10QByteArrayRK18QSSGShaderFeaturesN14QQsbCollection5EntryERK21QSSGRenderGraphObject6QFlagsIN21QSSGRhiShaderPipeline9StageFlagEE(
    QSSGShaderCache *self,
    const QByteArray *inKey,
    const QSSGShaderFeatures *inFeatures,
    const QQsbCollection::Entry *entry,
    const QSSGRenderGraphObject *obj,
    int stageFlags) {
  return new QSSGRhiShaderPipelinePtr(
      self->newPipelineFromPregenerated(
          *inKey,
          *inFeatures,
          *entry,
          *obj,
          QFlags<QSSGRhiShaderPipeline::StageFlag>::fromInt(stageFlags)));
}

//  QSSGRhiShaderPipelinePtr QSSGShaderCache::compileForRhi(const QByteArray
//      &inKey, const QByteArray &inVert, const QByteArray &inFrag, const
//      QSSGShaderFeatures &inFeatures, QSSGRhiShaderPipeline::StageFlags
//      stageFlags, const QSSGUserShaderAugmentation &shaderAugmentation, int
//      viewCount, bool perTargetCompilation)
extern "C" Q_DECL_EXPORT
QSSGRhiShaderPipelinePtr *ritual_ZN15QSSGShaderCache13compileForRhiERK10QByteArrayS2_S2_RK18QSSGShaderFeatures6QFlagsIN21QSSGRhiShaderPipeline9StageFlagEERK26QSSGUserShaderAugmentationib(
    QSSGShaderCache *self,
    const QByteArray *inKey,
    const QByteArray *inVert,
    const QByteArray *inFrag,
    const QSSGShaderFeatures *inFeatures,
    int stageFlags,
    const QSSGUserShaderAugmentation *shaderAugmentation,
    int viewCount,
    bool perTargetCompilation) {
  return new QSSGRhiShaderPipelinePtr(
      self->compileForRhi(
          *inKey,
          *inVert,
          *inFrag,
          *inFeatures,
          QFlags<QSSGRhiShaderPipeline::StageFlag>::fromInt(stageFlags),
          *shaderAugmentation,
          viewCount,
          perTargetCompilation));
}

//  QSSGBuiltInRhiShaderCache &QSSGShaderCache::getBuiltInRhiShaders()
extern "C" Q_DECL_EXPORT
QSSGBuiltInRhiShaderCache *ritual_ZN15QSSGShaderCache20getBuiltInRhiShadersEv(
    QSSGShaderCache *self) {
  return &(self->getBuiltInRhiShaders());
}

//  QByteArray QSSGShaderCache::resourceFolder()
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN15QSSGShaderCache14resourceFolderEv() {
  return new QByteArray(QSSGShaderCache::resourceFolder());
}

//  QByteArray QSSGShaderCache::shaderCollectionFile()
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN15QSSGShaderCache20shaderCollectionFileEv() {
  return new QByteArray(QSSGShaderCache::shaderCollectionFile());
}

//  QByteArray QSSGShaderCache::particleShaderCollectionFile()
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN15QSSGShaderCache28particleShaderCollectionFileEv() {
  return new QByteArray(QSSGShaderCache::particleShaderCollectionFile());
}

//  void QSSGShaderCache::initBakerForPersistentUse(QShaderBaker *baker, QRhi
//      *rhi)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSSGShaderCache25initBakerForPersistentUseEP12QShaderBakerP4QRhi(
    QShaderBaker *baker,
    QRhi *rhi) {
  QSSGShaderCache::initBakerForPersistentUse(baker, rhi);
}

//  a QSSGRhiShaderPipelinePtr a ritual of QSSGShaderCache gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QSSGShaderCache__QSSGRhiShaderPipelinePtr(
    QSSGRhiShaderPipelinePtr *self) {
  delete self;
}

//  QSSGShaderCache::QSSGShaderCache(QSSGRhiContext &ctx, const InitBakerFunc
//      initBakeFn)
extern "C" Q_DECL_EXPORT
QSSGShaderCache *ritual_ZN15QSSGShaderCacheC1ER14QSSGRhiContextPFvP12QShaderBakerP4QRhiE(
    QSSGRhiContext *ctx,
    void *initBakeFn) {
  return new QSSGShaderCache(
      *ctx, reinterpret_cast<QSSGShaderCache::InitBakerFunc>(initBakeFn));
}
