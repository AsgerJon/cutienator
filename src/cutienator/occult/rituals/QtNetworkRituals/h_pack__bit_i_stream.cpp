//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/bitstreams_p.h, Qt 6.12.0. Edited by
//  hand on 2026-11-25: added by hand, instances of templates of the class:
//  4. Kept as it is when the generator runs again.
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
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/network/access/http2/bitstreams.cpp, line 115, as _ZN5HPack10BitIStreamC1Ev
namespace HPack {
inline BitIStream::BitIStream()
    : first(),
      last(),
      offset(),
      streamError(Error::NoError)
{
}
}  // namespace HPack

//  from src/network/access/http2/bitstreams.cpp, line 123, as _ZN5HPack10BitIStreamC1EPKhS2_
namespace HPack {
inline BitIStream::BitIStream(const uchar *begin, const uchar *end)
                 : first(begin),
                   last(end),
                   offset(),
                   streamError(Error::NoError)
{
}
}  // namespace HPack

//  from src/network/access/http2/bitstreams.cpp, line 131, as _ZNK5HPack10BitIStream9bitLengthEv
namespace HPack {
inline quint64 BitIStream::bitLength() const
{
    return quint64(last - first) * 8;
}
}  // namespace HPack

//  from src/network/access/http2/bitstreams.cpp, line 136, as _ZNK5HPack10BitIStream11hasMoreBitsEv
namespace HPack {
inline bool BitIStream::hasMoreBits() const
{
    return offset < bitLength();
}
}  // namespace HPack

//  from src/network/access/http2/bitstreams.cpp, line 141, as _ZN5HPack10BitIStream8skipBitsEy
namespace HPack {
inline bool BitIStream::skipBits(quint64 nBits)
{
    if (nBits > bitLength() || bitLength() - nBits < offset)
        return false;

    offset += nBits;
    return true;
}
}  // namespace HPack

//  from src/network/access/http2/bitstreams.cpp, line 150, as _ZN5HPack10BitIStream12rewindOffsetEy
namespace HPack {
inline bool BitIStream::rewindOffset(quint64 nBits)
{
    if (nBits > offset)
        return false;

    offset -= nBits;
    return true;
}
}  // namespace HPack

//  from src/network/access/http2/bitstreams.cpp, line 159, as _ZN5HPack10BitIStream4readEPj
namespace HPack {
inline bool BitIStream::read(quint32 *dstPtr)
{
    Q_ASSERT(dstPtr);
    quint32 &dst = *dstPtr;

    // 5.1 Integer Representation
    //
    // Integers are used to represent name indexes, header field indexes, or string lengths.
    // An integer representation can start anywhere within an octet.
    // To allow for optimized processing, an integer representation always finishes at the end of an octet.
    // An integer is represented in two parts: a prefix that fills the current octet and an optional
    // list of octets that are used if the integer value does not fit within the prefix.
    // The number of bits of the prefix (called N) is a parameter of the integer representation.
    // If the integer value is small enough, i.e., strictly less than 2N-1, it is compressed within the N-bit prefix.
    // ...
    // The prefix size, N, is always between 1 and 8 bits. An integer
    // starting at an octet boundary will have an 8-bit prefix.

    // Technically, such integers can be of any size, but as we do not have arbitrary-long integers,
    // everything that does not fit into 'dst' we consider as an error (after all, try to allocate a string
    // of such size and ... hehehe - send it as a part of a header!

    // This function updates the offset _only_ if the read was successful.
    if (offset >= bitLength()) {
        setError(Error::NotEnoughData);
        return false;
    }

    setError(Error::NoError);

    const quint32 prefixLen = 8 - offset % 8;
    const quint32 fullPrefix = (1 << prefixLen) - 1;

    const uchar prefix = uchar(first[offset / 8] & fullPrefix);
    if (prefix < fullPrefix) {
        // The number fitted into the prefix bits.
        dst = prefix;
        offset += prefixLen;
        return true;
    }

    quint32 newOffset = offset + prefixLen;
    // We have a list of bytes representing an integer ...
    quint64 val = prefix;
    quint32 octetPower = 0;

    while (true) {
        if (newOffset >= bitLength()) {
            setError(Error::NotEnoughData);
            return false;
        }

        const uchar octet = first[newOffset / 8];

        if (octetPower == 28 && octet > 15) {
            qCritical("integer is too big");
            setError(Error::InvalidInteger);
            return false;
        }

        val += quint32(octet & 0x7f) << octetPower;
        newOffset += 8;

        if (!(octet & 0x80)) {
            // The most significant bit of each octet is used
            // as a continuation flag: its value is set to 1
            // except for the last octet in the list.
            break;
        }

        octetPower += 7;
    }

    dst = val;
    offset = newOffset;
    Q_ASSERT(!(offset % 8));

    return true;
}
}  // namespace HPack

//  from src/network/access/http2/bitstreams.cpp, line 289, as _ZNK5HPack10BitIStream5errorEv
namespace HPack {
inline BitIStream::Error BitIStream::error() const
{
    return streamError;
}
}  // namespace HPack

//  from src/network/access/http2/bitstreams.cpp, line 294, as _ZN5HPack10BitIStream8setErrorENS0_5ErrorE
namespace HPack {
inline void BitIStream::setError(Error newState)
{
    streamError = newState;
}
}  // namespace HPack
//  -----------------------------------------------------------------------

//  HPack::BitIStream::BitIStream()
extern "C" Q_DECL_EXPORT
HPack::BitIStream *ritual_ZN5HPack10BitIStreamC1Ev() {
  return new HPack::BitIStream();
}

//  HPack::BitIStream::BitIStream(const uchar *f, const uchar *l)
extern "C" Q_DECL_EXPORT
HPack::BitIStream *ritual_ZN5HPack10BitIStreamC1EPKhS2_(
    const uchar *f,
    const uchar *l) {
  return new HPack::BitIStream(f, l);
}

//  quint64 HPack::BitIStream::bitLength() const
extern "C" Q_DECL_EXPORT
quint64 ritual_ZNK5HPack10BitIStream9bitLengthEv(
    const HPack::BitIStream *self) {
  return self->bitLength();
}

//  bool HPack::BitIStream::hasMoreBits() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK5HPack10BitIStream11hasMoreBitsEv(
    const HPack::BitIStream *self) {
  return self->hasMoreBits();
}

//  quint64 HPack::BitIStream::streamOffset() const
extern "C" Q_DECL_EXPORT
quint64 ritual_ZNK5HPack10BitIStream12streamOffsetEv(
    const HPack::BitIStream *self) {
  return self->streamOffset();
}

//  bool HPack::BitIStream::skipBits(quint64 nBits)
extern "C" Q_DECL_EXPORT
bool ritual_ZN5HPack10BitIStream8skipBitsEy(
    HPack::BitIStream *self,
    quint64 nBits) {
  return self->skipBits(nBits);
}

//  bool HPack::BitIStream::rewindOffset(quint64 nBits)
extern "C" Q_DECL_EXPORT
bool ritual_ZN5HPack10BitIStream12rewindOffsetEy(
    HPack::BitIStream *self,
    quint64 nBits) {
  return self->rewindOffset(nBits);
}

//  bool HPack::BitIStream::read(quint32 *dstPtr)
extern "C" Q_DECL_EXPORT
bool ritual_ZN5HPack10BitIStream4readEPj(
    HPack::BitIStream *self,
    quint32 *dstPtr) {
  return self->read(dstPtr);
}

//  Error HPack::BitIStream::error() const
extern "C" Q_DECL_EXPORT
HPack::BitIStream::Error ritual_ZNK5HPack10BitIStream5errorEv(
    const HPack::BitIStream *self) {
  return self->error();
}

//  void HPack::BitIStream::setError(Error newState)
extern "C" Q_DECL_EXPORT
void ritual_ZN5HPack10BitIStream8setErrorENS0_5ErrorE(
    HPack::BitIStream *self,
    HPack::BitIStream::Error newState) {
  self->setError(newState);
}

//  HPack::BitIStream::~BitIStream()
extern "C" Q_DECL_EXPORT
void ritual_ZN5HPack10BitIStreamD1Ev(HPack::BitIStream *self) {
  delete self;
}

//  quint64 HPack::BitIStream::peekBits<unsigned char>(quint64 from,
//      quint64 length, unsigned char *dstPtr) const
extern "C" Q_DECL_EXPORT
quint64 ritual_ZNK5HPack10BitIStream8peekBitsIhEEyyyPT_(
    const HPack::BitIStream *self,
    quint64 from,
    quint64 length,
    uchar *dstPtr) {
  return self->peekBits<uchar>(from, length, dstPtr);
}

//  quint64 HPack::BitIStream::peekBits<unsigned short>(quint64 from,
//      quint64 length, unsigned short *dstPtr) const
extern "C" Q_DECL_EXPORT
quint64 ritual_ZNK5HPack10BitIStream8peekBitsItEEyyyPT_(
    const HPack::BitIStream *self,
    quint64 from,
    quint64 length,
    quint16 *dstPtr) {
  return self->peekBits<quint16>(from, length, dstPtr);
}

//  quint64 HPack::BitIStream::peekBits<unsigned int>(quint64 from,
//      quint64 length, unsigned int *dstPtr) const
extern "C" Q_DECL_EXPORT
quint64 ritual_ZNK5HPack10BitIStream8peekBitsIjEEyyyPT_(
    const HPack::BitIStream *self,
    quint64 from,
    quint64 length,
    quint32 *dstPtr) {
  return self->peekBits<quint32>(from, length, dstPtr);
}

//  quint64 HPack::BitIStream::peekBits<unsigned long long>(quint64 from,
//      quint64 length, unsigned long long *dstPtr) const
extern "C" Q_DECL_EXPORT
quint64 ritual_ZNK5HPack10BitIStream8peekBitsIyEEyyyPT_(
    const HPack::BitIStream *self,
    quint64 from,
    quint64 length,
    quint64 *dstPtr) {
  return self->peekBits<quint64>(from, length, dstPtr);
}

#endif  // QT_CONFIG(http)
