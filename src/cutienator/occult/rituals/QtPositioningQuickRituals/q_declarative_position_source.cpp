//  Written by dev_tooling.RitualGenerator from the records of QtPositioningQ
//  uick/6.12.0/QtPositioningQuick/private/qdeclarativepositionsource_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtPositioningQuick/6.12.0/QtPositioningQuick/private/qpositioningquickglobal_p.h>
#include <QtPositioningQuick/QtPositioningQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtPositioningQuick/6.12.0/QtPositioningQuick/private/qdeclarativepositionsource_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtPositioning/qgeopositioninfo.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#include <cstring>

//  A QDeclarativePositionSource that Python can take functions over in. Every QDeclarativePositionSource
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQDeclarativePositionSourceCall0)(const void *, int *);
typedef void (*CuteQDeclarativePositionSourceCall1)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDeclarativePositionSourceCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDeclarativePositionSourceCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativePositionSourceCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativePositionSourceCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativePositionSourceCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativePositionSourceCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDeclarativePositionSourceCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQDeclarativePositionSource : public QDeclarativePositionSource {
public:
  using QDeclarativePositionSource::QDeclarativePositionSource;
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

  //  void QDeclarativePositionSource::classBegin()
  void classBegin() override {
    if (taken[0]) {
      int handled = 0;
      CuteQDeclarativePositionSourceCall0 call = reinterpret_cast<CuteQDeclarativePositionSourceCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QDeclarativePositionSource::classBegin();
  }

  //  void QDeclarativePositionSource::componentComplete()
  void componentComplete() override {
    if (taken[1]) {
      int handled = 0;
      CuteQDeclarativePositionSourceCall1 call = reinterpret_cast<CuteQDeclarativePositionSourceCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QDeclarativePositionSource::componentComplete();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQDeclarativePositionSourceCall2 call = reinterpret_cast<CuteQDeclarativePositionSourceCall2>(taken[2]);
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
      CuteQDeclarativePositionSourceCall3 call = reinterpret_cast<CuteQDeclarativePositionSourceCall3>(taken[3]);
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
      CuteQDeclarativePositionSourceCall4 call = reinterpret_cast<CuteQDeclarativePositionSourceCall4>(taken[4]);
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
      CuteQDeclarativePositionSourceCall5 call = reinterpret_cast<CuteQDeclarativePositionSourceCall5>(taken[5]);
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
      CuteQDeclarativePositionSourceCall6 call = reinterpret_cast<CuteQDeclarativePositionSourceCall6>(taken[6]);
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
      CuteQDeclarativePositionSourceCall7 call = reinterpret_cast<CuteQDeclarativePositionSourceCall7>(taken[7]);
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
      CuteQDeclarativePositionSourceCall8 call = reinterpret_cast<CuteQDeclarativePositionSourceCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QDeclarativePositionSource::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK26QDeclarativePositionSource10metaObjectEv(
    const QDeclarativePositionSource *self) {
  return self->metaObject();
}

//  QString QDeclarativePositionSource::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN26QDeclarativePositionSource2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QDeclarativePositionSource::tr(s, c, n));
}

//  QDeclarativePositionSource::QDeclarativePositionSource()
extern "C" Q_DECL_EXPORT
QDeclarativePositionSource *ritual_ZN26QDeclarativePositionSourceC1Ev() {
  return new CuteQDeclarativePositionSource();
}

//  QDeclarativePositionSource::~QDeclarativePositionSource()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QDeclarativePositionSourceD1Ev(
    QDeclarativePositionSource *self) {
  delete self;
}

//  void QDeclarativePositionSource::setUpdateInterval(int updateInterval)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QDeclarativePositionSource17setUpdateIntervalEi(
    QDeclarativePositionSource *self,
    int updateInterval) {
  self->setUpdateInterval(updateInterval);
}

//  void QDeclarativePositionSource::setActive(bool active)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QDeclarativePositionSource9setActiveEb(
    QDeclarativePositionSource *self,
    bool active) {
  self->setActive(active);
}

//  void QDeclarativePositionSource::setPreferredPositioningMethods(Positioni
//      ngMethods methods)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QDeclarativePositionSource30setPreferredPositioningMethodsE6QFlagsINS_17PositioningMethodEE(
    QDeclarativePositionSource *self,
    int methods) {
  self->setPreferredPositioningMethods(
      QFlags<QDeclarativePositionSource::PositioningMethod>::fromInt(methods));
}

//  QString QDeclarativePositionSource::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK26QDeclarativePositionSource4nameEv(
    const QDeclarativePositionSource *self) {
  return new QString(self->name());
}

//  void QDeclarativePositionSource::setName(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QDeclarativePositionSource7setNameERK7QString(
    QDeclarativePositionSource *self,
    const QString *name) {
  self->setName(*name);
}

//  int QDeclarativePositionSource::updateInterval() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK26QDeclarativePositionSource14updateIntervalEv(
    const QDeclarativePositionSource *self) {
  return self->updateInterval();
}

//  bool QDeclarativePositionSource::isActive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK26QDeclarativePositionSource8isActiveEv(
    const QDeclarativePositionSource *self) {
  return self->isActive();
}

//  bool QDeclarativePositionSource::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK26QDeclarativePositionSource7isValidEv(
    const QDeclarativePositionSource *self) {
  return self->isValid();
}

//  QDeclarativePosition *QDeclarativePositionSource::position()
extern "C" Q_DECL_EXPORT
QDeclarativePosition *ritual_ZN26QDeclarativePositionSource8positionEv(
    QDeclarativePositionSource *self) {
  return self->position();
}

//  PositioningMethods
//      QDeclarativePositionSource::supportedPositioningMethods() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK26QDeclarativePositionSource27supportedPositioningMethodsEv(
    const QDeclarativePositionSource *self) {
  return static_cast<int>(self->supportedPositioningMethods().toInt());
}

//  PositioningMethods
//      QDeclarativePositionSource::preferredPositioningMethods() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK26QDeclarativePositionSource27preferredPositioningMethodsEv(
    const QDeclarativePositionSource *self) {
  return static_cast<int>(self->preferredPositioningMethods().toInt());
}

//  SourceError QDeclarativePositionSource::sourceError() const
extern "C" Q_DECL_EXPORT
QDeclarativePositionSource::SourceError ritual_ZNK26QDeclarativePositionSource11sourceErrorEv(
    const QDeclarativePositionSource *self) {
  return self->sourceError();
}

//  QGeoPositionInfoSource *QDeclarativePositionSource::positionSource()
//      const
extern "C" Q_DECL_EXPORT
QGeoPositionInfoSource *ritual_ZNK26QDeclarativePositionSource14positionSourceEv(
    const QDeclarativePositionSource *self) {
  return self->positionSource();
}

//  QVariantMap QDeclarativePositionSource::parameterMap() const
extern "C" Q_DECL_EXPORT
QMap<QString, QVariant> *ritual_ZNK26QDeclarativePositionSource12parameterMapEv(
    const QDeclarativePositionSource *self) {
  return new QMap<QString, QVariant>(self->parameterMap());
}

//  void QDeclarativePositionSource::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QDeclarativePositionSource10classBeginEv(
    QDeclarativePositionSource *self) {
  self->classBegin();
}

//  void QDeclarativePositionSource::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QDeclarativePositionSource17componentCompleteEv(
    QDeclarativePositionSource *self) {
  self->componentComplete();
}

//  bool QDeclarativePositionSource::setBackendProperty(const QString &name,
//      const QVariant &value)
extern "C" Q_DECL_EXPORT
bool ritual_ZN26QDeclarativePositionSource18setBackendPropertyERK7QStringRK8QVariant(
    QDeclarativePositionSource *self,
    const QString *name,
    const QVariant *value) {
  return self->setBackendProperty(*name, *value);
}

//  QVariant QDeclarativePositionSource::backendProperty(const QString &name)
//      const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK26QDeclarativePositionSource15backendPropertyERK7QString(
    const QDeclarativePositionSource *self,
    const QString *name) {
  return new QVariant(self->backendProperty(*name));
}

//  void QDeclarativePositionSource::update(int timeout)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QDeclarativePositionSource6updateEi(
    QDeclarativePositionSource *self,
    int timeout) {
  self->update(timeout);
}

//  void QDeclarativePositionSource::start()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QDeclarativePositionSource5startEv(
    QDeclarativePositionSource *self) {
  self->start();
}

//  void QDeclarativePositionSource::stop()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QDeclarativePositionSource4stopEv(
    QDeclarativePositionSource *self) {
  self->stop();
}

//  void QDeclarativePositionSource::positionUpdateReceived(const
//      QGeoPositionInfo &update)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QDeclarativePositionSource22positionUpdateReceivedERK16QGeoPositionInfo(
    QDeclarativePositionSource *self,
    const QGeoPositionInfo *update) {
  self->positionUpdateReceived(*update);
}

//  void QDeclarativePositionSource::onParameterInitialized()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QDeclarativePositionSource22onParameterInitializedEv(
    QDeclarativePositionSource *self) {
  self->onParameterInitialized();
}

//  void
//      QDeclarativePositionSource::notifySupportedPositioningMethodsChanged(
//      )
extern "C" Q_DECL_EXPORT
void ritual_ZN26QDeclarativePositionSource40notifySupportedPositioningMethodsChangedEv(
    QDeclarativePositionSource *self) {
  self->notifySupportedPositioningMethodsChanged();
}

//  void QDeclarativePositionSource::setPosition(const QGeoPositionInfo &pi)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QDeclarativePositionSource11setPositionERK16QGeoPositionInfo(
    QDeclarativePositionSource *self,
    const QGeoPositionInfo *pi) {
  self->setPosition(*pi);
}

//  void QDeclarativePositionSource::setSource(QGeoPositionInfoSource
//      *source)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QDeclarativePositionSource9setSourceEP22QGeoPositionInfoSource(
    QDeclarativePositionSource *self,
    QGeoPositionInfoSource *source) {
  self->setSource(source);
}

//  bool QDeclarativePositionSource::parametersReady()
extern "C" Q_DECL_EXPORT
bool ritual_ZN26QDeclarativePositionSource15parametersReadyEv(
    QDeclarativePositionSource *self) {
  return self->parametersReady();
}

//  void QDeclarativePositionSource::tryAttach(const QString &name, bool
//      useFallback)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QDeclarativePositionSource9tryAttachERK7QStringb(
    QDeclarativePositionSource *self,
    const QString *name,
    bool useFallback) {
  self->tryAttach(*name, useFallback);
}

//  bool QDeclarativePositionSource::isValidActualComputation() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK26QDeclarativePositionSource24isValidActualComputationEv(
    const QDeclarativePositionSource *self) {
  return self->isValidActualComputation();
}

//  PositioningMethods
//      QDeclarativePositionSource::supportedMethodsActualComputation() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK26QDeclarativePositionSource33supportedMethodsActualComputationEv(
    const QDeclarativePositionSource *self) {
  return static_cast<int>(self->supportedMethodsActualComputation().toInt());
}

//  void QDeclarativePositionSource::executeStart()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QDeclarativePositionSource12executeStartEv(
    QDeclarativePositionSource *self) {
  self->executeStart();
}

//  QDeclarativePositionSource as the QQmlParserStatus it is built on
extern "C" Q_DECL_EXPORT
QQmlParserStatus *ritual_cast_QDeclarativePositionSource_QQmlParserStatus(
    QDeclarativePositionSource *self) {
  return static_cast<QQmlParserStatus *>(self);
}

//  a Python function taken by a CuteQDeclarativePositionSource, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDeclarativePositionSource(
    QDeclarativePositionSource *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDeclarativePositionSource *>(self)->take(key, call);
}

//  void QDeclarativePositionSource::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN26QDeclarativePositionSource10classBeginEv(
    QDeclarativePositionSource *self) {
  self->QDeclarativePositionSource::classBegin();
}

//  void QDeclarativePositionSource::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN26QDeclarativePositionSource17componentCompleteEv(
    QDeclarativePositionSource *self) {
  self->QDeclarativePositionSource::componentComplete();
}
