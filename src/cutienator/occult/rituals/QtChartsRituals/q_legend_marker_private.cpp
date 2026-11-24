//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/6.12.0/QtCharts/private/qlegendmarker_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#include <QtCharts/qlegendmarker.h>
#include <QtCharts/QtCharts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCharts/6.12.0/QtCharts/private/qlegendmarker_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QLegendMarkerPrivate that Python can take functions over in. Every QLegendMarkerPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQLegendMarkerPrivateCall0)(const void *, int *);
typedef void * (*CuteQLegendMarkerPrivateCall1)(const void *, int *);
typedef void (*CuteQLegendMarkerPrivateCall2)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQLegendMarkerPrivateCall3)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQLegendMarkerPrivateCall4)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLegendMarkerPrivateCall5)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLegendMarkerPrivateCall6)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLegendMarkerPrivateCall7)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLegendMarkerPrivateCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLegendMarkerPrivateCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQLegendMarkerPrivate : public QLegendMarkerPrivate {
public:
  using QLegendMarkerPrivate::QLegendMarkerPrivate;
  void *taken[10] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN20QLegendMarkerPrivate6seriesEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QLegendMarkerPrivate13relatedObjectEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QLegendMarkerPrivate7updatedEv")) {
      taken[2] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  QAbstractSeries *QLegendMarkerPrivate::series()
  QAbstractSeries *series() override {
    if (taken[0]) {
      int handled = 0;
      CuteQLegendMarkerPrivateCall0 call = reinterpret_cast<CuteQLegendMarkerPrivateCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAbstractSeries *>(given);
    }
    return {};
  }

  //  QObject *QLegendMarkerPrivate::relatedObject()
  QObject *relatedObject() override {
    if (taken[1]) {
      int handled = 0;
      CuteQLegendMarkerPrivateCall1 call = reinterpret_cast<CuteQLegendMarkerPrivateCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QObject *>(given);
    }
    return {};
  }

  //  void QLegendMarkerPrivate::updated()
  void updated() override {
    if (taken[2]) {
      int handled = 0;
      CuteQLegendMarkerPrivateCall2 call = reinterpret_cast<CuteQLegendMarkerPrivateCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQLegendMarkerPrivateCall3 call = reinterpret_cast<CuteQLegendMarkerPrivateCall3>(taken[3]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQLegendMarkerPrivateCall4 call = reinterpret_cast<CuteQLegendMarkerPrivateCall4>(taken[4]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQLegendMarkerPrivateCall5 call = reinterpret_cast<CuteQLegendMarkerPrivateCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQLegendMarkerPrivateCall6 call = reinterpret_cast<CuteQLegendMarkerPrivateCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQLegendMarkerPrivateCall7 call = reinterpret_cast<CuteQLegendMarkerPrivateCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[8]) {
      int handled = 0;
      CuteQLegendMarkerPrivateCall8 call = reinterpret_cast<CuteQLegendMarkerPrivateCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[9]) {
      int handled = 0;
      CuteQLegendMarkerPrivateCall9 call = reinterpret_cast<CuteQLegendMarkerPrivateCall9>(taken[9]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QLegendMarkerPrivate::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20QLegendMarkerPrivate10metaObjectEv(
    const QLegendMarkerPrivate *self) {
  return self->metaObject();
}

//  QString QLegendMarkerPrivate::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN20QLegendMarkerPrivate2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QLegendMarkerPrivate::tr(s, c, n));
}

//  QLegendMarkerPrivate::~QLegendMarkerPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QLegendMarkerPrivateD1Ev(QLegendMarkerPrivate *self) {
  delete self;
}

//  LegendMarkerItem *QLegendMarkerPrivate::item() const
extern "C" Q_DECL_EXPORT
LegendMarkerItem *ritual_ZNK20QLegendMarkerPrivate4itemEv(
    const QLegendMarkerPrivate *self) {
  return self->item();
}

//  QAbstractSeries *QLegendMarkerPrivate::series()
extern "C" Q_DECL_EXPORT
QAbstractSeries *ritual_ZN20QLegendMarkerPrivate6seriesEv(
    QLegendMarkerPrivate *self) {
  return self->series();
}

//  QObject *QLegendMarkerPrivate::relatedObject()
extern "C" Q_DECL_EXPORT
QObject *ritual_ZN20QLegendMarkerPrivate13relatedObjectEv(
    QLegendMarkerPrivate *self) {
  return self->relatedObject();
}

//  void QLegendMarkerPrivate::invalidateLegend()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QLegendMarkerPrivate16invalidateLegendEv(
    QLegendMarkerPrivate *self) {
  self->invalidateLegend();
}

//  void QLegendMarkerPrivate::invalidateAllItems()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QLegendMarkerPrivate18invalidateAllItemsEv(
    QLegendMarkerPrivate *self) {
  self->invalidateAllItems();
}

//  void QLegendMarkerPrivate::updated()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QLegendMarkerPrivate7updatedEv(QLegendMarkerPrivate *self) {
  self->updated();
}

//  void QLegendMarkerPrivate::handleShapeChange()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QLegendMarkerPrivate17handleShapeChangeEv(
    QLegendMarkerPrivate *self) {
  self->handleShapeChange();
}

//  QLegendMarker *QLegendMarkerPrivate::q_func()
extern "C" Q_DECL_EXPORT
QLegendMarker *ritual_ZN20QLegendMarkerPrivate6q_funcEv(
    QLegendMarkerPrivate *self) {
  return self->q_func();
}

//  const QLegendMarker *QLegendMarkerPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QLegendMarker *ritual_ZNK20QLegendMarkerPrivate6q_funcEv(
    const QLegendMarkerPrivate *self) {
  return self->q_func();
}

//  a Python function taken by a CuteQLegendMarkerPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QLegendMarkerPrivate(
    QLegendMarkerPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQLegendMarkerPrivate *>(self)->take(key, call);
}
