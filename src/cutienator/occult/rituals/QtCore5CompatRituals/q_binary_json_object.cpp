//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore5Compat/6.12.0/QtCore5Compat/private/qbinaryjsonobject_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore5Compat/QtCore5Compat>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore5Compat/6.12.0/QtCore5Compat/private/qbinaryjsonobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qbinaryjsonobject_p.h"
#include "qbinaryjson_p.h"
#include <qjsonobject.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt5compat/src/core5/serialization/qbinaryjsonobject.cpp, line 12, as _ZN17QBinaryJsonObjectD1Ev
inline QBinaryJsonObject::~QBinaryJsonObject()
{
    if (d && !d->ref.deref())
        delete d;
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

//  bool QBinaryJsonObject::detach(uint reserve)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QBinaryJsonObject6detachEj(
    QBinaryJsonObject *self,
    uint reserve) {
  return self->detach(reserve);
}
