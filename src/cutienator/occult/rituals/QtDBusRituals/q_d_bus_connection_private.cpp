//  Written by dev_tooling.RitualGenerator from the records of
//  QtDBus/6.12.0/QtDBus/private/qdbusconnection_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtDBus/qtdbusglobal.h>
#include <QtDBus/6.12.0/QtDBus/private/qtdbusglobal_p.h>
#if !defined(QT_NO_DBUS)
#if !defined(QT_BOOTSTRAPPED)
#include <QtDBus/6.12.0/QtDBus/private/qtdbusglobal_p.h>
#include <QtDBus/QtDBus>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDBus/6.12.0/QtDBus/private/qdbusconnection_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtDBus/qdbusconnection.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qdbusintegrator_p.h"
#include <qcoreapplication.h>
#include <qelapsedtimer.h>
#include <private/qlatch_p.h>
#include <qloggingcategory.h>
#include <qmetaobject.h>
#include <qobject.h>
#include <qsocketnotifier.h>
#include <qstringlist.h>
#include <qthread.h>
#include <private/qlocking_p.h>
#include <QtCore/qset.h>
#include "qdbusargument.h"
#include "qdbusconnection_p.h"
#include "qdbusconnectionmanager_p.h"
#include "qdbusinterface_p.h"
#include "qdbusmessage.h"
#include "qdbusmetatype.h"
#include "qdbusmetatype_p.h"
#include "qdbusabstractadaptor.h"
#include "qdbusabstractadaptor_p.h"
#include "qdbusserver.h"
#include "qdbusutil_p.h"
#include "qdbusvirtualobject.h"
#include "qdbusmessage_p.h"
#include "qdbuscontext_p.h"
#include "qdbuspendingcall_p.h"
#include "qdbusthreaddebug_p.h"
#include <algorithm>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/dbus/qdbusintegrator.cpp, line 2536, as _ZN22QDBusConnectionPrivate18shouldWatchServiceERK7QString
#if !defined(QT_NO_DBUS)
inline bool QDBusConnectionPrivate::shouldWatchService(const QString &service)
{
    // we don't have to watch anything in peer mode
    if (mode != ClientMode)
        return false;
    // we don't have to watch wildcard services (empty strings)
    if (service.isEmpty())
        return false;
    // we don't have to watch the bus driver
    if (service == QDBusUtil::dbusService())
        return false;
    return true;
}
#endif  // !defined(QT_NO_DBUS)

//  from src/dbus/qdbusintegrator.cpp, line 2680, as _ZN22QDBusConnectionPrivate15registerServiceERK7QString
#if !defined(QT_NO_DBUS)
inline void QDBusConnectionPrivate::registerService(const QString &serviceName)
{
    QDBusWriteLocker locker(RegisterServiceAction, this);
    registerServiceNoLock(serviceName);
}
#endif  // !defined(QT_NO_DBUS)

//  from src/dbus/qdbusintegrator.cpp, line 2691, as _ZN22QDBusConnectionPrivate17unregisterServiceERK7QString
#if !defined(QT_NO_DBUS)
inline void QDBusConnectionPrivate::unregisterService(const QString &serviceName)
{
    QDBusWriteLocker locker(UnregisterServiceAction, this);
    unregisterServiceNoLock(serviceName);
}
#endif  // !defined(QT_NO_DBUS)

//  from src/dbus/qdbusintegrator.cpp, line 2713, as _ZN22QDBusConnectionPrivate17postEventToThreadEiP7QObjectP6QEvent
#if !defined(QT_NO_DBUS)
inline void QDBusConnectionPrivate::postEventToThread(int action, QObject *object, QEvent *ev)
{
    QDBusLockerBase::reportThreadAction(action, QDBusLockerBase::BeforePost, this);
    QCoreApplication::postEvent(object, ev);
    QDBusLockerBase::reportThreadAction(action, QDBusLockerBase::AfterPost, this);
}
#endif  // !defined(QT_NO_DBUS)

//  from src/dbus/qdbusintegrator.cpp, line 2702, as _ZN22QDBusConnectionPrivate27isServiceRegisteredByThreadERK7QString
#if !defined(QT_NO_DBUS)
inline bool QDBusConnectionPrivate::isServiceRegisteredByThread(const QString &serviceName)
{
    if (!serviceName.isEmpty() && serviceName == baseService)
        return true;
    if (serviceName == QDBusUtil::dbusService())
        return false;

    QDBusReadLocker locker(UnregisterServiceAction, this);
    return serviceNames.contains(serviceName);
}
#endif  // !defined(QT_NO_DBUS)

//  from src/dbus/qdbusintegrator.cpp, line 1179, as _ZN22QDBusConnectionPrivate10timerEventEP11QTimerEvent
#if !defined(QT_NO_DBUS)
inline void QDBusConnectionPrivate::timerEvent(QTimerEvent *e)
{
    {
        DBusTimeout *timeout = timeouts.value(e->timerId(), nullptr);
        if (timeout)
            q_dbus_timeout_handle(timeout);
    }

    doDispatch();
}
#endif  // !defined(QT_NO_DBUS)

//  from src/dbus/qdbusintegrator.cpp, line 2686, as _ZN22QDBusConnectionPrivate21registerServiceNoLockERK7QString
#if !defined(QT_NO_DBUS)
inline void QDBusConnectionPrivate::registerServiceNoLock(const QString &serviceName)
{
    serviceNames.append(serviceName);
}
#endif  // !defined(QT_NO_DBUS)

//  from src/dbus/qdbusintegrator.cpp, line 2697, as _ZN22QDBusConnectionPrivate23unregisterServiceNoLockERK7QString
#if !defined(QT_NO_DBUS)
inline void QDBusConnectionPrivate::unregisterServiceNoLock(const QString &serviceName)
{
    serviceNames.removeAll(serviceName);
}
#endif  // !defined(QT_NO_DBUS)
//  -----------------------------------------------------------------------

//  A QDBusConnectionPrivate that Python can take functions over in. Every QDBusConnectionPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_DBUS)
#if !defined(QT_BOOTSTRAPPED)
typedef void (*CuteQDBusConnectionPrivateCall0)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_BOOTSTRAPPED)
#endif  // !defined(QT_NO_DBUS)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDBusConnectionPrivateCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDBusConnectionPrivateCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDBusConnectionPrivateCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDBusConnectionPrivateCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDBusConnectionPrivateCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDBusConnectionPrivateCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQDBusConnectionPrivate : public QDBusConnectionPrivate {
public:
  using QDBusConnectionPrivate::QDBusConnectionPrivate;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_DBUS)
#if !defined(QT_BOOTSTRAPPED)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_BOOTSTRAPPED)
#endif  // !defined(QT_NO_DBUS)
#endif  // !defined(QT_NO_QOBJECT)
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
#if !defined(QT_NO_DBUS)
#if !defined(QT_BOOTSTRAPPED)
  //  void QDBusConnectionPrivate::timerEvent(QTimerEvent *e)
  void timerEvent(QTimerEvent *e) override {
    if (taken[0]) {
      int handled = 0;
      CuteQDBusConnectionPrivateCall0 call = reinterpret_cast<CuteQDBusConnectionPrivateCall0>(taken[0]);
      call(this, e, &handled);
      if (handled) return;
    }
    QDBusConnectionPrivate::timerEvent(e);
  }
#endif  // !defined(QT_BOOTSTRAPPED)
#endif  // !defined(QT_NO_DBUS)
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQDBusConnectionPrivateCall1 call = reinterpret_cast<CuteQDBusConnectionPrivateCall1>(taken[1]);
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
      CuteQDBusConnectionPrivateCall2 call = reinterpret_cast<CuteQDBusConnectionPrivateCall2>(taken[2]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQDBusConnectionPrivateCall3 call = reinterpret_cast<CuteQDBusConnectionPrivateCall3>(taken[3]);
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
      CuteQDBusConnectionPrivateCall4 call = reinterpret_cast<CuteQDBusConnectionPrivateCall4>(taken[4]);
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
      CuteQDBusConnectionPrivateCall5 call = reinterpret_cast<CuteQDBusConnectionPrivateCall5>(taken[5]);
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
      CuteQDBusConnectionPrivateCall6 call = reinterpret_cast<CuteQDBusConnectionPrivateCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QDBusConnectionPrivate::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK22QDBusConnectionPrivate10metaObjectEv(
    const QDBusConnectionPrivate *self) {
  return self->metaObject();
}

#if !defined(QT_NO_DBUS)
//  bool QDBusConnectionPrivate::shouldWatchService(const QString &service)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QDBusConnectionPrivate18shouldWatchServiceERK7QString(
    QDBusConnectionPrivate *self,
    const QString *service) {
  return self->shouldWatchService(*service);
}
#endif  // !defined(QT_NO_DBUS)

#if !defined(QT_NO_DBUS)
//  void QDBusConnectionPrivate::registerService(const QString &serviceName)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QDBusConnectionPrivate15registerServiceERK7QString(
    QDBusConnectionPrivate *self,
    const QString *serviceName) {
  self->registerService(*serviceName);
}
#endif  // !defined(QT_NO_DBUS)

#if !defined(QT_NO_DBUS)
//  void QDBusConnectionPrivate::unregisterService(const QString
//      &serviceName)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QDBusConnectionPrivate17unregisterServiceERK7QString(
    QDBusConnectionPrivate *self,
    const QString *serviceName) {
  self->unregisterService(*serviceName);
}
#endif  // !defined(QT_NO_DBUS)

#if !defined(QT_NO_DBUS)
//  void QDBusConnectionPrivate::postEventToThread(int action, QObject
//      *target, QEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QDBusConnectionPrivate17postEventToThreadEiP7QObjectP6QEvent(
    QDBusConnectionPrivate *self,
    int action,
    QObject *target,
    QEvent *event) {
  self->postEventToThread(action, target, event);
}
#endif  // !defined(QT_NO_DBUS)

#if !defined(QT_NO_DBUS)
//  bool QDBusConnectionPrivate::isServiceRegisteredByThread(const QString
//      &serviceName)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QDBusConnectionPrivate27isServiceRegisteredByThreadERK7QString(
    QDBusConnectionPrivate *self,
    const QString *serviceName) {
  return self->isServiceRegisteredByThread(*serviceName);
}
#endif  // !defined(QT_NO_DBUS)

//  void QDBusConnectionPrivate::timerEvent(QTimerEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QDBusConnectionPrivate10timerEventEP11QTimerEvent(
    QDBusConnectionPrivate *self,
    QTimerEvent *e) {
  self->timerEvent(e);
}

#if !defined(QT_NO_DBUS)
//  void QDBusConnectionPrivate::registerServiceNoLock(const QString
//      &serviceName)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QDBusConnectionPrivate21registerServiceNoLockERK7QString(
    QDBusConnectionPrivate *self,
    const QString *serviceName) {
  self->registerServiceNoLock(*serviceName);
}
#endif  // !defined(QT_NO_DBUS)

#if !defined(QT_NO_DBUS)
//  void QDBusConnectionPrivate::unregisterServiceNoLock(const QString
//      &serviceName)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QDBusConnectionPrivate23unregisterServiceNoLockERK7QString(
    QDBusConnectionPrivate *self,
    const QString *serviceName) {
  self->unregisterServiceNoLock(*serviceName);
}
#endif  // !defined(QT_NO_DBUS)

//  QDBusConnection::ConnectionCapabilities
//      QDBusConnectionPrivate::connectionCapabilities() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK22QDBusConnectionPrivate22connectionCapabilitiesEv(
    const QDBusConnectionPrivate *self) {
  return static_cast<int>(self->connectionCapabilities().toInt());
}

//  QDBusConnectionPrivate *QDBusConnectionPrivate::d(const QDBusConnection
//      &q)
extern "C" Q_DECL_EXPORT
QDBusConnectionPrivate *ritual_ZN22QDBusConnectionPrivate1dERK15QDBusConnection(
    const QDBusConnection *q) {
  return QDBusConnectionPrivate::d(*q);
}

//  QDBusConnection QDBusConnectionPrivate::q(QDBusConnectionPrivate
//      *connection)
extern "C" Q_DECL_EXPORT
QDBusConnection *ritual_ZN22QDBusConnectionPrivate1qEPS_(
    QDBusConnectionPrivate *connection) {
  return new QDBusConnection(QDBusConnectionPrivate::q(connection));
}

//  a Python function taken by a CuteQDBusConnectionPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDBusConnectionPrivate(
    QDBusConnectionPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDBusConnectionPrivate *>(self)->take(key, call);
}

#endif  // !defined(QT_BOOTSTRAPPED)
#endif  // !defined(QT_NO_DBUS)
