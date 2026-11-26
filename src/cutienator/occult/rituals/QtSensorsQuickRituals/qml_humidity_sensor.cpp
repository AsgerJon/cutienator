//  Written by dev_tooling.RitualGenerator from the records of
//  QtSensorsQuick/6.12.0/QtSensorsQuick/private/qmlhumiditysensor_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtSensorsQuick/6.12.0/QtSensorsQuick/private/qsensorsquickglobal_p.h>
#include <QtSensorsQuick/QtSensorsQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSensorsQuick/6.12.0/QtSensorsQuick/private/qmlhumiditysensor_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QmlHumiditySensor that Python can take functions over in. Every QmlHumiditySensor
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQmlHumiditySensorCall0)(const void *, int *);
typedef void * (*CuteQmlHumiditySensorCall1)(const void *, int *);
typedef void (*CuteQmlHumiditySensorCall2)(const void *, int *);
typedef void (*CuteQmlHumiditySensorCall3)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQmlHumiditySensorCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQmlHumiditySensorCall5)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQmlHumiditySensorCall6)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQmlHumiditySensorCall7)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQmlHumiditySensorCall8)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQmlHumiditySensorCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQmlHumiditySensorCall10)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQmlHumiditySensor : public QmlHumiditySensor {
public:
  using QmlHumiditySensor::QmlHumiditySensor;
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

  //  QSensor *QmlHumiditySensor::sensor() const
  QSensor *sensor() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQmlHumiditySensorCall0 call = reinterpret_cast<CuteQmlHumiditySensorCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSensor *>(given);
    }
    return QmlHumiditySensor::sensor();
  }

  //  QmlSensorReading *QmlHumiditySensor::createReading() const
  QmlSensorReading *createReading() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQmlHumiditySensorCall1 call = reinterpret_cast<CuteQmlHumiditySensorCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QmlSensorReading *>(given);
    }
    return QmlHumiditySensor::createReading();
  }

  //  void QmlSensor::componentComplete()
  void componentComplete() override {
    if (taken[2]) {
      int handled = 0;
      CuteQmlHumiditySensorCall2 call = reinterpret_cast<CuteQmlHumiditySensorCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QmlSensor::componentComplete();
  }

  //  void QmlSensor::classBegin()
  void classBegin() override {
    if (taken[3]) {
      int handled = 0;
      CuteQmlHumiditySensorCall3 call = reinterpret_cast<CuteQmlHumiditySensorCall3>(taken[3]);
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
      CuteQmlHumiditySensorCall4 call = reinterpret_cast<CuteQmlHumiditySensorCall4>(taken[4]);
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
      CuteQmlHumiditySensorCall5 call = reinterpret_cast<CuteQmlHumiditySensorCall5>(taken[5]);
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
      CuteQmlHumiditySensorCall6 call = reinterpret_cast<CuteQmlHumiditySensorCall6>(taken[6]);
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
      CuteQmlHumiditySensorCall7 call = reinterpret_cast<CuteQmlHumiditySensorCall7>(taken[7]);
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
      CuteQmlHumiditySensorCall8 call = reinterpret_cast<CuteQmlHumiditySensorCall8>(taken[8]);
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
      CuteQmlHumiditySensorCall9 call = reinterpret_cast<CuteQmlHumiditySensorCall9>(taken[9]);
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
      CuteQmlHumiditySensorCall10 call = reinterpret_cast<CuteQmlHumiditySensorCall10>(taken[10]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QmlHumiditySensor::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QmlHumiditySensor10metaObjectEv(
    const QmlHumiditySensor *self) {
  return self->metaObject();
}

//  void *QmlHumiditySensor::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN17QmlHumiditySensor11qt_metacastEPKc(
    QmlHumiditySensor *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QmlHumiditySensor::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN17QmlHumiditySensor11qt_metacallEN11QMetaObject4CallEiPPv(
    QmlHumiditySensor *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QmlHumiditySensor::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QmlHumiditySensor2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QmlHumiditySensor::tr(s, c, n));
}

//  QmlHumiditySensor::QmlHumiditySensor(QObject *parent)
extern "C" Q_DECL_EXPORT
QmlHumiditySensor *ritual_ZN17QmlHumiditySensorC1EP7QObject(
    QObject *parent) {
  return new CuteQmlHumiditySensor(parent);
}

//  QmlHumiditySensor::~QmlHumiditySensor()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QmlHumiditySensorD1Ev(QmlHumiditySensor *self) {
  delete self;
}

//  QSensor *QmlHumiditySensor::sensor() const
extern "C" Q_DECL_EXPORT
QSensor *ritual_ZNK17QmlHumiditySensor6sensorEv(
    const QmlHumiditySensor *self) {
  return self->sensor();
}

//  QmlSensorReading *QmlHumiditySensor::createReading() const
extern "C" Q_DECL_EXPORT
QmlSensorReading *ritual_ZNK17QmlHumiditySensor13createReadingEv(
    const QmlHumiditySensor *self) {
  return self->createReading();
}

//  a Python function taken by a CuteQmlHumiditySensor, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QmlHumiditySensor(
    QmlHumiditySensor *self,
    const char *key,
    void *call) {
  return static_cast<CuteQmlHumiditySensor *>(self)->take(key, call);
}

//  QSensor *QmlHumiditySensor::sensor() const
extern "C" Q_DECL_EXPORT
QSensor *ritual_own_ZNK17QmlHumiditySensor6sensorEv(
    const QmlHumiditySensor *self) {
  return self->QmlHumiditySensor::sensor();
}

//  QmlSensorReading *QmlHumiditySensor::createReading() const
extern "C" Q_DECL_EXPORT
QmlSensorReading *ritual_own_ZNK17QmlHumiditySensor13createReadingEv(
    const QmlHumiditySensor *self) {
  return self->QmlHumiditySensor::createReading();
}
