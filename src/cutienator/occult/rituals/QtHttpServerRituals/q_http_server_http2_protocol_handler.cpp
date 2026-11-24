//  Written by dev_tooling.RitualGenerator from the records of QtHttpServer/6
//  .12.0/QtHttpServer/private/qhttpserverhttp2protocolhandler_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtNetwork/qtnetworkglobal.h>
#include <QtHttpServer/qthttpserverglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(http) && QT_CONFIG(ssl)
#if QT_CONFIG(http)
#if QT_CONFIG(ssl)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtHttpServer/QtHttpServer>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtHttpServer/6.12.0/QtHttpServer/private/qhttpserverhttp2protocolhandler_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
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
#include <QtHttpServer/private/qhttpserverhttp2protocolhandler_p.h>
#include <QtCore/qloggingcategory.h>
#include <QtHttpServer/qabstracthttpserver.h>
#include <QtHttpServer/qhttpserverresponse.h>
#include <QtNetwork/private/qhttp2connection_p.h>
#include <QtNetwork/qtcpsocket.h>
#include <QtHttpServer/private/qhttpserverrequest_p.h>
#include <QtHttpServer/private/qhttpserverliterals_p.h>
#include <QtHttpServer/private/qhttpserverresponder_p.h>
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

//  from ../qthttpserver/src/httpserver/qhttpserverhttp2protocolhandler.cpp, line 75, as _ZN31QHttpServerHttp2ProtocolHandler18responderDestroyedEj
inline void QHttpServerHttp2ProtocolHandler::responderDestroyed(quint32 streamId)
{
    m_responderCounter--;
    disconnectResponder(streamId);
    m_responders.remove(streamId);
}

//  from ../qthttpserver/src/httpserver/qhttpserverhttp2protocolhandler.cpp, line 82, as _ZN31QHttpServerHttp2ProtocolHandler20startHandlingRequestEv
inline void QHttpServerHttp2ProtocolHandler::startHandlingRequest()
{
    m_responderCounter++;
}

//  from ../qthttpserver/src/httpserver/qhttpserverhttp2protocolhandler.cpp, line 87, as _ZN31QHttpServerHttp2ProtocolHandler18socketDisconnectedEv
inline void QHttpServerHttp2ProtocolHandler::socketDisconnected()
{
    if (m_responderCounter == 0)
        deleteLater();
}

//  from ../qthttpserver/src/httpserver/qhttpserverhttp2protocolhandler.cpp, line 424, as _ZN31QHttpServerHttp2ProtocolHandler21checkKeepAliveTimeoutEv
inline void QHttpServerHttp2ProtocolHandler::checkKeepAliveTimeout()
{
    if (m_streamQueue.size() > 0 || m_responderCounter > 0)
        return;

    if (lastActiveTimer.durationElapsed() > m_server->configuration().keepAliveTimeout()) {
        m_connection->close();
        m_tcpSocket->abort();
    }
}

//  from ../qthttpserver/src/httpserver/qhttpserverhttp2protocolhandler.cpp, line 435, as _ZN31QHttpServerHttp2ProtocolHandler12sendToStreamEj
inline void QHttpServerHttp2ProtocolHandler::sendToStream(quint32 streamId)
{
    QHttp2Stream *stream = getStream(streamId);
    if (!stream)
        return;

    if (stream->isUploadingDATA())
        return;

    auto &queue = m_streamQueue[streamId];
    if (!queue.data.isEmpty()) {
        QBuffer *buffer = new QBuffer(stream);
        buffer->setData(queue.data.dequeue());
        buffer->open(QIODevice::ReadOnly);
        connect(stream, &QHttp2Stream::uploadFinished, buffer, &QObject::deleteLater);
        bool endStream = queue.allEnqueued && queue.data.isEmpty() && queue.trailers.empty();
        stream->sendDATA(buffer, endStream);
    } else if (!queue.trailers.empty()) {
        stream->sendHEADERS(queue.trailers, true);
        queue.trailers.clear();
    }
}

//  from ../qthttpserver/src/httpserver/qhttpserverhttp2protocolhandler.cpp, line 228, as _ZNK31QHttpServerHttp2ProtocolHandler9getStreamEj
inline QHttp2Stream *QHttpServerHttp2ProtocolHandler::getStream(quint32 streamId) const
{
    QHttp2Stream *stream = m_connection->getStream(streamId);
    Q_ASSERT(stream);

    if (stream && stream->isActive())
        return stream;

    return nullptr;
}
//  -----------------------------------------------------------------------

//  const QMetaObject *QHttpServerHttp2ProtocolHandler::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK31QHttpServerHttp2ProtocolHandler10metaObjectEv(
    const QHttpServerHttp2ProtocolHandler *self) {
  return self->metaObject();
}

//  void QHttpServerHttp2ProtocolHandler::responderDestroyed(quint32
//      streamId)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QHttpServerHttp2ProtocolHandler18responderDestroyedEj(
    QHttpServerHttp2ProtocolHandler *self,
    quint32 streamId) {
  self->responderDestroyed(streamId);
}

//  void QHttpServerHttp2ProtocolHandler::startHandlingRequest()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QHttpServerHttp2ProtocolHandler20startHandlingRequestEv(
    QHttpServerHttp2ProtocolHandler *self) {
  self->startHandlingRequest();
}

//  void QHttpServerHttp2ProtocolHandler::socketDisconnected()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QHttpServerHttp2ProtocolHandler18socketDisconnectedEv(
    QHttpServerHttp2ProtocolHandler *self) {
  self->socketDisconnected();
}

//  void QHttpServerHttp2ProtocolHandler::checkKeepAliveTimeout()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QHttpServerHttp2ProtocolHandler21checkKeepAliveTimeoutEv(
    QHttpServerHttp2ProtocolHandler *self) {
  self->checkKeepAliveTimeout();
}

//  void QHttpServerHttp2ProtocolHandler::sendToStream(quint32 streamId)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QHttpServerHttp2ProtocolHandler12sendToStreamEj(
    QHttpServerHttp2ProtocolHandler *self,
    quint32 streamId) {
  self->sendToStream(streamId);
}

//  QHttp2Stream *QHttpServerHttp2ProtocolHandler::getStream(quint32
//      streamId) const
extern "C" Q_DECL_EXPORT
QHttp2Stream *ritual_ZNK31QHttpServerHttp2ProtocolHandler9getStreamEj(
    const QHttpServerHttp2ProtocolHandler *self,
    quint32 streamId) {
  return self->getStream(streamId);
}

#endif  // QT_CONFIG(ssl)
#endif  // QT_CONFIG(http)
#endif  // QT_CONFIG(http) && QT_CONFIG(ssl)
