//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/qpa/qplatformoffscreensurface.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qplatformoffscreensurface.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qsurfaceformat.h>
#include <cstring>

//  A QPlatformOffscreenSurface that Python can take functions over in. Every QPlatformOffscreenSurface
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQPlatformOffscreenSurfaceCall0)(const void *, int *);
typedef const QSurfaceFormat * (*CuteQPlatformOffscreenSurfaceCall1)(const void *, int *);
typedef bool (*CuteQPlatformOffscreenSurfaceCall2)(const void *, int *);
class CuteQPlatformOffscreenSurface : public QPlatformOffscreenSurface {
public:
  using QPlatformOffscreenSurface::QPlatformOffscreenSurface;
  void *taken[3] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK16QPlatformSurface6screenEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QPlatformSurface6formatEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK25QPlatformOffscreenSurface7isValidEv")) {
      taken[2] = call;
      return true;
    }
    return false;
  }

  //  QPlatformScreen *QPlatformOffscreenSurface::screen() const
  QPlatformScreen *screen() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQPlatformOffscreenSurfaceCall0 call = reinterpret_cast<CuteQPlatformOffscreenSurfaceCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPlatformScreen *>(given);
    }
    return QPlatformOffscreenSurface::screen();
  }

  //  QSurfaceFormat QPlatformOffscreenSurface::format() const
  QSurfaceFormat format() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQPlatformOffscreenSurfaceCall1 call = reinterpret_cast<CuteQPlatformOffscreenSurfaceCall1>(taken[1]);
      const QSurfaceFormat * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QPlatformOffscreenSurface::format();
  }

  //  bool QPlatformOffscreenSurface::isValid() const
  bool isValid() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQPlatformOffscreenSurfaceCall2 call = reinterpret_cast<CuteQPlatformOffscreenSurfaceCall2>(taken[2]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QPlatformOffscreenSurface::isValid();
  }
};

//  QPlatformOffscreenSurface::QPlatformOffscreenSurface(QOffscreenSurface
//      *offscreenSurface)
extern "C" Q_DECL_EXPORT
QPlatformOffscreenSurface *ritual_ZN25QPlatformOffscreenSurfaceC1EP17QOffscreenSurface(
    QOffscreenSurface *offscreenSurface) {
  return new CuteQPlatformOffscreenSurface(offscreenSurface);
}

//  QPlatformOffscreenSurface::~QPlatformOffscreenSurface()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QPlatformOffscreenSurfaceD1Ev(
    QPlatformOffscreenSurface *self) {
  delete self;
}

//  QOffscreenSurface *QPlatformOffscreenSurface::offscreenSurface() const
extern "C" Q_DECL_EXPORT
QOffscreenSurface *ritual_ZNK25QPlatformOffscreenSurface16offscreenSurfaceEv(
    const QPlatformOffscreenSurface *self) {
  return self->offscreenSurface();
}

//  QPlatformScreen *QPlatformOffscreenSurface::screen() const
extern "C" Q_DECL_EXPORT
QPlatformScreen *ritual_ZNK25QPlatformOffscreenSurface6screenEv(
    const QPlatformOffscreenSurface *self) {
  return self->screen();
}

//  QSurfaceFormat QPlatformOffscreenSurface::format() const
extern "C" Q_DECL_EXPORT
QSurfaceFormat *ritual_ZNK25QPlatformOffscreenSurface6formatEv(
    const QPlatformOffscreenSurface *self) {
  return new QSurfaceFormat(self->format());
}

//  bool QPlatformOffscreenSurface::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QPlatformOffscreenSurface7isValidEv(
    const QPlatformOffscreenSurface *self) {
  return self->isValid();
}

//  a Python function taken by a CuteQPlatformOffscreenSurface, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPlatformOffscreenSurface(
    QPlatformOffscreenSurface *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPlatformOffscreenSurface *>(self)->take(key, call);
}

//  QPlatformScreen *QPlatformOffscreenSurface::screen() const
extern "C" Q_DECL_EXPORT
QPlatformScreen *ritual_own_ZNK25QPlatformOffscreenSurface6screenEv(
    const QPlatformOffscreenSurface *self) {
  return self->QPlatformOffscreenSurface::screen();
}

//  QSurfaceFormat QPlatformOffscreenSurface::format() const
extern "C" Q_DECL_EXPORT
QSurfaceFormat *ritual_own_ZNK25QPlatformOffscreenSurface6formatEv(
    const QPlatformOffscreenSurface *self) {
  return new QSurfaceFormat(self->QPlatformOffscreenSurface::format());
}

//  bool QPlatformOffscreenSurface::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK25QPlatformOffscreenSurface7isValidEv(
    const QPlatformOffscreenSurface *self) {
  return self->QPlatformOffscreenSurface::isValid();
}
