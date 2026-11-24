//  Written by dev_tooling.RitualGenerator from the records of QtRemoteObject
//  s/6.12.0/QtRemoteObjects/private/qconnection_tcpip_backend_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtRemoteObjects/QtRemoteObjects>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtRemoteObjects/6.12.0/QtRemoteObjects/private/qconnection_tcpip_backend_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtRemoteObjects/private/qconnection_tcpip_backend_p.h>
#include <QtNetwork/qhostinfo.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtremoteobjects/src/remoteobjects/qconnection_tcpip_backend.cpp, line 103, as _ZNK11TcpServerIo10connectionEv
inline QIODevice *TcpServerIo::connection() const
{
    return m_connection;
}

//  from ../qtremoteobjects/src/remoteobjects/qconnection_tcpip_backend.cpp, line 108, as _ZN11TcpServerIo7doCloseEv
inline void TcpServerIo::doClose()
{
    m_connection->disconnectFromHost();
}
//  -----------------------------------------------------------------------

//  QIODevice *TcpServerIo::connection() const
extern "C" Q_DECL_EXPORT
QIODevice *ritual_ZNK11TcpServerIo10connectionEv(const TcpServerIo *self) {
  return self->connection();
}

//  void TcpServerIo::doClose()
extern "C" Q_DECL_EXPORT
void ritual_ZN11TcpServerIo7doCloseEv(TcpServerIo *self) {
  self->doClose();
}
