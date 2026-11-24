//  Written by dev_tooling.RitualGenerator from the records of
//  QtBluetooth/qlowenergyservice.h, Qt 6.12.0. Changes made here are lost.
#include <QtBluetooth/qlowenergyservice.h>
#include <QtCore/qstring.h>
#include <QtBluetooth/qbluetoothuuid.h>
#include <QtBluetooth/qlowenergycharacteristic.h>
#include <QtCore/qbytearray.h>
#include <QtBluetooth/qlowenergydescriptor.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QLowEnergyService that Python can take functions over in. Every QLowEnergyService
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQLowEnergyServiceCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQLowEnergyServiceCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLowEnergyServiceCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLowEnergyServiceCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLowEnergyServiceCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLowEnergyServiceCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLowEnergyServiceCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQLowEnergyService : public QLowEnergyService {
public:
  using QLowEnergyService::QLowEnergyService;
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
      CuteQLowEnergyServiceCall0 call = reinterpret_cast<CuteQLowEnergyServiceCall0>(taken[0]);
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
      CuteQLowEnergyServiceCall1 call = reinterpret_cast<CuteQLowEnergyServiceCall1>(taken[1]);
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
      CuteQLowEnergyServiceCall2 call = reinterpret_cast<CuteQLowEnergyServiceCall2>(taken[2]);
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
      CuteQLowEnergyServiceCall3 call = reinterpret_cast<CuteQLowEnergyServiceCall3>(taken[3]);
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
      CuteQLowEnergyServiceCall4 call = reinterpret_cast<CuteQLowEnergyServiceCall4>(taken[4]);
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
      CuteQLowEnergyServiceCall5 call = reinterpret_cast<CuteQLowEnergyServiceCall5>(taken[5]);
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
      CuteQLowEnergyServiceCall6 call = reinterpret_cast<CuteQLowEnergyServiceCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QLowEnergyService::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QLowEnergyService10metaObjectEv(
    const QLowEnergyService *self) {
  return self->metaObject();
}

//  QString QLowEnergyService::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QLowEnergyService2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QLowEnergyService::tr(s, c, n));
}

//  QLowEnergyService::~QLowEnergyService()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QLowEnergyServiceD1Ev(QLowEnergyService *self) {
  delete self;
}

//  QList<QBluetoothUuid> QLowEnergyService::includedServices() const
extern "C" Q_DECL_EXPORT
QList<QBluetoothUuid> *ritual_ZNK17QLowEnergyService16includedServicesEv(
    const QLowEnergyService *self) {
  return new QList<QBluetoothUuid>(self->includedServices());
}

//  QLowEnergyService::ServiceTypes QLowEnergyService::type() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QLowEnergyService4typeEv(const QLowEnergyService *self) {
  return static_cast<int>(self->type().toInt());
}

//  QLowEnergyService::ServiceState QLowEnergyService::state() const
extern "C" Q_DECL_EXPORT
QLowEnergyService::ServiceState ritual_ZNK17QLowEnergyService5stateEv(
    const QLowEnergyService *self) {
  return self->state();
}

//  QLowEnergyCharacteristic QLowEnergyService::characteristic(const
//      QBluetoothUuid &uuid) const
extern "C" Q_DECL_EXPORT
QLowEnergyCharacteristic *ritual_ZNK17QLowEnergyService14characteristicERK14QBluetoothUuid(
    const QLowEnergyService *self,
    const QBluetoothUuid *uuid) {
  return new QLowEnergyCharacteristic(self->characteristic(*uuid));
}

//  QList<QLowEnergyCharacteristic> QLowEnergyService::characteristics()
//      const
extern "C" Q_DECL_EXPORT
QList<QLowEnergyCharacteristic> *ritual_ZNK17QLowEnergyService15characteristicsEv(
    const QLowEnergyService *self) {
  return new QList<QLowEnergyCharacteristic>(self->characteristics());
}

//  QBluetoothUuid QLowEnergyService::serviceUuid() const
extern "C" Q_DECL_EXPORT
QBluetoothUuid *ritual_ZNK17QLowEnergyService11serviceUuidEv(
    const QLowEnergyService *self) {
  return new QBluetoothUuid(self->serviceUuid());
}

//  QString QLowEnergyService::serviceName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QLowEnergyService11serviceNameEv(
    const QLowEnergyService *self) {
  return new QString(self->serviceName());
}

//  void QLowEnergyService::discoverDetails(DiscoveryMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QLowEnergyService15discoverDetailsENS_13DiscoveryModeE(
    QLowEnergyService *self,
    QLowEnergyService::DiscoveryMode mode) {
  self->discoverDetails(mode);
}

//  ServiceError QLowEnergyService::error() const
extern "C" Q_DECL_EXPORT
QLowEnergyService::ServiceError ritual_ZNK17QLowEnergyService5errorEv(
    const QLowEnergyService *self) {
  return self->error();
}

//  bool QLowEnergyService::contains(const QLowEnergyCharacteristic
//      &characteristic) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QLowEnergyService8containsERK24QLowEnergyCharacteristic(
    const QLowEnergyService *self,
    const QLowEnergyCharacteristic *characteristic) {
  return self->contains(*characteristic);
}

//  void QLowEnergyService::readCharacteristic(const QLowEnergyCharacteristic
//      &characteristic)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QLowEnergyService18readCharacteristicERK24QLowEnergyCharacteristic(
    QLowEnergyService *self,
    const QLowEnergyCharacteristic *characteristic) {
  self->readCharacteristic(*characteristic);
}

//  void QLowEnergyService::writeCharacteristic(const
//      QLowEnergyCharacteristic &characteristic, const QByteArray &newValue,
//      WriteMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QLowEnergyService19writeCharacteristicERK24QLowEnergyCharacteristicRK10QByteArrayNS_9WriteModeE(
    QLowEnergyService *self,
    const QLowEnergyCharacteristic *characteristic,
    const QByteArray *newValue,
    QLowEnergyService::WriteMode mode) {
  self->writeCharacteristic(*characteristic, *newValue, mode);
}

//  bool QLowEnergyService::contains(const QLowEnergyDescriptor &descriptor)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QLowEnergyService8containsERK20QLowEnergyDescriptor(
    const QLowEnergyService *self,
    const QLowEnergyDescriptor *descriptor) {
  return self->contains(*descriptor);
}

//  void QLowEnergyService::readDescriptor(const QLowEnergyDescriptor
//      &descriptor)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QLowEnergyService14readDescriptorERK20QLowEnergyDescriptor(
    QLowEnergyService *self,
    const QLowEnergyDescriptor *descriptor) {
  self->readDescriptor(*descriptor);
}

//  void QLowEnergyService::writeDescriptor(const QLowEnergyDescriptor
//      &descriptor, const QByteArray &newValue)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QLowEnergyService15writeDescriptorERK20QLowEnergyDescriptorRK10QByteArray(
    QLowEnergyService *self,
    const QLowEnergyDescriptor *descriptor,
    const QByteArray *newValue) {
  self->writeDescriptor(*descriptor, *newValue);
}

//  QLowEnergyServicePrivate *QLowEnergyService::d_func()
extern "C" Q_DECL_EXPORT
QLowEnergyServicePrivate *ritual_ZN17QLowEnergyService6d_funcEv(
    QLowEnergyService *self) {
  return self->d_func();
}

//  const QLowEnergyServicePrivate *QLowEnergyService::d_func() const
extern "C" Q_DECL_EXPORT
const QLowEnergyServicePrivate *ritual_ZNK17QLowEnergyService6d_funcEv(
    const QLowEnergyService *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQLowEnergyService, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QLowEnergyService(
    QLowEnergyService *self,
    const char *key,
    void *call) {
  return static_cast<CuteQLowEnergyService *>(self)->take(key, call);
}

//  QList<QLowEnergyService *>::QList()
extern "C" Q_DECL_EXPORT
QList<QLowEnergyService *> *ritual_list_make_QLowEnergyService_ptr() {
  return new QList<QLowEnergyService *>();
}

//  void QList<QLowEnergyService *>::append(const QLowEnergyService * &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QLowEnergyService_ptr(
    QList<QLowEnergyService *> *self,
    QLowEnergyService *element) {
  self->append(element);
}

//  qsizetype QList<QLowEnergyService *>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QLowEnergyService_ptr(
    const QList<QLowEnergyService *> *self) {
  return self->size();
}

//  const QLowEnergyService * &QList<QLowEnergyService *>::at(qsizetype i)
//      const
extern "C" Q_DECL_EXPORT
QLowEnergyService *ritual_list_at_QLowEnergyService_ptr(
    const QList<QLowEnergyService *> *self,
    long long index) {
  return self->at(index);
}

//  QList<QLowEnergyService *>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QLowEnergyService_ptr(
    QList<QLowEnergyService *> *self) {
  delete self;
}
