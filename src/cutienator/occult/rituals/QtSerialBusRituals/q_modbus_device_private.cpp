//  Written by dev_tooling.RitualGenerator from the records of
//  QtSerialBus/6.12.0/QtSerialBus/private/qmodbusdevice_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtSerialBus/qmodbusdevice.h>
#include <QtSerialBus/QtSerialBus>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSerialBus/6.12.0/QtSerialBus/private/qmodbusdevice_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QModbusDevicePrivate that Python can take functions over in. Every QModbusDevicePrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQModbusDevicePrivateCall0)(const void *, int *);
class CuteQModbusDevicePrivate : public QModbusDevicePrivate {
public:
  using QModbusDevicePrivate::QModbusDevicePrivate;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK20QModbusDevicePrivate6deviceEv")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  QIODevice *QModbusDevicePrivate::device() const
  QIODevice *device() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQModbusDevicePrivateCall0 call = reinterpret_cast<CuteQModbusDevicePrivateCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QIODevice *>(given);
    }
    return QModbusDevicePrivate::device();
  }
};

//  QModbusDevice *QModbusDevicePrivate::q_func()
extern "C" Q_DECL_EXPORT
QModbusDevice *ritual_ZN20QModbusDevicePrivate6q_funcEv(
    QModbusDevicePrivate *self) {
  return self->q_func();
}

//  const QModbusDevice *QModbusDevicePrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QModbusDevice *ritual_ZNK20QModbusDevicePrivate6q_funcEv(
    const QModbusDevicePrivate *self) {
  return self->q_func();
}

#if QT_CONFIG(modbus_serialport)
//  void QModbusDevicePrivate::calculateInterFrameDelay()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QModbusDevicePrivate24calculateInterFrameDelayEv(
    QModbusDevicePrivate *self) {
  self->calculateInterFrameDelay();
}
#endif  // QT_CONFIG(modbus_serialport)

//  QIODevice *QModbusDevicePrivate::device() const
extern "C" Q_DECL_EXPORT
QIODevice *ritual_ZNK20QModbusDevicePrivate6deviceEv(
    const QModbusDevicePrivate *self) {
  return self->device();
}

//  a Python function taken by a CuteQModbusDevicePrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QModbusDevicePrivate(
    QModbusDevicePrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQModbusDevicePrivate *>(self)->take(key, call);
}

//  QIODevice *QModbusDevicePrivate::device() const
extern "C" Q_DECL_EXPORT
QIODevice *ritual_own_ZNK20QModbusDevicePrivate6deviceEv(
    const QModbusDevicePrivate *self) {
  return self->QModbusDevicePrivate::device();
}
