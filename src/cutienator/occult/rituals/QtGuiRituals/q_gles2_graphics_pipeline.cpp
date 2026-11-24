//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qrhigles2_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qrhigles2_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qrhigles2_p.h"
#include <QOffscreenSurface>
#include <QOpenGLContext>
#include <QtCore/qmap.h>
#include <QtGui/private/qguiapplication_p.h>
#include <QtGui/private/qopenglextensions_p.h>
#include <QtGui/private/qopenglprogrambinarycache_p.h>
#include <QtGui/private/qwindow_p.h>
#include <qpa/qplatformopenglcontext.h>
#include <qmath.h>
#include <limits>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/gui/rhi/qrhigles2.cpp, line 6909, as _ZN22QGles2GraphicsPipelineD1Ev
inline QGles2GraphicsPipeline::~QGles2GraphicsPipeline()
{
    destroy();
}

//  from src/gui/rhi/qrhigles2.cpp, line 6914, as _ZN22QGles2GraphicsPipeline7destroyEv
inline void QGles2GraphicsPipeline::destroy()
{
    if (!program)
        return;

    QRhiGles2::DeferredReleaseEntry e;
    e.type = QRhiGles2::DeferredReleaseEntry::Pipeline;

    e.pipeline.program = program;

    program = 0;
    uniforms.clear();
    samplers.clear();

    QRHI_RES_RHI(QRhiGles2);
    if (rhiD) {
        rhiD->releaseQueue.append(e);
        rhiD->unregisterResource(this);
    }
}
//  -----------------------------------------------------------------------

//  A QGles2GraphicsPipeline that Python can take functions over in. Every QGles2GraphicsPipeline
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQGles2GraphicsPipelineCall0)(const void *, int *);
typedef bool (*CuteQGles2GraphicsPipelineCall1)(const void *, int *);
typedef int (*CuteQGles2GraphicsPipelineCall2)(const void *, int *);
class CuteQGles2GraphicsPipeline : public QGles2GraphicsPipeline {
public:
  using QGles2GraphicsPipeline::QGles2GraphicsPipeline;
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

  //  void QGles2GraphicsPipeline::destroy()
  void destroy() override {
    if (taken[0]) {
      int handled = 0;
      CuteQGles2GraphicsPipelineCall0 call = reinterpret_cast<CuteQGles2GraphicsPipelineCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QGles2GraphicsPipeline::destroy();
  }

  //  bool QGles2GraphicsPipeline::create()
  bool create() override {
    if (taken[1]) {
      int handled = 0;
      CuteQGles2GraphicsPipelineCall1 call = reinterpret_cast<CuteQGles2GraphicsPipelineCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QGles2GraphicsPipeline::create();
  }

  //  QRhiResource::Type QRhiGraphicsPipeline::resourceType() const
  QRhiResource::Type resourceType() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQGles2GraphicsPipelineCall2 call = reinterpret_cast<CuteQGles2GraphicsPipelineCall2>(taken[2]);
      int given = call(this, &handled);
      if (handled) return static_cast<QRhiResource::Type>(given);
    }
    return QRhiGraphicsPipeline::resourceType();
  }
};

//  QGles2GraphicsPipeline::~QGles2GraphicsPipeline()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGles2GraphicsPipelineD1Ev(QGles2GraphicsPipeline *self) {
  delete self;
}

//  void QGles2GraphicsPipeline::destroy()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGles2GraphicsPipeline7destroyEv(
    QGles2GraphicsPipeline *self) {
  self->destroy();
}

//  a Python function taken by a CuteQGles2GraphicsPipeline, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGles2GraphicsPipeline(
    QGles2GraphicsPipeline *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGles2GraphicsPipeline *>(self)->take(key, call);
}

//  void QGles2GraphicsPipeline::destroy()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QGles2GraphicsPipeline7destroyEv(
    QGles2GraphicsPipeline *self) {
  self->QGles2GraphicsPipeline::destroy();
}
