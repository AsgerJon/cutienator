//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore5Compat/6.12.0/QtCore5Compat/private/qbinaryjsonarray_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore5Compat/QtCore5Compat>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore5Compat/6.12.0/QtCore5Compat/private/qbinaryjsonarray_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qbinaryjsonarray_p.h"
#include "qbinaryjson_p.h"
#include <qjsonarray.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt5compat/src/core5/serialization/qbinaryjsonarray.cpp, line 12, as _ZN16QBinaryJsonArrayD1Ev
inline QBinaryJsonArray::~QBinaryJsonArray()
{
    if (d && !d->ref.deref())
        delete d;
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

//  bool QBinaryJsonArray::detach(uint reserve)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QBinaryJsonArray6detachEj(
    QBinaryJsonArray *self,
    uint reserve) {
  return self->detach(reserve);
}
