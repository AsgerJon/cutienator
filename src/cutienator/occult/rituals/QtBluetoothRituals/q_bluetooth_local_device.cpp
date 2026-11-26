//  Written by dev_tooling.RitualGenerator from the records of
//  QtBluetooth/qbluetoothlocaldevice.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtBluetooth/qbluetoothlocaldevice.h>
#include <QtCore/qstring.h>
#include <QtBluetooth/qbluetoothaddress.h>
#include <QtBluetooth/qbluetoothhostinfo.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QBluetoothLocalDevice that Python can take functions over in. Every QBluetoothLocalDevice
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQBluetoothLocalDeviceCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQBluetoothLocalDeviceCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBluetoothLocalDeviceCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBluetoothLocalDeviceCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBluetoothLocalDeviceCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBluetoothLocalDeviceCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBluetoothLocalDeviceCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQBluetoothLocalDevice : public QBluetoothLocalDevice {
public:
  using QBluetoothLocalDevice::QBluetoothLocalDevice;
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
      CuteQBluetoothLocalDeviceCall0 call = reinterpret_cast<CuteQBluetoothLocalDeviceCall0>(taken[0]);
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
      CuteQBluetoothLocalDeviceCall1 call = reinterpret_cast<CuteQBluetoothLocalDeviceCall1>(taken[1]);
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
      CuteQBluetoothLocalDeviceCall2 call = reinterpret_cast<CuteQBluetoothLocalDeviceCall2>(taken[2]);
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
      CuteQBluetoothLocalDeviceCall3 call = reinterpret_cast<CuteQBluetoothLocalDeviceCall3>(taken[3]);
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
      CuteQBluetoothLocalDeviceCall4 call = reinterpret_cast<CuteQBluetoothLocalDeviceCall4>(taken[4]);
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
      CuteQBluetoothLocalDeviceCall5 call = reinterpret_cast<CuteQBluetoothLocalDeviceCall5>(taken[5]);
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
      CuteQBluetoothLocalDeviceCall6 call = reinterpret_cast<CuteQBluetoothLocalDeviceCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QBluetoothLocalDevice::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21QBluetoothLocalDevice10metaObjectEv(
    const QBluetoothLocalDevice *self) {
  return self->metaObject();
}

//  void *QBluetoothLocalDevice::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN21QBluetoothLocalDevice11qt_metacastEPKc(
    QBluetoothLocalDevice *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QBluetoothLocalDevice::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN21QBluetoothLocalDevice11qt_metacallEN11QMetaObject4CallEiPPv(
    QBluetoothLocalDevice *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QBluetoothLocalDevice::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN21QBluetoothLocalDevice2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QBluetoothLocalDevice::tr(s, c, n));
}

//  QBluetoothLocalDevice::QBluetoothLocalDevice(QObject *parent)
extern "C" Q_DECL_EXPORT
QBluetoothLocalDevice *ritual_ZN21QBluetoothLocalDeviceC1EP7QObject(
    QObject *parent) {
  return new CuteQBluetoothLocalDevice(parent);
}

//  QBluetoothLocalDevice::QBluetoothLocalDevice(const QBluetoothAddress
//      &address, QObject *parent)
extern "C" Q_DECL_EXPORT
QBluetoothLocalDevice *ritual_ZN21QBluetoothLocalDeviceC1ERK17QBluetoothAddressP7QObject(
    const QBluetoothAddress *address,
    QObject *parent) {
  return new CuteQBluetoothLocalDevice(*address, parent);
}

//  QBluetoothLocalDevice::~QBluetoothLocalDevice()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QBluetoothLocalDeviceD1Ev(QBluetoothLocalDevice *self) {
  delete self;
}

//  bool QBluetoothLocalDevice::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QBluetoothLocalDevice7isValidEv(
    const QBluetoothLocalDevice *self) {
  return self->isValid();
}

//  void QBluetoothLocalDevice::requestPairing(const QBluetoothAddress
//      &address, Pairing pairing)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QBluetoothLocalDevice14requestPairingERK17QBluetoothAddressNS_7PairingE(
    QBluetoothLocalDevice *self,
    const QBluetoothAddress *address,
    QBluetoothLocalDevice::Pairing pairing) {
  self->requestPairing(*address, pairing);
}

//  Pairing QBluetoothLocalDevice::pairingStatus(const QBluetoothAddress
//      &address) const
extern "C" Q_DECL_EXPORT
QBluetoothLocalDevice::Pairing ritual_ZNK21QBluetoothLocalDevice13pairingStatusERK17QBluetoothAddress(
    const QBluetoothLocalDevice *self,
    const QBluetoothAddress *address) {
  return self->pairingStatus(*address);
}

//  void QBluetoothLocalDevice::setHostMode(QBluetoothLocalDevice::HostMode
//      mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QBluetoothLocalDevice11setHostModeENS_8HostModeE(
    QBluetoothLocalDevice *self,
    QBluetoothLocalDevice::HostMode mode) {
  self->setHostMode(mode);
}

//  HostMode QBluetoothLocalDevice::hostMode() const
extern "C" Q_DECL_EXPORT
QBluetoothLocalDevice::HostMode ritual_ZNK21QBluetoothLocalDevice8hostModeEv(
    const QBluetoothLocalDevice *self) {
  return self->hostMode();
}

//  QList<QBluetoothAddress> QBluetoothLocalDevice::connectedDevices() const
extern "C" Q_DECL_EXPORT
QList<QBluetoothAddress> *ritual_ZNK21QBluetoothLocalDevice16connectedDevicesEv(
    const QBluetoothLocalDevice *self) {
  return new QList<QBluetoothAddress>(self->connectedDevices());
}

//  void QBluetoothLocalDevice::powerOn()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QBluetoothLocalDevice7powerOnEv(
    QBluetoothLocalDevice *self) {
  self->powerOn();
}

//  QString QBluetoothLocalDevice::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK21QBluetoothLocalDevice4nameEv(
    const QBluetoothLocalDevice *self) {
  return new QString(self->name());
}

//  QBluetoothAddress QBluetoothLocalDevice::address() const
extern "C" Q_DECL_EXPORT
QBluetoothAddress *ritual_ZNK21QBluetoothLocalDevice7addressEv(
    const QBluetoothLocalDevice *self) {
  return new QBluetoothAddress(self->address());
}

//  QList<QBluetoothHostInfo> QBluetoothLocalDevice::allDevices()
extern "C" Q_DECL_EXPORT
QList<QBluetoothHostInfo> *ritual_ZN21QBluetoothLocalDevice10allDevicesEv() {
  return new QList<QBluetoothHostInfo>(QBluetoothLocalDevice::allDevices());
}

//  void QBluetoothLocalDevice::hostModeStateChanged(QBluetoothLocalDevice::H
//      ostMode state)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QBluetoothLocalDevice20hostModeStateChangedENS_8HostModeE(
    QBluetoothLocalDevice *self,
    QBluetoothLocalDevice::HostMode state) {
  self->hostModeStateChanged(state);
}

//  void QBluetoothLocalDevice::deviceConnected(const QBluetoothAddress
//      &address)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QBluetoothLocalDevice15deviceConnectedERK17QBluetoothAddress(
    QBluetoothLocalDevice *self,
    const QBluetoothAddress *address) {
  self->deviceConnected(*address);
}

//  void QBluetoothLocalDevice::deviceDisconnected(const QBluetoothAddress
//      &address)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QBluetoothLocalDevice18deviceDisconnectedERK17QBluetoothAddress(
    QBluetoothLocalDevice *self,
    const QBluetoothAddress *address) {
  self->deviceDisconnected(*address);
}

//  void QBluetoothLocalDevice::pairingFinished(const QBluetoothAddress
//      &address, QBluetoothLocalDevice::Pairing pairing)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QBluetoothLocalDevice15pairingFinishedERK17QBluetoothAddressNS_7PairingE(
    QBluetoothLocalDevice *self,
    const QBluetoothAddress *address,
    QBluetoothLocalDevice::Pairing pairing) {
  self->pairingFinished(*address, pairing);
}

//  void QBluetoothLocalDevice::errorOccurred(QBluetoothLocalDevice::Error
//      error)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QBluetoothLocalDevice13errorOccurredENS_5ErrorE(
    QBluetoothLocalDevice *self,
    QBluetoothLocalDevice::Error error) {
  self->errorOccurred(error);
}

//  QBluetoothLocalDevicePrivate *QBluetoothLocalDevice::d_func()
extern "C" Q_DECL_EXPORT
QBluetoothLocalDevicePrivate *ritual_ZN21QBluetoothLocalDevice6d_funcEv(
    QBluetoothLocalDevice *self) {
  return self->d_func();
}

//  const QBluetoothLocalDevicePrivate *QBluetoothLocalDevice::d_func() const
extern "C" Q_DECL_EXPORT
const QBluetoothLocalDevicePrivate *ritual_ZNK21QBluetoothLocalDevice6d_funcEv(
    const QBluetoothLocalDevice *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQBluetoothLocalDevice, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QBluetoothLocalDevice(
    QBluetoothLocalDevice *self,
    const char *key,
    void *call) {
  return static_cast<CuteQBluetoothLocalDevice *>(self)->take(key, call);
}
