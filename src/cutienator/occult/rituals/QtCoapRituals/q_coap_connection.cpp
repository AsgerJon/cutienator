//  Written by dev_tooling.RitualGenerator from the records of
//  QtCoap/6.12.0/QtCoap/private/qcoapconnection_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtNetwork/qtnetworkglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCoap/QtCoap>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCoap/6.12.0/QtCoap/private/qcoapconnection_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCoap/qcoapsecurityconfiguration.h>
#include <QtNetwork/qnetworkinterface.h>
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qcoapconnection_p.h"
#include <QtCore/qloggingcategory.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtcoap/src/coap/qcoapconnection.cpp, line 189, as _ZNK15QCoapConnection8isSecureEv
inline bool QCoapConnection::isSecure() const
{
    Q_D(const QCoapConnection);
    return d->securityMode != QtCoap::SecurityMode::NoSecurity;
}

//  from ../qtcoap/src/coap/qcoapconnection.cpp, line 200, as _ZNK15QCoapConnection12securityModeEv
inline QtCoap::SecurityMode QCoapConnection::securityMode() const
{
    Q_D(const QCoapConnection);
    return d->securityMode;
}

//  from ../qtcoap/src/coap/qcoapconnection.cpp, line 211, as _ZNK15QCoapConnection5stateEv
inline QCoapConnection::ConnectionState QCoapConnection::state() const
{
    Q_D(const QCoapConnection);
    return d->state;
}

//  from ../qtcoap/src/coap/qcoapconnection.cpp, line 258, as _ZNK15QCoapConnection21securityConfigurationEv
inline QCoapSecurityConfiguration QCoapConnection::securityConfiguration() const
{
    Q_D(const QCoapConnection);
    return d->securityConfiguration;
}

//  from ../qtcoap/src/coap/qcoapconnection.cpp, line 270, as _ZN15QCoapConnection10disconnectEv
inline void QCoapConnection::disconnect()
{
    Q_D(QCoapConnection);

    close();

    d->framesToSend.clear();
    d->state = ConnectionState::Unconnected;
}

//  from ../qtcoap/src/coap/qcoapconnection.cpp, line 284, as _ZN15QCoapConnection22setUdpNetworkInterfaceERK17QNetworkInterface
#if QT_CONFIG(networkinterface)
inline void QCoapConnection::setUdpNetworkInterface(const QNetworkInterface &iface)
{
    Q_D(QCoapConnection);
    d->udpNetworkInterface = iface;
}
#endif  // QT_CONFIG(networkinterface)

//  from ../qtcoap/src/coap/qcoapconnection.cpp, line 293, as _ZNK15QCoapConnection19udpNetworkInterfaceEv
#if QT_CONFIG(networkinterface)
inline QNetworkInterface QCoapConnection::udpNetworkInterface() const
{
    Q_D(const QCoapConnection);
    return d->udpNetworkInterface;
}
#endif  // QT_CONFIG(networkinterface)

//  from ../qtcoap/src/coap/qcoapconnection.cpp, line 223, as _ZN15QCoapConnection18startToSendRequestEv
inline void QCoapConnection::startToSendRequest()
{
    Q_D(QCoapConnection);

    Q_ASSERT(!d->framesToSend.isEmpty());
    while (!d->framesToSend.isEmpty()) {
        const CoapFrame frame = d->framesToSend.dequeue();
        writeData(frame.currentPdu, frame.host, frame.port);
    }
}
//  -----------------------------------------------------------------------

//  A QCoapConnection that Python can take functions over in. Every QCoapConnection
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQCoapConnectionCall0)(const void *, const QString *, quint16, int *);
typedef void (*CuteQCoapConnectionCall1)(const void *, const QByteArray *, const QString *, quint16, int *);
typedef void (*CuteQCoapConnectionCall2)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQCoapConnectionCall3)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQCoapConnectionCall4)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCoapConnectionCall5)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCoapConnectionCall6)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCoapConnectionCall7)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCoapConnectionCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCoapConnectionCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQCoapConnection : public QCoapConnection {
public:
  using QCoapConnection::QCoapConnection;
  void *taken[10] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN15QCoapConnection4bindERK7QStringt")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QCoapConnection9writeDataERK10QByteArrayRK7QStringt")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QCoapConnection5closeEv")) {
      taken[2] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QCoapConnection::bind(const QString &host, quint16 port)
  void bind(const QString &host, quint16 port) override {
    if (taken[0]) {
      int handled = 0;
      CuteQCoapConnectionCall0 call = reinterpret_cast<CuteQCoapConnectionCall0>(taken[0]);
      call(this, &host, port, &handled);
      if (handled) return;
    }
  }

  //  void QCoapConnection::writeData(const QByteArray &data, const QString
  //      &host, quint16 port)
  void writeData(
      const QByteArray &data,
      const QString &host,
      quint16 port) override {
    if (taken[1]) {
      int handled = 0;
      CuteQCoapConnectionCall1 call = reinterpret_cast<CuteQCoapConnectionCall1>(taken[1]);
      call(this, &data, &host, port, &handled);
      if (handled) return;
    }
  }

  //  void QCoapConnection::close()
  void close() override {
    if (taken[2]) {
      int handled = 0;
      CuteQCoapConnectionCall2 call = reinterpret_cast<CuteQCoapConnectionCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQCoapConnectionCall3 call = reinterpret_cast<CuteQCoapConnectionCall3>(taken[3]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQCoapConnectionCall4 call = reinterpret_cast<CuteQCoapConnectionCall4>(taken[4]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQCoapConnectionCall5 call = reinterpret_cast<CuteQCoapConnectionCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQCoapConnectionCall6 call = reinterpret_cast<CuteQCoapConnectionCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQCoapConnectionCall7 call = reinterpret_cast<CuteQCoapConnectionCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[8]) {
      int handled = 0;
      CuteQCoapConnectionCall8 call = reinterpret_cast<CuteQCoapConnectionCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[9]) {
      int handled = 0;
      CuteQCoapConnectionCall9 call = reinterpret_cast<CuteQCoapConnectionCall9>(taken[9]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QCoapConnection::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QCoapConnection10metaObjectEv(
    const QCoapConnection *self) {
  return self->metaObject();
}

//  QCoapConnection::~QCoapConnection()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCoapConnectionD1Ev(QCoapConnection *self) {
  delete self;
}

//  bool QCoapConnection::isSecure() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QCoapConnection8isSecureEv(const QCoapConnection *self) {
  return self->isSecure();
}

//  QtCoap::SecurityMode QCoapConnection::securityMode() const
extern "C" Q_DECL_EXPORT
QtCoap::SecurityMode ritual_ZNK15QCoapConnection12securityModeEv(
    const QCoapConnection *self) {
  return self->securityMode();
}

//  ConnectionState QCoapConnection::state() const
extern "C" Q_DECL_EXPORT
QCoapConnection::ConnectionState ritual_ZNK15QCoapConnection5stateEv(
    const QCoapConnection *self) {
  return self->state();
}

//  QCoapSecurityConfiguration QCoapConnection::securityConfiguration() const
extern "C" Q_DECL_EXPORT
QCoapSecurityConfiguration *ritual_ZNK15QCoapConnection21securityConfigurationEv(
    const QCoapConnection *self) {
  return new QCoapSecurityConfiguration(self->securityConfiguration());
}

//  void QCoapConnection::disconnect()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCoapConnection10disconnectEv(QCoapConnection *self) {
  self->disconnect();
}

#if QT_CONFIG(networkinterface)
//  void QCoapConnection::setUdpNetworkInterface(const QNetworkInterface
//      &iface)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCoapConnection22setUdpNetworkInterfaceERK17QNetworkInterface(
    QCoapConnection *self,
    const QNetworkInterface *iface) {
  self->setUdpNetworkInterface(*iface);
}
#endif  // QT_CONFIG(networkinterface)

#if QT_CONFIG(networkinterface)
//  QNetworkInterface QCoapConnection::udpNetworkInterface() const
extern "C" Q_DECL_EXPORT
QNetworkInterface *ritual_ZNK15QCoapConnection19udpNetworkInterfaceEv(
    const QCoapConnection *self) {
  return new QNetworkInterface(self->udpNetworkInterface());
}
#endif  // QT_CONFIG(networkinterface)

//  void QCoapConnection::startToSendRequest()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCoapConnection18startToSendRequestEv(
    QCoapConnection *self) {
  self->startToSendRequest();
}

//  void QCoapConnection::bind(const QString &host, quint16 port)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCoapConnection4bindERK7QStringt(
    QCoapConnection *self,
    const QString *host,
    quint16 port) {
  self->bind(*host, port);
}

//  void QCoapConnection::writeData(const QByteArray &data, const QString
//      &host, quint16 port)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCoapConnection9writeDataERK10QByteArrayRK7QStringt(
    QCoapConnection *self,
    const QByteArray *data,
    const QString *host,
    quint16 port) {
  self->writeData(*data, *host, port);
}

//  void QCoapConnection::close()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCoapConnection5closeEv(QCoapConnection *self) {
  self->close();
}

//  QCoapConnectionPrivate *QCoapConnection::d_func()
extern "C" Q_DECL_EXPORT
QCoapConnectionPrivate *ritual_ZN15QCoapConnection6d_funcEv(
    QCoapConnection *self) {
  return self->d_func();
}

//  const QCoapConnectionPrivate *QCoapConnection::d_func() const
extern "C" Q_DECL_EXPORT
const QCoapConnectionPrivate *ritual_ZNK15QCoapConnection6d_funcEv(
    const QCoapConnection *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQCoapConnection, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QCoapConnection(
    QCoapConnection *self,
    const char *key,
    void *call) {
  return static_cast<CuteQCoapConnection *>(self)->take(key, call);
}
