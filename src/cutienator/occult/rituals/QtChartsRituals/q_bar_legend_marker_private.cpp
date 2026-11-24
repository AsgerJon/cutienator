//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/6.12.0/QtCharts/private/qbarlegendmarker_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#include <QtCharts/qbarlegendmarker.h>
#include <QtCharts/QtCharts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCharts/6.12.0/QtCharts/private/qbarlegendmarker_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QBarLegendMarkerPrivate that Python can take functions over in. Every QBarLegendMarkerPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQBarLegendMarkerPrivateCall0)(const void *, int *);
typedef void * (*CuteQBarLegendMarkerPrivateCall1)(const void *, int *);
typedef void (*CuteQBarLegendMarkerPrivateCall2)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQBarLegendMarkerPrivateCall3)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQBarLegendMarkerPrivateCall4)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBarLegendMarkerPrivateCall5)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBarLegendMarkerPrivateCall6)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBarLegendMarkerPrivateCall7)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBarLegendMarkerPrivateCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBarLegendMarkerPrivateCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQBarLegendMarkerPrivate : public QBarLegendMarkerPrivate {
public:
  using QBarLegendMarkerPrivate::QBarLegendMarkerPrivate;
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

  //  QAbstractBarSeries *QBarLegendMarkerPrivate::series()
  QAbstractBarSeries *series() override {
    if (taken[0]) {
      int handled = 0;
      CuteQBarLegendMarkerPrivateCall0 call = reinterpret_cast<CuteQBarLegendMarkerPrivateCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAbstractBarSeries *>(given);
    }
    return QBarLegendMarkerPrivate::series();
  }

  //  QObject *QBarLegendMarkerPrivate::relatedObject()
  QObject *relatedObject() override {
    if (taken[1]) {
      int handled = 0;
      CuteQBarLegendMarkerPrivateCall1 call = reinterpret_cast<CuteQBarLegendMarkerPrivateCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QObject *>(given);
    }
    return QBarLegendMarkerPrivate::relatedObject();
  }

  //  void QBarLegendMarkerPrivate::updated()
  void updated() override {
    if (taken[2]) {
      int handled = 0;
      CuteQBarLegendMarkerPrivateCall2 call = reinterpret_cast<CuteQBarLegendMarkerPrivateCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QBarLegendMarkerPrivate::updated();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQBarLegendMarkerPrivateCall3 call = reinterpret_cast<CuteQBarLegendMarkerPrivateCall3>(taken[3]);
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
      CuteQBarLegendMarkerPrivateCall4 call = reinterpret_cast<CuteQBarLegendMarkerPrivateCall4>(taken[4]);
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
      CuteQBarLegendMarkerPrivateCall5 call = reinterpret_cast<CuteQBarLegendMarkerPrivateCall5>(taken[5]);
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
      CuteQBarLegendMarkerPrivateCall6 call = reinterpret_cast<CuteQBarLegendMarkerPrivateCall6>(taken[6]);
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
      CuteQBarLegendMarkerPrivateCall7 call = reinterpret_cast<CuteQBarLegendMarkerPrivateCall7>(taken[7]);
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
      CuteQBarLegendMarkerPrivateCall8 call = reinterpret_cast<CuteQBarLegendMarkerPrivateCall8>(taken[8]);
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
      CuteQBarLegendMarkerPrivateCall9 call = reinterpret_cast<CuteQBarLegendMarkerPrivateCall9>(taken[9]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QBarLegendMarkerPrivate::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK23QBarLegendMarkerPrivate10metaObjectEv(
    const QBarLegendMarkerPrivate *self) {
  return self->metaObject();
}

//  QString QBarLegendMarkerPrivate::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN23QBarLegendMarkerPrivate2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QBarLegendMarkerPrivate::tr(s, c, n));
}

//  QBarLegendMarkerPrivate::QBarLegendMarkerPrivate(QBarLegendMarker *q,
//      QAbstractBarSeries *series, QBarSet *barset, QLegend *legend)
extern "C" Q_DECL_EXPORT
QBarLegendMarkerPrivate *ritual_ZN23QBarLegendMarkerPrivateC1EP16QBarLegendMarkerP18QAbstractBarSeriesP7QBarSetP7QLegend(
    QBarLegendMarker *q,
    QAbstractBarSeries *series,
    QBarSet *barset,
    QLegend *legend) {
  return new CuteQBarLegendMarkerPrivate(q, series, barset, legend);
}

//  QBarLegendMarkerPrivate::~QBarLegendMarkerPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QBarLegendMarkerPrivateD1Ev(QBarLegendMarkerPrivate *self) {
  delete self;
}

//  QAbstractBarSeries *QBarLegendMarkerPrivate::series()
extern "C" Q_DECL_EXPORT
QAbstractBarSeries *ritual_ZN23QBarLegendMarkerPrivate6seriesEv(
    QBarLegendMarkerPrivate *self) {
  return self->series();
}

//  QObject *QBarLegendMarkerPrivate::relatedObject()
extern "C" Q_DECL_EXPORT
QObject *ritual_ZN23QBarLegendMarkerPrivate13relatedObjectEv(
    QBarLegendMarkerPrivate *self) {
  return self->relatedObject();
}

//  void QBarLegendMarkerPrivate::updated()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QBarLegendMarkerPrivate7updatedEv(
    QBarLegendMarkerPrivate *self) {
  self->updated();
}

//  QBarLegendMarker *QBarLegendMarkerPrivate::q_func()
extern "C" Q_DECL_EXPORT
QBarLegendMarker *ritual_ZN23QBarLegendMarkerPrivate6q_funcEv(
    QBarLegendMarkerPrivate *self) {
  return self->q_func();
}

//  const QBarLegendMarker *QBarLegendMarkerPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QBarLegendMarker *ritual_ZNK23QBarLegendMarkerPrivate6q_funcEv(
    const QBarLegendMarkerPrivate *self) {
  return self->q_func();
}

//  a Python function taken by a CuteQBarLegendMarkerPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QBarLegendMarkerPrivate(
    QBarLegendMarkerPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQBarLegendMarkerPrivate *>(self)->take(key, call);
}

//  QAbstractBarSeries *QBarLegendMarkerPrivate::series()
extern "C" Q_DECL_EXPORT
QAbstractBarSeries *ritual_own_ZN23QBarLegendMarkerPrivate6seriesEv(
    QBarLegendMarkerPrivate *self) {
  return self->QBarLegendMarkerPrivate::series();
}

//  QObject *QBarLegendMarkerPrivate::relatedObject()
extern "C" Q_DECL_EXPORT
QObject *ritual_own_ZN23QBarLegendMarkerPrivate13relatedObjectEv(
    QBarLegendMarkerPrivate *self) {
  return self->QBarLegendMarkerPrivate::relatedObject();
}

//  void QBarLegendMarkerPrivate::updated()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QBarLegendMarkerPrivate7updatedEv(
    QBarLegendMarkerPrivate *self) {
  self->QBarLegendMarkerPrivate::updated();
}
