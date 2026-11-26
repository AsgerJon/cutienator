//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/qpa/qplatformsurface.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qplatformsurface.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qsurfaceformat.h>
#include <cstring>

//  A QPlatformSurface that Python can take functions over in. Every QPlatformSurface
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QSurfaceFormat * (*CuteQPlatformSurfaceCall0)(const void *, int *);
typedef void * (*CuteQPlatformSurfaceCall1)(const void *, int *);
class CuteQPlatformSurface : public QPlatformSurface {
public:
  using QPlatformSurface::QPlatformSurface;
  void *taken[2] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK16QPlatformSurface6formatEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QPlatformSurface6screenEv")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

  //  QSurfaceFormat QPlatformSurface::format() const
  QSurfaceFormat format() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQPlatformSurfaceCall0 call = reinterpret_cast<CuteQPlatformSurfaceCall0>(taken[0]);
      const QSurfaceFormat * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  QPlatformScreen *QPlatformSurface::screen() const
  QPlatformScreen *screen() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQPlatformSurfaceCall1 call = reinterpret_cast<CuteQPlatformSurfaceCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPlatformScreen *>(given);
    }
    return {};
  }
};

//  QPlatformSurface::~QPlatformSurface()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QPlatformSurfaceD1Ev(QPlatformSurface *self) {
  delete self;
}

//  QSurfaceFormat QPlatformSurface::format() const
extern "C" Q_DECL_EXPORT
QSurfaceFormat *ritual_ZNK16QPlatformSurface6formatEv(
    const QPlatformSurface *self) {
  return new QSurfaceFormat(self->format());
}

//  QSurface *QPlatformSurface::surface() const
extern "C" Q_DECL_EXPORT
QSurface *ritual_ZNK16QPlatformSurface7surfaceEv(
    const QPlatformSurface *self) {
  return self->surface();
}

//  QPlatformScreen *QPlatformSurface::screen() const
extern "C" Q_DECL_EXPORT
QPlatformScreen *ritual_ZNK16QPlatformSurface6screenEv(
    const QPlatformSurface *self) {
  return self->screen();
}

//  QPlatformSurface::QPlatformSurface(QSurface *surface)
extern "C" Q_DECL_EXPORT
QPlatformSurface *ritual_ZN16QPlatformSurfaceC1EP8QSurface(
    QSurface *surface) {
  return new CuteQPlatformSurface(surface);
}

//  a Python function taken by a CuteQPlatformSurface, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPlatformSurface(
    QPlatformSurface *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPlatformSurface *>(self)->take(key, call);
}
