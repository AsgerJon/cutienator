//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickControls2/6.12.0/QtQuickControls2/private/qquickstyleplugin_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtQuickControls2/QtQuickControls2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickControls2/6.12.0/QtQuickControls2/private/qquickstyleplugin_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QQuickStylePlugin that Python can take functions over in. Every QQuickStylePlugin
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef QString * (*CuteQQuickStylePluginCall0)(const void *, int *);
typedef void (*CuteQQuickStylePluginCall1)(const void *, QQuickTheme *, int *);
typedef void (*CuteQQuickStylePluginCall2)(const void *, int *);
typedef void (*CuteQQuickStylePluginCall3)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickStylePluginCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickStylePluginCall5)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickStylePluginCall6)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickStylePluginCall7)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickStylePluginCall8)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickStylePluginCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickStylePluginCall10)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickStylePlugin : public QQuickStylePlugin {
public:
  using QQuickStylePlugin::QQuickStylePlugin;
  void *taken[11] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK17QQuickStylePlugin4nameEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickStylePlugin15initializeThemeEP11QQuickTheme")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickStylePlugin11updateThemeEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QQmlExtensionPlugin15unregisterTypesEv")) {
      taken[3] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  QString QQuickStylePlugin::name() const
  QString name() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickStylePluginCall0 call = reinterpret_cast<CuteQQuickStylePluginCall0>(taken[0]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return {};
  }

  //  void QQuickStylePlugin::initializeTheme(QQuickTheme *theme)
  void initializeTheme(QQuickTheme *theme) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickStylePluginCall1 call = reinterpret_cast<CuteQQuickStylePluginCall1>(taken[1]);
      call(this, theme, &handled);
      if (handled) return;
    }
  }

  //  void QQuickStylePlugin::updateTheme()
  void updateTheme() override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickStylePluginCall2 call = reinterpret_cast<CuteQQuickStylePluginCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickStylePlugin::updateTheme();
  }

  //  void QQuickStylePlugin::unregisterTypes()
  void unregisterTypes() override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickStylePluginCall3 call = reinterpret_cast<CuteQQuickStylePluginCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickStylePlugin::unregisterTypes();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickStylePluginCall4 call = reinterpret_cast<CuteQQuickStylePluginCall4>(taken[4]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickStylePluginCall5 call = reinterpret_cast<CuteQQuickStylePluginCall5>(taken[5]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickStylePluginCall6 call = reinterpret_cast<CuteQQuickStylePluginCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickStylePluginCall7 call = reinterpret_cast<CuteQQuickStylePluginCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickStylePluginCall8 call = reinterpret_cast<CuteQQuickStylePluginCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickStylePluginCall9 call = reinterpret_cast<CuteQQuickStylePluginCall9>(taken[9]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickStylePluginCall10 call = reinterpret_cast<CuteQQuickStylePluginCall10>(taken[10]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickStylePlugin::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QQuickStylePlugin10metaObjectEv(
    const QQuickStylePlugin *self) {
  return self->metaObject();
}

//  void *QQuickStylePlugin::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN17QQuickStylePlugin11qt_metacastEPKc(
    QQuickStylePlugin *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickStylePlugin::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN17QQuickStylePlugin11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickStylePlugin *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickStylePlugin::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QQuickStylePlugin2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickStylePlugin::tr(s, c, n));
}

//  QQuickStylePlugin::QQuickStylePlugin(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickStylePlugin *ritual_ZN17QQuickStylePluginC1EP7QObject(
    QObject *parent) {
  return new CuteQQuickStylePlugin(parent);
}

//  QQuickStylePlugin::~QQuickStylePlugin()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickStylePluginD1Ev(QQuickStylePlugin *self) {
  delete self;
}

//  QString QQuickStylePlugin::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QQuickStylePlugin4nameEv(
    const QQuickStylePlugin *self) {
  return new QString(self->name());
}

//  void QQuickStylePlugin::initializeTheme(QQuickTheme *theme)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickStylePlugin15initializeThemeEP11QQuickTheme(
    QQuickStylePlugin *self,
    QQuickTheme *theme) {
  self->initializeTheme(theme);
}

//  void QQuickStylePlugin::updateTheme()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickStylePlugin11updateThemeEv(QQuickStylePlugin *self) {
  self->updateTheme();
}

//  void QQuickStylePlugin::registerTypes(const char *uri)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickStylePlugin13registerTypesEPKc(
    QQuickStylePlugin *self,
    const char *uri) {
  self->registerTypes(uri);
}

//  void QQuickStylePlugin::unregisterTypes()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickStylePlugin15unregisterTypesEv(
    QQuickStylePlugin *self) {
  self->unregisterTypes();
}

//  QQuickTheme *QQuickStylePlugin::createTheme(const QString &name)
extern "C" Q_DECL_EXPORT
QQuickTheme *ritual_ZN17QQuickStylePlugin11createThemeERK7QString(
    QQuickStylePlugin *self,
    const QString *name) {
  return self->createTheme(*name);
}

//  a Python function taken by a CuteQQuickStylePlugin, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickStylePlugin(
    QQuickStylePlugin *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickStylePlugin *>(self)->take(key, call);
}

//  void QQuickStylePlugin::updateTheme()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQuickStylePlugin11updateThemeEv(
    QQuickStylePlugin *self) {
  self->QQuickStylePlugin::updateTheme();
}

//  void QQuickStylePlugin::unregisterTypes()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQuickStylePlugin15unregisterTypesEv(
    QQuickStylePlugin *self) {
  self->QQuickStylePlugin::unregisterTypes();
}
