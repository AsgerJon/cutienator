//  Written by dev_tooling.RitualGenerator from the records of
//  QtSensors/qsensorbackend.h, Qt 6.12.0. Changes made here are lost.
#include <QtSensors/qsensorbackend.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QSensorBackend that Python can take functions over in. Every QSensorBackend
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQSensorBackendCall0)(const void *, int *);
typedef void (*CuteQSensorBackendCall1)(const void *, int *);
typedef bool (*CuteQSensorBackendCall2)(const void *, int, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSensorBackendCall3)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSensorBackendCall4)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSensorBackendCall5)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSensorBackendCall6)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSensorBackendCall7)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSensorBackendCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSensorBackendCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQSensorBackend : public QSensorBackend {
public:
  using QSensorBackend::QSensorBackend;
  void *taken[10] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN14QSensorBackend5startEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QSensorBackend4stopEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QSensorBackend18isFeatureSupportedEN7QSensor7FeatureE")) {
      taken[2] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QSensorBackend::start()
  void start() override {
    if (taken[0]) {
      int handled = 0;
      CuteQSensorBackendCall0 call = reinterpret_cast<CuteQSensorBackendCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QSensorBackend::stop()
  void stop() override {
    if (taken[1]) {
      int handled = 0;
      CuteQSensorBackendCall1 call = reinterpret_cast<CuteQSensorBackendCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  bool QSensorBackend::isFeatureSupported(QSensor::Feature feature)
  //      const
  bool isFeatureSupported(QSensor::Feature feature) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQSensorBackendCall2 call = reinterpret_cast<CuteQSensorBackendCall2>(taken[2]);
      bool given = call(this, static_cast<int>(feature), &handled);
      if (handled) return given;
    }
    return QSensorBackend::isFeatureSupported(feature);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQSensorBackendCall3 call = reinterpret_cast<CuteQSensorBackendCall3>(taken[3]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQSensorBackendCall4 call = reinterpret_cast<CuteQSensorBackendCall4>(taken[4]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQSensorBackendCall5 call = reinterpret_cast<CuteQSensorBackendCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQSensorBackendCall6 call = reinterpret_cast<CuteQSensorBackendCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQSensorBackendCall7 call = reinterpret_cast<CuteQSensorBackendCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[8]) {
      int handled = 0;
      CuteQSensorBackendCall8 call = reinterpret_cast<CuteQSensorBackendCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[9]) {
      int handled = 0;
      CuteQSensorBackendCall9 call = reinterpret_cast<CuteQSensorBackendCall9>(taken[9]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QSensorBackend::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14QSensorBackend10metaObjectEv(
    const QSensorBackend *self) {
  return self->metaObject();
}

//  QString QSensorBackend::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QSensorBackend2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QSensorBackend::tr(s, c, n));
}

//  QSensorBackend::~QSensorBackend()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSensorBackendD1Ev(QSensorBackend *self) {
  delete self;
}

//  void QSensorBackend::start()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSensorBackend5startEv(QSensorBackend *self) {
  self->start();
}

//  void QSensorBackend::stop()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSensorBackend4stopEv(QSensorBackend *self) {
  self->stop();
}

//  bool QSensorBackend::isFeatureSupported(QSensor::Feature feature) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QSensorBackend18isFeatureSupportedEN7QSensor7FeatureE(
    const QSensorBackend *self,
    QSensor::Feature feature) {
  return self->isFeatureSupported(feature);
}

//  void QSensorBackend::addDataRate(qreal min, qreal max)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSensorBackend11addDataRateEdd(
    QSensorBackend *self,
    qreal min,
    qreal max) {
  self->addDataRate(min, max);
}

//  void QSensorBackend::setDataRates(const QSensor *otherSensor)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSensorBackend12setDataRatesEPK7QSensor(
    QSensorBackend *self,
    const QSensor *otherSensor) {
  self->setDataRates(otherSensor);
}

//  void QSensorBackend::addOutputRange(qreal min, qreal max, qreal accuracy)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSensorBackend14addOutputRangeEddd(
    QSensorBackend *self,
    qreal min,
    qreal max,
    qreal accuracy) {
  self->addOutputRange(min, max, accuracy);
}

//  void QSensorBackend::setDescription(const QString &description)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSensorBackend14setDescriptionERK7QString(
    QSensorBackend *self,
    const QString *description) {
  self->setDescription(*description);
}

//  QSensorReading *QSensorBackend::reading() const
extern "C" Q_DECL_EXPORT
QSensorReading *ritual_ZNK14QSensorBackend7readingEv(
    const QSensorBackend *self) {
  return self->reading();
}

//  QSensor *QSensorBackend::sensor() const
extern "C" Q_DECL_EXPORT
QSensor *ritual_ZNK14QSensorBackend6sensorEv(const QSensorBackend *self) {
  return self->sensor();
}

//  void QSensorBackend::newReadingAvailable()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSensorBackend19newReadingAvailableEv(QSensorBackend *self) {
  self->newReadingAvailable();
}

//  void QSensorBackend::sensorStopped()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSensorBackend13sensorStoppedEv(QSensorBackend *self) {
  self->sensorStopped();
}

//  void QSensorBackend::sensorBusy(bool busy)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSensorBackend10sensorBusyEb(
    QSensorBackend *self,
    bool busy) {
  self->sensorBusy(busy);
}

//  void QSensorBackend::sensorError(int error)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSensorBackend11sensorErrorEi(
    QSensorBackend *self,
    int error) {
  self->sensorError(error);
}

//  void QSensorBackend::setReadings(QSensorReading *device, QSensorReading
//      *filter, QSensorReading *cache)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSensorBackend11setReadingsEP14QSensorReadingS1_S1_(
    QSensorBackend *self,
    QSensorReading *device,
    QSensorReading *filter,
    QSensorReading *cache) {
  self->setReadings(device, filter, cache);
}

//  a Python function taken by a CuteQSensorBackend, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSensorBackend(
    QSensorBackend *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSensorBackend *>(self)->take(key, call);
}

//  bool QSensorBackend::isFeatureSupported(QSensor::Feature feature) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK14QSensorBackend18isFeatureSupportedEN7QSensor7FeatureE(
    const QSensorBackend *self,
    QSensor::Feature feature) {
  return self->QSensorBackend::isFeatureSupported(feature);
}
