//  Written by dev_tooling.RitualGenerator from the records of
//  QtPositioning/qgeopositioninfosource.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtPositioning/qgeopositioninfosource.h>
#include <QtCore/qstring.h>
#include <QtPositioning/qgeopositioninfo.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#include <cstring>
#include <QtCore/QBindable>
#include <QtPositioning/QGeoPositionInfoSource>

//  A QGeoPositionInfoSource that Python can take functions over in. Every QGeoPositionInfoSource
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQGeoPositionInfoSourceCall0)(const void *, int, int *);
typedef void (*CuteQGeoPositionInfoSourceCall1)(const void *, int, int *);
typedef const QGeoPositionInfo * (*CuteQGeoPositionInfoSourceCall2)(const void *, bool, int *);
typedef int (*CuteQGeoPositionInfoSourceCall3)(const void *, int *);
typedef int (*CuteQGeoPositionInfoSourceCall4)(const void *, int *);
typedef bool (*CuteQGeoPositionInfoSourceCall5)(const void *, const QString *, const QVariant *, int *);
typedef const QVariant * (*CuteQGeoPositionInfoSourceCall6)(const void *, const QString *, int *);
typedef int (*CuteQGeoPositionInfoSourceCall7)(const void *, int *);
typedef void (*CuteQGeoPositionInfoSourceCall8)(const void *, int *);
typedef void (*CuteQGeoPositionInfoSourceCall9)(const void *, int *);
typedef void (*CuteQGeoPositionInfoSourceCall10)(const void *, int, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQGeoPositionInfoSourceCall11)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQGeoPositionInfoSourceCall12)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGeoPositionInfoSourceCall13)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGeoPositionInfoSourceCall14)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGeoPositionInfoSourceCall15)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGeoPositionInfoSourceCall16)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGeoPositionInfoSourceCall17)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQGeoPositionInfoSource : public QGeoPositionInfoSource {
public:
  using QGeoPositionInfoSource::QGeoPositionInfoSource;
  void *taken[18] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN22QGeoPositionInfoSource17setUpdateIntervalEi")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QGeoPositionInfoSource30setPreferredPositioningMethodsE6QFlagsINS_17PositioningMethodEE")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK22QGeoPositionInfoSource17lastKnownPositionEb")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK22QGeoPositionInfoSource27supportedPositioningMethodsEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK22QGeoPositionInfoSource21minimumUpdateIntervalEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QGeoPositionInfoSource18setBackendPropertyERK7QStringRK8QVariant")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK22QGeoPositionInfoSource15backendPropertyERK7QString")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK22QGeoPositionInfoSource5errorEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QGeoPositionInfoSource12startUpdatesEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QGeoPositionInfoSource11stopUpdatesEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QGeoPositionInfoSource13requestUpdateEi")) {
      taken[10] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[13] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[14] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[15] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[16] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[17] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QGeoPositionInfoSource::setUpdateInterval(int msec)
  void setUpdateInterval(int msec) override {
    if (taken[0]) {
      int handled = 0;
      CuteQGeoPositionInfoSourceCall0 call = reinterpret_cast<CuteQGeoPositionInfoSourceCall0>(taken[0]);
      call(this, msec, &handled);
      if (handled) return;
    }
    QGeoPositionInfoSource::setUpdateInterval(msec);
  }

  //  void QGeoPositionInfoSource::setPreferredPositioningMethods(Positioni
  //      ngMethods methods)
  void setPreferredPositioningMethods(
      QGeoPositionInfoSource::PositioningMethods methods) override {
    if (taken[1]) {
      int handled = 0;
      CuteQGeoPositionInfoSourceCall1 call = reinterpret_cast<CuteQGeoPositionInfoSourceCall1>(taken[1]);
      call(this, static_cast<int>(methods.toInt()), &handled);
      if (handled) return;
    }
    QGeoPositionInfoSource::setPreferredPositioningMethods(methods);
  }

  //  QGeoPositionInfo QGeoPositionInfoSource::lastKnownPosition(bool
  //      fromSatellitePositioningMethodsOnly) const
  QGeoPositionInfo lastKnownPosition(
      bool fromSatellitePositioningMethodsOnly) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQGeoPositionInfoSourceCall2 call = reinterpret_cast<CuteQGeoPositionInfoSourceCall2>(taken[2]);
      const QGeoPositionInfo * given = call(this, fromSatellitePositioningMethodsOnly, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  PositioningMethods
  //      QGeoPositionInfoSource::supportedPositioningMethods() const
  QGeoPositionInfoSource::PositioningMethods supportedPositioningMethods() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQGeoPositionInfoSourceCall3 call = reinterpret_cast<CuteQGeoPositionInfoSourceCall3>(taken[3]);
      int given = call(this, &handled);
      if (handled) return QFlags<QGeoPositionInfoSource::PositioningMethod>::fromInt(given);
    }
    return {};
  }

  //  int QGeoPositionInfoSource::minimumUpdateInterval() const
  int minimumUpdateInterval() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQGeoPositionInfoSourceCall4 call = reinterpret_cast<CuteQGeoPositionInfoSourceCall4>(taken[4]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QGeoPositionInfoSource::setBackendProperty(const QString &name,
  //      const QVariant &value)
  bool setBackendProperty(
      const QString &name,
      const QVariant &value) override {
    if (taken[5]) {
      int handled = 0;
      CuteQGeoPositionInfoSourceCall5 call = reinterpret_cast<CuteQGeoPositionInfoSourceCall5>(taken[5]);
      bool given = call(this, &name, &value, &handled);
      if (handled) return given;
    }
    return QGeoPositionInfoSource::setBackendProperty(name, value);
  }

  //  QVariant QGeoPositionInfoSource::backendProperty(const QString &name)
  //      const
  QVariant backendProperty(const QString &name) const override {
    if (taken[6]) {
      int handled = 0;
      CuteQGeoPositionInfoSourceCall6 call = reinterpret_cast<CuteQGeoPositionInfoSourceCall6>(taken[6]);
      const QVariant * given = call(this, &name, &handled);
      if (handled && given) return *given;
    }
    return QGeoPositionInfoSource::backendProperty(name);
  }

  //  Error QGeoPositionInfoSource::error() const
  QGeoPositionInfoSource::Error error() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQGeoPositionInfoSourceCall7 call = reinterpret_cast<CuteQGeoPositionInfoSourceCall7>(taken[7]);
      int given = call(this, &handled);
      if (handled) return static_cast<QGeoPositionInfoSource::Error>(given);
    }
    return {};
  }

  //  void QGeoPositionInfoSource::startUpdates()
  void startUpdates() override {
    if (taken[8]) {
      int handled = 0;
      CuteQGeoPositionInfoSourceCall8 call = reinterpret_cast<CuteQGeoPositionInfoSourceCall8>(taken[8]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QGeoPositionInfoSource::stopUpdates()
  void stopUpdates() override {
    if (taken[9]) {
      int handled = 0;
      CuteQGeoPositionInfoSourceCall9 call = reinterpret_cast<CuteQGeoPositionInfoSourceCall9>(taken[9]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QGeoPositionInfoSource::requestUpdate(int timeout)
  void requestUpdate(int timeout) override {
    if (taken[10]) {
      int handled = 0;
      CuteQGeoPositionInfoSourceCall10 call = reinterpret_cast<CuteQGeoPositionInfoSourceCall10>(taken[10]);
      call(this, timeout, &handled);
      if (handled) return;
    }
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQGeoPositionInfoSourceCall11 call = reinterpret_cast<CuteQGeoPositionInfoSourceCall11>(taken[11]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQGeoPositionInfoSourceCall12 call = reinterpret_cast<CuteQGeoPositionInfoSourceCall12>(taken[12]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQGeoPositionInfoSourceCall13 call = reinterpret_cast<CuteQGeoPositionInfoSourceCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQGeoPositionInfoSourceCall14 call = reinterpret_cast<CuteQGeoPositionInfoSourceCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQGeoPositionInfoSourceCall15 call = reinterpret_cast<CuteQGeoPositionInfoSourceCall15>(taken[15]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[16]) {
      int handled = 0;
      CuteQGeoPositionInfoSourceCall16 call = reinterpret_cast<CuteQGeoPositionInfoSourceCall16>(taken[16]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[17]) {
      int handled = 0;
      CuteQGeoPositionInfoSourceCall17 call = reinterpret_cast<CuteQGeoPositionInfoSourceCall17>(taken[17]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QGeoPositionInfoSource::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK22QGeoPositionInfoSource10metaObjectEv(
    const QGeoPositionInfoSource *self) {
  return self->metaObject();
}

//  void *QGeoPositionInfoSource::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN22QGeoPositionInfoSource11qt_metacastEPKc(
    QGeoPositionInfoSource *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QGeoPositionInfoSource::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN22QGeoPositionInfoSource11qt_metacallEN11QMetaObject4CallEiPPv(
    QGeoPositionInfoSource *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QGeoPositionInfoSource::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN22QGeoPositionInfoSource2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QGeoPositionInfoSource::tr(s, c, n));
}

//  QGeoPositionInfoSource::QGeoPositionInfoSource(QObject *parent)
extern "C" Q_DECL_EXPORT
QGeoPositionInfoSource *ritual_ZN22QGeoPositionInfoSourceC1EP7QObject(
    QObject *parent) {
  return new CuteQGeoPositionInfoSource(parent);
}

//  QGeoPositionInfoSource::~QGeoPositionInfoSource()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGeoPositionInfoSourceD1Ev(QGeoPositionInfoSource *self) {
  delete self;
}

//  void QGeoPositionInfoSource::setUpdateInterval(int msec)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGeoPositionInfoSource17setUpdateIntervalEi(
    QGeoPositionInfoSource *self,
    int msec) {
  self->setUpdateInterval(msec);
}

//  int QGeoPositionInfoSource::updateInterval() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK22QGeoPositionInfoSource14updateIntervalEv(
    const QGeoPositionInfoSource *self) {
  return self->updateInterval();
}

//  QBindable<int> QGeoPositionInfoSource::bindableUpdateInterval()
extern "C" Q_DECL_EXPORT
QBindable<int> *ritual_ZN22QGeoPositionInfoSource22bindableUpdateIntervalEv(
    QGeoPositionInfoSource *self) {
  return new QBindable<int>(self->bindableUpdateInterval());
}

//  void
//      QGeoPositionInfoSource::setPreferredPositioningMethods(PositioningMet
//      hods methods)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGeoPositionInfoSource30setPreferredPositioningMethodsE6QFlagsINS_17PositioningMethodEE(
    QGeoPositionInfoSource *self,
    int methods) {
  self->setPreferredPositioningMethods(
      QFlags<QGeoPositionInfoSource::PositioningMethod>::fromInt(methods));
}

//  PositioningMethods QGeoPositionInfoSource::preferredPositioningMethods()
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK22QGeoPositionInfoSource27preferredPositioningMethodsEv(
    const QGeoPositionInfoSource *self) {
  return static_cast<int>(self->preferredPositioningMethods().toInt());
}

//  QBindable<PositioningMethods>
//      QGeoPositionInfoSource::bindablePreferredPositioningMethods()
extern "C" Q_DECL_EXPORT
QBindable<QGeoPositionInfoSource::PositioningMethods> *ritual_ZN22QGeoPositionInfoSource35bindablePreferredPositioningMethodsEv(
    QGeoPositionInfoSource *self) {
  return new QBindable<QGeoPositionInfoSource::PositioningMethods>(
      self->bindablePreferredPositioningMethods());
}

//  QGeoPositionInfo QGeoPositionInfoSource::lastKnownPosition(bool
//      fromSatellitePositioningMethodsOnly) const
extern "C" Q_DECL_EXPORT
QGeoPositionInfo *ritual_ZNK22QGeoPositionInfoSource17lastKnownPositionEb(
    const QGeoPositionInfoSource *self,
    bool fromSatellitePositioningMethodsOnly) {
  return new QGeoPositionInfo(
      self->lastKnownPosition(
          fromSatellitePositioningMethodsOnly));
}

//  PositioningMethods QGeoPositionInfoSource::supportedPositioningMethods()
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK22QGeoPositionInfoSource27supportedPositioningMethodsEv(
    const QGeoPositionInfoSource *self) {
  return static_cast<int>(self->supportedPositioningMethods().toInt());
}

//  int QGeoPositionInfoSource::minimumUpdateInterval() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK22QGeoPositionInfoSource21minimumUpdateIntervalEv(
    const QGeoPositionInfoSource *self) {
  return self->minimumUpdateInterval();
}

//  QString QGeoPositionInfoSource::sourceName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK22QGeoPositionInfoSource10sourceNameEv(
    const QGeoPositionInfoSource *self) {
  return new QString(self->sourceName());
}

//  bool QGeoPositionInfoSource::setBackendProperty(const QString &name,
//      const QVariant &value)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QGeoPositionInfoSource18setBackendPropertyERK7QStringRK8QVariant(
    QGeoPositionInfoSource *self,
    const QString *name,
    const QVariant *value) {
  return self->setBackendProperty(*name, *value);
}

//  QVariant QGeoPositionInfoSource::backendProperty(const QString &name)
//      const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK22QGeoPositionInfoSource15backendPropertyERK7QString(
    const QGeoPositionInfoSource *self,
    const QString *name) {
  return new QVariant(self->backendProperty(*name));
}

//  QGeoPositionInfoSource
//      *QGeoPositionInfoSource::createDefaultSource(QObject *parent)
extern "C" Q_DECL_EXPORT
QGeoPositionInfoSource *ritual_ZN22QGeoPositionInfoSource19createDefaultSourceEP7QObject(
    QObject *parent) {
  return QGeoPositionInfoSource::createDefaultSource(parent);
}

//  QGeoPositionInfoSource *QGeoPositionInfoSource::createDefaultSource(const
//      QVariantMap &parameters, QObject *parent)
extern "C" Q_DECL_EXPORT
QGeoPositionInfoSource *ritual_ZN22QGeoPositionInfoSource19createDefaultSourceERK4QMapI7QString8QVariantEP7QObject(
    const QMap<QString, QVariant> *parameters,
    QObject *parent) {
  return QGeoPositionInfoSource::createDefaultSource(*parameters, parent);
}

//  QGeoPositionInfoSource *QGeoPositionInfoSource::createSource(const
//      QString &sourceName, QObject *parent)
extern "C" Q_DECL_EXPORT
QGeoPositionInfoSource *ritual_ZN22QGeoPositionInfoSource12createSourceERK7QStringP7QObject(
    const QString *sourceName,
    QObject *parent) {
  return QGeoPositionInfoSource::createSource(*sourceName, parent);
}

//  QGeoPositionInfoSource *QGeoPositionInfoSource::createSource(const
//      QString &sourceName, const QVariantMap &parameters, QObject *parent)
extern "C" Q_DECL_EXPORT
QGeoPositionInfoSource *ritual_ZN22QGeoPositionInfoSource12createSourceERK7QStringRK4QMapIS0_8QVariantEP7QObject(
    const QString *sourceName,
    const QMap<QString, QVariant> *parameters,
    QObject *parent) {
  return QGeoPositionInfoSource::createSource(
      *sourceName,
      *parameters,
      parent);
}

//  QStringList QGeoPositionInfoSource::availableSources()
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZN22QGeoPositionInfoSource16availableSourcesEv() {
  return new QList<QString>(QGeoPositionInfoSource::availableSources());
}

//  Error QGeoPositionInfoSource::error() const
extern "C" Q_DECL_EXPORT
QGeoPositionInfoSource::Error ritual_ZNK22QGeoPositionInfoSource5errorEv(
    const QGeoPositionInfoSource *self) {
  return self->error();
}

//  void QGeoPositionInfoSource::startUpdates()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGeoPositionInfoSource12startUpdatesEv(
    QGeoPositionInfoSource *self) {
  self->startUpdates();
}

//  void QGeoPositionInfoSource::stopUpdates()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGeoPositionInfoSource11stopUpdatesEv(
    QGeoPositionInfoSource *self) {
  self->stopUpdates();
}

//  void QGeoPositionInfoSource::requestUpdate(int timeout)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGeoPositionInfoSource13requestUpdateEi(
    QGeoPositionInfoSource *self,
    int timeout) {
  self->requestUpdate(timeout);
}

//  void QGeoPositionInfoSource::positionUpdated(const QGeoPositionInfo
//      &update)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGeoPositionInfoSource15positionUpdatedERK16QGeoPositionInfo(
    QGeoPositionInfoSource *self,
    const QGeoPositionInfo *update) {
  self->positionUpdated(*update);
}

//  void QGeoPositionInfoSource::errorOccurred(QGeoPositionInfoSource::Error
//      a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGeoPositionInfoSource13errorOccurredENS_5ErrorE(
    QGeoPositionInfoSource *self,
    QGeoPositionInfoSource::Error a0) {
  self->errorOccurred(a0);
}

//  void QGeoPositionInfoSource::supportedPositioningMethodsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGeoPositionInfoSource34supportedPositioningMethodsChangedEv(
    QGeoPositionInfoSource *self) {
  self->supportedPositioningMethodsChanged();
}

//  QGeoPositionInfoSource::QGeoPositionInfoSource(QGeoPositionInfoSourcePriv
//      ate &dd, QObject *parent)
extern "C" Q_DECL_EXPORT
QGeoPositionInfoSource *ritual_ZN22QGeoPositionInfoSourceC1ER29QGeoPositionInfoSourcePrivateP7QObject(
    QGeoPositionInfoSourcePrivate *dd,
    QObject *parent) {
  return new CuteQGeoPositionInfoSource(*dd, parent);
}

//  QGeoPositionInfoSourcePrivate *QGeoPositionInfoSource::d_func()
extern "C" Q_DECL_EXPORT
QGeoPositionInfoSourcePrivate *ritual_ZN22QGeoPositionInfoSource6d_funcEv(
    QGeoPositionInfoSource *self) {
  return self->d_func();
}

//  const QGeoPositionInfoSourcePrivate *QGeoPositionInfoSource::d_func()
//      const
extern "C" Q_DECL_EXPORT
const QGeoPositionInfoSourcePrivate *ritual_ZNK22QGeoPositionInfoSource6d_funcEv(
    const QGeoPositionInfoSource *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQGeoPositionInfoSource, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGeoPositionInfoSource(
    QGeoPositionInfoSource *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGeoPositionInfoSource *>(self)->take(key, call);
}

//  void QGeoPositionInfoSource::setUpdateInterval(int msec)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QGeoPositionInfoSource17setUpdateIntervalEi(
    QGeoPositionInfoSource *self,
    int msec) {
  self->QGeoPositionInfoSource::setUpdateInterval(msec);
}

//  void
//      QGeoPositionInfoSource::setPreferredPositioningMethods(PositioningMet
//      hods methods)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QGeoPositionInfoSource30setPreferredPositioningMethodsE6QFlagsINS_17PositioningMethodEE(
    QGeoPositionInfoSource *self,
    int methods) {
  self->QGeoPositionInfoSource::setPreferredPositioningMethods(
      QFlags<QGeoPositionInfoSource::PositioningMethod>::fromInt(methods));
}

//  bool QGeoPositionInfoSource::setBackendProperty(const QString &name,
//      const QVariant &value)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN22QGeoPositionInfoSource18setBackendPropertyERK7QStringRK8QVariant(
    QGeoPositionInfoSource *self,
    const QString *name,
    const QVariant *value) {
  return self->QGeoPositionInfoSource::setBackendProperty(*name, *value);
}

//  QVariant QGeoPositionInfoSource::backendProperty(const QString &name)
//      const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK22QGeoPositionInfoSource15backendPropertyERK7QString(
    const QGeoPositionInfoSource *self,
    const QString *name) {
  return new QVariant(self->QGeoPositionInfoSource::backendProperty(*name));
}

//  a QBindable<int> a ritual of QGeoPositionInfoSource gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QGeoPositionInfoSource__QBindable_int(
    QBindable<int> *self) {
  delete self;
}

//  a QBindable<QGeoPositionInfoSource::PositioningMethods> a ritual of
//      QGeoPositionInfoSource gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QGeoPositionInfoSource__QBindable_QGeoPositionInfoSource_PositioningMethods(
    QBindable<QGeoPositionInfoSource::PositioningMethods> *self) {
  delete self;
}
