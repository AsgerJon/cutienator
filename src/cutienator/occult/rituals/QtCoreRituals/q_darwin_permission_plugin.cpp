//  Written by hand on 2026-11-25 from
//  QtCore/6.12.0/QtCore/private/qdarwinpermissionplugin_p.h, Qt 6.12.0, as the Qt of
//  macOS installs it. Kept as it is when the generator runs again.
//  A 'QDarwinPermissionHandler *', which plain C++ sees as a
//  class of that name, is passed as an address. Not written:
//  'requestPermission' and 'permissionUpdated', which take a
//  'PermissionCallback', a 'std::function'.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if defined(Q_OS_DARWIN) && QT_CONFIG(permissions)
#include <QtCore/6.12.0/QtCore/private/qdarwinpermissionplugin_p.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qpermissions.h>
#include <QtCore/qstring.h>
#include <cstring>

//  A QDarwinPermissionPlugin that Python can take functions over in. Every
//  QDarwinPermissionPlugin Python makes is one. Each function below asks the
//  Python function handed over for it, and runs Qt's own without
//  one.
typedef int (*CuteQDarwinPermissionPluginCall0)(const void *, const QPermission *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDarwinPermissionPluginCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDarwinPermissionPluginCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDarwinPermissionPluginCall3)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDarwinPermissionPluginCall4)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDarwinPermissionPluginCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDarwinPermissionPluginCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDarwinPermissionPluginCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQDarwinPermissionPlugin : public QDarwinPermissionPlugin {
public:
  using QDarwinPermissionPlugin::QDarwinPermissionPlugin;
  void *taken[8] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN17QPermissionPlugin15checkPermissionERK11QPermission")) {
      taken[0] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  Qt::PermissionStatus QDarwinPermissionPlugin::checkPermission(const
  //      QPermission &permission)
  Qt::PermissionStatus checkPermission(const QPermission &permission) override {
    if (taken[0]) {
      int handled = 0;
      CuteQDarwinPermissionPluginCall0 call = reinterpret_cast<CuteQDarwinPermissionPluginCall0>(taken[0]);
      int given = call(this, &permission, &handled);
      if (handled) return static_cast<Qt::PermissionStatus>(given);
    }
    return QDarwinPermissionPlugin::checkPermission(permission);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQDarwinPermissionPluginCall1 call = reinterpret_cast<CuteQDarwinPermissionPluginCall1>(taken[1]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQDarwinPermissionPluginCall2 call = reinterpret_cast<CuteQDarwinPermissionPluginCall2>(taken[2]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQDarwinPermissionPluginCall3 call = reinterpret_cast<CuteQDarwinPermissionPluginCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQDarwinPermissionPluginCall4 call = reinterpret_cast<CuteQDarwinPermissionPluginCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQDarwinPermissionPluginCall5 call = reinterpret_cast<CuteQDarwinPermissionPluginCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQDarwinPermissionPluginCall6 call = reinterpret_cast<CuteQDarwinPermissionPluginCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[7]) {
      int handled = 0;
      CuteQDarwinPermissionPluginCall7 call = reinterpret_cast<CuteQDarwinPermissionPluginCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QDarwinPermissionPlugin::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK23QDarwinPermissionPlugin10metaObjectEv(
    const QDarwinPermissionPlugin *self) {
  return self->metaObject();
}

//  QString QDarwinPermissionPlugin::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN23QDarwinPermissionPlugin2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QDarwinPermissionPlugin::tr(s, c, n));
}

//  QDarwinPermissionPlugin::QDarwinPermissionPlugin(QDarwinPermissionHandler
//      *handler)
extern "C" Q_DECL_EXPORT
QDarwinPermissionPlugin *ritual_ZN23QDarwinPermissionPluginC1EP24QDarwinPermissionHandler(
    QDarwinPermissionHandler *handler) {
  return new CuteQDarwinPermissionPlugin(handler);
}

//  QDarwinPermissionPlugin::~QDarwinPermissionPlugin()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QDarwinPermissionPluginD1Ev(QDarwinPermissionPlugin *self) {
  delete self;
}

//  Qt::PermissionStatus QDarwinPermissionPlugin::checkPermission(const
//      QPermission &permission)
extern "C" Q_DECL_EXPORT
Qt::PermissionStatus ritual_ZN23QDarwinPermissionPlugin15checkPermissionERK11QPermission(
    QDarwinPermissionPlugin *self,
    const QPermission *permission) {
  return self->checkPermission(*permission);
}

//  bool QDarwinPermissionPlugin::verifyUsageDescriptions(const QPermission
//      &permission)
extern "C" Q_DECL_EXPORT
bool ritual_ZN23QDarwinPermissionPlugin23verifyUsageDescriptionsERK11QPermission(
    QDarwinPermissionPlugin *self,
    const QPermission *permission) {
  return self->verifyUsageDescriptions(*permission);
}

//  a Python function taken by a CuteQDarwinPermissionPlugin, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDarwinPermissionPlugin(
    QDarwinPermissionPlugin *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDarwinPermissionPlugin *>(self)->take(key, call);
}

//  Qt::PermissionStatus QDarwinPermissionPlugin::checkPermission(const
//      QPermission &permission)
extern "C" Q_DECL_EXPORT
Qt::PermissionStatus ritual_own_ZN23QDarwinPermissionPlugin15checkPermissionERK11QPermission(
    QDarwinPermissionPlugin *self,
    const QPermission *permission) {
  return self->QDarwinPermissionPlugin::checkPermission(*permission);
}

#endif  // defined(Q_OS_DARWIN) && QT_CONFIG(permissions)
