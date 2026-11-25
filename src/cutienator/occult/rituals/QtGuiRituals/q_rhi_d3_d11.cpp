//  Written by hand on 2026-11-25 from
//  QtGui/6.12.0/QtGui/private/qrhid3d11_p.h, Qt 6.12.0, as the Qt of
//  Windows installs it. Kept as it is when the generator runs again.
//  Qt's library offers nothing of this class by name: only its
//  virtual functions are called, through the object, and what its
//  header writes out. Direct3D's interfaces are passed as
//  addresses.
//  Not written: its constructor and the functions it does not take
//  from QRhiImplementation, which Qt's library offers not;
//  'setShaderResources' and 'setVertexInput', which take a
//  'std::pair'; and 'supportedSampleCounts', giving a list of
//  numbers.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if defined(Q_OS_WIN)
#include <QtGui/6.12.0/QtGui/private/qrhid3d11_p.h>

//  QRhiD3D11::~QRhiD3D11()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QRhiD3D11D1Ev(QRhiD3D11 *self) {
  delete self;
}

//  bool QRhiD3D11::create(QRhi::Flags flags)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QRhiD3D116createE6QFlagsIN4QRhi4FlagEE(
    QRhiD3D11 *self,
    int flags) {
  return self->create(QFlags<QRhi::Flag>::fromInt(flags));
}

//  void QRhiD3D11::destroy()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QRhiD3D117destroyEv(QRhiD3D11 *self) {
  self->destroy();
}

//  QRhi::AdapterList
//      QRhiD3D11::enumerateAdaptersBeforeCreate(QRhiNativeHandles
//      *nativeHandles) const
extern "C" Q_DECL_EXPORT
QList<QRhiAdapter *> *ritual_ZNK9QRhiD3D1129enumerateAdaptersBeforeCreateEP17QRhiNativeHandles(
    const QRhiD3D11 *self,
    QRhiNativeHandles *nativeHandles) {
  return new QList<QRhiAdapter *>(
      self->enumerateAdaptersBeforeCreate(nativeHandles));
}

//  QRhiGraphicsPipeline *QRhiD3D11::createGraphicsPipeline()
extern "C" Q_DECL_EXPORT
QRhiGraphicsPipeline *ritual_ZN9QRhiD3D1122createGraphicsPipelineEv(
    QRhiD3D11 *self) {
  return self->createGraphicsPipeline();
}

//  QRhiComputePipeline *QRhiD3D11::createComputePipeline()
extern "C" Q_DECL_EXPORT
QRhiComputePipeline *ritual_ZN9QRhiD3D1121createComputePipelineEv(
    QRhiD3D11 *self) {
  return self->createComputePipeline();
}

//  QRhiShaderResourceBindings *QRhiD3D11::createShaderResourceBindings()
extern "C" Q_DECL_EXPORT
QRhiShaderResourceBindings *ritual_ZN9QRhiD3D1128createShaderResourceBindingsEv(
    QRhiD3D11 *self) {
  return self->createShaderResourceBindings();
}

//  QRhiBuffer *QRhiD3D11::createBuffer(QRhiBuffer::Type type,
//      QRhiBuffer::UsageFlags usage, quint32 size)
extern "C" Q_DECL_EXPORT
QRhiBuffer *ritual_ZN9QRhiD3D1112createBufferEN10QRhiBuffer4TypeE6QFlagsINS0_9UsageFlagEEj(
    QRhiD3D11 *self,
    QRhiBuffer::Type type,
    int usage,
    quint32 size) {
  return self->createBuffer(
      type, QFlags<QRhiBuffer::UsageFlag>::fromInt(usage), size);
}

//  QRhiRenderBuffer *QRhiD3D11::createRenderBuffer(QRhiRenderBuffer::Type
//      type, const QSize &pixelSize, int sampleCount,
//      QRhiRenderBuffer::Flags flags, QRhiTexture::Format backingFormatHint)
extern "C" Q_DECL_EXPORT
QRhiRenderBuffer *ritual_ZN9QRhiD3D1118createRenderBufferEN16QRhiRenderBuffer4TypeERK5QSizei6QFlagsINS0_4FlagEEN11QRhiTexture6FormatE(
    QRhiD3D11 *self,
    QRhiRenderBuffer::Type type,
    const QSize *pixelSize,
    int sampleCount,
    int flags,
    QRhiTexture::Format backingFormatHint) {
  return self->createRenderBuffer(
      type, *pixelSize, sampleCount,
      QFlags<QRhiRenderBuffer::Flag>::fromInt(flags), backingFormatHint);
}

//  QRhiTexture *QRhiD3D11::createTexture(QRhiTexture::Format format, const
//      QSize &pixelSize, int depth, int arraySize, int sampleCount,
//      QRhiTexture::Flags flags)
extern "C" Q_DECL_EXPORT
QRhiTexture *ritual_ZN9QRhiD3D1113createTextureEN11QRhiTexture6FormatERK5QSizeiii6QFlagsINS0_4FlagEE(
    QRhiD3D11 *self,
    QRhiTexture::Format format,
    const QSize *pixelSize,
    int depth,
    int arraySize,
    int sampleCount,
    int flags) {
  return self->createTexture(
      format, *pixelSize, depth, arraySize, sampleCount,
      QFlags<QRhiTexture::Flag>::fromInt(flags));
}

//  QRhiSampler *QRhiD3D11::createSampler(QRhiSampler::Filter magFilter,
//      QRhiSampler::Filter minFilter, QRhiSampler::Filter mipmapMode,
//      QRhiSampler::AddressMode u, QRhiSampler::AddressMode v,
//      QRhiSampler::AddressMode w)
extern "C" Q_DECL_EXPORT
QRhiSampler *ritual_ZN9QRhiD3D1113createSamplerEN11QRhiSampler6FilterES1_S1_NS0_11AddressModeES2_S2_(
    QRhiD3D11 *self,
    QRhiSampler::Filter magFilter,
    QRhiSampler::Filter minFilter,
    QRhiSampler::Filter mipmapMode,
    QRhiSampler::AddressMode u,
    QRhiSampler::AddressMode v,
    QRhiSampler::AddressMode w) {
  return self->createSampler(magFilter, minFilter, mipmapMode, u, v, w);
}

//  QRhiTextureRenderTarget *QRhiD3D11::createTextureRenderTarget(const
//      QRhiTextureRenderTargetDescription &desc,
//      QRhiTextureRenderTarget::Flags flags)
extern "C" Q_DECL_EXPORT
QRhiTextureRenderTarget *ritual_ZN9QRhiD3D1125createTextureRenderTargetERK34QRhiTextureRenderTargetDescription6QFlagsIN23QRhiTextureRenderTarget4FlagEE(
    QRhiD3D11 *self,
    const QRhiTextureRenderTargetDescription *desc,
    int flags) {
  return self->createTextureRenderTarget(
      *desc, QFlags<QRhiTextureRenderTarget::Flag>::fromInt(flags));
}

//  QRhiShadingRateMap *QRhiD3D11::createShadingRateMap()
extern "C" Q_DECL_EXPORT
QRhiShadingRateMap *ritual_ZN9QRhiD3D1120createShadingRateMapEv(
    QRhiD3D11 *self) {
  return self->createShadingRateMap();
}

//  QRhiSwapChain *QRhiD3D11::createSwapChain()
extern "C" Q_DECL_EXPORT
QRhiSwapChain *ritual_ZN9QRhiD3D1115createSwapChainEv(QRhiD3D11 *self) {
  return self->createSwapChain();
}

//  QRhi::FrameOpResult QRhiD3D11::beginFrame(QRhiSwapChain *swapChain,
//      QRhi::BeginFrameFlags flags)
extern "C" Q_DECL_EXPORT
QRhi::FrameOpResult ritual_ZN9QRhiD3D1110beginFrameEP13QRhiSwapChain6QFlagsIN4QRhi14BeginFrameFlagEE(
    QRhiD3D11 *self,
    QRhiSwapChain *swapChain,
    int flags) {
  return self->beginFrame(swapChain, QFlags<QRhi::BeginFrameFlag>::fromInt(flags));
}

//  QRhi::FrameOpResult QRhiD3D11::endFrame(QRhiSwapChain *swapChain,
//      QRhi::EndFrameFlags flags)
extern "C" Q_DECL_EXPORT
QRhi::FrameOpResult ritual_ZN9QRhiD3D118endFrameEP13QRhiSwapChain6QFlagsIN4QRhi12EndFrameFlagEE(
    QRhiD3D11 *self,
    QRhiSwapChain *swapChain,
    int flags) {
  return self->endFrame(swapChain, QFlags<QRhi::EndFrameFlag>::fromInt(flags));
}

//  QRhi::FrameOpResult QRhiD3D11::beginOffscreenFrame(QRhiCommandBuffer
//      **cb, QRhi::BeginFrameFlags flags)
extern "C" Q_DECL_EXPORT
QRhi::FrameOpResult ritual_ZN9QRhiD3D1119beginOffscreenFrameEPP17QRhiCommandBuffer6QFlagsIN4QRhi14BeginFrameFlagEE(
    QRhiD3D11 *self,
    QRhiCommandBuffer **cb,
    int flags) {
  return self->beginOffscreenFrame(cb, QFlags<QRhi::BeginFrameFlag>::fromInt(flags));
}

//  QRhi::FrameOpResult QRhiD3D11::endOffscreenFrame(QRhi::EndFrameFlags
//      flags)
extern "C" Q_DECL_EXPORT
QRhi::FrameOpResult ritual_ZN9QRhiD3D1117endOffscreenFrameE6QFlagsIN4QRhi12EndFrameFlagEE(
    QRhiD3D11 *self,
    int flags) {
  return self->endOffscreenFrame(QFlags<QRhi::EndFrameFlag>::fromInt(flags));
}

//  QRhi::FrameOpResult QRhiD3D11::finish()
extern "C" Q_DECL_EXPORT
QRhi::FrameOpResult ritual_ZN9QRhiD3D116finishEv(QRhiD3D11 *self) {
  return self->finish();
}

//  void QRhiD3D11::resourceUpdate(QRhiCommandBuffer *cb,
//      QRhiResourceUpdateBatch *resourceUpdates)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QRhiD3D1114resourceUpdateEP17QRhiCommandBufferP23QRhiResourceUpdateBatch(
    QRhiD3D11 *self,
    QRhiCommandBuffer *cb,
    QRhiResourceUpdateBatch *resourceUpdates) {
  self->resourceUpdate(cb, resourceUpdates);
}

//  void QRhiD3D11::beginPass(QRhiCommandBuffer *cb, QRhiRenderTarget *rt,
//      const QColor &colorClearValue, const QRhiDepthStencilClearValue
//      &depthStencilClearValue, QRhiResourceUpdateBatch *resourceUpdates,
//      QRhiCommandBuffer::BeginPassFlags flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QRhiD3D119beginPassEP17QRhiCommandBufferP16QRhiRenderTargetRK6QColorRK26QRhiDepthStencilClearValueP23QRhiResourceUpdateBatch6QFlagsINS0_13BeginPassFlagEE(
    QRhiD3D11 *self,
    QRhiCommandBuffer *cb,
    QRhiRenderTarget *rt,
    const QColor *colorClearValue,
    const QRhiDepthStencilClearValue *depthStencilClearValue,
    QRhiResourceUpdateBatch *resourceUpdates,
    int flags) {
  self->beginPass(
      cb, rt, *colorClearValue, *depthStencilClearValue, resourceUpdates,
      QFlags<QRhiCommandBuffer::BeginPassFlag>::fromInt(flags));
}

//  void QRhiD3D11::endPass(QRhiCommandBuffer *cb, QRhiResourceUpdateBatch
//      *resourceUpdates)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QRhiD3D117endPassEP17QRhiCommandBufferP23QRhiResourceUpdateBatch(
    QRhiD3D11 *self,
    QRhiCommandBuffer *cb,
    QRhiResourceUpdateBatch *resourceUpdates) {
  self->endPass(cb, resourceUpdates);
}

//  void QRhiD3D11::setGraphicsPipeline(QRhiCommandBuffer *cb,
//      QRhiGraphicsPipeline *ps)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QRhiD3D1119setGraphicsPipelineEP17QRhiCommandBufferP20QRhiGraphicsPipeline(
    QRhiD3D11 *self,
    QRhiCommandBuffer *cb,
    QRhiGraphicsPipeline *ps) {
  self->setGraphicsPipeline(cb, ps);
}

//  void QRhiD3D11::setViewport(QRhiCommandBuffer *cb, const QRhiViewport
//      &viewport)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QRhiD3D1111setViewportEP17QRhiCommandBufferRK12QRhiViewport(
    QRhiD3D11 *self,
    QRhiCommandBuffer *cb,
    const QRhiViewport *viewport) {
  self->setViewport(cb, *viewport);
}

//  void QRhiD3D11::setScissor(QRhiCommandBuffer *cb, const QRhiScissor
//      &scissor)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QRhiD3D1110setScissorEP17QRhiCommandBufferRK11QRhiScissor(
    QRhiD3D11 *self,
    QRhiCommandBuffer *cb,
    const QRhiScissor *scissor) {
  self->setScissor(cb, *scissor);
}

//  void QRhiD3D11::setBlendConstants(QRhiCommandBuffer *cb, const QColor &c)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QRhiD3D1117setBlendConstantsEP17QRhiCommandBufferRK6QColor(
    QRhiD3D11 *self,
    QRhiCommandBuffer *cb,
    const QColor *c) {
  self->setBlendConstants(cb, *c);
}

//  void QRhiD3D11::setStencilRef(QRhiCommandBuffer *cb, quint32 refValue)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QRhiD3D1113setStencilRefEP17QRhiCommandBufferj(
    QRhiD3D11 *self,
    QRhiCommandBuffer *cb,
    quint32 refValue) {
  self->setStencilRef(cb, refValue);
}

//  void QRhiD3D11::setShadingRate(QRhiCommandBuffer *cb, const QSize
//      &coarsePixelSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QRhiD3D1114setShadingRateEP17QRhiCommandBufferRK5QSize(
    QRhiD3D11 *self,
    QRhiCommandBuffer *cb,
    const QSize *coarsePixelSize) {
  self->setShadingRate(cb, *coarsePixelSize);
}

//  void QRhiD3D11::draw(QRhiCommandBuffer *cb, quint32 vertexCount, quint32
//      instanceCount, quint32 firstVertex, quint32 firstInstance)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QRhiD3D114drawEP17QRhiCommandBufferjjjj(
    QRhiD3D11 *self,
    QRhiCommandBuffer *cb,
    quint32 vertexCount,
    quint32 instanceCount,
    quint32 firstVertex,
    quint32 firstInstance) {
  self->draw(cb, vertexCount, instanceCount, firstVertex, firstInstance);
}

//  void QRhiD3D11::drawIndexed(QRhiCommandBuffer *cb, quint32 indexCount,
//      quint32 instanceCount, quint32 firstIndex, qint32 vertexOffset,
//      quint32 firstInstance)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QRhiD3D1111drawIndexedEP17QRhiCommandBufferjjjij(
    QRhiD3D11 *self,
    QRhiCommandBuffer *cb,
    quint32 indexCount,
    quint32 instanceCount,
    quint32 firstIndex,
    qint32 vertexOffset,
    quint32 firstInstance) {
  self->drawIndexed(
      cb, indexCount, instanceCount, firstIndex, vertexOffset,
      firstInstance);
}

//  void QRhiD3D11::drawIndirect(QRhiCommandBuffer *cb, QRhiBuffer
//      *indirectBuffer, quint32 indirectBufferOffset, quint32 drawCount,
//      quint32 stride)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QRhiD3D1112drawIndirectEP17QRhiCommandBufferP10QRhiBufferjjj(
    QRhiD3D11 *self,
    QRhiCommandBuffer *cb,
    QRhiBuffer *indirectBuffer,
    quint32 indirectBufferOffset,
    quint32 drawCount,
    quint32 stride) {
  self->drawIndirect(cb, indirectBuffer, indirectBufferOffset, drawCount, stride);
}

//  void QRhiD3D11::drawIndexedIndirect(QRhiCommandBuffer *cb, QRhiBuffer
//      *indirectBuffer, quint32 indirectBufferOffset, quint32 drawCount,
//      quint32 stride)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QRhiD3D1119drawIndexedIndirectEP17QRhiCommandBufferP10QRhiBufferjjj(
    QRhiD3D11 *self,
    QRhiCommandBuffer *cb,
    QRhiBuffer *indirectBuffer,
    quint32 indirectBufferOffset,
    quint32 drawCount,
    quint32 stride) {
  self->drawIndexedIndirect(cb, indirectBuffer, indirectBufferOffset, drawCount, stride);
}

//  void QRhiD3D11::debugMarkBegin(QRhiCommandBuffer *cb, const QByteArray
//      &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QRhiD3D1114debugMarkBeginEP17QRhiCommandBufferRK10QByteArray(
    QRhiD3D11 *self,
    QRhiCommandBuffer *cb,
    const QByteArray *name) {
  self->debugMarkBegin(cb, *name);
}

//  void QRhiD3D11::debugMarkMsg(QRhiCommandBuffer *cb, const QByteArray
//      &msg)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QRhiD3D1112debugMarkMsgEP17QRhiCommandBufferRK10QByteArray(
    QRhiD3D11 *self,
    QRhiCommandBuffer *cb,
    const QByteArray *msg) {
  self->debugMarkMsg(cb, *msg);
}

//  void QRhiD3D11::debugMarkEnd(QRhiCommandBuffer *cb)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QRhiD3D1112debugMarkEndEP17QRhiCommandBuffer(
    QRhiD3D11 *self,
    QRhiCommandBuffer *cb) {
  self->debugMarkEnd(cb);
}

//  void QRhiD3D11::beginExternal(QRhiCommandBuffer *cb)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QRhiD3D1113beginExternalEP17QRhiCommandBuffer(
    QRhiD3D11 *self,
    QRhiCommandBuffer *cb) {
  self->beginExternal(cb);
}

//  void QRhiD3D11::endExternal(QRhiCommandBuffer *cb)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QRhiD3D1111endExternalEP17QRhiCommandBuffer(
    QRhiD3D11 *self,
    QRhiCommandBuffer *cb) {
  self->endExternal(cb);
}

//  void QRhiD3D11::beginComputePass(QRhiCommandBuffer *cb,
//      QRhiResourceUpdateBatch *resourceUpdates,
//      QRhiCommandBuffer::BeginPassFlags flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QRhiD3D1116beginComputePassEP17QRhiCommandBufferP23QRhiResourceUpdateBatch6QFlagsINS0_13BeginPassFlagEE(
    QRhiD3D11 *self,
    QRhiCommandBuffer *cb,
    QRhiResourceUpdateBatch *resourceUpdates,
    int flags) {
  self->beginComputePass(
      cb, resourceUpdates, QFlags<QRhiCommandBuffer::BeginPassFlag>::fromInt(flags));
}

//  void QRhiD3D11::endComputePass(QRhiCommandBuffer *cb,
//      QRhiResourceUpdateBatch *resourceUpdates)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QRhiD3D1114endComputePassEP17QRhiCommandBufferP23QRhiResourceUpdateBatch(
    QRhiD3D11 *self,
    QRhiCommandBuffer *cb,
    QRhiResourceUpdateBatch *resourceUpdates) {
  self->endComputePass(cb, resourceUpdates);
}

//  void QRhiD3D11::setComputePipeline(QRhiCommandBuffer *cb,
//      QRhiComputePipeline *ps)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QRhiD3D1118setComputePipelineEP17QRhiCommandBufferP19QRhiComputePipeline(
    QRhiD3D11 *self,
    QRhiCommandBuffer *cb,
    QRhiComputePipeline *ps) {
  self->setComputePipeline(cb, ps);
}

//  void QRhiD3D11::dispatch(QRhiCommandBuffer *cb, int x, int y, int z)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QRhiD3D118dispatchEP17QRhiCommandBufferiii(
    QRhiD3D11 *self,
    QRhiCommandBuffer *cb,
    int x,
    int y,
    int z) {
  self->dispatch(cb, x, y, z);
}

//  const QRhiNativeHandles *QRhiD3D11::nativeHandles(QRhiCommandBuffer *cb)
extern "C" Q_DECL_EXPORT
const QRhiNativeHandles *ritual_ZN9QRhiD3D1113nativeHandlesEP17QRhiCommandBuffer(
    QRhiD3D11 *self,
    QRhiCommandBuffer *cb) {
  return self->nativeHandles(cb);
}

//  double QRhiD3D11::lastCompletedGpuTime(QRhiCommandBuffer *cb)
extern "C" Q_DECL_EXPORT
double ritual_ZN9QRhiD3D1120lastCompletedGpuTimeEP17QRhiCommandBuffer(
    QRhiD3D11 *self,
    QRhiCommandBuffer *cb) {
  return self->lastCompletedGpuTime(cb);
}

//  QList<QSize> QRhiD3D11::supportedShadingRates(int sampleCount) const
extern "C" Q_DECL_EXPORT
QList<QSize> *ritual_ZNK9QRhiD3D1121supportedShadingRatesEi(
    const QRhiD3D11 *self,
    int sampleCount) {
  return new QList<QSize>(self->supportedShadingRates(sampleCount));
}

//  int QRhiD3D11::ubufAlignment() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QRhiD3D1113ubufAlignmentEv(const QRhiD3D11 *self) {
  return self->ubufAlignment();
}

//  bool QRhiD3D11::isYUpInFramebuffer() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QRhiD3D1118isYUpInFramebufferEv(const QRhiD3D11 *self) {
  return self->isYUpInFramebuffer();
}

//  bool QRhiD3D11::isYUpInNDC() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QRhiD3D1110isYUpInNDCEv(const QRhiD3D11 *self) {
  return self->isYUpInNDC();
}

//  bool QRhiD3D11::isClipDepthZeroToOne() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QRhiD3D1120isClipDepthZeroToOneEv(const QRhiD3D11 *self) {
  return self->isClipDepthZeroToOne();
}

//  QMatrix4x4 QRhiD3D11::clipSpaceCorrMatrix() const
extern "C" Q_DECL_EXPORT
QMatrix4x4 *ritual_ZNK9QRhiD3D1119clipSpaceCorrMatrixEv(
    const QRhiD3D11 *self) {
  self->clipSpaceCorrMatrix();
}

//  bool QRhiD3D11::isTextureFormatSupported(QRhiTexture::Format format,
//      QRhiTexture::Flags flags) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QRhiD3D1124isTextureFormatSupportedEN11QRhiTexture6FormatE6QFlagsINS0_4FlagEE(
    const QRhiD3D11 *self,
    QRhiTexture::Format format,
    int flags) {
  return self->isTextureFormatSupported(format, QFlags<QRhiTexture::Flag>::fromInt(flags));
}

//  bool QRhiD3D11::isFeatureSupported(QRhi::Feature feature) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QRhiD3D1118isFeatureSupportedEN4QRhi7FeatureE(
    const QRhiD3D11 *self,
    QRhi::Feature feature) {
  return self->isFeatureSupported(feature);
}

//  int QRhiD3D11::resourceLimit(QRhi::ResourceLimit limit) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QRhiD3D1113resourceLimitEN4QRhi13ResourceLimitE(
    const QRhiD3D11 *self,
    QRhi::ResourceLimit limit) {
  return self->resourceLimit(limit);
}

//  const QRhiNativeHandles *QRhiD3D11::nativeHandles()
extern "C" Q_DECL_EXPORT
const QRhiNativeHandles *ritual_ZN9QRhiD3D1113nativeHandlesEv(
    QRhiD3D11 *self) {
  return self->nativeHandles();
}

//  QRhiDriverInfo QRhiD3D11::driverInfo() const
extern "C" Q_DECL_EXPORT
QRhiDriverInfo *ritual_ZNK9QRhiD3D1110driverInfoEv(const QRhiD3D11 *self) {
  self->driverInfo();
}

//  QRhiStats QRhiD3D11::statistics()
extern "C" Q_DECL_EXPORT
QRhiStats *ritual_ZN9QRhiD3D1110statisticsEv(QRhiD3D11 *self) {
  self->statistics();
}

//  bool QRhiD3D11::makeThreadLocalNativeContextCurrent()
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QRhiD3D1135makeThreadLocalNativeContextCurrentEv(
    QRhiD3D11 *self) {
  return self->makeThreadLocalNativeContextCurrent();
}

//  void QRhiD3D11::setQueueSubmitParams(QRhiNativeHandles *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QRhiD3D1120setQueueSubmitParamsEP17QRhiNativeHandles(
    QRhiD3D11 *self,
    QRhiNativeHandles *params) {
  self->setQueueSubmitParams(params);
}

//  void QRhiD3D11::releaseCachedResources()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QRhiD3D1122releaseCachedResourcesEv(QRhiD3D11 *self) {
  self->releaseCachedResources();
}

//  bool QRhiD3D11::isDeviceLost() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QRhiD3D1112isDeviceLostEv(const QRhiD3D11 *self) {
  return self->isDeviceLost();
}

//  QByteArray QRhiD3D11::pipelineCacheData()
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN9QRhiD3D1117pipelineCacheDataEv(QRhiD3D11 *self) {
  self->pipelineCacheData();
}

//  void QRhiD3D11::setPipelineCacheData(const QByteArray &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QRhiD3D1120setPipelineCacheDataERK10QByteArray(
    QRhiD3D11 *self,
    const QByteArray *data) {
  self->setPipelineCacheData(*data);
}

#endif  // defined(Q_OS_WIN)
