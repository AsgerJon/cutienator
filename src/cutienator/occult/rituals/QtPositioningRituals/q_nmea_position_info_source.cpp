//  Written by dev_tooling.RitualGenerator from the records of
//  QtPositioning/qnmeapositioninfosource.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtPositioning/qnmeapositioninfosource.h>
#include <QtCore/qstring.h>
#include <QtPositioning/qgeopositioninfo.h>
#include <QtCore/qbytearrayview.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QNmeaPositionInfoSource that Python can take functions over in. Every QNmeaPositionInfoSource
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQNmeaPositionInfoSourceCall0)(const void *, int, int *);
typedef const QGeoPositionInfo * (*CuteQNmeaPositionInfoSourceCall1)(const void *, bool, int *);
typedef int (*CuteQNmeaPositionInfoSourceCall2)(const void *, int *);
typedef int (*CuteQNmeaPositionInfoSourceCall3)(const void *, int *);
typedef int (*CuteQNmeaPositionInfoSourceCall4)(const void *, int *);
typedef void (*CuteQNmeaPositionInfoSourceCall5)(const void *, int *);
typedef void (*CuteQNmeaPositionInfoSourceCall6)(const void *, int *);
typedef void (*CuteQNmeaPositionInfoSourceCall7)(const void *, int, int *);
typedef void (*CuteQNmeaPositionInfoSourceCall8)(const void *, int, int *);
typedef bool (*CuteQNmeaPositionInfoSourceCall9)(const void *, const QString *, const QVariant *, int *);
typedef const QVariant * (*CuteQNmeaPositionInfoSourceCall10)(const void *, const QString *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQNmeaPositionInfoSourceCall11)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQNmeaPositionInfoSourceCall12)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNmeaPositionInfoSourceCall13)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNmeaPositionInfoSourceCall14)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNmeaPositionInfoSourceCall15)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNmeaPositionInfoSourceCall16)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNmeaPositionInfoSourceCall17)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQNmeaPositionInfoSource : public QNmeaPositionInfoSource {
public:
  using QNmeaPositionInfoSource::QNmeaPositionInfoSource;
  void *taken[18] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN22QGeoPositionInfoSource17setUpdateIntervalEi")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK22QGeoPositionInfoSource17lastKnownPositionEb")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK22QGeoPositionInfoSource27supportedPositioningMethodsEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK22QGeoPositionInfoSource21minimumUpdateIntervalEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK22QGeoPositionInfoSource5errorEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QGeoPositionInfoSource12startUpdatesEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QGeoPositionInfoSource11stopUpdatesEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QGeoPositionInfoSource13requestUpdateEi")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QGeoPositionInfoSource30setPreferredPositioningMethodsE6QFlagsINS_17PositioningMethodEE")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QGeoPositionInfoSource18setBackendPropertyERK7QStringRK8QVariant")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK22QGeoPositionInfoSource15backendPropertyERK7QString")) {
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

  //  void QNmeaPositionInfoSource::setUpdateInterval(int msec)
  void setUpdateInterval(int msec) override {
    if (taken[0]) {
      int handled = 0;
      CuteQNmeaPositionInfoSourceCall0 call = reinterpret_cast<CuteQNmeaPositionInfoSourceCall0>(taken[0]);
      call(this, msec, &handled);
      if (handled) return;
    }
    QNmeaPositionInfoSource::setUpdateInterval(msec);
  }

  //  QGeoPositionInfo QNmeaPositionInfoSource::lastKnownPosition(bool
  //      fromSatellitePositioningMethodsOnly) const
  QGeoPositionInfo lastKnownPosition(
      bool fromSatellitePositioningMethodsOnly) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQNmeaPositionInfoSourceCall1 call = reinterpret_cast<CuteQNmeaPositionInfoSourceCall1>(taken[1]);
      const QGeoPositionInfo * given = call(this, fromSatellitePositioningMethodsOnly, &handled);
      if (handled && given) return *given;
    }
    return QNmeaPositionInfoSource::lastKnownPosition(fromSatellitePositioningMethodsOnly);
  }

  //  PositioningMethods
  //      QNmeaPositionInfoSource::supportedPositioningMethods() const
  QGeoPositionInfoSource::PositioningMethods supportedPositioningMethods() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQNmeaPositionInfoSourceCall2 call = reinterpret_cast<CuteQNmeaPositionInfoSourceCall2>(taken[2]);
      int given = call(this, &handled);
      if (handled) return QFlags<QGeoPositionInfoSource::PositioningMethod>::fromInt(given);
    }
    return QNmeaPositionInfoSource::supportedPositioningMethods();
  }

  //  int QNmeaPositionInfoSource::minimumUpdateInterval() const
  int minimumUpdateInterval() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQNmeaPositionInfoSourceCall3 call = reinterpret_cast<CuteQNmeaPositionInfoSourceCall3>(taken[3]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QNmeaPositionInfoSource::minimumUpdateInterval();
  }

  //  Error QNmeaPositionInfoSource::error() const
  QGeoPositionInfoSource::Error error() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQNmeaPositionInfoSourceCall4 call = reinterpret_cast<CuteQNmeaPositionInfoSourceCall4>(taken[4]);
      int given = call(this, &handled);
      if (handled) return static_cast<QGeoPositionInfoSource::Error>(given);
    }
    return QNmeaPositionInfoSource::error();
  }

  //  void QNmeaPositionInfoSource::startUpdates()
  void startUpdates() override {
    if (taken[5]) {
      int handled = 0;
      CuteQNmeaPositionInfoSourceCall5 call = reinterpret_cast<CuteQNmeaPositionInfoSourceCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    QNmeaPositionInfoSource::startUpdates();
  }

  //  void QNmeaPositionInfoSource::stopUpdates()
  void stopUpdates() override {
    if (taken[6]) {
      int handled = 0;
      CuteQNmeaPositionInfoSourceCall6 call = reinterpret_cast<CuteQNmeaPositionInfoSourceCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QNmeaPositionInfoSource::stopUpdates();
  }

  //  void QNmeaPositionInfoSource::requestUpdate(int timeout)
  void requestUpdate(int timeout) override {
    if (taken[7]) {
      int handled = 0;
      CuteQNmeaPositionInfoSourceCall7 call = reinterpret_cast<CuteQNmeaPositionInfoSourceCall7>(taken[7]);
      call(this, timeout, &handled);
      if (handled) return;
    }
    QNmeaPositionInfoSource::requestUpdate(timeout);
  }

  //  void QGeoPositionInfoSource::setPreferredPositioningMethods(Positioni
  //      ngMethods methods)
  void setPreferredPositioningMethods(
      QGeoPositionInfoSource::PositioningMethods methods) override {
    if (taken[8]) {
      int handled = 0;
      CuteQNmeaPositionInfoSourceCall8 call = reinterpret_cast<CuteQNmeaPositionInfoSourceCall8>(taken[8]);
      call(this, static_cast<int>(methods.toInt()), &handled);
      if (handled) return;
    }
    QGeoPositionInfoSource::setPreferredPositioningMethods(methods);
  }

  //  bool QGeoPositionInfoSource::setBackendProperty(const QString &name,
  //      const QVariant &value)
  bool setBackendProperty(
      const QString &name,
      const QVariant &value) override {
    if (taken[9]) {
      int handled = 0;
      CuteQNmeaPositionInfoSourceCall9 call = reinterpret_cast<CuteQNmeaPositionInfoSourceCall9>(taken[9]);
      bool given = call(this, &name, &value, &handled);
      if (handled) return given;
    }
    return QGeoPositionInfoSource::setBackendProperty(name, value);
  }

  //  QVariant QGeoPositionInfoSource::backendProperty(const QString &name)
  //      const
  QVariant backendProperty(const QString &name) const override {
    if (taken[10]) {
      int handled = 0;
      CuteQNmeaPositionInfoSourceCall10 call = reinterpret_cast<CuteQNmeaPositionInfoSourceCall10>(taken[10]);
      const QVariant * given = call(this, &name, &handled);
      if (handled && given) return *given;
    }
    return QGeoPositionInfoSource::backendProperty(name);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQNmeaPositionInfoSourceCall11 call = reinterpret_cast<CuteQNmeaPositionInfoSourceCall11>(taken[11]);
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
      CuteQNmeaPositionInfoSourceCall12 call = reinterpret_cast<CuteQNmeaPositionInfoSourceCall12>(taken[12]);
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
      CuteQNmeaPositionInfoSourceCall13 call = reinterpret_cast<CuteQNmeaPositionInfoSourceCall13>(taken[13]);
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
      CuteQNmeaPositionInfoSourceCall14 call = reinterpret_cast<CuteQNmeaPositionInfoSourceCall14>(taken[14]);
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
      CuteQNmeaPositionInfoSourceCall15 call = reinterpret_cast<CuteQNmeaPositionInfoSourceCall15>(taken[15]);
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
      CuteQNmeaPositionInfoSourceCall16 call = reinterpret_cast<CuteQNmeaPositionInfoSourceCall16>(taken[16]);
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
      CuteQNmeaPositionInfoSourceCall17 call = reinterpret_cast<CuteQNmeaPositionInfoSourceCall17>(taken[17]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QNmeaPositionInfoSource::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK23QNmeaPositionInfoSource10metaObjectEv(
    const QNmeaPositionInfoSource *self) {
  return self->metaObject();
}

//  void *QNmeaPositionInfoSource::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN23QNmeaPositionInfoSource11qt_metacastEPKc(
    QNmeaPositionInfoSource *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QNmeaPositionInfoSource::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN23QNmeaPositionInfoSource11qt_metacallEN11QMetaObject4CallEiPPv(
    QNmeaPositionInfoSource *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QNmeaPositionInfoSource::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN23QNmeaPositionInfoSource2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QNmeaPositionInfoSource::tr(s, c, n));
}

//  QNmeaPositionInfoSource::QNmeaPositionInfoSource(UpdateMode updateMode,
//      QObject *parent)
extern "C" Q_DECL_EXPORT
QNmeaPositionInfoSource *ritual_ZN23QNmeaPositionInfoSourceC1ENS_10UpdateModeEP7QObject(
    QNmeaPositionInfoSource::UpdateMode updateMode,
    QObject *parent) {
  return new CuteQNmeaPositionInfoSource(updateMode, parent);
}

//  QNmeaPositionInfoSource::~QNmeaPositionInfoSource()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QNmeaPositionInfoSourceD1Ev(QNmeaPositionInfoSource *self) {
  delete self;
}

//  void QNmeaPositionInfoSource::setUserEquivalentRangeError(double uere)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QNmeaPositionInfoSource27setUserEquivalentRangeErrorEd(
    QNmeaPositionInfoSource *self,
    double uere) {
  self->setUserEquivalentRangeError(uere);
}

//  double QNmeaPositionInfoSource::userEquivalentRangeError() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK23QNmeaPositionInfoSource24userEquivalentRangeErrorEv(
    const QNmeaPositionInfoSource *self) {
  return self->userEquivalentRangeError();
}

//  UpdateMode QNmeaPositionInfoSource::updateMode() const
extern "C" Q_DECL_EXPORT
QNmeaPositionInfoSource::UpdateMode ritual_ZNK23QNmeaPositionInfoSource10updateModeEv(
    const QNmeaPositionInfoSource *self) {
  return self->updateMode();
}

//  void QNmeaPositionInfoSource::setDevice(QIODevice *source)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QNmeaPositionInfoSource9setDeviceEP9QIODevice(
    QNmeaPositionInfoSource *self,
    QIODevice *source) {
  self->setDevice(source);
}

//  QIODevice *QNmeaPositionInfoSource::device() const
extern "C" Q_DECL_EXPORT
QIODevice *ritual_ZNK23QNmeaPositionInfoSource6deviceEv(
    const QNmeaPositionInfoSource *self) {
  return self->device();
}

//  void QNmeaPositionInfoSource::setUpdateInterval(int msec)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QNmeaPositionInfoSource17setUpdateIntervalEi(
    QNmeaPositionInfoSource *self,
    int msec) {
  self->setUpdateInterval(msec);
}

//  QGeoPositionInfo QNmeaPositionInfoSource::lastKnownPosition(bool
//      fromSatellitePositioningMethodsOnly) const
extern "C" Q_DECL_EXPORT
QGeoPositionInfo *ritual_ZNK23QNmeaPositionInfoSource17lastKnownPositionEb(
    const QNmeaPositionInfoSource *self,
    bool fromSatellitePositioningMethodsOnly) {
  return new QGeoPositionInfo(
      self->lastKnownPosition(
          fromSatellitePositioningMethodsOnly));
}

//  PositioningMethods QNmeaPositionInfoSource::supportedPositioningMethods()
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK23QNmeaPositionInfoSource27supportedPositioningMethodsEv(
    const QNmeaPositionInfoSource *self) {
  return static_cast<int>(self->supportedPositioningMethods().toInt());
}

//  int QNmeaPositionInfoSource::minimumUpdateInterval() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK23QNmeaPositionInfoSource21minimumUpdateIntervalEv(
    const QNmeaPositionInfoSource *self) {
  return self->minimumUpdateInterval();
}

//  Error QNmeaPositionInfoSource::error() const
extern "C" Q_DECL_EXPORT
QGeoPositionInfoSource::Error ritual_ZNK23QNmeaPositionInfoSource5errorEv(
    const QNmeaPositionInfoSource *self) {
  return self->error();
}

//  void QNmeaPositionInfoSource::startUpdates()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QNmeaPositionInfoSource12startUpdatesEv(
    QNmeaPositionInfoSource *self) {
  self->startUpdates();
}

//  void QNmeaPositionInfoSource::stopUpdates()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QNmeaPositionInfoSource11stopUpdatesEv(
    QNmeaPositionInfoSource *self) {
  self->stopUpdates();
}

//  void QNmeaPositionInfoSource::requestUpdate(int timeout)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QNmeaPositionInfoSource13requestUpdateEi(
    QNmeaPositionInfoSource *self,
    int timeout) {
  self->requestUpdate(timeout);
}

#if QT_DEPRECATED_SINCE(7, 0)
//  bool QNmeaPositionInfoSource::parsePosInfoFromNmeaData(const char *data,
//      int size, QGeoPositionInfo *posInfo, bool *hasFix)
extern "C" Q_DECL_EXPORT
bool ritual_ZN23QNmeaPositionInfoSource24parsePosInfoFromNmeaDataEPKciP16QGeoPositionInfoPb(
    QNmeaPositionInfoSource *self,
    const char *data,
    int size,
    QGeoPositionInfo *posInfo,
    bool *hasFix) {
  return self->parsePosInfoFromNmeaData(data, size, posInfo, hasFix);
}
#endif  // QT_DEPRECATED_SINCE(7, 0)

//  bool QNmeaPositionInfoSource::parsePosInfoFromNmeaData(QByteArrayView
//      data, QGeoPositionInfo *posInfo, bool *hasFix)
extern "C" Q_DECL_EXPORT
bool ritual_ZN23QNmeaPositionInfoSource24parsePosInfoFromNmeaDataE14QByteArrayViewP16QGeoPositionInfoPb(
    QNmeaPositionInfoSource *self,
    const QByteArrayView *data,
    QGeoPositionInfo *posInfo,
    bool *hasFix) {
  return self->parsePosInfoFromNmeaData(*data, posInfo, hasFix);
}

//  void QNmeaPositionInfoSource::setError(QGeoPositionInfoSource::Error
//      positionError)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QNmeaPositionInfoSource8setErrorEN22QGeoPositionInfoSource5ErrorE(
    QNmeaPositionInfoSource *self,
    QGeoPositionInfoSource::Error positionError) {
  self->setError(positionError);
}

//  a Python function taken by a CuteQNmeaPositionInfoSource, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QNmeaPositionInfoSource(
    QNmeaPositionInfoSource *self,
    const char *key,
    void *call) {
  return static_cast<CuteQNmeaPositionInfoSource *>(self)->take(key, call);
}

//  void QNmeaPositionInfoSource::setUpdateInterval(int msec)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QNmeaPositionInfoSource17setUpdateIntervalEi(
    QNmeaPositionInfoSource *self,
    int msec) {
  self->QNmeaPositionInfoSource::setUpdateInterval(msec);
}

//  QGeoPositionInfo QNmeaPositionInfoSource::lastKnownPosition(bool
//      fromSatellitePositioningMethodsOnly) const
extern "C" Q_DECL_EXPORT
QGeoPositionInfo *ritual_own_ZNK23QNmeaPositionInfoSource17lastKnownPositionEb(
    const QNmeaPositionInfoSource *self,
    bool fromSatellitePositioningMethodsOnly) {
  return new QGeoPositionInfo(
      self->QNmeaPositionInfoSource::lastKnownPosition(
          fromSatellitePositioningMethodsOnly));
}

//  PositioningMethods QNmeaPositionInfoSource::supportedPositioningMethods()
//      const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK23QNmeaPositionInfoSource27supportedPositioningMethodsEv(
    const QNmeaPositionInfoSource *self) {
  return static_cast<int>(
      self->QNmeaPositionInfoSource::supportedPositioningMethods().toInt());
}

//  int QNmeaPositionInfoSource::minimumUpdateInterval() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK23QNmeaPositionInfoSource21minimumUpdateIntervalEv(
    const QNmeaPositionInfoSource *self) {
  return self->QNmeaPositionInfoSource::minimumUpdateInterval();
}

//  Error QNmeaPositionInfoSource::error() const
extern "C" Q_DECL_EXPORT
QGeoPositionInfoSource::Error ritual_own_ZNK23QNmeaPositionInfoSource5errorEv(
    const QNmeaPositionInfoSource *self) {
  return self->QNmeaPositionInfoSource::error();
}

//  void QNmeaPositionInfoSource::startUpdates()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QNmeaPositionInfoSource12startUpdatesEv(
    QNmeaPositionInfoSource *self) {
  self->QNmeaPositionInfoSource::startUpdates();
}

//  void QNmeaPositionInfoSource::stopUpdates()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QNmeaPositionInfoSource11stopUpdatesEv(
    QNmeaPositionInfoSource *self) {
  self->QNmeaPositionInfoSource::stopUpdates();
}

//  void QNmeaPositionInfoSource::requestUpdate(int timeout)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QNmeaPositionInfoSource13requestUpdateEi(
    QNmeaPositionInfoSource *self,
    int timeout) {
  self->QNmeaPositionInfoSource::requestUpdate(timeout);
}
