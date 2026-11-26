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

//  A QmlSensorRange that Python can take functions over in. Every QmlSensorRange
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQmlSensorRangeCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQmlSensorRangeCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQmlSensorRangeCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQmlSensorRangeCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQmlSensorRangeCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQmlSensorRangeCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQmlSensorRangeCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQmlSensorRange : public QmlSensorRange {
public:
  using QmlSensorRange::QmlSensorRange;
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
      CuteQmlSensorRangeCall0 call = reinterpret_cast<CuteQmlSensorRangeCall0>(taken[0]);
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
      CuteQmlSensorRangeCall1 call = reinterpret_cast<CuteQmlSensorRangeCall1>(taken[1]);
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
      CuteQmlSensorRangeCall2 call = reinterpret_cast<CuteQmlSensorRangeCall2>(taken[2]);
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
      CuteQmlSensorRangeCall3 call = reinterpret_cast<CuteQmlSensorRangeCall3>(taken[3]);
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
      CuteQmlSensorRangeCall4 call = reinterpret_cast<CuteQmlSensorRangeCall4>(taken[4]);
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
      CuteQmlSensorRangeCall5 call = reinterpret_cast<CuteQmlSensorRangeCall5>(taken[5]);
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
      CuteQmlSensorRangeCall6 call = reinterpret_cast<CuteQmlSensorRangeCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QmlSensorRange::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14QmlSensorRange10metaObjectEv(
    const QmlSensorRange *self) {
  return self->metaObject();
}

//  void *QmlSensorRange::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN14QmlSensorRange11qt_metacastEPKc(
    QmlSensorRange *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QmlSensorRange::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN14QmlSensorRange11qt_metacallEN11QMetaObject4CallEiPPv(
    QmlSensorRange *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QmlSensorRange::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QmlSensorRange2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QmlSensorRange::tr(s, c, n));
}

//  void QmlSensorRange::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QmlSensorRange24qt_qmlMarker_uncreatableEv(
    QmlSensorRange *self) {
  self->qt_qmlMarker_uncreatable();
}

//  QmlSensorRange::QmlSensorRange(QObject *parent)
extern "C" Q_DECL_EXPORT
QmlSensorRange *ritual_ZN14QmlSensorRangeC1EP7QObject(QObject *parent) {
  return new CuteQmlSensorRange(parent);
}

//  QmlSensorRange::~QmlSensorRange()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QmlSensorRangeD1Ev(QmlSensorRange *self) {
  delete self;
}

//  int QmlSensorRange::minimum() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QmlSensorRange7minimumEv(const QmlSensorRange *self) {
  return self->minimum();
}

//  void QmlSensorRange::setMinumum(int mini)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QmlSensorRange10setMinumumEi(
    QmlSensorRange *self,
    int mini) {
  self->setMinumum(mini);
}

//  int QmlSensorRange::maximum() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QmlSensorRange7maximumEv(const QmlSensorRange *self) {
  return self->maximum();
}

//  void QmlSensorRange::setMaximum(int maxi)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QmlSensorRange10setMaximumEi(
    QmlSensorRange *self,
    int maxi) {
  self->setMaximum(maxi);
}

//  a Python function taken by a CuteQmlSensorRange, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QmlSensorRange(
    QmlSensorRange *self,
    const char *key,
    void *call) {
  return static_cast<CuteQmlSensorRange *>(self)->take(key, call);
}
