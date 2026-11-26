//  Written by dev_tooling.RitualGenerator from the records of
//  QtSensorsQuick/6.12.0/QtSensorsQuick/private/qmlcompass_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtSensorsQuick/6.12.0/QtSensorsQuick/private/qsensorsquickglobal_p.h>
#include <QtSensorsQuick/QtSensorsQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSensorsQuick/6.12.0/QtSensorsQuick/private/qmlcompass_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#include <QtCore/QBindable>

//  A QmlCompassReading that Python can take functions over in. Every QmlCompassReading
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQmlCompassReadingCall0)(const void *, int *);
typedef void (*CuteQmlCompassReadingCall1)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQmlCompassReadingCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQmlCompassReadingCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQmlCompassReadingCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQmlCompassReadingCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQmlCompassReadingCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQmlCompassReadingCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQmlCompassReadingCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQmlCompassReading : public QmlCompassReading {
public:
  using QmlCompassReading::QmlCompassReading;
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

  //  QSensorReading *QmlCompassReading::reading() const
  QSensorReading *reading() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQmlCompassReadingCall0 call = reinterpret_cast<CuteQmlCompassReadingCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSensorReading *>(given);
    }
    return QmlCompassReading::reading();
  }

  //  void QmlCompassReading::readingUpdate()
  void readingUpdate() override {
    if (taken[1]) {
      int handled = 0;
      CuteQmlCompassReadingCall1 call = reinterpret_cast<CuteQmlCompassReadingCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QmlCompassReading::readingUpdate();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQmlCompassReadingCall2 call = reinterpret_cast<CuteQmlCompassReadingCall2>(taken[2]);
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
      CuteQmlCompassReadingCall3 call = reinterpret_cast<CuteQmlCompassReadingCall3>(taken[3]);
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
      CuteQmlCompassReadingCall4 call = reinterpret_cast<CuteQmlCompassReadingCall4>(taken[4]);
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
      CuteQmlCompassReadingCall5 call = reinterpret_cast<CuteQmlCompassReadingCall5>(taken[5]);
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
      CuteQmlCompassReadingCall6 call = reinterpret_cast<CuteQmlCompassReadingCall6>(taken[6]);
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
      CuteQmlCompassReadingCall7 call = reinterpret_cast<CuteQmlCompassReadingCall7>(taken[7]);
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
      CuteQmlCompassReadingCall8 call = reinterpret_cast<CuteQmlCompassReadingCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QmlCompassReading::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QmlCompassReading10metaObjectEv(
    const QmlCompassReading *self) {
  return self->metaObject();
}

//  void *QmlCompassReading::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN17QmlCompassReading11qt_metacastEPKc(
    QmlCompassReading *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QmlCompassReading::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN17QmlCompassReading11qt_metacallEN11QMetaObject4CallEiPPv(
    QmlCompassReading *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QmlCompassReading::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QmlCompassReading2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QmlCompassReading::tr(s, c, n));
}

//  void QmlCompassReading::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QmlCompassReading24qt_qmlMarker_uncreatableEv(
    QmlCompassReading *self) {
  self->qt_qmlMarker_uncreatable();
}

//  QmlCompassReading::QmlCompassReading(QCompass *sensor)
extern "C" Q_DECL_EXPORT
QmlCompassReading *ritual_ZN17QmlCompassReadingC1EP8QCompass(
    QCompass *sensor) {
  return new CuteQmlCompassReading(sensor);
}

//  QmlCompassReading::~QmlCompassReading()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QmlCompassReadingD1Ev(QmlCompassReading *self) {
  delete self;
}

//  qreal QmlCompassReading::azimuth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK17QmlCompassReading7azimuthEv(
    const QmlCompassReading *self) {
  return self->azimuth();
}

//  QBindable<qreal> QmlCompassReading::bindableAzimuth() const
extern "C" Q_DECL_EXPORT
QBindable<qreal> *ritual_ZNK17QmlCompassReading15bindableAzimuthEv(
    const QmlCompassReading *self) {
  return new QBindable<qreal>(self->bindableAzimuth());
}

//  qreal QmlCompassReading::calibrationLevel() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK17QmlCompassReading16calibrationLevelEv(
    const QmlCompassReading *self) {
  return self->calibrationLevel();
}

//  QBindable<qreal> QmlCompassReading::bindableCalibrationLevel() const
extern "C" Q_DECL_EXPORT
QBindable<qreal> *ritual_ZNK17QmlCompassReading24bindableCalibrationLevelEv(
    const QmlCompassReading *self) {
  return new QBindable<qreal>(self->bindableCalibrationLevel());
}

//  void QmlCompassReading::azimuthChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QmlCompassReading14azimuthChangedEv(
    QmlCompassReading *self) {
  self->azimuthChanged();
}

//  void QmlCompassReading::calibrationLevelChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QmlCompassReading23calibrationLevelChangedEv(
    QmlCompassReading *self) {
  self->calibrationLevelChanged();
}

//  QSensorReading *QmlCompassReading::reading() const
extern "C" Q_DECL_EXPORT
QSensorReading *ritual_ZNK17QmlCompassReading7readingEv(
    const QmlCompassReading *self) {
  return self->reading();
}

//  void QmlCompassReading::readingUpdate()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QmlCompassReading13readingUpdateEv(QmlCompassReading *self) {
  self->readingUpdate();
}

//  size_t QmlCompassReading::_qt_property_m_azimuth_offset()
extern "C" Q_DECL_EXPORT
size_t ritual_ZN17QmlCompassReading29_qt_property_m_azimuth_offsetEv() {
  return QmlCompassReading::_qt_property_m_azimuth_offset();
}

//  size_t QmlCompassReading::_qt_property_m_calibrationLevel_offset()
extern "C" Q_DECL_EXPORT
size_t ritual_ZN17QmlCompassReading38_qt_property_m_calibrationLevel_offsetEv() {
  return QmlCompassReading::_qt_property_m_calibrationLevel_offset();
}

//  a Python function taken by a CuteQmlCompassReading, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QmlCompassReading(
    QmlCompassReading *self,
    const char *key,
    void *call) {
  return static_cast<CuteQmlCompassReading *>(self)->take(key, call);
}

//  QSensorReading *QmlCompassReading::reading() const
extern "C" Q_DECL_EXPORT
QSensorReading *ritual_own_ZNK17QmlCompassReading7readingEv(
    const QmlCompassReading *self) {
  return self->QmlCompassReading::reading();
}

//  void QmlCompassReading::readingUpdate()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QmlCompassReading13readingUpdateEv(
    QmlCompassReading *self) {
  self->QmlCompassReading::readingUpdate();
}

//  a QBindable<qreal> a ritual of QmlCompassReading gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QmlCompassReading__QBindable_qreal(QBindable<qreal> *self) {
  delete self;
}
