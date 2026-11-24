//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/qgeoroutingmanagerengine.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtLocation/qgeoroutingmanagerengine.h>
#include <QtCore/qstring.h>
#include <QtLocation/qgeorouterequest.h>
#include <QtLocation/qgeoroute.h>
#include <QtPositioning/qgeocoordinate.h>
#include <QtCore/qlocale.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QGeoRoutingManagerEngine that Python can take functions over in. Every QGeoRoutingManagerEngine
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQGeoRoutingManagerEngineCall0)(const void *, const QGeoRouteRequest *, int *);
typedef void * (*CuteQGeoRoutingManagerEngineCall1)(const void *, const QGeoRoute *, const QGeoCoordinate *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQGeoRoutingManagerEngineCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQGeoRoutingManagerEngineCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGeoRoutingManagerEngineCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGeoRoutingManagerEngineCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGeoRoutingManagerEngineCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGeoRoutingManagerEngineCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGeoRoutingManagerEngineCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQGeoRoutingManagerEngine : public QGeoRoutingManagerEngine {
public:
  using QGeoRoutingManagerEngine::QGeoRoutingManagerEngine;
  void *taken[9] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN24QGeoRoutingManagerEngine14calculateRouteERK16QGeoRouteRequest")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QGeoRoutingManagerEngine11updateRouteERK9QGeoRouteRK14QGeoCoordinate")) {
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

  //  QGeoRouteReply *QGeoRoutingManagerEngine::calculateRoute(const
  //      QGeoRouteRequest &request)
  QGeoRouteReply *calculateRoute(const QGeoRouteRequest &request) override {
    if (taken[0]) {
      int handled = 0;
      CuteQGeoRoutingManagerEngineCall0 call = reinterpret_cast<CuteQGeoRoutingManagerEngineCall0>(taken[0]);
      void * given = call(this, &request, &handled);
      if (handled) return static_cast<QGeoRouteReply *>(given);
    }
    return {};
  }

  //  QGeoRouteReply *QGeoRoutingManagerEngine::updateRoute(const QGeoRoute
  //      &route, const QGeoCoordinate &position)
  QGeoRouteReply *updateRoute(
      const QGeoRoute &route,
      const QGeoCoordinate &position) override {
    if (taken[1]) {
      int handled = 0;
      CuteQGeoRoutingManagerEngineCall1 call = reinterpret_cast<CuteQGeoRoutingManagerEngineCall1>(taken[1]);
      void * given = call(this, &route, &position, &handled);
      if (handled) return static_cast<QGeoRouteReply *>(given);
    }
    return QGeoRoutingManagerEngine::updateRoute(route, position);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQGeoRoutingManagerEngineCall2 call = reinterpret_cast<CuteQGeoRoutingManagerEngineCall2>(taken[2]);
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
      CuteQGeoRoutingManagerEngineCall3 call = reinterpret_cast<CuteQGeoRoutingManagerEngineCall3>(taken[3]);
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
      CuteQGeoRoutingManagerEngineCall4 call = reinterpret_cast<CuteQGeoRoutingManagerEngineCall4>(taken[4]);
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
      CuteQGeoRoutingManagerEngineCall5 call = reinterpret_cast<CuteQGeoRoutingManagerEngineCall5>(taken[5]);
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
      CuteQGeoRoutingManagerEngineCall6 call = reinterpret_cast<CuteQGeoRoutingManagerEngineCall6>(taken[6]);
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
      CuteQGeoRoutingManagerEngineCall7 call = reinterpret_cast<CuteQGeoRoutingManagerEngineCall7>(taken[7]);
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
      CuteQGeoRoutingManagerEngineCall8 call = reinterpret_cast<CuteQGeoRoutingManagerEngineCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QGeoRoutingManagerEngine::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK24QGeoRoutingManagerEngine10metaObjectEv(
    const QGeoRoutingManagerEngine *self) {
  return self->metaObject();
}

//  QString QGeoRoutingManagerEngine::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN24QGeoRoutingManagerEngine2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QGeoRoutingManagerEngine::tr(s, c, n));
}

//  QGeoRoutingManagerEngine::~QGeoRoutingManagerEngine()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QGeoRoutingManagerEngineD1Ev(
    QGeoRoutingManagerEngine *self) {
  delete self;
}

//  QString QGeoRoutingManagerEngine::managerName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK24QGeoRoutingManagerEngine11managerNameEv(
    const QGeoRoutingManagerEngine *self) {
  return new QString(self->managerName());
}

//  int QGeoRoutingManagerEngine::managerVersion() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK24QGeoRoutingManagerEngine14managerVersionEv(
    const QGeoRoutingManagerEngine *self) {
  return self->managerVersion();
}

//  QGeoRouteReply *QGeoRoutingManagerEngine::calculateRoute(const
//      QGeoRouteRequest &request)
extern "C" Q_DECL_EXPORT
QGeoRouteReply *ritual_ZN24QGeoRoutingManagerEngine14calculateRouteERK16QGeoRouteRequest(
    QGeoRoutingManagerEngine *self,
    const QGeoRouteRequest *request) {
  return self->calculateRoute(*request);
}

//  QGeoRouteReply *QGeoRoutingManagerEngine::updateRoute(const QGeoRoute
//      &route, const QGeoCoordinate &position)
extern "C" Q_DECL_EXPORT
QGeoRouteReply *ritual_ZN24QGeoRoutingManagerEngine11updateRouteERK9QGeoRouteRK14QGeoCoordinate(
    QGeoRoutingManagerEngine *self,
    const QGeoRoute *route,
    const QGeoCoordinate *position) {
  return self->updateRoute(*route, *position);
}

//  QGeoRouteRequest::TravelModes
//      QGeoRoutingManagerEngine::supportedTravelModes() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK24QGeoRoutingManagerEngine20supportedTravelModesEv(
    const QGeoRoutingManagerEngine *self) {
  return static_cast<int>(self->supportedTravelModes().toInt());
}

//  QGeoRouteRequest::FeatureTypes
//      QGeoRoutingManagerEngine::supportedFeatureTypes() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK24QGeoRoutingManagerEngine21supportedFeatureTypesEv(
    const QGeoRoutingManagerEngine *self) {
  return static_cast<int>(self->supportedFeatureTypes().toInt());
}

//  QGeoRouteRequest::FeatureWeights
//      QGeoRoutingManagerEngine::supportedFeatureWeights() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK24QGeoRoutingManagerEngine23supportedFeatureWeightsEv(
    const QGeoRoutingManagerEngine *self) {
  return static_cast<int>(self->supportedFeatureWeights().toInt());
}

//  QGeoRouteRequest::RouteOptimizations
//      QGeoRoutingManagerEngine::supportedRouteOptimizations() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK24QGeoRoutingManagerEngine27supportedRouteOptimizationsEv(
    const QGeoRoutingManagerEngine *self) {
  return static_cast<int>(self->supportedRouteOptimizations().toInt());
}

//  QGeoRouteRequest::SegmentDetails
//      QGeoRoutingManagerEngine::supportedSegmentDetails() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK24QGeoRoutingManagerEngine23supportedSegmentDetailsEv(
    const QGeoRoutingManagerEngine *self) {
  return static_cast<int>(self->supportedSegmentDetails().toInt());
}

//  QGeoRouteRequest::ManeuverDetails
//      QGeoRoutingManagerEngine::supportedManeuverDetails() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK24QGeoRoutingManagerEngine24supportedManeuverDetailsEv(
    const QGeoRoutingManagerEngine *self) {
  return static_cast<int>(self->supportedManeuverDetails().toInt());
}

//  void QGeoRoutingManagerEngine::setLocale(const QLocale &locale)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QGeoRoutingManagerEngine9setLocaleERK7QLocale(
    QGeoRoutingManagerEngine *self,
    const QLocale *locale) {
  self->setLocale(*locale);
}

//  QLocale QGeoRoutingManagerEngine::locale() const
extern "C" Q_DECL_EXPORT
QLocale *ritual_ZNK24QGeoRoutingManagerEngine6localeEv(
    const QGeoRoutingManagerEngine *self) {
  return new QLocale(self->locale());
}

//  void
//      QGeoRoutingManagerEngine::setMeasurementSystem(QLocale::MeasurementSy
//      stem system)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QGeoRoutingManagerEngine20setMeasurementSystemEN7QLocale17MeasurementSystemE(
    QGeoRoutingManagerEngine *self,
    QLocale::MeasurementSystem system) {
  self->setMeasurementSystem(system);
}

//  QLocale::MeasurementSystem QGeoRoutingManagerEngine::measurementSystem()
//      const
extern "C" Q_DECL_EXPORT
QLocale::MeasurementSystem ritual_ZNK24QGeoRoutingManagerEngine17measurementSystemEv(
    const QGeoRoutingManagerEngine *self) {
  return self->measurementSystem();
}

//  void QGeoRoutingManagerEngine::setSupportedTravelModes(QGeoRouteRequest::
//      TravelModes travelModes)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QGeoRoutingManagerEngine23setSupportedTravelModesE6QFlagsIN16QGeoRouteRequest10TravelModeEE(
    QGeoRoutingManagerEngine *self,
    int travelModes) {
  self->setSupportedTravelModes(
      QFlags<QGeoRouteRequest::TravelMode>::fromInt(travelModes));
}

//  void QGeoRoutingManagerEngine::setSupportedFeatureTypes(QGeoRouteRequest:
//      :FeatureTypes featureTypes)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QGeoRoutingManagerEngine24setSupportedFeatureTypesE6QFlagsIN16QGeoRouteRequest11FeatureTypeEE(
    QGeoRoutingManagerEngine *self,
    int featureTypes) {
  self->setSupportedFeatureTypes(
      QFlags<QGeoRouteRequest::FeatureType>::fromInt(featureTypes));
}

//  void QGeoRoutingManagerEngine::setSupportedFeatureWeights(QGeoRouteReques
//      t::FeatureWeights featureWeights)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QGeoRoutingManagerEngine26setSupportedFeatureWeightsE6QFlagsIN16QGeoRouteRequest13FeatureWeightEE(
    QGeoRoutingManagerEngine *self,
    int featureWeights) {
  self->setSupportedFeatureWeights(
      QFlags<QGeoRouteRequest::FeatureWeight>::fromInt(featureWeights));
}

//  void QGeoRoutingManagerEngine::setSupportedRouteOptimizations(QGeoRouteRe
//      quest::RouteOptimizations optimizations)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QGeoRoutingManagerEngine30setSupportedRouteOptimizationsE6QFlagsIN16QGeoRouteRequest17RouteOptimizationEE(
    QGeoRoutingManagerEngine *self,
    int optimizations) {
  self->setSupportedRouteOptimizations(
      QFlags<QGeoRouteRequest::RouteOptimization>::fromInt(optimizations));
}

//  void QGeoRoutingManagerEngine::setSupportedSegmentDetails(QGeoRouteReques
//      t::SegmentDetails segmentDetails)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QGeoRoutingManagerEngine26setSupportedSegmentDetailsE6QFlagsIN16QGeoRouteRequest13SegmentDetailEE(
    QGeoRoutingManagerEngine *self,
    int segmentDetails) {
  self->setSupportedSegmentDetails(
      QFlags<QGeoRouteRequest::SegmentDetail>::fromInt(segmentDetails));
}

//  void QGeoRoutingManagerEngine::setSupportedManeuverDetails(QGeoRouteReque
//      st::ManeuverDetails maneuverDetails)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QGeoRoutingManagerEngine27setSupportedManeuverDetailsE6QFlagsIN16QGeoRouteRequest14ManeuverDetailEE(
    QGeoRoutingManagerEngine *self,
    int maneuverDetails) {
  self->setSupportedManeuverDetails(
      QFlags<QGeoRouteRequest::ManeuverDetail>::fromInt(maneuverDetails));
}

//  void QGeoRoutingManagerEngine::setManagerName(const QString &managerName)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QGeoRoutingManagerEngine14setManagerNameERK7QString(
    QGeoRoutingManagerEngine *self,
    const QString *managerName) {
  self->setManagerName(*managerName);
}

//  void QGeoRoutingManagerEngine::setManagerVersion(int managerVersion)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QGeoRoutingManagerEngine17setManagerVersionEi(
    QGeoRoutingManagerEngine *self,
    int managerVersion) {
  self->setManagerVersion(managerVersion);
}

//  a Python function taken by a CuteQGeoRoutingManagerEngine, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGeoRoutingManagerEngine(
    QGeoRoutingManagerEngine *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGeoRoutingManagerEngine *>(self)->take(key, call);
}

//  QGeoRouteReply *QGeoRoutingManagerEngine::updateRoute(const QGeoRoute
//      &route, const QGeoCoordinate &position)
extern "C" Q_DECL_EXPORT
QGeoRouteReply *ritual_own_ZN24QGeoRoutingManagerEngine11updateRouteERK9QGeoRouteRK14QGeoCoordinate(
    QGeoRoutingManagerEngine *self,
    const QGeoRoute *route,
    const QGeoCoordinate *position) {
  return self->QGeoRoutingManagerEngine::updateRoute(*route, *position);
}
