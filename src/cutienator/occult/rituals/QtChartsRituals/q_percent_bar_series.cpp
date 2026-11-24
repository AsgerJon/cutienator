//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/qpercentbarseries.h, Qt 6.12.0. Changes made here are lost.
#include <QtCharts/qpercentbarseries.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QPercentBarSeries that Python can take functions over in. Every QPercentBarSeries
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQPercentBarSeriesCall0)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPercentBarSeriesCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPercentBarSeriesCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPercentBarSeriesCall3)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPercentBarSeriesCall4)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPercentBarSeriesCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPercentBarSeriesCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPercentBarSeriesCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQPercentBarSeries : public QPercentBarSeries {
public:
  using QPercentBarSeries::QPercentBarSeries;
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

  //  QAbstractSeries::SeriesType QPercentBarSeries::type() const
  QAbstractSeries::SeriesType type() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQPercentBarSeriesCall0 call = reinterpret_cast<CuteQPercentBarSeriesCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAbstractSeries::SeriesType>(given);
    }
    return QPercentBarSeries::type();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQPercentBarSeriesCall1 call = reinterpret_cast<CuteQPercentBarSeriesCall1>(taken[1]);
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
      CuteQPercentBarSeriesCall2 call = reinterpret_cast<CuteQPercentBarSeriesCall2>(taken[2]);
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
      CuteQPercentBarSeriesCall3 call = reinterpret_cast<CuteQPercentBarSeriesCall3>(taken[3]);
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
      CuteQPercentBarSeriesCall4 call = reinterpret_cast<CuteQPercentBarSeriesCall4>(taken[4]);
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
      CuteQPercentBarSeriesCall5 call = reinterpret_cast<CuteQPercentBarSeriesCall5>(taken[5]);
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
      CuteQPercentBarSeriesCall6 call = reinterpret_cast<CuteQPercentBarSeriesCall6>(taken[6]);
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
      CuteQPercentBarSeriesCall7 call = reinterpret_cast<CuteQPercentBarSeriesCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QPercentBarSeries::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QPercentBarSeries10metaObjectEv(
    const QPercentBarSeries *self) {
  return self->metaObject();
}

//  QString QPercentBarSeries::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QPercentBarSeries2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QPercentBarSeries::tr(s, c, n));
}

//  QPercentBarSeries::QPercentBarSeries(QObject *parent)
extern "C" Q_DECL_EXPORT
QPercentBarSeries *ritual_ZN17QPercentBarSeriesC1EP7QObject(
    QObject *parent) {
  return new CuteQPercentBarSeries(parent);
}

//  QPercentBarSeries::~QPercentBarSeries()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QPercentBarSeriesD1Ev(QPercentBarSeries *self) {
  delete self;
}

//  QAbstractSeries::SeriesType QPercentBarSeries::type() const
extern "C" Q_DECL_EXPORT
QAbstractSeries::SeriesType ritual_ZNK17QPercentBarSeries4typeEv(
    const QPercentBarSeries *self) {
  return self->type();
}

//  QPercentBarSeriesPrivate *QPercentBarSeries::d_func()
extern "C" Q_DECL_EXPORT
QPercentBarSeriesPrivate *ritual_ZN17QPercentBarSeries6d_funcEv(
    QPercentBarSeries *self) {
  return self->d_func();
}

//  const QPercentBarSeriesPrivate *QPercentBarSeries::d_func() const
extern "C" Q_DECL_EXPORT
const QPercentBarSeriesPrivate *ritual_ZNK17QPercentBarSeries6d_funcEv(
    const QPercentBarSeries *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQPercentBarSeries, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPercentBarSeries(
    QPercentBarSeries *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPercentBarSeries *>(self)->take(key, call);
}

//  QAbstractSeries::SeriesType QPercentBarSeries::type() const
extern "C" Q_DECL_EXPORT
QAbstractSeries::SeriesType ritual_own_ZNK17QPercentBarSeries4typeEv(
    const QPercentBarSeries *self) {
  return self->QPercentBarSeries::type();
}
