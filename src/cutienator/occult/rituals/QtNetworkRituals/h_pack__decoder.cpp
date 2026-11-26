//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/hpack_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtNetwork/qtnetworkglobal.h>
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#if QT_CONFIG(http)
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/hpack_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/private/hpacktable_p.h>
#include <QtCore/qdebug.h>
#include <algorithm>
#include <cstddef>
#include <cstring>
#include <limits>
#include <QtNetwork/private/bitstreams_p.h>
#include <QtNetwork/private/huffman_p.h>
#include <QtCore/qbytearray.h>
#include <limits>
#include <QtNetwork/private/bitstreams_p.h>
#include <QtNetwork/private/hpack_p.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qdebug.h>
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

//  from src/network/access/http2/hpack.cpp, line 47, as local:hpack.cpp:StreamError
namespace HPack {
namespace {
using StreamError = BitIStream::Error;
}  // namespace
}  // namespace HPack

//  from src/network/access/http2/hpacktable.cpp, line 109, as _ZN5HPack16FieldLookupTableC1Ejb
namespace HPack {
inline FieldLookupTable::FieldLookupTable(quint32 maxSize, bool use)
    : maxTableSize(maxSize),
      tableCapacity(maxSize),
      useIndex(use),
      nDynamic(),
      begin(),
      end(),
      dataSize()
{
}
}  // namespace HPack

//  from src/network/access/http2/hpacktable.cpp, line 206, as _ZNK5HPack16FieldLookupTable15dynamicDataSizeEv
namespace HPack {
inline quint32 FieldLookupTable::dynamicDataSize() const
{
    return dataSize;
}
}  // namespace HPack

//  from src/network/access/http2/hpacktable.cpp, line 211, as _ZNK5HPack16FieldLookupTable19dynamicDataCapacityEv
namespace HPack {
inline quint32 FieldLookupTable::dynamicDataCapacity() const
{
    return tableCapacity;
}
}  // namespace HPack

//  from src/network/access/http2/hpacktable.cpp, line 216, as _ZNK5HPack16FieldLookupTable22maxDynamicDataCapacityEv
namespace HPack {
inline quint32 FieldLookupTable::maxDynamicDataCapacity() const
{
    return maxTableSize;
}
}  // namespace HPack

//  from src/network/access/http2/hpacktable.cpp, line 413, as _ZN5HPack16FieldLookupTable22setMaxDynamicTableSizeEj
namespace HPack {
inline void FieldLookupTable::setMaxDynamicTableSize(quint32 size)
{
    // This is for an external user, for example, HTTP2 protocol
    // layer that can receive SETTINGS frame from its peer.
    // No validity checks here, up to this external user.
    // We update max size only, the capacity will be updated
    // later through the Dynamic Table Size Update mechanism
    // in HPack.
    maxTableSize = size;
}
}  // namespace HPack

//  from src/network/access/http2/bitstreams.cpp, line 289, as _ZNK5HPack10BitIStream5errorEv
namespace HPack {
inline BitIStream::Error BitIStream::error() const
{
    return streamError;
}
}  // namespace HPack

//  from src/network/access/http2/hpack.cpp, line 384, as _ZN5HPack7DecoderC1Ej
namespace HPack {
inline Decoder::Decoder(quint32 size)
    : lookupTable{size, false /* we do not need search index ... */}
{
}
}  // namespace HPack

//  from src/network/access/http2/hpack.cpp, line 417, as _ZNK5HPack7Decoder16dynamicTableSizeEv
namespace HPack {
inline quint32 Decoder::dynamicTableSize() const
{
    return lookupTable.dynamicDataSize();
}
}  // namespace HPack

//  from src/network/access/http2/hpack.cpp, line 422, as _ZNK5HPack7Decoder20dynamicTableCapacityEv
namespace HPack {
inline quint32 Decoder::dynamicTableCapacity() const
{
    return lookupTable.dynamicDataCapacity();
}
}  // namespace HPack

//  from src/network/access/http2/hpack.cpp, line 427, as _ZNK5HPack7Decoder23maxDynamicTableCapacityEv
namespace HPack {
inline quint32 Decoder::maxDynamicTableCapacity() const
{
    return lookupTable.maxDynamicDataCapacity();
}
}  // namespace HPack

//  from src/network/access/http2/hpack.cpp, line 432, as _ZN5HPack7Decoder22setMaxDynamicTableSizeEj
namespace HPack {
inline void Decoder::setMaxDynamicTableSize(quint32 size)
{
    // Up to a caller (HTTP2 protocol handler)
    // to validate this size first.
    lookupTable.setMaxDynamicTableSize(size);
}
}  // namespace HPack

//  from src/network/access/http2/hpack.cpp, line 439, as _ZN5HPack7Decoder20setMaxHeaderListSizeEj
namespace HPack {
inline void Decoder::setMaxHeaderListSize(quint32 size)
{
    maxHeaderListSize = size;
}
}  // namespace HPack

//  from src/network/access/http2/hpack.cpp, line 534, as _ZN5HPack7Decoder17handleStreamErrorERNS_10BitIStreamE
namespace HPack {
inline void Decoder::handleStreamError(BitIStream &inputStream)
{
    const auto errorCode(inputStream.error());
    if (errorCode == StreamError::NoError)
        return;

    // For now error handling not needed here,
    // HTTP2 layer will end with session error/COMPRESSION_ERROR.
}
}  // namespace HPack
//  -----------------------------------------------------------------------

//  HPack::Decoder::Decoder(quint32 maxTableSize)
extern "C" Q_DECL_EXPORT
HPack::Decoder *ritual_ZN5HPack7DecoderC1Ej(quint32 maxTableSize) {
  return new HPack::Decoder(maxTableSize);
}

//  const HttpHeader &HPack::Decoder::decodedHeader() const
extern "C" Q_DECL_EXPORT
const HPack::HttpHeader *ritual_ZNK5HPack7Decoder13decodedHeaderEv(
    const HPack::Decoder *self) {
  return &(self->decodedHeader());
}

//  quint32 HPack::Decoder::dynamicTableSize() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK5HPack7Decoder16dynamicTableSizeEv(
    const HPack::Decoder *self) {
  return self->dynamicTableSize();
}

//  quint32 HPack::Decoder::dynamicTableCapacity() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK5HPack7Decoder20dynamicTableCapacityEv(
    const HPack::Decoder *self) {
  return self->dynamicTableCapacity();
}

//  quint32 HPack::Decoder::maxDynamicTableCapacity() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK5HPack7Decoder23maxDynamicTableCapacityEv(
    const HPack::Decoder *self) {
  return self->maxDynamicTableCapacity();
}

//  void HPack::Decoder::setMaxDynamicTableSize(quint32 size)
extern "C" Q_DECL_EXPORT
void ritual_ZN5HPack7Decoder22setMaxDynamicTableSizeEj(
    HPack::Decoder *self,
    quint32 size) {
  self->setMaxDynamicTableSize(size);
}

//  void HPack::Decoder::setMaxHeaderListSize(quint32 size)
extern "C" Q_DECL_EXPORT
void ritual_ZN5HPack7Decoder20setMaxHeaderListSizeEj(
    HPack::Decoder *self,
    quint32 size) {
  self->setMaxHeaderListSize(size);
}

//  void HPack::Decoder::handleStreamError(BitIStream &inputStream)
extern "C" Q_DECL_EXPORT
void ritual_ZN5HPack7Decoder17handleStreamErrorERNS_10BitIStreamE(
    HPack::Decoder *self,
    HPack::BitIStream *inputStream) {
  self->handleStreamError(*inputStream);
}

#endif  // QT_CONFIG(http)
