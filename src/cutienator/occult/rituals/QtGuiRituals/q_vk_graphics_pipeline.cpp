//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qrhivulkan_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-25: the whole file stands under
//  '__has_include(<vulkan/vulkan.h>)' as well, as Qt's
//  'qvulkaninstance.h' checks it: 'qrhivulkan_p.h' needs the headers
//  of Vulkan, outside Qt, which a machine may lack.
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
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/gui/rhi/qrhivulkan.cpp, line 8677, as _ZN19QVkGraphicsPipelineD1Ev
inline QVkGraphicsPipeline::~QVkGraphicsPipeline()
{
    destroy();
}

//  from src/gui/rhi/qrhivulkan.cpp, line 8682, as _ZN19QVkGraphicsPipeline7destroyEv
inline void QVkGraphicsPipeline::destroy()
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

//  A QVkGraphicsPipeline that Python can take functions over in. Every QVkGraphicsPipeline
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQVkGraphicsPipelineCall0)(const void *, int *);
typedef bool (*CuteQVkGraphicsPipelineCall1)(const void *, int *);
typedef int (*CuteQVkGraphicsPipelineCall2)(const void *, int *);
class CuteQVkGraphicsPipeline : public QVkGraphicsPipeline {
public:
  using QVkGraphicsPipeline::QVkGraphicsPipeline;
  void *taken[3] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN12QRhiResource7destroyEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QRhiGraphicsPipeline6createEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QRhiResource12resourceTypeEv")) {
      taken[2] = call;
      return true;
    }
    return false;
  }

  //  void QVkGraphicsPipeline::destroy()
  void destroy() override {
    if (taken[0]) {
      int handled = 0;
      CuteQVkGraphicsPipelineCall0 call = reinterpret_cast<CuteQVkGraphicsPipelineCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QVkGraphicsPipeline::destroy();
  }

  //  bool QVkGraphicsPipeline::create()
  bool create() override {
    if (taken[1]) {
      int handled = 0;
      CuteQVkGraphicsPipelineCall1 call = reinterpret_cast<CuteQVkGraphicsPipelineCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QVkGraphicsPipeline::create();
  }

  //  QRhiResource::Type QRhiGraphicsPipeline::resourceType() const
  QRhiResource::Type resourceType() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQVkGraphicsPipelineCall2 call = reinterpret_cast<CuteQVkGraphicsPipelineCall2>(taken[2]);
      int given = call(this, &handled);
      if (handled) return static_cast<QRhiResource::Type>(given);
    }
    return QRhiGraphicsPipeline::resourceType();
  }
};

//  QVkGraphicsPipeline::~QVkGraphicsPipeline()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QVkGraphicsPipelineD1Ev(QVkGraphicsPipeline *self) {
  delete self;
}

//  void QVkGraphicsPipeline::destroy()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QVkGraphicsPipeline7destroyEv(QVkGraphicsPipeline *self) {
  self->destroy();
}

//  a Python function taken by a CuteQVkGraphicsPipeline, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QVkGraphicsPipeline(
    QVkGraphicsPipeline *self,
    const char *key,
    void *call) {
  return static_cast<CuteQVkGraphicsPipeline *>(self)->take(key, call);
}

//  void QVkGraphicsPipeline::destroy()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QVkGraphicsPipeline7destroyEv(
    QVkGraphicsPipeline *self) {
  self->QVkGraphicsPipeline::destroy();
}

#endif  // QT_CONFIG(vulkan) && __has_include(<vulkan/vulkan.h>)
