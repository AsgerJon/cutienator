//  Written by dev_tooling.RitualGenerator from the records of
//  QtRemoteObjects/6.12.0/QtRemoteObjects/private/qremoteobjectpacket_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtRemoteObjects/QtRemoteObjects>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtRemoteObjects/6.12.0/QtRemoteObjects/private/qremoteobjectpacket_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qbytearrayview.h>
#include <QtRemoteObjects/private/qremoteobjectcontainers_p.h>
#include <QtRemoteObjects/qremoteobjectpendingcall.h>
#include <QtRemoteObjects/qremoteobjectsource.h>
#include <QtRemoteObjects/private/qremoteobjectsource_p.h>
#include <QtRemoteObjects/private/qremoteobjectpacket_p.h>
#include <QtRemoteObjects/qconnectionfactories.h>
#include <QtRemoteObjects/private/qconnectionfactories_p.h>
#include <cstring>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectpacket.cpp, line 1101, as _ZN20QRemoteObjectPackets16DataStreamPacketC1Et
namespace QRemoteObjectPackets {
using namespace QtRemoteObjects;
inline DataStreamPacket::DataStreamPacket(quint16 id)
    : QDataStream(&array, QIODevice::WriteOnly), baseAddress(0), size(0)
{
    this->setVersion(QtRemoteObjects::dataStreamVersion);
    this->setByteOrder(QDataStream::LittleEndian);
    *this << quint32(0);
    *this << id;
}
}  // namespace QRemoteObjectPackets
//  -----------------------------------------------------------------------

//  QRemoteObjectPackets::DataStreamPacket::DataStreamPacket(quint16 id)
extern "C" Q_DECL_EXPORT
QRemoteObjectPackets::DataStreamPacket *ritual_ZN20QRemoteObjectPackets16DataStreamPacketC1Et(
    quint16 id) {
  return new QRemoteObjectPackets::DataStreamPacket(id);
}

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
