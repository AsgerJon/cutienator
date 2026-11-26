//  Written by dev_tooling.RitualGenerator from the records of
//  QtSensorsQuick/6.12.0/QtSensorsQuick/private/qmlsensor_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtSensorsQuick/6.12.0/QtSensorsQuick/private/qsensorsquickglobal_p.h>
#include <QtSensorsQuick/QtSensorsQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSensorsQuick/6.12.0/QtSensorsQuick/private/qmlsensor_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#include <QtCore/QBindable>

//  A QmlSensorReading that Python can take functions over in. Every QmlSensorReading
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQmlSensorReadingCall0)(const void *, int *);
typedef void (*CuteQmlSensorReadingCall1)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQmlSensorReadingCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQmlSensorReadingCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQmlSensorReadingCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQmlSensorReadingCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQmlSensorReadingCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQmlSensorReadingCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQmlSensorReadingCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQmlSensorReading : public QmlSensorReading {
public:
  using QmlSensorReading::QmlSensorReading;
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

  //  QSensorReading *QmlSensorReading::reading() const
  QSensorReading *reading() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQmlSensorReadingCall0 call = reinterpret_cast<CuteQmlSensorReadingCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSensorReading *>(given);
    }
    return {};
  }

  //  void QmlSensorReading::readingUpdate()
  void readingUpdate() override {
    if (taken[1]) {
      int handled = 0;
      CuteQmlSensorReadingCall1 call = reinterpret_cast<CuteQmlSensorReadingCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQmlSensorReadingCall2 call = reinterpret_cast<CuteQmlSensorReadingCall2>(taken[2]);
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
      CuteQmlSensorReadingCall3 call = reinterpret_cast<CuteQmlSensorReadingCall3>(taken[3]);
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
      CuteQmlSensorReadingCall4 call = reinterpret_cast<CuteQmlSensorReadingCall4>(taken[4]);
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
      CuteQmlSensorReadingCall5 call = reinterpret_cast<CuteQmlSensorReadingCall5>(taken[5]);
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
      CuteQmlSensorReadingCall6 call = reinterpret_cast<CuteQmlSensorReadingCall6>(taken[6]);
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
      CuteQmlSensorReadingCall7 call = reinterpret_cast<CuteQmlSensorReadingCall7>(taken[7]);
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
      CuteQmlSensorReadingCall8 call = reinterpret_cast<CuteQmlSensorReadingCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QmlSensorReading::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QmlSensorReading10metaObjectEv(
    const QmlSensorReading *self) {
  return self->metaObject();
}

//  void *QmlSensorReading::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN16QmlSensorReading11qt_metacastEPKc(
    QmlSensorReading *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QmlSensorReading::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN16QmlSensorReading11qt_metacallEN11QMetaObject4CallEiPPv(
    QmlSensorReading *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QmlSensorReading::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QmlSensorReading2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QmlSensorReading::tr(s, c, n));
}

//  void QmlSensorReading::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QmlSensorReading24qt_qmlMarker_uncreatableEv(
    QmlSensorReading *self) {
  self->qt_qmlMarker_uncreatable();
}

//  QmlSensorReading::QmlSensorReading()
extern "C" Q_DECL_EXPORT
QmlSensorReading *ritual_ZN16QmlSensorReadingC1Ev() {
  return new CuteQmlSensorReading();
}

//  QmlSensorReading::~QmlSensorReading()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QmlSensorReadingD1Ev(QmlSensorReading *self) {
  delete self;
}

//  quint64 QmlSensorReading::timestamp() const
extern "C" Q_DECL_EXPORT
quint64 ritual_ZNK16QmlSensorReading9timestampEv(
    const QmlSensorReading *self) {
  return self->timestamp();
}

//  QBindable<quint64> QmlSensorReading::bindableTimestamp() const
extern "C" Q_DECL_EXPORT
QBindable<quint64> *ritual_ZNK16QmlSensorReading17bindableTimestampEv(
    const QmlSensorReading *self) {
  return new QBindable<quint64>(self->bindableTimestamp());
}

//  void QmlSensorReading::update()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QmlSensorReading6updateEv(QmlSensorReading *self) {
  self->update();
}

//  void QmlSensorReading::timestampChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QmlSensorReading16timestampChangedEv(
    QmlSensorReading *self) {
  self->timestampChanged();
}

//  QSensorReading *QmlSensorReading::reading() const
extern "C" Q_DECL_EXPORT
QSensorReading *ritual_ZNK16QmlSensorReading7readingEv(
    const QmlSensorReading *self) {
  return self->reading();
}

//  void QmlSensorReading::readingUpdate()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QmlSensorReading13readingUpdateEv(QmlSensorReading *self) {
  self->readingUpdate();
}

//  size_t QmlSensorReading::_qt_property_m_timestamp_offset()
extern "C" Q_DECL_EXPORT
size_t ritual_ZN16QmlSensorReading31_qt_property_m_timestamp_offsetEv() {
  return QmlSensorReading::_qt_property_m_timestamp_offset();
}

//  a Python function taken by a CuteQmlSensorReading, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QmlSensorReading(
    QmlSensorReading *self,
    const char *key,
    void *call) {
  return static_cast<CuteQmlSensorReading *>(self)->take(key, call);
}

//  a QBindable<quint64> a ritual of QmlSensorReading gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QmlSensorReading__QBindable_quint64(
    QBindable<quint64> *self) {
  delete self;
}
