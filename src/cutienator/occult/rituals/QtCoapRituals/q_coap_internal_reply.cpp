//  Written by dev_tooling.RitualGenerator from the records of
//  QtCoap/6.12.0/QtCoap/private/qcoapinternalreply_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCoap/QtCoap>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCoap/6.12.0/QtCoap/private/qcoapinternalreply_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtCoap/qcoapoption.h>
#include <QtNetwork/qhostaddress.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCoap/private/qcoapinternalmessage_p.h>
#include <QtCoap/private/qcoaprequest_p.h>
#include <QtCoap/qcoaprequest.h>
#include <QtCore/qloggingcategory.h>
#include <QtCoap/private/qcoapinternalreply_p.h>
#include <QtCore/qendian.h>
#include <QtCore/qmath.h>
#include <memory>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

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

//  from ../qtcoap/src/coap/qcoapinternalreply.cpp, line 163, as _ZN18QCoapInternalReply10appendDataERK10QByteArray
inline void QCoapInternalReply::appendData(const QByteArray &data)
{
    Q_D(QCoapInternalReply);
    d->message.setPayload(d->message.payload().append(data));
}

//  from ../qtcoap/src/coap/qcoapinternalreply.cpp, line 228, as _ZNK18QCoapInternalReply19hasMoreBlocksToSendEv
inline bool QCoapInternalReply::hasMoreBlocksToSend() const
{
    return nextBlockToSend() >= 0;
}

//  from ../qtcoap/src/coap/qcoapinternalreply.cpp, line 198, as _ZNK18QCoapInternalReply15nextBlockToSendEv
inline int QCoapInternalReply::nextBlockToSend() const
{
    Q_D(const QCoapInternalReply);

    QCoapOption option = d->message.option(QCoapOption::Block1);
    if (!option.isValid())
        return -1;

    const auto value = option.opaqueValue();
    const quint8 *optionData = reinterpret_cast<const quint8 *>(value.data());
    // Zero-length block option => M=0 (no further block); avoid optionData[-1].
    const quint8 lastByte = option.length() > 0 ? optionData[option.length() - 1] : 0;

    // M field
    bool hasNextBlock = ((lastByte & 0x8) == 0x8);
    if (!hasNextBlock)
        return -1;

    // NUM field
    quint32 blockNumber = 0;
    for (int i = 0; i < option.length() - 1; ++i)
        blockNumber = (blockNumber << 8) | optionData[i];
    blockNumber = (blockNumber << 4) | (lastByte >> 4);
    return static_cast<int>(blockNumber) + 1;
}

//  from ../qtcoap/src/coap/qcoapinternalreply.cpp, line 173, as _ZN18QCoapInternalReply9addOptionERK11QCoapOption
inline void QCoapInternalReply::addOption(const QCoapOption &option)
{
    if (option.name() == QCoapOption::Block2)
        setFromDescriptiveBlockOption(option);

    QCoapInternalMessage::addOption(option);
}

//  from ../qtcoap/src/coap/qcoapinternalreply.cpp, line 185, as _ZN18QCoapInternalReply16setSenderAddressERK12QHostAddress
inline void QCoapInternalReply::setSenderAddress(const QHostAddress &address)
{
    Q_D(QCoapInternalReply);
    d->senderAddress = address;
}

//  from ../qtcoap/src/coap/qcoapinternalreply.cpp, line 237, as _ZNK18QCoapInternalReply12responseCodeEv
inline QtCoap::ResponseCode QCoapInternalReply::responseCode() const
{
    Q_D(const QCoapInternalReply);
    return d->responseCode;
}

//  from ../qtcoap/src/coap/qcoapinternalreply.cpp, line 247, as _ZNK18QCoapInternalReply13senderAddressEv
inline QHostAddress QCoapInternalReply::senderAddress() const
{
    Q_D(const QCoapInternalReply);
    return d->senderAddress;
}
//  -----------------------------------------------------------------------

//  const QMetaObject *QCoapInternalReply::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QCoapInternalReply10metaObjectEv(
    const QCoapInternalReply *self) {
  return self->metaObject();
}

//  void QCoapInternalReply::appendData(const QByteArray &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QCoapInternalReply10appendDataERK10QByteArray(
    QCoapInternalReply *self,
    const QByteArray *data) {
  self->appendData(*data);
}

//  bool QCoapInternalReply::hasMoreBlocksToSend() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QCoapInternalReply19hasMoreBlocksToSendEv(
    const QCoapInternalReply *self) {
  return self->hasMoreBlocksToSend();
}

//  int QCoapInternalReply::nextBlockToSend() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QCoapInternalReply15nextBlockToSendEv(
    const QCoapInternalReply *self) {
  return self->nextBlockToSend();
}

//  void QCoapInternalReply::addOption(const QCoapOption &option)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QCoapInternalReply9addOptionERK11QCoapOption(
    QCoapInternalReply *self,
    const QCoapOption *option) {
  self->addOption(*option);
}

//  void QCoapInternalReply::setSenderAddress(const QHostAddress &address)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QCoapInternalReply16setSenderAddressERK12QHostAddress(
    QCoapInternalReply *self,
    const QHostAddress *address) {
  self->setSenderAddress(*address);
}

//  QtCoap::ResponseCode QCoapInternalReply::responseCode() const
extern "C" Q_DECL_EXPORT
QtCoap::ResponseCode ritual_ZNK18QCoapInternalReply12responseCodeEv(
    const QCoapInternalReply *self) {
  return self->responseCode();
}

//  QHostAddress QCoapInternalReply::senderAddress() const
extern "C" Q_DECL_EXPORT
QHostAddress *ritual_ZNK18QCoapInternalReply13senderAddressEv(
    const QCoapInternalReply *self) {
  return new QHostAddress(self->senderAddress());
}

//  QCoapInternalReplyPrivate *QCoapInternalReply::d_func()
extern "C" Q_DECL_EXPORT
QCoapInternalReplyPrivate *ritual_ZN18QCoapInternalReply6d_funcEv(
    QCoapInternalReply *self) {
  return self->d_func();
}

//  const QCoapInternalReplyPrivate *QCoapInternalReply::d_func() const
extern "C" Q_DECL_EXPORT
const QCoapInternalReplyPrivate *ritual_ZNK18QCoapInternalReply6d_funcEv(
    const QCoapInternalReply *self) {
  return self->d_func();
}
