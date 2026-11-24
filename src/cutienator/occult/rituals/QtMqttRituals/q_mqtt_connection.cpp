//  Written by dev_tooling.RitualGenerator from the records of
//  QtMqtt/6.12.0/QtMqtt/private/qmqttconnection_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtMqtt/6.12.0/QtMqtt/private/qmqttglobal_p.h>
#include <QtMqtt/QtMqtt>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMqtt/6.12.0/QtMqtt/private/qmqttconnection_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMqtt/qmqtttopicfilter.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qmqttclient.h"
#include "qmqttclient_p.h"
#ifdef QT_MQTT_WITH_WEBSOCKETS
#endif
#include <QtCore/QLoggingCategory>
#include <QtCore/QUuid>
#include <QtCore/QtEndian>
#include "qmqttconnection_p.h"
#include "qmqttconnectionproperties_p.h"
#include "qmqttcontrolpacket_p.h"
#include "qmqttmessage_p.h"
#include "qmqttpublishproperties_p.h"
#include "qmqttsubscription_p.h"
#include "qmqttclient_p.h"
#include <QtCore/QLoggingCategory>
#include <QtNetwork/QSslSocket>
#include <QtNetwork/QTcpSocket>
#include <limits>
#include <cstdint>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtmqtt/src/mqtt/qmqttclient.cpp, line 1103, as _ZN18QMqttClientPrivate16setStateAndErrorEN11QMqttClient11ClientStateENS0_11ClientErrorE
inline void QMqttClientPrivate::setStateAndError(QMqttClient::ClientState s, QMqttClient::ClientError e)
{
    Q_Q(QMqttClient);

    if (e != QMqttClient::NoError)
        q->setError(e);
    q->setState(s);
}

//  from ../qtmqtt/src/mqtt/qmqttconnection.cpp, line 85, as _ZN15QMqttConnectionD1Ev
inline QMqttConnection::~QMqttConnection()
{
    if (m_internalState == BrokerConnected)
        sendControlDisconnect();
    m_transport = nullptr;
}

//  from ../qtmqtt/src/mqtt/qmqttconnection.cpp, line 200, as _ZNK15QMqttConnection9transportEv
inline QIODevice *QMqttConnection::transport() const
{
    return m_transport.get();
}

//  from ../qtmqtt/src/mqtt/qmqttconnection.cpp, line 744, as _ZN15QMqttConnection16setClientPrivateEP18QMqttClientPrivate
inline void QMqttConnection::setClientPrivate(QMqttClientPrivate *clientPrivate)
{
    m_clientPrivate = clientPrivate;
}

//  from ../qtmqtt/src/mqtt/qmqttconnection.cpp, line 774, as _ZN15QMqttConnection18cleanSubscriptionsEv
inline void QMqttConnection::cleanSubscriptions()
{
    for (auto item : std::as_const(m_pendingSubscriptionAck))
        item->setState(QMqttSubscription::Unsubscribed);
    m_pendingSubscriptionAck.clear();

    for (auto item : std::as_const(m_pendingUnsubscriptions))
        item->setState(QMqttSubscription::Unsubscribed);
    m_pendingUnsubscriptions.clear();

    for (auto item : std::as_const(m_activeSubscriptions))
        item->setState(QMqttSubscription::Unsubscribed);
    m_activeSubscriptions.clear();
}

//  from ../qtmqtt/src/mqtt/qmqttconnection.cpp, line 803, as _ZN15QMqttConnection25transportConnectionClosedEv
inline void QMqttConnection::transportConnectionClosed()
{
    m_readBuffer.clear();
    m_readPosition = 0;
    m_pingTimer.stop();
    m_pingTimeout = 0;
    if (m_internalState == ClientDestruction)
        return;
    if (m_internalState == BrokerDisconnected) // We manually disconnected
        m_clientPrivate->setStateAndError(QMqttClient::Disconnected, QMqttClient::NoError);
    else
        m_clientPrivate->setStateAndError(QMqttClient::Disconnected, QMqttClient::TransportInvalid);
}

//  from ../qtmqtt/src/mqtt/qmqttconnection.cpp, line 92, as _ZN15QMqttConnection10timerEventEP11QTimerEvent
inline void QMqttConnection::timerEvent(QTimerEvent *event)
{
    if (Q_LIKELY(event->timerId() == m_pingTimer.timerId())) {
        sendControlPingRequest();
        return;
    }

    QObject::timerEvent(event);
}

//  from ../qtmqtt/src/mqtt/qmqttconnection.cpp, line 862, as _ZN15QMqttConnection15closeConnectionEN11QMqttClient11ClientErrorE
inline void QMqttConnection::closeConnection(QMqttClient::ClientError error)
{
    m_readBuffer.clear();
    m_readPosition = 0;
    m_pingTimer.stop();
    m_pingTimeout = 0;
    m_activeSubscriptions.clear();
    m_internalState = BrokerDisconnected;
    m_transport->disconnect();
    m_transport->close();
    m_clientPrivate->setStateAndError(QMqttClient::Disconnected, error);
}

//  from ../qtmqtt/src/mqtt/qmqttconnection.cpp, line 62, as _ZNK15QMqttConnection20isPendingUnsubscribeEP17QMqttSubscription
inline bool QMqttConnection::isPendingUnsubscribe(QMqttSubscription *sub) const
{
    for (const auto [key, value] : m_pendingUnsubscriptions.asKeyValueRange()) {
        if (value == sub)
            return true;
    }
    return false;
}

//  from ../qtmqtt/src/mqtt/qmqttconnection.cpp, line 71, as _ZNK15QMqttConnection22findActiveSubscriptionERK16QMqttTopicFilter
inline QMqttSubscription *QMqttConnection::findActiveSubscription(const QMqttTopicFilter &topic) const
{
    const auto range = m_activeSubscriptions.equal_range(topic);
    for (auto it = range.first; it != range.second; ++it) {
        if (!isPendingUnsubscribe(it.value()))
            return it.value();
    }
    return nullptr;
}
//  -----------------------------------------------------------------------

//  A QMqttConnection that Python can take functions over in. Every QMqttConnection
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQMqttConnectionCall0)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQMqttConnectionCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQMqttConnectionCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQMqttConnectionCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQMqttConnectionCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQMqttConnectionCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQMqttConnectionCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQMqttConnection : public QMqttConnection {
public:
  using QMqttConnection::QMqttConnection;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !defined(QT_NO_QOBJECT)
  //  void QMqttConnection::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQMqttConnectionCall0 call = reinterpret_cast<CuteQMqttConnectionCall0>(taken[0]);
      call(this, event, &handled);
      if (handled) return;
    }
    QMqttConnection::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQMqttConnectionCall1 call = reinterpret_cast<CuteQMqttConnectionCall1>(taken[1]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQMqttConnectionCall2 call = reinterpret_cast<CuteQMqttConnectionCall2>(taken[2]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQMqttConnectionCall3 call = reinterpret_cast<CuteQMqttConnectionCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQMqttConnectionCall4 call = reinterpret_cast<CuteQMqttConnectionCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteQMqttConnectionCall5 call = reinterpret_cast<CuteQMqttConnectionCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQMqttConnectionCall6 call = reinterpret_cast<CuteQMqttConnectionCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QMqttConnection::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QMqttConnection10metaObjectEv(
    const QMqttConnection *self) {
  return self->metaObject();
}

//  QMqttConnection::~QMqttConnection()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QMqttConnectionD1Ev(QMqttConnection *self) {
  delete self;
}

//  QIODevice *QMqttConnection::transport() const
extern "C" Q_DECL_EXPORT
QIODevice *ritual_ZNK15QMqttConnection9transportEv(
    const QMqttConnection *self) {
  return self->transport();
}

//  void QMqttConnection::setClientPrivate(QMqttClientPrivate *clientPrivate)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QMqttConnection16setClientPrivateEP18QMqttClientPrivate(
    QMqttConnection *self,
    QMqttClientPrivate *clientPrivate) {
  self->setClientPrivate(clientPrivate);
}

//  InternalConnectionState QMqttConnection::internalState() const
extern "C" Q_DECL_EXPORT
QMqttConnection::InternalConnectionState ritual_ZNK15QMqttConnection13internalStateEv(
    const QMqttConnection *self) {
  return self->internalState();
}

//  void QMqttConnection::setClientDestruction()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QMqttConnection20setClientDestructionEv(
    QMqttConnection *self) {
  self->setClientDestruction();
}

//  void QMqttConnection::cleanSubscriptions()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QMqttConnection18cleanSubscriptionsEv(
    QMqttConnection *self) {
  self->cleanSubscriptions();
}

//  void QMqttConnection::transportConnectionClosed()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QMqttConnection25transportConnectionClosedEv(
    QMqttConnection *self) {
  self->transportConnectionClosed();
}

//  void QMqttConnection::timerEvent(QTimerEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QMqttConnection10timerEventEP11QTimerEvent(
    QMqttConnection *self,
    QTimerEvent *event) {
  self->timerEvent(event);
}

//  void QMqttConnection::closeConnection(QMqttClient::ClientError error)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QMqttConnection15closeConnectionEN11QMqttClient11ClientErrorE(
    QMqttConnection *self,
    QMqttClient::ClientError error) {
  self->closeConnection(error);
}

//  bool QMqttConnection::isPendingUnsubscribe(QMqttSubscription *a0) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QMqttConnection20isPendingUnsubscribeEP17QMqttSubscription(
    const QMqttConnection *self,
    QMqttSubscription *a0) {
  return self->isPendingUnsubscribe(a0);
}

//  QMqttSubscription *QMqttConnection::findActiveSubscription(const
//      QMqttTopicFilter &topic) const
extern "C" Q_DECL_EXPORT
QMqttSubscription *ritual_ZNK15QMqttConnection22findActiveSubscriptionERK16QMqttTopicFilter(
    const QMqttConnection *self,
    const QMqttTopicFilter *topic) {
  return self->findActiveSubscription(*topic);
}

//  a Python function taken by a CuteQMqttConnection, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QMqttConnection(
    QMqttConnection *self,
    const char *key,
    void *call) {
  return static_cast<CuteQMqttConnection *>(self)->take(key, call);
}
