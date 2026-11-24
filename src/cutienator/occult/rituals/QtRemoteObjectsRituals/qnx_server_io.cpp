//  Written by dev_tooling.RitualGenerator from the records of QtRemoteObject
//  s/6.12.0/QtRemoteObjects/private/qconnection_qnx_backend_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtRemoteObjects/qtremoteobjectglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if defined(Q_OS_QNX)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtRemoteObjects/QtRemoteObjects>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtRemoteObjects/6.12.0/QtRemoteObjects/private/qconnection_qnx_backend_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtRemoteObjects/private/qconnection_qnx_backend_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtremoteobjects/src/remoteobjects/qconnection_qnx_backend.cpp, line 94, as _ZNK11QnxServerIo10connectionEv
inline QIODevice *QnxServerIo::connection() const
{
    return m_connection.data();
}

//  from ../qtremoteobjects/src/remoteobjects/qconnection_qnx_backend.cpp, line 99, as _ZN11QnxServerIo7doCloseEv
inline void QnxServerIo::doClose()
{
    m_connection->close();
}
//  -----------------------------------------------------------------------

//  QIODevice *QnxServerIo::connection() const
extern "C" Q_DECL_EXPORT
QIODevice *ritual_ZNK11QnxServerIo10connectionEv(const QnxServerIo *self) {
  return self->connection();
}

//  void QnxServerIo::doClose()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QnxServerIo7doCloseEv(QnxServerIo *self) {
  self->doClose();
}

#endif  // defined(Q_OS_QNX)
