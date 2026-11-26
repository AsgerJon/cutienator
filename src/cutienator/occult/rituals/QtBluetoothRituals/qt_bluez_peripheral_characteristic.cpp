//  Written by dev_tooling.RitualGenerator from the records of
//  QtBluetooth/6.12.0/QtBluetooth/private/bluezperipheralobjects_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtBluetooth/qtbluetoothglobal.h>
#include <QtBluetooth/6.12.0/QtBluetooth/private/qtbluetoothglobal_p.h>
#if QT_CONFIG(bluez)
#include <QtBluetooth/6.12.0/QtBluetooth/private/qtbluetoothglobal_p.h>
#include <QtBluetooth/QtBluetooth>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtBluetooth/6.12.0/QtBluetooth/private/bluezperipheralobjects_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtBluetooth/private/bluezperipheralobjects_p.h>
#include <QtBluetooth/private/propertiesadaptor_p.h>
#include <QtBluetooth/private/gattservice1adaptor_p.h>
#include <QtBluetooth/private/gattcharacteristic1adaptor_p.h>
#include <QtBluetooth/private/gattdescriptor1adaptor_p.h>
#include <QtCore/QLoggingCategory>
#include <QtDBus/QDBusConnection>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from ../qtconnectivity/src/bluetooth/bluez/bluezperipheralobjects.cpp, line 21, as local:bluezperipheralobjects.cpp:characteristicPathTemplate
static constexpr auto characteristicPathTemplate{"%1/char%2"_L1};

//  from ../qtconnectivity/src/bluetooth/bluez/bluezperipheralobjects.cpp, line 27, as local:bluezperipheralobjects.cpp:bluezCharacteristicInterface
static constexpr auto bluezCharacteristicInterface{"org.bluez.GattCharacteristic1"_L1};

//  from ../qtconnectivity/src/bluetooth/bluez/bluezperipheralobjects.cpp, line 34, as local:bluezperipheralobjects.cpp:maximumAttributeLength
static constexpr int maximumAttributeLength{512};

//  from ../qtconnectivity/src/bluetooth/bluez/bluezperipheralobjects.cpp, line 215, as _ZNK31QtBluezPeripheralCharacteristic10propertiesEv
inline InterfaceList QtBluezPeripheralCharacteristic::properties() const
{
    InterfaceList properties;
    properties.insert(bluezCharacteristicInterface,
                      {
                          {"UUID"_L1, uuid},
                          {"Service"_L1, QDBusObjectPath(m_servicePath)},
                          {"Flags"_L1, m_flags}
                      });
    return properties;
}
//  -----------------------------------------------------------------------

//  const QMetaObject *QtBluezPeripheralCharacteristic::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK31QtBluezPeripheralCharacteristic10metaObjectEv(
    const QtBluezPeripheralCharacteristic *self) {
  return self->metaObject();
}

//  void *QtBluezPeripheralCharacteristic::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN31QtBluezPeripheralCharacteristic11qt_metacastEPKc(
    QtBluezPeripheralCharacteristic *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QtBluezPeripheralCharacteristic::qt_metacall(QMetaObject::Call a0,
//      int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN31QtBluezPeripheralCharacteristic11qt_metacallEN11QMetaObject4CallEiPPv(
    QtBluezPeripheralCharacteristic *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  InterfaceList QtBluezPeripheralCharacteristic::properties() const
extern "C" Q_DECL_EXPORT
InterfaceList *ritual_ZNK31QtBluezPeripheralCharacteristic10propertiesEv(
    const QtBluezPeripheralCharacteristic *self) {
  return new InterfaceList(self->properties());
}

//  void QtBluezPeripheralCharacteristic::StartNotify()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QtBluezPeripheralCharacteristic11StartNotifyEv(
    QtBluezPeripheralCharacteristic *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QtBluezPeripheralCharacteristic")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "StartNotify()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "StartNotify()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QtBluezPeripheralCharacteristic::StopNotify()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QtBluezPeripheralCharacteristic10StopNotifyEv(
    QtBluezPeripheralCharacteristic *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QtBluezPeripheralCharacteristic")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "StopNotify()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "StopNotify()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void
//      QtBluezPeripheralCharacteristic::valueUpdatedByRemote(QLowEnergyHandl
//      e handle, const QByteArray &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QtBluezPeripheralCharacteristic20valueUpdatedByRemoteEtRK10QByteArray(
    QtBluezPeripheralCharacteristic *self,
    QLowEnergyHandle handle,
    const QByteArray *value) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QtBluezPeripheralCharacteristic")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "valueUpdatedByRemote(QLowEnergyHandle,const QByteArray &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "valueUpdatedByRemote(QLowEnergyHandle,const QByteArray &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&handle)),
      const_cast<void *>(static_cast<const void *>(value)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  a InterfaceList a ritual of QtBluezPeripheralCharacteristic gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QtBluezPeripheralCharacteristic__InterfaceList(
    InterfaceList *self) {
  delete self;
}

#endif  // QT_CONFIG(bluez)
