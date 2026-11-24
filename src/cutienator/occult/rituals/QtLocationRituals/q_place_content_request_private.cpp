//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/6.12.0/QtLocation/private/qplacecontentrequest_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtLocation/6.12.0/QtLocation/private/qlocationglobal_p.h>
#include <QtLocation/QtLocation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/6.12.0/QtLocation/private/qplacecontentrequest_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/private/qplacecontentrequest_p.h>
#include <QtLocation/qplacecontentrequest.h>
#include <QtPositioning/qgeocoordinate.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtlocation/src/location/places/qplacecontentrequest.cpp, line 19, as _ZN27QPlaceContentRequestPrivate5clearEv
inline void QPlaceContentRequestPrivate::clear()
{
    contentType = QPlaceContent::NoType;
    limit = -1;
}
//  -----------------------------------------------------------------------

//  void QPlaceContentRequestPrivate::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QPlaceContentRequestPrivate5clearEv(
    QPlaceContentRequestPrivate *self) {
  self->clear();
}

//  QPlaceContentRequestPrivate::~QPlaceContentRequestPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QPlaceContentRequestPrivateD1Ev(
    QPlaceContentRequestPrivate *self) {
  delete self;
}
