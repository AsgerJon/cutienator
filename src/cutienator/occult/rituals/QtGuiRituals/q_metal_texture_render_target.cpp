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

//  A QMetalTextureRenderTarget that Python can take functions over in. Every QMetalTextureRenderTarget
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQMetalTextureRenderTargetCall0)(const void *, int *);
typedef const QSize * (*CuteQMetalTextureRenderTargetCall1)(const void *, int *);
typedef float (*CuteQMetalTextureRenderTargetCall2)(const void *, int *);
typedef int (*CuteQMetalTextureRenderTargetCall3)(const void *, int *);
typedef void * (*CuteQMetalTextureRenderTargetCall4)(const void *, int *);
typedef bool (*CuteQMetalTextureRenderTargetCall5)(const void *, int *);
typedef int (*CuteQMetalTextureRenderTargetCall6)(const void *, int *);
class CuteQMetalTextureRenderTarget : public QMetalTextureRenderTarget {
public:
  using QMetalTextureRenderTarget::QMetalTextureRenderTarget;
  void *taken[7] = {};

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
    if (!std::strcmp(key, "_ZN23QRhiTextureRenderTarget33newCompatibleRenderPassDescriptorEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN23QRhiTextureRenderTarget6createEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QRhiResource12resourceTypeEv")) {
      taken[6] = call;
      return true;
    }
    return false;
  }

  //  void QMetalTextureRenderTarget::destroy()
  void destroy() override {
    if (taken[0]) {
      int handled = 0;
      CuteQMetalTextureRenderTargetCall0 call = reinterpret_cast<CuteQMetalTextureRenderTargetCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QMetalTextureRenderTarget::destroy();
  }

  //  QSize QMetalTextureRenderTarget::pixelSize() const
  QSize pixelSize() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQMetalTextureRenderTargetCall1 call = reinterpret_cast<CuteQMetalTextureRenderTargetCall1>(taken[1]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QMetalTextureRenderTarget::pixelSize();
  }

  //  float QMetalTextureRenderTarget::devicePixelRatio() const
  float devicePixelRatio() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQMetalTextureRenderTargetCall2 call = reinterpret_cast<CuteQMetalTextureRenderTargetCall2>(taken[2]);
      float given = call(this, &handled);
      if (handled) return given;
    }
    return QMetalTextureRenderTarget::devicePixelRatio();
  }

  //  int QMetalTextureRenderTarget::sampleCount() const
  int sampleCount() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQMetalTextureRenderTargetCall3 call = reinterpret_cast<CuteQMetalTextureRenderTargetCall3>(taken[3]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QMetalTextureRenderTarget::sampleCount();
  }

  //  QRhiRenderPassDescriptor
  //      *QMetalTextureRenderTarget::newCompatibleRenderPassDescriptor()
  QRhiRenderPassDescriptor *newCompatibleRenderPassDescriptor() override {
    if (taken[4]) {
      int handled = 0;
      CuteQMetalTextureRenderTargetCall4 call = reinterpret_cast<CuteQMetalTextureRenderTargetCall4>(taken[4]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QRhiRenderPassDescriptor *>(given);
    }
    return QMetalTextureRenderTarget::newCompatibleRenderPassDescriptor();
  }

  //  bool QMetalTextureRenderTarget::create()
  bool create() override {
    if (taken[5]) {
      int handled = 0;
      CuteQMetalTextureRenderTargetCall5 call = reinterpret_cast<CuteQMetalTextureRenderTargetCall5>(taken[5]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QMetalTextureRenderTarget::create();
  }

  //  QRhiResource::Type QRhiTextureRenderTarget::resourceType() const
  QRhiResource::Type resourceType() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQMetalTextureRenderTargetCall6 call = reinterpret_cast<CuteQMetalTextureRenderTargetCall6>(taken[6]);
      int given = call(this, &handled);
      if (handled) return static_cast<QRhiResource::Type>(given);
    }
    return QRhiTextureRenderTarget::resourceType();
  }
};

//  void QMetalTextureRenderTarget::destroy()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QMetalTextureRenderTarget7destroyEv(
    QMetalTextureRenderTarget *self) {
  self->destroy();
}

//  QSize QMetalTextureRenderTarget::pixelSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK25QMetalTextureRenderTarget9pixelSizeEv(
    const QMetalTextureRenderTarget *self) {
  return new QSize(self->pixelSize());
}

//  float QMetalTextureRenderTarget::devicePixelRatio() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK25QMetalTextureRenderTarget16devicePixelRatioEv(
    const QMetalTextureRenderTarget *self) {
  return self->devicePixelRatio();
}

//  int QMetalTextureRenderTarget::sampleCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK25QMetalTextureRenderTarget11sampleCountEv(
    const QMetalTextureRenderTarget *self) {
  return self->sampleCount();
}

//  QRhiRenderPassDescriptor
//      *QMetalTextureRenderTarget::newCompatibleRenderPassDescriptor()
extern "C" Q_DECL_EXPORT
QRhiRenderPassDescriptor *ritual_ZN25QMetalTextureRenderTarget33newCompatibleRenderPassDescriptorEv(
    QMetalTextureRenderTarget *self) {
  return self->newCompatibleRenderPassDescriptor();
}

//  bool QMetalTextureRenderTarget::create()
extern "C" Q_DECL_EXPORT
bool ritual_ZN25QMetalTextureRenderTarget6createEv(
    QMetalTextureRenderTarget *self) {
  return self->create();
}

//  a Python function taken by a CuteQMetalTextureRenderTarget, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QMetalTextureRenderTarget(
    QMetalTextureRenderTarget *self,
    const char *key,
    void *call) {
  return static_cast<CuteQMetalTextureRenderTarget *>(self)->take(key, call);
}

#endif  // QT_CONFIG(metal)
