//  Written by dev_tooling.RitualGenerator from the records of
//  QtCoap/6.12.0/QtCoap/private/qcoapqudpconnection_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCoap/QtCoap>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCoap/6.12.0/QtCoap/private/qcoapqudpconnection_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/qnetworkdatagram.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
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

//  from ../qtcoap/src/coap/qcoapqudpconnection.cpp, line 161, as _ZN26QCoapQUdpConnectionPrivate4bindEv
inline bool QCoapQUdpConnectionPrivate::bind()
{
#if QT_CONFIG(networkinterface)
    // Using the QAbstractSocketPrivate private API to bind to a specific
    // network interface.
    auto priv = static_cast<QAbstractSocketPrivate *>(QObjectPrivate::get(socket()));
    QNetworkInterface *iface = udpNetworkInterface.isValid() ? &udpNetworkInterface : nullptr;
    return priv->bind(QHostAddress::Any, 0, QAbstractSocket::ShareAddress, iface);
#else
    return socket()->bind(QHostAddress::Any, 0, QAbstractSocket::ShareAddress);
#endif
}

//  from ../qtcoap/src/coap/qcoapqudpconnection.cpp, line 146, as _ZN26QCoapQUdpConnectionPrivateD1Ev
inline QCoapQUdpConnectionPrivate::~QCoapQUdpConnectionPrivate()
{
#if QT_CONFIG(dtls)
    if (dtls && dtls->isConnectionEncrypted()) {
        Q_ASSERT(udpSocket);
        dtls->shutdown(udpSocket);
    }
#endif
}

//  from ../qtcoap/src/coap/qcoapqudpconnection.cpp, line 393, as _ZNK26QCoapQUdpConnectionPrivate31datagramMatchesNetworkInterfaceERK16QNetworkDatagram
inline bool QCoapQUdpConnectionPrivate::datagramMatchesNetworkInterface(
        const QNetworkDatagram &datagram) const
{
#if QT_CONFIG(networkinterface)
    return !udpNetworkInterface.isValid()
            || uint(udpNetworkInterface.index()) == datagram.interfaceIndex();
#else
    Q_UNUSED(datagram);
    return true;
#endif
}
//  -----------------------------------------------------------------------

//  A QCoapQUdpConnectionPrivate that Python can take functions over in. Every QCoapQUdpConnectionPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQCoapQUdpConnectionPrivateCall0)(const void *, int *);
class CuteQCoapQUdpConnectionPrivate : public QCoapQUdpConnectionPrivate {
public:
  using QCoapQUdpConnectionPrivate::QCoapQUdpConnectionPrivate;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN26QCoapQUdpConnectionPrivate4bindEv")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  bool QCoapQUdpConnectionPrivate::bind()
  bool bind() override {
    if (taken[0]) {
      int handled = 0;
      CuteQCoapQUdpConnectionPrivateCall0 call = reinterpret_cast<CuteQCoapQUdpConnectionPrivateCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QCoapQUdpConnectionPrivate::bind();
  }
};

//  QCoapQUdpConnectionPrivate::~QCoapQUdpConnectionPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QCoapQUdpConnectionPrivateD1Ev(
    QCoapQUdpConnectionPrivate *self) {
  delete self;
}

//  bool QCoapQUdpConnectionPrivate::bind()
extern "C" Q_DECL_EXPORT
bool ritual_ZN26QCoapQUdpConnectionPrivate4bindEv(
    QCoapQUdpConnectionPrivate *self) {
  return self->bind();
}

//  QUdpSocket *QCoapQUdpConnectionPrivate::socket() const
extern "C" Q_DECL_EXPORT
QUdpSocket *ritual_ZNK26QCoapQUdpConnectionPrivate6socketEv(
    const QCoapQUdpConnectionPrivate *self) {
  return self->socket();
}

//  bool QCoapQUdpConnectionPrivate::datagramMatchesNetworkInterface(const
//      QNetworkDatagram &datagram) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK26QCoapQUdpConnectionPrivate31datagramMatchesNetworkInterfaceERK16QNetworkDatagram(
    const QCoapQUdpConnectionPrivate *self,
    const QNetworkDatagram *datagram) {
  return self->datagramMatchesNetworkInterface(*datagram);
}

//  QCoapQUdpConnection *QCoapQUdpConnectionPrivate::q_func()
extern "C" Q_DECL_EXPORT
QCoapQUdpConnection *ritual_ZN26QCoapQUdpConnectionPrivate6q_funcEv(
    QCoapQUdpConnectionPrivate *self) {
  return self->q_func();
}

//  const QCoapQUdpConnection *QCoapQUdpConnectionPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QCoapQUdpConnection *ritual_ZNK26QCoapQUdpConnectionPrivate6q_funcEv(
    const QCoapQUdpConnectionPrivate *self) {
  return self->q_func();
}

//  a Python function taken by a CuteQCoapQUdpConnectionPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QCoapQUdpConnectionPrivate(
    QCoapQUdpConnectionPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQCoapQUdpConnectionPrivate *>(self)->take(key, call);
}

//  bool QCoapQUdpConnectionPrivate::bind()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN26QCoapQUdpConnectionPrivate4bindEv(
    QCoapQUdpConnectionPrivate *self) {
  return self->QCoapQUdpConnectionPrivate::bind();
}
