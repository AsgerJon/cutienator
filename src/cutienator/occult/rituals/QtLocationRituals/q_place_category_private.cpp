//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/6.12.0/QtLocation/private/qplacecategory_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtLocation/6.12.0/QtLocation/private/qlocationglobal_p.h>
#include <QtLocation/QtLocation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/6.12.0/QtLocation/private/qplacecategory_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/qplacecategory.h>
#include <QtLocation/private/qplacecategory_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtlocation/src/location/places/qplacecategory.cpp, line 13, as _ZNK21QPlaceCategoryPrivate7isEmptyEv
inline bool QPlaceCategoryPrivate::isEmpty() const
{
    return  categoryId.isEmpty()
            && name.isEmpty()
            && icon.isEmpty()
            && QLocation::UnspecifiedVisibility == visibility;
}
//  -----------------------------------------------------------------------

//  bool QPlaceCategoryPrivate::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QPlaceCategoryPrivate7isEmptyEv(
    const QPlaceCategoryPrivate *self) {
  return self->isEmpty();
}

//  QPlaceCategoryPrivate::~QPlaceCategoryPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QPlaceCategoryPrivateD1Ev(QPlaceCategoryPrivate *self) {
  delete self;
}
