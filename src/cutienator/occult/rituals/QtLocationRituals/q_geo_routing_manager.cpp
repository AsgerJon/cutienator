//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/qgeoroutingmanager.h, Qt 6.12.0. Changes made here are lost.
#include <QtLocation/qgeoroutingmanager.h>
#include <QtCore/qstring.h>
#include <QtLocation/qgeorouterequest.h>
#include <QtLocation/qgeoroute.h>
#include <QtPositioning/qgeocoordinate.h>
#include <QtCore/qlocale.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QGeoRoutingManager that Python can take functions over in. Every QGeoRoutingManager
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQGeoRoutingManagerCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQGeoRoutingManagerCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGeoRoutingManagerCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGeoRoutingManagerCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGeoRoutingManagerCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGeoRoutingManagerCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGeoRoutingManagerCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQGeoRoutingManager : public QGeoRoutingManager {
public:
  using QGeoRoutingManager::QGeoRoutingManager;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQGeoRoutingManagerCall0 call = reinterpret_cast<CuteQGeoRoutingManagerCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQGeoRoutingManagerCall1 call = reinterpret_cast<CuteQGeoRoutingManagerCall1>(taken[1]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQGeoRoutingManagerCall2 call = reinterpret_cast<CuteQGeoRoutingManagerCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQGeoRoutingManagerCall3 call = reinterpret_cast<CuteQGeoRoutingManagerCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQGeoRoutingManagerCall4 call = reinterpret_cast<CuteQGeoRoutingManagerCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteQGeoRoutingManagerCall5 call = reinterpret_cast<CuteQGeoRoutingManagerCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQGeoRoutingManagerCall6 call = reinterpret_cast<CuteQGeoRoutingManagerCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QGeoRoutingManager::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QGeoRoutingManager10metaObjectEv(
    const QGeoRoutingManager *self) {
  return self->metaObject();
}

//  void *QGeoRoutingManager::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN18QGeoRoutingManager11qt_metacastEPKc(
    QGeoRoutingManager *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QGeoRoutingManager::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN18QGeoRoutingManager11qt_metacallEN11QMetaObject4CallEiPPv(
    QGeoRoutingManager *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QGeoRoutingManager::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QGeoRoutingManager2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QGeoRoutingManager::tr(s, c, n));
}

//  QGeoRoutingManager::~QGeoRoutingManager()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QGeoRoutingManagerD1Ev(QGeoRoutingManager *self) {
  delete self;
}

//  QString QGeoRoutingManager::managerName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QGeoRoutingManager11managerNameEv(
    const QGeoRoutingManager *self) {
  return new QString(self->managerName());
}

//  int QGeoRoutingManager::managerVersion() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QGeoRoutingManager14managerVersionEv(
    const QGeoRoutingManager *self) {
  return self->managerVersion();
}

//  QGeoRouteReply *QGeoRoutingManager::calculateRoute(const QGeoRouteRequest
//      &request)
extern "C" Q_DECL_EXPORT
QGeoRouteReply *ritual_ZN18QGeoRoutingManager14calculateRouteERK16QGeoRouteRequest(
    QGeoRoutingManager *self,
    const QGeoRouteRequest *request) {
  return self->calculateRoute(*request);
}

//  QGeoRouteReply *QGeoRoutingManager::updateRoute(const QGeoRoute &route,
//      const QGeoCoordinate &position)
extern "C" Q_DECL_EXPORT
QGeoRouteReply *ritual_ZN18QGeoRoutingManager11updateRouteERK9QGeoRouteRK14QGeoCoordinate(
    QGeoRoutingManager *self,
    const QGeoRoute *route,
    const QGeoCoordinate *position) {
  return self->updateRoute(*route, *position);
}

//  QGeoRouteRequest::TravelModes QGeoRoutingManager::supportedTravelModes()
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QGeoRoutingManager20supportedTravelModesEv(
    const QGeoRoutingManager *self) {
  return static_cast<int>(self->supportedTravelModes().toInt());
}

//  QGeoRouteRequest::FeatureTypes
//      QGeoRoutingManager::supportedFeatureTypes() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QGeoRoutingManager21supportedFeatureTypesEv(
    const QGeoRoutingManager *self) {
  return static_cast<int>(self->supportedFeatureTypes().toInt());
}

//  QGeoRouteRequest::FeatureWeights
//      QGeoRoutingManager::supportedFeatureWeights() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QGeoRoutingManager23supportedFeatureWeightsEv(
    const QGeoRoutingManager *self) {
  return static_cast<int>(self->supportedFeatureWeights().toInt());
}

//  QGeoRouteRequest::RouteOptimizations
//      QGeoRoutingManager::supportedRouteOptimizations() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QGeoRoutingManager27supportedRouteOptimizationsEv(
    const QGeoRoutingManager *self) {
  return static_cast<int>(self->supportedRouteOptimizations().toInt());
}

//  QGeoRouteRequest::SegmentDetails
//      QGeoRoutingManager::supportedSegmentDetails() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QGeoRoutingManager23supportedSegmentDetailsEv(
    const QGeoRoutingManager *self) {
  return static_cast<int>(self->supportedSegmentDetails().toInt());
}

//  QGeoRouteRequest::ManeuverDetails
//      QGeoRoutingManager::supportedManeuverDetails() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QGeoRoutingManager24supportedManeuverDetailsEv(
    const QGeoRoutingManager *self) {
  return static_cast<int>(self->supportedManeuverDetails().toInt());
}

//  void QGeoRoutingManager::setLocale(const QLocale &locale)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QGeoRoutingManager9setLocaleERK7QLocale(
    QGeoRoutingManager *self,
    const QLocale *locale) {
  self->setLocale(*locale);
}

//  QLocale QGeoRoutingManager::locale() const
extern "C" Q_DECL_EXPORT
QLocale *ritual_ZNK18QGeoRoutingManager6localeEv(
    const QGeoRoutingManager *self) {
  return new QLocale(self->locale());
}

//  void QGeoRoutingManager::setMeasurementSystem(QLocale::MeasurementSystem
//      system)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QGeoRoutingManager20setMeasurementSystemEN7QLocale17MeasurementSystemE(
    QGeoRoutingManager *self,
    QLocale::MeasurementSystem system) {
  self->setMeasurementSystem(system);
}

//  QLocale::MeasurementSystem QGeoRoutingManager::measurementSystem() const
extern "C" Q_DECL_EXPORT
QLocale::MeasurementSystem ritual_ZNK18QGeoRoutingManager17measurementSystemEv(
    const QGeoRoutingManager *self) {
  return self->measurementSystem();
}

//  void QGeoRoutingManager::finished(QGeoRouteReply *reply)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QGeoRoutingManager8finishedEP14QGeoRouteReply(
    QGeoRoutingManager *self,
    QGeoRouteReply *reply) {
  self->finished(reply);
}

//  void QGeoRoutingManager::errorOccurred(QGeoRouteReply *reply,
//      QGeoRouteReply::Error error, const QString &errorString)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QGeoRoutingManager13errorOccurredEP14QGeoRouteReplyNS0_5ErrorERK7QString(
    QGeoRoutingManager *self,
    QGeoRouteReply *reply,
    QGeoRouteReply::Error error,
    const QString *errorString) {
  self->errorOccurred(reply, error, *errorString);
}

//  QGeoRoutingManager::QGeoRoutingManager(QGeoRoutingManagerEngine *engine,
//      QObject *parent)
extern "C" Q_DECL_EXPORT
QGeoRoutingManager *ritual_ZN18QGeoRoutingManagerC1EP24QGeoRoutingManagerEngineP7QObject(
    QGeoRoutingManagerEngine *engine,
    QObject *parent) {
  return new CuteQGeoRoutingManager(engine, parent);
}

//  a Python function taken by a CuteQGeoRoutingManager, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGeoRoutingManager(
    QGeoRoutingManager *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGeoRoutingManager *>(self)->take(key, call);
}
