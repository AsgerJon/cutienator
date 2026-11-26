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
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from ../qtconnectivity/src/bluetooth/bluez/bluezperipheralobjects.cpp, line 22, as local:bluezperipheralobjects.cpp:descriptorPathTemplate
static constexpr auto descriptorPathTemplate{"%1/desc%2"_L1};

//  from ../qtconnectivity/src/bluetooth/bluez/bluezperipheralobjects.cpp, line 28, as local:bluezperipheralobjects.cpp:bluezDescriptorInterface
static constexpr auto bluezDescriptorInterface{"org.bluez.GattDescriptor1"_L1};

//  from ../qtconnectivity/src/bluetooth/bluez/bluezperipheralobjects.cpp, line 34, as local:bluezperipheralobjects.cpp:maximumAttributeLength
static constexpr int maximumAttributeLength{512};

//  from ../qtconnectivity/src/bluetooth/bluez/bluezperipheralobjects.cpp, line 101, as _ZNK27QtBluezPeripheralDescriptor10propertiesEv
inline InterfaceList QtBluezPeripheralDescriptor::properties() const
{
    InterfaceList properties;
    properties.insert(bluezDescriptorInterface,
                      {
                          {"UUID"_L1, uuid},
                          {"Characteristic"_L1, QDBusObjectPath(m_characteristicPath)},
                          {"Flags"_L1, m_flags}
                      });
    return  properties;
}
//  -----------------------------------------------------------------------

//  const QMetaObject *QtBluezPeripheralDescriptor::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK27QtBluezPeripheralDescriptor10metaObjectEv(
    const QtBluezPeripheralDescriptor *self) {
  return self->metaObject();
}

//  void *QtBluezPeripheralDescriptor::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN27QtBluezPeripheralDescriptor11qt_metacastEPKc(
    QtBluezPeripheralDescriptor *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QtBluezPeripheralDescriptor::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN27QtBluezPeripheralDescriptor11qt_metacallEN11QMetaObject4CallEiPPv(
    QtBluezPeripheralDescriptor *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  InterfaceList QtBluezPeripheralDescriptor::properties() const
extern "C" Q_DECL_EXPORT
InterfaceList *ritual_ZNK27QtBluezPeripheralDescriptor10propertiesEv(
    const QtBluezPeripheralDescriptor *self) {
  return new InterfaceList(self->properties());
}

//  void QtBluezPeripheralDescriptor::valueUpdatedByRemote(QLowEnergyHandle
//      characteristicHandle, QLowEnergyHandle descriptorHandle, const
//      QByteArray &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QtBluezPeripheralDescriptor20valueUpdatedByRemoteEttRK10QByteArray(
    QtBluezPeripheralDescriptor *self,
    QLowEnergyHandle characteristicHandle,
    QLowEnergyHandle descriptorHandle,
    const QByteArray *value) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QtBluezPeripheralDescriptor")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "valueUpdatedByRemote(QLowEnergyHandle,QLowEnergyHandle,const QByteArray &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "valueUpdatedByRemote(QLowEnergyHandle,QLowEnergyHandle,const QByteArray &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&characteristicHandle)),
      const_cast<void *>(static_cast<const void *>(&descriptorHandle)),
      const_cast<void *>(static_cast<const void *>(value)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  a InterfaceList a ritual of QtBluezPeripheralDescriptor gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QtBluezPeripheralDescriptor__InterfaceList(
    InterfaceList *self) {
  delete self;
}

#endif  // QT_CONFIG(bluez)
