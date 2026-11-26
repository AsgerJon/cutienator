//  Written by dev_tooling.RitualGenerator from the records of QtRemoteObject
//  s/6.12.0/QtRemoteObjects/private/qconnection_local_backend_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtRemoteObjects/qtremoteobjectglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if defined(Q_OS_LINUX)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtRemoteObjects/QtRemoteObjects>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtRemoteObjects/6.12.0/QtRemoteObjects/private/qconnection_local_backend_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qurl.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
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

//  from ../qtremoteobjects/src/remoteobjects/qconnection_local_backend.cpp, line 113, as _ZN15LocalServerImplC2EP7QObject
inline LocalServerImpl::LocalServerImpl(QObject *parent)
    : QConnectionAbstractServer(parent)
{
    connect(&m_server, &QLocalServer::newConnection, this, &QConnectionAbstractServer::newConnection);
}

//  from ../qtremoteobjects/src/remoteobjects/qconnection_local_backend.cpp, line 119, as _ZN15LocalServerImplD2Ev
inline LocalServerImpl::~LocalServerImpl()
{
    m_server.close();
}

//  from ../qtremoteobjects/src/remoteobjects/qconnection_local_backend.cpp, line 193, as _ZNK23AbstractLocalServerImpl7addressEv
#if defined(Q_OS_LINUX)
inline QUrl AbstractLocalServerImpl::address() const
{
    QUrl result;
    result.setPath(m_server.serverName());
    result.setScheme(QRemoteObjectStringLiterals::localabstract());

    return result;
}
#endif  // defined(Q_OS_LINUX)
//  -----------------------------------------------------------------------

#if defined(Q_OS_LINUX)
//  QUrl AbstractLocalServerImpl::address() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK23AbstractLocalServerImpl7addressEv(
    const AbstractLocalServerImpl *self) {
  return new QUrl(self->address());
}
#endif  // defined(Q_OS_LINUX)

#endif  // defined(Q_OS_LINUX)
