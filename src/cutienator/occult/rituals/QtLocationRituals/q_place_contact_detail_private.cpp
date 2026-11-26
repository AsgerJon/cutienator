//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/6.12.0/QtLocation/private/qplacecontactdetail_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtLocation/6.12.0/QtLocation/private/qlocationglobal_p.h>
#include <QtLocation/QtLocation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/6.12.0/QtLocation/private/qplacecontactdetail_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/private/qplacecontactdetail_p.h>
#include <QtLocation/qplacecontactdetail.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtlocation/src/location/places/qplacecontactdetail.cpp, line 12, as _ZNK26QPlaceContactDetailPrivateeqERKS_
inline bool QPlaceContactDetailPrivate::operator== (const QPlaceContactDetailPrivate &other) const
{
    return label == other.label
            && value == other.value;
}
//  -----------------------------------------------------------------------

//  bool QPlaceContactDetailPrivate::operator==(const
//      QPlaceContactDetailPrivate &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK26QPlaceContactDetailPrivateeqERKS_(
    const QPlaceContactDetailPrivate *self,
    const QPlaceContactDetailPrivate *other) {
  return self->operator==(*other);
}

//  QPlaceContactDetailPrivate::~QPlaceContactDetailPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QPlaceContactDetailPrivateD1Ev(
    QPlaceContactDetailPrivate *self) {
  delete self;
}
