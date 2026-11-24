//  Written by dev_tooling.RitualGenerator from the records of
//  QtSensorsQuick/6.12.0/QtSensorsQuick/private/qmlrotationsensor_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtSensorsQuick/6.12.0/QtSensorsQuick/private/qsensorsquickglobal_p.h>
#include <QtSensorsQuick/QtSensorsQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSensorsQuick/6.12.0/QtSensorsQuick/private/qmlrotationsensor_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QmlRotationSensorReading that Python can take functions over in. Every QmlRotationSensorReading
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQmlRotationSensorReadingCall0)(const void *, int *);
typedef void (*CuteQmlRotationSensorReadingCall1)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQmlRotationSensorReadingCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQmlRotationSensorReadingCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQmlRotationSensorReadingCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQmlRotationSensorReadingCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQmlRotationSensorReadingCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQmlRotationSensorReadingCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQmlRotationSensorReadingCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQmlRotationSensorReading : public QmlRotationSensorReading {
public:
  using QmlRotationSensorReading::QmlRotationSensorReading;
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

  //  QSensorReading *QmlRotationSensorReading::reading() const
  QSensorReading *reading() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQmlRotationSensorReadingCall0 call = reinterpret_cast<CuteQmlRotationSensorReadingCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSensorReading *>(given);
    }
    return QmlRotationSensorReading::reading();
  }

  //  void QmlRotationSensorReading::readingUpdate()
  void readingUpdate() override {
    if (taken[1]) {
      int handled = 0;
      CuteQmlRotationSensorReadingCall1 call = reinterpret_cast<CuteQmlRotationSensorReadingCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QmlRotationSensorReading::readingUpdate();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQmlRotationSensorReadingCall2 call = reinterpret_cast<CuteQmlRotationSensorReadingCall2>(taken[2]);
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
      CuteQmlRotationSensorReadingCall3 call = reinterpret_cast<CuteQmlRotationSensorReadingCall3>(taken[3]);
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
      CuteQmlRotationSensorReadingCall4 call = reinterpret_cast<CuteQmlRotationSensorReadingCall4>(taken[4]);
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
      CuteQmlRotationSensorReadingCall5 call = reinterpret_cast<CuteQmlRotationSensorReadingCall5>(taken[5]);
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
      CuteQmlRotationSensorReadingCall6 call = reinterpret_cast<CuteQmlRotationSensorReadingCall6>(taken[6]);
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
      CuteQmlRotationSensorReadingCall7 call = reinterpret_cast<CuteQmlRotationSensorReadingCall7>(taken[7]);
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
      CuteQmlRotationSensorReadingCall8 call = reinterpret_cast<CuteQmlRotationSensorReadingCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QmlRotationSensorReading::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK24QmlRotationSensorReading10metaObjectEv(
    const QmlRotationSensorReading *self) {
  return self->metaObject();
}

//  QString QmlRotationSensorReading::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN24QmlRotationSensorReading2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QmlRotationSensorReading::tr(s, c, n));
}

//  void QmlRotationSensorReading::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QmlRotationSensorReading24qt_qmlMarker_uncreatableEv(
    QmlRotationSensorReading *self) {
  self->qt_qmlMarker_uncreatable();
}

//  QmlRotationSensorReading::QmlRotationSensorReading(QRotationSensor
//      *sensor)
extern "C" Q_DECL_EXPORT
QmlRotationSensorReading *ritual_ZN24QmlRotationSensorReadingC1EP15QRotationSensor(
    QRotationSensor *sensor) {
  return new CuteQmlRotationSensorReading(sensor);
}

//  QmlRotationSensorReading::~QmlRotationSensorReading()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QmlRotationSensorReadingD1Ev(
    QmlRotationSensorReading *self) {
  delete self;
}

//  qreal QmlRotationSensorReading::x() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK24QmlRotationSensorReading1xEv(
    const QmlRotationSensorReading *self) {
  return self->x();
}

//  qreal QmlRotationSensorReading::y() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK24QmlRotationSensorReading1yEv(
    const QmlRotationSensorReading *self) {
  return self->y();
}

//  qreal QmlRotationSensorReading::z() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK24QmlRotationSensorReading1zEv(
    const QmlRotationSensorReading *self) {
  return self->z();
}

//  QSensorReading *QmlRotationSensorReading::reading() const
extern "C" Q_DECL_EXPORT
QSensorReading *ritual_ZNK24QmlRotationSensorReading7readingEv(
    const QmlRotationSensorReading *self) {
  return self->reading();
}

//  void QmlRotationSensorReading::readingUpdate()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QmlRotationSensorReading13readingUpdateEv(
    QmlRotationSensorReading *self) {
  self->readingUpdate();
}

//  a Python function taken by a CuteQmlRotationSensorReading, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QmlRotationSensorReading(
    QmlRotationSensorReading *self,
    const char *key,
    void *call) {
  return static_cast<CuteQmlRotationSensorReading *>(self)->take(key, call);
}

//  QSensorReading *QmlRotationSensorReading::reading() const
extern "C" Q_DECL_EXPORT
QSensorReading *ritual_own_ZNK24QmlRotationSensorReading7readingEv(
    const QmlRotationSensorReading *self) {
  return self->QmlRotationSensorReading::reading();
}

//  void QmlRotationSensorReading::readingUpdate()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QmlRotationSensorReading13readingUpdateEv(
    QmlRotationSensorReading *self) {
  self->QmlRotationSensorReading::readingUpdate();
}
