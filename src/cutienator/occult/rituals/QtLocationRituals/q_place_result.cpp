//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/qplaceresult.h, Qt 6.12.0. Changes made here are lost.
#include <QtLocation/6.12.0/QtLocation/private/qlocationglobal_p.h>
#include <QtLocation/qplaceresult.h>
#include <QtLocation/qplacesearchresult.h>
#include <QtLocation/qplace.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/qplaceresult.h>
#include <QtLocation/private/qplaceresult_p.h>
#include <QtCore/qnumeric.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtlocation/src/location/places/qplaceresult.cpp, line 65, as _ZNK12QPlaceResult6d_funcEv
inline const QPlaceResultPrivate *QPlaceResult::d_func() const { return reinterpret_cast<const QPlaceResultPrivate *>(d_ptr.constData()); }
//  -----------------------------------------------------------------------

//  QPlaceResult::QPlaceResult()
extern "C" Q_DECL_EXPORT
QPlaceResult *ritual_ZN12QPlaceResultC1Ev() {
  return new QPlaceResult();
}

#if !(defined(Q_QDOC))
//  QPlaceResult::QPlaceResult(const QPlaceSearchResult &other)
extern "C" Q_DECL_EXPORT
QPlaceResult *ritual_ZN12QPlaceResultC1ERK18QPlaceSearchResult(
    const QPlaceSearchResult *other) {
  return new QPlaceResult(*other);
}
#endif  // !(defined(Q_QDOC))

//  QPlaceResult::~QPlaceResult()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QPlaceResultD1Ev(QPlaceResult *self) {
  delete self;
}

//  qreal QPlaceResult::distance() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK12QPlaceResult8distanceEv(const QPlaceResult *self) {
  return self->distance();
}

//  void QPlaceResult::setDistance(qreal distance)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QPlaceResult11setDistanceEd(
    QPlaceResult *self,
    qreal distance) {
  self->setDistance(distance);
}

//  QPlace QPlaceResult::place() const
extern "C" Q_DECL_EXPORT
QPlace *ritual_ZNK12QPlaceResult5placeEv(const QPlaceResult *self) {
  return new QPlace(self->place());
}

//  void QPlaceResult::setPlace(const QPlace &place)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QPlaceResult8setPlaceERK6QPlace(
    QPlaceResult *self,
    const QPlace *place) {
  self->setPlace(*place);
}

//  bool QPlaceResult::isSponsored() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QPlaceResult11isSponsoredEv(const QPlaceResult *self) {
  return self->isSponsored();
}

//  void QPlaceResult::setSponsored(bool sponsored)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QPlaceResult12setSponsoredEb(
    QPlaceResult *self,
    bool sponsored) {
  self->setSponsored(sponsored);
}

//  const QPlaceResultPrivate *QPlaceResult::d_func() const
extern "C" Q_DECL_EXPORT
const QPlaceResultPrivate *ritual_ZNK12QPlaceResult6d_funcEv(
    const QPlaceResult *self) {
  return self->d_func();
}
