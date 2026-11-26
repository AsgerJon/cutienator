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

//  from ../qtremoteobjects/src/remoteobjects/qconnection_tcpip_backend.cpp, line 115, as _ZN13TcpServerImplC1EP7QObject
inline TcpServerImpl::TcpServerImpl(QObject *parent)
    : QConnectionAbstractServer(parent)
{
    connect(&m_server, &QTcpServer::newConnection, this, &QConnectionAbstractServer::newConnection);
}

//  from ../qtremoteobjects/src/remoteobjects/qconnection_local_backend.cpp, line 113, as _ZN15LocalServerImplC1EP7QObject
inline LocalServerImpl::LocalServerImpl(QObject *parent)
    : QConnectionAbstractServer(parent)
{
    connect(&m_server, &QLocalServer::newConnection, this, &QConnectionAbstractServer::newConnection);
}

//  from ../qtremoteobjects/src/remoteobjects/qconnection_local_backend.cpp, line 187, as _ZN23AbstractLocalServerImplC1EP7QObject
#if defined(Q_OS_LINUX)
inline AbstractLocalServerImpl::AbstractLocalServerImpl(QObject *parent)
    : LocalServerImpl(parent)
{
    m_server.setSocketOptions(QLocalServer::AbstractNamespaceOption);
}
#endif  // defined(Q_OS_LINUX)

//  from ../qtremoteobjects/src/remoteobjects/qconnection_local_backend.cpp, line 119, as _ZN15LocalServerImplD2Ev
inline LocalServerImpl::~LocalServerImpl()
{
    m_server.close();
}
//  -----------------------------------------------------------------------

//  QtROServerFactory *QtROServerFactory::instance()
extern "C" Q_DECL_EXPORT
QtROServerFactory *ritual_ZN17QtROServerFactory8instanceEv() {
  return QtROServerFactory::instance();
}

//  QConnectionAbstractServer *QtROServerFactory::create(const QUrl &url,
//      QObject *parent)
extern "C" Q_DECL_EXPORT
QConnectionAbstractServer *ritual_ZN17QtROServerFactory6createERK4QUrlP7QObject(
    QtROServerFactory *self,
    const QUrl *url,
    QObject *parent) {
  return self->create(*url, parent);
}

//  bool QtROServerFactory::isValid(const QUrl &url)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QtROServerFactory7isValidERK4QUrl(
    QtROServerFactory *self,
    const QUrl *url) {
  return self->isValid(*url);
}

//  QtROServerFactory::~QtROServerFactory()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtROServerFactoryD1Ev(QtROServerFactory *self) {
  delete self;
}
