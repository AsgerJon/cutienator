//  Written by dev_tooling.RitualGenerator from the records of QtWaylandCompo
//  sitor/6.12.0/QtWaylandCompositor/private/qwlserverbufferintegration_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtWaylandCompositor/qtwaylandcompositorglobal.h>
#include <QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qtwaylandcompositorglobal_p.h>
#if QT_CONFIG(opengl)
#include <QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qtwaylandcompositorglobal_p.h>
#include <QtWaylandCompositor/QtWaylandCompositor>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qwlserverbufferintegration_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qsize.h>
#include <cstring>

//  A QtWayland::ServerBuffer that Python can take functions over in. Every QtWayland::ServerBuffer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQtWayland_ServerBufferCall0)(const void *, struct ::wl_client *, int *);
typedef bool (*CuteQtWayland_ServerBufferCall1)(const void *, int *);
typedef void * (*CuteQtWayland_ServerBufferCall2)(const void *, int *);
typedef void (*CuteQtWayland_ServerBufferCall3)(const void *, int *);
typedef bool (*CuteQtWayland_ServerBufferCall4)(const void *, int *);
class CuteQtWayland_ServerBuffer : public QtWayland::ServerBuffer {
public:
  using QtWayland::ServerBuffer::ServerBuffer;
  void *taken[5] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN9QtWayland12ServerBuffer17resourceForClientEP9wl_client")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QtWayland12ServerBuffer11bufferInUseEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QtWayland12ServerBuffer15toOpenGlTextureEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QtWayland12ServerBuffer20releaseOpenGlTextureEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QtWayland12ServerBuffer11isYInvertedEv")) {
      taken[4] = call;
      return true;
    }
    return false;
  }

  //  struct ::wl_resource
  //      *QtWayland::ServerBuffer::resourceForClient(struct ::wl_client
  //      *a0)
  struct ::wl_resource *resourceForClient(struct ::wl_client *a0) override {
    if (taken[0]) {
      int handled = 0;
      CuteQtWayland_ServerBufferCall0 call = reinterpret_cast<CuteQtWayland_ServerBufferCall0>(taken[0]);
      void * given = call(this, a0, &handled);
      if (handled) return static_cast<struct ::wl_resource *>(given);
    }
    return {};
  }

  //  bool QtWayland::ServerBuffer::bufferInUse()
  bool bufferInUse() override {
    if (taken[1]) {
      int handled = 0;
      CuteQtWayland_ServerBufferCall1 call = reinterpret_cast<CuteQtWayland_ServerBufferCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QtWayland::ServerBuffer::bufferInUse();
  }

  //  QOpenGLTexture *QtWayland::ServerBuffer::toOpenGlTexture()
  QOpenGLTexture *toOpenGlTexture() override {
    if (taken[2]) {
      int handled = 0;
      CuteQtWayland_ServerBufferCall2 call = reinterpret_cast<CuteQtWayland_ServerBufferCall2>(taken[2]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QOpenGLTexture *>(given);
    }
    return {};
  }

  //  void QtWayland::ServerBuffer::releaseOpenGlTexture()
  void releaseOpenGlTexture() override {
    if (taken[3]) {
      int handled = 0;
      CuteQtWayland_ServerBufferCall3 call = reinterpret_cast<CuteQtWayland_ServerBufferCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QtWayland::ServerBuffer::releaseOpenGlTexture();
  }

  //  bool QtWayland::ServerBuffer::isYInverted() const
  bool isYInverted() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQtWayland_ServerBufferCall4 call = reinterpret_cast<CuteQtWayland_ServerBufferCall4>(taken[4]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QtWayland::ServerBuffer::isYInverted();
  }
};

//  QtWayland::ServerBuffer::ServerBuffer(const QSize &size,
//      ServerBuffer::Format format)
extern "C" Q_DECL_EXPORT
QtWayland::ServerBuffer *ritual_ZN9QtWayland12ServerBufferC1ERK5QSizeNS0_6FormatE(
    const QSize *size,
    QtWayland::ServerBuffer::Format format) {
  return new CuteQtWayland_ServerBuffer(*size, format);
}

//  QtWayland::ServerBuffer::~ServerBuffer()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtWayland12ServerBufferD1Ev(QtWayland::ServerBuffer *self) {
  delete self;
}

//  struct ::wl_resource *QtWayland::ServerBuffer::resourceForClient(struct
//      ::wl_client *a0)
extern "C" Q_DECL_EXPORT
struct ::wl_resource *ritual_ZN9QtWayland12ServerBuffer17resourceForClientEP9wl_client(
    QtWayland::ServerBuffer *self,
    struct ::wl_client *a0) {
  return self->resourceForClient(a0);
}

//  bool QtWayland::ServerBuffer::bufferInUse()
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QtWayland12ServerBuffer11bufferInUseEv(
    QtWayland::ServerBuffer *self) {
  return self->bufferInUse();
}

//  QOpenGLTexture *QtWayland::ServerBuffer::toOpenGlTexture()
extern "C" Q_DECL_EXPORT
QOpenGLTexture *ritual_ZN9QtWayland12ServerBuffer15toOpenGlTextureEv(
    QtWayland::ServerBuffer *self) {
  return self->toOpenGlTexture();
}

//  void QtWayland::ServerBuffer::releaseOpenGlTexture()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtWayland12ServerBuffer20releaseOpenGlTextureEv(
    QtWayland::ServerBuffer *self) {
  self->releaseOpenGlTexture();
}

//  bool QtWayland::ServerBuffer::isYInverted() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QtWayland12ServerBuffer11isYInvertedEv(
    const QtWayland::ServerBuffer *self) {
  return self->isYInverted();
}

//  QSize QtWayland::ServerBuffer::size() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK9QtWayland12ServerBuffer4sizeEv(
    const QtWayland::ServerBuffer *self) {
  return new QSize(self->size());
}

//  Format QtWayland::ServerBuffer::format() const
extern "C" Q_DECL_EXPORT
QtWayland::ServerBuffer::Format ritual_ZNK9QtWayland12ServerBuffer6formatEv(
    const QtWayland::ServerBuffer *self) {
  return self->format();
}

//  a Python function taken by a CuteQtWayland_ServerBuffer, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QtWayland_ServerBuffer(
    QtWayland::ServerBuffer *self,
    const char *key,
    void *call) {
  return static_cast<CuteQtWayland_ServerBuffer *>(self)->take(key, call);
}

//  bool QtWayland::ServerBuffer::bufferInUse()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN9QtWayland12ServerBuffer11bufferInUseEv(
    QtWayland::ServerBuffer *self) {
  return self->QtWayland::ServerBuffer::bufferInUse();
}

//  void QtWayland::ServerBuffer::releaseOpenGlTexture()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QtWayland12ServerBuffer20releaseOpenGlTextureEv(
    QtWayland::ServerBuffer *self) {
  self->QtWayland::ServerBuffer::releaseOpenGlTexture();
}

//  bool QtWayland::ServerBuffer::isYInverted() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK9QtWayland12ServerBuffer11isYInvertedEv(
    const QtWayland::ServerBuffer *self) {
  return self->QtWayland::ServerBuffer::isYInverted();
}

#endif  // QT_CONFIG(opengl)
