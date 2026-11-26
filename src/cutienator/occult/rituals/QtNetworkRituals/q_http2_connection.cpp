//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/qhttp2connection_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtNetwork/qtnetworkglobal.h>
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#if QT_CONFIG(http)
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qhttp2connection_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#if QT_CONFIG(http)
#include <QtNetwork/qhttp2configuration.h>
#endif
#include <QtCore/qurl.h>
#include <QtCore/qbytearrayview.h>
#if QT_CONFIG(http)
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/http2frames_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#endif
#include <QtCore/qmetaobject.h>
#include <cstring>
#include <optional>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/private/qhttp2connection_p.h>
#include <QtNetwork/private/qhttp2configuration_p.h>
#include <QtNetwork/private/bitstreams_p.h>
#include <QtCore/private/qnumeric_p.h>
#include <QtCore/private/qiodevice_p.h>
#include <QtCore/private/qnoncontiguousbytedevice_p.h>
#include <QtCore/qcoreapplication.h>
#include <QtCore/QRandomGenerator>
#include <QtCore/qloggingcategory.h>
#include <algorithm>
#include <memory>
#include <chrono>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from src/network/access/qhttp2connection.cpp, line 1417, as _ZNK16QHttp2Connection15streamIsIgnoredEj
inline bool QHttp2Connection::streamIsIgnored(quint32 streamID) const noexcept
{
    const bool streamIsRemote = (streamID & 1) == (m_connectionType == Type::Client ? 0 : 1);
    return Q_UNLIKELY(streamIsRemote && m_lastStreamToProcess < streamID);
}
//  -----------------------------------------------------------------------

//  A QHttp2Connection that Python can take functions over in. Every QHttp2Connection
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQHttp2ConnectionCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQHttp2ConnectionCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHttp2ConnectionCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHttp2ConnectionCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHttp2ConnectionCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHttp2ConnectionCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHttp2ConnectionCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQHttp2Connection : public QHttp2Connection {
public:
  using QHttp2Connection::QHttp2Connection;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQHttp2ConnectionCall0 call = reinterpret_cast<CuteQHttp2ConnectionCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQHttp2ConnectionCall1 call = reinterpret_cast<CuteQHttp2ConnectionCall1>(taken[1]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQHttp2ConnectionCall2 call = reinterpret_cast<CuteQHttp2ConnectionCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQHttp2ConnectionCall3 call = reinterpret_cast<CuteQHttp2ConnectionCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQHttp2ConnectionCall4 call = reinterpret_cast<CuteQHttp2ConnectionCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteQHttp2ConnectionCall5 call = reinterpret_cast<CuteQHttp2ConnectionCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQHttp2ConnectionCall6 call = reinterpret_cast<CuteQHttp2ConnectionCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QHttp2Connection::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QHttp2Connection10metaObjectEv(
    const QHttp2Connection *self) {
  return self->metaObject();
}

//  void *QHttp2Connection::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN16QHttp2Connection11qt_metacastEPKc(
    QHttp2Connection *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QHttp2Connection::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN16QHttp2Connection11qt_metacallEN11QMetaObject4CallEiPPv(
    QHttp2Connection *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QHttp2Connection::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QHttp2Connection2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QHttp2Connection::tr(s, c, n));
}

//  QHttp2Connection *QHttp2Connection::createUpgradedConnection(QIODevice
//      *socket, const QHttp2Configuration &config)
extern "C" Q_DECL_EXPORT
QHttp2Connection *ritual_ZN16QHttp2Connection24createUpgradedConnectionEP9QIODeviceRK19QHttp2Configuration(
    QIODevice *socket,
    const QHttp2Configuration *config) {
  return QHttp2Connection::createUpgradedConnection(socket, *config);
}

//  QHttp2Connection *QHttp2Connection::createDirectConnection(QIODevice
//      *socket, const QHttp2Configuration &config)
extern "C" Q_DECL_EXPORT
QHttp2Connection *ritual_ZN16QHttp2Connection22createDirectConnectionEP9QIODeviceRK19QHttp2Configuration(
    QIODevice *socket,
    const QHttp2Configuration *config) {
  return QHttp2Connection::createDirectConnection(socket, *config);
}

//  QHttp2Connection
//      *QHttp2Connection::createDirectServerConnection(QIODevice *socket,
//      const QHttp2Configuration &config)
extern "C" Q_DECL_EXPORT
QHttp2Connection *ritual_ZN16QHttp2Connection28createDirectServerConnectionEP9QIODeviceRK19QHttp2Configuration(
    QIODevice *socket,
    const QHttp2Configuration *config) {
  return QHttp2Connection::createDirectServerConnection(socket, *config);
}

//  QHttp2Connection::~QHttp2Connection()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QHttp2ConnectionD1Ev(QHttp2Connection *self) {
  delete self;
}

//  QH2Expected<QHttp2Stream *, CreateStreamError>
//      QHttp2Connection::createStream()
extern "C" Q_DECL_EXPORT
QH2Expected<QHttp2Stream *, QHttp2Connection::CreateStreamError> *ritual_ZN16QHttp2Connection12createStreamEv(
    QHttp2Connection *self) {
  return new QH2Expected<QHttp2Stream *, QHttp2Connection::CreateStreamError>(
      self->createStream());
}

//  QH2Expected<QHttp2Stream *, CreateStreamError>
//      QHttp2Connection::createStream(QHttp2Stream::Configuration config)
extern "C" Q_DECL_EXPORT
QH2Expected<QHttp2Stream *, QHttp2Connection::CreateStreamError> *ritual_ZN16QHttp2Connection12createStreamEN12QHttp2Stream13ConfigurationE(
    QHttp2Connection *self,
    const QHttp2Stream::Configuration *config) {
  return new QH2Expected<QHttp2Stream *, QHttp2Connection::CreateStreamError>(
      self->createStream(
          *config));
}

//  QHttp2Stream *QHttp2Connection::getStream(quint32 streamId) const
extern "C" Q_DECL_EXPORT
QHttp2Stream *ritual_ZNK16QHttp2Connection9getStreamEj(
    const QHttp2Connection *self,
    quint32 streamId) {
  return self->getStream(streamId);
}

//  QHttp2Stream *QHttp2Connection::promisedStream(const QUrl &streamKey)
//      const
extern "C" Q_DECL_EXPORT
QHttp2Stream *ritual_ZNK16QHttp2Connection14promisedStreamERK4QUrl(
    const QHttp2Connection *self,
    const QUrl *streamKey) {
  return self->promisedStream(*streamKey);
}

//  void QHttp2Connection::close(Http2::Http2Error errorCode)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QHttp2Connection5closeEN5Http210Http2ErrorE(
    QHttp2Connection *self,
    Http2::Http2Error errorCode) {
  self->close(errorCode);
}

//  bool QHttp2Connection::isGoingAway() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QHttp2Connection11isGoingAwayEv(
    const QHttp2Connection *self) {
  return self->isGoingAway();
}

//  std::optional<quint32> QHttp2Connection::lastGoAwayStreamID() const
extern "C" Q_DECL_EXPORT
std::optional<quint32> *ritual_ZNK16QHttp2Connection18lastGoAwayStreamIDEv(
    const QHttp2Connection *self) {
  return new std::optional<quint32>(self->lastGoAwayStreamID());
}

//  quint32 QHttp2Connection::maxConcurrentStreams() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK16QHttp2Connection20maxConcurrentStreamsEv(
    const QHttp2Connection *self) {
  return self->maxConcurrentStreams();
}

//  quint32 QHttp2Connection::peerMaxConcurrentStreams() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK16QHttp2Connection24peerMaxConcurrentStreamsEv(
    const QHttp2Connection *self) {
  return self->peerMaxConcurrentStreams();
}

//  quint32 QHttp2Connection::maxHeaderListSize() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK16QHttp2Connection17maxHeaderListSizeEv(
    const QHttp2Connection *self) {
  return self->maxHeaderListSize();
}

//  bool QHttp2Connection::isUpgradedConnection() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QHttp2Connection20isUpgradedConnectionEv(
    const QHttp2Connection *self) {
  return self->isUpgradedConnection();
}

//  void QHttp2Connection::newIncomingStream(QHttp2Stream *stream)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QHttp2Connection17newIncomingStreamEP12QHttp2Stream(
    QHttp2Connection *self,
    QHttp2Stream *stream) {
  self->newIncomingStream(stream);
}

//  void QHttp2Connection::newPromisedStream(QHttp2Stream *stream)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QHttp2Connection17newPromisedStreamEP12QHttp2Stream(
    QHttp2Connection *self,
    QHttp2Stream *stream) {
  self->newPromisedStream(stream);
}

//  void QHttp2Connection::errorReceived()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QHttp2Connection13errorReceivedEv(QHttp2Connection *self) {
  self->errorReceived();
}

//  void QHttp2Connection::connectionClosed()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QHttp2Connection16connectionClosedEv(
    QHttp2Connection *self) {
  self->connectionClosed();
}

//  void QHttp2Connection::settingsFrameReceived()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QHttp2Connection21settingsFrameReceivedEv(
    QHttp2Connection *self) {
  self->settingsFrameReceived();
}

//  void QHttp2Connection::pingFrameReceived(QHttp2Connection::PingState
//      state)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QHttp2Connection17pingFrameReceivedENS_9PingStateE(
    QHttp2Connection *self,
    QHttp2Connection::PingState state) {
  self->pingFrameReceived(state);
}

//  void QHttp2Connection::errorOccurred(Http2::Http2Error errorCode, const
//      QString &errorString)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QHttp2Connection13errorOccurredEN5Http210Http2ErrorERK7QString(
    QHttp2Connection *self,
    Http2::Http2Error errorCode,
    const QString *errorString) {
  self->errorOccurred(errorCode, *errorString);
}

//  void QHttp2Connection::receivedGOAWAY(Http2::Http2Error errorCode,
//      quint32 lastStreamID)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QHttp2Connection14receivedGOAWAYEN5Http210Http2ErrorEj(
    QHttp2Connection *self,
    Http2::Http2Error errorCode,
    quint32 lastStreamID) {
  self->receivedGOAWAY(errorCode, lastStreamID);
}

//  void QHttp2Connection::receivedEND_STREAM(quint32 streamID)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QHttp2Connection18receivedEND_STREAMEj(
    QHttp2Connection *self,
    quint32 streamID) {
  self->receivedEND_STREAM(streamID);
}

//  void QHttp2Connection::incomingStreamErrorOccured(CreateStreamError
//      error)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QHttp2Connection26incomingStreamErrorOccuredENS_17CreateStreamErrorE(
    QHttp2Connection *self,
    QHttp2Connection::CreateStreamError error) {
  self->incomingStreamErrorOccured(error);
}

//  bool QHttp2Connection::sendPing()
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QHttp2Connection8sendPingEv(QHttp2Connection *self) {
  return self->sendPing();
}

//  bool QHttp2Connection::sendPing(QByteArrayView data)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QHttp2Connection8sendPingE14QByteArrayView(
    QHttp2Connection *self,
    const QByteArrayView *data) {
  return self->sendPing(*data);
}

//  void QHttp2Connection::handleReadyRead()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QHttp2Connection15handleReadyReadEv(QHttp2Connection *self) {
  self->handleReadyRead();
}

//  void QHttp2Connection::handleConnectionClosure()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QHttp2Connection23handleConnectionClosureEv(
    QHttp2Connection *self) {
  self->handleConnectionClosure();
}

//  QIODevice *QHttp2Connection::getSocket() const
extern "C" Q_DECL_EXPORT
QIODevice *ritual_ZNK16QHttp2Connection9getSocketEv(
    const QHttp2Connection *self) {
  return self->getSocket();
}

//  QH2Expected<QHttp2Stream *, QHttp2Connection::CreateStreamError>
//      QHttp2Connection::createLocalStreamInternal(QHttp2Stream::Configurati
//      on a0)
extern "C" Q_DECL_EXPORT
QH2Expected<QHttp2Stream *, QHttp2Connection::CreateStreamError> *ritual_ZN16QHttp2Connection25createLocalStreamInternalEN12QHttp2Stream13ConfigurationE(
    QHttp2Connection *self,
    const QHttp2Stream::Configuration *a0) {
  return new QH2Expected<QHttp2Stream *, QHttp2Connection::CreateStreamError>(
      self->createLocalStreamInternal(
          *a0));
}

//  QHttp2Stream *QHttp2Connection::createStreamInternal_impl(quint32
//      streamID, QHttp2Stream::Configuration a1)
extern "C" Q_DECL_EXPORT
QHttp2Stream *ritual_ZN16QHttp2Connection25createStreamInternal_implEjN12QHttp2Stream13ConfigurationE(
    QHttp2Connection *self,
    quint32 streamID,
    const QHttp2Stream::Configuration *a1) {
  return self->createStreamInternal_impl(streamID, *a1);
}

//  bool QHttp2Connection::isInvalidStream(quint32 streamID)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QHttp2Connection15isInvalidStreamEj(
    QHttp2Connection *self,
    quint32 streamID) {
  return self->isInvalidStream(streamID);
}

//  bool QHttp2Connection::streamWasResetLocally(quint32 streamID)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QHttp2Connection21streamWasResetLocallyEj(
    QHttp2Connection *self,
    quint32 streamID) {
  return self->streamWasResetLocally(streamID);
}

//  bool QHttp2Connection::streamIsIgnored(quint32 streamID) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QHttp2Connection15streamIsIgnoredEj(
    const QHttp2Connection *self,
    quint32 streamID) {
  return self->streamIsIgnored(streamID);
}

//  void QHttp2Connection::connectionError(Http2::Http2Error errorCode, const
//      QString &message, bool logAsError)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QHttp2Connection15connectionErrorEN5Http210Http2ErrorERK7QStringb(
    QHttp2Connection *self,
    Http2::Http2Error errorCode,
    const QString *message,
    bool logAsError) {
  self->connectionError(errorCode, *message, logAsError);
}

//  void QHttp2Connection::setH2Configuration(QHttp2Configuration config)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QHttp2Connection18setH2ConfigurationE19QHttp2Configuration(
    QHttp2Connection *self,
    const QHttp2Configuration *config) {
  self->setH2Configuration(*config);
}

//  void QHttp2Connection::closeSession()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QHttp2Connection12closeSessionEv(QHttp2Connection *self) {
  self->closeSession();
}

//  void QHttp2Connection::registerStreamAsResetLocally(quint32 streamID)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QHttp2Connection28registerStreamAsResetLocallyEj(
    QHttp2Connection *self,
    quint32 streamID) {
  self->registerStreamAsResetLocally(streamID);
}

//  qsizetype QHttp2Connection::numActiveStreamsImpl(quint32 mask) const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK16QHttp2Connection20numActiveStreamsImplEj(
    const QHttp2Connection *self,
    quint32 mask) {
  return self->numActiveStreamsImpl(mask);
}

//  qsizetype QHttp2Connection::numActiveRemoteStreams() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK16QHttp2Connection22numActiveRemoteStreamsEv(
    const QHttp2Connection *self) {
  return self->numActiveRemoteStreams();
}

//  qsizetype QHttp2Connection::numActiveLocalStreams() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK16QHttp2Connection21numActiveLocalStreamsEv(
    const QHttp2Connection *self) {
  return self->numActiveLocalStreams();
}

//  bool QHttp2Connection::sendClientPreface()
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QHttp2Connection17sendClientPrefaceEv(
    QHttp2Connection *self) {
  return self->sendClientPreface();
}

//  bool QHttp2Connection::sendSETTINGS()
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QHttp2Connection12sendSETTINGSEv(QHttp2Connection *self) {
  return self->sendSETTINGS();
}

//  bool QHttp2Connection::sendServerPreface()
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QHttp2Connection17sendServerPrefaceEv(
    QHttp2Connection *self) {
  return self->sendServerPreface();
}

//  bool QHttp2Connection::serverCheckClientPreface()
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QHttp2Connection24serverCheckClientPrefaceEv(
    QHttp2Connection *self) {
  return self->serverCheckClientPreface();
}

//  bool QHttp2Connection::sendWINDOW_UPDATE(quint32 streamID, quint32 delta)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QHttp2Connection17sendWINDOW_UPDATEEjj(
    QHttp2Connection *self,
    quint32 streamID,
    quint32 delta) {
  return self->sendWINDOW_UPDATE(streamID, delta);
}

//  void QHttp2Connection::sendClientGracefulShutdownGoaway()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QHttp2Connection32sendClientGracefulShutdownGoawayEv(
    QHttp2Connection *self) {
  self->sendClientGracefulShutdownGoaway();
}

//  void QHttp2Connection::sendInitialServerGracefulShutdownGoaway()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QHttp2Connection39sendInitialServerGracefulShutdownGoawayEv(
    QHttp2Connection *self) {
  self->sendInitialServerGracefulShutdownGoaway();
}

//  void QHttp2Connection::sendFinalServerGracefulShutdownGoaway()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QHttp2Connection37sendFinalServerGracefulShutdownGoawayEv(
    QHttp2Connection *self) {
  self->sendFinalServerGracefulShutdownGoaway();
}

//  bool QHttp2Connection::sendGOAWAYFrame(Http2::Http2Error errorCode,
//      quint32 lastSreamID)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QHttp2Connection15sendGOAWAYFrameEN5Http210Http2ErrorEj(
    QHttp2Connection *self,
    Http2::Http2Error errorCode,
    quint32 lastSreamID) {
  return self->sendGOAWAYFrame(errorCode, lastSreamID);
}

//  void QHttp2Connection::maybeCloseOnGoingAway()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QHttp2Connection21maybeCloseOnGoingAwayEv(
    QHttp2Connection *self) {
  self->maybeCloseOnGoingAway();
}

//  bool QHttp2Connection::sendSETTINGS_ACK()
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QHttp2Connection16sendSETTINGS_ACKEv(
    QHttp2Connection *self) {
  return self->sendSETTINGS_ACK();
}

//  void QHttp2Connection::handleDATA()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QHttp2Connection10handleDATAEv(QHttp2Connection *self) {
  self->handleDATA();
}

//  void QHttp2Connection::handleHEADERS()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QHttp2Connection13handleHEADERSEv(QHttp2Connection *self) {
  self->handleHEADERS();
}

//  void QHttp2Connection::handlePRIORITY()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QHttp2Connection14handlePRIORITYEv(QHttp2Connection *self) {
  self->handlePRIORITY();
}

//  void QHttp2Connection::handleRST_STREAM()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QHttp2Connection16handleRST_STREAMEv(
    QHttp2Connection *self) {
  self->handleRST_STREAM();
}

//  void QHttp2Connection::handleSETTINGS()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QHttp2Connection14handleSETTINGSEv(QHttp2Connection *self) {
  self->handleSETTINGS();
}

//  void QHttp2Connection::handlePUSH_PROMISE()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QHttp2Connection18handlePUSH_PROMISEEv(
    QHttp2Connection *self) {
  self->handlePUSH_PROMISE();
}

//  void QHttp2Connection::handlePING()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QHttp2Connection10handlePINGEv(QHttp2Connection *self) {
  self->handlePING();
}

//  void QHttp2Connection::handleGOAWAY()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QHttp2Connection12handleGOAWAYEv(QHttp2Connection *self) {
  self->handleGOAWAY();
}

//  void QHttp2Connection::handleWINDOW_UPDATE()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QHttp2Connection19handleWINDOW_UPDATEEv(
    QHttp2Connection *self) {
  self->handleWINDOW_UPDATE();
}

//  void QHttp2Connection::handleCONTINUATION()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QHttp2Connection18handleCONTINUATIONEv(
    QHttp2Connection *self) {
  self->handleCONTINUATION();
}

//  void QHttp2Connection::handleContinuedHEADERS()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QHttp2Connection22handleContinuedHEADERSEv(
    QHttp2Connection *self) {
  self->handleContinuedHEADERS();
}

//  bool QHttp2Connection::validateHeaderListSize(const Http2::Frame &frame)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QHttp2Connection22validateHeaderListSizeERKN5Http25FrameE(
    QHttp2Connection *self,
    const Http2::Frame *frame) {
  return self->validateHeaderListSize(*frame);
}

//  bool QHttp2Connection::acceptSetting(Http2::Settings identifier, quint32
//      newValue)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QHttp2Connection13acceptSettingEN5Http28SettingsEj(
    QHttp2Connection *self,
    Http2::Settings identifier,
    quint32 newValue) {
  return self->acceptSetting(identifier, newValue);
}

//  bool QHttp2Connection::readClientPreface()
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QHttp2Connection17readClientPrefaceEv(
    QHttp2Connection *self) {
  return self->readClientPreface();
}

//  QHttp2Connection::QHttp2Connection(QIODevice *socket)
extern "C" Q_DECL_EXPORT
QHttp2Connection *ritual_ZN16QHttp2ConnectionC1EP9QIODevice(
    QIODevice *socket) {
  return new CuteQHttp2Connection(socket);
}

//  a Python function taken by a CuteQHttp2Connection, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QHttp2Connection(
    QHttp2Connection *self,
    const char *key,
    void *call) {
  return static_cast<CuteQHttp2Connection *>(self)->take(key, call);
}

//  a QH2Expected<QHttp2Stream *, QHttp2Connection::CreateStreamError> a
//      ritual of QHttp2Connection gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QHttp2Connection__QH2Expected_QHttp2Stream_QHttp2Connection_CreateStreamError(
    QH2Expected<QHttp2Stream *, QHttp2Connection::CreateStreamError> *self) {
  delete self;
}

//  a std::optional<quint32> a ritual of QHttp2Connection gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QHttp2Connection__std_optional_quint32(
    std::optional<quint32> *self) {
  delete self;
}

#endif  // QT_CONFIG(http)
