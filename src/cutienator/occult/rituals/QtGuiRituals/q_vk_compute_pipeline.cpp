//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qrhivulkan_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-25: the whole file now also asks
//  '__has_include(<vulkan/vulkan.h>)', as Qt's 'qvulkaninstance.h'
//  does: 'qrhivulkan_p.h' needs 'vulkan/vulkan.h' of Vulkan, outside
//  Qt, which a machine may lack although its Qt has Vulkan. Kept as it
//  is when the generator runs again.
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

//  from src/gui/rhi/qrhivulkan.cpp, line 8972, as _ZN18QVkComputePipelineD1Ev
inline QVkComputePipeline::~QVkComputePipeline()
{
    destroy();
}

//  from src/gui/rhi/qrhivulkan.cpp, line 8977, as _ZN18QVkComputePipeline7destroyEv
inline void QVkComputePipeline::destroy()
{
    if (!pipeline && !layout)
        return;

    QRhiVulkan::DeferredReleaseEntry e;
    e.type = QRhiVulkan::DeferredReleaseEntry::Pipeline;
    e.lastActiveFrameSlot = lastActiveFrameSlot;

    e.pipelineState.pipeline = pipeline;
    e.pipelineState.layout = layout;

    pipeline = VK_NULL_HANDLE;
    layout = VK_NULL_HANDLE;

    QRHI_RES_RHI(QRhiVulkan);
    if (rhiD) {
        rhiD->releaseQueue.append(e);
        rhiD->unregisterResource(this);
    }
}
//  -----------------------------------------------------------------------

//  A QVkComputePipeline that Python can take functions over in. Every QVkComputePipeline
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQVkComputePipelineCall0)(const void *, int *);
typedef bool (*CuteQVkComputePipelineCall1)(const void *, int *);
typedef int (*CuteQVkComputePipelineCall2)(const void *, int *);
class CuteQVkComputePipeline : public QVkComputePipeline {
public:
  using QVkComputePipeline::QVkComputePipeline;
  void *taken[3] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN12QRhiResource7destroyEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QRhiComputePipeline6createEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QRhiResource12resourceTypeEv")) {
      taken[2] = call;
      return true;
    }
    return false;
  }

  //  void QVkComputePipeline::destroy()
  void destroy() override {
    if (taken[0]) {
      int handled = 0;
      CuteQVkComputePipelineCall0 call = reinterpret_cast<CuteQVkComputePipelineCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QVkComputePipeline::destroy();
  }

  //  bool QVkComputePipeline::create()
  bool create() override {
    if (taken[1]) {
      int handled = 0;
      CuteQVkComputePipelineCall1 call = reinterpret_cast<CuteQVkComputePipelineCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QVkComputePipeline::create();
  }

  //  QRhiResource::Type QRhiComputePipeline::resourceType() const
  QRhiResource::Type resourceType() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQVkComputePipelineCall2 call = reinterpret_cast<CuteQVkComputePipelineCall2>(taken[2]);
      int given = call(this, &handled);
      if (handled) return static_cast<QRhiResource::Type>(given);
    }
    return QRhiComputePipeline::resourceType();
  }
};

//  QVkComputePipeline::~QVkComputePipeline()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QVkComputePipelineD1Ev(QVkComputePipeline *self) {
  delete self;
}

//  void QVkComputePipeline::destroy()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QVkComputePipeline7destroyEv(QVkComputePipeline *self) {
  self->destroy();
}

//  a Python function taken by a CuteQVkComputePipeline, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QVkComputePipeline(
    QVkComputePipeline *self,
    const char *key,
    void *call) {
  return static_cast<CuteQVkComputePipeline *>(self)->take(key, call);
}

//  void QVkComputePipeline::destroy()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QVkComputePipeline7destroyEv(QVkComputePipeline *self) {
  self->QVkComputePipeline::destroy();
}

#endif  // QT_CONFIG(vulkan) && __has_include(<vulkan/vulkan.h>)
