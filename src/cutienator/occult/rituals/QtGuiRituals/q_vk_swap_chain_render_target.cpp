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
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

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

//  from src/gui/rhi/qrhivulkan.cpp, line 8179, as _ZN24QVkSwapChainRenderTarget7destroyEv
inline void QVkSwapChainRenderTarget::destroy()
{
    // nothing to do here
}

//  from src/gui/rhi/qrhivulkan.cpp, line 8184, as _ZNK24QVkSwapChainRenderTarget9pixelSizeEv
inline QSize QVkSwapChainRenderTarget::pixelSize() const
{
    return d.pixelSize;
}

//  from src/gui/rhi/qrhivulkan.cpp, line 8189, as _ZNK24QVkSwapChainRenderTarget16devicePixelRatioEv
inline float QVkSwapChainRenderTarget::devicePixelRatio() const
{
    return d.dpr;
}

//  from src/gui/rhi/qrhivulkan.cpp, line 8194, as _ZNK24QVkSwapChainRenderTarget11sampleCountEv
inline int QVkSwapChainRenderTarget::sampleCount() const
{
    return d.sampleCount;
}
//  -----------------------------------------------------------------------

//  A QVkSwapChainRenderTarget that Python can take functions over in. Every QVkSwapChainRenderTarget
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQVkSwapChainRenderTargetCall0)(const void *, int *);
typedef const QSize * (*CuteQVkSwapChainRenderTargetCall1)(const void *, int *);
typedef float (*CuteQVkSwapChainRenderTargetCall2)(const void *, int *);
typedef int (*CuteQVkSwapChainRenderTargetCall3)(const void *, int *);
typedef int (*CuteQVkSwapChainRenderTargetCall4)(const void *, int *);
class CuteQVkSwapChainRenderTarget : public QVkSwapChainRenderTarget {
public:
  using QVkSwapChainRenderTarget::QVkSwapChainRenderTarget;
  void *taken[5] = {};

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
    if (!std::strcmp(key, "_ZNK12QRhiResource12resourceTypeEv")) {
      taken[4] = call;
      return true;
    }
    return false;
  }

  //  void QVkSwapChainRenderTarget::destroy()
  void destroy() override {
    if (taken[0]) {
      int handled = 0;
      CuteQVkSwapChainRenderTargetCall0 call = reinterpret_cast<CuteQVkSwapChainRenderTargetCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QVkSwapChainRenderTarget::destroy();
  }

  //  QSize QVkSwapChainRenderTarget::pixelSize() const
  QSize pixelSize() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQVkSwapChainRenderTargetCall1 call = reinterpret_cast<CuteQVkSwapChainRenderTargetCall1>(taken[1]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QVkSwapChainRenderTarget::pixelSize();
  }

  //  float QVkSwapChainRenderTarget::devicePixelRatio() const
  float devicePixelRatio() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQVkSwapChainRenderTargetCall2 call = reinterpret_cast<CuteQVkSwapChainRenderTargetCall2>(taken[2]);
      float given = call(this, &handled);
      if (handled) return given;
    }
    return QVkSwapChainRenderTarget::devicePixelRatio();
  }

  //  int QVkSwapChainRenderTarget::sampleCount() const
  int sampleCount() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQVkSwapChainRenderTargetCall3 call = reinterpret_cast<CuteQVkSwapChainRenderTargetCall3>(taken[3]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QVkSwapChainRenderTarget::sampleCount();
  }

  //  QRhiResource::Type QRhiSwapChainRenderTarget::resourceType() const
  QRhiResource::Type resourceType() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQVkSwapChainRenderTargetCall4 call = reinterpret_cast<CuteQVkSwapChainRenderTargetCall4>(taken[4]);
      int given = call(this, &handled);
      if (handled) return static_cast<QRhiResource::Type>(given);
    }
    return QRhiSwapChainRenderTarget::resourceType();
  }
};

//  QVkSwapChainRenderTarget::QVkSwapChainRenderTarget(QRhiImplementation
//      *rhi, QRhiSwapChain *swapchain)
extern "C" Q_DECL_EXPORT
QVkSwapChainRenderTarget *ritual_ZN24QVkSwapChainRenderTargetC1EP18QRhiImplementationP13QRhiSwapChain(
    QRhiImplementation *rhi,
    QRhiSwapChain *swapchain) {
  return new CuteQVkSwapChainRenderTarget(rhi, swapchain);
}

//  QVkSwapChainRenderTarget::~QVkSwapChainRenderTarget()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QVkSwapChainRenderTargetD1Ev(
    QVkSwapChainRenderTarget *self) {
  delete self;
}

//  void QVkSwapChainRenderTarget::destroy()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QVkSwapChainRenderTarget7destroyEv(
    QVkSwapChainRenderTarget *self) {
  self->destroy();
}

//  QSize QVkSwapChainRenderTarget::pixelSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK24QVkSwapChainRenderTarget9pixelSizeEv(
    const QVkSwapChainRenderTarget *self) {
  return new QSize(self->pixelSize());
}

//  float QVkSwapChainRenderTarget::devicePixelRatio() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK24QVkSwapChainRenderTarget16devicePixelRatioEv(
    const QVkSwapChainRenderTarget *self) {
  return self->devicePixelRatio();
}

//  int QVkSwapChainRenderTarget::sampleCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK24QVkSwapChainRenderTarget11sampleCountEv(
    const QVkSwapChainRenderTarget *self) {
  return self->sampleCount();
}

//  a Python function taken by a CuteQVkSwapChainRenderTarget, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QVkSwapChainRenderTarget(
    QVkSwapChainRenderTarget *self,
    const char *key,
    void *call) {
  return static_cast<CuteQVkSwapChainRenderTarget *>(self)->take(key, call);
}

//  void QVkSwapChainRenderTarget::destroy()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QVkSwapChainRenderTarget7destroyEv(
    QVkSwapChainRenderTarget *self) {
  self->QVkSwapChainRenderTarget::destroy();
}

//  QSize QVkSwapChainRenderTarget::pixelSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK24QVkSwapChainRenderTarget9pixelSizeEv(
    const QVkSwapChainRenderTarget *self) {
  return new QSize(self->QVkSwapChainRenderTarget::pixelSize());
}

//  float QVkSwapChainRenderTarget::devicePixelRatio() const
extern "C" Q_DECL_EXPORT
float ritual_own_ZNK24QVkSwapChainRenderTarget16devicePixelRatioEv(
    const QVkSwapChainRenderTarget *self) {
  return self->QVkSwapChainRenderTarget::devicePixelRatio();
}

//  int QVkSwapChainRenderTarget::sampleCount() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK24QVkSwapChainRenderTarget11sampleCountEv(
    const QVkSwapChainRenderTarget *self) {
  return self->QVkSwapChainRenderTarget::sampleCount();
}

#endif  // QT_CONFIG(vulkan) && __has_include(<vulkan/vulkan.h>)
