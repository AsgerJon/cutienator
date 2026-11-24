//  Written by dev_tooling.RitualGenerator from the records of
//  QtSensors/qmagnetometer.h, Qt 6.12.0. Changes made here are lost.
#include <QtSensors/qmagnetometer.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QMagnetometer that Python can take functions over in. Every QMagnetometer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQMagnetometerCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQMagnetometerCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQMagnetometerCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQMagnetometerCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQMagnetometerCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQMagnetometerCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQMagnetometerCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQMagnetometer : public QMagnetometer {
public:
  using QMagnetometer::QMagnetometer;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQMagnetometerCall0 call = reinterpret_cast<CuteQMagnetometerCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQMagnetometerCall1 call = reinterpret_cast<CuteQMagnetometerCall1>(taken[1]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQMagnetometerCall2 call = reinterpret_cast<CuteQMagnetometerCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQMagnetometerCall3 call = reinterpret_cast<CuteQMagnetometerCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQMagnetometerCall4 call = reinterpret_cast<CuteQMagnetometerCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteQMagnetometerCall5 call = reinterpret_cast<CuteQMagnetometerCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQMagnetometerCall6 call = reinterpret_cast<CuteQMagnetometerCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QMagnetometer::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13QMagnetometer10metaObjectEv(
    const QMagnetometer *self) {
  return self->metaObject();
}

//  QString QMagnetometer::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13QMagnetometer2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QMagnetometer::tr(s, c, n));
}

//  QMagnetometer::QMagnetometer(QObject *parent)
extern "C" Q_DECL_EXPORT
QMagnetometer *ritual_ZN13QMagnetometerC1EP7QObject(QObject *parent) {
  return new CuteQMagnetometer(parent);
}

//  QMagnetometer::~QMagnetometer()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QMagnetometerD1Ev(QMagnetometer *self) {
  delete self;
}

//  QMagnetometerReading *QMagnetometer::reading() const
extern "C" Q_DECL_EXPORT
QMagnetometerReading *ritual_ZNK13QMagnetometer7readingEv(
    const QMagnetometer *self) {
  return self->reading();
}

//  bool QMagnetometer::returnGeoValues() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QMagnetometer15returnGeoValuesEv(
    const QMagnetometer *self) {
  return self->returnGeoValues();
}

//  void QMagnetometer::setReturnGeoValues(bool returnGeoValues)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QMagnetometer18setReturnGeoValuesEb(
    QMagnetometer *self,
    bool returnGeoValues) {
  self->setReturnGeoValues(returnGeoValues);
}

//  QMagnetometerPrivate *QMagnetometer::d_func()
extern "C" Q_DECL_EXPORT
QMagnetometerPrivate *ritual_ZN13QMagnetometer6d_funcEv(
    QMagnetometer *self) {
  return self->d_func();
}

//  const QMagnetometerPrivate *QMagnetometer::d_func() const
extern "C" Q_DECL_EXPORT
const QMagnetometerPrivate *ritual_ZNK13QMagnetometer6d_funcEv(
    const QMagnetometer *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQMagnetometer, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QMagnetometer(
    QMagnetometer *self,
    const char *key,
    void *call) {
  return static_cast<CuteQMagnetometer *>(self)->take(key, call);
}
