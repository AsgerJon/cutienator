//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/rhi/qrhi.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/rhi/qrhi.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qsize.h>
#include <cstring>

//  A QRhiRenderTarget that Python can take functions over in. Every QRhiRenderTarget
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QSize * (*CuteQRhiRenderTargetCall0)(const void *, int *);
typedef float (*CuteQRhiRenderTargetCall1)(const void *, int *);
typedef int (*CuteQRhiRenderTargetCall2)(const void *, int *);
typedef int (*CuteQRhiRenderTargetCall3)(const void *, int *);
typedef void (*CuteQRhiRenderTargetCall4)(const void *, int *);
class CuteQRhiRenderTarget : public QRhiRenderTarget {
public:
  using QRhiRenderTarget::QRhiRenderTarget;
  void *taken[5] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK16QRhiRenderTarget9pixelSizeEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QRhiRenderTarget16devicePixelRatioEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QRhiRenderTarget11sampleCountEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QRhiResource12resourceTypeEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QRhiResource7destroyEv")) {
      taken[4] = call;
      return true;
    }
    return false;
  }

  //  QSize QRhiRenderTarget::pixelSize() const
  QSize pixelSize() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQRhiRenderTargetCall0 call = reinterpret_cast<CuteQRhiRenderTargetCall0>(taken[0]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  float QRhiRenderTarget::devicePixelRatio() const
  float devicePixelRatio() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQRhiRenderTargetCall1 call = reinterpret_cast<CuteQRhiRenderTargetCall1>(taken[1]);
      float given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  int QRhiRenderTarget::sampleCount() const
  int sampleCount() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQRhiRenderTargetCall2 call = reinterpret_cast<CuteQRhiRenderTargetCall2>(taken[2]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  Type QRhiResource::resourceType() const
  QRhiResource::Type resourceType() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQRhiRenderTargetCall3 call = reinterpret_cast<CuteQRhiRenderTargetCall3>(taken[3]);
      int given = call(this, &handled);
      if (handled) return static_cast<QRhiResource::Type>(given);
    }
    return {};
  }

  //  void QRhiResource::destroy()
  void destroy() override {
    if (taken[4]) {
      int handled = 0;
      CuteQRhiRenderTargetCall4 call = reinterpret_cast<CuteQRhiRenderTargetCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
  }
};

//  QSize QRhiRenderTarget::pixelSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK16QRhiRenderTarget9pixelSizeEv(
    const QRhiRenderTarget *self) {
  return new QSize(self->pixelSize());
}

//  float QRhiRenderTarget::devicePixelRatio() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK16QRhiRenderTarget16devicePixelRatioEv(
    const QRhiRenderTarget *self) {
  return self->devicePixelRatio();
}

//  int QRhiRenderTarget::sampleCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QRhiRenderTarget11sampleCountEv(
    const QRhiRenderTarget *self) {
  return self->sampleCount();
}

//  QRhiRenderPassDescriptor *QRhiRenderTarget::renderPassDescriptor() const
extern "C" Q_DECL_EXPORT
QRhiRenderPassDescriptor *ritual_ZNK16QRhiRenderTarget20renderPassDescriptorEv(
    const QRhiRenderTarget *self) {
  return self->renderPassDescriptor();
}

//  void QRhiRenderTarget::setRenderPassDescriptor(QRhiRenderPassDescriptor
//      *desc)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QRhiRenderTarget23setRenderPassDescriptorEP24QRhiRenderPassDescriptor(
    QRhiRenderTarget *self,
    QRhiRenderPassDescriptor *desc) {
  self->setRenderPassDescriptor(desc);
}

//  a Python function taken by a CuteQRhiRenderTarget, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QRhiRenderTarget(
    QRhiRenderTarget *self,
    const char *key,
    void *call) {
  return static_cast<CuteQRhiRenderTarget *>(self)->take(key, call);
}
