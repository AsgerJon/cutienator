//  Written by dev_tooling.RitualGenerator from the records of
//  QtDBus/qdbusabstractadaptor.h, Qt 6.12.0. Changes made here are lost.
#include <QtDBus/qtdbusglobal.h>
#if !defined(QT_NO_DBUS)
#include <QtDBus/qdbusabstractadaptor.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QDBusAbstractAdaptor that Python can take functions over in. Every QDBusAbstractAdaptor
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDBusAbstractAdaptorCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDBusAbstractAdaptorCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDBusAbstractAdaptorCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDBusAbstractAdaptorCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDBusAbstractAdaptorCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDBusAbstractAdaptorCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDBusAbstractAdaptorCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQDBusAbstractAdaptor : public QDBusAbstractAdaptor {
public:
  using QDBusAbstractAdaptor::QDBusAbstractAdaptor;
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
      CuteQDBusAbstractAdaptorCall0 call = reinterpret_cast<CuteQDBusAbstractAdaptorCall0>(taken[0]);
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
      CuteQDBusAbstractAdaptorCall1 call = reinterpret_cast<CuteQDBusAbstractAdaptorCall1>(taken[1]);
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
      CuteQDBusAbstractAdaptorCall2 call = reinterpret_cast<CuteQDBusAbstractAdaptorCall2>(taken[2]);
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
      CuteQDBusAbstractAdaptorCall3 call = reinterpret_cast<CuteQDBusAbstractAdaptorCall3>(taken[3]);
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
      CuteQDBusAbstractAdaptorCall4 call = reinterpret_cast<CuteQDBusAbstractAdaptorCall4>(taken[4]);
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
      CuteQDBusAbstractAdaptorCall5 call = reinterpret_cast<CuteQDBusAbstractAdaptorCall5>(taken[5]);
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
      CuteQDBusAbstractAdaptorCall6 call = reinterpret_cast<CuteQDBusAbstractAdaptorCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QDBusAbstractAdaptor::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20QDBusAbstractAdaptor10metaObjectEv(
    const QDBusAbstractAdaptor *self) {
  return self->metaObject();
}

//  QString QDBusAbstractAdaptor::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN20QDBusAbstractAdaptor2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QDBusAbstractAdaptor::tr(s, c, n));
}

//  QDBusAbstractAdaptor::QDBusAbstractAdaptor(QObject *parent)
extern "C" Q_DECL_EXPORT
QDBusAbstractAdaptor *ritual_ZN20QDBusAbstractAdaptorC1EP7QObject(
    QObject *parent) {
  return new CuteQDBusAbstractAdaptor(parent);
}

//  QDBusAbstractAdaptor::~QDBusAbstractAdaptor()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QDBusAbstractAdaptorD1Ev(QDBusAbstractAdaptor *self) {
  delete self;
}

//  void QDBusAbstractAdaptor::setAutoRelaySignals(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QDBusAbstractAdaptor19setAutoRelaySignalsEb(
    QDBusAbstractAdaptor *self,
    bool enable) {
  self->setAutoRelaySignals(enable);
}

//  bool QDBusAbstractAdaptor::autoRelaySignals() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QDBusAbstractAdaptor16autoRelaySignalsEv(
    const QDBusAbstractAdaptor *self) {
  return self->autoRelaySignals();
}

//  QDBusAbstractAdaptorPrivate *QDBusAbstractAdaptor::d_func()
extern "C" Q_DECL_EXPORT
QDBusAbstractAdaptorPrivate *ritual_ZN20QDBusAbstractAdaptor6d_funcEv(
    QDBusAbstractAdaptor *self) {
  return self->d_func();
}

//  const QDBusAbstractAdaptorPrivate *QDBusAbstractAdaptor::d_func() const
extern "C" Q_DECL_EXPORT
const QDBusAbstractAdaptorPrivate *ritual_ZNK20QDBusAbstractAdaptor6d_funcEv(
    const QDBusAbstractAdaptor *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQDBusAbstractAdaptor, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDBusAbstractAdaptor(
    QDBusAbstractAdaptor *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDBusAbstractAdaptor *>(self)->take(key, call);
}

#endif  // !defined(QT_NO_DBUS)
