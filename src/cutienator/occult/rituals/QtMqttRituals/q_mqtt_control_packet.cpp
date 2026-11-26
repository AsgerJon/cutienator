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
#include <QtCore/qloggingcategory.h>
#include <QtMqtt/private/qmqttcontrolpacket_p.h>
#include <QtCore/QtEndian>
#include <QtCore/QLoggingCategory>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtmqtt/src/mqtt/qmqttclient.cpp, line 19, as _Z12lcMqttClientv
inline const QLoggingCategory &lcMqttClient()
{
    static const QLoggingCategory category("qt.mqtt.client");
    return category;
}

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

//  from ../qtmqtt/src/mqtt/qmqttcontrolpacket.cpp, line 74, as _ZN18QMqttControlPacket24appendRawVariableIntegerEj
inline void QMqttControlPacket::appendRawVariableInteger(quint32 value)
{
    QByteArray data;
    // Add length
    if (value > 268435455)
        qCDebug(lcMqttClient) << "Attempting to write variable integer overflow.";
    do {
        quint8 b = value % 128;
        value /= 128;
        if (value > 0)
            b |= 0x80;
        data.append(char(b));
    } while (value > 0);
    appendRaw(data);
}

//  from ../qtmqtt/src/mqtt/qmqttcontrolpacket.cpp, line 90, as _ZNK18QMqttControlPacket9serializeEv
inline QByteArray QMqttControlPacket::serialize() const
{
    // Create ByteArray
    QByteArray data;
    // Add Header
    data.append(char(m_header));
    data.append(serializePayload());

    return data;
}

//  from ../qtmqtt/src/mqtt/qmqttcontrolpacket.cpp, line 101, as _ZNK18QMqttControlPacket16serializePayloadEv
inline QByteArray QMqttControlPacket::serializePayload() const
{
    QByteArray data;
    // Add length
    quint32 msgSize = quint32(m_payload.size());
    if (msgSize > 268435455)
        qCDebug(lcMqttClient) << "Publishing a message bigger than maximum size.";
    do {
        quint8 b = msgSize % 128;
        msgSize /= 128;
        if (msgSize > 0)
            b |= 0x80;
        data.append(char(b));
    } while (msgSize > 0);
    // Add payload
    data.append(m_payload);
    return data;
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

//  void QMqttControlPacket::appendRawVariableInteger(quint32 value)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QMqttControlPacket24appendRawVariableIntegerEj(
    QMqttControlPacket *self,
    quint32 value) {
  self->appendRawVariableInteger(value);
}

//  QByteArray QMqttControlPacket::serialize() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK18QMqttControlPacket9serializeEv(
    const QMqttControlPacket *self) {
  return new QByteArray(self->serialize());
}

//  QByteArray QMqttControlPacket::serializePayload() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK18QMqttControlPacket16serializePayloadEv(
    const QMqttControlPacket *self) {
  return new QByteArray(self->serializePayload());
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
