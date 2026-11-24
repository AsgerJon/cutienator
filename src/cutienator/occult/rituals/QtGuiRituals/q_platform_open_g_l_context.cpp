//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/qpa/qplatformopenglcontext.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if !defined(QT_NO_OPENGL)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qplatformopenglcontext.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qsurfaceformat.h>
#include <QtCore/qbytearray.h>
#include <cstring>

//  A QPlatformOpenGLContext that Python can take functions over in. Every QPlatformOpenGLContext
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_OPENGL)
typedef void (*CuteQPlatformOpenGLContextCall0)(const void *, int *);
#endif  // !defined(QT_NO_OPENGL)
#if !defined(QT_NO_OPENGL)
typedef const QSurfaceFormat * (*CuteQPlatformOpenGLContextCall1)(const void *, int *);
#endif  // !defined(QT_NO_OPENGL)
#if !defined(QT_NO_OPENGL)
typedef void (*CuteQPlatformOpenGLContextCall2)(const void *, QPlatformSurface *, int *);
#endif  // !defined(QT_NO_OPENGL)
#if !defined(QT_NO_OPENGL)
typedef bool (*CuteQPlatformOpenGLContextCall3)(const void *, QPlatformSurface *, int *);
#endif  // !defined(QT_NO_OPENGL)
#if !defined(QT_NO_OPENGL)
typedef void (*CuteQPlatformOpenGLContextCall4)(const void *, int *);
#endif  // !defined(QT_NO_OPENGL)
#if !defined(QT_NO_OPENGL)
typedef void (*CuteQPlatformOpenGLContextCall5)(const void *, int *);
#endif  // !defined(QT_NO_OPENGL)
#if !defined(QT_NO_OPENGL)
typedef void (*CuteQPlatformOpenGLContextCall6)(const void *, int *);
#endif  // !defined(QT_NO_OPENGL)
#if !defined(QT_NO_OPENGL)
typedef bool (*CuteQPlatformOpenGLContextCall7)(const void *, int *);
#endif  // !defined(QT_NO_OPENGL)
#if !defined(QT_NO_OPENGL)
typedef bool (*CuteQPlatformOpenGLContextCall8)(const void *, int *);
#endif  // !defined(QT_NO_OPENGL)
class CuteQPlatformOpenGLContext : public QPlatformOpenGLContext {
public:
  using QPlatformOpenGLContext::QPlatformOpenGLContext;
  void *taken[9] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_OPENGL)
    if (!std::strcmp(key, "_ZN22QPlatformOpenGLContext10initializeEv")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_OPENGL)
#if !defined(QT_NO_OPENGL)
    if (!std::strcmp(key, "_ZNK22QPlatformOpenGLContext6formatEv")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_OPENGL)
#if !defined(QT_NO_OPENGL)
    if (!std::strcmp(key, "_ZN22QPlatformOpenGLContext11swapBuffersEP16QPlatformSurface")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_OPENGL)
#if !defined(QT_NO_OPENGL)
    if (!std::strcmp(key, "_ZN22QPlatformOpenGLContext11makeCurrentEP16QPlatformSurface")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_OPENGL)
#if !defined(QT_NO_OPENGL)
    if (!std::strcmp(key, "_ZN22QPlatformOpenGLContext11doneCurrentEv")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_OPENGL)
#if !defined(QT_NO_OPENGL)
    if (!std::strcmp(key, "_ZN22QPlatformOpenGLContext10beginFrameEv")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_OPENGL)
#if !defined(QT_NO_OPENGL)
    if (!std::strcmp(key, "_ZN22QPlatformOpenGLContext8endFrameEv")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_OPENGL)
#if !defined(QT_NO_OPENGL)
    if (!std::strcmp(key, "_ZNK22QPlatformOpenGLContext9isSharingEv")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_OPENGL)
#if !defined(QT_NO_OPENGL)
    if (!std::strcmp(key, "_ZNK22QPlatformOpenGLContext7isValidEv")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_OPENGL)
    return false;
  }

#if !defined(QT_NO_OPENGL)
  //  void QPlatformOpenGLContext::initialize()
  void initialize() override {
    if (taken[0]) {
      int handled = 0;
      CuteQPlatformOpenGLContextCall0 call = reinterpret_cast<CuteQPlatformOpenGLContextCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QPlatformOpenGLContext::initialize();
  }
#endif  // !defined(QT_NO_OPENGL)

#if !defined(QT_NO_OPENGL)
  //  QSurfaceFormat QPlatformOpenGLContext::format() const
  QSurfaceFormat format() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQPlatformOpenGLContextCall1 call = reinterpret_cast<CuteQPlatformOpenGLContextCall1>(taken[1]);
      const QSurfaceFormat * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }
#endif  // !defined(QT_NO_OPENGL)

#if !defined(QT_NO_OPENGL)
  //  void QPlatformOpenGLContext::swapBuffers(QPlatformSurface *surface)
  void swapBuffers(QPlatformSurface *surface) override {
    if (taken[2]) {
      int handled = 0;
      CuteQPlatformOpenGLContextCall2 call = reinterpret_cast<CuteQPlatformOpenGLContextCall2>(taken[2]);
      call(this, surface, &handled);
      if (handled) return;
    }
  }
#endif  // !defined(QT_NO_OPENGL)

#if !defined(QT_NO_OPENGL)
  //  bool QPlatformOpenGLContext::makeCurrent(QPlatformSurface *surface)
  bool makeCurrent(QPlatformSurface *surface) override {
    if (taken[3]) {
      int handled = 0;
      CuteQPlatformOpenGLContextCall3 call = reinterpret_cast<CuteQPlatformOpenGLContextCall3>(taken[3]);
      bool given = call(this, surface, &handled);
      if (handled) return given;
    }
    return {};
  }
#endif  // !defined(QT_NO_OPENGL)

#if !defined(QT_NO_OPENGL)
  //  void QPlatformOpenGLContext::doneCurrent()
  void doneCurrent() override {
    if (taken[4]) {
      int handled = 0;
      CuteQPlatformOpenGLContextCall4 call = reinterpret_cast<CuteQPlatformOpenGLContextCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
  }
#endif  // !defined(QT_NO_OPENGL)

#if !defined(QT_NO_OPENGL)
  //  void QPlatformOpenGLContext::beginFrame()
  void beginFrame() override {
    if (taken[5]) {
      int handled = 0;
      CuteQPlatformOpenGLContextCall5 call = reinterpret_cast<CuteQPlatformOpenGLContextCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    QPlatformOpenGLContext::beginFrame();
  }
#endif  // !defined(QT_NO_OPENGL)

#if !defined(QT_NO_OPENGL)
  //  void QPlatformOpenGLContext::endFrame()
  void endFrame() override {
    if (taken[6]) {
      int handled = 0;
      CuteQPlatformOpenGLContextCall6 call = reinterpret_cast<CuteQPlatformOpenGLContextCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QPlatformOpenGLContext::endFrame();
  }
#endif  // !defined(QT_NO_OPENGL)

#if !defined(QT_NO_OPENGL)
  //  bool QPlatformOpenGLContext::isSharing() const
  bool isSharing() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQPlatformOpenGLContextCall7 call = reinterpret_cast<CuteQPlatformOpenGLContextCall7>(taken[7]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QPlatformOpenGLContext::isSharing();
  }
#endif  // !defined(QT_NO_OPENGL)

#if !defined(QT_NO_OPENGL)
  //  bool QPlatformOpenGLContext::isValid() const
  bool isValid() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQPlatformOpenGLContextCall8 call = reinterpret_cast<CuteQPlatformOpenGLContextCall8>(taken[8]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QPlatformOpenGLContext::isValid();
  }
#endif  // !defined(QT_NO_OPENGL)
};

//  QPlatformOpenGLContext::~QPlatformOpenGLContext()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QPlatformOpenGLContextD1Ev(QPlatformOpenGLContext *self) {
  delete self;
}

//  void QPlatformOpenGLContext::initialize()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QPlatformOpenGLContext10initializeEv(
    QPlatformOpenGLContext *self) {
  self->initialize();
}

//  QSurfaceFormat QPlatformOpenGLContext::format() const
extern "C" Q_DECL_EXPORT
QSurfaceFormat *ritual_ZNK22QPlatformOpenGLContext6formatEv(
    const QPlatformOpenGLContext *self) {
  return new QSurfaceFormat(self->format());
}

//  void QPlatformOpenGLContext::swapBuffers(QPlatformSurface *surface)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QPlatformOpenGLContext11swapBuffersEP16QPlatformSurface(
    QPlatformOpenGLContext *self,
    QPlatformSurface *surface) {
  self->swapBuffers(surface);
}

//  bool QPlatformOpenGLContext::makeCurrent(QPlatformSurface *surface)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QPlatformOpenGLContext11makeCurrentEP16QPlatformSurface(
    QPlatformOpenGLContext *self,
    QPlatformSurface *surface) {
  return self->makeCurrent(surface);
}

//  void QPlatformOpenGLContext::doneCurrent()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QPlatformOpenGLContext11doneCurrentEv(
    QPlatformOpenGLContext *self) {
  self->doneCurrent();
}

//  void QPlatformOpenGLContext::beginFrame()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QPlatformOpenGLContext10beginFrameEv(
    QPlatformOpenGLContext *self) {
  self->beginFrame();
}

//  void QPlatformOpenGLContext::endFrame()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QPlatformOpenGLContext8endFrameEv(
    QPlatformOpenGLContext *self) {
  self->endFrame();
}

//  bool QPlatformOpenGLContext::isSharing() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QPlatformOpenGLContext9isSharingEv(
    const QPlatformOpenGLContext *self) {
  return self->isSharing();
}

//  bool QPlatformOpenGLContext::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QPlatformOpenGLContext7isValidEv(
    const QPlatformOpenGLContext *self) {
  return self->isValid();
}

//  QOpenGLContext *QPlatformOpenGLContext::context() const
extern "C" Q_DECL_EXPORT
QOpenGLContext *ritual_ZNK22QPlatformOpenGLContext7contextEv(
    const QPlatformOpenGLContext *self) {
  return self->context();
}

//  bool QPlatformOpenGLContext::parseOpenGLVersion(const QByteArray
//      &versionString, int &major, int &minor)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QPlatformOpenGLContext18parseOpenGLVersionERK10QByteArrayRiS3_(
    const QByteArray *versionString,
    int *major,
    int *minor) {
  return QPlatformOpenGLContext::parseOpenGLVersion(
      *versionString,
      *major,
      *minor);
}

//  void QPlatformOpenGLContext::setContext(QOpenGLContext *context)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QPlatformOpenGLContext10setContextEP14QOpenGLContext(
    QPlatformOpenGLContext *self,
    QOpenGLContext *context) {
  self->setContext(context);
}

//  a Python function taken by a CuteQPlatformOpenGLContext, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPlatformOpenGLContext(
    QPlatformOpenGLContext *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPlatformOpenGLContext *>(self)->take(key, call);
}

//  void QPlatformOpenGLContext::initialize()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QPlatformOpenGLContext10initializeEv(
    QPlatformOpenGLContext *self) {
  self->QPlatformOpenGLContext::initialize();
}

//  void QPlatformOpenGLContext::beginFrame()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QPlatformOpenGLContext10beginFrameEv(
    QPlatformOpenGLContext *self) {
  self->QPlatformOpenGLContext::beginFrame();
}

//  void QPlatformOpenGLContext::endFrame()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QPlatformOpenGLContext8endFrameEv(
    QPlatformOpenGLContext *self) {
  self->QPlatformOpenGLContext::endFrame();
}

//  bool QPlatformOpenGLContext::isSharing() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK22QPlatformOpenGLContext9isSharingEv(
    const QPlatformOpenGLContext *self) {
  return self->QPlatformOpenGLContext::isSharing();
}

//  bool QPlatformOpenGLContext::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK22QPlatformOpenGLContext7isValidEv(
    const QPlatformOpenGLContext *self) {
  return self->QPlatformOpenGLContext::isValid();
}

#endif  // !defined(QT_NO_OPENGL)
