//  Written by dev_tooling.RitualGenerator from the records of
//  QtSensorsQuick/6.12.0/QtSensorsQuick/private/qmlmagnetometer_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtSensorsQuick/6.12.0/QtSensorsQuick/private/qsensorsquickglobal_p.h>
#include <QtSensorsQuick/QtSensorsQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSensorsQuick/6.12.0/QtSensorsQuick/private/qmlmagnetometer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QmlMagnetometer that Python can take functions over in. Every QmlMagnetometer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQmlMagnetometerCall0)(const void *, int *);
typedef void * (*CuteQmlMagnetometerCall1)(const void *, int *);
typedef void (*CuteQmlMagnetometerCall2)(const void *, int *);
typedef void (*CuteQmlMagnetometerCall3)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQmlMagnetometerCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQmlMagnetometerCall5)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQmlMagnetometerCall6)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQmlMagnetometerCall7)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQmlMagnetometerCall8)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQmlMagnetometerCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQmlMagnetometerCall10)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQmlMagnetometer : public QmlMagnetometer {
public:
  using QmlMagnetometer::QmlMagnetometer;
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

  //  QSensor *QmlMagnetometer::sensor() const
  QSensor *sensor() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQmlMagnetometerCall0 call = reinterpret_cast<CuteQmlMagnetometerCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSensor *>(given);
    }
    return QmlMagnetometer::sensor();
  }

  //  QmlSensorReading *QmlMagnetometer::createReading() const
  QmlSensorReading *createReading() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQmlMagnetometerCall1 call = reinterpret_cast<CuteQmlMagnetometerCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QmlSensorReading *>(given);
    }
    return QmlMagnetometer::createReading();
  }

  //  void QmlSensor::componentComplete()
  void componentComplete() override {
    if (taken[2]) {
      int handled = 0;
      CuteQmlMagnetometerCall2 call = reinterpret_cast<CuteQmlMagnetometerCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QmlSensor::componentComplete();
  }

  //  void QmlSensor::classBegin()
  void classBegin() override {
    if (taken[3]) {
      int handled = 0;
      CuteQmlMagnetometerCall3 call = reinterpret_cast<CuteQmlMagnetometerCall3>(taken[3]);
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
      CuteQmlMagnetometerCall4 call = reinterpret_cast<CuteQmlMagnetometerCall4>(taken[4]);
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
      CuteQmlMagnetometerCall5 call = reinterpret_cast<CuteQmlMagnetometerCall5>(taken[5]);
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
      CuteQmlMagnetometerCall6 call = reinterpret_cast<CuteQmlMagnetometerCall6>(taken[6]);
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
      CuteQmlMagnetometerCall7 call = reinterpret_cast<CuteQmlMagnetometerCall7>(taken[7]);
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
      CuteQmlMagnetometerCall8 call = reinterpret_cast<CuteQmlMagnetometerCall8>(taken[8]);
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
      CuteQmlMagnetometerCall9 call = reinterpret_cast<CuteQmlMagnetometerCall9>(taken[9]);
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
      CuteQmlMagnetometerCall10 call = reinterpret_cast<CuteQmlMagnetometerCall10>(taken[10]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QmlMagnetometer::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QmlMagnetometer10metaObjectEv(
    const QmlMagnetometer *self) {
  return self->metaObject();
}

//  void *QmlMagnetometer::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN15QmlMagnetometer11qt_metacastEPKc(
    QmlMagnetometer *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QmlMagnetometer::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN15QmlMagnetometer11qt_metacallEN11QMetaObject4CallEiPPv(
    QmlMagnetometer *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QmlMagnetometer::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QmlMagnetometer2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QmlMagnetometer::tr(s, c, n));
}

//  QmlMagnetometer::QmlMagnetometer(QObject *parent)
extern "C" Q_DECL_EXPORT
QmlMagnetometer *ritual_ZN15QmlMagnetometerC1EP7QObject(QObject *parent) {
  return new CuteQmlMagnetometer(parent);
}

//  QmlMagnetometer::~QmlMagnetometer()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QmlMagnetometerD1Ev(QmlMagnetometer *self) {
  delete self;
}

//  bool QmlMagnetometer::returnGeoValues() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QmlMagnetometer15returnGeoValuesEv(
    const QmlMagnetometer *self) {
  return self->returnGeoValues();
}

//  void QmlMagnetometer::setReturnGeoValues(bool geo)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QmlMagnetometer18setReturnGeoValuesEb(
    QmlMagnetometer *self,
    bool geo) {
  self->setReturnGeoValues(geo);
}

//  QSensor *QmlMagnetometer::sensor() const
extern "C" Q_DECL_EXPORT
QSensor *ritual_ZNK15QmlMagnetometer6sensorEv(const QmlMagnetometer *self) {
  return self->sensor();
}

//  void QmlMagnetometer::returnGeoValuesChanged(bool returnGeoValues)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QmlMagnetometer22returnGeoValuesChangedEb(
    QmlMagnetometer *self,
    bool returnGeoValues) {
  self->returnGeoValuesChanged(returnGeoValues);
}

//  QmlSensorReading *QmlMagnetometer::createReading() const
extern "C" Q_DECL_EXPORT
QmlSensorReading *ritual_ZNK15QmlMagnetometer13createReadingEv(
    const QmlMagnetometer *self) {
  return self->createReading();
}

//  a Python function taken by a CuteQmlMagnetometer, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QmlMagnetometer(
    QmlMagnetometer *self,
    const char *key,
    void *call) {
  return static_cast<CuteQmlMagnetometer *>(self)->take(key, call);
}

//  QSensor *QmlMagnetometer::sensor() const
extern "C" Q_DECL_EXPORT
QSensor *ritual_own_ZNK15QmlMagnetometer6sensorEv(
    const QmlMagnetometer *self) {
  return self->QmlMagnetometer::sensor();
}

//  QmlSensorReading *QmlMagnetometer::createReading() const
extern "C" Q_DECL_EXPORT
QmlSensorReading *ritual_own_ZNK15QmlMagnetometer13createReadingEv(
    const QmlMagnetometer *self) {
  return self->QmlMagnetometer::createReading();
}
