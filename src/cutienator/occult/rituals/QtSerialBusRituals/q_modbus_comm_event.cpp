//  Written by dev_tooling.RitualGenerator from the records of
//  QtSerialBus/6.12.0/QtSerialBus/private/qmodbuscommevent_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtSerialBus/QtSerialBus>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSerialBus/6.12.0/QtSerialBus/private/qmodbuscommevent_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QModbusCommEvent::QModbusCommEvent(QModbusCommEvent::EventByte byte)
extern "C" Q_DECL_EXPORT
QModbusCommEvent *ritual_ZN16QModbusCommEventC1ENS_9EventByteE(
    QModbusCommEvent::EventByte byte) {
  return new QModbusCommEvent(byte);
}

//  quint8 QModbusCommEvent::operator unsigned char() const
extern "C" Q_DECL_EXPORT
quint8 ritual_ZNK16QModbusCommEventcvhEv(const QModbusCommEvent *self) {
  return self->operator quint8();
}

//  QModbusCommEvent::EventByte QModbusCommEvent::operator
//      QModbusCommEvent::EventByte() const
extern "C" Q_DECL_EXPORT
QModbusCommEvent::EventByte ritual_ZNK16QModbusCommEventcvNS_9EventByteEEv(
    const QModbusCommEvent *self) {
  return self->operator QModbusCommEvent::EventByte();
}

//  QModbusCommEvent &QModbusCommEvent::operator=(QModbusCommEvent::EventByte
//      byte)
extern "C" Q_DECL_EXPORT
QModbusCommEvent *ritual_ZN16QModbusCommEventaSENS_9EventByteE(
    QModbusCommEvent *self,
    QModbusCommEvent::EventByte byte) {
  return &(self->operator=(byte));
}

//  QModbusCommEvent &QModbusCommEvent::operator|=(QModbusCommEvent::SendFlag
//      sf)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QModbusCommEventoRENS_8SendFlagE(
    QModbusCommEvent *self,
    QModbusCommEvent::SendFlag sf) {
  self->operator|=(sf);
}

//  QModbusCommEvent
//      &QModbusCommEvent::operator|=(QModbusCommEvent::ReceiveFlag rf)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QModbusCommEventoRENS_11ReceiveFlagE(
    QModbusCommEvent *self,
    QModbusCommEvent::ReceiveFlag rf) {
  self->operator|=(rf);
}

//  QModbusCommEvent::~QModbusCommEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QModbusCommEventD1Ev(QModbusCommEvent *self) {
  delete self;
}
