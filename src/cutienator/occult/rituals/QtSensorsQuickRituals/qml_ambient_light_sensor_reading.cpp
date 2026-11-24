//  Written by dev_tooling.RitualGenerator from the records of
//  QtSensorsQuick/6.12.0/QtSensorsQuick/private/qmlambientlightsensor_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtSensorsQuick/6.12.0/QtSensorsQuick/private/qsensorsquickglobal_p.h>
#include <QtSensorsQuick/QtSensorsQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSensorsQuick/6.12.0/QtSensorsQuick/private/qmlambientlightsensor_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QmlAmbientLightSensorReading that Python can take functions over in. Every QmlAmbientLightSensorReading
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQmlAmbientLightSensorReadingCall0)(const void *, int *);
typedef void (*CuteQmlAmbientLightSensorReadingCall1)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQmlAmbientLightSensorReadingCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQmlAmbientLightSensorReadingCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQmlAmbientLightSensorReadingCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQmlAmbientLightSensorReadingCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQmlAmbientLightSensorReadingCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQmlAmbientLightSensorReadingCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQmlAmbientLightSensorReadingCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQmlAmbientLightSensorReading : public QmlAmbientLightSensorReading {
public:
  using QmlAmbientLightSensorReading::QmlAmbientLightSensorReading;
  void *taken[9] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK16QmlSensorReading7readingEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QmlSensorReading13readingUpdateEv")) {
      taken[1] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  QSensorReading *QmlAmbientLightSensorReading::reading() const
  QSensorReading *reading() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQmlAmbientLightSensorReadingCall0 call = reinterpret_cast<CuteQmlAmbientLightSensorReadingCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSensorReading *>(given);
    }
    return QmlAmbientLightSensorReading::reading();
  }

  //  void QmlAmbientLightSensorReading::readingUpdate()
  void readingUpdate() override {
    if (taken[1]) {
      int handled = 0;
      CuteQmlAmbientLightSensorReadingCall1 call = reinterpret_cast<CuteQmlAmbientLightSensorReadingCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QmlAmbientLightSensorReading::readingUpdate();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQmlAmbientLightSensorReadingCall2 call = reinterpret_cast<CuteQmlAmbientLightSensorReadingCall2>(taken[2]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQmlAmbientLightSensorReadingCall3 call = reinterpret_cast<CuteQmlAmbientLightSensorReadingCall3>(taken[3]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQmlAmbientLightSensorReadingCall4 call = reinterpret_cast<CuteQmlAmbientLightSensorReadingCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQmlAmbientLightSensorReadingCall5 call = reinterpret_cast<CuteQmlAmbientLightSensorReadingCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQmlAmbientLightSensorReadingCall6 call = reinterpret_cast<CuteQmlAmbientLightSensorReadingCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[7]) {
      int handled = 0;
      CuteQmlAmbientLightSensorReadingCall7 call = reinterpret_cast<CuteQmlAmbientLightSensorReadingCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[8]) {
      int handled = 0;
      CuteQmlAmbientLightSensorReadingCall8 call = reinterpret_cast<CuteQmlAmbientLightSensorReadingCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QmlAmbientLightSensorReading::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK28QmlAmbientLightSensorReading10metaObjectEv(
    const QmlAmbientLightSensorReading *self) {
  return self->metaObject();
}

//  QString QmlAmbientLightSensorReading::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN28QmlAmbientLightSensorReading2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QmlAmbientLightSensorReading::tr(s, c, n));
}

//  void QmlAmbientLightSensorReading::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QmlAmbientLightSensorReading24qt_qmlMarker_uncreatableEv(
    QmlAmbientLightSensorReading *self) {
  self->qt_qmlMarker_uncreatable();
}

//  QmlAmbientLightSensorReading::QmlAmbientLightSensorReading(QAmbientLightS
//      ensor *sensor)
extern "C" Q_DECL_EXPORT
QmlAmbientLightSensorReading *ritual_ZN28QmlAmbientLightSensorReadingC1EP19QAmbientLightSensor(
    QAmbientLightSensor *sensor) {
  return new CuteQmlAmbientLightSensorReading(sensor);
}

//  QmlAmbientLightSensorReading::~QmlAmbientLightSensorReading()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QmlAmbientLightSensorReadingD1Ev(
    QmlAmbientLightSensorReading *self) {
  delete self;
}

//  QAmbientLightReading::LightLevel
//      QmlAmbientLightSensorReading::lightLevel() const
extern "C" Q_DECL_EXPORT
QAmbientLightReading::LightLevel ritual_ZNK28QmlAmbientLightSensorReading10lightLevelEv(
    const QmlAmbientLightSensorReading *self) {
  return self->lightLevel();
}

//  QSensorReading *QmlAmbientLightSensorReading::reading() const
extern "C" Q_DECL_EXPORT
QSensorReading *ritual_ZNK28QmlAmbientLightSensorReading7readingEv(
    const QmlAmbientLightSensorReading *self) {
  return self->reading();
}

//  void QmlAmbientLightSensorReading::readingUpdate()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QmlAmbientLightSensorReading13readingUpdateEv(
    QmlAmbientLightSensorReading *self) {
  self->readingUpdate();
}

//  a Python function taken by a CuteQmlAmbientLightSensorReading, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QmlAmbientLightSensorReading(
    QmlAmbientLightSensorReading *self,
    const char *key,
    void *call) {
  return static_cast<CuteQmlAmbientLightSensorReading *>(self)->take(key, call);
}

//  QSensorReading *QmlAmbientLightSensorReading::reading() const
extern "C" Q_DECL_EXPORT
QSensorReading *ritual_own_ZNK28QmlAmbientLightSensorReading7readingEv(
    const QmlAmbientLightSensorReading *self) {
  return self->QmlAmbientLightSensorReading::reading();
}

//  void QmlAmbientLightSensorReading::readingUpdate()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN28QmlAmbientLightSensorReading13readingUpdateEv(
    QmlAmbientLightSensorReading *self) {
  self->QmlAmbientLightSensorReading::readingUpdate();
}
