//  Written by dev_tooling.RitualGenerator from the records of
//  QtRemoteObjects/6.12.0/QtRemoteObjects/private/qremoteobjectpacket_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtRemoteObjects/QtRemoteObjects>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtRemoteObjects/6.12.0/QtRemoteObjects/private/qremoteobjectpacket_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>

//  Only a class built on QRemoteObjectPackets::QDataStreamCodec may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQRemoteObjectPackets_QDataStreamCodec : QRemoteObjectPackets::QDataStreamCodec {
  using QRemoteObjectPackets::QDataStreamCodec::getPayload;
  using QRemoteObjectPackets::QDataStreamCodec::reset;
};

//  const QByteArray &QRemoteObjectPackets::QDataStreamCodec::getPayload()
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN20QRemoteObjectPackets16QDataStreamCodec10getPayloadEv(
    QRemoteObjectPackets::QDataStreamCodec *self) {
  return new QByteArray(self->getPayload());
}

//  void QRemoteObjectPackets::QDataStreamCodec::reset()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QRemoteObjectPackets16QDataStreamCodec5resetEv(
    QRemoteObjectPackets::QDataStreamCodec *self) {
  self->reset();
}

//  const QByteArray &QRemoteObjectPackets::QDataStreamCodec::getPayload()
extern "C" Q_DECL_EXPORT
QByteArray *ritual_own_ZN20QRemoteObjectPackets16QDataStreamCodec10getPayloadEv(
    QRemoteObjectPackets::QDataStreamCodec *self) {
  return new QByteArray(
      static_cast<OwnQRemoteObjectPackets_QDataStreamCodec *>(self)->OwnQRemoteObjectPackets_QDataStreamCodec::getPayload());
}

//  void QRemoteObjectPackets::QDataStreamCodec::reset()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QRemoteObjectPackets16QDataStreamCodec5resetEv(
    QRemoteObjectPackets::QDataStreamCodec *self) {
  static_cast<OwnQRemoteObjectPackets_QDataStreamCodec *>(self)->OwnQRemoteObjectPackets_QDataStreamCodec::reset();
}
