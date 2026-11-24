//  Written by dev_tooling.RitualGenerator from the records of
//  QtCoap/6.12.0/QtCoap/private/qcoapprotocol_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCoap/QtCoap>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCoap/6.12.0/QtCoap/private/qcoapprotocol_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qcoapinternalmessage_p.h"
#include "qcoaprequest_p.h"
#include <QtCoap/qcoaprequest.h>
#include <QtCore/qloggingcategory.h>
#include "qcoapnamespace_p.h"
#include "qcoapinternalreply_p.h"
#include <QtCore/qendian.h>
#include <QtCore/qmath.h>
#include <memory>
#include "qcoaprequest.h"
#include "qcoapinternalrequest_p.h"
#include <QtCore/qmath.h>
#include <QtCore/qrandom.h>
#include <QtCore/qregularexpression.h>
#include <QtCore/qloggingcategory.h>
#include <QtNetwork/QHostAddress>
#include "qcoapprotocol_p.h"
#include "qcoapinternalrequest_p.h"
#include "qcoapinternalreply_p.h"
#include "qcoaprequest_p.h"
#include "qcoapconnection_p.h"
#include "qcoapnamespace_p.h"
#include <QtCore/qrandom.h>
#include <QtCore/qthread.h>
#include <QtCore/qloggingcategory.h>
#include <QtNetwork/qnetworkdatagram.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtcoap/src/coap/qcoapinternalmessage.cpp, line 163, as _ZN20QCoapInternalMessage7messageEv
inline QCoapMessage *QCoapInternalMessage::message()
{
    Q_D(QCoapInternalMessage);
    return &(d->message);
}

//  from ../qtcoap/src/coap/qcoapnamespace.cpp, line 283, as _ZN6QtCoap15randomGeneratorEv
inline QRandomGenerator &QtCoap::randomGenerator()
{
    static QRandomGenerator randomGenerator = QRandomGenerator::securelySeeded();
    return randomGenerator;
}

//  from ../qtcoap/src/coap/qcoapinternalreply.cpp, line 55, as _ZN18QCoapInternalReply15createFromFrameERK10QByteArrayP7QObject
inline QCoapInternalReply *QCoapInternalReply::createFromFrame(const QByteArray &reply, QObject *parent)
{
    // A CoAP message is at least 4 bytes long
    if (reply.size() < 4)
        return nullptr;

    auto internalReply = std::make_unique<QCoapInternalReply>(parent);
    QCoapInternalReplyPrivate *d = internalReply->d_func();

    const quint8 *pduData = reinterpret_cast<const quint8 *>(reply.data());

    // Parse Header and Token
    d->message.setVersion((pduData[0] >> 6) & 0x03);
    d->message.setType(QCoapMessage::Type((pduData[0] >> 4) & 0x03));
    quint8 tokenLength = (pduData[0]) & 0x0F;

    // RFC 7252 §3: token lengths 9-15 are reserved and must be treated as a
    // message format error. Also reject a token whose bytes are not all present.
    if (tokenLength > 8 || 4 + tokenLength > reply.size())
        return nullptr;

    d->responseCode = static_cast<QtCoap::ResponseCode>(pduData[1]);
    d->message.setMessageId(static_cast<quint16>((static_cast<quint16>(pduData[2]) << 8)
                                                 | static_cast<quint16>(pduData[3])));
    d->message.setToken(reply.mid(4, tokenLength));

    // Parse Options
    qsizetype i = 4 + tokenLength;
    quint32 lastOptionNumber = 0;
    while (i < reply.size() && pduData[i] != 0xFF) {
        quint32 optionDelta = ((pduData[i] >> 4) & 0x0F);
        quint32 optionLength = (pduData[i] & 0x0F);

        // Delta value > 12 : special values
        if (optionDelta == 13) {
            if (++i >= reply.size())
                return nullptr;
            optionDelta = pduData[i] + 13;
        } else if (optionDelta == 14) {
            // RFC 7252 §3.1: nibble 14 is a 16-bit unsigned integer in network
            // byte order, giving the value minus 269.
            if (i >= reply.size() - 2)
                return nullptr;
            optionDelta = qFromBigEndian<quint16>(pduData + i + 1) + 269;
            i += 2;
        }

        // Delta length > 12 : special values
        if (optionLength == 13) {
            if (++i >= reply.size())
                return nullptr;
            optionLength = pduData[i] + 13;
        } else if (optionLength == 14) {
            // RFC 7252 §3.1: nibble 14 is a 16-bit unsigned integer in network
            // byte order, giving the value minus 269.
            if (i >= reply.size() - 2)
                return nullptr;
            optionLength = qFromBigEndian<quint16>(pduData + i + 1) + 269;
            i += 2;
        }

        // The option value is optionLength bytes following the current byte.
        // Reject the frame if it would run past the end of the buffer.
        if (i >= reply.size() - static_cast<qsizetype>(optionLength))
            return nullptr;

        quint32 optionNumber = lastOptionNumber + optionDelta;
        // RFC 7252: option numbers do not exceed 65535. A larger cumulative
        // number means a malformed frame; every following option would be out of
        // range too, so reject the whole reply.
        if (optionNumber > 65535)
            return nullptr;

        const QByteArray optionValue = reply.sliced(i + 1, optionLength);

        // Validate block options (RFC 7959 §2.2) before they are interpreted.
        if (optionNumber == QCoapOption::Block1 || optionNumber == QCoapOption::Block2) {
            // A block option value is 0-3 bytes. A longer value yields a block
            // number that overflows the 20-bit NUM field.
            if (optionValue.size() > 3)
                return nullptr;
            // SZX value 7 (block size 2048) is reserved; it is the low 3 bits of
            // the last byte. Accepting it yields a 2048-byte block size, which is illegal
            if (!optionValue.isEmpty()
                && (static_cast<quint8>(optionValue.back()) & 0x7) == 0x7) {
                return nullptr;
            }
        }

        internalReply->addOption(QCoapOption::OptionName(optionNumber), optionValue);
        lastOptionNumber = optionNumber;
        i += 1 + optionLength;
    }

    // Parse Payload
    if (i < reply.size() && pduData[i] == 0xFF) {
        // -1 because of 0xFF at the beginning
        QByteArray currentPayload = reply.mid(i + 1);
        d->message.setPayload(d->message.payload().append(currentPayload));
    }

    return internalReply.release();
}

//  from ../qtcoap/src/coap/qcoapinternalreply.cpp, line 185, as _ZN18QCoapInternalReply16setSenderAddressERK12QHostAddress
inline void QCoapInternalReply::setSenderAddress(const QHostAddress &address)
{
    Q_D(QCoapInternalReply);
    d->senderAddress = address;
}

//  from ../qtcoap/src/coap/qcoapinternalrequest.cpp, line 596, as _ZN20QCoapInternalRequest12setTargetUriE4QUrl
inline void QCoapInternalRequest::setTargetUri(QUrl targetUri)
{
    Q_D(QCoapInternalRequest);
    d->targetUri = targetUri;
}

//  from ../qtcoap/src/coap/qcoapinternalrequest.cpp, line 572, as _ZN20QCoapInternalRequest13setConnectionEP15QCoapConnection
inline void QCoapInternalRequest::setConnection(QCoapConnection *connection)
{
    Q_D(QCoapInternalRequest);
    d->connection = connection;
}

//  from ../qtcoap/src/coap/qcoapinternalrequest.cpp, line 83, as _ZN20QCoapInternalRequest16initEmptyMessageEtN12QCoapMessage4TypeE
inline void QCoapInternalRequest::initEmptyMessage(quint16 messageId, QCoapMessage::Type type)
{
    Q_D(QCoapInternalRequest);

    Q_ASSERT(type == QCoapMessage::Type::Acknowledgment || type == QCoapMessage::Type::Reset);

    setMethod(QtCoap::Method::Invalid);
    d->message.setType(type);
    d->message.setMessageId(messageId);
    d->message.setToken(QByteArray());
    d->message.setPayload(QByteArray());
    d->message.clearOptions();
}

//  from ../qtcoap/src/coap/qcoapinternalrequest.cpp, line 34, as _ZN20QCoapInternalRequestC1EP7QObject
inline QCoapInternalRequest::QCoapInternalRequest(QObject *parent) :
    QCoapInternalMessage(*new QCoapInternalRequestPrivate, parent)
{
    Q_D(QCoapInternalRequest);
    d->timeoutTimer = new QTimer(this);
    connect(d->timeoutTimer, &QTimer::timeout, this, [this]() { emit timeout(this); });

    d->maxTransmitWaitTimer = new QTimer(this);
    connect(d->maxTransmitWaitTimer, &QTimer::timeout, this,
            [this]() { emit maxTransmissionSpanReached(this); });

    d->multicastExpireTimer = new QTimer(this);
    connect(d->multicastExpireTimer, &QTimer::timeout, this,
            [this]() { emit multicastRequestExpired(this); });
}

//  from ../qtcoap/src/coap/qcoapinternalrequest.cpp, line 492, as _ZNK20QCoapInternalRequest10connectionEv
inline QCoapConnection *QCoapInternalRequest::connection() const
{
    Q_D(const QCoapInternalRequest);
    return d->connection;
}

//  from ../qtcoap/src/coap/qcoapinternalrequest.cpp, line 416, as _ZNK20QCoapInternalRequest5tokenEv
inline QCoapToken QCoapInternalRequest::token() const
{
    return message()->token();
}

//  from ../qtcoap/src/coap/qcoapinternalrequest.cpp, line 480, as _ZNK20QCoapInternalRequest9targetUriEv
inline QUrl QCoapInternalRequest::targetUri() const
{
    Q_D(const QCoapInternalRequest);
    return d->targetUri;
}

//  from ../qtcoap/src/coap/qcoapinternalrequest.cpp, line 461, as _ZN20QCoapInternalRequest16stopTransmissionEv
inline void QCoapInternalRequest::stopTransmission()
{
    Q_D(QCoapInternalRequest);
    if (isMulticast()) {
        d->multicastExpireTimer->stop();
    } else {
        d->transmissionInProgress = false;
        d->retransmissionCounter = 0;
        d->maxTransmitWaitTimer->stop();
        d->timeoutTimer->stop();
    }
}

//  from ../qtcoap/src/coap/qcoapinternalreply.cpp, line 32, as _ZN18QCoapInternalReplyC1EP7QObject
inline QCoapInternalReply::QCoapInternalReply(QObject *parent) :
    QCoapInternalMessage(*new QCoapInternalReplyPrivate, parent)
{
}

//  from ../qtcoap/src/coap/qcoapinternalmessage.cpp, line 174, as _ZNK20QCoapInternalMessage7messageEv
inline const QCoapMessage *QCoapInternalMessage::message() const
{
    Q_D(const QCoapInternalMessage);
    return &(d->message);
}

//  from ../qtcoap/src/coap/qcoapinternalrequest.cpp, line 538, as _ZNK20QCoapInternalRequest11isMulticastEv
inline bool QCoapInternalRequest::isMulticast() const
{
    const QHostAddress hostAddress(targetUri().host());
    return hostAddress.isMulticast();
}

//  from ../qtcoap/src/coap/qcoapprotocol.cpp, line 660, as _ZNK20QCoapProtocolPrivate23generateUniqueMessageIdEv
inline quint16 QCoapProtocolPrivate::generateUniqueMessageId() const
{
    // TODO: Optimize message id generation for large sets
    // TODO: Store used message id for the period specified by CoAP spec
    quint16 id = 0;
    while (isMessageIdRegistered(id))
        id = static_cast<quint16>(QtCoap::randomGenerator().bounded(0x10000));

    return id;
}

//  from ../qtcoap/src/coap/qcoapprotocol.cpp, line 676, as _ZNK20QCoapProtocolPrivate19generateUniqueTokenEv
inline QCoapToken QCoapProtocolPrivate::generateUniqueToken() const
{
    // TODO: Optimize token generation for large sets
    // TODO: Store used token for the period specified by CoAP spec
    QCoapToken token;
    while (isTokenRegistered(token)) {
        quint8 length = static_cast<quint8>(QtCoap::randomGenerator().bounded(minimumTokenSize, 9));
        token.resize(length);
        quint8 *tokenData = reinterpret_cast<quint8 *>(token.data());
        for (int i = 0; i < token.size(); ++i)
            tokenData[i] = static_cast<quint8>(QtCoap::randomGenerator().bounded(256));
    }

    return token;
}

//  from ../qtcoap/src/coap/qcoapprotocol.cpp, line 716, as _ZN20QCoapProtocolPrivate16onRequestAbortedERK10QByteArray
inline void QCoapProtocolPrivate::onRequestAborted(const QCoapToken &token)
{
    QCoapInternalRequest *request = requestForToken(token);
    if (!request)
        return;

    request->stopTransmission();
    forgetExchange(request);
}

//  from ../qtcoap/src/coap/qcoapprotocol.cpp, line 867, as _ZNK20QCoapProtocolPrivate21isMessageIdRegisteredEt
inline bool QCoapProtocolPrivate::isMessageIdRegistered(quint16 id) const
{
    // Reserved for uninitialized message Id
    if (id == 0)
        return true;

    for (auto it = exchangeMap.constBegin(); it != exchangeMap.constEnd(); ++it) {
        if (it->request->message()->messageId() == id)
            return true;
    }

    return false;
}

//  from ../qtcoap/src/coap/qcoapprotocol.cpp, line 836, as _ZNK20QCoapProtocolPrivate17isTokenRegisteredERK10QByteArray
inline bool QCoapProtocolPrivate::isTokenRegistered(const QCoapToken &token) const
{
    // Reserved for empty messages and uninitialized tokens
    if (token == QByteArray())
        return true;

    return exchangeMap.contains(token);
}

//  from ../qtcoap/src/coap/qcoapprotocol.cpp, line 851, as _ZNK20QCoapProtocolPrivate19isRequestRegisteredEPK20QCoapInternalRequest
inline bool QCoapProtocolPrivate::isRequestRegistered(const QCoapInternalRequest *request) const
{
    for (auto it = exchangeMap.constBegin(); it != exchangeMap.constEnd(); ++it) {
        if (it->request.data() == request)
            return true;
    }

    return false;
}

//  from ../qtcoap/src/coap/qcoapprotocol.cpp, line 397, as _ZNK20QCoapProtocolPrivate15requestForTokenERK10QByteArray
inline QCoapInternalRequest *QCoapProtocolPrivate::requestForToken(const QCoapToken &token) const
{
    auto it = exchangeMap.find(token);
    if (it != exchangeMap.constEnd())
        return it->request.data();

    return nullptr;
}

//  from ../qtcoap/src/coap/qcoapprotocol.cpp, line 440, as _ZNK20QCoapProtocolPrivate17lastReplyForTokenERK10QByteArray
inline QCoapInternalReply *QCoapProtocolPrivate::lastReplyForToken(const QCoapToken &token) const
{
    auto it = exchangeMap.find(token);
    if (it != exchangeMap.constEnd())
        return it->replies.last().data();

    return nullptr;
}

//  from ../qtcoap/src/coap/qcoapprotocol.cpp, line 469, as _ZNK20QCoapProtocolPrivate22findRequestByMessageIdEt
inline QCoapInternalRequest *QCoapProtocolPrivate::findRequestByMessageId(quint16 messageId) const
{
    for (auto it = exchangeMap.constBegin(); it != exchangeMap.constEnd(); ++it) {
        if (it->request->message()->messageId() == messageId)
            return it->request.data();
    }

    return nullptr;
}

//  from ../qtcoap/src/coap/qcoapprotocol.cpp, line 454, as _ZNK20QCoapProtocolPrivate22findRequestByUserReplyEPK10QCoapReply
inline QCoapInternalRequest *QCoapProtocolPrivate::findRequestByUserReply(const QCoapReply *reply) const
{
    for (auto it = exchangeMap.constBegin(); it != exchangeMap.constEnd(); ++it) {
        if (it->userReply == reply)
            return it->request.data();
    }

    return nullptr;
}

//  from ../qtcoap/src/coap/qcoapprotocol.cpp, line 798, as _ZN20QCoapProtocolPrivate14forgetExchangeERK10QByteArray
inline bool QCoapProtocolPrivate::forgetExchange(const QCoapToken &token)
{
    return exchangeMap.remove(token) > 0;
}

//  from ../qtcoap/src/coap/qcoapprotocol.cpp, line 810, as _ZN20QCoapProtocolPrivate14forgetExchangeEPK20QCoapInternalRequest
inline bool QCoapProtocolPrivate::forgetExchange(const QCoapInternalRequest *request)
{
    return forgetExchange(request->token());
}

//  from ../qtcoap/src/coap/qcoapprotocol.cpp, line 820, as _ZN20QCoapProtocolPrivate21forgetExchangeRepliesERK10QByteArray
inline bool QCoapProtocolPrivate::forgetExchangeReplies(const QCoapToken &token)
{
    auto it = exchangeMap.find(token);
    if (it == exchangeMap.end())
        return false;

    it->replies.clear();
    return true;
}
//  -----------------------------------------------------------------------

//  QCoapProtocolPrivate::QCoapProtocolPrivate()
extern "C" Q_DECL_EXPORT
QCoapProtocolPrivate *ritual_ZN20QCoapProtocolPrivateC1Ev() {
  return new QCoapProtocolPrivate();
}

//  quint16 QCoapProtocolPrivate::generateUniqueMessageId() const
extern "C" Q_DECL_EXPORT
quint16 ritual_ZNK20QCoapProtocolPrivate23generateUniqueMessageIdEv(
    const QCoapProtocolPrivate *self) {
  return self->generateUniqueMessageId();
}

//  QCoapToken QCoapProtocolPrivate::generateUniqueToken() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK20QCoapProtocolPrivate19generateUniqueTokenEv(
    const QCoapProtocolPrivate *self) {
  return new QByteArray(self->generateUniqueToken());
}

//  void QCoapProtocolPrivate::onRequestAborted(const QCoapToken &token)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QCoapProtocolPrivate16onRequestAbortedERK10QByteArray(
    QCoapProtocolPrivate *self,
    const QByteArray *token) {
  self->onRequestAborted(*token);
}

//  bool QCoapProtocolPrivate::isMessageIdRegistered(quint16 id) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QCoapProtocolPrivate21isMessageIdRegisteredEt(
    const QCoapProtocolPrivate *self,
    quint16 id) {
  return self->isMessageIdRegistered(id);
}

//  bool QCoapProtocolPrivate::isTokenRegistered(const QCoapToken &token)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QCoapProtocolPrivate17isTokenRegisteredERK10QByteArray(
    const QCoapProtocolPrivate *self,
    const QByteArray *token) {
  return self->isTokenRegistered(*token);
}

//  bool QCoapProtocolPrivate::isRequestRegistered(const QCoapInternalRequest
//      *request) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QCoapProtocolPrivate19isRequestRegisteredEPK20QCoapInternalRequest(
    const QCoapProtocolPrivate *self,
    const QCoapInternalRequest *request) {
  return self->isRequestRegistered(request);
}

//  QCoapInternalRequest *QCoapProtocolPrivate::requestForToken(const
//      QCoapToken &token) const
extern "C" Q_DECL_EXPORT
QCoapInternalRequest *ritual_ZNK20QCoapProtocolPrivate15requestForTokenERK10QByteArray(
    const QCoapProtocolPrivate *self,
    const QByteArray *token) {
  return self->requestForToken(*token);
}

//  QCoapInternalReply *QCoapProtocolPrivate::lastReplyForToken(const
//      QCoapToken &token) const
extern "C" Q_DECL_EXPORT
QCoapInternalReply *ritual_ZNK20QCoapProtocolPrivate17lastReplyForTokenERK10QByteArray(
    const QCoapProtocolPrivate *self,
    const QByteArray *token) {
  return self->lastReplyForToken(*token);
}

//  QCoapInternalRequest
//      *QCoapProtocolPrivate::findRequestByMessageId(quint16 messageId)
//      const
extern "C" Q_DECL_EXPORT
QCoapInternalRequest *ritual_ZNK20QCoapProtocolPrivate22findRequestByMessageIdEt(
    const QCoapProtocolPrivate *self,
    quint16 messageId) {
  return self->findRequestByMessageId(messageId);
}

//  QCoapInternalRequest *QCoapProtocolPrivate::findRequestByUserReply(const
//      QCoapReply *reply) const
extern "C" Q_DECL_EXPORT
QCoapInternalRequest *ritual_ZNK20QCoapProtocolPrivate22findRequestByUserReplyEPK10QCoapReply(
    const QCoapProtocolPrivate *self,
    const QCoapReply *reply) {
  return self->findRequestByUserReply(reply);
}

//  bool QCoapProtocolPrivate::forgetExchange(const QCoapToken &token)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QCoapProtocolPrivate14forgetExchangeERK10QByteArray(
    QCoapProtocolPrivate *self,
    const QByteArray *token) {
  return self->forgetExchange(*token);
}

//  bool QCoapProtocolPrivate::forgetExchange(const QCoapInternalRequest
//      *request)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QCoapProtocolPrivate14forgetExchangeEPK20QCoapInternalRequest(
    QCoapProtocolPrivate *self,
    const QCoapInternalRequest *request) {
  return self->forgetExchange(request);
}

//  bool QCoapProtocolPrivate::forgetExchangeReplies(const QCoapToken &token)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QCoapProtocolPrivate21forgetExchangeRepliesERK10QByteArray(
    QCoapProtocolPrivate *self,
    const QByteArray *token) {
  return self->forgetExchangeReplies(*token);
}

//  QCoapProtocol *QCoapProtocolPrivate::q_func()
extern "C" Q_DECL_EXPORT
QCoapProtocol *ritual_ZN20QCoapProtocolPrivate6q_funcEv(
    QCoapProtocolPrivate *self) {
  return self->q_func();
}

//  const QCoapProtocol *QCoapProtocolPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QCoapProtocol *ritual_ZNK20QCoapProtocolPrivate6q_funcEv(
    const QCoapProtocolPrivate *self) {
  return self->q_func();
}
