//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qrhivulkan_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if QT_CONFIG(vulkan)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qrhivulkan_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qsize.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/rhi/qrhi.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/private/qrhivulkan_p.h>
#include <QtGui/qpa/qplatformvulkaninstance.h>
#include <QtCore/qmath.h>
#include <QtGui/qwindow.h>
#include <QtGui/private/qvulkandefaultinstance_p.h>
#include <QtCore/q20memory.h>
#include <optional>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/gui/rhi/qrhivulkan.cpp, line 9073, as _ZN16QVkCommandBufferC1EP18QRhiImplementation
inline QVkCommandBuffer::QVkCommandBuffer(QRhiImplementation *rhi)
    : QRhiCommandBuffer(rhi)
{
    resetState();
}

//  from src/gui/rhi/qrhivulkan.cpp, line 9079, as _ZN16QVkCommandBufferD1Ev
inline QVkCommandBuffer::~QVkCommandBuffer()
{
    destroy();
}

//  from src/gui/rhi/qrhivulkan.cpp, line 8014, as _ZN23QVkRenderPassDescriptor22updateSerializedFormatEv
inline void QVkRenderPassDescriptor::updateSerializedFormat()
{
    serializedFormatData.clear();
    auto p = std::back_inserter(serializedFormatData);

    *p++ = attDescs.size();
    *p++ = colorRefs.size();
    *p++ = resolveRefs.size();
    *p++ = hasDepthStencil;
    *p++ = hasDepthStencilResolve;
    *p++ = hasShadingRateMap;
    *p++ = multiViewCount;

    auto serializeAttachmentData = [this, &p](uint32_t attIdx) {
        const bool used = attIdx != VK_ATTACHMENT_UNUSED;
        const VkAttachmentDescription *a = used ? &attDescs[attIdx] : nullptr;
        *p++ = used ? a->format : 0;
        *p++ = used ? a->samples : 0;
        *p++ = used ? a->loadOp : 0;
        *p++ = used ? a->storeOp : 0;
        *p++ = used ? a->stencilLoadOp : 0;
        *p++ = used ? a->stencilStoreOp : 0;
        *p++ = used ? a->initialLayout : 0;
        *p++ = used ? a->finalLayout : 0;
    };

    for (int i = 0, ie = colorRefs.size(); i != ie; ++i) {
        const uint32_t attIdx = colorRefs[i].attachment;
        *p++ = attIdx;
        serializeAttachmentData(attIdx);
    }

    if (hasDepthStencil) {
        const uint32_t attIdx = dsRef.attachment;
        *p++ = attIdx;
        serializeAttachmentData(attIdx);
    }

    for (int i = 0, ie = resolveRefs.size(); i != ie; ++i) {
        const uint32_t attIdx = resolveRefs[i].attachment;
        *p++ = attIdx;
        serializeAttachmentData(attIdx);
    }

    if (hasDepthStencilResolve) {
        const uint32_t attIdx = dsResolveRef.attachment;
        *p++ = attIdx;
        serializeAttachmentData(attIdx);
    }

    if (hasShadingRateMap) {
        const uint32_t attIdx = shadingRateRef.attachment;
        *p++ = attIdx;
        serializeAttachmentData(attIdx);
    }
}

//  from src/gui/rhi/qrhivulkan.cpp, line 7896, as _ZN23QVkRenderPassDescriptorC1EP18QRhiImplementation
inline QVkRenderPassDescriptor::QVkRenderPassDescriptor(QRhiImplementation *rhi)
    : QRhiRenderPassDescriptor(rhi)
{
    serializedFormatData.reserve(64);
}

//  from src/gui/rhi/qrhivulkan.cpp, line 8169, as _ZN24QVkSwapChainRenderTargetC1EP18QRhiImplementationP13QRhiSwapChain
inline QVkSwapChainRenderTarget::QVkSwapChainRenderTarget(QRhiImplementation *rhi, QRhiSwapChain *swapchain)
    : QRhiSwapChainRenderTarget(rhi, swapchain)
{
}

//  from src/gui/rhi/qrhivulkan.cpp, line 8174, as _ZN24QVkSwapChainRenderTargetD1Ev
inline QVkSwapChainRenderTarget::~QVkSwapChainRenderTarget()
{
    destroy();
}

//  from src/gui/rhi/qrhivulkan.cpp, line 9117, as _ZN12QVkSwapChainD1Ev
inline QVkSwapChain::~QVkSwapChain()
{
    destroy();
}

//  from src/gui/rhi/qrhivulkan.cpp, line 9122, as _ZN12QVkSwapChain7destroyEv
inline void QVkSwapChain::destroy()
{
    if (sc == VK_NULL_HANDLE)
        return;

    QRHI_RES_RHI(QRhiVulkan);
    if (rhiD) {
        rhiD->swapchains.remove(this);
        rhiD->releaseSwapChainResources(this);
    }

    for (int i = 0; i < QVK_FRAMES_IN_FLIGHT; ++i) {
        QVkSwapChain::FrameResources &frame(frameRes[i]);
        frame.cmdBuf = VK_NULL_HANDLE;
        frame.timestampQueryIndex = -1;
    }

    surface = lastConnectedSurface = VK_NULL_HANDLE;

    if (rhiD)
        rhiD->unregisterResource(this);
}

//  from src/gui/rhi/qrhivulkan.cpp, line 9145, as _ZN12QVkSwapChain25currentFrameCommandBufferEv
inline QRhiCommandBuffer *QVkSwapChain::currentFrameCommandBuffer()
{
    return &cbWrapper;
}

//  from src/gui/rhi/qrhivulkan.cpp, line 9150, as _ZN12QVkSwapChain24currentFrameRenderTargetEv
inline QRhiRenderTarget *QVkSwapChain::currentFrameRenderTarget()
{
    return &rtWrapper;
}

//  from src/gui/rhi/qrhivulkan.cpp, line 9155, as _ZN12QVkSwapChain24currentFrameRenderTargetEN13QRhiSwapChain18StereoTargetBufferE
inline QRhiRenderTarget *QVkSwapChain::currentFrameRenderTarget(StereoTargetBuffer targetBuffer)
{
    return !stereo || targetBuffer == StereoTargetBuffer::LeftBuffer ? &rtWrapper : &rtWrapperRight;
}

//  from src/gui/rhi/qrhivulkan.cpp, line 9160, as _ZN12QVkSwapChain16surfacePixelSizeEv
inline QSize QVkSwapChain::surfacePixelSize()
{
    if (!ensureSurface())
        return QSize();

    // The size from the QWindow may not exactly match the surface... so if a
    // size is reported from the surface, use that.
    VkSurfaceCapabilitiesKHR surfaceCaps = {};
    QRHI_RES_RHI(QRhiVulkan);
    rhiD->vkGetPhysicalDeviceSurfaceCapabilitiesKHR(rhiD->physDev, surface, &surfaceCaps);
    VkExtent2D bufferSize = surfaceCaps.currentExtent;
    if (bufferSize.width == uint32_t(-1)) {
        Q_ASSERT(bufferSize.height == uint32_t(-1));
        return m_window->size() * m_window->devicePixelRatio();
    }
    return QSize(int(bufferSize.width), int(bufferSize.height));
}

//  from src/gui/rhi/qrhivulkan.cpp, line 9224, as _ZN12QVkSwapChain7hdrInfoEv
#if defined(Q_OS_LINUX)
inline QRhiSwapChainHdrInfo QVkSwapChain::hdrInfo()
{
    QRhiSwapChainHdrInfo info = QRhiSwapChain::hdrInfo();
#ifdef Q_OS_WIN
    QRHI_RES_RHI(QRhiVulkan);
    // Must use m_window, not window, given this may be called before createOrResize().
    if (m_window && rhiD->adapterLuidValid)
        info = rhiD->dxgiHdrInfo->queryHdrInfo(m_window);
#endif
    return info;
}
#endif  // defined(Q_OS_LINUX)

//  from src/gui/rhi/qrhivulkan.cpp, line 9236, as _ZN12QVkSwapChain33newCompatibleRenderPassDescriptorEv
inline QRhiRenderPassDescriptor *QVkSwapChain::newCompatibleRenderPassDescriptor()
{
    // not yet built so cannot rely on data computed in createOrResize()

    if (!ensureSurface()) // make sure sampleCount and colorFormat reflect what was requested
        return nullptr;

    QRHI_RES_RHI(QRhiVulkan);
    QVkRenderPassDescriptor *rp = new QVkRenderPassDescriptor(m_rhi);
    if (!rhiD->createDefaultRenderPass(rp,
                                       m_depthStencil != nullptr,
                                       samples,
                                       colorFormat,
                                       m_shadingRateMap))
    {
        delete rp;
        return nullptr;
    }

    rp->ownsRp = true;
    rp->updateSerializedFormat();
    rhiD->registerResource(rp);
    return rp;
}
//  -----------------------------------------------------------------------

//  A QVkSwapChain that Python can take functions over in. Every QVkSwapChain
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQVkSwapChainCall0)(const void *, int *);
typedef void * (*CuteQVkSwapChainCall1)(const void *, int *);
typedef void * (*CuteQVkSwapChainCall2)(const void *, int *);
typedef void * (*CuteQVkSwapChainCall3)(const void *, int, int *);
typedef const QSize * (*CuteQVkSwapChainCall4)(const void *, int *);
typedef bool (*CuteQVkSwapChainCall5)(const void *, int, int *);
typedef const QRhiSwapChainHdrInfo * (*CuteQVkSwapChainCall6)(const void *, int *);
typedef void * (*CuteQVkSwapChainCall7)(const void *, int *);
typedef bool (*CuteQVkSwapChainCall8)(const void *, int *);
typedef int (*CuteQVkSwapChainCall9)(const void *, int *);
class CuteQVkSwapChain : public QVkSwapChain {
public:
  using QVkSwapChain::QVkSwapChain;
  void *taken[10] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN12QRhiResource7destroyEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QRhiSwapChain25currentFrameCommandBufferEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QRhiSwapChain24currentFrameRenderTargetEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QRhiSwapChain24currentFrameRenderTargetENS_18StereoTargetBufferE")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QRhiSwapChain16surfacePixelSizeEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QRhiSwapChain17isFormatSupportedENS_6FormatE")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QRhiSwapChain7hdrInfoEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QRhiSwapChain33newCompatibleRenderPassDescriptorEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QRhiSwapChain14createOrResizeEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QRhiResource12resourceTypeEv")) {
      taken[9] = call;
      return true;
    }
    return false;
  }

  //  void QVkSwapChain::destroy()
  void destroy() override {
    if (taken[0]) {
      int handled = 0;
      CuteQVkSwapChainCall0 call = reinterpret_cast<CuteQVkSwapChainCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QVkSwapChain::destroy();
  }

  //  QRhiCommandBuffer *QVkSwapChain::currentFrameCommandBuffer()
  QRhiCommandBuffer *currentFrameCommandBuffer() override {
    if (taken[1]) {
      int handled = 0;
      CuteQVkSwapChainCall1 call = reinterpret_cast<CuteQVkSwapChainCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QRhiCommandBuffer *>(given);
    }
    return QVkSwapChain::currentFrameCommandBuffer();
  }

  //  QRhiRenderTarget *QVkSwapChain::currentFrameRenderTarget()
  QRhiRenderTarget *currentFrameRenderTarget() override {
    if (taken[2]) {
      int handled = 0;
      CuteQVkSwapChainCall2 call = reinterpret_cast<CuteQVkSwapChainCall2>(taken[2]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QRhiRenderTarget *>(given);
    }
    return QVkSwapChain::currentFrameRenderTarget();
  }

  //  QRhiRenderTarget
  //      *QVkSwapChain::currentFrameRenderTarget(StereoTargetBuffer
  //      targetBuffer)
  QRhiRenderTarget *currentFrameRenderTarget(
      QRhiSwapChain::StereoTargetBuffer targetBuffer) override {
    if (taken[3]) {
      int handled = 0;
      CuteQVkSwapChainCall3 call = reinterpret_cast<CuteQVkSwapChainCall3>(taken[3]);
      void * given = call(this, static_cast<int>(targetBuffer), &handled);
      if (handled) return static_cast<QRhiRenderTarget *>(given);
    }
    return QVkSwapChain::currentFrameRenderTarget(targetBuffer);
  }

  //  QSize QVkSwapChain::surfacePixelSize()
  QSize surfacePixelSize() override {
    if (taken[4]) {
      int handled = 0;
      CuteQVkSwapChainCall4 call = reinterpret_cast<CuteQVkSwapChainCall4>(taken[4]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QVkSwapChain::surfacePixelSize();
  }

  //  bool QVkSwapChain::isFormatSupported(Format f)
  bool isFormatSupported(QRhiSwapChain::Format f) override {
    if (taken[5]) {
      int handled = 0;
      CuteQVkSwapChainCall5 call = reinterpret_cast<CuteQVkSwapChainCall5>(taken[5]);
      bool given = call(this, static_cast<int>(f), &handled);
      if (handled) return given;
    }
    return QVkSwapChain::isFormatSupported(f);
  }

  //  QRhiSwapChainHdrInfo QVkSwapChain::hdrInfo()
  QRhiSwapChainHdrInfo hdrInfo() override {
    if (taken[6]) {
      int handled = 0;
      CuteQVkSwapChainCall6 call = reinterpret_cast<CuteQVkSwapChainCall6>(taken[6]);
      const QRhiSwapChainHdrInfo * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QVkSwapChain::hdrInfo();
  }

  //  QRhiRenderPassDescriptor
  //      *QVkSwapChain::newCompatibleRenderPassDescriptor()
  QRhiRenderPassDescriptor *newCompatibleRenderPassDescriptor() override {
    if (taken[7]) {
      int handled = 0;
      CuteQVkSwapChainCall7 call = reinterpret_cast<CuteQVkSwapChainCall7>(taken[7]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QRhiRenderPassDescriptor *>(given);
    }
    return QVkSwapChain::newCompatibleRenderPassDescriptor();
  }

  //  bool QVkSwapChain::createOrResize()
  bool createOrResize() override {
    if (taken[8]) {
      int handled = 0;
      CuteQVkSwapChainCall8 call = reinterpret_cast<CuteQVkSwapChainCall8>(taken[8]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QVkSwapChain::createOrResize();
  }

  //  QRhiResource::Type QRhiSwapChain::resourceType() const
  QRhiResource::Type resourceType() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQVkSwapChainCall9 call = reinterpret_cast<CuteQVkSwapChainCall9>(taken[9]);
      int given = call(this, &handled);
      if (handled) return static_cast<QRhiResource::Type>(given);
    }
    return QRhiSwapChain::resourceType();
  }
};

//  QVkSwapChain::~QVkSwapChain()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QVkSwapChainD1Ev(QVkSwapChain *self) {
  delete self;
}

//  void QVkSwapChain::destroy()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QVkSwapChain7destroyEv(QVkSwapChain *self) {
  self->destroy();
}

//  QRhiCommandBuffer *QVkSwapChain::currentFrameCommandBuffer()
extern "C" Q_DECL_EXPORT
QRhiCommandBuffer *ritual_ZN12QVkSwapChain25currentFrameCommandBufferEv(
    QVkSwapChain *self) {
  return self->currentFrameCommandBuffer();
}

//  QRhiRenderTarget *QVkSwapChain::currentFrameRenderTarget()
extern "C" Q_DECL_EXPORT
QRhiRenderTarget *ritual_ZN12QVkSwapChain24currentFrameRenderTargetEv(
    QVkSwapChain *self) {
  return self->currentFrameRenderTarget();
}

//  QRhiRenderTarget
//      *QVkSwapChain::currentFrameRenderTarget(StereoTargetBuffer
//      targetBuffer)
extern "C" Q_DECL_EXPORT
QRhiRenderTarget *ritual_ZN12QVkSwapChain24currentFrameRenderTargetEN13QRhiSwapChain18StereoTargetBufferE(
    QVkSwapChain *self,
    QRhiSwapChain::StereoTargetBuffer targetBuffer) {
  return self->currentFrameRenderTarget(targetBuffer);
}

//  QSize QVkSwapChain::surfacePixelSize()
extern "C" Q_DECL_EXPORT
QSize *ritual_ZN12QVkSwapChain16surfacePixelSizeEv(QVkSwapChain *self) {
  return new QSize(self->surfacePixelSize());
}

//  QRhiSwapChainHdrInfo QVkSwapChain::hdrInfo()
extern "C" Q_DECL_EXPORT
QRhiSwapChainHdrInfo *ritual_ZN12QVkSwapChain7hdrInfoEv(QVkSwapChain *self) {
  return new QRhiSwapChainHdrInfo(self->hdrInfo());
}

//  QRhiRenderPassDescriptor
//      *QVkSwapChain::newCompatibleRenderPassDescriptor()
extern "C" Q_DECL_EXPORT
QRhiRenderPassDescriptor *ritual_ZN12QVkSwapChain33newCompatibleRenderPassDescriptorEv(
    QVkSwapChain *self) {
  return self->newCompatibleRenderPassDescriptor();
}

//  a Python function taken by a CuteQVkSwapChain, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QVkSwapChain(
    QVkSwapChain *self,
    const char *key,
    void *call) {
  return static_cast<CuteQVkSwapChain *>(self)->take(key, call);
}

//  QRhiCommandBuffer *QVkSwapChain::currentFrameCommandBuffer()
extern "C" Q_DECL_EXPORT
QRhiCommandBuffer *ritual_own_ZN12QVkSwapChain25currentFrameCommandBufferEv(
    QVkSwapChain *self) {
  return self->QVkSwapChain::currentFrameCommandBuffer();
}

//  QRhiRenderTarget *QVkSwapChain::currentFrameRenderTarget()
extern "C" Q_DECL_EXPORT
QRhiRenderTarget *ritual_own_ZN12QVkSwapChain24currentFrameRenderTargetEv(
    QVkSwapChain *self) {
  return self->QVkSwapChain::currentFrameRenderTarget();
}

//  QRhiRenderTarget
//      *QVkSwapChain::currentFrameRenderTarget(StereoTargetBuffer
//      targetBuffer)
extern "C" Q_DECL_EXPORT
QRhiRenderTarget *ritual_own_ZN12QVkSwapChain24currentFrameRenderTargetEN13QRhiSwapChain18StereoTargetBufferE(
    QVkSwapChain *self,
    QRhiSwapChain::StereoTargetBuffer targetBuffer) {
  return self->QVkSwapChain::currentFrameRenderTarget(targetBuffer);
}

#if defined(Q_OS_LINUX)
//  QRhiSwapChainHdrInfo QVkSwapChain::hdrInfo()
extern "C" Q_DECL_EXPORT
QRhiSwapChainHdrInfo *ritual_own_ZN12QVkSwapChain7hdrInfoEv(
    QVkSwapChain *self) {
  return new QRhiSwapChainHdrInfo(self->QVkSwapChain::hdrInfo());
}
#endif  // defined(Q_OS_LINUX)

#endif  // QT_CONFIG(vulkan)
