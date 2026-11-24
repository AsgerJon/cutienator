//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/6.12.0/QtLocation/private/qgeoroutesegment_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtLocation/6.12.0/QtLocation/private/qlocationglobal_p.h>
#include <QtLocation/QtLocation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/6.12.0/QtLocation/private/qgeoroutesegment_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtPositioning/qgeocoordinate.h>
#include <QtLocation/qgeomaneuver.h>
#include <QtCore/qlist.h>

//  QGeoRouteSegmentPrivate::QGeoRouteSegmentPrivate()
extern "C" Q_DECL_EXPORT
QGeoRouteSegmentPrivate *ritual_ZN23QGeoRouteSegmentPrivateC1Ev() {
  return new QGeoRouteSegmentPrivate();
}

//  bool QGeoRouteSegmentPrivate::valid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QGeoRouteSegmentPrivate5validEv(
    const QGeoRouteSegmentPrivate *self) {
  return self->valid();
}

//  void QGeoRouteSegmentPrivate::setValid(bool valid)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QGeoRouteSegmentPrivate8setValidEb(
    QGeoRouteSegmentPrivate *self,
    bool valid) {
  self->setValid(valid);
}

//  bool QGeoRouteSegmentPrivate::isLegLastSegment() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QGeoRouteSegmentPrivate16isLegLastSegmentEv(
    const QGeoRouteSegmentPrivate *self) {
  return self->isLegLastSegment();
}

//  void QGeoRouteSegmentPrivate::setLegLastSegment(bool lastSegment)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QGeoRouteSegmentPrivate17setLegLastSegmentEb(
    QGeoRouteSegmentPrivate *self,
    bool lastSegment) {
  self->setLegLastSegment(lastSegment);
}

//  int QGeoRouteSegmentPrivate::travelTime() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK23QGeoRouteSegmentPrivate10travelTimeEv(
    const QGeoRouteSegmentPrivate *self) {
  return self->travelTime();
}

//  void QGeoRouteSegmentPrivate::setTravelTime(int travelTime)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QGeoRouteSegmentPrivate13setTravelTimeEi(
    QGeoRouteSegmentPrivate *self,
    int travelTime) {
  self->setTravelTime(travelTime);
}

//  qreal QGeoRouteSegmentPrivate::distance() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK23QGeoRouteSegmentPrivate8distanceEv(
    const QGeoRouteSegmentPrivate *self) {
  return self->distance();
}

//  void QGeoRouteSegmentPrivate::setDistance(qreal distance)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QGeoRouteSegmentPrivate11setDistanceEd(
    QGeoRouteSegmentPrivate *self,
    qreal distance) {
  self->setDistance(distance);
}

//  QList<QGeoCoordinate> QGeoRouteSegmentPrivate::path() const
extern "C" Q_DECL_EXPORT
QList<QGeoCoordinate> *ritual_ZNK23QGeoRouteSegmentPrivate4pathEv(
    const QGeoRouteSegmentPrivate *self) {
  return new QList<QGeoCoordinate>(self->path());
}

//  void QGeoRouteSegmentPrivate::setPath(const QList<QGeoCoordinate> &path)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QGeoRouteSegmentPrivate7setPathERK5QListI14QGeoCoordinateE(
    QGeoRouteSegmentPrivate *self,
    const QList<QGeoCoordinate> *path) {
  self->setPath(*path);
}

//  QGeoManeuver QGeoRouteSegmentPrivate::maneuver() const
extern "C" Q_DECL_EXPORT
QGeoManeuver *ritual_ZNK23QGeoRouteSegmentPrivate8maneuverEv(
    const QGeoRouteSegmentPrivate *self) {
  return new QGeoManeuver(self->maneuver());
}

//  void QGeoRouteSegmentPrivate::setManeuver(const QGeoManeuver &maneuver)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QGeoRouteSegmentPrivate11setManeuverERK12QGeoManeuver(
    QGeoRouteSegmentPrivate *self,
    const QGeoManeuver *maneuver) {
  self->setManeuver(*maneuver);
}

//  QGeoRouteSegmentPrivate::~QGeoRouteSegmentPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QGeoRouteSegmentPrivateD1Ev(QGeoRouteSegmentPrivate *self) {
  delete self;
}
