//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/qpa/qplatformintegrationplugin.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qplatformintegrationplugin.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QPlatformIntegrationPlugin that Python can take functions over in. Every QPlatformIntegrationPlugin
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPlatformIntegrationPluginCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPlatformIntegrationPluginCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlatformIntegrationPluginCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlatformIntegrationPluginCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlatformIntegrationPluginCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlatformIntegrationPluginCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlatformIntegrationPluginCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQPlatformIntegrationPlugin : public QPlatformIntegrationPlugin {
public:
  using QPlatformIntegrationPlugin::QPlatformIntegrationPlugin;
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
      CuteQPlatformIntegrationPluginCall0 call = reinterpret_cast<CuteQPlatformIntegrationPluginCall0>(taken[0]);
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
      CuteQPlatformIntegrationPluginCall1 call = reinterpret_cast<CuteQPlatformIntegrationPluginCall1>(taken[1]);
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
      CuteQPlatformIntegrationPluginCall2 call = reinterpret_cast<CuteQPlatformIntegrationPluginCall2>(taken[2]);
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
      CuteQPlatformIntegrationPluginCall3 call = reinterpret_cast<CuteQPlatformIntegrationPluginCall3>(taken[3]);
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
      CuteQPlatformIntegrationPluginCall4 call = reinterpret_cast<CuteQPlatformIntegrationPluginCall4>(taken[4]);
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
      CuteQPlatformIntegrationPluginCall5 call = reinterpret_cast<CuteQPlatformIntegrationPluginCall5>(taken[5]);
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
      CuteQPlatformIntegrationPluginCall6 call = reinterpret_cast<CuteQPlatformIntegrationPluginCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QPlatformIntegrationPlugin::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK26QPlatformIntegrationPlugin10metaObjectEv(
    const QPlatformIntegrationPlugin *self) {
  return self->metaObject();
}

//  void *QPlatformIntegrationPlugin::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN26QPlatformIntegrationPlugin11qt_metacastEPKc(
    QPlatformIntegrationPlugin *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QPlatformIntegrationPlugin::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN26QPlatformIntegrationPlugin11qt_metacallEN11QMetaObject4CallEiPPv(
    QPlatformIntegrationPlugin *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QPlatformIntegrationPlugin::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN26QPlatformIntegrationPlugin2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QPlatformIntegrationPlugin::tr(s, c, n));
}

//  QPlatformIntegrationPlugin::QPlatformIntegrationPlugin(QObject *parent)
extern "C" Q_DECL_EXPORT
QPlatformIntegrationPlugin *ritual_ZN26QPlatformIntegrationPluginC1EP7QObject(
    QObject *parent) {
  return new CuteQPlatformIntegrationPlugin(parent);
}

//  QPlatformIntegrationPlugin::~QPlatformIntegrationPlugin()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QPlatformIntegrationPluginD1Ev(
    QPlatformIntegrationPlugin *self) {
  delete self;
}

//  QPlatformIntegration *QPlatformIntegrationPlugin::create(const QString
//      &key, const QStringList &paramList)
extern "C" Q_DECL_EXPORT
QPlatformIntegration *ritual_ZN26QPlatformIntegrationPlugin6createERK7QStringRK5QListIS0_E(
    QPlatformIntegrationPlugin *self,
    const QString *key,
    const QList<QString> *paramList) {
  return self->create(*key, *paramList);
}

//  QPlatformIntegration *QPlatformIntegrationPlugin::create(const QString
//      &key, const QStringList &paramList, int &argc, char **argv)
extern "C" Q_DECL_EXPORT
QPlatformIntegration *ritual_ZN26QPlatformIntegrationPlugin6createERK7QStringRK5QListIS0_ERiPPc(
    QPlatformIntegrationPlugin *self,
    const QString *key,
    const QList<QString> *paramList,
    int *argc,
    char **argv) {
  return self->create(*key, *paramList, *argc, argv);
}

//  a Python function taken by a CuteQPlatformIntegrationPlugin, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPlatformIntegrationPlugin(
    QPlatformIntegrationPlugin *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPlatformIntegrationPlugin *>(self)->take(key, call);
}
