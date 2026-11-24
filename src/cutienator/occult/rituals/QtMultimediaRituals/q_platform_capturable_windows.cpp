//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/6.12.0/QtMultimedia/private/qplatformcapturablewindows_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#include <QtMultimedia/QtMultimedia>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/6.12.0/QtMultimedia/private/qplatformcapturablewindows_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/qcapturablewindow.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/6.12.0/QtMultimedia/private/qcapturablewindow_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qlist.h>
#include <cstring>

//  A QPlatformCapturableWindows that Python can take functions over in. Every QPlatformCapturableWindows
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQPlatformCapturableWindowsCall0)(const void *, const QCapturableWindowPrivate *, int *);
class CuteQPlatformCapturableWindows : public QPlatformCapturableWindows {
public:
  using QPlatformCapturableWindows::QPlatformCapturableWindows;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK26QPlatformCapturableWindows13isWindowValidERK24QCapturableWindowPrivate")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  bool QPlatformCapturableWindows::isWindowValid(const
  //      QCapturableWindowPrivate &a0) const
  bool isWindowValid(const QCapturableWindowPrivate &a0) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQPlatformCapturableWindowsCall0 call = reinterpret_cast<CuteQPlatformCapturableWindowsCall0>(taken[0]);
      bool given = call(this, &a0, &handled);
      if (handled) return given;
    }
    return QPlatformCapturableWindows::isWindowValid(a0);
  }
};

//  QPlatformCapturableWindows::QPlatformCapturableWindows()
extern "C" Q_DECL_EXPORT
QPlatformCapturableWindows *ritual_ZN26QPlatformCapturableWindowsC1Ev() {
  return new CuteQPlatformCapturableWindows();
}

//  QPlatformCapturableWindows::~QPlatformCapturableWindows()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QPlatformCapturableWindowsD1Ev(
    QPlatformCapturableWindows *self) {
  delete self;
}

//  QList<QCapturableWindow> QPlatformCapturableWindows::windows() const
extern "C" Q_DECL_EXPORT
QList<QCapturableWindow> *ritual_ZNK26QPlatformCapturableWindows7windowsEv(
    const QPlatformCapturableWindows *self) {
  return new QList<QCapturableWindow>(self->windows());
}

//  bool QPlatformCapturableWindows::isWindowValid(const
//      QCapturableWindowPrivate &a0) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK26QPlatformCapturableWindows13isWindowValidERK24QCapturableWindowPrivate(
    const QPlatformCapturableWindows *self,
    const QCapturableWindowPrivate *a0) {
  return self->isWindowValid(*a0);
}

//  a Python function taken by a CuteQPlatformCapturableWindows, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPlatformCapturableWindows(
    QPlatformCapturableWindows *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPlatformCapturableWindows *>(self)->take(key, call);
}

//  bool QPlatformCapturableWindows::isWindowValid(const
//      QCapturableWindowPrivate &a0) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK26QPlatformCapturableWindows13isWindowValidERK24QCapturableWindowPrivate(
    const QPlatformCapturableWindows *self,
    const QCapturableWindowPrivate *a0) {
  return self->QPlatformCapturableWindows::isWindowValid(*a0);
}
