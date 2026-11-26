//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore5Compat/6.12.0/QtCore5Compat/private/qbinaryjson_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore5Compat/QtCore5Compat>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore5Compat/6.12.0/QtCore5Compat/private/qbinaryjson_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstringview.h>
#include <QtCore/qstring.h>
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

//  from ../qt5compat/src/core5/serialization/qbinaryjson.cpp, line 527, as local:qbinaryjson.cpp:isValidValueOffset
namespace QBinaryJsonPrivate {
inline bool isValidValueOffset(uint offset, uint tableOffset)
{
    return offset >= sizeof(Base)
        && isAlignedOffset(offset)
        && offset + sizeof(uint) <= tableOffset;
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
//  -----------------------------------------------------------------------

//  const Entry *QBinaryJsonPrivate::Object::entryAt(uint i) const
extern "C" Q_DECL_EXPORT
const QBinaryJsonPrivate::Entry *ritual_ZNK18QBinaryJsonPrivate6Object7entryAtEj(
    const QBinaryJsonPrivate::Object *self,
    uint i) {
  return self->entryAt(i);
}

//  Entry *QBinaryJsonPrivate::Object::entryAt(uint i)
extern "C" Q_DECL_EXPORT
QBinaryJsonPrivate::Entry *ritual_ZN18QBinaryJsonPrivate6Object7entryAtEj(
    QBinaryJsonPrivate::Object *self,
    uint i) {
  return self->entryAt(i);
}

//  uint QBinaryJsonPrivate::Object::indexOf(QStringView key, bool *exists)
//      const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK18QBinaryJsonPrivate6Object7indexOfE11QStringViewPb(
    const QBinaryJsonPrivate::Object *self,
    const QString *key,
    bool *exists) {
  return self->indexOf(QStringView(*key), exists);
}

//  QBinaryJsonPrivate::Object::~Object()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QBinaryJsonPrivate6ObjectD1Ev(
    QBinaryJsonPrivate::Object *self) {
  delete self;
}
