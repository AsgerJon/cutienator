//  Written by dev_tooling.RitualGenerator from the records of
//  QtWaylandCompositor/qwaylandquicksurface.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtWaylandCompositor/qtwaylandcompositorglobal.h>
#if QT_CONFIG(wayland_compositor_quick)
#if QT_CONFIG(wayland_compositor_quick)
#include <QtWaylandCompositor/qwaylandquicksurface.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#include <QtQml/QQmlListProperty>
#include <QtCore/QObject>

//  A QWaylandQuickSurface that Python can take functions over in. Every QWaylandQuickSurface
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWaylandQuickSurfaceCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWaylandQuickSurfaceCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandQuickSurfaceCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandQuickSurfaceCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandQuickSurfaceCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandQuickSurfaceCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandQuickSurfaceCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQWaylandQuickSurface : public QWaylandQuickSurface {
public:
  using QWaylandQuickSurface::QWaylandQuickSurface;
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
      CuteQWaylandQuickSurfaceCall0 call = reinterpret_cast<CuteQWaylandQuickSurfaceCall0>(taken[0]);
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
      CuteQWaylandQuickSurfaceCall1 call = reinterpret_cast<CuteQWaylandQuickSurfaceCall1>(taken[1]);
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
      CuteQWaylandQuickSurfaceCall2 call = reinterpret_cast<CuteQWaylandQuickSurfaceCall2>(taken[2]);
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
      CuteQWaylandQuickSurfaceCall3 call = reinterpret_cast<CuteQWaylandQuickSurfaceCall3>(taken[3]);
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
      CuteQWaylandQuickSurfaceCall4 call = reinterpret_cast<CuteQWaylandQuickSurfaceCall4>(taken[4]);
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
      CuteQWaylandQuickSurfaceCall5 call = reinterpret_cast<CuteQWaylandQuickSurfaceCall5>(taken[5]);
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
      CuteQWaylandQuickSurfaceCall6 call = reinterpret_cast<CuteQWaylandQuickSurfaceCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QWaylandQuickSurface::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20QWaylandQuickSurface10metaObjectEv(
    const QWaylandQuickSurface *self) {
  return self->metaObject();
}

//  void *QWaylandQuickSurface::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN20QWaylandQuickSurface11qt_metacastEPKc(
    QWaylandQuickSurface *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QWaylandQuickSurface::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN20QWaylandQuickSurface11qt_metacallEN11QMetaObject4CallEiPPv(
    QWaylandQuickSurface *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QWaylandQuickSurface::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN20QWaylandQuickSurface2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QWaylandQuickSurface::tr(s, c, n));
}

//  QWaylandQuickSurfacePrivate *QWaylandQuickSurface::d_func()
extern "C" Q_DECL_EXPORT
QWaylandQuickSurfacePrivate *ritual_ZN20QWaylandQuickSurface6d_funcEv(
    QWaylandQuickSurface *self) {
  return self->d_func();
}

//  const QWaylandQuickSurfacePrivate *QWaylandQuickSurface::d_func() const
extern "C" Q_DECL_EXPORT
const QWaylandQuickSurfacePrivate *ritual_ZNK20QWaylandQuickSurface6d_funcEv(
    const QWaylandQuickSurface *self) {
  return self->d_func();
}

//  QQmlListProperty<QObject> QWaylandQuickSurface::data()
extern "C" Q_DECL_EXPORT
QQmlListProperty<QObject> *ritual_ZN20QWaylandQuickSurface4dataEv(
    QWaylandQuickSurface *self) {
  return new QQmlListProperty<QObject>(self->data());
}

//  void QWaylandQuickSurface::appendFunction(QQmlListProperty<QObject>
//      *list, QObject *object)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QWaylandQuickSurface14appendFunctionEP16QQmlListPropertyI7QObjectEPS1_(
    QQmlListProperty<QObject> *list,
    QObject *object) {
  QWaylandQuickSurface::appendFunction(list, object);
}

//  qsizetype QWaylandQuickSurface::countFunction(QQmlListProperty<QObject>
//      *list)
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZN20QWaylandQuickSurface13countFunctionEP16QQmlListPropertyI7QObjectE(
    QQmlListProperty<QObject> *list) {
  return QWaylandQuickSurface::countFunction(list);
}

//  QObject *QWaylandQuickSurface::atFunction(QQmlListProperty<QObject>
//      *list, qsizetype index)
extern "C" Q_DECL_EXPORT
QObject *ritual_ZN20QWaylandQuickSurface10atFunctionEP16QQmlListPropertyI7QObjectEx(
    QQmlListProperty<QObject> *list,
    qsizetype index) {
  return QWaylandQuickSurface::atFunction(list, index);
}

//  void QWaylandQuickSurface::clearFunction(QQmlListProperty<QObject> *list)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QWaylandQuickSurface13clearFunctionEP16QQmlListPropertyI7QObjectE(
    QQmlListProperty<QObject> *list) {
  QWaylandQuickSurface::clearFunction(list);
}

//  QWaylandQuickSurface::QWaylandQuickSurface()
extern "C" Q_DECL_EXPORT
QWaylandQuickSurface *ritual_ZN20QWaylandQuickSurfaceC1Ev() {
  return new CuteQWaylandQuickSurface();
}

//  QWaylandQuickSurface::QWaylandQuickSurface(QWaylandCompositor
//      *compositor, QWaylandClient *client, quint32 id, int version)
extern "C" Q_DECL_EXPORT
QWaylandQuickSurface *ritual_ZN20QWaylandQuickSurfaceC1EP18QWaylandCompositorP14QWaylandClientji(
    QWaylandCompositor *compositor,
    QWaylandClient *client,
    quint32 id,
    int version) {
  return new CuteQWaylandQuickSurface(compositor, client, id, version);
}

//  QWaylandQuickSurface::~QWaylandQuickSurface()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QWaylandQuickSurfaceD1Ev(QWaylandQuickSurface *self) {
  delete self;
}

//  bool QWaylandQuickSurface::useTextureAlpha() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QWaylandQuickSurface15useTextureAlphaEv(
    const QWaylandQuickSurface *self) {
  return self->useTextureAlpha();
}

//  void QWaylandQuickSurface::setUseTextureAlpha(bool useTextureAlpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QWaylandQuickSurface18setUseTextureAlphaEb(
    QWaylandQuickSurface *self,
    bool useTextureAlpha) {
  self->setUseTextureAlpha(useTextureAlpha);
}

//  QWaylandQuickSurface::QWaylandQuickSurface(QWaylandQuickSurfacePrivate
//      &dptr)
extern "C" Q_DECL_EXPORT
QWaylandQuickSurface *ritual_ZN20QWaylandQuickSurfaceC1ER27QWaylandQuickSurfacePrivate(
    QWaylandQuickSurfacePrivate *dptr) {
  return new CuteQWaylandQuickSurface(*dptr);
}

//  void QWaylandQuickSurface::useTextureAlphaChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QWaylandQuickSurface22useTextureAlphaChangedEv(
    QWaylandQuickSurface *self) {
  self->useTextureAlphaChanged();
}

//  a Python function taken by a CuteQWaylandQuickSurface, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QWaylandQuickSurface(
    QWaylandQuickSurface *self,
    const char *key,
    void *call) {
  return static_cast<CuteQWaylandQuickSurface *>(self)->take(key, call);
}

//  a QQmlListProperty<QObject> a ritual of QWaylandQuickSurface gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QWaylandQuickSurface__QQmlListProperty_QObject(
    QQmlListProperty<QObject> *self) {
  delete self;
}

#endif  // QT_CONFIG(wayland_compositor_quick)
#endif  // QT_CONFIG(wayland_compositor_quick)
