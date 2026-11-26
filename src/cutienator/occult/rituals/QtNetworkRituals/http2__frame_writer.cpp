//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/http2frames_p.h, Qt 6.12.0. Edited by
//  hand on 2026-11-25: added by hand, instances of templates of the class:
//  2. Kept as it is when the generator runs again.
#include <QtNetwork/qtnetworkglobal.h>
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#if QT_CONFIG(http)
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/http2frames_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearrayview.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/private/http2frames_p.h>
#include <QtNetwork/qabstractsocket.h>
#include <algorithm>
#include <utility>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/network/access/http2/http2frames.cpp, line 19, as _ZN5Http25FrameC1Ev
namespace Http2 {
inline Frame::Frame()
    : buffer(frameHeaderSize)
{
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

//  from src/network/access/http2/http2frames.cpp, line 47, as _ZNK5Http25Frame11payloadSizeEv
namespace Http2 {
inline quint32 Frame::payloadSize() const
{
    Q_ASSERT(buffer.size() >= frameHeaderSize);
    return buffer[0] << 16 | buffer[1] << 8 | buffer[2];
}
}  // namespace Http2

//  from src/network/access/http2/http2frames.cpp, line 363, as _ZN5Http211FrameWriterC1Ev
namespace Http2 {
inline FrameWriter::FrameWriter()
{
}
}  // namespace Http2

//  from src/network/access/http2/http2frames.cpp, line 367, as _ZN5Http211FrameWriterC1ENS_9FrameTypeE6QFlagsINS_9FrameFlagEEj
namespace Http2 {
inline FrameWriter::FrameWriter(FrameType type, FrameFlags flags, quint32 streamID)
{
    start(type, flags, streamID);
}
}  // namespace Http2

//  from src/network/access/http2/http2frames.cpp, line 372, as _ZN5Http211FrameWriter16setOutboundFrameEONS_5FrameE
namespace Http2 {
inline void FrameWriter::setOutboundFrame(Frame &&newFrame)
{
    frame = std::move(newFrame);
    updatePayloadSize();
}
}  // namespace Http2

//  from src/network/access/http2/http2frames.cpp, line 378, as _ZN5Http211FrameWriter5startENS_9FrameTypeE6QFlagsINS_9FrameFlagEEj
namespace Http2 {
inline void FrameWriter::start(FrameType type, FrameFlags flags, quint32 streamID)
{
    auto &buffer = frame.buffer;

    buffer.resize(frameHeaderSize);
    // The first three bytes - payload size, which is 0 for now.
    buffer[0] = 0;
    buffer[1] = 0;
    buffer[2] = 0;

    buffer[3] = uchar(type);
    buffer[4] = uchar(flags);

    qToBigEndian(streamID, &buffer[5]);
}
}  // namespace Http2

//  from src/network/access/http2/http2frames.cpp, line 394, as _ZN5Http211FrameWriter14setPayloadSizeEj
namespace Http2 {
inline void FrameWriter::setPayloadSize(quint32 size)
{
    auto &buffer = frame.buffer;

    Q_ASSERT(buffer.size() >= frameHeaderSize);
    Q_ASSERT(size <= maxPayloadSize);

    buffer[0] = size >> 16;
    buffer[1] = size >> 8;
    buffer[2] = size;
}
}  // namespace Http2

//  from src/network/access/http2/http2frames.cpp, line 406, as _ZN5Http211FrameWriter7setTypeENS_9FrameTypeE
namespace Http2 {
inline void FrameWriter::setType(FrameType type)
{
    Q_ASSERT(frame.buffer.size() >= frameHeaderSize);
    frame.buffer[3] = uchar(type);
}
}  // namespace Http2

//  from src/network/access/http2/http2frames.cpp, line 412, as _ZN5Http211FrameWriter8setFlagsE6QFlagsINS_9FrameFlagEE
namespace Http2 {
inline void FrameWriter::setFlags(FrameFlags flags)
{
    Q_ASSERT(frame.buffer.size() >= frameHeaderSize);
    frame.buffer[4] = uchar(flags);
}
}  // namespace Http2

//  from src/network/access/http2/http2frames.cpp, line 418, as _ZN5Http211FrameWriter7addFlagENS_9FrameFlagE
namespace Http2 {
inline void FrameWriter::addFlag(FrameFlag flag)
{
    setFlags(frame.flags() | flag);
}
}  // namespace Http2

//  from src/network/access/http2/http2frames.cpp, line 423, as _ZN5Http211FrameWriter6appendEPKhS2_
namespace Http2 {
inline void FrameWriter::append(const uchar *begin, const uchar *end)
{
    Q_ASSERT(begin && end);
    Q_ASSERT(begin < end);

    frame.buffer.insert(frame.buffer.end(), begin, end);
    updatePayloadSize();
}
}  // namespace Http2

//  from src/network/access/http2/http2frames.cpp, line 439, as _ZNK5Http211FrameWriter5writeER9QIODevice
namespace Http2 {
inline bool FrameWriter::write(QIODevice &socket) const
{
    auto &buffer = frame.buffer;
    Q_ASSERT(buffer.size() >= frameHeaderSize);
    // Do some sanity check first:

    Q_ASSERT(int(frame.type()) < int(FrameType::LAST_FRAME_TYPE));
    Q_ASSERT(frame.validateHeader() == FrameStatus::goodFrame);

    const auto nWritten = socket.write(reinterpret_cast<const char *>(&buffer[0]),
                                       buffer.size());
    return nWritten != -1 && size_type(nWritten) == buffer.size();
}
}  // namespace Http2

//  from src/network/access/http2/http2frames.cpp, line 453, as _ZN5Http211FrameWriter12writeHEADERSER9QIODevicej
namespace Http2 {
inline bool FrameWriter::writeHEADERS(QIODevice &socket, quint32 sizeLimit)
{
    auto &buffer = frame.buffer;
    Q_ASSERT(buffer.size() >= frameHeaderSize);

    if (sizeLimit > quint32(maxPayloadSize))
        sizeLimit = quint32(maxPayloadSize);

    if (quint32(buffer.size() - frameHeaderSize) <= sizeLimit) {
        addFlag(FrameFlag::END_HEADERS);
        updatePayloadSize();
        return write(socket);
    }

    // Our HPACK block does not fit into the size limit, remove
    // END_HEADERS bit from the first frame, we'll later set
    // it on the last CONTINUATION frame:
    setFlags(frame.flags() & ~FrameFlags(FrameFlag::END_HEADERS));
    // Write a frame's header (not controlled by sizeLimit) and
    // as many bytes of payload as we can within sizeLimit,
    // then send CONTINUATION frames, as needed.
    setPayloadSize(sizeLimit);
    const quint32 firstChunkSize = frameHeaderSize + sizeLimit;
    qint64 written = socket.write(reinterpret_cast<const char *>(&buffer[0]),
                                  firstChunkSize);

    if (written != qint64(firstChunkSize))
        return false;

    FrameWriter continuationWriter(FrameType::CONTINUATION, FrameFlag::EMPTY, frame.streamID());
    quint32 offset = firstChunkSize;

    while (offset != buffer.size()) {
        const auto chunkSize = std::min(sizeLimit, quint32(buffer.size() - offset));
        if (chunkSize + offset == buffer.size())
            continuationWriter.addFlag(FrameFlag::END_HEADERS);
        continuationWriter.setPayloadSize(chunkSize);
        if (!continuationWriter.write(socket))
            return false;
        written = socket.write(reinterpret_cast<const char *>(&buffer[offset]),
                               chunkSize);
        if (written != qint64(chunkSize))
            return false;

        offset += chunkSize;
    }

    return true;
}
}  // namespace Http2

//  from src/network/access/http2/http2frames.cpp, line 503, as _ZN5Http211FrameWriter9writeDATAER9QIODevicejPKhj
namespace Http2 {
inline bool FrameWriter::writeDATA(QIODevice &socket, quint32 sizeLimit,
                            const uchar *src, quint32 size)
{
    // With DATA frame(s) we always have:
    // 1) frame's header (9 bytes)
    // 2) a separate payload (from QNonContiguousByteDevice).
    // We either fit within a sizeLimit, or split into several
    // DATA frames.

    Q_ASSERT(src);

    if (sizeLimit > quint32(maxPayloadSize))
        sizeLimit = quint32(maxPayloadSize);
    // We NEVER set END_STREAM, since QHttp2ProtocolHandler works with
    // QNonContiguousByteDevice and this 'writeDATA' is probably
    // not the last one for a given request.
    // This has to be done externally (sending an empty DATA frame with END_STREAM).
    for (quint32 offset = 0; offset != size;) {
        const auto chunkSize = std::min(size - offset, sizeLimit);
        setPayloadSize(chunkSize);
        // Frame's header first:
        if (!write(socket))
            return false;
        // Payload (if any):
        if (chunkSize) {
            const auto written = socket.write(reinterpret_cast<const char*>(src + offset),
                                              chunkSize);
            if (written != qint64(chunkSize))
                return false;
        }

        offset += chunkSize;
    }

    return true;
}
}  // namespace Http2

//  from src/network/access/http2/http2frames.cpp, line 432, as _ZN5Http211FrameWriter17updatePayloadSizeEv
namespace Http2 {
inline void FrameWriter::updatePayloadSize()
{
    const quint32 size = quint32(frame.buffer.size() - frameHeaderSize);
    Q_ASSERT(size <= maxPayloadSize);
    setPayloadSize(size);
}
}  // namespace Http2
//  -----------------------------------------------------------------------

//  Http2::FrameWriter::FrameWriter()
extern "C" Q_DECL_EXPORT
Http2::FrameWriter *ritual_ZN5Http211FrameWriterC1Ev() {
  return new Http2::FrameWriter();
}

//  Http2::FrameWriter::FrameWriter(FrameType type, FrameFlags flags, quint32
//      streamID)
extern "C" Q_DECL_EXPORT
Http2::FrameWriter *ritual_ZN5Http211FrameWriterC1ENS_9FrameTypeE6QFlagsINS_9FrameFlagEEj(
    Http2::FrameType type,
    int flags,
    quint32 streamID) {
  return new Http2::FrameWriter(
      type,
      QFlags<Http2::FrameFlag>::fromInt(flags),
      streamID);
}

//  Frame &Http2::FrameWriter::outboundFrame()
extern "C" Q_DECL_EXPORT
Http2::Frame *ritual_ZN5Http211FrameWriter13outboundFrameEv(
    Http2::FrameWriter *self) {
  return &(self->outboundFrame());
}

//  void Http2::FrameWriter::setOutboundFrame(Frame &&newFrame)
extern "C" Q_DECL_EXPORT
void ritual_ZN5Http211FrameWriter16setOutboundFrameEONS_5FrameE(
    Http2::FrameWriter *self,
    Http2::Frame *newFrame) {
  self->setOutboundFrame(std::move(*newFrame));
}

//  void Http2::FrameWriter::start(FrameType type, FrameFlags flags, quint32
//      streamID)
extern "C" Q_DECL_EXPORT
void ritual_ZN5Http211FrameWriter5startENS_9FrameTypeE6QFlagsINS_9FrameFlagEEj(
    Http2::FrameWriter *self,
    Http2::FrameType type,
    int flags,
    quint32 streamID) {
  self->start(type, QFlags<Http2::FrameFlag>::fromInt(flags), streamID);
}

//  void Http2::FrameWriter::setPayloadSize(quint32 size)
extern "C" Q_DECL_EXPORT
void ritual_ZN5Http211FrameWriter14setPayloadSizeEj(
    Http2::FrameWriter *self,
    quint32 size) {
  self->setPayloadSize(size);
}

//  void Http2::FrameWriter::setType(FrameType type)
extern "C" Q_DECL_EXPORT
void ritual_ZN5Http211FrameWriter7setTypeENS_9FrameTypeE(
    Http2::FrameWriter *self,
    Http2::FrameType type) {
  self->setType(type);
}

//  void Http2::FrameWriter::setFlags(FrameFlags flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN5Http211FrameWriter8setFlagsE6QFlagsINS_9FrameFlagEE(
    Http2::FrameWriter *self,
    int flags) {
  self->setFlags(QFlags<Http2::FrameFlag>::fromInt(flags));
}

//  void Http2::FrameWriter::addFlag(FrameFlag flag)
extern "C" Q_DECL_EXPORT
void ritual_ZN5Http211FrameWriter7addFlagENS_9FrameFlagE(
    Http2::FrameWriter *self,
    Http2::FrameFlag flag) {
  self->addFlag(flag);
}

//  void Http2::FrameWriter::append(uchar val)
extern "C" Q_DECL_EXPORT
void ritual_ZN5Http211FrameWriter6appendEh(
    Http2::FrameWriter *self,
    uchar val) {
  self->append(val);
}

//  void Http2::FrameWriter::append(Settings identifier)
extern "C" Q_DECL_EXPORT
void ritual_ZN5Http211FrameWriter6appendENS_8SettingsE(
    Http2::FrameWriter *self,
    Http2::Settings identifier) {
  self->append(identifier);
}

//  void Http2::FrameWriter::append(const payload_type &payload)
extern "C" Q_DECL_EXPORT
void ritual_ZN5Http211FrameWriter6appendERKSt6vectorIhSaIhEE(
    Http2::FrameWriter *self,
    const Http2::FrameWriter::payload_type *payload) {
  self->append(*payload);
}

//  void Http2::FrameWriter::append(QByteArrayView payload)
extern "C" Q_DECL_EXPORT
void ritual_ZN5Http211FrameWriter6appendE14QByteArrayView(
    Http2::FrameWriter *self,
    const QByteArrayView *payload) {
  self->append(*payload);
}

//  void Http2::FrameWriter::append(const uchar *begin, const uchar *end)
extern "C" Q_DECL_EXPORT
void ritual_ZN5Http211FrameWriter6appendEPKhS2_(
    Http2::FrameWriter *self,
    const uchar *begin,
    const uchar *end) {
  self->append(begin, end);
}

//  bool Http2::FrameWriter::write(QIODevice &socket) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK5Http211FrameWriter5writeER9QIODevice(
    const Http2::FrameWriter *self,
    QIODevice *socket) {
  return self->write(*socket);
}

//  bool Http2::FrameWriter::writeHEADERS(QIODevice &socket, quint32
//      sizeLimit)
extern "C" Q_DECL_EXPORT
bool ritual_ZN5Http211FrameWriter12writeHEADERSER9QIODevicej(
    Http2::FrameWriter *self,
    QIODevice *socket,
    quint32 sizeLimit) {
  return self->writeHEADERS(*socket, sizeLimit);
}

//  bool Http2::FrameWriter::writeDATA(QIODevice &socket, quint32 sizeLimit,
//      const uchar *src, quint32 size)
extern "C" Q_DECL_EXPORT
bool ritual_ZN5Http211FrameWriter9writeDATAER9QIODevicejPKhj(
    Http2::FrameWriter *self,
    QIODevice *socket,
    quint32 sizeLimit,
    const uchar *src,
    quint32 size) {
  return self->writeDATA(*socket, sizeLimit, src, size);
}

//  void Http2::FrameWriter::updatePayloadSize()
extern "C" Q_DECL_EXPORT
void ritual_ZN5Http211FrameWriter17updatePayloadSizeEv(
    Http2::FrameWriter *self) {
  self->updatePayloadSize();
}

//  Http2::FrameWriter::~FrameWriter()
extern "C" Q_DECL_EXPORT
void ritual_ZN5Http211FrameWriterD1Ev(Http2::FrameWriter *self) {
  delete self;
}

//  void Http2::FrameWriter::append<unsigned short>(unsigned short val)
extern "C" Q_DECL_EXPORT
void ritual_ZN5Http211FrameWriter6appendItEEvT_(
    Http2::FrameWriter *self,
    quint16 val) {
  self->append<quint16>(val);
}

//  void Http2::FrameWriter::append<unsigned int>(unsigned int val)
extern "C" Q_DECL_EXPORT
void ritual_ZN5Http211FrameWriter6appendIjEEvT_(
    Http2::FrameWriter *self,
    quint32 val) {
  self->append<quint32>(val);
}

#endif  // QT_CONFIG(http)
