//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/6.12.0/QtLocation/private/qdeclarativegeoserviceprovider_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtLocation/6.12.0/QtLocation/private/qlocationglobal_p.h>
#include <QtLocation/QtLocation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/6.12.0/QtLocation/private/qdeclarativegeoserviceprovider_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QDeclarativeGeoServiceProviderRequirements that Python can take functions over in. Every QDeclarativeGeoServiceProviderRequirements
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDeclarativeGeoServiceProviderRequirementsCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDeclarativeGeoServiceProviderRequirementsCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativeGeoServiceProviderRequirementsCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativeGeoServiceProviderRequirementsCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativeGeoServiceProviderRequirementsCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativeGeoServiceProviderRequirementsCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativeGeoServiceProviderRequirementsCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQDeclarativeGeoServiceProviderRequirements : public QDeclarativeGeoServiceProviderRequirements {
public:
  using QDeclarativeGeoServiceProviderRequirements::QDeclarativeGeoServiceProviderRequirements;
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
      CuteQDeclarativeGeoServiceProviderRequirementsCall0 call = reinterpret_cast<CuteQDeclarativeGeoServiceProviderRequirementsCall0>(taken[0]);
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
      CuteQDeclarativeGeoServiceProviderRequirementsCall1 call = reinterpret_cast<CuteQDeclarativeGeoServiceProviderRequirementsCall1>(taken[1]);
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
      CuteQDeclarativeGeoServiceProviderRequirementsCall2 call = reinterpret_cast<CuteQDeclarativeGeoServiceProviderRequirementsCall2>(taken[2]);
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
      CuteQDeclarativeGeoServiceProviderRequirementsCall3 call = reinterpret_cast<CuteQDeclarativeGeoServiceProviderRequirementsCall3>(taken[3]);
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
      CuteQDeclarativeGeoServiceProviderRequirementsCall4 call = reinterpret_cast<CuteQDeclarativeGeoServiceProviderRequirementsCall4>(taken[4]);
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
      CuteQDeclarativeGeoServiceProviderRequirementsCall5 call = reinterpret_cast<CuteQDeclarativeGeoServiceProviderRequirementsCall5>(taken[5]);
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
      CuteQDeclarativeGeoServiceProviderRequirementsCall6 call = reinterpret_cast<CuteQDeclarativeGeoServiceProviderRequirementsCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject
//      *QDeclarativeGeoServiceProviderRequirements::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK42QDeclarativeGeoServiceProviderRequirements10metaObjectEv(
    const QDeclarativeGeoServiceProviderRequirements *self) {
  return self->metaObject();
}

//  void *QDeclarativeGeoServiceProviderRequirements::qt_metacast(const char
//      *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN42QDeclarativeGeoServiceProviderRequirements11qt_metacastEPKc(
    QDeclarativeGeoServiceProviderRequirements *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int
//      QDeclarativeGeoServiceProviderRequirements::qt_metacall(QMetaObject::
//      Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN42QDeclarativeGeoServiceProviderRequirements11qt_metacallEN11QMetaObject4CallEiPPv(
    QDeclarativeGeoServiceProviderRequirements *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QDeclarativeGeoServiceProviderRequirements::tr(const char *s,
//      const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN42QDeclarativeGeoServiceProviderRequirements2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(
      QDeclarativeGeoServiceProviderRequirements::tr(
          s,
          c,
          n));
}

//  void
//      QDeclarativeGeoServiceProviderRequirements::qt_qmlMarker_uncreatable(
//      )
extern "C" Q_DECL_EXPORT
void ritual_ZN42QDeclarativeGeoServiceProviderRequirements24qt_qmlMarker_uncreatableEv(
    QDeclarativeGeoServiceProviderRequirements *self) {
  self->qt_qmlMarker_uncreatable();
}

//  QDeclarativeGeoServiceProviderRequirements::QDeclarativeGeoServiceProvide
//      rRequirements(QObject *parent)
extern "C" Q_DECL_EXPORT
QDeclarativeGeoServiceProviderRequirements *ritual_ZN42QDeclarativeGeoServiceProviderRequirementsC1EP7QObject(
    QObject *parent) {
  return new CuteQDeclarativeGeoServiceProviderRequirements(parent);
}

//  QDeclarativeGeoServiceProviderRequirements::~QDeclarativeGeoServiceProvid
//      erRequirements()
extern "C" Q_DECL_EXPORT
void ritual_ZN42QDeclarativeGeoServiceProviderRequirementsD1Ev(
    QDeclarativeGeoServiceProviderRequirements *self) {
  delete self;
}

//  QDeclarativeGeoServiceProvider::MappingFeatures
//      QDeclarativeGeoServiceProviderRequirements::mappingRequirements()
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK42QDeclarativeGeoServiceProviderRequirements19mappingRequirementsEv(
    const QDeclarativeGeoServiceProviderRequirements *self) {
  return static_cast<int>(self->mappingRequirements().toInt());
}

//  void
//      QDeclarativeGeoServiceProviderRequirements::setMappingRequirements(co
//      nst QDeclarativeGeoServiceProvider::MappingFeatures &features)
extern "C" Q_DECL_EXPORT
void ritual_ZN42QDeclarativeGeoServiceProviderRequirements22setMappingRequirementsERK6QFlagsIN30QDeclarativeGeoServiceProvider14MappingFeatureEE(
    QDeclarativeGeoServiceProviderRequirements *self,
    const QDeclarativeGeoServiceProvider::MappingFeatures *features) {
  self->setMappingRequirements(*features);
}

//  QDeclarativeGeoServiceProvider::RoutingFeatures
//      QDeclarativeGeoServiceProviderRequirements::routingRequirements()
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK42QDeclarativeGeoServiceProviderRequirements19routingRequirementsEv(
    const QDeclarativeGeoServiceProviderRequirements *self) {
  return static_cast<int>(self->routingRequirements().toInt());
}

//  void
//      QDeclarativeGeoServiceProviderRequirements::setRoutingRequirements(co
//      nst QDeclarativeGeoServiceProvider::RoutingFeatures &features)
extern "C" Q_DECL_EXPORT
void ritual_ZN42QDeclarativeGeoServiceProviderRequirements22setRoutingRequirementsERK6QFlagsIN30QDeclarativeGeoServiceProvider14RoutingFeatureEE(
    QDeclarativeGeoServiceProviderRequirements *self,
    const QDeclarativeGeoServiceProvider::RoutingFeatures *features) {
  self->setRoutingRequirements(*features);
}

//  QDeclarativeGeoServiceProvider::GeocodingFeatures
//      QDeclarativeGeoServiceProviderRequirements::geocodingRequirements()
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK42QDeclarativeGeoServiceProviderRequirements21geocodingRequirementsEv(
    const QDeclarativeGeoServiceProviderRequirements *self) {
  return static_cast<int>(self->geocodingRequirements().toInt());
}

//  void QDeclarativeGeoServiceProviderRequirements::setGeocodingRequirements
//      (const QDeclarativeGeoServiceProvider::GeocodingFeatures &features)
extern "C" Q_DECL_EXPORT
void ritual_ZN42QDeclarativeGeoServiceProviderRequirements24setGeocodingRequirementsERK6QFlagsIN30QDeclarativeGeoServiceProvider16GeocodingFeatureEE(
    QDeclarativeGeoServiceProviderRequirements *self,
    const QDeclarativeGeoServiceProvider::GeocodingFeatures *features) {
  self->setGeocodingRequirements(*features);
}

//  QDeclarativeGeoServiceProvider::PlacesFeatures
//      QDeclarativeGeoServiceProviderRequirements::placesRequirements()
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK42QDeclarativeGeoServiceProviderRequirements18placesRequirementsEv(
    const QDeclarativeGeoServiceProviderRequirements *self) {
  return static_cast<int>(self->placesRequirements().toInt());
}

//  void
//      QDeclarativeGeoServiceProviderRequirements::setPlacesRequirements(con
//      st QDeclarativeGeoServiceProvider::PlacesFeatures &features)
extern "C" Q_DECL_EXPORT
void ritual_ZN42QDeclarativeGeoServiceProviderRequirements21setPlacesRequirementsERK6QFlagsIN30QDeclarativeGeoServiceProvider13PlacesFeatureEE(
    QDeclarativeGeoServiceProviderRequirements *self,
    const QDeclarativeGeoServiceProvider::PlacesFeatures *features) {
  self->setPlacesRequirements(*features);
}

//  QDeclarativeGeoServiceProvider::NavigationFeatures
//      QDeclarativeGeoServiceProviderRequirements::navigationRequirements()
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK42QDeclarativeGeoServiceProviderRequirements22navigationRequirementsEv(
    const QDeclarativeGeoServiceProviderRequirements *self) {
  return static_cast<int>(self->navigationRequirements().toInt());
}

//  void QDeclarativeGeoServiceProviderRequirements::setNavigationRequirement
//      s(const QDeclarativeGeoServiceProvider::NavigationFeatures &features)
extern "C" Q_DECL_EXPORT
void ritual_ZN42QDeclarativeGeoServiceProviderRequirements25setNavigationRequirementsERK6QFlagsIN30QDeclarativeGeoServiceProvider17NavigationFeatureEE(
    QDeclarativeGeoServiceProviderRequirements *self,
    const QDeclarativeGeoServiceProvider::NavigationFeatures *features) {
  self->setNavigationRequirements(*features);
}

//  bool QDeclarativeGeoServiceProviderRequirements::matches(const
//      QGeoServiceProvider *provider) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK42QDeclarativeGeoServiceProviderRequirements7matchesEPK19QGeoServiceProvider(
    const QDeclarativeGeoServiceProviderRequirements *self,
    const QGeoServiceProvider *provider) {
  return self->matches(provider);
}

//  bool QDeclarativeGeoServiceProviderRequirements::operator==(const
//      QDeclarativeGeoServiceProviderRequirements &rhs) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK42QDeclarativeGeoServiceProviderRequirementseqERKS_(
    const QDeclarativeGeoServiceProviderRequirements *self,
    const QDeclarativeGeoServiceProviderRequirements *rhs) {
  return self->operator==(*rhs);
}

//  void QDeclarativeGeoServiceProviderRequirements::mappingRequirementsChang
//      ed(const QDeclarativeGeoServiceProvider::MappingFeatures &features)
extern "C" Q_DECL_EXPORT
void ritual_ZN42QDeclarativeGeoServiceProviderRequirements26mappingRequirementsChangedERK6QFlagsIN30QDeclarativeGeoServiceProvider14MappingFeatureEE(
    QDeclarativeGeoServiceProviderRequirements *self,
    const QDeclarativeGeoServiceProvider::MappingFeatures *features) {
  self->mappingRequirementsChanged(*features);
}

//  void QDeclarativeGeoServiceProviderRequirements::routingRequirementsChang
//      ed(const QDeclarativeGeoServiceProvider::RoutingFeatures &features)
extern "C" Q_DECL_EXPORT
void ritual_ZN42QDeclarativeGeoServiceProviderRequirements26routingRequirementsChangedERK6QFlagsIN30QDeclarativeGeoServiceProvider14RoutingFeatureEE(
    QDeclarativeGeoServiceProviderRequirements *self,
    const QDeclarativeGeoServiceProvider::RoutingFeatures *features) {
  self->routingRequirementsChanged(*features);
}

//  void QDeclarativeGeoServiceProviderRequirements::geocodingRequirementsCha
//      nged(const QDeclarativeGeoServiceProvider::GeocodingFeatures
//      &features)
extern "C" Q_DECL_EXPORT
void ritual_ZN42QDeclarativeGeoServiceProviderRequirements28geocodingRequirementsChangedERK6QFlagsIN30QDeclarativeGeoServiceProvider16GeocodingFeatureEE(
    QDeclarativeGeoServiceProviderRequirements *self,
    const QDeclarativeGeoServiceProvider::GeocodingFeatures *features) {
  self->geocodingRequirementsChanged(*features);
}

//  void QDeclarativeGeoServiceProviderRequirements::placesRequirementsChange
//      d(const QDeclarativeGeoServiceProvider::PlacesFeatures &features)
extern "C" Q_DECL_EXPORT
void ritual_ZN42QDeclarativeGeoServiceProviderRequirements25placesRequirementsChangedERK6QFlagsIN30QDeclarativeGeoServiceProvider13PlacesFeatureEE(
    QDeclarativeGeoServiceProviderRequirements *self,
    const QDeclarativeGeoServiceProvider::PlacesFeatures *features) {
  self->placesRequirementsChanged(*features);
}

//  void QDeclarativeGeoServiceProviderRequirements::navigationRequirementsCh
//      anged(const QDeclarativeGeoServiceProvider::NavigationFeatures
//      &features)
extern "C" Q_DECL_EXPORT
void ritual_ZN42QDeclarativeGeoServiceProviderRequirements29navigationRequirementsChangedERK6QFlagsIN30QDeclarativeGeoServiceProvider17NavigationFeatureEE(
    QDeclarativeGeoServiceProviderRequirements *self,
    const QDeclarativeGeoServiceProvider::NavigationFeatures *features) {
  self->navigationRequirementsChanged(*features);
}

//  void QDeclarativeGeoServiceProviderRequirements::requirementsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN42QDeclarativeGeoServiceProviderRequirements19requirementsChangedEv(
    QDeclarativeGeoServiceProviderRequirements *self) {
  self->requirementsChanged();
}

//  a Python function taken by a
//      CuteQDeclarativeGeoServiceProviderRequirements, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDeclarativeGeoServiceProviderRequirements(
    QDeclarativeGeoServiceProviderRequirements *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDeclarativeGeoServiceProviderRequirements *>(self)->take(key, call);
}
