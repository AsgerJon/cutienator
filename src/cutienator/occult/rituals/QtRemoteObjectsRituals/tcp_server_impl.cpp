//  Written by dev_tooling.RitualGenerator from the records of QtRemoteObject
//  s/6.12.0/QtRemoteObjects/private/qconnection_tcpip_backend_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtRemoteObjects/QtRemoteObjects>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtRemoteObjects/6.12.0/QtRemoteObjects/private/qconnection_tcpip_backend_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qurl.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtRemoteObjects/private/qconnection_tcpip_backend_p.h>
#include <QtNetwork/qhostinfo.h>
#include <QtCore/qloggingcategory.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtremoteobjects/src/remoteobjects/qconnection_tcpip_backend.cpp, line 95, as _ZN11TcpServerIoC1EP10QTcpSocketP7QObject
inline TcpServerIo::TcpServerIo(QTcpSocket *conn, QObject *parent)
    : QtROServerIoDevice(parent), m_connection(conn)
{
    m_connection->setParent(this);
    connect(conn, &QIODevice::readyRead, this, &QtROServerIoDevice::readyRead);
    connect(conn, &QAbstractSocket::disconnected, this, &QtROServerIoDevice::disconnected);
}

//  from ../qtremoteobjects/src/remoteobjects/qtremoteobjectglobal.cpp, line 13, as _Z15QT_REMOTEOBJECTv
inline const QLoggingCategory &QT_REMOTEOBJECT()
{
    static const QLoggingCategory category("qt.remoteobjects", QtWarningMsg);
    return category;
}

//  from ../qtremoteobjects/src/remoteobjects/qconnection_tcpip_backend.cpp, line 121, as _ZN13TcpServerImplD1Ev
inline TcpServerImpl::~TcpServerImpl()
{
    close();
}

//  from ../qtremoteobjects/src/remoteobjects/qconnection_tcpip_backend.cpp, line 134, as _ZNK13TcpServerImpl21hasPendingConnectionsEv
inline bool TcpServerImpl::hasPendingConnections() const
{
    return m_server.hasPendingConnections();
}

//  from ../qtremoteobjects/src/remoteobjects/qconnection_tcpip_backend.cpp, line 139, as _ZNK13TcpServerImpl7addressEv
inline QUrl TcpServerImpl::address() const
{
    return m_originalUrl;
}

//  from ../qtremoteobjects/src/remoteobjects/qconnection_tcpip_backend.cpp, line 144, as _ZN13TcpServerImpl6listenERK4QUrl
inline bool TcpServerImpl::listen(const QUrl &address)
{
    QHostAddress host(address.host());
    if (host.isNull()) {
        if (address.host().isEmpty()) {
            host = QHostAddress::Any;
        } else {
            qCWarning(QT_REMOTEOBJECT) << address.host() << " is not an IP address, trying to resolve it";
            QHostInfo info = QHostInfo::fromName(address.host());
            if (info.addresses().isEmpty())
                host = QHostAddress::Any;
            else
                host = info.addresses().constFirst();
        }
    }

    bool ret = m_server.listen(host, quint16(address.port()));
    if (ret) {
        m_originalUrl.setScheme(QLatin1String("tcp"));
        m_originalUrl.setHost(m_server.serverAddress().toString());
        m_originalUrl.setPort(m_server.serverPort());
    }
    return ret;
}

//  from ../qtremoteobjects/src/remoteobjects/qconnection_tcpip_backend.cpp, line 169, as _ZNK13TcpServerImpl11serverErrorEv
inline QAbstractSocket::SocketError TcpServerImpl::serverError() const
{
    return m_server.serverError();
}

//  from ../qtremoteobjects/src/remoteobjects/qconnection_tcpip_backend.cpp, line 174, as _ZN13TcpServerImpl5closeEv
inline void TcpServerImpl::close()
{
    m_server.close();
}
//  -----------------------------------------------------------------------

//  TcpServerImpl::~TcpServerImpl()
extern "C" Q_DECL_EXPORT
void ritual_ZN13TcpServerImplD1Ev(TcpServerImpl *self) {
  delete self;
}

//  bool TcpServerImpl::hasPendingConnections() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13TcpServerImpl21hasPendingConnectionsEv(
    const TcpServerImpl *self) {
  return self->hasPendingConnections();
}

//  QUrl TcpServerImpl::address() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK13TcpServerImpl7addressEv(const TcpServerImpl *self) {
  return new QUrl(self->address());
}

//  bool TcpServerImpl::listen(const QUrl &address)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13TcpServerImpl6listenERK4QUrl(
    TcpServerImpl *self,
    const QUrl *address) {
  return self->listen(*address);
}

//  QAbstractSocket::SocketError TcpServerImpl::serverError() const
extern "C" Q_DECL_EXPORT
QAbstractSocket::SocketError ritual_ZNK13TcpServerImpl11serverErrorEv(
    const TcpServerImpl *self) {
  return self->serverError();
}

//  void TcpServerImpl::close()
extern "C" Q_DECL_EXPORT
void ritual_ZN13TcpServerImpl5closeEv(TcpServerImpl *self) {
  self->close();
}
