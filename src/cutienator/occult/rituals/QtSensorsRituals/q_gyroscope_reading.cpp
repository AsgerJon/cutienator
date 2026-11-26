//  Written by dev_tooling.RitualGenerator from the records of
//  QtSensors/qgyroscope.h, Qt 6.12.0. Changes made here are lost.
#include <QtSensors/qgyroscope.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QGyroscopeReading that Python can take functions over in. Every QGyroscopeReading
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQGyroscopeReadingCall0)(const void *, QSensorReading *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQGyroscopeReadingCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQGyroscopeReadingCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGyroscopeReadingCall3)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGyroscopeReadingCall4)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGyroscopeReadingCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGyroscopeReadingCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGyroscopeReadingCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQGyroscopeReading : public QGyroscopeReading {
public:
  using QGyroscopeReading::QGyroscopeReading;
  void *taken[8] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN14QSensorReading14copyValuesFromEPS_")) {
      taken[0] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QGyroscopeReading::copyValuesFrom(QSensorReading *other)
  void copyValuesFrom(QSensorReading *other) override {
    if (taken[0]) {
      int handled = 0;
      CuteQGyroscopeReadingCall0 call = reinterpret_cast<CuteQGyroscopeReadingCall0>(taken[0]);
      call(this, other, &handled);
      if (handled) return;
    }
    QGyroscopeReading::copyValuesFrom(other);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQGyroscopeReadingCall1 call = reinterpret_cast<CuteQGyroscopeReadingCall1>(taken[1]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQGyroscopeReadingCall2 call = reinterpret_cast<CuteQGyroscopeReadingCall2>(taken[2]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQGyroscopeReadingCall3 call = reinterpret_cast<CuteQGyroscopeReadingCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQGyroscopeReadingCall4 call = reinterpret_cast<CuteQGyroscopeReadingCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQGyroscopeReadingCall5 call = reinterpret_cast<CuteQGyroscopeReadingCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQGyroscopeReadingCall6 call = reinterpret_cast<CuteQGyroscopeReadingCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[7]) {
      int handled = 0;
      CuteQGyroscopeReadingCall7 call = reinterpret_cast<CuteQGyroscopeReadingCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QGyroscopeReading::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QGyroscopeReading10metaObjectEv(
    const QGyroscopeReading *self) {
  return self->metaObject();
}

//  void *QGyroscopeReading::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN17QGyroscopeReading11qt_metacastEPKc(
    QGyroscopeReading *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QGyroscopeReading::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN17QGyroscopeReading11qt_metacallEN11QMetaObject4CallEiPPv(
    QGyroscopeReading *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QGyroscopeReading::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QGyroscopeReading2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QGyroscopeReading::tr(s, c, n));
}

//  QGyroscopeReading::QGyroscopeReading(QObject *parent)
extern "C" Q_DECL_EXPORT
QGyroscopeReading *ritual_ZN17QGyroscopeReadingC1EP7QObject(
    QObject *parent) {
  return new CuteQGyroscopeReading(parent);
}

//  QGyroscopeReading::~QGyroscopeReading()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGyroscopeReadingD1Ev(QGyroscopeReading *self) {
  delete self;
}

//  void QGyroscopeReading::copyValuesFrom(QSensorReading *other)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGyroscopeReading14copyValuesFromEP14QSensorReading(
    QGyroscopeReading *self,
    QSensorReading *other) {
  self->copyValuesFrom(other);
}

//  qreal QGyroscopeReading::x() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK17QGyroscopeReading1xEv(const QGyroscopeReading *self) {
  return self->x();
}

//  void QGyroscopeReading::setX(qreal x)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGyroscopeReading4setXEd(QGyroscopeReading *self, qreal x) {
  self->setX(x);
}

//  qreal QGyroscopeReading::y() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK17QGyroscopeReading1yEv(const QGyroscopeReading *self) {
  return self->y();
}

//  void QGyroscopeReading::setY(qreal y)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGyroscopeReading4setYEd(QGyroscopeReading *self, qreal y) {
  self->setY(y);
}

//  qreal QGyroscopeReading::z() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK17QGyroscopeReading1zEv(const QGyroscopeReading *self) {
  return self->z();
}

//  void QGyroscopeReading::setZ(qreal z)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGyroscopeReading4setZEd(QGyroscopeReading *self, qreal z) {
  self->setZ(z);
}

//  a Python function taken by a CuteQGyroscopeReading, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGyroscopeReading(
    QGyroscopeReading *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGyroscopeReading *>(self)->take(key, call);
}

//  void QGyroscopeReading::copyValuesFrom(QSensorReading *other)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QGyroscopeReading14copyValuesFromEP14QSensorReading(
    QGyroscopeReading *self,
    QSensorReading *other) {
  self->QGyroscopeReading::copyValuesFrom(other);
}
