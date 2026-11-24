//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/6.12.0/QtLocation/private/qplacecontent_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtLocation/6.12.0/QtLocation/private/qlocationglobal_p.h>
#include <QtLocation/QtLocation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/6.12.0/QtLocation/private/qplacecontent_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qplacecontent.h"
#include "qplacecontent_p.h"
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtlocation/src/location/places/qplacecontent.cpp, line 20, as _ZNK20QPlaceContentPrivate7compareEPKS_
inline bool QPlaceContentPrivate::compare(const QPlaceContentPrivate *other) const
{
    return data == other->data;
}
//  -----------------------------------------------------------------------

//  QPlaceContentPrivate::QPlaceContentPrivate(QPlaceContent::Type type)
extern "C" Q_DECL_EXPORT
QPlaceContentPrivate *ritual_ZN20QPlaceContentPrivateC1EN13QPlaceContent4TypeE(
    QPlaceContent::Type type) {
  return new QPlaceContentPrivate(type);
}

//  bool QPlaceContentPrivate::compare(const QPlaceContentPrivate *other)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QPlaceContentPrivate7compareEPKS_(
    const QPlaceContentPrivate *self,
    const QPlaceContentPrivate *other) {
  return self->compare(other);
}

//  QPlaceContent::Type QPlaceContentPrivate::type() const
extern "C" Q_DECL_EXPORT
QPlaceContent::Type ritual_ZNK20QPlaceContentPrivate4typeEv(
    const QPlaceContentPrivate *self) {
  return self->type();
}

//  QPlaceContentPrivate::~QPlaceContentPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QPlaceContentPrivateD1Ev(QPlaceContentPrivate *self) {
  delete self;
}
