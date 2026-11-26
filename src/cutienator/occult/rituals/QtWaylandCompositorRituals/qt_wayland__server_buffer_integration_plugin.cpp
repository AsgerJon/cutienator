//  Written by dev_tooling.RitualGenerator from the records of QtWaylandCompo
//  sitor/6.12.0/QtWaylandCompositor/private/qwlserverbufferintegrationplugin
//  _p.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtWaylandCompositor/qtwaylandcompositorglobal.h>
#include <QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qtwaylandcompositorglobal_p.h>
#if QT_CONFIG(opengl)
#include <QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qtwaylandcompositorglobal_p.h>
#include <QtWaylandCompositor/QtWaylandCompositor>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qwlserverbufferintegrationplugin_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QtWayland::ServerBufferIntegrationPlugin that Python can take functions over in. Every QtWayland::ServerBufferIntegrationPlugin
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQtWayland_ServerBufferIntegrationPluginCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQtWayland_ServerBufferIntegrationPluginCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtWayland_ServerBufferIntegrationPluginCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtWayland_ServerBufferIntegrationPluginCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtWayland_ServerBufferIntegrationPluginCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtWayland_ServerBufferIntegrationPluginCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtWayland_ServerBufferIntegrationPluginCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQtWayland_ServerBufferIntegrationPlugin : public QtWayland::ServerBufferIntegrationPlugin {
public:
  using QtWayland::ServerBufferIntegrationPlugin::ServerBufferIntegrationPlugin;
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
      CuteQtWayland_ServerBufferIntegrationPluginCall0 call = reinterpret_cast<CuteQtWayland_ServerBufferIntegrationPluginCall0>(taken[0]);
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
      CuteQtWayland_ServerBufferIntegrationPluginCall1 call = reinterpret_cast<CuteQtWayland_ServerBufferIntegrationPluginCall1>(taken[1]);
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
      CuteQtWayland_ServerBufferIntegrationPluginCall2 call = reinterpret_cast<CuteQtWayland_ServerBufferIntegrationPluginCall2>(taken[2]);
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
      CuteQtWayland_ServerBufferIntegrationPluginCall3 call = reinterpret_cast<CuteQtWayland_ServerBufferIntegrationPluginCall3>(taken[3]);
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
      CuteQtWayland_ServerBufferIntegrationPluginCall4 call = reinterpret_cast<CuteQtWayland_ServerBufferIntegrationPluginCall4>(taken[4]);
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
      CuteQtWayland_ServerBufferIntegrationPluginCall5 call = reinterpret_cast<CuteQtWayland_ServerBufferIntegrationPluginCall5>(taken[5]);
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
      CuteQtWayland_ServerBufferIntegrationPluginCall6 call = reinterpret_cast<CuteQtWayland_ServerBufferIntegrationPluginCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QtWayland::ServerBufferIntegrationPlugin::metaObject()
//      const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK9QtWayland29ServerBufferIntegrationPlugin10metaObjectEv(
    const QtWayland::ServerBufferIntegrationPlugin *self) {
  return self->metaObject();
}

//  void *QtWayland::ServerBufferIntegrationPlugin::qt_metacast(const char
//      *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN9QtWayland29ServerBufferIntegrationPlugin11qt_metacastEPKc(
    QtWayland::ServerBufferIntegrationPlugin *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int
//      QtWayland::ServerBufferIntegrationPlugin::qt_metacall(QMetaObject::Ca
//      ll a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN9QtWayland29ServerBufferIntegrationPlugin11qt_metacallEN11QMetaObject4CallEiPPv(
    QtWayland::ServerBufferIntegrationPlugin *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QtWayland::ServerBufferIntegrationPlugin::tr(const char *s, const
//      char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN9QtWayland29ServerBufferIntegrationPlugin2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QtWayland::ServerBufferIntegrationPlugin::tr(s, c, n));
}

//  QtWayland::ServerBufferIntegrationPlugin::~ServerBufferIntegrationPlugin(
//      )
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtWayland29ServerBufferIntegrationPluginD1Ev(
    QtWayland::ServerBufferIntegrationPlugin *self) {
  delete self;
}

//  ServerBufferIntegration
//      *QtWayland::ServerBufferIntegrationPlugin::create(const QString &key,
//      const QStringList &paramList)
extern "C" Q_DECL_EXPORT
QtWayland::ServerBufferIntegration *ritual_ZN9QtWayland29ServerBufferIntegrationPlugin6createERK7QStringRK5QListIS1_E(
    QtWayland::ServerBufferIntegrationPlugin *self,
    const QString *key,
    const QList<QString> *paramList) {
  return self->create(*key, *paramList);
}

//  a Python function taken by a CuteQtWayland_ServerBufferIntegrationPlugin,
//      for the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QtWayland_ServerBufferIntegrationPlugin(
    QtWayland::ServerBufferIntegrationPlugin *self,
    const char *key,
    void *call) {
  return static_cast<CuteQtWayland_ServerBufferIntegrationPlugin *>(self)->take(key, call);
}

#endif  // QT_CONFIG(opengl)
