//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/qhttp2protocolhandler_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtNetwork/qtnetworkglobal.h>
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#if QT_CONFIG(http)
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qhttp2protocolhandler_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qhttpnetworkrequest_p.h"
#include "private/qnoncontiguousbytedevice_p.h"
#include <QtCore/private/qtools_p.h>
#include "qhttpnetworkreply_p.h"
#include "qhttpnetworkconnection_p.h"
#ifndef QT_NO_SSL
#    include <QtNetwork/qsslkey.h>
#    include <QtNetwork/qsslcipher.h>
#    include <QtNetwork/qsslconfiguration.h>
#endif
#include <private/qdecompresshelper_p.h>
#include "qhttpnetworkconnectionchannel_p.h"
#include "qhttpnetworkconnection_p.h"
#include "private/qnoncontiguousbytedevice_p.h"
#include <qdebug.h>
#include <private/qhttp2protocolhandler_p.h>
#include <private/qhttpprotocolhandler_p.h>
#include <private/http2protocol_p.h>
#include <private/qsocketabstraction_p.h>
#ifndef QT_NO_SSL
#    include <private/qsslsocket_p.h>
#    include <QtNetwork/qsslkey.h>
#    include <QtNetwork/qsslcipher.h>
#endif
#include <QtNetwork/private/qtnetworkglobal_p.h>
#include <memory>
#include <utility>
#include "qhttpnetworkconnection_p.h"
#include "qhttp2protocolhandler_p.h"
#include <private/qnoncontiguousbytedevice_p.h>
#include <private/qsocketabstraction_p.h>
#include <QtNetwork/qabstractsocket.h>
#include <QtCore/qloggingcategory.h>
#include <QtCore/qendian.h>
#include <QtCore/qdebug.h>
#include <QtCore/qlist.h>
#include <QtCore/qnumeric.h>
#include <QtCore/qurl.h>
#include <qhttp2configuration.h>
#ifndef QT_NO_NETWORKPROXY
#  include <QtNetwork/qnetworkproxy.h>
#endif
#include <qcoreapplication.h>
#include <algorithm>
#include <vector>
#include <optional>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/network/access/qhttpnetworkrequest.cpp, line 376, as _ZNK19QHttpNetworkRequest16uploadByteDeviceEv
inline QNonContiguousByteDevice* QHttpNetworkRequest::uploadByteDevice() const
{
    return d->uploadByteDevice;
}

//  from src/network/access/qhttpnetworkrequest.cpp, line 178, as _ZN19QHttpNetworkRequestC1ERK4QUrlNS_9OperationENS_8PriorityE
inline QHttpNetworkRequest::QHttpNetworkRequest(const QUrl &url, Operation operation, Priority priority)
    : d(new QHttpNetworkRequestPrivate(operation, priority, url))
{
}

//  from src/network/access/qhttpnetworkrequest.cpp, line 183, as _ZN19QHttpNetworkRequestC1ERKS_
inline QHttpNetworkRequest::QHttpNetworkRequest(const QHttpNetworkRequest &other)
    : QHttpNetworkHeader(other), d(other.d)
{
}

//  from src/network/access/qhttpnetworkrequest.cpp, line 188, as _ZN19QHttpNetworkRequestD1Ev
inline QHttpNetworkRequest::~QHttpNetworkRequest()
{
}

//  from src/network/access/qhttpnetworkreply.cpp, line 732, as _ZN24QHttpNetworkReplyPrivate17shouldEmitSignalsEv
inline bool QHttpNetworkReplyPrivate::shouldEmitSignals()
{
    // for 401 & 407 don't emit the data signals. Content along with these
    // responses are sent only if the authentication fails.
    return parser.getStatusCode() != 401 && parser.getStatusCode() != 407;
}

//  from src/network/access/qhttpnetworkrequest.cpp, line 23, as _ZN26QHttpNetworkRequestPrivateC1ERKS_
inline QHttpNetworkRequestPrivate::QHttpNetworkRequestPrivate(const QHttpNetworkRequestPrivate &other) // = default
    : QHttpNetworkHeaderPrivate(other),
      operation(other.operation),
      customVerb(other.customVerb),
      fullLocalServerName(other.fullLocalServerName),
      priority(other.priority),
      uploadByteDevice(other.uploadByteDevice),
      autoDecompress(other.autoDecompress),
      pipeliningAllowed(other.pipeliningAllowed),
      http2Allowed(other.http2Allowed),
      http2Direct(other.http2Direct),
      h2cAllowed(other.h2cAllowed),
      withCredentials(other.withCredentials),
      ssl(other.ssl),
      preConnect(other.preConnect),
      needResendWithCredentials(other.needResendWithCredentials),
      redirectCount(other.redirectCount),
      redirectPolicy(other.redirectPolicy),
      peerVerifyName(other.peerVerifyName)
{
}

//  from src/network/access/qhttpnetworkrequest.cpp, line 45, as _ZN26QHttpNetworkRequestPrivateD1Ev
inline QHttpNetworkRequestPrivate::~QHttpNetworkRequestPrivate()
{
}

//  from src/network/access/qhttpnetworkconnectionchannel.cpp, line 186, as _ZN29QHttpNetworkConnectionChannel5closeEv
inline void QHttpNetworkConnectionChannel::close()
{
    if (state == QHttpNetworkConnectionChannel::ClosingState)
        return;

    if (!socket)
        state = QHttpNetworkConnectionChannel::IdleState;
    else if (QSocketAbstraction::socketState(socket) == QAbstractSocket::UnconnectedState)
        state = QHttpNetworkConnectionChannel::IdleState;
    else
        state = QHttpNetworkConnectionChannel::ClosingState;

    // pendingEncrypt must only be true in between connected and encrypted states
    pendingEncrypt = false;

    if (socket) {
        // socket can be 0 since the host lookup is done from qhttpnetworkconnection.cpp while
        // there is no socket yet.
        socket->close();
    }
}

//  from src/network/access/qhttp2protocolhandler.cpp, line 150, as _ZN21QHttp2ProtocolHandler23handleConnectionClosureEv
inline void QHttp2ProtocolHandler::handleConnectionClosure()
{
    // The channel has just received RemoteHostClosedError and since it will
    // not try (for HTTP/2) to re-connect, it's time to finish all replies
    // with error.

    // Maybe we still have some data to read and can successfully finish
    // a stream/request?
    _q_receiveReply();
    h2Connection->handleConnectionClosure();
}

//  from src/network/access/qhttp2protocolhandler.cpp, line 145, as _ZNK21QHttp2ProtocolHandler11isGoingAwayEv
inline bool QHttp2ProtocolHandler::isGoingAway() const noexcept
{
    return h2Connection && h2Connection->isGoingAway();
}

//  from src/network/access/qhttp2protocolhandler.cpp, line 169, as _ZN21QHttp2ProtocolHandler12_q_readyReadEv
inline void QHttp2ProtocolHandler::_q_readyRead()
{
    _q_receiveReply();
}

//  from src/network/access/qhttp2protocolhandler.cpp, line 174, as _ZN21QHttp2ProtocolHandler15_q_receiveReplyEv
inline void QHttp2ProtocolHandler::_q_receiveReply()
{
    // not using QObject::connect because the QHttpNetworkConnectionChannel
    // already handles the signals we care about, so we just call the slot
    // directly.
    Q_ASSERT(h2Connection);
    h2Connection->handleReadyRead();
}

//  from src/network/access/qhttp2protocolhandler.cpp, line 266, as _ZN21QHttp2ProtocolHandler14tryRemoveReplyEP17QHttpNetworkReply
inline bool QHttp2ProtocolHandler::tryRemoveReply(QHttpNetworkReply *reply)
{
    QHttp2Stream *stream = streamIDs.take(reply);
    if (stream) {
        stream->sendRST_STREAM(stream->isUploadingDATA() ? Http2::CANCEL : Http2::HTTP2_NO_ERROR);
        clearStreamState(stream);
        stream->deleteLater();
        return true;
    }
    return false;
}

//  from src/network/access/qhttp2protocolhandler.cpp, line 298, as _ZN21QHttp2ProtocolHandler8sendDATAEP12QHttp2StreamP17QHttpNetworkReply
inline bool QHttp2ProtocolHandler::sendDATA(QHttp2Stream *stream, QHttpNetworkReply *reply)
{
    Q_ASSERT(reply);
    QHttpNetworkReplyPrivate *replyPrivate = reply->d_func();
    Q_ASSERT(replyPrivate);
    QHttpNetworkRequest &request = replyPrivate->request;
    Q_ASSERT(request.uploadByteDevice());

    bool startedSending = stream->sendDATA(request.uploadByteDevice(), true);
    return startedSending && !stream->wasReset();
}

//  from src/network/access/qhttp2protocolhandler.cpp, line 761, as _ZN21QHttp2ProtocolHandler12closeSessionEv
inline void QHttp2ProtocolHandler::closeSession()
{
    m_channel->close();
}
//  -----------------------------------------------------------------------

//  const QMetaObject *QHttp2ProtocolHandler::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21QHttp2ProtocolHandler10metaObjectEv(
    const QHttp2ProtocolHandler *self) {
  return self->metaObject();
}

//  void QHttp2ProtocolHandler::handleConnectionClosure()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QHttp2ProtocolHandler23handleConnectionClosureEv(
    QHttp2ProtocolHandler *self) {
  self->handleConnectionClosure();
}

//  bool QHttp2ProtocolHandler::isGoingAway() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QHttp2ProtocolHandler11isGoingAwayEv(
    const QHttp2ProtocolHandler *self) {
  return self->isGoingAway();
}

//  void QHttp2ProtocolHandler::_q_readyRead()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QHttp2ProtocolHandler12_q_readyReadEv(
    QHttp2ProtocolHandler *self) {
  self->_q_readyRead();
}

//  void QHttp2ProtocolHandler::_q_receiveReply()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QHttp2ProtocolHandler15_q_receiveReplyEv(
    QHttp2ProtocolHandler *self) {
  self->_q_receiveReply();
}

//  bool QHttp2ProtocolHandler::tryRemoveReply(QHttpNetworkReply *reply)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QHttp2ProtocolHandler14tryRemoveReplyEP17QHttpNetworkReply(
    QHttp2ProtocolHandler *self,
    QHttpNetworkReply *reply) {
  return self->tryRemoveReply(reply);
}

//  bool QHttp2ProtocolHandler::sendDATA(QHttp2Stream *stream,
//      QHttpNetworkReply *reply)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QHttp2ProtocolHandler8sendDATAEP12QHttp2StreamP17QHttpNetworkReply(
    QHttp2ProtocolHandler *self,
    QHttp2Stream *stream,
    QHttpNetworkReply *reply) {
  return self->sendDATA(stream, reply);
}

//  void QHttp2ProtocolHandler::closeSession()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QHttp2ProtocolHandler12closeSessionEv(
    QHttp2ProtocolHandler *self) {
  self->closeSession();
}

//  QHttp2ProtocolHandler as the QAbstractProtocolHandler it is built on
extern "C" Q_DECL_EXPORT
QAbstractProtocolHandler *ritual_cast_QHttp2ProtocolHandler_QAbstractProtocolHandler(
    QHttp2ProtocolHandler *self) {
  return static_cast<QAbstractProtocolHandler *>(self);
}

//  void QHttp2ProtocolHandler::_q_readyRead()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QHttp2ProtocolHandler12_q_readyReadEv(
    QHttp2ProtocolHandler *self) {
  self->QHttp2ProtocolHandler::_q_readyRead();
}

//  void QHttp2ProtocolHandler::_q_receiveReply()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QHttp2ProtocolHandler15_q_receiveReplyEv(
    QHttp2ProtocolHandler *self) {
  self->QHttp2ProtocolHandler::_q_receiveReply();
}

#endif  // QT_CONFIG(http)
