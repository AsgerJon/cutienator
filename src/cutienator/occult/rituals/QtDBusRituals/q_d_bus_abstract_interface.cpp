//  Written by dev_tooling.RitualGenerator from the records of
//  QtDBus/qdbusabstractinterface.h, Qt 6.12.0. Changes made here are lost.
#include <QtDBus/qtdbusglobal.h>
#if !defined(QT_NO_DBUS)
#include <QtDBus/qdbusabstractinterface.h>
#include <QtCore/qstring.h>
#include <QtDBus/qdbusconnection.h>
#include <QtDBus/qdbuserror.h>
#include <QtDBus/qdbusmessage.h>
#include <QtCore/qvariant.h>
#include <QtDBus/qdbuspendingcall.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  Only a class built on QDBusAbstractInterface may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQDBusAbstractInterface : QDBusAbstractInterface {
  using QDBusAbstractInterface::connectNotify;
  using QDBusAbstractInterface::disconnectNotify;
};

//  A QDBusAbstractInterface that Python can take functions over in. Every QDBusAbstractInterface
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_DBUS)
typedef void (*CuteQDBusAbstractInterfaceCall0)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_DBUS)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_DBUS)
typedef void (*CuteQDBusAbstractInterfaceCall1)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_DBUS)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDBusAbstractInterfaceCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDBusAbstractInterfaceCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDBusAbstractInterfaceCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDBusAbstractInterfaceCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDBusAbstractInterfaceCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQDBusAbstractInterface : public QDBusAbstractInterface {
public:
  using QDBusAbstractInterface::QDBusAbstractInterface;
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
      CuteQDBusAbstractInterfaceCall0 call = reinterpret_cast<CuteQDBusAbstractInterfaceCall0>(taken[0]);
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
      CuteQDBusAbstractInterfaceCall1 call = reinterpret_cast<CuteQDBusAbstractInterfaceCall1>(taken[1]);
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
      CuteQDBusAbstractInterfaceCall2 call = reinterpret_cast<CuteQDBusAbstractInterfaceCall2>(taken[2]);
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
      CuteQDBusAbstractInterfaceCall3 call = reinterpret_cast<CuteQDBusAbstractInterfaceCall3>(taken[3]);
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
      CuteQDBusAbstractInterfaceCall4 call = reinterpret_cast<CuteQDBusAbstractInterfaceCall4>(taken[4]);
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
      CuteQDBusAbstractInterfaceCall5 call = reinterpret_cast<CuteQDBusAbstractInterfaceCall5>(taken[5]);
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
      CuteQDBusAbstractInterfaceCall6 call = reinterpret_cast<CuteQDBusAbstractInterfaceCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QDBusAbstractInterface::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK22QDBusAbstractInterface10metaObjectEv(
    const QDBusAbstractInterface *self) {
  return self->metaObject();
}

//  void *QDBusAbstractInterface::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN22QDBusAbstractInterface11qt_metacastEPKc(
    QDBusAbstractInterface *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QDBusAbstractInterface::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN22QDBusAbstractInterface11qt_metacallEN11QMetaObject4CallEiPPv(
    QDBusAbstractInterface *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QDBusAbstractInterface::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN22QDBusAbstractInterface2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QDBusAbstractInterface::tr(s, c, n));
}

//  QDBusAbstractInterface::~QDBusAbstractInterface()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QDBusAbstractInterfaceD1Ev(QDBusAbstractInterface *self) {
  delete self;
}

//  bool QDBusAbstractInterface::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QDBusAbstractInterface7isValidEv(
    const QDBusAbstractInterface *self) {
  return self->isValid();
}

//  QDBusConnection QDBusAbstractInterface::connection() const
extern "C" Q_DECL_EXPORT
QDBusConnection *ritual_ZNK22QDBusAbstractInterface10connectionEv(
    const QDBusAbstractInterface *self) {
  return new QDBusConnection(self->connection());
}

//  QString QDBusAbstractInterface::service() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK22QDBusAbstractInterface7serviceEv(
    const QDBusAbstractInterface *self) {
  return new QString(self->service());
}

//  QString QDBusAbstractInterface::path() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK22QDBusAbstractInterface4pathEv(
    const QDBusAbstractInterface *self) {
  return new QString(self->path());
}

//  QString QDBusAbstractInterface::interface() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK22QDBusAbstractInterface9interfaceEv(
    const QDBusAbstractInterface *self) {
  return new QString(self->interface());
}

//  QDBusError QDBusAbstractInterface::lastError() const
extern "C" Q_DECL_EXPORT
QDBusError *ritual_ZNK22QDBusAbstractInterface9lastErrorEv(
    const QDBusAbstractInterface *self) {
  return new QDBusError(self->lastError());
}

//  void QDBusAbstractInterface::setTimeout(int timeout)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QDBusAbstractInterface10setTimeoutEi(
    QDBusAbstractInterface *self,
    int timeout) {
  self->setTimeout(timeout);
}

//  int QDBusAbstractInterface::timeout() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK22QDBusAbstractInterface7timeoutEv(
    const QDBusAbstractInterface *self) {
  return self->timeout();
}

//  void QDBusAbstractInterface::setInteractiveAuthorizationAllowed(bool
//      enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QDBusAbstractInterface34setInteractiveAuthorizationAllowedEb(
    QDBusAbstractInterface *self,
    bool enable) {
  self->setInteractiveAuthorizationAllowed(enable);
}

//  bool QDBusAbstractInterface::isInteractiveAuthorizationAllowed() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QDBusAbstractInterface33isInteractiveAuthorizationAllowedEv(
    const QDBusAbstractInterface *self) {
  return self->isInteractiveAuthorizationAllowed();
}

//  QDBusMessage QDBusAbstractInterface::call(const QString &method)
extern "C" Q_DECL_EXPORT
QDBusMessage *ritual_ZN22QDBusAbstractInterface4callERK7QString(
    QDBusAbstractInterface *self,
    const QString *method) {
  return new QDBusMessage(self->call(*method));
}

//  QDBusMessage QDBusAbstractInterface::call(QDBus::CallMode mode, const
//      QString &method)
extern "C" Q_DECL_EXPORT
QDBusMessage *ritual_ZN22QDBusAbstractInterface4callEN5QDBus8CallModeERK7QString(
    QDBusAbstractInterface *self,
    QDBus::CallMode mode,
    const QString *method) {
  return new QDBusMessage(self->call(mode, *method));
}

//  QDBusMessage QDBusAbstractInterface::callWithArgumentList(QDBus::CallMode
//      mode, const QString &method, const QList<QVariant> &args)
extern "C" Q_DECL_EXPORT
QDBusMessage *ritual_ZN22QDBusAbstractInterface20callWithArgumentListEN5QDBus8CallModeERK7QStringRK5QListI8QVariantE(
    QDBusAbstractInterface *self,
    QDBus::CallMode mode,
    const QString *method,
    const QList<QVariant> *args) {
  return new QDBusMessage(self->callWithArgumentList(mode, *method, *args));
}

//  bool QDBusAbstractInterface::callWithCallback(const QString &method,
//      const QList<QVariant> &args, QObject *receiver, const char *member,
//      const char *errorSlot)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QDBusAbstractInterface16callWithCallbackERK7QStringRK5QListI8QVariantEP7QObjectPKcSB_(
    QDBusAbstractInterface *self,
    const QString *method,
    const QList<QVariant> *args,
    QObject *receiver,
    const char *member,
    const char *errorSlot) {
  return self->callWithCallback(*method, *args, receiver, member, errorSlot);
}

//  bool QDBusAbstractInterface::callWithCallback(const QString &method,
//      const QList<QVariant> &args, QObject *receiver, const char *member)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QDBusAbstractInterface16callWithCallbackERK7QStringRK5QListI8QVariantEP7QObjectPKc(
    QDBusAbstractInterface *self,
    const QString *method,
    const QList<QVariant> *args,
    QObject *receiver,
    const char *member) {
  return self->callWithCallback(*method, *args, receiver, member);
}

//  QDBusPendingCall QDBusAbstractInterface::asyncCall(const QString &method)
extern "C" Q_DECL_EXPORT
QDBusPendingCall *ritual_ZN22QDBusAbstractInterface9asyncCallERK7QString(
    QDBusAbstractInterface *self,
    const QString *method) {
  return new QDBusPendingCall(self->asyncCall(*method));
}

//  QDBusPendingCall QDBusAbstractInterface::asyncCallWithArgumentList(const
//      QString &method, const QList<QVariant> &args)
extern "C" Q_DECL_EXPORT
QDBusPendingCall *ritual_ZN22QDBusAbstractInterface25asyncCallWithArgumentListERK7QStringRK5QListI8QVariantE(
    QDBusAbstractInterface *self,
    const QString *method,
    const QList<QVariant> *args) {
  return new QDBusPendingCall(
      self->asyncCallWithArgumentList(
          *method,
          *args));
}

//  QDBusAbstractInterface::QDBusAbstractInterface(const QString &service,
//      const QString &path, const char *interface, const QDBusConnection
//      &connection, QObject *parent)
extern "C" Q_DECL_EXPORT
QDBusAbstractInterface *ritual_ZN22QDBusAbstractInterfaceC1ERK7QStringS2_PKcRK15QDBusConnectionP7QObject(
    const QString *service,
    const QString *path,
    const char *interface,
    const QDBusConnection *connection,
    QObject *parent) {
  return new CuteQDBusAbstractInterface(
      *service,
      *path,
      interface,
      *connection,
      parent);
}

//  QDBusAbstractInterface::QDBusAbstractInterface(QDBusAbstractInterfacePriv
//      ate &a0, QObject *parent)
extern "C" Q_DECL_EXPORT
QDBusAbstractInterface *ritual_ZN22QDBusAbstractInterfaceC1ER29QDBusAbstractInterfacePrivateP7QObject(
    QDBusAbstractInterfacePrivate *a0,
    QObject *parent) {
  return new CuteQDBusAbstractInterface(*a0, parent);
}

//  void QDBusAbstractInterface::connectNotify(const QMetaMethod &signal)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QDBusAbstractInterface13connectNotifyERK11QMetaMethod(
    QDBusAbstractInterface *self,
    const QMetaMethod *signal) {
  self->connectNotify(*signal);
}

//  void QDBusAbstractInterface::disconnectNotify(const QMetaMethod &signal)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QDBusAbstractInterface16disconnectNotifyERK11QMetaMethod(
    QDBusAbstractInterface *self,
    const QMetaMethod *signal) {
  self->disconnectNotify(*signal);
}

//  QVariant QDBusAbstractInterface::internalPropGet(const char *propname)
//      const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK22QDBusAbstractInterface15internalPropGetEPKc(
    const QDBusAbstractInterface *self,
    const char *propname) {
  return new QVariant(self->internalPropGet(propname));
}

//  void QDBusAbstractInterface::internalPropSet(const char *propname, const
//      QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QDBusAbstractInterface15internalPropSetEPKcRK8QVariant(
    QDBusAbstractInterface *self,
    const char *propname,
    const QVariant *value) {
  self->internalPropSet(propname, *value);
}

//  QDBusMessage QDBusAbstractInterface::internalConstCall(QDBus::CallMode
//      mode, const QString &method, const QList<QVariant> &args) const
extern "C" Q_DECL_EXPORT
QDBusMessage *ritual_ZNK22QDBusAbstractInterface17internalConstCallEN5QDBus8CallModeERK7QStringRK5QListI8QVariantE(
    const QDBusAbstractInterface *self,
    QDBus::CallMode mode,
    const QString *method,
    const QList<QVariant> *args) {
  return new QDBusMessage(self->internalConstCall(mode, *method, *args));
}

//  QDBusMessage QDBusAbstractInterface::doCall(QDBus::CallMode mode, const
//      QString &method, const QVariant *args, size_t numArgs)
extern "C" Q_DECL_EXPORT
QDBusMessage *ritual_ZN22QDBusAbstractInterface6doCallEN5QDBus8CallModeERK7QStringPK8QVariantm(
    QDBusAbstractInterface *self,
    QDBus::CallMode mode,
    const QString *method,
    const QVariant *args,
    size_t numArgs) {
  return new QDBusMessage(self->doCall(mode, *method, args, numArgs));
}

//  QDBusPendingCall QDBusAbstractInterface::doAsyncCall(const QString
//      &method, const QVariant *args, size_t numArgs)
extern "C" Q_DECL_EXPORT
QDBusPendingCall *ritual_ZN22QDBusAbstractInterface11doAsyncCallERK7QStringPK8QVariantm(
    QDBusAbstractInterface *self,
    const QString *method,
    const QVariant *args,
    size_t numArgs) {
  return new QDBusPendingCall(self->doAsyncCall(*method, args, numArgs));
}

//  QDBusAbstractInterfacePrivate *QDBusAbstractInterface::d_func()
extern "C" Q_DECL_EXPORT
QDBusAbstractInterfacePrivate *ritual_ZN22QDBusAbstractInterface6d_funcEv(
    QDBusAbstractInterface *self) {
  return self->d_func();
}

//  const QDBusAbstractInterfacePrivate *QDBusAbstractInterface::d_func()
//      const
extern "C" Q_DECL_EXPORT
const QDBusAbstractInterfacePrivate *ritual_ZNK22QDBusAbstractInterface6d_funcEv(
    const QDBusAbstractInterface *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQDBusAbstractInterface, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDBusAbstractInterface(
    QDBusAbstractInterface *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDBusAbstractInterface *>(self)->take(key, call);
}

//  void QDBusAbstractInterface::connectNotify(const QMetaMethod &signal)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QDBusAbstractInterface13connectNotifyERK11QMetaMethod(
    QDBusAbstractInterface *self,
    const QMetaMethod *signal) {
  static_cast<OwnQDBusAbstractInterface *>(self)->OwnQDBusAbstractInterface::connectNotify(
      *signal);
}

//  void QDBusAbstractInterface::disconnectNotify(const QMetaMethod &signal)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QDBusAbstractInterface16disconnectNotifyERK11QMetaMethod(
    QDBusAbstractInterface *self,
    const QMetaMethod *signal) {
  static_cast<OwnQDBusAbstractInterface *>(self)->OwnQDBusAbstractInterface::disconnectNotify(
      *signal);
}

#endif  // !defined(QT_NO_DBUS)
