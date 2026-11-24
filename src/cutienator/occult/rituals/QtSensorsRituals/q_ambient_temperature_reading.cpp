//  Written by dev_tooling.RitualGenerator from the records of
//  QtSensors/qambienttemperaturesensor.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtSensors/qambienttemperaturesensor.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QAmbientTemperatureReading that Python can take functions over in. Every QAmbientTemperatureReading
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQAmbientTemperatureReadingCall0)(const void *, QSensorReading *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAmbientTemperatureReadingCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAmbientTemperatureReadingCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAmbientTemperatureReadingCall3)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAmbientTemperatureReadingCall4)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAmbientTemperatureReadingCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAmbientTemperatureReadingCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAmbientTemperatureReadingCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQAmbientTemperatureReading : public QAmbientTemperatureReading {
public:
  using QAmbientTemperatureReading::QAmbientTemperatureReading;
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

  //  void QAmbientTemperatureReading::copyValuesFrom(QSensorReading
  //      *other)
  void copyValuesFrom(QSensorReading *other) override {
    if (taken[0]) {
      int handled = 0;
      CuteQAmbientTemperatureReadingCall0 call = reinterpret_cast<CuteQAmbientTemperatureReadingCall0>(taken[0]);
      call(this, other, &handled);
      if (handled) return;
    }
    QAmbientTemperatureReading::copyValuesFrom(other);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQAmbientTemperatureReadingCall1 call = reinterpret_cast<CuteQAmbientTemperatureReadingCall1>(taken[1]);
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
      CuteQAmbientTemperatureReadingCall2 call = reinterpret_cast<CuteQAmbientTemperatureReadingCall2>(taken[2]);
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
      CuteQAmbientTemperatureReadingCall3 call = reinterpret_cast<CuteQAmbientTemperatureReadingCall3>(taken[3]);
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
      CuteQAmbientTemperatureReadingCall4 call = reinterpret_cast<CuteQAmbientTemperatureReadingCall4>(taken[4]);
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
      CuteQAmbientTemperatureReadingCall5 call = reinterpret_cast<CuteQAmbientTemperatureReadingCall5>(taken[5]);
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
      CuteQAmbientTemperatureReadingCall6 call = reinterpret_cast<CuteQAmbientTemperatureReadingCall6>(taken[6]);
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
      CuteQAmbientTemperatureReadingCall7 call = reinterpret_cast<CuteQAmbientTemperatureReadingCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QAmbientTemperatureReading::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK26QAmbientTemperatureReading10metaObjectEv(
    const QAmbientTemperatureReading *self) {
  return self->metaObject();
}

//  QString QAmbientTemperatureReading::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN26QAmbientTemperatureReading2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QAmbientTemperatureReading::tr(s, c, n));
}

//  QAmbientTemperatureReading::QAmbientTemperatureReading(QObject *parent)
extern "C" Q_DECL_EXPORT
QAmbientTemperatureReading *ritual_ZN26QAmbientTemperatureReadingC1EP7QObject(
    QObject *parent) {
  return new CuteQAmbientTemperatureReading(parent);
}

//  QAmbientTemperatureReading::~QAmbientTemperatureReading()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QAmbientTemperatureReadingD1Ev(
    QAmbientTemperatureReading *self) {
  delete self;
}

//  void QAmbientTemperatureReading::copyValuesFrom(QSensorReading *other)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QAmbientTemperatureReading14copyValuesFromEP14QSensorReading(
    QAmbientTemperatureReading *self,
    QSensorReading *other) {
  self->copyValuesFrom(other);
}

//  qreal QAmbientTemperatureReading::temperature() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK26QAmbientTemperatureReading11temperatureEv(
    const QAmbientTemperatureReading *self) {
  return self->temperature();
}

//  void QAmbientTemperatureReading::setTemperature(qreal temperature)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QAmbientTemperatureReading14setTemperatureEd(
    QAmbientTemperatureReading *self,
    qreal temperature) {
  self->setTemperature(temperature);
}

//  a Python function taken by a CuteQAmbientTemperatureReading, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAmbientTemperatureReading(
    QAmbientTemperatureReading *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAmbientTemperatureReading *>(self)->take(key, call);
}

//  void QAmbientTemperatureReading::copyValuesFrom(QSensorReading *other)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN26QAmbientTemperatureReading14copyValuesFromEP14QSensorReading(
    QAmbientTemperatureReading *self,
    QSensorReading *other) {
  self->QAmbientTemperatureReading::copyValuesFrom(other);
}
