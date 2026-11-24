//  Written by dev_tooling.RitualGenerator from the records of
//  QtSensorsQuick/6.12.0/QtSensorsQuick/private/qmlirproximitysensor_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtSensorsQuick/6.12.0/QtSensorsQuick/private/qsensorsquickglobal_p.h>
#include <QtSensorsQuick/QtSensorsQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSensorsQuick/6.12.0/QtSensorsQuick/private/qmlirproximitysensor_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QmlIRProximitySensorReading that Python can take functions over in. Every QmlIRProximitySensorReading
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQmlIRProximitySensorReadingCall0)(const void *, int *);
typedef void (*CuteQmlIRProximitySensorReadingCall1)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQmlIRProximitySensorReadingCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQmlIRProximitySensorReadingCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQmlIRProximitySensorReadingCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQmlIRProximitySensorReadingCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQmlIRProximitySensorReadingCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQmlIRProximitySensorReadingCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQmlIRProximitySensorReadingCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQmlIRProximitySensorReading : public QmlIRProximitySensorReading {
public:
  using QmlIRProximitySensorReading::QmlIRProximitySensorReading;
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

  //  QSensorReading *QmlIRProximitySensorReading::reading() const
  QSensorReading *reading() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQmlIRProximitySensorReadingCall0 call = reinterpret_cast<CuteQmlIRProximitySensorReadingCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSensorReading *>(given);
    }
    return QmlIRProximitySensorReading::reading();
  }

  //  void QmlIRProximitySensorReading::readingUpdate()
  void readingUpdate() override {
    if (taken[1]) {
      int handled = 0;
      CuteQmlIRProximitySensorReadingCall1 call = reinterpret_cast<CuteQmlIRProximitySensorReadingCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QmlIRProximitySensorReading::readingUpdate();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQmlIRProximitySensorReadingCall2 call = reinterpret_cast<CuteQmlIRProximitySensorReadingCall2>(taken[2]);
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
      CuteQmlIRProximitySensorReadingCall3 call = reinterpret_cast<CuteQmlIRProximitySensorReadingCall3>(taken[3]);
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
      CuteQmlIRProximitySensorReadingCall4 call = reinterpret_cast<CuteQmlIRProximitySensorReadingCall4>(taken[4]);
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
      CuteQmlIRProximitySensorReadingCall5 call = reinterpret_cast<CuteQmlIRProximitySensorReadingCall5>(taken[5]);
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
      CuteQmlIRProximitySensorReadingCall6 call = reinterpret_cast<CuteQmlIRProximitySensorReadingCall6>(taken[6]);
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
      CuteQmlIRProximitySensorReadingCall7 call = reinterpret_cast<CuteQmlIRProximitySensorReadingCall7>(taken[7]);
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
      CuteQmlIRProximitySensorReadingCall8 call = reinterpret_cast<CuteQmlIRProximitySensorReadingCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QmlIRProximitySensorReading::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK27QmlIRProximitySensorReading10metaObjectEv(
    const QmlIRProximitySensorReading *self) {
  return self->metaObject();
}

//  QString QmlIRProximitySensorReading::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN27QmlIRProximitySensorReading2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QmlIRProximitySensorReading::tr(s, c, n));
}

//  void QmlIRProximitySensorReading::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QmlIRProximitySensorReading24qt_qmlMarker_uncreatableEv(
    QmlIRProximitySensorReading *self) {
  self->qt_qmlMarker_uncreatable();
}

//  QmlIRProximitySensorReading::QmlIRProximitySensorReading(QIRProximitySens
//      or *sensor)
extern "C" Q_DECL_EXPORT
QmlIRProximitySensorReading *ritual_ZN27QmlIRProximitySensorReadingC1EP18QIRProximitySensor(
    QIRProximitySensor *sensor) {
  return new CuteQmlIRProximitySensorReading(sensor);
}

//  QmlIRProximitySensorReading::~QmlIRProximitySensorReading()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QmlIRProximitySensorReadingD1Ev(
    QmlIRProximitySensorReading *self) {
  delete self;
}

//  qreal QmlIRProximitySensorReading::reflectance() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK27QmlIRProximitySensorReading11reflectanceEv(
    const QmlIRProximitySensorReading *self) {
  return self->reflectance();
}

//  QSensorReading *QmlIRProximitySensorReading::reading() const
extern "C" Q_DECL_EXPORT
QSensorReading *ritual_ZNK27QmlIRProximitySensorReading7readingEv(
    const QmlIRProximitySensorReading *self) {
  return self->reading();
}

//  void QmlIRProximitySensorReading::readingUpdate()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QmlIRProximitySensorReading13readingUpdateEv(
    QmlIRProximitySensorReading *self) {
  self->readingUpdate();
}

//  a Python function taken by a CuteQmlIRProximitySensorReading, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QmlIRProximitySensorReading(
    QmlIRProximitySensorReading *self,
    const char *key,
    void *call) {
  return static_cast<CuteQmlIRProximitySensorReading *>(self)->take(key, call);
}

//  QSensorReading *QmlIRProximitySensorReading::reading() const
extern "C" Q_DECL_EXPORT
QSensorReading *ritual_own_ZNK27QmlIRProximitySensorReading7readingEv(
    const QmlIRProximitySensorReading *self) {
  return self->QmlIRProximitySensorReading::reading();
}

//  void QmlIRProximitySensorReading::readingUpdate()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN27QmlIRProximitySensorReading13readingUpdateEv(
    QmlIRProximitySensorReading *self) {
  self->QmlIRProximitySensorReading::readingUpdate();
}
