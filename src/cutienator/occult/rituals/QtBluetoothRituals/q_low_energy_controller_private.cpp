//  Written by dev_tooling.RitualGenerator from the records of
//  QtBluetooth/6.12.0/QtBluetooth/private/qlowenergycontrollerbase_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtBluetooth/6.12.0/QtBluetooth/private/qtbluetoothglobal_p.h>
#include <QtBluetooth/qlowenergycontroller.h>
#include <QtBluetooth/QtBluetooth>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtBluetooth/6.12.0/QtBluetooth/private/qlowenergycontrollerbase_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtBluetooth/qbluetoothuuid.h>
#include <QtCore/qbytearray.h>
#include <QtBluetooth/qlowenergyadvertisingparameters.h>
#include <QtBluetooth/qlowenergyadvertisingdata.h>
#include <QtBluetooth/qlowenergyconnectionparameters.h>
#include <QtBluetooth/qlowenergyservicedata.h>
#include <QtBluetooth/qlowenergycharacteristic.h>
#include <QtBluetooth/qlowenergydescriptor.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#include <QtCore/QSharedPointer>
#include <QtCore/QByteArray>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtBluetooth/private/qlowenergyserviceprivate_p.h>
#include <QtBluetooth/private/qlowenergycontrollerbase_p.h>
#include <QtBluetooth/private/qlowenergycontrollerbase_p.h>
#include <QtCore/QLoggingCategory>
#include <QtBluetooth/QBluetoothLocalDevice>
#include <QtBluetooth/QLowEnergyCharacteristicData>
#include <QtBluetooth/QLowEnergyDescriptorData>
#include <QtBluetooth/QLowEnergyServiceData>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtconnectivity/src/bluetooth/qlowenergyserviceprivate.cpp, line 19, as _ZN24QLowEnergyServicePrivate13setControllerEP27QLowEnergyControllerPrivate
inline void QLowEnergyServicePrivate::setController(QLowEnergyControllerPrivate *control)
{
    controller = control;

    if (control)
        setState(QLowEnergyService::RemoteService);
    else
        setState(QLowEnergyService::InvalidService);
}

//  from ../qtconnectivity/src/bluetooth/qlowenergyserviceprivate.cpp, line 35, as _ZN24QLowEnergyServicePrivate8setStateEN17QLowEnergyService12ServiceStateE
inline void QLowEnergyServicePrivate::setState(QLowEnergyService::ServiceState newState)
{
    if (state == newState)
        return;

    state = newState;
    emit stateChanged(newState);
}

//  from ../qtconnectivity/src/bluetooth/qlowenergycontrollerbase.cpp, line 31, as _ZN27QLowEnergyControllerPrivate19isValidLocalAdapterEv
#if defined(Q_OS_LINUX)
inline bool QLowEnergyControllerPrivate::isValidLocalAdapter()
{
#if defined(QT_WINRT_BLUETOOTH) || defined(Q_OS_DARWIN)
    return true;
#endif
    if (localAdapter.isNull())
        return false;

    const QList<QBluetoothHostInfo> foundAdapters = QBluetoothLocalDevice::allDevices();
    bool adapterFound = false;

    for (const QBluetoothHostInfo &info : foundAdapters) {
        if (info.address() == localAdapter) {
            adapterFound = true;
            break;
        }
    }

    return adapterFound;
}
#endif  // defined(Q_OS_LINUX)

//  from ../qtconnectivity/src/bluetooth/qlowenergycontrollerbase.cpp, line 53, as _ZN27QLowEnergyControllerPrivate8setErrorEN20QLowEnergyController5ErrorE
inline void QLowEnergyControllerPrivate::setError(
        QLowEnergyController::Error newError)
{
    Q_Q(QLowEnergyController);
    error = newError;

    switch (newError) {
    case QLowEnergyController::UnknownRemoteDeviceError:
        errorString = QLowEnergyController::tr("Remote device cannot be found");
        break;
    case QLowEnergyController::InvalidBluetoothAdapterError:
        errorString = QLowEnergyController::tr("Cannot find local adapter");
        break;
    case QLowEnergyController::NetworkError:
        errorString = QLowEnergyController::tr("Error occurred during connection I/O");
        break;
    case QLowEnergyController::ConnectionError:
        errorString = QLowEnergyController::tr("Error occurred trying to connect to remote device.");
        break;
    case QLowEnergyController::AdvertisingError:
        errorString = QLowEnergyController::tr("Error occurred trying to start advertising");
        break;
    case QLowEnergyController::RemoteHostClosedError:
        errorString = QLowEnergyController::tr("Remote device closed the connection");
        break;
    case QLowEnergyController::AuthorizationError:
        errorString = QLowEnergyController::tr("Failed to authorize on the remote device");
        break;
    case QLowEnergyController::MissingPermissionsError:
        errorString = QLowEnergyController::tr("Missing permissions error");
        break;
    case QLowEnergyController::RssiReadError:
        errorString = QLowEnergyController::tr("Error reading RSSI value");
        break;
    case QLowEnergyController::NoError:
        return;
    default:
    case QLowEnergyController::UnknownError:
        errorString = QLowEnergyController::tr("Unknown Error");
        break;
    }

    emit q->errorOccurred(newError);
}

//  from ../qtconnectivity/src/bluetooth/qlowenergycontrollerbase.cpp, line 114, as _ZN27QLowEnergyControllerPrivate16serviceForHandleEt
inline QSharedPointer<QLowEnergyServicePrivate> QLowEnergyControllerPrivate::serviceForHandle(
        QLowEnergyHandle handle)
{
    ServiceDataMap &currentList = serviceList;
    if (role == QLowEnergyController::PeripheralRole)
        currentList = localServices;

    const QList<QSharedPointer<QLowEnergyServicePrivate>> values = currentList.values();
    for (const auto &service: values) {
        if (service->startHandle <= handle && handle <= service->endHandle)
            return service;
    }

    return QSharedPointer<QLowEnergyServicePrivate>();
}

//  from ../qtconnectivity/src/bluetooth/qlowenergycontrollerbase.cpp, line 134, as _ZN27QLowEnergyControllerPrivate23characteristicForHandleEt
inline QLowEnergyCharacteristic QLowEnergyControllerPrivate::characteristicForHandle(
        QLowEnergyHandle handle)
{
    QSharedPointer<QLowEnergyServicePrivate> service = serviceForHandle(handle);
    if (service.isNull())
        return QLowEnergyCharacteristic();

    if (service->characteristicList.isEmpty())
        return QLowEnergyCharacteristic();

    // check whether it is the handle of a characteristic header
    if (service->characteristicList.contains(handle))
        return QLowEnergyCharacteristic(service, handle);

    // check whether it is the handle of the characteristic value or its descriptors
    QList<QLowEnergyHandle> charHandles = service->characteristicList.keys();
    std::sort(charHandles.begin(), charHandles.end());
    for (qsizetype i = charHandles.size() - 1; i >= 0; --i) {
        if (charHandles.at(i) > handle)
            continue;

        return QLowEnergyCharacteristic(service, charHandles.at(i));
    }

    return QLowEnergyCharacteristic();
}

//  from ../qtconnectivity/src/bluetooth/qlowenergycontrollerbase.cpp, line 165, as _ZN27QLowEnergyControllerPrivate19descriptorForHandleEt
inline QLowEnergyDescriptor QLowEnergyControllerPrivate::descriptorForHandle(
        QLowEnergyHandle handle)
{
    const QLowEnergyCharacteristic matchingChar = characteristicForHandle(handle);
    if (!matchingChar.isValid())
        return QLowEnergyDescriptor();

    const QLowEnergyServicePrivate::CharData charData = matchingChar.
            d_ptr->characteristicList[matchingChar.attributeHandle()];

    if (charData.descriptorList.contains(handle))
        return QLowEnergyDescriptor(matchingChar.d_ptr, matchingChar.attributeHandle(),
                                    handle);

    return QLowEnergyDescriptor();
}

//  from ../qtconnectivity/src/bluetooth/qlowenergycontrollerbase.cpp, line 185, as _ZN27QLowEnergyControllerPrivate27updateValueOfCharacteristicEtRK10QByteArrayb
inline quint16 QLowEnergyControllerPrivate::updateValueOfCharacteristic(
        QLowEnergyHandle charHandle,const QByteArray &value, bool appendValue)
{
    QSharedPointer<QLowEnergyServicePrivate> service = serviceForHandle(charHandle);
    if (!service.isNull()) {
        CharacteristicDataMap::iterator charIt = service->characteristicList.find(charHandle);
        if (charIt != service->characteristicList.end()) {
            QLowEnergyServicePrivate::CharData &charDetails = charIt.value();

            if (appendValue)
                charDetails.value += value;
            else
                charDetails.value = value;

            return charDetails.value.size();
        }
    }

    return 0;
}

//  from ../qtconnectivity/src/bluetooth/qlowenergycontrollerbase.cpp, line 209, as _ZN27QLowEnergyControllerPrivate23updateValueOfDescriptorEttRK10QByteArrayb
inline quint16 QLowEnergyControllerPrivate::updateValueOfDescriptor(
        QLowEnergyHandle charHandle, QLowEnergyHandle descriptorHandle,
        const QByteArray &value, bool appendValue)
{
    QSharedPointer<QLowEnergyServicePrivate> service = serviceForHandle(charHandle);
    if (!service.isNull()) {
        CharacteristicDataMap::iterator charIt = service->characteristicList.find(charHandle);
        if (charIt != service->characteristicList.end()) {
            QLowEnergyServicePrivate::CharData &charDetails = charIt.value();

            DescriptorDataMap::iterator descIt = charDetails.descriptorList.find(descriptorHandle);
            if (descIt != charDetails.descriptorList.end()) {
                QLowEnergyServicePrivate::DescData &descDetails = descIt.value();

                if (appendValue)
                    descDetails.value += value;
                else
                    descDetails.value = value;

                return descDetails.value.size();
            }
        }
    }

    return 0;
}
//  -----------------------------------------------------------------------

//  A QLowEnergyControllerPrivate that Python can take functions over in. Every QLowEnergyControllerPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQLowEnergyControllerPrivateCall0)(const void *, int *);
typedef void (*CuteQLowEnergyControllerPrivateCall1)(const void *, int *);
typedef void (*CuteQLowEnergyControllerPrivateCall2)(const void *, int *);
typedef void (*CuteQLowEnergyControllerPrivateCall3)(const void *, int *);
typedef void (*CuteQLowEnergyControllerPrivateCall4)(const void *, const QBluetoothUuid *, int, int *);
typedef void (*CuteQLowEnergyControllerPrivateCall5)(const void *, const QLowEnergyAdvertisingParameters *, const QLowEnergyAdvertisingData *, const QLowEnergyAdvertisingData *, int *);
typedef void (*CuteQLowEnergyControllerPrivateCall6)(const void *, int *);
typedef void (*CuteQLowEnergyControllerPrivateCall7)(const void *, const QLowEnergyConnectionParameters *, int *);
typedef void (*CuteQLowEnergyControllerPrivateCall8)(const void *, const QLowEnergyServiceData *, QLowEnergyHandle, int *);
typedef int (*CuteQLowEnergyControllerPrivateCall9)(const void *, int *);
typedef void (*CuteQLowEnergyControllerPrivateCall10)(const void *, int *);
typedef void * (*CuteQLowEnergyControllerPrivateCall11)(const void *, const QLowEnergyServiceData *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQLowEnergyControllerPrivateCall12)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQLowEnergyControllerPrivateCall13)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLowEnergyControllerPrivateCall14)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLowEnergyControllerPrivateCall15)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLowEnergyControllerPrivateCall16)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLowEnergyControllerPrivateCall17)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLowEnergyControllerPrivateCall18)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQLowEnergyControllerPrivate : public QLowEnergyControllerPrivate {
public:
  using QLowEnergyControllerPrivate::QLowEnergyControllerPrivate;
  void *taken[19] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN27QLowEnergyControllerPrivate4initEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN27QLowEnergyControllerPrivate15connectToDeviceEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN27QLowEnergyControllerPrivate20disconnectFromDeviceEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN27QLowEnergyControllerPrivate16discoverServicesEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN27QLowEnergyControllerPrivate22discoverServiceDetailsERK14QBluetoothUuidN17QLowEnergyService13DiscoveryModeE")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN27QLowEnergyControllerPrivate16startAdvertisingERK31QLowEnergyAdvertisingParametersRK25QLowEnergyAdvertisingDataS5_")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN27QLowEnergyControllerPrivate15stopAdvertisingEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN27QLowEnergyControllerPrivate23requestConnectionUpdateERK30QLowEnergyConnectionParameters")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN27QLowEnergyControllerPrivate25addToGenericAttributeListERK21QLowEnergyServiceDatat")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK27QLowEnergyControllerPrivate3mtuEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN27QLowEnergyControllerPrivate8readRssiEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN27QLowEnergyControllerPrivate16addServiceHelperERK21QLowEnergyServiceData")) {
      taken[11] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[13] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[14] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[15] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[16] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[17] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[18] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QLowEnergyControllerPrivate::init()
  void init() override {
    if (taken[0]) {
      int handled = 0;
      CuteQLowEnergyControllerPrivateCall0 call = reinterpret_cast<CuteQLowEnergyControllerPrivateCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QLowEnergyControllerPrivate::connectToDevice()
  void connectToDevice() override {
    if (taken[1]) {
      int handled = 0;
      CuteQLowEnergyControllerPrivateCall1 call = reinterpret_cast<CuteQLowEnergyControllerPrivateCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QLowEnergyControllerPrivate::disconnectFromDevice()
  void disconnectFromDevice() override {
    if (taken[2]) {
      int handled = 0;
      CuteQLowEnergyControllerPrivateCall2 call = reinterpret_cast<CuteQLowEnergyControllerPrivateCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QLowEnergyControllerPrivate::discoverServices()
  void discoverServices() override {
    if (taken[3]) {
      int handled = 0;
      CuteQLowEnergyControllerPrivateCall3 call = reinterpret_cast<CuteQLowEnergyControllerPrivateCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QLowEnergyControllerPrivate::discoverServiceDetails(const
  //      QBluetoothUuid &service, QLowEnergyService::DiscoveryMode mode)
  void discoverServiceDetails(
      const QBluetoothUuid &service,
      QLowEnergyService::DiscoveryMode mode) override {
    if (taken[4]) {
      int handled = 0;
      CuteQLowEnergyControllerPrivateCall4 call = reinterpret_cast<CuteQLowEnergyControllerPrivateCall4>(taken[4]);
      call(this, &service, static_cast<int>(mode), &handled);
      if (handled) return;
    }
  }

  //  void QLowEnergyControllerPrivate::startAdvertising(const
  //      QLowEnergyAdvertisingParameters &params, const
  //      QLowEnergyAdvertisingData &advertisingData, const
  //      QLowEnergyAdvertisingData &scanResponseData)
  void startAdvertising(
      const QLowEnergyAdvertisingParameters &params,
      const QLowEnergyAdvertisingData &advertisingData,
      const QLowEnergyAdvertisingData &scanResponseData) override {
    if (taken[5]) {
      int handled = 0;
      CuteQLowEnergyControllerPrivateCall5 call = reinterpret_cast<CuteQLowEnergyControllerPrivateCall5>(taken[5]);
      call(this, &params, &advertisingData, &scanResponseData, &handled);
      if (handled) return;
    }
  }

  //  void QLowEnergyControllerPrivate::stopAdvertising()
  void stopAdvertising() override {
    if (taken[6]) {
      int handled = 0;
      CuteQLowEnergyControllerPrivateCall6 call = reinterpret_cast<CuteQLowEnergyControllerPrivateCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QLowEnergyControllerPrivate::requestConnectionUpdate(const
  //      QLowEnergyConnectionParameters &params)
  void requestConnectionUpdate(
      const QLowEnergyConnectionParameters &params) override {
    if (taken[7]) {
      int handled = 0;
      CuteQLowEnergyControllerPrivateCall7 call = reinterpret_cast<CuteQLowEnergyControllerPrivateCall7>(taken[7]);
      call(this, &params, &handled);
      if (handled) return;
    }
  }

  //  void QLowEnergyControllerPrivate::addToGenericAttributeList(const
  //      QLowEnergyServiceData &service, QLowEnergyHandle startHandle)
  void addToGenericAttributeList(
      const QLowEnergyServiceData &service,
      QLowEnergyHandle startHandle) override {
    if (taken[8]) {
      int handled = 0;
      CuteQLowEnergyControllerPrivateCall8 call = reinterpret_cast<CuteQLowEnergyControllerPrivateCall8>(taken[8]);
      call(this, &service, startHandle, &handled);
      if (handled) return;
    }
  }

  //  int QLowEnergyControllerPrivate::mtu() const
  int mtu() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQLowEnergyControllerPrivateCall9 call = reinterpret_cast<CuteQLowEnergyControllerPrivateCall9>(taken[9]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QLowEnergyControllerPrivate::readRssi()
  void readRssi() override {
    if (taken[10]) {
      int handled = 0;
      CuteQLowEnergyControllerPrivateCall10 call = reinterpret_cast<CuteQLowEnergyControllerPrivateCall10>(taken[10]);
      call(this, &handled);
      if (handled) return;
    }
    QLowEnergyControllerPrivate::readRssi();
  }

  //  QLowEnergyService
  //      *QLowEnergyControllerPrivate::addServiceHelper(const
  //      QLowEnergyServiceData &service)
  QLowEnergyService *addServiceHelper(
      const QLowEnergyServiceData &service) override {
    if (taken[11]) {
      int handled = 0;
      CuteQLowEnergyControllerPrivateCall11 call = reinterpret_cast<CuteQLowEnergyControllerPrivateCall11>(taken[11]);
      void * given = call(this, &service, &handled);
      if (handled) return static_cast<QLowEnergyService *>(given);
    }
    return QLowEnergyControllerPrivate::addServiceHelper(service);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQLowEnergyControllerPrivateCall12 call = reinterpret_cast<CuteQLowEnergyControllerPrivateCall12>(taken[12]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQLowEnergyControllerPrivateCall13 call = reinterpret_cast<CuteQLowEnergyControllerPrivateCall13>(taken[13]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQLowEnergyControllerPrivateCall14 call = reinterpret_cast<CuteQLowEnergyControllerPrivateCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQLowEnergyControllerPrivateCall15 call = reinterpret_cast<CuteQLowEnergyControllerPrivateCall15>(taken[15]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQLowEnergyControllerPrivateCall16 call = reinterpret_cast<CuteQLowEnergyControllerPrivateCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[17]) {
      int handled = 0;
      CuteQLowEnergyControllerPrivateCall17 call = reinterpret_cast<CuteQLowEnergyControllerPrivateCall17>(taken[17]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[18]) {
      int handled = 0;
      CuteQLowEnergyControllerPrivateCall18 call = reinterpret_cast<CuteQLowEnergyControllerPrivateCall18>(taken[18]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QLowEnergyControllerPrivate::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK27QLowEnergyControllerPrivate10metaObjectEv(
    const QLowEnergyControllerPrivate *self) {
  return self->metaObject();
}

//  void *QLowEnergyControllerPrivate::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN27QLowEnergyControllerPrivate11qt_metacastEPKc(
    QLowEnergyControllerPrivate *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QLowEnergyControllerPrivate::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN27QLowEnergyControllerPrivate11qt_metacallEN11QMetaObject4CallEiPPv(
    QLowEnergyControllerPrivate *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QLowEnergyControllerPrivate::~QLowEnergyControllerPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QLowEnergyControllerPrivateD1Ev(
    QLowEnergyControllerPrivate *self) {
  delete self;
}

//  void QLowEnergyControllerPrivate::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QLowEnergyControllerPrivate4initEv(
    QLowEnergyControllerPrivate *self) {
  self->init();
}

//  void QLowEnergyControllerPrivate::connectToDevice()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QLowEnergyControllerPrivate15connectToDeviceEv(
    QLowEnergyControllerPrivate *self) {
  self->connectToDevice();
}

//  void QLowEnergyControllerPrivate::disconnectFromDevice()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QLowEnergyControllerPrivate20disconnectFromDeviceEv(
    QLowEnergyControllerPrivate *self) {
  self->disconnectFromDevice();
}

//  void QLowEnergyControllerPrivate::discoverServices()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QLowEnergyControllerPrivate16discoverServicesEv(
    QLowEnergyControllerPrivate *self) {
  self->discoverServices();
}

//  void QLowEnergyControllerPrivate::discoverServiceDetails(const
//      QBluetoothUuid &service, QLowEnergyService::DiscoveryMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QLowEnergyControllerPrivate22discoverServiceDetailsERK14QBluetoothUuidN17QLowEnergyService13DiscoveryModeE(
    QLowEnergyControllerPrivate *self,
    const QBluetoothUuid *service,
    QLowEnergyService::DiscoveryMode mode) {
  self->discoverServiceDetails(*service, mode);
}

//  void QLowEnergyControllerPrivate::readCharacteristic(const
//      QSharedPointer<QLowEnergyServicePrivate> service, const
//      QLowEnergyHandle charHandle)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QLowEnergyControllerPrivate18readCharacteristicE14QSharedPointerI24QLowEnergyServicePrivateEt(
    QLowEnergyControllerPrivate *self,
    const QSharedPointer<QLowEnergyServicePrivate> *service,
    QLowEnergyHandle charHandle) {
  self->readCharacteristic(*service, charHandle);
}

//  void QLowEnergyControllerPrivate::readDescriptor(const
//      QSharedPointer<QLowEnergyServicePrivate> service, const
//      QLowEnergyHandle charHandle, const QLowEnergyHandle descriptorHandle)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QLowEnergyControllerPrivate14readDescriptorE14QSharedPointerI24QLowEnergyServicePrivateEtt(
    QLowEnergyControllerPrivate *self,
    const QSharedPointer<QLowEnergyServicePrivate> *service,
    QLowEnergyHandle charHandle,
    QLowEnergyHandle descriptorHandle) {
  self->readDescriptor(*service, charHandle, descriptorHandle);
}

//  void QLowEnergyControllerPrivate::writeCharacteristic(const
//      QSharedPointer<QLowEnergyServicePrivate> service, const
//      QLowEnergyHandle charHandle, const QByteArray &newValue,
//      QLowEnergyService::WriteMode writeMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QLowEnergyControllerPrivate19writeCharacteristicE14QSharedPointerI24QLowEnergyServicePrivateEtRK10QByteArrayN17QLowEnergyService9WriteModeE(
    QLowEnergyControllerPrivate *self,
    const QSharedPointer<QLowEnergyServicePrivate> *service,
    QLowEnergyHandle charHandle,
    const QByteArray *newValue,
    QLowEnergyService::WriteMode writeMode) {
  self->writeCharacteristic(*service, charHandle, *newValue, writeMode);
}

//  void QLowEnergyControllerPrivate::writeDescriptor(const
//      QSharedPointer<QLowEnergyServicePrivate> service, const
//      QLowEnergyHandle charHandle, const QLowEnergyHandle descriptorHandle,
//      const QByteArray &newValue)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QLowEnergyControllerPrivate15writeDescriptorE14QSharedPointerI24QLowEnergyServicePrivateEttRK10QByteArray(
    QLowEnergyControllerPrivate *self,
    const QSharedPointer<QLowEnergyServicePrivate> *service,
    QLowEnergyHandle charHandle,
    QLowEnergyHandle descriptorHandle,
    const QByteArray *newValue) {
  self->writeDescriptor(*service, charHandle, descriptorHandle, *newValue);
}

//  void QLowEnergyControllerPrivate::startAdvertising(const
//      QLowEnergyAdvertisingParameters &params, const
//      QLowEnergyAdvertisingData &advertisingData, const
//      QLowEnergyAdvertisingData &scanResponseData)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QLowEnergyControllerPrivate16startAdvertisingERK31QLowEnergyAdvertisingParametersRK25QLowEnergyAdvertisingDataS5_(
    QLowEnergyControllerPrivate *self,
    const QLowEnergyAdvertisingParameters *params,
    const QLowEnergyAdvertisingData *advertisingData,
    const QLowEnergyAdvertisingData *scanResponseData) {
  self->startAdvertising(*params, *advertisingData, *scanResponseData);
}

//  void QLowEnergyControllerPrivate::stopAdvertising()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QLowEnergyControllerPrivate15stopAdvertisingEv(
    QLowEnergyControllerPrivate *self) {
  self->stopAdvertising();
}

//  void QLowEnergyControllerPrivate::requestConnectionUpdate(const
//      QLowEnergyConnectionParameters &params)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QLowEnergyControllerPrivate23requestConnectionUpdateERK30QLowEnergyConnectionParameters(
    QLowEnergyControllerPrivate *self,
    const QLowEnergyConnectionParameters *params) {
  self->requestConnectionUpdate(*params);
}

//  void QLowEnergyControllerPrivate::addToGenericAttributeList(const
//      QLowEnergyServiceData &service, QLowEnergyHandle startHandle)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QLowEnergyControllerPrivate25addToGenericAttributeListERK21QLowEnergyServiceDatat(
    QLowEnergyControllerPrivate *self,
    const QLowEnergyServiceData *service,
    QLowEnergyHandle startHandle) {
  self->addToGenericAttributeList(*service, startHandle);
}

//  int QLowEnergyControllerPrivate::mtu() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK27QLowEnergyControllerPrivate3mtuEv(
    const QLowEnergyControllerPrivate *self) {
  return self->mtu();
}

//  void QLowEnergyControllerPrivate::readRssi()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QLowEnergyControllerPrivate8readRssiEv(
    QLowEnergyControllerPrivate *self) {
  self->readRssi();
}

//  QLowEnergyService *QLowEnergyControllerPrivate::addServiceHelper(const
//      QLowEnergyServiceData &service)
extern "C" Q_DECL_EXPORT
QLowEnergyService *ritual_ZN27QLowEnergyControllerPrivate16addServiceHelperERK21QLowEnergyServiceData(
    QLowEnergyControllerPrivate *self,
    const QLowEnergyServiceData *service) {
  return self->addServiceHelper(*service);
}

#if defined(Q_OS_LINUX)
//  bool QLowEnergyControllerPrivate::isValidLocalAdapter()
extern "C" Q_DECL_EXPORT
bool ritual_ZN27QLowEnergyControllerPrivate19isValidLocalAdapterEv(
    QLowEnergyControllerPrivate *self) {
  return self->isValidLocalAdapter();
}
#endif  // defined(Q_OS_LINUX)

//  void QLowEnergyControllerPrivate::setError(QLowEnergyController::Error
//      newError)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QLowEnergyControllerPrivate8setErrorEN20QLowEnergyController5ErrorE(
    QLowEnergyControllerPrivate *self,
    QLowEnergyController::Error newError) {
  self->setError(newError);
}

//  QSharedPointer<QLowEnergyServicePrivate>
//      QLowEnergyControllerPrivate::serviceForHandle(QLowEnergyHandle
//      handle)
extern "C" Q_DECL_EXPORT
QSharedPointer<QLowEnergyServicePrivate> *ritual_ZN27QLowEnergyControllerPrivate16serviceForHandleEt(
    QLowEnergyControllerPrivate *self,
    QLowEnergyHandle handle) {
  return new QSharedPointer<QLowEnergyServicePrivate>(
      self->serviceForHandle(
          handle));
}

//  QLowEnergyCharacteristic
//      QLowEnergyControllerPrivate::characteristicForHandle(QLowEnergyHandle
//      handle)
extern "C" Q_DECL_EXPORT
QLowEnergyCharacteristic *ritual_ZN27QLowEnergyControllerPrivate23characteristicForHandleEt(
    QLowEnergyControllerPrivate *self,
    QLowEnergyHandle handle) {
  return new QLowEnergyCharacteristic(self->characteristicForHandle(handle));
}

//  QLowEnergyDescriptor
//      QLowEnergyControllerPrivate::descriptorForHandle(QLowEnergyHandle
//      handle)
extern "C" Q_DECL_EXPORT
QLowEnergyDescriptor *ritual_ZN27QLowEnergyControllerPrivate19descriptorForHandleEt(
    QLowEnergyControllerPrivate *self,
    QLowEnergyHandle handle) {
  return new QLowEnergyDescriptor(self->descriptorForHandle(handle));
}

//  quint16
//      QLowEnergyControllerPrivate::updateValueOfCharacteristic(QLowEnergyHa
//      ndle charHandle, const QByteArray &value, bool appendValue)
extern "C" Q_DECL_EXPORT
quint16 ritual_ZN27QLowEnergyControllerPrivate27updateValueOfCharacteristicEtRK10QByteArrayb(
    QLowEnergyControllerPrivate *self,
    QLowEnergyHandle charHandle,
    const QByteArray *value,
    bool appendValue) {
  return self->updateValueOfCharacteristic(charHandle, *value, appendValue);
}

//  quint16
//      QLowEnergyControllerPrivate::updateValueOfDescriptor(QLowEnergyHandle
//      charHandle, QLowEnergyHandle descriptorHandle, const QByteArray
//      &value, bool appendValue)
extern "C" Q_DECL_EXPORT
quint16 ritual_ZN27QLowEnergyControllerPrivate23updateValueOfDescriptorEttRK10QByteArrayb(
    QLowEnergyControllerPrivate *self,
    QLowEnergyHandle charHandle,
    QLowEnergyHandle descriptorHandle,
    const QByteArray *value,
    bool appendValue) {
  return self->updateValueOfDescriptor(
      charHandle,
      descriptorHandle,
      *value,
      appendValue);
}

//  QLowEnergyController *QLowEnergyControllerPrivate::q_func()
extern "C" Q_DECL_EXPORT
QLowEnergyController *ritual_ZN27QLowEnergyControllerPrivate6q_funcEv(
    QLowEnergyControllerPrivate *self) {
  return self->q_func();
}

//  const QLowEnergyController *QLowEnergyControllerPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QLowEnergyController *ritual_ZNK27QLowEnergyControllerPrivate6q_funcEv(
    const QLowEnergyControllerPrivate *self) {
  return self->q_func();
}

//  a Python function taken by a CuteQLowEnergyControllerPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QLowEnergyControllerPrivate(
    QLowEnergyControllerPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQLowEnergyControllerPrivate *>(self)->take(key, call);
}

//  a QSharedPointer<QLowEnergyServicePrivate> a ritual of
//      QLowEnergyControllerPrivate gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QLowEnergyControllerPrivate__QSharedPointer_QLowEnergyServicePrivate(
    QSharedPointer<QLowEnergyServicePrivate> *self) {
  delete self;
}
