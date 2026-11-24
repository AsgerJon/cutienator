//  Written by dev_tooling.RitualGenerator from the records of
//  QtSensorsQuick/6.12.0/QtSensorsQuick/private/qmlgyroscope_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtSensorsQuick/6.12.0/QtSensorsQuick/private/qsensorsquickglobal_p.h>
#include <QtSensorsQuick/QtSensorsQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSensorsQuick/6.12.0/QtSensorsQuick/private/qmlgyroscope_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QmlGyroscopeReading that Python can take functions over in. Every QmlGyroscopeReading
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQmlGyroscopeReadingCall0)(const void *, int *);
typedef void (*CuteQmlGyroscopeReadingCall1)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQmlGyroscopeReadingCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQmlGyroscopeReadingCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQmlGyroscopeReadingCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQmlGyroscopeReadingCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQmlGyroscopeReadingCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQmlGyroscopeReadingCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQmlGyroscopeReadingCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQmlGyroscopeReading : public QmlGyroscopeReading {
public:
  using QmlGyroscopeReading::QmlGyroscopeReading;
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

  //  QSensorReading *QmlGyroscopeReading::reading() const
  QSensorReading *reading() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQmlGyroscopeReadingCall0 call = reinterpret_cast<CuteQmlGyroscopeReadingCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSensorReading *>(given);
    }
    return QmlGyroscopeReading::reading();
  }

  //  void QmlGyroscopeReading::readingUpdate()
  void readingUpdate() override {
    if (taken[1]) {
      int handled = 0;
      CuteQmlGyroscopeReadingCall1 call = reinterpret_cast<CuteQmlGyroscopeReadingCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QmlGyroscopeReading::readingUpdate();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQmlGyroscopeReadingCall2 call = reinterpret_cast<CuteQmlGyroscopeReadingCall2>(taken[2]);
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
      CuteQmlGyroscopeReadingCall3 call = reinterpret_cast<CuteQmlGyroscopeReadingCall3>(taken[3]);
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
      CuteQmlGyroscopeReadingCall4 call = reinterpret_cast<CuteQmlGyroscopeReadingCall4>(taken[4]);
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
      CuteQmlGyroscopeReadingCall5 call = reinterpret_cast<CuteQmlGyroscopeReadingCall5>(taken[5]);
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
      CuteQmlGyroscopeReadingCall6 call = reinterpret_cast<CuteQmlGyroscopeReadingCall6>(taken[6]);
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
      CuteQmlGyroscopeReadingCall7 call = reinterpret_cast<CuteQmlGyroscopeReadingCall7>(taken[7]);
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
      CuteQmlGyroscopeReadingCall8 call = reinterpret_cast<CuteQmlGyroscopeReadingCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QmlGyroscopeReading::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19QmlGyroscopeReading10metaObjectEv(
    const QmlGyroscopeReading *self) {
  return self->metaObject();
}

//  QString QmlGyroscopeReading::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19QmlGyroscopeReading2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QmlGyroscopeReading::tr(s, c, n));
}

//  void QmlGyroscopeReading::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QmlGyroscopeReading24qt_qmlMarker_uncreatableEv(
    QmlGyroscopeReading *self) {
  self->qt_qmlMarker_uncreatable();
}

//  QmlGyroscopeReading::QmlGyroscopeReading(QGyroscope *sensor)
extern "C" Q_DECL_EXPORT
QmlGyroscopeReading *ritual_ZN19QmlGyroscopeReadingC1EP10QGyroscope(
    QGyroscope *sensor) {
  return new CuteQmlGyroscopeReading(sensor);
}

//  QmlGyroscopeReading::~QmlGyroscopeReading()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QmlGyroscopeReadingD1Ev(QmlGyroscopeReading *self) {
  delete self;
}

//  qreal QmlGyroscopeReading::x() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK19QmlGyroscopeReading1xEv(const QmlGyroscopeReading *self) {
  return self->x();
}

//  qreal QmlGyroscopeReading::y() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK19QmlGyroscopeReading1yEv(const QmlGyroscopeReading *self) {
  return self->y();
}

//  qreal QmlGyroscopeReading::z() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK19QmlGyroscopeReading1zEv(const QmlGyroscopeReading *self) {
  return self->z();
}

//  QSensorReading *QmlGyroscopeReading::reading() const
extern "C" Q_DECL_EXPORT
QSensorReading *ritual_ZNK19QmlGyroscopeReading7readingEv(
    const QmlGyroscopeReading *self) {
  return self->reading();
}

//  void QmlGyroscopeReading::readingUpdate()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QmlGyroscopeReading13readingUpdateEv(
    QmlGyroscopeReading *self) {
  self->readingUpdate();
}

//  a Python function taken by a CuteQmlGyroscopeReading, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QmlGyroscopeReading(
    QmlGyroscopeReading *self,
    const char *key,
    void *call) {
  return static_cast<CuteQmlGyroscopeReading *>(self)->take(key, call);
}

//  QSensorReading *QmlGyroscopeReading::reading() const
extern "C" Q_DECL_EXPORT
QSensorReading *ritual_own_ZNK19QmlGyroscopeReading7readingEv(
    const QmlGyroscopeReading *self) {
  return self->QmlGyroscopeReading::reading();
}

//  void QmlGyroscopeReading::readingUpdate()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QmlGyroscopeReading13readingUpdateEv(
    QmlGyroscopeReading *self) {
  self->QmlGyroscopeReading::readingUpdate();
}
