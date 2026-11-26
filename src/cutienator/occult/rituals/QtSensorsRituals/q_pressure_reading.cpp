//  Written by dev_tooling.RitualGenerator from the records of
//  QtSensors/qpressuresensor.h, Qt 6.12.0. Changes made here are lost.
#include <QtSensors/qpressuresensor.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QPressureReading that Python can take functions over in. Every QPressureReading
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQPressureReadingCall0)(const void *, QSensorReading *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPressureReadingCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPressureReadingCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPressureReadingCall3)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPressureReadingCall4)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPressureReadingCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPressureReadingCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPressureReadingCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQPressureReading : public QPressureReading {
public:
  using QPressureReading::QPressureReading;
  void *taken[8] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN14QSensorReading14copyValuesFromEPS_")) {
      taken[0] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QPressureReading::copyValuesFrom(QSensorReading *other)
  void copyValuesFrom(QSensorReading *other) override {
    if (taken[0]) {
      int handled = 0;
      CuteQPressureReadingCall0 call = reinterpret_cast<CuteQPressureReadingCall0>(taken[0]);
      call(this, other, &handled);
      if (handled) return;
    }
    QPressureReading::copyValuesFrom(other);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQPressureReadingCall1 call = reinterpret_cast<CuteQPressureReadingCall1>(taken[1]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQPressureReadingCall2 call = reinterpret_cast<CuteQPressureReadingCall2>(taken[2]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQPressureReadingCall3 call = reinterpret_cast<CuteQPressureReadingCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQPressureReadingCall4 call = reinterpret_cast<CuteQPressureReadingCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQPressureReadingCall5 call = reinterpret_cast<CuteQPressureReadingCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQPressureReadingCall6 call = reinterpret_cast<CuteQPressureReadingCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[7]) {
      int handled = 0;
      CuteQPressureReadingCall7 call = reinterpret_cast<CuteQPressureReadingCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QPressureReading::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QPressureReading10metaObjectEv(
    const QPressureReading *self) {
  return self->metaObject();
}

//  void *QPressureReading::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN16QPressureReading11qt_metacastEPKc(
    QPressureReading *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QPressureReading::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN16QPressureReading11qt_metacallEN11QMetaObject4CallEiPPv(
    QPressureReading *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QPressureReading::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QPressureReading2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QPressureReading::tr(s, c, n));
}

//  QPressureReading::QPressureReading(QObject *parent)
extern "C" Q_DECL_EXPORT
QPressureReading *ritual_ZN16QPressureReadingC1EP7QObject(QObject *parent) {
  return new CuteQPressureReading(parent);
}

//  QPressureReading::~QPressureReading()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QPressureReadingD1Ev(QPressureReading *self) {
  delete self;
}

//  void QPressureReading::copyValuesFrom(QSensorReading *other)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QPressureReading14copyValuesFromEP14QSensorReading(
    QPressureReading *self,
    QSensorReading *other) {
  self->copyValuesFrom(other);
}

//  qreal QPressureReading::pressure() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK16QPressureReading8pressureEv(const QPressureReading *self) {
  return self->pressure();
}

//  void QPressureReading::setPressure(qreal pressure)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QPressureReading11setPressureEd(
    QPressureReading *self,
    qreal pressure) {
  self->setPressure(pressure);
}

//  qreal QPressureReading::temperature() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK16QPressureReading11temperatureEv(
    const QPressureReading *self) {
  return self->temperature();
}

//  void QPressureReading::setTemperature(qreal temperature)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QPressureReading14setTemperatureEd(
    QPressureReading *self,
    qreal temperature) {
  self->setTemperature(temperature);
}

//  a Python function taken by a CuteQPressureReading, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPressureReading(
    QPressureReading *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPressureReading *>(self)->take(key, call);
}

//  void QPressureReading::copyValuesFrom(QSensorReading *other)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QPressureReading14copyValuesFromEP14QSensorReading(
    QPressureReading *self,
    QSensorReading *other) {
  self->QPressureReading::copyValuesFrom(other);
}
