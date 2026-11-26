//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/6.12.0/QtLocation/private/qplaceratings_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtLocation/6.12.0/QtLocation/private/qlocationglobal_p.h>
#include <QtLocation/QtLocation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/6.12.0/QtLocation/private/qplaceratings_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/qplaceratings.h>
#include <QtLocation/private/qplaceratings_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtlocation/src/location/places/qplaceratings.cpp, line 12, as _ZNK20QPlaceRatingsPrivateeqERKS_
inline bool QPlaceRatingsPrivate::operator==(const QPlaceRatingsPrivate &other) const
{
    return average == other.average && maximum == other.maximum && count == other.count;
}

//  from ../qtlocation/src/location/places/qplaceratings.cpp, line 17, as _ZNK20QPlaceRatingsPrivate7isEmptyEv
inline bool QPlaceRatingsPrivate::isEmpty() const
{
    return count == 0 && average == 0 && maximum == 0;
}
//  -----------------------------------------------------------------------

//  bool QPlaceRatingsPrivate::operator==(const QPlaceRatingsPrivate &other)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QPlaceRatingsPrivateeqERKS_(
    const QPlaceRatingsPrivate *self,
    const QPlaceRatingsPrivate *other) {
  return self->operator==(*other);
}

//  bool QPlaceRatingsPrivate::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QPlaceRatingsPrivate7isEmptyEv(
    const QPlaceRatingsPrivate *self) {
  return self->isEmpty();
}

//  QPlaceRatingsPrivate::~QPlaceRatingsPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QPlaceRatingsPrivateD1Ev(QPlaceRatingsPrivate *self) {
  delete self;
}
