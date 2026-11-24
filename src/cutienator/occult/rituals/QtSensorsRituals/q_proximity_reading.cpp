//  Written by dev_tooling.RitualGenerator from the records of
//  QtSensors/qproximitysensor.h, Qt 6.12.0. Changes made here are lost.
#include <QtSensors/qproximitysensor.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QProximityReading that Python can take functions over in. Every QProximityReading
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQProximityReadingCall0)(const void *, QSensorReading *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQProximityReadingCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQProximityReadingCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQProximityReadingCall3)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQProximityReadingCall4)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQProximityReadingCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQProximityReadingCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQProximityReadingCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQProximityReading : public QProximityReading {
public:
  using QProximityReading::QProximityReading;
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

  //  void QProximityReading::copyValuesFrom(QSensorReading *other)
  void copyValuesFrom(QSensorReading *other) override {
    if (taken[0]) {
      int handled = 0;
      CuteQProximityReadingCall0 call = reinterpret_cast<CuteQProximityReadingCall0>(taken[0]);
      call(this, other, &handled);
      if (handled) return;
    }
    QProximityReading::copyValuesFrom(other);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQProximityReadingCall1 call = reinterpret_cast<CuteQProximityReadingCall1>(taken[1]);
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
      CuteQProximityReadingCall2 call = reinterpret_cast<CuteQProximityReadingCall2>(taken[2]);
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
      CuteQProximityReadingCall3 call = reinterpret_cast<CuteQProximityReadingCall3>(taken[3]);
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
      CuteQProximityReadingCall4 call = reinterpret_cast<CuteQProximityReadingCall4>(taken[4]);
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
      CuteQProximityReadingCall5 call = reinterpret_cast<CuteQProximityReadingCall5>(taken[5]);
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
      CuteQProximityReadingCall6 call = reinterpret_cast<CuteQProximityReadingCall6>(taken[6]);
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
      CuteQProximityReadingCall7 call = reinterpret_cast<CuteQProximityReadingCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QProximityReading::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QProximityReading10metaObjectEv(
    const QProximityReading *self) {
  return self->metaObject();
}

//  QString QProximityReading::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QProximityReading2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QProximityReading::tr(s, c, n));
}

//  QProximityReading::QProximityReading(QObject *parent)
extern "C" Q_DECL_EXPORT
QProximityReading *ritual_ZN17QProximityReadingC1EP7QObject(
    QObject *parent) {
  return new CuteQProximityReading(parent);
}

//  QProximityReading::~QProximityReading()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QProximityReadingD1Ev(QProximityReading *self) {
  delete self;
}

//  void QProximityReading::copyValuesFrom(QSensorReading *other)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QProximityReading14copyValuesFromEP14QSensorReading(
    QProximityReading *self,
    QSensorReading *other) {
  self->copyValuesFrom(other);
}

//  bool QProximityReading::close() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QProximityReading5closeEv(const QProximityReading *self) {
  return self->close();
}

//  void QProximityReading::setClose(bool close)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QProximityReading8setCloseEb(
    QProximityReading *self,
    bool close) {
  self->setClose(close);
}

//  a Python function taken by a CuteQProximityReading, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QProximityReading(
    QProximityReading *self,
    const char *key,
    void *call) {
  return static_cast<CuteQProximityReading *>(self)->take(key, call);
}

//  void QProximityReading::copyValuesFrom(QSensorReading *other)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QProximityReading14copyValuesFromEP14QSensorReading(
    QProximityReading *self,
    QSensorReading *other) {
  self->QProximityReading::copyValuesFrom(other);
}
