//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qrhinull_p.h, Qt 6.12.0. Edited by hand on
//  2026-11-25: the line pulling in 'qrhivulkan_p.h' stands under
//  '__has_include(<vulkan/vulkan.h>)' as well, as Qt's 'qvulkaninstance.h'
//  checks it: that header needs the headers of Vulkan, outside Qt, which a
//  machine may lack, and no ritual here needs it. The line pulling in
//  'qrhid3d12_p.h' stands under '__has_include(<D3D12MemAlloc.h>)': that
//  header includes 'D3D12MemAlloc.h', a library Qt keeps in its source and
//  never installs, and no ritual here needs it. Kept as it is when the
//  generator runs again.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qrhinull_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/private/qrhi_p.h>
#include <QtCore/qmath.h>
#include <QtCore/QLoggingCategory>
#include <QtCore/private/qloggingregistry_p.h>
#include <QtGui/private/qrhinull_p.h>
#ifndef QT_NO_OPENGL
#include <QtGui/private/qrhigles2_p.h>
#endif
#if QT_CONFIG(vulkan) && __has_include(<vulkan/vulkan.h>)
#include <QtGui/private/qrhivulkan_p.h>
#endif
#ifdef Q_OS_WIN
#include <QtGui/private/qrhid3d11_p.h>
#if __has_include(<D3D12MemAlloc.h>)
#include <QtGui/private/qrhid3d12_p.h>
#endif
#endif
#if QT_CONFIG(metal)
#include <QtGui/private/qrhimetal_p.h>
#endif
#include <limits>
#include <memory>
#include <QtGui/private/qrhinull_p.h>
#include <QtCore/qmath.h>
#include <QtGui/QPainter>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/gui/rhi/qrhi.cpp, line 8906, as _ZN18QRhiImplementation27sanityCheckGraphicsPipelineEP20QRhiGraphicsPipeline
inline bool QRhiImplementation::sanityCheckGraphicsPipeline(QRhiGraphicsPipeline *ps)
{
    if (ps->cbeginShaderStages() == ps->cendShaderStages()) {
        qWarning("Cannot build a graphics pipeline without any stages");
        return false;
    }

    bool hasVertexStage = false;
    for (auto it = ps->cbeginShaderStages(), itEnd = ps->cendShaderStages(); it != itEnd; ++it) {
        if (!it->shader().isValid()) {
            qWarning("Empty shader passed to graphics pipeline");
            return false;
        }
        if (it->type() == QRhiShaderStage::Vertex)
            hasVertexStage = true;
    }
    if (!hasVertexStage) {
        qWarning("Cannot build a graphics pipeline without a vertex stage");
        return false;
    }

    if (!ps->renderPassDescriptor()) {
        qWarning("Cannot build a graphics pipeline without a QRhiRenderPassDescriptor");
        return false;
    }

    if (!ps->shaderResourceBindings()) {
        qWarning("Cannot build a graphics pipeline without QRhiShaderResourceBindings");
        return false;
    }

    return true;
}

//  from src/gui/rhi/qrhinull.cpp, line 976, as _ZN21QNullGraphicsPipelineC1EP18QRhiImplementation
inline QNullGraphicsPipeline::QNullGraphicsPipeline(QRhiImplementation *rhi)
    : QRhiGraphicsPipeline(rhi)
{
}

//  from src/gui/rhi/qrhinull.cpp, line 981, as _ZN21QNullGraphicsPipelineD1Ev
inline QNullGraphicsPipeline::~QNullGraphicsPipeline()
{
    destroy();
}

//  from src/gui/rhi/qrhinull.cpp, line 986, as _ZN21QNullGraphicsPipeline7destroyEv
inline void QNullGraphicsPipeline::destroy()
{
    QRHI_RES_RHI(QRhiNull);
    if (rhiD)
        rhiD->unregisterResource(this);
}

//  from src/gui/rhi/qrhinull.cpp, line 993, as _ZN21QNullGraphicsPipeline6createEv
inline bool QNullGraphicsPipeline::create()
{
    QRHI_RES_RHI(QRhiNull);
    if (!rhiD->sanityCheckGraphicsPipeline(this))
        return false;

    rhiD->registerResource(this);
    return true;
}
//  -----------------------------------------------------------------------

//  A QNullGraphicsPipeline that Python can take functions over in. Every QNullGraphicsPipeline
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQNullGraphicsPipelineCall0)(const void *, int *);
typedef bool (*CuteQNullGraphicsPipelineCall1)(const void *, int *);
typedef int (*CuteQNullGraphicsPipelineCall2)(const void *, int *);
class CuteQNullGraphicsPipeline : public QNullGraphicsPipeline {
public:
  using QNullGraphicsPipeline::QNullGraphicsPipeline;
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

  //  void QNullGraphicsPipeline::destroy()
  void destroy() override {
    if (taken[0]) {
      int handled = 0;
      CuteQNullGraphicsPipelineCall0 call = reinterpret_cast<CuteQNullGraphicsPipelineCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QNullGraphicsPipeline::destroy();
  }

  //  bool QNullGraphicsPipeline::create()
  bool create() override {
    if (taken[1]) {
      int handled = 0;
      CuteQNullGraphicsPipelineCall1 call = reinterpret_cast<CuteQNullGraphicsPipelineCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QNullGraphicsPipeline::create();
  }

  //  QRhiResource::Type QRhiGraphicsPipeline::resourceType() const
  QRhiResource::Type resourceType() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQNullGraphicsPipelineCall2 call = reinterpret_cast<CuteQNullGraphicsPipelineCall2>(taken[2]);
      int given = call(this, &handled);
      if (handled) return static_cast<QRhiResource::Type>(given);
    }
    return QRhiGraphicsPipeline::resourceType();
  }
};

//  QNullGraphicsPipeline::QNullGraphicsPipeline(QRhiImplementation *rhi)
extern "C" Q_DECL_EXPORT
QNullGraphicsPipeline *ritual_ZN21QNullGraphicsPipelineC1EP18QRhiImplementation(
    QRhiImplementation *rhi) {
  return new CuteQNullGraphicsPipeline(rhi);
}

//  QNullGraphicsPipeline::~QNullGraphicsPipeline()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QNullGraphicsPipelineD1Ev(QNullGraphicsPipeline *self) {
  delete self;
}

//  void QNullGraphicsPipeline::destroy()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QNullGraphicsPipeline7destroyEv(
    QNullGraphicsPipeline *self) {
  self->destroy();
}

//  bool QNullGraphicsPipeline::create()
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QNullGraphicsPipeline6createEv(QNullGraphicsPipeline *self) {
  return self->create();
}

//  a Python function taken by a CuteQNullGraphicsPipeline, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QNullGraphicsPipeline(
    QNullGraphicsPipeline *self,
    const char *key,
    void *call) {
  return static_cast<CuteQNullGraphicsPipeline *>(self)->take(key, call);
}

//  void QNullGraphicsPipeline::destroy()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QNullGraphicsPipeline7destroyEv(
    QNullGraphicsPipeline *self) {
  self->QNullGraphicsPipeline::destroy();
}

//  bool QNullGraphicsPipeline::create()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN21QNullGraphicsPipeline6createEv(
    QNullGraphicsPipeline *self) {
  return self->QNullGraphicsPipeline::create();
}
