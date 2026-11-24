//  Written by dev_tooling.RitualGenerator from the records of QtHttpServer/6
//  .12.0/QtHttpServer/private/qhttpserverhttp1protocolhandler_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtHttpServer/QtHttpServer>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtHttpServer/6.12.0/QtHttpServer/private/qhttpserverhttp1protocolhandler_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtHttpServer/private/qhttpserverstream_p.h>
#include <QtHttpServer/private/qhttpserverresponder_p.h>
#include <QtNetwork/qtcpsocket.h>
#if QT_CONFIG(ssl)
#include <QtNetwork/qsslsocket.h>
#endif
#if QT_CONFIG(localserver)
#include <QtNetwork/qlocalsocket.h>
#endif
#include <QtHttpServer/private/qhttpserverliterals_p.h>
#include <QtCore/qbytearray.h>
#include <QtHttpServer/private/qhttpserverhttp1protocolhandler_p.h>
#include <QtCore/qloggingcategory.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qthread.h>
#include <QtCore/qpointer.h>
#include <QtHttpServer/qabstracthttpserver.h>
#include <QtHttpServer/qhttpserverrequest.h>
#include <QtHttpServer/qhttpserverresponder.h>
#include <QtHttpServer/qhttpserverresponse.h>
#if QT_CONFIG(localserver)
#include <QtNetwork/qlocalsocket.h>
#endif
#include <QtNetwork/qtcpsocket.h>
#include <QtHttpServer/private/qabstracthttpserver_p.h>
#include <QtHttpServer/private/qhttpserverliterals_p.h>
#include <QtHttpServer/private/qhttpserverrequest_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qthttpserver/src/httpserver/qhttpserverstream.cpp, line 65, as _ZN17QHttpServerStream19disconnectResponderEj
inline void QHttpServerStream::disconnectResponder(quint32 streamId)
{
    auto connection = responderConnections.take(streamId);
    if (connection)
        disconnect(connection);
}

//  from ../qthttpserver/src/httpserver/qhttpserverliterals.cpp, line 15, as _ZN19QHttpServerLiterals17contentTypeXEmptyEv
inline QByteArray QHttpServerLiterals::contentTypeXEmpty()
{
    static QByteArray ba("application/x-empty");
    return ba;
}

//  from ../qthttpserver/src/httpserver/qhttpserverhttp1protocolhandler.cpp, line 333, as _ZN31QHttpServerHttp1ProtocolHandler20startHandlingRequestEv
inline void QHttpServerHttp1ProtocolHandler::startHandlingRequest()
{
    handlingRequest = true;
}

//  from ../qthttpserver/src/httpserver/qhttpserverhttp1protocolhandler.cpp, line 338, as _ZN31QHttpServerHttp1ProtocolHandler18socketDisconnectedEv
inline void QHttpServerHttp1ProtocolHandler::socketDisconnected()
{
    if (!handlingRequest)
        deleteLater();
}

//  from ../qthttpserver/src/httpserver/qhttpserverhttp1protocolhandler.cpp, line 608, as _ZN31QHttpServerHttp1ProtocolHandler11writeHeaderERK10QByteArrayS2_
inline void QHttpServerHttp1ProtocolHandler::writeHeader(const QByteArray &key, const QByteArray &value)
{
    write(key + ": " + value + "\r\n");
}

//  from ../qthttpserver/src/httpserver/qhttpserverhttp1protocolhandler.cpp, line 613, as _ZN31QHttpServerHttp1ProtocolHandler5writeERK10QByteArray
inline void QHttpServerHttp1ProtocolHandler::write(const QByteArray &ba)
{
    Q_ASSERT(QThread::currentThread() == thread());
    socket->write(ba);
}

//  from ../qthttpserver/src/httpserver/qhttpserverhttp1protocolhandler.cpp, line 619, as _ZN31QHttpServerHttp1ProtocolHandler5writeEPKcx
inline void QHttpServerHttp1ProtocolHandler::write(const char *body, qint64 size)
{
    Q_ASSERT(QThread::currentThread() == thread());
    socket->write(body, size);
}

//  from ../qthttpserver/src/httpserver/qhttpserverhttp1protocolhandler.cpp, line 647, as _ZN31QHttpServerHttp1ProtocolHandler21checkKeepAliveTimeoutEv
inline void QHttpServerHttp1ProtocolHandler::checkKeepAliveTimeout()
{
    if (handlingRequest || state != TransferState::Ready)
        return;

    if (lastActiveTimer.durationElapsed() > server->configuration().keepAliveTimeout()) {
        if (tcpSocket)
            tcpSocket->abort();
#if QT_CONFIG(localserver)
        else if (localSocket)
            localSocket->abort();
#endif
    }
}

//  from ../qthttpserver/src/httpserver/qhttpserverhttp1protocolhandler.cpp, line 662, as _ZN31QHttpServerHttp1ProtocolHandler15closeConnectionEv
inline void QHttpServerHttp1ProtocolHandler::closeConnection()
{
    if (tcpSocket) {
        QMetaObject::invokeMethod(tcpSocket, &QTcpSocket::disconnectFromHost, Qt::QueuedConnection);
#if QT_CONFIG(localserver)
    } else if (localSocket) {
        QMetaObject::invokeMethod(localSocket, &QLocalSocket::disconnectFromServer,
                                  Qt::QueuedConnection);
#endif
    }
}
//  -----------------------------------------------------------------------

//  const QMetaObject *QHttpServerHttp1ProtocolHandler::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK31QHttpServerHttp1ProtocolHandler10metaObjectEv(
    const QHttpServerHttp1ProtocolHandler *self) {
  return self->metaObject();
}

//  void QHttpServerHttp1ProtocolHandler::startHandlingRequest()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QHttpServerHttp1ProtocolHandler20startHandlingRequestEv(
    QHttpServerHttp1ProtocolHandler *self) {
  self->startHandlingRequest();
}

//  void QHttpServerHttp1ProtocolHandler::socketDisconnected()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QHttpServerHttp1ProtocolHandler18socketDisconnectedEv(
    QHttpServerHttp1ProtocolHandler *self) {
  self->socketDisconnected();
}

//  void QHttpServerHttp1ProtocolHandler::writeHeader(const QByteArray &key,
//      const QByteArray &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QHttpServerHttp1ProtocolHandler11writeHeaderERK10QByteArrayS2_(
    QHttpServerHttp1ProtocolHandler *self,
    const QByteArray *key,
    const QByteArray *value) {
  self->writeHeader(*key, *value);
}

//  void QHttpServerHttp1ProtocolHandler::write(const QByteArray &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QHttpServerHttp1ProtocolHandler5writeERK10QByteArray(
    QHttpServerHttp1ProtocolHandler *self,
    const QByteArray *data) {
  self->write(*data);
}

//  void QHttpServerHttp1ProtocolHandler::write(const char *body, qint64
//      size)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QHttpServerHttp1ProtocolHandler5writeEPKcx(
    QHttpServerHttp1ProtocolHandler *self,
    const char *body,
    qint64 size) {
  self->write(body, size);
}

//  void QHttpServerHttp1ProtocolHandler::checkKeepAliveTimeout()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QHttpServerHttp1ProtocolHandler21checkKeepAliveTimeoutEv(
    QHttpServerHttp1ProtocolHandler *self) {
  self->checkKeepAliveTimeout();
}

//  void QHttpServerHttp1ProtocolHandler::closeConnection()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QHttpServerHttp1ProtocolHandler15closeConnectionEv(
    QHttpServerHttp1ProtocolHandler *self) {
  self->closeConnection();
}
