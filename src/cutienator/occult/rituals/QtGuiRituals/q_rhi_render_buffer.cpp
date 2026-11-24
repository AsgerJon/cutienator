//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/rhi/qrhi.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/rhi/qrhi.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qsize.h>
#include <cstring>

//  A QRhiRenderBuffer that Python can take functions over in. Every QRhiRenderBuffer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQRhiRenderBufferCall0)(const void *, int *);
typedef bool (*CuteQRhiRenderBufferCall1)(const void *, int *);
typedef bool (*CuteQRhiRenderBufferCall2)(const void *, const QRhiRenderBuffer::NativeRenderBuffer *, int *);
typedef int (*CuteQRhiRenderBufferCall3)(const void *, int *);
typedef void (*CuteQRhiRenderBufferCall4)(const void *, int *);
class CuteQRhiRenderBuffer : public QRhiRenderBuffer {
public:
  using QRhiRenderBuffer::QRhiRenderBuffer;
  void *taken[5] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK12QRhiResource12resourceTypeEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QRhiRenderBuffer6createEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QRhiRenderBuffer10createFromENS_18NativeRenderBufferE")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QRhiRenderBuffer13backingFormatEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QRhiResource7destroyEv")) {
      taken[4] = call;
      return true;
    }
    return false;
  }

  //  QRhiResource::Type QRhiRenderBuffer::resourceType() const
  QRhiResource::Type resourceType() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQRhiRenderBufferCall0 call = reinterpret_cast<CuteQRhiRenderBufferCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<QRhiResource::Type>(given);
    }
    return QRhiRenderBuffer::resourceType();
  }

  //  bool QRhiRenderBuffer::create()
  bool create() override {
    if (taken[1]) {
      int handled = 0;
      CuteQRhiRenderBufferCall1 call = reinterpret_cast<CuteQRhiRenderBufferCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QRhiRenderBuffer::createFrom(NativeRenderBuffer src)
  bool createFrom(QRhiRenderBuffer::NativeRenderBuffer src) override {
    if (taken[2]) {
      int handled = 0;
      CuteQRhiRenderBufferCall2 call = reinterpret_cast<CuteQRhiRenderBufferCall2>(taken[2]);
      bool given = call(this, &src, &handled);
      if (handled) return given;
    }
    return QRhiRenderBuffer::createFrom(src);
  }

  //  QRhiTexture::Format QRhiRenderBuffer::backingFormat() const
  QRhiTexture::Format backingFormat() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQRhiRenderBufferCall3 call = reinterpret_cast<CuteQRhiRenderBufferCall3>(taken[3]);
      int given = call(this, &handled);
      if (handled) return static_cast<QRhiTexture::Format>(given);
    }
    return {};
  }

  //  void QRhiResource::destroy()
  void destroy() override {
    if (taken[4]) {
      int handled = 0;
      CuteQRhiRenderBufferCall4 call = reinterpret_cast<CuteQRhiRenderBufferCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
  }
};

//  QRhiResource::Type QRhiRenderBuffer::resourceType() const
extern "C" Q_DECL_EXPORT
QRhiResource::Type ritual_ZNK16QRhiRenderBuffer12resourceTypeEv(
    const QRhiRenderBuffer *self) {
  return self->resourceType();
}

//  Type QRhiRenderBuffer::type() const
extern "C" Q_DECL_EXPORT
QRhiRenderBuffer::Type ritual_ZNK16QRhiRenderBuffer4typeEv(
    const QRhiRenderBuffer *self) {
  return self->type();
}

//  void QRhiRenderBuffer::setType(Type t)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QRhiRenderBuffer7setTypeENS_4TypeE(
    QRhiRenderBuffer *self,
    QRhiRenderBuffer::Type t) {
  self->setType(t);
}

//  QSize QRhiRenderBuffer::pixelSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK16QRhiRenderBuffer9pixelSizeEv(
    const QRhiRenderBuffer *self) {
  return new QSize(self->pixelSize());
}

//  void QRhiRenderBuffer::setPixelSize(const QSize &sz)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QRhiRenderBuffer12setPixelSizeERK5QSize(
    QRhiRenderBuffer *self,
    const QSize *sz) {
  self->setPixelSize(*sz);
}

//  int QRhiRenderBuffer::sampleCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QRhiRenderBuffer11sampleCountEv(
    const QRhiRenderBuffer *self) {
  return self->sampleCount();
}

//  void QRhiRenderBuffer::setSampleCount(int s)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QRhiRenderBuffer14setSampleCountEi(
    QRhiRenderBuffer *self,
    int s) {
  self->setSampleCount(s);
}

//  Flags QRhiRenderBuffer::flags() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QRhiRenderBuffer5flagsEv(const QRhiRenderBuffer *self) {
  return static_cast<int>(self->flags().toInt());
}

//  void QRhiRenderBuffer::setFlags(Flags f)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QRhiRenderBuffer8setFlagsE6QFlagsINS_4FlagEE(
    QRhiRenderBuffer *self,
    int f) {
  self->setFlags(QFlags<QRhiRenderBuffer::Flag>::fromInt(f));
}

//  bool QRhiRenderBuffer::create()
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QRhiRenderBuffer6createEv(QRhiRenderBuffer *self) {
  return self->create();
}

//  bool QRhiRenderBuffer::createFrom(NativeRenderBuffer src)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QRhiRenderBuffer10createFromENS_18NativeRenderBufferE(
    QRhiRenderBuffer *self,
    const QRhiRenderBuffer::NativeRenderBuffer *src) {
  return self->createFrom(*src);
}

//  QRhiTexture::Format QRhiRenderBuffer::backingFormat() const
extern "C" Q_DECL_EXPORT
QRhiTexture::Format ritual_ZNK16QRhiRenderBuffer13backingFormatEv(
    const QRhiRenderBuffer *self) {
  return self->backingFormat();
}

//  a Python function taken by a CuteQRhiRenderBuffer, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QRhiRenderBuffer(
    QRhiRenderBuffer *self,
    const char *key,
    void *call) {
  return static_cast<CuteQRhiRenderBuffer *>(self)->take(key, call);
}

//  QRhiResource::Type QRhiRenderBuffer::resourceType() const
extern "C" Q_DECL_EXPORT
QRhiResource::Type ritual_own_ZNK16QRhiRenderBuffer12resourceTypeEv(
    const QRhiRenderBuffer *self) {
  return self->QRhiRenderBuffer::resourceType();
}

//  bool QRhiRenderBuffer::createFrom(NativeRenderBuffer src)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN16QRhiRenderBuffer10createFromENS_18NativeRenderBufferE(
    QRhiRenderBuffer *self,
    const QRhiRenderBuffer::NativeRenderBuffer *src) {
  return self->QRhiRenderBuffer::createFrom(*src);
}
