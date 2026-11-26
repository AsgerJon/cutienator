//  Written by dev_tooling.RitualGenerator from the records of
//  QtSensors/qambientlightsensor.h, Qt 6.12.0. Changes made here are lost.
#include <QtSensors/qambientlightsensor.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QAmbientLightReading that Python can take functions over in. Every QAmbientLightReading
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQAmbientLightReadingCall0)(const void *, QSensorReading *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAmbientLightReadingCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAmbientLightReadingCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAmbientLightReadingCall3)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAmbientLightReadingCall4)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAmbientLightReadingCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAmbientLightReadingCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAmbientLightReadingCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQAmbientLightReading : public QAmbientLightReading {
public:
  using QAmbientLightReading::QAmbientLightReading;
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

  //  void QAmbientLightReading::copyValuesFrom(QSensorReading *other)
  void copyValuesFrom(QSensorReading *other) override {
    if (taken[0]) {
      int handled = 0;
      CuteQAmbientLightReadingCall0 call = reinterpret_cast<CuteQAmbientLightReadingCall0>(taken[0]);
      call(this, other, &handled);
      if (handled) return;
    }
    QAmbientLightReading::copyValuesFrom(other);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQAmbientLightReadingCall1 call = reinterpret_cast<CuteQAmbientLightReadingCall1>(taken[1]);
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
      CuteQAmbientLightReadingCall2 call = reinterpret_cast<CuteQAmbientLightReadingCall2>(taken[2]);
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
      CuteQAmbientLightReadingCall3 call = reinterpret_cast<CuteQAmbientLightReadingCall3>(taken[3]);
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
      CuteQAmbientLightReadingCall4 call = reinterpret_cast<CuteQAmbientLightReadingCall4>(taken[4]);
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
      CuteQAmbientLightReadingCall5 call = reinterpret_cast<CuteQAmbientLightReadingCall5>(taken[5]);
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
      CuteQAmbientLightReadingCall6 call = reinterpret_cast<CuteQAmbientLightReadingCall6>(taken[6]);
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
      CuteQAmbientLightReadingCall7 call = reinterpret_cast<CuteQAmbientLightReadingCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QAmbientLightReading::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20QAmbientLightReading10metaObjectEv(
    const QAmbientLightReading *self) {
  return self->metaObject();
}

//  void *QAmbientLightReading::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN20QAmbientLightReading11qt_metacastEPKc(
    QAmbientLightReading *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QAmbientLightReading::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN20QAmbientLightReading11qt_metacallEN11QMetaObject4CallEiPPv(
    QAmbientLightReading *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QAmbientLightReading::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN20QAmbientLightReading2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QAmbientLightReading::tr(s, c, n));
}

//  QAmbientLightReading::QAmbientLightReading(QObject *parent)
extern "C" Q_DECL_EXPORT
QAmbientLightReading *ritual_ZN20QAmbientLightReadingC1EP7QObject(
    QObject *parent) {
  return new CuteQAmbientLightReading(parent);
}

//  QAmbientLightReading::~QAmbientLightReading()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAmbientLightReadingD1Ev(QAmbientLightReading *self) {
  delete self;
}

//  void QAmbientLightReading::copyValuesFrom(QSensorReading *other)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAmbientLightReading14copyValuesFromEP14QSensorReading(
    QAmbientLightReading *self,
    QSensorReading *other) {
  self->copyValuesFrom(other);
}

//  LightLevel QAmbientLightReading::lightLevel() const
extern "C" Q_DECL_EXPORT
QAmbientLightReading::LightLevel ritual_ZNK20QAmbientLightReading10lightLevelEv(
    const QAmbientLightReading *self) {
  return self->lightLevel();
}

//  void QAmbientLightReading::setLightLevel(LightLevel lightLevel)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAmbientLightReading13setLightLevelENS_10LightLevelE(
    QAmbientLightReading *self,
    QAmbientLightReading::LightLevel lightLevel) {
  self->setLightLevel(lightLevel);
}

//  a Python function taken by a CuteQAmbientLightReading, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAmbientLightReading(
    QAmbientLightReading *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAmbientLightReading *>(self)->take(key, call);
}

//  void QAmbientLightReading::copyValuesFrom(QSensorReading *other)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QAmbientLightReading14copyValuesFromEP14QSensorReading(
    QAmbientLightReading *self,
    QSensorReading *other) {
  self->QAmbientLightReading::copyValuesFrom(other);
}
