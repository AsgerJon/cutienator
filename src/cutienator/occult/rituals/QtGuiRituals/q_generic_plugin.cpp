//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qgenericplugin.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qgenericplugin.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QGenericPlugin that Python can take functions over in. Every QGenericPlugin
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQGenericPluginCall0)(const void *, const QString *, const QString *, int *);
typedef bool (*CuteQGenericPluginCall1)(const void *, QEvent *, int *);
typedef bool (*CuteQGenericPluginCall2)(const void *, QObject *, QEvent *, int *);
typedef void (*CuteQGenericPluginCall3)(const void *, QTimerEvent *, int *);
typedef void (*CuteQGenericPluginCall4)(const void *, QChildEvent *, int *);
typedef void (*CuteQGenericPluginCall5)(const void *, QEvent *, int *);
typedef void (*CuteQGenericPluginCall6)(const void *, const QMetaMethod *, int *);
typedef void (*CuteQGenericPluginCall7)(const void *, const QMetaMethod *, int *);
class CuteQGenericPlugin : public QGenericPlugin {
public:
  using QGenericPlugin::QGenericPlugin;
  void *taken[8] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN14QGenericPlugin6createERK7QStringS2_")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[7] = call;
      return true;
    }
    return false;
  }

  //  QObject *QGenericPlugin::create(const QString &name, const QString
  //      &spec)
  QObject *create(const QString &name, const QString &spec) override {
    if (taken[0]) {
      int handled = 0;
      CuteQGenericPluginCall0 call = reinterpret_cast<CuteQGenericPluginCall0>(taken[0]);
      void * given = call(this, &name, &spec, &handled);
      if (handled) return static_cast<QObject *>(given);
    }
    return {};
  }

  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQGenericPluginCall1 call = reinterpret_cast<CuteQGenericPluginCall1>(taken[1]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }

  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQGenericPluginCall2 call = reinterpret_cast<CuteQGenericPluginCall2>(taken[2]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }

  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQGenericPluginCall3 call = reinterpret_cast<CuteQGenericPluginCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }

  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQGenericPluginCall4 call = reinterpret_cast<CuteQGenericPluginCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }

  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQGenericPluginCall5 call = reinterpret_cast<CuteQGenericPluginCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }

  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQGenericPluginCall6 call = reinterpret_cast<CuteQGenericPluginCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }

  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[7]) {
      int handled = 0;
      CuteQGenericPluginCall7 call = reinterpret_cast<CuteQGenericPluginCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
};

//  const QMetaObject *QGenericPlugin::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14QGenericPlugin10metaObjectEv(
    const QGenericPlugin *self) {
  return self->metaObject();
}

//  QString QGenericPlugin::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QGenericPlugin2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QGenericPlugin::tr(s, c, n));
}

//  QGenericPlugin::~QGenericPlugin()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGenericPluginD1Ev(QGenericPlugin *self) {
  delete self;
}

//  QObject *QGenericPlugin::create(const QString &name, const QString &spec)
extern "C" Q_DECL_EXPORT
QObject *ritual_ZN14QGenericPlugin6createERK7QStringS2_(
    QGenericPlugin *self,
    const QString *name,
    const QString *spec) {
  return self->create(*name, *spec);
}

//  a Python function taken by a CuteQGenericPlugin, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGenericPlugin(
    QGenericPlugin *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGenericPlugin *>(self)->take(key, call);
}
