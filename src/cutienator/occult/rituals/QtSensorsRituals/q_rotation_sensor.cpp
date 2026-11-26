//  Written by dev_tooling.RitualGenerator from the records of
//  QtSensors/qrotationsensor.h, Qt 6.12.0. Changes made here are lost.
#include <QtSensors/qrotationsensor.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QRotationSensor that Python can take functions over in. Every QRotationSensor
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQRotationSensorCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQRotationSensorCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRotationSensorCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRotationSensorCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRotationSensorCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRotationSensorCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRotationSensorCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQRotationSensor : public QRotationSensor {
public:
  using QRotationSensor::QRotationSensor;
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
      CuteQRotationSensorCall0 call = reinterpret_cast<CuteQRotationSensorCall0>(taken[0]);
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
      CuteQRotationSensorCall1 call = reinterpret_cast<CuteQRotationSensorCall1>(taken[1]);
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
      CuteQRotationSensorCall2 call = reinterpret_cast<CuteQRotationSensorCall2>(taken[2]);
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
      CuteQRotationSensorCall3 call = reinterpret_cast<CuteQRotationSensorCall3>(taken[3]);
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
      CuteQRotationSensorCall4 call = reinterpret_cast<CuteQRotationSensorCall4>(taken[4]);
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
      CuteQRotationSensorCall5 call = reinterpret_cast<CuteQRotationSensorCall5>(taken[5]);
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
      CuteQRotationSensorCall6 call = reinterpret_cast<CuteQRotationSensorCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QRotationSensor::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QRotationSensor10metaObjectEv(
    const QRotationSensor *self) {
  return self->metaObject();
}

//  void *QRotationSensor::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN15QRotationSensor11qt_metacastEPKc(
    QRotationSensor *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QRotationSensor::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN15QRotationSensor11qt_metacallEN11QMetaObject4CallEiPPv(
    QRotationSensor *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QRotationSensor::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QRotationSensor2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QRotationSensor::tr(s, c, n));
}

//  QRotationSensor::QRotationSensor(QObject *parent)
extern "C" Q_DECL_EXPORT
QRotationSensor *ritual_ZN15QRotationSensorC1EP7QObject(QObject *parent) {
  return new CuteQRotationSensor(parent);
}

//  QRotationSensor::~QRotationSensor()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QRotationSensorD1Ev(QRotationSensor *self) {
  delete self;
}

//  QRotationReading *QRotationSensor::reading() const
extern "C" Q_DECL_EXPORT
QRotationReading *ritual_ZNK15QRotationSensor7readingEv(
    const QRotationSensor *self) {
  return self->reading();
}

//  bool QRotationSensor::hasZ() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QRotationSensor4hasZEv(const QRotationSensor *self) {
  return self->hasZ();
}

//  void QRotationSensor::setHasZ(bool hasZ)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QRotationSensor7setHasZEb(QRotationSensor *self, bool hasZ) {
  self->setHasZ(hasZ);
}

//  void QRotationSensor::hasZChanged(bool hasZ)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QRotationSensor11hasZChangedEb(
    QRotationSensor *self,
    bool hasZ) {
  self->hasZChanged(hasZ);
}

//  QRotationSensorPrivate *QRotationSensor::d_func()
extern "C" Q_DECL_EXPORT
QRotationSensorPrivate *ritual_ZN15QRotationSensor6d_funcEv(
    QRotationSensor *self) {
  return self->d_func();
}

//  const QRotationSensorPrivate *QRotationSensor::d_func() const
extern "C" Q_DECL_EXPORT
const QRotationSensorPrivate *ritual_ZNK15QRotationSensor6d_funcEv(
    const QRotationSensor *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQRotationSensor, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QRotationSensor(
    QRotationSensor *self,
    const char *key,
    void *call) {
  return static_cast<CuteQRotationSensor *>(self)->take(key, call);
}
