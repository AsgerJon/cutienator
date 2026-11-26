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

//  from ../qtconnectivity/src/bluetooth/bluez/bluezperipheralobjects.cpp, line 23, as local:bluezperipheralobjects.cpp:servicePathTemplate
static constexpr auto servicePathTemplate{"%1/service%2"_L1};

//  from ../qtconnectivity/src/bluetooth/bluez/bluezperipheralobjects.cpp, line 26, as local:bluezperipheralobjects.cpp:bluezServiceInterface
static constexpr auto bluezServiceInterface{"org.bluez.GattService1"_L1};

//  from ../qtconnectivity/src/bluetooth/bluez/bluezperipheralobjects.cpp, line 393, as _ZNK24QtBluezPeripheralService10propertiesEv
inline InterfaceList QtBluezPeripheralService::properties() const {
    InterfaceList interfaces;
    interfaces.insert(bluezServiceInterface,{
                          {"UUID"_L1, uuid},
                          {"Primary"_L1, m_isPrimary},
                          {"Includes"_L1, QVariant::fromValue(m_includedServices)}
                      });
    return interfaces;
}
//  -----------------------------------------------------------------------

//  const QMetaObject *QtBluezPeripheralService::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK24QtBluezPeripheralService10metaObjectEv(
    const QtBluezPeripheralService *self) {
  return self->metaObject();
}

//  void *QtBluezPeripheralService::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN24QtBluezPeripheralService11qt_metacastEPKc(
    QtBluezPeripheralService *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QtBluezPeripheralService::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN24QtBluezPeripheralService11qt_metacallEN11QMetaObject4CallEiPPv(
    QtBluezPeripheralService *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  InterfaceList QtBluezPeripheralService::properties() const
extern "C" Q_DECL_EXPORT
InterfaceList *ritual_ZNK24QtBluezPeripheralService10propertiesEv(
    const QtBluezPeripheralService *self) {
  return new InterfaceList(self->properties());
}

//  a InterfaceList a ritual of QtBluezPeripheralService gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QtBluezPeripheralService__InterfaceList(
    InterfaceList *self) {
  delete self;
}

#endif  // QT_CONFIG(bluez)
