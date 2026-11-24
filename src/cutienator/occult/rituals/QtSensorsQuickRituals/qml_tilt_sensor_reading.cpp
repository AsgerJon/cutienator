//  Written by dev_tooling.RitualGenerator from the records of
//  QtSensorsQuick/6.12.0/QtSensorsQuick/private/qmltiltsensor_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtSensorsQuick/6.12.0/QtSensorsQuick/private/qsensorsquickglobal_p.h>
#include <QtSensorsQuick/QtSensorsQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSensorsQuick/6.12.0/QtSensorsQuick/private/qmltiltsensor_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QmlTiltSensorReading that Python can take functions over in. Every QmlTiltSensorReading
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQmlTiltSensorReadingCall0)(const void *, int *);
typedef void (*CuteQmlTiltSensorReadingCall1)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQmlTiltSensorReadingCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQmlTiltSensorReadingCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQmlTiltSensorReadingCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQmlTiltSensorReadingCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQmlTiltSensorReadingCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQmlTiltSensorReadingCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQmlTiltSensorReadingCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQmlTiltSensorReading : public QmlTiltSensorReading {
public:
  using QmlTiltSensorReading::QmlTiltSensorReading;
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

  //  QSensorReading *QmlTiltSensorReading::reading() const
  QSensorReading *reading() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQmlTiltSensorReadingCall0 call = reinterpret_cast<CuteQmlTiltSensorReadingCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSensorReading *>(given);
    }
    return QmlTiltSensorReading::reading();
  }

  //  void QmlTiltSensorReading::readingUpdate()
  void readingUpdate() override {
    if (taken[1]) {
      int handled = 0;
      CuteQmlTiltSensorReadingCall1 call = reinterpret_cast<CuteQmlTiltSensorReadingCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QmlTiltSensorReading::readingUpdate();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQmlTiltSensorReadingCall2 call = reinterpret_cast<CuteQmlTiltSensorReadingCall2>(taken[2]);
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
      CuteQmlTiltSensorReadingCall3 call = reinterpret_cast<CuteQmlTiltSensorReadingCall3>(taken[3]);
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
      CuteQmlTiltSensorReadingCall4 call = reinterpret_cast<CuteQmlTiltSensorReadingCall4>(taken[4]);
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
      CuteQmlTiltSensorReadingCall5 call = reinterpret_cast<CuteQmlTiltSensorReadingCall5>(taken[5]);
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
      CuteQmlTiltSensorReadingCall6 call = reinterpret_cast<CuteQmlTiltSensorReadingCall6>(taken[6]);
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
      CuteQmlTiltSensorReadingCall7 call = reinterpret_cast<CuteQmlTiltSensorReadingCall7>(taken[7]);
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
      CuteQmlTiltSensorReadingCall8 call = reinterpret_cast<CuteQmlTiltSensorReadingCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QmlTiltSensorReading::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20QmlTiltSensorReading10metaObjectEv(
    const QmlTiltSensorReading *self) {
  return self->metaObject();
}

//  QString QmlTiltSensorReading::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN20QmlTiltSensorReading2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QmlTiltSensorReading::tr(s, c, n));
}

//  void QmlTiltSensorReading::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QmlTiltSensorReading24qt_qmlMarker_uncreatableEv(
    QmlTiltSensorReading *self) {
  self->qt_qmlMarker_uncreatable();
}

//  QmlTiltSensorReading::QmlTiltSensorReading(QTiltSensor *sensor)
extern "C" Q_DECL_EXPORT
QmlTiltSensorReading *ritual_ZN20QmlTiltSensorReadingC1EP11QTiltSensor(
    QTiltSensor *sensor) {
  return new CuteQmlTiltSensorReading(sensor);
}

//  QmlTiltSensorReading::~QmlTiltSensorReading()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QmlTiltSensorReadingD1Ev(QmlTiltSensorReading *self) {
  delete self;
}

//  qreal QmlTiltSensorReading::yRotation() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK20QmlTiltSensorReading9yRotationEv(
    const QmlTiltSensorReading *self) {
  return self->yRotation();
}

//  qreal QmlTiltSensorReading::xRotation() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK20QmlTiltSensorReading9xRotationEv(
    const QmlTiltSensorReading *self) {
  return self->xRotation();
}

//  QSensorReading *QmlTiltSensorReading::reading() const
extern "C" Q_DECL_EXPORT
QSensorReading *ritual_ZNK20QmlTiltSensorReading7readingEv(
    const QmlTiltSensorReading *self) {
  return self->reading();
}

//  void QmlTiltSensorReading::readingUpdate()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QmlTiltSensorReading13readingUpdateEv(
    QmlTiltSensorReading *self) {
  self->readingUpdate();
}

//  a Python function taken by a CuteQmlTiltSensorReading, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QmlTiltSensorReading(
    QmlTiltSensorReading *self,
    const char *key,
    void *call) {
  return static_cast<CuteQmlTiltSensorReading *>(self)->take(key, call);
}

//  QSensorReading *QmlTiltSensorReading::reading() const
extern "C" Q_DECL_EXPORT
QSensorReading *ritual_own_ZNK20QmlTiltSensorReading7readingEv(
    const QmlTiltSensorReading *self) {
  return self->QmlTiltSensorReading::reading();
}

//  void QmlTiltSensorReading::readingUpdate()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QmlTiltSensorReading13readingUpdateEv(
    QmlTiltSensorReading *self) {
  self->QmlTiltSensorReading::readingUpdate();
}
