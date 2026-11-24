//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/qqmlextensionplugin.h, Qt 6.12.0. Changes made here are lost.
#include <QtQml/QtQml>
#include <QtQml/qqmlextensionplugin.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QQmlEngineExtensionPlugin that Python can take functions over in. Every QQmlEngineExtensionPlugin
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlEngineExtensionPluginCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlEngineExtensionPluginCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlEngineExtensionPluginCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlEngineExtensionPluginCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlEngineExtensionPluginCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlEngineExtensionPluginCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlEngineExtensionPluginCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQmlEngineExtensionPlugin : public QQmlEngineExtensionPlugin {
public:
  using QQmlEngineExtensionPlugin::QQmlEngineExtensionPlugin;
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
      CuteQQmlEngineExtensionPluginCall0 call = reinterpret_cast<CuteQQmlEngineExtensionPluginCall0>(taken[0]);
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
      CuteQQmlEngineExtensionPluginCall1 call = reinterpret_cast<CuteQQmlEngineExtensionPluginCall1>(taken[1]);
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
      CuteQQmlEngineExtensionPluginCall2 call = reinterpret_cast<CuteQQmlEngineExtensionPluginCall2>(taken[2]);
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
      CuteQQmlEngineExtensionPluginCall3 call = reinterpret_cast<CuteQQmlEngineExtensionPluginCall3>(taken[3]);
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
      CuteQQmlEngineExtensionPluginCall4 call = reinterpret_cast<CuteQQmlEngineExtensionPluginCall4>(taken[4]);
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
      CuteQQmlEngineExtensionPluginCall5 call = reinterpret_cast<CuteQQmlEngineExtensionPluginCall5>(taken[5]);
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
      CuteQQmlEngineExtensionPluginCall6 call = reinterpret_cast<CuteQQmlEngineExtensionPluginCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQmlEngineExtensionPlugin::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK25QQmlEngineExtensionPlugin10metaObjectEv(
    const QQmlEngineExtensionPlugin *self) {
  return self->metaObject();
}

//  QString QQmlEngineExtensionPlugin::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN25QQmlEngineExtensionPlugin2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQmlEngineExtensionPlugin::tr(s, c, n));
}

//  QQmlEngineExtensionPlugin::QQmlEngineExtensionPlugin(QObject *parent)
extern "C" Q_DECL_EXPORT
QQmlEngineExtensionPlugin *ritual_ZN25QQmlEngineExtensionPluginC1EP7QObject(
    QObject *parent) {
  return new CuteQQmlEngineExtensionPlugin(parent);
}

//  QQmlEngineExtensionPlugin::~QQmlEngineExtensionPlugin()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQmlEngineExtensionPluginD1Ev(
    QQmlEngineExtensionPlugin *self) {
  delete self;
}

//  void QQmlEngineExtensionPlugin::initializeEngine(QQmlEngine *engine,
//      const char *uri)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQmlEngineExtensionPlugin16initializeEngineEP10QQmlEnginePKc(
    QQmlEngineExtensionPlugin *self,
    QQmlEngine *engine,
    const char *uri) {
  self->initializeEngine(engine, uri);
}

//  QQmlEngineExtensionPlugin as the QQmlEngineExtensionInterface it is built
//      on
extern "C" Q_DECL_EXPORT
QQmlEngineExtensionInterface *ritual_cast_QQmlEngineExtensionPlugin_QQmlEngineExtensionInterface(
    QQmlEngineExtensionPlugin *self) {
  return static_cast<QQmlEngineExtensionInterface *>(self);
}

//  a Python function taken by a CuteQQmlEngineExtensionPlugin, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlEngineExtensionPlugin(
    QQmlEngineExtensionPlugin *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlEngineExtensionPlugin *>(self)->take(key, call);
}
