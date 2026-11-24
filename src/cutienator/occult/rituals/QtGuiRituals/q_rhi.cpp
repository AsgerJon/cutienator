//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/rhi/qrhi.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/rhi/qrhi.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qsize.h>
#include <QtGui/qmatrix4x4.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qlist.h>

//  QRhi::~QRhi()
extern "C" Q_DECL_EXPORT
void ritual_ZN4QRhiD1Ev(QRhi *self) {
  delete self;
}

//  QRhi *QRhi::create(Implementation impl, QRhiInitParams *params, Flags
//      flags, QRhiNativeHandles *importDevice)
extern "C" Q_DECL_EXPORT
QRhi *ritual_ZN4QRhi6createENS_14ImplementationEP14QRhiInitParams6QFlagsINS_4FlagEEP17QRhiNativeHandles(
    QRhi::Implementation impl,
    QRhiInitParams *params,
    int flags,
    QRhiNativeHandles *importDevice) {
  return QRhi::create(
      impl,
      params,
      QFlags<QRhi::Flag>::fromInt(flags),
      importDevice);
}

//  QRhi *QRhi::create(Implementation impl, QRhiInitParams *params, Flags
//      flags, QRhiNativeHandles *importDevice, QRhiAdapter *adapter)
extern "C" Q_DECL_EXPORT
QRhi *ritual_ZN4QRhi6createENS_14ImplementationEP14QRhiInitParams6QFlagsINS_4FlagEEP17QRhiNativeHandlesP11QRhiAdapter(
    QRhi::Implementation impl,
    QRhiInitParams *params,
    int flags,
    QRhiNativeHandles *importDevice,
    QRhiAdapter *adapter) {
  return QRhi::create(
      impl,
      params,
      QFlags<QRhi::Flag>::fromInt(flags),
      importDevice,
      adapter);
}

//  bool QRhi::probe(Implementation impl, QRhiInitParams *params)
extern "C" Q_DECL_EXPORT
bool ritual_ZN4QRhi5probeENS_14ImplementationEP14QRhiInitParams(
    QRhi::Implementation impl,
    QRhiInitParams *params) {
  return QRhi::probe(impl, params);
}

//  AdapterList QRhi::enumerateAdapters(Implementation impl, QRhiInitParams
//      *params, QRhiNativeHandles *nativeHandles)
extern "C" Q_DECL_EXPORT
QList<QRhiAdapter *> *ritual_ZN4QRhi17enumerateAdaptersENS_14ImplementationEP14QRhiInitParamsP17QRhiNativeHandles(
    QRhi::Implementation impl,
    QRhiInitParams *params,
    QRhiNativeHandles *nativeHandles) {
  return new QList<QRhiAdapter *>(
      QRhi::enumerateAdapters(
          impl,
          params,
          nativeHandles));
}

//  Implementation QRhi::backend() const
extern "C" Q_DECL_EXPORT
QRhi::Implementation ritual_ZNK4QRhi7backendEv(const QRhi *self) {
  return self->backend();
}

//  const char *QRhi::backendName() const
extern "C" Q_DECL_EXPORT
const char *ritual_ZNK4QRhi11backendNameEv(const QRhi *self) {
  return self->backendName();
}

//  const char *QRhi::backendName(Implementation impl)
extern "C" Q_DECL_EXPORT
const char *ritual_ZN4QRhi11backendNameENS_14ImplementationE(
    QRhi::Implementation impl) {
  return QRhi::backendName(impl);
}

//  QRhiDriverInfo QRhi::driverInfo() const
extern "C" Q_DECL_EXPORT
QRhiDriverInfo *ritual_ZNK4QRhi10driverInfoEv(const QRhi *self) {
  return new QRhiDriverInfo(self->driverInfo());
}

//  QThread *QRhi::thread() const
extern "C" Q_DECL_EXPORT
QThread *ritual_ZNK4QRhi6threadEv(const QRhi *self) {
  return self->thread();
}

//  QRhiGraphicsPipeline *QRhi::newGraphicsPipeline()
extern "C" Q_DECL_EXPORT
QRhiGraphicsPipeline *ritual_ZN4QRhi19newGraphicsPipelineEv(QRhi *self) {
  return self->newGraphicsPipeline();
}

//  QRhiComputePipeline *QRhi::newComputePipeline()
extern "C" Q_DECL_EXPORT
QRhiComputePipeline *ritual_ZN4QRhi18newComputePipelineEv(QRhi *self) {
  return self->newComputePipeline();
}

//  QRhiShaderResourceBindings *QRhi::newShaderResourceBindings()
extern "C" Q_DECL_EXPORT
QRhiShaderResourceBindings *ritual_ZN4QRhi25newShaderResourceBindingsEv(
    QRhi *self) {
  return self->newShaderResourceBindings();
}

//  QRhiBuffer *QRhi::newBuffer(QRhiBuffer::Type type, QRhiBuffer::UsageFlags
//      usage, quint32 size)
extern "C" Q_DECL_EXPORT
QRhiBuffer *ritual_ZN4QRhi9newBufferEN10QRhiBuffer4TypeE6QFlagsINS0_9UsageFlagEEj(
    QRhi *self,
    QRhiBuffer::Type type,
    int usage,
    quint32 size) {
  return self->newBuffer(
      type,
      QFlags<QRhiBuffer::UsageFlag>::fromInt(usage),
      size);
}

//  QRhiRenderBuffer *QRhi::newRenderBuffer(QRhiRenderBuffer::Type type,
//      const QSize &pixelSize, int sampleCount, QRhiRenderBuffer::Flags
//      flags, QRhiTexture::Format backingFormatHint)
extern "C" Q_DECL_EXPORT
QRhiRenderBuffer *ritual_ZN4QRhi15newRenderBufferEN16QRhiRenderBuffer4TypeERK5QSizei6QFlagsINS0_4FlagEEN11QRhiTexture6FormatE(
    QRhi *self,
    QRhiRenderBuffer::Type type,
    const QSize *pixelSize,
    int sampleCount,
    int flags,
    QRhiTexture::Format backingFormatHint) {
  return self->newRenderBuffer(
      type,
      *pixelSize,
      sampleCount,
      QFlags<QRhiRenderBuffer::Flag>::fromInt(flags),
      backingFormatHint);
}

//  QRhiTexture *QRhi::newTexture(QRhiTexture::Format format, const QSize
//      &pixelSize, int sampleCount, QRhiTexture::Flags flags)
extern "C" Q_DECL_EXPORT
QRhiTexture *ritual_ZN4QRhi10newTextureEN11QRhiTexture6FormatERK5QSizei6QFlagsINS0_4FlagEE(
    QRhi *self,
    QRhiTexture::Format format,
    const QSize *pixelSize,
    int sampleCount,
    int flags) {
  return self->newTexture(
      format,
      *pixelSize,
      sampleCount,
      QFlags<QRhiTexture::Flag>::fromInt(flags));
}

//  QRhiTexture *QRhi::newTexture(QRhiTexture::Format format, int width, int
//      height, int depth, int sampleCount, QRhiTexture::Flags flags)
extern "C" Q_DECL_EXPORT
QRhiTexture *ritual_ZN4QRhi10newTextureEN11QRhiTexture6FormatEiiii6QFlagsINS0_4FlagEE(
    QRhi *self,
    QRhiTexture::Format format,
    int width,
    int height,
    int depth,
    int sampleCount,
    int flags) {
  return self->newTexture(
      format,
      width,
      height,
      depth,
      sampleCount,
      QFlags<QRhiTexture::Flag>::fromInt(flags));
}

//  QRhiTexture *QRhi::newTextureArray(QRhiTexture::Format format, int
//      arraySize, const QSize &pixelSize, int sampleCount,
//      QRhiTexture::Flags flags)
extern "C" Q_DECL_EXPORT
QRhiTexture *ritual_ZN4QRhi15newTextureArrayEN11QRhiTexture6FormatEiRK5QSizei6QFlagsINS0_4FlagEE(
    QRhi *self,
    QRhiTexture::Format format,
    int arraySize,
    const QSize *pixelSize,
    int sampleCount,
    int flags) {
  return self->newTextureArray(
      format,
      arraySize,
      *pixelSize,
      sampleCount,
      QFlags<QRhiTexture::Flag>::fromInt(flags));
}

//  QRhiSampler *QRhi::newSampler(QRhiSampler::Filter magFilter,
//      QRhiSampler::Filter minFilter, QRhiSampler::Filter mipmapMode,
//      QRhiSampler::AddressMode addressU, QRhiSampler::AddressMode addressV,
//      QRhiSampler::AddressMode addressW)
extern "C" Q_DECL_EXPORT
QRhiSampler *ritual_ZN4QRhi10newSamplerEN11QRhiSampler6FilterES1_S1_NS0_11AddressModeES2_S2_(
    QRhi *self,
    QRhiSampler::Filter magFilter,
    QRhiSampler::Filter minFilter,
    QRhiSampler::Filter mipmapMode,
    QRhiSampler::AddressMode addressU,
    QRhiSampler::AddressMode addressV,
    QRhiSampler::AddressMode addressW) {
  return self->newSampler(
      magFilter,
      minFilter,
      mipmapMode,
      addressU,
      addressV,
      addressW);
}

//  QRhiShadingRateMap *QRhi::newShadingRateMap()
extern "C" Q_DECL_EXPORT
QRhiShadingRateMap *ritual_ZN4QRhi17newShadingRateMapEv(QRhi *self) {
  return self->newShadingRateMap();
}

//  QRhiTextureRenderTarget *QRhi::newTextureRenderTarget(const
//      QRhiTextureRenderTargetDescription &desc,
//      QRhiTextureRenderTarget::Flags flags)
extern "C" Q_DECL_EXPORT
QRhiTextureRenderTarget *ritual_ZN4QRhi22newTextureRenderTargetERK34QRhiTextureRenderTargetDescription6QFlagsIN23QRhiTextureRenderTarget4FlagEE(
    QRhi *self,
    const QRhiTextureRenderTargetDescription *desc,
    int flags) {
  return self->newTextureRenderTarget(
      *desc,
      QFlags<QRhiTextureRenderTarget::Flag>::fromInt(flags));
}

//  QRhiSwapChain *QRhi::newSwapChain()
extern "C" Q_DECL_EXPORT
QRhiSwapChain *ritual_ZN4QRhi12newSwapChainEv(QRhi *self) {
  return self->newSwapChain();
}

//  FrameOpResult QRhi::beginFrame(QRhiSwapChain *swapChain, BeginFrameFlags
//      flags)
extern "C" Q_DECL_EXPORT
QRhi::FrameOpResult ritual_ZN4QRhi10beginFrameEP13QRhiSwapChain6QFlagsINS_14BeginFrameFlagEE(
    QRhi *self,
    QRhiSwapChain *swapChain,
    int flags) {
  return self->beginFrame(
      swapChain,
      QFlags<QRhi::BeginFrameFlag>::fromInt(flags));
}

//  FrameOpResult QRhi::endFrame(QRhiSwapChain *swapChain, EndFrameFlags
//      flags)
extern "C" Q_DECL_EXPORT
QRhi::FrameOpResult ritual_ZN4QRhi8endFrameEP13QRhiSwapChain6QFlagsINS_12EndFrameFlagEE(
    QRhi *self,
    QRhiSwapChain *swapChain,
    int flags) {
  return self->endFrame(
      swapChain,
      QFlags<QRhi::EndFrameFlag>::fromInt(flags));
}

//  bool QRhi::isRecordingFrame() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK4QRhi16isRecordingFrameEv(const QRhi *self) {
  return self->isRecordingFrame();
}

//  int QRhi::currentFrameSlot() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK4QRhi16currentFrameSlotEv(const QRhi *self) {
  return self->currentFrameSlot();
}

//  FrameOpResult QRhi::endOffscreenFrame(EndFrameFlags flags)
extern "C" Q_DECL_EXPORT
QRhi::FrameOpResult ritual_ZN4QRhi17endOffscreenFrameE6QFlagsINS_12EndFrameFlagEE(
    QRhi *self,
    int flags) {
  return self->endOffscreenFrame(QFlags<QRhi::EndFrameFlag>::fromInt(flags));
}

//  QRhi::FrameOpResult QRhi::finish()
extern "C" Q_DECL_EXPORT
QRhi::FrameOpResult ritual_ZN4QRhi6finishEv(QRhi *self) {
  return self->finish();
}

//  QRhiResourceUpdateBatch *QRhi::nextResourceUpdateBatch()
extern "C" Q_DECL_EXPORT
QRhiResourceUpdateBatch *ritual_ZN4QRhi23nextResourceUpdateBatchEv(
    QRhi *self) {
  return self->nextResourceUpdateBatch();
}

//  int QRhi::ubufAlignment() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK4QRhi13ubufAlignmentEv(const QRhi *self) {
  return self->ubufAlignment();
}

//  int QRhi::ubufAligned(int v) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK4QRhi11ubufAlignedEi(const QRhi *self, int v) {
  return self->ubufAligned(v);
}

//  int QRhi::mipLevelsForSize(const QSize &size)
extern "C" Q_DECL_EXPORT
int ritual_ZN4QRhi16mipLevelsForSizeERK5QSize(const QSize *size) {
  return QRhi::mipLevelsForSize(*size);
}

//  QSize QRhi::sizeForMipLevel(int mipLevel, const QSize &baseLevelSize)
extern "C" Q_DECL_EXPORT
QSize *ritual_ZN4QRhi15sizeForMipLevelEiRK5QSize(
    int mipLevel,
    const QSize *baseLevelSize) {
  return new QSize(QRhi::sizeForMipLevel(mipLevel, *baseLevelSize));
}

//  bool QRhi::isYUpInFramebuffer() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK4QRhi18isYUpInFramebufferEv(const QRhi *self) {
  return self->isYUpInFramebuffer();
}

//  bool QRhi::isYUpInNDC() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK4QRhi10isYUpInNDCEv(const QRhi *self) {
  return self->isYUpInNDC();
}

//  bool QRhi::isClipDepthZeroToOne() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK4QRhi20isClipDepthZeroToOneEv(const QRhi *self) {
  return self->isClipDepthZeroToOne();
}

//  QMatrix4x4 QRhi::clipSpaceCorrMatrix() const
extern "C" Q_DECL_EXPORT
QMatrix4x4 *ritual_ZNK4QRhi19clipSpaceCorrMatrixEv(const QRhi *self) {
  return new QMatrix4x4(self->clipSpaceCorrMatrix());
}

//  bool QRhi::isTextureFormatSupported(QRhiTexture::Format format,
//      QRhiTexture::Flags flags) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK4QRhi24isTextureFormatSupportedEN11QRhiTexture6FormatE6QFlagsINS0_4FlagEE(
    const QRhi *self,
    QRhiTexture::Format format,
    int flags) {
  return self->isTextureFormatSupported(
      format,
      QFlags<QRhiTexture::Flag>::fromInt(flags));
}

//  bool QRhi::isFeatureSupported(QRhi::Feature feature) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK4QRhi18isFeatureSupportedENS_7FeatureE(
    const QRhi *self,
    QRhi::Feature feature) {
  return self->isFeatureSupported(feature);
}

//  int QRhi::resourceLimit(ResourceLimit limit) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK4QRhi13resourceLimitENS_13ResourceLimitE(
    const QRhi *self,
    QRhi::ResourceLimit limit) {
  return self->resourceLimit(limit);
}

//  const QRhiNativeHandles *QRhi::nativeHandles()
extern "C" Q_DECL_EXPORT
const QRhiNativeHandles *ritual_ZN4QRhi13nativeHandlesEv(QRhi *self) {
  return self->nativeHandles();
}

//  bool QRhi::makeThreadLocalNativeContextCurrent()
extern "C" Q_DECL_EXPORT
bool ritual_ZN4QRhi35makeThreadLocalNativeContextCurrentEv(QRhi *self) {
  return self->makeThreadLocalNativeContextCurrent();
}

//  void QRhi::setQueueSubmitParams(QRhiNativeHandles *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN4QRhi20setQueueSubmitParamsEP17QRhiNativeHandles(
    QRhi *self,
    QRhiNativeHandles *params) {
  self->setQueueSubmitParams(params);
}

//  void QRhi::releaseCachedResources()
extern "C" Q_DECL_EXPORT
void ritual_ZN4QRhi22releaseCachedResourcesEv(QRhi *self) {
  self->releaseCachedResources();
}

//  bool QRhi::isDeviceLost() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK4QRhi12isDeviceLostEv(const QRhi *self) {
  return self->isDeviceLost();
}

//  QByteArray QRhi::pipelineCacheData()
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN4QRhi17pipelineCacheDataEv(QRhi *self) {
  return new QByteArray(self->pipelineCacheData());
}

//  void QRhi::setPipelineCacheData(const QByteArray &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN4QRhi20setPipelineCacheDataERK10QByteArray(
    QRhi *self,
    const QByteArray *data) {
  self->setPipelineCacheData(*data);
}

//  QRhiStats QRhi::statistics() const
extern "C" Q_DECL_EXPORT
QRhiStats *ritual_ZNK4QRhi10statisticsEv(const QRhi *self) {
  return new QRhiStats(self->statistics());
}

//  QRhiSwapChainProxyData QRhi::updateSwapChainProxyData(Implementation
//      impl, QWindow *window)
extern "C" Q_DECL_EXPORT
QRhiSwapChainProxyData *ritual_ZN4QRhi24updateSwapChainProxyDataENS_14ImplementationEP7QWindow(
    QRhi::Implementation impl,
    QWindow *window) {
  return new QRhiSwapChainProxyData(
      QRhi::updateSwapChainProxyData(
          impl,
          window));
}

//  QList<QSize> QRhi::supportedShadingRates(int sampleCount) const
extern "C" Q_DECL_EXPORT
QList<QSize> *ritual_ZNK4QRhi21supportedShadingRatesEi(
    const QRhi *self,
    int sampleCount) {
  return new QList<QSize>(self->supportedShadingRates(sampleCount));
}

//  QRhi::QRhi()
extern "C" Q_DECL_EXPORT
QRhi *ritual_ZN4QRhiC1Ev() {
  return new QRhi();
}
