//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/qgeorouterequest.h, Qt 6.12.0. Changes made here are lost.
#include <QtLocation/qgeorouterequest.h>
#include <QtPositioning/qgeocoordinate.h>
#include <QtPositioning/qgeorectangle.h>
#include <QtCore/qdatetime.h>
#include <QtCore/qlist.h>
#include <QtCore/QList>
#include <QtLocation/QGeoRouteRequest>

//  QGeoRouteRequest::QGeoRouteRequest(const QList<QGeoCoordinate>
//      &waypoints)
extern "C" Q_DECL_EXPORT
QGeoRouteRequest *ritual_ZN16QGeoRouteRequestC1ERK5QListI14QGeoCoordinateE(
    const QList<QGeoCoordinate> *waypoints) {
  return new QGeoRouteRequest(*waypoints);
}

//  QGeoRouteRequest::QGeoRouteRequest(const QGeoCoordinate &origin, const
//      QGeoCoordinate &destination)
extern "C" Q_DECL_EXPORT
QGeoRouteRequest *ritual_ZN16QGeoRouteRequestC1ERK14QGeoCoordinateS2_(
    const QGeoCoordinate *origin,
    const QGeoCoordinate *destination) {
  return new QGeoRouteRequest(*origin, *destination);
}

//  QGeoRouteRequest::QGeoRouteRequest(const QGeoRouteRequest &other)
extern "C" Q_DECL_EXPORT
QGeoRouteRequest *ritual_ZN16QGeoRouteRequestC1ERKS_(
    const QGeoRouteRequest *other) {
  return new QGeoRouteRequest(*other);
}

//  QGeoRouteRequest::QGeoRouteRequest(QGeoRouteRequest &&other)
extern "C" Q_DECL_EXPORT
QGeoRouteRequest *ritual_ZN16QGeoRouteRequestC1EOS_(
    QGeoRouteRequest *other) {
  return new QGeoRouteRequest(std::move(*other));
}

//  QGeoRouteRequest::~QGeoRouteRequest()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QGeoRouteRequestD1Ev(QGeoRouteRequest *self) {
  delete self;
}

//  QGeoRouteRequest &QGeoRouteRequest::operator=(const QGeoRouteRequest
//      &other)
extern "C" Q_DECL_EXPORT
QGeoRouteRequest *ritual_ZN16QGeoRouteRequestaSERKS_(
    QGeoRouteRequest *self,
    const QGeoRouteRequest *other) {
  return &(self->operator=(*other));
}

//  QGeoRouteRequest &QGeoRouteRequest::operator=(QGeoRouteRequest &&other)
extern "C" Q_DECL_EXPORT
QGeoRouteRequest *ritual_ZN16QGeoRouteRequestaSEOS_(
    QGeoRouteRequest *self,
    QGeoRouteRequest *other) {
  return &(self->operator=(std::move(*other)));
}

//  void QGeoRouteRequest::swap(QGeoRouteRequest &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QGeoRouteRequest4swapERS_(
    QGeoRouteRequest *self,
    QGeoRouteRequest *other) {
  self->swap(*other);
}

//  bool operator==(const QGeoRouteRequest &lhs, const QGeoRouteRequest &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK16QGeoRouteRequestS1_(
    const QGeoRouteRequest *lhs,
    const QGeoRouteRequest *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QGeoRouteRequest &lhs, const QGeoRouteRequest &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK16QGeoRouteRequestS1_(
    const QGeoRouteRequest *lhs,
    const QGeoRouteRequest *rhs) {
  return operator!=(*lhs, *rhs);
}

//  void QGeoRouteRequest::setWaypoints(const QList<QGeoCoordinate>
//      &waypoints)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QGeoRouteRequest12setWaypointsERK5QListI14QGeoCoordinateE(
    QGeoRouteRequest *self,
    const QList<QGeoCoordinate> *waypoints) {
  self->setWaypoints(*waypoints);
}

//  QList<QGeoCoordinate> QGeoRouteRequest::waypoints() const
extern "C" Q_DECL_EXPORT
QList<QGeoCoordinate> *ritual_ZNK16QGeoRouteRequest9waypointsEv(
    const QGeoRouteRequest *self) {
  return new QList<QGeoCoordinate>(self->waypoints());
}

//  void QGeoRouteRequest::setExcludeAreas(const QList<QGeoRectangle> &areas)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QGeoRouteRequest15setExcludeAreasERK5QListI13QGeoRectangleE(
    QGeoRouteRequest *self,
    const QList<QGeoRectangle> *areas) {
  self->setExcludeAreas(*areas);
}

//  QList<QGeoRectangle> QGeoRouteRequest::excludeAreas() const
extern "C" Q_DECL_EXPORT
QList<QGeoRectangle> *ritual_ZNK16QGeoRouteRequest12excludeAreasEv(
    const QGeoRouteRequest *self) {
  return new QList<QGeoRectangle>(self->excludeAreas());
}

//  void QGeoRouteRequest::setNumberAlternativeRoutes(int alternatives)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QGeoRouteRequest26setNumberAlternativeRoutesEi(
    QGeoRouteRequest *self,
    int alternatives) {
  self->setNumberAlternativeRoutes(alternatives);
}

//  int QGeoRouteRequest::numberAlternativeRoutes() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QGeoRouteRequest23numberAlternativeRoutesEv(
    const QGeoRouteRequest *self) {
  return self->numberAlternativeRoutes();
}

//  void QGeoRouteRequest::setTravelModes(TravelModes travelModes)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QGeoRouteRequest14setTravelModesE6QFlagsINS_10TravelModeEE(
    QGeoRouteRequest *self,
    int travelModes) {
  self->setTravelModes(
      QFlags<QGeoRouteRequest::TravelMode>::fromInt(travelModes));
}

//  TravelModes QGeoRouteRequest::travelModes() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QGeoRouteRequest11travelModesEv(
    const QGeoRouteRequest *self) {
  return static_cast<int>(self->travelModes().toInt());
}

//  void QGeoRouteRequest::setFeatureWeight(FeatureType featureType,
//      FeatureWeight featureWeight)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QGeoRouteRequest16setFeatureWeightENS_11FeatureTypeENS_13FeatureWeightE(
    QGeoRouteRequest *self,
    QGeoRouteRequest::FeatureType featureType,
    QGeoRouteRequest::FeatureWeight featureWeight) {
  self->setFeatureWeight(featureType, featureWeight);
}

//  FeatureWeight QGeoRouteRequest::featureWeight(FeatureType featureType)
//      const
extern "C" Q_DECL_EXPORT
QGeoRouteRequest::FeatureWeight ritual_ZNK16QGeoRouteRequest13featureWeightENS_11FeatureTypeE(
    const QGeoRouteRequest *self,
    QGeoRouteRequest::FeatureType featureType) {
  return self->featureWeight(featureType);
}

//  QList<FeatureType> QGeoRouteRequest::featureTypes() const
extern "C" Q_DECL_EXPORT
QList<QGeoRouteRequest::FeatureType> *ritual_ZNK16QGeoRouteRequest12featureTypesEv(
    const QGeoRouteRequest *self) {
  return new QList<QGeoRouteRequest::FeatureType>(self->featureTypes());
}

//  void QGeoRouteRequest::setRouteOptimization(RouteOptimizations
//      optimization)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QGeoRouteRequest20setRouteOptimizationE6QFlagsINS_17RouteOptimizationEE(
    QGeoRouteRequest *self,
    int optimization) {
  self->setRouteOptimization(
      QFlags<QGeoRouteRequest::RouteOptimization>::fromInt(optimization));
}

//  RouteOptimizations QGeoRouteRequest::routeOptimization() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QGeoRouteRequest17routeOptimizationEv(
    const QGeoRouteRequest *self) {
  return static_cast<int>(self->routeOptimization().toInt());
}

//  void QGeoRouteRequest::setSegmentDetail(SegmentDetail segmentDetail)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QGeoRouteRequest16setSegmentDetailENS_13SegmentDetailE(
    QGeoRouteRequest *self,
    QGeoRouteRequest::SegmentDetail segmentDetail) {
  self->setSegmentDetail(segmentDetail);
}

//  SegmentDetail QGeoRouteRequest::segmentDetail() const
extern "C" Q_DECL_EXPORT
QGeoRouteRequest::SegmentDetail ritual_ZNK16QGeoRouteRequest13segmentDetailEv(
    const QGeoRouteRequest *self) {
  return self->segmentDetail();
}

//  void QGeoRouteRequest::setManeuverDetail(ManeuverDetail maneuverDetail)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QGeoRouteRequest17setManeuverDetailENS_14ManeuverDetailE(
    QGeoRouteRequest *self,
    QGeoRouteRequest::ManeuverDetail maneuverDetail) {
  self->setManeuverDetail(maneuverDetail);
}

//  ManeuverDetail QGeoRouteRequest::maneuverDetail() const
extern "C" Q_DECL_EXPORT
QGeoRouteRequest::ManeuverDetail ritual_ZNK16QGeoRouteRequest14maneuverDetailEv(
    const QGeoRouteRequest *self) {
  return self->maneuverDetail();
}

//  void QGeoRouteRequest::setDepartureTime(const QDateTime &departureTime)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QGeoRouteRequest16setDepartureTimeERK9QDateTime(
    QGeoRouteRequest *self,
    const QDateTime *departureTime) {
  self->setDepartureTime(*departureTime);
}

//  QDateTime QGeoRouteRequest::departureTime() const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK16QGeoRouteRequest13departureTimeEv(
    const QGeoRouteRequest *self) {
  return new QDateTime(self->departureTime());
}

//  bool QGeoRouteRequest::isEqual(const QGeoRouteRequest &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QGeoRouteRequest7isEqualERKS_(
    const QGeoRouteRequest *self,
    const QGeoRouteRequest *other) {
  return self->isEqual(*other);
}

//  a QList<QGeoRouteRequest::FeatureType> a ritual of QGeoRouteRequest gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QGeoRouteRequest__QList_QGeoRouteRequest_FeatureType(
    QList<QGeoRouteRequest::FeatureType> *self) {
  delete self;
}
