//  Written by dev_tooling.RitualGenerator from the records of
//  QtWaylandCompositor/qwaylanddestroylistener.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtWaylandCompositor/qwaylanddestroylistener.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QWaylandDestroyListener that Python can take functions over in. Every QWaylandDestroyListener
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWaylandDestroyListenerCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWaylandDestroyListenerCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandDestroyListenerCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandDestroyListenerCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandDestroyListenerCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandDestroyListenerCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandDestroyListenerCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQWaylandDestroyListener : public QWaylandDestroyListener {
public:
  using QWaylandDestroyListener::QWaylandDestroyListener;
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
      CuteQWaylandDestroyListenerCall0 call = reinterpret_cast<CuteQWaylandDestroyListenerCall0>(taken[0]);
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
      CuteQWaylandDestroyListenerCall1 call = reinterpret_cast<CuteQWaylandDestroyListenerCall1>(taken[1]);
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
      CuteQWaylandDestroyListenerCall2 call = reinterpret_cast<CuteQWaylandDestroyListenerCall2>(taken[2]);
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
      CuteQWaylandDestroyListenerCall3 call = reinterpret_cast<CuteQWaylandDestroyListenerCall3>(taken[3]);
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
      CuteQWaylandDestroyListenerCall4 call = reinterpret_cast<CuteQWaylandDestroyListenerCall4>(taken[4]);
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
      CuteQWaylandDestroyListenerCall5 call = reinterpret_cast<CuteQWaylandDestroyListenerCall5>(taken[5]);
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
      CuteQWaylandDestroyListenerCall6 call = reinterpret_cast<CuteQWaylandDestroyListenerCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QWaylandDestroyListener::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK23QWaylandDestroyListener10metaObjectEv(
    const QWaylandDestroyListener *self) {
  return self->metaObject();
}

//  void *QWaylandDestroyListener::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN23QWaylandDestroyListener11qt_metacastEPKc(
    QWaylandDestroyListener *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QWaylandDestroyListener::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN23QWaylandDestroyListener11qt_metacallEN11QMetaObject4CallEiPPv(
    QWaylandDestroyListener *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QWaylandDestroyListener::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN23QWaylandDestroyListener2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QWaylandDestroyListener::tr(s, c, n));
}

//  QWaylandDestroyListenerPrivate *QWaylandDestroyListener::d_func()
extern "C" Q_DECL_EXPORT
QWaylandDestroyListenerPrivate *ritual_ZN23QWaylandDestroyListener6d_funcEv(
    QWaylandDestroyListener *self) {
  return self->d_func();
}

//  const QWaylandDestroyListenerPrivate *QWaylandDestroyListener::d_func()
//      const
extern "C" Q_DECL_EXPORT
const QWaylandDestroyListenerPrivate *ritual_ZNK23QWaylandDestroyListener6d_funcEv(
    const QWaylandDestroyListener *self) {
  return self->d_func();
}

//  QWaylandDestroyListener::QWaylandDestroyListener(QObject *parent)
extern "C" Q_DECL_EXPORT
QWaylandDestroyListener *ritual_ZN23QWaylandDestroyListenerC1EP7QObject(
    QObject *parent) {
  return new CuteQWaylandDestroyListener(parent);
}

//  void QWaylandDestroyListener::listenForDestruction(struct wl_resource
//      *resource)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QWaylandDestroyListener20listenForDestructionEP11wl_resource(
    QWaylandDestroyListener *self,
    struct wl_resource *resource) {
  self->listenForDestruction(resource);
}

//  void QWaylandDestroyListener::reset()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QWaylandDestroyListener5resetEv(
    QWaylandDestroyListener *self) {
  self->reset();
}

//  void QWaylandDestroyListener::fired(void *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QWaylandDestroyListener5firedEPv(
    QWaylandDestroyListener *self,
    void *data) {
  self->fired(data);
}

//  a Python function taken by a CuteQWaylandDestroyListener, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QWaylandDestroyListener(
    QWaylandDestroyListener *self,
    const char *key,
    void *call) {
  return static_cast<CuteQWaylandDestroyListener *>(self)->take(key, call);
}
