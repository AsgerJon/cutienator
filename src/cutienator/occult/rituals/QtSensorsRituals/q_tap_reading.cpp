//  Written by dev_tooling.RitualGenerator from the records of
//  QtSensors/qtapsensor.h, Qt 6.12.0. Changes made here are lost.
#include <QtSensors/qtapsensor.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QTapReading that Python can take functions over in. Every QTapReading
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQTapReadingCall0)(const void *, QSensorReading *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQTapReadingCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQTapReadingCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTapReadingCall3)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTapReadingCall4)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTapReadingCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTapReadingCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTapReadingCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQTapReading : public QTapReading {
public:
  using QTapReading::QTapReading;
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

  //  void QTapReading::copyValuesFrom(QSensorReading *other)
  void copyValuesFrom(QSensorReading *other) override {
    if (taken[0]) {
      int handled = 0;
      CuteQTapReadingCall0 call = reinterpret_cast<CuteQTapReadingCall0>(taken[0]);
      call(this, other, &handled);
      if (handled) return;
    }
    QTapReading::copyValuesFrom(other);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQTapReadingCall1 call = reinterpret_cast<CuteQTapReadingCall1>(taken[1]);
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
      CuteQTapReadingCall2 call = reinterpret_cast<CuteQTapReadingCall2>(taken[2]);
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
      CuteQTapReadingCall3 call = reinterpret_cast<CuteQTapReadingCall3>(taken[3]);
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
      CuteQTapReadingCall4 call = reinterpret_cast<CuteQTapReadingCall4>(taken[4]);
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
      CuteQTapReadingCall5 call = reinterpret_cast<CuteQTapReadingCall5>(taken[5]);
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
      CuteQTapReadingCall6 call = reinterpret_cast<CuteQTapReadingCall6>(taken[6]);
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
      CuteQTapReadingCall7 call = reinterpret_cast<CuteQTapReadingCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QTapReading::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK11QTapReading10metaObjectEv(
    const QTapReading *self) {
  return self->metaObject();
}

//  QString QTapReading::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11QTapReading2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QTapReading::tr(s, c, n));
}

//  QTapReading::QTapReading(QObject *parent)
extern "C" Q_DECL_EXPORT
QTapReading *ritual_ZN11QTapReadingC1EP7QObject(QObject *parent) {
  return new CuteQTapReading(parent);
}

//  QTapReading::~QTapReading()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTapReadingD1Ev(QTapReading *self) {
  delete self;
}

//  void QTapReading::copyValuesFrom(QSensorReading *other)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTapReading14copyValuesFromEP14QSensorReading(
    QTapReading *self,
    QSensorReading *other) {
  self->copyValuesFrom(other);
}

//  TapDirection QTapReading::tapDirection() const
extern "C" Q_DECL_EXPORT
QTapReading::TapDirection ritual_ZNK11QTapReading12tapDirectionEv(
    const QTapReading *self) {
  return self->tapDirection();
}

//  void QTapReading::setTapDirection(TapDirection tapDirection)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTapReading15setTapDirectionENS_12TapDirectionE(
    QTapReading *self,
    QTapReading::TapDirection tapDirection) {
  self->setTapDirection(tapDirection);
}

//  bool QTapReading::isDoubleTap() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QTapReading11isDoubleTapEv(const QTapReading *self) {
  return self->isDoubleTap();
}

//  void QTapReading::setDoubleTap(bool doubleTap)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTapReading12setDoubleTapEb(
    QTapReading *self,
    bool doubleTap) {
  self->setDoubleTap(doubleTap);
}

//  a Python function taken by a CuteQTapReading, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QTapReading(
    QTapReading *self,
    const char *key,
    void *call) {
  return static_cast<CuteQTapReading *>(self)->take(key, call);
}

//  void QTapReading::copyValuesFrom(QSensorReading *other)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QTapReading14copyValuesFromEP14QSensorReading(
    QTapReading *self,
    QSensorReading *other) {
  self->QTapReading::copyValuesFrom(other);
}
