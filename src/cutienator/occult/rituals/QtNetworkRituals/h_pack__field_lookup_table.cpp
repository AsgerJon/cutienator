//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/hpacktable_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtNetwork/qtnetworkglobal.h>
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#if QT_CONFIG(http)
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/hpacktable_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <vector>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/private/hpacktable_p.h>
#include <QtCore/qdebug.h>
#include <algorithm>
#include <cstddef>
#include <cstring>
#include <limits>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/network/access/http2/hpacktable.cpp, line 41, as local:hpacktable.cpp:compare
namespace HPack {
namespace {
inline int compare(const QByteArray &lhs, const QByteArray &rhs)
{
    if (const int minLen = std::min(lhs.size(), rhs.size())) {
        // We use memcmp, since strings in headers are allowed
        // to contain '\0'.
        const int cmp = std::memcmp(lhs.constData(), rhs.constData(), std::size_t(minLen));
        if (cmp)
            return cmp;
    }

    return lhs.size() - rhs.size();
}
}  // namespace
}  // namespace HPack

//  from src/network/access/http2/hpacktable.cpp, line 64, as _ZN5HPack16FieldLookupTable11SearchEntryC1EPKNS_11HeaderFieldEPKSt6vectorIS2_SaIS2_EEjPKS0_
namespace HPack {
inline FieldLookupTable::SearchEntry::SearchEntry(const HeaderField *f,
                                           const Chunk *c,
                                           quint32 o,
                                           const FieldLookupTable *t)
    : field(f),
      chunk(c),
      offset(o),
      table(t)
{
    Q_ASSERT(field);
}
}  // namespace HPack

//  from src/network/access/http2/hpacktable.cpp, line 495, as _ZN5HPack16FieldLookupTable16findInStaticPartERKNS_11HeaderFieldENS0_11CompareModeE
namespace HPack {
inline std::vector<HeaderField>::const_iterator FieldLookupTable::findInStaticPart(const HeaderField &field, CompareMode mode)
{
    const auto &table = staticPart();
    const auto acceptPos = table.begin() + 18;
    if (field.name == "accept") {
        if (mode == CompareMode::nameAndValue && field.value != "")
            return table.end();
        return acceptPos;
    }

    auto predicate = [mode](const HeaderField &lhs, const HeaderField &rhs) {
        const int cmp = compare(lhs.name, rhs.name);
        if (cmp)
            return cmp < 0;
        else if (mode == CompareMode::nameAndValue)
            return compare(lhs.value, rhs.value) < 0;
        return false;
    };

    const auto staticPos = std::lower_bound(table.begin(), acceptPos, field, predicate);
    if (staticPos != acceptPos)
        return staticPos;

    return std::lower_bound(acceptPos + 1, table.end(), field, predicate);
}
}  // namespace HPack

//  from src/network/access/http2/hpacktable.cpp, line 76, as _ZNK5HPack16FieldLookupTable11SearchEntryltERKS1_
namespace HPack {
inline bool FieldLookupTable::SearchEntry::operator < (const SearchEntry &rhs)const
{
    Q_ASSERT(field);
    Q_ASSERT(rhs.field);

    int cmp = compare(field->name, rhs.field->name);
    if (cmp)
        return cmp < 0;

    cmp = compare(field->value, rhs.field->value);
    if (cmp)
        return cmp < 0;

    if (!chunk) // 'this' is not in the searchIndex.
        return rhs.chunk;

    if (!rhs.chunk) // not in the searchIndex.
        return false;

    Q_ASSERT(table);
    Q_ASSERT(rhs.table == table);

    const quint32 leftChunkIndex = table->indexOfChunk(chunk);
    const quint32 rightChunkIndex = rhs.table->indexOfChunk(rhs.chunk);

    // Later added - smaller is chunk index (since we push_front).
    if (leftChunkIndex != rightChunkIndex)
        return leftChunkIndex > rightChunkIndex;

    // Later added - smaller is offset.
    return offset > rhs.offset;
}
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

//  from src/network/access/http2/hpacktable.cpp, line 191, as _ZNK5HPack16FieldLookupTable15numberOfEntriesEv
namespace HPack {
inline quint32 FieldLookupTable::numberOfEntries() const
{
    return quint32(staticPart().size()) + nDynamic;
}
}  // namespace HPack

//  from src/network/access/http2/hpacktable.cpp, line 196, as _ZNK5HPack16FieldLookupTable21numberOfStaticEntriesEv
namespace HPack {
inline quint32 FieldLookupTable::numberOfStaticEntries() const
{
    return quint32(staticPart().size());
}
}  // namespace HPack

//  from src/network/access/http2/hpacktable.cpp, line 201, as _ZNK5HPack16FieldLookupTable22numberOfDynamicEntriesEv
namespace HPack {
inline quint32 FieldLookupTable::numberOfDynamicEntries() const
{
    return nDynamic;
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

//  from src/network/access/http2/hpacktable.cpp, line 221, as _ZN5HPack16FieldLookupTable17clearDynamicTableEv
namespace HPack {
inline void FieldLookupTable::clearDynamicTable()
{
    searchIndex.clear();
    chunks.clear();
    begin = 0;
    end = 0;
    nDynamic = 0;
    dataSize = 0;
}
}  // namespace HPack

//  from src/network/access/http2/hpacktable.cpp, line 231, as _ZNK5HPack16FieldLookupTable12indexIsValidEj
namespace HPack {
inline bool FieldLookupTable::indexIsValid(quint32 index) const
{
    return index && index <= staticPart().size() + nDynamic;
}
}  // namespace HPack

//  from src/network/access/http2/hpacktable.cpp, line 236, as _ZNK5HPack16FieldLookupTable7indexOfERK10QByteArrayS3_
namespace HPack {
inline quint32 FieldLookupTable::indexOf(const QByteArray &name, const QByteArray &value)const
{
    // Start from the static part first:
    const auto &table = staticPart();
    const HeaderField field(name, value);
    const auto staticPos = findInStaticPart(field, CompareMode::nameAndValue);
    if (staticPos != table.end()) {
        if (staticPos->name == name && staticPos->value == value)
            return quint32(staticPos - table.begin() + 1);
    }

    // Now we have to lookup in our dynamic part ...
    if (!useIndex) {
        qCritical("lookup in dynamic table requires search index enabled");
        return 0;
    }

    const SearchEntry key(&field, nullptr, 0, this);
    const auto pos = searchIndex.lower_bound(key);
    if (pos != searchIndex.end()) {
        const HeaderField &found = *pos->field;
        if (found.name == name && found.value == value)
            return keyToIndex(*pos);
    }

    return 0;
}
}  // namespace HPack

//  from src/network/access/http2/hpacktable.cpp, line 264, as _ZNK5HPack16FieldLookupTable7indexOfERK10QByteArray
namespace HPack {
inline quint32 FieldLookupTable::indexOf(const QByteArray &name) const
{
    // Start from the static part first:
    const auto &table = staticPart();
    const HeaderField field(name, QByteArray());
    const auto staticPos = findInStaticPart(field, CompareMode::nameOnly);
    if (staticPos != table.end()) {
        if (staticPos->name == name)
            return quint32(staticPos - table.begin() + 1);
    }

    // Now we have to lookup in our dynamic part ...
    if (!useIndex) {
        qCritical("lookup in dynamic table requires search index enabled");
        return 0;
    }

    const SearchEntry key(&field, nullptr, 0, this);
    const auto pos = searchIndex.lower_bound(key);
    if (pos != searchIndex.end()) {
        const HeaderField &found = *pos->field;
        if (found.name == name)
            return keyToIndex(*pos);
    }

    return 0;
}
}  // namespace HPack

//  from src/network/access/http2/hpacktable.cpp, line 292, as _ZNK5HPack16FieldLookupTable5fieldEjP10QByteArrayS2_
namespace HPack {
inline bool FieldLookupTable::field(quint32 index, QByteArray *name, QByteArray *value) const
{
    Q_ASSERT(name);
    Q_ASSERT(value);

    if (!indexIsValid(index))
        return false;

    const auto &table = staticPart();
    if (index - 1 < table.size()) {
        *name = table[index - 1].name;
        *value = table[index - 1].value;
        return true;
    }

    index = index - 1 - quint32(table.size()) + begin;
    const auto chunkIndex = index / ChunkSize;
    Q_ASSERT(chunkIndex < chunks.size());
    const auto offset = index % ChunkSize;
    const HeaderField &found = (*chunks[chunkIndex])[offset];
    *name = found.name;
    *value = found.value;

    return true;
}
}  // namespace HPack

//  from src/network/access/http2/hpacktable.cpp, line 318, as _ZNK5HPack16FieldLookupTable9fieldNameEjP10QByteArray
namespace HPack {
inline bool FieldLookupTable::fieldName(quint32 index, QByteArray *dst) const
{
    Q_ASSERT(dst);
    return field(index, dst, &dummyDst);
}
}  // namespace HPack

//  from src/network/access/http2/hpacktable.cpp, line 324, as _ZNK5HPack16FieldLookupTable10fieldValueEjP10QByteArray
namespace HPack {
inline bool FieldLookupTable::fieldValue(quint32 index, QByteArray *dst) const
{
    Q_ASSERT(dst);
    return field(index, &dummyDst, dst);
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

//  from src/network/access/http2/hpacktable.cpp, line 426, as _ZN5HPack16FieldLookupTable10staticPartEv
namespace HPack {
inline const std::vector<HeaderField> &FieldLookupTable::staticPart()
{
    static std::vector<HeaderField> table = {
    {":authority", ""},
    {":method", "GET"},
    {":method", "POST"},
    {":path", "/"},
    {":path", "/index.html"},
    {":scheme", "http"},
    {":scheme", "https"},
    {":status", "200"},
    {":status", "204"},
    {":status", "206"},
    {":status", "304"},
    {":status", "400"},
    {":status", "404"},
    {":status", "500"},
    {"accept-charset", ""},
    {"accept-encoding", "gzip, deflate"},
    {"accept-language", ""},
    {"accept-ranges", ""},
    {"accept", ""},
    {"access-control-allow-origin", ""},
    {"age", ""},
    {"allow", ""},
    {"authorization", ""},
    {"cache-control", ""},
    {"content-disposition", ""},
    {"content-encoding", ""},
    {"content-language", ""},
    {"content-length", ""},
    {"content-location", ""},
    {"content-range", ""},
    {"content-type", ""},
    {"cookie", ""},
    {"date", ""},
    {"etag", ""},
    {"expect", ""},
    {"expires", ""},
    {"from", ""},
    {"host", ""},
    {"if-match", ""},
    {"if-modified-since", ""},
    {"if-none-match", ""},
    {"if-range", ""},
    {"if-unmodified-since", ""},
    {"last-modified", ""},
    {"link", ""},
    {"location", ""},
    {"max-forwards", ""},
    {"proxy-authenticate", ""},
    {"proxy-authorization", ""},
    {"range", ""},
    {"referer", ""},
    {"refresh", ""},
    {"retry-after", ""},
    {"server", ""},
    {"set-cookie", ""},
    {"strict-transport-security", ""},
    {"transfer-encoding", ""},
    {"user-agent", ""},
    {"vary", ""},
    {"via", ""},
    {"www-authenticate", ""}
    };

    return table;
}
}  // namespace HPack

//  from src/network/access/http2/hpacktable.cpp, line 377, as _ZNK5HPack16FieldLookupTable8frontKeyEv
namespace HPack {
inline FieldLookupTable::SearchEntry FieldLookupTable::frontKey() const
{
    Q_ASSERT(chunks.size() && end != begin);
    return SearchEntry(&front(), chunks.front().get(), begin, this);
}
}  // namespace HPack

//  from src/network/access/http2/hpacktable.cpp, line 383, as _ZNK5HPack16FieldLookupTable7backKeyEv
namespace HPack {
inline FieldLookupTable::SearchEntry FieldLookupTable::backKey() const
{
    Q_ASSERT(chunks.size() && end != begin);

    const HeaderField &field = back();
    const quint32 absIndex = end - 1;
    const auto offset = absIndex % ChunkSize;
    const auto chunk = chunks[absIndex / ChunkSize].get();

    return SearchEntry(&field, chunk, offset, this);
}
}  // namespace HPack

//  from src/network/access/http2/hpacktable.cpp, line 330, as _ZNK5HPack16FieldLookupTable5frontEv
namespace HPack {
inline const HeaderField &FieldLookupTable::front() const
{
    Q_ASSERT(nDynamic && begin != end && chunks.size());
    return (*chunks[0])[begin];
}
}  // namespace HPack

//  from src/network/access/http2/hpacktable.cpp, line 336, as _ZN5HPack16FieldLookupTable5frontEv
namespace HPack {
inline HeaderField &FieldLookupTable::front()
{
    Q_ASSERT(nDynamic && begin != end && chunks.size());
    return (*chunks[0])[begin];
}
}  // namespace HPack

//  from src/network/access/http2/hpacktable.cpp, line 342, as _ZNK5HPack16FieldLookupTable4backEv
namespace HPack {
inline const HeaderField &FieldLookupTable::back() const
{
    Q_ASSERT(nDynamic && end && end != begin);

    const quint32 absIndex = end - 1;
    const quint32 chunkIndex = absIndex / ChunkSize;
    Q_ASSERT(chunkIndex < chunks.size());
    const quint32 offset = absIndex % ChunkSize;
    return (*chunks[chunkIndex])[offset];
}
}  // namespace HPack

//  from src/network/access/http2/hpacktable.cpp, line 353, as _ZNK5HPack16FieldLookupTable12indexOfChunkEPKSt6vectorINS_11HeaderFieldESaIS2_EE
namespace HPack {
inline quint32 FieldLookupTable::indexOfChunk(const Chunk *chunk) const
{
    Q_ASSERT(chunk);

    for (size_type i = 0; i < chunks.size(); ++i) {
        if (chunks[i].get() == chunk)
            return quint32(i);
    }

    Q_UNREACHABLE_RETURN(0);
}
}  // namespace HPack

//  from src/network/access/http2/hpacktable.cpp, line 365, as _ZNK5HPack16FieldLookupTable10keyToIndexERKNS0_11SearchEntryE
namespace HPack {
inline quint32 FieldLookupTable::keyToIndex(const SearchEntry &key) const
{
    Q_ASSERT(key.chunk);

    const auto chunkIndex = indexOfChunk(key.chunk);
    const auto offset = key.offset;
    Q_ASSERT(offset < ChunkSize);
    Q_ASSERT(chunkIndex || offset >= begin);

    return quint32(offset + chunkIndex * ChunkSize - begin + 1 + staticPart().size());
}
}  // namespace HPack
//  -----------------------------------------------------------------------

//  HPack::FieldLookupTable::FieldLookupTable(quint32 maxTableSize, bool
//      useIndex)
extern "C" Q_DECL_EXPORT
HPack::FieldLookupTable *ritual_ZN5HPack16FieldLookupTableC1Ejb(
    quint32 maxTableSize,
    bool useIndex) {
  return new HPack::FieldLookupTable(maxTableSize, useIndex);
}

//  quint32 HPack::FieldLookupTable::numberOfEntries() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK5HPack16FieldLookupTable15numberOfEntriesEv(
    const HPack::FieldLookupTable *self) {
  return self->numberOfEntries();
}

//  quint32 HPack::FieldLookupTable::numberOfStaticEntries() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK5HPack16FieldLookupTable21numberOfStaticEntriesEv(
    const HPack::FieldLookupTable *self) {
  return self->numberOfStaticEntries();
}

//  quint32 HPack::FieldLookupTable::numberOfDynamicEntries() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK5HPack16FieldLookupTable22numberOfDynamicEntriesEv(
    const HPack::FieldLookupTable *self) {
  return self->numberOfDynamicEntries();
}

//  quint32 HPack::FieldLookupTable::dynamicDataSize() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK5HPack16FieldLookupTable15dynamicDataSizeEv(
    const HPack::FieldLookupTable *self) {
  return self->dynamicDataSize();
}

//  quint32 HPack::FieldLookupTable::dynamicDataCapacity() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK5HPack16FieldLookupTable19dynamicDataCapacityEv(
    const HPack::FieldLookupTable *self) {
  return self->dynamicDataCapacity();
}

//  quint32 HPack::FieldLookupTable::maxDynamicDataCapacity() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK5HPack16FieldLookupTable22maxDynamicDataCapacityEv(
    const HPack::FieldLookupTable *self) {
  return self->maxDynamicDataCapacity();
}

//  void HPack::FieldLookupTable::clearDynamicTable()
extern "C" Q_DECL_EXPORT
void ritual_ZN5HPack16FieldLookupTable17clearDynamicTableEv(
    HPack::FieldLookupTable *self) {
  self->clearDynamicTable();
}

//  bool HPack::FieldLookupTable::indexIsValid(quint32 index) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK5HPack16FieldLookupTable12indexIsValidEj(
    const HPack::FieldLookupTable *self,
    quint32 index) {
  return self->indexIsValid(index);
}

//  quint32 HPack::FieldLookupTable::indexOf(const QByteArray &name, const
//      QByteArray &value) const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK5HPack16FieldLookupTable7indexOfERK10QByteArrayS3_(
    const HPack::FieldLookupTable *self,
    const QByteArray *name,
    const QByteArray *value) {
  return self->indexOf(*name, *value);
}

//  quint32 HPack::FieldLookupTable::indexOf(const QByteArray &name) const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK5HPack16FieldLookupTable7indexOfERK10QByteArray(
    const HPack::FieldLookupTable *self,
    const QByteArray *name) {
  return self->indexOf(*name);
}

//  bool HPack::FieldLookupTable::field(quint32 index, QByteArray *name,
//      QByteArray *value) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK5HPack16FieldLookupTable5fieldEjP10QByteArrayS2_(
    const HPack::FieldLookupTable *self,
    quint32 index,
    QByteArray *name,
    QByteArray *value) {
  return self->field(index, name, value);
}

//  bool HPack::FieldLookupTable::fieldName(quint32 index, QByteArray *dst)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK5HPack16FieldLookupTable9fieldNameEjP10QByteArray(
    const HPack::FieldLookupTable *self,
    quint32 index,
    QByteArray *dst) {
  return self->fieldName(index, dst);
}

//  bool HPack::FieldLookupTable::fieldValue(quint32 index, QByteArray *dst)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK5HPack16FieldLookupTable10fieldValueEjP10QByteArray(
    const HPack::FieldLookupTable *self,
    quint32 index,
    QByteArray *dst) {
  return self->fieldValue(index, dst);
}

//  void HPack::FieldLookupTable::setMaxDynamicTableSize(quint32 size)
extern "C" Q_DECL_EXPORT
void ritual_ZN5HPack16FieldLookupTable22setMaxDynamicTableSizeEj(
    HPack::FieldLookupTable *self,
    quint32 size) {
  self->setMaxDynamicTableSize(size);
}

//  const std::vector<HeaderField> &HPack::FieldLookupTable::staticPart()
extern "C" Q_DECL_EXPORT
const std::vector<HPack::HeaderField> *ritual_ZN5HPack16FieldLookupTable10staticPartEv() {
  return &(HPack::FieldLookupTable::staticPart());
}

//  SearchEntry HPack::FieldLookupTable::frontKey() const
extern "C" Q_DECL_EXPORT
HPack::FieldLookupTable::SearchEntry *ritual_ZNK5HPack16FieldLookupTable8frontKeyEv(
    const HPack::FieldLookupTable *self) {
  return new HPack::FieldLookupTable::SearchEntry(self->frontKey());
}

//  SearchEntry HPack::FieldLookupTable::backKey() const
extern "C" Q_DECL_EXPORT
HPack::FieldLookupTable::SearchEntry *ritual_ZNK5HPack16FieldLookupTable7backKeyEv(
    const HPack::FieldLookupTable *self) {
  return new HPack::FieldLookupTable::SearchEntry(self->backKey());
}

//  const HeaderField &HPack::FieldLookupTable::front() const
extern "C" Q_DECL_EXPORT
HPack::HeaderField *ritual_ZNK5HPack16FieldLookupTable5frontEv(
    const HPack::FieldLookupTable *self) {
  return new HPack::HeaderField(self->front());
}

//  HeaderField &HPack::FieldLookupTable::front()
extern "C" Q_DECL_EXPORT
HPack::HeaderField *ritual_ZN5HPack16FieldLookupTable5frontEv(
    HPack::FieldLookupTable *self) {
  return &(self->front());
}

//  const HeaderField &HPack::FieldLookupTable::back() const
extern "C" Q_DECL_EXPORT
HPack::HeaderField *ritual_ZNK5HPack16FieldLookupTable4backEv(
    const HPack::FieldLookupTable *self) {
  return new HPack::HeaderField(self->back());
}

//  quint32 HPack::FieldLookupTable::indexOfChunk(const Chunk *chunk) const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK5HPack16FieldLookupTable12indexOfChunkEPKSt6vectorINS_11HeaderFieldESaIS2_EE(
    const HPack::FieldLookupTable *self,
    const HPack::FieldLookupTable::Chunk *chunk) {
  return self->indexOfChunk(chunk);
}

//  quint32 HPack::FieldLookupTable::keyToIndex(const SearchEntry &key) const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK5HPack16FieldLookupTable10keyToIndexERKNS0_11SearchEntryE(
    const HPack::FieldLookupTable *self,
    const HPack::FieldLookupTable::SearchEntry *key) {
  return self->keyToIndex(*key);
}

//  a HPack::FieldLookupTable::SearchEntry a ritual of
//      HPack::FieldLookupTable gave
extern "C" Q_DECL_EXPORT
void ritual_drop_HPack_FieldLookupTable__HPack_FieldLookupTable_SearchEntry(
    HPack::FieldLookupTable::SearchEntry *self) {
  delete self;
}

//  a std::vector<HPack::HeaderField>::const_iterator a ritual of
//      HPack::FieldLookupTable gave
extern "C" Q_DECL_EXPORT
void ritual_drop_HPack_FieldLookupTable__std_vector_HPack_HeaderField_const_iterator(
    std::vector<HPack::HeaderField>::const_iterator *self) {
  delete self;
}

#endif  // QT_CONFIG(http)
