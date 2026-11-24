//  Written by dev_tooling.RitualGenerator from the records of
//  QtSensors/qrotationsensor.h, Qt 6.12.0. Changes made here are lost.
#include <QtSensors/qrotationsensor.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QRotationReading that Python can take functions over in. Every QRotationReading
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQRotationReadingCall0)(const void *, QSensorReading *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQRotationReadingCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQRotationReadingCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRotationReadingCall3)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRotationReadingCall4)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRotationReadingCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRotationReadingCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRotationReadingCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQRotationReading : public QRotationReading {
public:
  using QRotationReading::QRotationReading;
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

  //  void QRotationReading::copyValuesFrom(QSensorReading *other)
  void copyValuesFrom(QSensorReading *other) override {
    if (taken[0]) {
      int handled = 0;
      CuteQRotationReadingCall0 call = reinterpret_cast<CuteQRotationReadingCall0>(taken[0]);
      call(this, other, &handled);
      if (handled) return;
    }
    QRotationReading::copyValuesFrom(other);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQRotationReadingCall1 call = reinterpret_cast<CuteQRotationReadingCall1>(taken[1]);
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
      CuteQRotationReadingCall2 call = reinterpret_cast<CuteQRotationReadingCall2>(taken[2]);
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
      CuteQRotationReadingCall3 call = reinterpret_cast<CuteQRotationReadingCall3>(taken[3]);
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
      CuteQRotationReadingCall4 call = reinterpret_cast<CuteQRotationReadingCall4>(taken[4]);
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
      CuteQRotationReadingCall5 call = reinterpret_cast<CuteQRotationReadingCall5>(taken[5]);
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
      CuteQRotationReadingCall6 call = reinterpret_cast<CuteQRotationReadingCall6>(taken[6]);
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
      CuteQRotationReadingCall7 call = reinterpret_cast<CuteQRotationReadingCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QRotationReading::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QRotationReading10metaObjectEv(
    const QRotationReading *self) {
  return self->metaObject();
}

//  QString QRotationReading::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QRotationReading2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QRotationReading::tr(s, c, n));
}

//  QRotationReading::QRotationReading(QObject *parent)
extern "C" Q_DECL_EXPORT
QRotationReading *ritual_ZN16QRotationReadingC1EP7QObject(QObject *parent) {
  return new CuteQRotationReading(parent);
}

//  QRotationReading::~QRotationReading()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QRotationReadingD1Ev(QRotationReading *self) {
  delete self;
}

//  void QRotationReading::copyValuesFrom(QSensorReading *other)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QRotationReading14copyValuesFromEP14QSensorReading(
    QRotationReading *self,
    QSensorReading *other) {
  self->copyValuesFrom(other);
}

//  qreal QRotationReading::x() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK16QRotationReading1xEv(const QRotationReading *self) {
  return self->x();
}

//  qreal QRotationReading::y() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK16QRotationReading1yEv(const QRotationReading *self) {
  return self->y();
}

//  qreal QRotationReading::z() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK16QRotationReading1zEv(const QRotationReading *self) {
  return self->z();
}

//  void QRotationReading::setFromEuler(qreal x, qreal y, qreal z)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QRotationReading12setFromEulerEddd(
    QRotationReading *self,
    qreal x,
    qreal y,
    qreal z) {
  self->setFromEuler(x, y, z);
}

//  a Python function taken by a CuteQRotationReading, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QRotationReading(
    QRotationReading *self,
    const char *key,
    void *call) {
  return static_cast<CuteQRotationReading *>(self)->take(key, call);
}

//  void QRotationReading::copyValuesFrom(QSensorReading *other)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QRotationReading14copyValuesFromEP14QSensorReading(
    QRotationReading *self,
    QSensorReading *other) {
  self->QRotationReading::copyValuesFrom(other);
}
