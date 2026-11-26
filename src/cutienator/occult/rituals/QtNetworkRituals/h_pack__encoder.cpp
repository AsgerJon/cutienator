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

//  from src/network/access/http2/hpack.cpp, line 95, as local:hpack.cpp:is_request_pseudo_header
namespace HPack {
namespace {
inline bool is_request_pseudo_header(QByteArrayView name)
{
    return name == ":method" || name == ":scheme" ||
           name == ":authority" || name == ":path";
}
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

//  from src/network/access/http2/hpack.cpp, line 295, as _ZN5HPack7Encoder27encodeResponsePseudoHeadersERNS_10BitOStreamERKSt6vectorINS_11HeaderFieldESaIS4_EE
namespace HPack {
inline bool Encoder::encodeResponsePseudoHeaders(BitOStream &outputStream, const HttpHeader &header)
{
    bool statusFound = false;
    for (const auto &field : header) {
        if (is_request_pseudo_header(field.name)) {
            qCritical() << "invalid pseudo-header" << field.name << "in http response";
            return false;
        }

        if (field.name == ":status") {
            if (statusFound) {
                qDebug("only one :status pseudo-header is allowed");
                return false;
            }
            if (!encodeHeaderField(outputStream, field))
                return false;
            statusFound = true;
        } else if (field.name == "cookie") {
            // "crumbs"..
        }
    }

    if (!statusFound)
        qCritical("mandatory :status pseudo-header not found");

    return statusFound;
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

//  from src/network/access/http2/hpack.cpp, line 103, as _ZN5HPack7EncoderC1Ejb
namespace HPack {
inline Encoder::Encoder(quint32 size, bool compress)
    : lookupTable(size, true /*encoder needs search index*/),
      compressStrings(compress)
{
}
}  // namespace HPack

//  from src/network/access/http2/hpack.cpp, line 109, as _ZNK5HPack7Encoder16dynamicTableSizeEv
namespace HPack {
inline quint32 Encoder::dynamicTableSize() const
{
    return lookupTable.dynamicDataSize();
}
}  // namespace HPack

//  from src/network/access/http2/hpack.cpp, line 114, as _ZNK5HPack7Encoder20dynamicTableCapacityEv
namespace HPack {
inline quint32 Encoder::dynamicTableCapacity() const
{
    return lookupTable.dynamicDataCapacity();
}
}  // namespace HPack

//  from src/network/access/http2/hpack.cpp, line 119, as _ZNK5HPack7Encoder23maxDynamicTableCapacityEv
namespace HPack {
inline quint32 Encoder::maxDynamicTableCapacity() const
{
    return lookupTable.maxDynamicDataCapacity();
}
}  // namespace HPack

//  from src/network/access/http2/hpack.cpp, line 179, as _ZN5HPack7Encoder22setMaxDynamicTableSizeEj
namespace HPack {
inline void Encoder::setMaxDynamicTableSize(quint32 size)
{
    // Up to a caller (HTTP2 protocol handler)
    // to validate this size first.
    lookupTable.setMaxDynamicTableSize(size);
}
}  // namespace HPack

//  from src/network/access/http2/hpack.cpp, line 186, as _ZN5HPack7Encoder18setCompressStringsEb
namespace HPack {
inline void Encoder::setCompressStrings(bool compress)
{
    compressStrings = compress;
}
}  // namespace HPack
//  -----------------------------------------------------------------------

//  HPack::Encoder::Encoder(quint32 maxTableSize, bool compressStrings)
extern "C" Q_DECL_EXPORT
HPack::Encoder *ritual_ZN5HPack7EncoderC1Ejb(
    quint32 maxTableSize,
    bool compressStrings) {
  return new HPack::Encoder(maxTableSize, compressStrings);
}

//  quint32 HPack::Encoder::dynamicTableSize() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK5HPack7Encoder16dynamicTableSizeEv(
    const HPack::Encoder *self) {
  return self->dynamicTableSize();
}

//  quint32 HPack::Encoder::dynamicTableCapacity() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK5HPack7Encoder20dynamicTableCapacityEv(
    const HPack::Encoder *self) {
  return self->dynamicTableCapacity();
}

//  quint32 HPack::Encoder::maxDynamicTableCapacity() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK5HPack7Encoder23maxDynamicTableCapacityEv(
    const HPack::Encoder *self) {
  return self->maxDynamicTableCapacity();
}

//  void HPack::Encoder::setMaxDynamicTableSize(quint32 size)
extern "C" Q_DECL_EXPORT
void ritual_ZN5HPack7Encoder22setMaxDynamicTableSizeEj(
    HPack::Encoder *self,
    quint32 size) {
  self->setMaxDynamicTableSize(size);
}

//  void HPack::Encoder::setCompressStrings(bool compress)
extern "C" Q_DECL_EXPORT
void ritual_ZN5HPack7Encoder18setCompressStringsEb(
    HPack::Encoder *self,
    bool compress) {
  self->setCompressStrings(compress);
}

#endif  // QT_CONFIG(http)
