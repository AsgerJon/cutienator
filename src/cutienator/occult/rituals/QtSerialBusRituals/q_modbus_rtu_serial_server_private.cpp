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
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qloggingcategory.h>
#include <QtSerialBus/qmodbusdeviceidentification.h>
#include <QtSerialBus/qmodbusserver.h>
#include <QtSerialBus/private/qmodbusserver_p.h>
#include <QtSerialBus/private/qmodbus_symbols_p.h>
#include <QtCore/qbitarray.h>
#include <QtCore/qdebug.h>
#include <QtCore/qlist.h>
#include <QtCore/qloggingcategory.h>
#include <algorithm>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtserialbus/src/serialbus/qmodbusdevice.cpp, line 372, as _Z13QT_MODBUS_LOWv
inline const QLoggingCategory &QT_MODBUS_LOW()
{
    static const QLoggingCategory category("qt.modbus.lowlevel");
    return category;
}

//  from ../qtserialbus/src/serialbus/qmodbusdevice.cpp, line 371, as _Z9QT_MODBUSv
inline const QLoggingCategory &QT_MODBUS()
{
    static const QLoggingCategory category("qt.modbus");
    return category;
}

//  from ../qtserialbus/src/serialbus/qmodbusserver.cpp, line 1270, as _ZN20QModbusServerPrivate20storeModbusCommEventERK16QModbusCommEvent
inline void QModbusServerPrivate::storeModbusCommEvent(const QModbusCommEvent &eventByte)
{
    // Inserts an event byte at the start of the event log. If the event log
    // is already full, the byte at the end of the log will be removed. The
    // event log size is 64 bytes, starting at index 0.
    m_commEventLog.push_front(eventByte);
    if (m_commEventLog.size() > 64)
        m_commEventLog.pop_back();
}
//  -----------------------------------------------------------------------

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

//  void QModbusRtuSerialServerPrivate::setupSerialPort()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QModbusRtuSerialServerPrivate15setupSerialPortEv(
    QModbusRtuSerialServerPrivate *self) {
  self->setupSerialPort();
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
