//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qrhimetal_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if QT_CONFIG(metal)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qrhimetal_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qsize.h>
#include <cstring>

//  A QMetalSwapChainRenderTarget that Python can take functions over in. Every QMetalSwapChainRenderTarget
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQMetalSwapChainRenderTargetCall0)(const void *, int *);
typedef const QSize * (*CuteQMetalSwapChainRenderTargetCall1)(const void *, int *);
typedef float (*CuteQMetalSwapChainRenderTargetCall2)(const void *, int *);
typedef int (*CuteQMetalSwapChainRenderTargetCall3)(const void *, int *);
typedef int (*CuteQMetalSwapChainRenderTargetCall4)(const void *, int *);
class CuteQMetalSwapChainRenderTarget : public QMetalSwapChainRenderTarget {
public:
  using QMetalSwapChainRenderTarget::QMetalSwapChainRenderTarget;
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

  //  void QMetalSwapChainRenderTarget::destroy()
  void destroy() override {
    if (taken[0]) {
      int handled = 0;
      CuteQMetalSwapChainRenderTargetCall0 call = reinterpret_cast<CuteQMetalSwapChainRenderTargetCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QMetalSwapChainRenderTarget::destroy();
  }

  //  QSize QMetalSwapChainRenderTarget::pixelSize() const
  QSize pixelSize() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQMetalSwapChainRenderTargetCall1 call = reinterpret_cast<CuteQMetalSwapChainRenderTargetCall1>(taken[1]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QMetalSwapChainRenderTarget::pixelSize();
  }

  //  float QMetalSwapChainRenderTarget::devicePixelRatio() const
  float devicePixelRatio() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQMetalSwapChainRenderTargetCall2 call = reinterpret_cast<CuteQMetalSwapChainRenderTargetCall2>(taken[2]);
      float given = call(this, &handled);
      if (handled) return given;
    }
    return QMetalSwapChainRenderTarget::devicePixelRatio();
  }

  //  int QMetalSwapChainRenderTarget::sampleCount() const
  int sampleCount() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQMetalSwapChainRenderTargetCall3 call = reinterpret_cast<CuteQMetalSwapChainRenderTargetCall3>(taken[3]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QMetalSwapChainRenderTarget::sampleCount();
  }

  //  QRhiResource::Type QRhiSwapChainRenderTarget::resourceType() const
  QRhiResource::Type resourceType() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQMetalSwapChainRenderTargetCall4 call = reinterpret_cast<CuteQMetalSwapChainRenderTargetCall4>(taken[4]);
      int given = call(this, &handled);
      if (handled) return static_cast<QRhiResource::Type>(given);
    }
    return QRhiSwapChainRenderTarget::resourceType();
  }
};

//  void QMetalSwapChainRenderTarget::destroy()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QMetalSwapChainRenderTarget7destroyEv(
    QMetalSwapChainRenderTarget *self) {
  self->destroy();
}

//  QSize QMetalSwapChainRenderTarget::pixelSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK27QMetalSwapChainRenderTarget9pixelSizeEv(
    const QMetalSwapChainRenderTarget *self) {
  return new QSize(self->pixelSize());
}

//  float QMetalSwapChainRenderTarget::devicePixelRatio() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK27QMetalSwapChainRenderTarget16devicePixelRatioEv(
    const QMetalSwapChainRenderTarget *self) {
  return self->devicePixelRatio();
}

//  int QMetalSwapChainRenderTarget::sampleCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK27QMetalSwapChainRenderTarget11sampleCountEv(
    const QMetalSwapChainRenderTarget *self) {
  return self->sampleCount();
}

//  a Python function taken by a CuteQMetalSwapChainRenderTarget, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QMetalSwapChainRenderTarget(
    QMetalSwapChainRenderTarget *self,
    const char *key,
    void *call) {
  return static_cast<CuteQMetalSwapChainRenderTarget *>(self)->take(key, call);
}

#endif  // QT_CONFIG(metal)
