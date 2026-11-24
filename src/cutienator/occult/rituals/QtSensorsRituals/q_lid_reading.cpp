//  Written by dev_tooling.RitualGenerator from the records of
//  QtSensors/qlidsensor.h, Qt 6.12.0. Changes made here are lost.
#include <QtSensors/qlidsensor.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QLidReading that Python can take functions over in. Every QLidReading
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQLidReadingCall0)(const void *, QSensorReading *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQLidReadingCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQLidReadingCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLidReadingCall3)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLidReadingCall4)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLidReadingCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLidReadingCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLidReadingCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQLidReading : public QLidReading {
public:
  using QLidReading::QLidReading;
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

  //  void QLidReading::copyValuesFrom(QSensorReading *other)
  void copyValuesFrom(QSensorReading *other) override {
    if (taken[0]) {
      int handled = 0;
      CuteQLidReadingCall0 call = reinterpret_cast<CuteQLidReadingCall0>(taken[0]);
      call(this, other, &handled);
      if (handled) return;
    }
    QLidReading::copyValuesFrom(other);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQLidReadingCall1 call = reinterpret_cast<CuteQLidReadingCall1>(taken[1]);
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
      CuteQLidReadingCall2 call = reinterpret_cast<CuteQLidReadingCall2>(taken[2]);
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
      CuteQLidReadingCall3 call = reinterpret_cast<CuteQLidReadingCall3>(taken[3]);
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
      CuteQLidReadingCall4 call = reinterpret_cast<CuteQLidReadingCall4>(taken[4]);
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
      CuteQLidReadingCall5 call = reinterpret_cast<CuteQLidReadingCall5>(taken[5]);
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
      CuteQLidReadingCall6 call = reinterpret_cast<CuteQLidReadingCall6>(taken[6]);
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
      CuteQLidReadingCall7 call = reinterpret_cast<CuteQLidReadingCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QLidReading::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK11QLidReading10metaObjectEv(
    const QLidReading *self) {
  return self->metaObject();
}

//  QString QLidReading::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11QLidReading2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QLidReading::tr(s, c, n));
}

//  QLidReading::QLidReading(QObject *parent)
extern "C" Q_DECL_EXPORT
QLidReading *ritual_ZN11QLidReadingC1EP7QObject(QObject *parent) {
  return new CuteQLidReading(parent);
}

//  QLidReading::~QLidReading()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QLidReadingD1Ev(QLidReading *self) {
  delete self;
}

//  void QLidReading::copyValuesFrom(QSensorReading *other)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QLidReading14copyValuesFromEP14QSensorReading(
    QLidReading *self,
    QSensorReading *other) {
  self->copyValuesFrom(other);
}

//  bool QLidReading::backLidClosed() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QLidReading13backLidClosedEv(const QLidReading *self) {
  return self->backLidClosed();
}

//  void QLidReading::setBackLidClosed(bool closed)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QLidReading16setBackLidClosedEb(
    QLidReading *self,
    bool closed) {
  self->setBackLidClosed(closed);
}

//  bool QLidReading::frontLidClosed() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QLidReading14frontLidClosedEv(const QLidReading *self) {
  return self->frontLidClosed();
}

//  void QLidReading::setFrontLidClosed(bool closed)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QLidReading17setFrontLidClosedEb(
    QLidReading *self,
    bool closed) {
  self->setFrontLidClosed(closed);
}

//  a Python function taken by a CuteQLidReading, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QLidReading(
    QLidReading *self,
    const char *key,
    void *call) {
  return static_cast<CuteQLidReading *>(self)->take(key, call);
}

//  void QLidReading::copyValuesFrom(QSensorReading *other)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QLidReading14copyValuesFromEP14QSensorReading(
    QLidReading *self,
    QSensorReading *other) {
  self->QLidReading::copyValuesFrom(other);
}
