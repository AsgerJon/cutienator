//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/6.12.0/QtLocation/private/qgeorouterequest_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtLocation/6.12.0/QtLocation/private/qlocationglobal_p.h>
#include <QtLocation/QtLocation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/6.12.0/QtLocation/private/qgeorouterequest_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/qgeorouterequest.h>
#include <QtLocation/private/qgeorouterequest_p.h>
#include <QtPositioning/QGeoCoordinate>
#include <QtPositioning/QGeoRectangle>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtlocation/src/location/maps/qgeorouterequest.cpp, line 450, as _ZNK23QGeoRouteRequestPrivateeqERKS_
inline bool QGeoRouteRequestPrivate::operator==(const QGeoRouteRequestPrivate &other) const
{
    return ((waypoints == other.waypoints)
            && (excludeAreas == other.excludeAreas)
            && (numberAlternativeRoutes == other.numberAlternativeRoutes)
            && (travelModes == other.travelModes)
            && (featureWeights == other.featureWeights)
            && (routeOptimization == other.routeOptimization)
            && (segmentDetail == other.segmentDetail)
            && (maneuverDetail == other.maneuverDetail));
}
//  -----------------------------------------------------------------------

//  bool QGeoRouteRequestPrivate::operator==(const QGeoRouteRequestPrivate
//      &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QGeoRouteRequestPrivateeqERKS_(
    const QGeoRouteRequestPrivate *self,
    const QGeoRouteRequestPrivate *other) {
  return self->operator==(*other);
}

//  QGeoRouteRequestPrivate::~QGeoRouteRequestPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QGeoRouteRequestPrivateD1Ev(QGeoRouteRequestPrivate *self) {
  delete self;
}
