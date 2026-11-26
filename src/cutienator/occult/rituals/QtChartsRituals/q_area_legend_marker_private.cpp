//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/6.12.0/QtCharts/private/qarealegendmarker_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCharts/qchartglobal.h>
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#if QT_CONFIG(charts_area_chart)
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#if QT_CONFIG(charts_area_chart)
#include <QtCharts/qarealegendmarker.h>
#endif
#include <QtCharts/QtCharts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCharts/6.12.0/QtCharts/private/qarealegendmarker_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QAreaLegendMarkerPrivate that Python can take functions over in. Every QAreaLegendMarkerPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQAreaLegendMarkerPrivateCall0)(const void *, int *);
typedef void * (*CuteQAreaLegendMarkerPrivateCall1)(const void *, int *);
typedef void (*CuteQAreaLegendMarkerPrivateCall2)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAreaLegendMarkerPrivateCall3)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAreaLegendMarkerPrivateCall4)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAreaLegendMarkerPrivateCall5)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAreaLegendMarkerPrivateCall6)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAreaLegendMarkerPrivateCall7)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAreaLegendMarkerPrivateCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAreaLegendMarkerPrivateCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQAreaLegendMarkerPrivate : public QAreaLegendMarkerPrivate {
public:
  using QAreaLegendMarkerPrivate::QAreaLegendMarkerPrivate;
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

  //  QAreaSeries *QAreaLegendMarkerPrivate::series()
  QAreaSeries *series() override {
    if (taken[0]) {
      int handled = 0;
      CuteQAreaLegendMarkerPrivateCall0 call = reinterpret_cast<CuteQAreaLegendMarkerPrivateCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAreaSeries *>(given);
    }
    return QAreaLegendMarkerPrivate::series();
  }

  //  QObject *QAreaLegendMarkerPrivate::relatedObject()
  QObject *relatedObject() override {
    if (taken[1]) {
      int handled = 0;
      CuteQAreaLegendMarkerPrivateCall1 call = reinterpret_cast<CuteQAreaLegendMarkerPrivateCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QObject *>(given);
    }
    return QAreaLegendMarkerPrivate::relatedObject();
  }

  //  void QAreaLegendMarkerPrivate::updated()
  void updated() override {
    if (taken[2]) {
      int handled = 0;
      CuteQAreaLegendMarkerPrivateCall2 call = reinterpret_cast<CuteQAreaLegendMarkerPrivateCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QAreaLegendMarkerPrivate::updated();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQAreaLegendMarkerPrivateCall3 call = reinterpret_cast<CuteQAreaLegendMarkerPrivateCall3>(taken[3]);
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
      CuteQAreaLegendMarkerPrivateCall4 call = reinterpret_cast<CuteQAreaLegendMarkerPrivateCall4>(taken[4]);
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
      CuteQAreaLegendMarkerPrivateCall5 call = reinterpret_cast<CuteQAreaLegendMarkerPrivateCall5>(taken[5]);
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
      CuteQAreaLegendMarkerPrivateCall6 call = reinterpret_cast<CuteQAreaLegendMarkerPrivateCall6>(taken[6]);
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
      CuteQAreaLegendMarkerPrivateCall7 call = reinterpret_cast<CuteQAreaLegendMarkerPrivateCall7>(taken[7]);
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
      CuteQAreaLegendMarkerPrivateCall8 call = reinterpret_cast<CuteQAreaLegendMarkerPrivateCall8>(taken[8]);
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
      CuteQAreaLegendMarkerPrivateCall9 call = reinterpret_cast<CuteQAreaLegendMarkerPrivateCall9>(taken[9]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QAreaLegendMarkerPrivate::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK24QAreaLegendMarkerPrivate10metaObjectEv(
    const QAreaLegendMarkerPrivate *self) {
  return self->metaObject();
}

//  void *QAreaLegendMarkerPrivate::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN24QAreaLegendMarkerPrivate11qt_metacastEPKc(
    QAreaLegendMarkerPrivate *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QAreaLegendMarkerPrivate::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN24QAreaLegendMarkerPrivate11qt_metacallEN11QMetaObject4CallEiPPv(
    QAreaLegendMarkerPrivate *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QAreaLegendMarkerPrivate::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN24QAreaLegendMarkerPrivate2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QAreaLegendMarkerPrivate::tr(s, c, n));
}

//  QAreaLegendMarkerPrivate::QAreaLegendMarkerPrivate(QAreaLegendMarker *q,
//      QAreaSeries *series, QLegend *legend)
extern "C" Q_DECL_EXPORT
QAreaLegendMarkerPrivate *ritual_ZN24QAreaLegendMarkerPrivateC1EP17QAreaLegendMarkerP11QAreaSeriesP7QLegend(
    QAreaLegendMarker *q,
    QAreaSeries *series,
    QLegend *legend) {
  return new CuteQAreaLegendMarkerPrivate(q, series, legend);
}

//  QAreaLegendMarkerPrivate::~QAreaLegendMarkerPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAreaLegendMarkerPrivateD1Ev(
    QAreaLegendMarkerPrivate *self) {
  delete self;
}

//  QAreaSeries *QAreaLegendMarkerPrivate::series()
extern "C" Q_DECL_EXPORT
QAreaSeries *ritual_ZN24QAreaLegendMarkerPrivate6seriesEv(
    QAreaLegendMarkerPrivate *self) {
  return self->series();
}

//  QObject *QAreaLegendMarkerPrivate::relatedObject()
extern "C" Q_DECL_EXPORT
QObject *ritual_ZN24QAreaLegendMarkerPrivate13relatedObjectEv(
    QAreaLegendMarkerPrivate *self) {
  return self->relatedObject();
}

//  void QAreaLegendMarkerPrivate::updated()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAreaLegendMarkerPrivate7updatedEv(
    QAreaLegendMarkerPrivate *self) {
  self->updated();
}

//  QAreaLegendMarker *QAreaLegendMarkerPrivate::q_func()
extern "C" Q_DECL_EXPORT
QAreaLegendMarker *ritual_ZN24QAreaLegendMarkerPrivate6q_funcEv(
    QAreaLegendMarkerPrivate *self) {
  return self->q_func();
}

//  const QAreaLegendMarker *QAreaLegendMarkerPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QAreaLegendMarker *ritual_ZNK24QAreaLegendMarkerPrivate6q_funcEv(
    const QAreaLegendMarkerPrivate *self) {
  return self->q_func();
}

//  a Python function taken by a CuteQAreaLegendMarkerPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAreaLegendMarkerPrivate(
    QAreaLegendMarkerPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAreaLegendMarkerPrivate *>(self)->take(key, call);
}

//  QAreaSeries *QAreaLegendMarkerPrivate::series()
extern "C" Q_DECL_EXPORT
QAreaSeries *ritual_own_ZN24QAreaLegendMarkerPrivate6seriesEv(
    QAreaLegendMarkerPrivate *self) {
  return self->QAreaLegendMarkerPrivate::series();
}

//  QObject *QAreaLegendMarkerPrivate::relatedObject()
extern "C" Q_DECL_EXPORT
QObject *ritual_own_ZN24QAreaLegendMarkerPrivate13relatedObjectEv(
    QAreaLegendMarkerPrivate *self) {
  return self->QAreaLegendMarkerPrivate::relatedObject();
}

//  void QAreaLegendMarkerPrivate::updated()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QAreaLegendMarkerPrivate7updatedEv(
    QAreaLegendMarkerPrivate *self) {
  self->QAreaLegendMarkerPrivate::updated();
}

#endif  // QT_CONFIG(charts_area_chart)
