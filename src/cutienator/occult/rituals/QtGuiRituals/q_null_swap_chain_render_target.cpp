//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qrhinull_p.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qrhinull_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qsize.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qrhinull_p.h"
#include <qmath.h>
#include <QPainter>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/gui/rhi/qrhinull.cpp, line 847, as _ZN26QNullSwapChainRenderTargetC1EP18QRhiImplementationP13QRhiSwapChain
inline QNullSwapChainRenderTarget::QNullSwapChainRenderTarget(QRhiImplementation *rhi, QRhiSwapChain *swapchain)
    : QRhiSwapChainRenderTarget(rhi, swapchain),
      d(rhi)
{
}

//  from src/gui/rhi/qrhinull.cpp, line 853, as _ZN26QNullSwapChainRenderTargetD1Ev
inline QNullSwapChainRenderTarget::~QNullSwapChainRenderTarget()
{
    destroy();
}

//  from src/gui/rhi/qrhinull.cpp, line 858, as _ZN26QNullSwapChainRenderTarget7destroyEv
inline void QNullSwapChainRenderTarget::destroy()
{
}

//  from src/gui/rhi/qrhinull.cpp, line 862, as _ZNK26QNullSwapChainRenderTarget9pixelSizeEv
inline QSize QNullSwapChainRenderTarget::pixelSize() const
{
    return d.pixelSize;
}

//  from src/gui/rhi/qrhinull.cpp, line 867, as _ZNK26QNullSwapChainRenderTarget16devicePixelRatioEv
inline float QNullSwapChainRenderTarget::devicePixelRatio() const
{
    return d.dpr;
}

//  from src/gui/rhi/qrhinull.cpp, line 872, as _ZNK26QNullSwapChainRenderTarget11sampleCountEv
inline int QNullSwapChainRenderTarget::sampleCount() const
{
    return 1;
}
//  -----------------------------------------------------------------------

//  A QNullSwapChainRenderTarget that Python can take functions over in. Every QNullSwapChainRenderTarget
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQNullSwapChainRenderTargetCall0)(const void *, int *);
typedef const QSize * (*CuteQNullSwapChainRenderTargetCall1)(const void *, int *);
typedef float (*CuteQNullSwapChainRenderTargetCall2)(const void *, int *);
typedef int (*CuteQNullSwapChainRenderTargetCall3)(const void *, int *);
typedef int (*CuteQNullSwapChainRenderTargetCall4)(const void *, int *);
class CuteQNullSwapChainRenderTarget : public QNullSwapChainRenderTarget {
public:
  using QNullSwapChainRenderTarget::QNullSwapChainRenderTarget;
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

  //  void QNullSwapChainRenderTarget::destroy()
  void destroy() override {
    if (taken[0]) {
      int handled = 0;
      CuteQNullSwapChainRenderTargetCall0 call = reinterpret_cast<CuteQNullSwapChainRenderTargetCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QNullSwapChainRenderTarget::destroy();
  }

  //  QSize QNullSwapChainRenderTarget::pixelSize() const
  QSize pixelSize() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQNullSwapChainRenderTargetCall1 call = reinterpret_cast<CuteQNullSwapChainRenderTargetCall1>(taken[1]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QNullSwapChainRenderTarget::pixelSize();
  }

  //  float QNullSwapChainRenderTarget::devicePixelRatio() const
  float devicePixelRatio() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQNullSwapChainRenderTargetCall2 call = reinterpret_cast<CuteQNullSwapChainRenderTargetCall2>(taken[2]);
      float given = call(this, &handled);
      if (handled) return given;
    }
    return QNullSwapChainRenderTarget::devicePixelRatio();
  }

  //  int QNullSwapChainRenderTarget::sampleCount() const
  int sampleCount() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQNullSwapChainRenderTargetCall3 call = reinterpret_cast<CuteQNullSwapChainRenderTargetCall3>(taken[3]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QNullSwapChainRenderTarget::sampleCount();
  }

  //  QRhiResource::Type QRhiSwapChainRenderTarget::resourceType() const
  QRhiResource::Type resourceType() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQNullSwapChainRenderTargetCall4 call = reinterpret_cast<CuteQNullSwapChainRenderTargetCall4>(taken[4]);
      int given = call(this, &handled);
      if (handled) return static_cast<QRhiResource::Type>(given);
    }
    return QRhiSwapChainRenderTarget::resourceType();
  }
};

//  QNullSwapChainRenderTarget::QNullSwapChainRenderTarget(QRhiImplementation
//      *rhi, QRhiSwapChain *swapchain)
extern "C" Q_DECL_EXPORT
QNullSwapChainRenderTarget *ritual_ZN26QNullSwapChainRenderTargetC1EP18QRhiImplementationP13QRhiSwapChain(
    QRhiImplementation *rhi,
    QRhiSwapChain *swapchain) {
  return new CuteQNullSwapChainRenderTarget(rhi, swapchain);
}

//  QNullSwapChainRenderTarget::~QNullSwapChainRenderTarget()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QNullSwapChainRenderTargetD1Ev(
    QNullSwapChainRenderTarget *self) {
  delete self;
}

//  void QNullSwapChainRenderTarget::destroy()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QNullSwapChainRenderTarget7destroyEv(
    QNullSwapChainRenderTarget *self) {
  self->destroy();
}

//  QSize QNullSwapChainRenderTarget::pixelSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK26QNullSwapChainRenderTarget9pixelSizeEv(
    const QNullSwapChainRenderTarget *self) {
  return new QSize(self->pixelSize());
}

//  float QNullSwapChainRenderTarget::devicePixelRatio() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK26QNullSwapChainRenderTarget16devicePixelRatioEv(
    const QNullSwapChainRenderTarget *self) {
  return self->devicePixelRatio();
}

//  int QNullSwapChainRenderTarget::sampleCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK26QNullSwapChainRenderTarget11sampleCountEv(
    const QNullSwapChainRenderTarget *self) {
  return self->sampleCount();
}

//  a Python function taken by a CuteQNullSwapChainRenderTarget, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QNullSwapChainRenderTarget(
    QNullSwapChainRenderTarget *self,
    const char *key,
    void *call) {
  return static_cast<CuteQNullSwapChainRenderTarget *>(self)->take(key, call);
}

//  void QNullSwapChainRenderTarget::destroy()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN26QNullSwapChainRenderTarget7destroyEv(
    QNullSwapChainRenderTarget *self) {
  self->QNullSwapChainRenderTarget::destroy();
}

//  QSize QNullSwapChainRenderTarget::pixelSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK26QNullSwapChainRenderTarget9pixelSizeEv(
    const QNullSwapChainRenderTarget *self) {
  return new QSize(self->QNullSwapChainRenderTarget::pixelSize());
}

//  float QNullSwapChainRenderTarget::devicePixelRatio() const
extern "C" Q_DECL_EXPORT
float ritual_own_ZNK26QNullSwapChainRenderTarget16devicePixelRatioEv(
    const QNullSwapChainRenderTarget *self) {
  return self->QNullSwapChainRenderTarget::devicePixelRatio();
}

//  int QNullSwapChainRenderTarget::sampleCount() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK26QNullSwapChainRenderTarget11sampleCountEv(
    const QNullSwapChainRenderTarget *self) {
  return self->QNullSwapChainRenderTarget::sampleCount();
}
