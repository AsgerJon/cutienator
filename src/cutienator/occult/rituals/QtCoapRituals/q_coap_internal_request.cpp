//  Written by dev_tooling.RitualGenerator from the records of
//  QtCoap/6.12.0/QtCoap/private/qcoapinternalrequest_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCoap/QtCoap>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCoap/6.12.0/QtCoap/private/qcoapinternalrequest_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtCoap/qcoapoption.h>
#include <QtCore/qurl.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCoap/private/qcoapinternalmessage_p.h>
#include <QtCoap/private/qcoaprequest_p.h>
#include <QtCoap/qcoaprequest.h>
#include <QtCore/qloggingcategory.h>
#include <QtCoap/qcoaprequest.h>
#include <QtCoap/private/qcoapinternalrequest_p.h>
#include <QtCore/qmath.h>
#include <QtCore/qrandom.h>
#include <QtCore/qregularexpression.h>
#include <QtCore/qloggingcategory.h>
#include <QtNetwork/QHostAddress>
#include <QtCoap/private/qcoaprequest_p.h>
#include <QtCore/qmath.h>
#include <QtCore/qdatetime.h>
#include <QtCore/qloggingcategory.h>
#include <QtCore/QDebug>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from ../qtcoap/src/coap/qcoapinternalrequest.cpp, line 101, as local:qcoapinternalrequest.cpp:appendByte
template<typename T>
static void appendByte(QByteArray *buffer, T value) {
    buffer->append(static_cast<char>(value));
}

//  from ../qtcoap/src/coap/qcoaprequest.cpp, line 18, as local:qcoaprequest.cpp:CoapScheme
namespace {
const auto CoapScheme = QLatin1String("coap");
}  // namespace

//  from ../qtcoap/src/coap/qcoaprequest.cpp, line 19, as local:qcoaprequest.cpp:CoapSecureScheme
namespace {
const auto CoapSecureScheme = QLatin1String("coaps");
}  // namespace

//  from ../qtcoap/src/coap/qcoapinternalmessage.cpp, line 232, as _ZN20QCoapInternalMessage10isUrlValidERK4QUrl
inline bool QCoapInternalMessage::isUrlValid(const QUrl &url)
{
    return QCoapRequestPrivate::isUrlValid(url);
}

//  from ../qtcoap/src/coap/qcoapinternalmessage.cpp, line 14, as _Z14lcCoapExchangev
inline const QLoggingCategory &lcCoapExchange()
{
    static const QLoggingCategory category("qt.coap.exchange");
    return category;
}

//  from ../qtcoap/src/coap/qcoapinternalrequest.cpp, line 271, as _ZNK20QCoapInternalRequest11blockOptionEN11QCoapOption10OptionNameEjj
inline QCoapOption QCoapInternalRequest::blockOption(QCoapOption::OptionName name, uint blockNumber, uint blockSize) const
{
    Q_D(const QCoapInternalRequest);

    Q_ASSERT((blockSize & (blockSize - 1)) == 0); // is a power of two
    Q_ASSERT(!(blockSize >> 11)); // blockSize <= 1024

    // NUM field: the relative number of the block within a sequence of blocks
    // 4, 12 or 20 bits (as little as possible)
    Q_ASSERT(!(blockNumber >> 20)); // Fits in 20 bits
    quint32 optionData = (blockNumber << 4);

    // SZX field: the size of the block
    // 3 bits, set to "log2(blockSize) - 4"
    optionData |= (blockSize >> 7)
                  ? ((blockSize >> 10) ? 6 : (3 + (blockSize >> 8)))
                  : (blockSize >> 5);

    // M field: whether more blocks are following
    // 1 bit
    if (name == QCoapOption::Block1
            && static_cast<int>((blockNumber + 1) * blockSize) < d->fullPayload.size()) {
        optionData |= 8;
    }

    QByteArray optionValue;
    Q_ASSERT(!(optionData >> 24));
    if (optionData > 0xFFFF)
        appendByte(&optionValue, optionData >> 16);
    if (optionData > 0xFF)
        appendByte(&optionValue, (optionData >> 8) & 0xFF);
    appendByte(&optionValue, optionData & 0xFF);

    return QCoapOption(name, optionValue);
}

//  from ../qtcoap/src/coap/qcoapinternalmessage.cpp, line 174, as _ZNK20QCoapInternalMessage7messageEv
inline const QCoapMessage *QCoapInternalMessage::message() const
{
    Q_D(const QCoapInternalMessage);
    return &(d->message);
}

//  from ../qtcoap/src/coap/qcoapinternalrequest.cpp, line 70, as _ZNK20QCoapInternalRequest7isValidEv
inline bool QCoapInternalRequest::isValid() const
{
    Q_D(const QCoapInternalRequest);
    return isUrlValid(d->targetUri) && d->method != QtCoap::Method::Invalid;
}

//  from ../qtcoap/src/coap/qcoapinternalrequest.cpp, line 331, as _ZN20QCoapInternalRequest9addOptionERK11QCoapOption
inline void QCoapInternalRequest::addOption(const QCoapOption &option)
{
    if (option.name() == QCoapOption::Block1)
        setFromDescriptiveBlockOption(option);

    QCoapInternalMessage::addOption(option);
}

//  from ../qtcoap/src/coap/qcoaprequest.cpp, line 236, as _ZN19QCoapRequestPrivate10isUrlValidERK4QUrl
inline bool QCoapRequestPrivate::isUrlValid(const QUrl &url)
{
    return (url.isValid() && !url.isLocalFile() && !url.isRelative()
            && (url.scheme() == CoapScheme || url.scheme() == CoapSecureScheme)
            && !url.hasFragment());
}

//  from ../qtcoap/src/coap/qcoapinternalmessage.cpp, line 87, as _ZN20QCoapInternalMessage29setFromDescriptiveBlockOptionERK11QCoapOption
inline void QCoapInternalMessage::setFromDescriptiveBlockOption(const QCoapOption &option)
{
    Q_D(QCoapInternalMessage);

    const auto value = option.opaqueValue();
    const quint8 *optionData = reinterpret_cast<const quint8 *>(value.data());

    // A zero-length block option is valid and encodes NUM=0, M=0, SZX=0
    // (RFC 7959 §2.2). Treat the absent last byte as 0 instead of reading
    // optionData[-1]; the loop below is then skipped and every field resolves to 0.
    const quint8 lastByte = option.length() > 0 ? optionData[option.length() - 1] : 0;
    quint32 blockNumber = 0;

    for (int i = 0; i < option.length() - 1; ++i)
        blockNumber = (blockNumber << 8) | optionData[i];

    blockNumber = (blockNumber << 4) | (lastByte >> 4);
    d->currentBlockNumber = blockNumber;
    d->hasNextBlock = ((lastByte & 0x8) == 0x8);
    d->blockSize = static_cast<uint>(1u << ((lastByte & 0x7) + 4));

    if (d->blockSize > 1024)
        qCWarning(lcCoapExchange, "Received a block size larger than 1024, something may be wrong.");
}

//  from ../qtcoap/src/coap/qcoapinternalmessage.cpp, line 141, as _ZN20QCoapInternalMessage9addOptionERK11QCoapOption
inline void QCoapInternalMessage::addOption(const QCoapOption &option)
{
    Q_D(QCoapInternalMessage);
    d->message.addOption(option);
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

//  from ../qtcoap/src/coap/qcoapinternalrequest.cpp, line 311, as _ZN20QCoapInternalRequest12setMessageIdEt
inline void QCoapInternalRequest::setMessageId(quint16 id)
{
    Q_D(QCoapInternalRequest);
    d->message.setMessageId(id);
}

//  from ../qtcoap/src/coap/qcoapinternalrequest.cpp, line 321, as _ZN20QCoapInternalRequest8setTokenERK10QByteArray
inline void QCoapInternalRequest::setToken(const QCoapToken &token)
{
    Q_D(QCoapInternalRequest);
    d->message.setToken(token);
}

//  from ../qtcoap/src/coap/qcoapinternalrequest.cpp, line 213, as _ZN20QCoapInternalRequest17setToRequestBlockEjj
inline void QCoapInternalRequest::setToRequestBlock(uint blockNumber, uint blockSize)
{
    Q_D(QCoapInternalRequest);

    if (!checkBlockNumber(blockNumber))
        return;

    d->message.removeOption(QCoapOption::Block1);
    d->message.removeOption(QCoapOption::Block2);

    addOption(blockOption(QCoapOption::Block2, blockNumber, blockSize));
}

//  from ../qtcoap/src/coap/qcoapinternalrequest.cpp, line 233, as _ZN20QCoapInternalRequest14setToSendBlockEjj
inline void QCoapInternalRequest::setToSendBlock(uint blockNumber, uint blockSize)
{
    Q_D(QCoapInternalRequest);

    if (!checkBlockNumber(blockNumber))
        return;

    d->message.setPayload(d->fullPayload.mid(static_cast<int>(blockNumber * blockSize),
                                             static_cast<int>(blockSize)));
    d->message.removeOption(QCoapOption::Block1);

    addOption(blockOption(QCoapOption::Block1, blockNumber, blockSize));
}

//  from ../qtcoap/src/coap/qcoapinternalrequest.cpp, line 252, as _ZN20QCoapInternalRequest16checkBlockNumberEj
inline bool QCoapInternalRequest::checkBlockNumber(uint blockNumber)
{
    if (blockNumber >> 20) {
        qCWarning(lcCoapExchange) << "Block number" << blockNumber
                                  << "is too large. It should fit in 20 bits.";
        return false;
    }

    return true;
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

//  from ../qtcoap/src/coap/qcoapinternalrequest.cpp, line 504, as _ZNK20QCoapInternalRequest6methodEv
inline QtCoap::Method QCoapInternalRequest::method() const
{
    Q_D(const QCoapInternalRequest);
    return d->method;
}

//  from ../qtcoap/src/coap/qcoapinternalrequest.cpp, line 515, as _ZNK20QCoapInternalRequest9isObserveEv
inline bool QCoapInternalRequest::isObserve() const
{
    Q_D(const QCoapInternalRequest);
    return d->message.hasOption(QCoapOption::Observe);
}

//  from ../qtcoap/src/coap/qcoapinternalrequest.cpp, line 527, as _ZNK20QCoapInternalRequest18isObserveCancelledEv
inline bool QCoapInternalRequest::isObserveCancelled() const
{
    Q_D(const QCoapInternalRequest);
    return d->observeCancelled;
}

//  from ../qtcoap/src/coap/qcoapinternalrequest.cpp, line 538, as _ZNK20QCoapInternalRequest11isMulticastEv
inline bool QCoapInternalRequest::isMulticast() const
{
    const QHostAddress hostAddress(targetUri().host());
    return hostAddress.isMulticast();
}

//  from ../qtcoap/src/coap/qcoapinternalrequest.cpp, line 492, as _ZNK20QCoapInternalRequest10connectionEv
inline QCoapConnection *QCoapInternalRequest::connection() const
{
    Q_D(const QCoapInternalRequest);
    return d->connection;
}

//  from ../qtcoap/src/coap/qcoapinternalrequest.cpp, line 548, as _ZNK20QCoapInternalRequest21retransmissionCounterEv
inline uint QCoapInternalRequest::retransmissionCounter() const
{
    Q_D(const QCoapInternalRequest);
    return d->retransmissionCounter;
}

//  from ../qtcoap/src/coap/qcoapinternalrequest.cpp, line 560, as _ZN20QCoapInternalRequest9setMethodEN6QtCoap6MethodE
inline void QCoapInternalRequest::setMethod(QtCoap::Method method)
{
    Q_D(QCoapInternalRequest);
    d->method = method;
}

//  from ../qtcoap/src/coap/qcoapinternalrequest.cpp, line 572, as _ZN20QCoapInternalRequest13setConnectionEP15QCoapConnection
inline void QCoapInternalRequest::setConnection(QCoapConnection *connection)
{
    Q_D(QCoapInternalRequest);
    d->connection = connection;
}

//  from ../qtcoap/src/coap/qcoapinternalrequest.cpp, line 584, as _ZN20QCoapInternalRequest19setObserveCancelledEv
inline void QCoapInternalRequest::setObserveCancelled()
{
    Q_D(QCoapInternalRequest);
    d->observeCancelled = true;
}

//  from ../qtcoap/src/coap/qcoapinternalrequest.cpp, line 596, as _ZN20QCoapInternalRequest12setTargetUriE4QUrl
inline void QCoapInternalRequest::setTargetUri(QUrl targetUri)
{
    Q_D(QCoapInternalRequest);
    d->targetUri = targetUri;
}

//  from ../qtcoap/src/coap/qcoapinternalrequest.cpp, line 609, as _ZN20QCoapInternalRequest10setTimeoutEj
inline void QCoapInternalRequest::setTimeout(uint timeout)
{
    Q_D(QCoapInternalRequest);
    d->timeout = timeout;
}

//  from ../qtcoap/src/coap/qcoapinternalrequest.cpp, line 620, as _ZN20QCoapInternalRequest22setMaxTransmissionWaitEj
inline void QCoapInternalRequest::setMaxTransmissionWait(uint duration)
{
    Q_D(QCoapInternalRequest);
    d->maxTransmitWaitTimer->setInterval(static_cast<int>(duration));
}

//  from ../qtcoap/src/coap/qcoapinternalrequest.cpp, line 638, as _ZN20QCoapInternalRequest19setMulticastTimeoutEj
inline void QCoapInternalRequest::setMulticastTimeout(uint responseDelay)
{
    Q_D(QCoapInternalRequest);
    d->multicastExpireTimer->setInterval(static_cast<int>(responseDelay));
}

//  from ../qtcoap/src/coap/qcoapinternalrequest.cpp, line 427, as _ZN20QCoapInternalRequest19restartTransmissionEv
inline void QCoapInternalRequest::restartTransmission()
{
    Q_D(QCoapInternalRequest);

    if (!d->transmissionInProgress) {
        d->transmissionInProgress = true;
        d->maxTransmitWaitTimer->start();
    } else {
        d->retransmissionCounter++;
        d->timeout *= 2;
    }

    if (d->timeout > 0)
        d->timeoutTimer->start(static_cast<int>(d->timeout));
}

//  from ../qtcoap/src/coap/qcoapinternalrequest.cpp, line 448, as _ZN20QCoapInternalRequest26startMulticastTransmissionEv
inline void QCoapInternalRequest::startMulticastTransmission()
{
    Q_ASSERT(isMulticast());

    Q_D(QCoapInternalRequest);
    d->multicastExpireTimer->start();
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

//  from ../qtcoap/src/coap/qcoapinternalrequest.cpp, line 648, as _ZNK20QCoapInternalRequest13uriHostOptionERK4QUrl
inline QCoapOption QCoapInternalRequest::uriHostOption(const QUrl &uri) const
{
    QHostAddress address(uri.host());

    // No need for Uri-Host option with an IPv4 or IPv6 address
    if (!address.isNull())
        return QCoapOption();

    return QCoapOption(QCoapOption::UriHost, uri.host());
}
//  -----------------------------------------------------------------------

//  const QMetaObject *QCoapInternalRequest::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20QCoapInternalRequest10metaObjectEv(
    const QCoapInternalRequest *self) {
  return self->metaObject();
}

//  void *QCoapInternalRequest::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN20QCoapInternalRequest11qt_metacastEPKc(
    QCoapInternalRequest *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QCoapInternalRequest::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN20QCoapInternalRequest11qt_metacallEN11QMetaObject4CallEiPPv(
    QCoapInternalRequest *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  bool QCoapInternalRequest::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QCoapInternalRequest7isValidEv(
    const QCoapInternalRequest *self) {
  return self->isValid();
}

//  void QCoapInternalRequest::initEmptyMessage(quint16 messageId,
//      QCoapMessage::Type type)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QCoapInternalRequest16initEmptyMessageEtN12QCoapMessage4TypeE(
    QCoapInternalRequest *self,
    quint16 messageId,
    QCoapMessage::Type type) {
  self->initEmptyMessage(messageId, type);
}

//  void QCoapInternalRequest::setMessageId(quint16 a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QCoapInternalRequest12setMessageIdEt(
    QCoapInternalRequest *self,
    quint16 a0) {
  self->setMessageId(a0);
}

//  void QCoapInternalRequest::setToken(const QCoapToken &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QCoapInternalRequest8setTokenERK10QByteArray(
    QCoapInternalRequest *self,
    const QByteArray *a0) {
  self->setToken(*a0);
}

//  void QCoapInternalRequest::setToRequestBlock(uint blockNumber, uint
//      blockSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QCoapInternalRequest17setToRequestBlockEjj(
    QCoapInternalRequest *self,
    uint blockNumber,
    uint blockSize) {
  self->setToRequestBlock(blockNumber, blockSize);
}

//  void QCoapInternalRequest::setToSendBlock(uint blockNumber, uint
//      blockSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QCoapInternalRequest14setToSendBlockEjj(
    QCoapInternalRequest *self,
    uint blockNumber,
    uint blockSize) {
  self->setToSendBlock(blockNumber, blockSize);
}

//  bool QCoapInternalRequest::checkBlockNumber(uint blockNumber)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QCoapInternalRequest16checkBlockNumberEj(
    QCoapInternalRequest *self,
    uint blockNumber) {
  return self->checkBlockNumber(blockNumber);
}

//  void QCoapInternalRequest::addOption(const QCoapOption &option)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QCoapInternalRequest9addOptionERK11QCoapOption(
    QCoapInternalRequest *self,
    const QCoapOption *option) {
  self->addOption(*option);
}

//  QCoapToken QCoapInternalRequest::token() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK20QCoapInternalRequest5tokenEv(
    const QCoapInternalRequest *self) {
  return new QByteArray(self->token());
}

//  QUrl QCoapInternalRequest::targetUri() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK20QCoapInternalRequest9targetUriEv(
    const QCoapInternalRequest *self) {
  return new QUrl(self->targetUri());
}

//  QtCoap::Method QCoapInternalRequest::method() const
extern "C" Q_DECL_EXPORT
QtCoap::Method ritual_ZNK20QCoapInternalRequest6methodEv(
    const QCoapInternalRequest *self) {
  return self->method();
}

//  bool QCoapInternalRequest::isObserve() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QCoapInternalRequest9isObserveEv(
    const QCoapInternalRequest *self) {
  return self->isObserve();
}

//  bool QCoapInternalRequest::isObserveCancelled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QCoapInternalRequest18isObserveCancelledEv(
    const QCoapInternalRequest *self) {
  return self->isObserveCancelled();
}

//  bool QCoapInternalRequest::isMulticast() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QCoapInternalRequest11isMulticastEv(
    const QCoapInternalRequest *self) {
  return self->isMulticast();
}

//  QCoapConnection *QCoapInternalRequest::connection() const
extern "C" Q_DECL_EXPORT
QCoapConnection *ritual_ZNK20QCoapInternalRequest10connectionEv(
    const QCoapInternalRequest *self) {
  return self->connection();
}

//  uint QCoapInternalRequest::retransmissionCounter() const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK20QCoapInternalRequest21retransmissionCounterEv(
    const QCoapInternalRequest *self) {
  return self->retransmissionCounter();
}

//  void QCoapInternalRequest::setMethod(QtCoap::Method method)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QCoapInternalRequest9setMethodEN6QtCoap6MethodE(
    QCoapInternalRequest *self,
    QtCoap::Method method) {
  self->setMethod(method);
}

//  void QCoapInternalRequest::setConnection(QCoapConnection *connection)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QCoapInternalRequest13setConnectionEP15QCoapConnection(
    QCoapInternalRequest *self,
    QCoapConnection *connection) {
  self->setConnection(connection);
}

//  void QCoapInternalRequest::setObserveCancelled()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QCoapInternalRequest19setObserveCancelledEv(
    QCoapInternalRequest *self) {
  self->setObserveCancelled();
}

//  void QCoapInternalRequest::setTargetUri(QUrl targetUri)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QCoapInternalRequest12setTargetUriE4QUrl(
    QCoapInternalRequest *self,
    const QUrl *targetUri) {
  self->setTargetUri(*targetUri);
}

//  void QCoapInternalRequest::setTimeout(uint timeout)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QCoapInternalRequest10setTimeoutEj(
    QCoapInternalRequest *self,
    uint timeout) {
  self->setTimeout(timeout);
}

//  void QCoapInternalRequest::setMaxTransmissionWait(uint timeout)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QCoapInternalRequest22setMaxTransmissionWaitEj(
    QCoapInternalRequest *self,
    uint timeout) {
  self->setMaxTransmissionWait(timeout);
}

//  void QCoapInternalRequest::setMulticastTimeout(uint responseDelay)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QCoapInternalRequest19setMulticastTimeoutEj(
    QCoapInternalRequest *self,
    uint responseDelay) {
  self->setMulticastTimeout(responseDelay);
}

//  void QCoapInternalRequest::restartTransmission()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QCoapInternalRequest19restartTransmissionEv(
    QCoapInternalRequest *self) {
  self->restartTransmission();
}

//  void QCoapInternalRequest::startMulticastTransmission()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QCoapInternalRequest26startMulticastTransmissionEv(
    QCoapInternalRequest *self) {
  self->startMulticastTransmission();
}

//  void QCoapInternalRequest::stopTransmission()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QCoapInternalRequest16stopTransmissionEv(
    QCoapInternalRequest *self) {
  self->stopTransmission();
}

//  void QCoapInternalRequest::timeout(QCoapInternalRequest *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QCoapInternalRequest7timeoutEPS_(
    QCoapInternalRequest *self,
    QCoapInternalRequest *a0) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QCoapInternalRequest")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "timeout(QCoapInternalRequest *)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "timeout(QCoapInternalRequest *)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&a0)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void
//      QCoapInternalRequest::maxTransmissionSpanReached(QCoapInternalRequest
//      *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QCoapInternalRequest26maxTransmissionSpanReachedEPS_(
    QCoapInternalRequest *self,
    QCoapInternalRequest *a0) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QCoapInternalRequest")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "maxTransmissionSpanReached(QCoapInternalRequest *)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "maxTransmissionSpanReached(QCoapInternalRequest *)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&a0)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QCoapInternalRequest::multicastRequestExpired(QCoapInternalRequest
//      *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QCoapInternalRequest23multicastRequestExpiredEPS_(
    QCoapInternalRequest *self,
    QCoapInternalRequest *a0) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QCoapInternalRequest")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "multicastRequestExpired(QCoapInternalRequest *)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "multicastRequestExpired(QCoapInternalRequest *)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&a0)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  QCoapOption QCoapInternalRequest::uriHostOption(const QUrl &uri) const
extern "C" Q_DECL_EXPORT
QCoapOption *ritual_ZNK20QCoapInternalRequest13uriHostOptionERK4QUrl(
    const QCoapInternalRequest *self,
    const QUrl *uri) {
  return new QCoapOption(self->uriHostOption(*uri));
}

//  QCoapInternalRequestPrivate *QCoapInternalRequest::d_func()
extern "C" Q_DECL_EXPORT
QCoapInternalRequestPrivate *ritual_ZN20QCoapInternalRequest6d_funcEv(
    QCoapInternalRequest *self) {
  return self->d_func();
}

//  const QCoapInternalRequestPrivate *QCoapInternalRequest::d_func() const
extern "C" Q_DECL_EXPORT
const QCoapInternalRequestPrivate *ritual_ZNK20QCoapInternalRequest6d_funcEv(
    const QCoapInternalRequest *self) {
  return self->d_func();
}

//  bool QCoapInternalRequest::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK20QCoapInternalRequest7isValidEv(
    const QCoapInternalRequest *self) {
  return self->QCoapInternalRequest::isValid();
}

//  void QCoapInternalRequest::addOption(const QCoapOption &option)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QCoapInternalRequest9addOptionERK11QCoapOption(
    QCoapInternalRequest *self,
    const QCoapOption *option) {
  self->QCoapInternalRequest::addOption(*option);
}
