//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgshadermaterialadapter_
//  p.h, Qt 6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgshadermaterialadapter_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qvectornd.h>
#include <cstring>

//  A QSSGShaderMaterialAdapter that Python can take functions over in. Every QSSGShaderMaterialAdapter
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQSSGShaderMaterialAdapterCall0)(const void *, int *);
typedef bool (*CuteQSSGShaderMaterialAdapterCall1)(const void *, int *);
typedef bool (*CuteQSSGShaderMaterialAdapterCall2)(const void *, int *);
typedef bool (*CuteQSSGShaderMaterialAdapterCall3)(const void *, int *);
typedef bool (*CuteQSSGShaderMaterialAdapterCall4)(const void *, int *);
typedef bool (*CuteQSSGShaderMaterialAdapterCall5)(const void *, int *);
typedef bool (*CuteQSSGShaderMaterialAdapterCall6)(const void *, int *);
typedef bool (*CuteQSSGShaderMaterialAdapterCall7)(const void *, int *);
typedef bool (*CuteQSSGShaderMaterialAdapterCall8)(const void *, int *);
typedef bool (*CuteQSSGShaderMaterialAdapterCall9)(const void *, int *);
typedef bool (*CuteQSSGShaderMaterialAdapterCall10)(const void *, int *);
typedef bool (*CuteQSSGShaderMaterialAdapterCall11)(const void *, int *);
typedef bool (*CuteQSSGShaderMaterialAdapterCall12)(const void *, int *);
typedef bool (*CuteQSSGShaderMaterialAdapterCall13)(const void *, int *);
typedef bool (*CuteQSSGShaderMaterialAdapterCall14)(const void *, int *);
typedef bool (*CuteQSSGShaderMaterialAdapterCall15)(const void *, int *);
typedef bool (*CuteQSSGShaderMaterialAdapterCall16)(const void *, int *);
typedef int (*CuteQSSGShaderMaterialAdapterCall17)(const void *, int *);
typedef int (*CuteQSSGShaderMaterialAdapterCall18)(const void *, int *);
typedef int (*CuteQSSGShaderMaterialAdapterCall19)(const void *, int *);
typedef int (*CuteQSSGShaderMaterialAdapterCall20)(const void *, int *);
typedef int (*CuteQSSGShaderMaterialAdapterCall21)(const void *, int *);
typedef int (*CuteQSSGShaderMaterialAdapterCall22)(const void *, int *);
typedef void * (*CuteQSSGShaderMaterialAdapterCall23)(const void *, int *);
typedef const QVector3D * (*CuteQSSGShaderMaterialAdapterCall24)(const void *, int *);
typedef const QVector4D * (*CuteQSSGShaderMaterialAdapterCall25)(const void *, int *);
typedef const QVector3D * (*CuteQSSGShaderMaterialAdapterCall26)(const void *, int *);
typedef float (*CuteQSSGShaderMaterialAdapterCall27)(const void *, int *);
typedef float (*CuteQSSGShaderMaterialAdapterCall28)(const void *, int *);
typedef float (*CuteQSSGShaderMaterialAdapterCall29)(const void *, int *);
typedef float (*CuteQSSGShaderMaterialAdapterCall30)(const void *, int *);
typedef float (*CuteQSSGShaderMaterialAdapterCall31)(const void *, int *);
typedef float (*CuteQSSGShaderMaterialAdapterCall32)(const void *, int *);
typedef float (*CuteQSSGShaderMaterialAdapterCall33)(const void *, int *);
typedef float (*CuteQSSGShaderMaterialAdapterCall34)(const void *, int *);
typedef float (*CuteQSSGShaderMaterialAdapterCall35)(const void *, int *);
typedef float (*CuteQSSGShaderMaterialAdapterCall36)(const void *, int *);
typedef float (*CuteQSSGShaderMaterialAdapterCall37)(const void *, int *);
typedef float (*CuteQSSGShaderMaterialAdapterCall38)(const void *, int *);
typedef float (*CuteQSSGShaderMaterialAdapterCall39)(const void *, int *);
typedef float (*CuteQSSGShaderMaterialAdapterCall40)(const void *, int *);
typedef float (*CuteQSSGShaderMaterialAdapterCall41)(const void *, int *);
typedef float (*CuteQSSGShaderMaterialAdapterCall42)(const void *, int *);
typedef float (*CuteQSSGShaderMaterialAdapterCall43)(const void *, int *);
typedef float (*CuteQSSGShaderMaterialAdapterCall44)(const void *, int *);
typedef float (*CuteQSSGShaderMaterialAdapterCall45)(const void *, int *);
typedef float (*CuteQSSGShaderMaterialAdapterCall46)(const void *, int *);
typedef float (*CuteQSSGShaderMaterialAdapterCall47)(const void *, int *);
typedef float (*CuteQSSGShaderMaterialAdapterCall48)(const void *, int *);
typedef float (*CuteQSSGShaderMaterialAdapterCall49)(const void *, int *);
typedef float (*CuteQSSGShaderMaterialAdapterCall50)(const void *, int *);
typedef float (*CuteQSSGShaderMaterialAdapterCall51)(const void *, int *);
typedef float (*CuteQSSGShaderMaterialAdapterCall52)(const void *, int *);
typedef const QVector3D * (*CuteQSSGShaderMaterialAdapterCall53)(const void *, int *);
typedef bool (*CuteQSSGShaderMaterialAdapterCall54)(const void *, int *);
typedef bool (*CuteQSSGShaderMaterialAdapterCall55)(const void *, int, int *);
typedef bool (*CuteQSSGShaderMaterialAdapterCall56)(const void *, int *);
class CuteQSSGShaderMaterialAdapter : public QSSGShaderMaterialAdapter {
public:
  using QSSGShaderMaterialAdapter::QSSGShaderMaterialAdapter;
  void *taken[57] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN25QSSGShaderMaterialAdapter12isPrincipledEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN25QSSGShaderMaterialAdapter16isSpecularGlossyEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN25QSSGShaderMaterialAdapter18isMetalnessEnabledEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN25QSSGShaderMaterialAdapter17isSpecularEnabledEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN25QSSGShaderMaterialAdapter21isVertexColorsEnabledEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN25QSSGShaderMaterialAdapter25isVertexColorsMaskEnabledEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN25QSSGShaderMaterialAdapter23isInvertOpacityMapValueEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN25QSSGShaderMaterialAdapter31isBaseColorSingleChannelEnabledEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN25QSSGShaderMaterialAdapter36isSpecularAmountSingleChannelEnabledEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN25QSSGShaderMaterialAdapter30isEmissiveSingleChannelEnabledEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN25QSSGShaderMaterialAdapter25isFresnelScaleBiasEnabledEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN25QSSGShaderMaterialAdapter34isClearcoatFresnelScaleBiasEnabledEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN25QSSGShaderMaterialAdapter18isClearcoatEnabledEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN25QSSGShaderMaterialAdapter21isTransmissionEnabledEv")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN25QSSGShaderMaterialAdapter11hasLightingEv")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN25QSSGShaderMaterialAdapter18usesCustomSkinningEv")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN25QSSGShaderMaterialAdapter18usesCustomMorphingEv")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN25QSSGShaderMaterialAdapter13specularModelEv")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN25QSSGShaderMaterialAdapter9alphaModeEv")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN25QSSGShaderMaterialAdapter18vertexColorRedMaskEv")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN25QSSGShaderMaterialAdapter20vertexColorGreenMaskEv")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN25QSSGShaderMaterialAdapter19vertexColorBlueMaskEv")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN25QSSGShaderMaterialAdapter20vertexColorAlphaMaskEv")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN25QSSGShaderMaterialAdapter8iblProbeEv")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN25QSSGShaderMaterialAdapter13emissiveColorEv")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN25QSSGShaderMaterialAdapter5colorEv")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN25QSSGShaderMaterialAdapter12specularTintEv")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN25QSSGShaderMaterialAdapter3iorEv")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN25QSSGShaderMaterialAdapter12fresnelScaleEv")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN25QSSGShaderMaterialAdapter11fresnelBiasEv")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN25QSSGShaderMaterialAdapter12fresnelPowerEv")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN25QSSGShaderMaterialAdapter21clearcoatFresnelScaleEv")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN25QSSGShaderMaterialAdapter20clearcoatFresnelBiasEv")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN25QSSGShaderMaterialAdapter21clearcoatFresnelPowerEv")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN25QSSGShaderMaterialAdapter15metalnessAmountEv")) {
      taken[34] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN25QSSGShaderMaterialAdapter14specularAmountEv")) {
      taken[35] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN25QSSGShaderMaterialAdapter17specularRoughnessEv")) {
      taken[36] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN25QSSGShaderMaterialAdapter10bumpAmountEv")) {
      taken[37] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN25QSSGShaderMaterialAdapter18translucentFallOffEv")) {
      taken[38] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN25QSSGShaderMaterialAdapter16diffuseLightWrapEv")) {
      taken[39] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN25QSSGShaderMaterialAdapter15occlusionAmountEv")) {
      taken[40] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN25QSSGShaderMaterialAdapter11alphaCutOffEv")) {
      taken[41] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN25QSSGShaderMaterialAdapter9pointSizeEv")) {
      taken[42] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN25QSSGShaderMaterialAdapter9lineWidthEv")) {
      taken[43] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN25QSSGShaderMaterialAdapter12heightAmountEv")) {
      taken[44] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN25QSSGShaderMaterialAdapter16minHeightSamplesEv")) {
      taken[45] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN25QSSGShaderMaterialAdapter16maxHeightSamplesEv")) {
      taken[46] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN25QSSGShaderMaterialAdapter15clearcoatAmountEv")) {
      taken[47] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN25QSSGShaderMaterialAdapter24clearcoatRoughnessAmountEv")) {
      taken[48] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN25QSSGShaderMaterialAdapter23clearcoatNormalStrengthEv")) {
      taken[49] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN25QSSGShaderMaterialAdapter18transmissionFactorEv")) {
      taken[50] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN25QSSGShaderMaterialAdapter15thicknessFactorEv")) {
      taken[51] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN25QSSGShaderMaterialAdapter19attenuationDistanceEv")) {
      taken[52] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN25QSSGShaderMaterialAdapter16attenuationColorEv")) {
      taken[53] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN25QSSGShaderMaterialAdapter10isUnshadedEv")) {
      taken[54] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN25QSSGShaderMaterialAdapter22hasCustomShaderSnippetEN15QSSGShaderCache10ShaderTypeE")) {
      taken[55] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN25QSSGShaderMaterialAdapter19usesSharedVariablesEv")) {
      taken[56] = call;
      return true;
    }
    return false;
  }

  //  bool QSSGShaderMaterialAdapter::isPrincipled()
  bool isPrincipled() override {
    if (taken[0]) {
      int handled = 0;
      CuteQSSGShaderMaterialAdapterCall0 call = reinterpret_cast<CuteQSSGShaderMaterialAdapterCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QSSGShaderMaterialAdapter::isSpecularGlossy()
  bool isSpecularGlossy() override {
    if (taken[1]) {
      int handled = 0;
      CuteQSSGShaderMaterialAdapterCall1 call = reinterpret_cast<CuteQSSGShaderMaterialAdapterCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QSSGShaderMaterialAdapter::isMetalnessEnabled()
  bool isMetalnessEnabled() override {
    if (taken[2]) {
      int handled = 0;
      CuteQSSGShaderMaterialAdapterCall2 call = reinterpret_cast<CuteQSSGShaderMaterialAdapterCall2>(taken[2]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QSSGShaderMaterialAdapter::isSpecularEnabled()
  bool isSpecularEnabled() override {
    if (taken[3]) {
      int handled = 0;
      CuteQSSGShaderMaterialAdapterCall3 call = reinterpret_cast<CuteQSSGShaderMaterialAdapterCall3>(taken[3]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QSSGShaderMaterialAdapter::isVertexColorsEnabled()
  bool isVertexColorsEnabled() override {
    if (taken[4]) {
      int handled = 0;
      CuteQSSGShaderMaterialAdapterCall4 call = reinterpret_cast<CuteQSSGShaderMaterialAdapterCall4>(taken[4]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QSSGShaderMaterialAdapter::isVertexColorsMaskEnabled()
  bool isVertexColorsMaskEnabled() override {
    if (taken[5]) {
      int handled = 0;
      CuteQSSGShaderMaterialAdapterCall5 call = reinterpret_cast<CuteQSSGShaderMaterialAdapterCall5>(taken[5]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QSSGShaderMaterialAdapter::isInvertOpacityMapValue()
  bool isInvertOpacityMapValue() override {
    if (taken[6]) {
      int handled = 0;
      CuteQSSGShaderMaterialAdapterCall6 call = reinterpret_cast<CuteQSSGShaderMaterialAdapterCall6>(taken[6]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QSSGShaderMaterialAdapter::isBaseColorSingleChannelEnabled()
  bool isBaseColorSingleChannelEnabled() override {
    if (taken[7]) {
      int handled = 0;
      CuteQSSGShaderMaterialAdapterCall7 call = reinterpret_cast<CuteQSSGShaderMaterialAdapterCall7>(taken[7]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool
  //      QSSGShaderMaterialAdapter::isSpecularAmountSingleChannelEnabled()
  bool isSpecularAmountSingleChannelEnabled() override {
    if (taken[8]) {
      int handled = 0;
      CuteQSSGShaderMaterialAdapterCall8 call = reinterpret_cast<CuteQSSGShaderMaterialAdapterCall8>(taken[8]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QSSGShaderMaterialAdapter::isEmissiveSingleChannelEnabled()
  bool isEmissiveSingleChannelEnabled() override {
    if (taken[9]) {
      int handled = 0;
      CuteQSSGShaderMaterialAdapterCall9 call = reinterpret_cast<CuteQSSGShaderMaterialAdapterCall9>(taken[9]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QSSGShaderMaterialAdapter::isFresnelScaleBiasEnabled()
  bool isFresnelScaleBiasEnabled() override {
    if (taken[10]) {
      int handled = 0;
      CuteQSSGShaderMaterialAdapterCall10 call = reinterpret_cast<CuteQSSGShaderMaterialAdapterCall10>(taken[10]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QSSGShaderMaterialAdapter::isClearcoatFresnelScaleBiasEnabled()
  bool isClearcoatFresnelScaleBiasEnabled() override {
    if (taken[11]) {
      int handled = 0;
      CuteQSSGShaderMaterialAdapterCall11 call = reinterpret_cast<CuteQSSGShaderMaterialAdapterCall11>(taken[11]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QSSGShaderMaterialAdapter::isClearcoatEnabled()
  bool isClearcoatEnabled() override {
    if (taken[12]) {
      int handled = 0;
      CuteQSSGShaderMaterialAdapterCall12 call = reinterpret_cast<CuteQSSGShaderMaterialAdapterCall12>(taken[12]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QSSGShaderMaterialAdapter::isTransmissionEnabled()
  bool isTransmissionEnabled() override {
    if (taken[13]) {
      int handled = 0;
      CuteQSSGShaderMaterialAdapterCall13 call = reinterpret_cast<CuteQSSGShaderMaterialAdapterCall13>(taken[13]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QSSGShaderMaterialAdapter::hasLighting()
  bool hasLighting() override {
    if (taken[14]) {
      int handled = 0;
      CuteQSSGShaderMaterialAdapterCall14 call = reinterpret_cast<CuteQSSGShaderMaterialAdapterCall14>(taken[14]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QSSGShaderMaterialAdapter::usesCustomSkinning()
  bool usesCustomSkinning() override {
    if (taken[15]) {
      int handled = 0;
      CuteQSSGShaderMaterialAdapterCall15 call = reinterpret_cast<CuteQSSGShaderMaterialAdapterCall15>(taken[15]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QSSGShaderMaterialAdapter::usesCustomMorphing()
  bool usesCustomMorphing() override {
    if (taken[16]) {
      int handled = 0;
      CuteQSSGShaderMaterialAdapterCall16 call = reinterpret_cast<CuteQSSGShaderMaterialAdapterCall16>(taken[16]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  QSSGRenderDefaultMaterial::MaterialSpecularModel
  //      QSSGShaderMaterialAdapter::specularModel()
  QSSGRenderDefaultMaterial::MaterialSpecularModel specularModel() override {
    if (taken[17]) {
      int handled = 0;
      CuteQSSGShaderMaterialAdapterCall17 call = reinterpret_cast<CuteQSSGShaderMaterialAdapterCall17>(taken[17]);
      int given = call(this, &handled);
      if (handled) return static_cast<QSSGRenderDefaultMaterial::MaterialSpecularModel>(given);
    }
    return {};
  }

  //  QSSGRenderDefaultMaterial::MaterialAlphaMode
  //      QSSGShaderMaterialAdapter::alphaMode()
  QSSGRenderDefaultMaterial::MaterialAlphaMode alphaMode() override {
    if (taken[18]) {
      int handled = 0;
      CuteQSSGShaderMaterialAdapterCall18 call = reinterpret_cast<CuteQSSGShaderMaterialAdapterCall18>(taken[18]);
      int given = call(this, &handled);
      if (handled) return static_cast<QSSGRenderDefaultMaterial::MaterialAlphaMode>(given);
    }
    return {};
  }

  //  QSSGRenderDefaultMaterial::VertexColorMaskFlags
  //      QSSGShaderMaterialAdapter::vertexColorRedMask()
  QSSGRenderDefaultMaterial::VertexColorMaskFlags vertexColorRedMask() override {
    if (taken[19]) {
      int handled = 0;
      CuteQSSGShaderMaterialAdapterCall19 call = reinterpret_cast<CuteQSSGShaderMaterialAdapterCall19>(taken[19]);
      int given = call(this, &handled);
      if (handled) return QFlags<QSSGRenderDefaultMaterial::VertexColorMask>::fromInt(given);
    }
    return {};
  }

  //  QSSGRenderDefaultMaterial::VertexColorMaskFlags
  //      QSSGShaderMaterialAdapter::vertexColorGreenMask()
  QSSGRenderDefaultMaterial::VertexColorMaskFlags vertexColorGreenMask() override {
    if (taken[20]) {
      int handled = 0;
      CuteQSSGShaderMaterialAdapterCall20 call = reinterpret_cast<CuteQSSGShaderMaterialAdapterCall20>(taken[20]);
      int given = call(this, &handled);
      if (handled) return QFlags<QSSGRenderDefaultMaterial::VertexColorMask>::fromInt(given);
    }
    return {};
  }

  //  QSSGRenderDefaultMaterial::VertexColorMaskFlags
  //      QSSGShaderMaterialAdapter::vertexColorBlueMask()
  QSSGRenderDefaultMaterial::VertexColorMaskFlags vertexColorBlueMask() override {
    if (taken[21]) {
      int handled = 0;
      CuteQSSGShaderMaterialAdapterCall21 call = reinterpret_cast<CuteQSSGShaderMaterialAdapterCall21>(taken[21]);
      int given = call(this, &handled);
      if (handled) return QFlags<QSSGRenderDefaultMaterial::VertexColorMask>::fromInt(given);
    }
    return {};
  }

  //  QSSGRenderDefaultMaterial::VertexColorMaskFlags
  //      QSSGShaderMaterialAdapter::vertexColorAlphaMask()
  QSSGRenderDefaultMaterial::VertexColorMaskFlags vertexColorAlphaMask() override {
    if (taken[22]) {
      int handled = 0;
      CuteQSSGShaderMaterialAdapterCall22 call = reinterpret_cast<CuteQSSGShaderMaterialAdapterCall22>(taken[22]);
      int given = call(this, &handled);
      if (handled) return QFlags<QSSGRenderDefaultMaterial::VertexColorMask>::fromInt(given);
    }
    return {};
  }

  //  QSSGRenderImage *QSSGShaderMaterialAdapter::iblProbe()
  QSSGRenderImage *iblProbe() override {
    if (taken[23]) {
      int handled = 0;
      CuteQSSGShaderMaterialAdapterCall23 call = reinterpret_cast<CuteQSSGShaderMaterialAdapterCall23>(taken[23]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSSGRenderImage *>(given);
    }
    return {};
  }

  //  QVector3D QSSGShaderMaterialAdapter::emissiveColor()
  QVector3D emissiveColor() override {
    if (taken[24]) {
      int handled = 0;
      CuteQSSGShaderMaterialAdapterCall24 call = reinterpret_cast<CuteQSSGShaderMaterialAdapterCall24>(taken[24]);
      const QVector3D * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  QVector4D QSSGShaderMaterialAdapter::color()
  QVector4D color() override {
    if (taken[25]) {
      int handled = 0;
      CuteQSSGShaderMaterialAdapterCall25 call = reinterpret_cast<CuteQSSGShaderMaterialAdapterCall25>(taken[25]);
      const QVector4D * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  QVector3D QSSGShaderMaterialAdapter::specularTint()
  QVector3D specularTint() override {
    if (taken[26]) {
      int handled = 0;
      CuteQSSGShaderMaterialAdapterCall26 call = reinterpret_cast<CuteQSSGShaderMaterialAdapterCall26>(taken[26]);
      const QVector3D * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  float QSSGShaderMaterialAdapter::ior()
  float ior() override {
    if (taken[27]) {
      int handled = 0;
      CuteQSSGShaderMaterialAdapterCall27 call = reinterpret_cast<CuteQSSGShaderMaterialAdapterCall27>(taken[27]);
      float given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  float QSSGShaderMaterialAdapter::fresnelScale()
  float fresnelScale() override {
    if (taken[28]) {
      int handled = 0;
      CuteQSSGShaderMaterialAdapterCall28 call = reinterpret_cast<CuteQSSGShaderMaterialAdapterCall28>(taken[28]);
      float given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  float QSSGShaderMaterialAdapter::fresnelBias()
  float fresnelBias() override {
    if (taken[29]) {
      int handled = 0;
      CuteQSSGShaderMaterialAdapterCall29 call = reinterpret_cast<CuteQSSGShaderMaterialAdapterCall29>(taken[29]);
      float given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  float QSSGShaderMaterialAdapter::fresnelPower()
  float fresnelPower() override {
    if (taken[30]) {
      int handled = 0;
      CuteQSSGShaderMaterialAdapterCall30 call = reinterpret_cast<CuteQSSGShaderMaterialAdapterCall30>(taken[30]);
      float given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  float QSSGShaderMaterialAdapter::clearcoatFresnelScale()
  float clearcoatFresnelScale() override {
    if (taken[31]) {
      int handled = 0;
      CuteQSSGShaderMaterialAdapterCall31 call = reinterpret_cast<CuteQSSGShaderMaterialAdapterCall31>(taken[31]);
      float given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  float QSSGShaderMaterialAdapter::clearcoatFresnelBias()
  float clearcoatFresnelBias() override {
    if (taken[32]) {
      int handled = 0;
      CuteQSSGShaderMaterialAdapterCall32 call = reinterpret_cast<CuteQSSGShaderMaterialAdapterCall32>(taken[32]);
      float given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  float QSSGShaderMaterialAdapter::clearcoatFresnelPower()
  float clearcoatFresnelPower() override {
    if (taken[33]) {
      int handled = 0;
      CuteQSSGShaderMaterialAdapterCall33 call = reinterpret_cast<CuteQSSGShaderMaterialAdapterCall33>(taken[33]);
      float given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  float QSSGShaderMaterialAdapter::metalnessAmount()
  float metalnessAmount() override {
    if (taken[34]) {
      int handled = 0;
      CuteQSSGShaderMaterialAdapterCall34 call = reinterpret_cast<CuteQSSGShaderMaterialAdapterCall34>(taken[34]);
      float given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  float QSSGShaderMaterialAdapter::specularAmount()
  float specularAmount() override {
    if (taken[35]) {
      int handled = 0;
      CuteQSSGShaderMaterialAdapterCall35 call = reinterpret_cast<CuteQSSGShaderMaterialAdapterCall35>(taken[35]);
      float given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  float QSSGShaderMaterialAdapter::specularRoughness()
  float specularRoughness() override {
    if (taken[36]) {
      int handled = 0;
      CuteQSSGShaderMaterialAdapterCall36 call = reinterpret_cast<CuteQSSGShaderMaterialAdapterCall36>(taken[36]);
      float given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  float QSSGShaderMaterialAdapter::bumpAmount()
  float bumpAmount() override {
    if (taken[37]) {
      int handled = 0;
      CuteQSSGShaderMaterialAdapterCall37 call = reinterpret_cast<CuteQSSGShaderMaterialAdapterCall37>(taken[37]);
      float given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  float QSSGShaderMaterialAdapter::translucentFallOff()
  float translucentFallOff() override {
    if (taken[38]) {
      int handled = 0;
      CuteQSSGShaderMaterialAdapterCall38 call = reinterpret_cast<CuteQSSGShaderMaterialAdapterCall38>(taken[38]);
      float given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  float QSSGShaderMaterialAdapter::diffuseLightWrap()
  float diffuseLightWrap() override {
    if (taken[39]) {
      int handled = 0;
      CuteQSSGShaderMaterialAdapterCall39 call = reinterpret_cast<CuteQSSGShaderMaterialAdapterCall39>(taken[39]);
      float given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  float QSSGShaderMaterialAdapter::occlusionAmount()
  float occlusionAmount() override {
    if (taken[40]) {
      int handled = 0;
      CuteQSSGShaderMaterialAdapterCall40 call = reinterpret_cast<CuteQSSGShaderMaterialAdapterCall40>(taken[40]);
      float given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  float QSSGShaderMaterialAdapter::alphaCutOff()
  float alphaCutOff() override {
    if (taken[41]) {
      int handled = 0;
      CuteQSSGShaderMaterialAdapterCall41 call = reinterpret_cast<CuteQSSGShaderMaterialAdapterCall41>(taken[41]);
      float given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  float QSSGShaderMaterialAdapter::pointSize()
  float pointSize() override {
    if (taken[42]) {
      int handled = 0;
      CuteQSSGShaderMaterialAdapterCall42 call = reinterpret_cast<CuteQSSGShaderMaterialAdapterCall42>(taken[42]);
      float given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  float QSSGShaderMaterialAdapter::lineWidth()
  float lineWidth() override {
    if (taken[43]) {
      int handled = 0;
      CuteQSSGShaderMaterialAdapterCall43 call = reinterpret_cast<CuteQSSGShaderMaterialAdapterCall43>(taken[43]);
      float given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  float QSSGShaderMaterialAdapter::heightAmount()
  float heightAmount() override {
    if (taken[44]) {
      int handled = 0;
      CuteQSSGShaderMaterialAdapterCall44 call = reinterpret_cast<CuteQSSGShaderMaterialAdapterCall44>(taken[44]);
      float given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  float QSSGShaderMaterialAdapter::minHeightSamples()
  float minHeightSamples() override {
    if (taken[45]) {
      int handled = 0;
      CuteQSSGShaderMaterialAdapterCall45 call = reinterpret_cast<CuteQSSGShaderMaterialAdapterCall45>(taken[45]);
      float given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  float QSSGShaderMaterialAdapter::maxHeightSamples()
  float maxHeightSamples() override {
    if (taken[46]) {
      int handled = 0;
      CuteQSSGShaderMaterialAdapterCall46 call = reinterpret_cast<CuteQSSGShaderMaterialAdapterCall46>(taken[46]);
      float given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  float QSSGShaderMaterialAdapter::clearcoatAmount()
  float clearcoatAmount() override {
    if (taken[47]) {
      int handled = 0;
      CuteQSSGShaderMaterialAdapterCall47 call = reinterpret_cast<CuteQSSGShaderMaterialAdapterCall47>(taken[47]);
      float given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  float QSSGShaderMaterialAdapter::clearcoatRoughnessAmount()
  float clearcoatRoughnessAmount() override {
    if (taken[48]) {
      int handled = 0;
      CuteQSSGShaderMaterialAdapterCall48 call = reinterpret_cast<CuteQSSGShaderMaterialAdapterCall48>(taken[48]);
      float given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  float QSSGShaderMaterialAdapter::clearcoatNormalStrength()
  float clearcoatNormalStrength() override {
    if (taken[49]) {
      int handled = 0;
      CuteQSSGShaderMaterialAdapterCall49 call = reinterpret_cast<CuteQSSGShaderMaterialAdapterCall49>(taken[49]);
      float given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  float QSSGShaderMaterialAdapter::transmissionFactor()
  float transmissionFactor() override {
    if (taken[50]) {
      int handled = 0;
      CuteQSSGShaderMaterialAdapterCall50 call = reinterpret_cast<CuteQSSGShaderMaterialAdapterCall50>(taken[50]);
      float given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  float QSSGShaderMaterialAdapter::thicknessFactor()
  float thicknessFactor() override {
    if (taken[51]) {
      int handled = 0;
      CuteQSSGShaderMaterialAdapterCall51 call = reinterpret_cast<CuteQSSGShaderMaterialAdapterCall51>(taken[51]);
      float given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  float QSSGShaderMaterialAdapter::attenuationDistance()
  float attenuationDistance() override {
    if (taken[52]) {
      int handled = 0;
      CuteQSSGShaderMaterialAdapterCall52 call = reinterpret_cast<CuteQSSGShaderMaterialAdapterCall52>(taken[52]);
      float given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  QVector3D QSSGShaderMaterialAdapter::attenuationColor()
  QVector3D attenuationColor() override {
    if (taken[53]) {
      int handled = 0;
      CuteQSSGShaderMaterialAdapterCall53 call = reinterpret_cast<CuteQSSGShaderMaterialAdapterCall53>(taken[53]);
      const QVector3D * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  bool QSSGShaderMaterialAdapter::isUnshaded()
  bool isUnshaded() override {
    if (taken[54]) {
      int handled = 0;
      CuteQSSGShaderMaterialAdapterCall54 call = reinterpret_cast<CuteQSSGShaderMaterialAdapterCall54>(taken[54]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSSGShaderMaterialAdapter::isUnshaded();
  }

  //  bool QSSGShaderMaterialAdapter::hasCustomShaderSnippet(QSSGShaderCach
  //      e::ShaderType type)
  bool hasCustomShaderSnippet(QSSGShaderCache::ShaderType type) override {
    if (taken[55]) {
      int handled = 0;
      CuteQSSGShaderMaterialAdapterCall55 call = reinterpret_cast<CuteQSSGShaderMaterialAdapterCall55>(taken[55]);
      bool given = call(this, static_cast<int>(type), &handled);
      if (handled) return given;
    }
    return QSSGShaderMaterialAdapter::hasCustomShaderSnippet(type);
  }

  //  bool QSSGShaderMaterialAdapter::usesSharedVariables()
  bool usesSharedVariables() override {
    if (taken[56]) {
      int handled = 0;
      CuteQSSGShaderMaterialAdapterCall56 call = reinterpret_cast<CuteQSSGShaderMaterialAdapterCall56>(taken[56]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSSGShaderMaterialAdapter::usesSharedVariables();
  }
};

//  QSSGShaderMaterialAdapter::~QSSGShaderMaterialAdapter()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QSSGShaderMaterialAdapterD1Ev(
    QSSGShaderMaterialAdapter *self) {
  delete self;
}

//  bool QSSGShaderMaterialAdapter::isPrincipled()
extern "C" Q_DECL_EXPORT
bool ritual_ZN25QSSGShaderMaterialAdapter12isPrincipledEv(
    QSSGShaderMaterialAdapter *self) {
  return self->isPrincipled();
}

//  bool QSSGShaderMaterialAdapter::isSpecularGlossy()
extern "C" Q_DECL_EXPORT
bool ritual_ZN25QSSGShaderMaterialAdapter16isSpecularGlossyEv(
    QSSGShaderMaterialAdapter *self) {
  return self->isSpecularGlossy();
}

//  bool QSSGShaderMaterialAdapter::isMetalnessEnabled()
extern "C" Q_DECL_EXPORT
bool ritual_ZN25QSSGShaderMaterialAdapter18isMetalnessEnabledEv(
    QSSGShaderMaterialAdapter *self) {
  return self->isMetalnessEnabled();
}

//  bool QSSGShaderMaterialAdapter::isSpecularEnabled()
extern "C" Q_DECL_EXPORT
bool ritual_ZN25QSSGShaderMaterialAdapter17isSpecularEnabledEv(
    QSSGShaderMaterialAdapter *self) {
  return self->isSpecularEnabled();
}

//  bool QSSGShaderMaterialAdapter::isVertexColorsEnabled()
extern "C" Q_DECL_EXPORT
bool ritual_ZN25QSSGShaderMaterialAdapter21isVertexColorsEnabledEv(
    QSSGShaderMaterialAdapter *self) {
  return self->isVertexColorsEnabled();
}

//  bool QSSGShaderMaterialAdapter::isVertexColorsMaskEnabled()
extern "C" Q_DECL_EXPORT
bool ritual_ZN25QSSGShaderMaterialAdapter25isVertexColorsMaskEnabledEv(
    QSSGShaderMaterialAdapter *self) {
  return self->isVertexColorsMaskEnabled();
}

//  bool QSSGShaderMaterialAdapter::isInvertOpacityMapValue()
extern "C" Q_DECL_EXPORT
bool ritual_ZN25QSSGShaderMaterialAdapter23isInvertOpacityMapValueEv(
    QSSGShaderMaterialAdapter *self) {
  return self->isInvertOpacityMapValue();
}

//  bool QSSGShaderMaterialAdapter::isBaseColorSingleChannelEnabled()
extern "C" Q_DECL_EXPORT
bool ritual_ZN25QSSGShaderMaterialAdapter31isBaseColorSingleChannelEnabledEv(
    QSSGShaderMaterialAdapter *self) {
  return self->isBaseColorSingleChannelEnabled();
}

//  bool QSSGShaderMaterialAdapter::isSpecularAmountSingleChannelEnabled()
extern "C" Q_DECL_EXPORT
bool ritual_ZN25QSSGShaderMaterialAdapter36isSpecularAmountSingleChannelEnabledEv(
    QSSGShaderMaterialAdapter *self) {
  return self->isSpecularAmountSingleChannelEnabled();
}

//  bool QSSGShaderMaterialAdapter::isEmissiveSingleChannelEnabled()
extern "C" Q_DECL_EXPORT
bool ritual_ZN25QSSGShaderMaterialAdapter30isEmissiveSingleChannelEnabledEv(
    QSSGShaderMaterialAdapter *self) {
  return self->isEmissiveSingleChannelEnabled();
}

//  bool QSSGShaderMaterialAdapter::isFresnelScaleBiasEnabled()
extern "C" Q_DECL_EXPORT
bool ritual_ZN25QSSGShaderMaterialAdapter25isFresnelScaleBiasEnabledEv(
    QSSGShaderMaterialAdapter *self) {
  return self->isFresnelScaleBiasEnabled();
}

//  bool QSSGShaderMaterialAdapter::isClearcoatFresnelScaleBiasEnabled()
extern "C" Q_DECL_EXPORT
bool ritual_ZN25QSSGShaderMaterialAdapter34isClearcoatFresnelScaleBiasEnabledEv(
    QSSGShaderMaterialAdapter *self) {
  return self->isClearcoatFresnelScaleBiasEnabled();
}

//  bool QSSGShaderMaterialAdapter::isClearcoatEnabled()
extern "C" Q_DECL_EXPORT
bool ritual_ZN25QSSGShaderMaterialAdapter18isClearcoatEnabledEv(
    QSSGShaderMaterialAdapter *self) {
  return self->isClearcoatEnabled();
}

//  bool QSSGShaderMaterialAdapter::isTransmissionEnabled()
extern "C" Q_DECL_EXPORT
bool ritual_ZN25QSSGShaderMaterialAdapter21isTransmissionEnabledEv(
    QSSGShaderMaterialAdapter *self) {
  return self->isTransmissionEnabled();
}

//  bool QSSGShaderMaterialAdapter::hasLighting()
extern "C" Q_DECL_EXPORT
bool ritual_ZN25QSSGShaderMaterialAdapter11hasLightingEv(
    QSSGShaderMaterialAdapter *self) {
  return self->hasLighting();
}

//  bool QSSGShaderMaterialAdapter::usesCustomSkinning()
extern "C" Q_DECL_EXPORT
bool ritual_ZN25QSSGShaderMaterialAdapter18usesCustomSkinningEv(
    QSSGShaderMaterialAdapter *self) {
  return self->usesCustomSkinning();
}

//  bool QSSGShaderMaterialAdapter::usesCustomMorphing()
extern "C" Q_DECL_EXPORT
bool ritual_ZN25QSSGShaderMaterialAdapter18usesCustomMorphingEv(
    QSSGShaderMaterialAdapter *self) {
  return self->usesCustomMorphing();
}

//  QSSGRenderDefaultMaterial::MaterialSpecularModel
//      QSSGShaderMaterialAdapter::specularModel()
extern "C" Q_DECL_EXPORT
QSSGRenderDefaultMaterial::MaterialSpecularModel ritual_ZN25QSSGShaderMaterialAdapter13specularModelEv(
    QSSGShaderMaterialAdapter *self) {
  return self->specularModel();
}

//  QSSGRenderDefaultMaterial::MaterialAlphaMode
//      QSSGShaderMaterialAdapter::alphaMode()
extern "C" Q_DECL_EXPORT
QSSGRenderDefaultMaterial::MaterialAlphaMode ritual_ZN25QSSGShaderMaterialAdapter9alphaModeEv(
    QSSGShaderMaterialAdapter *self) {
  return self->alphaMode();
}

//  QSSGRenderDefaultMaterial::VertexColorMaskFlags
//      QSSGShaderMaterialAdapter::vertexColorRedMask()
extern "C" Q_DECL_EXPORT
int ritual_ZN25QSSGShaderMaterialAdapter18vertexColorRedMaskEv(
    QSSGShaderMaterialAdapter *self) {
  return static_cast<int>(self->vertexColorRedMask().toInt());
}

//  QSSGRenderDefaultMaterial::VertexColorMaskFlags
//      QSSGShaderMaterialAdapter::vertexColorGreenMask()
extern "C" Q_DECL_EXPORT
int ritual_ZN25QSSGShaderMaterialAdapter20vertexColorGreenMaskEv(
    QSSGShaderMaterialAdapter *self) {
  return static_cast<int>(self->vertexColorGreenMask().toInt());
}

//  QSSGRenderDefaultMaterial::VertexColorMaskFlags
//      QSSGShaderMaterialAdapter::vertexColorBlueMask()
extern "C" Q_DECL_EXPORT
int ritual_ZN25QSSGShaderMaterialAdapter19vertexColorBlueMaskEv(
    QSSGShaderMaterialAdapter *self) {
  return static_cast<int>(self->vertexColorBlueMask().toInt());
}

//  QSSGRenderDefaultMaterial::VertexColorMaskFlags
//      QSSGShaderMaterialAdapter::vertexColorAlphaMask()
extern "C" Q_DECL_EXPORT
int ritual_ZN25QSSGShaderMaterialAdapter20vertexColorAlphaMaskEv(
    QSSGShaderMaterialAdapter *self) {
  return static_cast<int>(self->vertexColorAlphaMask().toInt());
}

//  QSSGRenderImage *QSSGShaderMaterialAdapter::iblProbe()
extern "C" Q_DECL_EXPORT
QSSGRenderImage *ritual_ZN25QSSGShaderMaterialAdapter8iblProbeEv(
    QSSGShaderMaterialAdapter *self) {
  return self->iblProbe();
}

//  QVector3D QSSGShaderMaterialAdapter::emissiveColor()
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZN25QSSGShaderMaterialAdapter13emissiveColorEv(
    QSSGShaderMaterialAdapter *self) {
  return new QVector3D(self->emissiveColor());
}

//  QVector4D QSSGShaderMaterialAdapter::color()
extern "C" Q_DECL_EXPORT
QVector4D *ritual_ZN25QSSGShaderMaterialAdapter5colorEv(
    QSSGShaderMaterialAdapter *self) {
  return new QVector4D(self->color());
}

//  QVector3D QSSGShaderMaterialAdapter::specularTint()
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZN25QSSGShaderMaterialAdapter12specularTintEv(
    QSSGShaderMaterialAdapter *self) {
  return new QVector3D(self->specularTint());
}

//  float QSSGShaderMaterialAdapter::ior()
extern "C" Q_DECL_EXPORT
float ritual_ZN25QSSGShaderMaterialAdapter3iorEv(
    QSSGShaderMaterialAdapter *self) {
  return self->ior();
}

//  float QSSGShaderMaterialAdapter::fresnelScale()
extern "C" Q_DECL_EXPORT
float ritual_ZN25QSSGShaderMaterialAdapter12fresnelScaleEv(
    QSSGShaderMaterialAdapter *self) {
  return self->fresnelScale();
}

//  float QSSGShaderMaterialAdapter::fresnelBias()
extern "C" Q_DECL_EXPORT
float ritual_ZN25QSSGShaderMaterialAdapter11fresnelBiasEv(
    QSSGShaderMaterialAdapter *self) {
  return self->fresnelBias();
}

//  float QSSGShaderMaterialAdapter::fresnelPower()
extern "C" Q_DECL_EXPORT
float ritual_ZN25QSSGShaderMaterialAdapter12fresnelPowerEv(
    QSSGShaderMaterialAdapter *self) {
  return self->fresnelPower();
}

//  float QSSGShaderMaterialAdapter::clearcoatFresnelScale()
extern "C" Q_DECL_EXPORT
float ritual_ZN25QSSGShaderMaterialAdapter21clearcoatFresnelScaleEv(
    QSSGShaderMaterialAdapter *self) {
  return self->clearcoatFresnelScale();
}

//  float QSSGShaderMaterialAdapter::clearcoatFresnelBias()
extern "C" Q_DECL_EXPORT
float ritual_ZN25QSSGShaderMaterialAdapter20clearcoatFresnelBiasEv(
    QSSGShaderMaterialAdapter *self) {
  return self->clearcoatFresnelBias();
}

//  float QSSGShaderMaterialAdapter::clearcoatFresnelPower()
extern "C" Q_DECL_EXPORT
float ritual_ZN25QSSGShaderMaterialAdapter21clearcoatFresnelPowerEv(
    QSSGShaderMaterialAdapter *self) {
  return self->clearcoatFresnelPower();
}

//  float QSSGShaderMaterialAdapter::metalnessAmount()
extern "C" Q_DECL_EXPORT
float ritual_ZN25QSSGShaderMaterialAdapter15metalnessAmountEv(
    QSSGShaderMaterialAdapter *self) {
  return self->metalnessAmount();
}

//  float QSSGShaderMaterialAdapter::specularAmount()
extern "C" Q_DECL_EXPORT
float ritual_ZN25QSSGShaderMaterialAdapter14specularAmountEv(
    QSSGShaderMaterialAdapter *self) {
  return self->specularAmount();
}

//  float QSSGShaderMaterialAdapter::specularRoughness()
extern "C" Q_DECL_EXPORT
float ritual_ZN25QSSGShaderMaterialAdapter17specularRoughnessEv(
    QSSGShaderMaterialAdapter *self) {
  return self->specularRoughness();
}

//  float QSSGShaderMaterialAdapter::bumpAmount()
extern "C" Q_DECL_EXPORT
float ritual_ZN25QSSGShaderMaterialAdapter10bumpAmountEv(
    QSSGShaderMaterialAdapter *self) {
  return self->bumpAmount();
}

//  float QSSGShaderMaterialAdapter::translucentFallOff()
extern "C" Q_DECL_EXPORT
float ritual_ZN25QSSGShaderMaterialAdapter18translucentFallOffEv(
    QSSGShaderMaterialAdapter *self) {
  return self->translucentFallOff();
}

//  float QSSGShaderMaterialAdapter::diffuseLightWrap()
extern "C" Q_DECL_EXPORT
float ritual_ZN25QSSGShaderMaterialAdapter16diffuseLightWrapEv(
    QSSGShaderMaterialAdapter *self) {
  return self->diffuseLightWrap();
}

//  float QSSGShaderMaterialAdapter::occlusionAmount()
extern "C" Q_DECL_EXPORT
float ritual_ZN25QSSGShaderMaterialAdapter15occlusionAmountEv(
    QSSGShaderMaterialAdapter *self) {
  return self->occlusionAmount();
}

//  float QSSGShaderMaterialAdapter::alphaCutOff()
extern "C" Q_DECL_EXPORT
float ritual_ZN25QSSGShaderMaterialAdapter11alphaCutOffEv(
    QSSGShaderMaterialAdapter *self) {
  return self->alphaCutOff();
}

//  float QSSGShaderMaterialAdapter::pointSize()
extern "C" Q_DECL_EXPORT
float ritual_ZN25QSSGShaderMaterialAdapter9pointSizeEv(
    QSSGShaderMaterialAdapter *self) {
  return self->pointSize();
}

//  float QSSGShaderMaterialAdapter::lineWidth()
extern "C" Q_DECL_EXPORT
float ritual_ZN25QSSGShaderMaterialAdapter9lineWidthEv(
    QSSGShaderMaterialAdapter *self) {
  return self->lineWidth();
}

//  float QSSGShaderMaterialAdapter::heightAmount()
extern "C" Q_DECL_EXPORT
float ritual_ZN25QSSGShaderMaterialAdapter12heightAmountEv(
    QSSGShaderMaterialAdapter *self) {
  return self->heightAmount();
}

//  float QSSGShaderMaterialAdapter::minHeightSamples()
extern "C" Q_DECL_EXPORT
float ritual_ZN25QSSGShaderMaterialAdapter16minHeightSamplesEv(
    QSSGShaderMaterialAdapter *self) {
  return self->minHeightSamples();
}

//  float QSSGShaderMaterialAdapter::maxHeightSamples()
extern "C" Q_DECL_EXPORT
float ritual_ZN25QSSGShaderMaterialAdapter16maxHeightSamplesEv(
    QSSGShaderMaterialAdapter *self) {
  return self->maxHeightSamples();
}

//  float QSSGShaderMaterialAdapter::clearcoatAmount()
extern "C" Q_DECL_EXPORT
float ritual_ZN25QSSGShaderMaterialAdapter15clearcoatAmountEv(
    QSSGShaderMaterialAdapter *self) {
  return self->clearcoatAmount();
}

//  float QSSGShaderMaterialAdapter::clearcoatRoughnessAmount()
extern "C" Q_DECL_EXPORT
float ritual_ZN25QSSGShaderMaterialAdapter24clearcoatRoughnessAmountEv(
    QSSGShaderMaterialAdapter *self) {
  return self->clearcoatRoughnessAmount();
}

//  float QSSGShaderMaterialAdapter::clearcoatNormalStrength()
extern "C" Q_DECL_EXPORT
float ritual_ZN25QSSGShaderMaterialAdapter23clearcoatNormalStrengthEv(
    QSSGShaderMaterialAdapter *self) {
  return self->clearcoatNormalStrength();
}

//  float QSSGShaderMaterialAdapter::transmissionFactor()
extern "C" Q_DECL_EXPORT
float ritual_ZN25QSSGShaderMaterialAdapter18transmissionFactorEv(
    QSSGShaderMaterialAdapter *self) {
  return self->transmissionFactor();
}

//  float QSSGShaderMaterialAdapter::thicknessFactor()
extern "C" Q_DECL_EXPORT
float ritual_ZN25QSSGShaderMaterialAdapter15thicknessFactorEv(
    QSSGShaderMaterialAdapter *self) {
  return self->thicknessFactor();
}

//  float QSSGShaderMaterialAdapter::attenuationDistance()
extern "C" Q_DECL_EXPORT
float ritual_ZN25QSSGShaderMaterialAdapter19attenuationDistanceEv(
    QSSGShaderMaterialAdapter *self) {
  return self->attenuationDistance();
}

//  QVector3D QSSGShaderMaterialAdapter::attenuationColor()
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZN25QSSGShaderMaterialAdapter16attenuationColorEv(
    QSSGShaderMaterialAdapter *self) {
  return new QVector3D(self->attenuationColor());
}

//  bool QSSGShaderMaterialAdapter::isUnshaded()
extern "C" Q_DECL_EXPORT
bool ritual_ZN25QSSGShaderMaterialAdapter10isUnshadedEv(
    QSSGShaderMaterialAdapter *self) {
  return self->isUnshaded();
}

//  bool QSSGShaderMaterialAdapter::hasCustomShaderSnippet(QSSGShaderCache::S
//      haderType type)
extern "C" Q_DECL_EXPORT
bool ritual_ZN25QSSGShaderMaterialAdapter22hasCustomShaderSnippetEN15QSSGShaderCache10ShaderTypeE(
    QSSGShaderMaterialAdapter *self,
    QSSGShaderCache::ShaderType type) {
  return self->hasCustomShaderSnippet(type);
}

//  bool QSSGShaderMaterialAdapter::usesSharedVariables()
extern "C" Q_DECL_EXPORT
bool ritual_ZN25QSSGShaderMaterialAdapter19usesSharedVariablesEv(
    QSSGShaderMaterialAdapter *self) {
  return self->usesSharedVariables();
}

//  a Python function taken by a CuteQSSGShaderMaterialAdapter, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSSGShaderMaterialAdapter(
    QSSGShaderMaterialAdapter *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSSGShaderMaterialAdapter *>(self)->take(key, call);
}

//  bool QSSGShaderMaterialAdapter::isUnshaded()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN25QSSGShaderMaterialAdapter10isUnshadedEv(
    QSSGShaderMaterialAdapter *self) {
  return self->QSSGShaderMaterialAdapter::isUnshaded();
}

//  bool QSSGShaderMaterialAdapter::hasCustomShaderSnippet(QSSGShaderCache::S
//      haderType type)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN25QSSGShaderMaterialAdapter22hasCustomShaderSnippetEN15QSSGShaderCache10ShaderTypeE(
    QSSGShaderMaterialAdapter *self,
    QSSGShaderCache::ShaderType type) {
  return self->QSSGShaderMaterialAdapter::hasCustomShaderSnippet(type);
}

//  bool QSSGShaderMaterialAdapter::usesSharedVariables()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN25QSSGShaderMaterialAdapter19usesSharedVariablesEv(
    QSSGShaderMaterialAdapter *self) {
  return self->QSSGShaderMaterialAdapter::usesSharedVariables();
}
