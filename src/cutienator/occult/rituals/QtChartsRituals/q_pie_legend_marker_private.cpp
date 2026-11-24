//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/6.12.0/QtCharts/private/qpielegendmarker_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#include <QtCharts/qpielegendmarker.h>
#include <QtCharts/QtCharts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCharts/6.12.0/QtCharts/private/qpielegendmarker_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QPieLegendMarkerPrivate that Python can take functions over in. Every QPieLegendMarkerPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQPieLegendMarkerPrivateCall0)(const void *, int *);
typedef void * (*CuteQPieLegendMarkerPrivateCall1)(const void *, int *);
typedef void (*CuteQPieLegendMarkerPrivateCall2)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPieLegendMarkerPrivateCall3)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPieLegendMarkerPrivateCall4)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPieLegendMarkerPrivateCall5)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPieLegendMarkerPrivateCall6)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPieLegendMarkerPrivateCall7)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPieLegendMarkerPrivateCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPieLegendMarkerPrivateCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQPieLegendMarkerPrivate : public QPieLegendMarkerPrivate {
public:
  using QPieLegendMarkerPrivate::QPieLegendMarkerPrivate;
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

  //  QPieSeries *QPieLegendMarkerPrivate::series()
  QPieSeries *series() override {
    if (taken[0]) {
      int handled = 0;
      CuteQPieLegendMarkerPrivateCall0 call = reinterpret_cast<CuteQPieLegendMarkerPrivateCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPieSeries *>(given);
    }
    return QPieLegendMarkerPrivate::series();
  }

  //  QObject *QPieLegendMarkerPrivate::relatedObject()
  QObject *relatedObject() override {
    if (taken[1]) {
      int handled = 0;
      CuteQPieLegendMarkerPrivateCall1 call = reinterpret_cast<CuteQPieLegendMarkerPrivateCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QObject *>(given);
    }
    return QPieLegendMarkerPrivate::relatedObject();
  }

  //  void QPieLegendMarkerPrivate::updated()
  void updated() override {
    if (taken[2]) {
      int handled = 0;
      CuteQPieLegendMarkerPrivateCall2 call = reinterpret_cast<CuteQPieLegendMarkerPrivateCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QPieLegendMarkerPrivate::updated();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQPieLegendMarkerPrivateCall3 call = reinterpret_cast<CuteQPieLegendMarkerPrivateCall3>(taken[3]);
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
      CuteQPieLegendMarkerPrivateCall4 call = reinterpret_cast<CuteQPieLegendMarkerPrivateCall4>(taken[4]);
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
      CuteQPieLegendMarkerPrivateCall5 call = reinterpret_cast<CuteQPieLegendMarkerPrivateCall5>(taken[5]);
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
      CuteQPieLegendMarkerPrivateCall6 call = reinterpret_cast<CuteQPieLegendMarkerPrivateCall6>(taken[6]);
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
      CuteQPieLegendMarkerPrivateCall7 call = reinterpret_cast<CuteQPieLegendMarkerPrivateCall7>(taken[7]);
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
      CuteQPieLegendMarkerPrivateCall8 call = reinterpret_cast<CuteQPieLegendMarkerPrivateCall8>(taken[8]);
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
      CuteQPieLegendMarkerPrivateCall9 call = reinterpret_cast<CuteQPieLegendMarkerPrivateCall9>(taken[9]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QPieLegendMarkerPrivate::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK23QPieLegendMarkerPrivate10metaObjectEv(
    const QPieLegendMarkerPrivate *self) {
  return self->metaObject();
}

//  QString QPieLegendMarkerPrivate::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN23QPieLegendMarkerPrivate2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QPieLegendMarkerPrivate::tr(s, c, n));
}

//  QPieLegendMarkerPrivate::QPieLegendMarkerPrivate(QPieLegendMarker *q,
//      QPieSeries *series, QPieSlice *slice, QLegend *legend)
extern "C" Q_DECL_EXPORT
QPieLegendMarkerPrivate *ritual_ZN23QPieLegendMarkerPrivateC1EP16QPieLegendMarkerP10QPieSeriesP9QPieSliceP7QLegend(
    QPieLegendMarker *q,
    QPieSeries *series,
    QPieSlice *slice,
    QLegend *legend) {
  return new CuteQPieLegendMarkerPrivate(q, series, slice, legend);
}

//  QPieLegendMarkerPrivate::~QPieLegendMarkerPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QPieLegendMarkerPrivateD1Ev(QPieLegendMarkerPrivate *self) {
  delete self;
}

//  QPieSeries *QPieLegendMarkerPrivate::series()
extern "C" Q_DECL_EXPORT
QPieSeries *ritual_ZN23QPieLegendMarkerPrivate6seriesEv(
    QPieLegendMarkerPrivate *self) {
  return self->series();
}

//  QObject *QPieLegendMarkerPrivate::relatedObject()
extern "C" Q_DECL_EXPORT
QObject *ritual_ZN23QPieLegendMarkerPrivate13relatedObjectEv(
    QPieLegendMarkerPrivate *self) {
  return self->relatedObject();
}

//  void QPieLegendMarkerPrivate::updated()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QPieLegendMarkerPrivate7updatedEv(
    QPieLegendMarkerPrivate *self) {
  self->updated();
}

//  QPieLegendMarker *QPieLegendMarkerPrivate::q_func()
extern "C" Q_DECL_EXPORT
QPieLegendMarker *ritual_ZN23QPieLegendMarkerPrivate6q_funcEv(
    QPieLegendMarkerPrivate *self) {
  return self->q_func();
}

//  const QPieLegendMarker *QPieLegendMarkerPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QPieLegendMarker *ritual_ZNK23QPieLegendMarkerPrivate6q_funcEv(
    const QPieLegendMarkerPrivate *self) {
  return self->q_func();
}

//  a Python function taken by a CuteQPieLegendMarkerPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPieLegendMarkerPrivate(
    QPieLegendMarkerPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPieLegendMarkerPrivate *>(self)->take(key, call);
}

//  QPieSeries *QPieLegendMarkerPrivate::series()
extern "C" Q_DECL_EXPORT
QPieSeries *ritual_own_ZN23QPieLegendMarkerPrivate6seriesEv(
    QPieLegendMarkerPrivate *self) {
  return self->QPieLegendMarkerPrivate::series();
}

//  QObject *QPieLegendMarkerPrivate::relatedObject()
extern "C" Q_DECL_EXPORT
QObject *ritual_own_ZN23QPieLegendMarkerPrivate13relatedObjectEv(
    QPieLegendMarkerPrivate *self) {
  return self->QPieLegendMarkerPrivate::relatedObject();
}

//  void QPieLegendMarkerPrivate::updated()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QPieLegendMarkerPrivate7updatedEv(
    QPieLegendMarkerPrivate *self) {
  self->QPieLegendMarkerPrivate::updated();
}
