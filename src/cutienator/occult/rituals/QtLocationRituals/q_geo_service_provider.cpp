//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/qgeoserviceprovider.h, Qt 6.12.0. Changes made here are lost.
#include <QtLocation/qgeoserviceprovider.h>
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qlocale.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#include <cstring>

//  A QGeoServiceProvider that Python can take functions over in. Every QGeoServiceProvider
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQGeoServiceProviderCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQGeoServiceProviderCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGeoServiceProviderCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGeoServiceProviderCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGeoServiceProviderCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGeoServiceProviderCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGeoServiceProviderCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQGeoServiceProvider : public QGeoServiceProvider {
public:
  using QGeoServiceProvider::QGeoServiceProvider;
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
      CuteQGeoServiceProviderCall0 call = reinterpret_cast<CuteQGeoServiceProviderCall0>(taken[0]);
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
      CuteQGeoServiceProviderCall1 call = reinterpret_cast<CuteQGeoServiceProviderCall1>(taken[1]);
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
      CuteQGeoServiceProviderCall2 call = reinterpret_cast<CuteQGeoServiceProviderCall2>(taken[2]);
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
      CuteQGeoServiceProviderCall3 call = reinterpret_cast<CuteQGeoServiceProviderCall3>(taken[3]);
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
      CuteQGeoServiceProviderCall4 call = reinterpret_cast<CuteQGeoServiceProviderCall4>(taken[4]);
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
      CuteQGeoServiceProviderCall5 call = reinterpret_cast<CuteQGeoServiceProviderCall5>(taken[5]);
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
      CuteQGeoServiceProviderCall6 call = reinterpret_cast<CuteQGeoServiceProviderCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QGeoServiceProvider::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19QGeoServiceProvider10metaObjectEv(
    const QGeoServiceProvider *self) {
  return self->metaObject();
}

//  void *QGeoServiceProvider::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN19QGeoServiceProvider11qt_metacastEPKc(
    QGeoServiceProvider *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QGeoServiceProvider::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN19QGeoServiceProvider11qt_metacallEN11QMetaObject4CallEiPPv(
    QGeoServiceProvider *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QGeoServiceProvider::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19QGeoServiceProvider2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QGeoServiceProvider::tr(s, c, n));
}

//  QStringList QGeoServiceProvider::availableServiceProviders()
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZN19QGeoServiceProvider25availableServiceProvidersEv() {
  return new QList<QString>(
      QGeoServiceProvider::availableServiceProviders());
}

//  QGeoServiceProvider::QGeoServiceProvider(const QString &providerName,
//      const QVariantMap &parameters, bool allowExperimental)
extern "C" Q_DECL_EXPORT
QGeoServiceProvider *ritual_ZN19QGeoServiceProviderC1ERK7QStringRK4QMapIS0_8QVariantEb(
    const QString *providerName,
    const QMap<QString, QVariant> *parameters,
    bool allowExperimental) {
  return new CuteQGeoServiceProvider(
      *providerName,
      *parameters,
      allowExperimental);
}

//  QGeoServiceProvider::~QGeoServiceProvider()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGeoServiceProviderD1Ev(QGeoServiceProvider *self) {
  delete self;
}

//  RoutingFeatures QGeoServiceProvider::routingFeatures() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QGeoServiceProvider15routingFeaturesEv(
    const QGeoServiceProvider *self) {
  return static_cast<int>(self->routingFeatures().toInt());
}

//  GeocodingFeatures QGeoServiceProvider::geocodingFeatures() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QGeoServiceProvider17geocodingFeaturesEv(
    const QGeoServiceProvider *self) {
  return static_cast<int>(self->geocodingFeatures().toInt());
}

//  MappingFeatures QGeoServiceProvider::mappingFeatures() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QGeoServiceProvider15mappingFeaturesEv(
    const QGeoServiceProvider *self) {
  return static_cast<int>(self->mappingFeatures().toInt());
}

//  PlacesFeatures QGeoServiceProvider::placesFeatures() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QGeoServiceProvider14placesFeaturesEv(
    const QGeoServiceProvider *self) {
  return static_cast<int>(self->placesFeatures().toInt());
}

//  NavigationFeatures QGeoServiceProvider::navigationFeatures() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QGeoServiceProvider18navigationFeaturesEv(
    const QGeoServiceProvider *self) {
  return static_cast<int>(self->navigationFeatures().toInt());
}

//  QGeoCodingManager *QGeoServiceProvider::geocodingManager() const
extern "C" Q_DECL_EXPORT
QGeoCodingManager *ritual_ZNK19QGeoServiceProvider16geocodingManagerEv(
    const QGeoServiceProvider *self) {
  return self->geocodingManager();
}

//  QGeoMappingManager *QGeoServiceProvider::mappingManager() const
extern "C" Q_DECL_EXPORT
QGeoMappingManager *ritual_ZNK19QGeoServiceProvider14mappingManagerEv(
    const QGeoServiceProvider *self) {
  return self->mappingManager();
}

//  QGeoRoutingManager *QGeoServiceProvider::routingManager() const
extern "C" Q_DECL_EXPORT
QGeoRoutingManager *ritual_ZNK19QGeoServiceProvider14routingManagerEv(
    const QGeoServiceProvider *self) {
  return self->routingManager();
}

//  QPlaceManager *QGeoServiceProvider::placeManager() const
extern "C" Q_DECL_EXPORT
QPlaceManager *ritual_ZNK19QGeoServiceProvider12placeManagerEv(
    const QGeoServiceProvider *self) {
  return self->placeManager();
}

//  Error QGeoServiceProvider::error() const
extern "C" Q_DECL_EXPORT
QGeoServiceProvider::Error ritual_ZNK19QGeoServiceProvider5errorEv(
    const QGeoServiceProvider *self) {
  return self->error();
}

//  QString QGeoServiceProvider::errorString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QGeoServiceProvider11errorStringEv(
    const QGeoServiceProvider *self) {
  return new QString(self->errorString());
}

//  Error QGeoServiceProvider::mappingError() const
extern "C" Q_DECL_EXPORT
QGeoServiceProvider::Error ritual_ZNK19QGeoServiceProvider12mappingErrorEv(
    const QGeoServiceProvider *self) {
  return self->mappingError();
}

//  QString QGeoServiceProvider::mappingErrorString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QGeoServiceProvider18mappingErrorStringEv(
    const QGeoServiceProvider *self) {
  return new QString(self->mappingErrorString());
}

//  Error QGeoServiceProvider::geocodingError() const
extern "C" Q_DECL_EXPORT
QGeoServiceProvider::Error ritual_ZNK19QGeoServiceProvider14geocodingErrorEv(
    const QGeoServiceProvider *self) {
  return self->geocodingError();
}

//  QString QGeoServiceProvider::geocodingErrorString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QGeoServiceProvider20geocodingErrorStringEv(
    const QGeoServiceProvider *self) {
  return new QString(self->geocodingErrorString());
}

//  Error QGeoServiceProvider::routingError() const
extern "C" Q_DECL_EXPORT
QGeoServiceProvider::Error ritual_ZNK19QGeoServiceProvider12routingErrorEv(
    const QGeoServiceProvider *self) {
  return self->routingError();
}

//  QString QGeoServiceProvider::routingErrorString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QGeoServiceProvider18routingErrorStringEv(
    const QGeoServiceProvider *self) {
  return new QString(self->routingErrorString());
}

//  Error QGeoServiceProvider::placesError() const
extern "C" Q_DECL_EXPORT
QGeoServiceProvider::Error ritual_ZNK19QGeoServiceProvider11placesErrorEv(
    const QGeoServiceProvider *self) {
  return self->placesError();
}

//  QString QGeoServiceProvider::placesErrorString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QGeoServiceProvider17placesErrorStringEv(
    const QGeoServiceProvider *self) {
  return new QString(self->placesErrorString());
}

//  Error QGeoServiceProvider::navigationError() const
extern "C" Q_DECL_EXPORT
QGeoServiceProvider::Error ritual_ZNK19QGeoServiceProvider15navigationErrorEv(
    const QGeoServiceProvider *self) {
  return self->navigationError();
}

//  QString QGeoServiceProvider::navigationErrorString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QGeoServiceProvider21navigationErrorStringEv(
    const QGeoServiceProvider *self) {
  return new QString(self->navigationErrorString());
}

//  void QGeoServiceProvider::setParameters(const QVariantMap &parameters)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGeoServiceProvider13setParametersERK4QMapI7QString8QVariantE(
    QGeoServiceProvider *self,
    const QMap<QString, QVariant> *parameters) {
  self->setParameters(*parameters);
}

//  void QGeoServiceProvider::setLocale(const QLocale &locale)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGeoServiceProvider9setLocaleERK7QLocale(
    QGeoServiceProvider *self,
    const QLocale *locale) {
  self->setLocale(*locale);
}

//  void QGeoServiceProvider::setAllowExperimental(bool allow)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGeoServiceProvider20setAllowExperimentalEb(
    QGeoServiceProvider *self,
    bool allow) {
  self->setAllowExperimental(allow);
}

//  void QGeoServiceProvider::setQmlEngine(QQmlEngine *engine)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGeoServiceProvider12setQmlEngineEP10QQmlEngine(
    QGeoServiceProvider *self,
    QQmlEngine *engine) {
  self->setQmlEngine(engine);
}

//  a Python function taken by a CuteQGeoServiceProvider, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGeoServiceProvider(
    QGeoServiceProvider *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGeoServiceProvider *>(self)->take(key, call);
}
