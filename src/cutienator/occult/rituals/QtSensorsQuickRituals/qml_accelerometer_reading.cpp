//  Written by dev_tooling.RitualGenerator from the records of
//  QtSensorsQuick/6.12.0/QtSensorsQuick/private/qmlaccelerometer_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtSensorsQuick/6.12.0/QtSensorsQuick/private/qsensorsquickglobal_p.h>
#include <QtSensorsQuick/QtSensorsQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSensorsQuick/6.12.0/QtSensorsQuick/private/qmlaccelerometer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QmlAccelerometerReading that Python can take functions over in. Every QmlAccelerometerReading
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQmlAccelerometerReadingCall0)(const void *, int *);
typedef void (*CuteQmlAccelerometerReadingCall1)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQmlAccelerometerReadingCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQmlAccelerometerReadingCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQmlAccelerometerReadingCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQmlAccelerometerReadingCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQmlAccelerometerReadingCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQmlAccelerometerReadingCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQmlAccelerometerReadingCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQmlAccelerometerReading : public QmlAccelerometerReading {
public:
  using QmlAccelerometerReading::QmlAccelerometerReading;
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

  //  QSensorReading *QmlAccelerometerReading::reading() const
  QSensorReading *reading() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQmlAccelerometerReadingCall0 call = reinterpret_cast<CuteQmlAccelerometerReadingCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSensorReading *>(given);
    }
    return QmlAccelerometerReading::reading();
  }

  //  void QmlAccelerometerReading::readingUpdate()
  void readingUpdate() override {
    if (taken[1]) {
      int handled = 0;
      CuteQmlAccelerometerReadingCall1 call = reinterpret_cast<CuteQmlAccelerometerReadingCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QmlAccelerometerReading::readingUpdate();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQmlAccelerometerReadingCall2 call = reinterpret_cast<CuteQmlAccelerometerReadingCall2>(taken[2]);
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
      CuteQmlAccelerometerReadingCall3 call = reinterpret_cast<CuteQmlAccelerometerReadingCall3>(taken[3]);
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
      CuteQmlAccelerometerReadingCall4 call = reinterpret_cast<CuteQmlAccelerometerReadingCall4>(taken[4]);
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
      CuteQmlAccelerometerReadingCall5 call = reinterpret_cast<CuteQmlAccelerometerReadingCall5>(taken[5]);
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
      CuteQmlAccelerometerReadingCall6 call = reinterpret_cast<CuteQmlAccelerometerReadingCall6>(taken[6]);
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
      CuteQmlAccelerometerReadingCall7 call = reinterpret_cast<CuteQmlAccelerometerReadingCall7>(taken[7]);
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
      CuteQmlAccelerometerReadingCall8 call = reinterpret_cast<CuteQmlAccelerometerReadingCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QmlAccelerometerReading::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK23QmlAccelerometerReading10metaObjectEv(
    const QmlAccelerometerReading *self) {
  return self->metaObject();
}

//  QString QmlAccelerometerReading::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN23QmlAccelerometerReading2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QmlAccelerometerReading::tr(s, c, n));
}

//  void QmlAccelerometerReading::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QmlAccelerometerReading24qt_qmlMarker_uncreatableEv(
    QmlAccelerometerReading *self) {
  self->qt_qmlMarker_uncreatable();
}

//  QmlAccelerometerReading::QmlAccelerometerReading(QAccelerometer *sensor)
extern "C" Q_DECL_EXPORT
QmlAccelerometerReading *ritual_ZN23QmlAccelerometerReadingC1EP14QAccelerometer(
    QAccelerometer *sensor) {
  return new CuteQmlAccelerometerReading(sensor);
}

//  QmlAccelerometerReading::~QmlAccelerometerReading()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QmlAccelerometerReadingD1Ev(QmlAccelerometerReading *self) {
  delete self;
}

//  qreal QmlAccelerometerReading::x() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK23QmlAccelerometerReading1xEv(
    const QmlAccelerometerReading *self) {
  return self->x();
}

//  qreal QmlAccelerometerReading::y() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK23QmlAccelerometerReading1yEv(
    const QmlAccelerometerReading *self) {
  return self->y();
}

//  qreal QmlAccelerometerReading::z() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK23QmlAccelerometerReading1zEv(
    const QmlAccelerometerReading *self) {
  return self->z();
}

//  QSensorReading *QmlAccelerometerReading::reading() const
extern "C" Q_DECL_EXPORT
QSensorReading *ritual_ZNK23QmlAccelerometerReading7readingEv(
    const QmlAccelerometerReading *self) {
  return self->reading();
}

//  void QmlAccelerometerReading::readingUpdate()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QmlAccelerometerReading13readingUpdateEv(
    QmlAccelerometerReading *self) {
  self->readingUpdate();
}

//  a Python function taken by a CuteQmlAccelerometerReading, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QmlAccelerometerReading(
    QmlAccelerometerReading *self,
    const char *key,
    void *call) {
  return static_cast<CuteQmlAccelerometerReading *>(self)->take(key, call);
}

//  QSensorReading *QmlAccelerometerReading::reading() const
extern "C" Q_DECL_EXPORT
QSensorReading *ritual_own_ZNK23QmlAccelerometerReading7readingEv(
    const QmlAccelerometerReading *self) {
  return self->QmlAccelerometerReading::reading();
}

//  void QmlAccelerometerReading::readingUpdate()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QmlAccelerometerReading13readingUpdateEv(
    QmlAccelerometerReading *self) {
  self->QmlAccelerometerReading::readingUpdate();
}
