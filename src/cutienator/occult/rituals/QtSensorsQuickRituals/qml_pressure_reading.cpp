//  Written by dev_tooling.RitualGenerator from the records of
//  QtSensorsQuick/6.12.0/QtSensorsQuick/private/qmlpressuresensor_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtSensorsQuick/6.12.0/QtSensorsQuick/private/qsensorsquickglobal_p.h>
#include <QtSensorsQuick/QtSensorsQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSensorsQuick/6.12.0/QtSensorsQuick/private/qmlpressuresensor_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#include <QtCore/QBindable>

//  A QmlPressureReading that Python can take functions over in. Every QmlPressureReading
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQmlPressureReadingCall0)(const void *, int *);
typedef void (*CuteQmlPressureReadingCall1)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQmlPressureReadingCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQmlPressureReadingCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQmlPressureReadingCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQmlPressureReadingCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQmlPressureReadingCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQmlPressureReadingCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQmlPressureReadingCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQmlPressureReading : public QmlPressureReading {
public:
  using QmlPressureReading::QmlPressureReading;
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

  //  QSensorReading *QmlPressureReading::reading() const
  QSensorReading *reading() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQmlPressureReadingCall0 call = reinterpret_cast<CuteQmlPressureReadingCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSensorReading *>(given);
    }
    return QmlPressureReading::reading();
  }

  //  void QmlPressureReading::readingUpdate()
  void readingUpdate() override {
    if (taken[1]) {
      int handled = 0;
      CuteQmlPressureReadingCall1 call = reinterpret_cast<CuteQmlPressureReadingCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QmlPressureReading::readingUpdate();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQmlPressureReadingCall2 call = reinterpret_cast<CuteQmlPressureReadingCall2>(taken[2]);
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
      CuteQmlPressureReadingCall3 call = reinterpret_cast<CuteQmlPressureReadingCall3>(taken[3]);
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
      CuteQmlPressureReadingCall4 call = reinterpret_cast<CuteQmlPressureReadingCall4>(taken[4]);
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
      CuteQmlPressureReadingCall5 call = reinterpret_cast<CuteQmlPressureReadingCall5>(taken[5]);
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
      CuteQmlPressureReadingCall6 call = reinterpret_cast<CuteQmlPressureReadingCall6>(taken[6]);
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
      CuteQmlPressureReadingCall7 call = reinterpret_cast<CuteQmlPressureReadingCall7>(taken[7]);
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
      CuteQmlPressureReadingCall8 call = reinterpret_cast<CuteQmlPressureReadingCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QmlPressureReading::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QmlPressureReading10metaObjectEv(
    const QmlPressureReading *self) {
  return self->metaObject();
}

//  void *QmlPressureReading::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN18QmlPressureReading11qt_metacastEPKc(
    QmlPressureReading *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QmlPressureReading::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN18QmlPressureReading11qt_metacallEN11QMetaObject4CallEiPPv(
    QmlPressureReading *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QmlPressureReading::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QmlPressureReading2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QmlPressureReading::tr(s, c, n));
}

//  void QmlPressureReading::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QmlPressureReading24qt_qmlMarker_uncreatableEv(
    QmlPressureReading *self) {
  self->qt_qmlMarker_uncreatable();
}

//  QmlPressureReading::QmlPressureReading(QPressureSensor *sensor)
extern "C" Q_DECL_EXPORT
QmlPressureReading *ritual_ZN18QmlPressureReadingC1EP15QPressureSensor(
    QPressureSensor *sensor) {
  return new CuteQmlPressureReading(sensor);
}

//  QmlPressureReading::~QmlPressureReading()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QmlPressureReadingD1Ev(QmlPressureReading *self) {
  delete self;
}

//  qreal QmlPressureReading::pressure() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK18QmlPressureReading8pressureEv(
    const QmlPressureReading *self) {
  return self->pressure();
}

//  QBindable<qreal> QmlPressureReading::bindablePressure() const
extern "C" Q_DECL_EXPORT
QBindable<qreal> *ritual_ZNK18QmlPressureReading16bindablePressureEv(
    const QmlPressureReading *self) {
  return new QBindable<qreal>(self->bindablePressure());
}

//  qreal QmlPressureReading::temperature() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK18QmlPressureReading11temperatureEv(
    const QmlPressureReading *self) {
  return self->temperature();
}

//  QBindable<qreal> QmlPressureReading::bindableTemperature() const
extern "C" Q_DECL_EXPORT
QBindable<qreal> *ritual_ZNK18QmlPressureReading19bindableTemperatureEv(
    const QmlPressureReading *self) {
  return new QBindable<qreal>(self->bindableTemperature());
}

//  void QmlPressureReading::pressureChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QmlPressureReading15pressureChangedEv(
    QmlPressureReading *self) {
  self->pressureChanged();
}

//  void QmlPressureReading::temperatureChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QmlPressureReading18temperatureChangedEv(
    QmlPressureReading *self) {
  self->temperatureChanged();
}

//  QSensorReading *QmlPressureReading::reading() const
extern "C" Q_DECL_EXPORT
QSensorReading *ritual_ZNK18QmlPressureReading7readingEv(
    const QmlPressureReading *self) {
  return self->reading();
}

//  void QmlPressureReading::readingUpdate()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QmlPressureReading13readingUpdateEv(
    QmlPressureReading *self) {
  self->readingUpdate();
}

//  size_t QmlPressureReading::_qt_property_m_pressure_offset()
extern "C" Q_DECL_EXPORT
size_t ritual_ZN18QmlPressureReading30_qt_property_m_pressure_offsetEv() {
  return QmlPressureReading::_qt_property_m_pressure_offset();
}

//  size_t QmlPressureReading::_qt_property_m_temperature_offset()
extern "C" Q_DECL_EXPORT
size_t ritual_ZN18QmlPressureReading33_qt_property_m_temperature_offsetEv() {
  return QmlPressureReading::_qt_property_m_temperature_offset();
}

//  a Python function taken by a CuteQmlPressureReading, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QmlPressureReading(
    QmlPressureReading *self,
    const char *key,
    void *call) {
  return static_cast<CuteQmlPressureReading *>(self)->take(key, call);
}

//  QSensorReading *QmlPressureReading::reading() const
extern "C" Q_DECL_EXPORT
QSensorReading *ritual_own_ZNK18QmlPressureReading7readingEv(
    const QmlPressureReading *self) {
  return self->QmlPressureReading::reading();
}

//  void QmlPressureReading::readingUpdate()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QmlPressureReading13readingUpdateEv(
    QmlPressureReading *self) {
  self->QmlPressureReading::readingUpdate();
}

//  a QBindable<qreal> a ritual of QmlPressureReading gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QmlPressureReading__QBindable_qreal(
    QBindable<qreal> *self) {
  delete self;
}
