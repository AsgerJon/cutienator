//  Written by dev_tooling.RitualGenerator from the records of
//  QtPositioning/qnmeasatelliteinfosource.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtPositioning/qnmeasatelliteinfosource.h>
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QNmeaSatelliteInfoSource that Python can take functions over in. Every QNmeaSatelliteInfoSource
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQNmeaSatelliteInfoSourceCall0)(const void *, int, int *);
typedef int (*CuteQNmeaSatelliteInfoSourceCall1)(const void *, int *);
typedef int (*CuteQNmeaSatelliteInfoSourceCall2)(const void *, int *);
typedef bool (*CuteQNmeaSatelliteInfoSourceCall3)(const void *, const QString *, const QVariant *, int *);
typedef const QVariant * (*CuteQNmeaSatelliteInfoSourceCall4)(const void *, const QString *, int *);
typedef void (*CuteQNmeaSatelliteInfoSourceCall5)(const void *, int *);
typedef void (*CuteQNmeaSatelliteInfoSourceCall6)(const void *, int *);
typedef void (*CuteQNmeaSatelliteInfoSourceCall7)(const void *, int, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQNmeaSatelliteInfoSourceCall8)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQNmeaSatelliteInfoSourceCall9)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNmeaSatelliteInfoSourceCall10)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNmeaSatelliteInfoSourceCall11)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNmeaSatelliteInfoSourceCall12)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNmeaSatelliteInfoSourceCall13)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNmeaSatelliteInfoSourceCall14)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQNmeaSatelliteInfoSource : public QNmeaSatelliteInfoSource {
public:
  using QNmeaSatelliteInfoSource::QNmeaSatelliteInfoSource;
  void *taken[15] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN23QGeoSatelliteInfoSource17setUpdateIntervalEi")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK23QGeoSatelliteInfoSource21minimumUpdateIntervalEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK23QGeoSatelliteInfoSource5errorEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN23QGeoSatelliteInfoSource18setBackendPropertyERK7QStringRK8QVariant")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK23QGeoSatelliteInfoSource15backendPropertyERK7QString")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN23QGeoSatelliteInfoSource12startUpdatesEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN23QGeoSatelliteInfoSource11stopUpdatesEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN23QGeoSatelliteInfoSource13requestUpdateEi")) {
      taken[7] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[13] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[14] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QNmeaSatelliteInfoSource::setUpdateInterval(int msec)
  void setUpdateInterval(int msec) override {
    if (taken[0]) {
      int handled = 0;
      CuteQNmeaSatelliteInfoSourceCall0 call = reinterpret_cast<CuteQNmeaSatelliteInfoSourceCall0>(taken[0]);
      call(this, msec, &handled);
      if (handled) return;
    }
    QNmeaSatelliteInfoSource::setUpdateInterval(msec);
  }

  //  int QNmeaSatelliteInfoSource::minimumUpdateInterval() const
  int minimumUpdateInterval() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQNmeaSatelliteInfoSourceCall1 call = reinterpret_cast<CuteQNmeaSatelliteInfoSourceCall1>(taken[1]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QNmeaSatelliteInfoSource::minimumUpdateInterval();
  }

  //  Error QNmeaSatelliteInfoSource::error() const
  QGeoSatelliteInfoSource::Error error() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQNmeaSatelliteInfoSourceCall2 call = reinterpret_cast<CuteQNmeaSatelliteInfoSourceCall2>(taken[2]);
      int given = call(this, &handled);
      if (handled) return static_cast<QGeoSatelliteInfoSource::Error>(given);
    }
    return QNmeaSatelliteInfoSource::error();
  }

  //  bool QNmeaSatelliteInfoSource::setBackendProperty(const QString
  //      &name, const QVariant &value)
  bool setBackendProperty(
      const QString &name,
      const QVariant &value) override {
    if (taken[3]) {
      int handled = 0;
      CuteQNmeaSatelliteInfoSourceCall3 call = reinterpret_cast<CuteQNmeaSatelliteInfoSourceCall3>(taken[3]);
      bool given = call(this, &name, &value, &handled);
      if (handled) return given;
    }
    return QNmeaSatelliteInfoSource::setBackendProperty(name, value);
  }

  //  QVariant QNmeaSatelliteInfoSource::backendProperty(const QString
  //      &name) const
  QVariant backendProperty(const QString &name) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQNmeaSatelliteInfoSourceCall4 call = reinterpret_cast<CuteQNmeaSatelliteInfoSourceCall4>(taken[4]);
      const QVariant * given = call(this, &name, &handled);
      if (handled && given) return *given;
    }
    return QNmeaSatelliteInfoSource::backendProperty(name);
  }

  //  void QNmeaSatelliteInfoSource::startUpdates()
  void startUpdates() override {
    if (taken[5]) {
      int handled = 0;
      CuteQNmeaSatelliteInfoSourceCall5 call = reinterpret_cast<CuteQNmeaSatelliteInfoSourceCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    QNmeaSatelliteInfoSource::startUpdates();
  }

  //  void QNmeaSatelliteInfoSource::stopUpdates()
  void stopUpdates() override {
    if (taken[6]) {
      int handled = 0;
      CuteQNmeaSatelliteInfoSourceCall6 call = reinterpret_cast<CuteQNmeaSatelliteInfoSourceCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QNmeaSatelliteInfoSource::stopUpdates();
  }

  //  void QNmeaSatelliteInfoSource::requestUpdate(int timeout)
  void requestUpdate(int timeout) override {
    if (taken[7]) {
      int handled = 0;
      CuteQNmeaSatelliteInfoSourceCall7 call = reinterpret_cast<CuteQNmeaSatelliteInfoSourceCall7>(taken[7]);
      call(this, timeout, &handled);
      if (handled) return;
    }
    QNmeaSatelliteInfoSource::requestUpdate(timeout);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQNmeaSatelliteInfoSourceCall8 call = reinterpret_cast<CuteQNmeaSatelliteInfoSourceCall8>(taken[8]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQNmeaSatelliteInfoSourceCall9 call = reinterpret_cast<CuteQNmeaSatelliteInfoSourceCall9>(taken[9]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQNmeaSatelliteInfoSourceCall10 call = reinterpret_cast<CuteQNmeaSatelliteInfoSourceCall10>(taken[10]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQNmeaSatelliteInfoSourceCall11 call = reinterpret_cast<CuteQNmeaSatelliteInfoSourceCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQNmeaSatelliteInfoSourceCall12 call = reinterpret_cast<CuteQNmeaSatelliteInfoSourceCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[13]) {
      int handled = 0;
      CuteQNmeaSatelliteInfoSourceCall13 call = reinterpret_cast<CuteQNmeaSatelliteInfoSourceCall13>(taken[13]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[14]) {
      int handled = 0;
      CuteQNmeaSatelliteInfoSourceCall14 call = reinterpret_cast<CuteQNmeaSatelliteInfoSourceCall14>(taken[14]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QNmeaSatelliteInfoSource::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK24QNmeaSatelliteInfoSource10metaObjectEv(
    const QNmeaSatelliteInfoSource *self) {
  return self->metaObject();
}

//  QString QNmeaSatelliteInfoSource::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN24QNmeaSatelliteInfoSource2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QNmeaSatelliteInfoSource::tr(s, c, n));
}

//  QNmeaSatelliteInfoSource::QNmeaSatelliteInfoSource(UpdateMode mode,
//      QObject *parent)
extern "C" Q_DECL_EXPORT
QNmeaSatelliteInfoSource *ritual_ZN24QNmeaSatelliteInfoSourceC1ENS_10UpdateModeEP7QObject(
    QNmeaSatelliteInfoSource::UpdateMode mode,
    QObject *parent) {
  return new CuteQNmeaSatelliteInfoSource(mode, parent);
}

//  QNmeaSatelliteInfoSource::~QNmeaSatelliteInfoSource()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QNmeaSatelliteInfoSourceD1Ev(
    QNmeaSatelliteInfoSource *self) {
  delete self;
}

//  UpdateMode QNmeaSatelliteInfoSource::updateMode() const
extern "C" Q_DECL_EXPORT
QNmeaSatelliteInfoSource::UpdateMode ritual_ZNK24QNmeaSatelliteInfoSource10updateModeEv(
    const QNmeaSatelliteInfoSource *self) {
  return self->updateMode();
}

//  void QNmeaSatelliteInfoSource::setDevice(QIODevice *source)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QNmeaSatelliteInfoSource9setDeviceEP9QIODevice(
    QNmeaSatelliteInfoSource *self,
    QIODevice *source) {
  self->setDevice(source);
}

//  QIODevice *QNmeaSatelliteInfoSource::device() const
extern "C" Q_DECL_EXPORT
QIODevice *ritual_ZNK24QNmeaSatelliteInfoSource6deviceEv(
    const QNmeaSatelliteInfoSource *self) {
  return self->device();
}

//  void QNmeaSatelliteInfoSource::setUpdateInterval(int msec)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QNmeaSatelliteInfoSource17setUpdateIntervalEi(
    QNmeaSatelliteInfoSource *self,
    int msec) {
  self->setUpdateInterval(msec);
}

//  int QNmeaSatelliteInfoSource::minimumUpdateInterval() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK24QNmeaSatelliteInfoSource21minimumUpdateIntervalEv(
    const QNmeaSatelliteInfoSource *self) {
  return self->minimumUpdateInterval();
}

//  Error QNmeaSatelliteInfoSource::error() const
extern "C" Q_DECL_EXPORT
QGeoSatelliteInfoSource::Error ritual_ZNK24QNmeaSatelliteInfoSource5errorEv(
    const QNmeaSatelliteInfoSource *self) {
  return self->error();
}

//  bool QNmeaSatelliteInfoSource::setBackendProperty(const QString &name,
//      const QVariant &value)
extern "C" Q_DECL_EXPORT
bool ritual_ZN24QNmeaSatelliteInfoSource18setBackendPropertyERK7QStringRK8QVariant(
    QNmeaSatelliteInfoSource *self,
    const QString *name,
    const QVariant *value) {
  return self->setBackendProperty(*name, *value);
}

//  QVariant QNmeaSatelliteInfoSource::backendProperty(const QString &name)
//      const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK24QNmeaSatelliteInfoSource15backendPropertyERK7QString(
    const QNmeaSatelliteInfoSource *self,
    const QString *name) {
  return new QVariant(self->backendProperty(*name));
}

//  void QNmeaSatelliteInfoSource::startUpdates()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QNmeaSatelliteInfoSource12startUpdatesEv(
    QNmeaSatelliteInfoSource *self) {
  self->startUpdates();
}

//  void QNmeaSatelliteInfoSource::stopUpdates()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QNmeaSatelliteInfoSource11stopUpdatesEv(
    QNmeaSatelliteInfoSource *self) {
  self->stopUpdates();
}

//  void QNmeaSatelliteInfoSource::requestUpdate(int timeout)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QNmeaSatelliteInfoSource13requestUpdateEi(
    QNmeaSatelliteInfoSource *self,
    int timeout) {
  self->requestUpdate(timeout);
}

//  void QNmeaSatelliteInfoSource::setError(QGeoSatelliteInfoSource::Error
//      satelliteError)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QNmeaSatelliteInfoSource8setErrorEN23QGeoSatelliteInfoSource5ErrorE(
    QNmeaSatelliteInfoSource *self,
    QGeoSatelliteInfoSource::Error satelliteError) {
  self->setError(satelliteError);
}

//  a Python function taken by a CuteQNmeaSatelliteInfoSource, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QNmeaSatelliteInfoSource(
    QNmeaSatelliteInfoSource *self,
    const char *key,
    void *call) {
  return static_cast<CuteQNmeaSatelliteInfoSource *>(self)->take(key, call);
}

//  void QNmeaSatelliteInfoSource::setUpdateInterval(int msec)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QNmeaSatelliteInfoSource17setUpdateIntervalEi(
    QNmeaSatelliteInfoSource *self,
    int msec) {
  self->QNmeaSatelliteInfoSource::setUpdateInterval(msec);
}

//  int QNmeaSatelliteInfoSource::minimumUpdateInterval() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK24QNmeaSatelliteInfoSource21minimumUpdateIntervalEv(
    const QNmeaSatelliteInfoSource *self) {
  return self->QNmeaSatelliteInfoSource::minimumUpdateInterval();
}

//  Error QNmeaSatelliteInfoSource::error() const
extern "C" Q_DECL_EXPORT
QGeoSatelliteInfoSource::Error ritual_own_ZNK24QNmeaSatelliteInfoSource5errorEv(
    const QNmeaSatelliteInfoSource *self) {
  return self->QNmeaSatelliteInfoSource::error();
}

//  bool QNmeaSatelliteInfoSource::setBackendProperty(const QString &name,
//      const QVariant &value)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN24QNmeaSatelliteInfoSource18setBackendPropertyERK7QStringRK8QVariant(
    QNmeaSatelliteInfoSource *self,
    const QString *name,
    const QVariant *value) {
  return self->QNmeaSatelliteInfoSource::setBackendProperty(*name, *value);
}

//  QVariant QNmeaSatelliteInfoSource::backendProperty(const QString &name)
//      const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK24QNmeaSatelliteInfoSource15backendPropertyERK7QString(
    const QNmeaSatelliteInfoSource *self,
    const QString *name) {
  return new QVariant(
      self->QNmeaSatelliteInfoSource::backendProperty(
          *name));
}

//  void QNmeaSatelliteInfoSource::startUpdates()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QNmeaSatelliteInfoSource12startUpdatesEv(
    QNmeaSatelliteInfoSource *self) {
  self->QNmeaSatelliteInfoSource::startUpdates();
}

//  void QNmeaSatelliteInfoSource::stopUpdates()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QNmeaSatelliteInfoSource11stopUpdatesEv(
    QNmeaSatelliteInfoSource *self) {
  self->QNmeaSatelliteInfoSource::stopUpdates();
}

//  void QNmeaSatelliteInfoSource::requestUpdate(int timeout)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QNmeaSatelliteInfoSource13requestUpdateEi(
    QNmeaSatelliteInfoSource *self,
    int timeout) {
  self->QNmeaSatelliteInfoSource::requestUpdate(timeout);
}
