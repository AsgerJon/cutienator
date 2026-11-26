//  Written by dev_tooling.RitualGenerator from the records of
//  QtSensorsQuick/6.12.0/QtSensorsQuick/private/qmlproximitysensor_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtSensorsQuick/6.12.0/QtSensorsQuick/private/qsensorsquickglobal_p.h>
#include <QtSensorsQuick/QtSensorsQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSensorsQuick/6.12.0/QtSensorsQuick/private/qmlproximitysensor_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#include <QtCore/QBindable>

//  A QmlProximitySensorReading that Python can take functions over in. Every QmlProximitySensorReading
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQmlProximitySensorReadingCall0)(const void *, int *);
typedef void (*CuteQmlProximitySensorReadingCall1)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQmlProximitySensorReadingCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQmlProximitySensorReadingCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQmlProximitySensorReadingCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQmlProximitySensorReadingCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQmlProximitySensorReadingCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQmlProximitySensorReadingCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQmlProximitySensorReadingCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQmlProximitySensorReading : public QmlProximitySensorReading {
public:
  using QmlProximitySensorReading::QmlProximitySensorReading;
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

  //  QSensorReading *QmlProximitySensorReading::reading() const
  QSensorReading *reading() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQmlProximitySensorReadingCall0 call = reinterpret_cast<CuteQmlProximitySensorReadingCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSensorReading *>(given);
    }
    return QmlProximitySensorReading::reading();
  }

  //  void QmlProximitySensorReading::readingUpdate()
  void readingUpdate() override {
    if (taken[1]) {
      int handled = 0;
      CuteQmlProximitySensorReadingCall1 call = reinterpret_cast<CuteQmlProximitySensorReadingCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QmlProximitySensorReading::readingUpdate();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQmlProximitySensorReadingCall2 call = reinterpret_cast<CuteQmlProximitySensorReadingCall2>(taken[2]);
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
      CuteQmlProximitySensorReadingCall3 call = reinterpret_cast<CuteQmlProximitySensorReadingCall3>(taken[3]);
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
      CuteQmlProximitySensorReadingCall4 call = reinterpret_cast<CuteQmlProximitySensorReadingCall4>(taken[4]);
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
      CuteQmlProximitySensorReadingCall5 call = reinterpret_cast<CuteQmlProximitySensorReadingCall5>(taken[5]);
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
      CuteQmlProximitySensorReadingCall6 call = reinterpret_cast<CuteQmlProximitySensorReadingCall6>(taken[6]);
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
      CuteQmlProximitySensorReadingCall7 call = reinterpret_cast<CuteQmlProximitySensorReadingCall7>(taken[7]);
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
      CuteQmlProximitySensorReadingCall8 call = reinterpret_cast<CuteQmlProximitySensorReadingCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QmlProximitySensorReading::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK25QmlProximitySensorReading10metaObjectEv(
    const QmlProximitySensorReading *self) {
  return self->metaObject();
}

//  void *QmlProximitySensorReading::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN25QmlProximitySensorReading11qt_metacastEPKc(
    QmlProximitySensorReading *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QmlProximitySensorReading::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN25QmlProximitySensorReading11qt_metacallEN11QMetaObject4CallEiPPv(
    QmlProximitySensorReading *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QmlProximitySensorReading::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN25QmlProximitySensorReading2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QmlProximitySensorReading::tr(s, c, n));
}

//  void QmlProximitySensorReading::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QmlProximitySensorReading24qt_qmlMarker_uncreatableEv(
    QmlProximitySensorReading *self) {
  self->qt_qmlMarker_uncreatable();
}

//  QmlProximitySensorReading::QmlProximitySensorReading(QProximitySensor
//      *sensor)
extern "C" Q_DECL_EXPORT
QmlProximitySensorReading *ritual_ZN25QmlProximitySensorReadingC1EP16QProximitySensor(
    QProximitySensor *sensor) {
  return new CuteQmlProximitySensorReading(sensor);
}

//  QmlProximitySensorReading::~QmlProximitySensorReading()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QmlProximitySensorReadingD1Ev(
    QmlProximitySensorReading *self) {
  delete self;
}

//  bool QmlProximitySensorReading::near() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QmlProximitySensorReading4nearEv(
    const QmlProximitySensorReading *self) {
  return self->near();
}

//  QBindable<bool> QmlProximitySensorReading::bindableNear() const
extern "C" Q_DECL_EXPORT
QBindable<bool> *ritual_ZNK25QmlProximitySensorReading12bindableNearEv(
    const QmlProximitySensorReading *self) {
  return new QBindable<bool>(self->bindableNear());
}

//  void QmlProximitySensorReading::nearChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QmlProximitySensorReading11nearChangedEv(
    QmlProximitySensorReading *self) {
  self->nearChanged();
}

//  QSensorReading *QmlProximitySensorReading::reading() const
extern "C" Q_DECL_EXPORT
QSensorReading *ritual_ZNK25QmlProximitySensorReading7readingEv(
    const QmlProximitySensorReading *self) {
  return self->reading();
}

//  void QmlProximitySensorReading::readingUpdate()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QmlProximitySensorReading13readingUpdateEv(
    QmlProximitySensorReading *self) {
  self->readingUpdate();
}

//  size_t QmlProximitySensorReading::_qt_property_m_near_offset()
extern "C" Q_DECL_EXPORT
size_t ritual_ZN25QmlProximitySensorReading26_qt_property_m_near_offsetEv() {
  return QmlProximitySensorReading::_qt_property_m_near_offset();
}

//  a Python function taken by a CuteQmlProximitySensorReading, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QmlProximitySensorReading(
    QmlProximitySensorReading *self,
    const char *key,
    void *call) {
  return static_cast<CuteQmlProximitySensorReading *>(self)->take(key, call);
}

//  QSensorReading *QmlProximitySensorReading::reading() const
extern "C" Q_DECL_EXPORT
QSensorReading *ritual_own_ZNK25QmlProximitySensorReading7readingEv(
    const QmlProximitySensorReading *self) {
  return self->QmlProximitySensorReading::reading();
}

//  void QmlProximitySensorReading::readingUpdate()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN25QmlProximitySensorReading13readingUpdateEv(
    QmlProximitySensorReading *self) {
  self->QmlProximitySensorReading::readingUpdate();
}

//  a QBindable<bool> a ritual of QmlProximitySensorReading gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QmlProximitySensorReading__QBindable_bool(
    QBindable<bool> *self) {
  delete self;
}
