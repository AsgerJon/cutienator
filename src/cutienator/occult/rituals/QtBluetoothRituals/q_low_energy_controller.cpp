//  Written by dev_tooling.RitualGenerator from the records of
//  QtBluetooth/qlowenergycontroller.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtBluetooth/qlowenergycontroller.h>
#include <QtCore/qstring.h>
#include <QtBluetooth/qbluetoothdeviceinfo.h>
#include <QtBluetooth/qbluetoothaddress.h>
#include <QtBluetooth/qbluetoothuuid.h>
#include <QtBluetooth/qlowenergyadvertisingparameters.h>
#include <QtBluetooth/qlowenergyadvertisingdata.h>
#include <QtBluetooth/qlowenergyservicedata.h>
#include <QtBluetooth/qlowenergyconnectionparameters.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QLowEnergyController that Python can take functions over in. Every QLowEnergyController
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQLowEnergyControllerCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQLowEnergyControllerCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLowEnergyControllerCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLowEnergyControllerCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLowEnergyControllerCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLowEnergyControllerCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLowEnergyControllerCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQLowEnergyController : public QLowEnergyController {
public:
  using QLowEnergyController::QLowEnergyController;
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
      CuteQLowEnergyControllerCall0 call = reinterpret_cast<CuteQLowEnergyControllerCall0>(taken[0]);
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
      CuteQLowEnergyControllerCall1 call = reinterpret_cast<CuteQLowEnergyControllerCall1>(taken[1]);
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
      CuteQLowEnergyControllerCall2 call = reinterpret_cast<CuteQLowEnergyControllerCall2>(taken[2]);
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
      CuteQLowEnergyControllerCall3 call = reinterpret_cast<CuteQLowEnergyControllerCall3>(taken[3]);
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
      CuteQLowEnergyControllerCall4 call = reinterpret_cast<CuteQLowEnergyControllerCall4>(taken[4]);
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
      CuteQLowEnergyControllerCall5 call = reinterpret_cast<CuteQLowEnergyControllerCall5>(taken[5]);
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
      CuteQLowEnergyControllerCall6 call = reinterpret_cast<CuteQLowEnergyControllerCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QLowEnergyController::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20QLowEnergyController10metaObjectEv(
    const QLowEnergyController *self) {
  return self->metaObject();
}

//  void *QLowEnergyController::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN20QLowEnergyController11qt_metacastEPKc(
    QLowEnergyController *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QLowEnergyController::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN20QLowEnergyController11qt_metacallEN11QMetaObject4CallEiPPv(
    QLowEnergyController *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QLowEnergyController::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN20QLowEnergyController2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QLowEnergyController::tr(s, c, n));
}

//  QLowEnergyController *QLowEnergyController::createCentral(const
//      QBluetoothDeviceInfo &remoteDevice, QObject *parent)
extern "C" Q_DECL_EXPORT
QLowEnergyController *ritual_ZN20QLowEnergyController13createCentralERK20QBluetoothDeviceInfoP7QObject(
    const QBluetoothDeviceInfo *remoteDevice,
    QObject *parent) {
  return QLowEnergyController::createCentral(*remoteDevice, parent);
}

//  QLowEnergyController *QLowEnergyController::createCentral(const
//      QBluetoothDeviceInfo &remoteDevice, const QBluetoothAddress
//      &localDevice, QObject *parent)
extern "C" Q_DECL_EXPORT
QLowEnergyController *ritual_ZN20QLowEnergyController13createCentralERK20QBluetoothDeviceInfoRK17QBluetoothAddressP7QObject(
    const QBluetoothDeviceInfo *remoteDevice,
    const QBluetoothAddress *localDevice,
    QObject *parent) {
  return QLowEnergyController::createCentral(
      *remoteDevice,
      *localDevice,
      parent);
}

//  QLowEnergyController *QLowEnergyController::createPeripheral(const
//      QBluetoothAddress &localDevice, QObject *parent)
extern "C" Q_DECL_EXPORT
QLowEnergyController *ritual_ZN20QLowEnergyController16createPeripheralERK17QBluetoothAddressP7QObject(
    const QBluetoothAddress *localDevice,
    QObject *parent) {
  return QLowEnergyController::createPeripheral(*localDevice, parent);
}

//  QLowEnergyController *QLowEnergyController::createPeripheral(QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QLowEnergyController *ritual_ZN20QLowEnergyController16createPeripheralEP7QObject(
    QObject *parent) {
  return QLowEnergyController::createPeripheral(parent);
}

//  QLowEnergyController::~QLowEnergyController()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QLowEnergyControllerD1Ev(QLowEnergyController *self) {
  delete self;
}

//  QBluetoothAddress QLowEnergyController::localAddress() const
extern "C" Q_DECL_EXPORT
QBluetoothAddress *ritual_ZNK20QLowEnergyController12localAddressEv(
    const QLowEnergyController *self) {
  return new QBluetoothAddress(self->localAddress());
}

//  QBluetoothAddress QLowEnergyController::remoteAddress() const
extern "C" Q_DECL_EXPORT
QBluetoothAddress *ritual_ZNK20QLowEnergyController13remoteAddressEv(
    const QLowEnergyController *self) {
  return new QBluetoothAddress(self->remoteAddress());
}

//  QBluetoothUuid QLowEnergyController::remoteDeviceUuid() const
extern "C" Q_DECL_EXPORT
QBluetoothUuid *ritual_ZNK20QLowEnergyController16remoteDeviceUuidEv(
    const QLowEnergyController *self) {
  return new QBluetoothUuid(self->remoteDeviceUuid());
}

//  QString QLowEnergyController::remoteName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK20QLowEnergyController10remoteNameEv(
    const QLowEnergyController *self) {
  return new QString(self->remoteName());
}

//  ControllerState QLowEnergyController::state() const
extern "C" Q_DECL_EXPORT
QLowEnergyController::ControllerState ritual_ZNK20QLowEnergyController5stateEv(
    const QLowEnergyController *self) {
  return self->state();
}

//  RemoteAddressType QLowEnergyController::remoteAddressType() const
extern "C" Q_DECL_EXPORT
QLowEnergyController::RemoteAddressType ritual_ZNK20QLowEnergyController17remoteAddressTypeEv(
    const QLowEnergyController *self) {
  return self->remoteAddressType();
}

//  void QLowEnergyController::setRemoteAddressType(RemoteAddressType type)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QLowEnergyController20setRemoteAddressTypeENS_17RemoteAddressTypeE(
    QLowEnergyController *self,
    QLowEnergyController::RemoteAddressType type) {
  self->setRemoteAddressType(type);
}

//  void QLowEnergyController::connectToDevice()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QLowEnergyController15connectToDeviceEv(
    QLowEnergyController *self) {
  self->connectToDevice();
}

//  void QLowEnergyController::disconnectFromDevice()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QLowEnergyController20disconnectFromDeviceEv(
    QLowEnergyController *self) {
  self->disconnectFromDevice();
}

//  void QLowEnergyController::discoverServices()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QLowEnergyController16discoverServicesEv(
    QLowEnergyController *self) {
  self->discoverServices();
}

//  QList<QBluetoothUuid> QLowEnergyController::services() const
extern "C" Q_DECL_EXPORT
QList<QBluetoothUuid> *ritual_ZNK20QLowEnergyController8servicesEv(
    const QLowEnergyController *self) {
  return new QList<QBluetoothUuid>(self->services());
}

//  QLowEnergyService *QLowEnergyController::createServiceObject(const
//      QBluetoothUuid &service, QObject *parent)
extern "C" Q_DECL_EXPORT
QLowEnergyService *ritual_ZN20QLowEnergyController19createServiceObjectERK14QBluetoothUuidP7QObject(
    QLowEnergyController *self,
    const QBluetoothUuid *service,
    QObject *parent) {
  return self->createServiceObject(*service, parent);
}

//  void QLowEnergyController::startAdvertising(const
//      QLowEnergyAdvertisingParameters &parameters, const
//      QLowEnergyAdvertisingData &advertisingData, const
//      QLowEnergyAdvertisingData &scanResponseData)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QLowEnergyController16startAdvertisingERK31QLowEnergyAdvertisingParametersRK25QLowEnergyAdvertisingDataS5_(
    QLowEnergyController *self,
    const QLowEnergyAdvertisingParameters *parameters,
    const QLowEnergyAdvertisingData *advertisingData,
    const QLowEnergyAdvertisingData *scanResponseData) {
  self->startAdvertising(*parameters, *advertisingData, *scanResponseData);
}

//  void QLowEnergyController::stopAdvertising()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QLowEnergyController15stopAdvertisingEv(
    QLowEnergyController *self) {
  self->stopAdvertising();
}

//  QLowEnergyService *QLowEnergyController::addService(const
//      QLowEnergyServiceData &service, QObject *parent)
extern "C" Q_DECL_EXPORT
QLowEnergyService *ritual_ZN20QLowEnergyController10addServiceERK21QLowEnergyServiceDataP7QObject(
    QLowEnergyController *self,
    const QLowEnergyServiceData *service,
    QObject *parent) {
  return self->addService(*service, parent);
}

//  void QLowEnergyController::requestConnectionUpdate(const
//      QLowEnergyConnectionParameters &parameters)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QLowEnergyController23requestConnectionUpdateERK30QLowEnergyConnectionParameters(
    QLowEnergyController *self,
    const QLowEnergyConnectionParameters *parameters) {
  self->requestConnectionUpdate(*parameters);
}

//  Error QLowEnergyController::error() const
extern "C" Q_DECL_EXPORT
QLowEnergyController::Error ritual_ZNK20QLowEnergyController5errorEv(
    const QLowEnergyController *self) {
  return self->error();
}

//  QString QLowEnergyController::errorString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK20QLowEnergyController11errorStringEv(
    const QLowEnergyController *self) {
  return new QString(self->errorString());
}

//  Role QLowEnergyController::role() const
extern "C" Q_DECL_EXPORT
QLowEnergyController::Role ritual_ZNK20QLowEnergyController4roleEv(
    const QLowEnergyController *self) {
  return self->role();
}

//  int QLowEnergyController::mtu() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QLowEnergyController3mtuEv(
    const QLowEnergyController *self) {
  return self->mtu();
}

//  void QLowEnergyController::readRssi()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QLowEnergyController8readRssiEv(QLowEnergyController *self) {
  self->readRssi();
}

//  void QLowEnergyController::connected()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QLowEnergyController9connectedEv(
    QLowEnergyController *self) {
  self->connected();
}

//  void QLowEnergyController::disconnected()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QLowEnergyController12disconnectedEv(
    QLowEnergyController *self) {
  self->disconnected();
}

//  void
//      QLowEnergyController::stateChanged(QLowEnergyController::ControllerSt
//      ate state)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QLowEnergyController12stateChangedENS_15ControllerStateE(
    QLowEnergyController *self,
    QLowEnergyController::ControllerState state) {
  self->stateChanged(state);
}

//  void QLowEnergyController::errorOccurred(QLowEnergyController::Error
//      newError)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QLowEnergyController13errorOccurredENS_5ErrorE(
    QLowEnergyController *self,
    QLowEnergyController::Error newError) {
  self->errorOccurred(newError);
}

//  void QLowEnergyController::mtuChanged(int mtu)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QLowEnergyController10mtuChangedEi(
    QLowEnergyController *self,
    int mtu) {
  self->mtuChanged(mtu);
}

//  void QLowEnergyController::rssiRead(qint16 rssi)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QLowEnergyController8rssiReadEs(
    QLowEnergyController *self,
    qint16 rssi) {
  self->rssiRead(rssi);
}

//  void QLowEnergyController::serviceDiscovered(const QBluetoothUuid
//      &newService)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QLowEnergyController17serviceDiscoveredERK14QBluetoothUuid(
    QLowEnergyController *self,
    const QBluetoothUuid *newService) {
  self->serviceDiscovered(*newService);
}

//  void QLowEnergyController::discoveryFinished()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QLowEnergyController17discoveryFinishedEv(
    QLowEnergyController *self) {
  self->discoveryFinished();
}

//  void QLowEnergyController::connectionUpdated(const
//      QLowEnergyConnectionParameters &parameters)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QLowEnergyController17connectionUpdatedERK30QLowEnergyConnectionParameters(
    QLowEnergyController *self,
    const QLowEnergyConnectionParameters *parameters) {
  self->connectionUpdated(*parameters);
}

//  QLowEnergyController::QLowEnergyController(const QBluetoothAddress
//      &localDevice, QObject *parent)
extern "C" Q_DECL_EXPORT
QLowEnergyController *ritual_ZN20QLowEnergyControllerC1ERK17QBluetoothAddressP7QObject(
    const QBluetoothAddress *localDevice,
    QObject *parent) {
  return new CuteQLowEnergyController(*localDevice, parent);
}

//  QLowEnergyController::QLowEnergyController(const QBluetoothDeviceInfo
//      &remoteDevice, const QBluetoothAddress &localDevice, QObject *parent)
extern "C" Q_DECL_EXPORT
QLowEnergyController *ritual_ZN20QLowEnergyControllerC1ERK20QBluetoothDeviceInfoRK17QBluetoothAddressP7QObject(
    const QBluetoothDeviceInfo *remoteDevice,
    const QBluetoothAddress *localDevice,
    QObject *parent) {
  return new CuteQLowEnergyController(*remoteDevice, *localDevice, parent);
}

//  QLowEnergyControllerPrivate *QLowEnergyController::d_func()
extern "C" Q_DECL_EXPORT
QLowEnergyControllerPrivate *ritual_ZN20QLowEnergyController6d_funcEv(
    QLowEnergyController *self) {
  return self->d_func();
}

//  const QLowEnergyControllerPrivate *QLowEnergyController::d_func() const
extern "C" Q_DECL_EXPORT
const QLowEnergyControllerPrivate *ritual_ZNK20QLowEnergyController6d_funcEv(
    const QLowEnergyController *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQLowEnergyController, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QLowEnergyController(
    QLowEnergyController *self,
    const char *key,
    void *call) {
  return static_cast<CuteQLowEnergyController *>(self)->take(key, call);
}
