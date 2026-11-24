//  Written by dev_tooling.RitualGenerator from the records of
//  QtDBus/6.12.0/QtDBus/private/qdbusconnectionmanager_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtDBus/qtdbusglobal.h>
#include <QtDBus/6.12.0/QtDBus/private/qtdbusglobal_p.h>
#if !defined(QT_NO_DBUS)
#include <QtDBus/6.12.0/QtDBus/private/qtdbusglobal_p.h>
#include <QtDBus/QtDBus>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDBus/6.12.0/QtDBus/private/qdbusconnectionmanager_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDBus/private/qdbusconnectionmanager_p.h>
#include <QtCore/qcoreapplication.h>
#include <QtCore/qthread.h>
#include <QtCore/qstringlist.h>
#include <QtCore/private/qlocking_p.h>
#include <QtDBus/qdbuserror.h>
#include <QtDBus/private/qdbuspendingcall_p.h>
#include <QtDBus/private/qdbusmetatype_p.h>
#ifndef QT_NO_DBUS
#ifdef Q_OS_WIN
#  include <QtCore/qt_windows.h>
#endif
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/dbus/qdbusconnectionmanager.cpp, line 115, as _ZN22QDBusConnectionManagerD1Ev
#if !defined(QT_NO_DBUS)
inline QDBusConnectionManager::~QDBusConnectionManager()
{
    quit();
    wait();
}
#endif  // !defined(QT_NO_DBUS)

//  from src/dbus/qdbusconnectionmanager.cpp, line 54, as _ZNK22QDBusConnectionManager18existingConnectionERK7QString
#if !defined(QT_NO_DBUS)
inline QDBusConnectionPrivate *QDBusConnectionManager::existingConnection(const QString &name) const
{
    const auto locker = qt_scoped_lock(mutex);
    auto *conn = connection(name);
    if (conn)
        conn->ref.ref();
    return conn;
}
#endif  // !defined(QT_NO_DBUS)

//  from src/dbus/qdbusconnectionmanager.cpp, line 77, as _ZN22QDBusConnectionManager17removeConnectionsERK5QListI7QStringE
#if !defined(QT_NO_DBUS)
inline void QDBusConnectionManager::removeConnections(const QStringList &names)
{
    const auto locker = qt_scoped_lock(mutex);

    for (const auto &name : names)
        removeConnection(name);
}
#endif  // !defined(QT_NO_DBUS)

//  from src/dbus/qdbusconnectionmanager.cpp, line 85, as _ZN22QDBusConnectionManager14disconnectFromERK7QStringN22QDBusConnectionPrivate14ConnectionModeE
#if !defined(QT_NO_DBUS)
inline void QDBusConnectionManager::disconnectFrom(const QString &name,
                                            QDBusConnectionPrivate::ConnectionMode mode)
{
    const auto locker = qt_scoped_lock(mutex);

    QDBusConnectionPrivate *d = connection(name);
    if (d && d->mode != mode)
        return;
    removeConnection(name);
}
#endif  // !defined(QT_NO_DBUS)

//  from src/dbus/qdbusconnectionmanager.cpp, line 137, as _ZN22QDBusConnectionManager13addConnectionERK7QStringP22QDBusConnectionPrivate
#if !defined(QT_NO_DBUS)
inline void QDBusConnectionManager::addConnection(const QString &name, QDBusConnectionPrivate *c)
{
    const auto locker = qt_scoped_lock(mutex);
    setConnection(name, c);
}
#endif  // !defined(QT_NO_DBUS)

//  from src/dbus/qdbusconnectionmanager.cpp, line 143, as _ZN22QDBusConnectionManager3runEv
#if !defined(QT_NO_DBUS)
inline void QDBusConnectionManager::run()
{
    exec();

    // cleanup:
    const auto locker = qt_scoped_lock(mutex);
    for (QDBusConnectionPrivate *d : std::as_const(connectionHash)) {
        if (!d->ref.deref()) {
            delete d;
        } else {
            d->closeConnection();
            d->moveToThread(nullptr);     // allow it to be deleted in another thread
        }
    }
    connectionHash.clear();

    // allow deletion from any thread without warning
    moveToThread(nullptr);
}
#endif  // !defined(QT_NO_DBUS)

//  from src/dbus/qdbusconnectionmanager.cpp, line 49, as _ZNK22QDBusConnectionManager10connectionERK7QString
#if !defined(QT_NO_DBUS)
inline QDBusConnectionPrivate *QDBusConnectionManager::connection(const QString &name) const
{
    return connectionHash.value(name, nullptr);
}
#endif  // !defined(QT_NO_DBUS)

//  from src/dbus/qdbusconnectionmanager.cpp, line 63, as _ZN22QDBusConnectionManager16removeConnectionERK7QString
#if !defined(QT_NO_DBUS)
inline void QDBusConnectionManager::removeConnection(const QString &name)
{
    QDBusConnectionPrivate *d = nullptr;
    d = connectionHash.take(name);
    if (d && !d->ref.deref())
        d->deleteLater();

    // Static objects may be keeping the connection open.
    // However, it is harmless to have outstanding references to a connection that is
    // closing as long as those references will be soon dropped without being used.

    // ### Output a warning if connections are being used after they have been removed.
}
#endif  // !defined(QT_NO_DBUS)

//  from src/dbus/qdbusconnectionmanager.cpp, line 131, as _ZN22QDBusConnectionManager13setConnectionERK7QStringP22QDBusConnectionPrivate
#if !defined(QT_NO_DBUS)
inline void QDBusConnectionManager::setConnection(const QString &name, QDBusConnectionPrivate *c)
{
    connectionHash[name] = c;
    c->name = name;
}
#endif  // !defined(QT_NO_DBUS)
//  -----------------------------------------------------------------------

//  A QDBusConnectionManager that Python can take functions over in. Every QDBusConnectionManager
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_DBUS)
typedef void (*CuteQDBusConnectionManagerCall0)(const void *, int *);
#endif  // !defined(QT_NO_DBUS)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDBusConnectionManagerCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDBusConnectionManagerCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDBusConnectionManagerCall3)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDBusConnectionManagerCall4)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDBusConnectionManagerCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDBusConnectionManagerCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDBusConnectionManagerCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQDBusConnectionManager : public QDBusConnectionManager {
public:
  using QDBusConnectionManager::QDBusConnectionManager;
  void *taken[8] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_DBUS)
    if (!std::strcmp(key, "_ZN7QThread3runEv")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_DBUS)
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

#if !defined(QT_NO_DBUS)
  //  void QDBusConnectionManager::run()
  void run() override {
    if (taken[0]) {
      int handled = 0;
      CuteQDBusConnectionManagerCall0 call = reinterpret_cast<CuteQDBusConnectionManagerCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QDBusConnectionManager::run();
  }
#endif  // !defined(QT_NO_DBUS)

#if !defined(QT_NO_QOBJECT)
  //  bool QThread::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQDBusConnectionManagerCall1 call = reinterpret_cast<CuteQDBusConnectionManagerCall1>(taken[1]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QThread::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQDBusConnectionManagerCall2 call = reinterpret_cast<CuteQDBusConnectionManagerCall2>(taken[2]);
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
      CuteQDBusConnectionManagerCall3 call = reinterpret_cast<CuteQDBusConnectionManagerCall3>(taken[3]);
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
      CuteQDBusConnectionManagerCall4 call = reinterpret_cast<CuteQDBusConnectionManagerCall4>(taken[4]);
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
      CuteQDBusConnectionManagerCall5 call = reinterpret_cast<CuteQDBusConnectionManagerCall5>(taken[5]);
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
      CuteQDBusConnectionManagerCall6 call = reinterpret_cast<CuteQDBusConnectionManagerCall6>(taken[6]);
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
      CuteQDBusConnectionManagerCall7 call = reinterpret_cast<CuteQDBusConnectionManagerCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QDBusConnectionManager::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK22QDBusConnectionManager10metaObjectEv(
    const QDBusConnectionManager *self) {
  return self->metaObject();
}

//  QDBusConnectionManager::~QDBusConnectionManager()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QDBusConnectionManagerD1Ev(QDBusConnectionManager *self) {
  delete self;
}

#if !defined(QT_NO_DBUS)
//  QDBusConnectionPrivate *QDBusConnectionManager::existingConnection(const
//      QString &name) const
extern "C" Q_DECL_EXPORT
QDBusConnectionPrivate *ritual_ZNK22QDBusConnectionManager18existingConnectionERK7QString(
    const QDBusConnectionManager *self,
    const QString *name) {
  return self->existingConnection(*name);
}
#endif  // !defined(QT_NO_DBUS)

#if !defined(QT_NO_DBUS)
//  void QDBusConnectionManager::removeConnections(const QStringList &names)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QDBusConnectionManager17removeConnectionsERK5QListI7QStringE(
    QDBusConnectionManager *self,
    const QList<QString> *names) {
  self->removeConnections(*names);
}
#endif  // !defined(QT_NO_DBUS)

#if !defined(QT_NO_DBUS)
//  void QDBusConnectionManager::disconnectFrom(const QString &name,
//      QDBusConnectionPrivate::ConnectionMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QDBusConnectionManager14disconnectFromERK7QStringN22QDBusConnectionPrivate14ConnectionModeE(
    QDBusConnectionManager *self,
    const QString *name,
    QDBusConnectionPrivate::ConnectionMode mode) {
  self->disconnectFrom(*name, mode);
}
#endif  // !defined(QT_NO_DBUS)

#if !defined(QT_NO_DBUS)
//  void QDBusConnectionManager::addConnection(const QString &name,
//      QDBusConnectionPrivate *c)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QDBusConnectionManager13addConnectionERK7QStringP22QDBusConnectionPrivate(
    QDBusConnectionManager *self,
    const QString *name,
    QDBusConnectionPrivate *c) {
  self->addConnection(*name, c);
}
#endif  // !defined(QT_NO_DBUS)

//  void QDBusConnectionManager::run()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QDBusConnectionManager3runEv(QDBusConnectionManager *self) {
  self->run();
}

#if !defined(QT_NO_DBUS)
//  QDBusConnectionPrivate *QDBusConnectionManager::connection(const QString
//      &name) const
extern "C" Q_DECL_EXPORT
QDBusConnectionPrivate *ritual_ZNK22QDBusConnectionManager10connectionERK7QString(
    const QDBusConnectionManager *self,
    const QString *name) {
  return self->connection(*name);
}
#endif  // !defined(QT_NO_DBUS)

#if !defined(QT_NO_DBUS)
//  void QDBusConnectionManager::removeConnection(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QDBusConnectionManager16removeConnectionERK7QString(
    QDBusConnectionManager *self,
    const QString *name) {
  self->removeConnection(*name);
}
#endif  // !defined(QT_NO_DBUS)

#if !defined(QT_NO_DBUS)
//  void QDBusConnectionManager::setConnection(const QString &name,
//      QDBusConnectionPrivate *c)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QDBusConnectionManager13setConnectionERK7QStringP22QDBusConnectionPrivate(
    QDBusConnectionManager *self,
    const QString *name,
    QDBusConnectionPrivate *c) {
  self->setConnection(*name, c);
}
#endif  // !defined(QT_NO_DBUS)

//  a Python function taken by a CuteQDBusConnectionManager, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDBusConnectionManager(
    QDBusConnectionManager *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDBusConnectionManager *>(self)->take(key, call);
}

#endif  // !defined(QT_NO_DBUS)
