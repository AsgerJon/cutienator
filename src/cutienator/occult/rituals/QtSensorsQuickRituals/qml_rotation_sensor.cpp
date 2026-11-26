//  Written by dev_tooling.RitualGenerator from the records of
//  QtSensorsQuick/6.12.0/QtSensorsQuick/private/qmlrotationsensor_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtSensorsQuick/6.12.0/QtSensorsQuick/private/qsensorsquickglobal_p.h>
#include <QtSensorsQuick/QtSensorsQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSensorsQuick/6.12.0/QtSensorsQuick/private/qmlrotationsensor_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QmlRotationSensor that Python can take functions over in. Every QmlRotationSensor
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQmlRotationSensorCall0)(const void *, int *);
typedef void * (*CuteQmlRotationSensorCall1)(const void *, int *);
typedef void (*CuteQmlRotationSensorCall2)(const void *, int *);
typedef void (*CuteQmlRotationSensorCall3)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQmlRotationSensorCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQmlRotationSensorCall5)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQmlRotationSensorCall6)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQmlRotationSensorCall7)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQmlRotationSensorCall8)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQmlRotationSensorCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQmlRotationSensorCall10)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQmlRotationSensor : public QmlRotationSensor {
public:
  using QmlRotationSensor::QmlRotationSensor;
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

  //  QSensor *QmlRotationSensor::sensor() const
  QSensor *sensor() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQmlRotationSensorCall0 call = reinterpret_cast<CuteQmlRotationSensorCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSensor *>(given);
    }
    return QmlRotationSensor::sensor();
  }

  //  QmlSensorReading *QmlRotationSensor::createReading() const
  QmlSensorReading *createReading() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQmlRotationSensorCall1 call = reinterpret_cast<CuteQmlRotationSensorCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QmlSensorReading *>(given);
    }
    return QmlRotationSensor::createReading();
  }

  //  void QmlSensor::componentComplete()
  void componentComplete() override {
    if (taken[2]) {
      int handled = 0;
      CuteQmlRotationSensorCall2 call = reinterpret_cast<CuteQmlRotationSensorCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QmlSensor::componentComplete();
  }

  //  void QmlSensor::classBegin()
  void classBegin() override {
    if (taken[3]) {
      int handled = 0;
      CuteQmlRotationSensorCall3 call = reinterpret_cast<CuteQmlRotationSensorCall3>(taken[3]);
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
      CuteQmlRotationSensorCall4 call = reinterpret_cast<CuteQmlRotationSensorCall4>(taken[4]);
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
      CuteQmlRotationSensorCall5 call = reinterpret_cast<CuteQmlRotationSensorCall5>(taken[5]);
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
      CuteQmlRotationSensorCall6 call = reinterpret_cast<CuteQmlRotationSensorCall6>(taken[6]);
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
      CuteQmlRotationSensorCall7 call = reinterpret_cast<CuteQmlRotationSensorCall7>(taken[7]);
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
      CuteQmlRotationSensorCall8 call = reinterpret_cast<CuteQmlRotationSensorCall8>(taken[8]);
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
      CuteQmlRotationSensorCall9 call = reinterpret_cast<CuteQmlRotationSensorCall9>(taken[9]);
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
      CuteQmlRotationSensorCall10 call = reinterpret_cast<CuteQmlRotationSensorCall10>(taken[10]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QmlRotationSensor::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QmlRotationSensor10metaObjectEv(
    const QmlRotationSensor *self) {
  return self->metaObject();
}

//  void *QmlRotationSensor::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN17QmlRotationSensor11qt_metacastEPKc(
    QmlRotationSensor *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QmlRotationSensor::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN17QmlRotationSensor11qt_metacallEN11QMetaObject4CallEiPPv(
    QmlRotationSensor *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QmlRotationSensor::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QmlRotationSensor2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QmlRotationSensor::tr(s, c, n));
}

//  QmlRotationSensor::QmlRotationSensor(QObject *parent)
extern "C" Q_DECL_EXPORT
QmlRotationSensor *ritual_ZN17QmlRotationSensorC1EP7QObject(
    QObject *parent) {
  return new CuteQmlRotationSensor(parent);
}

//  QmlRotationSensor::~QmlRotationSensor()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QmlRotationSensorD1Ev(QmlRotationSensor *self) {
  delete self;
}

//  bool QmlRotationSensor::hasZ() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QmlRotationSensor4hasZEv(const QmlRotationSensor *self) {
  return self->hasZ();
}

//  QSensor *QmlRotationSensor::sensor() const
extern "C" Q_DECL_EXPORT
QSensor *ritual_ZNK17QmlRotationSensor6sensorEv(
    const QmlRotationSensor *self) {
  return self->sensor();
}

//  void QmlRotationSensor::hasZChanged(bool hasZ)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QmlRotationSensor11hasZChangedEb(
    QmlRotationSensor *self,
    bool hasZ) {
  self->hasZChanged(hasZ);
}

//  QmlSensorReading *QmlRotationSensor::createReading() const
extern "C" Q_DECL_EXPORT
QmlSensorReading *ritual_ZNK17QmlRotationSensor13createReadingEv(
    const QmlRotationSensor *self) {
  return self->createReading();
}

//  a Python function taken by a CuteQmlRotationSensor, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QmlRotationSensor(
    QmlRotationSensor *self,
    const char *key,
    void *call) {
  return static_cast<CuteQmlRotationSensor *>(self)->take(key, call);
}

//  QSensor *QmlRotationSensor::sensor() const
extern "C" Q_DECL_EXPORT
QSensor *ritual_own_ZNK17QmlRotationSensor6sensorEv(
    const QmlRotationSensor *self) {
  return self->QmlRotationSensor::sensor();
}

//  QmlSensorReading *QmlRotationSensor::createReading() const
extern "C" Q_DECL_EXPORT
QmlSensorReading *ritual_own_ZNK17QmlRotationSensor13createReadingEv(
    const QmlRotationSensor *self) {
  return self->QmlRotationSensor::createReading();
}
