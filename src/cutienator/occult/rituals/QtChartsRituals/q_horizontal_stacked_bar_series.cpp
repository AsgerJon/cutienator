//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/qhorizontalstackedbarseries.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtCharts/qhorizontalstackedbarseries.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QHorizontalStackedBarSeries that Python can take functions over in. Every QHorizontalStackedBarSeries
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQHorizontalStackedBarSeriesCall0)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQHorizontalStackedBarSeriesCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQHorizontalStackedBarSeriesCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHorizontalStackedBarSeriesCall3)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHorizontalStackedBarSeriesCall4)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHorizontalStackedBarSeriesCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHorizontalStackedBarSeriesCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHorizontalStackedBarSeriesCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQHorizontalStackedBarSeries : public QHorizontalStackedBarSeries {
public:
  using QHorizontalStackedBarSeries::QHorizontalStackedBarSeries;
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

  //  QAbstractSeries::SeriesType QHorizontalStackedBarSeries::type() const
  QAbstractSeries::SeriesType type() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQHorizontalStackedBarSeriesCall0 call = reinterpret_cast<CuteQHorizontalStackedBarSeriesCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAbstractSeries::SeriesType>(given);
    }
    return QHorizontalStackedBarSeries::type();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQHorizontalStackedBarSeriesCall1 call = reinterpret_cast<CuteQHorizontalStackedBarSeriesCall1>(taken[1]);
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
      CuteQHorizontalStackedBarSeriesCall2 call = reinterpret_cast<CuteQHorizontalStackedBarSeriesCall2>(taken[2]);
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
      CuteQHorizontalStackedBarSeriesCall3 call = reinterpret_cast<CuteQHorizontalStackedBarSeriesCall3>(taken[3]);
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
      CuteQHorizontalStackedBarSeriesCall4 call = reinterpret_cast<CuteQHorizontalStackedBarSeriesCall4>(taken[4]);
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
      CuteQHorizontalStackedBarSeriesCall5 call = reinterpret_cast<CuteQHorizontalStackedBarSeriesCall5>(taken[5]);
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
      CuteQHorizontalStackedBarSeriesCall6 call = reinterpret_cast<CuteQHorizontalStackedBarSeriesCall6>(taken[6]);
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
      CuteQHorizontalStackedBarSeriesCall7 call = reinterpret_cast<CuteQHorizontalStackedBarSeriesCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QHorizontalStackedBarSeries::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK27QHorizontalStackedBarSeries10metaObjectEv(
    const QHorizontalStackedBarSeries *self) {
  return self->metaObject();
}

//  QString QHorizontalStackedBarSeries::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN27QHorizontalStackedBarSeries2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QHorizontalStackedBarSeries::tr(s, c, n));
}

//  QHorizontalStackedBarSeries::QHorizontalStackedBarSeries(QObject *parent)
extern "C" Q_DECL_EXPORT
QHorizontalStackedBarSeries *ritual_ZN27QHorizontalStackedBarSeriesC1EP7QObject(
    QObject *parent) {
  return new CuteQHorizontalStackedBarSeries(parent);
}

//  QHorizontalStackedBarSeries::~QHorizontalStackedBarSeries()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QHorizontalStackedBarSeriesD1Ev(
    QHorizontalStackedBarSeries *self) {
  delete self;
}

//  QAbstractSeries::SeriesType QHorizontalStackedBarSeries::type() const
extern "C" Q_DECL_EXPORT
QAbstractSeries::SeriesType ritual_ZNK27QHorizontalStackedBarSeries4typeEv(
    const QHorizontalStackedBarSeries *self) {
  return self->type();
}

//  QHorizontalStackedBarSeriesPrivate *QHorizontalStackedBarSeries::d_func()
extern "C" Q_DECL_EXPORT
QHorizontalStackedBarSeriesPrivate *ritual_ZN27QHorizontalStackedBarSeries6d_funcEv(
    QHorizontalStackedBarSeries *self) {
  return self->d_func();
}

//  const QHorizontalStackedBarSeriesPrivate
//      *QHorizontalStackedBarSeries::d_func() const
extern "C" Q_DECL_EXPORT
const QHorizontalStackedBarSeriesPrivate *ritual_ZNK27QHorizontalStackedBarSeries6d_funcEv(
    const QHorizontalStackedBarSeries *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQHorizontalStackedBarSeries, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QHorizontalStackedBarSeries(
    QHorizontalStackedBarSeries *self,
    const char *key,
    void *call) {
  return static_cast<CuteQHorizontalStackedBarSeries *>(self)->take(key, call);
}

//  QAbstractSeries::SeriesType QHorizontalStackedBarSeries::type() const
extern "C" Q_DECL_EXPORT
QAbstractSeries::SeriesType ritual_own_ZNK27QHorizontalStackedBarSeries4typeEv(
    const QHorizontalStackedBarSeries *self) {
  return self->QHorizontalStackedBarSeries::type();
}
