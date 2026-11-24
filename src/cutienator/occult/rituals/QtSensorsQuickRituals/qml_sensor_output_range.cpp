//  Written by dev_tooling.RitualGenerator from the records of
//  QtSensorsQuick/6.12.0/QtSensorsQuick/private/qmlsensorrange_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtSensorsQuick/6.12.0/QtSensorsQuick/private/qsensorsquickglobal_p.h>
#include <QtSensorsQuick/QtSensorsQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSensorsQuick/6.12.0/QtSensorsQuick/private/qmlsensorrange_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QmlSensorOutputRange that Python can take functions over in. Every QmlSensorOutputRange
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQmlSensorOutputRangeCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQmlSensorOutputRangeCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQmlSensorOutputRangeCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQmlSensorOutputRangeCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQmlSensorOutputRangeCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQmlSensorOutputRangeCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQmlSensorOutputRangeCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQmlSensorOutputRange : public QmlSensorOutputRange {
public:
  using QmlSensorOutputRange::QmlSensorOutputRange;
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
      CuteQmlSensorOutputRangeCall0 call = reinterpret_cast<CuteQmlSensorOutputRangeCall0>(taken[0]);
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
      CuteQmlSensorOutputRangeCall1 call = reinterpret_cast<CuteQmlSensorOutputRangeCall1>(taken[1]);
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
      CuteQmlSensorOutputRangeCall2 call = reinterpret_cast<CuteQmlSensorOutputRangeCall2>(taken[2]);
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
      CuteQmlSensorOutputRangeCall3 call = reinterpret_cast<CuteQmlSensorOutputRangeCall3>(taken[3]);
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
      CuteQmlSensorOutputRangeCall4 call = reinterpret_cast<CuteQmlSensorOutputRangeCall4>(taken[4]);
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
      CuteQmlSensorOutputRangeCall5 call = reinterpret_cast<CuteQmlSensorOutputRangeCall5>(taken[5]);
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
      CuteQmlSensorOutputRangeCall6 call = reinterpret_cast<CuteQmlSensorOutputRangeCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QmlSensorOutputRange::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20QmlSensorOutputRange10metaObjectEv(
    const QmlSensorOutputRange *self) {
  return self->metaObject();
}

//  QString QmlSensorOutputRange::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN20QmlSensorOutputRange2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QmlSensorOutputRange::tr(s, c, n));
}

//  void QmlSensorOutputRange::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QmlSensorOutputRange24qt_qmlMarker_uncreatableEv(
    QmlSensorOutputRange *self) {
  self->qt_qmlMarker_uncreatable();
}

//  QmlSensorOutputRange::QmlSensorOutputRange(QObject *parent)
extern "C" Q_DECL_EXPORT
QmlSensorOutputRange *ritual_ZN20QmlSensorOutputRangeC1EP7QObject(
    QObject *parent) {
  return new CuteQmlSensorOutputRange(parent);
}

//  QmlSensorOutputRange::~QmlSensorOutputRange()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QmlSensorOutputRangeD1Ev(QmlSensorOutputRange *self) {
  delete self;
}

//  qreal QmlSensorOutputRange::minimum() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK20QmlSensorOutputRange7minimumEv(
    const QmlSensorOutputRange *self) {
  return self->minimum();
}

//  void QmlSensorOutputRange::setMinimum(qreal mini)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QmlSensorOutputRange10setMinimumEd(
    QmlSensorOutputRange *self,
    qreal mini) {
  self->setMinimum(mini);
}

//  qreal QmlSensorOutputRange::maximum() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK20QmlSensorOutputRange7maximumEv(
    const QmlSensorOutputRange *self) {
  return self->maximum();
}

//  void QmlSensorOutputRange::setMaximum(qreal maxi)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QmlSensorOutputRange10setMaximumEd(
    QmlSensorOutputRange *self,
    qreal maxi) {
  self->setMaximum(maxi);
}

//  qreal QmlSensorOutputRange::accuracy() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK20QmlSensorOutputRange8accuracyEv(
    const QmlSensorOutputRange *self) {
  return self->accuracy();
}

//  void QmlSensorOutputRange::setAccuracy(qreal accu)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QmlSensorOutputRange11setAccuracyEd(
    QmlSensorOutputRange *self,
    qreal accu) {
  self->setAccuracy(accu);
}

//  a Python function taken by a CuteQmlSensorOutputRange, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QmlSensorOutputRange(
    QmlSensorOutputRange *self,
    const char *key,
    void *call) {
  return static_cast<CuteQmlSensorOutputRange *>(self)->take(key, call);
}
