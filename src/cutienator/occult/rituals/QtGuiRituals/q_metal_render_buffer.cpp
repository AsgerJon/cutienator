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
#include <QtGui/6.12.0/QtGui/rhi/qrhi.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QMetalRenderBuffer that Python can take functions over in. Every QMetalRenderBuffer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQMetalRenderBufferCall0)(const void *, int *);
typedef bool (*CuteQMetalRenderBufferCall1)(const void *, int *);
typedef int (*CuteQMetalRenderBufferCall2)(const void *, int *);
typedef int (*CuteQMetalRenderBufferCall3)(const void *, int *);
typedef bool (*CuteQMetalRenderBufferCall4)(const void *, const QRhiRenderBuffer::NativeRenderBuffer *, int *);
class CuteQMetalRenderBuffer : public QMetalRenderBuffer {
public:
  using QMetalRenderBuffer::QMetalRenderBuffer;
  void *taken[5] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN12QRhiResource7destroyEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QRhiRenderBuffer6createEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QRhiRenderBuffer13backingFormatEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QRhiResource12resourceTypeEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QRhiRenderBuffer10createFromENS_18NativeRenderBufferE")) {
      taken[4] = call;
      return true;
    }
    return false;
  }

  //  void QMetalRenderBuffer::destroy()
  void destroy() override {
    if (taken[0]) {
      int handled = 0;
      CuteQMetalRenderBufferCall0 call = reinterpret_cast<CuteQMetalRenderBufferCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QMetalRenderBuffer::destroy();
  }

  //  bool QMetalRenderBuffer::create()
  bool create() override {
    if (taken[1]) {
      int handled = 0;
      CuteQMetalRenderBufferCall1 call = reinterpret_cast<CuteQMetalRenderBufferCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QMetalRenderBuffer::create();
  }

  //  QRhiTexture::Format QMetalRenderBuffer::backingFormat() const
  QRhiTexture::Format backingFormat() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQMetalRenderBufferCall2 call = reinterpret_cast<CuteQMetalRenderBufferCall2>(taken[2]);
      int given = call(this, &handled);
      if (handled) return static_cast<QRhiTexture::Format>(given);
    }
    return QMetalRenderBuffer::backingFormat();
  }

  //  QRhiResource::Type QRhiRenderBuffer::resourceType() const
  QRhiResource::Type resourceType() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQMetalRenderBufferCall3 call = reinterpret_cast<CuteQMetalRenderBufferCall3>(taken[3]);
      int given = call(this, &handled);
      if (handled) return static_cast<QRhiResource::Type>(given);
    }
    return QRhiRenderBuffer::resourceType();
  }

  //  bool QRhiRenderBuffer::createFrom(NativeRenderBuffer src)
  bool createFrom(QRhiRenderBuffer::NativeRenderBuffer src) override {
    if (taken[4]) {
      int handled = 0;
      CuteQMetalRenderBufferCall4 call = reinterpret_cast<CuteQMetalRenderBufferCall4>(taken[4]);
      bool given = call(this, &src, &handled);
      if (handled) return given;
    }
    return QRhiRenderBuffer::createFrom(src);
  }
};

//  void QMetalRenderBuffer::destroy()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QMetalRenderBuffer7destroyEv(QMetalRenderBuffer *self) {
  self->destroy();
}

//  bool QMetalRenderBuffer::create()
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QMetalRenderBuffer6createEv(QMetalRenderBuffer *self) {
  return self->create();
}

//  QRhiTexture::Format QMetalRenderBuffer::backingFormat() const
extern "C" Q_DECL_EXPORT
QRhiTexture::Format ritual_ZNK18QMetalRenderBuffer13backingFormatEv(
    const QMetalRenderBuffer *self) {
  return self->backingFormat();
}

//  a Python function taken by a CuteQMetalRenderBuffer, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QMetalRenderBuffer(
    QMetalRenderBuffer *self,
    const char *key,
    void *call) {
  return static_cast<CuteQMetalRenderBuffer *>(self)->take(key, call);
}

#endif  // QT_CONFIG(metal)
