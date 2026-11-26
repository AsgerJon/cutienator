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

//  from src/network/access/http2/http2frames.cpp, line 47, as _ZNK5Http25Frame11payloadSizeEv
namespace Http2 {
inline quint32 Frame::payloadSize() const
{
    Q_ASSERT(buffer.size() >= frameHeaderSize);
    return buffer[0] << 16 | buffer[1] << 8 | buffer[2];
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

//  from src/network/access/http2/http2frames.cpp, line 277, as _ZN5Http211FrameReader4readER9QIODevice
namespace Http2 {
inline FrameStatus FrameReader::read(QIODevice &socket)
{
    if (offset < frameHeaderSize) {
        if (!readHeader(socket))
            return FrameStatus::incompleteFrame;
    }

    const auto status = frame.validateHeader();
    if (status != FrameStatus::goodFrame) {
        if (status == FrameStatus::sizeError && frame.streamID() != connectionStreamID) {
            if (!discardPayload(socket))
                return FrameStatus::incompleteFrame;
        }
        return status;
    }

    Q_ASSERT(maxPayloadSize >= frame.payloadSize());
    frame.buffer.resize(frame.payloadSize() + frameHeaderSize);

    if (offset < frame.buffer.size() && !readPayload(socket))
        return FrameStatus::incompleteFrame;

    // Reset the offset, our frame can be re-used
    // now (re-read):
    offset = 0;

    return frame.validatePayload();
}
}  // namespace Http2

//  from src/network/access/http2/http2frames.cpp, line 306, as _ZN5Http211FrameReader10readHeaderER9QIODevice
namespace Http2 {
inline bool FrameReader::readHeader(QIODevice &socket)
{
    Q_ASSERT(offset < frameHeaderSize);

    auto &buffer = frame.buffer;
    if (buffer.size() < frameHeaderSize)
        buffer.resize(frameHeaderSize);

    const auto chunkSize = socket.read(reinterpret_cast<char *>(&buffer[offset]),
                                       frameHeaderSize - offset);
    if (chunkSize > 0)
        offset += chunkSize;

    return offset == frameHeaderSize;
}
}  // namespace Http2

//  from src/network/access/http2/http2frames.cpp, line 322, as _ZN5Http211FrameReader11readPayloadER9QIODevice
namespace Http2 {
inline bool FrameReader::readPayload(QIODevice &socket)
{
    Q_ASSERT(offset < frame.buffer.size());
    Q_ASSERT(frame.buffer.size() > frameHeaderSize);

    auto &buffer = frame.buffer;
    // Casts and ugliness - to deal with MSVC. Values are guaranteed to fit into quint32.
    const auto chunkSize = socket.read(reinterpret_cast<char *>(&buffer[offset]),
                                       qint64(buffer.size() - offset));
    if (chunkSize > 0)
        offset += quint32(chunkSize);

    return offset == buffer.size();
}
}  // namespace Http2

//  from src/network/access/http2/http2frames.cpp, line 338, as _ZN5Http211FrameReader14discardPayloadER9QIODevice
namespace Http2 {
inline bool FrameReader::discardPayload(QIODevice &socket)
{
    Q_ASSERT(offset >= frameHeaderSize); // Frame header is already read when this is called

    using namespace Http2;
    auto frameType = frame.type();
    if (frameType != FrameType::DATA && frameType != FrameType::PRIORITY &&
        frameType != FrameType::WINDOW_UPDATE)
        return true; // Connection will be closed, nothing needs to be discarded

    const quint32 payload = frame.payloadSize();
    Q_ASSERT(maxPayloadSize >= payload);
    const quint32 totalFrameSize = frameHeaderSize + payload;
    while (totalFrameSize > offset) {
        const quint32 remainingSize = totalFrameSize - offset;
        const auto skipped = socket.skip(remainingSize);
        if (skipped > 0)
            offset += quint32(skipped);
        else
            return false;
    }
    offset = 0;
    return true;
}
}  // namespace Http2
//  -----------------------------------------------------------------------

//  FrameStatus Http2::FrameReader::read(QIODevice &socket)
extern "C" Q_DECL_EXPORT
Http2::FrameStatus ritual_ZN5Http211FrameReader4readER9QIODevice(
    Http2::FrameReader *self,
    QIODevice *socket) {
  return self->read(*socket);
}

//  Frame &Http2::FrameReader::inboundFrame()
extern "C" Q_DECL_EXPORT
Http2::Frame *ritual_ZN5Http211FrameReader12inboundFrameEv(
    Http2::FrameReader *self) {
  return &(self->inboundFrame());
}

//  bool Http2::FrameReader::readHeader(QIODevice &socket)
extern "C" Q_DECL_EXPORT
bool ritual_ZN5Http211FrameReader10readHeaderER9QIODevice(
    Http2::FrameReader *self,
    QIODevice *socket) {
  return self->readHeader(*socket);
}

//  bool Http2::FrameReader::readPayload(QIODevice &socket)
extern "C" Q_DECL_EXPORT
bool ritual_ZN5Http211FrameReader11readPayloadER9QIODevice(
    Http2::FrameReader *self,
    QIODevice *socket) {
  return self->readPayload(*socket);
}

//  bool Http2::FrameReader::discardPayload(QIODevice &socket)
extern "C" Q_DECL_EXPORT
bool ritual_ZN5Http211FrameReader14discardPayloadER9QIODevice(
    Http2::FrameReader *self,
    QIODevice *socket) {
  return self->discardPayload(*socket);
}

//  Http2::FrameReader::~FrameReader()
extern "C" Q_DECL_EXPORT
void ritual_ZN5Http211FrameReaderD1Ev(Http2::FrameReader *self) {
  delete self;
}

#endif  // QT_CONFIG(http)
