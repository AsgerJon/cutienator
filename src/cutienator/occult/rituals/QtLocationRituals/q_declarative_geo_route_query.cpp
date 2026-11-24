//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/6.12.0/QtLocation/private/qdeclarativegeoroutemodel_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtLocation/6.12.0/QtLocation/private/qlocationglobal_p.h>
#include <QtLocation/QtLocation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/6.12.0/QtLocation/private/qdeclarativegeoroutemodel_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtLocation/qgeorouterequest.h>
#include <QtPositioning/qgeocoordinate.h>
#include <QtPositioning/qgeorectangle.h>
#include <QtCore/qdatetime.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QDeclarativeGeoRouteQuery that Python can take functions over in. Every QDeclarativeGeoRouteQuery
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQDeclarativeGeoRouteQueryCall0)(const void *, int *);
typedef void (*CuteQDeclarativeGeoRouteQueryCall1)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDeclarativeGeoRouteQueryCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDeclarativeGeoRouteQueryCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativeGeoRouteQueryCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativeGeoRouteQueryCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativeGeoRouteQueryCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativeGeoRouteQueryCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativeGeoRouteQueryCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQDeclarativeGeoRouteQuery : public QDeclarativeGeoRouteQuery {
public:
  using QDeclarativeGeoRouteQuery::QDeclarativeGeoRouteQuery;
  void *taken[9] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[1] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QDeclarativeGeoRouteQuery::classBegin()
  void classBegin() override {
    if (taken[0]) {
      int handled = 0;
      CuteQDeclarativeGeoRouteQueryCall0 call = reinterpret_cast<CuteQDeclarativeGeoRouteQueryCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QDeclarativeGeoRouteQuery::classBegin();
  }

  //  void QDeclarativeGeoRouteQuery::componentComplete()
  void componentComplete() override {
    if (taken[1]) {
      int handled = 0;
      CuteQDeclarativeGeoRouteQueryCall1 call = reinterpret_cast<CuteQDeclarativeGeoRouteQueryCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QDeclarativeGeoRouteQuery::componentComplete();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQDeclarativeGeoRouteQueryCall2 call = reinterpret_cast<CuteQDeclarativeGeoRouteQueryCall2>(taken[2]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQDeclarativeGeoRouteQueryCall3 call = reinterpret_cast<CuteQDeclarativeGeoRouteQueryCall3>(taken[3]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQDeclarativeGeoRouteQueryCall4 call = reinterpret_cast<CuteQDeclarativeGeoRouteQueryCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQDeclarativeGeoRouteQueryCall5 call = reinterpret_cast<CuteQDeclarativeGeoRouteQueryCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQDeclarativeGeoRouteQueryCall6 call = reinterpret_cast<CuteQDeclarativeGeoRouteQueryCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[7]) {
      int handled = 0;
      CuteQDeclarativeGeoRouteQueryCall7 call = reinterpret_cast<CuteQDeclarativeGeoRouteQueryCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[8]) {
      int handled = 0;
      CuteQDeclarativeGeoRouteQueryCall8 call = reinterpret_cast<CuteQDeclarativeGeoRouteQueryCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QDeclarativeGeoRouteQuery::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK25QDeclarativeGeoRouteQuery10metaObjectEv(
    const QDeclarativeGeoRouteQuery *self) {
  return self->metaObject();
}

//  QString QDeclarativeGeoRouteQuery::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN25QDeclarativeGeoRouteQuery2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QDeclarativeGeoRouteQuery::tr(s, c, n));
}

//  QDeclarativeGeoRouteQuery::QDeclarativeGeoRouteQuery(QObject *parent)
extern "C" Q_DECL_EXPORT
QDeclarativeGeoRouteQuery *ritual_ZN25QDeclarativeGeoRouteQueryC1EP7QObject(
    QObject *parent) {
  return new CuteQDeclarativeGeoRouteQuery(parent);
}

//  QDeclarativeGeoRouteQuery::QDeclarativeGeoRouteQuery(const
//      QGeoRouteRequest &request, QObject *parent)
extern "C" Q_DECL_EXPORT
QDeclarativeGeoRouteQuery *ritual_ZN25QDeclarativeGeoRouteQueryC1ERK16QGeoRouteRequestP7QObject(
    const QGeoRouteRequest *request,
    QObject *parent) {
  return new CuteQDeclarativeGeoRouteQuery(*request, parent);
}

//  QDeclarativeGeoRouteQuery::~QDeclarativeGeoRouteQuery()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QDeclarativeGeoRouteQueryD1Ev(
    QDeclarativeGeoRouteQuery *self) {
  delete self;
}

//  void QDeclarativeGeoRouteQuery::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QDeclarativeGeoRouteQuery10classBeginEv(
    QDeclarativeGeoRouteQuery *self) {
  self->classBegin();
}

//  void QDeclarativeGeoRouteQuery::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QDeclarativeGeoRouteQuery17componentCompleteEv(
    QDeclarativeGeoRouteQuery *self) {
  self->componentComplete();
}

//  QGeoRouteRequest QDeclarativeGeoRouteQuery::routeRequest() const
extern "C" Q_DECL_EXPORT
QGeoRouteRequest *ritual_ZNK25QDeclarativeGeoRouteQuery12routeRequestEv(
    const QDeclarativeGeoRouteQuery *self) {
  return new QGeoRouteRequest(self->routeRequest());
}

//  void QDeclarativeGeoRouteQuery::setNumberAlternativeRoutes(int
//      numberAlternativeRoutes)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QDeclarativeGeoRouteQuery26setNumberAlternativeRoutesEi(
    QDeclarativeGeoRouteQuery *self,
    int numberAlternativeRoutes) {
  self->setNumberAlternativeRoutes(numberAlternativeRoutes);
}

//  int QDeclarativeGeoRouteQuery::numberAlternativeRoutes() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK25QDeclarativeGeoRouteQuery23numberAlternativeRoutesEv(
    const QDeclarativeGeoRouteQuery *self) {
  return self->numberAlternativeRoutes();
}

//  QList<QGeoCoordinate> QDeclarativeGeoRouteQuery::waypoints() const
extern "C" Q_DECL_EXPORT
QList<QGeoCoordinate> *ritual_ZNK25QDeclarativeGeoRouteQuery9waypointsEv(
    const QDeclarativeGeoRouteQuery *self) {
  return new QList<QGeoCoordinate>(self->waypoints());
}

//  void QDeclarativeGeoRouteQuery::setWaypoints(const QList<QGeoCoordinate>
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QDeclarativeGeoRouteQuery12setWaypointsERK5QListI14QGeoCoordinateE(
    QDeclarativeGeoRouteQuery *self,
    const QList<QGeoCoordinate> *value) {
  self->setWaypoints(*value);
}

//  QList<QGeoRectangle> QDeclarativeGeoRouteQuery::excludedAreas() const
extern "C" Q_DECL_EXPORT
QList<QGeoRectangle> *ritual_ZNK25QDeclarativeGeoRouteQuery13excludedAreasEv(
    const QDeclarativeGeoRouteQuery *self) {
  return new QList<QGeoRectangle>(self->excludedAreas());
}

//  void QDeclarativeGeoRouteQuery::setExcludedAreas(const
//      QList<QGeoRectangle> &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QDeclarativeGeoRouteQuery16setExcludedAreasERK5QListI13QGeoRectangleE(
    QDeclarativeGeoRouteQuery *self,
    const QList<QGeoRectangle> *value) {
  self->setExcludedAreas(*value);
}

//  void QDeclarativeGeoRouteQuery::addWaypoint(const QGeoCoordinate &w)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QDeclarativeGeoRouteQuery11addWaypointERK14QGeoCoordinate(
    QDeclarativeGeoRouteQuery *self,
    const QGeoCoordinate *w) {
  self->addWaypoint(*w);
}

//  void QDeclarativeGeoRouteQuery::removeWaypoint(const QGeoCoordinate
//      &waypoint)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QDeclarativeGeoRouteQuery14removeWaypointERK14QGeoCoordinate(
    QDeclarativeGeoRouteQuery *self,
    const QGeoCoordinate *waypoint) {
  self->removeWaypoint(*waypoint);
}

//  void QDeclarativeGeoRouteQuery::clearWaypoints()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QDeclarativeGeoRouteQuery14clearWaypointsEv(
    QDeclarativeGeoRouteQuery *self) {
  self->clearWaypoints();
}

//  void QDeclarativeGeoRouteQuery::addExcludedArea(const QGeoRectangle
//      &area)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QDeclarativeGeoRouteQuery15addExcludedAreaERK13QGeoRectangle(
    QDeclarativeGeoRouteQuery *self,
    const QGeoRectangle *area) {
  self->addExcludedArea(*area);
}

//  void QDeclarativeGeoRouteQuery::removeExcludedArea(const QGeoRectangle
//      &area)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QDeclarativeGeoRouteQuery18removeExcludedAreaERK13QGeoRectangle(
    QDeclarativeGeoRouteQuery *self,
    const QGeoRectangle *area) {
  self->removeExcludedArea(*area);
}

//  void QDeclarativeGeoRouteQuery::clearExcludedAreas()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QDeclarativeGeoRouteQuery18clearExcludedAreasEv(
    QDeclarativeGeoRouteQuery *self) {
  self->clearExcludedAreas();
}

//  void QDeclarativeGeoRouteQuery::setFeatureWeight(FeatureType featureType,
//      FeatureWeight featureWeight)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QDeclarativeGeoRouteQuery16setFeatureWeightENS_11FeatureTypeENS_13FeatureWeightE(
    QDeclarativeGeoRouteQuery *self,
    QDeclarativeGeoRouteQuery::FeatureType featureType,
    QDeclarativeGeoRouteQuery::FeatureWeight featureWeight) {
  self->setFeatureWeight(featureType, featureWeight);
}

//  int QDeclarativeGeoRouteQuery::featureWeight(FeatureType featureType)
extern "C" Q_DECL_EXPORT
int ritual_ZN25QDeclarativeGeoRouteQuery13featureWeightENS_11FeatureTypeE(
    QDeclarativeGeoRouteQuery *self,
    QDeclarativeGeoRouteQuery::FeatureType featureType) {
  return self->featureWeight(featureType);
}

//  void QDeclarativeGeoRouteQuery::resetFeatureWeights()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QDeclarativeGeoRouteQuery19resetFeatureWeightsEv(
    QDeclarativeGeoRouteQuery *self) {
  self->resetFeatureWeights();
}

//  void QDeclarativeGeoRouteQuery::setTravelModes(TravelModes travelModes)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QDeclarativeGeoRouteQuery14setTravelModesE6QFlagsINS_10TravelModeEE(
    QDeclarativeGeoRouteQuery *self,
    int travelModes) {
  self->setTravelModes(
      QFlags<QDeclarativeGeoRouteQuery::TravelMode>::fromInt(travelModes));
}

//  TravelModes QDeclarativeGeoRouteQuery::travelModes() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK25QDeclarativeGeoRouteQuery11travelModesEv(
    const QDeclarativeGeoRouteQuery *self) {
  return static_cast<int>(self->travelModes().toInt());
}

//  void QDeclarativeGeoRouteQuery::setSegmentDetail(SegmentDetail
//      segmentDetail)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QDeclarativeGeoRouteQuery16setSegmentDetailENS_13SegmentDetailE(
    QDeclarativeGeoRouteQuery *self,
    QDeclarativeGeoRouteQuery::SegmentDetail segmentDetail) {
  self->setSegmentDetail(segmentDetail);
}

//  SegmentDetail QDeclarativeGeoRouteQuery::segmentDetail() const
extern "C" Q_DECL_EXPORT
QDeclarativeGeoRouteQuery::SegmentDetail ritual_ZNK25QDeclarativeGeoRouteQuery13segmentDetailEv(
    const QDeclarativeGeoRouteQuery *self) {
  return self->segmentDetail();
}

//  void QDeclarativeGeoRouteQuery::setManeuverDetail(ManeuverDetail
//      maneuverDetail)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QDeclarativeGeoRouteQuery17setManeuverDetailENS_14ManeuverDetailE(
    QDeclarativeGeoRouteQuery *self,
    QDeclarativeGeoRouteQuery::ManeuverDetail maneuverDetail) {
  self->setManeuverDetail(maneuverDetail);
}

//  ManeuverDetail QDeclarativeGeoRouteQuery::maneuverDetail() const
extern "C" Q_DECL_EXPORT
QDeclarativeGeoRouteQuery::ManeuverDetail ritual_ZNK25QDeclarativeGeoRouteQuery14maneuverDetailEv(
    const QDeclarativeGeoRouteQuery *self) {
  return self->maneuverDetail();
}

//  void QDeclarativeGeoRouteQuery::setRouteOptimizations(RouteOptimizations
//      optimization)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QDeclarativeGeoRouteQuery21setRouteOptimizationsE6QFlagsINS_17RouteOptimizationEE(
    QDeclarativeGeoRouteQuery *self,
    int optimization) {
  self->setRouteOptimizations(
      QFlags<QDeclarativeGeoRouteQuery::RouteOptimization>::fromInt(optimization));
}

//  RouteOptimizations QDeclarativeGeoRouteQuery::routeOptimizations() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK25QDeclarativeGeoRouteQuery18routeOptimizationsEv(
    const QDeclarativeGeoRouteQuery *self) {
  return static_cast<int>(self->routeOptimizations().toInt());
}

//  void QDeclarativeGeoRouteQuery::setDepartureTime(const QDateTime
//      &departureTime)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QDeclarativeGeoRouteQuery16setDepartureTimeERK9QDateTime(
    QDeclarativeGeoRouteQuery *self,
    const QDateTime *departureTime) {
  self->setDepartureTime(*departureTime);
}

//  QDateTime QDeclarativeGeoRouteQuery::departureTime() const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK25QDeclarativeGeoRouteQuery13departureTimeEv(
    const QDeclarativeGeoRouteQuery *self) {
  return new QDateTime(self->departureTime());
}

//  void QDeclarativeGeoRouteQuery::excludedAreaCoordinateChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QDeclarativeGeoRouteQuery29excludedAreaCoordinateChangedEv(
    QDeclarativeGeoRouteQuery *self) {
  self->excludedAreaCoordinateChanged();
}

//  void QDeclarativeGeoRouteQuery::waypointChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QDeclarativeGeoRouteQuery15waypointChangedEv(
    QDeclarativeGeoRouteQuery *self) {
  self->waypointChanged();
}

//  void QDeclarativeGeoRouteQuery::doCoordinateChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QDeclarativeGeoRouteQuery19doCoordinateChangedEv(
    QDeclarativeGeoRouteQuery *self) {
  self->doCoordinateChanged();
}

//  QDeclarativeGeoRouteQuery as the QQmlParserStatus it is built on
extern "C" Q_DECL_EXPORT
QQmlParserStatus *ritual_cast_QDeclarativeGeoRouteQuery_QQmlParserStatus(
    QDeclarativeGeoRouteQuery *self) {
  return static_cast<QQmlParserStatus *>(self);
}

//  a Python function taken by a CuteQDeclarativeGeoRouteQuery, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDeclarativeGeoRouteQuery(
    QDeclarativeGeoRouteQuery *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDeclarativeGeoRouteQuery *>(self)->take(key, call);
}

//  void QDeclarativeGeoRouteQuery::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN25QDeclarativeGeoRouteQuery10classBeginEv(
    QDeclarativeGeoRouteQuery *self) {
  self->QDeclarativeGeoRouteQuery::classBegin();
}

//  void QDeclarativeGeoRouteQuery::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN25QDeclarativeGeoRouteQuery17componentCompleteEv(
    QDeclarativeGeoRouteQuery *self) {
  self->QDeclarativeGeoRouteQuery::componentComplete();
}
