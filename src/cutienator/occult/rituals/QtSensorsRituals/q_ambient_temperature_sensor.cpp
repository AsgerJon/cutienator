//  Written by dev_tooling.RitualGenerator from the records of
//  QtSensors/qambienttemperaturesensor.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtSensors/qambienttemperaturesensor.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QAmbientTemperatureSensor that Python can take functions over in. Every QAmbientTemperatureSensor
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAmbientTemperatureSensorCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAmbientTemperatureSensorCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAmbientTemperatureSensorCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAmbientTemperatureSensorCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAmbientTemperatureSensorCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAmbientTemperatureSensorCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAmbientTemperatureSensorCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQAmbientTemperatureSensor : public QAmbientTemperatureSensor {
public:
  using QAmbientTemperatureSensor::QAmbientTemperatureSensor;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQAmbientTemperatureSensorCall0 call = reinterpret_cast<CuteQAmbientTemperatureSensorCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQAmbientTemperatureSensorCall1 call = reinterpret_cast<CuteQAmbientTemperatureSensorCall1>(taken[1]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQAmbientTemperatureSensorCall2 call = reinterpret_cast<CuteQAmbientTemperatureSensorCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQAmbientTemperatureSensorCall3 call = reinterpret_cast<CuteQAmbientTemperatureSensorCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQAmbientTemperatureSensorCall4 call = reinterpret_cast<CuteQAmbientTemperatureSensorCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteQAmbientTemperatureSensorCall5 call = reinterpret_cast<CuteQAmbientTemperatureSensorCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQAmbientTemperatureSensorCall6 call = reinterpret_cast<CuteQAmbientTemperatureSensorCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QAmbientTemperatureSensor::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK25QAmbientTemperatureSensor10metaObjectEv(
    const QAmbientTemperatureSensor *self) {
  return self->metaObject();
}

//  QString QAmbientTemperatureSensor::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN25QAmbientTemperatureSensor2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QAmbientTemperatureSensor::tr(s, c, n));
}

//  QAmbientTemperatureSensor::QAmbientTemperatureSensor(QObject *parent)
extern "C" Q_DECL_EXPORT
QAmbientTemperatureSensor *ritual_ZN25QAmbientTemperatureSensorC1EP7QObject(
    QObject *parent) {
  return new CuteQAmbientTemperatureSensor(parent);
}

//  QAmbientTemperatureSensor::~QAmbientTemperatureSensor()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QAmbientTemperatureSensorD1Ev(
    QAmbientTemperatureSensor *self) {
  delete self;
}

//  QAmbientTemperatureReading *QAmbientTemperatureSensor::reading() const
extern "C" Q_DECL_EXPORT
QAmbientTemperatureReading *ritual_ZNK25QAmbientTemperatureSensor7readingEv(
    const QAmbientTemperatureSensor *self) {
  return self->reading();
}

//  a Python function taken by a CuteQAmbientTemperatureSensor, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAmbientTemperatureSensor(
    QAmbientTemperatureSensor *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAmbientTemperatureSensor *>(self)->take(key, call);
}
