//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/qhorizontalpercentbarseries.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtCharts/qhorizontalpercentbarseries.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QHorizontalPercentBarSeries that Python can take functions over in. Every QHorizontalPercentBarSeries
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQHorizontalPercentBarSeriesCall0)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQHorizontalPercentBarSeriesCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQHorizontalPercentBarSeriesCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHorizontalPercentBarSeriesCall3)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHorizontalPercentBarSeriesCall4)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHorizontalPercentBarSeriesCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHorizontalPercentBarSeriesCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHorizontalPercentBarSeriesCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQHorizontalPercentBarSeries : public QHorizontalPercentBarSeries {
public:
  using QHorizontalPercentBarSeries::QHorizontalPercentBarSeries;
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

  //  QAbstractSeries::SeriesType QHorizontalPercentBarSeries::type() const
  QAbstractSeries::SeriesType type() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQHorizontalPercentBarSeriesCall0 call = reinterpret_cast<CuteQHorizontalPercentBarSeriesCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAbstractSeries::SeriesType>(given);
    }
    return QHorizontalPercentBarSeries::type();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQHorizontalPercentBarSeriesCall1 call = reinterpret_cast<CuteQHorizontalPercentBarSeriesCall1>(taken[1]);
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
      CuteQHorizontalPercentBarSeriesCall2 call = reinterpret_cast<CuteQHorizontalPercentBarSeriesCall2>(taken[2]);
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
      CuteQHorizontalPercentBarSeriesCall3 call = reinterpret_cast<CuteQHorizontalPercentBarSeriesCall3>(taken[3]);
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
      CuteQHorizontalPercentBarSeriesCall4 call = reinterpret_cast<CuteQHorizontalPercentBarSeriesCall4>(taken[4]);
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
      CuteQHorizontalPercentBarSeriesCall5 call = reinterpret_cast<CuteQHorizontalPercentBarSeriesCall5>(taken[5]);
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
      CuteQHorizontalPercentBarSeriesCall6 call = reinterpret_cast<CuteQHorizontalPercentBarSeriesCall6>(taken[6]);
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
      CuteQHorizontalPercentBarSeriesCall7 call = reinterpret_cast<CuteQHorizontalPercentBarSeriesCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QHorizontalPercentBarSeries::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK27QHorizontalPercentBarSeries10metaObjectEv(
    const QHorizontalPercentBarSeries *self) {
  return self->metaObject();
}

//  QString QHorizontalPercentBarSeries::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN27QHorizontalPercentBarSeries2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QHorizontalPercentBarSeries::tr(s, c, n));
}

//  QHorizontalPercentBarSeries::QHorizontalPercentBarSeries(QObject *parent)
extern "C" Q_DECL_EXPORT
QHorizontalPercentBarSeries *ritual_ZN27QHorizontalPercentBarSeriesC1EP7QObject(
    QObject *parent) {
  return new CuteQHorizontalPercentBarSeries(parent);
}

//  QHorizontalPercentBarSeries::~QHorizontalPercentBarSeries()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QHorizontalPercentBarSeriesD1Ev(
    QHorizontalPercentBarSeries *self) {
  delete self;
}

//  QAbstractSeries::SeriesType QHorizontalPercentBarSeries::type() const
extern "C" Q_DECL_EXPORT
QAbstractSeries::SeriesType ritual_ZNK27QHorizontalPercentBarSeries4typeEv(
    const QHorizontalPercentBarSeries *self) {
  return self->type();
}

//  QHorizontalPercentBarSeriesPrivate *QHorizontalPercentBarSeries::d_func()
extern "C" Q_DECL_EXPORT
QHorizontalPercentBarSeriesPrivate *ritual_ZN27QHorizontalPercentBarSeries6d_funcEv(
    QHorizontalPercentBarSeries *self) {
  return self->d_func();
}

//  const QHorizontalPercentBarSeriesPrivate
//      *QHorizontalPercentBarSeries::d_func() const
extern "C" Q_DECL_EXPORT
const QHorizontalPercentBarSeriesPrivate *ritual_ZNK27QHorizontalPercentBarSeries6d_funcEv(
    const QHorizontalPercentBarSeries *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQHorizontalPercentBarSeries, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QHorizontalPercentBarSeries(
    QHorizontalPercentBarSeries *self,
    const char *key,
    void *call) {
  return static_cast<CuteQHorizontalPercentBarSeries *>(self)->take(key, call);
}

//  QAbstractSeries::SeriesType QHorizontalPercentBarSeries::type() const
extern "C" Q_DECL_EXPORT
QAbstractSeries::SeriesType ritual_own_ZNK27QHorizontalPercentBarSeries4typeEv(
    const QHorizontalPercentBarSeries *self) {
  return self->QHorizontalPercentBarSeries::type();
}
