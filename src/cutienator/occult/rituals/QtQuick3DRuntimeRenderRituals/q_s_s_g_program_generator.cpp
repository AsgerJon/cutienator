//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendershadercodegenera
//  tor_p.h, Qt 6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendershadercodegenerator_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendershadercache_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/QByteArray>
#include <QtCore/QFlags>

//  QSSGProgramGenerator::QSSGProgramGenerator()
extern "C" Q_DECL_EXPORT
QSSGProgramGenerator *ritual_ZN20QSSGProgramGeneratorC1Ev() {
  return new QSSGProgramGenerator();
}

//  QSSGShaderGeneratorStageFlags QSSGProgramGenerator::defaultFlags()
extern "C" Q_DECL_EXPORT
int ritual_ZN20QSSGProgramGenerator12defaultFlagsEv() {
  return static_cast<int>(QSSGProgramGenerator::defaultFlags().toInt());
}

//  void QSSGProgramGenerator::linkStages()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QSSGProgramGenerator10linkStagesEv(
    QSSGProgramGenerator *self) {
  self->linkStages();
}

//  void QSSGProgramGenerator::beginProgram(QSSGShaderGeneratorStageFlags
//      inEnabledStages)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QSSGProgramGenerator12beginProgramE6QFlagsI24QSSGShaderGeneratorStageE(
    QSSGProgramGenerator *self,
    int inEnabledStages) {
  self->beginProgram(
      QFlags<QSSGShaderGeneratorStage>::fromInt(inEnabledStages));
}

//  QSSGShaderGeneratorStageFlags QSSGProgramGenerator::getEnabledStages()
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QSSGProgramGenerator16getEnabledStagesEv(
    const QSSGProgramGenerator *self) {
  return static_cast<int>(self->getEnabledStages().toInt());
}

//  QSSGStageGeneratorBase
//      &QSSGProgramGenerator::internalGetStage(QSSGShaderGeneratorStage
//      inStage)
extern "C" Q_DECL_EXPORT
QSSGStageGeneratorBase *ritual_ZN20QSSGProgramGenerator16internalGetStageE24QSSGShaderGeneratorStage(
    QSSGProgramGenerator *self,
    QSSGShaderGeneratorStage inStage) {
  return &(self->internalGetStage(inStage));
}

//  QSSGStageGeneratorBase
//      *QSSGProgramGenerator::getStage(QSSGShaderGeneratorStage inStage)
extern "C" Q_DECL_EXPORT
QSSGStageGeneratorBase *ritual_ZN20QSSGProgramGenerator8getStageE24QSSGShaderGeneratorStage(
    QSSGProgramGenerator *self,
    QSSGShaderGeneratorStage inStage) {
  return self->getStage(inStage);
}

//  void QSSGProgramGenerator::registerShaderMetaDataFromSource(QSSGShaderRes
//      ourceMergeContext *mergeContext, const QByteArray &contents,
//      QSSGShaderGeneratorStage stage)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QSSGProgramGenerator32registerShaderMetaDataFromSourceEP30QSSGShaderResourceMergeContextRK10QByteArray24QSSGShaderGeneratorStage(
    QSSGProgramGenerator *self,
    QSSGShaderResourceMergeContext *mergeContext,
    const QByteArray *contents,
    QSSGShaderGeneratorStage stage) {
  self->registerShaderMetaDataFromSource(mergeContext, *contents, stage);
}

//  QSSGRhiShaderPipelinePtr
//      QSSGProgramGenerator::compileGeneratedRhiShader(const QByteArray
//      &inMaterialInfoString, const QSSGShaderFeatures &inFeatureSet,
//      QSSGShaderLibraryManager &shaderLibraryManager, QSSGShaderCache
//      &theCache, QSSGRhiShaderPipeline::StageFlags stageFlags, const
//      QSSGUserShaderAugmentation &shaderAugmentation, int viewCount, bool
//      perTargetCompilation)
extern "C" Q_DECL_EXPORT
QSSGRhiShaderPipelinePtr *ritual_ZN20QSSGProgramGenerator25compileGeneratedRhiShaderERK10QByteArrayRK18QSSGShaderFeaturesR24QSSGShaderLibraryManagerR15QSSGShaderCache6QFlagsIN21QSSGRhiShaderPipeline9StageFlagEERK26QSSGUserShaderAugmentationib(
    QSSGProgramGenerator *self,
    const QByteArray *inMaterialInfoString,
    const QSSGShaderFeatures *inFeatureSet,
    QSSGShaderLibraryManager *shaderLibraryManager,
    QSSGShaderCache *theCache,
    int stageFlags,
    const QSSGUserShaderAugmentation *shaderAugmentation,
    int viewCount,
    bool perTargetCompilation) {
  return new QSSGRhiShaderPipelinePtr(
      self->compileGeneratedRhiShader(
          *inMaterialInfoString,
          *inFeatureSet,
          *shaderLibraryManager,
          *theCache,
          QFlags<QSSGRhiShaderPipeline::StageFlag>::fromInt(stageFlags),
          *shaderAugmentation,
          viewCount,
          perTargetCompilation));
}

//  a QSSGRhiShaderPipelinePtr a ritual of QSSGProgramGenerator gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QSSGProgramGenerator__QSSGRhiShaderPipelinePtr(
    QSSGRhiShaderPipelinePtr *self) {
  delete self;
}
