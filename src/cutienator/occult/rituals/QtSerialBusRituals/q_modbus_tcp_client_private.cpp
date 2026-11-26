//  Written by dev_tooling.RitualGenerator from the records of
//  QtSerialBus/6.12.0/QtSerialBus/private/qmodbustcpclient_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtSerialBus/qmodbustcpclient.h>
#include <QtSerialBus/QtSerialBus>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSerialBus/6.12.0/QtSerialBus/private/qmodbustcpclient_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSerialBus/qmodbuspdu.h>
#include <QtSerialBus/qmodbusdataunit.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qloggingcategory.h>
#include <QtSerialBus/qmodbusclient.h>
#include <QtSerialBus/private/qmodbusclient_p.h>
#include <QtSerialBus/private/qmodbus_symbols_p.h>
#include <QtCore/qdebug.h>
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

//  QModbusTcpClient *QModbusTcpClientPrivate::q_func()
extern "C" Q_DECL_EXPORT
QModbusTcpClient *ritual_ZN23QModbusTcpClientPrivate6q_funcEv(
    QModbusTcpClientPrivate *self) {
  return self->q_func();
}

//  const QModbusTcpClient *QModbusTcpClientPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QModbusTcpClient *ritual_ZNK23QModbusTcpClientPrivate6q_funcEv(
    const QModbusTcpClientPrivate *self) {
  return self->q_func();
}

//  void QModbusTcpClientPrivate::setupTcpSocket()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QModbusTcpClientPrivate14setupTcpSocketEv(
    QModbusTcpClientPrivate *self) {
  self->setupTcpSocket();
}

//  QModbusReply *QModbusTcpClientPrivate::enqueueRequest(const
//      QModbusRequest &request, int serverAddress, const QModbusDataUnit
//      &unit, QModbusReply::ReplyType type)
extern "C" Q_DECL_EXPORT
QModbusReply *ritual_ZN23QModbusTcpClientPrivate14enqueueRequestERK14QModbusRequestiRK15QModbusDataUnitN12QModbusReply9ReplyTypeE(
    QModbusTcpClientPrivate *self,
    const QModbusRequest *request,
    int serverAddress,
    const QModbusDataUnit *unit,
    QModbusReply::ReplyType type) {
  return self->enqueueRequest(*request, serverAddress, *unit, type);
}

//  bool QModbusTcpClientPrivate::isOpen() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QModbusTcpClientPrivate6isOpenEv(
    const QModbusTcpClientPrivate *self) {
  return self->isOpen();
}

//  void QModbusTcpClientPrivate::cleanupTransactionStore()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QModbusTcpClientPrivate23cleanupTransactionStoreEv(
    QModbusTcpClientPrivate *self) {
  self->cleanupTransactionStore();
}

//  void QModbusTcpClientPrivate::incrementTransactionId()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QModbusTcpClientPrivate22incrementTransactionIdEv(
    QModbusTcpClientPrivate *self) {
  self->incrementTransactionId();
}

//  int QModbusTcpClientPrivate::transactionId() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK23QModbusTcpClientPrivate13transactionIdEv(
    const QModbusTcpClientPrivate *self) {
  return self->transactionId();
}

//  QIODevice *QModbusTcpClientPrivate::device() const
extern "C" Q_DECL_EXPORT
QIODevice *ritual_ZNK23QModbusTcpClientPrivate6deviceEv(
    const QModbusTcpClientPrivate *self) {
  return self->device();
}

//  QModbusReply *QModbusTcpClientPrivate::enqueueRequest(const
//      QModbusRequest &request, int serverAddress, const QModbusDataUnit
//      &unit, QModbusReply::ReplyType type)
extern "C" Q_DECL_EXPORT
QModbusReply *ritual_own_ZN23QModbusTcpClientPrivate14enqueueRequestERK14QModbusRequestiRK15QModbusDataUnitN12QModbusReply9ReplyTypeE(
    QModbusTcpClientPrivate *self,
    const QModbusRequest *request,
    int serverAddress,
    const QModbusDataUnit *unit,
    QModbusReply::ReplyType type) {
  return self->QModbusTcpClientPrivate::enqueueRequest(
      *request,
      serverAddress,
      *unit,
      type);
}

//  bool QModbusTcpClientPrivate::isOpen() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK23QModbusTcpClientPrivate6isOpenEv(
    const QModbusTcpClientPrivate *self) {
  return self->QModbusTcpClientPrivate::isOpen();
}

//  QIODevice *QModbusTcpClientPrivate::device() const
extern "C" Q_DECL_EXPORT
QIODevice *ritual_own_ZNK23QModbusTcpClientPrivate6deviceEv(
    const QModbusTcpClientPrivate *self) {
  return self->QModbusTcpClientPrivate::device();
}
