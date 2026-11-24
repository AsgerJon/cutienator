//  Written by dev_tooling.RitualGenerator from the records of
//  QtSensors/qcompass.h, Qt 6.12.0. Changes made here are lost.
#include <QtSensors/qcompass.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QCompassReading that Python can take functions over in. Every QCompassReading
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQCompassReadingCall0)(const void *, QSensorReading *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQCompassReadingCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQCompassReadingCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCompassReadingCall3)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCompassReadingCall4)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCompassReadingCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCompassReadingCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCompassReadingCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQCompassReading : public QCompassReading {
public:
  using QCompassReading::QCompassReading;
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

  //  void QCompassReading::copyValuesFrom(QSensorReading *other)
  void copyValuesFrom(QSensorReading *other) override {
    if (taken[0]) {
      int handled = 0;
      CuteQCompassReadingCall0 call = reinterpret_cast<CuteQCompassReadingCall0>(taken[0]);
      call(this, other, &handled);
      if (handled) return;
    }
    QCompassReading::copyValuesFrom(other);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQCompassReadingCall1 call = reinterpret_cast<CuteQCompassReadingCall1>(taken[1]);
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
      CuteQCompassReadingCall2 call = reinterpret_cast<CuteQCompassReadingCall2>(taken[2]);
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
      CuteQCompassReadingCall3 call = reinterpret_cast<CuteQCompassReadingCall3>(taken[3]);
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
      CuteQCompassReadingCall4 call = reinterpret_cast<CuteQCompassReadingCall4>(taken[4]);
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
      CuteQCompassReadingCall5 call = reinterpret_cast<CuteQCompassReadingCall5>(taken[5]);
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
      CuteQCompassReadingCall6 call = reinterpret_cast<CuteQCompassReadingCall6>(taken[6]);
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
      CuteQCompassReadingCall7 call = reinterpret_cast<CuteQCompassReadingCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QCompassReading::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QCompassReading10metaObjectEv(
    const QCompassReading *self) {
  return self->metaObject();
}

//  QString QCompassReading::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QCompassReading2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QCompassReading::tr(s, c, n));
}

//  QCompassReading::QCompassReading(QObject *parent)
extern "C" Q_DECL_EXPORT
QCompassReading *ritual_ZN15QCompassReadingC1EP7QObject(QObject *parent) {
  return new CuteQCompassReading(parent);
}

//  QCompassReading::~QCompassReading()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCompassReadingD1Ev(QCompassReading *self) {
  delete self;
}

//  void QCompassReading::copyValuesFrom(QSensorReading *other)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCompassReading14copyValuesFromEP14QSensorReading(
    QCompassReading *self,
    QSensorReading *other) {
  self->copyValuesFrom(other);
}

//  qreal QCompassReading::azimuth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QCompassReading7azimuthEv(const QCompassReading *self) {
  return self->azimuth();
}

//  void QCompassReading::setAzimuth(qreal azimuth)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCompassReading10setAzimuthEd(
    QCompassReading *self,
    qreal azimuth) {
  self->setAzimuth(azimuth);
}

//  qreal QCompassReading::calibrationLevel() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QCompassReading16calibrationLevelEv(
    const QCompassReading *self) {
  return self->calibrationLevel();
}

//  void QCompassReading::setCalibrationLevel(qreal calibrationLevel)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCompassReading19setCalibrationLevelEd(
    QCompassReading *self,
    qreal calibrationLevel) {
  self->setCalibrationLevel(calibrationLevel);
}

//  a Python function taken by a CuteQCompassReading, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QCompassReading(
    QCompassReading *self,
    const char *key,
    void *call) {
  return static_cast<CuteQCompassReading *>(self)->take(key, call);
}

//  void QCompassReading::copyValuesFrom(QSensorReading *other)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QCompassReading14copyValuesFromEP14QSensorReading(
    QCompassReading *self,
    QSensorReading *other) {
  self->QCompassReading::copyValuesFrom(other);
}
