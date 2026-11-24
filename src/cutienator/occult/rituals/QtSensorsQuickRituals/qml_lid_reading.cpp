//  Written by dev_tooling.RitualGenerator from the records of
//  QtSensorsQuick/6.12.0/QtSensorsQuick/private/qmllidsensor_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtSensorsQuick/6.12.0/QtSensorsQuick/private/qsensorsquickglobal_p.h>
#include <QtSensorsQuick/QtSensorsQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSensorsQuick/6.12.0/QtSensorsQuick/private/qmllidsensor_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QmlLidReading that Python can take functions over in. Every QmlLidReading
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQmlLidReadingCall0)(const void *, int *);
typedef void (*CuteQmlLidReadingCall1)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQmlLidReadingCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQmlLidReadingCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQmlLidReadingCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQmlLidReadingCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQmlLidReadingCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQmlLidReadingCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQmlLidReadingCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQmlLidReading : public QmlLidReading {
public:
  using QmlLidReading::QmlLidReading;
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

  //  QSensorReading *QmlLidReading::reading() const
  QSensorReading *reading() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQmlLidReadingCall0 call = reinterpret_cast<CuteQmlLidReadingCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSensorReading *>(given);
    }
    return QmlLidReading::reading();
  }

  //  void QmlLidReading::readingUpdate()
  void readingUpdate() override {
    if (taken[1]) {
      int handled = 0;
      CuteQmlLidReadingCall1 call = reinterpret_cast<CuteQmlLidReadingCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QmlLidReading::readingUpdate();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQmlLidReadingCall2 call = reinterpret_cast<CuteQmlLidReadingCall2>(taken[2]);
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
      CuteQmlLidReadingCall3 call = reinterpret_cast<CuteQmlLidReadingCall3>(taken[3]);
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
      CuteQmlLidReadingCall4 call = reinterpret_cast<CuteQmlLidReadingCall4>(taken[4]);
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
      CuteQmlLidReadingCall5 call = reinterpret_cast<CuteQmlLidReadingCall5>(taken[5]);
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
      CuteQmlLidReadingCall6 call = reinterpret_cast<CuteQmlLidReadingCall6>(taken[6]);
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
      CuteQmlLidReadingCall7 call = reinterpret_cast<CuteQmlLidReadingCall7>(taken[7]);
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
      CuteQmlLidReadingCall8 call = reinterpret_cast<CuteQmlLidReadingCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QmlLidReading::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13QmlLidReading10metaObjectEv(
    const QmlLidReading *self) {
  return self->metaObject();
}

//  QString QmlLidReading::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13QmlLidReading2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QmlLidReading::tr(s, c, n));
}

//  void QmlLidReading::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QmlLidReading24qt_qmlMarker_uncreatableEv(
    QmlLidReading *self) {
  self->qt_qmlMarker_uncreatable();
}

//  QmlLidReading::QmlLidReading(QLidSensor *sensor)
extern "C" Q_DECL_EXPORT
QmlLidReading *ritual_ZN13QmlLidReadingC1EP10QLidSensor(QLidSensor *sensor) {
  return new CuteQmlLidReading(sensor);
}

//  QmlLidReading::~QmlLidReading()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QmlLidReadingD1Ev(QmlLidReading *self) {
  delete self;
}

//  bool QmlLidReading::backLidClosed() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QmlLidReading13backLidClosedEv(const QmlLidReading *self) {
  return self->backLidClosed();
}

//  bool QmlLidReading::frontLidClosed() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QmlLidReading14frontLidClosedEv(const QmlLidReading *self) {
  return self->frontLidClosed();
}

//  QSensorReading *QmlLidReading::reading() const
extern "C" Q_DECL_EXPORT
QSensorReading *ritual_ZNK13QmlLidReading7readingEv(
    const QmlLidReading *self) {
  return self->reading();
}

//  void QmlLidReading::readingUpdate()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QmlLidReading13readingUpdateEv(QmlLidReading *self) {
  self->readingUpdate();
}

//  a Python function taken by a CuteQmlLidReading, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QmlLidReading(
    QmlLidReading *self,
    const char *key,
    void *call) {
  return static_cast<CuteQmlLidReading *>(self)->take(key, call);
}

//  QSensorReading *QmlLidReading::reading() const
extern "C" Q_DECL_EXPORT
QSensorReading *ritual_own_ZNK13QmlLidReading7readingEv(
    const QmlLidReading *self) {
  return self->QmlLidReading::reading();
}

//  void QmlLidReading::readingUpdate()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QmlLidReading13readingUpdateEv(QmlLidReading *self) {
  self->QmlLidReading::readingUpdate();
}
