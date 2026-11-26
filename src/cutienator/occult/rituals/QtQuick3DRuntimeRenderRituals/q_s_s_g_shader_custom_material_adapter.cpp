//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgshadermaterialadapter_
//  p.h, Qt 6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgshadermaterialadapter_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qvectornd.h>
#include <QtCore/qbytearray.h>

//  QSSGShaderCustomMaterialAdapter::QSSGShaderCustomMaterialAdapter(const
//      QSSGRenderCustomMaterial &material)
extern "C" Q_DECL_EXPORT
QSSGShaderCustomMaterialAdapter *ritual_ZN31QSSGShaderCustomMaterialAdapterC1ERK24QSSGRenderCustomMaterial(
    const QSSGRenderCustomMaterial *material) {
  return new QSSGShaderCustomMaterialAdapter(*material);
}

//  bool QSSGShaderCustomMaterialAdapter::isPrincipled()
extern "C" Q_DECL_EXPORT
bool ritual_ZN31QSSGShaderCustomMaterialAdapter12isPrincipledEv(
    QSSGShaderCustomMaterialAdapter *self) {
  return self->isPrincipled();
}

//  bool QSSGShaderCustomMaterialAdapter::isSpecularGlossy()
extern "C" Q_DECL_EXPORT
bool ritual_ZN31QSSGShaderCustomMaterialAdapter16isSpecularGlossyEv(
    QSSGShaderCustomMaterialAdapter *self) {
  return self->isSpecularGlossy();
}

//  bool QSSGShaderCustomMaterialAdapter::isMetalnessEnabled()
extern "C" Q_DECL_EXPORT
bool ritual_ZN31QSSGShaderCustomMaterialAdapter18isMetalnessEnabledEv(
    QSSGShaderCustomMaterialAdapter *self) {
  return self->isMetalnessEnabled();
}

//  bool QSSGShaderCustomMaterialAdapter::isSpecularEnabled()
extern "C" Q_DECL_EXPORT
bool ritual_ZN31QSSGShaderCustomMaterialAdapter17isSpecularEnabledEv(
    QSSGShaderCustomMaterialAdapter *self) {
  return self->isSpecularEnabled();
}

//  bool QSSGShaderCustomMaterialAdapter::isVertexColorsEnabled()
extern "C" Q_DECL_EXPORT
bool ritual_ZN31QSSGShaderCustomMaterialAdapter21isVertexColorsEnabledEv(
    QSSGShaderCustomMaterialAdapter *self) {
  return self->isVertexColorsEnabled();
}

//  bool QSSGShaderCustomMaterialAdapter::isVertexColorsMaskEnabled()
extern "C" Q_DECL_EXPORT
bool ritual_ZN31QSSGShaderCustomMaterialAdapter25isVertexColorsMaskEnabledEv(
    QSSGShaderCustomMaterialAdapter *self) {
  return self->isVertexColorsMaskEnabled();
}

//  bool QSSGShaderCustomMaterialAdapter::isInvertOpacityMapValue()
extern "C" Q_DECL_EXPORT
bool ritual_ZN31QSSGShaderCustomMaterialAdapter23isInvertOpacityMapValueEv(
    QSSGShaderCustomMaterialAdapter *self) {
  return self->isInvertOpacityMapValue();
}

//  bool QSSGShaderCustomMaterialAdapter::isBaseColorSingleChannelEnabled()
extern "C" Q_DECL_EXPORT
bool ritual_ZN31QSSGShaderCustomMaterialAdapter31isBaseColorSingleChannelEnabledEv(
    QSSGShaderCustomMaterialAdapter *self) {
  return self->isBaseColorSingleChannelEnabled();
}

//  bool
//      QSSGShaderCustomMaterialAdapter::isSpecularAmountSingleChannelEnabled
//      ()
extern "C" Q_DECL_EXPORT
bool ritual_ZN31QSSGShaderCustomMaterialAdapter36isSpecularAmountSingleChannelEnabledEv(
    QSSGShaderCustomMaterialAdapter *self) {
  return self->isSpecularAmountSingleChannelEnabled();
}

//  bool QSSGShaderCustomMaterialAdapter::isEmissiveSingleChannelEnabled()
extern "C" Q_DECL_EXPORT
bool ritual_ZN31QSSGShaderCustomMaterialAdapter30isEmissiveSingleChannelEnabledEv(
    QSSGShaderCustomMaterialAdapter *self) {
  return self->isEmissiveSingleChannelEnabled();
}

//  bool QSSGShaderCustomMaterialAdapter::isClearcoatEnabled()
extern "C" Q_DECL_EXPORT
bool ritual_ZN31QSSGShaderCustomMaterialAdapter18isClearcoatEnabledEv(
    QSSGShaderCustomMaterialAdapter *self) {
  return self->isClearcoatEnabled();
}

//  bool QSSGShaderCustomMaterialAdapter::isTransmissionEnabled()
extern "C" Q_DECL_EXPORT
bool ritual_ZN31QSSGShaderCustomMaterialAdapter21isTransmissionEnabledEv(
    QSSGShaderCustomMaterialAdapter *self) {
  return self->isTransmissionEnabled();
}

//  bool QSSGShaderCustomMaterialAdapter::isFresnelScaleBiasEnabled()
extern "C" Q_DECL_EXPORT
bool ritual_ZN31QSSGShaderCustomMaterialAdapter25isFresnelScaleBiasEnabledEv(
    QSSGShaderCustomMaterialAdapter *self) {
  return self->isFresnelScaleBiasEnabled();
}

//  bool
//      QSSGShaderCustomMaterialAdapter::isClearcoatFresnelScaleBiasEnabled()
extern "C" Q_DECL_EXPORT
bool ritual_ZN31QSSGShaderCustomMaterialAdapter34isClearcoatFresnelScaleBiasEnabledEv(
    QSSGShaderCustomMaterialAdapter *self) {
  return self->isClearcoatFresnelScaleBiasEnabled();
}

//  bool QSSGShaderCustomMaterialAdapter::hasLighting()
extern "C" Q_DECL_EXPORT
bool ritual_ZN31QSSGShaderCustomMaterialAdapter11hasLightingEv(
    QSSGShaderCustomMaterialAdapter *self) {
  return self->hasLighting();
}

//  bool QSSGShaderCustomMaterialAdapter::usesCustomSkinning()
extern "C" Q_DECL_EXPORT
bool ritual_ZN31QSSGShaderCustomMaterialAdapter18usesCustomSkinningEv(
    QSSGShaderCustomMaterialAdapter *self) {
  return self->usesCustomSkinning();
}

//  bool QSSGShaderCustomMaterialAdapter::usesCustomMorphing()
extern "C" Q_DECL_EXPORT
bool ritual_ZN31QSSGShaderCustomMaterialAdapter18usesCustomMorphingEv(
    QSSGShaderCustomMaterialAdapter *self) {
  return self->usesCustomMorphing();
}

//  QSSGRenderDefaultMaterial::MaterialSpecularModel
//      QSSGShaderCustomMaterialAdapter::specularModel()
extern "C" Q_DECL_EXPORT
QSSGRenderDefaultMaterial::MaterialSpecularModel ritual_ZN31QSSGShaderCustomMaterialAdapter13specularModelEv(
    QSSGShaderCustomMaterialAdapter *self) {
  return self->specularModel();
}

//  QSSGRenderDefaultMaterial::MaterialAlphaMode
//      QSSGShaderCustomMaterialAdapter::alphaMode()
extern "C" Q_DECL_EXPORT
QSSGRenderDefaultMaterial::MaterialAlphaMode ritual_ZN31QSSGShaderCustomMaterialAdapter9alphaModeEv(
    QSSGShaderCustomMaterialAdapter *self) {
  return self->alphaMode();
}

//  QSSGRenderDefaultMaterial::VertexColorMaskFlags
//      QSSGShaderCustomMaterialAdapter::vertexColorRedMask()
extern "C" Q_DECL_EXPORT
int ritual_ZN31QSSGShaderCustomMaterialAdapter18vertexColorRedMaskEv(
    QSSGShaderCustomMaterialAdapter *self) {
  return static_cast<int>(self->vertexColorRedMask().toInt());
}

//  QSSGRenderDefaultMaterial::VertexColorMaskFlags
//      QSSGShaderCustomMaterialAdapter::vertexColorGreenMask()
extern "C" Q_DECL_EXPORT
int ritual_ZN31QSSGShaderCustomMaterialAdapter20vertexColorGreenMaskEv(
    QSSGShaderCustomMaterialAdapter *self) {
  return static_cast<int>(self->vertexColorGreenMask().toInt());
}

//  QSSGRenderDefaultMaterial::VertexColorMaskFlags
//      QSSGShaderCustomMaterialAdapter::vertexColorBlueMask()
extern "C" Q_DECL_EXPORT
int ritual_ZN31QSSGShaderCustomMaterialAdapter19vertexColorBlueMaskEv(
    QSSGShaderCustomMaterialAdapter *self) {
  return static_cast<int>(self->vertexColorBlueMask().toInt());
}

//  QSSGRenderDefaultMaterial::VertexColorMaskFlags
//      QSSGShaderCustomMaterialAdapter::vertexColorAlphaMask()
extern "C" Q_DECL_EXPORT
int ritual_ZN31QSSGShaderCustomMaterialAdapter20vertexColorAlphaMaskEv(
    QSSGShaderCustomMaterialAdapter *self) {
  return static_cast<int>(self->vertexColorAlphaMask().toInt());
}

//  QSSGRenderImage *QSSGShaderCustomMaterialAdapter::iblProbe()
extern "C" Q_DECL_EXPORT
QSSGRenderImage *ritual_ZN31QSSGShaderCustomMaterialAdapter8iblProbeEv(
    QSSGShaderCustomMaterialAdapter *self) {
  return self->iblProbe();
}

//  QVector3D QSSGShaderCustomMaterialAdapter::emissiveColor()
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZN31QSSGShaderCustomMaterialAdapter13emissiveColorEv(
    QSSGShaderCustomMaterialAdapter *self) {
  return new QVector3D(self->emissiveColor());
}

//  QVector4D QSSGShaderCustomMaterialAdapter::color()
extern "C" Q_DECL_EXPORT
QVector4D *ritual_ZN31QSSGShaderCustomMaterialAdapter5colorEv(
    QSSGShaderCustomMaterialAdapter *self) {
  return new QVector4D(self->color());
}

//  QVector3D QSSGShaderCustomMaterialAdapter::specularTint()
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZN31QSSGShaderCustomMaterialAdapter12specularTintEv(
    QSSGShaderCustomMaterialAdapter *self) {
  return new QVector3D(self->specularTint());
}

//  float QSSGShaderCustomMaterialAdapter::ior()
extern "C" Q_DECL_EXPORT
float ritual_ZN31QSSGShaderCustomMaterialAdapter3iorEv(
    QSSGShaderCustomMaterialAdapter *self) {
  return self->ior();
}

//  float QSSGShaderCustomMaterialAdapter::fresnelScale()
extern "C" Q_DECL_EXPORT
float ritual_ZN31QSSGShaderCustomMaterialAdapter12fresnelScaleEv(
    QSSGShaderCustomMaterialAdapter *self) {
  return self->fresnelScale();
}

//  float QSSGShaderCustomMaterialAdapter::fresnelBias()
extern "C" Q_DECL_EXPORT
float ritual_ZN31QSSGShaderCustomMaterialAdapter11fresnelBiasEv(
    QSSGShaderCustomMaterialAdapter *self) {
  return self->fresnelBias();
}

//  float QSSGShaderCustomMaterialAdapter::fresnelPower()
extern "C" Q_DECL_EXPORT
float ritual_ZN31QSSGShaderCustomMaterialAdapter12fresnelPowerEv(
    QSSGShaderCustomMaterialAdapter *self) {
  return self->fresnelPower();
}

//  float QSSGShaderCustomMaterialAdapter::clearcoatFresnelScale()
extern "C" Q_DECL_EXPORT
float ritual_ZN31QSSGShaderCustomMaterialAdapter21clearcoatFresnelScaleEv(
    QSSGShaderCustomMaterialAdapter *self) {
  return self->clearcoatFresnelScale();
}

//  float QSSGShaderCustomMaterialAdapter::clearcoatFresnelBias()
extern "C" Q_DECL_EXPORT
float ritual_ZN31QSSGShaderCustomMaterialAdapter20clearcoatFresnelBiasEv(
    QSSGShaderCustomMaterialAdapter *self) {
  return self->clearcoatFresnelBias();
}

//  float QSSGShaderCustomMaterialAdapter::clearcoatFresnelPower()
extern "C" Q_DECL_EXPORT
float ritual_ZN31QSSGShaderCustomMaterialAdapter21clearcoatFresnelPowerEv(
    QSSGShaderCustomMaterialAdapter *self) {
  return self->clearcoatFresnelPower();
}

//  float QSSGShaderCustomMaterialAdapter::metalnessAmount()
extern "C" Q_DECL_EXPORT
float ritual_ZN31QSSGShaderCustomMaterialAdapter15metalnessAmountEv(
    QSSGShaderCustomMaterialAdapter *self) {
  return self->metalnessAmount();
}

//  float QSSGShaderCustomMaterialAdapter::specularAmount()
extern "C" Q_DECL_EXPORT
float ritual_ZN31QSSGShaderCustomMaterialAdapter14specularAmountEv(
    QSSGShaderCustomMaterialAdapter *self) {
  return self->specularAmount();
}

//  float QSSGShaderCustomMaterialAdapter::specularRoughness()
extern "C" Q_DECL_EXPORT
float ritual_ZN31QSSGShaderCustomMaterialAdapter17specularRoughnessEv(
    QSSGShaderCustomMaterialAdapter *self) {
  return self->specularRoughness();
}

//  float QSSGShaderCustomMaterialAdapter::bumpAmount()
extern "C" Q_DECL_EXPORT
float ritual_ZN31QSSGShaderCustomMaterialAdapter10bumpAmountEv(
    QSSGShaderCustomMaterialAdapter *self) {
  return self->bumpAmount();
}

//  float QSSGShaderCustomMaterialAdapter::translucentFallOff()
extern "C" Q_DECL_EXPORT
float ritual_ZN31QSSGShaderCustomMaterialAdapter18translucentFallOffEv(
    QSSGShaderCustomMaterialAdapter *self) {
  return self->translucentFallOff();
}

//  float QSSGShaderCustomMaterialAdapter::diffuseLightWrap()
extern "C" Q_DECL_EXPORT
float ritual_ZN31QSSGShaderCustomMaterialAdapter16diffuseLightWrapEv(
    QSSGShaderCustomMaterialAdapter *self) {
  return self->diffuseLightWrap();
}

//  float QSSGShaderCustomMaterialAdapter::occlusionAmount()
extern "C" Q_DECL_EXPORT
float ritual_ZN31QSSGShaderCustomMaterialAdapter15occlusionAmountEv(
    QSSGShaderCustomMaterialAdapter *self) {
  return self->occlusionAmount();
}

//  float QSSGShaderCustomMaterialAdapter::alphaCutOff()
extern "C" Q_DECL_EXPORT
float ritual_ZN31QSSGShaderCustomMaterialAdapter11alphaCutOffEv(
    QSSGShaderCustomMaterialAdapter *self) {
  return self->alphaCutOff();
}

//  float QSSGShaderCustomMaterialAdapter::pointSize()
extern "C" Q_DECL_EXPORT
float ritual_ZN31QSSGShaderCustomMaterialAdapter9pointSizeEv(
    QSSGShaderCustomMaterialAdapter *self) {
  return self->pointSize();
}

//  float QSSGShaderCustomMaterialAdapter::lineWidth()
extern "C" Q_DECL_EXPORT
float ritual_ZN31QSSGShaderCustomMaterialAdapter9lineWidthEv(
    QSSGShaderCustomMaterialAdapter *self) {
  return self->lineWidth();
}

//  float QSSGShaderCustomMaterialAdapter::heightAmount()
extern "C" Q_DECL_EXPORT
float ritual_ZN31QSSGShaderCustomMaterialAdapter12heightAmountEv(
    QSSGShaderCustomMaterialAdapter *self) {
  return self->heightAmount();
}

//  float QSSGShaderCustomMaterialAdapter::minHeightSamples()
extern "C" Q_DECL_EXPORT
float ritual_ZN31QSSGShaderCustomMaterialAdapter16minHeightSamplesEv(
    QSSGShaderCustomMaterialAdapter *self) {
  return self->minHeightSamples();
}

//  float QSSGShaderCustomMaterialAdapter::maxHeightSamples()
extern "C" Q_DECL_EXPORT
float ritual_ZN31QSSGShaderCustomMaterialAdapter16maxHeightSamplesEv(
    QSSGShaderCustomMaterialAdapter *self) {
  return self->maxHeightSamples();
}

//  float QSSGShaderCustomMaterialAdapter::clearcoatAmount()
extern "C" Q_DECL_EXPORT
float ritual_ZN31QSSGShaderCustomMaterialAdapter15clearcoatAmountEv(
    QSSGShaderCustomMaterialAdapter *self) {
  return self->clearcoatAmount();
}

//  float QSSGShaderCustomMaterialAdapter::clearcoatRoughnessAmount()
extern "C" Q_DECL_EXPORT
float ritual_ZN31QSSGShaderCustomMaterialAdapter24clearcoatRoughnessAmountEv(
    QSSGShaderCustomMaterialAdapter *self) {
  return self->clearcoatRoughnessAmount();
}

//  float QSSGShaderCustomMaterialAdapter::clearcoatNormalStrength()
extern "C" Q_DECL_EXPORT
float ritual_ZN31QSSGShaderCustomMaterialAdapter23clearcoatNormalStrengthEv(
    QSSGShaderCustomMaterialAdapter *self) {
  return self->clearcoatNormalStrength();
}

//  float QSSGShaderCustomMaterialAdapter::transmissionFactor()
extern "C" Q_DECL_EXPORT
float ritual_ZN31QSSGShaderCustomMaterialAdapter18transmissionFactorEv(
    QSSGShaderCustomMaterialAdapter *self) {
  return self->transmissionFactor();
}

//  float QSSGShaderCustomMaterialAdapter::thicknessFactor()
extern "C" Q_DECL_EXPORT
float ritual_ZN31QSSGShaderCustomMaterialAdapter15thicknessFactorEv(
    QSSGShaderCustomMaterialAdapter *self) {
  return self->thicknessFactor();
}

//  float QSSGShaderCustomMaterialAdapter::attenuationDistance()
extern "C" Q_DECL_EXPORT
float ritual_ZN31QSSGShaderCustomMaterialAdapter19attenuationDistanceEv(
    QSSGShaderCustomMaterialAdapter *self) {
  return self->attenuationDistance();
}

//  QVector3D QSSGShaderCustomMaterialAdapter::attenuationColor()
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZN31QSSGShaderCustomMaterialAdapter16attenuationColorEv(
    QSSGShaderCustomMaterialAdapter *self) {
  return new QVector3D(self->attenuationColor());
}

//  bool QSSGShaderCustomMaterialAdapter::isUnshaded()
extern "C" Q_DECL_EXPORT
bool ritual_ZN31QSSGShaderCustomMaterialAdapter10isUnshadedEv(
    QSSGShaderCustomMaterialAdapter *self) {
  return self->isUnshaded();
}

//  bool QSSGShaderCustomMaterialAdapter::hasCustomShaderSnippet(QSSGShaderCa
//      che::ShaderType type)
extern "C" Q_DECL_EXPORT
bool ritual_ZN31QSSGShaderCustomMaterialAdapter22hasCustomShaderSnippetEN15QSSGShaderCache10ShaderTypeE(
    QSSGShaderCustomMaterialAdapter *self,
    QSSGShaderCache::ShaderType type) {
  return self->hasCustomShaderSnippet(type);
}

//  QByteArray QSSGShaderCustomMaterialAdapter::customShaderSnippet(QSSGShade
//      rCache::ShaderType type, QSSGShaderLibraryManager
//      &shaderLibraryManager, bool multiViewCompatible)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN31QSSGShaderCustomMaterialAdapter19customShaderSnippetEN15QSSGShaderCache10ShaderTypeER24QSSGShaderLibraryManagerb(
    QSSGShaderCustomMaterialAdapter *self,
    QSSGShaderCache::ShaderType type,
    QSSGShaderLibraryManager *shaderLibraryManager,
    bool multiViewCompatible) {
  return new QByteArray(
      self->customShaderSnippet(
          type,
          *shaderLibraryManager,
          multiViewCompatible));
}

//  bool QSSGShaderCustomMaterialAdapter::hasCustomShaderFunction(QSSGShaderC
//      ache::ShaderType shaderType, const QByteArray &funcName,
//      QSSGShaderLibraryManager &shaderLibraryManager)
extern "C" Q_DECL_EXPORT
bool ritual_ZN31QSSGShaderCustomMaterialAdapter23hasCustomShaderFunctionEN15QSSGShaderCache10ShaderTypeERK10QByteArrayR24QSSGShaderLibraryManager(
    QSSGShaderCustomMaterialAdapter *self,
    QSSGShaderCache::ShaderType shaderType,
    const QByteArray *funcName,
    QSSGShaderLibraryManager *shaderLibraryManager) {
  return self->hasCustomShaderFunction(
      shaderType,
      *funcName,
      *shaderLibraryManager);
}

//  void QSSGShaderCustomMaterialAdapter::setCustomPropertyUniforms(char
//      *ubufData, QSSGRhiShaderPipeline &shaderPipeline, const
//      QSSGRenderContextInterface &context)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QSSGShaderCustomMaterialAdapter25setCustomPropertyUniformsEPcR21QSSGRhiShaderPipelineRK26QSSGRenderContextInterface(
    QSSGShaderCustomMaterialAdapter *self,
    char *ubufData,
    QSSGRhiShaderPipeline *shaderPipeline,
    const QSSGRenderContextInterface *context) {
  self->setCustomPropertyUniforms(ubufData, *shaderPipeline, *context);
}

//  bool QSSGShaderCustomMaterialAdapter::usesSharedVariables()
extern "C" Q_DECL_EXPORT
bool ritual_ZN31QSSGShaderCustomMaterialAdapter19usesSharedVariablesEv(
    QSSGShaderCustomMaterialAdapter *self) {
  return self->usesSharedVariables();
}

//  void QSSGShaderCustomMaterialAdapter::beginPrepareCustomShader(CustomShad
//      erPrepWorkData *workData, ShaderCodeAndMetaData *codeAndMetaData,
//      const QByteArray &shaderCode, QSSGShaderCache::ShaderType type, bool
//      multiViewCompatible)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QSSGShaderCustomMaterialAdapter24beginPrepareCustomShaderEPNS_24CustomShaderPrepWorkDataEPSt4pairI10QByteArray24QSSGCustomShaderMetaDataERKS3_N15QSSGShaderCache10ShaderTypeEb(
    QSSGShaderCustomMaterialAdapter::CustomShaderPrepWorkData *workData,
    QSSGShaderCustomMaterialAdapter::ShaderCodeAndMetaData *codeAndMetaData,
    const QByteArray *shaderCode,
    QSSGShaderCache::ShaderType type,
    bool multiViewCompatible) {
  QSSGShaderCustomMaterialAdapter::beginPrepareCustomShader(
      workData,
      codeAndMetaData,
      *shaderCode,
      type,
      multiViewCompatible);
}

//  void
//      QSSGShaderCustomMaterialAdapter::finishPrepareCustomShader(QByteArray
//      *dst, const CustomShaderPrepWorkData &workData, const
//      ShaderCodeAndMetaData &codeAndMetaData, QSSGShaderCache::ShaderType
//      type, bool multiViewCompatible, const StringPairList &baseUniforms,
//      const StringPairList &baseInputs, const StringPairList &baseOutputs,
//      const StringPairList &multiViewDependentSamplers, const
//      StringPairList &multiViewDependentUniforms)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QSSGShaderCustomMaterialAdapter25finishPrepareCustomShaderEP10QByteArrayRKNS_24CustomShaderPrepWorkDataERKSt4pairIS0_24QSSGCustomShaderMetaDataEN15QSSGShaderCache10ShaderTypeEbRK15QVarLengthArrayIS5_IS0_S0_ELx16EESG_SG_SG_SG_(
    QByteArray *dst,
    const QSSGShaderCustomMaterialAdapter::CustomShaderPrepWorkData *workData,
    const QSSGShaderCustomMaterialAdapter::ShaderCodeAndMetaData *codeAndMetaData,
    QSSGShaderCache::ShaderType type,
    bool multiViewCompatible,
    const QSSGShaderCustomMaterialAdapter::StringPairList *baseUniforms,
    const QSSGShaderCustomMaterialAdapter::StringPairList *baseInputs,
    const QSSGShaderCustomMaterialAdapter::StringPairList *baseOutputs,
    const QSSGShaderCustomMaterialAdapter::StringPairList *multiViewDependentSamplers,
    const QSSGShaderCustomMaterialAdapter::StringPairList *multiViewDependentUniforms) {
  QSSGShaderCustomMaterialAdapter::finishPrepareCustomShader(
      dst,
      *workData,
      *codeAndMetaData,
      type,
      multiViewCompatible,
      *baseUniforms,
      *baseInputs,
      *baseOutputs,
      *multiViewDependentSamplers,
      *multiViewDependentUniforms);
}

//  QSSGShaderCustomMaterialAdapter::~QSSGShaderCustomMaterialAdapter()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QSSGShaderCustomMaterialAdapterD1Ev(
    QSSGShaderCustomMaterialAdapter *self) {
  delete self;
}
