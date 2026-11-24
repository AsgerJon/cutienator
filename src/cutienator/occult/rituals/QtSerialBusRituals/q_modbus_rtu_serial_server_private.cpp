//  Written by dev_tooling.RitualGenerator from the records of
//  QtSerialBus/6.12.0/QtSerialBus/private/qmodbusrtuserialserver_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtSerialBus/qtserialbusglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(modbus_serialport)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtSerialBus/qmodbusrtuserialserver.h>
#include <QtSerialBus/QtSerialBus>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSerialBus/6.12.0/QtSerialBus/private/qmodbusrtuserialserver_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QModbusRtuSerialServerPrivate that Python can take functions over in. Every QModbusRtuSerialServerPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQModbusRtuSerialServerPrivateCall0)(const void *, int *);
class CuteQModbusRtuSerialServerPrivate : public QModbusRtuSerialServerPrivate {
public:
  using QModbusRtuSerialServerPrivate::QModbusRtuSerialServerPrivate;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK20QModbusDevicePrivate6deviceEv")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  QIODevice *QModbusRtuSerialServerPrivate::device() const
  QIODevice *device() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQModbusRtuSerialServerPrivateCall0 call = reinterpret_cast<CuteQModbusRtuSerialServerPrivateCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QIODevice *>(given);
    }
    return QModbusRtuSerialServerPrivate::device();
  }
};

//  QModbusRtuSerialServer *QModbusRtuSerialServerPrivate::q_func()
extern "C" Q_DECL_EXPORT
QModbusRtuSerialServer *ritual_ZN29QModbusRtuSerialServerPrivate6q_funcEv(
    QModbusRtuSerialServerPrivate *self) {
  return self->q_func();
}

//  const QModbusRtuSerialServer *QModbusRtuSerialServerPrivate::q_func()
//      const
extern "C" Q_DECL_EXPORT
const QModbusRtuSerialServer *ritual_ZNK29QModbusRtuSerialServerPrivate6q_funcEv(
    const QModbusRtuSerialServerPrivate *self) {
  return self->q_func();
}

//  void QModbusRtuSerialServerPrivate::setupEnvironment()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QModbusRtuSerialServerPrivate16setupEnvironmentEv(
    QModbusRtuSerialServerPrivate *self) {
  self->setupEnvironment();
}

//  QIODevice *QModbusRtuSerialServerPrivate::device() const
extern "C" Q_DECL_EXPORT
QIODevice *ritual_ZNK29QModbusRtuSerialServerPrivate6deviceEv(
    const QModbusRtuSerialServerPrivate *self) {
  return self->device();
}

//  a Python function taken by a CuteQModbusRtuSerialServerPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QModbusRtuSerialServerPrivate(
    QModbusRtuSerialServerPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQModbusRtuSerialServerPrivate *>(self)->take(key, call);
}

//  QIODevice *QModbusRtuSerialServerPrivate::device() const
extern "C" Q_DECL_EXPORT
QIODevice *ritual_own_ZNK29QModbusRtuSerialServerPrivate6deviceEv(
    const QModbusRtuSerialServerPrivate *self) {
  return self->QModbusRtuSerialServerPrivate::device();
}

#endif  // QT_CONFIG(modbus_serialport)
