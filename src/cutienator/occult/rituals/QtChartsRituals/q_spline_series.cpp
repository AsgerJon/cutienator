//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/qsplineseries.h, Qt 6.12.0. Changes made here are lost.
#include <QtCharts/qchartglobal.h>
#if QT_CONFIG(charts_spline_chart)
#include <QtCharts/qsplineseries.h>
#include <QtCore/qstring.h>
#include <QtGui/qpen.h>
#include <QtGui/qbrush.h>
#include <QtGui/qcolor.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QSplineSeries that Python can take functions over in. Every QSplineSeries
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(charts_spline_chart)
typedef int (*CuteQSplineSeriesCall0)(const void *, int *);
#endif  // QT_CONFIG(charts_spline_chart)
typedef void (*CuteQSplineSeriesCall1)(const void *, const QPen *, int *);
typedef void (*CuteQSplineSeriesCall2)(const void *, const QBrush *, int *);
typedef void (*CuteQSplineSeriesCall3)(const void *, const QColor *, int *);
typedef const QColor * (*CuteQSplineSeriesCall4)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSplineSeriesCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSplineSeriesCall6)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSplineSeriesCall7)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSplineSeriesCall8)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSplineSeriesCall9)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSplineSeriesCall10)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSplineSeriesCall11)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQSplineSeries : public QSplineSeries {
public:
  using QSplineSeries::QSplineSeries;
  void *taken[12] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(charts_spline_chart)
    if (!std::strcmp(key, "_ZNK15QAbstractSeries4typeEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(charts_spline_chart)
    if (!std::strcmp(key, "_ZN9QXYSeries6setPenERK4QPen")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QXYSeries8setBrushERK6QBrush")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QXYSeries8setColorERK6QColor")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QXYSeries5colorEv")) {
      taken[4] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if QT_CONFIG(charts_spline_chart)
  //  QAbstractSeries::SeriesType QSplineSeries::type() const
  QAbstractSeries::SeriesType type() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSplineSeriesCall0 call = reinterpret_cast<CuteQSplineSeriesCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAbstractSeries::SeriesType>(given);
    }
    return QSplineSeries::type();
  }
#endif  // QT_CONFIG(charts_spline_chart)

  //  void QXYSeries::setPen(const QPen &pen)
  void setPen(const QPen &pen) override {
    if (taken[1]) {
      int handled = 0;
      CuteQSplineSeriesCall1 call = reinterpret_cast<CuteQSplineSeriesCall1>(taken[1]);
      call(this, &pen, &handled);
      if (handled) return;
    }
    QXYSeries::setPen(pen);
  }

  //  void QXYSeries::setBrush(const QBrush &brush)
  void setBrush(const QBrush &brush) override {
    if (taken[2]) {
      int handled = 0;
      CuteQSplineSeriesCall2 call = reinterpret_cast<CuteQSplineSeriesCall2>(taken[2]);
      call(this, &brush, &handled);
      if (handled) return;
    }
    QXYSeries::setBrush(brush);
  }

  //  void QXYSeries::setColor(const QColor &color)
  void setColor(const QColor &color) override {
    if (taken[3]) {
      int handled = 0;
      CuteQSplineSeriesCall3 call = reinterpret_cast<CuteQSplineSeriesCall3>(taken[3]);
      call(this, &color, &handled);
      if (handled) return;
    }
    QXYSeries::setColor(color);
  }

  //  QColor QXYSeries::color() const
  QColor color() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQSplineSeriesCall4 call = reinterpret_cast<CuteQSplineSeriesCall4>(taken[4]);
      const QColor * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QXYSeries::color();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQSplineSeriesCall5 call = reinterpret_cast<CuteQSplineSeriesCall5>(taken[5]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQSplineSeriesCall6 call = reinterpret_cast<CuteQSplineSeriesCall6>(taken[6]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQSplineSeriesCall7 call = reinterpret_cast<CuteQSplineSeriesCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQSplineSeriesCall8 call = reinterpret_cast<CuteQSplineSeriesCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQSplineSeriesCall9 call = reinterpret_cast<CuteQSplineSeriesCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[10]) {
      int handled = 0;
      CuteQSplineSeriesCall10 call = reinterpret_cast<CuteQSplineSeriesCall10>(taken[10]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[11]) {
      int handled = 0;
      CuteQSplineSeriesCall11 call = reinterpret_cast<CuteQSplineSeriesCall11>(taken[11]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QSplineSeries::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13QSplineSeries10metaObjectEv(
    const QSplineSeries *self) {
  return self->metaObject();
}

//  QString QSplineSeries::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13QSplineSeries2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QSplineSeries::tr(s, c, n));
}

//  QSplineSeries::QSplineSeries(QObject *parent)
extern "C" Q_DECL_EXPORT
QSplineSeries *ritual_ZN13QSplineSeriesC1EP7QObject(QObject *parent) {
  return new CuteQSplineSeries(parent);
}

//  QSplineSeries::~QSplineSeries()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSplineSeriesD1Ev(QSplineSeries *self) {
  delete self;
}

//  QAbstractSeries::SeriesType QSplineSeries::type() const
extern "C" Q_DECL_EXPORT
QAbstractSeries::SeriesType ritual_ZNK13QSplineSeries4typeEv(
    const QSplineSeries *self) {
  return self->type();
}

//  QSplineSeriesPrivate *QSplineSeries::d_func()
extern "C" Q_DECL_EXPORT
QSplineSeriesPrivate *ritual_ZN13QSplineSeries6d_funcEv(
    QSplineSeries *self) {
  return self->d_func();
}

//  const QSplineSeriesPrivate *QSplineSeries::d_func() const
extern "C" Q_DECL_EXPORT
const QSplineSeriesPrivate *ritual_ZNK13QSplineSeries6d_funcEv(
    const QSplineSeries *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQSplineSeries, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSplineSeries(
    QSplineSeries *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSplineSeries *>(self)->take(key, call);
}

//  QAbstractSeries::SeriesType QSplineSeries::type() const
extern "C" Q_DECL_EXPORT
QAbstractSeries::SeriesType ritual_own_ZNK13QSplineSeries4typeEv(
    const QSplineSeries *self) {
  return self->QSplineSeries::type();
}

#endif  // QT_CONFIG(charts_spline_chart)
