//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qiconengineplugin.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qiconengineplugin.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QIconEnginePlugin that Python can take functions over in. Every QIconEnginePlugin
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQIconEnginePluginCall0)(const void *, QEvent *, int *);
typedef bool (*CuteQIconEnginePluginCall1)(const void *, QObject *, QEvent *, int *);
typedef void (*CuteQIconEnginePluginCall2)(const void *, QTimerEvent *, int *);
typedef void (*CuteQIconEnginePluginCall3)(const void *, QChildEvent *, int *);
typedef void (*CuteQIconEnginePluginCall4)(const void *, QEvent *, int *);
typedef void (*CuteQIconEnginePluginCall5)(const void *, const QMetaMethod *, int *);
typedef void (*CuteQIconEnginePluginCall6)(const void *, const QMetaMethod *, int *);
class CuteQIconEnginePlugin : public QIconEnginePlugin {
public:
  using QIconEnginePlugin::QIconEnginePlugin;
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
      CuteQIconEnginePluginCall0 call = reinterpret_cast<CuteQIconEnginePluginCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }

  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQIconEnginePluginCall1 call = reinterpret_cast<CuteQIconEnginePluginCall1>(taken[1]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }

  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQIconEnginePluginCall2 call = reinterpret_cast<CuteQIconEnginePluginCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }

  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQIconEnginePluginCall3 call = reinterpret_cast<CuteQIconEnginePluginCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }

  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQIconEnginePluginCall4 call = reinterpret_cast<CuteQIconEnginePluginCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }

  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteQIconEnginePluginCall5 call = reinterpret_cast<CuteQIconEnginePluginCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }

  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQIconEnginePluginCall6 call = reinterpret_cast<CuteQIconEnginePluginCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
};

//  const QMetaObject *QIconEnginePlugin::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QIconEnginePlugin10metaObjectEv(
    const QIconEnginePlugin *self) {
  return self->metaObject();
}

//  QString QIconEnginePlugin::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QIconEnginePlugin2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QIconEnginePlugin::tr(s, c, n));
}

//  QIconEnginePlugin::~QIconEnginePlugin()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QIconEnginePluginD1Ev(QIconEnginePlugin *self) {
  delete self;
}

//  QIconEngine *QIconEnginePlugin::create(const QString &filename)
extern "C" Q_DECL_EXPORT
QIconEngine *ritual_ZN17QIconEnginePlugin6createERK7QString(
    QIconEnginePlugin *self,
    const QString *filename) {
  return self->create(*filename);
}

//  a Python function taken by a CuteQIconEnginePlugin, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QIconEnginePlugin(
    QIconEnginePlugin *self,
    const char *key,
    void *call) {
  return static_cast<CuteQIconEnginePlugin *>(self)->take(key, call);
}
