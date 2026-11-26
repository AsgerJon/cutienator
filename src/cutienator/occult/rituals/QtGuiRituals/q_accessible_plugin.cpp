//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qaccessibleplugin.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#if QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#include <QtGui/qaccessibleplugin.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QAccessiblePlugin that Python can take functions over in. Every QAccessiblePlugin
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessiblePluginCall0)(const void *, const QString *, QObject *, int *);
#endif  // QT_CONFIG(accessibility)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAccessiblePluginCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAccessiblePluginCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAccessiblePluginCall3)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAccessiblePluginCall4)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAccessiblePluginCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAccessiblePluginCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAccessiblePluginCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQAccessiblePlugin : public QAccessiblePlugin {
public:
  using QAccessiblePlugin::QAccessiblePlugin;
  void *taken[8] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN17QAccessiblePlugin6createERK7QStringP7QObject")) {
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
  //  QAccessibleInterface *QAccessiblePlugin::create(const QString &key,
  //      QObject *object)
  QAccessibleInterface *create(
      const QString &key,
      QObject *object) override {
    if (taken[0]) {
      int handled = 0;
      CuteQAccessiblePluginCall0 call = reinterpret_cast<CuteQAccessiblePluginCall0>(taken[0]);
      void * given = call(this, &key, object, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return {};
  }
#endif  // QT_CONFIG(accessibility)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQAccessiblePluginCall1 call = reinterpret_cast<CuteQAccessiblePluginCall1>(taken[1]);
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
      CuteQAccessiblePluginCall2 call = reinterpret_cast<CuteQAccessiblePluginCall2>(taken[2]);
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
      CuteQAccessiblePluginCall3 call = reinterpret_cast<CuteQAccessiblePluginCall3>(taken[3]);
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
      CuteQAccessiblePluginCall4 call = reinterpret_cast<CuteQAccessiblePluginCall4>(taken[4]);
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
      CuteQAccessiblePluginCall5 call = reinterpret_cast<CuteQAccessiblePluginCall5>(taken[5]);
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
      CuteQAccessiblePluginCall6 call = reinterpret_cast<CuteQAccessiblePluginCall6>(taken[6]);
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
      CuteQAccessiblePluginCall7 call = reinterpret_cast<CuteQAccessiblePluginCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QAccessiblePlugin::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QAccessiblePlugin10metaObjectEv(
    const QAccessiblePlugin *self) {
  return self->metaObject();
}

//  void *QAccessiblePlugin::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN17QAccessiblePlugin11qt_metacastEPKc(
    QAccessiblePlugin *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QAccessiblePlugin::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN17QAccessiblePlugin11qt_metacallEN11QMetaObject4CallEiPPv(
    QAccessiblePlugin *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QAccessiblePlugin::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QAccessiblePlugin2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QAccessiblePlugin::tr(s, c, n));
}

//  QAccessiblePlugin::QAccessiblePlugin(QObject *parent)
extern "C" Q_DECL_EXPORT
QAccessiblePlugin *ritual_ZN17QAccessiblePluginC1EP7QObject(
    QObject *parent) {
  return new CuteQAccessiblePlugin(parent);
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

#endif  // QT_CONFIG(accessibility)
#endif  // QT_CONFIG(accessibility)
