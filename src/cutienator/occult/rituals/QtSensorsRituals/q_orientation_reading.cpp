//  Written by dev_tooling.RitualGenerator from the records of
//  QtSensors/qorientationsensor.h, Qt 6.12.0. Changes made here are lost.
#include <QtSensors/qorientationsensor.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QOrientationReading that Python can take functions over in. Every QOrientationReading
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQOrientationReadingCall0)(const void *, QSensorReading *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQOrientationReadingCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQOrientationReadingCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOrientationReadingCall3)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOrientationReadingCall4)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOrientationReadingCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOrientationReadingCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOrientationReadingCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQOrientationReading : public QOrientationReading {
public:
  using QOrientationReading::QOrientationReading;
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

  //  void QOrientationReading::copyValuesFrom(QSensorReading *other)
  void copyValuesFrom(QSensorReading *other) override {
    if (taken[0]) {
      int handled = 0;
      CuteQOrientationReadingCall0 call = reinterpret_cast<CuteQOrientationReadingCall0>(taken[0]);
      call(this, other, &handled);
      if (handled) return;
    }
    QOrientationReading::copyValuesFrom(other);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQOrientationReadingCall1 call = reinterpret_cast<CuteQOrientationReadingCall1>(taken[1]);
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
      CuteQOrientationReadingCall2 call = reinterpret_cast<CuteQOrientationReadingCall2>(taken[2]);
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
      CuteQOrientationReadingCall3 call = reinterpret_cast<CuteQOrientationReadingCall3>(taken[3]);
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
      CuteQOrientationReadingCall4 call = reinterpret_cast<CuteQOrientationReadingCall4>(taken[4]);
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
      CuteQOrientationReadingCall5 call = reinterpret_cast<CuteQOrientationReadingCall5>(taken[5]);
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
      CuteQOrientationReadingCall6 call = reinterpret_cast<CuteQOrientationReadingCall6>(taken[6]);
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
      CuteQOrientationReadingCall7 call = reinterpret_cast<CuteQOrientationReadingCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QOrientationReading::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19QOrientationReading10metaObjectEv(
    const QOrientationReading *self) {
  return self->metaObject();
}

//  QString QOrientationReading::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19QOrientationReading2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QOrientationReading::tr(s, c, n));
}

//  QOrientationReading::QOrientationReading(QObject *parent)
extern "C" Q_DECL_EXPORT
QOrientationReading *ritual_ZN19QOrientationReadingC1EP7QObject(
    QObject *parent) {
  return new CuteQOrientationReading(parent);
}

//  QOrientationReading::~QOrientationReading()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QOrientationReadingD1Ev(QOrientationReading *self) {
  delete self;
}

//  void QOrientationReading::copyValuesFrom(QSensorReading *other)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QOrientationReading14copyValuesFromEP14QSensorReading(
    QOrientationReading *self,
    QSensorReading *other) {
  self->copyValuesFrom(other);
}

//  Orientation QOrientationReading::orientation() const
extern "C" Q_DECL_EXPORT
QOrientationReading::Orientation ritual_ZNK19QOrientationReading11orientationEv(
    const QOrientationReading *self) {
  return self->orientation();
}

//  void QOrientationReading::setOrientation(Orientation orientation)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QOrientationReading14setOrientationENS_11OrientationE(
    QOrientationReading *self,
    QOrientationReading::Orientation orientation) {
  self->setOrientation(orientation);
}

//  a Python function taken by a CuteQOrientationReading, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QOrientationReading(
    QOrientationReading *self,
    const char *key,
    void *call) {
  return static_cast<CuteQOrientationReading *>(self)->take(key, call);
}

//  void QOrientationReading::copyValuesFrom(QSensorReading *other)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QOrientationReading14copyValuesFromEP14QSensorReading(
    QOrientationReading *self,
    QSensorReading *other) {
  self->QOrientationReading::copyValuesFrom(other);
}
