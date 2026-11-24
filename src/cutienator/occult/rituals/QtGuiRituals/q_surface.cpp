//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qsurface.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qsurface.h>
#include <QtGui/qsurfaceformat.h>
#include <QtCore/qsize.h>
#include <cstring>

//  A QSurface that Python can take functions over in. Every QSurface
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QSurfaceFormat * (*CuteQSurfaceCall0)(const void *, int *);
typedef void * (*CuteQSurfaceCall1)(const void *, int *);
typedef int (*CuteQSurfaceCall2)(const void *, int *);
typedef const QSize * (*CuteQSurfaceCall3)(const void *, int *);
class CuteQSurface : public QSurface {
public:
  using QSurface::QSurface;
  void *taken[4] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK8QSurface6formatEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK8QSurface13surfaceHandleEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK8QSurface11surfaceTypeEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK8QSurface4sizeEv")) {
      taken[3] = call;
      return true;
    }
    return false;
  }

  //  QSurfaceFormat QSurface::format() const
  QSurfaceFormat format() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSurfaceCall0 call = reinterpret_cast<CuteQSurfaceCall0>(taken[0]);
      const QSurfaceFormat * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  QPlatformSurface *QSurface::surfaceHandle() const
  QPlatformSurface *surfaceHandle() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQSurfaceCall1 call = reinterpret_cast<CuteQSurfaceCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPlatformSurface *>(given);
    }
    return {};
  }

  //  SurfaceType QSurface::surfaceType() const
  QSurface::SurfaceType surfaceType() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQSurfaceCall2 call = reinterpret_cast<CuteQSurfaceCall2>(taken[2]);
      int given = call(this, &handled);
      if (handled) return static_cast<QSurface::SurfaceType>(given);
    }
    return {};
  }

  //  QSize QSurface::size() const
  QSize size() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQSurfaceCall3 call = reinterpret_cast<CuteQSurfaceCall3>(taken[3]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }
};

//  QSurface::~QSurface()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QSurfaceD1Ev(QSurface *self) {
  delete self;
}

//  SurfaceClass QSurface::surfaceClass() const
extern "C" Q_DECL_EXPORT
QSurface::SurfaceClass ritual_ZNK8QSurface12surfaceClassEv(
    const QSurface *self) {
  return self->surfaceClass();
}

//  QSurfaceFormat QSurface::format() const
extern "C" Q_DECL_EXPORT
QSurfaceFormat *ritual_ZNK8QSurface6formatEv(const QSurface *self) {
  return new QSurfaceFormat(self->format());
}

//  QPlatformSurface *QSurface::surfaceHandle() const
extern "C" Q_DECL_EXPORT
QPlatformSurface *ritual_ZNK8QSurface13surfaceHandleEv(
    const QSurface *self) {
  return self->surfaceHandle();
}

//  SurfaceType QSurface::surfaceType() const
extern "C" Q_DECL_EXPORT
QSurface::SurfaceType ritual_ZNK8QSurface11surfaceTypeEv(
    const QSurface *self) {
  return self->surfaceType();
}

//  bool QSurface::supportsOpenGL() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QSurface14supportsOpenGLEv(const QSurface *self) {
  return self->supportsOpenGL();
}

//  QSize QSurface::size() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK8QSurface4sizeEv(const QSurface *self) {
  return new QSize(self->size());
}

//  a Python function taken by a CuteQSurface, for the function named by the
//      key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSurface(QSurface *self, const char *key, void *call) {
  return static_cast<CuteQSurface *>(self)->take(key, call);
}
