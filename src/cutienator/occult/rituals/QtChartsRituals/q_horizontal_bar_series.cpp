//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/qhorizontalbarseries.h, Qt 6.12.0. Changes made here are lost.
#include <QtCharts/qchartglobal.h>
#if QT_CONFIG(charts_bar_chart)
#include <QtCharts/qhorizontalbarseries.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QHorizontalBarSeries that Python can take functions over in. Every QHorizontalBarSeries
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQHorizontalBarSeriesCall0)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQHorizontalBarSeriesCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQHorizontalBarSeriesCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHorizontalBarSeriesCall3)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHorizontalBarSeriesCall4)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHorizontalBarSeriesCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHorizontalBarSeriesCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHorizontalBarSeriesCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQHorizontalBarSeries : public QHorizontalBarSeries {
public:
  using QHorizontalBarSeries::QHorizontalBarSeries;
  void *taken[8] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK15QAbstractSeries4typeEv")) {
      taken[0] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  QAbstractSeries::SeriesType QHorizontalBarSeries::type() const
  QAbstractSeries::SeriesType type() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQHorizontalBarSeriesCall0 call = reinterpret_cast<CuteQHorizontalBarSeriesCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAbstractSeries::SeriesType>(given);
    }
    return QHorizontalBarSeries::type();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQHorizontalBarSeriesCall1 call = reinterpret_cast<CuteQHorizontalBarSeriesCall1>(taken[1]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQHorizontalBarSeriesCall2 call = reinterpret_cast<CuteQHorizontalBarSeriesCall2>(taken[2]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQHorizontalBarSeriesCall3 call = reinterpret_cast<CuteQHorizontalBarSeriesCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQHorizontalBarSeriesCall4 call = reinterpret_cast<CuteQHorizontalBarSeriesCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQHorizontalBarSeriesCall5 call = reinterpret_cast<CuteQHorizontalBarSeriesCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQHorizontalBarSeriesCall6 call = reinterpret_cast<CuteQHorizontalBarSeriesCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[7]) {
      int handled = 0;
      CuteQHorizontalBarSeriesCall7 call = reinterpret_cast<CuteQHorizontalBarSeriesCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QHorizontalBarSeries::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20QHorizontalBarSeries10metaObjectEv(
    const QHorizontalBarSeries *self) {
  return self->metaObject();
}

//  void *QHorizontalBarSeries::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN20QHorizontalBarSeries11qt_metacastEPKc(
    QHorizontalBarSeries *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QHorizontalBarSeries::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN20QHorizontalBarSeries11qt_metacallEN11QMetaObject4CallEiPPv(
    QHorizontalBarSeries *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QHorizontalBarSeries::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN20QHorizontalBarSeries2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QHorizontalBarSeries::tr(s, c, n));
}

//  QHorizontalBarSeries::QHorizontalBarSeries(QObject *parent)
extern "C" Q_DECL_EXPORT
QHorizontalBarSeries *ritual_ZN20QHorizontalBarSeriesC1EP7QObject(
    QObject *parent) {
  return new CuteQHorizontalBarSeries(parent);
}

//  QHorizontalBarSeries::~QHorizontalBarSeries()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QHorizontalBarSeriesD1Ev(QHorizontalBarSeries *self) {
  delete self;
}

//  QAbstractSeries::SeriesType QHorizontalBarSeries::type() const
extern "C" Q_DECL_EXPORT
QAbstractSeries::SeriesType ritual_ZNK20QHorizontalBarSeries4typeEv(
    const QHorizontalBarSeries *self) {
  return self->type();
}

//  QHorizontalBarSeriesPrivate *QHorizontalBarSeries::d_func()
extern "C" Q_DECL_EXPORT
QHorizontalBarSeriesPrivate *ritual_ZN20QHorizontalBarSeries6d_funcEv(
    QHorizontalBarSeries *self) {
  return self->d_func();
}

//  const QHorizontalBarSeriesPrivate *QHorizontalBarSeries::d_func() const
extern "C" Q_DECL_EXPORT
const QHorizontalBarSeriesPrivate *ritual_ZNK20QHorizontalBarSeries6d_funcEv(
    const QHorizontalBarSeries *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQHorizontalBarSeries, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QHorizontalBarSeries(
    QHorizontalBarSeries *self,
    const char *key,
    void *call) {
  return static_cast<CuteQHorizontalBarSeries *>(self)->take(key, call);
}

//  QAbstractSeries::SeriesType QHorizontalBarSeries::type() const
extern "C" Q_DECL_EXPORT
QAbstractSeries::SeriesType ritual_own_ZNK20QHorizontalBarSeries4typeEv(
    const QHorizontalBarSeries *self) {
  return self->QHorizontalBarSeries::type();
}

#endif  // QT_CONFIG(charts_bar_chart)
