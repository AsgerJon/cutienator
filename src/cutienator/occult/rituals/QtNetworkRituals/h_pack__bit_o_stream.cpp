//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/bitstreams_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtNetwork/qtnetworkglobal.h>
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#if QT_CONFIG(http)
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/bitstreams_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/private/bitstreams_p.h>
#include <QtNetwork/private/huffman_p.h>
#include <QtCore/qbytearray.h>
#include <limits>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/network/access/http2/bitstreams.cpp, line 19, as _ZN5HPack10BitOStreamC1ERSt6vectorIhSaIhEE
namespace HPack {
inline BitOStream::BitOStream(std::vector<uchar> &b)
    : buffer(b),
      // All data 'packed' before:
      bitsSet(8 * quint64(b.size()))
{
}
}  // namespace HPack

//  from src/network/access/http2/bitstreams.cpp, line 26, as _ZN5HPack10BitOStream9writeBitsEhh
namespace HPack {
inline void BitOStream::writeBits(uchar bits, quint8 bitLength)
{
    Q_ASSERT(bitLength <= 8);

    quint8 count = bitsSet % 8; // bits used in buffer.back(), but 0 means 8
    bits <<= 8 - bitLength; // at top of byte, lower bits clear
    if (count) { // we have a part-used byte; fill it some more:
        buffer.back() |= bits >> count;
        count = 8 - count;
    } // count bits have been consumed (and 0 now means 0)
    if (bitLength > count)
        buffer.push_back(bits << count);

    bitsSet += bitLength;
}
}  // namespace HPack

//  from src/network/access/http2/bitstreams.cpp, line 42, as _ZN5HPack10BitOStream5writeEj
namespace HPack {
inline void BitOStream::write(quint32 src)
{
    const quint8 prefixLen = 8 - bitsSet % 8;
    const quint32 fullPrefix = (1 << prefixLen) - 1;

    // https://http2.github.io/http2-spec/compression.html#low-level.representation,
    // 5.1
    if (src < fullPrefix) {
        writeBits(uchar(src), prefixLen);
    } else {
        writeBits(uchar(fullPrefix), prefixLen);
        // We're on the byte boundary now,
        // so we can just 'push_back'.
        Q_ASSERT(!(bitsSet % 8));
        src -= fullPrefix;
        while (src >= 128) {
            buffer.push_back(uchar(src % 128 + 128));
            src /= 128;
            bitsSet += 8;
        }
        buffer.push_back(src);
        bitsSet += 8;
    }
}
}  // namespace HPack

//  from src/network/access/http2/bitstreams.cpp, line 89, as _ZNK5HPack10BitOStream9bitLengthEv
namespace HPack {
inline quint64 BitOStream::bitLength() const
{
    return bitsSet;
}
}  // namespace HPack

//  from src/network/access/http2/bitstreams.cpp, line 94, as _ZNK5HPack10BitOStream10byteLengthEv
namespace HPack {
inline quint64 BitOStream::byteLength() const
{
    return buffer.size();
}
}  // namespace HPack

//  from src/network/access/http2/bitstreams.cpp, line 99, as _ZNK5HPack10BitOStream5beginEv
namespace HPack {
inline const uchar *BitOStream::begin() const
{
    return &buffer[0];
}
}  // namespace HPack

//  from src/network/access/http2/bitstreams.cpp, line 104, as _ZNK5HPack10BitOStream3endEv
namespace HPack {
inline const uchar *BitOStream::end() const
{
    return &buffer[0] + buffer.size();
}
}  // namespace HPack

//  from src/network/access/http2/bitstreams.cpp, line 109, as _ZN5HPack10BitOStream5clearEv
namespace HPack {
inline void BitOStream::clear()
{
    buffer.clear();
    bitsSet = 0;
}
}  // namespace HPack
//  -----------------------------------------------------------------------

//  HPack::BitOStream::BitOStream(std::vector<uchar> &buffer)
extern "C" Q_DECL_EXPORT
HPack::BitOStream *ritual_ZN5HPack10BitOStreamC1ERSt6vectorIhSaIhEE(
    std::vector<uchar> *buffer) {
  return new HPack::BitOStream(*buffer);
}

//  void HPack::BitOStream::writeBits(uchar bits, quint8 bitLength)
extern "C" Q_DECL_EXPORT
void ritual_ZN5HPack10BitOStream9writeBitsEhh(
    HPack::BitOStream *self,
    uchar bits,
    quint8 bitLength) {
  self->writeBits(bits, bitLength);
}

//  void HPack::BitOStream::write(quint32 src)
extern "C" Q_DECL_EXPORT
void ritual_ZN5HPack10BitOStream5writeEj(
    HPack::BitOStream *self,
    quint32 src) {
  self->write(src);
}

//  quint64 HPack::BitOStream::bitLength() const
extern "C" Q_DECL_EXPORT
quint64 ritual_ZNK5HPack10BitOStream9bitLengthEv(
    const HPack::BitOStream *self) {
  return self->bitLength();
}

//  quint64 HPack::BitOStream::byteLength() const
extern "C" Q_DECL_EXPORT
quint64 ritual_ZNK5HPack10BitOStream10byteLengthEv(
    const HPack::BitOStream *self) {
  return self->byteLength();
}

//  const uchar *HPack::BitOStream::begin() const
extern "C" Q_DECL_EXPORT
const uchar *ritual_ZNK5HPack10BitOStream5beginEv(
    const HPack::BitOStream *self) {
  return self->begin();
}

//  const uchar *HPack::BitOStream::end() const
extern "C" Q_DECL_EXPORT
const uchar *ritual_ZNK5HPack10BitOStream3endEv(
    const HPack::BitOStream *self) {
  return self->end();
}

//  void HPack::BitOStream::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN5HPack10BitOStream5clearEv(HPack::BitOStream *self) {
  self->clear();
}

#endif  // QT_CONFIG(http)
