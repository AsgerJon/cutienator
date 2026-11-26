//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore5Compat/6.12.0/QtCore5Compat/private/qbinaryjsonarray_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore5Compat/QtCore5Compat>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore5Compat/6.12.0/QtCore5Compat/private/qbinaryjsonarray_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore5Compat/private/qbinaryjson_p.h>
#include <QtCore/qjsonobject.h>
#include <QtCore/qjsonarray.h>
#include <QtCore/qscopeguard.h>
#include <QtCore/qvarlengtharray.h>
#include <QtCore5Compat/private/qbinaryjsonarray_p.h>
#include <QtCore5Compat/private/qbinaryjsonobject_p.h>
#include <QtCore5Compat/private/qbinaryjsonarray_p.h>
#include <QtCore5Compat/private/qbinaryjson_p.h>
#include <QtCore/qjsonarray.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt5compat/src/core5/serialization/qbinaryjson.cpp, line 231, as _ZN18QBinaryJsonPrivate11MutableData7compactEv
namespace QBinaryJsonPrivate {
inline void MutableData::compact()
{
    static_assert(sizeof(Value) == sizeof(offset));

    Base *base = header->root();
    int reserve = 0;
    if (base->isObject()) {
        auto *o = static_cast<Object *>(base);
        for (uint i = 0; i < o->length(); ++i)
            reserve += o->entryAt(i)->usedStorage(o);
    } else {
        auto *a = static_cast<Array *>(base);
        for (uint i = 0; i < a->length(); ++i)
            reserve += a->at(i)->usedStorage(a);
    }

    uint size = sizeof(Base) + reserve + base->length() * sizeof(offset);
    uint alloc = sizeof(Header) + size;
    auto *h = reinterpret_cast<Header *>(malloc(alloc));
    Q_CHECK_PTR(h);
    h->tag = QJsonDocument::BinaryFormatTag;
    h->version = 1;
    Base *b = new (h->root()) Base{};
    b->size = size;
    if (header->root()->isObject())
        b->setIsObject();
    else
        b->setIsArray();
    b->setLength(base->length());
    b->tableOffset = reserve + sizeof(Array);

    uint offset = sizeof(Base);
    if (b->isObject()) {
        const auto *o = static_cast<const Object *>(base);
        auto *no = static_cast<Object *>(b);

        for (uint i = 0; i < o->length(); ++i) {
            no->table()[i] = offset;

            const Entry *e = o->entryAt(i);
            Entry *ne = no->entryAt(i);
            uint s = e->size();
            memcpy(ne, e, s);
            offset += s;
            uint dataSize = e->value.usedStorage(o);
            if (dataSize) {
                memcpy(reinterpret_cast<char *>(no) + offset, e->value.data(o), dataSize);
                ne->value.setValue(offset);
                offset += dataSize;
            }
        }
    } else {
        const auto *a = static_cast<const Array *>(base);
        auto *na = static_cast<Array *>(b);

        for (uint i = 0; i < a->length(); ++i) {
            const Value *v = a->at(i);
            Value *nv = na->at(i);
            *nv = *v;
            uint dataSize = v->usedStorage(a);
            if (dataSize) {
                memcpy(reinterpret_cast<char *>(na) + offset, v->data(a), dataSize);
                nv->setValue(offset);
                offset += dataSize;
            }
        }
    }
    Q_ASSERT(offset == uint(b->tableOffset));

    free(header);
    header = h;
    this->alloc = alloc;
    compactionCounter = 0;
}
}  // namespace QBinaryJsonPrivate

//  from ../qt5compat/src/core5/serialization/qbinaryjson.cpp, line 384, as _ZN18QBinaryJsonPrivate4Base12reserveSpaceEjjjb
namespace QBinaryJsonPrivate {
inline uint Base::reserveSpace(uint dataSize, uint posInTable, uint numItems, bool replace)
{
    Q_ASSERT(posInTable <= length());
    if (size + dataSize >= Value::MaxSize) {
        qWarning("QJson: Document too large to store in data structure %d %d %d",
                 uint(size), dataSize, Value::MaxSize);
        return 0;
    }

    offset off = tableOffset;
    // move table to new position
    if (replace) {
        memmove(reinterpret_cast<char *>(table()) + dataSize, table(), length() * sizeof(offset));
    } else {
        memmove(reinterpret_cast<char *>(table() + posInTable + numItems) + dataSize,
                table() + posInTable, (length() - posInTable) * sizeof(offset));
        memmove(reinterpret_cast<char *>(table()) + dataSize, table(), posInTable * sizeof(offset));
    }
    tableOffset += dataSize;
    for (uint i = 0; i < numItems; ++i)
        table()[posInTable + i] = off;
    size += dataSize;
    if (!replace) {
        setLength(length() + numItems);
        size += numItems * sizeof(offset);
    }
    return off;
}
}  // namespace QBinaryJsonPrivate

//  from ../qt5compat/src/core5/serialization/qbinaryjson.cpp, line 589, as _ZN18QBinaryJsonPrivate5Value12valueToStoreERK16QBinaryJsonValuej
namespace QBinaryJsonPrivate {
inline uint Value::valueToStore(const QBinaryJsonValue &v, uint offset)
{
    switch (v.type()) {
    case QJsonValue::Undefined:
    case QJsonValue::Null:
        break;
    case QJsonValue::Bool:
        return v.toBool();
    case QJsonValue::Double: {
        int c = QBinaryJsonPrivate::compressedNumber(v.toDouble());
        if (c != INT_MAX)
            return c;
    }
        Q_FALLTHROUGH();
    case QJsonValue::String:
    case QJsonValue::Array:
    case QJsonValue::Object:
        return offset;
    }
    return 0;
}
}  // namespace QBinaryJsonPrivate

//  from ../qt5compat/src/core5/serialization/qbinaryjson.cpp, line 563, as _ZN18QBinaryJsonPrivate5Value15requiredStorageERK16QBinaryJsonValuePb
namespace QBinaryJsonPrivate {
inline uint Value::requiredStorage(const QBinaryJsonValue &v, bool *compressed)
{
    *compressed = false;
    switch (v.type()) {
    case QJsonValue::Double:
        if (QBinaryJsonPrivate::compressedNumber(v.toDouble()) != INT_MAX) {
            *compressed = true;
            return 0;
        }
        return sizeof(double);
    case QJsonValue::String: {
        QString s = v.toString();
        *compressed = QBinaryJsonPrivate::useCompressed(s);
        return QBinaryJsonPrivate::qStringSize(s, *compressed);
    }
    case QJsonValue::Array:
    case QJsonValue::Object:
        return v.base ? uint(v.base->size) : sizeof(QBinaryJsonPrivate::Base);
    case QJsonValue::Undefined:
    case QJsonValue::Null:
    case QJsonValue::Bool:
        break;
    }
    return 0;
}
}  // namespace QBinaryJsonPrivate

//  from ../qt5compat/src/core5/serialization/qbinaryjson.cpp, line 477, as _ZNK18QBinaryJsonPrivate5Value11usedStorageEPKNS_4BaseE
namespace QBinaryJsonPrivate {
inline uint Value::usedStorage(const Base *b) const
{
    uint s = 0;
    switch (type()) {
    case QJsonValue::Double:
        if (!isLatinOrIntValue())
            s = sizeof(double);
        break;
    case QJsonValue::String: {
        const char *d = data(b);
        s = isLatinOrIntValue()
                ? (sizeof(ushort)
                   + qFromLittleEndian(*reinterpret_cast<const ushort *>(d)))
                : (sizeof(int)
                   + sizeof(ushort) * qFromLittleEndian(*reinterpret_cast<const int *>(d)));
        break;
    }
    case QJsonValue::Array:
    case QJsonValue::Object:
        s = base(b)->size;
        break;
    case QJsonValue::Null:
    case QJsonValue::Bool:
    default:
        break;
    }
    return alignedSize(s);
}
}  // namespace QBinaryJsonPrivate

//  from ../qt5compat/src/core5/serialization/qbinaryjsonarray.cpp, line 12, as _ZN16QBinaryJsonArrayD1Ev
inline QBinaryJsonArray::~QBinaryJsonArray()
{
    if (d && !d->ref.deref())
        delete d;
}

//  from ../qt5compat/src/core5/serialization/qbinaryjsonarray.cpp, line 56, as _ZN16QBinaryJsonArray11takeRawDataEPj
inline char *QBinaryJsonArray::takeRawData(uint *size)
{
    if (d)
        return d->takeRawData(size);
    *size = 0;
    return nullptr;
}

//  from ../qt5compat/src/core5/serialization/qbinaryjsonarray.cpp, line 92, as _ZN16QBinaryJsonArray7compactEv
inline void QBinaryJsonArray::compact()
{
    if (!d || !d->compactionCounter)
        return;

    detach();
    d->compact();
    a = static_cast<QBinaryJsonPrivate::Array *>(d->header->root());
}

//  from ../qt5compat/src/core5/serialization/qbinaryjsonarray.cpp, line 64, as _ZN16QBinaryJsonArray6detachEj
inline bool QBinaryJsonArray::detach(uint reserve)
{
    if (!d) {
        if (reserve >= QBinaryJsonPrivate::Value::MaxSize) {
            qWarning("QBinaryJson: Document too large to store in data structure");
            return false;
        }
        d = new QBinaryJsonPrivate::MutableData(reserve, QJsonValue::Array);
        a = static_cast<QBinaryJsonPrivate::Array *>(d->header->root());
        d->ref.ref();
        return true;
    }
    if (reserve == 0 && d->ref.loadRelaxed() == 1)
        return true;

    QBinaryJsonPrivate::MutableData *x = d->clone(a, reserve);
    if (!x)
        return false;
    if (x != d) {
        x->ref.ref();
        if (!d->ref.deref())
            delete d;
        d = x;
    }
    a = static_cast<QBinaryJsonPrivate::Array *>(d->header->root());
    return true;
}
//  -----------------------------------------------------------------------

//  QBinaryJsonArray::QBinaryJsonArray()
extern "C" Q_DECL_EXPORT
QBinaryJsonArray *ritual_ZN16QBinaryJsonArrayC1Ev() {
  return new QBinaryJsonArray();
}

//  QBinaryJsonArray::~QBinaryJsonArray()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QBinaryJsonArrayD1Ev(QBinaryJsonArray *self) {
  delete self;
}

//  QBinaryJsonArray::QBinaryJsonArray(QBinaryJsonArray &&other)
extern "C" Q_DECL_EXPORT
QBinaryJsonArray *ritual_ZN16QBinaryJsonArrayC1EOS_(
    QBinaryJsonArray *other) {
  return new QBinaryJsonArray(std::move(*other));
}

//  QBinaryJsonArray &QBinaryJsonArray::operator=(QBinaryJsonArray &&other)
extern "C" Q_DECL_EXPORT
QBinaryJsonArray *ritual_ZN16QBinaryJsonArrayaSEOS_(
    QBinaryJsonArray *self,
    QBinaryJsonArray *other) {
  return &(self->operator=(std::move(*other)));
}

//  char *QBinaryJsonArray::takeRawData(uint *size)
extern "C" Q_DECL_EXPORT
char *ritual_ZN16QBinaryJsonArray11takeRawDataEPj(
    QBinaryJsonArray *self,
    uint *size) {
  return self->takeRawData(size);
}

//  void QBinaryJsonArray::compact()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QBinaryJsonArray7compactEv(QBinaryJsonArray *self) {
  self->compact();
}

//  bool QBinaryJsonArray::detach(uint reserve)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QBinaryJsonArray6detachEj(
    QBinaryJsonArray *self,
    uint reserve) {
  return self->detach(reserve);
}

//  a QBinaryJsonArray a ritual of QBinaryJsonArray gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QBinaryJsonArray__QBinaryJsonArray(QBinaryJsonArray *self) {
  delete self;
}
