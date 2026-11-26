//  Written by dev_tooling.RitualGenerator from the records of
//  QtSensors/qaccelerometer.h, Qt 6.12.0. Changes made here are lost.
#include <QtSensors/qaccelerometer.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QAccelerometer that Python can take functions over in. Every QAccelerometer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAccelerometerCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAccelerometerCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAccelerometerCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAccelerometerCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAccelerometerCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAccelerometerCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAccelerometerCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQAccelerometer : public QAccelerometer {
public:
  using QAccelerometer::QAccelerometer;
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
      CuteQAccelerometerCall0 call = reinterpret_cast<CuteQAccelerometerCall0>(taken[0]);
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
      CuteQAccelerometerCall1 call = reinterpret_cast<CuteQAccelerometerCall1>(taken[1]);
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
      CuteQAccelerometerCall2 call = reinterpret_cast<CuteQAccelerometerCall2>(taken[2]);
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
      CuteQAccelerometerCall3 call = reinterpret_cast<CuteQAccelerometerCall3>(taken[3]);
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
      CuteQAccelerometerCall4 call = reinterpret_cast<CuteQAccelerometerCall4>(taken[4]);
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
      CuteQAccelerometerCall5 call = reinterpret_cast<CuteQAccelerometerCall5>(taken[5]);
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
      CuteQAccelerometerCall6 call = reinterpret_cast<CuteQAccelerometerCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QAccelerometer::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14QAccelerometer10metaObjectEv(
    const QAccelerometer *self) {
  return self->metaObject();
}

//  void *QAccelerometer::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN14QAccelerometer11qt_metacastEPKc(
    QAccelerometer *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QAccelerometer::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN14QAccelerometer11qt_metacallEN11QMetaObject4CallEiPPv(
    QAccelerometer *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QAccelerometer::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QAccelerometer2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QAccelerometer::tr(s, c, n));
}

//  QAccelerometer::QAccelerometer(QObject *parent)
extern "C" Q_DECL_EXPORT
QAccelerometer *ritual_ZN14QAccelerometerC1EP7QObject(QObject *parent) {
  return new CuteQAccelerometer(parent);
}

//  QAccelerometer::~QAccelerometer()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QAccelerometerD1Ev(QAccelerometer *self) {
  delete self;
}

//  AccelerationMode QAccelerometer::accelerationMode() const
extern "C" Q_DECL_EXPORT
QAccelerometer::AccelerationMode ritual_ZNK14QAccelerometer16accelerationModeEv(
    const QAccelerometer *self) {
  return self->accelerationMode();
}

//  void QAccelerometer::setAccelerationMode(AccelerationMode
//      accelerationMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QAccelerometer19setAccelerationModeENS_16AccelerationModeE(
    QAccelerometer *self,
    QAccelerometer::AccelerationMode accelerationMode) {
  self->setAccelerationMode(accelerationMode);
}

//  QAccelerometerReading *QAccelerometer::reading() const
extern "C" Q_DECL_EXPORT
QAccelerometerReading *ritual_ZNK14QAccelerometer7readingEv(
    const QAccelerometer *self) {
  return self->reading();
}

//  void QAccelerometer::accelerationModeChanged(AccelerationMode
//      accelerationMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QAccelerometer23accelerationModeChangedENS_16AccelerationModeE(
    QAccelerometer *self,
    QAccelerometer::AccelerationMode accelerationMode) {
  self->accelerationModeChanged(accelerationMode);
}

//  QAccelerometerPrivate *QAccelerometer::d_func()
extern "C" Q_DECL_EXPORT
QAccelerometerPrivate *ritual_ZN14QAccelerometer6d_funcEv(
    QAccelerometer *self) {
  return self->d_func();
}

//  const QAccelerometerPrivate *QAccelerometer::d_func() const
extern "C" Q_DECL_EXPORT
const QAccelerometerPrivate *ritual_ZNK14QAccelerometer6d_funcEv(
    const QAccelerometer *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQAccelerometer, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAccelerometer(
    QAccelerometer *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAccelerometer *>(self)->take(key, call);
}
