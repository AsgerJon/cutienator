//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendershadercodegenera
//  tor_p.h, Qt 6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendershadercodegenerator_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>

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
