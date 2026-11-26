//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore5Compat/6.12.0/QtCore5Compat/private/qbinaryjson_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore5Compat/QtCore5Compat>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore5Compat/6.12.0/QtCore5Compat/private/qbinaryjson_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore5Compat/private/qbinaryjson_p.h>
#include <QtCore/qjsonobject.h>
#include <QtCore/qjsonarray.h>
#include <QtCore/qscopeguard.h>
#include <QtCore/qvarlengtharray.h>
#include <QtCore5Compat/private/qbinaryjsonarray_p.h>
#include <QtCore5Compat/private/qbinaryjsonobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

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
//  -----------------------------------------------------------------------

//  QBinaryJsonPrivate::MutableData::MutableData(char *raw, uint a)
extern "C" Q_DECL_EXPORT
QBinaryJsonPrivate::MutableData *ritual_ZN18QBinaryJsonPrivate11MutableDataC1EPcj(
    char *raw,
    uint a) {
  return new QBinaryJsonPrivate::MutableData(raw, a);
}

//  QBinaryJsonPrivate::MutableData::MutableData(uint reserved,
//      QJsonValue::Type valueType)
extern "C" Q_DECL_EXPORT
QBinaryJsonPrivate::MutableData *ritual_ZN18QBinaryJsonPrivate11MutableDataC1EjN10QJsonValue4TypeE(
    uint reserved,
    QJsonValue::Type valueType) {
  return new QBinaryJsonPrivate::MutableData(reserved, valueType);
}

//  QBinaryJsonPrivate::MutableData::~MutableData()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QBinaryJsonPrivate11MutableDataD1Ev(
    QBinaryJsonPrivate::MutableData *self) {
  delete self;
}

//  MutableData *QBinaryJsonPrivate::MutableData::clone(const Base *b, uint
//      reserve)
extern "C" Q_DECL_EXPORT
QBinaryJsonPrivate::MutableData *ritual_ZN18QBinaryJsonPrivate11MutableData5cloneEPKNS_4BaseEj(
    QBinaryJsonPrivate::MutableData *self,
    const QBinaryJsonPrivate::Base *b,
    uint reserve) {
  return self->clone(b, reserve);
}

//  char *QBinaryJsonPrivate::MutableData::takeRawData(uint *size)
extern "C" Q_DECL_EXPORT
char *ritual_ZN18QBinaryJsonPrivate11MutableData11takeRawDataEPj(
    QBinaryJsonPrivate::MutableData *self,
    uint *size) {
  return self->takeRawData(size);
}

//  void QBinaryJsonPrivate::MutableData::compact()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QBinaryJsonPrivate11MutableData7compactEv(
    QBinaryJsonPrivate::MutableData *self) {
  self->compact();
}
