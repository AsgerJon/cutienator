//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qaccessibleplugin.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qaccessibleplugin.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QAccessiblePlugin that Python can take functions over in. Every QAccessiblePlugin
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQAccessiblePluginCall0)(const void *, QEvent *, int *);
typedef bool (*CuteQAccessiblePluginCall1)(const void *, QObject *, QEvent *, int *);
typedef void (*CuteQAccessiblePluginCall2)(const void *, QTimerEvent *, int *);
typedef void (*CuteQAccessiblePluginCall3)(const void *, QChildEvent *, int *);
typedef void (*CuteQAccessiblePluginCall4)(const void *, QEvent *, int *);
typedef void (*CuteQAccessiblePluginCall5)(const void *, const QMetaMethod *, int *);
typedef void (*CuteQAccessiblePluginCall6)(const void *, const QMetaMethod *, int *);
class CuteQAccessiblePlugin : public QAccessiblePlugin {
public:
  using QAccessiblePlugin::QAccessiblePlugin;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
    return false;
  }

  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQAccessiblePluginCall0 call = reinterpret_cast<CuteQAccessiblePluginCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }

  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQAccessiblePluginCall1 call = reinterpret_cast<CuteQAccessiblePluginCall1>(taken[1]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }

  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQAccessiblePluginCall2 call = reinterpret_cast<CuteQAccessiblePluginCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }

  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQAccessiblePluginCall3 call = reinterpret_cast<CuteQAccessiblePluginCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }

  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQAccessiblePluginCall4 call = reinterpret_cast<CuteQAccessiblePluginCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }

  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteQAccessiblePluginCall5 call = reinterpret_cast<CuteQAccessiblePluginCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }

  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQAccessiblePluginCall6 call = reinterpret_cast<CuteQAccessiblePluginCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
};

//  const QMetaObject *QAccessiblePlugin::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QAccessiblePlugin10metaObjectEv(
    const QAccessiblePlugin *self) {
  return self->metaObject();
}

//  QString QAccessiblePlugin::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QAccessiblePlugin2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QAccessiblePlugin::tr(s, c, n));
}

//  QAccessiblePlugin::~QAccessiblePlugin()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAccessiblePluginD1Ev(QAccessiblePlugin *self) {
  delete self;
}

//  QAccessibleInterface *QAccessiblePlugin::create(const QString &key,
//      QObject *object)
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_ZN17QAccessiblePlugin6createERK7QStringP7QObject(
    QAccessiblePlugin *self,
    const QString *key,
    QObject *object) {
  return self->create(*key, object);
}

//  a Python function taken by a CuteQAccessiblePlugin, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAccessiblePlugin(
    QAccessiblePlugin *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAccessiblePlugin *>(self)->take(key, call);
}
