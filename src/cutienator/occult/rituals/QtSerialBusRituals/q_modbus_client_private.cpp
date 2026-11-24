//  Written by dev_tooling.RitualGenerator from the records of
//  QtSerialBus/6.12.0/QtSerialBus/private/qmodbusclient_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtSerialBus/qmodbusclient.h>
#include <QtSerialBus/QtSerialBus>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSerialBus/6.12.0/QtSerialBus/private/qmodbusclient_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSerialBus/qmodbusdataunit.h>
#include <QtSerialBus/qmodbuspdu.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSerialBus/qmodbusclient.h>
#include <QtSerialBus/private/qmodbusclient_p.h>
#include <QtSerialBus/private/qmodbus_symbols_p.h>
#include <QtCore/qdebug.h>
#include <QtCore/qloggingcategory.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtserialbus/src/serialbus/qmodbusclient.cpp, line 235, as _ZNK20QModbusClientPrivate17createReadRequestERK15QModbusDataUnit
inline QModbusRequest QModbusClientPrivate::createReadRequest(const QModbusDataUnit &data) const
{
    if (!data.isValid())
        return QModbusRequest();

    switch (data.registerType()) {
    case QModbusDataUnit::Coils:
        return QModbusRequest(QModbusRequest::ReadCoils, quint16(data.startAddress()),
                              quint16(data.valueCount()));
    case QModbusDataUnit::DiscreteInputs:
        return QModbusRequest(QModbusRequest::ReadDiscreteInputs, quint16(data.startAddress()),
                              quint16(data.valueCount()));
    case QModbusDataUnit::InputRegisters:
        return QModbusRequest(QModbusRequest::ReadInputRegisters, quint16(data.startAddress()),
                              quint16(data.valueCount()));
    case QModbusDataUnit::HoldingRegisters:
        return QModbusRequest(QModbusRequest::ReadHoldingRegisters, quint16(data.startAddress()),
                              quint16(data.valueCount()));
    default:
        break;
    }

    return QModbusRequest();
}

//  from ../qtserialbus/src/serialbus/qmodbusclient.cpp, line 260, as _ZNK20QModbusClientPrivate18createWriteRequestERK15QModbusDataUnit
inline QModbusRequest QModbusClientPrivate::createWriteRequest(const QModbusDataUnit &data) const
{
    switch (data.registerType()) {
    case QModbusDataUnit::Coils: {
        if (data.valueCount() == 1) {
            return QModbusRequest(QModbusRequest::WriteSingleCoil, quint16(data.startAddress()),
                                  quint16((data.value(0) == 0u) ? Coil::Off : Coil::On));
        }

        quint8 byteCount = quint8(data.valueCount() / 8);
        if ((data.valueCount() % 8) != 0)
            byteCount += 1;

        qsizetype address = 0;
        QList<quint8> bytes;
        for (quint8 i = 0; i < byteCount; ++i) {
            quint8 byte = 0;
            for (int currentBit = 0; currentBit < 8; ++currentBit)
                if (data.value(address++))
                    byte |= (1U << currentBit);
            bytes.append(byte);
        }

        return QModbusRequest(QModbusRequest::WriteMultipleCoils, quint16(data.startAddress()),
                              quint16(data.valueCount()), byteCount, bytes);
    }   break;

    case QModbusDataUnit::HoldingRegisters: {
        if (data.valueCount() == 1) {
            return QModbusRequest(QModbusRequest::WriteSingleRegister, quint16(data.startAddress()),
                                  data.value(0));
        }

        const quint8 byteCount = quint8(data.valueCount() * 2);
        return QModbusRequest(QModbusRequest::WriteMultipleRegisters, quint16(data.startAddress()),
                              quint16(data.valueCount()), byteCount, data.values());
    }   break;

    case QModbusDataUnit::DiscreteInputs:
    case QModbusDataUnit::InputRegisters:
    default:    // fall through on purpose
        break;
    }
    return QModbusRequest();
}

//  from ../qtserialbus/src/serialbus/qmodbusclient.cpp, line 306, as _ZNK20QModbusClientPrivate15createRWRequestERK15QModbusDataUnitS2_
inline QModbusRequest QModbusClientPrivate::createRWRequest(const QModbusDataUnit &read,
                                                     const QModbusDataUnit &write) const
{
    if ((read.registerType() != QModbusDataUnit::HoldingRegisters)
        || (write.registerType() != QModbusDataUnit::HoldingRegisters)) {
        return QModbusRequest();
    }

    const quint8 byteCount = quint8(write.valueCount() * 2);
    return QModbusRequest(QModbusRequest::ReadWriteMultipleRegisters, quint16(read.startAddress()),
                          quint16(read.valueCount()), quint16(write.startAddress()),
                          quint16(write.valueCount()), byteCount, write.values());
}

//  from ../qtserialbus/src/serialbus/qmodbusclient.cpp, line 320, as _ZN20QModbusClientPrivate19processQueueElementERK15QModbusResponseRKNS_12QueueElementE
inline void QModbusClientPrivate::processQueueElement(const QModbusResponse &pdu,
                                               const QueueElement &element)
{
    if (element.reply.isNull())
        return;

    element.reply->setRawResult(pdu);
    if (pdu.isException()) {
        element.reply->setError(QModbusDevice::ProtocolError,
            QModbusClient::tr("Modbus Exception Response."));
        return;
    }

    if (element.reply->type() == QModbusReply::Broadcast) {
        element.reply->setFinished(true);
        return;
    }

    QModbusDataUnit unit = element.unit;
    if (!q_func()->processResponse(pdu, &unit)) {
        element.reply->setError(QModbusDevice::InvalidResponseError,
            QModbusClient::tr("An invalid response has been received."));
        return;
    }

    element.reply->setResult(unit);
    element.reply->setFinished(true);
}
//  -----------------------------------------------------------------------

//  A QModbusClientPrivate that Python can take functions over in. Every QModbusClientPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQModbusClientPrivateCall0)(const void *, const QModbusRequest *, int, const QModbusDataUnit *, int, int *);
typedef bool (*CuteQModbusClientPrivateCall1)(const void *, int *);
typedef void * (*CuteQModbusClientPrivateCall2)(const void *, int *);
class CuteQModbusClientPrivate : public QModbusClientPrivate {
public:
  using QModbusClientPrivate::QModbusClientPrivate;
  void *taken[3] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN20QModbusClientPrivate14enqueueRequestERK14QModbusRequestiRK15QModbusDataUnitN12QModbusReply9ReplyTypeE")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QModbusClientPrivate6isOpenEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QModbusDevicePrivate6deviceEv")) {
      taken[2] = call;
      return true;
    }
    return false;
  }

  //  QModbusReply *QModbusClientPrivate::enqueueRequest(const
  //      QModbusRequest &a0, int a1, const QModbusDataUnit &a2,
  //      QModbusReply::ReplyType a3)
  QModbusReply *enqueueRequest(
      const QModbusRequest &a0,
      int a1,
      const QModbusDataUnit &a2,
      QModbusReply::ReplyType a3) override {
    if (taken[0]) {
      int handled = 0;
      CuteQModbusClientPrivateCall0 call = reinterpret_cast<CuteQModbusClientPrivateCall0>(taken[0]);
      void * given = call(this, &a0, a1, &a2, static_cast<int>(a3), &handled);
      if (handled) return static_cast<QModbusReply *>(given);
    }
    return QModbusClientPrivate::enqueueRequest(a0, a1, a2, a3);
  }

  //  bool QModbusClientPrivate::isOpen() const
  bool isOpen() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQModbusClientPrivateCall1 call = reinterpret_cast<CuteQModbusClientPrivateCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QModbusClientPrivate::isOpen();
  }

  //  QIODevice *QModbusDevicePrivate::device() const
  QIODevice *device() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQModbusClientPrivateCall2 call = reinterpret_cast<CuteQModbusClientPrivateCall2>(taken[2]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QIODevice *>(given);
    }
    return QModbusDevicePrivate::device();
  }
};

//  QModbusClient *QModbusClientPrivate::q_func()
extern "C" Q_DECL_EXPORT
QModbusClient *ritual_ZN20QModbusClientPrivate6q_funcEv(
    QModbusClientPrivate *self) {
  return self->q_func();
}

//  const QModbusClient *QModbusClientPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QModbusClient *ritual_ZNK20QModbusClientPrivate6q_funcEv(
    const QModbusClientPrivate *self) {
  return self->q_func();
}

//  QModbusRequest QModbusClientPrivate::createReadRequest(const
//      QModbusDataUnit &data) const
extern "C" Q_DECL_EXPORT
QModbusRequest *ritual_ZNK20QModbusClientPrivate17createReadRequestERK15QModbusDataUnit(
    const QModbusClientPrivate *self,
    const QModbusDataUnit *data) {
  return new QModbusRequest(self->createReadRequest(*data));
}

//  QModbusRequest QModbusClientPrivate::createWriteRequest(const
//      QModbusDataUnit &data) const
extern "C" Q_DECL_EXPORT
QModbusRequest *ritual_ZNK20QModbusClientPrivate18createWriteRequestERK15QModbusDataUnit(
    const QModbusClientPrivate *self,
    const QModbusDataUnit *data) {
  return new QModbusRequest(self->createWriteRequest(*data));
}

//  QModbusRequest QModbusClientPrivate::createRWRequest(const
//      QModbusDataUnit &read, const QModbusDataUnit &write) const
extern "C" Q_DECL_EXPORT
QModbusRequest *ritual_ZNK20QModbusClientPrivate15createRWRequestERK15QModbusDataUnitS2_(
    const QModbusClientPrivate *self,
    const QModbusDataUnit *read,
    const QModbusDataUnit *write) {
  return new QModbusRequest(self->createRWRequest(*read, *write));
}

//  QModbusReply *QModbusClientPrivate::enqueueRequest(const QModbusRequest
//      &a0, int a1, const QModbusDataUnit &a2, QModbusReply::ReplyType a3)
extern "C" Q_DECL_EXPORT
QModbusReply *ritual_ZN20QModbusClientPrivate14enqueueRequestERK14QModbusRequestiRK15QModbusDataUnitN12QModbusReply9ReplyTypeE(
    QModbusClientPrivate *self,
    const QModbusRequest *a0,
    int a1,
    const QModbusDataUnit *a2,
    QModbusReply::ReplyType a3) {
  return self->enqueueRequest(*a0, a1, *a2, a3);
}

//  bool QModbusClientPrivate::isOpen() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QModbusClientPrivate6isOpenEv(
    const QModbusClientPrivate *self) {
  return self->isOpen();
}

//  void QModbusClientPrivate::processQueueElement(const QModbusResponse
//      &pdu, const QueueElement &element)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QModbusClientPrivate19processQueueElementERK15QModbusResponseRKNS_12QueueElementE(
    QModbusClientPrivate *self,
    const QModbusResponse *pdu,
    const QModbusClientPrivate::QueueElement *element) {
  self->processQueueElement(*pdu, *element);
}

//  a Python function taken by a CuteQModbusClientPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QModbusClientPrivate(
    QModbusClientPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQModbusClientPrivate *>(self)->take(key, call);
}

//  QModbusReply *QModbusClientPrivate::enqueueRequest(const QModbusRequest
//      &a0, int a1, const QModbusDataUnit &a2, QModbusReply::ReplyType a3)
extern "C" Q_DECL_EXPORT
QModbusReply *ritual_own_ZN20QModbusClientPrivate14enqueueRequestERK14QModbusRequestiRK15QModbusDataUnitN12QModbusReply9ReplyTypeE(
    QModbusClientPrivate *self,
    const QModbusRequest *a0,
    int a1,
    const QModbusDataUnit *a2,
    QModbusReply::ReplyType a3) {
  return self->QModbusClientPrivate::enqueueRequest(*a0, a1, *a2, a3);
}

//  bool QModbusClientPrivate::isOpen() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK20QModbusClientPrivate6isOpenEv(
    const QModbusClientPrivate *self) {
  return self->QModbusClientPrivate::isOpen();
}
