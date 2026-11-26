//  Written by dev_tooling.RitualGenerator from the records of
//  QtSensorsQuick/6.12.0/QtSensorsQuick/private/qmlhumiditysensor_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtSensorsQuick/6.12.0/QtSensorsQuick/private/qsensorsquickglobal_p.h>
#include <QtSensorsQuick/QtSensorsQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSensorsQuick/6.12.0/QtSensorsQuick/private/qmlhumiditysensor_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#include <QtCore/QBindable>

//  A QmlHumidityReading that Python can take functions over in. Every QmlHumidityReading
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQmlHumidityReadingCall0)(const void *, int *);
typedef void (*CuteQmlHumidityReadingCall1)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQmlHumidityReadingCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQmlHumidityReadingCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQmlHumidityReadingCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQmlHumidityReadingCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQmlHumidityReadingCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQmlHumidityReadingCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQmlHumidityReadingCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQmlHumidityReading : public QmlHumidityReading {
public:
  using QmlHumidityReading::QmlHumidityReading;
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

  //  QSensorReading *QmlHumidityReading::reading() const
  QSensorReading *reading() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQmlHumidityReadingCall0 call = reinterpret_cast<CuteQmlHumidityReadingCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSensorReading *>(given);
    }
    return QmlHumidityReading::reading();
  }

  //  void QmlHumidityReading::readingUpdate()
  void readingUpdate() override {
    if (taken[1]) {
      int handled = 0;
      CuteQmlHumidityReadingCall1 call = reinterpret_cast<CuteQmlHumidityReadingCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QmlHumidityReading::readingUpdate();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQmlHumidityReadingCall2 call = reinterpret_cast<CuteQmlHumidityReadingCall2>(taken[2]);
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
      CuteQmlHumidityReadingCall3 call = reinterpret_cast<CuteQmlHumidityReadingCall3>(taken[3]);
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
      CuteQmlHumidityReadingCall4 call = reinterpret_cast<CuteQmlHumidityReadingCall4>(taken[4]);
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
      CuteQmlHumidityReadingCall5 call = reinterpret_cast<CuteQmlHumidityReadingCall5>(taken[5]);
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
      CuteQmlHumidityReadingCall6 call = reinterpret_cast<CuteQmlHumidityReadingCall6>(taken[6]);
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
      CuteQmlHumidityReadingCall7 call = reinterpret_cast<CuteQmlHumidityReadingCall7>(taken[7]);
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
      CuteQmlHumidityReadingCall8 call = reinterpret_cast<CuteQmlHumidityReadingCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QmlHumidityReading::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QmlHumidityReading10metaObjectEv(
    const QmlHumidityReading *self) {
  return self->metaObject();
}

//  void *QmlHumidityReading::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN18QmlHumidityReading11qt_metacastEPKc(
    QmlHumidityReading *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QmlHumidityReading::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN18QmlHumidityReading11qt_metacallEN11QMetaObject4CallEiPPv(
    QmlHumidityReading *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QmlHumidityReading::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QmlHumidityReading2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QmlHumidityReading::tr(s, c, n));
}

//  void QmlHumidityReading::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QmlHumidityReading24qt_qmlMarker_uncreatableEv(
    QmlHumidityReading *self) {
  self->qt_qmlMarker_uncreatable();
}

//  QmlHumidityReading::QmlHumidityReading(QHumiditySensor *sensor)
extern "C" Q_DECL_EXPORT
QmlHumidityReading *ritual_ZN18QmlHumidityReadingC1EP15QHumiditySensor(
    QHumiditySensor *sensor) {
  return new CuteQmlHumidityReading(sensor);
}

//  QmlHumidityReading::~QmlHumidityReading()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QmlHumidityReadingD1Ev(QmlHumidityReading *self) {
  delete self;
}

//  qreal QmlHumidityReading::relativeHumidity() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK18QmlHumidityReading16relativeHumidityEv(
    const QmlHumidityReading *self) {
  return self->relativeHumidity();
}

//  QBindable<qreal> QmlHumidityReading::bindableRelativeHumidity() const
extern "C" Q_DECL_EXPORT
QBindable<qreal> *ritual_ZNK18QmlHumidityReading24bindableRelativeHumidityEv(
    const QmlHumidityReading *self) {
  return new QBindable<qreal>(self->bindableRelativeHumidity());
}

//  qreal QmlHumidityReading::absoluteHumidity() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK18QmlHumidityReading16absoluteHumidityEv(
    const QmlHumidityReading *self) {
  return self->absoluteHumidity();
}

//  QBindable<qreal> QmlHumidityReading::bindableAbsoluteHumidity() const
extern "C" Q_DECL_EXPORT
QBindable<qreal> *ritual_ZNK18QmlHumidityReading24bindableAbsoluteHumidityEv(
    const QmlHumidityReading *self) {
  return new QBindable<qreal>(self->bindableAbsoluteHumidity());
}

//  void QmlHumidityReading::relativeHumidityChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QmlHumidityReading23relativeHumidityChangedEv(
    QmlHumidityReading *self) {
  self->relativeHumidityChanged();
}

//  void QmlHumidityReading::absoluteHumidityChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QmlHumidityReading23absoluteHumidityChangedEv(
    QmlHumidityReading *self) {
  self->absoluteHumidityChanged();
}

//  QSensorReading *QmlHumidityReading::reading() const
extern "C" Q_DECL_EXPORT
QSensorReading *ritual_ZNK18QmlHumidityReading7readingEv(
    const QmlHumidityReading *self) {
  return self->reading();
}

//  void QmlHumidityReading::readingUpdate()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QmlHumidityReading13readingUpdateEv(
    QmlHumidityReading *self) {
  self->readingUpdate();
}

//  size_t QmlHumidityReading::_qt_property_m_relativeHumidity_offset()
extern "C" Q_DECL_EXPORT
size_t ritual_ZN18QmlHumidityReading38_qt_property_m_relativeHumidity_offsetEv() {
  return QmlHumidityReading::_qt_property_m_relativeHumidity_offset();
}

//  size_t QmlHumidityReading::_qt_property_m_absoluteHumidity_offset()
extern "C" Q_DECL_EXPORT
size_t ritual_ZN18QmlHumidityReading38_qt_property_m_absoluteHumidity_offsetEv() {
  return QmlHumidityReading::_qt_property_m_absoluteHumidity_offset();
}

//  a Python function taken by a CuteQmlHumidityReading, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QmlHumidityReading(
    QmlHumidityReading *self,
    const char *key,
    void *call) {
  return static_cast<CuteQmlHumidityReading *>(self)->take(key, call);
}

//  QSensorReading *QmlHumidityReading::reading() const
extern "C" Q_DECL_EXPORT
QSensorReading *ritual_own_ZNK18QmlHumidityReading7readingEv(
    const QmlHumidityReading *self) {
  return self->QmlHumidityReading::reading();
}

//  void QmlHumidityReading::readingUpdate()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QmlHumidityReading13readingUpdateEv(
    QmlHumidityReading *self) {
  self->QmlHumidityReading::readingUpdate();
}

//  a QBindable<qreal> a ritual of QmlHumidityReading gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QmlHumidityReading__QBindable_qreal(
    QBindable<qreal> *self) {
  delete self;
}
