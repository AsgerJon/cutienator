//  Written by dev_tooling.RitualGenerator from the records of QtWaylandCompo
//  sitor/6.12.0/QtWaylandCompositor/private/qwlclientbuffer_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-25: 'isSharedMemory' is left out: Qt's
//  header writes it as a call of 'wl_shm_buffer_get' of the Wayland
//  library, outside Qt. Kept as it is when the generator runs again.
#include <QtGui/qtguiglobal.h>
#include <QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qtwaylandcompositorglobal_p.h>
#include <QtWaylandCompositor/QtWaylandCompositor>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qwlclientbuffer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qsize.h>
#include <QtGui/qimage.h>
#include <cstring>

//  Only a class built on QtWayland::ClientBuffer may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQtWayland_ClientBuffer : QtWayland::ClientBuffer {
  using QtWayland::ClientBuffer::setDestroyed;
};

//  A QtWayland::ClientBuffer that Python can take functions over in. Every QtWayland::ClientBuffer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQtWayland_ClientBufferCall0)(const void *, int *);
typedef const QSize * (*CuteQtWayland_ClientBufferCall1)(const void *, int *);
typedef int (*CuteQtWayland_ClientBufferCall2)(const void *, int *);
typedef quintptr (*CuteQtWayland_ClientBufferCall3)(const void *, int *);
typedef void (*CuteQtWayland_ClientBufferCall4)(const void *, quintptr, int *);
typedef const QImage * (*CuteQtWayland_ClientBufferCall5)(const void *, int *);
typedef bool (*CuteQtWayland_ClientBufferCall6)(const void *, int *);
#if QT_CONFIG(opengl)
typedef void * (*CuteQtWayland_ClientBufferCall7)(const void *, int, int *);
#endif  // QT_CONFIG(opengl)
typedef void (*CuteQtWayland_ClientBufferCall8)(const void *, int *);
class CuteQtWayland_ClientBuffer : public QtWayland::ClientBuffer {
public:
  using QtWayland::ClientBuffer::ClientBuffer;
  void *taken[9] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK9QtWayland12ClientBuffer15bufferFormatEglEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QtWayland12ClientBuffer4sizeEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QtWayland12ClientBuffer6originEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QtWayland12ClientBuffer16lockNativeBufferEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QtWayland12ClientBuffer18unlockNativeBufferEy")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QtWayland12ClientBuffer5imageEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QtWayland12ClientBuffer11isProtectedEv")) {
      taken[6] = call;
      return true;
    }
#if QT_CONFIG(opengl)
    if (!std::strcmp(key, "_ZN9QtWayland12ClientBuffer15toOpenGlTextureEi")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(opengl)
    if (!std::strcmp(key, "_ZN9QtWayland12ClientBuffer12setDestroyedEv")) {
      taken[8] = call;
      return true;
    }
    return false;
  }

  //  QWaylandBufferRef::BufferFormatEgl
  //      QtWayland::ClientBuffer::bufferFormatEgl() const
  QWaylandBufferRef::BufferFormatEgl bufferFormatEgl() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQtWayland_ClientBufferCall0 call = reinterpret_cast<CuteQtWayland_ClientBufferCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<QWaylandBufferRef::BufferFormatEgl>(given);
    }
    return QtWayland::ClientBuffer::bufferFormatEgl();
  }

  //  QSize QtWayland::ClientBuffer::size() const
  QSize size() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQtWayland_ClientBufferCall1 call = reinterpret_cast<CuteQtWayland_ClientBufferCall1>(taken[1]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  QWaylandSurface::Origin QtWayland::ClientBuffer::origin() const
  QWaylandSurface::Origin origin() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQtWayland_ClientBufferCall2 call = reinterpret_cast<CuteQtWayland_ClientBufferCall2>(taken[2]);
      int given = call(this, &handled);
      if (handled) return static_cast<QWaylandSurface::Origin>(given);
    }
    return {};
  }

  //  quintptr QtWayland::ClientBuffer::lockNativeBuffer()
  quintptr lockNativeBuffer() override {
    if (taken[3]) {
      int handled = 0;
      CuteQtWayland_ClientBufferCall3 call = reinterpret_cast<CuteQtWayland_ClientBufferCall3>(taken[3]);
      quintptr given = call(this, &handled);
      if (handled) return given;
    }
    return QtWayland::ClientBuffer::lockNativeBuffer();
  }

  //  void QtWayland::ClientBuffer::unlockNativeBuffer(quintptr
  //      native_buffer) const
  void unlockNativeBuffer(quintptr native_buffer) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQtWayland_ClientBufferCall4 call = reinterpret_cast<CuteQtWayland_ClientBufferCall4>(taken[4]);
      call(this, native_buffer, &handled);
      if (handled) return;
    }
    QtWayland::ClientBuffer::unlockNativeBuffer(native_buffer);
  }

  //  QImage QtWayland::ClientBuffer::image() const
  QImage image() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQtWayland_ClientBufferCall5 call = reinterpret_cast<CuteQtWayland_ClientBufferCall5>(taken[5]);
      const QImage * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QtWayland::ClientBuffer::image();
  }

  //  bool QtWayland::ClientBuffer::isProtected()
  bool isProtected() override {
    if (taken[6]) {
      int handled = 0;
      CuteQtWayland_ClientBufferCall6 call = reinterpret_cast<CuteQtWayland_ClientBufferCall6>(taken[6]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QtWayland::ClientBuffer::isProtected();
  }

#if QT_CONFIG(opengl)
  //  QOpenGLTexture *QtWayland::ClientBuffer::toOpenGlTexture(int plane)
  QOpenGLTexture *toOpenGlTexture(int plane) override {
    if (taken[7]) {
      int handled = 0;
      CuteQtWayland_ClientBufferCall7 call = reinterpret_cast<CuteQtWayland_ClientBufferCall7>(taken[7]);
      void * given = call(this, plane, &handled);
      if (handled) return static_cast<QOpenGLTexture *>(given);
    }
    return {};
  }
#endif  // QT_CONFIG(opengl)

  //  void QtWayland::ClientBuffer::setDestroyed()
  void setDestroyed() override {
    if (taken[8]) {
      int handled = 0;
      CuteQtWayland_ClientBufferCall8 call = reinterpret_cast<CuteQtWayland_ClientBufferCall8>(taken[8]);
      call(this, &handled);
      if (handled) return;
    }
    QtWayland::ClientBuffer::setDestroyed();
  }
};

//  QtWayland::ClientBuffer::~ClientBuffer()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtWayland12ClientBufferD1Ev(QtWayland::ClientBuffer *self) {
  delete self;
}

//  QWaylandBufferRef::BufferFormatEgl
//      QtWayland::ClientBuffer::bufferFormatEgl() const
extern "C" Q_DECL_EXPORT
QWaylandBufferRef::BufferFormatEgl ritual_ZNK9QtWayland12ClientBuffer15bufferFormatEglEv(
    const QtWayland::ClientBuffer *self) {
  return self->bufferFormatEgl();
}

//  QSize QtWayland::ClientBuffer::size() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK9QtWayland12ClientBuffer4sizeEv(
    const QtWayland::ClientBuffer *self) {
  return new QSize(self->size());
}

//  QWaylandSurface::Origin QtWayland::ClientBuffer::origin() const
extern "C" Q_DECL_EXPORT
QWaylandSurface::Origin ritual_ZNK9QtWayland12ClientBuffer6originEv(
    const QtWayland::ClientBuffer *self) {
  return self->origin();
}

//  quintptr QtWayland::ClientBuffer::lockNativeBuffer()
extern "C" Q_DECL_EXPORT
quintptr ritual_ZN9QtWayland12ClientBuffer16lockNativeBufferEv(
    QtWayland::ClientBuffer *self) {
  return self->lockNativeBuffer();
}

//  void QtWayland::ClientBuffer::unlockNativeBuffer(quintptr native_buffer)
//      const
extern "C" Q_DECL_EXPORT
void ritual_ZNK9QtWayland12ClientBuffer18unlockNativeBufferEy(
    const QtWayland::ClientBuffer *self,
    quintptr native_buffer) {
  self->unlockNativeBuffer(native_buffer);
}

//  QImage QtWayland::ClientBuffer::image() const
extern "C" Q_DECL_EXPORT
QImage *ritual_ZNK9QtWayland12ClientBuffer5imageEv(
    const QtWayland::ClientBuffer *self) {
  return new QImage(self->image());
}

//  bool QtWayland::ClientBuffer::isCommitted() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QtWayland12ClientBuffer11isCommittedEv(
    const QtWayland::ClientBuffer *self) {
  return self->isCommitted();
}

//  bool QtWayland::ClientBuffer::isDestroyed()
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QtWayland12ClientBuffer11isDestroyedEv(
    QtWayland::ClientBuffer *self) {
  return self->isDestroyed();
}

//  bool QtWayland::ClientBuffer::isProtected()
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QtWayland12ClientBuffer11isProtectedEv(
    QtWayland::ClientBuffer *self) {
  return self->isProtected();
}

#if QT_CONFIG(opengl)
//  QOpenGLTexture *QtWayland::ClientBuffer::toOpenGlTexture(int plane)
extern "C" Q_DECL_EXPORT
QOpenGLTexture *ritual_ZN9QtWayland12ClientBuffer15toOpenGlTextureEi(
    QtWayland::ClientBuffer *self,
    int plane) {
  return self->toOpenGlTexture(plane);
}
#endif  // QT_CONFIG(opengl)

//  bool QtWayland::ClientBuffer::hasContent(ClientBuffer *buffer)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QtWayland12ClientBuffer10hasContentEPS0_(
    QtWayland::ClientBuffer *buffer) {
  return QtWayland::ClientBuffer::hasContent(buffer);
}

//  bool QtWayland::ClientBuffer::hasProtectedContent(ClientBuffer *buffer)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QtWayland12ClientBuffer19hasProtectedContentEPS0_(
    QtWayland::ClientBuffer *buffer) {
  return QtWayland::ClientBuffer::hasProtectedContent(buffer);
}

//  void QtWayland::ClientBuffer::setDestroyed()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtWayland12ClientBuffer12setDestroyedEv(
    QtWayland::ClientBuffer *self) {
  self->setDestroyed();
}

//  a Python function taken by a CuteQtWayland_ClientBuffer, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QtWayland_ClientBuffer(
    QtWayland::ClientBuffer *self,
    const char *key,
    void *call) {
  return static_cast<CuteQtWayland_ClientBuffer *>(self)->take(key, call);
}

//  QWaylandBufferRef::BufferFormatEgl
//      QtWayland::ClientBuffer::bufferFormatEgl() const
extern "C" Q_DECL_EXPORT
QWaylandBufferRef::BufferFormatEgl ritual_own_ZNK9QtWayland12ClientBuffer15bufferFormatEglEv(
    const QtWayland::ClientBuffer *self) {
  return self->QtWayland::ClientBuffer::bufferFormatEgl();
}

//  quintptr QtWayland::ClientBuffer::lockNativeBuffer()
extern "C" Q_DECL_EXPORT
quintptr ritual_own_ZN9QtWayland12ClientBuffer16lockNativeBufferEv(
    QtWayland::ClientBuffer *self) {
  return self->QtWayland::ClientBuffer::lockNativeBuffer();
}

//  void QtWayland::ClientBuffer::unlockNativeBuffer(quintptr native_buffer)
//      const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK9QtWayland12ClientBuffer18unlockNativeBufferEy(
    const QtWayland::ClientBuffer *self,
    quintptr native_buffer) {
  self->QtWayland::ClientBuffer::unlockNativeBuffer(native_buffer);
}

//  QImage QtWayland::ClientBuffer::image() const
extern "C" Q_DECL_EXPORT
QImage *ritual_own_ZNK9QtWayland12ClientBuffer5imageEv(
    const QtWayland::ClientBuffer *self) {
  return new QImage(self->QtWayland::ClientBuffer::image());
}

//  bool QtWayland::ClientBuffer::isProtected()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN9QtWayland12ClientBuffer11isProtectedEv(
    QtWayland::ClientBuffer *self) {
  return self->QtWayland::ClientBuffer::isProtected();
}

//  void QtWayland::ClientBuffer::setDestroyed()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QtWayland12ClientBuffer12setDestroyedEv(
    QtWayland::ClientBuffer *self) {
  static_cast<OwnQtWayland_ClientBuffer *>(self)->OwnQtWayland_ClientBuffer::setDestroyed();
}
