//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/qqmlextensionplugin.h, Qt 6.12.0. Changes made here are lost.
#include <QtQml/QtQml>
#include <QtQml/qqmlextensionplugin.h>
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QQmlExtensionPlugin that Python can take functions over in. Every QQmlExtensionPlugin
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQmlExtensionPluginCall0)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlExtensionPluginCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlExtensionPluginCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlExtensionPluginCall3)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlExtensionPluginCall4)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlExtensionPluginCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlExtensionPluginCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlExtensionPluginCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQmlExtensionPlugin : public QQmlExtensionPlugin {
public:
  using QQmlExtensionPlugin::QQmlExtensionPlugin;
  void *taken[8] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN19QQmlExtensionPlugin15unregisterTypesEv")) {
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

  //  void QQmlExtensionPlugin::unregisterTypes()
  void unregisterTypes() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQmlExtensionPluginCall0 call = reinterpret_cast<CuteQQmlExtensionPluginCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlExtensionPlugin::unregisterTypes();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQmlExtensionPluginCall1 call = reinterpret_cast<CuteQQmlExtensionPluginCall1>(taken[1]);
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
      CuteQQmlExtensionPluginCall2 call = reinterpret_cast<CuteQQmlExtensionPluginCall2>(taken[2]);
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
      CuteQQmlExtensionPluginCall3 call = reinterpret_cast<CuteQQmlExtensionPluginCall3>(taken[3]);
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
      CuteQQmlExtensionPluginCall4 call = reinterpret_cast<CuteQQmlExtensionPluginCall4>(taken[4]);
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
      CuteQQmlExtensionPluginCall5 call = reinterpret_cast<CuteQQmlExtensionPluginCall5>(taken[5]);
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
      CuteQQmlExtensionPluginCall6 call = reinterpret_cast<CuteQQmlExtensionPluginCall6>(taken[6]);
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
      CuteQQmlExtensionPluginCall7 call = reinterpret_cast<CuteQQmlExtensionPluginCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQmlExtensionPlugin::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19QQmlExtensionPlugin10metaObjectEv(
    const QQmlExtensionPlugin *self) {
  return self->metaObject();
}

//  QString QQmlExtensionPlugin::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19QQmlExtensionPlugin2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQmlExtensionPlugin::tr(s, c, n));
}

//  QQmlExtensionPluginPrivate *QQmlExtensionPlugin::d_func()
extern "C" Q_DECL_EXPORT
QQmlExtensionPluginPrivate *ritual_ZN19QQmlExtensionPlugin6d_funcEv(
    QQmlExtensionPlugin *self) {
  return self->d_func();
}

//  const QQmlExtensionPluginPrivate *QQmlExtensionPlugin::d_func() const
extern "C" Q_DECL_EXPORT
const QQmlExtensionPluginPrivate *ritual_ZNK19QQmlExtensionPlugin6d_funcEv(
    const QQmlExtensionPlugin *self) {
  return self->d_func();
}

//  QQmlExtensionPlugin::~QQmlExtensionPlugin()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlExtensionPluginD1Ev(QQmlExtensionPlugin *self) {
  delete self;
}

#if QT_DEPRECATED_SINCE(6, 3)
//  QUrl QQmlExtensionPlugin::baseUrl() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK19QQmlExtensionPlugin7baseUrlEv(
    const QQmlExtensionPlugin *self) {
  return new QUrl(self->baseUrl());
}
#endif  // QT_DEPRECATED_SINCE(6, 3)

//  void QQmlExtensionPlugin::registerTypes(const char *uri)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlExtensionPlugin13registerTypesEPKc(
    QQmlExtensionPlugin *self,
    const char *uri) {
  self->registerTypes(uri);
}

//  void QQmlExtensionPlugin::unregisterTypes()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlExtensionPlugin15unregisterTypesEv(
    QQmlExtensionPlugin *self) {
  self->unregisterTypes();
}

//  void QQmlExtensionPlugin::initializeEngine(QQmlEngine *engine, const char
//      *uri)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlExtensionPlugin16initializeEngineEP10QQmlEnginePKc(
    QQmlExtensionPlugin *self,
    QQmlEngine *engine,
    const char *uri) {
  self->initializeEngine(engine, uri);
}

//  QQmlExtensionPlugin as the QQmlExtensionInterface it is built on
extern "C" Q_DECL_EXPORT
QQmlExtensionInterface *ritual_cast_QQmlExtensionPlugin_QQmlExtensionInterface(
    QQmlExtensionPlugin *self) {
  return static_cast<QQmlExtensionInterface *>(self);
}

//  a Python function taken by a CuteQQmlExtensionPlugin, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlExtensionPlugin(
    QQmlExtensionPlugin *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlExtensionPlugin *>(self)->take(key, call);
}

//  void QQmlExtensionPlugin::unregisterTypes()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlExtensionPlugin15unregisterTypesEv(
    QQmlExtensionPlugin *self) {
  self->QQmlExtensionPlugin::unregisterTypes();
}
