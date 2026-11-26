//  Written by dev_tooling.RitualGenerator from the records of
//  QtRemoteObjects/qconnectionfactories.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtRemoteObjects/qconnectionfactories.h>
#include <QtCore/qurl.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtRemoteObjects/private/qconnection_tcpip_backend_p.h>
#include <QtNetwork/qhostinfo.h>
#include <QtRemoteObjects/private/qconnection_local_backend_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtremoteobjects/src/remoteobjects/qconnection_tcpip_backend.cpp, line 11, as _ZN11TcpClientIoC1EP7QObject
inline TcpClientIo::TcpClientIo(QObject *parent)
    : QtROClientIoDevice(parent)
    , m_socket(new QTcpSocket(this))
{
    connect(m_socket, &QTcpSocket::readyRead, this, &QtROClientIoDevice::readyRead);
    connect(m_socket, &QAbstractSocket::errorOccurred, this, &TcpClientIo::onError);
    connect(m_socket, &QTcpSocket::stateChanged, this, &TcpClientIo::onStateChanged);
}

//  from ../qtremoteobjects/src/remoteobjects/qconnection_local_backend.cpp, line 9, as _ZN13LocalClientIoC1EP7QObject
inline LocalClientIo::LocalClientIo(QObject *parent)
    : QtROClientIoDevice(parent)
    , m_socket(new QLocalSocket(this))
{
    connect(m_socket, &QLocalSocket::readyRead, this, &QtROClientIoDevice::readyRead);
    connect(m_socket, &QLocalSocket::errorOccurred, this, &LocalClientIo::onError);
    connect(m_socket, &QLocalSocket::stateChanged, this, &LocalClientIo::onStateChanged);
}

//  from ../qtremoteobjects/src/remoteobjects/qconnection_local_backend.cpp, line 181, as _ZN21AbstractLocalClientIoC1EP7QObject
#if defined(Q_OS_LINUX)
inline AbstractLocalClientIo::AbstractLocalClientIo(QObject *parent)
    : LocalClientIo(parent)
{
    m_socket->setSocketOptions(QLocalSocket::AbstractNamespaceOption);
}
#endif  // defined(Q_OS_LINUX)

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
//  -----------------------------------------------------------------------

//  QtROClientFactory *QtROClientFactory::instance()
extern "C" Q_DECL_EXPORT
QtROClientFactory *ritual_ZN17QtROClientFactory8instanceEv() {
  return QtROClientFactory::instance();
}

//  QtROClientIoDevice *QtROClientFactory::create(const QUrl &url, QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QtROClientIoDevice *ritual_ZN17QtROClientFactory6createERK4QUrlP7QObject(
    QtROClientFactory *self,
    const QUrl *url,
    QObject *parent) {
  return self->create(*url, parent);
}

//  bool QtROClientFactory::isValid(const QUrl &url)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QtROClientFactory7isValidERK4QUrl(
    QtROClientFactory *self,
    const QUrl *url) {
  return self->isValid(*url);
}

//  QtROClientFactory::~QtROClientFactory()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtROClientFactoryD1Ev(QtROClientFactory *self) {
  delete self;
}
