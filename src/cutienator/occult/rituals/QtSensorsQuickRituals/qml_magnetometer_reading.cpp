//  Written by dev_tooling.RitualGenerator from the records of
//  QtSensorsQuick/6.12.0/QtSensorsQuick/private/qmlmagnetometer_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtSensorsQuick/6.12.0/QtSensorsQuick/private/qsensorsquickglobal_p.h>
#include <QtSensorsQuick/QtSensorsQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSensorsQuick/6.12.0/QtSensorsQuick/private/qmlmagnetometer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QmlMagnetometerReading that Python can take functions over in. Every QmlMagnetometerReading
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQmlMagnetometerReadingCall0)(const void *, int *);
typedef void (*CuteQmlMagnetometerReadingCall1)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQmlMagnetometerReadingCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQmlMagnetometerReadingCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQmlMagnetometerReadingCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQmlMagnetometerReadingCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQmlMagnetometerReadingCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQmlMagnetometerReadingCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQmlMagnetometerReadingCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQmlMagnetometerReading : public QmlMagnetometerReading {
public:
  using QmlMagnetometerReading::QmlMagnetometerReading;
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

  //  QSensorReading *QmlMagnetometerReading::reading() const
  QSensorReading *reading() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQmlMagnetometerReadingCall0 call = reinterpret_cast<CuteQmlMagnetometerReadingCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSensorReading *>(given);
    }
    return QmlMagnetometerReading::reading();
  }

  //  void QmlMagnetometerReading::readingUpdate()
  void readingUpdate() override {
    if (taken[1]) {
      int handled = 0;
      CuteQmlMagnetometerReadingCall1 call = reinterpret_cast<CuteQmlMagnetometerReadingCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QmlMagnetometerReading::readingUpdate();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQmlMagnetometerReadingCall2 call = reinterpret_cast<CuteQmlMagnetometerReadingCall2>(taken[2]);
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
      CuteQmlMagnetometerReadingCall3 call = reinterpret_cast<CuteQmlMagnetometerReadingCall3>(taken[3]);
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
      CuteQmlMagnetometerReadingCall4 call = reinterpret_cast<CuteQmlMagnetometerReadingCall4>(taken[4]);
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
      CuteQmlMagnetometerReadingCall5 call = reinterpret_cast<CuteQmlMagnetometerReadingCall5>(taken[5]);
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
      CuteQmlMagnetometerReadingCall6 call = reinterpret_cast<CuteQmlMagnetometerReadingCall6>(taken[6]);
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
      CuteQmlMagnetometerReadingCall7 call = reinterpret_cast<CuteQmlMagnetometerReadingCall7>(taken[7]);
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
      CuteQmlMagnetometerReadingCall8 call = reinterpret_cast<CuteQmlMagnetometerReadingCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QmlMagnetometerReading::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK22QmlMagnetometerReading10metaObjectEv(
    const QmlMagnetometerReading *self) {
  return self->metaObject();
}

//  QString QmlMagnetometerReading::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN22QmlMagnetometerReading2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QmlMagnetometerReading::tr(s, c, n));
}

//  void QmlMagnetometerReading::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QmlMagnetometerReading24qt_qmlMarker_uncreatableEv(
    QmlMagnetometerReading *self) {
  self->qt_qmlMarker_uncreatable();
}

//  QmlMagnetometerReading::QmlMagnetometerReading(QMagnetometer *sensor)
extern "C" Q_DECL_EXPORT
QmlMagnetometerReading *ritual_ZN22QmlMagnetometerReadingC1EP13QMagnetometer(
    QMagnetometer *sensor) {
  return new CuteQmlMagnetometerReading(sensor);
}

//  QmlMagnetometerReading::~QmlMagnetometerReading()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QmlMagnetometerReadingD1Ev(QmlMagnetometerReading *self) {
  delete self;
}

//  qreal QmlMagnetometerReading::x() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK22QmlMagnetometerReading1xEv(
    const QmlMagnetometerReading *self) {
  return self->x();
}

//  qreal QmlMagnetometerReading::y() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK22QmlMagnetometerReading1yEv(
    const QmlMagnetometerReading *self) {
  return self->y();
}

//  qreal QmlMagnetometerReading::z() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK22QmlMagnetometerReading1zEv(
    const QmlMagnetometerReading *self) {
  return self->z();
}

//  qreal QmlMagnetometerReading::calibrationLevel() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK22QmlMagnetometerReading16calibrationLevelEv(
    const QmlMagnetometerReading *self) {
  return self->calibrationLevel();
}

//  QSensorReading *QmlMagnetometerReading::reading() const
extern "C" Q_DECL_EXPORT
QSensorReading *ritual_ZNK22QmlMagnetometerReading7readingEv(
    const QmlMagnetometerReading *self) {
  return self->reading();
}

//  void QmlMagnetometerReading::readingUpdate()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QmlMagnetometerReading13readingUpdateEv(
    QmlMagnetometerReading *self) {
  self->readingUpdate();
}

//  a Python function taken by a CuteQmlMagnetometerReading, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QmlMagnetometerReading(
    QmlMagnetometerReading *self,
    const char *key,
    void *call) {
  return static_cast<CuteQmlMagnetometerReading *>(self)->take(key, call);
}

//  QSensorReading *QmlMagnetometerReading::reading() const
extern "C" Q_DECL_EXPORT
QSensorReading *ritual_own_ZNK22QmlMagnetometerReading7readingEv(
    const QmlMagnetometerReading *self) {
  return self->QmlMagnetometerReading::reading();
}

//  void QmlMagnetometerReading::readingUpdate()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QmlMagnetometerReading13readingUpdateEv(
    QmlMagnetometerReading *self) {
  self->QmlMagnetometerReading::readingUpdate();
}
