//  Written by dev_tooling.RitualGenerator from the records of
//  QtHttpServer/6.12.0/QtHttpServer/private/qhttpserverstream_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtHttpServer/QtHttpServer>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtHttpServer/6.12.0/QtHttpServer/private/qhttpserverstream_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtNetwork/qhttpheaders.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
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
#include <QtHttpServer/private/qhttpserverstream_p.h>
#include <QtHttpServer/private/qhttpserverresponder_p.h>
#include <QtNetwork/qtcpsocket.h>
#if QT_CONFIG(ssl)
#include <QtNetwork/qsslsocket.h>
#endif
#if QT_CONFIG(localserver)
#include <QtNetwork/qlocalsocket.h>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qthttpserver/src/httpserver/qhttpserverresponder.cpp, line 124, as _ZN27QHttpServerResponderPrivate6cancelEv
inline void QHttpServerResponderPrivate::cancel()
{
    canceled = true;
}

//  from ../qthttpserver/src/httpserver/qhttpserverstream.cpp, line 50, as _ZN17QHttpServerStream16connectResponderEP27QHttpServerResponderPrivate
inline void QHttpServerStream::connectResponder(QHttpServerResponderPrivate *responder)
{
    if (QTcpSocket *tcpSocket = qobject_cast<QTcpSocket *>(clientSocket)) {
        responderConnections.insert(responder->m_streamId,
                                    connect(tcpSocket, &QAbstractSocket::disconnected, tcpSocket,
                                            [responder]() { responder->cancel(); }));
#if QT_CONFIG(localserver)
    } else if (QLocalSocket *localSocket = qobject_cast<QLocalSocket *>(clientSocket)) {
        responderConnections.insert(responder->m_streamId,
                                    connect(localSocket, &QLocalSocket::disconnected, localSocket,
                                            [responder]() { responder->cancel(); }));
#endif
    }
}

//  from ../qthttpserver/src/httpserver/qhttpserverstream.cpp, line 65, as _ZN17QHttpServerStream19disconnectResponderEj
inline void QHttpServerStream::disconnectResponder(quint32 streamId)
{
    auto connection = responderConnections.take(streamId);
    if (connection)
        disconnect(connection);
}
//  -----------------------------------------------------------------------

//  A QHttpServerStream that Python can take functions over in. Every QHttpServerStream
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQHttpServerStreamCall0)(const void *, quint32, int *);
typedef void (*CuteQHttpServerStreamCall1)(const void *, int *);
typedef void (*CuteQHttpServerStreamCall2)(const void *, int *);
typedef void (*CuteQHttpServerStreamCall3)(const void *, const QByteArray *, const QHttpHeaders *, int, quint32, int *);
typedef void (*CuteQHttpServerStreamCall4)(const void *, int, quint32, int *);
typedef void (*CuteQHttpServerStreamCall5)(const void *, QIODevice *, const QHttpHeaders *, int, quint32, int *);
typedef void (*CuteQHttpServerStreamCall6)(const void *, const QHttpHeaders *, int, quint32, int *);
typedef void (*CuteQHttpServerStreamCall7)(const void *, const QByteArray *, quint32, int *);
typedef void (*CuteQHttpServerStreamCall8)(const void *, const QByteArray *, const QHttpHeaders *, quint32, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQHttpServerStreamCall9)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQHttpServerStreamCall10)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHttpServerStreamCall11)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHttpServerStreamCall12)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHttpServerStreamCall13)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHttpServerStreamCall14)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHttpServerStreamCall15)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQHttpServerStream : public QHttpServerStream {
public:
  using QHttpServerStream::QHttpServerStream;
  void *taken[16] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN17QHttpServerStream18responderDestroyedEj")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QHttpServerStream20startHandlingRequestEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QHttpServerStream18socketDisconnectedEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QHttpServerStream5writeERK10QByteArrayRK12QHttpHeadersN20QHttpServerResponder10StatusCodeEj")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QHttpServerStream5writeEN20QHttpServerResponder10StatusCodeEj")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QHttpServerStream5writeEP9QIODeviceRK12QHttpHeadersN20QHttpServerResponder10StatusCodeEj")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QHttpServerStream17writeBeginChunkedERK12QHttpHeadersN20QHttpServerResponder10StatusCodeEj")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QHttpServerStream10writeChunkERK10QByteArrayj")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QHttpServerStream15writeEndChunkedERK10QByteArrayRK12QHttpHeadersj")) {
      taken[8] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[13] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[14] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[15] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QHttpServerStream::responderDestroyed(quint32 streamId)
  void responderDestroyed(quint32 streamId) override {
    if (taken[0]) {
      int handled = 0;
      CuteQHttpServerStreamCall0 call = reinterpret_cast<CuteQHttpServerStreamCall0>(taken[0]);
      call(this, streamId, &handled);
      if (handled) return;
    }
  }

  //  void QHttpServerStream::startHandlingRequest()
  void startHandlingRequest() override {
    if (taken[1]) {
      int handled = 0;
      CuteQHttpServerStreamCall1 call = reinterpret_cast<CuteQHttpServerStreamCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QHttpServerStream::socketDisconnected()
  void socketDisconnected() override {
    if (taken[2]) {
      int handled = 0;
      CuteQHttpServerStreamCall2 call = reinterpret_cast<CuteQHttpServerStreamCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QHttpServerStream::write(const QByteArray &body, const
  //      QHttpHeaders &headers, QHttpServerResponder::StatusCode status,
  //      quint32 streamId)
  void write(
      const QByteArray &body,
      const QHttpHeaders &headers,
      QHttpServerResponder::StatusCode status,
      quint32 streamId) override {
    if (taken[3]) {
      int handled = 0;
      CuteQHttpServerStreamCall3 call = reinterpret_cast<CuteQHttpServerStreamCall3>(taken[3]);
      call(this, &body, &headers, static_cast<int>(status), streamId, &handled);
      if (handled) return;
    }
  }

  //  void QHttpServerStream::write(QHttpServerResponder::StatusCode
  //      status, quint32 streamId)
  void write(
      QHttpServerResponder::StatusCode status,
      quint32 streamId) override {
    if (taken[4]) {
      int handled = 0;
      CuteQHttpServerStreamCall4 call = reinterpret_cast<CuteQHttpServerStreamCall4>(taken[4]);
      call(this, static_cast<int>(status), streamId, &handled);
      if (handled) return;
    }
  }

  //  void QHttpServerStream::write(QIODevice *data, const QHttpHeaders
  //      &headers, QHttpServerResponder::StatusCode status, quint32
  //      streamId)
  void write(
      QIODevice *data,
      const QHttpHeaders &headers,
      QHttpServerResponder::StatusCode status,
      quint32 streamId) override {
    if (taken[5]) {
      int handled = 0;
      CuteQHttpServerStreamCall5 call = reinterpret_cast<CuteQHttpServerStreamCall5>(taken[5]);
      call(this, data, &headers, static_cast<int>(status), streamId, &handled);
      if (handled) return;
    }
  }

  //  void QHttpServerStream::writeBeginChunked(const QHttpHeaders
  //      &headers, QHttpServerResponder::StatusCode status, quint32
  //      streamId)
  void writeBeginChunked(
      const QHttpHeaders &headers,
      QHttpServerResponder::StatusCode status,
      quint32 streamId) override {
    if (taken[6]) {
      int handled = 0;
      CuteQHttpServerStreamCall6 call = reinterpret_cast<CuteQHttpServerStreamCall6>(taken[6]);
      call(this, &headers, static_cast<int>(status), streamId, &handled);
      if (handled) return;
    }
  }

  //  void QHttpServerStream::writeChunk(const QByteArray &body, quint32
  //      streamId)
  void writeChunk(const QByteArray &body, quint32 streamId) override {
    if (taken[7]) {
      int handled = 0;
      CuteQHttpServerStreamCall7 call = reinterpret_cast<CuteQHttpServerStreamCall7>(taken[7]);
      call(this, &body, streamId, &handled);
      if (handled) return;
    }
  }

  //  void QHttpServerStream::writeEndChunked(const QByteArray &data, const
  //      QHttpHeaders &trailers, quint32 streamId)
  void writeEndChunked(
      const QByteArray &data,
      const QHttpHeaders &trailers,
      quint32 streamId) override {
    if (taken[8]) {
      int handled = 0;
      CuteQHttpServerStreamCall8 call = reinterpret_cast<CuteQHttpServerStreamCall8>(taken[8]);
      call(this, &data, &trailers, streamId, &handled);
      if (handled) return;
    }
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQHttpServerStreamCall9 call = reinterpret_cast<CuteQHttpServerStreamCall9>(taken[9]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQHttpServerStreamCall10 call = reinterpret_cast<CuteQHttpServerStreamCall10>(taken[10]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQHttpServerStreamCall11 call = reinterpret_cast<CuteQHttpServerStreamCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQHttpServerStreamCall12 call = reinterpret_cast<CuteQHttpServerStreamCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQHttpServerStreamCall13 call = reinterpret_cast<CuteQHttpServerStreamCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[14]) {
      int handled = 0;
      CuteQHttpServerStreamCall14 call = reinterpret_cast<CuteQHttpServerStreamCall14>(taken[14]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[15]) {
      int handled = 0;
      CuteQHttpServerStreamCall15 call = reinterpret_cast<CuteQHttpServerStreamCall15>(taken[15]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QHttpServerStream::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QHttpServerStream10metaObjectEv(
    const QHttpServerStream *self) {
  return self->metaObject();
}

//  void QHttpServerStream::responderDestroyed(quint32 streamId)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QHttpServerStream18responderDestroyedEj(
    QHttpServerStream *self,
    quint32 streamId) {
  self->responderDestroyed(streamId);
}

//  void QHttpServerStream::startHandlingRequest()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QHttpServerStream20startHandlingRequestEv(
    QHttpServerStream *self) {
  self->startHandlingRequest();
}

//  void QHttpServerStream::socketDisconnected()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QHttpServerStream18socketDisconnectedEv(
    QHttpServerStream *self) {
  self->socketDisconnected();
}

//  void QHttpServerStream::write(const QByteArray &body, const QHttpHeaders
//      &headers, QHttpServerResponder::StatusCode status, quint32 streamId)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QHttpServerStream5writeERK10QByteArrayRK12QHttpHeadersN20QHttpServerResponder10StatusCodeEj(
    QHttpServerStream *self,
    const QByteArray *body,
    const QHttpHeaders *headers,
    QHttpServerResponder::StatusCode status,
    quint32 streamId) {
  self->write(*body, *headers, status, streamId);
}

//  void QHttpServerStream::write(QHttpServerResponder::StatusCode status,
//      quint32 streamId)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QHttpServerStream5writeEN20QHttpServerResponder10StatusCodeEj(
    QHttpServerStream *self,
    QHttpServerResponder::StatusCode status,
    quint32 streamId) {
  self->write(status, streamId);
}

//  void QHttpServerStream::write(QIODevice *data, const QHttpHeaders
//      &headers, QHttpServerResponder::StatusCode status, quint32 streamId)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QHttpServerStream5writeEP9QIODeviceRK12QHttpHeadersN20QHttpServerResponder10StatusCodeEj(
    QHttpServerStream *self,
    QIODevice *data,
    const QHttpHeaders *headers,
    QHttpServerResponder::StatusCode status,
    quint32 streamId) {
  self->write(data, *headers, status, streamId);
}

//  void QHttpServerStream::writeBeginChunked(const QHttpHeaders &headers,
//      QHttpServerResponder::StatusCode status, quint32 streamId)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QHttpServerStream17writeBeginChunkedERK12QHttpHeadersN20QHttpServerResponder10StatusCodeEj(
    QHttpServerStream *self,
    const QHttpHeaders *headers,
    QHttpServerResponder::StatusCode status,
    quint32 streamId) {
  self->writeBeginChunked(*headers, status, streamId);
}

//  void QHttpServerStream::writeChunk(const QByteArray &body, quint32
//      streamId)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QHttpServerStream10writeChunkERK10QByteArrayj(
    QHttpServerStream *self,
    const QByteArray *body,
    quint32 streamId) {
  self->writeChunk(*body, streamId);
}

//  void QHttpServerStream::writeEndChunked(const QByteArray &data, const
//      QHttpHeaders &trailers, quint32 streamId)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QHttpServerStream15writeEndChunkedERK10QByteArrayRK12QHttpHeadersj(
    QHttpServerStream *self,
    const QByteArray *data,
    const QHttpHeaders *trailers,
    quint32 streamId) {
  self->writeEndChunked(*data, *trailers, streamId);
}

//  void QHttpServerStream::connectResponder(QHttpServerResponderPrivate
//      *responder)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QHttpServerStream16connectResponderEP27QHttpServerResponderPrivate(
    QHttpServerStream *self,
    QHttpServerResponderPrivate *responder) {
  self->connectResponder(responder);
}

//  void QHttpServerStream::disconnectResponder(quint32 streamId)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QHttpServerStream19disconnectResponderEj(
    QHttpServerStream *self,
    quint32 streamId) {
  self->disconnectResponder(streamId);
}

//  a Python function taken by a CuteQHttpServerStream, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QHttpServerStream(
    QHttpServerStream *self,
    const char *key,
    void *call) {
  return static_cast<CuteQHttpServerStream *>(self)->take(key, call);
}
