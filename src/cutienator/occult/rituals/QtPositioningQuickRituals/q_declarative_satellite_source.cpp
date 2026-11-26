//  Written by dev_tooling.RitualGenerator from the records of QtPositioningQ
//  uick/6.12.0/QtPositioningQuick/private/qdeclarativesatellitesource_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtPositioningQuick/6.12.0/QtPositioningQuick/private/qpositioningquickglobal_p.h>
#include <QtPositioningQuick/QtPositioningQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtPositioningQuick/6.12.0/QtPositioningQuick/private/qdeclarativesatellitesource_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtPositioning/qgeosatelliteinfo.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#include <cstring>
#include <QtQml/QQmlListProperty>
#include <QtPositioning/QGeoSatelliteInfoSource>

//  A QDeclarativeSatelliteSource that Python can take functions over in. Every QDeclarativeSatelliteSource
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQDeclarativeSatelliteSourceCall0)(const void *, int *);
typedef void (*CuteQDeclarativeSatelliteSourceCall1)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDeclarativeSatelliteSourceCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDeclarativeSatelliteSourceCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativeSatelliteSourceCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativeSatelliteSourceCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativeSatelliteSourceCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativeSatelliteSourceCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativeSatelliteSourceCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQDeclarativeSatelliteSource : public QDeclarativeSatelliteSource {
public:
  using QDeclarativeSatelliteSource::QDeclarativeSatelliteSource;
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

  //  void QDeclarativeSatelliteSource::classBegin()
  void classBegin() override {
    if (taken[0]) {
      int handled = 0;
      CuteQDeclarativeSatelliteSourceCall0 call = reinterpret_cast<CuteQDeclarativeSatelliteSourceCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QDeclarativeSatelliteSource::classBegin();
  }

  //  void QDeclarativeSatelliteSource::componentComplete()
  void componentComplete() override {
    if (taken[1]) {
      int handled = 0;
      CuteQDeclarativeSatelliteSourceCall1 call = reinterpret_cast<CuteQDeclarativeSatelliteSourceCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QDeclarativeSatelliteSource::componentComplete();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQDeclarativeSatelliteSourceCall2 call = reinterpret_cast<CuteQDeclarativeSatelliteSourceCall2>(taken[2]);
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
      CuteQDeclarativeSatelliteSourceCall3 call = reinterpret_cast<CuteQDeclarativeSatelliteSourceCall3>(taken[3]);
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
      CuteQDeclarativeSatelliteSourceCall4 call = reinterpret_cast<CuteQDeclarativeSatelliteSourceCall4>(taken[4]);
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
      CuteQDeclarativeSatelliteSourceCall5 call = reinterpret_cast<CuteQDeclarativeSatelliteSourceCall5>(taken[5]);
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
      CuteQDeclarativeSatelliteSourceCall6 call = reinterpret_cast<CuteQDeclarativeSatelliteSourceCall6>(taken[6]);
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
      CuteQDeclarativeSatelliteSourceCall7 call = reinterpret_cast<CuteQDeclarativeSatelliteSourceCall7>(taken[7]);
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
      CuteQDeclarativeSatelliteSourceCall8 call = reinterpret_cast<CuteQDeclarativeSatelliteSourceCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QDeclarativeSatelliteSource::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK27QDeclarativeSatelliteSource10metaObjectEv(
    const QDeclarativeSatelliteSource *self) {
  return self->metaObject();
}

//  void *QDeclarativeSatelliteSource::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN27QDeclarativeSatelliteSource11qt_metacastEPKc(
    QDeclarativeSatelliteSource *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QDeclarativeSatelliteSource::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN27QDeclarativeSatelliteSource11qt_metacallEN11QMetaObject4CallEiPPv(
    QDeclarativeSatelliteSource *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QDeclarativeSatelliteSource::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN27QDeclarativeSatelliteSource2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QDeclarativeSatelliteSource::tr(s, c, n));
}

//  QDeclarativeSatelliteSource::QDeclarativeSatelliteSource()
extern "C" Q_DECL_EXPORT
QDeclarativeSatelliteSource *ritual_ZN27QDeclarativeSatelliteSourceC1Ev() {
  return new CuteQDeclarativeSatelliteSource();
}

//  QDeclarativeSatelliteSource::~QDeclarativeSatelliteSource()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QDeclarativeSatelliteSourceD1Ev(
    QDeclarativeSatelliteSource *self) {
  delete self;
}

//  bool QDeclarativeSatelliteSource::isActive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK27QDeclarativeSatelliteSource8isActiveEv(
    const QDeclarativeSatelliteSource *self) {
  return self->isActive();
}

//  bool QDeclarativeSatelliteSource::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK27QDeclarativeSatelliteSource7isValidEv(
    const QDeclarativeSatelliteSource *self) {
  return self->isValid();
}

//  int QDeclarativeSatelliteSource::updateInterval() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK27QDeclarativeSatelliteSource14updateIntervalEv(
    const QDeclarativeSatelliteSource *self) {
  return self->updateInterval();
}

//  SourceError QDeclarativeSatelliteSource::sourceError() const
extern "C" Q_DECL_EXPORT
QDeclarativeSatelliteSource::SourceError ritual_ZNK27QDeclarativeSatelliteSource11sourceErrorEv(
    const QDeclarativeSatelliteSource *self) {
  return self->sourceError();
}

//  QString QDeclarativeSatelliteSource::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK27QDeclarativeSatelliteSource4nameEv(
    const QDeclarativeSatelliteSource *self) {
  return new QString(self->name());
}

//  QQmlListProperty<QDeclarativePluginParameter>
//      QDeclarativeSatelliteSource::parameters()
extern "C" Q_DECL_EXPORT
QQmlListProperty<QDeclarativePluginParameter> *ritual_ZN27QDeclarativeSatelliteSource10parametersEv(
    QDeclarativeSatelliteSource *self) {
  return new QQmlListProperty<QDeclarativePluginParameter>(
      self->parameters());
}

//  QList<QGeoSatelliteInfo> QDeclarativeSatelliteSource::satellitesInUse()
//      const
extern "C" Q_DECL_EXPORT
QList<QGeoSatelliteInfo> *ritual_ZNK27QDeclarativeSatelliteSource15satellitesInUseEv(
    const QDeclarativeSatelliteSource *self) {
  return new QList<QGeoSatelliteInfo>(self->satellitesInUse());
}

//  QList<QGeoSatelliteInfo> QDeclarativeSatelliteSource::satellitesInView()
//      const
extern "C" Q_DECL_EXPORT
QList<QGeoSatelliteInfo> *ritual_ZNK27QDeclarativeSatelliteSource16satellitesInViewEv(
    const QDeclarativeSatelliteSource *self) {
  return new QList<QGeoSatelliteInfo>(self->satellitesInView());
}

//  void QDeclarativeSatelliteSource::setUpdateInterval(int updateInterval)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QDeclarativeSatelliteSource17setUpdateIntervalEi(
    QDeclarativeSatelliteSource *self,
    int updateInterval) {
  self->setUpdateInterval(updateInterval);
}

//  void QDeclarativeSatelliteSource::setActive(bool active)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QDeclarativeSatelliteSource9setActiveEb(
    QDeclarativeSatelliteSource *self,
    bool active) {
  self->setActive(active);
}

//  void QDeclarativeSatelliteSource::setName(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QDeclarativeSatelliteSource7setNameERK7QString(
    QDeclarativeSatelliteSource *self,
    const QString *name) {
  self->setName(*name);
}

//  void QDeclarativeSatelliteSource::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QDeclarativeSatelliteSource10classBeginEv(
    QDeclarativeSatelliteSource *self) {
  self->classBegin();
}

//  void QDeclarativeSatelliteSource::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QDeclarativeSatelliteSource17componentCompleteEv(
    QDeclarativeSatelliteSource *self) {
  self->componentComplete();
}

//  bool QDeclarativeSatelliteSource::setBackendProperty(const QString &name,
//      const QVariant &value)
extern "C" Q_DECL_EXPORT
bool ritual_ZN27QDeclarativeSatelliteSource18setBackendPropertyERK7QStringRK8QVariant(
    QDeclarativeSatelliteSource *self,
    const QString *name,
    const QVariant *value) {
  return self->setBackendProperty(*name, *value);
}

//  QVariant QDeclarativeSatelliteSource::backendProperty(const QString
//      &name) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK27QDeclarativeSatelliteSource15backendPropertyERK7QString(
    const QDeclarativeSatelliteSource *self,
    const QString *name) {
  return new QVariant(self->backendProperty(*name));
}

//  void QDeclarativeSatelliteSource::update(int timeout)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QDeclarativeSatelliteSource6updateEi(
    QDeclarativeSatelliteSource *self,
    int timeout) {
  self->update(timeout);
}

//  void QDeclarativeSatelliteSource::start()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QDeclarativeSatelliteSource5startEv(
    QDeclarativeSatelliteSource *self) {
  self->start();
}

//  void QDeclarativeSatelliteSource::stop()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QDeclarativeSatelliteSource4stopEv(
    QDeclarativeSatelliteSource *self) {
  self->stop();
}

//  void QDeclarativeSatelliteSource::activeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QDeclarativeSatelliteSource13activeChangedEv(
    QDeclarativeSatelliteSource *self) {
  self->activeChanged();
}

//  void QDeclarativeSatelliteSource::validityChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QDeclarativeSatelliteSource15validityChangedEv(
    QDeclarativeSatelliteSource *self) {
  self->validityChanged();
}

//  void QDeclarativeSatelliteSource::updateIntervalChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QDeclarativeSatelliteSource21updateIntervalChangedEv(
    QDeclarativeSatelliteSource *self) {
  self->updateIntervalChanged();
}

//  void QDeclarativeSatelliteSource::sourceErrorChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QDeclarativeSatelliteSource18sourceErrorChangedEv(
    QDeclarativeSatelliteSource *self) {
  self->sourceErrorChanged();
}

//  void QDeclarativeSatelliteSource::nameChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QDeclarativeSatelliteSource11nameChangedEv(
    QDeclarativeSatelliteSource *self) {
  self->nameChanged();
}

//  void QDeclarativeSatelliteSource::satellitesInUseChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QDeclarativeSatelliteSource22satellitesInUseChangedEv(
    QDeclarativeSatelliteSource *self) {
  self->satellitesInUseChanged();
}

//  void QDeclarativeSatelliteSource::satellitesInViewChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QDeclarativeSatelliteSource23satellitesInViewChangedEv(
    QDeclarativeSatelliteSource *self) {
  self->satellitesInViewChanged();
}

//  void QDeclarativeSatelliteSource::sourceErrorReceived(const
//      QGeoSatelliteInfoSource::Error error)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QDeclarativeSatelliteSource19sourceErrorReceivedEN23QGeoSatelliteInfoSource5ErrorE(
    QDeclarativeSatelliteSource *self,
    const QGeoSatelliteInfoSource::Error *error) {
  self->sourceErrorReceived(*error);
}

//  void QDeclarativeSatelliteSource::onParameterInitialized()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QDeclarativeSatelliteSource22onParameterInitializedEv(
    QDeclarativeSatelliteSource *self) {
  self->onParameterInitialized();
}

//  void QDeclarativeSatelliteSource::satellitesInViewUpdateReceived(const
//      QList<QGeoSatelliteInfo> &satellites)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QDeclarativeSatelliteSource30satellitesInViewUpdateReceivedERK5QListI17QGeoSatelliteInfoE(
    QDeclarativeSatelliteSource *self,
    const QList<QGeoSatelliteInfo> *satellites) {
  self->satellitesInViewUpdateReceived(*satellites);
}

//  void QDeclarativeSatelliteSource::satellitesInUseUpdateReceived(const
//      QList<QGeoSatelliteInfo> &satellites)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QDeclarativeSatelliteSource29satellitesInUseUpdateReceivedERK5QListI17QGeoSatelliteInfoE(
    QDeclarativeSatelliteSource *self,
    const QList<QGeoSatelliteInfo> *satellites) {
  self->satellitesInUseUpdateReceived(*satellites);
}

//  QVariantMap QDeclarativeSatelliteSource::parameterMap() const
extern "C" Q_DECL_EXPORT
QMap<QString, QVariant> *ritual_ZNK27QDeclarativeSatelliteSource12parameterMapEv(
    const QDeclarativeSatelliteSource *self) {
  return new QMap<QString, QVariant>(self->parameterMap());
}

//  void QDeclarativeSatelliteSource::createSource(const QString &newName)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QDeclarativeSatelliteSource12createSourceERK7QString(
    QDeclarativeSatelliteSource *self,
    const QString *newName) {
  self->createSource(*newName);
}

//  void QDeclarativeSatelliteSource::handleSingleUpdateReceived()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QDeclarativeSatelliteSource26handleSingleUpdateReceivedEv(
    QDeclarativeSatelliteSource *self) {
  self->handleSingleUpdateReceived();
}

//  void QDeclarativeSatelliteSource::executeStart()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QDeclarativeSatelliteSource12executeStartEv(
    QDeclarativeSatelliteSource *self) {
  self->executeStart();
}

//  void QDeclarativeSatelliteSource::executeSingleUpdate(int timeout)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QDeclarativeSatelliteSource19executeSingleUpdateEi(
    QDeclarativeSatelliteSource *self,
    int timeout) {
  self->executeSingleUpdate(timeout);
}

//  void
//      QDeclarativeSatelliteSource::parameter_append(PluginParameterProperty
//      *prop, QDeclarativePluginParameter *parameter)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QDeclarativeSatelliteSource16parameter_appendEP16QQmlListPropertyI27QDeclarativePluginParameterEPS1_(
    QDeclarativeSatelliteSource::PluginParameterProperty *prop,
    QDeclarativePluginParameter *parameter) {
  QDeclarativeSatelliteSource::parameter_append(prop, parameter);
}

//  qsizetype
//      QDeclarativeSatelliteSource::parameter_count(PluginParameterProperty
//      *prop)
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZN27QDeclarativeSatelliteSource15parameter_countEP16QQmlListPropertyI27QDeclarativePluginParameterE(
    QDeclarativeSatelliteSource::PluginParameterProperty *prop) {
  return QDeclarativeSatelliteSource::parameter_count(prop);
}

//  QDeclarativePluginParameter
//      *QDeclarativeSatelliteSource::parameter_at(PluginParameterProperty
//      *prop, qsizetype index)
extern "C" Q_DECL_EXPORT
QDeclarativePluginParameter *ritual_ZN27QDeclarativeSatelliteSource12parameter_atEP16QQmlListPropertyI27QDeclarativePluginParameterEx(
    QDeclarativeSatelliteSource::PluginParameterProperty *prop,
    qsizetype index) {
  return QDeclarativeSatelliteSource::parameter_at(prop, index);
}

//  void QDeclarativeSatelliteSource::parameter_clear(PluginParameterProperty
//      *prop)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QDeclarativeSatelliteSource15parameter_clearEP16QQmlListPropertyI27QDeclarativePluginParameterE(
    QDeclarativeSatelliteSource::PluginParameterProperty *prop) {
  QDeclarativeSatelliteSource::parameter_clear(prop);
}

//  QDeclarativeSatelliteSource as the QQmlParserStatus it is built on
extern "C" Q_DECL_EXPORT
QQmlParserStatus *ritual_cast_QDeclarativeSatelliteSource_QQmlParserStatus(
    QDeclarativeSatelliteSource *self) {
  return static_cast<QQmlParserStatus *>(self);
}

//  a Python function taken by a CuteQDeclarativeSatelliteSource, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDeclarativeSatelliteSource(
    QDeclarativeSatelliteSource *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDeclarativeSatelliteSource *>(self)->take(key, call);
}

//  void QDeclarativeSatelliteSource::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN27QDeclarativeSatelliteSource10classBeginEv(
    QDeclarativeSatelliteSource *self) {
  self->QDeclarativeSatelliteSource::classBegin();
}

//  void QDeclarativeSatelliteSource::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN27QDeclarativeSatelliteSource17componentCompleteEv(
    QDeclarativeSatelliteSource *self) {
  self->QDeclarativeSatelliteSource::componentComplete();
}

//  a QQmlListProperty<QDeclarativePluginParameter> a ritual of
//      QDeclarativeSatelliteSource gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QDeclarativeSatelliteSource__QQmlListProperty_QDeclarativePluginParameter(
    QQmlListProperty<QDeclarativePluginParameter> *self) {
  delete self;
}
