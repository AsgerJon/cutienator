//  Written by dev_tooling.RitualGenerator from the records of
//  QtSensors/qhumiditysensor.h, Qt 6.12.0. Changes made here are lost.
#include <QtSensors/qhumiditysensor.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QHumidityReading that Python can take functions over in. Every QHumidityReading
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQHumidityReadingCall0)(const void *, QSensorReading *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQHumidityReadingCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQHumidityReadingCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHumidityReadingCall3)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHumidityReadingCall4)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHumidityReadingCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHumidityReadingCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHumidityReadingCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQHumidityReading : public QHumidityReading {
public:
  using QHumidityReading::QHumidityReading;
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

  //  void QHumidityReading::copyValuesFrom(QSensorReading *other)
  void copyValuesFrom(QSensorReading *other) override {
    if (taken[0]) {
      int handled = 0;
      CuteQHumidityReadingCall0 call = reinterpret_cast<CuteQHumidityReadingCall0>(taken[0]);
      call(this, other, &handled);
      if (handled) return;
    }
    QHumidityReading::copyValuesFrom(other);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQHumidityReadingCall1 call = reinterpret_cast<CuteQHumidityReadingCall1>(taken[1]);
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
      CuteQHumidityReadingCall2 call = reinterpret_cast<CuteQHumidityReadingCall2>(taken[2]);
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
      CuteQHumidityReadingCall3 call = reinterpret_cast<CuteQHumidityReadingCall3>(taken[3]);
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
      CuteQHumidityReadingCall4 call = reinterpret_cast<CuteQHumidityReadingCall4>(taken[4]);
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
      CuteQHumidityReadingCall5 call = reinterpret_cast<CuteQHumidityReadingCall5>(taken[5]);
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
      CuteQHumidityReadingCall6 call = reinterpret_cast<CuteQHumidityReadingCall6>(taken[6]);
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
      CuteQHumidityReadingCall7 call = reinterpret_cast<CuteQHumidityReadingCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QHumidityReading::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QHumidityReading10metaObjectEv(
    const QHumidityReading *self) {
  return self->metaObject();
}

//  QString QHumidityReading::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QHumidityReading2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QHumidityReading::tr(s, c, n));
}

//  QHumidityReading::QHumidityReading(QObject *parent)
extern "C" Q_DECL_EXPORT
QHumidityReading *ritual_ZN16QHumidityReadingC1EP7QObject(QObject *parent) {
  return new CuteQHumidityReading(parent);
}

//  QHumidityReading::~QHumidityReading()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QHumidityReadingD1Ev(QHumidityReading *self) {
  delete self;
}

//  void QHumidityReading::copyValuesFrom(QSensorReading *other)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QHumidityReading14copyValuesFromEP14QSensorReading(
    QHumidityReading *self,
    QSensorReading *other) {
  self->copyValuesFrom(other);
}

//  qreal QHumidityReading::relativeHumidity() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK16QHumidityReading16relativeHumidityEv(
    const QHumidityReading *self) {
  return self->relativeHumidity();
}

//  void QHumidityReading::setRelativeHumidity(qreal percent)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QHumidityReading19setRelativeHumidityEd(
    QHumidityReading *self,
    qreal percent) {
  self->setRelativeHumidity(percent);
}

//  qreal QHumidityReading::absoluteHumidity() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK16QHumidityReading16absoluteHumidityEv(
    const QHumidityReading *self) {
  return self->absoluteHumidity();
}

//  void QHumidityReading::setAbsoluteHumidity(qreal value)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QHumidityReading19setAbsoluteHumidityEd(
    QHumidityReading *self,
    qreal value) {
  self->setAbsoluteHumidity(value);
}

//  a Python function taken by a CuteQHumidityReading, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QHumidityReading(
    QHumidityReading *self,
    const char *key,
    void *call) {
  return static_cast<CuteQHumidityReading *>(self)->take(key, call);
}

//  void QHumidityReading::copyValuesFrom(QSensorReading *other)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QHumidityReading14copyValuesFromEP14QSensorReading(
    QHumidityReading *self,
    QSensorReading *other) {
  self->QHumidityReading::copyValuesFrom(other);
}
