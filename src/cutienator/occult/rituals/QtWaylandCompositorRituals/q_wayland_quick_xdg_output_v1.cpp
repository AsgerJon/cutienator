//  Written by dev_tooling.RitualGenerator from the records of
//  QtWaylandCompositor/qwaylandquickxdgoutputv1.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtWaylandCompositor/qtwaylandcompositorglobal.h>
#if QT_CONFIG(wayland_compositor_quick)
#if QT_CONFIG(wayland_compositor_quick)
#include <QtWaylandCompositor/qwaylandquickxdgoutputv1.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QWaylandQuickXdgOutputV1 may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQWaylandQuickXdgOutputV1 : QWaylandQuickXdgOutputV1 {
  using QWaylandQuickXdgOutputV1::classBegin;
  using QWaylandQuickXdgOutputV1::componentComplete;
};

//  A QWaylandQuickXdgOutputV1 that Python can take functions over in. Every QWaylandQuickXdgOutputV1
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(wayland_compositor_quick)
typedef void (*CuteQWaylandQuickXdgOutputV1Call0)(const void *, int *);
#endif  // QT_CONFIG(wayland_compositor_quick)
#if QT_CONFIG(wayland_compositor_quick)
typedef void (*CuteQWaylandQuickXdgOutputV1Call1)(const void *, int *);
#endif  // QT_CONFIG(wayland_compositor_quick)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWaylandQuickXdgOutputV1Call2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWaylandQuickXdgOutputV1Call3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandQuickXdgOutputV1Call4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandQuickXdgOutputV1Call5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandQuickXdgOutputV1Call6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandQuickXdgOutputV1Call7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandQuickXdgOutputV1Call8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQWaylandQuickXdgOutputV1 : public QWaylandQuickXdgOutputV1 {
public:
  using QWaylandQuickXdgOutputV1::QWaylandQuickXdgOutputV1;
  void *taken[9] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(wayland_compositor_quick)
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(wayland_compositor_quick)
#if QT_CONFIG(wayland_compositor_quick)
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(wayland_compositor_quick)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if QT_CONFIG(wayland_compositor_quick)
  //  void QWaylandQuickXdgOutputV1::classBegin()
  void classBegin() override {
    if (taken[0]) {
      int handled = 0;
      CuteQWaylandQuickXdgOutputV1Call0 call = reinterpret_cast<CuteQWaylandQuickXdgOutputV1Call0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QWaylandQuickXdgOutputV1::classBegin();
  }
#endif  // QT_CONFIG(wayland_compositor_quick)

#if QT_CONFIG(wayland_compositor_quick)
  //  void QWaylandQuickXdgOutputV1::componentComplete()
  void componentComplete() override {
    if (taken[1]) {
      int handled = 0;
      CuteQWaylandQuickXdgOutputV1Call1 call = reinterpret_cast<CuteQWaylandQuickXdgOutputV1Call1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QWaylandQuickXdgOutputV1::componentComplete();
  }
#endif  // QT_CONFIG(wayland_compositor_quick)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQWaylandQuickXdgOutputV1Call2 call = reinterpret_cast<CuteQWaylandQuickXdgOutputV1Call2>(taken[2]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQWaylandQuickXdgOutputV1Call3 call = reinterpret_cast<CuteQWaylandQuickXdgOutputV1Call3>(taken[3]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQWaylandQuickXdgOutputV1Call4 call = reinterpret_cast<CuteQWaylandQuickXdgOutputV1Call4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQWaylandQuickXdgOutputV1Call5 call = reinterpret_cast<CuteQWaylandQuickXdgOutputV1Call5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQWaylandQuickXdgOutputV1Call6 call = reinterpret_cast<CuteQWaylandQuickXdgOutputV1Call6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[7]) {
      int handled = 0;
      CuteQWaylandQuickXdgOutputV1Call7 call = reinterpret_cast<CuteQWaylandQuickXdgOutputV1Call7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[8]) {
      int handled = 0;
      CuteQWaylandQuickXdgOutputV1Call8 call = reinterpret_cast<CuteQWaylandQuickXdgOutputV1Call8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QWaylandQuickXdgOutputV1::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK24QWaylandQuickXdgOutputV110metaObjectEv(
    const QWaylandQuickXdgOutputV1 *self) {
  return self->metaObject();
}

//  void *QWaylandQuickXdgOutputV1::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN24QWaylandQuickXdgOutputV111qt_metacastEPKc(
    QWaylandQuickXdgOutputV1 *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QWaylandQuickXdgOutputV1::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN24QWaylandQuickXdgOutputV111qt_metacallEN11QMetaObject4CallEiPPv(
    QWaylandQuickXdgOutputV1 *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QWaylandQuickXdgOutputV1::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN24QWaylandQuickXdgOutputV12trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QWaylandQuickXdgOutputV1::tr(s, c, n));
}

//  QWaylandQuickXdgOutputV1::QWaylandQuickXdgOutputV1()
extern "C" Q_DECL_EXPORT
QWaylandQuickXdgOutputV1 *ritual_ZN24QWaylandQuickXdgOutputV1C1Ev() {
  return new CuteQWaylandQuickXdgOutputV1();
}

//  void QWaylandQuickXdgOutputV1::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QWaylandQuickXdgOutputV110classBeginEv(
    QWaylandQuickXdgOutputV1 *self) {
  self->classBegin();
}

//  void QWaylandQuickXdgOutputV1::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QWaylandQuickXdgOutputV117componentCompleteEv(
    QWaylandQuickXdgOutputV1 *self) {
  self->componentComplete();
}

//  QWaylandQuickXdgOutputV1 as the QQmlParserStatus it is built on
extern "C" Q_DECL_EXPORT
QQmlParserStatus *ritual_cast_QWaylandQuickXdgOutputV1_QQmlParserStatus(
    QWaylandQuickXdgOutputV1 *self) {
  return static_cast<QQmlParserStatus *>(self);
}

//  a Python function taken by a CuteQWaylandQuickXdgOutputV1, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QWaylandQuickXdgOutputV1(
    QWaylandQuickXdgOutputV1 *self,
    const char *key,
    void *call) {
  return static_cast<CuteQWaylandQuickXdgOutputV1 *>(self)->take(key, call);
}

//  void QWaylandQuickXdgOutputV1::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QWaylandQuickXdgOutputV110classBeginEv(
    QWaylandQuickXdgOutputV1 *self) {
  static_cast<OwnQWaylandQuickXdgOutputV1 *>(self)->OwnQWaylandQuickXdgOutputV1::classBegin();
}

//  void QWaylandQuickXdgOutputV1::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QWaylandQuickXdgOutputV117componentCompleteEv(
    QWaylandQuickXdgOutputV1 *self) {
  static_cast<OwnQWaylandQuickXdgOutputV1 *>(self)->OwnQWaylandQuickXdgOutputV1::componentComplete();
}

#endif  // QT_CONFIG(wayland_compositor_quick)
#endif  // QT_CONFIG(wayland_compositor_quick)
