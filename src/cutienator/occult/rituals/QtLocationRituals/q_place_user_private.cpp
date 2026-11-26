//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/6.12.0/QtLocation/private/qplaceuser_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtLocation/6.12.0/QtLocation/private/qlocationglobal_p.h>
#include <QtLocation/QtLocation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/6.12.0/QtLocation/private/qplaceuser_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/qplaceuser.h>
#include <QtLocation/private/qplaceuser_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtlocation/src/location/places/qplaceuser.cpp, line 12, as _ZNK17QPlaceUserPrivateeqERKS_
inline bool QPlaceUserPrivate::operator==(const QPlaceUserPrivate &other) const
{
    return userId == other.userId && name == other.name;
}
//  -----------------------------------------------------------------------

//  bool QPlaceUserPrivate::operator==(const QPlaceUserPrivate &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QPlaceUserPrivateeqERKS_(
    const QPlaceUserPrivate *self,
    const QPlaceUserPrivate *other) {
  return self->operator==(*other);
}

//  QPlaceUserPrivate::~QPlaceUserPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QPlaceUserPrivateD1Ev(QPlaceUserPrivate *self) {
  delete self;
}
