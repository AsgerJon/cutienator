//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrhieffectsystem_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrhieffectsystem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qsize.h>
#include <QtCore/qbytearray.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/ssg/qssgrhicontext.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

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

//  QSSGRenderTextureFormat::Format
//      QSSGRhiEffectSystem::overriddenOutputFormat(const QSSGRenderEffect
//      *inEffect)
extern "C" Q_DECL_EXPORT
QSSGRenderTextureFormat::Format ritual_ZN19QSSGRhiEffectSystem22overriddenOutputFormatEPK16QSSGRenderEffect(
    const QSSGRenderEffect *inEffect) {
  return QSSGRhiEffectSystem::overriddenOutputFormat(inEffect);
}

//  void QSSGRhiEffectSystem::releaseResources()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSSGRhiEffectSystem16releaseResourcesEv(
    QSSGRhiEffectSystem *self) {
  self->releaseResources();
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

//  void QSSGRhiEffectSystem::releaseTextures()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSSGRhiEffectSystem15releaseTexturesEv(
    QSSGRhiEffectSystem *self) {
  self->releaseTextures();
}
