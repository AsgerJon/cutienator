//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/qgeoroutesegment.h, Qt 6.12.0. Changes made here are lost.
#include <QtLocation/qgeoroutesegment.h>
#include <QtPositioning/qgeocoordinate.h>
#include <QtLocation/qgeomaneuver.h>
#include <QtCore/qlist.h>

//  QGeoRouteSegment::QGeoRouteSegment()
extern "C" Q_DECL_EXPORT
QGeoRouteSegment *ritual_ZN16QGeoRouteSegmentC1Ev() {
  return new QGeoRouteSegment();
}

//  QGeoRouteSegment::QGeoRouteSegment(const QGeoRouteSegment &other)
extern "C" Q_DECL_EXPORT
QGeoRouteSegment *ritual_ZN16QGeoRouteSegmentC1ERKS_(
    const QGeoRouteSegment *other) {
  return new QGeoRouteSegment(*other);
}

//  QGeoRouteSegment::~QGeoRouteSegment()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QGeoRouteSegmentD1Ev(QGeoRouteSegment *self) {
  delete self;
}

//  bool operator==(const QGeoRouteSegment &lhs, const QGeoRouteSegment &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK16QGeoRouteSegmentS1_(
    const QGeoRouteSegment *lhs,
    const QGeoRouteSegment *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QGeoRouteSegment &lhs, const QGeoRouteSegment &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK16QGeoRouteSegmentS1_(
    const QGeoRouteSegment *lhs,
    const QGeoRouteSegment *rhs) {
  return operator!=(*lhs, *rhs);
}

//  bool QGeoRouteSegment::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QGeoRouteSegment7isValidEv(const QGeoRouteSegment *self) {
  return self->isValid();
}

//  bool QGeoRouteSegment::isLegLastSegment() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QGeoRouteSegment16isLegLastSegmentEv(
    const QGeoRouteSegment *self) {
  return self->isLegLastSegment();
}

//  void QGeoRouteSegment::setNextRouteSegment(const QGeoRouteSegment
//      &routeSegment)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QGeoRouteSegment19setNextRouteSegmentERKS_(
    QGeoRouteSegment *self,
    const QGeoRouteSegment *routeSegment) {
  self->setNextRouteSegment(*routeSegment);
}

//  QGeoRouteSegment QGeoRouteSegment::nextRouteSegment() const
extern "C" Q_DECL_EXPORT
QGeoRouteSegment *ritual_ZNK16QGeoRouteSegment16nextRouteSegmentEv(
    const QGeoRouteSegment *self) {
  return new QGeoRouteSegment(self->nextRouteSegment());
}

//  void QGeoRouteSegment::setTravelTime(int secs)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QGeoRouteSegment13setTravelTimeEi(
    QGeoRouteSegment *self,
    int secs) {
  self->setTravelTime(secs);
}

//  int QGeoRouteSegment::travelTime() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QGeoRouteSegment10travelTimeEv(
    const QGeoRouteSegment *self) {
  return self->travelTime();
}

//  void QGeoRouteSegment::setDistance(qreal distance)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QGeoRouteSegment11setDistanceEd(
    QGeoRouteSegment *self,
    qreal distance) {
  self->setDistance(distance);
}

//  qreal QGeoRouteSegment::distance() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK16QGeoRouteSegment8distanceEv(const QGeoRouteSegment *self) {
  return self->distance();
}

//  void QGeoRouteSegment::setPath(const QList<QGeoCoordinate> &path)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QGeoRouteSegment7setPathERK5QListI14QGeoCoordinateE(
    QGeoRouteSegment *self,
    const QList<QGeoCoordinate> *path) {
  self->setPath(*path);
}

//  QList<QGeoCoordinate> QGeoRouteSegment::path() const
extern "C" Q_DECL_EXPORT
QList<QGeoCoordinate> *ritual_ZNK16QGeoRouteSegment4pathEv(
    const QGeoRouteSegment *self) {
  return new QList<QGeoCoordinate>(self->path());
}

//  void QGeoRouteSegment::setManeuver(const QGeoManeuver &maneuver)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QGeoRouteSegment11setManeuverERK12QGeoManeuver(
    QGeoRouteSegment *self,
    const QGeoManeuver *maneuver) {
  self->setManeuver(*maneuver);
}

//  QGeoManeuver QGeoRouteSegment::maneuver() const
extern "C" Q_DECL_EXPORT
QGeoManeuver *ritual_ZNK16QGeoRouteSegment8maneuverEv(
    const QGeoRouteSegment *self) {
  return new QGeoManeuver(self->maneuver());
}

//  bool QGeoRouteSegment::isEqual(const QGeoRouteSegment &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QGeoRouteSegment7isEqualERKS_(
    const QGeoRouteSegment *self,
    const QGeoRouteSegment *other) {
  return self->isEqual(*other);
}

//  QList<QGeoRouteSegment>::QList()
extern "C" Q_DECL_EXPORT
QList<QGeoRouteSegment> *ritual_list_make_QGeoRouteSegment() {
  return new QList<QGeoRouteSegment>();
}

//  void QList<QGeoRouteSegment>::append(const QGeoRouteSegment &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QGeoRouteSegment(
    QList<QGeoRouteSegment> *self,
    const QGeoRouteSegment *element) {
  self->append(*element);
}

//  qsizetype QList<QGeoRouteSegment>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QGeoRouteSegment(
    const QList<QGeoRouteSegment> *self) {
  return self->size();
}

//  const QGeoRouteSegment &QList<QGeoRouteSegment>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QGeoRouteSegment *ritual_list_at_QGeoRouteSegment(
    const QList<QGeoRouteSegment> *self,
    long long index) {
  return new QGeoRouteSegment(self->at(index));
}

//  QList<QGeoRouteSegment>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QGeoRouteSegment(QList<QGeoRouteSegment> *self) {
  delete self;
}
