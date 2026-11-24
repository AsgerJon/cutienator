//  Written by dev_tooling.RitualGenerator from the records of QtRemoteObject
//  s/6.12.0/QtRemoteObjects/private/qconnection_tcpip_backend_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtRemoteObjects/QtRemoteObjects>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtRemoteObjects/6.12.0/QtRemoteObjects/private/qconnection_tcpip_backend_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qconnection_tcpip_backend_p.h"
#include <QtNetwork/qhostinfo.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtremoteobjects/src/remoteobjects/qconnection_tcpip_backend.cpp, line 20, as _ZN11TcpClientIoD1Ev
inline TcpClientIo::~TcpClientIo()
{
    close();
}

//  from ../qtremoteobjects/src/remoteobjects/qconnection_tcpip_backend.cpp, line 25, as _ZNK11TcpClientIo10connectionEv
inline QIODevice *TcpClientIo::connection() const
{
    return m_socket;
}

//  from ../qtremoteobjects/src/remoteobjects/qconnection_tcpip_backend.cpp, line 45, as _ZN11TcpClientIo15connectToServerEv
inline void TcpClientIo::connectToServer()
{
    if (isOpen())
        return;
    const QString &host = url().host();
    QHostAddress address(host);
    if (address.isNull())
        address = QHostInfo::fromName(host).addresses().value(0);

    if (address.isNull())
        qWarning("connectToServer(): Failed to resolve host %s", qUtf8Printable(host));
    else
        m_socket->connectToHost(address, url().port());
}

//  from ../qtremoteobjects/src/remoteobjects/qconnection_tcpip_backend.cpp, line 60, as _ZNK11TcpClientIo6isOpenEv
inline bool TcpClientIo::isOpen() const
{
    return (!isClosing() && (m_socket->state() == QAbstractSocket::ConnectedState
                             || m_socket->state() == QAbstractSocket::ConnectingState));
}

//  from ../qtremoteobjects/src/remoteobjects/qconnection_tcpip_backend.cpp, line 84, as _ZN11TcpClientIo14onStateChangedEN15QAbstractSocket11SocketStateE
inline void TcpClientIo::onStateChanged(QAbstractSocket::SocketState state)
{
    if (state == QAbstractSocket::ClosingState && !isClosing()) {
        m_socket->abort();
        emit shouldReconnect(this);
    }
    if (state == QAbstractSocket::ConnectedState)
        initializeDataStream();
}

//  from ../qtremoteobjects/src/remoteobjects/qconnection_tcpip_backend.cpp, line 30, as _ZN11TcpClientIo7doCloseEv
inline void TcpClientIo::doClose()
{
    if (m_socket->isOpen()) {
        connect(m_socket, &QTcpSocket::disconnected, this, &QObject::deleteLater);
        m_socket->disconnectFromHost();
    } else {
        this->deleteLater();
    }
}

//  from ../qtremoteobjects/src/remoteobjects/qconnection_tcpip_backend.cpp, line 40, as _ZN11TcpClientIo22doDisconnectFromServerEv
inline void TcpClientIo::doDisconnectFromServer()
{
    m_socket->disconnectFromHost();
}
//  -----------------------------------------------------------------------

//  TcpClientIo::~TcpClientIo()
extern "C" Q_DECL_EXPORT
void ritual_ZN11TcpClientIoD1Ev(TcpClientIo *self) {
  delete self;
}

//  QIODevice *TcpClientIo::connection() const
extern "C" Q_DECL_EXPORT
QIODevice *ritual_ZNK11TcpClientIo10connectionEv(const TcpClientIo *self) {
  return self->connection();
}

//  void TcpClientIo::connectToServer()
extern "C" Q_DECL_EXPORT
void ritual_ZN11TcpClientIo15connectToServerEv(TcpClientIo *self) {
  self->connectToServer();
}

//  bool TcpClientIo::isOpen() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11TcpClientIo6isOpenEv(const TcpClientIo *self) {
  return self->isOpen();
}

//  void TcpClientIo::onStateChanged(QAbstractSocket::SocketState state)
extern "C" Q_DECL_EXPORT
void ritual_ZN11TcpClientIo14onStateChangedEN15QAbstractSocket11SocketStateE(
    TcpClientIo *self,
    QAbstractSocket::SocketState state) {
  self->onStateChanged(state);
}

//  void TcpClientIo::doClose()
extern "C" Q_DECL_EXPORT
void ritual_ZN11TcpClientIo7doCloseEv(TcpClientIo *self) {
  self->doClose();
}

//  void TcpClientIo::doDisconnectFromServer()
extern "C" Q_DECL_EXPORT
void ritual_ZN11TcpClientIo22doDisconnectFromServerEv(TcpClientIo *self) {
  self->doDisconnectFromServer();
}
