//  Written by dev_tooling.RitualGenerator from the records of
//  QtDBus/qdbusconnectioninterface.h, Qt 6.12.0. Changes made here are lost.
#include <QtDBus/qtdbusglobal.h>
#include <QtDBus/6.12.0/QtDBus/private/qtdbusglobal_p.h>
#if !defined(QT_NO_DBUS)
#include <QtDBus/6.12.0/QtDBus/private/qtdbusglobal_p.h>
#include <QtDBus/qdbusconnectioninterface.h>
#include <QtCore/qstring.h>
#include <QtDBus/qdbusconnection.h>
#include <QtDBus/qdbuserror.h>
#include <QtDBus/qdbusmessage.h>
#include <QtCore/qmetaobject.h>
#include <QtDBus/QDBusReply>
#include <QtCore/QStringList>
#include <QtCore/QString>
#include <QtDBus/QDBusConnectionInterface>
#include <QtCore/QVariantMap>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDBus/qdbusconnectioninterface.h>
#include <QtCore/QByteArray>
#include <QtCore/QList>
#include <QtCore/QMap>
#include <QtCore/QMetaMethod>
#include <QtCore/QString>
#include <QtCore/QStringList>
#include <QtCore/QVariant>
#include <QtCore/QDebug>
#include <QtDBus/private/qdbusutil_p.h>          // for the DBUS_* constants
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from src/dbus/qdbusconnectioninterface.cpp, line 122, as _ZN24QDBusConnectionInterface19staticInterfaceNameEv
#if !defined(QT_NO_DBUS)
inline const char *QDBusConnectionInterface::staticInterfaceName()
{ return "org.freedesktop.DBus"; }
#endif  // !defined(QT_NO_DBUS)
//  -----------------------------------------------------------------------

//  Only a class built on QDBusConnectionInterface may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQDBusConnectionInterface : QDBusConnectionInterface {
  using QDBusConnectionInterface::connectNotify;
  using QDBusConnectionInterface::disconnectNotify;
};

//  const QMetaObject *QDBusConnectionInterface::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK24QDBusConnectionInterface10metaObjectEv(
    const QDBusConnectionInterface *self) {
  return self->metaObject();
}

//  void *QDBusConnectionInterface::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN24QDBusConnectionInterface11qt_metacastEPKc(
    QDBusConnectionInterface *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QDBusConnectionInterface::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN24QDBusConnectionInterface11qt_metacallEN11QMetaObject4CallEiPPv(
    QDBusConnectionInterface *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QDBusConnectionInterface::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN24QDBusConnectionInterface2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QDBusConnectionInterface::tr(s, c, n));
}

#if !defined(QT_NO_DBUS)
//  const char *QDBusConnectionInterface::staticInterfaceName()
extern "C" Q_DECL_EXPORT
const char *ritual_ZN24QDBusConnectionInterface19staticInterfaceNameEv() {
  return QDBusConnectionInterface::staticInterfaceName();
}
#endif  // !defined(QT_NO_DBUS)

//  QDBusConnectionInterface::QDBusConnectionInterface(const QDBusConnection
//      &connection, QObject *parent)
extern "C" Q_DECL_EXPORT
QDBusConnectionInterface *ritual_ZN24QDBusConnectionInterfaceC1ERK15QDBusConnectionP7QObject(
    const QDBusConnection *connection,
    QObject *parent) {
  return new QDBusConnectionInterface(*connection, parent);
}

//  QDBusConnectionInterface::~QDBusConnectionInterface()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QDBusConnectionInterfaceD1Ev(
    QDBusConnectionInterface *self) {
  delete self;
}

//  QDBusReply<QStringList>
//      QDBusConnectionInterface::registeredServiceNames() const
extern "C" Q_DECL_EXPORT
QDBusReply<QStringList> *ritual_ZNK24QDBusConnectionInterface22registeredServiceNamesEv(
    const QDBusConnectionInterface *self) {
  return new QDBusReply<QStringList>(self->registeredServiceNames());
}

//  QDBusReply<QStringList>
//      QDBusConnectionInterface::activatableServiceNames() const
extern "C" Q_DECL_EXPORT
QDBusReply<QStringList> *ritual_ZNK24QDBusConnectionInterface23activatableServiceNamesEv(
    const QDBusConnectionInterface *self) {
  return new QDBusReply<QStringList>(self->activatableServiceNames());
}

//  QDBusReply<bool> QDBusConnectionInterface::isServiceRegistered(const
//      QString &serviceName) const
extern "C" Q_DECL_EXPORT
QDBusReply<bool> *ritual_ZNK24QDBusConnectionInterface19isServiceRegisteredERK7QString(
    const QDBusConnectionInterface *self,
    const QString *serviceName) {
  return new QDBusReply<bool>(self->isServiceRegistered(*serviceName));
}

//  QDBusReply<QString> QDBusConnectionInterface::serviceOwner(const QString
//      &name) const
extern "C" Q_DECL_EXPORT
QDBusReply<QString> *ritual_ZNK24QDBusConnectionInterface12serviceOwnerERK7QString(
    const QDBusConnectionInterface *self,
    const QString *name) {
  return new QDBusReply<QString>(self->serviceOwner(*name));
}

//  QDBusReply<bool> QDBusConnectionInterface::unregisterService(const
//      QString &serviceName)
extern "C" Q_DECL_EXPORT
QDBusReply<bool> *ritual_ZN24QDBusConnectionInterface17unregisterServiceERK7QString(
    QDBusConnectionInterface *self,
    const QString *serviceName) {
  return new QDBusReply<bool>(self->unregisterService(*serviceName));
}

//  QDBusReply<QDBusConnectionInterface::RegisterServiceReply>
//      QDBusConnectionInterface::registerService(const QString &serviceName,
//      ServiceQueueOptions qoption, ServiceReplacementOptions roption)
extern "C" Q_DECL_EXPORT
QDBusReply<QDBusConnectionInterface::RegisterServiceReply> *ritual_ZN24QDBusConnectionInterface15registerServiceERK7QStringNS_19ServiceQueueOptionsENS_25ServiceReplacementOptionsE(
    QDBusConnectionInterface *self,
    const QString *serviceName,
    QDBusConnectionInterface::ServiceQueueOptions qoption,
    QDBusConnectionInterface::ServiceReplacementOptions roption) {
  return new QDBusReply<QDBusConnectionInterface::RegisterServiceReply>(
      self->registerService(
          *serviceName,
          qoption,
          roption));
}

//  QDBusReply<uint> QDBusConnectionInterface::servicePid(const QString
//      &serviceName) const
extern "C" Q_DECL_EXPORT
QDBusReply<uint> *ritual_ZNK24QDBusConnectionInterface10servicePidERK7QString(
    const QDBusConnectionInterface *self,
    const QString *serviceName) {
  return new QDBusReply<uint>(self->servicePid(*serviceName));
}

//  QDBusReply<uint> QDBusConnectionInterface::serviceUid(const QString
//      &serviceName) const
extern "C" Q_DECL_EXPORT
QDBusReply<uint> *ritual_ZNK24QDBusConnectionInterface10serviceUidERK7QString(
    const QDBusConnectionInterface *self,
    const QString *serviceName) {
  return new QDBusReply<uint>(self->serviceUid(*serviceName));
}

//  QDBusReply<QVariantMap>
//      QDBusConnectionInterface::serviceCredentials(const QString
//      &serviceName) const
extern "C" Q_DECL_EXPORT
QDBusReply<QVariantMap> *ritual_ZNK24QDBusConnectionInterface18serviceCredentialsERK7QString(
    const QDBusConnectionInterface *self,
    const QString *serviceName) {
  return new QDBusReply<QVariantMap>(self->serviceCredentials(*serviceName));
}

//  QDBusReply<void> QDBusConnectionInterface::startService(const QString
//      &name)
extern "C" Q_DECL_EXPORT
QDBusReply<void> *ritual_ZN24QDBusConnectionInterface12startServiceERK7QString(
    QDBusConnectionInterface *self,
    const QString *name) {
  return new QDBusReply<void>(self->startService(*name));
}

//  void QDBusConnectionInterface::serviceRegistered(const QString &service)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QDBusConnectionInterface17serviceRegisteredERK7QString(
    QDBusConnectionInterface *self,
    const QString *service) {
  self->serviceRegistered(*service);
}

//  void QDBusConnectionInterface::serviceUnregistered(const QString
//      &service)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QDBusConnectionInterface19serviceUnregisteredERK7QString(
    QDBusConnectionInterface *self,
    const QString *service) {
  self->serviceUnregistered(*service);
}

//  void QDBusConnectionInterface::serviceOwnerChanged(const QString &name,
//      const QString &oldOwner, const QString &newOwner)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QDBusConnectionInterface19serviceOwnerChangedERK7QStringS2_S2_(
    QDBusConnectionInterface *self,
    const QString *name,
    const QString *oldOwner,
    const QString *newOwner) {
  self->serviceOwnerChanged(*name, *oldOwner, *newOwner);
}

//  void QDBusConnectionInterface::callWithCallbackFailed(const QDBusError
//      &error, const QDBusMessage &call)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QDBusConnectionInterface22callWithCallbackFailedERK10QDBusErrorRK12QDBusMessage(
    QDBusConnectionInterface *self,
    const QDBusError *error,
    const QDBusMessage *call) {
  self->callWithCallbackFailed(*error, *call);
}

#if !defined(Q_QDOC)
//  void QDBusConnectionInterface::NameAcquired(const QString &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QDBusConnectionInterface12NameAcquiredERK7QString(
    QDBusConnectionInterface *self,
    const QString *a0) {
  self->NameAcquired(*a0);
}
#endif  // !defined(Q_QDOC)

#if !defined(Q_QDOC)
//  void QDBusConnectionInterface::NameLost(const QString &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QDBusConnectionInterface8NameLostERK7QString(
    QDBusConnectionInterface *self,
    const QString *a0) {
  self->NameLost(*a0);
}
#endif  // !defined(Q_QDOC)

#if !defined(Q_QDOC)
//  void QDBusConnectionInterface::NameOwnerChanged(const QString &a0, const
//      QString &a1, const QString &a2)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QDBusConnectionInterface16NameOwnerChangedERK7QStringS2_S2_(
    QDBusConnectionInterface *self,
    const QString *a0,
    const QString *a1,
    const QString *a2) {
  self->NameOwnerChanged(*a0, *a1, *a2);
}
#endif  // !defined(Q_QDOC)

#if !defined(Q_QDOC)
//  void QDBusConnectionInterface::connectNotify(const QMetaMethod &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QDBusConnectionInterface13connectNotifyERK11QMetaMethod(
    QDBusConnectionInterface *self,
    const QMetaMethod *a0) {
  self->connectNotify(*a0);
}
#endif  // !defined(Q_QDOC)

#if !defined(Q_QDOC)
//  void QDBusConnectionInterface::disconnectNotify(const QMetaMethod &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QDBusConnectionInterface16disconnectNotifyERK11QMetaMethod(
    QDBusConnectionInterface *self,
    const QMetaMethod *a0) {
  self->disconnectNotify(*a0);
}
#endif  // !defined(Q_QDOC)

#if !defined(Q_QDOC)
//  void QDBusConnectionInterface::connectNotify(const QMetaMethod &a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QDBusConnectionInterface13connectNotifyERK11QMetaMethod(
    QDBusConnectionInterface *self,
    const QMetaMethod *a0) {
  static_cast<OwnQDBusConnectionInterface *>(self)->OwnQDBusConnectionInterface::connectNotify(
      *a0);
}
#endif  // !defined(Q_QDOC)

#if !defined(Q_QDOC)
//  void QDBusConnectionInterface::disconnectNotify(const QMetaMethod &a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QDBusConnectionInterface16disconnectNotifyERK11QMetaMethod(
    QDBusConnectionInterface *self,
    const QMetaMethod *a0) {
  static_cast<OwnQDBusConnectionInterface *>(self)->OwnQDBusConnectionInterface::disconnectNotify(
      *a0);
}
#endif  // !defined(Q_QDOC)

//  a QDBusReply<QStringList> a ritual of QDBusConnectionInterface gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QDBusConnectionInterface__QDBusReply_QStringList(
    QDBusReply<QStringList> *self) {
  delete self;
}

//  a QDBusReply<bool> a ritual of QDBusConnectionInterface gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QDBusConnectionInterface__QDBusReply_bool(
    QDBusReply<bool> *self) {
  delete self;
}

//  a QDBusReply<QString> a ritual of QDBusConnectionInterface gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QDBusConnectionInterface__QDBusReply_QString(
    QDBusReply<QString> *self) {
  delete self;
}

//  a QDBusReply<QDBusConnectionInterface::RegisterServiceReply> a ritual of
//      QDBusConnectionInterface gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QDBusConnectionInterface__QDBusReply_QDBusConnectionInterface_RegisterServiceReply(
    QDBusReply<QDBusConnectionInterface::RegisterServiceReply> *self) {
  delete self;
}

//  a QDBusReply<uint> a ritual of QDBusConnectionInterface gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QDBusConnectionInterface__QDBusReply_uint(
    QDBusReply<uint> *self) {
  delete self;
}

//  a QDBusReply<QVariantMap> a ritual of QDBusConnectionInterface gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QDBusConnectionInterface__QDBusReply_QVariantMap(
    QDBusReply<QVariantMap> *self) {
  delete self;
}

//  a QDBusReply<void> a ritual of QDBusConnectionInterface gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QDBusConnectionInterface__QDBusReply_void(
    QDBusReply<void> *self) {
  delete self;
}

#endif  // !defined(QT_NO_DBUS)
