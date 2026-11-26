//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderskymaterial_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderskymaterial_p.h>
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendershadercache_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qmatrix4x4.h>
#include <QtCore/qbytearray.h>
#include <QtGui/QMatrix4x4>
#include <QtCore/QVarLengthArray>
#include <QtCore/QByteArray>

//  QSSGRenderSkyMaterial::QSSGRenderSkyMaterial()
extern "C" Q_DECL_EXPORT
QSSGRenderSkyMaterial *ritual_ZN21QSSGRenderSkyMaterialC1Ev() {
  return new QSSGRenderSkyMaterial();
}

//  QSSGRenderSkyMaterial::~QSSGRenderSkyMaterial()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSSGRenderSkyMaterialD1Ev(QSSGRenderSkyMaterial *self) {
  delete self;
}

//  QSSGRhiShaderPipelinePtr QSSGRenderSkyMaterial::ensurePipeline(const
//      QSSGRenderContextInterface &sgContext)
extern "C" Q_DECL_EXPORT
QSSGRhiShaderPipelinePtr *ritual_ZN21QSSGRenderSkyMaterial14ensurePipelineERK26QSSGRenderContextInterface(
    QSSGRenderSkyMaterial *self,
    const QSSGRenderContextInterface *sgContext) {
  return new QSSGRhiShaderPipelinePtr(self->ensurePipeline(*sgContext));
}

//  QSSGRhiShaderPipelinePtr
//      QSSGRenderSkyMaterial::ensureBackgroundPipeline(const
//      QSSGRenderContextInterface &sgContext, const QSSGShaderFeatures
//      &tonemapFeatures, quint32 tonemapKey, int viewCount)
extern "C" Q_DECL_EXPORT
QSSGRhiShaderPipelinePtr *ritual_ZN21QSSGRenderSkyMaterial24ensureBackgroundPipelineERK26QSSGRenderContextInterfaceRK18QSSGShaderFeaturesji(
    QSSGRenderSkyMaterial *self,
    const QSSGRenderContextInterface *sgContext,
    const QSSGShaderFeatures *tonemapFeatures,
    quint32 tonemapKey,
    int viewCount) {
  return new QSSGRhiShaderPipelinePtr(
      self->ensureBackgroundPipeline(
          *sgContext,
          *tonemapFeatures,
          tonemapKey,
          viewCount));
}

//  quint32 QSSGRenderSkyMaterial::updateUniforms(const
//      QSSGRenderContextInterface &sgContext, const QMatrix4x4 &mvp, const
//      QVarLengthArray<QMatrix4x4, 6> views)
extern "C" Q_DECL_EXPORT
quint32 ritual_ZN21QSSGRenderSkyMaterial14updateUniformsERK26QSSGRenderContextInterfaceRK10QMatrix4x415QVarLengthArrayIS3_Lx6EE(
    QSSGRenderSkyMaterial *self,
    const QSSGRenderContextInterface *sgContext,
    const QMatrix4x4 *mvp,
    const QVarLengthArray<QMatrix4x4, 6> *views) {
  return self->updateUniforms(*sgContext, *mvp, *views);
}

//  void QSSGRenderSkyMaterial::updateBackgroundUniforms(const
//      QSSGRenderContextInterface &sgContext, const
//      QVarLengthArray<QMatrix4x4, 2> &inverseProjections, const
//      QVarLengthArray<QMatrix4x4, 2> &viewRotations, float adjustY, float
//      exposure)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSSGRenderSkyMaterial24updateBackgroundUniformsERK26QSSGRenderContextInterfaceRK15QVarLengthArrayI10QMatrix4x4Lx2EES7_ff(
    QSSGRenderSkyMaterial *self,
    const QSSGRenderContextInterface *sgContext,
    const QVarLengthArray<QMatrix4x4, 2> *inverseProjections,
    const QVarLengthArray<QMatrix4x4, 2> *viewRotations,
    float adjustY,
    float exposure) {
  self->updateBackgroundUniforms(
      *sgContext,
      *inverseProjections,
      *viewRotations,
      adjustY,
      exposure);
}

//  QSSGRhiShaderPipelinePtr QSSGRenderSkyMaterial::buildPipeline(const
//      QSSGRenderContextInterface &sgContext, QByteArray vertexShader, const
//      QSSGShaderCustomMaterialAdapter::StringPairList
//      &vertexViewDependentUniforms, const
//      QSSGShaderCustomMaterialAdapter::StringPairList &vertexUniforms,
//      const QByteArray &fragmentMainSnippet, const
//      QSSGShaderCustomMaterialAdapter::StringPairList &fragmentUniforms,
//      const QSSGShaderFeatures &features, int viewCount, const QByteArray
//      &cacheKeyTag)
extern "C" Q_DECL_EXPORT
QSSGRhiShaderPipelinePtr *ritual_ZN21QSSGRenderSkyMaterial13buildPipelineERK26QSSGRenderContextInterface10QByteArrayRK15QVarLengthArrayISt4pairIS3_S3_ELx16EES9_RKS3_S9_RK18QSSGShaderFeaturesiSB_(
    QSSGRenderSkyMaterial *self,
    const QSSGRenderContextInterface *sgContext,
    const QByteArray *vertexShader,
    const QSSGShaderCustomMaterialAdapter::StringPairList *vertexViewDependentUniforms,
    const QSSGShaderCustomMaterialAdapter::StringPairList *vertexUniforms,
    const QByteArray *fragmentMainSnippet,
    const QSSGShaderCustomMaterialAdapter::StringPairList *fragmentUniforms,
    const QSSGShaderFeatures *features,
    int viewCount,
    const QByteArray *cacheKeyTag) {
  return new QSSGRhiShaderPipelinePtr(
      self->buildPipeline(
          *sgContext,
          *vertexShader,
          *vertexViewDependentUniforms,
          *vertexUniforms,
          *fragmentMainSnippet,
          *fragmentUniforms,
          *features,
          viewCount,
          *cacheKeyTag));
}

//  a QSSGRhiShaderPipelinePtr a ritual of QSSGRenderSkyMaterial gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QSSGRenderSkyMaterial__QSSGRhiShaderPipelinePtr(
    QSSGRhiShaderPipelinePtr *self) {
  delete self;
}
