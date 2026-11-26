//  Written by dev_tooling.RitualGenerator from the records of QtBluetooth/6.
//  12.0/QtBluetooth/private/bluezperipheralconnectionmanager_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtBluetooth/qtbluetoothglobal.h>
#include <QtBluetooth/6.12.0/QtBluetooth/private/qtbluetoothglobal_p.h>
#if QT_CONFIG(bluez)
#include <QtBluetooth/6.12.0/QtBluetooth/private/qtbluetoothglobal_p.h>
#include <QtBluetooth/QtBluetooth>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtBluetooth/6.12.0/QtBluetooth/private/bluezperipheralconnectionmanager_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtBluetooth/qbluetoothaddress.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtBluetooth/private/bluezperipheralconnectionmanager_p.h>
#include <QtBluetooth/private/device1_bluez5_p.h>
#include <QtBluetooth/QBluetoothLocalDevice>
#include <QtDBus/QDBusConnection>
#include <QtCore/QLoggingCategory>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from ../qtconnectivity/src/bluetooth/bluez/bluezperipheralconnectionmanager.cpp, line 89, as _ZN34QtBluezPeripheralConnectionManager5resetEv
inline void QtBluezPeripheralConnectionManager::reset()
{
    m_connected = false;
    m_clients.clear();
}
//  -----------------------------------------------------------------------

//  const QMetaObject *QtBluezPeripheralConnectionManager::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK34QtBluezPeripheralConnectionManager10metaObjectEv(
    const QtBluezPeripheralConnectionManager *self) {
  return self->metaObject();
}

//  void *QtBluezPeripheralConnectionManager::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN34QtBluezPeripheralConnectionManager11qt_metacastEPKc(
    QtBluezPeripheralConnectionManager *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QtBluezPeripheralConnectionManager::qt_metacall(QMetaObject::Call a0,
//      int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN34QtBluezPeripheralConnectionManager11qt_metacallEN11QMetaObject4CallEiPPv(
    QtBluezPeripheralConnectionManager *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  void QtBluezPeripheralConnectionManager::reset()
extern "C" Q_DECL_EXPORT
void ritual_ZN34QtBluezPeripheralConnectionManager5resetEv(
    QtBluezPeripheralConnectionManager *self) {
  self->reset();
}

//  void QtBluezPeripheralConnectionManager::remoteDeviceAccessEvent(const
//      QString &remoteDeviceObjectPath, quint16 mtu)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QtBluezPeripheralConnectionManager23remoteDeviceAccessEventERK7QStringt(
    QtBluezPeripheralConnectionManager *self,
    const QString *remoteDeviceObjectPath,
    quint16 mtu) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QtBluezPeripheralConnectionManager")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "remoteDeviceAccessEvent(const QString &,quint16)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "remoteDeviceAccessEvent(const QString &,quint16)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(remoteDeviceObjectPath)),
      const_cast<void *>(static_cast<const void *>(&mtu)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QtBluezPeripheralConnectionManager::connectivityStateChanged(bool
//      connected)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QtBluezPeripheralConnectionManager24connectivityStateChangedEb(
    QtBluezPeripheralConnectionManager *self,
    bool connected) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QtBluezPeripheralConnectionManager")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "connectivityStateChanged(bool)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "connectivityStateChanged(bool)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&connected)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QtBluezPeripheralConnectionManager::remoteDeviceChanged(const
//      QBluetoothAddress &address, const QString &name, quint16 mtu)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QtBluezPeripheralConnectionManager19remoteDeviceChangedERK17QBluetoothAddressRK7QStringt(
    QtBluezPeripheralConnectionManager *self,
    const QBluetoothAddress *address,
    const QString *name,
    quint16 mtu) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QtBluezPeripheralConnectionManager")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "remoteDeviceChanged(const QBluetoothAddress &,const QString &,quint16)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "remoteDeviceChanged(const QBluetoothAddress &,const QString &,quint16)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(address)),
      const_cast<void *>(static_cast<const void *>(name)),
      const_cast<void *>(static_cast<const void *>(&mtu)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QtBluezPeripheralConnectionManager::remoteDeviceDisconnected(const
//      QBluetoothAddress &address)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QtBluezPeripheralConnectionManager24remoteDeviceDisconnectedERK17QBluetoothAddress(
    QtBluezPeripheralConnectionManager *self,
    const QBluetoothAddress *address) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QtBluezPeripheralConnectionManager")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "remoteDeviceDisconnected(const QBluetoothAddress &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "remoteDeviceDisconnected(const QBluetoothAddress &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(address)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

#endif  // QT_CONFIG(bluez)
