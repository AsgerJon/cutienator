//  Written by dev_tooling.RitualGenerator from the records of QtRemoteObject
//  s/6.12.0/QtRemoteObjects/private/qconnection_local_backend_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtRemoteObjects/QtRemoteObjects>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtRemoteObjects/6.12.0/QtRemoteObjects/private/qconnection_local_backend_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtRemoteObjects/private/qconnection_local_backend_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtremoteobjects/src/remoteobjects/qconnection_local_backend.cpp, line 103, as _ZNK13LocalServerIo10connectionEv
inline QIODevice *LocalServerIo::connection() const
{
    return m_connection;
}

//  from ../qtremoteobjects/src/remoteobjects/qconnection_local_backend.cpp, line 108, as _ZN13LocalServerIo7doCloseEv
inline void LocalServerIo::doClose()
{
    m_connection->disconnectFromServer();
}
//  -----------------------------------------------------------------------

//  QIODevice *LocalServerIo::connection() const
extern "C" Q_DECL_EXPORT
QIODevice *ritual_ZNK13LocalServerIo10connectionEv(
    const LocalServerIo *self) {
  return self->connection();
}

//  void LocalServerIo::doClose()
extern "C" Q_DECL_EXPORT
void ritual_ZN13LocalServerIo7doCloseEv(LocalServerIo *self) {
  self->doClose();
}
