//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/rhi/qrhi.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/rhi/qrhi.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qsize.h>
#include <cstring>

//  A QRhiSwapChainRenderTarget that Python can take functions over in. Every QRhiSwapChainRenderTarget
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQRhiSwapChainRenderTargetCall0)(const void *, int *);
typedef const QSize * (*CuteQRhiSwapChainRenderTargetCall1)(const void *, int *);
typedef float (*CuteQRhiSwapChainRenderTargetCall2)(const void *, int *);
typedef int (*CuteQRhiSwapChainRenderTargetCall3)(const void *, int *);
typedef void (*CuteQRhiSwapChainRenderTargetCall4)(const void *, int *);
class CuteQRhiSwapChainRenderTarget : public QRhiSwapChainRenderTarget {
public:
  using QRhiSwapChainRenderTarget::QRhiSwapChainRenderTarget;
  void *taken[5] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK12QRhiResource12resourceTypeEv")) {
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
    if (!std::strcmp(key, "_ZN12QRhiResource7destroyEv")) {
      taken[4] = call;
      return true;
    }
    return false;
  }

  //  QRhiResource::Type QRhiSwapChainRenderTarget::resourceType() const
  QRhiResource::Type resourceType() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQRhiSwapChainRenderTargetCall0 call = reinterpret_cast<CuteQRhiSwapChainRenderTargetCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<QRhiResource::Type>(given);
    }
    return QRhiSwapChainRenderTarget::resourceType();
  }

  //  QSize QRhiRenderTarget::pixelSize() const
  QSize pixelSize() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQRhiSwapChainRenderTargetCall1 call = reinterpret_cast<CuteQRhiSwapChainRenderTargetCall1>(taken[1]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  float QRhiRenderTarget::devicePixelRatio() const
  float devicePixelRatio() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQRhiSwapChainRenderTargetCall2 call = reinterpret_cast<CuteQRhiSwapChainRenderTargetCall2>(taken[2]);
      float given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  int QRhiRenderTarget::sampleCount() const
  int sampleCount() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQRhiSwapChainRenderTargetCall3 call = reinterpret_cast<CuteQRhiSwapChainRenderTargetCall3>(taken[3]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QRhiResource::destroy()
  void destroy() override {
    if (taken[4]) {
      int handled = 0;
      CuteQRhiSwapChainRenderTargetCall4 call = reinterpret_cast<CuteQRhiSwapChainRenderTargetCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
  }
};

//  QRhiResource::Type QRhiSwapChainRenderTarget::resourceType() const
extern "C" Q_DECL_EXPORT
QRhiResource::Type ritual_ZNK25QRhiSwapChainRenderTarget12resourceTypeEv(
    const QRhiSwapChainRenderTarget *self) {
  return self->resourceType();
}

//  QRhiSwapChain *QRhiSwapChainRenderTarget::swapChain() const
extern "C" Q_DECL_EXPORT
QRhiSwapChain *ritual_ZNK25QRhiSwapChainRenderTarget9swapChainEv(
    const QRhiSwapChainRenderTarget *self) {
  return self->swapChain();
}

//  a Python function taken by a CuteQRhiSwapChainRenderTarget, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QRhiSwapChainRenderTarget(
    QRhiSwapChainRenderTarget *self,
    const char *key,
    void *call) {
  return static_cast<CuteQRhiSwapChainRenderTarget *>(self)->take(key, call);
}

//  QRhiResource::Type QRhiSwapChainRenderTarget::resourceType() const
extern "C" Q_DECL_EXPORT
QRhiResource::Type ritual_own_ZNK25QRhiSwapChainRenderTarget12resourceTypeEv(
    const QRhiSwapChainRenderTarget *self) {
  return self->QRhiSwapChainRenderTarget::resourceType();
}
