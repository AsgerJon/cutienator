//  Written by dev_tooling.RitualGenerator from the records of
//  QtSerialBus/6.12.0/QtSerialBus/private/qmodbusserver_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtSerialBus/qmodbusserver.h>
#include <QtSerialBus/QtSerialBus>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSerialBus/6.12.0/QtSerialBus/private/qmodbusserver_p.h>
#include <QtSerialBus/6.12.0/QtSerialBus/private/qmodbuscommevent_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qmodbusdeviceidentification.h"
#include "qmodbusserver.h"
#include "qmodbusserver_p.h"
#include "qmodbus_symbols_p.h"
#include <QtCore/qbitarray.h>
#include <QtCore/qdebug.h>
#include <QtCore/qlist.h>
#include <QtCore/qloggingcategory.h>
#include <algorithm>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

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

//  A QModbusServerPrivate that Python can take functions over in. Every QModbusServerPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQModbusServerPrivateCall0)(const void *, int *);
class CuteQModbusServerPrivate : public QModbusServerPrivate {
public:
  using QModbusServerPrivate::QModbusServerPrivate;
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
      CuteQModbusServerPrivateCall0 call = reinterpret_cast<CuteQModbusServerPrivateCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QIODevice *>(given);
    }
    return QModbusDevicePrivate::device();
  }
};

//  QModbusServer *QModbusServerPrivate::q_func()
extern "C" Q_DECL_EXPORT
QModbusServer *ritual_ZN20QModbusServerPrivate6q_funcEv(
    QModbusServerPrivate *self) {
  return self->q_func();
}

//  const QModbusServer *QModbusServerPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QModbusServer *ritual_ZNK20QModbusServerPrivate6q_funcEv(
    const QModbusServerPrivate *self) {
  return self->q_func();
}

//  QModbusServerPrivate::QModbusServerPrivate()
extern "C" Q_DECL_EXPORT
QModbusServerPrivate *ritual_ZN20QModbusServerPrivateC1Ev() {
  return new CuteQModbusServerPrivate();
}

//  void QModbusServerPrivate::resetCommunicationCounters()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QModbusServerPrivate26resetCommunicationCountersEv(
    QModbusServerPrivate *self) {
  self->resetCommunicationCounters();
}

//  void QModbusServerPrivate::incrementCounter(QModbusServerPrivate::Counter
//      counter)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QModbusServerPrivate16incrementCounterENS_7CounterE(
    QModbusServerPrivate *self,
    QModbusServerPrivate::Counter counter) {
  self->incrementCounter(counter);
}

//  void QModbusServerPrivate::storeModbusCommEvent(const QModbusCommEvent
//      &eventByte)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QModbusServerPrivate20storeModbusCommEventERK16QModbusCommEvent(
    QModbusServerPrivate *self,
    const QModbusCommEvent *eventByte) {
  self->storeModbusCommEvent(*eventByte);
}

//  a Python function taken by a CuteQModbusServerPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QModbusServerPrivate(
    QModbusServerPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQModbusServerPrivate *>(self)->take(key, call);
}
