//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/6.12.0/QtLocation/private/qgeoroute_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtLocation/6.12.0/QtLocation/private/qlocationglobal_p.h>
#include <QtLocation/QtLocation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/6.12.0/QtLocation/private/qgeoroute_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtLocation/qgeorouterequest.h>
#include <QtPositioning/qgeorectangle.h>
#include <QtPositioning/qgeocoordinate.h>
#include <QtLocation/qgeoroutesegment.h>
#include <QtLocation/qgeoroute.h>
#include <QtCore/qvariant.h>
#include <QtCore/qlist.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>

//  bool QGeoRoutePrivate::operator==(const QGeoRoutePrivate &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QGeoRoutePrivateeqERKS_(
    const QGeoRoutePrivate *self,
    const QGeoRoutePrivate *other) {
  return self->operator==(*other);
}

//  bool QGeoRoutePrivate::equals(const QGeoRoutePrivate &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QGeoRoutePrivate6equalsERKS_(
    const QGeoRoutePrivate *self,
    const QGeoRoutePrivate *other) {
  return self->equals(*other);
}

//  void QGeoRoutePrivate::setId(const QString &id)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QGeoRoutePrivate5setIdERK7QString(
    QGeoRoutePrivate *self,
    const QString *id) {
  self->setId(*id);
}

//  QString QGeoRoutePrivate::id() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QGeoRoutePrivate2idEv(const QGeoRoutePrivate *self) {
  return new QString(self->id());
}

//  void QGeoRoutePrivate::setRequest(const QGeoRouteRequest &request)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QGeoRoutePrivate10setRequestERK16QGeoRouteRequest(
    QGeoRoutePrivate *self,
    const QGeoRouteRequest *request) {
  self->setRequest(*request);
}

//  QGeoRouteRequest QGeoRoutePrivate::request() const
extern "C" Q_DECL_EXPORT
QGeoRouteRequest *ritual_ZNK16QGeoRoutePrivate7requestEv(
    const QGeoRoutePrivate *self) {
  return new QGeoRouteRequest(self->request());
}

//  void QGeoRoutePrivate::setBounds(const QGeoRectangle &bounds)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QGeoRoutePrivate9setBoundsERK13QGeoRectangle(
    QGeoRoutePrivate *self,
    const QGeoRectangle *bounds) {
  self->setBounds(*bounds);
}

//  QGeoRectangle QGeoRoutePrivate::bounds() const
extern "C" Q_DECL_EXPORT
QGeoRectangle *ritual_ZNK16QGeoRoutePrivate6boundsEv(
    const QGeoRoutePrivate *self) {
  return new QGeoRectangle(self->bounds());
}

//  void QGeoRoutePrivate::setTravelTime(int travelTime)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QGeoRoutePrivate13setTravelTimeEi(
    QGeoRoutePrivate *self,
    int travelTime) {
  self->setTravelTime(travelTime);
}

//  int QGeoRoutePrivate::travelTime() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QGeoRoutePrivate10travelTimeEv(
    const QGeoRoutePrivate *self) {
  return self->travelTime();
}

//  void QGeoRoutePrivate::setDistance(qreal distance)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QGeoRoutePrivate11setDistanceEd(
    QGeoRoutePrivate *self,
    qreal distance) {
  self->setDistance(distance);
}

//  qreal QGeoRoutePrivate::distance() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK16QGeoRoutePrivate8distanceEv(const QGeoRoutePrivate *self) {
  return self->distance();
}

//  void QGeoRoutePrivate::setTravelMode(QGeoRouteRequest::TravelMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QGeoRoutePrivate13setTravelModeEN16QGeoRouteRequest10TravelModeE(
    QGeoRoutePrivate *self,
    QGeoRouteRequest::TravelMode mode) {
  self->setTravelMode(mode);
}

//  QGeoRouteRequest::TravelMode QGeoRoutePrivate::travelMode() const
extern "C" Q_DECL_EXPORT
QGeoRouteRequest::TravelMode ritual_ZNK16QGeoRoutePrivate10travelModeEv(
    const QGeoRoutePrivate *self) {
  return self->travelMode();
}

//  void QGeoRoutePrivate::setPath(const QList<QGeoCoordinate> &path)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QGeoRoutePrivate7setPathERK5QListI14QGeoCoordinateE(
    QGeoRoutePrivate *self,
    const QList<QGeoCoordinate> *path) {
  self->setPath(*path);
}

//  QList<QGeoCoordinate> QGeoRoutePrivate::path() const
extern "C" Q_DECL_EXPORT
QList<QGeoCoordinate> *ritual_ZNK16QGeoRoutePrivate4pathEv(
    const QGeoRoutePrivate *self) {
  return new QList<QGeoCoordinate>(self->path());
}

//  void QGeoRoutePrivate::setFirstSegment(const QGeoRouteSegment
//      &firstSegment)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QGeoRoutePrivate15setFirstSegmentERK16QGeoRouteSegment(
    QGeoRoutePrivate *self,
    const QGeoRouteSegment *firstSegment) {
  self->setFirstSegment(*firstSegment);
}

//  QGeoRouteSegment QGeoRoutePrivate::firstSegment() const
extern "C" Q_DECL_EXPORT
QGeoRouteSegment *ritual_ZNK16QGeoRoutePrivate12firstSegmentEv(
    const QGeoRoutePrivate *self) {
  return new QGeoRouteSegment(self->firstSegment());
}

//  int QGeoRoutePrivate::segmentsCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QGeoRoutePrivate13segmentsCountEv(
    const QGeoRoutePrivate *self) {
  return self->segmentsCount();
}

//  QList<QGeoRouteSegment> QGeoRoutePrivate::segments() const
extern "C" Q_DECL_EXPORT
QList<QGeoRouteSegment> *ritual_ZNK16QGeoRoutePrivate8segmentsEv(
    const QGeoRoutePrivate *self) {
  return new QList<QGeoRouteSegment>(self->segments());
}

//  void QGeoRoutePrivate::setRouteLegs(const QList<QGeoRoute> &legs)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QGeoRoutePrivate12setRouteLegsERK5QListI9QGeoRouteE(
    QGeoRoutePrivate *self,
    const QList<QGeoRoute> *legs) {
  self->setRouteLegs(*legs);
}

//  QList<QGeoRoute> QGeoRoutePrivate::routeLegs() const
extern "C" Q_DECL_EXPORT
QList<QGeoRoute> *ritual_ZNK16QGeoRoutePrivate9routeLegsEv(
    const QGeoRoutePrivate *self) {
  return new QList<QGeoRoute>(self->routeLegs());
}

//  void QGeoRoutePrivate::setExtendedAttributes(const QVariantMap
//      &extendedAttributes)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QGeoRoutePrivate21setExtendedAttributesERK4QMapI7QString8QVariantE(
    QGeoRoutePrivate *self,
    const QMap<QString, QVariant> *extendedAttributes) {
  self->setExtendedAttributes(*extendedAttributes);
}

//  QVariantMap QGeoRoutePrivate::extendedAttributes() const
extern "C" Q_DECL_EXPORT
QMap<QString, QVariant> *ritual_ZNK16QGeoRoutePrivate18extendedAttributesEv(
    const QGeoRoutePrivate *self) {
  return new QMap<QString, QVariant>(self->extendedAttributes());
}

//  void QGeoRoutePrivate::setLegIndex(int idx)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QGeoRoutePrivate11setLegIndexEi(
    QGeoRoutePrivate *self,
    int idx) {
  self->setLegIndex(idx);
}

//  int QGeoRoutePrivate::legIndex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QGeoRoutePrivate8legIndexEv(const QGeoRoutePrivate *self) {
  return self->legIndex();
}

//  void QGeoRoutePrivate::setContainingRoute(const QGeoRoute &route)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QGeoRoutePrivate18setContainingRouteERK9QGeoRoute(
    QGeoRoutePrivate *self,
    const QGeoRoute *route) {
  self->setContainingRoute(*route);
}

//  QGeoRoute QGeoRoutePrivate::containingRoute() const
extern "C" Q_DECL_EXPORT
QGeoRoute *ritual_ZNK16QGeoRoutePrivate15containingRouteEv(
    const QGeoRoutePrivate *self) {
  return new QGeoRoute(self->containingRoute());
}
