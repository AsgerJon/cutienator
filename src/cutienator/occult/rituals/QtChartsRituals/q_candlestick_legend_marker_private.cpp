//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/6.12.0/QtCharts/private/qcandlesticklegendmarker_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#include <QtCharts/qcandlesticklegendmarker.h>
#include <QtCharts/QtCharts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCharts/6.12.0/QtCharts/private/qcandlesticklegendmarker_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QCandlestickLegendMarkerPrivate that Python can take functions over in. Every QCandlestickLegendMarkerPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQCandlestickLegendMarkerPrivateCall0)(const void *, int *);
typedef void * (*CuteQCandlestickLegendMarkerPrivateCall1)(const void *, int *);
typedef void (*CuteQCandlestickLegendMarkerPrivateCall2)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQCandlestickLegendMarkerPrivateCall3)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQCandlestickLegendMarkerPrivateCall4)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCandlestickLegendMarkerPrivateCall5)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCandlestickLegendMarkerPrivateCall6)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCandlestickLegendMarkerPrivateCall7)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCandlestickLegendMarkerPrivateCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCandlestickLegendMarkerPrivateCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQCandlestickLegendMarkerPrivate : public QCandlestickLegendMarkerPrivate {
public:
  using QCandlestickLegendMarkerPrivate::QCandlestickLegendMarkerPrivate;
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

  //  QAbstractSeries *QCandlestickLegendMarkerPrivate::series()
  QAbstractSeries *series() override {
    if (taken[0]) {
      int handled = 0;
      CuteQCandlestickLegendMarkerPrivateCall0 call = reinterpret_cast<CuteQCandlestickLegendMarkerPrivateCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAbstractSeries *>(given);
    }
    return QCandlestickLegendMarkerPrivate::series();
  }

  //  QObject *QCandlestickLegendMarkerPrivate::relatedObject()
  QObject *relatedObject() override {
    if (taken[1]) {
      int handled = 0;
      CuteQCandlestickLegendMarkerPrivateCall1 call = reinterpret_cast<CuteQCandlestickLegendMarkerPrivateCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QObject *>(given);
    }
    return QCandlestickLegendMarkerPrivate::relatedObject();
  }

  //  void QCandlestickLegendMarkerPrivate::updated()
  void updated() override {
    if (taken[2]) {
      int handled = 0;
      CuteQCandlestickLegendMarkerPrivateCall2 call = reinterpret_cast<CuteQCandlestickLegendMarkerPrivateCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QCandlestickLegendMarkerPrivate::updated();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQCandlestickLegendMarkerPrivateCall3 call = reinterpret_cast<CuteQCandlestickLegendMarkerPrivateCall3>(taken[3]);
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
      CuteQCandlestickLegendMarkerPrivateCall4 call = reinterpret_cast<CuteQCandlestickLegendMarkerPrivateCall4>(taken[4]);
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
      CuteQCandlestickLegendMarkerPrivateCall5 call = reinterpret_cast<CuteQCandlestickLegendMarkerPrivateCall5>(taken[5]);
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
      CuteQCandlestickLegendMarkerPrivateCall6 call = reinterpret_cast<CuteQCandlestickLegendMarkerPrivateCall6>(taken[6]);
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
      CuteQCandlestickLegendMarkerPrivateCall7 call = reinterpret_cast<CuteQCandlestickLegendMarkerPrivateCall7>(taken[7]);
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
      CuteQCandlestickLegendMarkerPrivateCall8 call = reinterpret_cast<CuteQCandlestickLegendMarkerPrivateCall8>(taken[8]);
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
      CuteQCandlestickLegendMarkerPrivateCall9 call = reinterpret_cast<CuteQCandlestickLegendMarkerPrivateCall9>(taken[9]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QCandlestickLegendMarkerPrivate::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK31QCandlestickLegendMarkerPrivate10metaObjectEv(
    const QCandlestickLegendMarkerPrivate *self) {
  return self->metaObject();
}

//  QString QCandlestickLegendMarkerPrivate::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN31QCandlestickLegendMarkerPrivate2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QCandlestickLegendMarkerPrivate::tr(s, c, n));
}

//  QCandlestickLegendMarkerPrivate::QCandlestickLegendMarkerPrivate(QCandles
//      tickLegendMarker *q, QCandlestickSeries *series, QLegend *legend)
extern "C" Q_DECL_EXPORT
QCandlestickLegendMarkerPrivate *ritual_ZN31QCandlestickLegendMarkerPrivateC1EP24QCandlestickLegendMarkerP18QCandlestickSeriesP7QLegend(
    QCandlestickLegendMarker *q,
    QCandlestickSeries *series,
    QLegend *legend) {
  return new CuteQCandlestickLegendMarkerPrivate(q, series, legend);
}

//  QCandlestickLegendMarkerPrivate::~QCandlestickLegendMarkerPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QCandlestickLegendMarkerPrivateD1Ev(
    QCandlestickLegendMarkerPrivate *self) {
  delete self;
}

//  QAbstractSeries *QCandlestickLegendMarkerPrivate::series()
extern "C" Q_DECL_EXPORT
QAbstractSeries *ritual_ZN31QCandlestickLegendMarkerPrivate6seriesEv(
    QCandlestickLegendMarkerPrivate *self) {
  return self->series();
}

//  QObject *QCandlestickLegendMarkerPrivate::relatedObject()
extern "C" Q_DECL_EXPORT
QObject *ritual_ZN31QCandlestickLegendMarkerPrivate13relatedObjectEv(
    QCandlestickLegendMarkerPrivate *self) {
  return self->relatedObject();
}

//  void QCandlestickLegendMarkerPrivate::updated()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QCandlestickLegendMarkerPrivate7updatedEv(
    QCandlestickLegendMarkerPrivate *self) {
  self->updated();
}

//  QCandlestickLegendMarker *QCandlestickLegendMarkerPrivate::q_func()
extern "C" Q_DECL_EXPORT
QCandlestickLegendMarker *ritual_ZN31QCandlestickLegendMarkerPrivate6q_funcEv(
    QCandlestickLegendMarkerPrivate *self) {
  return self->q_func();
}

//  const QCandlestickLegendMarker *QCandlestickLegendMarkerPrivate::q_func()
//      const
extern "C" Q_DECL_EXPORT
const QCandlestickLegendMarker *ritual_ZNK31QCandlestickLegendMarkerPrivate6q_funcEv(
    const QCandlestickLegendMarkerPrivate *self) {
  return self->q_func();
}

//  a Python function taken by a CuteQCandlestickLegendMarkerPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QCandlestickLegendMarkerPrivate(
    QCandlestickLegendMarkerPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQCandlestickLegendMarkerPrivate *>(self)->take(key, call);
}

//  QAbstractSeries *QCandlestickLegendMarkerPrivate::series()
extern "C" Q_DECL_EXPORT
QAbstractSeries *ritual_own_ZN31QCandlestickLegendMarkerPrivate6seriesEv(
    QCandlestickLegendMarkerPrivate *self) {
  return self->QCandlestickLegendMarkerPrivate::series();
}

//  QObject *QCandlestickLegendMarkerPrivate::relatedObject()
extern "C" Q_DECL_EXPORT
QObject *ritual_own_ZN31QCandlestickLegendMarkerPrivate13relatedObjectEv(
    QCandlestickLegendMarkerPrivate *self) {
  return self->QCandlestickLegendMarkerPrivate::relatedObject();
}

//  void QCandlestickLegendMarkerPrivate::updated()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN31QCandlestickLegendMarkerPrivate7updatedEv(
    QCandlestickLegendMarkerPrivate *self) {
  self->QCandlestickLegendMarkerPrivate::updated();
}
