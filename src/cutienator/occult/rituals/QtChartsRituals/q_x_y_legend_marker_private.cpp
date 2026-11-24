//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/6.12.0/QtCharts/private/qxylegendmarker_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#include <QtCharts/qxylegendmarker.h>
#include <QtCharts/QtCharts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCharts/6.12.0/QtCharts/private/qxylegendmarker_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QXYLegendMarkerPrivate that Python can take functions over in. Every QXYLegendMarkerPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQXYLegendMarkerPrivateCall0)(const void *, int *);
typedef void * (*CuteQXYLegendMarkerPrivateCall1)(const void *, int *);
typedef void (*CuteQXYLegendMarkerPrivateCall2)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQXYLegendMarkerPrivateCall3)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQXYLegendMarkerPrivateCall4)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQXYLegendMarkerPrivateCall5)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQXYLegendMarkerPrivateCall6)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQXYLegendMarkerPrivateCall7)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQXYLegendMarkerPrivateCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQXYLegendMarkerPrivateCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQXYLegendMarkerPrivate : public QXYLegendMarkerPrivate {
public:
  using QXYLegendMarkerPrivate::QXYLegendMarkerPrivate;
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

  //  QAbstractSeries *QXYLegendMarkerPrivate::series()
  QAbstractSeries *series() override {
    if (taken[0]) {
      int handled = 0;
      CuteQXYLegendMarkerPrivateCall0 call = reinterpret_cast<CuteQXYLegendMarkerPrivateCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAbstractSeries *>(given);
    }
    return QXYLegendMarkerPrivate::series();
  }

  //  QObject *QXYLegendMarkerPrivate::relatedObject()
  QObject *relatedObject() override {
    if (taken[1]) {
      int handled = 0;
      CuteQXYLegendMarkerPrivateCall1 call = reinterpret_cast<CuteQXYLegendMarkerPrivateCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QObject *>(given);
    }
    return QXYLegendMarkerPrivate::relatedObject();
  }

  //  void QXYLegendMarkerPrivate::updated()
  void updated() override {
    if (taken[2]) {
      int handled = 0;
      CuteQXYLegendMarkerPrivateCall2 call = reinterpret_cast<CuteQXYLegendMarkerPrivateCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QXYLegendMarkerPrivate::updated();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQXYLegendMarkerPrivateCall3 call = reinterpret_cast<CuteQXYLegendMarkerPrivateCall3>(taken[3]);
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
      CuteQXYLegendMarkerPrivateCall4 call = reinterpret_cast<CuteQXYLegendMarkerPrivateCall4>(taken[4]);
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
      CuteQXYLegendMarkerPrivateCall5 call = reinterpret_cast<CuteQXYLegendMarkerPrivateCall5>(taken[5]);
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
      CuteQXYLegendMarkerPrivateCall6 call = reinterpret_cast<CuteQXYLegendMarkerPrivateCall6>(taken[6]);
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
      CuteQXYLegendMarkerPrivateCall7 call = reinterpret_cast<CuteQXYLegendMarkerPrivateCall7>(taken[7]);
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
      CuteQXYLegendMarkerPrivateCall8 call = reinterpret_cast<CuteQXYLegendMarkerPrivateCall8>(taken[8]);
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
      CuteQXYLegendMarkerPrivateCall9 call = reinterpret_cast<CuteQXYLegendMarkerPrivateCall9>(taken[9]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QXYLegendMarkerPrivate::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK22QXYLegendMarkerPrivate10metaObjectEv(
    const QXYLegendMarkerPrivate *self) {
  return self->metaObject();
}

//  QString QXYLegendMarkerPrivate::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN22QXYLegendMarkerPrivate2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QXYLegendMarkerPrivate::tr(s, c, n));
}

//  QXYLegendMarkerPrivate::QXYLegendMarkerPrivate(QXYLegendMarker *q,
//      QXYSeries *series, QLegend *legend)
extern "C" Q_DECL_EXPORT
QXYLegendMarkerPrivate *ritual_ZN22QXYLegendMarkerPrivateC1EP15QXYLegendMarkerP9QXYSeriesP7QLegend(
    QXYLegendMarker *q,
    QXYSeries *series,
    QLegend *legend) {
  return new CuteQXYLegendMarkerPrivate(q, series, legend);
}

//  QXYLegendMarkerPrivate::~QXYLegendMarkerPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QXYLegendMarkerPrivateD1Ev(QXYLegendMarkerPrivate *self) {
  delete self;
}

//  QAbstractSeries *QXYLegendMarkerPrivate::series()
extern "C" Q_DECL_EXPORT
QAbstractSeries *ritual_ZN22QXYLegendMarkerPrivate6seriesEv(
    QXYLegendMarkerPrivate *self) {
  return self->series();
}

//  QObject *QXYLegendMarkerPrivate::relatedObject()
extern "C" Q_DECL_EXPORT
QObject *ritual_ZN22QXYLegendMarkerPrivate13relatedObjectEv(
    QXYLegendMarkerPrivate *self) {
  return self->relatedObject();
}

//  void QXYLegendMarkerPrivate::updated()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QXYLegendMarkerPrivate7updatedEv(
    QXYLegendMarkerPrivate *self) {
  self->updated();
}

//  QXYLegendMarker *QXYLegendMarkerPrivate::q_func()
extern "C" Q_DECL_EXPORT
QXYLegendMarker *ritual_ZN22QXYLegendMarkerPrivate6q_funcEv(
    QXYLegendMarkerPrivate *self) {
  return self->q_func();
}

//  const QXYLegendMarker *QXYLegendMarkerPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QXYLegendMarker *ritual_ZNK22QXYLegendMarkerPrivate6q_funcEv(
    const QXYLegendMarkerPrivate *self) {
  return self->q_func();
}

//  a Python function taken by a CuteQXYLegendMarkerPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QXYLegendMarkerPrivate(
    QXYLegendMarkerPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQXYLegendMarkerPrivate *>(self)->take(key, call);
}

//  QAbstractSeries *QXYLegendMarkerPrivate::series()
extern "C" Q_DECL_EXPORT
QAbstractSeries *ritual_own_ZN22QXYLegendMarkerPrivate6seriesEv(
    QXYLegendMarkerPrivate *self) {
  return self->QXYLegendMarkerPrivate::series();
}

//  QObject *QXYLegendMarkerPrivate::relatedObject()
extern "C" Q_DECL_EXPORT
QObject *ritual_own_ZN22QXYLegendMarkerPrivate13relatedObjectEv(
    QXYLegendMarkerPrivate *self) {
  return self->QXYLegendMarkerPrivate::relatedObject();
}

//  void QXYLegendMarkerPrivate::updated()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QXYLegendMarkerPrivate7updatedEv(
    QXYLegendMarkerPrivate *self) {
  self->QXYLegendMarkerPrivate::updated();
}
