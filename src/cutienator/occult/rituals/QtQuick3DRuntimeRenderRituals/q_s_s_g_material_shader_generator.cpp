//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderdefaultmaterials
//  hadergenerator_p.h, Qt 6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderdefaultmaterialshadergenerator_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendershaderkeys_p.h>
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendershadercache_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qmatrix4x4.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderableobjects_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/QByteArray>

//  QSSGMaterialShaderGenerator::~QSSGMaterialShaderGenerator()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QSSGMaterialShaderGeneratorD1Ev(
    QSSGMaterialShaderGenerator *self) {
  delete self;
}

//  const char
//      *QSSGMaterialShaderGenerator::getSamplerName(QSSGRenderableImage::Typ
//      e type)
extern "C" Q_DECL_EXPORT
const char *ritual_ZN27QSSGMaterialShaderGenerator14getSamplerNameEN19QSSGRenderableImage4TypeE(
    QSSGRenderableImage::Type type) {
  return QSSGMaterialShaderGenerator::getSamplerName(type);
}

//  QSSGRhiShaderPipelinePtr
//      QSSGMaterialShaderGenerator::generateMaterialRhiShader(const
//      QByteArray &inShaderKeyPrefix, QSSGMaterialVertexPipeline
//      &vertexGenerator, const QSSGShaderDefaultMaterialKey &key, const
//      QSSGShaderDefaultMaterialKeyProperties &inProperties, const
//      QSSGShaderFeatures &inFeatureSet, const QSSGRenderGraphObject
//      &inMaterial, QSSGShaderLibraryManager &shaderLibraryManager,
//      QSSGShaderCache &theCache, const QSSGUserShaderAugmentation
//      &shaderAugmentation)
extern "C" Q_DECL_EXPORT
QSSGRhiShaderPipelinePtr *ritual_ZN27QSSGMaterialShaderGenerator25generateMaterialRhiShaderERK10QByteArrayR26QSSGMaterialVertexPipelineRK25QSSGShaderBaseMaterialKeyI38QSSGShaderDefaultMaterialKeyPropertiesLm25EERKS6_RK18QSSGShaderFeaturesRK21QSSGRenderGraphObjectR24QSSGShaderLibraryManagerR15QSSGShaderCacheRK26QSSGUserShaderAugmentation(
    const QByteArray *inShaderKeyPrefix,
    QSSGMaterialVertexPipeline *vertexGenerator,
    const QSSGShaderDefaultMaterialKey *key,
    const QSSGShaderDefaultMaterialKeyProperties *inProperties,
    const QSSGShaderFeatures *inFeatureSet,
    const QSSGRenderGraphObject *inMaterial,
    QSSGShaderLibraryManager *shaderLibraryManager,
    QSSGShaderCache *theCache,
    const QSSGUserShaderAugmentation *shaderAugmentation) {
  return new QSSGRhiShaderPipelinePtr(
      QSSGMaterialShaderGenerator::generateMaterialRhiShader(
          *inShaderKeyPrefix,
          *vertexGenerator,
          *key,
          *inProperties,
          *inFeatureSet,
          *inMaterial,
          *shaderLibraryManager,
          *theCache,
          *shaderAugmentation));
}

//  void QSSGMaterialShaderGenerator::setRhiMaterialProperties(const
//      QSSGRenderContextInterface &a0, QSSGRhiShaderPipeline &shaders, char
//      *ubufData, QSSGRhiGraphicsPipelineState *inPipelineState, const
//      QSSGRenderGraphObject &inMaterial, const QSSGShaderDefaultMaterialKey
//      &inKey, const QSSGShaderDefaultMaterialKeyProperties &inProperties,
//      const QSSGRenderCameraList &inCameras, const QSSGRenderMvpArray
//      &inModelViewProjections, const QMatrix3x3 &inNormalMatrix, const
//      QMatrix4x4 &inGlobalTransform, const QMatrix4x4 &clipSpaceCorrMatrix,
//      const QMatrix4x4 &localInstanceTransform, const QMatrix4x4
//      &globalInstanceTransform, const QSSGDataView<float> &inMorphWeights,
//      QSSGRenderableImage *inFirstImage, float inOpacity, const
//      QSSGLayerRenderData &inRenderProperties, const
//      QSSGShaderLightListView &inLights, const QSSGShaderReflectionProbe
//      &reflectionProbe, bool receivesShadows, bool receivesReflections,
//      const QVector2D *shadowDepthAdjust, QRhiTexture *lightmapTexture)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QSSGMaterialShaderGenerator24setRhiMaterialPropertiesERK26QSSGRenderContextInterfaceR21QSSGRhiShaderPipelinePcP28QSSGRhiGraphicsPipelineStateRK21QSSGRenderGraphObjectRK25QSSGShaderBaseMaterialKeyI38QSSGShaderDefaultMaterialKeyPropertiesLm25EERKSC_RK15QVarLengthArrayIP16QSSGRenderCameraLx2EERKSt5arrayI10QMatrix4x4Lm2EERK14QGenericMatrixILi3ELi3EfERKSP_SY_SY_SY_RK12QSSGDataViewIfEP19QSSGRenderableImagefRK19QSSGLayerRenderDataRKSZ_I15QSSGShaderLightERK25QSSGShaderReflectionProbebbPK9QVector2DP11QRhiTexture(
    const QSSGRenderContextInterface *a0,
    QSSGRhiShaderPipeline *shaders,
    char *ubufData,
    QSSGRhiGraphicsPipelineState *inPipelineState,
    const QSSGRenderGraphObject *inMaterial,
    const QSSGShaderDefaultMaterialKey *inKey,
    const QSSGShaderDefaultMaterialKeyProperties *inProperties,
    const QSSGRenderCameraList *inCameras,
    const QSSGRenderMvpArray *inModelViewProjections,
    const QMatrix3x3 *inNormalMatrix,
    const QMatrix4x4 *inGlobalTransform,
    const QMatrix4x4 *clipSpaceCorrMatrix,
    const QMatrix4x4 *localInstanceTransform,
    const QMatrix4x4 *globalInstanceTransform,
    const QSSGDataView<float> *inMorphWeights,
    QSSGRenderableImage *inFirstImage,
    float inOpacity,
    const QSSGLayerRenderData *inRenderProperties,
    const QSSGShaderLightListView *inLights,
    const QSSGShaderReflectionProbe *reflectionProbe,
    bool receivesShadows,
    bool receivesReflections,
    const QVector2D *shadowDepthAdjust,
    QRhiTexture *lightmapTexture) {
  QSSGMaterialShaderGenerator::setRhiMaterialProperties(
      *a0,
      *shaders,
      ubufData,
      inPipelineState,
      *inMaterial,
      *inKey,
      *inProperties,
      *inCameras,
      *inModelViewProjections,
      *inNormalMatrix,
      *inGlobalTransform,
      *clipSpaceCorrMatrix,
      *localInstanceTransform,
      *globalInstanceTransform,
      *inMorphWeights,
      inFirstImage,
      inOpacity,
      *inRenderProperties,
      *inLights,
      *reflectionProbe,
      receivesShadows,
      receivesReflections,
      shadowDepthAdjust,
      lightmapTexture);
}

//  const char
//      *QSSGMaterialShaderGenerator::directionalLightProcessorArgumentList()
extern "C" Q_DECL_EXPORT
const char *ritual_ZN27QSSGMaterialShaderGenerator37directionalLightProcessorArgumentListEv() {
  return QSSGMaterialShaderGenerator::directionalLightProcessorArgumentList();
}

//  const char
//      *QSSGMaterialShaderGenerator::pointLightProcessorArgumentList()
extern "C" Q_DECL_EXPORT
const char *ritual_ZN27QSSGMaterialShaderGenerator31pointLightProcessorArgumentListEv() {
  return QSSGMaterialShaderGenerator::pointLightProcessorArgumentList();
}

//  const char *QSSGMaterialShaderGenerator::spotLightProcessorArgumentList()
extern "C" Q_DECL_EXPORT
const char *ritual_ZN27QSSGMaterialShaderGenerator30spotLightProcessorArgumentListEv() {
  return QSSGMaterialShaderGenerator::spotLightProcessorArgumentList();
}

//  const char
//      *QSSGMaterialShaderGenerator::ambientLightProcessorArgumentList()
extern "C" Q_DECL_EXPORT
const char *ritual_ZN27QSSGMaterialShaderGenerator33ambientLightProcessorArgumentListEv() {
  return QSSGMaterialShaderGenerator::ambientLightProcessorArgumentList();
}

//  const char
//      *QSSGMaterialShaderGenerator::specularLightProcessorArgumentList()
extern "C" Q_DECL_EXPORT
const char *ritual_ZN27QSSGMaterialShaderGenerator34specularLightProcessorArgumentListEv() {
  return QSSGMaterialShaderGenerator::specularLightProcessorArgumentList();
}

//  const char *QSSGMaterialShaderGenerator::shadedFragmentMainArgumentList()
extern "C" Q_DECL_EXPORT
const char *ritual_ZN27QSSGMaterialShaderGenerator30shadedFragmentMainArgumentListEv() {
  return QSSGMaterialShaderGenerator::shadedFragmentMainArgumentList();
}

//  const char *QSSGMaterialShaderGenerator::postProcessorArgumentList()
extern "C" Q_DECL_EXPORT
const char *ritual_ZN27QSSGMaterialShaderGenerator25postProcessorArgumentListEv() {
  return QSSGMaterialShaderGenerator::postProcessorArgumentList();
}

//  const char *QSSGMaterialShaderGenerator::iblProbeProcessorArgumentList()
extern "C" Q_DECL_EXPORT
const char *ritual_ZN27QSSGMaterialShaderGenerator29iblProbeProcessorArgumentListEv() {
  return QSSGMaterialShaderGenerator::iblProbeProcessorArgumentList();
}

//  const char *QSSGMaterialShaderGenerator::vertexMainArgumentList()
extern "C" Q_DECL_EXPORT
const char *ritual_ZN27QSSGMaterialShaderGenerator22vertexMainArgumentListEv() {
  return QSSGMaterialShaderGenerator::vertexMainArgumentList();
}

//  const char
//      *QSSGMaterialShaderGenerator::vertexInstancedMainArgumentList()
extern "C" Q_DECL_EXPORT
const char *ritual_ZN27QSSGMaterialShaderGenerator31vertexInstancedMainArgumentListEv() {
  return QSSGMaterialShaderGenerator::vertexInstancedMainArgumentList();
}

//  a QSSGRhiShaderPipelinePtr a ritual of QSSGMaterialShaderGenerator gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QSSGMaterialShaderGenerator__QSSGRhiShaderPipelinePtr(
    QSSGRhiShaderPipelinePtr *self) {
  delete self;
}
