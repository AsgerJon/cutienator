//  Written by dev_tooling.RitualGenerator from the records of
//  QtBluetooth/6.12.0/QtBluetooth/private/bluezperipheralapplication_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtBluetooth/qtbluetoothglobal.h>
#include <QtBluetooth/6.12.0/QtBluetooth/private/qtbluetoothglobal_p.h>
#if QT_CONFIG(bluez)
#include <QtBluetooth/6.12.0/QtBluetooth/private/qtbluetoothglobal_p.h>
#include <QtBluetooth/QtBluetooth>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtBluetooth/6.12.0/QtBluetooth/private/bluezperipheralapplication_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <QtBluetooth/qbluetoothuuid.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#include <QtBluetooth/QBluetoothUuid>
#include <QtCore/QSharedPointer>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtBluetooth/private/bluezperipheralobjects_p.h>
#include <QtBluetooth/private/propertiesadaptor_p.h>
#include <QtBluetooth/private/gattservice1adaptor_p.h>
#include <QtBluetooth/private/gattcharacteristic1adaptor_p.h>
#include <QtBluetooth/private/gattdescriptor1adaptor_p.h>
#include <QtCore/QLoggingCategory>
#include <QtDBus/QDBusConnection>
#include <QtBluetooth/private/bluezperipheralapplication_p.h>
#include <QtBluetooth/private/bluezperipheralobjects_p.h>
#include <QtBluetooth/private/objectmanageradaptor_p.h>
#include <QtBluetooth/private/gattmanager1_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from ../qtconnectivity/src/bluetooth/bluez/bluezperipheralapplication.cpp, line 16, as local:bluezperipheralapplication.cpp:appObjectPathTemplate
static constexpr QLatin1String appObjectPathTemplate{"/qt/btle/application/%1%2/%3"};

//  from ../qtconnectivity/src/bluetooth/bluez/bluezperipheralobjects.cpp, line 26, as local:bluezperipheralobjects.cpp:bluezServiceInterface
static constexpr auto bluezServiceInterface{"org.bluez.GattService1"_L1};

//  from ../qtconnectivity/src/bluetooth/bluez/bluezperipheralobjects.cpp, line 27, as local:bluezperipheralobjects.cpp:bluezCharacteristicInterface
static constexpr auto bluezCharacteristicInterface{"org.bluez.GattCharacteristic1"_L1};

//  from ../qtconnectivity/src/bluetooth/bluez/bluezperipheralobjects.cpp, line 28, as local:bluezperipheralobjects.cpp:bluezDescriptorInterface
static constexpr auto bluezDescriptorInterface{"org.bluez.GattDescriptor1"_L1};

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

//  from ../qtconnectivity/src/bluetooth/bluez/bluezperipheralapplication.cpp, line 31, as _ZN28QtBluezPeripheralApplicationD1Ev
inline QtBluezPeripheralApplication::~QtBluezPeripheralApplication()
{
    unregisterApplication();
}

//  from ../qtconnectivity/src/bluetooth/bluez/bluezperipheralapplication.cpp, line 236, as _ZN28QtBluezPeripheralApplication18registrationNeededEv
inline bool QtBluezPeripheralApplication::registrationNeeded()
{
    return !m_applicationRegistered && !m_services.isEmpty();
}

//  from ../qtconnectivity/src/bluetooth/bluez/bluezperipheralapplication.cpp, line 243, as _ZN28QtBluezPeripheralApplication17GetManagedObjectsEv
inline ManagedObjectList QtBluezPeripheralApplication::GetManagedObjects()
{
    ManagedObjectList managedObjects;
    for (const auto service: std::as_const(m_services))
        managedObjects.insert(QDBusObjectPath(service->objectPath), service->properties());
    for (const auto& charac : std::as_const(m_characteristics))
        managedObjects.insert(QDBusObjectPath(charac->objectPath), charac->properties());
    for (const auto& descriptor : std::as_const(m_descriptors))
        managedObjects.insert(QDBusObjectPath(descriptor->objectPath), descriptor->properties());

    return managedObjects;
}

//  from ../qtconnectivity/src/bluetooth/bluez/bluezperipheralapplication.cpp, line 257, as _ZN28QtBluezPeripheralApplication23handleForCharacteristicE14QBluetoothUuid14QSharedPointerI24QLowEnergyServicePrivateE
inline QLowEnergyHandle QtBluezPeripheralApplication::handleForCharacteristic(QBluetoothUuid uuid,
                                         QSharedPointer<QLowEnergyServicePrivate> service)
{
    const auto handles = service->characteristicList.keys();
    for (const auto handle : handles) {
        if (uuid == service->characteristicList[handle].uuid)
            return handle;
    }
    return 0;
}

//  from ../qtconnectivity/src/bluetooth/bluez/bluezperipheralapplication.cpp, line 269, as _ZN28QtBluezPeripheralApplication19handleForDescriptorE14QBluetoothUuid14QSharedPointerI24QLowEnergyServicePrivateEt
inline QLowEnergyHandle QtBluezPeripheralApplication::handleForDescriptor(QBluetoothUuid uuid,
                                     QSharedPointer<QLowEnergyServicePrivate> service,
                                     QLowEnergyHandle characteristicHandle)
{
    const auto characteristicData = service->characteristicList[characteristicHandle];
    const auto handles = characteristicData.descriptorList.keys();
    for (const auto handle : handles) {
        if (uuid == characteristicData.descriptorList[handle].uuid)
            return handle;
    }
    return 0;
}
//  -----------------------------------------------------------------------

//  A QtBluezPeripheralApplication that Python can take functions over in. Every QtBluezPeripheralApplication
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQtBluezPeripheralApplicationCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQtBluezPeripheralApplicationCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtBluezPeripheralApplicationCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtBluezPeripheralApplicationCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtBluezPeripheralApplicationCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtBluezPeripheralApplicationCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtBluezPeripheralApplicationCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQtBluezPeripheralApplication : public QtBluezPeripheralApplication {
public:
  using QtBluezPeripheralApplication::QtBluezPeripheralApplication;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
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
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQtBluezPeripheralApplicationCall0 call = reinterpret_cast<CuteQtBluezPeripheralApplicationCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQtBluezPeripheralApplicationCall1 call = reinterpret_cast<CuteQtBluezPeripheralApplicationCall1>(taken[1]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQtBluezPeripheralApplicationCall2 call = reinterpret_cast<CuteQtBluezPeripheralApplicationCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQtBluezPeripheralApplicationCall3 call = reinterpret_cast<CuteQtBluezPeripheralApplicationCall3>(taken[3]);
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
      CuteQtBluezPeripheralApplicationCall4 call = reinterpret_cast<CuteQtBluezPeripheralApplicationCall4>(taken[4]);
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
      CuteQtBluezPeripheralApplicationCall5 call = reinterpret_cast<CuteQtBluezPeripheralApplicationCall5>(taken[5]);
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
      CuteQtBluezPeripheralApplicationCall6 call = reinterpret_cast<CuteQtBluezPeripheralApplicationCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QtBluezPeripheralApplication::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK28QtBluezPeripheralApplication10metaObjectEv(
    const QtBluezPeripheralApplication *self) {
  return self->metaObject();
}

//  void *QtBluezPeripheralApplication::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN28QtBluezPeripheralApplication11qt_metacastEPKc(
    QtBluezPeripheralApplication *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QtBluezPeripheralApplication::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN28QtBluezPeripheralApplication11qt_metacallEN11QMetaObject4CallEiPPv(
    QtBluezPeripheralApplication *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QtBluezPeripheralApplication::~QtBluezPeripheralApplication()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QtBluezPeripheralApplicationD1Ev(
    QtBluezPeripheralApplication *self) {
  delete self;
}

//  bool QtBluezPeripheralApplication::registrationNeeded()
extern "C" Q_DECL_EXPORT
bool ritual_ZN28QtBluezPeripheralApplication18registrationNeededEv(
    QtBluezPeripheralApplication *self) {
  return self->registrationNeeded();
}

//  ManagedObjectList QtBluezPeripheralApplication::GetManagedObjects()
extern "C" Q_DECL_EXPORT
ManagedObjectList *ritual_ZN28QtBluezPeripheralApplication17GetManagedObjectsEv(
    QtBluezPeripheralApplication *self) {
  return new ManagedObjectList(self->GetManagedObjects());
}

//  void QtBluezPeripheralApplication::errorOccurred()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QtBluezPeripheralApplication13errorOccurredEv(
    QtBluezPeripheralApplication *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QtBluezPeripheralApplication")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "errorOccurred()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "errorOccurred()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QtBluezPeripheralApplication::registered()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QtBluezPeripheralApplication10registeredEv(
    QtBluezPeripheralApplication *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QtBluezPeripheralApplication")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "registered()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "registered()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QtBluezPeripheralApplication::remoteDeviceAccessEvent(const QString
//      &remoteDeviceObjectPath, quint16 mtu)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QtBluezPeripheralApplication23remoteDeviceAccessEventERK7QStringt(
    QtBluezPeripheralApplication *self,
    const QString *remoteDeviceObjectPath,
    quint16 mtu) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QtBluezPeripheralApplication")) {
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

//  void QtBluezPeripheralApplication::characteristicValueUpdatedByRemote(QLo
//      wEnergyHandle handle, const QByteArray &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QtBluezPeripheralApplication34characteristicValueUpdatedByRemoteEtRK10QByteArray(
    QtBluezPeripheralApplication *self,
    QLowEnergyHandle handle,
    const QByteArray *value) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QtBluezPeripheralApplication")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "characteristicValueUpdatedByRemote(QLowEnergyHandle,const QByteArray &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "characteristicValueUpdatedByRemote(QLowEnergyHandle,const QByteArray &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&handle)),
      const_cast<void *>(static_cast<const void *>(value)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QtBluezPeripheralApplication::descriptorValueUpdatedByRemote(QLowEne
//      rgyHandle characteristicHandle, QLowEnergyHandle descriptorHandle,
//      const QByteArray &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QtBluezPeripheralApplication30descriptorValueUpdatedByRemoteEttRK10QByteArray(
    QtBluezPeripheralApplication *self,
    QLowEnergyHandle characteristicHandle,
    QLowEnergyHandle descriptorHandle,
    const QByteArray *value) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QtBluezPeripheralApplication")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "descriptorValueUpdatedByRemote(QLowEnergyHandle,QLowEnergyHandle,const QByteArray &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "descriptorValueUpdatedByRemote(QLowEnergyHandle,QLowEnergyHandle,const QByteArray &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&characteristicHandle)),
      const_cast<void *>(static_cast<const void *>(&descriptorHandle)),
      const_cast<void *>(static_cast<const void *>(value)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  QLowEnergyHandle
//      QtBluezPeripheralApplication::handleForCharacteristic(QBluetoothUuid
//      uuid, QSharedPointer<QLowEnergyServicePrivate> service)
extern "C" Q_DECL_EXPORT
QLowEnergyHandle ritual_ZN28QtBluezPeripheralApplication23handleForCharacteristicE14QBluetoothUuid14QSharedPointerI24QLowEnergyServicePrivateE(
    QtBluezPeripheralApplication *self,
    const QBluetoothUuid *uuid,
    const QSharedPointer<QLowEnergyServicePrivate> *service) {
  return self->handleForCharacteristic(*uuid, *service);
}

//  QLowEnergyHandle
//      QtBluezPeripheralApplication::handleForDescriptor(QBluetoothUuid
//      uuid, QSharedPointer<QLowEnergyServicePrivate> service,
//      QLowEnergyHandle characteristicHandle)
extern "C" Q_DECL_EXPORT
QLowEnergyHandle ritual_ZN28QtBluezPeripheralApplication19handleForDescriptorE14QBluetoothUuid14QSharedPointerI24QLowEnergyServicePrivateEt(
    QtBluezPeripheralApplication *self,
    const QBluetoothUuid *uuid,
    const QSharedPointer<QLowEnergyServicePrivate> *service,
    QLowEnergyHandle characteristicHandle) {
  return self->handleForDescriptor(*uuid, *service, characteristicHandle);
}

//  a Python function taken by a CuteQtBluezPeripheralApplication, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QtBluezPeripheralApplication(
    QtBluezPeripheralApplication *self,
    const char *key,
    void *call) {
  return static_cast<CuteQtBluezPeripheralApplication *>(self)->take(key, call);
}

//  a ManagedObjectList a ritual of QtBluezPeripheralApplication gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QtBluezPeripheralApplication__ManagedObjectList(
    ManagedObjectList *self) {
  delete self;
}

#endif  // QT_CONFIG(bluez)
