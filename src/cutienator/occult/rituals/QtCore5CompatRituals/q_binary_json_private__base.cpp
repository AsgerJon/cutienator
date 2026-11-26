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
//  -----------------------------------------------------------------------

//  void QBinaryJsonPrivate::Base::setIsObject()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QBinaryJsonPrivate4Base11setIsObjectEv(
    QBinaryJsonPrivate::Base *self) {
  self->setIsObject();
}

//  bool QBinaryJsonPrivate::Base::isObject() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QBinaryJsonPrivate4Base8isObjectEv(
    const QBinaryJsonPrivate::Base *self) {
  return self->isObject();
}

//  void QBinaryJsonPrivate::Base::setIsArray()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QBinaryJsonPrivate4Base10setIsArrayEv(
    QBinaryJsonPrivate::Base *self) {
  self->setIsArray();
}

//  bool QBinaryJsonPrivate::Base::isArray() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QBinaryJsonPrivate4Base7isArrayEv(
    const QBinaryJsonPrivate::Base *self) {
  return self->isArray();
}

//  void QBinaryJsonPrivate::Base::setLength(uint length)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QBinaryJsonPrivate4Base9setLengthEj(
    QBinaryJsonPrivate::Base *self,
    uint length) {
  self->setLength(length);
}

//  uint QBinaryJsonPrivate::Base::length() const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK18QBinaryJsonPrivate4Base6lengthEv(
    const QBinaryJsonPrivate::Base *self) {
  return self->length();
}

//  offset *QBinaryJsonPrivate::Base::table()
extern "C" Q_DECL_EXPORT
QBinaryJsonPrivate::offset *ritual_ZN18QBinaryJsonPrivate4Base5tableEv(
    QBinaryJsonPrivate::Base *self) {
  return self->table();
}

//  const offset *QBinaryJsonPrivate::Base::table() const
extern "C" Q_DECL_EXPORT
const QBinaryJsonPrivate::offset *ritual_ZNK18QBinaryJsonPrivate4Base5tableEv(
    const QBinaryJsonPrivate::Base *self) {
  return self->table();
}

//  uint QBinaryJsonPrivate::Base::reserveSpace(uint dataSize, uint
//      posInTable, uint numItems, bool replace)
extern "C" Q_DECL_EXPORT
uint ritual_ZN18QBinaryJsonPrivate4Base12reserveSpaceEjjjb(
    QBinaryJsonPrivate::Base *self,
    uint dataSize,
    uint posInTable,
    uint numItems,
    bool replace) {
  return self->reserveSpace(dataSize, posInTable, numItems, replace);
}

//  QBinaryJsonPrivate::Base::~Base()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QBinaryJsonPrivate4BaseD1Ev(QBinaryJsonPrivate::Base *self) {
  delete self;
}
