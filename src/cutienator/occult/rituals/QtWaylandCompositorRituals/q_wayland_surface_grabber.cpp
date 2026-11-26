//  Written by dev_tooling.RitualGenerator from the records of
//  QtWaylandCompositor/qwaylandsurfacegrabber.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtWaylandCompositor/qwaylandsurfacegrabber.h>
#include <QtCore/qstring.h>
#include <QtGui/qimage.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QWaylandSurfaceGrabber that Python can take functions over in. Every QWaylandSurfaceGrabber
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWaylandSurfaceGrabberCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWaylandSurfaceGrabberCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandSurfaceGrabberCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandSurfaceGrabberCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandSurfaceGrabberCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandSurfaceGrabberCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandSurfaceGrabberCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQWaylandSurfaceGrabber : public QWaylandSurfaceGrabber {
public:
  using QWaylandSurfaceGrabber::QWaylandSurfaceGrabber;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQWaylandSurfaceGrabberCall0 call = reinterpret_cast<CuteQWaylandSurfaceGrabberCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQWaylandSurfaceGrabberCall1 call = reinterpret_cast<CuteQWaylandSurfaceGrabberCall1>(taken[1]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQWaylandSurfaceGrabberCall2 call = reinterpret_cast<CuteQWaylandSurfaceGrabberCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQWaylandSurfaceGrabberCall3 call = reinterpret_cast<CuteQWaylandSurfaceGrabberCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQWaylandSurfaceGrabberCall4 call = reinterpret_cast<CuteQWaylandSurfaceGrabberCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteQWaylandSurfaceGrabberCall5 call = reinterpret_cast<CuteQWaylandSurfaceGrabberCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQWaylandSurfaceGrabberCall6 call = reinterpret_cast<CuteQWaylandSurfaceGrabberCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QWaylandSurfaceGrabber::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK22QWaylandSurfaceGrabber10metaObjectEv(
    const QWaylandSurfaceGrabber *self) {
  return self->metaObject();
}

//  void *QWaylandSurfaceGrabber::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN22QWaylandSurfaceGrabber11qt_metacastEPKc(
    QWaylandSurfaceGrabber *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QWaylandSurfaceGrabber::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN22QWaylandSurfaceGrabber11qt_metacallEN11QMetaObject4CallEiPPv(
    QWaylandSurfaceGrabber *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QWaylandSurfaceGrabber::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN22QWaylandSurfaceGrabber2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QWaylandSurfaceGrabber::tr(s, c, n));
}

//  QWaylandSurfaceGrabberPrivate *QWaylandSurfaceGrabber::d_func()
extern "C" Q_DECL_EXPORT
QWaylandSurfaceGrabberPrivate *ritual_ZN22QWaylandSurfaceGrabber6d_funcEv(
    QWaylandSurfaceGrabber *self) {
  return self->d_func();
}

//  const QWaylandSurfaceGrabberPrivate *QWaylandSurfaceGrabber::d_func()
//      const
extern "C" Q_DECL_EXPORT
const QWaylandSurfaceGrabberPrivate *ritual_ZNK22QWaylandSurfaceGrabber6d_funcEv(
    const QWaylandSurfaceGrabber *self) {
  return self->d_func();
}

//  QWaylandSurfaceGrabber::QWaylandSurfaceGrabber(QWaylandSurface *surface,
//      QObject *parent)
extern "C" Q_DECL_EXPORT
QWaylandSurfaceGrabber *ritual_ZN22QWaylandSurfaceGrabberC1EP15QWaylandSurfaceP7QObject(
    QWaylandSurface *surface,
    QObject *parent) {
  return new CuteQWaylandSurfaceGrabber(surface, parent);
}

//  QWaylandSurface *QWaylandSurfaceGrabber::surface() const
extern "C" Q_DECL_EXPORT
QWaylandSurface *ritual_ZNK22QWaylandSurfaceGrabber7surfaceEv(
    const QWaylandSurfaceGrabber *self) {
  return self->surface();
}

//  void QWaylandSurfaceGrabber::grab()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QWaylandSurfaceGrabber4grabEv(QWaylandSurfaceGrabber *self) {
  self->grab();
}

//  void QWaylandSurfaceGrabber::success(const QImage &image)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QWaylandSurfaceGrabber7successERK6QImage(
    QWaylandSurfaceGrabber *self,
    const QImage *image) {
  self->success(*image);
}

//  void QWaylandSurfaceGrabber::failed(Error error)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QWaylandSurfaceGrabber6failedENS_5ErrorE(
    QWaylandSurfaceGrabber *self,
    QWaylandSurfaceGrabber::Error error) {
  self->failed(error);
}

//  a Python function taken by a CuteQWaylandSurfaceGrabber, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QWaylandSurfaceGrabber(
    QWaylandSurfaceGrabber *self,
    const char *key,
    void *call) {
  return static_cast<CuteQWaylandSurfaceGrabber *>(self)->take(key, call);
}
