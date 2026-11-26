//  Written by dev_tooling.RitualGenerator from the records of
//  QtSensors/qmagnetometer.h, Qt 6.12.0. Changes made here are lost.
#include <QtSensors/qmagnetometer.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QMagnetometerReading that Python can take functions over in. Every QMagnetometerReading
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQMagnetometerReadingCall0)(const void *, QSensorReading *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQMagnetometerReadingCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQMagnetometerReadingCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQMagnetometerReadingCall3)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQMagnetometerReadingCall4)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQMagnetometerReadingCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQMagnetometerReadingCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQMagnetometerReadingCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQMagnetometerReading : public QMagnetometerReading {
public:
  using QMagnetometerReading::QMagnetometerReading;
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

  //  void QMagnetometerReading::copyValuesFrom(QSensorReading *other)
  void copyValuesFrom(QSensorReading *other) override {
    if (taken[0]) {
      int handled = 0;
      CuteQMagnetometerReadingCall0 call = reinterpret_cast<CuteQMagnetometerReadingCall0>(taken[0]);
      call(this, other, &handled);
      if (handled) return;
    }
    QMagnetometerReading::copyValuesFrom(other);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQMagnetometerReadingCall1 call = reinterpret_cast<CuteQMagnetometerReadingCall1>(taken[1]);
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
      CuteQMagnetometerReadingCall2 call = reinterpret_cast<CuteQMagnetometerReadingCall2>(taken[2]);
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
      CuteQMagnetometerReadingCall3 call = reinterpret_cast<CuteQMagnetometerReadingCall3>(taken[3]);
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
      CuteQMagnetometerReadingCall4 call = reinterpret_cast<CuteQMagnetometerReadingCall4>(taken[4]);
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
      CuteQMagnetometerReadingCall5 call = reinterpret_cast<CuteQMagnetometerReadingCall5>(taken[5]);
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
      CuteQMagnetometerReadingCall6 call = reinterpret_cast<CuteQMagnetometerReadingCall6>(taken[6]);
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
      CuteQMagnetometerReadingCall7 call = reinterpret_cast<CuteQMagnetometerReadingCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QMagnetometerReading::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20QMagnetometerReading10metaObjectEv(
    const QMagnetometerReading *self) {
  return self->metaObject();
}

//  void *QMagnetometerReading::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN20QMagnetometerReading11qt_metacastEPKc(
    QMagnetometerReading *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QMagnetometerReading::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN20QMagnetometerReading11qt_metacallEN11QMetaObject4CallEiPPv(
    QMagnetometerReading *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QMagnetometerReading::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN20QMagnetometerReading2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QMagnetometerReading::tr(s, c, n));
}

//  QMagnetometerReading::QMagnetometerReading(QObject *parent)
extern "C" Q_DECL_EXPORT
QMagnetometerReading *ritual_ZN20QMagnetometerReadingC1EP7QObject(
    QObject *parent) {
  return new CuteQMagnetometerReading(parent);
}

//  QMagnetometerReading::~QMagnetometerReading()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QMagnetometerReadingD1Ev(QMagnetometerReading *self) {
  delete self;
}

//  void QMagnetometerReading::copyValuesFrom(QSensorReading *other)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QMagnetometerReading14copyValuesFromEP14QSensorReading(
    QMagnetometerReading *self,
    QSensorReading *other) {
  self->copyValuesFrom(other);
}

//  qreal QMagnetometerReading::x() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK20QMagnetometerReading1xEv(
    const QMagnetometerReading *self) {
  return self->x();
}

//  void QMagnetometerReading::setX(qreal x)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QMagnetometerReading4setXEd(
    QMagnetometerReading *self,
    qreal x) {
  self->setX(x);
}

//  qreal QMagnetometerReading::y() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK20QMagnetometerReading1yEv(
    const QMagnetometerReading *self) {
  return self->y();
}

//  void QMagnetometerReading::setY(qreal y)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QMagnetometerReading4setYEd(
    QMagnetometerReading *self,
    qreal y) {
  self->setY(y);
}

//  qreal QMagnetometerReading::z() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK20QMagnetometerReading1zEv(
    const QMagnetometerReading *self) {
  return self->z();
}

//  void QMagnetometerReading::setZ(qreal z)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QMagnetometerReading4setZEd(
    QMagnetometerReading *self,
    qreal z) {
  self->setZ(z);
}

//  qreal QMagnetometerReading::calibrationLevel() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK20QMagnetometerReading16calibrationLevelEv(
    const QMagnetometerReading *self) {
  return self->calibrationLevel();
}

//  void QMagnetometerReading::setCalibrationLevel(qreal calibrationLevel)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QMagnetometerReading19setCalibrationLevelEd(
    QMagnetometerReading *self,
    qreal calibrationLevel) {
  self->setCalibrationLevel(calibrationLevel);
}

//  a Python function taken by a CuteQMagnetometerReading, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QMagnetometerReading(
    QMagnetometerReading *self,
    const char *key,
    void *call) {
  return static_cast<CuteQMagnetometerReading *>(self)->take(key, call);
}

//  void QMagnetometerReading::copyValuesFrom(QSensorReading *other)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QMagnetometerReading14copyValuesFromEP14QSensorReading(
    QMagnetometerReading *self,
    QSensorReading *other) {
  self->QMagnetometerReading::copyValuesFrom(other);
}
