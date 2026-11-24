//  Written by dev_tooling.RitualGenerator from the records of QtSensorsQuick
//  /6.12.0/QtSensorsQuick/private/qmlambienttemperaturesensor_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtSensorsQuick/6.12.0/QtSensorsQuick/private/qsensorsquickglobal_p.h>
#include <QtSensorsQuick/QtSensorsQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSensorsQuick/6.12.0/QtSensorsQuick/private/qmlambienttemperaturesensor_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QmlAmbientTemperatureReading that Python can take functions over in. Every QmlAmbientTemperatureReading
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQmlAmbientTemperatureReadingCall0)(const void *, int *);
typedef void (*CuteQmlAmbientTemperatureReadingCall1)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQmlAmbientTemperatureReadingCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQmlAmbientTemperatureReadingCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQmlAmbientTemperatureReadingCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQmlAmbientTemperatureReadingCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQmlAmbientTemperatureReadingCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQmlAmbientTemperatureReadingCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQmlAmbientTemperatureReadingCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQmlAmbientTemperatureReading : public QmlAmbientTemperatureReading {
public:
  using QmlAmbientTemperatureReading::QmlAmbientTemperatureReading;
  void *taken[9] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK16QmlSensorReading7readingEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QmlSensorReading13readingUpdateEv")) {
      taken[1] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  QSensorReading *QmlAmbientTemperatureReading::reading() const
  QSensorReading *reading() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQmlAmbientTemperatureReadingCall0 call = reinterpret_cast<CuteQmlAmbientTemperatureReadingCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSensorReading *>(given);
    }
    return QmlAmbientTemperatureReading::reading();
  }

  //  void QmlAmbientTemperatureReading::readingUpdate()
  void readingUpdate() override {
    if (taken[1]) {
      int handled = 0;
      CuteQmlAmbientTemperatureReadingCall1 call = reinterpret_cast<CuteQmlAmbientTemperatureReadingCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QmlAmbientTemperatureReading::readingUpdate();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQmlAmbientTemperatureReadingCall2 call = reinterpret_cast<CuteQmlAmbientTemperatureReadingCall2>(taken[2]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQmlAmbientTemperatureReadingCall3 call = reinterpret_cast<CuteQmlAmbientTemperatureReadingCall3>(taken[3]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQmlAmbientTemperatureReadingCall4 call = reinterpret_cast<CuteQmlAmbientTemperatureReadingCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQmlAmbientTemperatureReadingCall5 call = reinterpret_cast<CuteQmlAmbientTemperatureReadingCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQmlAmbientTemperatureReadingCall6 call = reinterpret_cast<CuteQmlAmbientTemperatureReadingCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[7]) {
      int handled = 0;
      CuteQmlAmbientTemperatureReadingCall7 call = reinterpret_cast<CuteQmlAmbientTemperatureReadingCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[8]) {
      int handled = 0;
      CuteQmlAmbientTemperatureReadingCall8 call = reinterpret_cast<CuteQmlAmbientTemperatureReadingCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QmlAmbientTemperatureReading::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK28QmlAmbientTemperatureReading10metaObjectEv(
    const QmlAmbientTemperatureReading *self) {
  return self->metaObject();
}

//  QString QmlAmbientTemperatureReading::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN28QmlAmbientTemperatureReading2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QmlAmbientTemperatureReading::tr(s, c, n));
}

//  void QmlAmbientTemperatureReading::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QmlAmbientTemperatureReading24qt_qmlMarker_uncreatableEv(
    QmlAmbientTemperatureReading *self) {
  self->qt_qmlMarker_uncreatable();
}

//  QmlAmbientTemperatureReading::QmlAmbientTemperatureReading(QAmbientTemper
//      atureSensor *sensor)
extern "C" Q_DECL_EXPORT
QmlAmbientTemperatureReading *ritual_ZN28QmlAmbientTemperatureReadingC1EP25QAmbientTemperatureSensor(
    QAmbientTemperatureSensor *sensor) {
  return new CuteQmlAmbientTemperatureReading(sensor);
}

//  QmlAmbientTemperatureReading::~QmlAmbientTemperatureReading()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QmlAmbientTemperatureReadingD1Ev(
    QmlAmbientTemperatureReading *self) {
  delete self;
}

//  qreal QmlAmbientTemperatureReading::temperature() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK28QmlAmbientTemperatureReading11temperatureEv(
    const QmlAmbientTemperatureReading *self) {
  return self->temperature();
}

//  QSensorReading *QmlAmbientTemperatureReading::reading() const
extern "C" Q_DECL_EXPORT
QSensorReading *ritual_ZNK28QmlAmbientTemperatureReading7readingEv(
    const QmlAmbientTemperatureReading *self) {
  return self->reading();
}

//  void QmlAmbientTemperatureReading::readingUpdate()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QmlAmbientTemperatureReading13readingUpdateEv(
    QmlAmbientTemperatureReading *self) {
  self->readingUpdate();
}

//  a Python function taken by a CuteQmlAmbientTemperatureReading, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QmlAmbientTemperatureReading(
    QmlAmbientTemperatureReading *self,
    const char *key,
    void *call) {
  return static_cast<CuteQmlAmbientTemperatureReading *>(self)->take(key, call);
}

//  QSensorReading *QmlAmbientTemperatureReading::reading() const
extern "C" Q_DECL_EXPORT
QSensorReading *ritual_own_ZNK28QmlAmbientTemperatureReading7readingEv(
    const QmlAmbientTemperatureReading *self) {
  return self->QmlAmbientTemperatureReading::reading();
}

//  void QmlAmbientTemperatureReading::readingUpdate()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN28QmlAmbientTemperatureReading13readingUpdateEv(
    QmlAmbientTemperatureReading *self) {
  self->QmlAmbientTemperatureReading::readingUpdate();
}
