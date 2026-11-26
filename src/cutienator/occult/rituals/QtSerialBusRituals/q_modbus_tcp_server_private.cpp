//  Written by dev_tooling.RitualGenerator from the records of
//  QtSerialBus/6.12.0/QtSerialBus/private/qmodbustcpserver_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtSerialBus/qmodbustcpserver.h>
#include <QtSerialBus/QtSerialBus>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSerialBus/6.12.0/QtSerialBus/private/qmodbustcpserver_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSerialBus/qmodbuspdu.h>
#include <QtCore/qstring.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qloggingcategory.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtserialbus/src/serialbus/qmodbusdevice.cpp, line 371, as _Z9QT_MODBUSv
inline const QLoggingCategory &QT_MODBUS()
{
    static const QLoggingCategory category("qt.modbus");
    return category;
}

//  from ../qtserialbus/src/serialbus/qmodbusdevice.cpp, line 372, as _Z13QT_MODBUS_LOWv
inline const QLoggingCategory &QT_MODBUS_LOW()
{
    static const QLoggingCategory category("qt.modbus.lowlevel");
    return category;
}
//  -----------------------------------------------------------------------

//  A QModbusTcpServerPrivate that Python can take functions over in. Every QModbusTcpServerPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQModbusTcpServerPrivateCall0)(const void *, int *);
class CuteQModbusTcpServerPrivate : public QModbusTcpServerPrivate {
public:
  using QModbusTcpServerPrivate::QModbusTcpServerPrivate;
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
      CuteQModbusTcpServerPrivateCall0 call = reinterpret_cast<CuteQModbusTcpServerPrivateCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QIODevice *>(given);
    }
    return QModbusDevicePrivate::device();
  }
};

//  QModbusTcpServer *QModbusTcpServerPrivate::q_func()
extern "C" Q_DECL_EXPORT
QModbusTcpServer *ritual_ZN23QModbusTcpServerPrivate6q_funcEv(
    QModbusTcpServerPrivate *self) {
  return self->q_func();
}

//  const QModbusTcpServer *QModbusTcpServerPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QModbusTcpServer *ritual_ZNK23QModbusTcpServerPrivate6q_funcEv(
    const QModbusTcpServerPrivate *self) {
  return self->q_func();
}

//  QModbusResponse QModbusTcpServerPrivate::forwardProcessRequest(const
//      QModbusRequest &r)
extern "C" Q_DECL_EXPORT
QModbusResponse *ritual_ZN23QModbusTcpServerPrivate21forwardProcessRequestERK14QModbusRequest(
    QModbusTcpServerPrivate *self,
    const QModbusRequest *r) {
  return new QModbusResponse(self->forwardProcessRequest(*r));
}

//  void QModbusTcpServerPrivate::forwardError(const QString &errorText,
//      QModbusDevice::Error error)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QModbusTcpServerPrivate12forwardErrorERK7QStringN13QModbusDevice5ErrorE(
    QModbusTcpServerPrivate *self,
    const QString *errorText,
    QModbusDevice::Error error) {
  self->forwardError(*errorText, error);
}

//  bool QModbusTcpServerPrivate::matchingServerAddress(quint8 unitId) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QModbusTcpServerPrivate21matchingServerAddressEh(
    const QModbusTcpServerPrivate *self,
    quint8 unitId) {
  return self->matchingServerAddress(unitId);
}

//  void QModbusTcpServerPrivate::setupTcpServer()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QModbusTcpServerPrivate14setupTcpServerEv(
    QModbusTcpServerPrivate *self) {
  self->setupTcpServer();
}

//  a Python function taken by a CuteQModbusTcpServerPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QModbusTcpServerPrivate(
    QModbusTcpServerPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQModbusTcpServerPrivate *>(self)->take(key, call);
}
