//  Written by dev_tooling.RitualGenerator from the records of
//  QtPositioning/6.12.0/QtPositioning/private/qgeopath_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtPositioning/6.12.0/QtPositioning/private/qpositioningglobal_p.h>
#include <QtPositioning/QtPositioning>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtPositioning/6.12.0/QtPositioning/private/qgeopath_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtPositioning/qgeocoordinate.h>
#include <QtPositioning/qgeopath.h>
#include <QtPositioning/qgeoshape.h>
#include <QtCore/qlist.h>

//  QGeoPathEager::QGeoPathEager()
extern "C" Q_DECL_EXPORT
QGeoPathEager *ritual_ZN13QGeoPathEagerC1Ev() {
  return new QGeoPathEager();
}

//  QGeoPathEager::QGeoPathEager(const QList<QGeoCoordinate> &path, const
//      qreal &width)
extern "C" Q_DECL_EXPORT
QGeoPathEager *ritual_ZN13QGeoPathEagerC1ERK5QListI14QGeoCoordinateERKd(
    const QList<QGeoCoordinate> *path,
    qreal width) {
  return new QGeoPathEager(*path, width);
}

//  QGeoPathEager::QGeoPathEager(const QGeoPath &other)
extern "C" Q_DECL_EXPORT
QGeoPathEager *ritual_ZN13QGeoPathEagerC1ERK8QGeoPath(
    const QGeoPath *other) {
  return new QGeoPathEager(*other);
}

//  QGeoPathEager::QGeoPathEager(const QGeoShape &other)
extern "C" Q_DECL_EXPORT
QGeoPathEager *ritual_ZN13QGeoPathEagerC1ERK9QGeoShape(
    const QGeoShape *other) {
  return new QGeoPathEager(*other);
}

//  QGeoPathEager::~QGeoPathEager()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGeoPathEagerD1Ev(QGeoPathEager *self) {
  delete self;
}
