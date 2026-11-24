//  Written by dev_tooling.RitualGenerator from the records of
//  QtPositioning/6.12.0/QtPositioning/private/qgeopolygon_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtPositioning/6.12.0/QtPositioning/private/qpositioningglobal_p.h>
#include <QtPositioning/QtPositioning>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtPositioning/6.12.0/QtPositioning/private/qgeopolygon_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtPositioning/qgeocoordinate.h>
#include <QtCore/qlist.h>

//  QGeoPolygonPrivateEager::QGeoPolygonPrivateEager()
extern "C" Q_DECL_EXPORT
QGeoPolygonPrivateEager *ritual_ZN23QGeoPolygonPrivateEagerC1Ev() {
  return new QGeoPolygonPrivateEager();
}

//  QGeoPolygonPrivateEager::QGeoPolygonPrivateEager(const
//      QList<QGeoCoordinate> &path)
extern "C" Q_DECL_EXPORT
QGeoPolygonPrivateEager *ritual_ZN23QGeoPolygonPrivateEagerC1ERK5QListI14QGeoCoordinateE(
    const QList<QGeoCoordinate> *path) {
  return new QGeoPolygonPrivateEager(*path);
}

//  QGeoPolygonPrivateEager::QGeoPolygonPrivateEager(const
//      QGeoPolygonPrivateEager &other)
extern "C" Q_DECL_EXPORT
QGeoPolygonPrivateEager *ritual_ZN23QGeoPolygonPrivateEagerC1ERKS_(
    const QGeoPolygonPrivateEager *other) {
  return new QGeoPolygonPrivateEager(*other);
}

//  QGeoPolygonPrivateEager::~QGeoPolygonPrivateEager()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QGeoPolygonPrivateEagerD1Ev(QGeoPolygonPrivateEager *self) {
  delete self;
}

//  QGeoShapePrivate *QGeoPolygonPrivateEager::clone() const
extern "C" Q_DECL_EXPORT
QGeoShapePrivate *ritual_ZNK23QGeoPolygonPrivateEager5cloneEv(
    const QGeoPolygonPrivateEager *self) {
  return self->clone();
}

//  void QGeoPolygonPrivateEager::translate(double degreesLatitude, double
//      degreesLongitude)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QGeoPolygonPrivateEager9translateEdd(
    QGeoPolygonPrivateEager *self,
    double degreesLatitude,
    double degreesLongitude) {
  self->translate(degreesLatitude, degreesLongitude);
}

//  void QGeoPolygonPrivateEager::markDirty()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QGeoPolygonPrivateEager9markDirtyEv(
    QGeoPolygonPrivateEager *self) {
  self->markDirty();
}

//  void QGeoPolygonPrivateEager::addCoordinate(const QGeoCoordinate
//      &coordinate)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QGeoPolygonPrivateEager13addCoordinateERK14QGeoCoordinate(
    QGeoPolygonPrivateEager *self,
    const QGeoCoordinate *coordinate) {
  self->addCoordinate(*coordinate);
}

//  void QGeoPolygonPrivateEager::updateBoundingBox()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QGeoPolygonPrivateEager17updateBoundingBoxEv(
    QGeoPolygonPrivateEager *self) {
  self->updateBoundingBox();
}
