//  Written by dev_tooling.RitualGenerator from the records of
//  QtRemoteObjects/6.12.0/QtRemoteObjects/private/qremoteobjectpacket_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtRemoteObjects/QtRemoteObjects>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtRemoteObjects/6.12.0/QtRemoteObjects/private/qremoteobjectpacket_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>

//  void QRemoteObjectPackets::DataStreamPacket::setId(quint16 id)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QRemoteObjectPackets16DataStreamPacket5setIdEt(
    QRemoteObjectPackets::DataStreamPacket *self,
    quint16 id) {
  self->setId(id);
}

//  void QRemoteObjectPackets::DataStreamPacket::finishPacket()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QRemoteObjectPackets16DataStreamPacket12finishPacketEv(
    QRemoteObjectPackets::DataStreamPacket *self) {
  self->finishPacket();
}

//  const QByteArray &QRemoteObjectPackets::DataStreamPacket::payload()
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN20QRemoteObjectPackets16DataStreamPacket7payloadEv(
    QRemoteObjectPackets::DataStreamPacket *self) {
  return new QByteArray(self->payload());
}

//  void QRemoteObjectPackets::DataStreamPacket::reset()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QRemoteObjectPackets16DataStreamPacket5resetEv(
    QRemoteObjectPackets::DataStreamPacket *self) {
  self->reset();
}
