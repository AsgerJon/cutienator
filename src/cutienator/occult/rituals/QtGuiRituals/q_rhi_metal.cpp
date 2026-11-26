//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qrhimetal_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if QT_CONFIG(metal)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qrhimetal_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qsize.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/rhi/qrhi.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qcolor.h>
#include <QtCore/qbytearray.h>
#include <QtGui/qmatrix4x4.h>
#include <QtCore/qlist.h>
#include <cstring>
#include <QtCore/QList>

//  A QRhiMetal that Python can take functions over in. Every QRhiMetal
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQRhiMetalCall0)(const void *, int, int *);
typedef void (*CuteQRhiMetalCall1)(const void *, int *);
typedef void * (*CuteQRhiMetalCall2)(const void *, int *);
typedef void * (*CuteQRhiMetalCall3)(const void *, int *);
typedef void * (*CuteQRhiMetalCall4)(const void *, int *);
typedef void * (*CuteQRhiMetalCall5)(const void *, int, int, quint32, int *);
typedef void * (*CuteQRhiMetalCall6)(const void *, int, const QSize *, int, int, int, int *);
typedef void * (*CuteQRhiMetalCall7)(const void *, int, const QSize *, int, int, int, int, int *);
typedef void * (*CuteQRhiMetalCall8)(const void *, int, int, int, int, int, int, int *);
typedef void * (*CuteQRhiMetalCall9)(const void *, const QRhiTextureRenderTargetDescription *, int, int *);
typedef void * (*CuteQRhiMetalCall10)(const void *, int *);
typedef void * (*CuteQRhiMetalCall11)(const void *, int *);
typedef int (*CuteQRhiMetalCall12)(const void *, QRhiSwapChain *, int, int *);
typedef int (*CuteQRhiMetalCall13)(const void *, QRhiSwapChain *, int, int *);
typedef int (*CuteQRhiMetalCall14)(const void *, int, int *);
typedef int (*CuteQRhiMetalCall15)(const void *, int *);
typedef void (*CuteQRhiMetalCall16)(const void *, QRhiCommandBuffer *, QRhiResourceUpdateBatch *, int *);
typedef void (*CuteQRhiMetalCall17)(const void *, QRhiCommandBuffer *, QRhiRenderTarget *, const QColor *, const QRhiDepthStencilClearValue *, QRhiResourceUpdateBatch *, int, int *);
typedef void (*CuteQRhiMetalCall18)(const void *, QRhiCommandBuffer *, QRhiResourceUpdateBatch *, int *);
typedef void (*CuteQRhiMetalCall19)(const void *, QRhiCommandBuffer *, QRhiGraphicsPipeline *, int *);
typedef void (*CuteQRhiMetalCall20)(const void *, QRhiCommandBuffer *, QRhiShaderResourceBindings *, int, const QRhiCommandBuffer::DynamicOffset *, int *);
typedef void (*CuteQRhiMetalCall21)(const void *, QRhiCommandBuffer *, int, int, const QRhiCommandBuffer::VertexInput *, QRhiBuffer *, quint32, int, int *);
typedef void (*CuteQRhiMetalCall22)(const void *, QRhiCommandBuffer *, const QRhiViewport *, int *);
typedef void (*CuteQRhiMetalCall23)(const void *, QRhiCommandBuffer *, const QRhiScissor *, int *);
typedef void (*CuteQRhiMetalCall24)(const void *, QRhiCommandBuffer *, const QColor *, int *);
typedef void (*CuteQRhiMetalCall25)(const void *, QRhiCommandBuffer *, quint32, int *);
typedef void (*CuteQRhiMetalCall26)(const void *, QRhiCommandBuffer *, const QSize *, int *);
typedef void (*CuteQRhiMetalCall27)(const void *, QRhiCommandBuffer *, quint32, quint32, quint32, quint32, int *);
typedef void (*CuteQRhiMetalCall28)(const void *, QRhiCommandBuffer *, quint32, quint32, quint32, qint32, quint32, int *);
typedef void (*CuteQRhiMetalCall29)(const void *, QRhiCommandBuffer *, QRhiBuffer *, quint32, quint32, quint32, int *);
typedef void (*CuteQRhiMetalCall30)(const void *, QRhiCommandBuffer *, QRhiBuffer *, quint32, quint32, quint32, int *);
typedef void (*CuteQRhiMetalCall31)(const void *, QRhiCommandBuffer *, const QByteArray *, int *);
typedef void (*CuteQRhiMetalCall32)(const void *, QRhiCommandBuffer *, int *);
typedef void (*CuteQRhiMetalCall33)(const void *, QRhiCommandBuffer *, const QByteArray *, int *);
typedef void (*CuteQRhiMetalCall34)(const void *, QRhiCommandBuffer *, QRhiResourceUpdateBatch *, int, int *);
typedef void (*CuteQRhiMetalCall35)(const void *, QRhiCommandBuffer *, QRhiResourceUpdateBatch *, int *);
typedef void (*CuteQRhiMetalCall36)(const void *, QRhiCommandBuffer *, QRhiComputePipeline *, int *);
typedef void (*CuteQRhiMetalCall37)(const void *, QRhiCommandBuffer *, int, int, int, int *);
typedef void * (*CuteQRhiMetalCall38)(const void *, QRhiCommandBuffer *, int *);
typedef void (*CuteQRhiMetalCall39)(const void *, QRhiCommandBuffer *, int *);
typedef void (*CuteQRhiMetalCall40)(const void *, QRhiCommandBuffer *, int *);
typedef double (*CuteQRhiMetalCall41)(const void *, QRhiCommandBuffer *, int *);
typedef int (*CuteQRhiMetalCall42)(const void *, int *);
typedef bool (*CuteQRhiMetalCall43)(const void *, int *);
typedef bool (*CuteQRhiMetalCall44)(const void *, int *);
typedef bool (*CuteQRhiMetalCall45)(const void *, int *);
typedef const QMatrix4x4 * (*CuteQRhiMetalCall46)(const void *, int *);
typedef bool (*CuteQRhiMetalCall47)(const void *, int, int, int *);
typedef bool (*CuteQRhiMetalCall48)(const void *, int, int *);
typedef int (*CuteQRhiMetalCall49)(const void *, int, int *);
typedef void * (*CuteQRhiMetalCall50)(const void *, int *);
typedef const QRhiDriverInfo * (*CuteQRhiMetalCall51)(const void *, int *);
typedef const QRhiStats * (*CuteQRhiMetalCall52)(const void *, int *);
typedef bool (*CuteQRhiMetalCall53)(const void *, int *);
typedef void (*CuteQRhiMetalCall54)(const void *, QRhiNativeHandles *, int *);
typedef void (*CuteQRhiMetalCall55)(const void *, int *);
typedef bool (*CuteQRhiMetalCall56)(const void *, int *);
typedef const QByteArray * (*CuteQRhiMetalCall57)(const void *, int *);
typedef void (*CuteQRhiMetalCall58)(const void *, const QByteArray *, int *);
class CuteQRhiMetal : public QRhiMetal {
public:
  using QRhiMetal::QRhiMetal;
  CuteQRhiMetal(const QRhiMetal & other) : QRhiMetal(other) {}
  void *taken[59] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN18QRhiImplementation6createE6QFlagsIN4QRhi4FlagEE")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QRhiImplementation7destroyEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QRhiImplementation22createGraphicsPipelineEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QRhiImplementation21createComputePipelineEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QRhiImplementation28createShaderResourceBindingsEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QRhiImplementation12createBufferEN10QRhiBuffer4TypeE6QFlagsINS0_9UsageFlagEEj")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QRhiImplementation18createRenderBufferEN16QRhiRenderBuffer4TypeERK5QSizei6QFlagsINS0_4FlagEEN11QRhiTexture6FormatE")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QRhiImplementation13createTextureEN11QRhiTexture6FormatERK5QSizeiii6QFlagsINS0_4FlagEE")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QRhiImplementation13createSamplerEN11QRhiSampler6FilterES1_S1_NS0_11AddressModeES2_S2_")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QRhiImplementation25createTextureRenderTargetERK34QRhiTextureRenderTargetDescription6QFlagsIN23QRhiTextureRenderTarget4FlagEE")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QRhiImplementation20createShadingRateMapEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QRhiImplementation15createSwapChainEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QRhiImplementation10beginFrameEP13QRhiSwapChain6QFlagsIN4QRhi14BeginFrameFlagEE")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QRhiImplementation8endFrameEP13QRhiSwapChain6QFlagsIN4QRhi12EndFrameFlagEE")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QRhiImplementation17endOffscreenFrameE6QFlagsIN4QRhi12EndFrameFlagEE")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QRhiImplementation6finishEv")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QRhiImplementation14resourceUpdateEP17QRhiCommandBufferP23QRhiResourceUpdateBatch")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QRhiImplementation9beginPassEP17QRhiCommandBufferP16QRhiRenderTargetRK6QColorRK26QRhiDepthStencilClearValueP23QRhiResourceUpdateBatch6QFlagsINS0_13BeginPassFlagEE")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QRhiImplementation7endPassEP17QRhiCommandBufferP23QRhiResourceUpdateBatch")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QRhiImplementation19setGraphicsPipelineEP17QRhiCommandBufferP20QRhiGraphicsPipeline")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QRhiImplementation18setShaderResourcesEP17QRhiCommandBufferP26QRhiShaderResourceBindingsiPKSt4pairIijE")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QRhiImplementation14setVertexInputEP17QRhiCommandBufferiiPKSt4pairIP10QRhiBufferjES4_jNS0_11IndexFormatE")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QRhiImplementation11setViewportEP17QRhiCommandBufferRK12QRhiViewport")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QRhiImplementation10setScissorEP17QRhiCommandBufferRK11QRhiScissor")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QRhiImplementation17setBlendConstantsEP17QRhiCommandBufferRK6QColor")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QRhiImplementation13setStencilRefEP17QRhiCommandBufferj")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QRhiImplementation14setShadingRateEP17QRhiCommandBufferRK5QSize")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QRhiImplementation4drawEP17QRhiCommandBufferjjjj")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QRhiImplementation11drawIndexedEP17QRhiCommandBufferjjjij")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QRhiImplementation12drawIndirectEP17QRhiCommandBufferP10QRhiBufferjjj")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QRhiImplementation19drawIndexedIndirectEP17QRhiCommandBufferP10QRhiBufferjjj")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QRhiImplementation14debugMarkBeginEP17QRhiCommandBufferRK10QByteArray")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QRhiImplementation12debugMarkEndEP17QRhiCommandBuffer")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QRhiImplementation12debugMarkMsgEP17QRhiCommandBufferRK10QByteArray")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QRhiImplementation16beginComputePassEP17QRhiCommandBufferP23QRhiResourceUpdateBatch6QFlagsINS0_13BeginPassFlagEE")) {
      taken[34] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QRhiImplementation14endComputePassEP17QRhiCommandBufferP23QRhiResourceUpdateBatch")) {
      taken[35] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QRhiImplementation18setComputePipelineEP17QRhiCommandBufferP19QRhiComputePipeline")) {
      taken[36] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QRhiImplementation8dispatchEP17QRhiCommandBufferiii")) {
      taken[37] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QRhiImplementation13nativeHandlesEP17QRhiCommandBuffer")) {
      taken[38] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QRhiImplementation13beginExternalEP17QRhiCommandBuffer")) {
      taken[39] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QRhiImplementation11endExternalEP17QRhiCommandBuffer")) {
      taken[40] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QRhiImplementation20lastCompletedGpuTimeEP17QRhiCommandBuffer")) {
      taken[41] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QRhiImplementation13ubufAlignmentEv")) {
      taken[42] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QRhiImplementation18isYUpInFramebufferEv")) {
      taken[43] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QRhiImplementation10isYUpInNDCEv")) {
      taken[44] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QRhiImplementation20isClipDepthZeroToOneEv")) {
      taken[45] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QRhiImplementation19clipSpaceCorrMatrixEv")) {
      taken[46] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QRhiImplementation24isTextureFormatSupportedEN11QRhiTexture6FormatE6QFlagsINS0_4FlagEE")) {
      taken[47] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QRhiImplementation18isFeatureSupportedEN4QRhi7FeatureE")) {
      taken[48] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QRhiImplementation13resourceLimitEN4QRhi13ResourceLimitE")) {
      taken[49] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QRhiImplementation13nativeHandlesEv")) {
      taken[50] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QRhiImplementation10driverInfoEv")) {
      taken[51] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QRhiImplementation10statisticsEv")) {
      taken[52] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QRhiImplementation35makeThreadLocalNativeContextCurrentEv")) {
      taken[53] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QRhiImplementation20setQueueSubmitParamsEP17QRhiNativeHandles")) {
      taken[54] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QRhiImplementation22releaseCachedResourcesEv")) {
      taken[55] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QRhiImplementation12isDeviceLostEv")) {
      taken[56] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QRhiImplementation17pipelineCacheDataEv")) {
      taken[57] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QRhiImplementation20setPipelineCacheDataERK10QByteArray")) {
      taken[58] = call;
      return true;
    }
    return false;
  }

  //  bool QRhiMetal::create(QRhi::Flags flags)
  bool create(QRhi::Flags flags) override {
    if (taken[0]) {
      int handled = 0;
      CuteQRhiMetalCall0 call = reinterpret_cast<CuteQRhiMetalCall0>(taken[0]);
      bool given = call(this, static_cast<int>(flags.toInt()), &handled);
      if (handled) return given;
    }
    return QRhiMetal::create(flags);
  }

  //  void QRhiMetal::destroy()
  void destroy() override {
    if (taken[1]) {
      int handled = 0;
      CuteQRhiMetalCall1 call = reinterpret_cast<CuteQRhiMetalCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QRhiMetal::destroy();
  }

  //  QRhiGraphicsPipeline *QRhiMetal::createGraphicsPipeline()
  QRhiGraphicsPipeline *createGraphicsPipeline() override {
    if (taken[2]) {
      int handled = 0;
      CuteQRhiMetalCall2 call = reinterpret_cast<CuteQRhiMetalCall2>(taken[2]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QRhiGraphicsPipeline *>(given);
    }
    return QRhiMetal::createGraphicsPipeline();
  }

  //  QRhiComputePipeline *QRhiMetal::createComputePipeline()
  QRhiComputePipeline *createComputePipeline() override {
    if (taken[3]) {
      int handled = 0;
      CuteQRhiMetalCall3 call = reinterpret_cast<CuteQRhiMetalCall3>(taken[3]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QRhiComputePipeline *>(given);
    }
    return QRhiMetal::createComputePipeline();
  }

  //  QRhiShaderResourceBindings *QRhiMetal::createShaderResourceBindings()
  QRhiShaderResourceBindings *createShaderResourceBindings() override {
    if (taken[4]) {
      int handled = 0;
      CuteQRhiMetalCall4 call = reinterpret_cast<CuteQRhiMetalCall4>(taken[4]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QRhiShaderResourceBindings *>(given);
    }
    return QRhiMetal::createShaderResourceBindings();
  }

  //  QRhiBuffer *QRhiMetal::createBuffer(QRhiBuffer::Type type,
  //      QRhiBuffer::UsageFlags usage, quint32 size)
  QRhiBuffer *createBuffer(
      QRhiBuffer::Type type,
      QRhiBuffer::UsageFlags usage,
      quint32 size) override {
    if (taken[5]) {
      int handled = 0;
      CuteQRhiMetalCall5 call = reinterpret_cast<CuteQRhiMetalCall5>(taken[5]);
      void * given = call(this, static_cast<int>(type), static_cast<int>(usage.toInt()), size, &handled);
      if (handled) return static_cast<QRhiBuffer *>(given);
    }
    return QRhiMetal::createBuffer(type, usage, size);
  }

  //  QRhiRenderBuffer
  //      *QRhiMetal::createRenderBuffer(QRhiRenderBuffer::Type type, const
  //      QSize &pixelSize, int sampleCount, QRhiRenderBuffer::Flags flags,
  //      QRhiTexture::Format backingFormatHint)
  QRhiRenderBuffer *createRenderBuffer(
      QRhiRenderBuffer::Type type,
      const QSize &pixelSize,
      int sampleCount,
      QRhiRenderBuffer::Flags flags,
      QRhiTexture::Format backingFormatHint) override {
    if (taken[6]) {
      int handled = 0;
      CuteQRhiMetalCall6 call = reinterpret_cast<CuteQRhiMetalCall6>(taken[6]);
      void * given = call(this, static_cast<int>(type), &pixelSize, sampleCount, static_cast<int>(flags.toInt()), static_cast<int>(backingFormatHint), &handled);
      if (handled) return static_cast<QRhiRenderBuffer *>(given);
    }
    return QRhiMetal::createRenderBuffer(type, pixelSize, sampleCount, flags, backingFormatHint);
  }

  //  QRhiTexture *QRhiMetal::createTexture(QRhiTexture::Format format,
  //      const QSize &pixelSize, int depth, int arraySize, int
  //      sampleCount, QRhiTexture::Flags flags)
  QRhiTexture *createTexture(
      QRhiTexture::Format format,
      const QSize &pixelSize,
      int depth,
      int arraySize,
      int sampleCount,
      QRhiTexture::Flags flags) override {
    if (taken[7]) {
      int handled = 0;
      CuteQRhiMetalCall7 call = reinterpret_cast<CuteQRhiMetalCall7>(taken[7]);
      void * given = call(this, static_cast<int>(format), &pixelSize, depth, arraySize, sampleCount, static_cast<int>(flags.toInt()), &handled);
      if (handled) return static_cast<QRhiTexture *>(given);
    }
    return QRhiMetal::createTexture(format, pixelSize, depth, arraySize, sampleCount, flags);
  }

  //  QRhiSampler *QRhiMetal::createSampler(QRhiSampler::Filter magFilter,
  //      QRhiSampler::Filter minFilter, QRhiSampler::Filter mipmapMode,
  //      QRhiSampler::AddressMode u, QRhiSampler::AddressMode v,
  //      QRhiSampler::AddressMode w)
  QRhiSampler *createSampler(
      QRhiSampler::Filter magFilter,
      QRhiSampler::Filter minFilter,
      QRhiSampler::Filter mipmapMode,
      QRhiSampler::AddressMode u,
      QRhiSampler::AddressMode v,
      QRhiSampler::AddressMode w) override {
    if (taken[8]) {
      int handled = 0;
      CuteQRhiMetalCall8 call = reinterpret_cast<CuteQRhiMetalCall8>(taken[8]);
      void * given = call(this, static_cast<int>(magFilter), static_cast<int>(minFilter), static_cast<int>(mipmapMode), static_cast<int>(u), static_cast<int>(v), static_cast<int>(w), &handled);
      if (handled) return static_cast<QRhiSampler *>(given);
    }
    return QRhiMetal::createSampler(magFilter, minFilter, mipmapMode, u, v, w);
  }

  //  QRhiTextureRenderTarget *QRhiMetal::createTextureRenderTarget(const
  //      QRhiTextureRenderTargetDescription &desc,
  //      QRhiTextureRenderTarget::Flags flags)
  QRhiTextureRenderTarget *createTextureRenderTarget(
      const QRhiTextureRenderTargetDescription &desc,
      QRhiTextureRenderTarget::Flags flags) override {
    if (taken[9]) {
      int handled = 0;
      CuteQRhiMetalCall9 call = reinterpret_cast<CuteQRhiMetalCall9>(taken[9]);
      void * given = call(this, &desc, static_cast<int>(flags.toInt()), &handled);
      if (handled) return static_cast<QRhiTextureRenderTarget *>(given);
    }
    return QRhiMetal::createTextureRenderTarget(desc, flags);
  }

  //  QRhiShadingRateMap *QRhiMetal::createShadingRateMap()
  QRhiShadingRateMap *createShadingRateMap() override {
    if (taken[10]) {
      int handled = 0;
      CuteQRhiMetalCall10 call = reinterpret_cast<CuteQRhiMetalCall10>(taken[10]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QRhiShadingRateMap *>(given);
    }
    return QRhiMetal::createShadingRateMap();
  }

  //  QRhiSwapChain *QRhiMetal::createSwapChain()
  QRhiSwapChain *createSwapChain() override {
    if (taken[11]) {
      int handled = 0;
      CuteQRhiMetalCall11 call = reinterpret_cast<CuteQRhiMetalCall11>(taken[11]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QRhiSwapChain *>(given);
    }
    return QRhiMetal::createSwapChain();
  }

  //  QRhi::FrameOpResult QRhiMetal::beginFrame(QRhiSwapChain *swapChain,
  //      QRhi::BeginFrameFlags flags)
  QRhi::FrameOpResult beginFrame(
      QRhiSwapChain *swapChain,
      QRhi::BeginFrameFlags flags) override {
    if (taken[12]) {
      int handled = 0;
      CuteQRhiMetalCall12 call = reinterpret_cast<CuteQRhiMetalCall12>(taken[12]);
      int given = call(this, swapChain, static_cast<int>(flags.toInt()), &handled);
      if (handled) return static_cast<QRhi::FrameOpResult>(given);
    }
    return QRhiMetal::beginFrame(swapChain, flags);
  }

  //  QRhi::FrameOpResult QRhiMetal::endFrame(QRhiSwapChain *swapChain,
  //      QRhi::EndFrameFlags flags)
  QRhi::FrameOpResult endFrame(
      QRhiSwapChain *swapChain,
      QRhi::EndFrameFlags flags) override {
    if (taken[13]) {
      int handled = 0;
      CuteQRhiMetalCall13 call = reinterpret_cast<CuteQRhiMetalCall13>(taken[13]);
      int given = call(this, swapChain, static_cast<int>(flags.toInt()), &handled);
      if (handled) return static_cast<QRhi::FrameOpResult>(given);
    }
    return QRhiMetal::endFrame(swapChain, flags);
  }

  //  QRhi::FrameOpResult QRhiMetal::endOffscreenFrame(QRhi::EndFrameFlags
  //      flags)
  QRhi::FrameOpResult endOffscreenFrame(QRhi::EndFrameFlags flags) override {
    if (taken[14]) {
      int handled = 0;
      CuteQRhiMetalCall14 call = reinterpret_cast<CuteQRhiMetalCall14>(taken[14]);
      int given = call(this, static_cast<int>(flags.toInt()), &handled);
      if (handled) return static_cast<QRhi::FrameOpResult>(given);
    }
    return QRhiMetal::endOffscreenFrame(flags);
  }

  //  QRhi::FrameOpResult QRhiMetal::finish()
  QRhi::FrameOpResult finish() override {
    if (taken[15]) {
      int handled = 0;
      CuteQRhiMetalCall15 call = reinterpret_cast<CuteQRhiMetalCall15>(taken[15]);
      int given = call(this, &handled);
      if (handled) return static_cast<QRhi::FrameOpResult>(given);
    }
    return QRhiMetal::finish();
  }

  //  void QRhiMetal::resourceUpdate(QRhiCommandBuffer *cb,
  //      QRhiResourceUpdateBatch *resourceUpdates)
  void resourceUpdate(
      QRhiCommandBuffer *cb,
      QRhiResourceUpdateBatch *resourceUpdates) override {
    if (taken[16]) {
      int handled = 0;
      CuteQRhiMetalCall16 call = reinterpret_cast<CuteQRhiMetalCall16>(taken[16]);
      call(this, cb, resourceUpdates, &handled);
      if (handled) return;
    }
    QRhiMetal::resourceUpdate(cb, resourceUpdates);
  }

  //  void QRhiMetal::beginPass(QRhiCommandBuffer *cb, QRhiRenderTarget
  //      *rt, const QColor &colorClearValue, const
  //      QRhiDepthStencilClearValue &depthStencilClearValue,
  //      QRhiResourceUpdateBatch *resourceUpdates,
  //      QRhiCommandBuffer::BeginPassFlags flags)
  void beginPass(
      QRhiCommandBuffer *cb,
      QRhiRenderTarget *rt,
      const QColor &colorClearValue,
      const QRhiDepthStencilClearValue &depthStencilClearValue,
      QRhiResourceUpdateBatch *resourceUpdates,
      QRhiCommandBuffer::BeginPassFlags flags) override {
    if (taken[17]) {
      int handled = 0;
      CuteQRhiMetalCall17 call = reinterpret_cast<CuteQRhiMetalCall17>(taken[17]);
      call(this, cb, rt, &colorClearValue, &depthStencilClearValue, resourceUpdates, static_cast<int>(flags.toInt()), &handled);
      if (handled) return;
    }
    QRhiMetal::beginPass(cb, rt, colorClearValue, depthStencilClearValue, resourceUpdates, flags);
  }

  //  void QRhiMetal::endPass(QRhiCommandBuffer *cb,
  //      QRhiResourceUpdateBatch *resourceUpdates)
  void endPass(
      QRhiCommandBuffer *cb,
      QRhiResourceUpdateBatch *resourceUpdates) override {
    if (taken[18]) {
      int handled = 0;
      CuteQRhiMetalCall18 call = reinterpret_cast<CuteQRhiMetalCall18>(taken[18]);
      call(this, cb, resourceUpdates, &handled);
      if (handled) return;
    }
    QRhiMetal::endPass(cb, resourceUpdates);
  }

  //  void QRhiMetal::setGraphicsPipeline(QRhiCommandBuffer *cb,
  //      QRhiGraphicsPipeline *ps)
  void setGraphicsPipeline(
      QRhiCommandBuffer *cb,
      QRhiGraphicsPipeline *ps) override {
    if (taken[19]) {
      int handled = 0;
      CuteQRhiMetalCall19 call = reinterpret_cast<CuteQRhiMetalCall19>(taken[19]);
      call(this, cb, ps, &handled);
      if (handled) return;
    }
    QRhiMetal::setGraphicsPipeline(cb, ps);
  }

  //  void QRhiMetal::setShaderResources(QRhiCommandBuffer *cb,
  //      QRhiShaderResourceBindings *srb, int dynamicOffsetCount, const
  //      QRhiCommandBuffer::DynamicOffset *dynamicOffsets)
  void setShaderResources(
      QRhiCommandBuffer *cb,
      QRhiShaderResourceBindings *srb,
      int dynamicOffsetCount,
      const QRhiCommandBuffer::DynamicOffset *dynamicOffsets) override {
    if (taken[20]) {
      int handled = 0;
      CuteQRhiMetalCall20 call = reinterpret_cast<CuteQRhiMetalCall20>(taken[20]);
      call(this, cb, srb, dynamicOffsetCount, dynamicOffsets, &handled);
      if (handled) return;
    }
    QRhiMetal::setShaderResources(cb, srb, dynamicOffsetCount, dynamicOffsets);
  }

  //  void QRhiMetal::setVertexInput(QRhiCommandBuffer *cb, int
  //      startBinding, int bindingCount, const
  //      QRhiCommandBuffer::VertexInput *bindings, QRhiBuffer *indexBuf,
  //      quint32 indexOffset, QRhiCommandBuffer::IndexFormat indexFormat)
  void setVertexInput(
      QRhiCommandBuffer *cb,
      int startBinding,
      int bindingCount,
      const QRhiCommandBuffer::VertexInput *bindings,
      QRhiBuffer *indexBuf,
      quint32 indexOffset,
      QRhiCommandBuffer::IndexFormat indexFormat) override {
    if (taken[21]) {
      int handled = 0;
      CuteQRhiMetalCall21 call = reinterpret_cast<CuteQRhiMetalCall21>(taken[21]);
      call(this, cb, startBinding, bindingCount, bindings, indexBuf, indexOffset, static_cast<int>(indexFormat), &handled);
      if (handled) return;
    }
    QRhiMetal::setVertexInput(cb, startBinding, bindingCount, bindings, indexBuf, indexOffset, indexFormat);
  }

  //  void QRhiMetal::setViewport(QRhiCommandBuffer *cb, const QRhiViewport
  //      &viewport)
  void setViewport(
      QRhiCommandBuffer *cb,
      const QRhiViewport &viewport) override {
    if (taken[22]) {
      int handled = 0;
      CuteQRhiMetalCall22 call = reinterpret_cast<CuteQRhiMetalCall22>(taken[22]);
      call(this, cb, &viewport, &handled);
      if (handled) return;
    }
    QRhiMetal::setViewport(cb, viewport);
  }

  //  void QRhiMetal::setScissor(QRhiCommandBuffer *cb, const QRhiScissor
  //      &scissor)
  void setScissor(
      QRhiCommandBuffer *cb,
      const QRhiScissor &scissor) override {
    if (taken[23]) {
      int handled = 0;
      CuteQRhiMetalCall23 call = reinterpret_cast<CuteQRhiMetalCall23>(taken[23]);
      call(this, cb, &scissor, &handled);
      if (handled) return;
    }
    QRhiMetal::setScissor(cb, scissor);
  }

  //  void QRhiMetal::setBlendConstants(QRhiCommandBuffer *cb, const QColor
  //      &c)
  void setBlendConstants(QRhiCommandBuffer *cb, const QColor &c) override {
    if (taken[24]) {
      int handled = 0;
      CuteQRhiMetalCall24 call = reinterpret_cast<CuteQRhiMetalCall24>(taken[24]);
      call(this, cb, &c, &handled);
      if (handled) return;
    }
    QRhiMetal::setBlendConstants(cb, c);
  }

  //  void QRhiMetal::setStencilRef(QRhiCommandBuffer *cb, quint32
  //      refValue)
  void setStencilRef(QRhiCommandBuffer *cb, quint32 refValue) override {
    if (taken[25]) {
      int handled = 0;
      CuteQRhiMetalCall25 call = reinterpret_cast<CuteQRhiMetalCall25>(taken[25]);
      call(this, cb, refValue, &handled);
      if (handled) return;
    }
    QRhiMetal::setStencilRef(cb, refValue);
  }

  //  void QRhiMetal::setShadingRate(QRhiCommandBuffer *cb, const QSize
  //      &coarsePixelSize)
  void setShadingRate(
      QRhiCommandBuffer *cb,
      const QSize &coarsePixelSize) override {
    if (taken[26]) {
      int handled = 0;
      CuteQRhiMetalCall26 call = reinterpret_cast<CuteQRhiMetalCall26>(taken[26]);
      call(this, cb, &coarsePixelSize, &handled);
      if (handled) return;
    }
    QRhiMetal::setShadingRate(cb, coarsePixelSize);
  }

  //  void QRhiMetal::draw(QRhiCommandBuffer *cb, quint32 vertexCount,
  //      quint32 instanceCount, quint32 firstVertex, quint32
  //      firstInstance)
  void draw(
      QRhiCommandBuffer *cb,
      quint32 vertexCount,
      quint32 instanceCount,
      quint32 firstVertex,
      quint32 firstInstance) override {
    if (taken[27]) {
      int handled = 0;
      CuteQRhiMetalCall27 call = reinterpret_cast<CuteQRhiMetalCall27>(taken[27]);
      call(this, cb, vertexCount, instanceCount, firstVertex, firstInstance, &handled);
      if (handled) return;
    }
    QRhiMetal::draw(cb, vertexCount, instanceCount, firstVertex, firstInstance);
  }

  //  void QRhiMetal::drawIndexed(QRhiCommandBuffer *cb, quint32
  //      indexCount, quint32 instanceCount, quint32 firstIndex, qint32
  //      vertexOffset, quint32 firstInstance)
  void drawIndexed(
      QRhiCommandBuffer *cb,
      quint32 indexCount,
      quint32 instanceCount,
      quint32 firstIndex,
      qint32 vertexOffset,
      quint32 firstInstance) override {
    if (taken[28]) {
      int handled = 0;
      CuteQRhiMetalCall28 call = reinterpret_cast<CuteQRhiMetalCall28>(taken[28]);
      call(this, cb, indexCount, instanceCount, firstIndex, vertexOffset, firstInstance, &handled);
      if (handled) return;
    }
    QRhiMetal::drawIndexed(cb, indexCount, instanceCount, firstIndex, vertexOffset, firstInstance);
  }

  //  void QRhiMetal::drawIndirect(QRhiCommandBuffer *cb, QRhiBuffer
  //      *indirectBuffer, quint32 indirectBufferOffset, quint32 drawCount,
  //      quint32 stride)
  void drawIndirect(
      QRhiCommandBuffer *cb,
      QRhiBuffer *indirectBuffer,
      quint32 indirectBufferOffset,
      quint32 drawCount,
      quint32 stride) override {
    if (taken[29]) {
      int handled = 0;
      CuteQRhiMetalCall29 call = reinterpret_cast<CuteQRhiMetalCall29>(taken[29]);
      call(this, cb, indirectBuffer, indirectBufferOffset, drawCount, stride, &handled);
      if (handled) return;
    }
    QRhiMetal::drawIndirect(cb, indirectBuffer, indirectBufferOffset, drawCount, stride);
  }

  //  void QRhiMetal::drawIndexedIndirect(QRhiCommandBuffer *cb, QRhiBuffer
  //      *indirectBuffer, quint32 indirectBufferOffset, quint32 drawCount,
  //      quint32 stride)
  void drawIndexedIndirect(
      QRhiCommandBuffer *cb,
      QRhiBuffer *indirectBuffer,
      quint32 indirectBufferOffset,
      quint32 drawCount,
      quint32 stride) override {
    if (taken[30]) {
      int handled = 0;
      CuteQRhiMetalCall30 call = reinterpret_cast<CuteQRhiMetalCall30>(taken[30]);
      call(this, cb, indirectBuffer, indirectBufferOffset, drawCount, stride, &handled);
      if (handled) return;
    }
    QRhiMetal::drawIndexedIndirect(cb, indirectBuffer, indirectBufferOffset, drawCount, stride);
  }

  //  void QRhiMetal::debugMarkBegin(QRhiCommandBuffer *cb, const
  //      QByteArray &name)
  void debugMarkBegin(
      QRhiCommandBuffer *cb,
      const QByteArray &name) override {
    if (taken[31]) {
      int handled = 0;
      CuteQRhiMetalCall31 call = reinterpret_cast<CuteQRhiMetalCall31>(taken[31]);
      call(this, cb, &name, &handled);
      if (handled) return;
    }
    QRhiMetal::debugMarkBegin(cb, name);
  }

  //  void QRhiMetal::debugMarkEnd(QRhiCommandBuffer *cb)
  void debugMarkEnd(QRhiCommandBuffer *cb) override {
    if (taken[32]) {
      int handled = 0;
      CuteQRhiMetalCall32 call = reinterpret_cast<CuteQRhiMetalCall32>(taken[32]);
      call(this, cb, &handled);
      if (handled) return;
    }
    QRhiMetal::debugMarkEnd(cb);
  }

  //  void QRhiMetal::debugMarkMsg(QRhiCommandBuffer *cb, const QByteArray
  //      &msg)
  void debugMarkMsg(QRhiCommandBuffer *cb, const QByteArray &msg) override {
    if (taken[33]) {
      int handled = 0;
      CuteQRhiMetalCall33 call = reinterpret_cast<CuteQRhiMetalCall33>(taken[33]);
      call(this, cb, &msg, &handled);
      if (handled) return;
    }
    QRhiMetal::debugMarkMsg(cb, msg);
  }

  //  void QRhiMetal::beginComputePass(QRhiCommandBuffer *cb,
  //      QRhiResourceUpdateBatch *resourceUpdates,
  //      QRhiCommandBuffer::BeginPassFlags flags)
  void beginComputePass(
      QRhiCommandBuffer *cb,
      QRhiResourceUpdateBatch *resourceUpdates,
      QRhiCommandBuffer::BeginPassFlags flags) override {
    if (taken[34]) {
      int handled = 0;
      CuteQRhiMetalCall34 call = reinterpret_cast<CuteQRhiMetalCall34>(taken[34]);
      call(this, cb, resourceUpdates, static_cast<int>(flags.toInt()), &handled);
      if (handled) return;
    }
    QRhiMetal::beginComputePass(cb, resourceUpdates, flags);
  }

  //  void QRhiMetal::endComputePass(QRhiCommandBuffer *cb,
  //      QRhiResourceUpdateBatch *resourceUpdates)
  void endComputePass(
      QRhiCommandBuffer *cb,
      QRhiResourceUpdateBatch *resourceUpdates) override {
    if (taken[35]) {
      int handled = 0;
      CuteQRhiMetalCall35 call = reinterpret_cast<CuteQRhiMetalCall35>(taken[35]);
      call(this, cb, resourceUpdates, &handled);
      if (handled) return;
    }
    QRhiMetal::endComputePass(cb, resourceUpdates);
  }

  //  void QRhiMetal::setComputePipeline(QRhiCommandBuffer *cb,
  //      QRhiComputePipeline *ps)
  void setComputePipeline(
      QRhiCommandBuffer *cb,
      QRhiComputePipeline *ps) override {
    if (taken[36]) {
      int handled = 0;
      CuteQRhiMetalCall36 call = reinterpret_cast<CuteQRhiMetalCall36>(taken[36]);
      call(this, cb, ps, &handled);
      if (handled) return;
    }
    QRhiMetal::setComputePipeline(cb, ps);
  }

  //  void QRhiMetal::dispatch(QRhiCommandBuffer *cb, int x, int y, int z)
  void dispatch(QRhiCommandBuffer *cb, int x, int y, int z) override {
    if (taken[37]) {
      int handled = 0;
      CuteQRhiMetalCall37 call = reinterpret_cast<CuteQRhiMetalCall37>(taken[37]);
      call(this, cb, x, y, z, &handled);
      if (handled) return;
    }
    QRhiMetal::dispatch(cb, x, y, z);
  }

  //  const QRhiNativeHandles *QRhiMetal::nativeHandles(QRhiCommandBuffer
  //      *cb)
  const QRhiNativeHandles *nativeHandles(QRhiCommandBuffer *cb) override {
    if (taken[38]) {
      int handled = 0;
      CuteQRhiMetalCall38 call = reinterpret_cast<CuteQRhiMetalCall38>(taken[38]);
      void * given = call(this, cb, &handled);
      if (handled) return static_cast<const QRhiNativeHandles *>(given);
    }
    return QRhiMetal::nativeHandles(cb);
  }

  //  void QRhiMetal::beginExternal(QRhiCommandBuffer *cb)
  void beginExternal(QRhiCommandBuffer *cb) override {
    if (taken[39]) {
      int handled = 0;
      CuteQRhiMetalCall39 call = reinterpret_cast<CuteQRhiMetalCall39>(taken[39]);
      call(this, cb, &handled);
      if (handled) return;
    }
    QRhiMetal::beginExternal(cb);
  }

  //  void QRhiMetal::endExternal(QRhiCommandBuffer *cb)
  void endExternal(QRhiCommandBuffer *cb) override {
    if (taken[40]) {
      int handled = 0;
      CuteQRhiMetalCall40 call = reinterpret_cast<CuteQRhiMetalCall40>(taken[40]);
      call(this, cb, &handled);
      if (handled) return;
    }
    QRhiMetal::endExternal(cb);
  }

  //  double QRhiMetal::lastCompletedGpuTime(QRhiCommandBuffer *cb)
  double lastCompletedGpuTime(QRhiCommandBuffer *cb) override {
    if (taken[41]) {
      int handled = 0;
      CuteQRhiMetalCall41 call = reinterpret_cast<CuteQRhiMetalCall41>(taken[41]);
      double given = call(this, cb, &handled);
      if (handled) return given;
    }
    return QRhiMetal::lastCompletedGpuTime(cb);
  }

  //  int QRhiMetal::ubufAlignment() const
  int ubufAlignment() const override {
    if (taken[42]) {
      int handled = 0;
      CuteQRhiMetalCall42 call = reinterpret_cast<CuteQRhiMetalCall42>(taken[42]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QRhiMetal::ubufAlignment();
  }

  //  bool QRhiMetal::isYUpInFramebuffer() const
  bool isYUpInFramebuffer() const override {
    if (taken[43]) {
      int handled = 0;
      CuteQRhiMetalCall43 call = reinterpret_cast<CuteQRhiMetalCall43>(taken[43]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QRhiMetal::isYUpInFramebuffer();
  }

  //  bool QRhiMetal::isYUpInNDC() const
  bool isYUpInNDC() const override {
    if (taken[44]) {
      int handled = 0;
      CuteQRhiMetalCall44 call = reinterpret_cast<CuteQRhiMetalCall44>(taken[44]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QRhiMetal::isYUpInNDC();
  }

  //  bool QRhiMetal::isClipDepthZeroToOne() const
  bool isClipDepthZeroToOne() const override {
    if (taken[45]) {
      int handled = 0;
      CuteQRhiMetalCall45 call = reinterpret_cast<CuteQRhiMetalCall45>(taken[45]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QRhiMetal::isClipDepthZeroToOne();
  }

  //  QMatrix4x4 QRhiMetal::clipSpaceCorrMatrix() const
  QMatrix4x4 clipSpaceCorrMatrix() const override {
    if (taken[46]) {
      int handled = 0;
      CuteQRhiMetalCall46 call = reinterpret_cast<CuteQRhiMetalCall46>(taken[46]);
      const QMatrix4x4 * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QRhiMetal::clipSpaceCorrMatrix();
  }

  //  bool QRhiMetal::isTextureFormatSupported(QRhiTexture::Format format,
  //      QRhiTexture::Flags flags) const
  bool isTextureFormatSupported(
      QRhiTexture::Format format,
      QRhiTexture::Flags flags) const override {
    if (taken[47]) {
      int handled = 0;
      CuteQRhiMetalCall47 call = reinterpret_cast<CuteQRhiMetalCall47>(taken[47]);
      bool given = call(this, static_cast<int>(format), static_cast<int>(flags.toInt()), &handled);
      if (handled) return given;
    }
    return QRhiMetal::isTextureFormatSupported(format, flags);
  }

  //  bool QRhiMetal::isFeatureSupported(QRhi::Feature feature) const
  bool isFeatureSupported(QRhi::Feature feature) const override {
    if (taken[48]) {
      int handled = 0;
      CuteQRhiMetalCall48 call = reinterpret_cast<CuteQRhiMetalCall48>(taken[48]);
      bool given = call(this, static_cast<int>(feature), &handled);
      if (handled) return given;
    }
    return QRhiMetal::isFeatureSupported(feature);
  }

  //  int QRhiMetal::resourceLimit(QRhi::ResourceLimit limit) const
  int resourceLimit(QRhi::ResourceLimit limit) const override {
    if (taken[49]) {
      int handled = 0;
      CuteQRhiMetalCall49 call = reinterpret_cast<CuteQRhiMetalCall49>(taken[49]);
      int given = call(this, static_cast<int>(limit), &handled);
      if (handled) return given;
    }
    return QRhiMetal::resourceLimit(limit);
  }

  //  const QRhiNativeHandles *QRhiMetal::nativeHandles()
  const QRhiNativeHandles *nativeHandles() override {
    if (taken[50]) {
      int handled = 0;
      CuteQRhiMetalCall50 call = reinterpret_cast<CuteQRhiMetalCall50>(taken[50]);
      void * given = call(this, &handled);
      if (handled) return static_cast<const QRhiNativeHandles *>(given);
    }
    return QRhiMetal::nativeHandles();
  }

  //  QRhiDriverInfo QRhiMetal::driverInfo() const
  QRhiDriverInfo driverInfo() const override {
    if (taken[51]) {
      int handled = 0;
      CuteQRhiMetalCall51 call = reinterpret_cast<CuteQRhiMetalCall51>(taken[51]);
      const QRhiDriverInfo * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QRhiMetal::driverInfo();
  }

  //  QRhiStats QRhiMetal::statistics()
  QRhiStats statistics() override {
    if (taken[52]) {
      int handled = 0;
      CuteQRhiMetalCall52 call = reinterpret_cast<CuteQRhiMetalCall52>(taken[52]);
      const QRhiStats * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QRhiMetal::statistics();
  }

  //  bool QRhiMetal::makeThreadLocalNativeContextCurrent()
  bool makeThreadLocalNativeContextCurrent() override {
    if (taken[53]) {
      int handled = 0;
      CuteQRhiMetalCall53 call = reinterpret_cast<CuteQRhiMetalCall53>(taken[53]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QRhiMetal::makeThreadLocalNativeContextCurrent();
  }

  //  void QRhiMetal::setQueueSubmitParams(QRhiNativeHandles *params)
  void setQueueSubmitParams(QRhiNativeHandles *params) override {
    if (taken[54]) {
      int handled = 0;
      CuteQRhiMetalCall54 call = reinterpret_cast<CuteQRhiMetalCall54>(taken[54]);
      call(this, params, &handled);
      if (handled) return;
    }
    QRhiMetal::setQueueSubmitParams(params);
  }

  //  void QRhiMetal::releaseCachedResources()
  void releaseCachedResources() override {
    if (taken[55]) {
      int handled = 0;
      CuteQRhiMetalCall55 call = reinterpret_cast<CuteQRhiMetalCall55>(taken[55]);
      call(this, &handled);
      if (handled) return;
    }
    QRhiMetal::releaseCachedResources();
  }

  //  bool QRhiMetal::isDeviceLost() const
  bool isDeviceLost() const override {
    if (taken[56]) {
      int handled = 0;
      CuteQRhiMetalCall56 call = reinterpret_cast<CuteQRhiMetalCall56>(taken[56]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QRhiMetal::isDeviceLost();
  }

  //  QByteArray QRhiMetal::pipelineCacheData()
  QByteArray pipelineCacheData() override {
    if (taken[57]) {
      int handled = 0;
      CuteQRhiMetalCall57 call = reinterpret_cast<CuteQRhiMetalCall57>(taken[57]);
      const QByteArray * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QRhiMetal::pipelineCacheData();
  }

  //  void QRhiMetal::setPipelineCacheData(const QByteArray &data)
  void setPipelineCacheData(const QByteArray &data) override {
    if (taken[58]) {
      int handled = 0;
      CuteQRhiMetalCall58 call = reinterpret_cast<CuteQRhiMetalCall58>(taken[58]);
      call(this, &data, &handled);
      if (handled) return;
    }
    QRhiMetal::setPipelineCacheData(data);
  }
};

//  bool QRhiMetal::create(QRhi::Flags flags)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QRhiMetal6createE6QFlagsIN4QRhi4FlagEE(
    QRhiMetal *self,
    int flags) {
  return self->create(QFlags<QRhi::Flag>::fromInt(flags));
}

//  void QRhiMetal::destroy()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QRhiMetal7destroyEv(QRhiMetal *self) {
  self->destroy();
}

//  QRhiGraphicsPipeline *QRhiMetal::createGraphicsPipeline()
extern "C" Q_DECL_EXPORT
QRhiGraphicsPipeline *ritual_ZN9QRhiMetal22createGraphicsPipelineEv(
    QRhiMetal *self) {
  return self->createGraphicsPipeline();
}

//  QRhiComputePipeline *QRhiMetal::createComputePipeline()
extern "C" Q_DECL_EXPORT
QRhiComputePipeline *ritual_ZN9QRhiMetal21createComputePipelineEv(
    QRhiMetal *self) {
  return self->createComputePipeline();
}

//  QRhiShaderResourceBindings *QRhiMetal::createShaderResourceBindings()
extern "C" Q_DECL_EXPORT
QRhiShaderResourceBindings *ritual_ZN9QRhiMetal28createShaderResourceBindingsEv(
    QRhiMetal *self) {
  return self->createShaderResourceBindings();
}

//  QRhiBuffer *QRhiMetal::createBuffer(QRhiBuffer::Type type,
//      QRhiBuffer::UsageFlags usage, quint32 size)
extern "C" Q_DECL_EXPORT
QRhiBuffer *ritual_ZN9QRhiMetal12createBufferEN10QRhiBuffer4TypeE6QFlagsINS0_9UsageFlagEEj(
    QRhiMetal *self,
    QRhiBuffer::Type type,
    int usage,
    quint32 size) {
  return self->createBuffer(
      type,
      QFlags<QRhiBuffer::UsageFlag>::fromInt(usage),
      size);
}

//  QRhiRenderBuffer *QRhiMetal::createRenderBuffer(QRhiRenderBuffer::Type
//      type, const QSize &pixelSize, int sampleCount,
//      QRhiRenderBuffer::Flags flags, QRhiTexture::Format backingFormatHint)
extern "C" Q_DECL_EXPORT
QRhiRenderBuffer *ritual_ZN9QRhiMetal18createRenderBufferEN16QRhiRenderBuffer4TypeERK5QSizei6QFlagsINS0_4FlagEEN11QRhiTexture6FormatE(
    QRhiMetal *self,
    QRhiRenderBuffer::Type type,
    const QSize *pixelSize,
    int sampleCount,
    int flags,
    QRhiTexture::Format backingFormatHint) {
  return self->createRenderBuffer(
      type,
      *pixelSize,
      sampleCount,
      QFlags<QRhiRenderBuffer::Flag>::fromInt(flags),
      backingFormatHint);
}

//  QRhiTexture *QRhiMetal::createTexture(QRhiTexture::Format format, const
//      QSize &pixelSize, int depth, int arraySize, int sampleCount,
//      QRhiTexture::Flags flags)
extern "C" Q_DECL_EXPORT
QRhiTexture *ritual_ZN9QRhiMetal13createTextureEN11QRhiTexture6FormatERK5QSizeiii6QFlagsINS0_4FlagEE(
    QRhiMetal *self,
    QRhiTexture::Format format,
    const QSize *pixelSize,
    int depth,
    int arraySize,
    int sampleCount,
    int flags) {
  return self->createTexture(
      format,
      *pixelSize,
      depth,
      arraySize,
      sampleCount,
      QFlags<QRhiTexture::Flag>::fromInt(flags));
}

//  QRhiSampler *QRhiMetal::createSampler(QRhiSampler::Filter magFilter,
//      QRhiSampler::Filter minFilter, QRhiSampler::Filter mipmapMode,
//      QRhiSampler::AddressMode u, QRhiSampler::AddressMode v,
//      QRhiSampler::AddressMode w)
extern "C" Q_DECL_EXPORT
QRhiSampler *ritual_ZN9QRhiMetal13createSamplerEN11QRhiSampler6FilterES1_S1_NS0_11AddressModeES2_S2_(
    QRhiMetal *self,
    QRhiSampler::Filter magFilter,
    QRhiSampler::Filter minFilter,
    QRhiSampler::Filter mipmapMode,
    QRhiSampler::AddressMode u,
    QRhiSampler::AddressMode v,
    QRhiSampler::AddressMode w) {
  return self->createSampler(magFilter, minFilter, mipmapMode, u, v, w);
}

//  QRhiTextureRenderTarget *QRhiMetal::createTextureRenderTarget(const
//      QRhiTextureRenderTargetDescription &desc,
//      QRhiTextureRenderTarget::Flags flags)
extern "C" Q_DECL_EXPORT
QRhiTextureRenderTarget *ritual_ZN9QRhiMetal25createTextureRenderTargetERK34QRhiTextureRenderTargetDescription6QFlagsIN23QRhiTextureRenderTarget4FlagEE(
    QRhiMetal *self,
    const QRhiTextureRenderTargetDescription *desc,
    int flags) {
  return self->createTextureRenderTarget(
      *desc,
      QFlags<QRhiTextureRenderTarget::Flag>::fromInt(flags));
}

//  QRhiShadingRateMap *QRhiMetal::createShadingRateMap()
extern "C" Q_DECL_EXPORT
QRhiShadingRateMap *ritual_ZN9QRhiMetal20createShadingRateMapEv(
    QRhiMetal *self) {
  return self->createShadingRateMap();
}

//  QRhiSwapChain *QRhiMetal::createSwapChain()
extern "C" Q_DECL_EXPORT
QRhiSwapChain *ritual_ZN9QRhiMetal15createSwapChainEv(QRhiMetal *self) {
  return self->createSwapChain();
}

//  QRhi::FrameOpResult QRhiMetal::beginFrame(QRhiSwapChain *swapChain,
//      QRhi::BeginFrameFlags flags)
extern "C" Q_DECL_EXPORT
QRhi::FrameOpResult ritual_ZN9QRhiMetal10beginFrameEP13QRhiSwapChain6QFlagsIN4QRhi14BeginFrameFlagEE(
    QRhiMetal *self,
    QRhiSwapChain *swapChain,
    int flags) {
  return self->beginFrame(
      swapChain,
      QFlags<QRhi::BeginFrameFlag>::fromInt(flags));
}

//  QRhi::FrameOpResult QRhiMetal::endFrame(QRhiSwapChain *swapChain,
//      QRhi::EndFrameFlags flags)
extern "C" Q_DECL_EXPORT
QRhi::FrameOpResult ritual_ZN9QRhiMetal8endFrameEP13QRhiSwapChain6QFlagsIN4QRhi12EndFrameFlagEE(
    QRhiMetal *self,
    QRhiSwapChain *swapChain,
    int flags) {
  return self->endFrame(
      swapChain,
      QFlags<QRhi::EndFrameFlag>::fromInt(flags));
}

//  QRhi::FrameOpResult QRhiMetal::beginOffscreenFrame(QRhiCommandBuffer
//      **cb, QRhi::BeginFrameFlags flags)
extern "C" Q_DECL_EXPORT
QRhi::FrameOpResult ritual_ZN9QRhiMetal19beginOffscreenFrameEPP17QRhiCommandBuffer6QFlagsIN4QRhi14BeginFrameFlagEE(
    QRhiMetal *self,
    QRhiCommandBuffer **cb,
    int flags) {
  return self->beginOffscreenFrame(
      cb,
      QFlags<QRhi::BeginFrameFlag>::fromInt(flags));
}

//  QRhi::FrameOpResult QRhiMetal::endOffscreenFrame(QRhi::EndFrameFlags
//      flags)
extern "C" Q_DECL_EXPORT
QRhi::FrameOpResult ritual_ZN9QRhiMetal17endOffscreenFrameE6QFlagsIN4QRhi12EndFrameFlagEE(
    QRhiMetal *self,
    int flags) {
  return self->endOffscreenFrame(QFlags<QRhi::EndFrameFlag>::fromInt(flags));
}

//  QRhi::FrameOpResult QRhiMetal::finish()
extern "C" Q_DECL_EXPORT
QRhi::FrameOpResult ritual_ZN9QRhiMetal6finishEv(QRhiMetal *self) {
  return self->finish();
}

//  void QRhiMetal::resourceUpdate(QRhiCommandBuffer *cb,
//      QRhiResourceUpdateBatch *resourceUpdates)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QRhiMetal14resourceUpdateEP17QRhiCommandBufferP23QRhiResourceUpdateBatch(
    QRhiMetal *self,
    QRhiCommandBuffer *cb,
    QRhiResourceUpdateBatch *resourceUpdates) {
  self->resourceUpdate(cb, resourceUpdates);
}

//  void QRhiMetal::beginPass(QRhiCommandBuffer *cb, QRhiRenderTarget *rt,
//      const QColor &colorClearValue, const QRhiDepthStencilClearValue
//      &depthStencilClearValue, QRhiResourceUpdateBatch *resourceUpdates,
//      QRhiCommandBuffer::BeginPassFlags flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QRhiMetal9beginPassEP17QRhiCommandBufferP16QRhiRenderTargetRK6QColorRK26QRhiDepthStencilClearValueP23QRhiResourceUpdateBatch6QFlagsINS0_13BeginPassFlagEE(
    QRhiMetal *self,
    QRhiCommandBuffer *cb,
    QRhiRenderTarget *rt,
    const QColor *colorClearValue,
    const QRhiDepthStencilClearValue *depthStencilClearValue,
    QRhiResourceUpdateBatch *resourceUpdates,
    int flags) {
  self->beginPass(
      cb,
      rt,
      *colorClearValue,
      *depthStencilClearValue,
      resourceUpdates,
      QFlags<QRhiCommandBuffer::BeginPassFlag>::fromInt(flags));
}

//  void QRhiMetal::endPass(QRhiCommandBuffer *cb, QRhiResourceUpdateBatch
//      *resourceUpdates)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QRhiMetal7endPassEP17QRhiCommandBufferP23QRhiResourceUpdateBatch(
    QRhiMetal *self,
    QRhiCommandBuffer *cb,
    QRhiResourceUpdateBatch *resourceUpdates) {
  self->endPass(cb, resourceUpdates);
}

//  void QRhiMetal::setGraphicsPipeline(QRhiCommandBuffer *cb,
//      QRhiGraphicsPipeline *ps)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QRhiMetal19setGraphicsPipelineEP17QRhiCommandBufferP20QRhiGraphicsPipeline(
    QRhiMetal *self,
    QRhiCommandBuffer *cb,
    QRhiGraphicsPipeline *ps) {
  self->setGraphicsPipeline(cb, ps);
}

//  void QRhiMetal::setShaderResources(QRhiCommandBuffer *cb,
//      QRhiShaderResourceBindings *srb, int dynamicOffsetCount, const
//      QRhiCommandBuffer::DynamicOffset *dynamicOffsets)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QRhiMetal18setShaderResourcesEP17QRhiCommandBufferP26QRhiShaderResourceBindingsiPKSt4pairIijE(
    QRhiMetal *self,
    QRhiCommandBuffer *cb,
    QRhiShaderResourceBindings *srb,
    int dynamicOffsetCount,
    const QRhiCommandBuffer::DynamicOffset *dynamicOffsets) {
  self->setShaderResources(cb, srb, dynamicOffsetCount, dynamicOffsets);
}

//  void QRhiMetal::setVertexInput(QRhiCommandBuffer *cb, int startBinding,
//      int bindingCount, const QRhiCommandBuffer::VertexInput *bindings,
//      QRhiBuffer *indexBuf, quint32 indexOffset,
//      QRhiCommandBuffer::IndexFormat indexFormat)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QRhiMetal14setVertexInputEP17QRhiCommandBufferiiPKSt4pairIP10QRhiBufferjES4_jNS0_11IndexFormatE(
    QRhiMetal *self,
    QRhiCommandBuffer *cb,
    int startBinding,
    int bindingCount,
    const QRhiCommandBuffer::VertexInput *bindings,
    QRhiBuffer *indexBuf,
    quint32 indexOffset,
    QRhiCommandBuffer::IndexFormat indexFormat) {
  self->setVertexInput(
      cb,
      startBinding,
      bindingCount,
      bindings,
      indexBuf,
      indexOffset,
      indexFormat);
}

//  void QRhiMetal::setViewport(QRhiCommandBuffer *cb, const QRhiViewport
//      &viewport)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QRhiMetal11setViewportEP17QRhiCommandBufferRK12QRhiViewport(
    QRhiMetal *self,
    QRhiCommandBuffer *cb,
    const QRhiViewport *viewport) {
  self->setViewport(cb, *viewport);
}

//  void QRhiMetal::setScissor(QRhiCommandBuffer *cb, const QRhiScissor
//      &scissor)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QRhiMetal10setScissorEP17QRhiCommandBufferRK11QRhiScissor(
    QRhiMetal *self,
    QRhiCommandBuffer *cb,
    const QRhiScissor *scissor) {
  self->setScissor(cb, *scissor);
}

//  void QRhiMetal::setBlendConstants(QRhiCommandBuffer *cb, const QColor &c)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QRhiMetal17setBlendConstantsEP17QRhiCommandBufferRK6QColor(
    QRhiMetal *self,
    QRhiCommandBuffer *cb,
    const QColor *c) {
  self->setBlendConstants(cb, *c);
}

//  void QRhiMetal::setStencilRef(QRhiCommandBuffer *cb, quint32 refValue)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QRhiMetal13setStencilRefEP17QRhiCommandBufferj(
    QRhiMetal *self,
    QRhiCommandBuffer *cb,
    quint32 refValue) {
  self->setStencilRef(cb, refValue);
}

//  void QRhiMetal::setShadingRate(QRhiCommandBuffer *cb, const QSize
//      &coarsePixelSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QRhiMetal14setShadingRateEP17QRhiCommandBufferRK5QSize(
    QRhiMetal *self,
    QRhiCommandBuffer *cb,
    const QSize *coarsePixelSize) {
  self->setShadingRate(cb, *coarsePixelSize);
}

//  void QRhiMetal::draw(QRhiCommandBuffer *cb, quint32 vertexCount, quint32
//      instanceCount, quint32 firstVertex, quint32 firstInstance)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QRhiMetal4drawEP17QRhiCommandBufferjjjj(
    QRhiMetal *self,
    QRhiCommandBuffer *cb,
    quint32 vertexCount,
    quint32 instanceCount,
    quint32 firstVertex,
    quint32 firstInstance) {
  self->draw(cb, vertexCount, instanceCount, firstVertex, firstInstance);
}

//  void QRhiMetal::drawIndexed(QRhiCommandBuffer *cb, quint32 indexCount,
//      quint32 instanceCount, quint32 firstIndex, qint32 vertexOffset,
//      quint32 firstInstance)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QRhiMetal11drawIndexedEP17QRhiCommandBufferjjjij(
    QRhiMetal *self,
    QRhiCommandBuffer *cb,
    quint32 indexCount,
    quint32 instanceCount,
    quint32 firstIndex,
    qint32 vertexOffset,
    quint32 firstInstance) {
  self->drawIndexed(
      cb,
      indexCount,
      instanceCount,
      firstIndex,
      vertexOffset,
      firstInstance);
}

//  void QRhiMetal::drawIndirect(QRhiCommandBuffer *cb, QRhiBuffer
//      *indirectBuffer, quint32 indirectBufferOffset, quint32 drawCount,
//      quint32 stride)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QRhiMetal12drawIndirectEP17QRhiCommandBufferP10QRhiBufferjjj(
    QRhiMetal *self,
    QRhiCommandBuffer *cb,
    QRhiBuffer *indirectBuffer,
    quint32 indirectBufferOffset,
    quint32 drawCount,
    quint32 stride) {
  self->drawIndirect(
      cb,
      indirectBuffer,
      indirectBufferOffset,
      drawCount,
      stride);
}

//  void QRhiMetal::drawIndexedIndirect(QRhiCommandBuffer *cb, QRhiBuffer
//      *indirectBuffer, quint32 indirectBufferOffset, quint32 drawCount,
//      quint32 stride)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QRhiMetal19drawIndexedIndirectEP17QRhiCommandBufferP10QRhiBufferjjj(
    QRhiMetal *self,
    QRhiCommandBuffer *cb,
    QRhiBuffer *indirectBuffer,
    quint32 indirectBufferOffset,
    quint32 drawCount,
    quint32 stride) {
  self->drawIndexedIndirect(
      cb,
      indirectBuffer,
      indirectBufferOffset,
      drawCount,
      stride);
}

//  void QRhiMetal::debugMarkBegin(QRhiCommandBuffer *cb, const QByteArray
//      &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QRhiMetal14debugMarkBeginEP17QRhiCommandBufferRK10QByteArray(
    QRhiMetal *self,
    QRhiCommandBuffer *cb,
    const QByteArray *name) {
  self->debugMarkBegin(cb, *name);
}

//  void QRhiMetal::debugMarkEnd(QRhiCommandBuffer *cb)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QRhiMetal12debugMarkEndEP17QRhiCommandBuffer(
    QRhiMetal *self,
    QRhiCommandBuffer *cb) {
  self->debugMarkEnd(cb);
}

//  void QRhiMetal::debugMarkMsg(QRhiCommandBuffer *cb, const QByteArray
//      &msg)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QRhiMetal12debugMarkMsgEP17QRhiCommandBufferRK10QByteArray(
    QRhiMetal *self,
    QRhiCommandBuffer *cb,
    const QByteArray *msg) {
  self->debugMarkMsg(cb, *msg);
}

//  void QRhiMetal::beginComputePass(QRhiCommandBuffer *cb,
//      QRhiResourceUpdateBatch *resourceUpdates,
//      QRhiCommandBuffer::BeginPassFlags flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QRhiMetal16beginComputePassEP17QRhiCommandBufferP23QRhiResourceUpdateBatch6QFlagsINS0_13BeginPassFlagEE(
    QRhiMetal *self,
    QRhiCommandBuffer *cb,
    QRhiResourceUpdateBatch *resourceUpdates,
    int flags) {
  self->beginComputePass(
      cb,
      resourceUpdates,
      QFlags<QRhiCommandBuffer::BeginPassFlag>::fromInt(flags));
}

//  void QRhiMetal::endComputePass(QRhiCommandBuffer *cb,
//      QRhiResourceUpdateBatch *resourceUpdates)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QRhiMetal14endComputePassEP17QRhiCommandBufferP23QRhiResourceUpdateBatch(
    QRhiMetal *self,
    QRhiCommandBuffer *cb,
    QRhiResourceUpdateBatch *resourceUpdates) {
  self->endComputePass(cb, resourceUpdates);
}

//  void QRhiMetal::setComputePipeline(QRhiCommandBuffer *cb,
//      QRhiComputePipeline *ps)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QRhiMetal18setComputePipelineEP17QRhiCommandBufferP19QRhiComputePipeline(
    QRhiMetal *self,
    QRhiCommandBuffer *cb,
    QRhiComputePipeline *ps) {
  self->setComputePipeline(cb, ps);
}

//  void QRhiMetal::dispatch(QRhiCommandBuffer *cb, int x, int y, int z)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QRhiMetal8dispatchEP17QRhiCommandBufferiii(
    QRhiMetal *self,
    QRhiCommandBuffer *cb,
    int x,
    int y,
    int z) {
  self->dispatch(cb, x, y, z);
}

//  const QRhiNativeHandles *QRhiMetal::nativeHandles(QRhiCommandBuffer *cb)
extern "C" Q_DECL_EXPORT
const QRhiNativeHandles *ritual_ZN9QRhiMetal13nativeHandlesEP17QRhiCommandBuffer(
    QRhiMetal *self,
    QRhiCommandBuffer *cb) {
  return self->nativeHandles(cb);
}

//  void QRhiMetal::beginExternal(QRhiCommandBuffer *cb)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QRhiMetal13beginExternalEP17QRhiCommandBuffer(
    QRhiMetal *self,
    QRhiCommandBuffer *cb) {
  self->beginExternal(cb);
}

//  void QRhiMetal::endExternal(QRhiCommandBuffer *cb)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QRhiMetal11endExternalEP17QRhiCommandBuffer(
    QRhiMetal *self,
    QRhiCommandBuffer *cb) {
  self->endExternal(cb);
}

//  double QRhiMetal::lastCompletedGpuTime(QRhiCommandBuffer *cb)
extern "C" Q_DECL_EXPORT
double ritual_ZN9QRhiMetal20lastCompletedGpuTimeEP17QRhiCommandBuffer(
    QRhiMetal *self,
    QRhiCommandBuffer *cb) {
  return self->lastCompletedGpuTime(cb);
}

//  QList<int> QRhiMetal::supportedSampleCounts() const
extern "C" Q_DECL_EXPORT
QList<int> *ritual_ZNK9QRhiMetal21supportedSampleCountsEv(
    const QRhiMetal *self) {
  return new QList<int>(self->supportedSampleCounts());
}

//  QList<QSize> QRhiMetal::supportedShadingRates(int sampleCount) const
extern "C" Q_DECL_EXPORT
QList<QSize> *ritual_ZNK9QRhiMetal21supportedShadingRatesEi(
    const QRhiMetal *self,
    int sampleCount) {
  return new QList<QSize>(self->supportedShadingRates(sampleCount));
}

//  int QRhiMetal::ubufAlignment() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QRhiMetal13ubufAlignmentEv(const QRhiMetal *self) {
  return self->ubufAlignment();
}

//  bool QRhiMetal::isYUpInFramebuffer() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QRhiMetal18isYUpInFramebufferEv(const QRhiMetal *self) {
  return self->isYUpInFramebuffer();
}

//  bool QRhiMetal::isYUpInNDC() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QRhiMetal10isYUpInNDCEv(const QRhiMetal *self) {
  return self->isYUpInNDC();
}

//  bool QRhiMetal::isClipDepthZeroToOne() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QRhiMetal20isClipDepthZeroToOneEv(const QRhiMetal *self) {
  return self->isClipDepthZeroToOne();
}

//  QMatrix4x4 QRhiMetal::clipSpaceCorrMatrix() const
extern "C" Q_DECL_EXPORT
QMatrix4x4 *ritual_ZNK9QRhiMetal19clipSpaceCorrMatrixEv(
    const QRhiMetal *self) {
  return new QMatrix4x4(self->clipSpaceCorrMatrix());
}

//  bool QRhiMetal::isTextureFormatSupported(QRhiTexture::Format format,
//      QRhiTexture::Flags flags) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QRhiMetal24isTextureFormatSupportedEN11QRhiTexture6FormatE6QFlagsINS0_4FlagEE(
    const QRhiMetal *self,
    QRhiTexture::Format format,
    int flags) {
  return self->isTextureFormatSupported(
      format,
      QFlags<QRhiTexture::Flag>::fromInt(flags));
}

//  bool QRhiMetal::isFeatureSupported(QRhi::Feature feature) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QRhiMetal18isFeatureSupportedEN4QRhi7FeatureE(
    const QRhiMetal *self,
    QRhi::Feature feature) {
  return self->isFeatureSupported(feature);
}

//  int QRhiMetal::resourceLimit(QRhi::ResourceLimit limit) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QRhiMetal13resourceLimitEN4QRhi13ResourceLimitE(
    const QRhiMetal *self,
    QRhi::ResourceLimit limit) {
  return self->resourceLimit(limit);
}

//  const QRhiNativeHandles *QRhiMetal::nativeHandles()
extern "C" Q_DECL_EXPORT
const QRhiNativeHandles *ritual_ZN9QRhiMetal13nativeHandlesEv(
    QRhiMetal *self) {
  return self->nativeHandles();
}

//  QRhiDriverInfo QRhiMetal::driverInfo() const
extern "C" Q_DECL_EXPORT
QRhiDriverInfo *ritual_ZNK9QRhiMetal10driverInfoEv(const QRhiMetal *self) {
  return new QRhiDriverInfo(self->driverInfo());
}

//  QRhiStats QRhiMetal::statistics()
extern "C" Q_DECL_EXPORT
QRhiStats *ritual_ZN9QRhiMetal10statisticsEv(QRhiMetal *self) {
  return new QRhiStats(self->statistics());
}

//  bool QRhiMetal::makeThreadLocalNativeContextCurrent()
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QRhiMetal35makeThreadLocalNativeContextCurrentEv(
    QRhiMetal *self) {
  return self->makeThreadLocalNativeContextCurrent();
}

//  void QRhiMetal::setQueueSubmitParams(QRhiNativeHandles *params)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QRhiMetal20setQueueSubmitParamsEP17QRhiNativeHandles(
    QRhiMetal *self,
    QRhiNativeHandles *params) {
  self->setQueueSubmitParams(params);
}

//  void QRhiMetal::releaseCachedResources()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QRhiMetal22releaseCachedResourcesEv(QRhiMetal *self) {
  self->releaseCachedResources();
}

//  bool QRhiMetal::isDeviceLost() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QRhiMetal12isDeviceLostEv(const QRhiMetal *self) {
  return self->isDeviceLost();
}

//  QByteArray QRhiMetal::pipelineCacheData()
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN9QRhiMetal17pipelineCacheDataEv(QRhiMetal *self) {
  return new QByteArray(self->pipelineCacheData());
}

//  void QRhiMetal::setPipelineCacheData(const QByteArray &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QRhiMetal20setPipelineCacheDataERK10QByteArray(
    QRhiMetal *self,
    const QByteArray *data) {
  self->setPipelineCacheData(*data);
}

//  a Python function taken by a CuteQRhiMetal, for the function named by the
//      key
extern "C" Q_DECL_EXPORT
bool ritual_take_QRhiMetal(QRhiMetal *self, const char *key, void *call) {
  return static_cast<CuteQRhiMetal *>(self)->take(key, call);
}

//  a QList<int> a ritual of QRhiMetal gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QRhiMetal__QList_int(QList<int> *self) {
  delete self;
}

#endif  // QT_CONFIG(metal)
