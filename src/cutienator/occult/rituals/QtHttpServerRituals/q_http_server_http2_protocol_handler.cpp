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
#include <QtCore/qbytearray.h>
#include <QtNetwork/qhttpheaders.h>
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
#include <QtHttpServer/private/qhttpserverhttp2protocolhandler_p.h>
#include <QtCore/qloggingcategory.h>
#include <QtHttpServer/qabstracthttpserver.h>
#include <QtHttpServer/qhttpserverresponse.h>
#include <QtNetwork/private/qhttp2connection_p.h>
#include <QtNetwork/qtcpsocket.h>
#include <QtHttpServer/private/qhttpserverrequest_p.h>
#include <QtHttpServer/private/qhttpserverliterals_p.h>
#include <QtHttpServer/private/qhttpserverresponder_p.h>
#include <QtHttpServer/private/qhttpserverliterals_p.h>
#include <QtCore/qbytearray.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qthttpserver/src/httpserver/qhttpserverhttp2protocolhandler.cpp, line 23, as local:qhttpserverhttp2protocolhandler.cpp:toHeaderPairs
namespace {
inline void toHeaderPairs(HPack::HttpHeader &fields, const QHttpHeaders &headers)
{
    for (qsizetype i = 0; i < headers.size(); ++i) {
        const auto name = headers.nameAt(i);
        fields.push_back(HPack::HeaderField(QByteArray(name.data(), name.size()).toLower(),
                                            headers.valueAt(i).toByteArray()));
    }
}
}  // namespace

//  from ../qthttpserver/src/httpserver/qhttpserverstream.cpp, line 19, as local:qhttpserverstream.cpp:initParserFromSocket
static QHttpServerParser initParserFromSocket(QIODevice *socket, QHttpServerRequestFilter *filter)
{
    QTcpSocket *tcpSocket = qobject_cast<QTcpSocket *>(socket);
    if (tcpSocket) {
        return QHttpServerParser(tcpSocket->peerAddress(), tcpSocket->peerPort(),
                                 tcpSocket->localAddress(), tcpSocket->localPort(), filter);
    }
    return QHttpServerParser(QHostAddress::LocalHost, 0, QHostAddress::LocalHost, 0, filter);
}

//  from ../qthttpserver/src/httpserver/qhttpserverstream.cpp, line 30, as local:qhttpserverstream.cpp:initSslConfigurationFromSocket
#if QT_CONFIG(ssl)
static QSslConfiguration initSslConfigurationFromSocket(QIODevice *socket)
{
    if (auto *ssl = qobject_cast<const QSslSocket *>(socket))
        return ssl->sslConfiguration();

    return QSslConfiguration();
}
#endif  // QT_CONFIG(ssl)

//  from ../qthttpserver/src/httpserver/qhttpserverstream.cpp, line 39, as _ZN17QHttpServerStreamC2EP9QIODeviceP24QHttpServerRequestFilterP7QObject
inline QHttpServerStream::QHttpServerStream(QIODevice *socket, QHttpServerRequestFilter *filter,
                                     QObject *parent)
    : QObject(parent)
    , parser(initParserFromSocket(socket, filter))
#if QT_CONFIG(ssl)
    , sslConfiguration(initSslConfigurationFromSocket(socket))
#endif
    , clientSocket(socket)
{
}

//  from ../qthttpserver/src/httpserver/qhttpserverhttp2protocolhandler.cpp, line 239, as _ZN31QHttpServerHttp2ProtocolHandler15onStreamCreatedEP12QHttp2Stream
inline void QHttpServerHttp2ProtocolHandler::onStreamCreated(QHttp2Stream *stream)
{
    const quint32 id = stream->streamID();
    m_streamQueue.insert(id, QHttpServerHttp2Queue());

    auto onStateChanged = [this, id](QHttp2Stream::State newState) {
        switch (newState) {
        case QHttp2Stream::State::HalfClosedRemote:
            onStreamHalfClosed(id);
            break;
        case QHttp2Stream::State::Closed:
            onStreamClosed(id);
            break;
        default:
            break;
        }
    };

    m_streamConnections[id] = {
                   connect(stream,
                           &QHttp2Stream::stateChanged,
                           this,
                           onStateChanged,
                           Qt::QueuedConnection),

                   connect(stream, &QHttp2Stream::uploadFinished, this,
                           [this, id]() { sendToStream(id); }),

                   connect(stream, &QHttp2Stream::headersReceived, this,
                           [this, id](const HPack::HttpHeader &headers, bool endStream) {
                               Q_UNUSED(endStream);
                               onHeadersReceived(id, headers);
                           }),

                   connect(stream, &QHttp2Stream::dataReceived, this,
                           [this, id](const QByteArray &data, bool endStream) {
                               Q_UNUSED(endStream);
                               onDataReceived(id, data.size());
                           }),
    };

    lastActiveTimer.restart();
}

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

//  from ../qthttpserver/src/httpserver/qhttpserverhttp2protocolhandler.cpp, line 192, as _ZN31QHttpServerHttp2ProtocolHandler12enqueueChunkERK10QByteArraybRK12QHttpHeadersj
inline void QHttpServerHttp2ProtocolHandler::enqueueChunk(const QByteArray &body, bool allEnqueued,
                                                   const QHttpHeaders &trailers, quint32 streamId)
{
    QHttp2Stream *stream = getStream(streamId);
    if (!stream)
        return;

    auto &queue = m_streamQueue[streamId];

    if (!trailers.isEmpty()) {
        Q_ASSERT(queue.trailers.empty());
        toHeaderPairs(queue.trailers, trailers);
    }

    queue.data.enqueue(body);
    if (allEnqueued)
        queue.allEnqueued = true;

    if (!stream->isUploadingDATA())
        sendToStream(streamId);
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

//  from ../qthttpserver/src/httpserver/qhttpserverhttp2protocolhandler.cpp, line 93, as _ZN31QHttpServerHttp2ProtocolHandler5writeERK10QByteArrayRK12QHttpHeadersN20QHttpServerResponder10StatusCodeEj
inline void QHttpServerHttp2ProtocolHandler::write(const QByteArray &body, const QHttpHeaders &headers,
                                            QHttpServerResponder::StatusCode status,
                                            quint32 streamId)
{
    QHttp2Stream *stream = getStream(streamId);
    if (!stream)
        return;

    writeHeadersAndStatus(headers, status, false, streamId);

    QBuffer *buffer = new QBuffer(stream);
    buffer->setData(body);
    buffer->open(QIODevice::ReadOnly);

    connect(stream, &QHttp2Stream::uploadFinished, buffer, &QObject::deleteLater);
    stream->sendDATA(buffer, true);
    disconnectResponder(streamId);
    m_responders.remove(streamId);
}

//  from ../qthttpserver/src/httpserver/qhttpserverhttp2protocolhandler.cpp, line 113, as _ZN31QHttpServerHttp2ProtocolHandler5writeEN20QHttpServerResponder10StatusCodeEj
inline void QHttpServerHttp2ProtocolHandler::write(QHttpServerResponder::StatusCode status,
                                            quint32 streamId)
{
    QHttpHeaders headers;
    headers.append(QHttpHeaders::WellKnownHeader::ContentType,
                   QHttpServerLiterals::contentTypeXEmpty());
    headers.append(QHttpHeaders::WellKnownHeader::ContentLength, "0");

    // RFC 9113, 8.1
    // A HEADERS frame with the END_STREAM flag set that carries
    // an informational status code is malformed
    bool isInfoStatus = QHttpServerResponder::StatusCode::Continue <= status
                        && status < QHttpServerResponder::StatusCode::Ok;
    writeHeadersAndStatus(headers, status, !isInfoStatus, streamId);
    disconnectResponder(streamId);
    m_responders.remove(streamId);
}

//  from ../qthttpserver/src/httpserver/qhttpserverhttp2protocolhandler.cpp, line 171, as _ZN31QHttpServerHttp2ProtocolHandler17writeBeginChunkedERK12QHttpHeadersN20QHttpServerResponder10StatusCodeEj
inline void QHttpServerHttp2ProtocolHandler::writeBeginChunked(const QHttpHeaders &headers,
                                                        QHttpServerResponder::StatusCode status,
                                                        quint32 streamId)
{
    writeHeadersAndStatus(headers, status, false, streamId);
}

//  from ../qthttpserver/src/httpserver/qhttpserverhttp2protocolhandler.cpp, line 178, as _ZN31QHttpServerHttp2ProtocolHandler10writeChunkERK10QByteArrayj
inline void QHttpServerHttp2ProtocolHandler::writeChunk(const QByteArray &body, quint32 streamId)
{
    enqueueChunk(body, false, {}, streamId);
}

//  from ../qthttpserver/src/httpserver/qhttpserverhttp2protocolhandler.cpp, line 183, as _ZN31QHttpServerHttp2ProtocolHandler15writeEndChunkedERK10QByteArrayRK12QHttpHeadersj
inline void QHttpServerHttp2ProtocolHandler::writeEndChunked(const QByteArray &body,
                                                      const QHttpHeaders &trailers,
                                                      quint32 streamId)
{
    enqueueChunk(body, true, trailers, streamId);
    disconnectResponder(streamId);
    m_responders.remove(streamId);
}

//  from ../qthttpserver/src/httpserver/qhttpserverhttp2protocolhandler.cpp, line 214, as _ZN31QHttpServerHttp2ProtocolHandler21writeHeadersAndStatusERK12QHttpHeadersN20QHttpServerResponder10StatusCodeEbj
inline void QHttpServerHttp2ProtocolHandler::writeHeadersAndStatus(const QHttpHeaders &headers,
                               QHttpServerResponder::StatusCode status,
                               bool endStream, quint32 streamId)
{
    QHttp2Stream *stream = getStream(streamId);
    if (!stream)
        return;

    HPack::HttpHeader h;
    h.push_back(HPack::HeaderField(":status", QByteArray::number(quint32(status))));
    toHeaderPairs(h, headers);
    stream->sendHEADERS(h, endStream);
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

//  void *QHttpServerHttp2ProtocolHandler::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN31QHttpServerHttp2ProtocolHandler11qt_metacastEPKc(
    QHttpServerHttp2ProtocolHandler *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QHttpServerHttp2ProtocolHandler::qt_metacall(QMetaObject::Call a0,
//      int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN31QHttpServerHttp2ProtocolHandler11qt_metacallEN11QMetaObject4CallEiPPv(
    QHttpServerHttp2ProtocolHandler *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
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

//  void QHttpServerHttp2ProtocolHandler::write(const QByteArray &body, const
//      QHttpHeaders &headers, QHttpServerResponder::StatusCode status,
//      quint32 streamId)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QHttpServerHttp2ProtocolHandler5writeERK10QByteArrayRK12QHttpHeadersN20QHttpServerResponder10StatusCodeEj(
    QHttpServerHttp2ProtocolHandler *self,
    const QByteArray *body,
    const QHttpHeaders *headers,
    QHttpServerResponder::StatusCode status,
    quint32 streamId) {
  self->write(*body, *headers, status, streamId);
}

//  void
//      QHttpServerHttp2ProtocolHandler::write(QHttpServerResponder::StatusCo
//      de status, quint32 streamId)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QHttpServerHttp2ProtocolHandler5writeEN20QHttpServerResponder10StatusCodeEj(
    QHttpServerHttp2ProtocolHandler *self,
    QHttpServerResponder::StatusCode status,
    quint32 streamId) {
  self->write(status, streamId);
}

//  void QHttpServerHttp2ProtocolHandler::writeBeginChunked(const
//      QHttpHeaders &headers, QHttpServerResponder::StatusCode status,
//      quint32 streamId)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QHttpServerHttp2ProtocolHandler17writeBeginChunkedERK12QHttpHeadersN20QHttpServerResponder10StatusCodeEj(
    QHttpServerHttp2ProtocolHandler *self,
    const QHttpHeaders *headers,
    QHttpServerResponder::StatusCode status,
    quint32 streamId) {
  self->writeBeginChunked(*headers, status, streamId);
}

//  void QHttpServerHttp2ProtocolHandler::writeChunk(const QByteArray &body,
//      quint32 streamId)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QHttpServerHttp2ProtocolHandler10writeChunkERK10QByteArrayj(
    QHttpServerHttp2ProtocolHandler *self,
    const QByteArray *body,
    quint32 streamId) {
  self->writeChunk(*body, streamId);
}

//  void QHttpServerHttp2ProtocolHandler::writeEndChunked(const QByteArray
//      &data, const QHttpHeaders &trailers, quint32 streamId)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QHttpServerHttp2ProtocolHandler15writeEndChunkedERK10QByteArrayRK12QHttpHeadersj(
    QHttpServerHttp2ProtocolHandler *self,
    const QByteArray *data,
    const QHttpHeaders *trailers,
    quint32 streamId) {
  self->writeEndChunked(*data, *trailers, streamId);
}

//  void QHttpServerHttp2ProtocolHandler::writeHeadersAndStatus(const
//      QHttpHeaders &headers, QHttpServerResponder::StatusCode status, bool
//      endStream, quint32 streamId)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QHttpServerHttp2ProtocolHandler21writeHeadersAndStatusERK12QHttpHeadersN20QHttpServerResponder10StatusCodeEbj(
    QHttpServerHttp2ProtocolHandler *self,
    const QHttpHeaders *headers,
    QHttpServerResponder::StatusCode status,
    bool endStream,
    quint32 streamId) {
  self->writeHeadersAndStatus(*headers, status, endStream, streamId);
}

//  void QHttpServerHttp2ProtocolHandler::checkKeepAliveTimeout()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QHttpServerHttp2ProtocolHandler21checkKeepAliveTimeoutEv(
    QHttpServerHttp2ProtocolHandler *self) {
  self->checkKeepAliveTimeout();
}

//  void QHttpServerHttp2ProtocolHandler::onStreamCreated(QHttp2Stream
//      *stream)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QHttpServerHttp2ProtocolHandler15onStreamCreatedEP12QHttp2Stream(
    QHttpServerHttp2ProtocolHandler *self,
    QHttp2Stream *stream) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QHttpServerHttp2ProtocolHandler")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "onStreamCreated(QHttp2Stream *)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "onStreamCreated(QHttp2Stream *)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&stream)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QHttpServerHttp2ProtocolHandler::onStreamClosed(quint32 streamId)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QHttpServerHttp2ProtocolHandler14onStreamClosedEj(
    QHttpServerHttp2ProtocolHandler *self,
    quint32 streamId) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QHttpServerHttp2ProtocolHandler")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "onStreamClosed(quint32)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "onStreamClosed(quint32)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&streamId)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QHttpServerHttp2ProtocolHandler::onStreamHalfClosed(quint32
//      streamId)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QHttpServerHttp2ProtocolHandler18onStreamHalfClosedEj(
    QHttpServerHttp2ProtocolHandler *self,
    quint32 streamId) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QHttpServerHttp2ProtocolHandler")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "onStreamHalfClosed(quint32)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "onStreamHalfClosed(quint32)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&streamId)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QHttpServerHttp2ProtocolHandler::sendToStream(quint32 streamId)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QHttpServerHttp2ProtocolHandler12sendToStreamEj(
    QHttpServerHttp2ProtocolHandler *self,
    quint32 streamId) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QHttpServerHttp2ProtocolHandler")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "sendToStream(quint32)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "sendToStream(quint32)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&streamId)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QHttpServerHttp2ProtocolHandler::onHeadersReceived(quint32 id, const
//      HPack::HttpHeader &headers)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QHttpServerHttp2ProtocolHandler17onHeadersReceivedEjRKSt6vectorIN5HPack11HeaderFieldESaIS2_EE(
    QHttpServerHttp2ProtocolHandler *self,
    quint32 id,
    const HPack::HttpHeader *headers) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QHttpServerHttp2ProtocolHandler")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "onHeadersReceived(quint32,const HPack::HttpHeader &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "onHeadersReceived(quint32,const HPack::HttpHeader &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&id)),
      const_cast<void *>(static_cast<const void *>(headers)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QHttpServerHttp2ProtocolHandler::onDataReceived(quint32 id,
//      qsizetype size)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QHttpServerHttp2ProtocolHandler14onDataReceivedEjx(
    QHttpServerHttp2ProtocolHandler *self,
    quint32 id,
    qsizetype size) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QHttpServerHttp2ProtocolHandler")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "onDataReceived(quint32,qsizetype)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "onDataReceived(quint32,qsizetype)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&id)),
      const_cast<void *>(static_cast<const void *>(&size)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
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
