//  Written by dev_tooling.RitualGenerator from the records of
//  QtSensors/qaccelerometer.h, Qt 6.12.0. Changes made here are lost.
#include <QtSensors/qaccelerometer.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QAccelerometerReading that Python can take functions over in. Every QAccelerometerReading
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQAccelerometerReadingCall0)(const void *, QSensorReading *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAccelerometerReadingCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAccelerometerReadingCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAccelerometerReadingCall3)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAccelerometerReadingCall4)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAccelerometerReadingCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAccelerometerReadingCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAccelerometerReadingCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQAccelerometerReading : public QAccelerometerReading {
public:
  using QAccelerometerReading::QAccelerometerReading;
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

  //  void QAccelerometerReading::copyValuesFrom(QSensorReading *other)
  void copyValuesFrom(QSensorReading *other) override {
    if (taken[0]) {
      int handled = 0;
      CuteQAccelerometerReadingCall0 call = reinterpret_cast<CuteQAccelerometerReadingCall0>(taken[0]);
      call(this, other, &handled);
      if (handled) return;
    }
    QAccelerometerReading::copyValuesFrom(other);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQAccelerometerReadingCall1 call = reinterpret_cast<CuteQAccelerometerReadingCall1>(taken[1]);
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
      CuteQAccelerometerReadingCall2 call = reinterpret_cast<CuteQAccelerometerReadingCall2>(taken[2]);
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
      CuteQAccelerometerReadingCall3 call = reinterpret_cast<CuteQAccelerometerReadingCall3>(taken[3]);
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
      CuteQAccelerometerReadingCall4 call = reinterpret_cast<CuteQAccelerometerReadingCall4>(taken[4]);
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
      CuteQAccelerometerReadingCall5 call = reinterpret_cast<CuteQAccelerometerReadingCall5>(taken[5]);
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
      CuteQAccelerometerReadingCall6 call = reinterpret_cast<CuteQAccelerometerReadingCall6>(taken[6]);
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
      CuteQAccelerometerReadingCall7 call = reinterpret_cast<CuteQAccelerometerReadingCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QAccelerometerReading::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21QAccelerometerReading10metaObjectEv(
    const QAccelerometerReading *self) {
  return self->metaObject();
}

//  QString QAccelerometerReading::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN21QAccelerometerReading2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QAccelerometerReading::tr(s, c, n));
}

//  QAccelerometerReading::QAccelerometerReading(QObject *parent)
extern "C" Q_DECL_EXPORT
QAccelerometerReading *ritual_ZN21QAccelerometerReadingC1EP7QObject(
    QObject *parent) {
  return new CuteQAccelerometerReading(parent);
}

//  QAccelerometerReading::~QAccelerometerReading()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QAccelerometerReadingD1Ev(QAccelerometerReading *self) {
  delete self;
}

//  void QAccelerometerReading::copyValuesFrom(QSensorReading *other)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QAccelerometerReading14copyValuesFromEP14QSensorReading(
    QAccelerometerReading *self,
    QSensorReading *other) {
  self->copyValuesFrom(other);
}

//  qreal QAccelerometerReading::x() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK21QAccelerometerReading1xEv(
    const QAccelerometerReading *self) {
  return self->x();
}

//  void QAccelerometerReading::setX(qreal x)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QAccelerometerReading4setXEd(
    QAccelerometerReading *self,
    qreal x) {
  self->setX(x);
}

//  qreal QAccelerometerReading::y() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK21QAccelerometerReading1yEv(
    const QAccelerometerReading *self) {
  return self->y();
}

//  void QAccelerometerReading::setY(qreal y)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QAccelerometerReading4setYEd(
    QAccelerometerReading *self,
    qreal y) {
  self->setY(y);
}

//  qreal QAccelerometerReading::z() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK21QAccelerometerReading1zEv(
    const QAccelerometerReading *self) {
  return self->z();
}

//  void QAccelerometerReading::setZ(qreal z)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QAccelerometerReading4setZEd(
    QAccelerometerReading *self,
    qreal z) {
  self->setZ(z);
}

//  a Python function taken by a CuteQAccelerometerReading, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAccelerometerReading(
    QAccelerometerReading *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAccelerometerReading *>(self)->take(key, call);
}

//  void QAccelerometerReading::copyValuesFrom(QSensorReading *other)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QAccelerometerReading14copyValuesFromEP14QSensorReading(
    QAccelerometerReading *self,
    QSensorReading *other) {
  self->QAccelerometerReading::copyValuesFrom(other);
}
