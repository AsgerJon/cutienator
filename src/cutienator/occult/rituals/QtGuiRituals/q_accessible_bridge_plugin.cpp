//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qaccessiblebridge.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#if QT_CONFIG(accessibility)
#include <QtGui/qaccessiblebridge.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QAccessibleBridgePlugin that Python can take functions over in. Every QAccessibleBridgePlugin
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleBridgePluginCall0)(const void *, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAccessibleBridgePluginCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAccessibleBridgePluginCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAccessibleBridgePluginCall3)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAccessibleBridgePluginCall4)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAccessibleBridgePluginCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAccessibleBridgePluginCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAccessibleBridgePluginCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQAccessibleBridgePlugin : public QAccessibleBridgePlugin {
public:
  using QAccessibleBridgePlugin::QAccessibleBridgePlugin;
  void *taken[8] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN23QAccessibleBridgePlugin6createERK7QString")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
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

#if QT_CONFIG(accessibility)
  //  QAccessibleBridge *QAccessibleBridgePlugin::create(const QString
  //      &key)
  QAccessibleBridge *create(const QString &key) override {
    if (taken[0]) {
      int handled = 0;
      CuteQAccessibleBridgePluginCall0 call = reinterpret_cast<CuteQAccessibleBridgePluginCall0>(taken[0]);
      void * given = call(this, &key, &handled);
      if (handled) return static_cast<QAccessibleBridge *>(given);
    }
    return {};
  }
#endif  // QT_CONFIG(accessibility)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQAccessibleBridgePluginCall1 call = reinterpret_cast<CuteQAccessibleBridgePluginCall1>(taken[1]);
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
      CuteQAccessibleBridgePluginCall2 call = reinterpret_cast<CuteQAccessibleBridgePluginCall2>(taken[2]);
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
      CuteQAccessibleBridgePluginCall3 call = reinterpret_cast<CuteQAccessibleBridgePluginCall3>(taken[3]);
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
      CuteQAccessibleBridgePluginCall4 call = reinterpret_cast<CuteQAccessibleBridgePluginCall4>(taken[4]);
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
      CuteQAccessibleBridgePluginCall5 call = reinterpret_cast<CuteQAccessibleBridgePluginCall5>(taken[5]);
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
      CuteQAccessibleBridgePluginCall6 call = reinterpret_cast<CuteQAccessibleBridgePluginCall6>(taken[6]);
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
      CuteQAccessibleBridgePluginCall7 call = reinterpret_cast<CuteQAccessibleBridgePluginCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QAccessibleBridgePlugin::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK23QAccessibleBridgePlugin10metaObjectEv(
    const QAccessibleBridgePlugin *self) {
  return self->metaObject();
}

//  QString QAccessibleBridgePlugin::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN23QAccessibleBridgePlugin2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QAccessibleBridgePlugin::tr(s, c, n));
}

//  QAccessibleBridgePlugin::~QAccessibleBridgePlugin()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QAccessibleBridgePluginD1Ev(QAccessibleBridgePlugin *self) {
  delete self;
}

//  QAccessibleBridge *QAccessibleBridgePlugin::create(const QString &key)
extern "C" Q_DECL_EXPORT
QAccessibleBridge *ritual_ZN23QAccessibleBridgePlugin6createERK7QString(
    QAccessibleBridgePlugin *self,
    const QString *key) {
  return self->create(*key);
}

//  a Python function taken by a CuteQAccessibleBridgePlugin, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAccessibleBridgePlugin(
    QAccessibleBridgePlugin *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAccessibleBridgePlugin *>(self)->take(key, call);
}

#endif  // QT_CONFIG(accessibility)
