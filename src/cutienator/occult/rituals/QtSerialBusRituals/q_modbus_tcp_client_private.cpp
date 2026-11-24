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
