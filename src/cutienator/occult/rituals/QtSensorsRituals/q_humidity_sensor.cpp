//  Written by dev_tooling.RitualGenerator from the records of
//  QtSensors/qhumiditysensor.h, Qt 6.12.0. Changes made here are lost.
#include <QtSensors/qhumiditysensor.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QHumiditySensor that Python can take functions over in. Every QHumiditySensor
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQHumiditySensorCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQHumiditySensorCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHumiditySensorCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHumiditySensorCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHumiditySensorCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHumiditySensorCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHumiditySensorCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQHumiditySensor : public QHumiditySensor {
public:
  using QHumiditySensor::QHumiditySensor;
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
      CuteQHumiditySensorCall0 call = reinterpret_cast<CuteQHumiditySensorCall0>(taken[0]);
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
      CuteQHumiditySensorCall1 call = reinterpret_cast<CuteQHumiditySensorCall1>(taken[1]);
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
      CuteQHumiditySensorCall2 call = reinterpret_cast<CuteQHumiditySensorCall2>(taken[2]);
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
      CuteQHumiditySensorCall3 call = reinterpret_cast<CuteQHumiditySensorCall3>(taken[3]);
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
      CuteQHumiditySensorCall4 call = reinterpret_cast<CuteQHumiditySensorCall4>(taken[4]);
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
      CuteQHumiditySensorCall5 call = reinterpret_cast<CuteQHumiditySensorCall5>(taken[5]);
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
      CuteQHumiditySensorCall6 call = reinterpret_cast<CuteQHumiditySensorCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QHumiditySensor::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QHumiditySensor10metaObjectEv(
    const QHumiditySensor *self) {
  return self->metaObject();
}

//  void *QHumiditySensor::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN15QHumiditySensor11qt_metacastEPKc(
    QHumiditySensor *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QHumiditySensor::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN15QHumiditySensor11qt_metacallEN11QMetaObject4CallEiPPv(
    QHumiditySensor *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QHumiditySensor::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QHumiditySensor2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QHumiditySensor::tr(s, c, n));
}

//  QHumiditySensor::QHumiditySensor(QObject *parent)
extern "C" Q_DECL_EXPORT
QHumiditySensor *ritual_ZN15QHumiditySensorC1EP7QObject(QObject *parent) {
  return new CuteQHumiditySensor(parent);
}

//  QHumiditySensor::~QHumiditySensor()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QHumiditySensorD1Ev(QHumiditySensor *self) {
  delete self;
}

//  QHumidityReading *QHumiditySensor::reading() const
extern "C" Q_DECL_EXPORT
QHumidityReading *ritual_ZNK15QHumiditySensor7readingEv(
    const QHumiditySensor *self) {
  return self->reading();
}

//  QHumiditySensorPrivate *QHumiditySensor::d_func()
extern "C" Q_DECL_EXPORT
QHumiditySensorPrivate *ritual_ZN15QHumiditySensor6d_funcEv(
    QHumiditySensor *self) {
  return self->d_func();
}

//  const QHumiditySensorPrivate *QHumiditySensor::d_func() const
extern "C" Q_DECL_EXPORT
const QHumiditySensorPrivate *ritual_ZNK15QHumiditySensor6d_funcEv(
    const QHumiditySensor *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQHumiditySensor, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QHumiditySensor(
    QHumiditySensor *self,
    const char *key,
    void *call) {
  return static_cast<CuteQHumiditySensor *>(self)->take(key, call);
}
