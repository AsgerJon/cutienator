//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore5Compat/6.12.0/QtCore5Compat/private/qbinaryjsonobject_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore5Compat/QtCore5Compat>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore5Compat/6.12.0/QtCore5Compat/private/qbinaryjsonobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore5Compat/private/qbinaryjson_p.h>
#include <QtCore/qjsonobject.h>
#include <QtCore/qjsonarray.h>
#include <QtCore/qscopeguard.h>
#include <QtCore/qvarlengtharray.h>
#include <QtCore5Compat/private/qbinaryjsonarray_p.h>
#include <QtCore5Compat/private/qbinaryjsonobject_p.h>
#include <QtCore5Compat/private/qbinaryjsonobject_p.h>
#include <QtCore5Compat/private/qbinaryjson_p.h>
#include <QtCore/qjsonobject.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
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

//  from ../qt5compat/src/core5/serialization/qbinaryjson.cpp, line 413, as _ZNK18QBinaryJsonPrivate6Object7indexOfE11QStringViewPb
namespace QBinaryJsonPrivate {
inline uint Object::indexOf(QStringView key, bool *exists) const
{
    uint min = 0;
    uint n = length();
    while (n > 0) {
        uint half = n >> 1;
        uint middle = min + half;
        if (*entryAt(middle) >= key) {
            n = half;
        } else {
            min = middle + 1;
            n -= half + 1;
        }
    }
    if (min < length() && *entryAt(min) == key) {
        *exists = true;
        return min;
    }
    *exists = false;
    return min;
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

//  from ../qt5compat/src/core5/serialization/qbinaryjsonobject.cpp, line 12, as _ZN17QBinaryJsonObjectD1Ev
inline QBinaryJsonObject::~QBinaryJsonObject()
{
    if (d && !d->ref.deref())
        delete d;
}

//  from ../qt5compat/src/core5/serialization/qbinaryjsonobject.cpp, line 70, as _ZNK17QBinaryJsonObject11takeRawDataEPj
inline char *QBinaryJsonObject::takeRawData(uint *size) const
{
    if (d)
        return d->takeRawData(size);
    *size = 0;
    return nullptr;
}

//  from ../qt5compat/src/core5/serialization/qbinaryjsonobject.cpp, line 78, as _ZN17QBinaryJsonObject6detachEj
inline bool QBinaryJsonObject::detach(uint reserve)
{
    if (!d) {
        if (reserve >= QBinaryJsonPrivate::Value::MaxSize) {
            qWarning("QBinaryJson: Document too large to store in data structure");
            return false;
        }
        d = new QBinaryJsonPrivate::MutableData(reserve, QJsonValue::Object);
        o = static_cast<QBinaryJsonPrivate::Object *>(d->header->root());
        d->ref.ref();
        return true;
    }
    if (reserve == 0 && d->ref.loadRelaxed() == 1)
        return true;

    QBinaryJsonPrivate::MutableData *x = d->clone(o, reserve);
    if (!x)
        return false;
    if (x != d) {
        x->ref.ref();
        if (!d->ref.deref())
            delete d;
        d = x;
    }
    o = static_cast<QBinaryJsonPrivate::Object *>(d->header->root());
    return true;
}

//  from ../qt5compat/src/core5/serialization/qbinaryjsonobject.cpp, line 106, as _ZN17QBinaryJsonObject7compactEv
inline void QBinaryJsonObject::compact()
{
    if (!d || !d->compactionCounter)
        return;

    detach();
    d->compact();
    o = static_cast<QBinaryJsonPrivate::Object *>(d->header->root());
}
//  -----------------------------------------------------------------------

//  QBinaryJsonObject::QBinaryJsonObject()
extern "C" Q_DECL_EXPORT
QBinaryJsonObject *ritual_ZN17QBinaryJsonObjectC1Ev() {
  return new QBinaryJsonObject();
}

//  QBinaryJsonObject::~QBinaryJsonObject()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QBinaryJsonObjectD1Ev(QBinaryJsonObject *self) {
  delete self;
}

//  QBinaryJsonObject::QBinaryJsonObject(QBinaryJsonObject &&other)
extern "C" Q_DECL_EXPORT
QBinaryJsonObject *ritual_ZN17QBinaryJsonObjectC1EOS_(
    QBinaryJsonObject *other) {
  return new QBinaryJsonObject(std::move(*other));
}

//  QBinaryJsonObject &QBinaryJsonObject::operator=(QBinaryJsonObject
//      &&other)
extern "C" Q_DECL_EXPORT
QBinaryJsonObject *ritual_ZN17QBinaryJsonObjectaSEOS_(
    QBinaryJsonObject *self,
    QBinaryJsonObject *other) {
  return &(self->operator=(std::move(*other)));
}

//  char *QBinaryJsonObject::takeRawData(uint *size) const
extern "C" Q_DECL_EXPORT
char *ritual_ZNK17QBinaryJsonObject11takeRawDataEPj(
    const QBinaryJsonObject *self,
    uint *size) {
  return self->takeRawData(size);
}

//  bool QBinaryJsonObject::detach(uint reserve)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QBinaryJsonObject6detachEj(
    QBinaryJsonObject *self,
    uint reserve) {
  return self->detach(reserve);
}

//  void QBinaryJsonObject::compact()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QBinaryJsonObject7compactEv(QBinaryJsonObject *self) {
  self->compact();
}

//  a QBinaryJsonObject a ritual of QBinaryJsonObject gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QBinaryJsonObject__QBinaryJsonObject(
    QBinaryJsonObject *self) {
  delete self;
}
