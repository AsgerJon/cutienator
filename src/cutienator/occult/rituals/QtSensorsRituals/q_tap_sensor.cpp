//  Written by dev_tooling.RitualGenerator from the records of
//  QtSensors/qtapsensor.h, Qt 6.12.0. Changes made here are lost.
#include <QtSensors/qtapsensor.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QTapSensor that Python can take functions over in. Every QTapSensor
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQTapSensorCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQTapSensorCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTapSensorCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTapSensorCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTapSensorCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTapSensorCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTapSensorCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQTapSensor : public QTapSensor {
public:
  using QTapSensor::QTapSensor;
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
      CuteQTapSensorCall0 call = reinterpret_cast<CuteQTapSensorCall0>(taken[0]);
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
      CuteQTapSensorCall1 call = reinterpret_cast<CuteQTapSensorCall1>(taken[1]);
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
      CuteQTapSensorCall2 call = reinterpret_cast<CuteQTapSensorCall2>(taken[2]);
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
      CuteQTapSensorCall3 call = reinterpret_cast<CuteQTapSensorCall3>(taken[3]);
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
      CuteQTapSensorCall4 call = reinterpret_cast<CuteQTapSensorCall4>(taken[4]);
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
      CuteQTapSensorCall5 call = reinterpret_cast<CuteQTapSensorCall5>(taken[5]);
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
      CuteQTapSensorCall6 call = reinterpret_cast<CuteQTapSensorCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QTapSensor::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10QTapSensor10metaObjectEv(
    const QTapSensor *self) {
  return self->metaObject();
}

//  QString QTapSensor::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10QTapSensor2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QTapSensor::tr(s, c, n));
}

//  QTapSensor::QTapSensor(QObject *parent)
extern "C" Q_DECL_EXPORT
QTapSensor *ritual_ZN10QTapSensorC1EP7QObject(QObject *parent) {
  return new CuteQTapSensor(parent);
}

//  QTapSensor::~QTapSensor()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTapSensorD1Ev(QTapSensor *self) {
  delete self;
}

//  QTapReading *QTapSensor::reading() const
extern "C" Q_DECL_EXPORT
QTapReading *ritual_ZNK10QTapSensor7readingEv(const QTapSensor *self) {
  return self->reading();
}

//  bool QTapSensor::returnDoubleTapEvents() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QTapSensor21returnDoubleTapEventsEv(
    const QTapSensor *self) {
  return self->returnDoubleTapEvents();
}

//  void QTapSensor::setReturnDoubleTapEvents(bool returnDoubleTapEvents)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTapSensor24setReturnDoubleTapEventsEb(
    QTapSensor *self,
    bool returnDoubleTapEvents) {
  self->setReturnDoubleTapEvents(returnDoubleTapEvents);
}

//  QTapSensorPrivate *QTapSensor::d_func()
extern "C" Q_DECL_EXPORT
QTapSensorPrivate *ritual_ZN10QTapSensor6d_funcEv(QTapSensor *self) {
  return self->d_func();
}

//  const QTapSensorPrivate *QTapSensor::d_func() const
extern "C" Q_DECL_EXPORT
const QTapSensorPrivate *ritual_ZNK10QTapSensor6d_funcEv(
    const QTapSensor *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQTapSensor, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QTapSensor(QTapSensor *self, const char *key, void *call) {
  return static_cast<CuteQTapSensor *>(self)->take(key, call);
}
