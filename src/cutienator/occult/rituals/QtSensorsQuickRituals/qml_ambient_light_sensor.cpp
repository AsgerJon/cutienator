//  Written by dev_tooling.RitualGenerator from the records of
//  QtSensorsQuick/6.12.0/QtSensorsQuick/private/qmlambientlightsensor_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtSensorsQuick/6.12.0/QtSensorsQuick/private/qsensorsquickglobal_p.h>
#include <QtSensorsQuick/QtSensorsQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSensorsQuick/6.12.0/QtSensorsQuick/private/qmlambientlightsensor_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QmlAmbientLightSensor that Python can take functions over in. Every QmlAmbientLightSensor
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQmlAmbientLightSensorCall0)(const void *, int *);
typedef void * (*CuteQmlAmbientLightSensorCall1)(const void *, int *);
typedef void (*CuteQmlAmbientLightSensorCall2)(const void *, int *);
typedef void (*CuteQmlAmbientLightSensorCall3)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQmlAmbientLightSensorCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQmlAmbientLightSensorCall5)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQmlAmbientLightSensorCall6)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQmlAmbientLightSensorCall7)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQmlAmbientLightSensorCall8)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQmlAmbientLightSensorCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQmlAmbientLightSensorCall10)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQmlAmbientLightSensor : public QmlAmbientLightSensor {
public:
  using QmlAmbientLightSensor::QmlAmbientLightSensor;
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

  //  QSensor *QmlAmbientLightSensor::sensor() const
  QSensor *sensor() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQmlAmbientLightSensorCall0 call = reinterpret_cast<CuteQmlAmbientLightSensorCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSensor *>(given);
    }
    return QmlAmbientLightSensor::sensor();
  }

  //  QmlSensorReading *QmlAmbientLightSensor::createReading() const
  QmlSensorReading *createReading() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQmlAmbientLightSensorCall1 call = reinterpret_cast<CuteQmlAmbientLightSensorCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QmlSensorReading *>(given);
    }
    return QmlAmbientLightSensor::createReading();
  }

  //  void QmlSensor::componentComplete()
  void componentComplete() override {
    if (taken[2]) {
      int handled = 0;
      CuteQmlAmbientLightSensorCall2 call = reinterpret_cast<CuteQmlAmbientLightSensorCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QmlSensor::componentComplete();
  }

  //  void QmlSensor::classBegin()
  void classBegin() override {
    if (taken[3]) {
      int handled = 0;
      CuteQmlAmbientLightSensorCall3 call = reinterpret_cast<CuteQmlAmbientLightSensorCall3>(taken[3]);
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
      CuteQmlAmbientLightSensorCall4 call = reinterpret_cast<CuteQmlAmbientLightSensorCall4>(taken[4]);
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
      CuteQmlAmbientLightSensorCall5 call = reinterpret_cast<CuteQmlAmbientLightSensorCall5>(taken[5]);
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
      CuteQmlAmbientLightSensorCall6 call = reinterpret_cast<CuteQmlAmbientLightSensorCall6>(taken[6]);
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
      CuteQmlAmbientLightSensorCall7 call = reinterpret_cast<CuteQmlAmbientLightSensorCall7>(taken[7]);
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
      CuteQmlAmbientLightSensorCall8 call = reinterpret_cast<CuteQmlAmbientLightSensorCall8>(taken[8]);
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
      CuteQmlAmbientLightSensorCall9 call = reinterpret_cast<CuteQmlAmbientLightSensorCall9>(taken[9]);
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
      CuteQmlAmbientLightSensorCall10 call = reinterpret_cast<CuteQmlAmbientLightSensorCall10>(taken[10]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QmlAmbientLightSensor::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21QmlAmbientLightSensor10metaObjectEv(
    const QmlAmbientLightSensor *self) {
  return self->metaObject();
}

//  void *QmlAmbientLightSensor::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN21QmlAmbientLightSensor11qt_metacastEPKc(
    QmlAmbientLightSensor *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QmlAmbientLightSensor::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN21QmlAmbientLightSensor11qt_metacallEN11QMetaObject4CallEiPPv(
    QmlAmbientLightSensor *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QmlAmbientLightSensor::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN21QmlAmbientLightSensor2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QmlAmbientLightSensor::tr(s, c, n));
}

//  QmlAmbientLightSensor::QmlAmbientLightSensor(QObject *parent)
extern "C" Q_DECL_EXPORT
QmlAmbientLightSensor *ritual_ZN21QmlAmbientLightSensorC1EP7QObject(
    QObject *parent) {
  return new CuteQmlAmbientLightSensor(parent);
}

//  QmlAmbientLightSensor::~QmlAmbientLightSensor()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QmlAmbientLightSensorD1Ev(QmlAmbientLightSensor *self) {
  delete self;
}

//  QSensor *QmlAmbientLightSensor::sensor() const
extern "C" Q_DECL_EXPORT
QSensor *ritual_ZNK21QmlAmbientLightSensor6sensorEv(
    const QmlAmbientLightSensor *self) {
  return self->sensor();
}

//  QmlSensorReading *QmlAmbientLightSensor::createReading() const
extern "C" Q_DECL_EXPORT
QmlSensorReading *ritual_ZNK21QmlAmbientLightSensor13createReadingEv(
    const QmlAmbientLightSensor *self) {
  return self->createReading();
}

//  a Python function taken by a CuteQmlAmbientLightSensor, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QmlAmbientLightSensor(
    QmlAmbientLightSensor *self,
    const char *key,
    void *call) {
  return static_cast<CuteQmlAmbientLightSensor *>(self)->take(key, call);
}

//  QSensor *QmlAmbientLightSensor::sensor() const
extern "C" Q_DECL_EXPORT
QSensor *ritual_own_ZNK21QmlAmbientLightSensor6sensorEv(
    const QmlAmbientLightSensor *self) {
  return self->QmlAmbientLightSensor::sensor();
}

//  QmlSensorReading *QmlAmbientLightSensor::createReading() const
extern "C" Q_DECL_EXPORT
QmlSensorReading *ritual_own_ZNK21QmlAmbientLightSensor13createReadingEv(
    const QmlAmbientLightSensor *self) {
  return self->QmlAmbientLightSensor::createReading();
}
