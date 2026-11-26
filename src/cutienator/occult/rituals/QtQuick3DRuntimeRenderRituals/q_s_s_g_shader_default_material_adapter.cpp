//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgshadermaterialadapter_
//  p.h, Qt 6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgshadermaterialadapter_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qvectornd.h>

//  QSSGShaderDefaultMaterialAdapter::QSSGShaderDefaultMaterialAdapter(const
//      QSSGRenderDefaultMaterial &material)
extern "C" Q_DECL_EXPORT
QSSGShaderDefaultMaterialAdapter *ritual_ZN32QSSGShaderDefaultMaterialAdapterC1ERK25QSSGRenderDefaultMaterial(
    const QSSGRenderDefaultMaterial *material) {
  return new QSSGShaderDefaultMaterialAdapter(*material);
}

//  bool QSSGShaderDefaultMaterialAdapter::isPrincipled()
extern "C" Q_DECL_EXPORT
bool ritual_ZN32QSSGShaderDefaultMaterialAdapter12isPrincipledEv(
    QSSGShaderDefaultMaterialAdapter *self) {
  return self->isPrincipled();
}

//  bool QSSGShaderDefaultMaterialAdapter::isSpecularGlossy()
extern "C" Q_DECL_EXPORT
bool ritual_ZN32QSSGShaderDefaultMaterialAdapter16isSpecularGlossyEv(
    QSSGShaderDefaultMaterialAdapter *self) {
  return self->isSpecularGlossy();
}

//  bool QSSGShaderDefaultMaterialAdapter::isMetalnessEnabled()
extern "C" Q_DECL_EXPORT
bool ritual_ZN32QSSGShaderDefaultMaterialAdapter18isMetalnessEnabledEv(
    QSSGShaderDefaultMaterialAdapter *self) {
  return self->isMetalnessEnabled();
}

//  bool QSSGShaderDefaultMaterialAdapter::isSpecularEnabled()
extern "C" Q_DECL_EXPORT
bool ritual_ZN32QSSGShaderDefaultMaterialAdapter17isSpecularEnabledEv(
    QSSGShaderDefaultMaterialAdapter *self) {
  return self->isSpecularEnabled();
}

//  bool QSSGShaderDefaultMaterialAdapter::isVertexColorsEnabled()
extern "C" Q_DECL_EXPORT
bool ritual_ZN32QSSGShaderDefaultMaterialAdapter21isVertexColorsEnabledEv(
    QSSGShaderDefaultMaterialAdapter *self) {
  return self->isVertexColorsEnabled();
}

//  bool QSSGShaderDefaultMaterialAdapter::isVertexColorsMaskEnabled()
extern "C" Q_DECL_EXPORT
bool ritual_ZN32QSSGShaderDefaultMaterialAdapter25isVertexColorsMaskEnabledEv(
    QSSGShaderDefaultMaterialAdapter *self) {
  return self->isVertexColorsMaskEnabled();
}

//  bool QSSGShaderDefaultMaterialAdapter::isInvertOpacityMapValue()
extern "C" Q_DECL_EXPORT
bool ritual_ZN32QSSGShaderDefaultMaterialAdapter23isInvertOpacityMapValueEv(
    QSSGShaderDefaultMaterialAdapter *self) {
  return self->isInvertOpacityMapValue();
}

//  bool QSSGShaderDefaultMaterialAdapter::isBaseColorSingleChannelEnabled()
extern "C" Q_DECL_EXPORT
bool ritual_ZN32QSSGShaderDefaultMaterialAdapter31isBaseColorSingleChannelEnabledEv(
    QSSGShaderDefaultMaterialAdapter *self) {
  return self->isBaseColorSingleChannelEnabled();
}

//  bool
//      QSSGShaderDefaultMaterialAdapter::isSpecularAmountSingleChannelEnable
//      d()
extern "C" Q_DECL_EXPORT
bool ritual_ZN32QSSGShaderDefaultMaterialAdapter36isSpecularAmountSingleChannelEnabledEv(
    QSSGShaderDefaultMaterialAdapter *self) {
  return self->isSpecularAmountSingleChannelEnabled();
}

//  bool QSSGShaderDefaultMaterialAdapter::isEmissiveSingleChannelEnabled()
extern "C" Q_DECL_EXPORT
bool ritual_ZN32QSSGShaderDefaultMaterialAdapter30isEmissiveSingleChannelEnabledEv(
    QSSGShaderDefaultMaterialAdapter *self) {
  return self->isEmissiveSingleChannelEnabled();
}

//  bool QSSGShaderDefaultMaterialAdapter::isClearcoatEnabled()
extern "C" Q_DECL_EXPORT
bool ritual_ZN32QSSGShaderDefaultMaterialAdapter18isClearcoatEnabledEv(
    QSSGShaderDefaultMaterialAdapter *self) {
  return self->isClearcoatEnabled();
}

//  bool QSSGShaderDefaultMaterialAdapter::isTransmissionEnabled()
extern "C" Q_DECL_EXPORT
bool ritual_ZN32QSSGShaderDefaultMaterialAdapter21isTransmissionEnabledEv(
    QSSGShaderDefaultMaterialAdapter *self) {
  return self->isTransmissionEnabled();
}

//  bool QSSGShaderDefaultMaterialAdapter::isFresnelScaleBiasEnabled()
extern "C" Q_DECL_EXPORT
bool ritual_ZN32QSSGShaderDefaultMaterialAdapter25isFresnelScaleBiasEnabledEv(
    QSSGShaderDefaultMaterialAdapter *self) {
  return self->isFresnelScaleBiasEnabled();
}

//  bool
//      QSSGShaderDefaultMaterialAdapter::isClearcoatFresnelScaleBiasEnabled(
//      )
extern "C" Q_DECL_EXPORT
bool ritual_ZN32QSSGShaderDefaultMaterialAdapter34isClearcoatFresnelScaleBiasEnabledEv(
    QSSGShaderDefaultMaterialAdapter *self) {
  return self->isClearcoatFresnelScaleBiasEnabled();
}

//  bool QSSGShaderDefaultMaterialAdapter::hasLighting()
extern "C" Q_DECL_EXPORT
bool ritual_ZN32QSSGShaderDefaultMaterialAdapter11hasLightingEv(
    QSSGShaderDefaultMaterialAdapter *self) {
  return self->hasLighting();
}

//  bool QSSGShaderDefaultMaterialAdapter::usesCustomSkinning()
extern "C" Q_DECL_EXPORT
bool ritual_ZN32QSSGShaderDefaultMaterialAdapter18usesCustomSkinningEv(
    QSSGShaderDefaultMaterialAdapter *self) {
  return self->usesCustomSkinning();
}

//  bool QSSGShaderDefaultMaterialAdapter::usesCustomMorphing()
extern "C" Q_DECL_EXPORT
bool ritual_ZN32QSSGShaderDefaultMaterialAdapter18usesCustomMorphingEv(
    QSSGShaderDefaultMaterialAdapter *self) {
  return self->usesCustomMorphing();
}

//  QSSGRenderDefaultMaterial::MaterialSpecularModel
//      QSSGShaderDefaultMaterialAdapter::specularModel()
extern "C" Q_DECL_EXPORT
QSSGRenderDefaultMaterial::MaterialSpecularModel ritual_ZN32QSSGShaderDefaultMaterialAdapter13specularModelEv(
    QSSGShaderDefaultMaterialAdapter *self) {
  return self->specularModel();
}

//  QSSGRenderDefaultMaterial::MaterialAlphaMode
//      QSSGShaderDefaultMaterialAdapter::alphaMode()
extern "C" Q_DECL_EXPORT
QSSGRenderDefaultMaterial::MaterialAlphaMode ritual_ZN32QSSGShaderDefaultMaterialAdapter9alphaModeEv(
    QSSGShaderDefaultMaterialAdapter *self) {
  return self->alphaMode();
}

//  QSSGRenderDefaultMaterial::VertexColorMaskFlags
//      QSSGShaderDefaultMaterialAdapter::vertexColorRedMask()
extern "C" Q_DECL_EXPORT
int ritual_ZN32QSSGShaderDefaultMaterialAdapter18vertexColorRedMaskEv(
    QSSGShaderDefaultMaterialAdapter *self) {
  return static_cast<int>(self->vertexColorRedMask().toInt());
}

//  QSSGRenderDefaultMaterial::VertexColorMaskFlags
//      QSSGShaderDefaultMaterialAdapter::vertexColorGreenMask()
extern "C" Q_DECL_EXPORT
int ritual_ZN32QSSGShaderDefaultMaterialAdapter20vertexColorGreenMaskEv(
    QSSGShaderDefaultMaterialAdapter *self) {
  return static_cast<int>(self->vertexColorGreenMask().toInt());
}

//  QSSGRenderDefaultMaterial::VertexColorMaskFlags
//      QSSGShaderDefaultMaterialAdapter::vertexColorBlueMask()
extern "C" Q_DECL_EXPORT
int ritual_ZN32QSSGShaderDefaultMaterialAdapter19vertexColorBlueMaskEv(
    QSSGShaderDefaultMaterialAdapter *self) {
  return static_cast<int>(self->vertexColorBlueMask().toInt());
}

//  QSSGRenderDefaultMaterial::VertexColorMaskFlags
//      QSSGShaderDefaultMaterialAdapter::vertexColorAlphaMask()
extern "C" Q_DECL_EXPORT
int ritual_ZN32QSSGShaderDefaultMaterialAdapter20vertexColorAlphaMaskEv(
    QSSGShaderDefaultMaterialAdapter *self) {
  return static_cast<int>(self->vertexColorAlphaMask().toInt());
}

//  QSSGRenderImage *QSSGShaderDefaultMaterialAdapter::iblProbe()
extern "C" Q_DECL_EXPORT
QSSGRenderImage *ritual_ZN32QSSGShaderDefaultMaterialAdapter8iblProbeEv(
    QSSGShaderDefaultMaterialAdapter *self) {
  return self->iblProbe();
}

//  QVector3D QSSGShaderDefaultMaterialAdapter::emissiveColor()
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZN32QSSGShaderDefaultMaterialAdapter13emissiveColorEv(
    QSSGShaderDefaultMaterialAdapter *self) {
  return new QVector3D(self->emissiveColor());
}

//  QVector4D QSSGShaderDefaultMaterialAdapter::color()
extern "C" Q_DECL_EXPORT
QVector4D *ritual_ZN32QSSGShaderDefaultMaterialAdapter5colorEv(
    QSSGShaderDefaultMaterialAdapter *self) {
  return new QVector4D(self->color());
}

//  QVector3D QSSGShaderDefaultMaterialAdapter::specularTint()
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZN32QSSGShaderDefaultMaterialAdapter12specularTintEv(
    QSSGShaderDefaultMaterialAdapter *self) {
  return new QVector3D(self->specularTint());
}

//  float QSSGShaderDefaultMaterialAdapter::ior()
extern "C" Q_DECL_EXPORT
float ritual_ZN32QSSGShaderDefaultMaterialAdapter3iorEv(
    QSSGShaderDefaultMaterialAdapter *self) {
  return self->ior();
}

//  float QSSGShaderDefaultMaterialAdapter::fresnelScale()
extern "C" Q_DECL_EXPORT
float ritual_ZN32QSSGShaderDefaultMaterialAdapter12fresnelScaleEv(
    QSSGShaderDefaultMaterialAdapter *self) {
  return self->fresnelScale();
}

//  float QSSGShaderDefaultMaterialAdapter::fresnelBias()
extern "C" Q_DECL_EXPORT
float ritual_ZN32QSSGShaderDefaultMaterialAdapter11fresnelBiasEv(
    QSSGShaderDefaultMaterialAdapter *self) {
  return self->fresnelBias();
}

//  float QSSGShaderDefaultMaterialAdapter::fresnelPower()
extern "C" Q_DECL_EXPORT
float ritual_ZN32QSSGShaderDefaultMaterialAdapter12fresnelPowerEv(
    QSSGShaderDefaultMaterialAdapter *self) {
  return self->fresnelPower();
}

//  float QSSGShaderDefaultMaterialAdapter::clearcoatFresnelScale()
extern "C" Q_DECL_EXPORT
float ritual_ZN32QSSGShaderDefaultMaterialAdapter21clearcoatFresnelScaleEv(
    QSSGShaderDefaultMaterialAdapter *self) {
  return self->clearcoatFresnelScale();
}

//  float QSSGShaderDefaultMaterialAdapter::clearcoatFresnelBias()
extern "C" Q_DECL_EXPORT
float ritual_ZN32QSSGShaderDefaultMaterialAdapter20clearcoatFresnelBiasEv(
    QSSGShaderDefaultMaterialAdapter *self) {
  return self->clearcoatFresnelBias();
}

//  float QSSGShaderDefaultMaterialAdapter::clearcoatFresnelPower()
extern "C" Q_DECL_EXPORT
float ritual_ZN32QSSGShaderDefaultMaterialAdapter21clearcoatFresnelPowerEv(
    QSSGShaderDefaultMaterialAdapter *self) {
  return self->clearcoatFresnelPower();
}

//  float QSSGShaderDefaultMaterialAdapter::metalnessAmount()
extern "C" Q_DECL_EXPORT
float ritual_ZN32QSSGShaderDefaultMaterialAdapter15metalnessAmountEv(
    QSSGShaderDefaultMaterialAdapter *self) {
  return self->metalnessAmount();
}

//  float QSSGShaderDefaultMaterialAdapter::specularAmount()
extern "C" Q_DECL_EXPORT
float ritual_ZN32QSSGShaderDefaultMaterialAdapter14specularAmountEv(
    QSSGShaderDefaultMaterialAdapter *self) {
  return self->specularAmount();
}

//  float QSSGShaderDefaultMaterialAdapter::specularRoughness()
extern "C" Q_DECL_EXPORT
float ritual_ZN32QSSGShaderDefaultMaterialAdapter17specularRoughnessEv(
    QSSGShaderDefaultMaterialAdapter *self) {
  return self->specularRoughness();
}

//  float QSSGShaderDefaultMaterialAdapter::bumpAmount()
extern "C" Q_DECL_EXPORT
float ritual_ZN32QSSGShaderDefaultMaterialAdapter10bumpAmountEv(
    QSSGShaderDefaultMaterialAdapter *self) {
  return self->bumpAmount();
}

//  float QSSGShaderDefaultMaterialAdapter::translucentFallOff()
extern "C" Q_DECL_EXPORT
float ritual_ZN32QSSGShaderDefaultMaterialAdapter18translucentFallOffEv(
    QSSGShaderDefaultMaterialAdapter *self) {
  return self->translucentFallOff();
}

//  float QSSGShaderDefaultMaterialAdapter::diffuseLightWrap()
extern "C" Q_DECL_EXPORT
float ritual_ZN32QSSGShaderDefaultMaterialAdapter16diffuseLightWrapEv(
    QSSGShaderDefaultMaterialAdapter *self) {
  return self->diffuseLightWrap();
}

//  float QSSGShaderDefaultMaterialAdapter::occlusionAmount()
extern "C" Q_DECL_EXPORT
float ritual_ZN32QSSGShaderDefaultMaterialAdapter15occlusionAmountEv(
    QSSGShaderDefaultMaterialAdapter *self) {
  return self->occlusionAmount();
}

//  float QSSGShaderDefaultMaterialAdapter::alphaCutOff()
extern "C" Q_DECL_EXPORT
float ritual_ZN32QSSGShaderDefaultMaterialAdapter11alphaCutOffEv(
    QSSGShaderDefaultMaterialAdapter *self) {
  return self->alphaCutOff();
}

//  float QSSGShaderDefaultMaterialAdapter::pointSize()
extern "C" Q_DECL_EXPORT
float ritual_ZN32QSSGShaderDefaultMaterialAdapter9pointSizeEv(
    QSSGShaderDefaultMaterialAdapter *self) {
  return self->pointSize();
}

//  float QSSGShaderDefaultMaterialAdapter::lineWidth()
extern "C" Q_DECL_EXPORT
float ritual_ZN32QSSGShaderDefaultMaterialAdapter9lineWidthEv(
    QSSGShaderDefaultMaterialAdapter *self) {
  return self->lineWidth();
}

//  float QSSGShaderDefaultMaterialAdapter::heightAmount()
extern "C" Q_DECL_EXPORT
float ritual_ZN32QSSGShaderDefaultMaterialAdapter12heightAmountEv(
    QSSGShaderDefaultMaterialAdapter *self) {
  return self->heightAmount();
}

//  float QSSGShaderDefaultMaterialAdapter::minHeightSamples()
extern "C" Q_DECL_EXPORT
float ritual_ZN32QSSGShaderDefaultMaterialAdapter16minHeightSamplesEv(
    QSSGShaderDefaultMaterialAdapter *self) {
  return self->minHeightSamples();
}

//  float QSSGShaderDefaultMaterialAdapter::maxHeightSamples()
extern "C" Q_DECL_EXPORT
float ritual_ZN32QSSGShaderDefaultMaterialAdapter16maxHeightSamplesEv(
    QSSGShaderDefaultMaterialAdapter *self) {
  return self->maxHeightSamples();
}

//  float QSSGShaderDefaultMaterialAdapter::clearcoatAmount()
extern "C" Q_DECL_EXPORT
float ritual_ZN32QSSGShaderDefaultMaterialAdapter15clearcoatAmountEv(
    QSSGShaderDefaultMaterialAdapter *self) {
  return self->clearcoatAmount();
}

//  float QSSGShaderDefaultMaterialAdapter::clearcoatRoughnessAmount()
extern "C" Q_DECL_EXPORT
float ritual_ZN32QSSGShaderDefaultMaterialAdapter24clearcoatRoughnessAmountEv(
    QSSGShaderDefaultMaterialAdapter *self) {
  return self->clearcoatRoughnessAmount();
}

//  float QSSGShaderDefaultMaterialAdapter::clearcoatNormalStrength()
extern "C" Q_DECL_EXPORT
float ritual_ZN32QSSGShaderDefaultMaterialAdapter23clearcoatNormalStrengthEv(
    QSSGShaderDefaultMaterialAdapter *self) {
  return self->clearcoatNormalStrength();
}

//  float QSSGShaderDefaultMaterialAdapter::transmissionFactor()
extern "C" Q_DECL_EXPORT
float ritual_ZN32QSSGShaderDefaultMaterialAdapter18transmissionFactorEv(
    QSSGShaderDefaultMaterialAdapter *self) {
  return self->transmissionFactor();
}

//  float QSSGShaderDefaultMaterialAdapter::thicknessFactor()
extern "C" Q_DECL_EXPORT
float ritual_ZN32QSSGShaderDefaultMaterialAdapter15thicknessFactorEv(
    QSSGShaderDefaultMaterialAdapter *self) {
  return self->thicknessFactor();
}

//  float QSSGShaderDefaultMaterialAdapter::attenuationDistance()
extern "C" Q_DECL_EXPORT
float ritual_ZN32QSSGShaderDefaultMaterialAdapter19attenuationDistanceEv(
    QSSGShaderDefaultMaterialAdapter *self) {
  return self->attenuationDistance();
}

//  QVector3D QSSGShaderDefaultMaterialAdapter::attenuationColor()
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZN32QSSGShaderDefaultMaterialAdapter16attenuationColorEv(
    QSSGShaderDefaultMaterialAdapter *self) {
  return new QVector3D(self->attenuationColor());
}

//  QSSGShaderDefaultMaterialAdapter::~QSSGShaderDefaultMaterialAdapter()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QSSGShaderDefaultMaterialAdapterD1Ev(
    QSSGShaderDefaultMaterialAdapter *self) {
  delete self;
}
