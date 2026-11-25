//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qrhivulkan_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-25: the whole file stands under
//  '__has_include(<vulkan/vulkan.h>)' beside 'QT_CONFIG(vulkan)', as
//  Qt's 'qvulkaninstance.h' checks it, since without Vulkan's headers
//  'qrhivulkan_p.h' fails on 'VkBuffer'. Kept as it is when the
//  generator runs again.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if QT_CONFIG(vulkan) && __has_include(<vulkan/vulkan.h>)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qrhivulkan_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qsize.h>
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

//  from src/gui/rhi/qrhivulkan.cpp, line 8210, as _ZN22QVkTextureRenderTargetD1Ev
inline QVkTextureRenderTarget::~QVkTextureRenderTarget()
{
    destroy();
}

//  from src/gui/rhi/qrhivulkan.cpp, line 8215, as _ZN22QVkTextureRenderTarget7destroyEv
inline void QVkTextureRenderTarget::destroy()
{
    if (!d.fb)
        return;

    QRhiVulkan::DeferredReleaseEntry e;
    e.type = QRhiVulkan::DeferredReleaseEntry::TextureRenderTarget;
    e.lastActiveFrameSlot = lastActiveFrameSlot;

    e.textureRenderTarget.fb = d.fb;
    d.fb = VK_NULL_HANDLE;

    for (int att = 0; att < QVkRenderTargetData::MAX_COLOR_ATTACHMENTS; ++att) {
        e.textureRenderTarget.rtv[att] = rtv[att];
        e.textureRenderTarget.resrtv[att] = resrtv[att];
        rtv[att] = VK_NULL_HANDLE;
        resrtv[att] = VK_NULL_HANDLE;
    }

    e.textureRenderTarget.dsv = dsv;
    dsv = VK_NULL_HANDLE;
    e.textureRenderTarget.resdsv = resdsv;
    resdsv = VK_NULL_HANDLE;

    e.textureRenderTarget.shadingRateMapView = shadingRateMapView;
    shadingRateMapView = VK_NULL_HANDLE;

    QRHI_RES_RHI(QRhiVulkan);
    if (rhiD) {
        rhiD->releaseQueue.append(e);
        rhiD->unregisterResource(this);
    }
}

//  from src/gui/rhi/qrhivulkan.cpp, line 8505, as _ZNK22QVkTextureRenderTarget9pixelSizeEv
inline QSize QVkTextureRenderTarget::pixelSize() const
{
    if (!QRhiRenderTargetAttachmentTracker::isUpToDate<QVkTexture, QVkRenderBuffer>(m_desc, d.currentResIdList))
        const_cast<QVkTextureRenderTarget *>(this)->create();

    return d.pixelSize;
}

//  from src/gui/rhi/qrhivulkan.cpp, line 8513, as _ZNK22QVkTextureRenderTarget16devicePixelRatioEv
inline float QVkTextureRenderTarget::devicePixelRatio() const
{
    return d.dpr;
}

//  from src/gui/rhi/qrhivulkan.cpp, line 8518, as _ZNK22QVkTextureRenderTarget11sampleCountEv
inline int QVkTextureRenderTarget::sampleCount() const
{
    return d.sampleCount;
}

//  from src/gui/rhi/qrhivulkan.cpp, line 8249, as _ZN22QVkTextureRenderTarget33newCompatibleRenderPassDescriptorEv
inline QRhiRenderPassDescriptor *QVkTextureRenderTarget::newCompatibleRenderPassDescriptor()
{
    // not yet built so cannot rely on data computed in create()

    QRHI_RES_RHI(QRhiVulkan);
    QVkRenderPassDescriptor *rp = new QVkRenderPassDescriptor(m_rhi);
    if (!rhiD->createOffscreenRenderPass(rp,
                                         m_desc.cbeginColorAttachments(),
                                         m_desc.cendColorAttachments(),
                                         m_flags.testFlag(QRhiTextureRenderTarget::PreserveColorContents),
                                         m_flags.testFlag(QRhiTextureRenderTarget::PreserveDepthStencilContents),
                                         m_desc.depthTexture() && !m_flags.testFlag(DoNotStoreDepthStencilContents) && !m_desc.depthResolveTexture(),
                                         m_desc.depthStencilBuffer(),
                                         m_desc.depthTexture(),
                                         m_desc.depthResolveTexture(),
                                         m_desc.depthLayer(),
                                         m_desc.shadingRateMap()))
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

//  A QVkTextureRenderTarget that Python can take functions over in. Every QVkTextureRenderTarget
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQVkTextureRenderTargetCall0)(const void *, int *);
typedef const QSize * (*CuteQVkTextureRenderTargetCall1)(const void *, int *);
typedef float (*CuteQVkTextureRenderTargetCall2)(const void *, int *);
typedef int (*CuteQVkTextureRenderTargetCall3)(const void *, int *);
typedef void * (*CuteQVkTextureRenderTargetCall4)(const void *, int *);
typedef bool (*CuteQVkTextureRenderTargetCall5)(const void *, int *);
typedef int (*CuteQVkTextureRenderTargetCall6)(const void *, int *);
class CuteQVkTextureRenderTarget : public QVkTextureRenderTarget {
public:
  using QVkTextureRenderTarget::QVkTextureRenderTarget;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN12QRhiResource7destroyEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QRhiRenderTarget9pixelSizeEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QRhiRenderTarget16devicePixelRatioEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QRhiRenderTarget11sampleCountEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN23QRhiTextureRenderTarget33newCompatibleRenderPassDescriptorEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN23QRhiTextureRenderTarget6createEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QRhiResource12resourceTypeEv")) {
      taken[6] = call;
      return true;
    }
    return false;
  }

  //  void QVkTextureRenderTarget::destroy()
  void destroy() override {
    if (taken[0]) {
      int handled = 0;
      CuteQVkTextureRenderTargetCall0 call = reinterpret_cast<CuteQVkTextureRenderTargetCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QVkTextureRenderTarget::destroy();
  }

  //  QSize QVkTextureRenderTarget::pixelSize() const
  QSize pixelSize() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQVkTextureRenderTargetCall1 call = reinterpret_cast<CuteQVkTextureRenderTargetCall1>(taken[1]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QVkTextureRenderTarget::pixelSize();
  }

  //  float QVkTextureRenderTarget::devicePixelRatio() const
  float devicePixelRatio() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQVkTextureRenderTargetCall2 call = reinterpret_cast<CuteQVkTextureRenderTargetCall2>(taken[2]);
      float given = call(this, &handled);
      if (handled) return given;
    }
    return QVkTextureRenderTarget::devicePixelRatio();
  }

  //  int QVkTextureRenderTarget::sampleCount() const
  int sampleCount() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQVkTextureRenderTargetCall3 call = reinterpret_cast<CuteQVkTextureRenderTargetCall3>(taken[3]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QVkTextureRenderTarget::sampleCount();
  }

  //  QRhiRenderPassDescriptor
  //      *QVkTextureRenderTarget::newCompatibleRenderPassDescriptor()
  QRhiRenderPassDescriptor *newCompatibleRenderPassDescriptor() override {
    if (taken[4]) {
      int handled = 0;
      CuteQVkTextureRenderTargetCall4 call = reinterpret_cast<CuteQVkTextureRenderTargetCall4>(taken[4]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QRhiRenderPassDescriptor *>(given);
    }
    return QVkTextureRenderTarget::newCompatibleRenderPassDescriptor();
  }

  //  bool QVkTextureRenderTarget::create()
  bool create() override {
    if (taken[5]) {
      int handled = 0;
      CuteQVkTextureRenderTargetCall5 call = reinterpret_cast<CuteQVkTextureRenderTargetCall5>(taken[5]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QVkTextureRenderTarget::create();
  }

  //  QRhiResource::Type QRhiTextureRenderTarget::resourceType() const
  QRhiResource::Type resourceType() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQVkTextureRenderTargetCall6 call = reinterpret_cast<CuteQVkTextureRenderTargetCall6>(taken[6]);
      int given = call(this, &handled);
      if (handled) return static_cast<QRhiResource::Type>(given);
    }
    return QRhiTextureRenderTarget::resourceType();
  }
};

//  QVkTextureRenderTarget::~QVkTextureRenderTarget()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QVkTextureRenderTargetD1Ev(QVkTextureRenderTarget *self) {
  delete self;
}

//  void QVkTextureRenderTarget::destroy()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QVkTextureRenderTarget7destroyEv(
    QVkTextureRenderTarget *self) {
  self->destroy();
}

//  QSize QVkTextureRenderTarget::pixelSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK22QVkTextureRenderTarget9pixelSizeEv(
    const QVkTextureRenderTarget *self) {
  return new QSize(self->pixelSize());
}

//  float QVkTextureRenderTarget::devicePixelRatio() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK22QVkTextureRenderTarget16devicePixelRatioEv(
    const QVkTextureRenderTarget *self) {
  return self->devicePixelRatio();
}

//  int QVkTextureRenderTarget::sampleCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK22QVkTextureRenderTarget11sampleCountEv(
    const QVkTextureRenderTarget *self) {
  return self->sampleCount();
}

//  QRhiRenderPassDescriptor
//      *QVkTextureRenderTarget::newCompatibleRenderPassDescriptor()
extern "C" Q_DECL_EXPORT
QRhiRenderPassDescriptor *ritual_ZN22QVkTextureRenderTarget33newCompatibleRenderPassDescriptorEv(
    QVkTextureRenderTarget *self) {
  return self->newCompatibleRenderPassDescriptor();
}

//  a Python function taken by a CuteQVkTextureRenderTarget, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QVkTextureRenderTarget(
    QVkTextureRenderTarget *self,
    const char *key,
    void *call) {
  return static_cast<CuteQVkTextureRenderTarget *>(self)->take(key, call);
}

//  void QVkTextureRenderTarget::destroy()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QVkTextureRenderTarget7destroyEv(
    QVkTextureRenderTarget *self) {
  self->QVkTextureRenderTarget::destroy();
}

//  QSize QVkTextureRenderTarget::pixelSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK22QVkTextureRenderTarget9pixelSizeEv(
    const QVkTextureRenderTarget *self) {
  return new QSize(self->QVkTextureRenderTarget::pixelSize());
}

//  float QVkTextureRenderTarget::devicePixelRatio() const
extern "C" Q_DECL_EXPORT
float ritual_own_ZNK22QVkTextureRenderTarget16devicePixelRatioEv(
    const QVkTextureRenderTarget *self) {
  return self->QVkTextureRenderTarget::devicePixelRatio();
}

//  int QVkTextureRenderTarget::sampleCount() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK22QVkTextureRenderTarget11sampleCountEv(
    const QVkTextureRenderTarget *self) {
  return self->QVkTextureRenderTarget::sampleCount();
}

#endif  // QT_CONFIG(vulkan) && __has_include(<vulkan/vulkan.h>)
