//  Written by dev_tooling.RitualGenerator from the records of
//  QtWaylandCompositor/qwaylandquickshellintegration.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtWaylandCompositor/qtwaylandcompositorglobal.h>
#if QT_CONFIG(wayland_compositor_quick)
#if QT_CONFIG(wayland_compositor_quick)
#include <QtWaylandCompositor/qwaylandquickshellintegration.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QWaylandQuickShellIntegration that Python can take functions over in. Every QWaylandQuickShellIntegration
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWaylandQuickShellIntegrationCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWaylandQuickShellIntegrationCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandQuickShellIntegrationCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandQuickShellIntegrationCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandQuickShellIntegrationCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandQuickShellIntegrationCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandQuickShellIntegrationCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQWaylandQuickShellIntegration : public QWaylandQuickShellIntegration {
public:
  using QWaylandQuickShellIntegration::QWaylandQuickShellIntegration;
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
      CuteQWaylandQuickShellIntegrationCall0 call = reinterpret_cast<CuteQWaylandQuickShellIntegrationCall0>(taken[0]);
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
      CuteQWaylandQuickShellIntegrationCall1 call = reinterpret_cast<CuteQWaylandQuickShellIntegrationCall1>(taken[1]);
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
      CuteQWaylandQuickShellIntegrationCall2 call = reinterpret_cast<CuteQWaylandQuickShellIntegrationCall2>(taken[2]);
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
      CuteQWaylandQuickShellIntegrationCall3 call = reinterpret_cast<CuteQWaylandQuickShellIntegrationCall3>(taken[3]);
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
      CuteQWaylandQuickShellIntegrationCall4 call = reinterpret_cast<CuteQWaylandQuickShellIntegrationCall4>(taken[4]);
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
      CuteQWaylandQuickShellIntegrationCall5 call = reinterpret_cast<CuteQWaylandQuickShellIntegrationCall5>(taken[5]);
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
      CuteQWaylandQuickShellIntegrationCall6 call = reinterpret_cast<CuteQWaylandQuickShellIntegrationCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QWaylandQuickShellIntegration::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK29QWaylandQuickShellIntegration10metaObjectEv(
    const QWaylandQuickShellIntegration *self) {
  return self->metaObject();
}

//  void *QWaylandQuickShellIntegration::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN29QWaylandQuickShellIntegration11qt_metacastEPKc(
    QWaylandQuickShellIntegration *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QWaylandQuickShellIntegration::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN29QWaylandQuickShellIntegration11qt_metacallEN11QMetaObject4CallEiPPv(
    QWaylandQuickShellIntegration *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QWaylandQuickShellIntegration::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN29QWaylandQuickShellIntegration2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QWaylandQuickShellIntegration::tr(s, c, n));
}

//  QWaylandQuickShellIntegration::QWaylandQuickShellIntegration(QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QWaylandQuickShellIntegration *ritual_ZN29QWaylandQuickShellIntegrationC1EP7QObject(
    QObject *parent) {
  return new CuteQWaylandQuickShellIntegration(parent);
}

//  QWaylandQuickShellIntegration::~QWaylandQuickShellIntegration()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QWaylandQuickShellIntegrationD1Ev(
    QWaylandQuickShellIntegration *self) {
  delete self;
}

//  a Python function taken by a CuteQWaylandQuickShellIntegration, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QWaylandQuickShellIntegration(
    QWaylandQuickShellIntegration *self,
    const char *key,
    void *call) {
  return static_cast<CuteQWaylandQuickShellIntegration *>(self)->take(key, call);
}

#endif  // QT_CONFIG(wayland_compositor_quick)
#endif  // QT_CONFIG(wayland_compositor_quick)
