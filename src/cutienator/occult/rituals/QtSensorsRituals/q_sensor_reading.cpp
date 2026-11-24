//  Written by dev_tooling.RitualGenerator from the records of
//  QtSensors/qsensor.h, Qt 6.12.0. Changes made here are lost.
#include <QtSensors/qsensor.h>
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QSensorReading may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQSensorReading : QSensorReading {
  using QSensorReading::copyValuesFrom;
};

//  A QSensorReading that Python can take functions over in. Every QSensorReading
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQSensorReadingCall0)(const void *, QSensorReading *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSensorReadingCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSensorReadingCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSensorReadingCall3)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSensorReadingCall4)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSensorReadingCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSensorReadingCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSensorReadingCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQSensorReading : public QSensorReading {
public:
  using QSensorReading::QSensorReading;
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

  //  void QSensorReading::copyValuesFrom(QSensorReading *other)
  void copyValuesFrom(QSensorReading *other) override {
    if (taken[0]) {
      int handled = 0;
      CuteQSensorReadingCall0 call = reinterpret_cast<CuteQSensorReadingCall0>(taken[0]);
      call(this, other, &handled);
      if (handled) return;
    }
    QSensorReading::copyValuesFrom(other);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQSensorReadingCall1 call = reinterpret_cast<CuteQSensorReadingCall1>(taken[1]);
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
      CuteQSensorReadingCall2 call = reinterpret_cast<CuteQSensorReadingCall2>(taken[2]);
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
      CuteQSensorReadingCall3 call = reinterpret_cast<CuteQSensorReadingCall3>(taken[3]);
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
      CuteQSensorReadingCall4 call = reinterpret_cast<CuteQSensorReadingCall4>(taken[4]);
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
      CuteQSensorReadingCall5 call = reinterpret_cast<CuteQSensorReadingCall5>(taken[5]);
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
      CuteQSensorReadingCall6 call = reinterpret_cast<CuteQSensorReadingCall6>(taken[6]);
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
      CuteQSensorReadingCall7 call = reinterpret_cast<CuteQSensorReadingCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QSensorReading::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14QSensorReading10metaObjectEv(
    const QSensorReading *self) {
  return self->metaObject();
}

//  QString QSensorReading::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QSensorReading2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QSensorReading::tr(s, c, n));
}

//  QSensorReading::~QSensorReading()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSensorReadingD1Ev(QSensorReading *self) {
  delete self;
}

//  quint64 QSensorReading::timestamp() const
extern "C" Q_DECL_EXPORT
quint64 ritual_ZNK14QSensorReading9timestampEv(const QSensorReading *self) {
  return self->timestamp();
}

//  void QSensorReading::setTimestamp(quint64 timestamp)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSensorReading12setTimestampEy(
    QSensorReading *self,
    quint64 timestamp) {
  self->setTimestamp(timestamp);
}

//  int QSensorReading::valueCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QSensorReading10valueCountEv(const QSensorReading *self) {
  return self->valueCount();
}

//  QVariant QSensorReading::value(int index) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK14QSensorReading5valueEi(
    const QSensorReading *self,
    int index) {
  return new QVariant(self->value(index));
}

//  QSensorReading::QSensorReading(QObject *parent, QSensorReadingPrivate *d)
extern "C" Q_DECL_EXPORT
QSensorReading *ritual_ZN14QSensorReadingC1EP7QObjectP21QSensorReadingPrivate(
    QObject *parent,
    QSensorReadingPrivate *d) {
  return new CuteQSensorReading(parent, d);
}

//  void QSensorReading::copyValuesFrom(QSensorReading *other)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSensorReading14copyValuesFromEPS_(
    QSensorReading *self,
    QSensorReading *other) {
  self->copyValuesFrom(other);
}

//  a Python function taken by a CuteQSensorReading, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSensorReading(
    QSensorReading *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSensorReading *>(self)->take(key, call);
}

//  void QSensorReading::copyValuesFrom(QSensorReading *other)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QSensorReading14copyValuesFromEPS_(
    QSensorReading *self,
    QSensorReading *other) {
  static_cast<OwnQSensorReading *>(self)->OwnQSensorReading::copyValuesFrom(
      other);
}
