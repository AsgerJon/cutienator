//  Written by dev_tooling.RitualGenerator from the records of
//  QtPositioning/6.12.0/QtPositioning/private/qgeocoordinate_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtPositioning/6.12.0/QtPositioning/private/qpositioningglobal_p.h>
#include <QtPositioning/QtPositioning>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtPositioning/6.12.0/QtPositioning/private/qgeocoordinate_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QGeoMercatorCoordinatePrivate::QGeoMercatorCoordinatePrivate()
extern "C" Q_DECL_EXPORT
QGeoMercatorCoordinatePrivate *ritual_ZN29QGeoMercatorCoordinatePrivateC1Ev() {
  return new QGeoMercatorCoordinatePrivate();
}

//  QGeoMercatorCoordinatePrivate::QGeoMercatorCoordinatePrivate(const
//      QGeoMercatorCoordinatePrivate &other)
extern "C" Q_DECL_EXPORT
QGeoMercatorCoordinatePrivate *ritual_ZN29QGeoMercatorCoordinatePrivateC1ERKS_(
    const QGeoMercatorCoordinatePrivate *other) {
  return new QGeoMercatorCoordinatePrivate(*other);
}

//  QGeoMercatorCoordinatePrivate::~QGeoMercatorCoordinatePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QGeoMercatorCoordinatePrivateD1Ev(
    QGeoMercatorCoordinatePrivate *self) {
  delete self;
}
