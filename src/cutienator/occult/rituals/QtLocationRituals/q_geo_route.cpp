//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/qgeoroute.h, Qt 6.12.0. Changes made here are lost.
#include <QtLocation/qgeoroute.h>
#include <QtCore/qstring.h>
#include <QtLocation/qgeorouterequest.h>
#include <QtPositioning/qgeorectangle.h>
#include <QtLocation/qgeoroutesegment.h>
#include <QtPositioning/qgeocoordinate.h>
#include <QtCore/qvariant.h>
#include <QtCore/qlist.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>

//  QGeoRoute::QGeoRoute()
extern "C" Q_DECL_EXPORT
QGeoRoute *ritual_ZN9QGeoRouteC1Ev() {
  return new QGeoRoute();
}

//  QGeoRoute::QGeoRoute(const QGeoRoute &other)
extern "C" Q_DECL_EXPORT
QGeoRoute *ritual_ZN9QGeoRouteC1ERKS_(const QGeoRoute *other) {
  return new QGeoRoute(*other);
}

//  QGeoRoute::QGeoRoute(QGeoRoute &&other)
extern "C" Q_DECL_EXPORT
QGeoRoute *ritual_ZN9QGeoRouteC1EOS_(QGeoRoute *other) {
  return new QGeoRoute(std::move(*other));
}

//  QGeoRoute::~QGeoRoute()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QGeoRouteD1Ev(QGeoRoute *self) {
  delete self;
}

//  QGeoRoute &QGeoRoute::operator=(const QGeoRoute &other)
extern "C" Q_DECL_EXPORT
QGeoRoute *ritual_ZN9QGeoRouteaSERKS_(
    QGeoRoute *self,
    const QGeoRoute *other) {
  return &(self->operator=(*other));
}

//  QGeoRoute &QGeoRoute::operator=(QGeoRoute &&other)
extern "C" Q_DECL_EXPORT
QGeoRoute *ritual_ZN9QGeoRouteaSEOS_(QGeoRoute *self, QGeoRoute *other) {
  return &(self->operator=(std::move(*other)));
}

//  void QGeoRoute::swap(QGeoRoute &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QGeoRoute4swapERS_(QGeoRoute *self, QGeoRoute *other) {
  self->swap(*other);
}

//  bool operator==(const QGeoRoute &lhs, const QGeoRoute &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK9QGeoRouteS1_(const QGeoRoute *lhs, const QGeoRoute *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QGeoRoute &lhs, const QGeoRoute &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK9QGeoRouteS1_(const QGeoRoute *lhs, const QGeoRoute *rhs) {
  return operator!=(*lhs, *rhs);
}

//  void QGeoRoute::setRouteId(const QString &id)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QGeoRoute10setRouteIdERK7QString(
    QGeoRoute *self,
    const QString *id) {
  self->setRouteId(*id);
}

//  QString QGeoRoute::routeId() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QGeoRoute7routeIdEv(const QGeoRoute *self) {
  return new QString(self->routeId());
}

//  void QGeoRoute::setRequest(const QGeoRouteRequest &request)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QGeoRoute10setRequestERK16QGeoRouteRequest(
    QGeoRoute *self,
    const QGeoRouteRequest *request) {
  self->setRequest(*request);
}

//  QGeoRouteRequest QGeoRoute::request() const
extern "C" Q_DECL_EXPORT
QGeoRouteRequest *ritual_ZNK9QGeoRoute7requestEv(const QGeoRoute *self) {
  return new QGeoRouteRequest(self->request());
}

//  void QGeoRoute::setBounds(const QGeoRectangle &bounds)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QGeoRoute9setBoundsERK13QGeoRectangle(
    QGeoRoute *self,
    const QGeoRectangle *bounds) {
  self->setBounds(*bounds);
}

//  QGeoRectangle QGeoRoute::bounds() const
extern "C" Q_DECL_EXPORT
QGeoRectangle *ritual_ZNK9QGeoRoute6boundsEv(const QGeoRoute *self) {
  return new QGeoRectangle(self->bounds());
}

//  void QGeoRoute::setFirstRouteSegment(const QGeoRouteSegment
//      &routeSegment)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QGeoRoute20setFirstRouteSegmentERK16QGeoRouteSegment(
    QGeoRoute *self,
    const QGeoRouteSegment *routeSegment) {
  self->setFirstRouteSegment(*routeSegment);
}

//  QGeoRouteSegment QGeoRoute::firstRouteSegment() const
extern "C" Q_DECL_EXPORT
QGeoRouteSegment *ritual_ZNK9QGeoRoute17firstRouteSegmentEv(
    const QGeoRoute *self) {
  return new QGeoRouteSegment(self->firstRouteSegment());
}

//  qsizetype QGeoRoute::segmentsCount() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK9QGeoRoute13segmentsCountEv(const QGeoRoute *self) {
  return self->segmentsCount();
}

//  QList<QGeoRouteSegment> QGeoRoute::segments() const
extern "C" Q_DECL_EXPORT
QList<QGeoRouteSegment> *ritual_ZNK9QGeoRoute8segmentsEv(
    const QGeoRoute *self) {
  return new QList<QGeoRouteSegment>(self->segments());
}

//  void QGeoRoute::setTravelTime(int secs)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QGeoRoute13setTravelTimeEi(QGeoRoute *self, int secs) {
  self->setTravelTime(secs);
}

//  int QGeoRoute::travelTime() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QGeoRoute10travelTimeEv(const QGeoRoute *self) {
  return self->travelTime();
}

//  void QGeoRoute::setDistance(qreal distance)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QGeoRoute11setDistanceEd(QGeoRoute *self, qreal distance) {
  self->setDistance(distance);
}

//  qreal QGeoRoute::distance() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK9QGeoRoute8distanceEv(const QGeoRoute *self) {
  return self->distance();
}

//  void QGeoRoute::setTravelMode(QGeoRouteRequest::TravelMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QGeoRoute13setTravelModeEN16QGeoRouteRequest10TravelModeE(
    QGeoRoute *self,
    QGeoRouteRequest::TravelMode mode) {
  self->setTravelMode(mode);
}

//  QGeoRouteRequest::TravelMode QGeoRoute::travelMode() const
extern "C" Q_DECL_EXPORT
QGeoRouteRequest::TravelMode ritual_ZNK9QGeoRoute10travelModeEv(
    const QGeoRoute *self) {
  return self->travelMode();
}

//  void QGeoRoute::setPath(const QList<QGeoCoordinate> &path)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QGeoRoute7setPathERK5QListI14QGeoCoordinateE(
    QGeoRoute *self,
    const QList<QGeoCoordinate> *path) {
  self->setPath(*path);
}

//  QList<QGeoCoordinate> QGeoRoute::path() const
extern "C" Q_DECL_EXPORT
QList<QGeoCoordinate> *ritual_ZNK9QGeoRoute4pathEv(const QGeoRoute *self) {
  return new QList<QGeoCoordinate>(self->path());
}

//  void QGeoRoute::setRouteLegs(const QList<QGeoRoute> &legs)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QGeoRoute12setRouteLegsERK5QListIS_E(
    QGeoRoute *self,
    const QList<QGeoRoute> *legs) {
  self->setRouteLegs(*legs);
}

//  QList<QGeoRoute> QGeoRoute::routeLegs() const
extern "C" Q_DECL_EXPORT
QList<QGeoRoute> *ritual_ZNK9QGeoRoute9routeLegsEv(const QGeoRoute *self) {
  return new QList<QGeoRoute>(self->routeLegs());
}

//  void QGeoRoute::setExtendedAttributes(const QVariantMap
//      &extendedAttributes)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QGeoRoute21setExtendedAttributesERK4QMapI7QString8QVariantE(
    QGeoRoute *self,
    const QMap<QString, QVariant> *extendedAttributes) {
  self->setExtendedAttributes(*extendedAttributes);
}

//  QVariantMap QGeoRoute::extendedAttributes() const
extern "C" Q_DECL_EXPORT
QMap<QString, QVariant> *ritual_ZNK9QGeoRoute18extendedAttributesEv(
    const QGeoRoute *self) {
  return new QMap<QString, QVariant>(self->extendedAttributes());
}

//  void QGeoRoute::setLegIndex(int idx)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QGeoRoute11setLegIndexEi(QGeoRoute *self, int idx) {
  self->setLegIndex(idx);
}

//  int QGeoRoute::legIndex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QGeoRoute8legIndexEv(const QGeoRoute *self) {
  return self->legIndex();
}

//  void QGeoRoute::setOverallRoute(const QGeoRoute &route)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QGeoRoute15setOverallRouteERKS_(
    QGeoRoute *self,
    const QGeoRoute *route) {
  self->setOverallRoute(*route);
}

//  QGeoRoute QGeoRoute::overallRoute() const
extern "C" Q_DECL_EXPORT
QGeoRoute *ritual_ZNK9QGeoRoute12overallRouteEv(const QGeoRoute *self) {
  return new QGeoRoute(self->overallRoute());
}

//  QExplicitlySharedDataPointer<QGeoRoutePrivate> &QGeoRoute::d()
extern "C" Q_DECL_EXPORT
QExplicitlySharedDataPointer<QGeoRoutePrivate> *ritual_ZN9QGeoRoute1dEv(
    QGeoRoute *self) {
  return &(self->d());
}

//  const QExplicitlySharedDataPointer<QGeoRoutePrivate>
//      &QGeoRoute::const_d() const
extern "C" Q_DECL_EXPORT
const QExplicitlySharedDataPointer<QGeoRoutePrivate> *ritual_ZNK9QGeoRoute7const_dEv(
    const QGeoRoute *self) {
  return &(self->const_d());
}

//  bool QGeoRoute::isEqual(const QGeoRoute &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QGeoRoute7isEqualERKS_(
    const QGeoRoute *self,
    const QGeoRoute *other) {
  return self->isEqual(*other);
}

//  QList<QGeoRoute>::QList()
extern "C" Q_DECL_EXPORT
QList<QGeoRoute> *ritual_list_make_QGeoRoute() {
  return new QList<QGeoRoute>();
}

//  void QList<QGeoRoute>::append(const QGeoRoute &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QGeoRoute(
    QList<QGeoRoute> *self,
    const QGeoRoute *element) {
  self->append(*element);
}

//  qsizetype QList<QGeoRoute>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QGeoRoute(const QList<QGeoRoute> *self) {
  return self->size();
}

//  const QGeoRoute &QList<QGeoRoute>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QGeoRoute *ritual_list_at_QGeoRoute(
    const QList<QGeoRoute> *self,
    long long index) {
  return new QGeoRoute(self->at(index));
}

//  QList<QGeoRoute>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QGeoRoute(QList<QGeoRoute> *self) {
  delete self;
}
