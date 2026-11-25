//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qrhivulkan_p.h, Qt 6.12.0. Edited by hand
//  on 2026-11-25: everything after the global includes stands also
//  under '__has_include(<vulkan/vulkan.h>)', the check Qt's
//  'qvulkaninstance.h' makes, because without Vulkan's headers Qt
//  declares none of the Vulkan types ('VkBuffer' and the rest) that
//  'qrhivulkan_p.h' uses. Kept as it is when the generator runs again.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if QT_CONFIG(vulkan) && __has_include(<vulkan/vulkan.h>)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qrhivulkan_p.h>
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

//  from src/gui/rhi/qrhivulkan.cpp, line 7215, as _ZN9QVkBufferD1Ev
inline QVkBuffer::~QVkBuffer()
{
    destroy();
}

//  from src/gui/rhi/qrhivulkan.cpp, line 7220, as _ZN9QVkBuffer7destroyEv
inline void QVkBuffer::destroy()
{
    if (!buffers[0])
        return;

    QRhiVulkan::DeferredReleaseEntry e;
    e.type = QRhiVulkan::DeferredReleaseEntry::Buffer;
    e.lastActiveFrameSlot = lastActiveFrameSlot;

    for (int i = 0; i < QVK_FRAMES_IN_FLIGHT; ++i) {
        e.buffer.buffers[i] = buffers[i];
        e.buffer.allocations[i] = allocations[i];
        e.buffer.stagingBuffers[i] = stagingBuffers[i];
        e.buffer.stagingAllocations[i] = stagingAllocations[i];

        buffers[i] = VK_NULL_HANDLE;
        allocations[i] = nullptr;
        stagingBuffers[i] = VK_NULL_HANDLE;
        stagingAllocations[i] = nullptr;
        pendingDynamicUpdates[i].clear();
    }

    QRHI_RES_RHI(QRhiVulkan);
    // destroy() implementations, unlike other functions, are expected to test
    // for m_rhi being null, to allow surviving in case one attempts to destroy
    // a (leaked) resource after the QRhi.
    if (rhiD) {
        rhiD->releaseQueue.append(e);
        rhiD->unregisterResource(this);
    }
}

//  from src/gui/rhi/qrhivulkan.cpp, line 7315, as _ZN9QVkBuffer12nativeBufferEv
inline QRhiBuffer::NativeBuffer QVkBuffer::nativeBuffer()
{
    if (m_type == Dynamic) {
        QRHI_RES_RHI(QRhiVulkan);
        NativeBuffer b;
        Q_ASSERT(sizeof(b.objects) / sizeof(b.objects[0]) >= size_t(QVK_FRAMES_IN_FLIGHT));
        for (int i = 0; i < QVK_FRAMES_IN_FLIGHT; ++i) {
            rhiD->executeBufferHostWritesForSlot(this, i);
            b.objects[i] = &buffers[i];
        }
        b.slotCount = QVK_FRAMES_IN_FLIGHT;
        return b;
    }
    return { { &buffers[0] }, 1 };
}
//  -----------------------------------------------------------------------

//  A QVkBuffer that Python can take functions over in. Every QVkBuffer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQVkBufferCall0)(const void *, int *);
typedef bool (*CuteQVkBufferCall1)(const void *, int *);
typedef const QRhiBuffer::NativeBuffer * (*CuteQVkBufferCall2)(const void *, int *);
typedef void (*CuteQVkBufferCall3)(const void *, int *);
typedef int (*CuteQVkBufferCall4)(const void *, int *);
class CuteQVkBuffer : public QVkBuffer {
public:
  using QVkBuffer::QVkBuffer;
  void *taken[5] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN12QRhiResource7destroyEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QRhiBuffer6createEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QRhiBuffer12nativeBufferEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QRhiBuffer41endFullDynamicBufferUpdateForCurrentFrameEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QRhiResource12resourceTypeEv")) {
      taken[4] = call;
      return true;
    }
    return false;
  }

  //  void QVkBuffer::destroy()
  void destroy() override {
    if (taken[0]) {
      int handled = 0;
      CuteQVkBufferCall0 call = reinterpret_cast<CuteQVkBufferCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QVkBuffer::destroy();
  }

  //  bool QVkBuffer::create()
  bool create() override {
    if (taken[1]) {
      int handled = 0;
      CuteQVkBufferCall1 call = reinterpret_cast<CuteQVkBufferCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QVkBuffer::create();
  }

  //  QRhiBuffer::NativeBuffer QVkBuffer::nativeBuffer()
  QRhiBuffer::NativeBuffer nativeBuffer() override {
    if (taken[2]) {
      int handled = 0;
      CuteQVkBufferCall2 call = reinterpret_cast<CuteQVkBufferCall2>(taken[2]);
      const QRhiBuffer::NativeBuffer * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QVkBuffer::nativeBuffer();
  }

  //  void QVkBuffer::endFullDynamicBufferUpdateForCurrentFrame()
  void endFullDynamicBufferUpdateForCurrentFrame() override {
    if (taken[3]) {
      int handled = 0;
      CuteQVkBufferCall3 call = reinterpret_cast<CuteQVkBufferCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QVkBuffer::endFullDynamicBufferUpdateForCurrentFrame();
  }

  //  QRhiResource::Type QRhiBuffer::resourceType() const
  QRhiResource::Type resourceType() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQVkBufferCall4 call = reinterpret_cast<CuteQVkBufferCall4>(taken[4]);
      int given = call(this, &handled);
      if (handled) return static_cast<QRhiResource::Type>(given);
    }
    return QRhiBuffer::resourceType();
  }
};

//  QVkBuffer::~QVkBuffer()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QVkBufferD1Ev(QVkBuffer *self) {
  delete self;
}

//  void QVkBuffer::destroy()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QVkBuffer7destroyEv(QVkBuffer *self) {
  self->destroy();
}

//  QRhiBuffer::NativeBuffer QVkBuffer::nativeBuffer()
extern "C" Q_DECL_EXPORT
QRhiBuffer::NativeBuffer *ritual_ZN9QVkBuffer12nativeBufferEv(
    QVkBuffer *self) {
  return new QRhiBuffer::NativeBuffer(self->nativeBuffer());
}

//  a Python function taken by a CuteQVkBuffer, for the function named by the
//      key
extern "C" Q_DECL_EXPORT
bool ritual_take_QVkBuffer(QVkBuffer *self, const char *key, void *call) {
  return static_cast<CuteQVkBuffer *>(self)->take(key, call);
}

//  void QVkBuffer::destroy()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QVkBuffer7destroyEv(QVkBuffer *self) {
  self->QVkBuffer::destroy();
}

#endif  // QT_CONFIG(vulkan) && __has_include(<vulkan/vulkan.h>)
