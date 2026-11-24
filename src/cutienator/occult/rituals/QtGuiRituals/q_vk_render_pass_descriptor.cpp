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

//  from src/gui/rhi/qrhivulkan.cpp, line 8130, as _ZNK23QVkRenderPassDescriptor16serializedFormatEv
inline QVector<quint32> QVkRenderPassDescriptor::serializedFormat() const
{
    return serializedFormatData;
}

//  from src/gui/rhi/qrhivulkan.cpp, line 7902, as _ZN23QVkRenderPassDescriptorD1Ev
inline QVkRenderPassDescriptor::~QVkRenderPassDescriptor()
{
    destroy();
}

//  from src/gui/rhi/qrhivulkan.cpp, line 7907, as _ZN23QVkRenderPassDescriptor7destroyEv
inline void QVkRenderPassDescriptor::destroy()
{
    if (!rp)
        return;

    if (!ownsRp) {
        rp = VK_NULL_HANDLE;
        return;
    }

    QRhiVulkan::DeferredReleaseEntry e;
    e.type = QRhiVulkan::DeferredReleaseEntry::RenderPass;
    e.lastActiveFrameSlot = lastActiveFrameSlot;

    e.renderPass.rp = rp;

    rp = VK_NULL_HANDLE;

    QRHI_RES_RHI(QRhiVulkan);
    if (rhiD) {
        rhiD->releaseQueue.append(e);
        rhiD->unregisterResource(this);
    }
}

//  from src/gui/rhi/qrhivulkan.cpp, line 8135, as _ZN23QVkRenderPassDescriptor13nativeHandlesEv
inline const QRhiNativeHandles *QVkRenderPassDescriptor::nativeHandles()
{
    nativeHandlesStruct.renderPass = rp;
    return &nativeHandlesStruct;
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
//  -----------------------------------------------------------------------

//  A QVkRenderPassDescriptor that Python can take functions over in. Every QVkRenderPassDescriptor
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQVkRenderPassDescriptorCall0)(const void *, int *);
typedef bool (*CuteQVkRenderPassDescriptorCall1)(const void *, const QRhiRenderPassDescriptor *, int *);
typedef void * (*CuteQVkRenderPassDescriptorCall2)(const void *, int *);
typedef void * (*CuteQVkRenderPassDescriptorCall3)(const void *, int *);
typedef int (*CuteQVkRenderPassDescriptorCall4)(const void *, int *);
class CuteQVkRenderPassDescriptor : public QVkRenderPassDescriptor {
public:
  using QVkRenderPassDescriptor::QVkRenderPassDescriptor;
  void *taken[5] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN12QRhiResource7destroyEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK24QRhiRenderPassDescriptor12isCompatibleEPKS_")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK24QRhiRenderPassDescriptor33newCompatibleRenderPassDescriptorEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QRhiRenderPassDescriptor13nativeHandlesEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QRhiResource12resourceTypeEv")) {
      taken[4] = call;
      return true;
    }
    return false;
  }

  //  void QVkRenderPassDescriptor::destroy()
  void destroy() override {
    if (taken[0]) {
      int handled = 0;
      CuteQVkRenderPassDescriptorCall0 call = reinterpret_cast<CuteQVkRenderPassDescriptorCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QVkRenderPassDescriptor::destroy();
  }

  //  bool QVkRenderPassDescriptor::isCompatible(const
  //      QRhiRenderPassDescriptor *other) const
  bool isCompatible(const QRhiRenderPassDescriptor *other) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQVkRenderPassDescriptorCall1 call = reinterpret_cast<CuteQVkRenderPassDescriptorCall1>(taken[1]);
      bool given = call(this, other, &handled);
      if (handled) return given;
    }
    return QVkRenderPassDescriptor::isCompatible(other);
  }

  //  QRhiRenderPassDescriptor
  //      *QVkRenderPassDescriptor::newCompatibleRenderPassDescriptor()
  //      const
  QRhiRenderPassDescriptor *newCompatibleRenderPassDescriptor() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQVkRenderPassDescriptorCall2 call = reinterpret_cast<CuteQVkRenderPassDescriptorCall2>(taken[2]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QRhiRenderPassDescriptor *>(given);
    }
    return QVkRenderPassDescriptor::newCompatibleRenderPassDescriptor();
  }

  //  const QRhiNativeHandles *QVkRenderPassDescriptor::nativeHandles()
  const QRhiNativeHandles *nativeHandles() override {
    if (taken[3]) {
      int handled = 0;
      CuteQVkRenderPassDescriptorCall3 call = reinterpret_cast<CuteQVkRenderPassDescriptorCall3>(taken[3]);
      void * given = call(this, &handled);
      if (handled) return static_cast<const QRhiNativeHandles *>(given);
    }
    return QVkRenderPassDescriptor::nativeHandles();
  }

  //  QRhiResource::Type QRhiRenderPassDescriptor::resourceType() const
  QRhiResource::Type resourceType() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQVkRenderPassDescriptorCall4 call = reinterpret_cast<CuteQVkRenderPassDescriptorCall4>(taken[4]);
      int given = call(this, &handled);
      if (handled) return static_cast<QRhiResource::Type>(given);
    }
    return QRhiRenderPassDescriptor::resourceType();
  }
};

//  QVkRenderPassDescriptor::~QVkRenderPassDescriptor()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QVkRenderPassDescriptorD1Ev(QVkRenderPassDescriptor *self) {
  delete self;
}

//  void QVkRenderPassDescriptor::destroy()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QVkRenderPassDescriptor7destroyEv(
    QVkRenderPassDescriptor *self) {
  self->destroy();
}

//  const QRhiNativeHandles *QVkRenderPassDescriptor::nativeHandles()
extern "C" Q_DECL_EXPORT
const QRhiNativeHandles *ritual_ZN23QVkRenderPassDescriptor13nativeHandlesEv(
    QVkRenderPassDescriptor *self) {
  return self->nativeHandles();
}

//  void QVkRenderPassDescriptor::updateSerializedFormat()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QVkRenderPassDescriptor22updateSerializedFormatEv(
    QVkRenderPassDescriptor *self) {
  self->updateSerializedFormat();
}

//  a Python function taken by a CuteQVkRenderPassDescriptor, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QVkRenderPassDescriptor(
    QVkRenderPassDescriptor *self,
    const char *key,
    void *call) {
  return static_cast<CuteQVkRenderPassDescriptor *>(self)->take(key, call);
}

//  void QVkRenderPassDescriptor::destroy()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QVkRenderPassDescriptor7destroyEv(
    QVkRenderPassDescriptor *self) {
  self->QVkRenderPassDescriptor::destroy();
}

//  const QRhiNativeHandles *QVkRenderPassDescriptor::nativeHandles()
extern "C" Q_DECL_EXPORT
const QRhiNativeHandles *ritual_own_ZN23QVkRenderPassDescriptor13nativeHandlesEv(
    QVkRenderPassDescriptor *self) {
  return self->QVkRenderPassDescriptor::nativeHandles();
}

#endif  // QT_CONFIG(vulkan)
