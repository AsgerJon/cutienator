//  Written by dev_tooling.RitualGenerator from the records of
//  QtSensors/qlightsensor.h, Qt 6.12.0. Changes made here are lost.
#include <QtSensors/qlightsensor.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QLightSensor that Python can take functions over in. Every QLightSensor
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQLightSensorCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQLightSensorCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLightSensorCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLightSensorCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLightSensorCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLightSensorCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLightSensorCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQLightSensor : public QLightSensor {
public:
  using QLightSensor::QLightSensor;
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
      CuteQLightSensorCall0 call = reinterpret_cast<CuteQLightSensorCall0>(taken[0]);
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
      CuteQLightSensorCall1 call = reinterpret_cast<CuteQLightSensorCall1>(taken[1]);
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
      CuteQLightSensorCall2 call = reinterpret_cast<CuteQLightSensorCall2>(taken[2]);
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
      CuteQLightSensorCall3 call = reinterpret_cast<CuteQLightSensorCall3>(taken[3]);
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
      CuteQLightSensorCall4 call = reinterpret_cast<CuteQLightSensorCall4>(taken[4]);
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
      CuteQLightSensorCall5 call = reinterpret_cast<CuteQLightSensorCall5>(taken[5]);
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
      CuteQLightSensorCall6 call = reinterpret_cast<CuteQLightSensorCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QLightSensor::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK12QLightSensor10metaObjectEv(
    const QLightSensor *self) {
  return self->metaObject();
}

//  QString QLightSensor::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN12QLightSensor2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QLightSensor::tr(s, c, n));
}

//  QLightSensor::QLightSensor(QObject *parent)
extern "C" Q_DECL_EXPORT
QLightSensor *ritual_ZN12QLightSensorC1EP7QObject(QObject *parent) {
  return new CuteQLightSensor(parent);
}

//  QLightSensor::~QLightSensor()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QLightSensorD1Ev(QLightSensor *self) {
  delete self;
}

//  QLightReading *QLightSensor::reading() const
extern "C" Q_DECL_EXPORT
QLightReading *ritual_ZNK12QLightSensor7readingEv(const QLightSensor *self) {
  return self->reading();
}

//  qreal QLightSensor::fieldOfView() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK12QLightSensor11fieldOfViewEv(const QLightSensor *self) {
  return self->fieldOfView();
}

//  void QLightSensor::setFieldOfView(qreal fieldOfView)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QLightSensor14setFieldOfViewEd(
    QLightSensor *self,
    qreal fieldOfView) {
  self->setFieldOfView(fieldOfView);
}

//  QLightSensorPrivate *QLightSensor::d_func()
extern "C" Q_DECL_EXPORT
QLightSensorPrivate *ritual_ZN12QLightSensor6d_funcEv(QLightSensor *self) {
  return self->d_func();
}

//  const QLightSensorPrivate *QLightSensor::d_func() const
extern "C" Q_DECL_EXPORT
const QLightSensorPrivate *ritual_ZNK12QLightSensor6d_funcEv(
    const QLightSensor *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQLightSensor, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QLightSensor(
    QLightSensor *self,
    const char *key,
    void *call) {
  return static_cast<CuteQLightSensor *>(self)->take(key, call);
}
