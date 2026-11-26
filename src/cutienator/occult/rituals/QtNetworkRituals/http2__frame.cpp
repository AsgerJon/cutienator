//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/http2frames_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtNetwork/qtnetworkglobal.h>
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#if QT_CONFIG(http)
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/http2frames_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/private/http2frames_p.h>
#include <QtNetwork/qabstractsocket.h>
#include <algorithm>
#include <utility>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/network/access/http2/http2frames.cpp, line 19, as _ZN5Http25FrameC1Ev
namespace Http2 {
inline Frame::Frame()
    : buffer(frameHeaderSize)
{
}
}  // namespace Http2

//  from src/network/access/http2/http2frames.cpp, line 24, as _ZNK5Http25Frame4typeEv
namespace Http2 {
inline FrameType Frame::type() const
{
    Q_ASSERT(buffer.size() >= frameHeaderSize);

    if (int(buffer[3]) >= int(FrameType::LAST_FRAME_TYPE))
        return FrameType::LAST_FRAME_TYPE;

    return FrameType(buffer[3]);
}
}  // namespace Http2

//  from src/network/access/http2/http2frames.cpp, line 34, as _ZNK5Http25Frame8streamIDEv
namespace Http2 {
inline quint32 Frame::streamID() const
{
    Q_ASSERT(buffer.size() >= frameHeaderSize);
    // RFC 9113, 4.1: 31-bit Stream ID; lastValidStreamID(0x7FFFFFFF) masks out the reserved MSB
    return qFromBigEndian<quint32>(&buffer[5]) & lastValidStreamID;
}
}  // namespace Http2

//  from src/network/access/http2/http2frames.cpp, line 41, as _ZNK5Http25Frame5flagsEv
namespace Http2 {
inline FrameFlags Frame::flags() const
{
    Q_ASSERT(buffer.size() >= frameHeaderSize);
    return FrameFlags(buffer[4]);
}
}  // namespace Http2

//  from src/network/access/http2/http2frames.cpp, line 47, as _ZNK5Http25Frame11payloadSizeEv
namespace Http2 {
inline quint32 Frame::payloadSize() const
{
    Q_ASSERT(buffer.size() >= frameHeaderSize);
    return buffer[0] << 16 | buffer[1] << 8 | buffer[2];
}
}  // namespace Http2

//  from src/network/access/http2/http2frames.cpp, line 53, as _ZNK5Http25Frame7paddingEv
namespace Http2 {
inline uchar Frame::padding() const
{
    Q_ASSERT(validateHeader() == FrameStatus::goodFrame);

    if (!isPadded())
        return 0;

    Q_ASSERT(buffer.size() > frameHeaderSize);
    return buffer[frameHeaderSize];
}
}  // namespace Http2

//  from src/network/access/http2/http2frames.cpp, line 69, as _ZNK5Http25Frame18supportsPaddedFlagEv
namespace Http2 {
inline bool Frame::supportsPaddedFlag() const
{
    switch (type()) {
    case FrameType::DATA:
    case FrameType::PUSH_PROMISE:
    case FrameType::HEADERS:
        return true;
    default:
        break;
    }
    return false;
}
}  // namespace Http2

//  from src/network/access/http2/http2frames.cpp, line 64, as _ZNK5Http25Frame8isPaddedEv
namespace Http2 {
inline bool Frame::isPadded() const
{
    return supportsPaddedFlag() && flags().testFlag(FrameFlag::PADDED);
}
}  // namespace Http2

//  from src/network/access/http2/http2frames.cpp, line 82, as _ZNK5Http25Frame8priorityEPjPh
namespace Http2 {
inline bool Frame::priority(quint32 *streamID, uchar *weight) const
{
    Q_ASSERT(validatePayload() == FrameStatus::goodFrame);

    if (buffer.size() <= frameHeaderSize)
        return false;

    const uchar *src = &buffer[0] + frameHeaderSize;
    if (type() == FrameType::HEADERS && flags().testFlag(FrameFlag::PADDED))
        ++src;

    if ((type() == FrameType::HEADERS && flags().testFlag(FrameFlag::PRIORITY))
        || type() == FrameType::PRIORITY) {
        if (streamID)
            *streamID = qFromBigEndian<quint32>(src);
        if (weight)
            *weight = src[4];
        return true;
    }

    return false;
}
}  // namespace Http2

//  from src/network/access/http2/http2frames.cpp, line 105, as _ZNK5Http25Frame14validateHeaderEv
namespace Http2 {
inline FrameStatus Frame::validateHeader() const
{
    // Should be called only on a frame with
    // a complete header.
    Q_ASSERT(buffer.size() >= frameHeaderSize);

    const auto framePayloadSize = payloadSize();
    // 4.2 Frame Size
    if (framePayloadSize > maxPayloadSize)
        return FrameStatus::sizeError;

    switch (type()) {
    case FrameType::SETTINGS:
        // SETTINGS ACK can not have any payload.
        // The payload of a SETTINGS frame consists of zero
        // or more parameters, each consisting of an unsigned
        // 16-bit setting identifier and an unsigned 32-bit value.
        // Thus the payload size must be a multiple of 6.
        if (flags().testFlag(FrameFlag::ACK) ? framePayloadSize : framePayloadSize % 6)
            return FrameStatus::sizeError;
        break;
    case FrameType::PRIORITY:
        // 6.3 PRIORITY
        if (framePayloadSize != 5)
            return FrameStatus::sizeError;
        break;
    case FrameType::PING:
        // 6.7 PING
        if (framePayloadSize != 8)
            return FrameStatus::sizeError;
        break;
    case FrameType::GOAWAY:
        // 6.8 GOAWAY
        if (framePayloadSize < 8)
            return FrameStatus::sizeError;
        break;
    case FrameType::RST_STREAM:
    case FrameType::WINDOW_UPDATE:
        // 6.4 RST_STREAM, 6.9 WINDOW_UPDATE
        if (framePayloadSize != 4)
            return FrameStatus::sizeError;
        break;
    case FrameType::PUSH_PROMISE:
        // 6.6 PUSH_PROMISE
        if (framePayloadSize < 4)
            return FrameStatus::sizeError;
        break;
    default:
        // DATA/HEADERS/CONTINUATION will be verified
        // when we have payload.
        // Frames of unknown types are ignored (5.1)
        break;
    }

    return FrameStatus::goodFrame;
}
}  // namespace Http2

//  from src/network/access/http2/http2frames.cpp, line 162, as _ZNK5Http25Frame15validatePayloadEv
namespace Http2 {
inline FrameStatus Frame::validatePayload() const
{
    // Should be called only on a complete frame with a valid header.
    Q_ASSERT(validateHeader() == FrameStatus::goodFrame);

    // Ignored, 5.1
    if (type() == FrameType::LAST_FRAME_TYPE)
        return FrameStatus::goodFrame;

    auto size = payloadSize();
    Q_ASSERT(buffer.size() >= frameHeaderSize && size == buffer.size() - frameHeaderSize);

    const uchar *src = size ? &buffer[0] + frameHeaderSize : nullptr;
    const auto frameFlags = flags();
    switch (type()) {
    // 6.1 DATA, 6.2 HEADERS
    case FrameType::DATA:
    case FrameType::HEADERS:
        if (frameFlags.testFlag(FrameFlag::PADDED)) {
            // size must cover the 1-byte pad-length field plus src[0] padding bytes
            if (!size || size - 1 < src[0])
                return FrameStatus::sizeError;
            size -= src[0] + 1;
        }
        if (type() == FrameType::HEADERS && frameFlags.testFlag(FrameFlag::PRIORITY)) {
            if (size < 5)
                return FrameStatus::sizeError;
        }
        break;
    // 6.6 PUSH_PROMISE
    case FrameType::PUSH_PROMISE:
        if (frameFlags.testFlag(FrameFlag::PADDED)) {
            // size must cover the 1-byte pad-length field plus src[0] padding bytes
            if (!size || size - 1 < src[0])
                return FrameStatus::sizeError;
            size -= src[0] + 1;
        }

        if (size < 4)
            return FrameStatus::sizeError;
        break;
    default:
        break;
    }

    return FrameStatus::goodFrame;
}
}  // namespace Http2

//  from src/network/access/http2/http2frames.cpp, line 211, as _ZNK5Http25Frame8dataSizeEv
namespace Http2 {
inline quint32 Frame::dataSize() const
{
    Q_ASSERT(validatePayload() == FrameStatus::goodFrame);

    quint32 size = payloadSize();
    if (isPadded()) {
        const uchar pad = padding();
        // + 1 one for a byte with padding number itself:
        size -= pad + 1;
    }

    if (priority())
        size -= 5;

    return size;
}
}  // namespace Http2

//  from src/network/access/http2/http2frames.cpp, line 228, as _ZNK5Http25Frame14hpackBlockSizeEv
namespace Http2 {
inline quint32 Frame::hpackBlockSize() const
{
    Q_ASSERT(validatePayload() == FrameStatus::goodFrame);

    const auto frameType = type();
    Q_ASSERT(frameType == FrameType::HEADERS ||
             frameType == FrameType::PUSH_PROMISE ||
             frameType == FrameType::CONTINUATION);

    quint32 size = dataSize();
    if (frameType == FrameType::PUSH_PROMISE) {
        Q_ASSERT(size >= 4);
        size -= 4;
    }

    return size;
}
}  // namespace Http2

//  from src/network/access/http2/http2frames.cpp, line 246, as _ZNK5Http25Frame9dataBeginEv
namespace Http2 {
inline const uchar *Frame::dataBegin() const
{
    Q_ASSERT(validatePayload() == FrameStatus::goodFrame);
    if (buffer.size() <= frameHeaderSize)
        return nullptr;

    const uchar *src = &buffer[0] + frameHeaderSize;
    if (isPadded())
        ++src;

    if (priority())
        src += 5;

    return src;
}
}  // namespace Http2

//  from src/network/access/http2/http2frames.cpp, line 262, as _ZNK5Http25Frame15hpackBlockBeginEv
namespace Http2 {
inline const uchar *Frame::hpackBlockBegin() const
{
    Q_ASSERT(validatePayload() == FrameStatus::goodFrame);

    const auto frameType = type();
    Q_ASSERT(frameType == FrameType::HEADERS ||
             frameType == FrameType::PUSH_PROMISE ||
             frameType == FrameType::CONTINUATION);

    const uchar *begin = dataBegin();
    if (frameType == FrameType::PUSH_PROMISE)
        begin += 4; // That's a promised stream, skip it.
    return begin;
}
}  // namespace Http2
//  -----------------------------------------------------------------------

//  Http2::Frame::Frame()
extern "C" Q_DECL_EXPORT
Http2::Frame *ritual_ZN5Http25FrameC1Ev() {
  return new Http2::Frame();
}

//  FrameType Http2::Frame::type() const
extern "C" Q_DECL_EXPORT
Http2::FrameType ritual_ZNK5Http25Frame4typeEv(const Http2::Frame *self) {
  return self->type();
}

//  quint32 Http2::Frame::streamID() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK5Http25Frame8streamIDEv(const Http2::Frame *self) {
  return self->streamID();
}

//  FrameFlags Http2::Frame::flags() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK5Http25Frame5flagsEv(const Http2::Frame *self) {
  return static_cast<int>(self->flags().toInt());
}

//  quint32 Http2::Frame::payloadSize() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK5Http25Frame11payloadSizeEv(const Http2::Frame *self) {
  return self->payloadSize();
}

//  uchar Http2::Frame::padding() const
extern "C" Q_DECL_EXPORT
uchar ritual_ZNK5Http25Frame7paddingEv(const Http2::Frame *self) {
  return self->padding();
}

//  bool Http2::Frame::supportsPaddedFlag() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK5Http25Frame18supportsPaddedFlagEv(const Http2::Frame *self) {
  return self->supportsPaddedFlag();
}

//  bool Http2::Frame::isPadded() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK5Http25Frame8isPaddedEv(const Http2::Frame *self) {
  return self->isPadded();
}

//  bool Http2::Frame::priority(quint32 *streamID, uchar *weight) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK5Http25Frame8priorityEPjPh(
    const Http2::Frame *self,
    quint32 *streamID,
    uchar *weight) {
  return self->priority(streamID, weight);
}

//  FrameStatus Http2::Frame::validateHeader() const
extern "C" Q_DECL_EXPORT
Http2::FrameStatus ritual_ZNK5Http25Frame14validateHeaderEv(
    const Http2::Frame *self) {
  return self->validateHeader();
}

//  FrameStatus Http2::Frame::validatePayload() const
extern "C" Q_DECL_EXPORT
Http2::FrameStatus ritual_ZNK5Http25Frame15validatePayloadEv(
    const Http2::Frame *self) {
  return self->validatePayload();
}

//  quint32 Http2::Frame::dataSize() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK5Http25Frame8dataSizeEv(const Http2::Frame *self) {
  return self->dataSize();
}

//  quint32 Http2::Frame::hpackBlockSize() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK5Http25Frame14hpackBlockSizeEv(const Http2::Frame *self) {
  return self->hpackBlockSize();
}

//  const uchar *Http2::Frame::dataBegin() const
extern "C" Q_DECL_EXPORT
const uchar *ritual_ZNK5Http25Frame9dataBeginEv(const Http2::Frame *self) {
  return self->dataBegin();
}

//  const uchar *Http2::Frame::hpackBlockBegin() const
extern "C" Q_DECL_EXPORT
const uchar *ritual_ZNK5Http25Frame15hpackBlockBeginEv(
    const Http2::Frame *self) {
  return self->hpackBlockBegin();
}

//  Http2::Frame::~Frame()
extern "C" Q_DECL_EXPORT
void ritual_ZN5Http25FrameD1Ev(Http2::Frame *self) {
  delete self;
}

#endif  // QT_CONFIG(http)
