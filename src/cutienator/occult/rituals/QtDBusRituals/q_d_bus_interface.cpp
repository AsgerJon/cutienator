//  Edited by hand on 2026-11-25: the ritual of the constructor
//  'QDBusInterface::QDBusInterface(QDBusInterfacePrivate *p)' is taken
//  out, with its row. Qt's library offers nothing by that name (the
//  linker found none). Kept as it is when the generator runs again.
//  Written by dev_tooling.RitualGenerator from the records of
//  QtDBus/qdbusinterface.h, Qt 6.12.0.
#include <QtDBus/qtdbusglobal.h>
#if !defined(QT_NO_DBUS)
#include <QtDBus/qdbusinterface.h>
#include <QtCore/qstring.h>
#include <QtDBus/qdbusconnection.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QDBusInterface that Python can take functions over in. Every QDBusInterface
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_DBUS)
typedef void (*CuteQDBusInterfaceCall0)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_DBUS)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_DBUS)
typedef void (*CuteQDBusInterfaceCall1)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_DBUS)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDBusInterfaceCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDBusInterfaceCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDBusInterfaceCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDBusInterfaceCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDBusInterfaceCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQDBusInterface : public QDBusInterface {
public:
  using QDBusInterface::QDBusInterface;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_DBUS)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_DBUS)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_DBUS)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_DBUS)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_DBUS)
  //  void QDBusAbstractInterface::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[0]) {
      int handled = 0;
      CuteQDBusInterfaceCall0 call = reinterpret_cast<CuteQDBusInterfaceCall0>(taken[0]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QDBusAbstractInterface::connectNotify(signal);
  }
#endif  // !defined(QT_NO_DBUS)
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_DBUS)
  //  void QDBusAbstractInterface::disconnectNotify(const QMetaMethod
  //      &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[1]) {
      int handled = 0;
      CuteQDBusInterfaceCall1 call = reinterpret_cast<CuteQDBusInterfaceCall1>(taken[1]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QDBusAbstractInterface::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_DBUS)
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQDBusInterfaceCall2 call = reinterpret_cast<CuteQDBusInterfaceCall2>(taken[2]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQDBusInterfaceCall3 call = reinterpret_cast<CuteQDBusInterfaceCall3>(taken[3]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQDBusInterfaceCall4 call = reinterpret_cast<CuteQDBusInterfaceCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQDBusInterfaceCall5 call = reinterpret_cast<CuteQDBusInterfaceCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQDBusInterfaceCall6 call = reinterpret_cast<CuteQDBusInterfaceCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  QDBusInterface::QDBusInterface(const QString &service, const QString
//      &path, const QString &interface, const QDBusConnection &connection,
//      QObject *parent)
extern "C" Q_DECL_EXPORT
QDBusInterface *ritual_ZN14QDBusInterfaceC1ERK7QStringS2_S2_RK15QDBusConnectionP7QObject(
    const QString *service,
    const QString *path,
    const QString *interface,
    const QDBusConnection *connection,
    QObject *parent) {
  return new CuteQDBusInterface(
      *service,
      *path,
      *interface,
      *connection,
      parent);
}

//  QDBusInterface::~QDBusInterface()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QDBusInterfaceD1Ev(QDBusInterface *self) {
  delete self;
}

//  const QMetaObject *QDBusInterface::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14QDBusInterface10metaObjectEv(
    const QDBusInterface *self) {
  return self->metaObject();
}

//  void *QDBusInterface::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN14QDBusInterface11qt_metacastEPKc(
    QDBusInterface *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  QDBusInterfacePrivate *QDBusInterface::d_func()
extern "C" Q_DECL_EXPORT
QDBusInterfacePrivate *ritual_ZN14QDBusInterface6d_funcEv(
    QDBusInterface *self) {
  return self->d_func();
}

//  const QDBusInterfacePrivate *QDBusInterface::d_func() const
extern "C" Q_DECL_EXPORT
const QDBusInterfacePrivate *ritual_ZNK14QDBusInterface6d_funcEv(
    const QDBusInterface *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQDBusInterface, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDBusInterface(
    QDBusInterface *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDBusInterface *>(self)->take(key, call);
}

#endif  // !defined(QT_NO_DBUS)
