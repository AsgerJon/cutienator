//  Written by dev_tooling.RitualGenerator from the records of
//  QtCoap/6.12.0/QtCoap/private/qcoapqudpconnection_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtNetwork/qtnetworkglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCoap/QtCoap>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCoap/6.12.0/QtCoap/private/qcoapqudpconnection_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qcoapconnection_p.h"
#include <QtCore/qloggingcategory.h>
#include "qcoapqudpconnection_p.h"
#include <private/qcoapnamespace_p.h>
#include <QtCore/qloggingcategory.h>
#include <QtNetwork/qnetworkdatagram.h>
#include <QtNetwork/private/qabstractsocket_p.h>
#if QT_CONFIG(dtls)
#include <QtNetwork/QDtls>
#include <QtNetwork/QSslPreSharedKeyAuthenticator>
#include <QtNetwork/QSslConfiguration>
#include <QtNetwork/QSslKey>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtcoap/src/coap/qcoapconnection.cpp, line 258, as _ZNK15QCoapConnection21securityConfigurationEv
inline QCoapSecurityConfiguration QCoapConnection::securityConfiguration() const
{
    Q_D(const QCoapConnection);
    return d->securityConfiguration;
}

//  from ../qtcoap/src/coap/qcoapqudpconnection.cpp, line 271, as _ZN26QCoapQUdpConnectionPrivate13writeToSocketERK10QByteArrayRK7QStringt
inline void QCoapQUdpConnectionPrivate::writeToSocket(const QByteArray &data, const QString &host, quint16 port)
{
#if QT_CONFIG(dtls)
    Q_Q(QCoapQUdpConnection);
#endif
    if (!socket()->isWritable()) {
        bool opened = socket()->open(socket()->openMode() | QIODevice::WriteOnly);
        if (!opened) {
            qCWarning(lcCoapConnection, "Failed to open the UDP socket with write permission");
            return;
        }
    }

    QHostAddress hostAddress(host);
    if (hostAddress.isNull()) {
        qCWarning(lcCoapConnection) << "Invalid host IP address" << host
                                    << "- only IPv4/IPv6 destination addresses are supported.";
        return;
    }

    const qint64 bytesWritten =
#if QT_CONFIG(dtls)
            q->isSecure() ? (Q_ASSERT(dtls), dtls->writeDatagramEncrypted(socket(), data)) :
#endif
            socket()->writeDatagram(data, hostAddress, port);

    if (bytesWritten < 0)
        qCWarning(lcCoapConnection) << "Failed to write datagram:" << socket()->errorString();
}

//  from ../qtcoap/src/coap/qcoapconnection.cpp, line 189, as _ZNK15QCoapConnection8isSecureEv
inline bool QCoapConnection::isSecure() const
{
    Q_D(const QCoapConnection);
    return d->securityMode != QtCoap::SecurityMode::NoSecurity;
}

//  from ../qtcoap/src/coap/qcoapqudpconnection.cpp, line 337, as _ZNK19QCoapQUdpConnection6socketEv
inline QUdpSocket *QCoapQUdpConnection::socket() const
{
    Q_D(const QCoapQUdpConnection);
    return d->udpSocket;
}

//  from ../qtcoap/src/coap/qcoapqudpconnection.cpp, line 260, as _ZN19QCoapQUdpConnection15setSocketOptionEN15QAbstractSocket12SocketOptionERK8QVariant
inline void QCoapQUdpConnection::setSocketOption(QAbstractSocket::SocketOption option, const QVariant &value)
{
    Q_D(QCoapQUdpConnection);
    d->socket()->setSocketOption(option, value);
}

//  from ../qtcoap/src/coap/qcoapqudpconnection.cpp, line 413, as _ZN19QCoapQUdpConnection11pskRequiredEP29QSslPreSharedKeyAuthenticator
#if QT_CONFIG(dtls)
inline void QCoapQUdpConnection::pskRequired(QSslPreSharedKeyAuthenticator *authenticator)
{
    Q_ASSERT(authenticator);
    authenticator->setIdentity(securityConfiguration().preSharedKeyIdentity());
    authenticator->setPreSharedKey(securityConfiguration().preSharedKey());
}
#endif  // QT_CONFIG(dtls)

//  from ../qtcoap/src/coap/qcoapqudpconnection.cpp, line 196, as _ZN19QCoapQUdpConnection4bindERK7QStringt
inline void QCoapQUdpConnection::bind(const QString &host, quint16 port)
{
    Q_D(QCoapQUdpConnection);

    if (!isSecure()) {
        d->bindSocket();
#if QT_CONFIG(dtls)
    } else {
        Q_ASSERT(d->dtls);
        if (d->dtls->isConnectionEncrypted()) {
            emit bound();
        } else if (socket()->state() == QAbstractSocket::UnconnectedState) {
            d->bind();
            d->dtls->setPeer(QHostAddress(host), port);
            if (!d->dtls->doHandshake(d->socket()))
                qCWarning(lcCoapConnection) << "Handshake error: " << d->dtls->dtlsErrorString();
        }
#else
        Q_UNUSED(host);
        Q_UNUSED(port);
#endif
    }
}

//  from ../qtcoap/src/coap/qcoapqudpconnection.cpp, line 225, as _ZN19QCoapQUdpConnection9writeDataERK10QByteArrayRK7QStringt
inline void QCoapQUdpConnection::writeData(const QByteArray &data, const QString &host, quint16 port)
{
    Q_D(QCoapQUdpConnection);
    d->writeToSocket(data, host, port);
}

//  from ../qtcoap/src/coap/qcoapqudpconnection.cpp, line 239, as _ZN19QCoapQUdpConnection5closeEv
inline void QCoapQUdpConnection::close()
{
    Q_D(QCoapQUdpConnection);

#if QT_CONFIG(dtls)
    if (isSecure()) {
        if (d->dtls->handshakeState() == QDtls::HandshakeInProgress)
            d->dtls->abortHandshake(d->socket());

        if (d->dtls->isConnectionEncrypted())
            d->dtls->shutdown(d->socket());
    }
#endif
    d->socket()->close();
}
//  -----------------------------------------------------------------------

//  Only a class built on QCoapQUdpConnection may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQCoapQUdpConnection : QCoapQUdpConnection {
  using QCoapQUdpConnection::close;
};

//  A QCoapQUdpConnection that Python can take functions over in. Every QCoapQUdpConnection
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQCoapQUdpConnectionCall0)(const void *, const QString *, quint16, int *);
typedef void (*CuteQCoapQUdpConnectionCall1)(const void *, const QByteArray *, const QString *, quint16, int *);
typedef void (*CuteQCoapQUdpConnectionCall2)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQCoapQUdpConnectionCall3)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQCoapQUdpConnectionCall4)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCoapQUdpConnectionCall5)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCoapQUdpConnectionCall6)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCoapQUdpConnectionCall7)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCoapQUdpConnectionCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCoapQUdpConnectionCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQCoapQUdpConnection : public QCoapQUdpConnection {
public:
  using QCoapQUdpConnection::QCoapQUdpConnection;
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

  //  void QCoapQUdpConnection::bind(const QString &host, quint16 port)
  void bind(const QString &host, quint16 port) override {
    if (taken[0]) {
      int handled = 0;
      CuteQCoapQUdpConnectionCall0 call = reinterpret_cast<CuteQCoapQUdpConnectionCall0>(taken[0]);
      call(this, &host, port, &handled);
      if (handled) return;
    }
    QCoapQUdpConnection::bind(host, port);
  }

  //  void QCoapQUdpConnection::writeData(const QByteArray &data, const
  //      QString &host, quint16 port)
  void writeData(
      const QByteArray &data,
      const QString &host,
      quint16 port) override {
    if (taken[1]) {
      int handled = 0;
      CuteQCoapQUdpConnectionCall1 call = reinterpret_cast<CuteQCoapQUdpConnectionCall1>(taken[1]);
      call(this, &data, &host, port, &handled);
      if (handled) return;
    }
    QCoapQUdpConnection::writeData(data, host, port);
  }

  //  void QCoapQUdpConnection::close()
  void close() override {
    if (taken[2]) {
      int handled = 0;
      CuteQCoapQUdpConnectionCall2 call = reinterpret_cast<CuteQCoapQUdpConnectionCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QCoapQUdpConnection::close();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQCoapQUdpConnectionCall3 call = reinterpret_cast<CuteQCoapQUdpConnectionCall3>(taken[3]);
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
      CuteQCoapQUdpConnectionCall4 call = reinterpret_cast<CuteQCoapQUdpConnectionCall4>(taken[4]);
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
      CuteQCoapQUdpConnectionCall5 call = reinterpret_cast<CuteQCoapQUdpConnectionCall5>(taken[5]);
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
      CuteQCoapQUdpConnectionCall6 call = reinterpret_cast<CuteQCoapQUdpConnectionCall6>(taken[6]);
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
      CuteQCoapQUdpConnectionCall7 call = reinterpret_cast<CuteQCoapQUdpConnectionCall7>(taken[7]);
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
      CuteQCoapQUdpConnectionCall8 call = reinterpret_cast<CuteQCoapQUdpConnectionCall8>(taken[8]);
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
      CuteQCoapQUdpConnectionCall9 call = reinterpret_cast<CuteQCoapQUdpConnectionCall9>(taken[9]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QCoapQUdpConnection::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19QCoapQUdpConnection10metaObjectEv(
    const QCoapQUdpConnection *self) {
  return self->metaObject();
}

//  QCoapQUdpConnection::~QCoapQUdpConnection()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QCoapQUdpConnectionD1Ev(QCoapQUdpConnection *self) {
  delete self;
}

//  QUdpSocket *QCoapQUdpConnection::socket() const
extern "C" Q_DECL_EXPORT
QUdpSocket *ritual_ZNK19QCoapQUdpConnection6socketEv(
    const QCoapQUdpConnection *self) {
  return self->socket();
}

//  void QCoapQUdpConnection::setSocketOption(QAbstractSocket::SocketOption
//      a0, const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QCoapQUdpConnection15setSocketOptionEN15QAbstractSocket12SocketOptionERK8QVariant(
    QCoapQUdpConnection *self,
    QAbstractSocket::SocketOption a0,
    const QVariant *value) {
  self->setSocketOption(a0, *value);
}

#if QT_CONFIG(dtls)
//  void QCoapQUdpConnection::pskRequired(QSslPreSharedKeyAuthenticator
//      *authenticator)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QCoapQUdpConnection11pskRequiredEP29QSslPreSharedKeyAuthenticator(
    QCoapQUdpConnection *self,
    QSslPreSharedKeyAuthenticator *authenticator) {
  self->pskRequired(authenticator);
}
#endif  // QT_CONFIG(dtls)

//  void QCoapQUdpConnection::bind(const QString &host, quint16 port)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QCoapQUdpConnection4bindERK7QStringt(
    QCoapQUdpConnection *self,
    const QString *host,
    quint16 port) {
  self->bind(*host, port);
}

//  void QCoapQUdpConnection::writeData(const QByteArray &data, const QString
//      &host, quint16 port)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QCoapQUdpConnection9writeDataERK10QByteArrayRK7QStringt(
    QCoapQUdpConnection *self,
    const QByteArray *data,
    const QString *host,
    quint16 port) {
  self->writeData(*data, *host, port);
}

//  void QCoapQUdpConnection::close()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QCoapQUdpConnection5closeEv(QCoapQUdpConnection *self) {
  self->close();
}

//  QCoapQUdpConnectionPrivate *QCoapQUdpConnection::d_func()
extern "C" Q_DECL_EXPORT
QCoapQUdpConnectionPrivate *ritual_ZN19QCoapQUdpConnection6d_funcEv(
    QCoapQUdpConnection *self) {
  return self->d_func();
}

//  const QCoapQUdpConnectionPrivate *QCoapQUdpConnection::d_func() const
extern "C" Q_DECL_EXPORT
const QCoapQUdpConnectionPrivate *ritual_ZNK19QCoapQUdpConnection6d_funcEv(
    const QCoapQUdpConnection *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQCoapQUdpConnection, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QCoapQUdpConnection(
    QCoapQUdpConnection *self,
    const char *key,
    void *call) {
  return static_cast<CuteQCoapQUdpConnection *>(self)->take(key, call);
}

//  void QCoapQUdpConnection::close()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QCoapQUdpConnection5closeEv(QCoapQUdpConnection *self) {
  static_cast<OwnQCoapQUdpConnection *>(self)->OwnQCoapQUdpConnection::close();
}
