//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/6.12.0/QtCharts/private/qboxplotlegendmarker_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCharts/qchartglobal.h>
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#if QT_CONFIG(charts_boxplot_chart)
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#if QT_CONFIG(charts_boxplot_chart)
#include <QtCharts/qboxplotlegendmarker.h>
#endif
#include <QtCharts/QtCharts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCharts/6.12.0/QtCharts/private/qboxplotlegendmarker_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QBoxPlotLegendMarkerPrivate that Python can take functions over in. Every QBoxPlotLegendMarkerPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQBoxPlotLegendMarkerPrivateCall0)(const void *, int *);
typedef void * (*CuteQBoxPlotLegendMarkerPrivateCall1)(const void *, int *);
typedef void (*CuteQBoxPlotLegendMarkerPrivateCall2)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQBoxPlotLegendMarkerPrivateCall3)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQBoxPlotLegendMarkerPrivateCall4)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBoxPlotLegendMarkerPrivateCall5)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBoxPlotLegendMarkerPrivateCall6)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBoxPlotLegendMarkerPrivateCall7)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBoxPlotLegendMarkerPrivateCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBoxPlotLegendMarkerPrivateCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQBoxPlotLegendMarkerPrivate : public QBoxPlotLegendMarkerPrivate {
public:
  using QBoxPlotLegendMarkerPrivate::QBoxPlotLegendMarkerPrivate;
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

  //  QAbstractSeries *QBoxPlotLegendMarkerPrivate::series()
  QAbstractSeries *series() override {
    if (taken[0]) {
      int handled = 0;
      CuteQBoxPlotLegendMarkerPrivateCall0 call = reinterpret_cast<CuteQBoxPlotLegendMarkerPrivateCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAbstractSeries *>(given);
    }
    return QBoxPlotLegendMarkerPrivate::series();
  }

  //  QObject *QBoxPlotLegendMarkerPrivate::relatedObject()
  QObject *relatedObject() override {
    if (taken[1]) {
      int handled = 0;
      CuteQBoxPlotLegendMarkerPrivateCall1 call = reinterpret_cast<CuteQBoxPlotLegendMarkerPrivateCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QObject *>(given);
    }
    return QBoxPlotLegendMarkerPrivate::relatedObject();
  }

  //  void QBoxPlotLegendMarkerPrivate::updated()
  void updated() override {
    if (taken[2]) {
      int handled = 0;
      CuteQBoxPlotLegendMarkerPrivateCall2 call = reinterpret_cast<CuteQBoxPlotLegendMarkerPrivateCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QBoxPlotLegendMarkerPrivate::updated();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQBoxPlotLegendMarkerPrivateCall3 call = reinterpret_cast<CuteQBoxPlotLegendMarkerPrivateCall3>(taken[3]);
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
      CuteQBoxPlotLegendMarkerPrivateCall4 call = reinterpret_cast<CuteQBoxPlotLegendMarkerPrivateCall4>(taken[4]);
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
      CuteQBoxPlotLegendMarkerPrivateCall5 call = reinterpret_cast<CuteQBoxPlotLegendMarkerPrivateCall5>(taken[5]);
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
      CuteQBoxPlotLegendMarkerPrivateCall6 call = reinterpret_cast<CuteQBoxPlotLegendMarkerPrivateCall6>(taken[6]);
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
      CuteQBoxPlotLegendMarkerPrivateCall7 call = reinterpret_cast<CuteQBoxPlotLegendMarkerPrivateCall7>(taken[7]);
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
      CuteQBoxPlotLegendMarkerPrivateCall8 call = reinterpret_cast<CuteQBoxPlotLegendMarkerPrivateCall8>(taken[8]);
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
      CuteQBoxPlotLegendMarkerPrivateCall9 call = reinterpret_cast<CuteQBoxPlotLegendMarkerPrivateCall9>(taken[9]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QBoxPlotLegendMarkerPrivate::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK27QBoxPlotLegendMarkerPrivate10metaObjectEv(
    const QBoxPlotLegendMarkerPrivate *self) {
  return self->metaObject();
}

//  void *QBoxPlotLegendMarkerPrivate::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN27QBoxPlotLegendMarkerPrivate11qt_metacastEPKc(
    QBoxPlotLegendMarkerPrivate *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QBoxPlotLegendMarkerPrivate::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN27QBoxPlotLegendMarkerPrivate11qt_metacallEN11QMetaObject4CallEiPPv(
    QBoxPlotLegendMarkerPrivate *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QBoxPlotLegendMarkerPrivate::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN27QBoxPlotLegendMarkerPrivate2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QBoxPlotLegendMarkerPrivate::tr(s, c, n));
}

//  QBoxPlotLegendMarkerPrivate::QBoxPlotLegendMarkerPrivate(QBoxPlotLegendMa
//      rker *q, QBoxPlotSeries *series, QLegend *legend)
extern "C" Q_DECL_EXPORT
QBoxPlotLegendMarkerPrivate *ritual_ZN27QBoxPlotLegendMarkerPrivateC1EP20QBoxPlotLegendMarkerP14QBoxPlotSeriesP7QLegend(
    QBoxPlotLegendMarker *q,
    QBoxPlotSeries *series,
    QLegend *legend) {
  return new CuteQBoxPlotLegendMarkerPrivate(q, series, legend);
}

//  QBoxPlotLegendMarkerPrivate::~QBoxPlotLegendMarkerPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QBoxPlotLegendMarkerPrivateD1Ev(
    QBoxPlotLegendMarkerPrivate *self) {
  delete self;
}

//  QAbstractSeries *QBoxPlotLegendMarkerPrivate::series()
extern "C" Q_DECL_EXPORT
QAbstractSeries *ritual_ZN27QBoxPlotLegendMarkerPrivate6seriesEv(
    QBoxPlotLegendMarkerPrivate *self) {
  return self->series();
}

//  QObject *QBoxPlotLegendMarkerPrivate::relatedObject()
extern "C" Q_DECL_EXPORT
QObject *ritual_ZN27QBoxPlotLegendMarkerPrivate13relatedObjectEv(
    QBoxPlotLegendMarkerPrivate *self) {
  return self->relatedObject();
}

//  void QBoxPlotLegendMarkerPrivate::updated()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QBoxPlotLegendMarkerPrivate7updatedEv(
    QBoxPlotLegendMarkerPrivate *self) {
  self->updated();
}

//  QBoxPlotLegendMarker *QBoxPlotLegendMarkerPrivate::q_func()
extern "C" Q_DECL_EXPORT
QBoxPlotLegendMarker *ritual_ZN27QBoxPlotLegendMarkerPrivate6q_funcEv(
    QBoxPlotLegendMarkerPrivate *self) {
  return self->q_func();
}

//  const QBoxPlotLegendMarker *QBoxPlotLegendMarkerPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QBoxPlotLegendMarker *ritual_ZNK27QBoxPlotLegendMarkerPrivate6q_funcEv(
    const QBoxPlotLegendMarkerPrivate *self) {
  return self->q_func();
}

//  a Python function taken by a CuteQBoxPlotLegendMarkerPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QBoxPlotLegendMarkerPrivate(
    QBoxPlotLegendMarkerPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQBoxPlotLegendMarkerPrivate *>(self)->take(key, call);
}

//  QAbstractSeries *QBoxPlotLegendMarkerPrivate::series()
extern "C" Q_DECL_EXPORT
QAbstractSeries *ritual_own_ZN27QBoxPlotLegendMarkerPrivate6seriesEv(
    QBoxPlotLegendMarkerPrivate *self) {
  return self->QBoxPlotLegendMarkerPrivate::series();
}

//  QObject *QBoxPlotLegendMarkerPrivate::relatedObject()
extern "C" Q_DECL_EXPORT
QObject *ritual_own_ZN27QBoxPlotLegendMarkerPrivate13relatedObjectEv(
    QBoxPlotLegendMarkerPrivate *self) {
  return self->QBoxPlotLegendMarkerPrivate::relatedObject();
}

//  void QBoxPlotLegendMarkerPrivate::updated()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN27QBoxPlotLegendMarkerPrivate7updatedEv(
    QBoxPlotLegendMarkerPrivate *self) {
  self->QBoxPlotLegendMarkerPrivate::updated();
}

#endif  // QT_CONFIG(charts_boxplot_chart)
