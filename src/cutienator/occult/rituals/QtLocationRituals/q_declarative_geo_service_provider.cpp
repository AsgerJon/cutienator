//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/6.12.0/QtLocation/private/qdeclarativegeoserviceprovider_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtLocation/6.12.0/QtLocation/private/qlocationglobal_p.h>
#include <QtLocation/QtLocation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/6.12.0/QtLocation/private/qdeclarativegeoserviceprovider_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#include <cstring>
#include <QtQml/QQmlListProperty>

//  A QDeclarativeGeoServiceProvider that Python can take functions over in. Every QDeclarativeGeoServiceProvider
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQDeclarativeGeoServiceProviderCall0)(const void *, int *);
typedef void (*CuteQDeclarativeGeoServiceProviderCall1)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDeclarativeGeoServiceProviderCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDeclarativeGeoServiceProviderCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativeGeoServiceProviderCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativeGeoServiceProviderCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativeGeoServiceProviderCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativeGeoServiceProviderCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativeGeoServiceProviderCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQDeclarativeGeoServiceProvider : public QDeclarativeGeoServiceProvider {
public:
  using QDeclarativeGeoServiceProvider::QDeclarativeGeoServiceProvider;
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

  //  void QDeclarativeGeoServiceProvider::classBegin()
  void classBegin() override {
    if (taken[0]) {
      int handled = 0;
      CuteQDeclarativeGeoServiceProviderCall0 call = reinterpret_cast<CuteQDeclarativeGeoServiceProviderCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QDeclarativeGeoServiceProvider::classBegin();
  }

  //  void QDeclarativeGeoServiceProvider::componentComplete()
  void componentComplete() override {
    if (taken[1]) {
      int handled = 0;
      CuteQDeclarativeGeoServiceProviderCall1 call = reinterpret_cast<CuteQDeclarativeGeoServiceProviderCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QDeclarativeGeoServiceProvider::componentComplete();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQDeclarativeGeoServiceProviderCall2 call = reinterpret_cast<CuteQDeclarativeGeoServiceProviderCall2>(taken[2]);
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
      CuteQDeclarativeGeoServiceProviderCall3 call = reinterpret_cast<CuteQDeclarativeGeoServiceProviderCall3>(taken[3]);
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
      CuteQDeclarativeGeoServiceProviderCall4 call = reinterpret_cast<CuteQDeclarativeGeoServiceProviderCall4>(taken[4]);
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
      CuteQDeclarativeGeoServiceProviderCall5 call = reinterpret_cast<CuteQDeclarativeGeoServiceProviderCall5>(taken[5]);
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
      CuteQDeclarativeGeoServiceProviderCall6 call = reinterpret_cast<CuteQDeclarativeGeoServiceProviderCall6>(taken[6]);
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
      CuteQDeclarativeGeoServiceProviderCall7 call = reinterpret_cast<CuteQDeclarativeGeoServiceProviderCall7>(taken[7]);
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
      CuteQDeclarativeGeoServiceProviderCall8 call = reinterpret_cast<CuteQDeclarativeGeoServiceProviderCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QDeclarativeGeoServiceProvider::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK30QDeclarativeGeoServiceProvider10metaObjectEv(
    const QDeclarativeGeoServiceProvider *self) {
  return self->metaObject();
}

//  void *QDeclarativeGeoServiceProvider::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN30QDeclarativeGeoServiceProvider11qt_metacastEPKc(
    QDeclarativeGeoServiceProvider *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QDeclarativeGeoServiceProvider::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN30QDeclarativeGeoServiceProvider11qt_metacallEN11QMetaObject4CallEiPPv(
    QDeclarativeGeoServiceProvider *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QDeclarativeGeoServiceProvider::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN30QDeclarativeGeoServiceProvider2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QDeclarativeGeoServiceProvider::tr(s, c, n));
}

//  QDeclarativeGeoServiceProvider::QDeclarativeGeoServiceProvider(QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QDeclarativeGeoServiceProvider *ritual_ZN30QDeclarativeGeoServiceProviderC1EP7QObject(
    QObject *parent) {
  return new CuteQDeclarativeGeoServiceProvider(parent);
}

//  QDeclarativeGeoServiceProvider::~QDeclarativeGeoServiceProvider()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QDeclarativeGeoServiceProviderD1Ev(
    QDeclarativeGeoServiceProvider *self) {
  delete self;
}

//  void QDeclarativeGeoServiceProvider::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QDeclarativeGeoServiceProvider10classBeginEv(
    QDeclarativeGeoServiceProvider *self) {
  self->classBegin();
}

//  void QDeclarativeGeoServiceProvider::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QDeclarativeGeoServiceProvider17componentCompleteEv(
    QDeclarativeGeoServiceProvider *self) {
  self->componentComplete();
}

//  void QDeclarativeGeoServiceProvider::setName(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QDeclarativeGeoServiceProvider7setNameERK7QString(
    QDeclarativeGeoServiceProvider *self,
    const QString *name) {
  self->setName(*name);
}

//  QString QDeclarativeGeoServiceProvider::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK30QDeclarativeGeoServiceProvider4nameEv(
    const QDeclarativeGeoServiceProvider *self) {
  return new QString(self->name());
}

//  QQmlListProperty<QDeclarativePluginParameter>
//      QDeclarativeGeoServiceProvider::parameters()
extern "C" Q_DECL_EXPORT
QQmlListProperty<QDeclarativePluginParameter> *ritual_ZN30QDeclarativeGeoServiceProvider10parametersEv(
    QDeclarativeGeoServiceProvider *self) {
  return new QQmlListProperty<QDeclarativePluginParameter>(
      self->parameters());
}

//  QVariantMap QDeclarativeGeoServiceProvider::parameterMap() const
extern "C" Q_DECL_EXPORT
QMap<QString, QVariant> *ritual_ZNK30QDeclarativeGeoServiceProvider12parameterMapEv(
    const QDeclarativeGeoServiceProvider *self) {
  return new QMap<QString, QVariant>(self->parameterMap());
}

//  QStringList QDeclarativeGeoServiceProvider::availableServiceProviders()
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZN30QDeclarativeGeoServiceProvider25availableServiceProvidersEv(
    QDeclarativeGeoServiceProvider *self) {
  return new QList<QString>(self->availableServiceProviders());
}

//  QDeclarativeGeoServiceProviderRequirements
//      *QDeclarativeGeoServiceProvider::requirements() const
extern "C" Q_DECL_EXPORT
QDeclarativeGeoServiceProviderRequirements *ritual_ZNK30QDeclarativeGeoServiceProvider12requirementsEv(
    const QDeclarativeGeoServiceProvider *self) {
  return self->requirements();
}

//  void QDeclarativeGeoServiceProvider::setRequirements(QDeclarativeGeoServi
//      ceProviderRequirements *req)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QDeclarativeGeoServiceProvider15setRequirementsEP42QDeclarativeGeoServiceProviderRequirements(
    QDeclarativeGeoServiceProvider *self,
    QDeclarativeGeoServiceProviderRequirements *req) {
  self->setRequirements(req);
}

//  QStringList QDeclarativeGeoServiceProvider::preferred() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK30QDeclarativeGeoServiceProvider9preferredEv(
    const QDeclarativeGeoServiceProvider *self) {
  return new QList<QString>(self->preferred());
}

//  void QDeclarativeGeoServiceProvider::setPreferred(const QStringList &val)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QDeclarativeGeoServiceProvider12setPreferredERK5QListI7QStringE(
    QDeclarativeGeoServiceProvider *self,
    const QList<QString> *val) {
  self->setPreferred(*val);
}

//  QGeoServiceProvider
//      *QDeclarativeGeoServiceProvider::sharedGeoServiceProvider() const
extern "C" Q_DECL_EXPORT
QGeoServiceProvider *ritual_ZNK30QDeclarativeGeoServiceProvider24sharedGeoServiceProviderEv(
    const QDeclarativeGeoServiceProvider *self) {
  return self->sharedGeoServiceProvider();
}

//  bool QDeclarativeGeoServiceProvider::supportsRouting(const
//      RoutingFeatures &feature) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK30QDeclarativeGeoServiceProvider15supportsRoutingERK6QFlagsINS_14RoutingFeatureEE(
    const QDeclarativeGeoServiceProvider *self,
    const QDeclarativeGeoServiceProvider::RoutingFeatures *feature) {
  return self->supportsRouting(*feature);
}

//  bool QDeclarativeGeoServiceProvider::supportsGeocoding(const
//      GeocodingFeatures &feature) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK30QDeclarativeGeoServiceProvider17supportsGeocodingERK6QFlagsINS_16GeocodingFeatureEE(
    const QDeclarativeGeoServiceProvider *self,
    const QDeclarativeGeoServiceProvider::GeocodingFeatures *feature) {
  return self->supportsGeocoding(*feature);
}

//  bool QDeclarativeGeoServiceProvider::supportsMapping(const
//      MappingFeatures &feature) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK30QDeclarativeGeoServiceProvider15supportsMappingERK6QFlagsINS_14MappingFeatureEE(
    const QDeclarativeGeoServiceProvider *self,
    const QDeclarativeGeoServiceProvider::MappingFeatures *feature) {
  return self->supportsMapping(*feature);
}

//  bool QDeclarativeGeoServiceProvider::supportsPlaces(const PlacesFeatures
//      &feature) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK30QDeclarativeGeoServiceProvider14supportsPlacesERK6QFlagsINS_13PlacesFeatureEE(
    const QDeclarativeGeoServiceProvider *self,
    const QDeclarativeGeoServiceProvider::PlacesFeatures *feature) {
  return self->supportsPlaces(*feature);
}

//  bool QDeclarativeGeoServiceProvider::supportsNavigation(const
//      NavigationFeature &feature) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK30QDeclarativeGeoServiceProvider18supportsNavigationERKNS_17NavigationFeatureE(
    const QDeclarativeGeoServiceProvider *self,
    const QDeclarativeGeoServiceProvider::NavigationFeature *feature) {
  return self->supportsNavigation(*feature);
}

//  QStringList QDeclarativeGeoServiceProvider::locales() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK30QDeclarativeGeoServiceProvider7localesEv(
    const QDeclarativeGeoServiceProvider *self) {
  return new QList<QString>(self->locales());
}

//  void QDeclarativeGeoServiceProvider::setLocales(const QStringList
//      &locales)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QDeclarativeGeoServiceProvider10setLocalesERK5QListI7QStringE(
    QDeclarativeGeoServiceProvider *self,
    const QList<QString> *locales) {
  self->setLocales(*locales);
}

//  bool QDeclarativeGeoServiceProvider::isAttached() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK30QDeclarativeGeoServiceProvider10isAttachedEv(
    const QDeclarativeGeoServiceProvider *self) {
  return self->isAttached();
}

//  void QDeclarativeGeoServiceProvider::setAllowExperimental(bool allow)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QDeclarativeGeoServiceProvider20setAllowExperimentalEb(
    QDeclarativeGeoServiceProvider *self,
    bool allow) {
  self->setAllowExperimental(allow);
}

//  bool QDeclarativeGeoServiceProvider::allowExperimental() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK30QDeclarativeGeoServiceProvider17allowExperimentalEv(
    const QDeclarativeGeoServiceProvider *self) {
  return self->allowExperimental();
}

//  void QDeclarativeGeoServiceProvider::nameChanged(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QDeclarativeGeoServiceProvider11nameChangedERK7QString(
    QDeclarativeGeoServiceProvider *self,
    const QString *name) {
  self->nameChanged(*name);
}

//  void QDeclarativeGeoServiceProvider::localesChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QDeclarativeGeoServiceProvider14localesChangedEv(
    QDeclarativeGeoServiceProvider *self) {
  self->localesChanged();
}

//  void QDeclarativeGeoServiceProvider::attached()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QDeclarativeGeoServiceProvider8attachedEv(
    QDeclarativeGeoServiceProvider *self) {
  self->attached();
}

//  void QDeclarativeGeoServiceProvider::preferredChanged(const QStringList
//      &preferences)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QDeclarativeGeoServiceProvider16preferredChangedERK5QListI7QStringE(
    QDeclarativeGeoServiceProvider *self,
    const QList<QString> *preferences) {
  self->preferredChanged(*preferences);
}

//  void QDeclarativeGeoServiceProvider::allowExperimentalChanged(bool allow)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QDeclarativeGeoServiceProvider24allowExperimentalChangedEb(
    QDeclarativeGeoServiceProvider *self,
    bool allow) {
  self->allowExperimentalChanged(allow);
}

//  bool QDeclarativeGeoServiceProvider::parametersReady()
extern "C" Q_DECL_EXPORT
bool ritual_ZN30QDeclarativeGeoServiceProvider15parametersReadyEv(
    QDeclarativeGeoServiceProvider *self) {
  return self->parametersReady();
}

//  void QDeclarativeGeoServiceProvider::tryAttach()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QDeclarativeGeoServiceProvider9tryAttachEv(
    QDeclarativeGeoServiceProvider *self) {
  self->tryAttach();
}

//  void QDeclarativeGeoServiceProvider::parameter_append(QQmlListProperty<QD
//      eclarativePluginParameter> *prop, QDeclarativePluginParameter
//      *mapObject)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QDeclarativeGeoServiceProvider16parameter_appendEP16QQmlListPropertyI27QDeclarativePluginParameterEPS1_(
    QQmlListProperty<QDeclarativePluginParameter> *prop,
    QDeclarativePluginParameter *mapObject) {
  QDeclarativeGeoServiceProvider::parameter_append(prop, mapObject);
}

//  qsizetype QDeclarativeGeoServiceProvider::parameter_count(QQmlListPropert
//      y<QDeclarativePluginParameter> *prop)
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZN30QDeclarativeGeoServiceProvider15parameter_countEP16QQmlListPropertyI27QDeclarativePluginParameterE(
    QQmlListProperty<QDeclarativePluginParameter> *prop) {
  return QDeclarativeGeoServiceProvider::parameter_count(prop);
}

//  QDeclarativePluginParameter *QDeclarativeGeoServiceProvider::parameter_at
//      (QQmlListProperty<QDeclarativePluginParameter> *prop, qsizetype
//      index)
extern "C" Q_DECL_EXPORT
QDeclarativePluginParameter *ritual_ZN30QDeclarativeGeoServiceProvider12parameter_atEP16QQmlListPropertyI27QDeclarativePluginParameterEx(
    QQmlListProperty<QDeclarativePluginParameter> *prop,
    qsizetype index) {
  return QDeclarativeGeoServiceProvider::parameter_at(prop, index);
}

//  void QDeclarativeGeoServiceProvider::parameter_clear(QQmlListProperty<QDe
//      clarativePluginParameter> *prop)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QDeclarativeGeoServiceProvider15parameter_clearEP16QQmlListPropertyI27QDeclarativePluginParameterE(
    QQmlListProperty<QDeclarativePluginParameter> *prop) {
  QDeclarativeGeoServiceProvider::parameter_clear(prop);
}

//  QDeclarativeGeoServiceProvider as the QQmlParserStatus it is built on
extern "C" Q_DECL_EXPORT
QQmlParserStatus *ritual_cast_QDeclarativeGeoServiceProvider_QQmlParserStatus(
    QDeclarativeGeoServiceProvider *self) {
  return static_cast<QQmlParserStatus *>(self);
}

//  a Python function taken by a CuteQDeclarativeGeoServiceProvider, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDeclarativeGeoServiceProvider(
    QDeclarativeGeoServiceProvider *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDeclarativeGeoServiceProvider *>(self)->take(key, call);
}

//  void QDeclarativeGeoServiceProvider::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN30QDeclarativeGeoServiceProvider10classBeginEv(
    QDeclarativeGeoServiceProvider *self) {
  self->QDeclarativeGeoServiceProvider::classBegin();
}

//  void QDeclarativeGeoServiceProvider::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN30QDeclarativeGeoServiceProvider17componentCompleteEv(
    QDeclarativeGeoServiceProvider *self) {
  self->QDeclarativeGeoServiceProvider::componentComplete();
}

//  a QQmlListProperty<QDeclarativePluginParameter> a ritual of
//      QDeclarativeGeoServiceProvider gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QDeclarativeGeoServiceProvider__QQmlListProperty_QDeclarativePluginParameter(
    QQmlListProperty<QDeclarativePluginParameter> *self) {
  delete self;
}
