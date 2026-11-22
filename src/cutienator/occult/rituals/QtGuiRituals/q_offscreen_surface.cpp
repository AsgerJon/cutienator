//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qoffscreensurface.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qoffscreensurface.h>
#include <QtCore/qstring.h>
#include <QtGui/qsurfaceformat.h>
#include <QtCore/qsize.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QOffscreenSurface that Python can take functions over in. Every QOffscreenSurface
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQOffscreenSurfaceCall0)(const void *, int *);
typedef const QSurfaceFormat * (*CuteQOffscreenSurfaceCall1)(const void *, int *);
typedef const QSize * (*CuteQOffscreenSurfaceCall2)(const void *, int *);
typedef bool (*CuteQOffscreenSurfaceCall3)(const void *, QEvent *, int *);
typedef bool (*CuteQOffscreenSurfaceCall4)(const void *, QObject *, QEvent *, int *);
typedef void (*CuteQOffscreenSurfaceCall5)(const void *, QTimerEvent *, int *);
typedef void (*CuteQOffscreenSurfaceCall6)(const void *, QChildEvent *, int *);
typedef void (*CuteQOffscreenSurfaceCall7)(const void *, QEvent *, int *);
typedef void (*CuteQOffscreenSurfaceCall8)(const void *, const QMetaMethod *, int *);
typedef void (*CuteQOffscreenSurfaceCall9)(const void *, const QMetaMethod *, int *);
class CuteQOffscreenSurface : public QOffscreenSurface {
public:
  using QOffscreenSurface::QOffscreenSurface;
  void *taken[10] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK8QSurface11surfaceTypeEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK8QSurface6formatEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK8QSurface4sizeEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[9] = call;
      return true;
    }
    return false;
  }

  //  SurfaceType QOffscreenSurface::surfaceType() const
  QSurface::SurfaceType surfaceType() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQOffscreenSurfaceCall0 call = reinterpret_cast<CuteQOffscreenSurfaceCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<QSurface::SurfaceType>(given);
    }
    return QOffscreenSurface::surfaceType();
  }

  //  QSurfaceFormat QOffscreenSurface::format() const
  QSurfaceFormat format() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQOffscreenSurfaceCall1 call = reinterpret_cast<CuteQOffscreenSurfaceCall1>(taken[1]);
      const QSurfaceFormat * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QOffscreenSurface::format();
  }

  //  QSize QOffscreenSurface::size() const
  QSize size() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQOffscreenSurfaceCall2 call = reinterpret_cast<CuteQOffscreenSurfaceCall2>(taken[2]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QOffscreenSurface::size();
  }

  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQOffscreenSurfaceCall3 call = reinterpret_cast<CuteQOffscreenSurfaceCall3>(taken[3]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }

  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQOffscreenSurfaceCall4 call = reinterpret_cast<CuteQOffscreenSurfaceCall4>(taken[4]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }

  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQOffscreenSurfaceCall5 call = reinterpret_cast<CuteQOffscreenSurfaceCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }

  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQOffscreenSurfaceCall6 call = reinterpret_cast<CuteQOffscreenSurfaceCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }

  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQOffscreenSurfaceCall7 call = reinterpret_cast<CuteQOffscreenSurfaceCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }

  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[8]) {
      int handled = 0;
      CuteQOffscreenSurfaceCall8 call = reinterpret_cast<CuteQOffscreenSurfaceCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }

  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[9]) {
      int handled = 0;
      CuteQOffscreenSurfaceCall9 call = reinterpret_cast<CuteQOffscreenSurfaceCall9>(taken[9]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
};

//  const QMetaObject *QOffscreenSurface::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QOffscreenSurface10metaObjectEv(
    const QOffscreenSurface *self) {
  return self->metaObject();
}

//  QString QOffscreenSurface::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QOffscreenSurface2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QOffscreenSurface::tr(s, c, n));
}

//  QOffscreenSurface::QOffscreenSurface(QScreen *screen, QObject *parent)
extern "C" Q_DECL_EXPORT
QOffscreenSurface *ritual_ZN17QOffscreenSurfaceC1EP7QScreenP7QObject(
    QScreen *screen,
    QObject *parent) {
  return new CuteQOffscreenSurface(screen, parent);
}

//  QOffscreenSurface::~QOffscreenSurface()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QOffscreenSurfaceD1Ev(QOffscreenSurface *self) {
  delete self;
}

//  SurfaceType QOffscreenSurface::surfaceType() const
extern "C" Q_DECL_EXPORT
QSurface::SurfaceType ritual_ZNK17QOffscreenSurface11surfaceTypeEv(
    const QOffscreenSurface *self) {
  return self->surfaceType();
}

//  void QOffscreenSurface::create()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QOffscreenSurface6createEv(QOffscreenSurface *self) {
  self->create();
}

//  void QOffscreenSurface::destroy()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QOffscreenSurface7destroyEv(QOffscreenSurface *self) {
  self->destroy();
}

//  bool QOffscreenSurface::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QOffscreenSurface7isValidEv(const QOffscreenSurface *self) {
  return self->isValid();
}

//  void QOffscreenSurface::setFormat(const QSurfaceFormat &format)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QOffscreenSurface9setFormatERK14QSurfaceFormat(
    QOffscreenSurface *self,
    const QSurfaceFormat *format) {
  self->setFormat(*format);
}

//  QSurfaceFormat QOffscreenSurface::format() const
extern "C" Q_DECL_EXPORT
QSurfaceFormat *ritual_ZNK17QOffscreenSurface6formatEv(
    const QOffscreenSurface *self) {
  return new QSurfaceFormat(self->format());
}

//  QSurfaceFormat QOffscreenSurface::requestedFormat() const
extern "C" Q_DECL_EXPORT
QSurfaceFormat *ritual_ZNK17QOffscreenSurface15requestedFormatEv(
    const QOffscreenSurface *self) {
  return new QSurfaceFormat(self->requestedFormat());
}

//  QSize QOffscreenSurface::size() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK17QOffscreenSurface4sizeEv(const QOffscreenSurface *self) {
  return new QSize(self->size());
}

//  QScreen *QOffscreenSurface::screen() const
extern "C" Q_DECL_EXPORT
QScreen *ritual_ZNK17QOffscreenSurface6screenEv(
    const QOffscreenSurface *self) {
  return self->screen();
}

//  void QOffscreenSurface::setScreen(QScreen *screen)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QOffscreenSurface9setScreenEP7QScreen(
    QOffscreenSurface *self,
    QScreen *screen) {
  self->setScreen(screen);
}

//  QOffscreenSurface as the QSurface it is built on
extern "C" Q_DECL_EXPORT
QSurface *ritual_cast_QOffscreenSurface_QSurface(QOffscreenSurface *self) {
  return static_cast<QSurface *>(self);
}

//  a Python function taken by a CuteQOffscreenSurface, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QOffscreenSurface(
    QOffscreenSurface *self,
    const char *key,
    void *call) {
  return static_cast<CuteQOffscreenSurface *>(self)->take(key, call);
}

//  SurfaceType QOffscreenSurface::surfaceType() const
extern "C" Q_DECL_EXPORT
QSurface::SurfaceType ritual_own_ZNK17QOffscreenSurface11surfaceTypeEv(
    const QOffscreenSurface *self) {
  return self->QOffscreenSurface::surfaceType();
}

//  QSurfaceFormat QOffscreenSurface::format() const
extern "C" Q_DECL_EXPORT
QSurfaceFormat *ritual_own_ZNK17QOffscreenSurface6formatEv(
    const QOffscreenSurface *self) {
  return new QSurfaceFormat(self->QOffscreenSurface::format());
}

//  QSize QOffscreenSurface::size() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK17QOffscreenSurface4sizeEv(
    const QOffscreenSurface *self) {
  return new QSize(self->QOffscreenSurface::size());
}
