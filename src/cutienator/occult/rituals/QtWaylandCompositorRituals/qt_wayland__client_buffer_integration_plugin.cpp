//  Written by hand on 2026-11-25 from
//  QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qwlclientbufferintegrationplugin_p.h,
//  Qt 6.12.0, from Qt's source. Kept as it is when the generator runs
//  again.
//  Qt builds the class under QT_CONFIG(opengl), as its CMakeLists.txt
//  says.
//  The Cute class takes over 'create' too, which is pure: the class
//  would be abstract without it. Without a Python function handed over
//  for it, 'create' gives a null pointer.
#include <QtGui/qtguiglobal.h>
#include <QtWaylandCompositor/qtwaylandcompositorglobal.h>
#if QT_CONFIG(opengl)
#include <QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qwlclientbufferintegrationplugin_p.h>
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QtWayland::ClientBufferIntegrationPlugin that Python can take functions over in. Every QtWayland::ClientBufferIntegrationPlugin
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQtWayland_ClientBufferIntegrationPluginCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQtWayland_ClientBufferIntegrationPluginCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtWayland_ClientBufferIntegrationPluginCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtWayland_ClientBufferIntegrationPluginCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtWayland_ClientBufferIntegrationPluginCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtWayland_ClientBufferIntegrationPluginCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtWayland_ClientBufferIntegrationPluginCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef QtWayland::ClientBufferIntegration *(*CuteQtWayland_ClientBufferIntegrationPluginCall7)(const void *, const QString *, const QList<QString> *, int *);
class CuteQtWayland_ClientBufferIntegrationPlugin : public QtWayland::ClientBufferIntegrationPlugin {
public:
  using QtWayland::ClientBufferIntegrationPlugin::ClientBufferIntegrationPlugin;
  void *taken[8] = {};

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
    if (!std::strcmp(key, "_ZN9QtWayland29ClientBufferIntegrationPlugin6createERK7QStringRK5QListIS1_E")) {
      taken[7] = call;
      return true;
    }
    return false;
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQtWayland_ClientBufferIntegrationPluginCall0 call = reinterpret_cast<CuteQtWayland_ClientBufferIntegrationPluginCall0>(taken[0]);
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
      CuteQtWayland_ClientBufferIntegrationPluginCall1 call = reinterpret_cast<CuteQtWayland_ClientBufferIntegrationPluginCall1>(taken[1]);
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
      CuteQtWayland_ClientBufferIntegrationPluginCall2 call = reinterpret_cast<CuteQtWayland_ClientBufferIntegrationPluginCall2>(taken[2]);
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
      CuteQtWayland_ClientBufferIntegrationPluginCall3 call = reinterpret_cast<CuteQtWayland_ClientBufferIntegrationPluginCall3>(taken[3]);
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
      CuteQtWayland_ClientBufferIntegrationPluginCall4 call = reinterpret_cast<CuteQtWayland_ClientBufferIntegrationPluginCall4>(taken[4]);
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
      CuteQtWayland_ClientBufferIntegrationPluginCall5 call = reinterpret_cast<CuteQtWayland_ClientBufferIntegrationPluginCall5>(taken[5]);
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
      CuteQtWayland_ClientBufferIntegrationPluginCall6 call = reinterpret_cast<CuteQtWayland_ClientBufferIntegrationPluginCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  ClientBufferIntegration
  //      *QtWayland::ClientBufferIntegrationPlugin::create(const QString
  //      &key, const QStringList &paramList)
  QtWayland::ClientBufferIntegration *create(
      const QString &key, const QStringList &paramList) override {
    if (taken[7]) {
      int handled = 0;
      CuteQtWayland_ClientBufferIntegrationPluginCall7 call = reinterpret_cast<CuteQtWayland_ClientBufferIntegrationPluginCall7>(taken[7]);
      QtWayland::ClientBufferIntegration *given = call(this, &key, &paramList, &handled);
      if (handled) return given;
    }
    return nullptr;
  }
};

//  const QMetaObject *QtWayland::ClientBufferIntegrationPlugin::metaObject()
//      const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK9QtWayland29ClientBufferIntegrationPlugin10metaObjectEv(
    const QtWayland::ClientBufferIntegrationPlugin *self) {
  return self->metaObject();
}

//  QString QtWayland::ClientBufferIntegrationPlugin::tr(const char *s, const
//      char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN9QtWayland29ClientBufferIntegrationPlugin2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QtWayland::ClientBufferIntegrationPlugin::tr(s, c, n));
}

//  ClientBufferIntegration
//      *QtWayland::ClientBufferIntegrationPlugin::create(const QString
//      &key, const QStringList &paramList)
extern "C" Q_DECL_EXPORT
QtWayland::ClientBufferIntegration *ritual_ZN9QtWayland29ClientBufferIntegrationPlugin6createERK7QStringRK5QListIS1_E(
    QtWayland::ClientBufferIntegrationPlugin *self,
    const QString *key,
    const QList<QString> *paramList) {
  return self->create(*key, *paramList);
}

//  QtWayland::ClientBufferIntegrationPlugin::ClientBufferIntegrationPlugin(
//      QObject *parent)
extern "C" Q_DECL_EXPORT
QtWayland::ClientBufferIntegrationPlugin *ritual_ZN9QtWayland29ClientBufferIntegrationPluginC1EP7QObject(
    QObject *parent) {
  return new CuteQtWayland_ClientBufferIntegrationPlugin(parent);
}

//  QtWayland::ClientBufferIntegrationPlugin::~ClientBufferIntegrationPlugin()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtWayland29ClientBufferIntegrationPluginD1Ev(
    QtWayland::ClientBufferIntegrationPlugin *self) {
  delete self;
}

//  a Python function taken by a CuteQtWayland_ClientBufferIntegrationPlugin,
//      for the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QtWayland_ClientBufferIntegrationPlugin(
    QtWayland::ClientBufferIntegrationPlugin *self,
    const char *key,
    void *call) {
  return static_cast<CuteQtWayland_ClientBufferIntegrationPlugin *>(self)->take(key, call);
}

#endif  // QT_CONFIG(opengl)
