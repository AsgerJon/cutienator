//  Written by dev_tooling.RitualGenerator from the records of
//  QtDBus/qdbusvirtualobject.h, Qt 6.12.0. Changes made here are lost.
#include <QtDBus/qtdbusglobal.h>
#if !defined(QT_NO_DBUS)
#include <QtDBus/qdbusvirtualobject.h>
#include <QtCore/qstring.h>
#include <QtDBus/qdbusmessage.h>
#include <QtDBus/qdbusconnection.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QDBusVirtualObject that Python can take functions over in. Every QDBusVirtualObject
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_DBUS)
typedef QString * (*CuteQDBusVirtualObjectCall0)(const void *, const QString *, int *);
#endif  // !defined(QT_NO_DBUS)
#if !defined(QT_NO_DBUS)
typedef bool (*CuteQDBusVirtualObjectCall1)(const void *, const QDBusMessage *, const QDBusConnection *, int *);
#endif  // !defined(QT_NO_DBUS)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDBusVirtualObjectCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDBusVirtualObjectCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDBusVirtualObjectCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDBusVirtualObjectCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDBusVirtualObjectCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDBusVirtualObjectCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDBusVirtualObjectCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQDBusVirtualObject : public QDBusVirtualObject {
public:
  using QDBusVirtualObject::QDBusVirtualObject;
  void *taken[9] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_DBUS)
    if (!std::strcmp(key, "_ZNK18QDBusVirtualObject10introspectERK7QString")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_DBUS)
#if !defined(QT_NO_DBUS)
    if (!std::strcmp(key, "_ZN18QDBusVirtualObject13handleMessageERK12QDBusMessageRK15QDBusConnection")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_DBUS)
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
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !defined(QT_NO_DBUS)
  //  QString QDBusVirtualObject::introspect(const QString &path) const
  QString introspect(const QString &path) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQDBusVirtualObjectCall0 call = reinterpret_cast<CuteQDBusVirtualObjectCall0>(taken[0]);
      QString * given = call(this, &path, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return {};
  }
#endif  // !defined(QT_NO_DBUS)

#if !defined(QT_NO_DBUS)
  //  bool QDBusVirtualObject::handleMessage(const QDBusMessage &message,
  //      const QDBusConnection &connection)
  bool handleMessage(
      const QDBusMessage &message,
      const QDBusConnection &connection) override {
    if (taken[1]) {
      int handled = 0;
      CuteQDBusVirtualObjectCall1 call = reinterpret_cast<CuteQDBusVirtualObjectCall1>(taken[1]);
      bool given = call(this, &message, &connection, &handled);
      if (handled) return given;
    }
    return {};
  }
#endif  // !defined(QT_NO_DBUS)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQDBusVirtualObjectCall2 call = reinterpret_cast<CuteQDBusVirtualObjectCall2>(taken[2]);
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
      CuteQDBusVirtualObjectCall3 call = reinterpret_cast<CuteQDBusVirtualObjectCall3>(taken[3]);
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
      CuteQDBusVirtualObjectCall4 call = reinterpret_cast<CuteQDBusVirtualObjectCall4>(taken[4]);
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
      CuteQDBusVirtualObjectCall5 call = reinterpret_cast<CuteQDBusVirtualObjectCall5>(taken[5]);
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
      CuteQDBusVirtualObjectCall6 call = reinterpret_cast<CuteQDBusVirtualObjectCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[7]) {
      int handled = 0;
      CuteQDBusVirtualObjectCall7 call = reinterpret_cast<CuteQDBusVirtualObjectCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[8]) {
      int handled = 0;
      CuteQDBusVirtualObjectCall8 call = reinterpret_cast<CuteQDBusVirtualObjectCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QDBusVirtualObject::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QDBusVirtualObject10metaObjectEv(
    const QDBusVirtualObject *self) {
  return self->metaObject();
}

//  QString QDBusVirtualObject::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QDBusVirtualObject2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QDBusVirtualObject::tr(s, c, n));
}

//  QDBusVirtualObject::~QDBusVirtualObject()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QDBusVirtualObjectD1Ev(QDBusVirtualObject *self) {
  delete self;
}

//  QString QDBusVirtualObject::introspect(const QString &path) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QDBusVirtualObject10introspectERK7QString(
    const QDBusVirtualObject *self,
    const QString *path) {
  return new QString(self->introspect(*path));
}

//  bool QDBusVirtualObject::handleMessage(const QDBusMessage &message, const
//      QDBusConnection &connection)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QDBusVirtualObject13handleMessageERK12QDBusMessageRK15QDBusConnection(
    QDBusVirtualObject *self,
    const QDBusMessage *message,
    const QDBusConnection *connection) {
  return self->handleMessage(*message, *connection);
}

//  a Python function taken by a CuteQDBusVirtualObject, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDBusVirtualObject(
    QDBusVirtualObject *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDBusVirtualObject *>(self)->take(key, call);
}

#endif  // !defined(QT_NO_DBUS)
