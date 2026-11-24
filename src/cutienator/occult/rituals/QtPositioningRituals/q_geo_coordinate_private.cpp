//  Written by dev_tooling.RitualGenerator from the records of
//  QtPositioning/6.12.0/QtPositioning/private/qgeocoordinate_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtPositioning/6.12.0/QtPositioning/private/qpositioningglobal_p.h>
#include <QtPositioning/QtPositioning>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtPositioning/6.12.0/QtPositioning/private/qgeocoordinate_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtPositioning/qgeocoordinate.h>

//  QGeoCoordinatePrivate::QGeoCoordinatePrivate()
extern "C" Q_DECL_EXPORT
QGeoCoordinatePrivate *ritual_ZN21QGeoCoordinatePrivateC1Ev() {
  return new QGeoCoordinatePrivate();
}

//  QGeoCoordinatePrivate::QGeoCoordinatePrivate(const QGeoCoordinatePrivate
//      &other)
extern "C" Q_DECL_EXPORT
QGeoCoordinatePrivate *ritual_ZN21QGeoCoordinatePrivateC1ERKS_(
    const QGeoCoordinatePrivate *other) {
  return new QGeoCoordinatePrivate(*other);
}

//  QGeoCoordinatePrivate::~QGeoCoordinatePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGeoCoordinatePrivateD1Ev(QGeoCoordinatePrivate *self) {
  delete self;
}

//  void QGeoCoordinatePrivate::atDistanceAndAzimuth(const QGeoCoordinate
//      &coord, qreal distance, qreal azimuth, double *lon, double *lat)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGeoCoordinatePrivate20atDistanceAndAzimuthERK14QGeoCoordinateddPdS3_(
    const QGeoCoordinate *coord,
    qreal distance,
    qreal azimuth,
    double *lon,
    double *lat) {
  QGeoCoordinatePrivate::atDistanceAndAzimuth(
      *coord,
      distance,
      azimuth,
      lon,
      lat);
}

//  const QGeoCoordinatePrivate *QGeoCoordinatePrivate::get(const
//      QGeoCoordinate *c)
extern "C" Q_DECL_EXPORT
const QGeoCoordinatePrivate *ritual_ZN21QGeoCoordinatePrivate3getEPK14QGeoCoordinate(
    const QGeoCoordinate *c) {
  return QGeoCoordinatePrivate::get(c);
}
