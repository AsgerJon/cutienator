//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qrhivulkan_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-25: the whole file also stands under
//  '__has_include(<vulkan/vulkan.h>)', since Qt's 'qrhivulkan_p.h' does
//  not compile on a machine without the headers of Vulkan.
//  Kept as it is when the generator runs again.
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
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/gui/rhi/qrhivulkan.cpp, line 7841, as _ZN10QVkSamplerD1Ev
inline QVkSampler::~QVkSampler()
{
    destroy();
}

//  from src/gui/rhi/qrhivulkan.cpp, line 7846, as _ZN10QVkSampler7destroyEv
inline void QVkSampler::destroy()
{
    if (!sampler)
        return;

    QRhiVulkan::DeferredReleaseEntry e;
    e.type = QRhiVulkan::DeferredReleaseEntry::Sampler;
    e.lastActiveFrameSlot = lastActiveFrameSlot;

    e.sampler.sampler = sampler;
    sampler = VK_NULL_HANDLE;

    QRHI_RES_RHI(QRhiVulkan);
    if (rhiD) {
        rhiD->releaseQueue.append(e);
        rhiD->unregisterResource(this);
    }
}
//  -----------------------------------------------------------------------

//  A QVkSampler that Python can take functions over in. Every QVkSampler
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQVkSamplerCall0)(const void *, int *);
typedef bool (*CuteQVkSamplerCall1)(const void *, int *);
typedef int (*CuteQVkSamplerCall2)(const void *, int *);
class CuteQVkSampler : public QVkSampler {
public:
  using QVkSampler::QVkSampler;
  void *taken[3] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN12QRhiResource7destroyEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QRhiSampler6createEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QRhiResource12resourceTypeEv")) {
      taken[2] = call;
      return true;
    }
    return false;
  }

  //  void QVkSampler::destroy()
  void destroy() override {
    if (taken[0]) {
      int handled = 0;
      CuteQVkSamplerCall0 call = reinterpret_cast<CuteQVkSamplerCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QVkSampler::destroy();
  }

  //  bool QVkSampler::create()
  bool create() override {
    if (taken[1]) {
      int handled = 0;
      CuteQVkSamplerCall1 call = reinterpret_cast<CuteQVkSamplerCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QVkSampler::create();
  }

  //  QRhiResource::Type QRhiSampler::resourceType() const
  QRhiResource::Type resourceType() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQVkSamplerCall2 call = reinterpret_cast<CuteQVkSamplerCall2>(taken[2]);
      int given = call(this, &handled);
      if (handled) return static_cast<QRhiResource::Type>(given);
    }
    return QRhiSampler::resourceType();
  }
};

//  QVkSampler::~QVkSampler()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QVkSamplerD1Ev(QVkSampler *self) {
  delete self;
}

//  void QVkSampler::destroy()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QVkSampler7destroyEv(QVkSampler *self) {
  self->destroy();
}

//  a Python function taken by a CuteQVkSampler, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QVkSampler(QVkSampler *self, const char *key, void *call) {
  return static_cast<CuteQVkSampler *>(self)->take(key, call);
}

//  void QVkSampler::destroy()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QVkSampler7destroyEv(QVkSampler *self) {
  self->QVkSampler::destroy();
}

#endif  // QT_CONFIG(vulkan) && __has_include(<vulkan/vulkan.h>)
