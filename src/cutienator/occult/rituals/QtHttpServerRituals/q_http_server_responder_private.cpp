//  Written by dev_tooling.RitualGenerator from the records of
//  QtHttpServer/6.12.0/QtHttpServer/private/qhttpserverresponder_p.h, Qt
//  6.12.0.
//  Edited by hand on 2026-11-26: added are 8 rituals that lean on what moc
//  writes for a class of the part Qt keeps to itself, whose ritual file
//  carries moc's output, drafted by a copy of the generator that lets those
//  names through. A copy of a meta-object is a second one: 'qobject_cast'
//  between it and Qt's own does not match. Kept as it is when the generator
//  runs again.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtHttpServer/QtHttpServer>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtHttpServer/6.12.0/QtHttpServer/private/qhttpserverresponder_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtNetwork/qhttpheaders.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtHttpServer/qhttpserverresponder.h>
#include <QtHttpServer/qhttpserverrequest.h>
#include <QtHttpServer/qhttpserverresponse.h>
#include <QtHttpServer/private/qhttpserverresponder_p.h>
#include <QtHttpServer/private/qhttpserverliterals_p.h>
#include <QtHttpServer/private/qhttpserverrequest_p.h>
#include <QtHttpServer/private/qhttpserverresponse_p.h>
#include <QtHttpServer/private/qhttpserverstream_p.h>
#include <QtCore/qjsondocument.h>
#include <QtCore/qloggingcategory.h>
#include <memory>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qthttpserver/src/httpserver/qhttpserverresponder.cpp, line 106, as _ZN27QHttpServerResponderPrivateC1EP17QHttpServerStream
inline QHttpServerResponderPrivate::QHttpServerResponderPrivate(QHttpServerStream *stream) : stream(stream)
{
    Q_ASSERT(stream);
    QMetaObject::invokeMethod(stream, &QHttpServerStream::startHandlingRequest);
}

//  from ../qthttpserver/src/httpserver/qhttpserverresponder.cpp, line 115, as _ZN27QHttpServerResponderPrivateD1Ev
inline QHttpServerResponderPrivate::~QHttpServerResponderPrivate()
{
    Q_ASSERT(stream);
    QMetaObject::invokeMethod(stream, &QHttpServerStream::responderDestroyed, m_streamId);
}

//  from ../qthttpserver/src/httpserver/qhttpserverresponder.cpp, line 145, as _ZN27QHttpServerResponderPrivate5writeERK10QByteArrayRK12QHttpHeadersN20QHttpServerResponder10StatusCodeE
inline void QHttpServerResponderPrivate::write(const QByteArray &body, const QHttpHeaders &headers,
                                        QHttpServerResponder::StatusCode status)
{
    if (canceled)
        return;
    Q_ASSERT(stream);
    QMetaObject::invokeMethod(
            stream,
            qOverload<const QByteArray &, const QHttpHeaders &, QHttpServerResponder::StatusCode,
                      quint32>(&QHttpServerStream::write),
            body, headers, status, m_streamId);
}

//  from ../qthttpserver/src/httpserver/qhttpserverresponder.cpp, line 132, as _ZN27QHttpServerResponderPrivate5writeEN20QHttpServerResponder10StatusCodeE
inline void QHttpServerResponderPrivate::write(QHttpServerResponder::StatusCode status)
{
    if (canceled)
        return;
    Q_ASSERT(stream);
    QMetaObject::invokeMethod(
            stream, qOverload<QHttpServerResponder::StatusCode, quint32>(&QHttpServerStream::write),
            status, m_streamId);
}

//  from ../qthttpserver/src/httpserver/qhttpserverresponder.cpp, line 161, as _ZN27QHttpServerResponderPrivate5writeEP9QIODeviceRK12QHttpHeadersN20QHttpServerResponder10StatusCodeE
inline void QHttpServerResponderPrivate::write(QIODevice *data, const QHttpHeaders &headers,
                                        QHttpServerResponder::StatusCode status)
{
    if (canceled)
        return;
    Q_ASSERT(stream);
    Q_ASSERT(data);
    data->setParent(nullptr);
    data->moveToThread(stream->thread());
    QMetaObject::invokeMethod(
            stream,
            qOverload<QIODevice *, const QHttpHeaders &, QHttpServerResponder::StatusCode, quint32>(
                    &QHttpServerStream::write),
            data, headers, status, m_streamId);
}

//  from ../qthttpserver/src/httpserver/qhttpserverresponder.cpp, line 180, as _ZN27QHttpServerResponderPrivate17writeBeginChunkedERK12QHttpHeadersN20QHttpServerResponder10StatusCodeE
inline void QHttpServerResponderPrivate::writeBeginChunked(const QHttpHeaders &headers,
                                                    QHttpServerResponder::StatusCode status)
{
    if (canceled)
        return;
    Q_ASSERT(stream);
    QMetaObject::invokeMethod(stream, &QHttpServerStream::writeBeginChunked, headers, status,
                              m_streamId);
}

//  from ../qthttpserver/src/httpserver/qhttpserverresponder.cpp, line 193, as _ZN27QHttpServerResponderPrivate10writeChunkERK10QByteArray
inline void QHttpServerResponderPrivate::writeChunk(const QByteArray &data)
{
    if (canceled)
        return;
    Q_ASSERT(stream);
    QMetaObject::invokeMethod(stream, &QHttpServerStream::writeChunk, data, m_streamId);
}

//  from ../qthttpserver/src/httpserver/qhttpserverresponder.cpp, line 204, as _ZN27QHttpServerResponderPrivate15writeEndChunkedERK10QByteArrayRK12QHttpHeaders
inline void QHttpServerResponderPrivate::writeEndChunked(const QByteArray &data,
                                                  const QHttpHeaders &trailers)
{
    if (canceled)
        return;
    Q_ASSERT(stream);
    QMetaObject::invokeMethod(stream, &QHttpServerStream::writeEndChunked, data, trailers,
                              m_streamId);
}

//  from ../qthttpserver/src/httpserver/qhttpserverresponder.cpp, line 124, as _ZN27QHttpServerResponderPrivate6cancelEv
inline void QHttpServerResponderPrivate::cancel()
{
    canceled = true;
}
//  -----------------------------------------------------------------------

//  QHttpServerResponderPrivate::QHttpServerResponderPrivate(QHttpServerStrea
//      m *stream)
extern "C" Q_DECL_EXPORT
QHttpServerResponderPrivate *ritual_ZN27QHttpServerResponderPrivateC1EP17QHttpServerStream(
    QHttpServerStream *stream) {
  return new QHttpServerResponderPrivate(stream);
}

//  QHttpServerResponderPrivate::~QHttpServerResponderPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QHttpServerResponderPrivateD1Ev(
    QHttpServerResponderPrivate *self) {
  delete self;
}

//  void QHttpServerResponderPrivate::write(const QByteArray &body, const
//      QHttpHeaders &headers, QHttpServerResponder::StatusCode status)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QHttpServerResponderPrivate5writeERK10QByteArrayRK12QHttpHeadersN20QHttpServerResponder10StatusCodeE(
    QHttpServerResponderPrivate *self,
    const QByteArray *body,
    const QHttpHeaders *headers,
    QHttpServerResponder::StatusCode status) {
  self->write(*body, *headers, status);
}

//  void QHttpServerResponderPrivate::write(QHttpServerResponder::StatusCode
//      status)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QHttpServerResponderPrivate5writeEN20QHttpServerResponder10StatusCodeE(
    QHttpServerResponderPrivate *self,
    QHttpServerResponder::StatusCode status) {
  self->write(status);
}

//  void QHttpServerResponderPrivate::write(QIODevice *data, const
//      QHttpHeaders &headers, QHttpServerResponder::StatusCode status)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QHttpServerResponderPrivate5writeEP9QIODeviceRK12QHttpHeadersN20QHttpServerResponder10StatusCodeE(
    QHttpServerResponderPrivate *self,
    QIODevice *data,
    const QHttpHeaders *headers,
    QHttpServerResponder::StatusCode status) {
  self->write(data, *headers, status);
}

//  void QHttpServerResponderPrivate::writeBeginChunked(const QHttpHeaders
//      &headers, QHttpServerResponder::StatusCode status)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QHttpServerResponderPrivate17writeBeginChunkedERK12QHttpHeadersN20QHttpServerResponder10StatusCodeE(
    QHttpServerResponderPrivate *self,
    const QHttpHeaders *headers,
    QHttpServerResponder::StatusCode status) {
  self->writeBeginChunked(*headers, status);
}

//  void QHttpServerResponderPrivate::writeChunk(const QByteArray &body)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QHttpServerResponderPrivate10writeChunkERK10QByteArray(
    QHttpServerResponderPrivate *self,
    const QByteArray *body) {
  self->writeChunk(*body);
}

//  void QHttpServerResponderPrivate::writeEndChunked(const QByteArray &data,
//      const QHttpHeaders &trailers)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QHttpServerResponderPrivate15writeEndChunkedERK10QByteArrayRK12QHttpHeaders(
    QHttpServerResponderPrivate *self,
    const QByteArray *data,
    const QHttpHeaders *trailers) {
  self->writeEndChunked(*data, *trailers);
}

//  void QHttpServerResponderPrivate::cancel()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QHttpServerResponderPrivate6cancelEv(
    QHttpServerResponderPrivate *self) {
  self->cancel();
}
