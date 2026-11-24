//  Written by dev_tooling.RitualGenerator from the records of
//  QtPositioning/6.12.0/QtPositioning/private/qgeopolygon_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtPositioning/6.12.0/QtPositioning/private/qpositioningglobal_p.h>
#include <QtPositioning/QtPositioning>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtPositioning/6.12.0/QtPositioning/private/qgeopolygon_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtPositioning/qgeocoordinate.h>
#include <QtPositioning/qgeopolygon.h>
#include <QtPositioning/qgeoshape.h>
#include <QtCore/qlist.h>

//  QGeoPolygonEager::QGeoPolygonEager()
extern "C" Q_DECL_EXPORT
QGeoPolygonEager *ritual_ZN16QGeoPolygonEagerC1Ev() {
  return new QGeoPolygonEager();
}

//  QGeoPolygonEager::QGeoPolygonEager(const QList<QGeoCoordinate> &path)
extern "C" Q_DECL_EXPORT
QGeoPolygonEager *ritual_ZN16QGeoPolygonEagerC1ERK5QListI14QGeoCoordinateE(
    const QList<QGeoCoordinate> *path) {
  return new QGeoPolygonEager(*path);
}

//  QGeoPolygonEager::QGeoPolygonEager(const QGeoPolygon &other)
extern "C" Q_DECL_EXPORT
QGeoPolygonEager *ritual_ZN16QGeoPolygonEagerC1ERK11QGeoPolygon(
    const QGeoPolygon *other) {
  return new QGeoPolygonEager(*other);
}

//  QGeoPolygonEager::QGeoPolygonEager(const QGeoShape &other)
extern "C" Q_DECL_EXPORT
QGeoPolygonEager *ritual_ZN16QGeoPolygonEagerC1ERK9QGeoShape(
    const QGeoShape *other) {
  return new QGeoPolygonEager(*other);
}

//  QGeoPolygonEager::~QGeoPolygonEager()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QGeoPolygonEagerD1Ev(QGeoPolygonEager *self) {
  delete self;
}
