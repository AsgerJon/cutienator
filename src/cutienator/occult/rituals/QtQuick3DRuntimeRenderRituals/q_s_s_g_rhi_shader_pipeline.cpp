//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrhicontext_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrhicontext_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/rhi/qrhi.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>

//  bool QSSGRhiShaderPipeline::isNull() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QSSGRhiShaderPipeline6isNullEv(
    const QSSGRhiShaderPipeline *self) {
  return self->isNull();
}

//  void QSSGRhiShaderPipeline::addStage(const QRhiShaderStage &stage,
//      StageFlags flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSSGRhiShaderPipeline8addStageERK15QRhiShaderStage6QFlagsINS_9StageFlagEE(
    QSSGRhiShaderPipeline *self,
    const QRhiShaderStage *stage,
    int flags) {
  self->addStage(
      *stage,
      QFlags<QSSGRhiShaderPipeline::StageFlag>::fromInt(flags));
}

//  const QRhiShaderStage *QSSGRhiShaderPipeline::cbeginStages() const
extern "C" Q_DECL_EXPORT
const QRhiShaderStage *ritual_ZNK21QSSGRhiShaderPipeline12cbeginStagesEv(
    const QSSGRhiShaderPipeline *self) {
  return self->cbeginStages();
}

//  const QRhiShaderStage *QSSGRhiShaderPipeline::cendStages() const
extern "C" Q_DECL_EXPORT
const QRhiShaderStage *ritual_ZNK21QSSGRhiShaderPipeline10cendStagesEv(
    const QSSGRhiShaderPipeline *self) {
  return self->cendStages();
}

//  const QRhiShaderStage *QSSGRhiShaderPipeline::vertexStage() const
extern "C" Q_DECL_EXPORT
const QRhiShaderStage *ritual_ZNK21QSSGRhiShaderPipeline11vertexStageEv(
    const QSSGRhiShaderPipeline *self) {
  return self->vertexStage();
}

//  const QRhiShaderStage *QSSGRhiShaderPipeline::fragmentStage() const
extern "C" Q_DECL_EXPORT
const QRhiShaderStage *ritual_ZNK21QSSGRhiShaderPipeline13fragmentStageEv(
    const QSSGRhiShaderPipeline *self) {
  return self->fragmentStage();
}

//  int QSSGRhiShaderPipeline::ub0Size() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QSSGRhiShaderPipeline7ub0SizeEv(
    const QSSGRhiShaderPipeline *self) {
  return self->ub0Size();
}

//  int QSSGRhiShaderPipeline::ub0LightDataOffset() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QSSGRhiShaderPipeline18ub0LightDataOffsetEv(
    const QSSGRhiShaderPipeline *self) {
  return self->ub0LightDataOffset();
}

//  int QSSGRhiShaderPipeline::ub0DirectionalLightDataOffset() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QSSGRhiShaderPipeline29ub0DirectionalLightDataOffsetEv(
    const QSSGRhiShaderPipeline *self) {
  return self->ub0DirectionalLightDataOffset();
}

//  int QSSGRhiShaderPipeline::bindingForTexture(const char *name, int hint)
extern "C" Q_DECL_EXPORT
int ritual_ZN21QSSGRhiShaderPipeline17bindingForTextureEPKci(
    QSSGRhiShaderPipeline *self,
    const char *name,
    int hint) {
  return self->bindingForTexture(name, hint);
}

//  int QSSGRhiShaderPipeline::bindingForImage(const char *name)
extern "C" Q_DECL_EXPORT
int ritual_ZN21QSSGRhiShaderPipeline15bindingForImageEPKc(
    QSSGRhiShaderPipeline *self,
    const char *name) {
  return self->bindingForImage(name);
}

//  void QSSGRhiShaderPipeline::setLightsEnabled(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSSGRhiShaderPipeline16setLightsEnabledEb(
    QSSGRhiShaderPipeline *self,
    bool enable) {
  self->setLightsEnabled(enable);
}

//  bool QSSGRhiShaderPipeline::isLightingEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QSSGRhiShaderPipeline17isLightingEnabledEv(
    const QSSGRhiShaderPipeline *self) {
  return self->isLightingEnabled();
}

//  void QSSGRhiShaderPipeline::setLightProbeTexture(QRhiTexture *texture,
//      QSSGRenderTextureCoordOp hTile, QSSGRenderTextureCoordOp vTile)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSSGRhiShaderPipeline20setLightProbeTextureEP11QRhiTexture24QSSGRenderTextureCoordOpS2_(
    QSSGRhiShaderPipeline *self,
    QRhiTexture *texture,
    QSSGRenderTextureCoordOp hTile,
    QSSGRenderTextureCoordOp vTile) {
  self->setLightProbeTexture(texture, hTile, vTile);
}

//  QRhiTexture *QSSGRhiShaderPipeline::lightProbeTexture() const
extern "C" Q_DECL_EXPORT
QRhiTexture *ritual_ZNK21QSSGRhiShaderPipeline17lightProbeTextureEv(
    const QSSGRhiShaderPipeline *self) {
  return self->lightProbeTexture();
}

//  void QSSGRhiShaderPipeline::setScreenTexture(QRhiTexture *texture)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSSGRhiShaderPipeline16setScreenTextureEP11QRhiTexture(
    QSSGRhiShaderPipeline *self,
    QRhiTexture *texture) {
  self->setScreenTexture(texture);
}

//  QRhiTexture *QSSGRhiShaderPipeline::screenTexture() const
extern "C" Q_DECL_EXPORT
QRhiTexture *ritual_ZNK21QSSGRhiShaderPipeline13screenTextureEv(
    const QSSGRhiShaderPipeline *self) {
  return self->screenTexture();
}

//  void QSSGRhiShaderPipeline::setDepthTexture(QRhiTexture *texture)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSSGRhiShaderPipeline15setDepthTextureEP11QRhiTexture(
    QSSGRhiShaderPipeline *self,
    QRhiTexture *texture) {
  self->setDepthTexture(texture);
}

//  QRhiTexture *QSSGRhiShaderPipeline::depthTexture() const
extern "C" Q_DECL_EXPORT
QRhiTexture *ritual_ZNK21QSSGRhiShaderPipeline12depthTextureEv(
    const QSSGRhiShaderPipeline *self) {
  return self->depthTexture();
}

//  void QSSGRhiShaderPipeline::setNormalTexture(QRhiTexture *texture)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSSGRhiShaderPipeline16setNormalTextureEP11QRhiTexture(
    QSSGRhiShaderPipeline *self,
    QRhiTexture *texture) {
  self->setNormalTexture(texture);
}

//  QRhiTexture *QSSGRhiShaderPipeline::normalTexture() const
extern "C" Q_DECL_EXPORT
QRhiTexture *ritual_ZNK21QSSGRhiShaderPipeline13normalTextureEv(
    const QSSGRhiShaderPipeline *self) {
  return self->normalTexture();
}

//  void QSSGRhiShaderPipeline::setSsaoTexture(QRhiTexture *texture)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSSGRhiShaderPipeline14setSsaoTextureEP11QRhiTexture(
    QSSGRhiShaderPipeline *self,
    QRhiTexture *texture) {
  self->setSsaoTexture(texture);
}

//  QRhiTexture *QSSGRhiShaderPipeline::ssaoTexture() const
extern "C" Q_DECL_EXPORT
QRhiTexture *ritual_ZNK21QSSGRhiShaderPipeline11ssaoTextureEv(
    const QSSGRhiShaderPipeline *self) {
  return self->ssaoTexture();
}

//  void QSSGRhiShaderPipeline::setLightmapTexture(QRhiTexture *texture)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSSGRhiShaderPipeline18setLightmapTextureEP11QRhiTexture(
    QSSGRhiShaderPipeline *self,
    QRhiTexture *texture) {
  self->setLightmapTexture(texture);
}

//  QRhiTexture *QSSGRhiShaderPipeline::lightmapTexture() const
extern "C" Q_DECL_EXPORT
QRhiTexture *ritual_ZNK21QSSGRhiShaderPipeline15lightmapTextureEv(
    const QSSGRhiShaderPipeline *self) {
  return self->lightmapTexture();
}

//  void QSSGRhiShaderPipeline::setMotionVectorTexture(QRhiTexture *texture)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSSGRhiShaderPipeline22setMotionVectorTextureEP11QRhiTexture(
    QSSGRhiShaderPipeline *self,
    QRhiTexture *texture) {
  self->setMotionVectorTexture(texture);
}

//  QRhiTexture *QSSGRhiShaderPipeline::MotionVectorTexture() const
extern "C" Q_DECL_EXPORT
QRhiTexture *ritual_ZNK21QSSGRhiShaderPipeline19MotionVectorTextureEv(
    const QSSGRhiShaderPipeline *self) {
  return self->MotionVectorTexture();
}

//  void QSSGRhiShaderPipeline::setShadowMapAtlasTexture(QRhiTexture
//      *texture)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSSGRhiShaderPipeline24setShadowMapAtlasTextureEP11QRhiTexture(
    QSSGRhiShaderPipeline *self,
    QRhiTexture *texture) {
  self->setShadowMapAtlasTexture(texture);
}

//  QRhiTexture *QSSGRhiShaderPipeline::shadowMapAtlasTexture() const
extern "C" Q_DECL_EXPORT
QRhiTexture *ritual_ZNK21QSSGRhiShaderPipeline21shadowMapAtlasTextureEv(
    const QSSGRhiShaderPipeline *self) {
  return self->shadowMapAtlasTexture();
}

//  void QSSGRhiShaderPipeline::setShadowMapBlueNoiseTexture(QRhiTexture
//      *texture)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSSGRhiShaderPipeline28setShadowMapBlueNoiseTextureEP11QRhiTexture(
    QSSGRhiShaderPipeline *self,
    QRhiTexture *texture) {
  self->setShadowMapBlueNoiseTexture(texture);
}

//  QRhiTexture *QSSGRhiShaderPipeline::shadowMapBlueNoiseTexture() const
extern "C" Q_DECL_EXPORT
QRhiTexture *ritual_ZNK21QSSGRhiShaderPipeline25shadowMapBlueNoiseTextureEv(
    const QSSGRhiShaderPipeline *self) {
  return self->shadowMapBlueNoiseTexture();
}

//  void QSSGRhiShaderPipeline::setOITImages(QRhiTexture *accumulator,
//      QRhiTexture *auxiliary, QRhiTexture *counter)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSSGRhiShaderPipeline12setOITImagesEP11QRhiTextureS1_S1_(
    QSSGRhiShaderPipeline *self,
    QRhiTexture *accumulator,
    QRhiTexture *auxiliary,
    QRhiTexture *counter) {
  self->setOITImages(accumulator, auxiliary, counter);
}

//  void QSSGRhiShaderPipeline::resetExtraTextures()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSSGRhiShaderPipeline18resetExtraTexturesEv(
    QSSGRhiShaderPipeline *self) {
  self->resetExtraTextures();
}

//  void QSSGRhiShaderPipeline::addExtraTexture(const QSSGRhiTexture &t)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSSGRhiShaderPipeline15addExtraTextureERK14QSSGRhiTexture(
    QSSGRhiShaderPipeline *self,
    const QSSGRhiTexture *t) {
  self->addExtraTexture(*t);
}

//  int QSSGRhiShaderPipeline::extraTextureCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QSSGRhiShaderPipeline17extraTextureCountEv(
    const QSSGRhiShaderPipeline *self) {
  return self->extraTextureCount();
}

//  const QSSGRhiTexture &QSSGRhiShaderPipeline::extraTextureAt(int index)
//      const
extern "C" Q_DECL_EXPORT
QSSGRhiTexture *ritual_ZNK21QSSGRhiShaderPipeline14extraTextureAtEi(
    const QSSGRhiShaderPipeline *self,
    int index) {
  return new QSSGRhiTexture(self->extraTextureAt(index));
}

//  InstanceLocations QSSGRhiShaderPipeline::instanceBufferLocations() const
extern "C" Q_DECL_EXPORT
QSSGRhiShaderPipeline::InstanceLocations *ritual_ZNK21QSSGRhiShaderPipeline23instanceBufferLocationsEv(
    const QSSGRhiShaderPipeline *self) {
  return new QSSGRhiShaderPipeline::InstanceLocations(
      self->instanceBufferLocations());
}

//  int QSSGRhiShaderPipeline::offsetOfUniform(const QByteArray &name)
extern "C" Q_DECL_EXPORT
int ritual_ZN21QSSGRhiShaderPipeline15offsetOfUniformERK10QByteArray(
    QSSGRhiShaderPipeline *self,
    const QByteArray *name) {
  return self->offsetOfUniform(*name);
}
