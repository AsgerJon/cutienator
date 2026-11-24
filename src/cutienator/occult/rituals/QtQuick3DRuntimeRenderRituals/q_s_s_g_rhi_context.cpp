//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/ssg/qssgrhicontext.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/ssg/qssgrhicontext.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qsize.h>
#include <QtGui/qcolor.h>

//  QSSGRhiContext::QSSGRhiContext(QRhi *rhi)
extern "C" Q_DECL_EXPORT
QSSGRhiContext *ritual_ZN14QSSGRhiContextC1EP4QRhi(QRhi *rhi) {
  return new QSSGRhiContext(rhi);
}

//  QSSGRhiContext::~QSSGRhiContext()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSSGRhiContextD1Ev(QSSGRhiContext *self) {
  delete self;
}

//  QRhi *QSSGRhiContext::rhi() const
extern "C" Q_DECL_EXPORT
QRhi *ritual_ZNK14QSSGRhiContext3rhiEv(const QSSGRhiContext *self) {
  return self->rhi();
}

//  bool QSSGRhiContext::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QSSGRhiContext7isValidEv(const QSSGRhiContext *self) {
  return self->isValid();
}

//  QRhiRenderPassDescriptor *QSSGRhiContext::mainRenderPassDescriptor()
//      const
extern "C" Q_DECL_EXPORT
QRhiRenderPassDescriptor *ritual_ZNK14QSSGRhiContext24mainRenderPassDescriptorEv(
    const QSSGRhiContext *self) {
  return self->mainRenderPassDescriptor();
}

//  QRhiCommandBuffer *QSSGRhiContext::commandBuffer() const
extern "C" Q_DECL_EXPORT
QRhiCommandBuffer *ritual_ZNK14QSSGRhiContext13commandBufferEv(
    const QSSGRhiContext *self) {
  return self->commandBuffer();
}

//  QRhiRenderTarget *QSSGRhiContext::renderTarget() const
extern "C" Q_DECL_EXPORT
QRhiRenderTarget *ritual_ZNK14QSSGRhiContext12renderTargetEv(
    const QSSGRhiContext *self) {
  return self->renderTarget();
}

//  int QSSGRhiContext::mainPassSampleCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QSSGRhiContext19mainPassSampleCountEv(
    const QSSGRhiContext *self) {
  return self->mainPassSampleCount();
}

//  int QSSGRhiContext::mainPassViewCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QSSGRhiContext17mainPassViewCountEv(
    const QSSGRhiContext *self) {
  return self->mainPassViewCount();
}

//  QRhiSampler *QSSGRhiContext::sampler(const QSSGRhiSamplerDescription
//      &samplerDescription)
extern "C" Q_DECL_EXPORT
QRhiSampler *ritual_ZN14QSSGRhiContext7samplerERK25QSSGRhiSamplerDescription(
    QSSGRhiContext *self,
    const QSSGRhiSamplerDescription *samplerDescription) {
  return self->sampler(*samplerDescription);
}

//  void QSSGRhiContext::checkAndAdjustForNPoT(QRhiTexture *texture,
//      QSSGRhiSamplerDescription *samplerDescription)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSSGRhiContext21checkAndAdjustForNPoTEP11QRhiTextureP25QSSGRhiSamplerDescription(
    QSSGRhiContext *self,
    QRhiTexture *texture,
    QSSGRhiSamplerDescription *samplerDescription) {
  self->checkAndAdjustForNPoT(texture, samplerDescription);
}

//  QRhiTexture *QSSGRhiContext::dummyTexture(QRhiTexture::Flags flags,
//      QRhiResourceUpdateBatch *rub, const QSize &size, const QColor
//      &fillColor, int arraySize)
extern "C" Q_DECL_EXPORT
QRhiTexture *ritual_ZN14QSSGRhiContext12dummyTextureE6QFlagsIN11QRhiTexture4FlagEEP23QRhiResourceUpdateBatchRK5QSizeRK6QColori(
    QSSGRhiContext *self,
    int flags,
    QRhiResourceUpdateBatch *rub,
    const QSize *size,
    const QColor *fillColor,
    int arraySize) {
  return self->dummyTexture(
      QFlags<QRhiTexture::Flag>::fromInt(flags),
      rub,
      *size,
      *fillColor,
      arraySize);
}

//  QRhiCommandBuffer::BeginPassFlags QSSGRhiContext::commonPassFlags() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QSSGRhiContext15commonPassFlagsEv(
    const QSSGRhiContext *self) {
  return static_cast<int>(self->commonPassFlags().toInt());
}

//  QSSGRhiContextPrivate *QSSGRhiContext::d_func()
extern "C" Q_DECL_EXPORT
QSSGRhiContextPrivate *ritual_ZN14QSSGRhiContext6d_funcEv(
    QSSGRhiContext *self) {
  return self->d_func();
}

//  const QSSGRhiContextPrivate *QSSGRhiContext::d_func() const
extern "C" Q_DECL_EXPORT
const QSSGRhiContextPrivate *ritual_ZNK14QSSGRhiContext6d_funcEv(
    const QSSGRhiContext *self) {
  return self->d_func();
}
