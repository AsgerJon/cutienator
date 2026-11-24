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
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qconnection_qnx_backend_p.h"
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtremoteobjects/src/remoteobjects/qconnection_qnx_backend.cpp, line 104, as _ZN13QnxServerImplC1EP7QObject
inline QnxServerImpl::QnxServerImpl(QObject *parent)
    : QConnectionAbstractServer(parent)
{
    connect(&m_server,
            &QQnxNativeServer::newConnection,
            this,
            &QConnectionAbstractServer::newConnection);
}

//  from ../qtremoteobjects/src/remoteobjects/qconnection_qnx_backend.cpp, line 113, as _ZN13QnxServerImplD1Ev
inline QnxServerImpl::~QnxServerImpl()
{
    m_server.close();
}

//  from ../qtremoteobjects/src/remoteobjects/qconnection_qnx_backend.cpp, line 126, as _ZNK13QnxServerImpl21hasPendingConnectionsEv
inline bool QnxServerImpl::hasPendingConnections() const
{
    return m_server.hasPendingConnections();
}

//  from ../qtremoteobjects/src/remoteobjects/qconnection_qnx_backend.cpp, line 118, as _ZN13QnxServerImpl22configureNewConnectionEv
inline QtROServerIoDevice *QnxServerImpl::configureNewConnection()
{
    if (!m_server.isListening())
        return nullptr;

    return new QnxServerIo(m_server.nextPendingConnection(), this);
}

//  from ../qtremoteobjects/src/remoteobjects/qconnection_qnx_backend.cpp, line 131, as _ZNK13QnxServerImpl7addressEv
inline QUrl QnxServerImpl::address() const
{
    QUrl result;
    result.setPath(m_server.serverName());
    result.setScheme(QStringLiteral("qnx"));

    return result;
}

//  from ../qtremoteobjects/src/remoteobjects/qconnection_qnx_backend.cpp, line 140, as _ZN13QnxServerImpl6listenERK4QUrl
inline bool QnxServerImpl::listen(const QUrl &address)
{
    return m_server.listen(address.path());
}

//  from ../qtremoteobjects/src/remoteobjects/qconnection_qnx_backend.cpp, line 145, as _ZNK13QnxServerImpl11serverErrorEv
inline QAbstractSocket::SocketError QnxServerImpl::serverError() const
{
    //TODO implement on QQnxNativeServer and here
    //return m_server.serverError();
    return QAbstractSocket::AddressInUseError;
}

//  from ../qtremoteobjects/src/remoteobjects/qconnection_qnx_backend.cpp, line 152, as _ZN13QnxServerImpl5closeEv
inline void QnxServerImpl::close()
{
    close();
}
//  -----------------------------------------------------------------------

//  const QMetaObject *QnxServerImpl::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13QnxServerImpl10metaObjectEv(
    const QnxServerImpl *self) {
  return self->metaObject();
}

//  QString QnxServerImpl::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13QnxServerImpl2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QnxServerImpl::tr(s, c, n));
}

//  QnxServerImpl::QnxServerImpl(QObject *parent)
extern "C" Q_DECL_EXPORT
QnxServerImpl *ritual_ZN13QnxServerImplC1EP7QObject(QObject *parent) {
  return new QnxServerImpl(parent);
}

//  QnxServerImpl::~QnxServerImpl()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QnxServerImplD1Ev(QnxServerImpl *self) {
  delete self;
}

//  bool QnxServerImpl::hasPendingConnections() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QnxServerImpl21hasPendingConnectionsEv(
    const QnxServerImpl *self) {
  return self->hasPendingConnections();
}

//  QtROServerIoDevice *QnxServerImpl::configureNewConnection()
extern "C" Q_DECL_EXPORT
QtROServerIoDevice *ritual_ZN13QnxServerImpl22configureNewConnectionEv(
    QnxServerImpl *self) {
  return self->configureNewConnection();
}

//  QUrl QnxServerImpl::address() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK13QnxServerImpl7addressEv(const QnxServerImpl *self) {
  return new QUrl(self->address());
}

//  bool QnxServerImpl::listen(const QUrl &address)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QnxServerImpl6listenERK4QUrl(
    QnxServerImpl *self,
    const QUrl *address) {
  return self->listen(*address);
}

//  QAbstractSocket::SocketError QnxServerImpl::serverError() const
extern "C" Q_DECL_EXPORT
QAbstractSocket::SocketError ritual_ZNK13QnxServerImpl11serverErrorEv(
    const QnxServerImpl *self) {
  return self->serverError();
}

//  void QnxServerImpl::close()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QnxServerImpl5closeEv(QnxServerImpl *self) {
  self->close();
}

#endif  // defined(Q_OS_QNX)
