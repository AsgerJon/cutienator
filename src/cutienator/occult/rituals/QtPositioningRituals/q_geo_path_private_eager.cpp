//  Written by dev_tooling.RitualGenerator from the records of
//  QtPositioning/6.12.0/QtPositioning/private/qgeopath_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtPositioning/6.12.0/QtPositioning/private/qpositioningglobal_p.h>
#include <QtPositioning/QtPositioning>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtPositioning/6.12.0/QtPositioning/private/qgeopath_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtPositioning/qgeocoordinate.h>
#include <QtCore/qlist.h>

//  QGeoPathPrivateEager::QGeoPathPrivateEager()
extern "C" Q_DECL_EXPORT
QGeoPathPrivateEager *ritual_ZN20QGeoPathPrivateEagerC1Ev() {
  return new QGeoPathPrivateEager();
}

//  QGeoPathPrivateEager::QGeoPathPrivateEager(const QList<QGeoCoordinate>
//      &path, const qreal width)
extern "C" Q_DECL_EXPORT
QGeoPathPrivateEager *ritual_ZN20QGeoPathPrivateEagerC1ERK5QListI14QGeoCoordinateEd(
    const QList<QGeoCoordinate> *path,
    qreal width) {
  return new QGeoPathPrivateEager(*path, width);
}

//  QGeoPathPrivateEager::QGeoPathPrivateEager(const QGeoPathPrivateEager
//      &other)
extern "C" Q_DECL_EXPORT
QGeoPathPrivateEager *ritual_ZN20QGeoPathPrivateEagerC1ERKS_(
    const QGeoPathPrivateEager *other) {
  return new QGeoPathPrivateEager(*other);
}

//  QGeoPathPrivateEager::~QGeoPathPrivateEager()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QGeoPathPrivateEagerD1Ev(QGeoPathPrivateEager *self) {
  delete self;
}

//  QGeoShapePrivate *QGeoPathPrivateEager::clone() const
extern "C" Q_DECL_EXPORT
QGeoShapePrivate *ritual_ZNK20QGeoPathPrivateEager5cloneEv(
    const QGeoPathPrivateEager *self) {
  return self->clone();
}

//  void QGeoPathPrivateEager::translate(double degreesLatitude, double
//      degreesLongitude)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QGeoPathPrivateEager9translateEdd(
    QGeoPathPrivateEager *self,
    double degreesLatitude,
    double degreesLongitude) {
  self->translate(degreesLatitude, degreesLongitude);
}

//  void QGeoPathPrivateEager::markDirty()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QGeoPathPrivateEager9markDirtyEv(
    QGeoPathPrivateEager *self) {
  self->markDirty();
}

//  void QGeoPathPrivateEager::addCoordinate(const QGeoCoordinate
//      &coordinate)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QGeoPathPrivateEager13addCoordinateERK14QGeoCoordinate(
    QGeoPathPrivateEager *self,
    const QGeoCoordinate *coordinate) {
  self->addCoordinate(*coordinate);
}
