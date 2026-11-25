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

//  from src/gui/rhi/qrhivulkan.cpp, line 9084, as _ZN16QVkCommandBuffer7destroyEv
inline void QVkCommandBuffer::destroy()
{
    // nothing to do here, cb is not owned by us
}

//  from src/gui/rhi/qrhivulkan.cpp, line 9089, as _ZN16QVkCommandBuffer13nativeHandlesEv
inline const QRhiNativeHandles *QVkCommandBuffer::nativeHandles()
{
    // Ok this is messy but no other way has been devised yet. Outside
    // begin(Compute)Pass - end(Compute)Pass it is simple - just return the
    // primary VkCommandBuffer. Inside, however, we need to provide the current
    // secondary command buffer (typically the one started by beginExternal(),
    // in case we are between beginExternal - endExternal inside a pass).

    if (recordingPass == QVkCommandBuffer::NoPass) {
        nativeHandlesStruct.commandBuffer = cb;
    } else {
        if (passUsesSecondaryCb && !activeSecondaryCbStack.isEmpty())
            nativeHandlesStruct.commandBuffer = activeSecondaryCbStack.last();
        else
            nativeHandlesStruct.commandBuffer = cb;
    }

    return &nativeHandlesStruct;
}
//  -----------------------------------------------------------------------

//  A QVkCommandBuffer that Python can take functions over in. Every QVkCommandBuffer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQVkCommandBufferCall0)(const void *, int *);
typedef int (*CuteQVkCommandBufferCall1)(const void *, int *);
class CuteQVkCommandBuffer : public QVkCommandBuffer {
public:
  using QVkCommandBuffer::QVkCommandBuffer;
  void *taken[2] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN12QRhiResource7destroyEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QRhiResource12resourceTypeEv")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

  //  void QVkCommandBuffer::destroy()
  void destroy() override {
    if (taken[0]) {
      int handled = 0;
      CuteQVkCommandBufferCall0 call = reinterpret_cast<CuteQVkCommandBufferCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QVkCommandBuffer::destroy();
  }

  //  QRhiResource::Type QRhiCommandBuffer::resourceType() const
  QRhiResource::Type resourceType() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQVkCommandBufferCall1 call = reinterpret_cast<CuteQVkCommandBufferCall1>(taken[1]);
      int given = call(this, &handled);
      if (handled) return static_cast<QRhiResource::Type>(given);
    }
    return QRhiCommandBuffer::resourceType();
  }
};

//  QVkCommandBuffer::QVkCommandBuffer(QRhiImplementation *rhi)
extern "C" Q_DECL_EXPORT
QVkCommandBuffer *ritual_ZN16QVkCommandBufferC1EP18QRhiImplementation(
    QRhiImplementation *rhi) {
  return new CuteQVkCommandBuffer(rhi);
}

//  QVkCommandBuffer::~QVkCommandBuffer()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QVkCommandBufferD1Ev(QVkCommandBuffer *self) {
  delete self;
}

//  void QVkCommandBuffer::destroy()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QVkCommandBuffer7destroyEv(QVkCommandBuffer *self) {
  self->destroy();
}

//  const QRhiNativeHandles *QVkCommandBuffer::nativeHandles()
extern "C" Q_DECL_EXPORT
const QRhiNativeHandles *ritual_ZN16QVkCommandBuffer13nativeHandlesEv(
    QVkCommandBuffer *self) {
  return self->nativeHandles();
}

//  void QVkCommandBuffer::resetState()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QVkCommandBuffer10resetStateEv(QVkCommandBuffer *self) {
  self->resetState();
}

//  void QVkCommandBuffer::resetPerPassState()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QVkCommandBuffer17resetPerPassStateEv(
    QVkCommandBuffer *self) {
  self->resetPerPassState();
}

//  void QVkCommandBuffer::resetCommands()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QVkCommandBuffer13resetCommandsEv(QVkCommandBuffer *self) {
  self->resetCommands();
}

//  void QVkCommandBuffer::resetPools()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QVkCommandBuffer10resetPoolsEv(QVkCommandBuffer *self) {
  self->resetPools();
}

//  a Python function taken by a CuteQVkCommandBuffer, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QVkCommandBuffer(
    QVkCommandBuffer *self,
    const char *key,
    void *call) {
  return static_cast<CuteQVkCommandBuffer *>(self)->take(key, call);
}

//  void QVkCommandBuffer::destroy()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QVkCommandBuffer7destroyEv(QVkCommandBuffer *self) {
  self->QVkCommandBuffer::destroy();
}

#endif  // QT_CONFIG(vulkan) && __has_include(<vulkan/vulkan.h>)
