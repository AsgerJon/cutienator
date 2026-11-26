//  Written by dev_tooling.RitualGenerator from the records of
//  QtSensorsQuick/6.12.0/QtSensorsQuick/private/qmlaccelerometer_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtSensorsQuick/6.12.0/QtSensorsQuick/private/qsensorsquickglobal_p.h>
#include <QtSensorsQuick/QtSensorsQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSensorsQuick/6.12.0/QtSensorsQuick/private/qmlaccelerometer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QmlAccelerometer that Python can take functions over in. Every QmlAccelerometer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQmlAccelerometerCall0)(const void *, int *);
typedef void * (*CuteQmlAccelerometerCall1)(const void *, int *);
typedef void (*CuteQmlAccelerometerCall2)(const void *, int *);
typedef void (*CuteQmlAccelerometerCall3)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQmlAccelerometerCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQmlAccelerometerCall5)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQmlAccelerometerCall6)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQmlAccelerometerCall7)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQmlAccelerometerCall8)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQmlAccelerometerCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQmlAccelerometerCall10)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQmlAccelerometer : public QmlAccelerometer {
public:
  using QmlAccelerometer::QmlAccelerometer;
  void *taken[11] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK9QmlSensor6sensorEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QmlSensor13createReadingEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[3] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  QSensor *QmlAccelerometer::sensor() const
  QSensor *sensor() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQmlAccelerometerCall0 call = reinterpret_cast<CuteQmlAccelerometerCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSensor *>(given);
    }
    return QmlAccelerometer::sensor();
  }

  //  QmlSensorReading *QmlAccelerometer::createReading() const
  QmlSensorReading *createReading() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQmlAccelerometerCall1 call = reinterpret_cast<CuteQmlAccelerometerCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QmlSensorReading *>(given);
    }
    return QmlAccelerometer::createReading();
  }

  //  void QmlSensor::componentComplete()
  void componentComplete() override {
    if (taken[2]) {
      int handled = 0;
      CuteQmlAccelerometerCall2 call = reinterpret_cast<CuteQmlAccelerometerCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QmlSensor::componentComplete();
  }

  //  void QmlSensor::classBegin()
  void classBegin() override {
    if (taken[3]) {
      int handled = 0;
      CuteQmlAccelerometerCall3 call = reinterpret_cast<CuteQmlAccelerometerCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QmlSensor::classBegin();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQmlAccelerometerCall4 call = reinterpret_cast<CuteQmlAccelerometerCall4>(taken[4]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQmlAccelerometerCall5 call = reinterpret_cast<CuteQmlAccelerometerCall5>(taken[5]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQmlAccelerometerCall6 call = reinterpret_cast<CuteQmlAccelerometerCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQmlAccelerometerCall7 call = reinterpret_cast<CuteQmlAccelerometerCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQmlAccelerometerCall8 call = reinterpret_cast<CuteQmlAccelerometerCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[9]) {
      int handled = 0;
      CuteQmlAccelerometerCall9 call = reinterpret_cast<CuteQmlAccelerometerCall9>(taken[9]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[10]) {
      int handled = 0;
      CuteQmlAccelerometerCall10 call = reinterpret_cast<CuteQmlAccelerometerCall10>(taken[10]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QmlAccelerometer::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QmlAccelerometer10metaObjectEv(
    const QmlAccelerometer *self) {
  return self->metaObject();
}

//  void *QmlAccelerometer::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN16QmlAccelerometer11qt_metacastEPKc(
    QmlAccelerometer *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QmlAccelerometer::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN16QmlAccelerometer11qt_metacallEN11QMetaObject4CallEiPPv(
    QmlAccelerometer *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QmlAccelerometer::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QmlAccelerometer2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QmlAccelerometer::tr(s, c, n));
}

//  QmlAccelerometer::QmlAccelerometer(QObject *parent)
extern "C" Q_DECL_EXPORT
QmlAccelerometer *ritual_ZN16QmlAccelerometerC1EP7QObject(QObject *parent) {
  return new CuteQmlAccelerometer(parent);
}

//  QmlAccelerometer::~QmlAccelerometer()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QmlAccelerometerD1Ev(QmlAccelerometer *self) {
  delete self;
}

//  AccelerationMode QmlAccelerometer::accelerationMode() const
extern "C" Q_DECL_EXPORT
QmlAccelerometer::AccelerationMode ritual_ZNK16QmlAccelerometer16accelerationModeEv(
    const QmlAccelerometer *self) {
  return self->accelerationMode();
}

//  void QmlAccelerometer::setAccelerationMode(AccelerationMode
//      accelerationMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QmlAccelerometer19setAccelerationModeENS_16AccelerationModeE(
    QmlAccelerometer *self,
    QmlAccelerometer::AccelerationMode accelerationMode) {
  self->setAccelerationMode(accelerationMode);
}

//  QSensor *QmlAccelerometer::sensor() const
extern "C" Q_DECL_EXPORT
QSensor *ritual_ZNK16QmlAccelerometer6sensorEv(
    const QmlAccelerometer *self) {
  return self->sensor();
}

//  void QmlAccelerometer::accelerationModeChanged(AccelerationMode
//      accelerationMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QmlAccelerometer23accelerationModeChangedENS_16AccelerationModeE(
    QmlAccelerometer *self,
    QmlAccelerometer::AccelerationMode accelerationMode) {
  self->accelerationModeChanged(accelerationMode);
}

//  QmlSensorReading *QmlAccelerometer::createReading() const
extern "C" Q_DECL_EXPORT
QmlSensorReading *ritual_ZNK16QmlAccelerometer13createReadingEv(
    const QmlAccelerometer *self) {
  return self->createReading();
}

//  a Python function taken by a CuteQmlAccelerometer, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QmlAccelerometer(
    QmlAccelerometer *self,
    const char *key,
    void *call) {
  return static_cast<CuteQmlAccelerometer *>(self)->take(key, call);
}

//  QSensor *QmlAccelerometer::sensor() const
extern "C" Q_DECL_EXPORT
QSensor *ritual_own_ZNK16QmlAccelerometer6sensorEv(
    const QmlAccelerometer *self) {
  return self->QmlAccelerometer::sensor();
}

//  QmlSensorReading *QmlAccelerometer::createReading() const
extern "C" Q_DECL_EXPORT
QmlSensorReading *ritual_own_ZNK16QmlAccelerometer13createReadingEv(
    const QmlAccelerometer *self) {
  return self->QmlAccelerometer::createReading();
}
