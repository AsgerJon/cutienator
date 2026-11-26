//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrhieffectsystem_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrhieffectsystem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qsize.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendercommands_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/ssg/qssgrhicontext.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QSSGRhiEffectSystem::QSSGRhiEffectSystem(const
//      std::shared_ptr<QSSGRenderContextInterface> &sgContext)
extern "C" Q_DECL_EXPORT
QSSGRhiEffectSystem *ritual_ZN19QSSGRhiEffectSystemC1ERKSt10shared_ptrI26QSSGRenderContextInterfaceE(
    const std::shared_ptr<QSSGRenderContextInterface> *sgContext) {
  return new QSSGRhiEffectSystem(*sgContext);
}

//  QSSGRhiEffectSystem::~QSSGRhiEffectSystem()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSSGRhiEffectSystemD1Ev(QSSGRhiEffectSystem *self) {
  delete self;
}

//  void QSSGRhiEffectSystem::setup(QSize outputSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSSGRhiEffectSystem5setupE5QSize(
    QSSGRhiEffectSystem *self,
    const QSize *outputSize) {
  self->setup(*outputSize);
}

//  QRhiTexture *QSSGRhiEffectSystem::process(const QSSGRenderLayer &layer,
//      QRhiTexture *inTexture, QRhiTexture *inDepthTexture, QRhiTexture
//      *inNormalTexture, QRhiTexture *inMotionVectorTexture)
extern "C" Q_DECL_EXPORT
QRhiTexture *ritual_ZN19QSSGRhiEffectSystem7processERK15QSSGRenderLayerP11QRhiTextureS4_S4_S4_(
    QSSGRhiEffectSystem *self,
    const QSSGRenderLayer *layer,
    QRhiTexture *inTexture,
    QRhiTexture *inDepthTexture,
    QRhiTexture *inNormalTexture,
    QRhiTexture *inMotionVectorTexture) {
  return self->process(
      *layer,
      inTexture,
      inDepthTexture,
      inNormalTexture,
      inMotionVectorTexture);
}

//  QSSGRenderTextureFormat::Format
//      QSSGRhiEffectSystem::overriddenOutputFormat(const QSSGRenderEffect
//      *inEffect)
extern "C" Q_DECL_EXPORT
QSSGRenderTextureFormat::Format ritual_ZN19QSSGRhiEffectSystem22overriddenOutputFormatEPK16QSSGRenderEffect(
    const QSSGRenderEffect *inEffect) {
  return QSSGRhiEffectSystem::overriddenOutputFormat(inEffect);
}

//  QSSGRhiShaderPipelinePtr QSSGRhiEffectSystem::buildShaderForEffect(const
//      QSSGBindShader &inCmd, QSSGProgramGenerator &generator,
//      QSSGShaderLibraryManager &shaderLib, QSSGShaderCache &shaderCache,
//      bool isYUpInFramebuffer, int viewCount)
extern "C" Q_DECL_EXPORT
QSSGRhiShaderPipelinePtr *ritual_ZN19QSSGRhiEffectSystem20buildShaderForEffectERK14QSSGBindShaderR20QSSGProgramGeneratorR24QSSGShaderLibraryManagerR15QSSGShaderCachebi(
    const QSSGBindShader *inCmd,
    QSSGProgramGenerator *generator,
    QSSGShaderLibraryManager *shaderLib,
    QSSGShaderCache *shaderCache,
    bool isYUpInFramebuffer,
    int viewCount) {
  return new QSSGRhiShaderPipelinePtr(
      QSSGRhiEffectSystem::buildShaderForEffect(
          *inCmd,
          *generator,
          *shaderLib,
          *shaderCache,
          isYUpInFramebuffer,
          viewCount));
}

//  void QSSGRhiEffectSystem::releaseResources()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSSGRhiEffectSystem16releaseResourcesEv(
    QSSGRhiEffectSystem *self) {
  self->releaseResources();
}

//  QSSGRhiEffectTexture *QSSGRhiEffectSystem::doRenderEffect(const
//      QSSGRenderEffect *inEffect, QSSGRhiEffectTexture *inTexture, quint8
//      viewCount)
extern "C" Q_DECL_EXPORT
QSSGRhiEffectTexture *ritual_ZN19QSSGRhiEffectSystem14doRenderEffectEPK16QSSGRenderEffectP20QSSGRhiEffectTextureh(
    QSSGRhiEffectSystem *self,
    const QSSGRenderEffect *inEffect,
    QSSGRhiEffectTexture *inTexture,
    quint8 viewCount) {
  return self->doRenderEffect(inEffect, inTexture, viewCount);
}

//  void QSSGRhiEffectSystem::allocateBufferCmd(const QSSGAllocateBuffer
//      *inCmd, QSSGRhiEffectTexture *inTexture, const QSSGRenderEffect
//      *inEffect, quint8 viewCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSSGRhiEffectSystem17allocateBufferCmdEPK18QSSGAllocateBufferP20QSSGRhiEffectTexturePK16QSSGRenderEffecth(
    QSSGRhiEffectSystem *self,
    const QSSGAllocateBuffer *inCmd,
    QSSGRhiEffectTexture *inTexture,
    const QSSGRenderEffect *inEffect,
    quint8 viewCount) {
  self->allocateBufferCmd(inCmd, inTexture, inEffect, viewCount);
}

//  void QSSGRhiEffectSystem::applyInstanceValueCmd(const
//      QSSGApplyInstanceValue *inCmd, const QSSGRenderEffect *inEffect)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSSGRhiEffectSystem21applyInstanceValueCmdEPK22QSSGApplyInstanceValuePK16QSSGRenderEffect(
    QSSGRhiEffectSystem *self,
    const QSSGApplyInstanceValue *inCmd,
    const QSSGRenderEffect *inEffect) {
  self->applyInstanceValueCmd(inCmd, inEffect);
}

//  void QSSGRhiEffectSystem::applyValueCmd(const QSSGApplyValue *inCmd,
//      const QSSGRenderEffect *inEffect)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSSGRhiEffectSystem13applyValueCmdEPK14QSSGApplyValuePK16QSSGRenderEffect(
    QSSGRhiEffectSystem *self,
    const QSSGApplyValue *inCmd,
    const QSSGRenderEffect *inEffect) {
  self->applyValueCmd(inCmd, inEffect);
}

//  void QSSGRhiEffectSystem::bindShaderCmd(const QSSGBindShader *inCmd,
//      const QSSGRenderEffect *inEffect, quint8 viewCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSSGRhiEffectSystem13bindShaderCmdEPK14QSSGBindShaderPK16QSSGRenderEffecth(
    QSSGRhiEffectSystem *self,
    const QSSGBindShader *inCmd,
    const QSSGRenderEffect *inEffect,
    quint8 viewCount) {
  self->bindShaderCmd(inCmd, inEffect, viewCount);
}

//  void QSSGRhiEffectSystem::renderCmd(const QSSGRenderEffect *inEffect,
//      QSSGRhiEffectTexture *inTexture, QSSGRhiEffectTexture *target, quint8
//      viewCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSSGRhiEffectSystem9renderCmdEPK16QSSGRenderEffectP20QSSGRhiEffectTextureS4_h(
    QSSGRhiEffectSystem *self,
    const QSSGRenderEffect *inEffect,
    QSSGRhiEffectTexture *inTexture,
    QSSGRhiEffectTexture *target,
    quint8 viewCount) {
  self->renderCmd(inEffect, inTexture, target, viewCount);
}

//  void QSSGRhiEffectSystem::addCommonEffectUniforms(const QSSGRenderEffect
//      *inEffect, const QSize &inputSize, const QSize &outputSize, quint8
//      viewCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSSGRhiEffectSystem23addCommonEffectUniformsEPK16QSSGRenderEffectRK5QSizeS5_h(
    QSSGRhiEffectSystem *self,
    const QSSGRenderEffect *inEffect,
    const QSize *inputSize,
    const QSize *outputSize,
    quint8 viewCount) {
  self->addCommonEffectUniforms(
      inEffect,
      *inputSize,
      *outputSize,
      viewCount);
}

//  void QSSGRhiEffectSystem::addTextureToShaderPipeline(const QByteArray
//      &name, QRhiTexture *texture, const QSSGRhiSamplerDescription
//      &samplerDesc)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSSGRhiEffectSystem26addTextureToShaderPipelineERK10QByteArrayP11QRhiTextureRK25QSSGRhiSamplerDescription(
    QSSGRhiEffectSystem *self,
    const QByteArray *name,
    QRhiTexture *texture,
    const QSSGRhiSamplerDescription *samplerDesc) {
  self->addTextureToShaderPipeline(*name, texture, *samplerDesc);
}

//  QSSGRhiEffectTexture *QSSGRhiEffectSystem::findTexture(const QByteArray
//      &bufferName)
extern "C" Q_DECL_EXPORT
QSSGRhiEffectTexture *ritual_ZN19QSSGRhiEffectSystem11findTextureERK10QByteArray(
    QSSGRhiEffectSystem *self,
    const QByteArray *bufferName) {
  return self->findTexture(*bufferName);
}

//  QSSGRhiEffectTexture *QSSGRhiEffectSystem::getTexture(const QByteArray
//      &bufferName, const QSize &size, QRhiTexture::Format format, bool
//      isFinalOutput, const QSSGRenderEffect *inEffect, quint8 viewCount)
extern "C" Q_DECL_EXPORT
QSSGRhiEffectTexture *ritual_ZN19QSSGRhiEffectSystem10getTextureERK10QByteArrayRK5QSizeN11QRhiTexture6FormatEbPK16QSSGRenderEffecth(
    QSSGRhiEffectSystem *self,
    const QByteArray *bufferName,
    const QSize *size,
    QRhiTexture::Format format,
    bool isFinalOutput,
    const QSSGRenderEffect *inEffect,
    quint8 viewCount) {
  return self->getTexture(
      *bufferName,
      *size,
      format,
      isFinalOutput,
      inEffect,
      viewCount);
}

//  void QSSGRhiEffectSystem::releaseTexture(QSSGRhiEffectTexture *texture)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSSGRhiEffectSystem14releaseTextureEP20QSSGRhiEffectTexture(
    QSSGRhiEffectSystem *self,
    QSSGRhiEffectTexture *texture) {
  self->releaseTexture(texture);
}

//  void QSSGRhiEffectSystem::releaseTextures()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSSGRhiEffectSystem15releaseTexturesEv(
    QSSGRhiEffectSystem *self) {
  self->releaseTextures();
}

//  a QSSGRhiShaderPipelinePtr a ritual of QSSGRhiEffectSystem gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QSSGRhiEffectSystem__QSSGRhiShaderPipelinePtr(
    QSSGRhiShaderPipelinePtr *self) {
  delete self;
}
