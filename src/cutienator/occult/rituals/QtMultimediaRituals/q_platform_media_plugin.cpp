//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/6.12.0/QtMultimedia/private/qplatformmediaplugin_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#include <QtMultimedia/QtMultimedia>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/6.12.0/QtMultimedia/private/qplatformmediaplugin_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QPlatformMediaPlugin that Python can take functions over in. Every QPlatformMediaPlugin
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQPlatformMediaPluginCall0)(const void *, const QString *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPlatformMediaPluginCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPlatformMediaPluginCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlatformMediaPluginCall3)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlatformMediaPluginCall4)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlatformMediaPluginCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlatformMediaPluginCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlatformMediaPluginCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQPlatformMediaPlugin : public QPlatformMediaPlugin {
public:
  using QPlatformMediaPlugin::QPlatformMediaPlugin;
  void *taken[8] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN20QPlatformMediaPlugin6createERK7QString")) {
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

  //  QPlatformMediaIntegration *QPlatformMediaPlugin::create(const QString
  //      &key)
  QPlatformMediaIntegration *create(const QString &key) override {
    if (taken[0]) {
      int handled = 0;
      CuteQPlatformMediaPluginCall0 call = reinterpret_cast<CuteQPlatformMediaPluginCall0>(taken[0]);
      void * given = call(this, &key, &handled);
      if (handled) return static_cast<QPlatformMediaIntegration *>(given);
    }
    return {};
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQPlatformMediaPluginCall1 call = reinterpret_cast<CuteQPlatformMediaPluginCall1>(taken[1]);
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
      CuteQPlatformMediaPluginCall2 call = reinterpret_cast<CuteQPlatformMediaPluginCall2>(taken[2]);
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
      CuteQPlatformMediaPluginCall3 call = reinterpret_cast<CuteQPlatformMediaPluginCall3>(taken[3]);
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
      CuteQPlatformMediaPluginCall4 call = reinterpret_cast<CuteQPlatformMediaPluginCall4>(taken[4]);
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
      CuteQPlatformMediaPluginCall5 call = reinterpret_cast<CuteQPlatformMediaPluginCall5>(taken[5]);
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
      CuteQPlatformMediaPluginCall6 call = reinterpret_cast<CuteQPlatformMediaPluginCall6>(taken[6]);
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
      CuteQPlatformMediaPluginCall7 call = reinterpret_cast<CuteQPlatformMediaPluginCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QPlatformMediaPlugin::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20QPlatformMediaPlugin10metaObjectEv(
    const QPlatformMediaPlugin *self) {
  return self->metaObject();
}

//  QString QPlatformMediaPlugin::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN20QPlatformMediaPlugin2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QPlatformMediaPlugin::tr(s, c, n));
}

//  QPlatformMediaPlugin::~QPlatformMediaPlugin()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QPlatformMediaPluginD1Ev(QPlatformMediaPlugin *self) {
  delete self;
}

//  QPlatformMediaIntegration *QPlatformMediaPlugin::create(const QString
//      &key)
extern "C" Q_DECL_EXPORT
QPlatformMediaIntegration *ritual_ZN20QPlatformMediaPlugin6createERK7QString(
    QPlatformMediaPlugin *self,
    const QString *key) {
  return self->create(*key);
}

//  a Python function taken by a CuteQPlatformMediaPlugin, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPlatformMediaPlugin(
    QPlatformMediaPlugin *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPlatformMediaPlugin *>(self)->take(key, call);
}
