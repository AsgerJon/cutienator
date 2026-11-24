//  Written by dev_tooling.RitualGenerator from the records of
//  QtSensors/qirproximitysensor.h, Qt 6.12.0. Changes made here are lost.
#include <QtSensors/qirproximitysensor.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QIRProximityReading that Python can take functions over in. Every QIRProximityReading
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQIRProximityReadingCall0)(const void *, QSensorReading *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQIRProximityReadingCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQIRProximityReadingCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQIRProximityReadingCall3)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQIRProximityReadingCall4)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQIRProximityReadingCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQIRProximityReadingCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQIRProximityReadingCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQIRProximityReading : public QIRProximityReading {
public:
  using QIRProximityReading::QIRProximityReading;
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

  //  void QIRProximityReading::copyValuesFrom(QSensorReading *other)
  void copyValuesFrom(QSensorReading *other) override {
    if (taken[0]) {
      int handled = 0;
      CuteQIRProximityReadingCall0 call = reinterpret_cast<CuteQIRProximityReadingCall0>(taken[0]);
      call(this, other, &handled);
      if (handled) return;
    }
    QIRProximityReading::copyValuesFrom(other);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQIRProximityReadingCall1 call = reinterpret_cast<CuteQIRProximityReadingCall1>(taken[1]);
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
      CuteQIRProximityReadingCall2 call = reinterpret_cast<CuteQIRProximityReadingCall2>(taken[2]);
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
      CuteQIRProximityReadingCall3 call = reinterpret_cast<CuteQIRProximityReadingCall3>(taken[3]);
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
      CuteQIRProximityReadingCall4 call = reinterpret_cast<CuteQIRProximityReadingCall4>(taken[4]);
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
      CuteQIRProximityReadingCall5 call = reinterpret_cast<CuteQIRProximityReadingCall5>(taken[5]);
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
      CuteQIRProximityReadingCall6 call = reinterpret_cast<CuteQIRProximityReadingCall6>(taken[6]);
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
      CuteQIRProximityReadingCall7 call = reinterpret_cast<CuteQIRProximityReadingCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QIRProximityReading::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19QIRProximityReading10metaObjectEv(
    const QIRProximityReading *self) {
  return self->metaObject();
}

//  QString QIRProximityReading::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19QIRProximityReading2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QIRProximityReading::tr(s, c, n));
}

//  QIRProximityReading::QIRProximityReading(QObject *parent)
extern "C" Q_DECL_EXPORT
QIRProximityReading *ritual_ZN19QIRProximityReadingC1EP7QObject(
    QObject *parent) {
  return new CuteQIRProximityReading(parent);
}

//  QIRProximityReading::~QIRProximityReading()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QIRProximityReadingD1Ev(QIRProximityReading *self) {
  delete self;
}

//  void QIRProximityReading::copyValuesFrom(QSensorReading *other)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QIRProximityReading14copyValuesFromEP14QSensorReading(
    QIRProximityReading *self,
    QSensorReading *other) {
  self->copyValuesFrom(other);
}

//  qreal QIRProximityReading::reflectance() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK19QIRProximityReading11reflectanceEv(
    const QIRProximityReading *self) {
  return self->reflectance();
}

//  void QIRProximityReading::setReflectance(qreal reflectance)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QIRProximityReading14setReflectanceEd(
    QIRProximityReading *self,
    qreal reflectance) {
  self->setReflectance(reflectance);
}

//  a Python function taken by a CuteQIRProximityReading, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QIRProximityReading(
    QIRProximityReading *self,
    const char *key,
    void *call) {
  return static_cast<CuteQIRProximityReading *>(self)->take(key, call);
}

//  void QIRProximityReading::copyValuesFrom(QSensorReading *other)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QIRProximityReading14copyValuesFromEP14QSensorReading(
    QIRProximityReading *self,
    QSensorReading *other) {
  self->QIRProximityReading::copyValuesFrom(other);
}
