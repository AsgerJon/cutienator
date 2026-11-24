//  Written by dev_tooling.RitualGenerator from the records of
//  QtMqtt/6.12.0/QtMqtt/private/qmqttcontrolpacket_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtMqtt/6.12.0/QtMqtt/private/qmqttglobal_p.h>
#include <QtMqtt/QtMqtt>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMqtt/6.12.0/QtMqtt/private/qmqttcontrolpacket_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qmqttcontrolpacket_p.h"
#include <QtCore/QtEndian>
#include <QtCore/QLoggingCategory>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtmqtt/src/mqtt/qmqttcontrolpacket.cpp, line 12, as _ZN18QMqttControlPacketC1Ev
inline QMqttControlPacket::QMqttControlPacket()
{

}

//  from ../qtmqtt/src/mqtt/qmqttcontrolpacket.cpp, line 17, as _ZN18QMqttControlPacketC1Eh
inline QMqttControlPacket::QMqttControlPacket(quint8 header)
    : m_header(header)
{

}

//  from ../qtmqtt/src/mqtt/qmqttcontrolpacket.cpp, line 23, as _ZN18QMqttControlPacketC1EhRK10QByteArray
inline QMqttControlPacket::QMqttControlPacket(quint8 header, const QByteArray &pay)
    : m_header(header)
    , m_payload(pay)
{

}

//  from ../qtmqtt/src/mqtt/qmqttcontrolpacket.cpp, line 30, as _ZN18QMqttControlPacket5clearEv
inline void QMqttControlPacket::clear()
{
    m_header = 0;
    m_payload.clear();
}

//  from ../qtmqtt/src/mqtt/qmqttcontrolpacket.cpp, line 36, as _ZN18QMqttControlPacket9setHeaderEh
inline void QMqttControlPacket::setHeader(quint8 h)
{
    if (h < QMqttControlPacket::CONNECT || h > DISCONNECT || h & 0x0F)
        m_header = QMqttControlPacket::UNKNOWN;
    else
        m_header = h;
}

//  from ../qtmqtt/src/mqtt/qmqttcontrolpacket.cpp, line 44, as _ZN18QMqttControlPacket6appendEc
inline void QMqttControlPacket::append(char value)
{
    m_payload.append(value);
}

//  from ../qtmqtt/src/mqtt/qmqttcontrolpacket.cpp, line 49, as _ZN18QMqttControlPacket6appendEt
inline void QMqttControlPacket::append(quint16 value)
{
    const quint16 msb = qToBigEndian<quint16>(value);
    const char * msb_c = reinterpret_cast<const char*>(&msb);
    m_payload.append(msb_c, 2);
}

//  from ../qtmqtt/src/mqtt/qmqttcontrolpacket.cpp, line 56, as _ZN18QMqttControlPacket6appendEj
inline void QMqttControlPacket::append(quint32 value)
{
    const quint32 msb = qToBigEndian<quint32>(value);
    const char * msb_c = reinterpret_cast<const char*>(&msb);
    m_payload.append(msb_c, 4);
}

//  from ../qtmqtt/src/mqtt/qmqttcontrolpacket.cpp, line 63, as _ZN18QMqttControlPacket6appendERK10QByteArray
inline void QMqttControlPacket::append(const QByteArray &data)
{
    append(static_cast<quint16>(data.size()));
    m_payload.append(data);
}

//  from ../qtmqtt/src/mqtt/qmqttcontrolpacket.cpp, line 69, as _ZN18QMqttControlPacket9appendRawERK10QByteArray
inline void QMqttControlPacket::appendRaw(const QByteArray &data)
{
    m_payload.append(data);
}
//  -----------------------------------------------------------------------

//  QMqttControlPacket::QMqttControlPacket()
extern "C" Q_DECL_EXPORT
QMqttControlPacket *ritual_ZN18QMqttControlPacketC1Ev() {
  return new QMqttControlPacket();
}

//  QMqttControlPacket::QMqttControlPacket(quint8 header)
extern "C" Q_DECL_EXPORT
QMqttControlPacket *ritual_ZN18QMqttControlPacketC1Eh(quint8 header) {
  return new QMqttControlPacket(header);
}

//  QMqttControlPacket::QMqttControlPacket(quint8 header, const QByteArray
//      &pay)
extern "C" Q_DECL_EXPORT
QMqttControlPacket *ritual_ZN18QMqttControlPacketC1EhRK10QByteArray(
    quint8 header,
    const QByteArray *pay) {
  return new QMqttControlPacket(header, *pay);
}

//  void QMqttControlPacket::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QMqttControlPacket5clearEv(QMqttControlPacket *self) {
  self->clear();
}

//  void QMqttControlPacket::setHeader(quint8 h)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QMqttControlPacket9setHeaderEh(
    QMqttControlPacket *self,
    quint8 h) {
  self->setHeader(h);
}

//  quint8 QMqttControlPacket::header() const
extern "C" Q_DECL_EXPORT
quint8 ritual_ZNK18QMqttControlPacket6headerEv(
    const QMqttControlPacket *self) {
  return self->header();
}

//  void QMqttControlPacket::append(char value)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QMqttControlPacket6appendEc(
    QMqttControlPacket *self,
    char value) {
  self->append(value);
}

//  void QMqttControlPacket::append(quint16 value)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QMqttControlPacket6appendEt(
    QMqttControlPacket *self,
    quint16 value) {
  self->append(value);
}

//  void QMqttControlPacket::append(quint32 value)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QMqttControlPacket6appendEj(
    QMqttControlPacket *self,
    quint32 value) {
  self->append(value);
}

//  void QMqttControlPacket::append(const QByteArray &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QMqttControlPacket6appendERK10QByteArray(
    QMqttControlPacket *self,
    const QByteArray *data) {
  self->append(*data);
}

//  void QMqttControlPacket::appendRaw(const QByteArray &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QMqttControlPacket9appendRawERK10QByteArray(
    QMqttControlPacket *self,
    const QByteArray *data) {
  self->appendRaw(*data);
}

//  QByteArray QMqttControlPacket::payload() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK18QMqttControlPacket7payloadEv(
    const QMqttControlPacket *self) {
  return new QByteArray(self->payload());
}

//  QMqttControlPacket::~QMqttControlPacket()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QMqttControlPacketD1Ev(QMqttControlPacket *self) {
  delete self;
}
