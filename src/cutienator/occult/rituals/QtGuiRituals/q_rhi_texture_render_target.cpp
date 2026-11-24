//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/rhi/qrhi.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/rhi/qrhi.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qsize.h>
#include <cstring>

//  A QRhiTextureRenderTarget that Python can take functions over in. Every QRhiTextureRenderTarget
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQRhiTextureRenderTargetCall0)(const void *, int *);
typedef void * (*CuteQRhiTextureRenderTargetCall1)(const void *, int *);
typedef bool (*CuteQRhiTextureRenderTargetCall2)(const void *, int *);
typedef const QSize * (*CuteQRhiTextureRenderTargetCall3)(const void *, int *);
typedef float (*CuteQRhiTextureRenderTargetCall4)(const void *, int *);
typedef int (*CuteQRhiTextureRenderTargetCall5)(const void *, int *);
typedef void (*CuteQRhiTextureRenderTargetCall6)(const void *, int *);
class CuteQRhiTextureRenderTarget : public QRhiTextureRenderTarget {
public:
  using QRhiTextureRenderTarget::QRhiTextureRenderTarget;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK12QRhiResource12resourceTypeEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN23QRhiTextureRenderTarget33newCompatibleRenderPassDescriptorEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN23QRhiTextureRenderTarget6createEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QRhiRenderTarget9pixelSizeEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QRhiRenderTarget16devicePixelRatioEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QRhiRenderTarget11sampleCountEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QRhiResource7destroyEv")) {
      taken[6] = call;
      return true;
    }
    return false;
  }

  //  QRhiResource::Type QRhiTextureRenderTarget::resourceType() const
  QRhiResource::Type resourceType() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQRhiTextureRenderTargetCall0 call = reinterpret_cast<CuteQRhiTextureRenderTargetCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<QRhiResource::Type>(given);
    }
    return QRhiTextureRenderTarget::resourceType();
  }

  //  QRhiRenderPassDescriptor
  //      *QRhiTextureRenderTarget::newCompatibleRenderPassDescriptor()
  QRhiRenderPassDescriptor *newCompatibleRenderPassDescriptor() override {
    if (taken[1]) {
      int handled = 0;
      CuteQRhiTextureRenderTargetCall1 call = reinterpret_cast<CuteQRhiTextureRenderTargetCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QRhiRenderPassDescriptor *>(given);
    }
    return {};
  }

  //  bool QRhiTextureRenderTarget::create()
  bool create() override {
    if (taken[2]) {
      int handled = 0;
      CuteQRhiTextureRenderTargetCall2 call = reinterpret_cast<CuteQRhiTextureRenderTargetCall2>(taken[2]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  QSize QRhiRenderTarget::pixelSize() const
  QSize pixelSize() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQRhiTextureRenderTargetCall3 call = reinterpret_cast<CuteQRhiTextureRenderTargetCall3>(taken[3]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  float QRhiRenderTarget::devicePixelRatio() const
  float devicePixelRatio() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQRhiTextureRenderTargetCall4 call = reinterpret_cast<CuteQRhiTextureRenderTargetCall4>(taken[4]);
      float given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  int QRhiRenderTarget::sampleCount() const
  int sampleCount() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQRhiTextureRenderTargetCall5 call = reinterpret_cast<CuteQRhiTextureRenderTargetCall5>(taken[5]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QRhiResource::destroy()
  void destroy() override {
    if (taken[6]) {
      int handled = 0;
      CuteQRhiTextureRenderTargetCall6 call = reinterpret_cast<CuteQRhiTextureRenderTargetCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
  }
};

//  QRhiResource::Type QRhiTextureRenderTarget::resourceType() const
extern "C" Q_DECL_EXPORT
QRhiResource::Type ritual_ZNK23QRhiTextureRenderTarget12resourceTypeEv(
    const QRhiTextureRenderTarget *self) {
  return self->resourceType();
}

//  QRhiTextureRenderTargetDescription QRhiTextureRenderTarget::description()
//      const
extern "C" Q_DECL_EXPORT
QRhiTextureRenderTargetDescription *ritual_ZNK23QRhiTextureRenderTarget11descriptionEv(
    const QRhiTextureRenderTarget *self) {
  return new QRhiTextureRenderTargetDescription(self->description());
}

//  void QRhiTextureRenderTarget::setDescription(const
//      QRhiTextureRenderTargetDescription &desc)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QRhiTextureRenderTarget14setDescriptionERK34QRhiTextureRenderTargetDescription(
    QRhiTextureRenderTarget *self,
    const QRhiTextureRenderTargetDescription *desc) {
  self->setDescription(*desc);
}

//  Flags QRhiTextureRenderTarget::flags() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK23QRhiTextureRenderTarget5flagsEv(
    const QRhiTextureRenderTarget *self) {
  return static_cast<int>(self->flags().toInt());
}

//  void QRhiTextureRenderTarget::setFlags(Flags f)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QRhiTextureRenderTarget8setFlagsE6QFlagsINS_4FlagEE(
    QRhiTextureRenderTarget *self,
    int f) {
  self->setFlags(QFlags<QRhiTextureRenderTarget::Flag>::fromInt(f));
}

//  QRhiRenderPassDescriptor
//      *QRhiTextureRenderTarget::newCompatibleRenderPassDescriptor()
extern "C" Q_DECL_EXPORT
QRhiRenderPassDescriptor *ritual_ZN23QRhiTextureRenderTarget33newCompatibleRenderPassDescriptorEv(
    QRhiTextureRenderTarget *self) {
  return self->newCompatibleRenderPassDescriptor();
}

//  bool QRhiTextureRenderTarget::create()
extern "C" Q_DECL_EXPORT
bool ritual_ZN23QRhiTextureRenderTarget6createEv(
    QRhiTextureRenderTarget *self) {
  return self->create();
}

//  a Python function taken by a CuteQRhiTextureRenderTarget, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QRhiTextureRenderTarget(
    QRhiTextureRenderTarget *self,
    const char *key,
    void *call) {
  return static_cast<CuteQRhiTextureRenderTarget *>(self)->take(key, call);
}

//  QRhiResource::Type QRhiTextureRenderTarget::resourceType() const
extern "C" Q_DECL_EXPORT
QRhiResource::Type ritual_own_ZNK23QRhiTextureRenderTarget12resourceTypeEv(
    const QRhiTextureRenderTarget *self) {
  return self->QRhiTextureRenderTarget::resourceType();
}
