//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qrhigles2_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qrhigles2_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qsize.h>
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

//  from src/gui/rhi/qrhigles2.cpp, line 6498, as _ZN27QGles2SwapChainRenderTargetC1EP18QRhiImplementationP13QRhiSwapChain
inline QGles2SwapChainRenderTarget::QGles2SwapChainRenderTarget(QRhiImplementation *rhi, QRhiSwapChain *swapchain)
    : QRhiSwapChainRenderTarget(rhi, swapchain),
      d(rhi)
{
}

//  from src/gui/rhi/qrhigles2.cpp, line 6504, as _ZN27QGles2SwapChainRenderTargetD1Ev
inline QGles2SwapChainRenderTarget::~QGles2SwapChainRenderTarget()
{
    destroy();
}

//  from src/gui/rhi/qrhigles2.cpp, line 6509, as _ZN27QGles2SwapChainRenderTarget7destroyEv
inline void QGles2SwapChainRenderTarget::destroy()
{
    // nothing to do here
}

//  from src/gui/rhi/qrhigles2.cpp, line 6514, as _ZNK27QGles2SwapChainRenderTarget9pixelSizeEv
inline QSize QGles2SwapChainRenderTarget::pixelSize() const
{
    return d.pixelSize;
}

//  from src/gui/rhi/qrhigles2.cpp, line 6519, as _ZNK27QGles2SwapChainRenderTarget16devicePixelRatioEv
inline float QGles2SwapChainRenderTarget::devicePixelRatio() const
{
    return d.dpr;
}

//  from src/gui/rhi/qrhigles2.cpp, line 6524, as _ZNK27QGles2SwapChainRenderTarget11sampleCountEv
inline int QGles2SwapChainRenderTarget::sampleCount() const
{
    return d.sampleCount;
}
//  -----------------------------------------------------------------------

//  A QGles2SwapChainRenderTarget that Python can take functions over in. Every QGles2SwapChainRenderTarget
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQGles2SwapChainRenderTargetCall0)(const void *, int *);
typedef const QSize * (*CuteQGles2SwapChainRenderTargetCall1)(const void *, int *);
typedef float (*CuteQGles2SwapChainRenderTargetCall2)(const void *, int *);
typedef int (*CuteQGles2SwapChainRenderTargetCall3)(const void *, int *);
typedef int (*CuteQGles2SwapChainRenderTargetCall4)(const void *, int *);
class CuteQGles2SwapChainRenderTarget : public QGles2SwapChainRenderTarget {
public:
  using QGles2SwapChainRenderTarget::QGles2SwapChainRenderTarget;
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

  //  void QGles2SwapChainRenderTarget::destroy()
  void destroy() override {
    if (taken[0]) {
      int handled = 0;
      CuteQGles2SwapChainRenderTargetCall0 call = reinterpret_cast<CuteQGles2SwapChainRenderTargetCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QGles2SwapChainRenderTarget::destroy();
  }

  //  QSize QGles2SwapChainRenderTarget::pixelSize() const
  QSize pixelSize() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQGles2SwapChainRenderTargetCall1 call = reinterpret_cast<CuteQGles2SwapChainRenderTargetCall1>(taken[1]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QGles2SwapChainRenderTarget::pixelSize();
  }

  //  float QGles2SwapChainRenderTarget::devicePixelRatio() const
  float devicePixelRatio() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQGles2SwapChainRenderTargetCall2 call = reinterpret_cast<CuteQGles2SwapChainRenderTargetCall2>(taken[2]);
      float given = call(this, &handled);
      if (handled) return given;
    }
    return QGles2SwapChainRenderTarget::devicePixelRatio();
  }

  //  int QGles2SwapChainRenderTarget::sampleCount() const
  int sampleCount() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQGles2SwapChainRenderTargetCall3 call = reinterpret_cast<CuteQGles2SwapChainRenderTargetCall3>(taken[3]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QGles2SwapChainRenderTarget::sampleCount();
  }

  //  QRhiResource::Type QRhiSwapChainRenderTarget::resourceType() const
  QRhiResource::Type resourceType() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQGles2SwapChainRenderTargetCall4 call = reinterpret_cast<CuteQGles2SwapChainRenderTargetCall4>(taken[4]);
      int given = call(this, &handled);
      if (handled) return static_cast<QRhiResource::Type>(given);
    }
    return QRhiSwapChainRenderTarget::resourceType();
  }
};

//  QGles2SwapChainRenderTarget::QGles2SwapChainRenderTarget(QRhiImplementati
//      on *rhi, QRhiSwapChain *swapchain)
extern "C" Q_DECL_EXPORT
QGles2SwapChainRenderTarget *ritual_ZN27QGles2SwapChainRenderTargetC1EP18QRhiImplementationP13QRhiSwapChain(
    QRhiImplementation *rhi,
    QRhiSwapChain *swapchain) {
  return new CuteQGles2SwapChainRenderTarget(rhi, swapchain);
}

//  QGles2SwapChainRenderTarget::~QGles2SwapChainRenderTarget()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QGles2SwapChainRenderTargetD1Ev(
    QGles2SwapChainRenderTarget *self) {
  delete self;
}

//  void QGles2SwapChainRenderTarget::destroy()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QGles2SwapChainRenderTarget7destroyEv(
    QGles2SwapChainRenderTarget *self) {
  self->destroy();
}

//  QSize QGles2SwapChainRenderTarget::pixelSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK27QGles2SwapChainRenderTarget9pixelSizeEv(
    const QGles2SwapChainRenderTarget *self) {
  return new QSize(self->pixelSize());
}

//  float QGles2SwapChainRenderTarget::devicePixelRatio() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK27QGles2SwapChainRenderTarget16devicePixelRatioEv(
    const QGles2SwapChainRenderTarget *self) {
  return self->devicePixelRatio();
}

//  int QGles2SwapChainRenderTarget::sampleCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK27QGles2SwapChainRenderTarget11sampleCountEv(
    const QGles2SwapChainRenderTarget *self) {
  return self->sampleCount();
}

//  a Python function taken by a CuteQGles2SwapChainRenderTarget, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGles2SwapChainRenderTarget(
    QGles2SwapChainRenderTarget *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGles2SwapChainRenderTarget *>(self)->take(key, call);
}

//  void QGles2SwapChainRenderTarget::destroy()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN27QGles2SwapChainRenderTarget7destroyEv(
    QGles2SwapChainRenderTarget *self) {
  self->QGles2SwapChainRenderTarget::destroy();
}

//  QSize QGles2SwapChainRenderTarget::pixelSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK27QGles2SwapChainRenderTarget9pixelSizeEv(
    const QGles2SwapChainRenderTarget *self) {
  return new QSize(self->QGles2SwapChainRenderTarget::pixelSize());
}

//  float QGles2SwapChainRenderTarget::devicePixelRatio() const
extern "C" Q_DECL_EXPORT
float ritual_own_ZNK27QGles2SwapChainRenderTarget16devicePixelRatioEv(
    const QGles2SwapChainRenderTarget *self) {
  return self->QGles2SwapChainRenderTarget::devicePixelRatio();
}

//  int QGles2SwapChainRenderTarget::sampleCount() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK27QGles2SwapChainRenderTarget11sampleCountEv(
    const QGles2SwapChainRenderTarget *self) {
  return self->QGles2SwapChainRenderTarget::sampleCount();
}
