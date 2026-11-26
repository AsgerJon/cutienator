//  Written by dev_tooling.RitualGenerator from the records of
//  QtMqtt/6.12.0/QtMqtt/private/qmqttclient_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtMqtt/6.12.0/QtMqtt/private/qmqttglobal_p.h>
#include <QtMqtt/qmqttclient.h>
#include <QtMqtt/QtMqtt>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMqtt/6.12.0/QtMqtt/private/qmqttclient_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMqtt/private/qmqttconnection_p.h>
#include <QtMqtt/private/qmqttconnectionproperties_p.h>
#include <QtMqtt/private/qmqttcontrolpacket_p.h>
#include <QtMqtt/private/qmqttmessage_p.h>
#include <QtMqtt/private/qmqttpublishproperties_p.h>
#include <QtMqtt/private/qmqttsubscription_p.h>
#include <QtMqtt/private/qmqttclient_p.h>
#include <QtCore/QLoggingCategory>
#include <QtNetwork/QSslSocket>
#include <QtNetwork/QTcpSocket>
#include <limits>
#include <cstdint>
#include <QtMqtt/qmqttclient.h>
#include <QtMqtt/private/qmqttclient_p.h>
#ifdef QT_MQTT_WITH_WEBSOCKETS
#endif
#include <QtCore/QLoggingCategory>
#include <QtCore/QUuid>
#include <QtCore/QtEndian>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtmqtt/src/mqtt/qmqttconnection.cpp, line 81, as _ZN15QMqttConnectionC1EP7QObject
inline QMqttConnection::QMqttConnection(QObject *parent) : QObject(parent)
{
}

//  from ../qtmqtt/src/mqtt/qmqttconnection.cpp, line 85, as _ZN15QMqttConnectionD1Ev
inline QMqttConnection::~QMqttConnection()
{
    if (m_internalState == BrokerConnected)
        sendControlDisconnect();
    m_transport = nullptr;
}

//  from ../qtmqtt/src/mqtt/qmqttclient.cpp, line 1099, as _ZN18QMqttClientPrivateD1Ev
inline QMqttClientPrivate::~QMqttClientPrivate()
{
}

//  from ../qtmqtt/src/mqtt/qmqttconnection.cpp, line 716, as _ZN15QMqttConnection21sendControlDisconnectEv
inline bool QMqttConnection::sendControlDisconnect()
{
    qCDebug(lcMqttConnection) << Q_FUNC_INFO;

    m_pingTimer.stop();
    m_pingTimeout = 0;

    m_activeSubscriptions.clear();

    m_receiveAliases.clear();
    m_publishAliases.clear();

    const QMqttControlPacket packet(QMqttControlPacket::DISCONNECT);
    if (!writePacketToTransport(packet)) {
        qCDebug(lcMqttConnection) << "Failed to write DISCONNECT to transport.";
        return false;
    }
    if (m_internalState != ClientDestruction)
        m_internalState = BrokerDisconnected;

    if (m_transport->waitForBytesWritten(30000)) {
        // MQTT-3.14.4-1 must disconnect
        m_transport->close();
        return true;
    }
    return false;
}

//  from ../qtmqtt/src/mqtt/qmqttclient.cpp, line 1103, as _ZN18QMqttClientPrivate16setStateAndErrorEN11QMqttClient11ClientStateENS0_11ClientErrorE
inline void QMqttClientPrivate::setStateAndError(QMqttClient::ClientState s, QMqttClient::ClientError e)
{
    Q_Q(QMqttClient);

    if (e != QMqttClient::NoError)
        q->setError(e);
    q->setState(s);
}

//  from ../qtmqtt/src/mqtt/qmqttclient.cpp, line 1112, as _ZN18QMqttClientPrivate11setClientIdERK7QString
inline void QMqttClientPrivate::setClientId(const QString &id)
{
    Q_Q(QMqttClient);

    if (m_clientId == id)
        return;

    m_clientId = id;
    emit q->clientIdChanged(id);
}
//  -----------------------------------------------------------------------

//  QMqttClient *QMqttClientPrivate::q_func()
extern "C" Q_DECL_EXPORT
QMqttClient *ritual_ZN18QMqttClientPrivate6q_funcEv(
    QMqttClientPrivate *self) {
  return self->q_func();
}

//  const QMqttClient *QMqttClientPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QMqttClient *ritual_ZNK18QMqttClientPrivate6q_funcEv(
    const QMqttClientPrivate *self) {
  return self->q_func();
}

//  QMqttClientPrivate::~QMqttClientPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QMqttClientPrivateD1Ev(QMqttClientPrivate *self) {
  delete self;
}

//  void QMqttClientPrivate::setStateAndError(QMqttClient::ClientState s,
//      QMqttClient::ClientError e)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QMqttClientPrivate16setStateAndErrorEN11QMqttClient11ClientStateENS0_11ClientErrorE(
    QMqttClientPrivate *self,
    QMqttClient::ClientState s,
    QMqttClient::ClientError e) {
  self->setStateAndError(s, e);
}

//  void QMqttClientPrivate::setClientId(const QString &id)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QMqttClientPrivate11setClientIdERK7QString(
    QMqttClientPrivate *self,
    const QString *id) {
  self->setClientId(*id);
}
