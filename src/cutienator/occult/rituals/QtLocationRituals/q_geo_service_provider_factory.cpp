//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/qgeoserviceproviderfactory.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtLocation/qgeoserviceproviderfactory.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#include <cstring>

//  A QGeoServiceProviderFactory that Python can take functions over in. Every QGeoServiceProviderFactory
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQGeoServiceProviderFactoryCall0)(const void *, QQmlEngine *, int *);
class CuteQGeoServiceProviderFactory : public QGeoServiceProviderFactory {
public:
  using QGeoServiceProviderFactory::QGeoServiceProviderFactory;
  CuteQGeoServiceProviderFactory(const QGeoServiceProviderFactory & other) : QGeoServiceProviderFactory(other) {}
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN26QGeoServiceProviderFactory12setQmlEngineEP10QQmlEngine")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  void QGeoServiceProviderFactory::setQmlEngine(QQmlEngine *engine)
  void setQmlEngine(QQmlEngine *engine) override {
    if (taken[0]) {
      int handled = 0;
      CuteQGeoServiceProviderFactoryCall0 call = reinterpret_cast<CuteQGeoServiceProviderFactoryCall0>(taken[0]);
      call(this, engine, &handled);
      if (handled) return;
    }
    QGeoServiceProviderFactory::setQmlEngine(engine);
  }
};

//  QGeoServiceProviderFactory::~QGeoServiceProviderFactory()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QGeoServiceProviderFactoryD1Ev(
    QGeoServiceProviderFactory *self) {
  delete self;
}

//  QGeoCodingManagerEngine
//      *QGeoServiceProviderFactory::createGeocodingManagerEngine(const
//      QVariantMap &parameters, QGeoServiceProvider::Error *error, QString
//      *errorString) const
extern "C" Q_DECL_EXPORT
QGeoCodingManagerEngine *ritual_ZNK26QGeoServiceProviderFactory28createGeocodingManagerEngineERK4QMapI7QString8QVariantEPN19QGeoServiceProvider5ErrorEPS1_(
    const QGeoServiceProviderFactory *self,
    const QMap<QString, QVariant> *parameters,
    QGeoServiceProvider::Error *error,
    QString *errorString) {
  return self->createGeocodingManagerEngine(*parameters, error, errorString);
}

//  QGeoMappingManagerEngine
//      *QGeoServiceProviderFactory::createMappingManagerEngine(const
//      QVariantMap &parameters, QGeoServiceProvider::Error *error, QString
//      *errorString) const
extern "C" Q_DECL_EXPORT
QGeoMappingManagerEngine *ritual_ZNK26QGeoServiceProviderFactory26createMappingManagerEngineERK4QMapI7QString8QVariantEPN19QGeoServiceProvider5ErrorEPS1_(
    const QGeoServiceProviderFactory *self,
    const QMap<QString, QVariant> *parameters,
    QGeoServiceProvider::Error *error,
    QString *errorString) {
  return self->createMappingManagerEngine(*parameters, error, errorString);
}

//  QGeoRoutingManagerEngine
//      *QGeoServiceProviderFactory::createRoutingManagerEngine(const
//      QVariantMap &parameters, QGeoServiceProvider::Error *error, QString
//      *errorString) const
extern "C" Q_DECL_EXPORT
QGeoRoutingManagerEngine *ritual_ZNK26QGeoServiceProviderFactory26createRoutingManagerEngineERK4QMapI7QString8QVariantEPN19QGeoServiceProvider5ErrorEPS1_(
    const QGeoServiceProviderFactory *self,
    const QMap<QString, QVariant> *parameters,
    QGeoServiceProvider::Error *error,
    QString *errorString) {
  return self->createRoutingManagerEngine(*parameters, error, errorString);
}

//  QPlaceManagerEngine
//      *QGeoServiceProviderFactory::createPlaceManagerEngine(const
//      QVariantMap &parameters, QGeoServiceProvider::Error *error, QString
//      *errorString) const
extern "C" Q_DECL_EXPORT
QPlaceManagerEngine *ritual_ZNK26QGeoServiceProviderFactory24createPlaceManagerEngineERK4QMapI7QString8QVariantEPN19QGeoServiceProvider5ErrorEPS1_(
    const QGeoServiceProviderFactory *self,
    const QMap<QString, QVariant> *parameters,
    QGeoServiceProvider::Error *error,
    QString *errorString) {
  return self->createPlaceManagerEngine(*parameters, error, errorString);
}

//  void QGeoServiceProviderFactory::setQmlEngine(QQmlEngine *engine)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QGeoServiceProviderFactory12setQmlEngineEP10QQmlEngine(
    QGeoServiceProviderFactory *self,
    QQmlEngine *engine) {
  self->setQmlEngine(engine);
}

//  a Python function taken by a CuteQGeoServiceProviderFactory, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGeoServiceProviderFactory(
    QGeoServiceProviderFactory *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGeoServiceProviderFactory *>(self)->take(key, call);
}

//  void QGeoServiceProviderFactory::setQmlEngine(QQmlEngine *engine)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN26QGeoServiceProviderFactory12setQmlEngineEP10QQmlEngine(
    QGeoServiceProviderFactory *self,
    QQmlEngine *engine) {
  self->QGeoServiceProviderFactory::setQmlEngine(engine);
}
