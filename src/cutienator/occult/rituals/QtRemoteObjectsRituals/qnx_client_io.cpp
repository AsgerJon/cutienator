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
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtRemoteObjects/private/qconnection_qnx_backend_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtremoteobjects/src/remoteobjects/qconnection_qnx_backend.cpp, line 9, as _ZN11QnxClientIoC1EP7QObject
inline QnxClientIo::QnxClientIo(QObject *parent)
    : QtROClientIoDevice(parent)
    , m_socket(new QQnxNativeIo(this))
{
    connect(m_socket, &QQnxNativeIo::readyRead, this, &QtROClientIoDevice::readyRead);
    connect(m_socket,
            static_cast<void(QQnxNativeIo::*)(QAbstractSocket::SocketError)>(&QQnxNativeIo::error),
            this,
            &QnxClientIo::onError);
    connect(m_socket, &QQnxNativeIo::stateChanged, this, &QnxClientIo::onStateChanged);
}

//  from ../qtremoteobjects/src/remoteobjects/qconnection_qnx_backend.cpp, line 21, as _ZN11QnxClientIoD1Ev
inline QnxClientIo::~QnxClientIo()
{
    close();
}

//  from ../qtremoteobjects/src/remoteobjects/qconnection_qnx_backend.cpp, line 26, as _ZNK11QnxClientIo10connectionEv
inline QIODevice *QnxClientIo::connection() const
{
    return m_socket;
}

//  from ../qtremoteobjects/src/remoteobjects/qconnection_qnx_backend.cpp, line 46, as _ZN11QnxClientIo15connectToServerEv
inline void QnxClientIo::connectToServer()
{
    if (!isOpen())
        m_socket->connectToServer(url().path());
}

//  from ../qtremoteobjects/src/remoteobjects/qconnection_qnx_backend.cpp, line 52, as _ZNK11QnxClientIo6isOpenEv
inline bool QnxClientIo::isOpen() const
{
    return !isClosing() && (m_socket->state() == QAbstractSocket::ConnectedState
                            || m_socket->state() == QAbstractSocket::ConnectingState);
}

//  from ../qtremoteobjects/src/remoteobjects/qconnection_qnx_backend.cpp, line 58, as _ZN11QnxClientIo7onErrorEN15QAbstractSocket11SocketErrorE
inline void QnxClientIo::onError(QAbstractSocket::SocketError error)
{
    qCDebug(QT_REMOTEOBJECT) << "onError" << error << m_socket->serverName();

    switch (error) {
    case QAbstractSocket::RemoteHostClosedError:
        m_socket->close();
        qCWarning(QT_REMOTEOBJECT) << "RemoteHostClosedError";
        Q_FALLTHROUGH();
    case QAbstractSocket::HostNotFoundError:     //Host not there, wait and try again
    case QAbstractSocket::AddressInUseError:
    case QAbstractSocket::ConnectionRefusedError:
        //... TODO error reporting
        emit shouldReconnect(this);
        break;
    default:
        break;
    }
}

//  from ../qtremoteobjects/src/remoteobjects/qconnection_qnx_backend.cpp, line 78, as _ZN11QnxClientIo14onStateChangedEN15QAbstractSocket11SocketStateE
inline void QnxClientIo::onStateChanged(QAbstractSocket::SocketState state)
{
    if (state == QAbstractSocket::ClosingState && !isClosing()) {
        m_socket->abort();
        emit shouldReconnect(this);
    } else if (state == QAbstractSocket::ConnectedState)
        initializeDataStream();
}

//  from ../qtremoteobjects/src/remoteobjects/qconnection_qnx_backend.cpp, line 31, as _ZN11QnxClientIo7doCloseEv
inline void QnxClientIo::doClose()
{
    if (m_socket->isOpen()) {
        connect(m_socket, &QQnxNativeIo::disconnected, this, &QObject::deleteLater);
        m_socket->disconnectFromServer();
    } else {
        deleteLater();
    }
}

//  from ../qtremoteobjects/src/remoteobjects/qconnection_qnx_backend.cpp, line 41, as _ZN11QnxClientIo22doDisconnectFromServerEv
inline void QnxClientIo::doDisconnectFromServer()
{
    m_socket->disconnectFromServer();
}
//  -----------------------------------------------------------------------

//  const QMetaObject *QnxClientIo::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK11QnxClientIo10metaObjectEv(
    const QnxClientIo *self) {
  return self->metaObject();
}

//  QString QnxClientIo::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11QnxClientIo2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QnxClientIo::tr(s, c, n));
}

//  QnxClientIo::QnxClientIo(QObject *parent)
extern "C" Q_DECL_EXPORT
QnxClientIo *ritual_ZN11QnxClientIoC1EP7QObject(QObject *parent) {
  return new QnxClientIo(parent);
}

//  QnxClientIo::~QnxClientIo()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QnxClientIoD1Ev(QnxClientIo *self) {
  delete self;
}

//  QIODevice *QnxClientIo::connection() const
extern "C" Q_DECL_EXPORT
QIODevice *ritual_ZNK11QnxClientIo10connectionEv(const QnxClientIo *self) {
  return self->connection();
}

//  void QnxClientIo::connectToServer()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QnxClientIo15connectToServerEv(QnxClientIo *self) {
  self->connectToServer();
}

//  bool QnxClientIo::isOpen() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QnxClientIo6isOpenEv(const QnxClientIo *self) {
  return self->isOpen();
}

//  void QnxClientIo::onError(QAbstractSocket::SocketError error)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QnxClientIo7onErrorEN15QAbstractSocket11SocketErrorE(
    QnxClientIo *self,
    QAbstractSocket::SocketError error) {
  self->onError(error);
}

//  void QnxClientIo::onStateChanged(QAbstractSocket::SocketState state)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QnxClientIo14onStateChangedEN15QAbstractSocket11SocketStateE(
    QnxClientIo *self,
    QAbstractSocket::SocketState state) {
  self->onStateChanged(state);
}

//  void QnxClientIo::doClose()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QnxClientIo7doCloseEv(QnxClientIo *self) {
  self->doClose();
}

//  void QnxClientIo::doDisconnectFromServer()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QnxClientIo22doDisconnectFromServerEv(QnxClientIo *self) {
  self->doDisconnectFromServer();
}

#endif  // defined(Q_OS_QNX)
