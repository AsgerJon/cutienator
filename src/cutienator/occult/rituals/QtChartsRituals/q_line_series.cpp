//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/qlineseries.h, Qt 6.12.0. Changes made here are lost.
#include <QtCharts/qchartglobal.h>
#if QT_CONFIG(charts_line_chart)
#if QT_CONFIG(charts_line_chart)
#include <QtCharts/qlineseries.h>
#include <QtCore/qstring.h>
#include <QtGui/qpen.h>
#include <QtGui/qbrush.h>
#include <QtGui/qcolor.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QLineSeries that Python can take functions over in. Every QLineSeries
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(charts_line_chart)
typedef int (*CuteQLineSeriesCall0)(const void *, int *);
#endif  // QT_CONFIG(charts_line_chart)
typedef void (*CuteQLineSeriesCall1)(const void *, const QPen *, int *);
typedef void (*CuteQLineSeriesCall2)(const void *, const QBrush *, int *);
typedef void (*CuteQLineSeriesCall3)(const void *, const QColor *, int *);
typedef const QColor * (*CuteQLineSeriesCall4)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQLineSeriesCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQLineSeriesCall6)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLineSeriesCall7)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLineSeriesCall8)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLineSeriesCall9)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLineSeriesCall10)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLineSeriesCall11)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQLineSeries : public QLineSeries {
public:
  using QLineSeries::QLineSeries;
  void *taken[12] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(charts_line_chart)
    if (!std::strcmp(key, "_ZNK15QAbstractSeries4typeEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(charts_line_chart)
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

#if QT_CONFIG(charts_line_chart)
  //  QAbstractSeries::SeriesType QLineSeries::type() const
  QAbstractSeries::SeriesType type() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQLineSeriesCall0 call = reinterpret_cast<CuteQLineSeriesCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAbstractSeries::SeriesType>(given);
    }
    return QLineSeries::type();
  }
#endif  // QT_CONFIG(charts_line_chart)

  //  void QXYSeries::setPen(const QPen &pen)
  void setPen(const QPen &pen) override {
    if (taken[1]) {
      int handled = 0;
      CuteQLineSeriesCall1 call = reinterpret_cast<CuteQLineSeriesCall1>(taken[1]);
      call(this, &pen, &handled);
      if (handled) return;
    }
    QXYSeries::setPen(pen);
  }

  //  void QXYSeries::setBrush(const QBrush &brush)
  void setBrush(const QBrush &brush) override {
    if (taken[2]) {
      int handled = 0;
      CuteQLineSeriesCall2 call = reinterpret_cast<CuteQLineSeriesCall2>(taken[2]);
      call(this, &brush, &handled);
      if (handled) return;
    }
    QXYSeries::setBrush(brush);
  }

  //  void QXYSeries::setColor(const QColor &color)
  void setColor(const QColor &color) override {
    if (taken[3]) {
      int handled = 0;
      CuteQLineSeriesCall3 call = reinterpret_cast<CuteQLineSeriesCall3>(taken[3]);
      call(this, &color, &handled);
      if (handled) return;
    }
    QXYSeries::setColor(color);
  }

  //  QColor QXYSeries::color() const
  QColor color() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQLineSeriesCall4 call = reinterpret_cast<CuteQLineSeriesCall4>(taken[4]);
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
      CuteQLineSeriesCall5 call = reinterpret_cast<CuteQLineSeriesCall5>(taken[5]);
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
      CuteQLineSeriesCall6 call = reinterpret_cast<CuteQLineSeriesCall6>(taken[6]);
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
      CuteQLineSeriesCall7 call = reinterpret_cast<CuteQLineSeriesCall7>(taken[7]);
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
      CuteQLineSeriesCall8 call = reinterpret_cast<CuteQLineSeriesCall8>(taken[8]);
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
      CuteQLineSeriesCall9 call = reinterpret_cast<CuteQLineSeriesCall9>(taken[9]);
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
      CuteQLineSeriesCall10 call = reinterpret_cast<CuteQLineSeriesCall10>(taken[10]);
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
      CuteQLineSeriesCall11 call = reinterpret_cast<CuteQLineSeriesCall11>(taken[11]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QLineSeries::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK11QLineSeries10metaObjectEv(
    const QLineSeries *self) {
  return self->metaObject();
}

//  void *QLineSeries::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN11QLineSeries11qt_metacastEPKc(
    QLineSeries *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QLineSeries::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN11QLineSeries11qt_metacallEN11QMetaObject4CallEiPPv(
    QLineSeries *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QLineSeries::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11QLineSeries2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QLineSeries::tr(s, c, n));
}

//  QLineSeries::QLineSeries(QObject *parent)
extern "C" Q_DECL_EXPORT
QLineSeries *ritual_ZN11QLineSeriesC1EP7QObject(QObject *parent) {
  return new CuteQLineSeries(parent);
}

//  QLineSeries::~QLineSeries()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QLineSeriesD1Ev(QLineSeries *self) {
  delete self;
}

//  QAbstractSeries::SeriesType QLineSeries::type() const
extern "C" Q_DECL_EXPORT
QAbstractSeries::SeriesType ritual_ZNK11QLineSeries4typeEv(
    const QLineSeries *self) {
  return self->type();
}

//  QLineSeries::QLineSeries(QLineSeriesPrivate &d, QObject *parent)
extern "C" Q_DECL_EXPORT
QLineSeries *ritual_ZN11QLineSeriesC1ER18QLineSeriesPrivateP7QObject(
    QLineSeriesPrivate *d,
    QObject *parent) {
  return new CuteQLineSeries(*d, parent);
}

//  QLineSeriesPrivate *QLineSeries::d_func()
extern "C" Q_DECL_EXPORT
QLineSeriesPrivate *ritual_ZN11QLineSeries6d_funcEv(QLineSeries *self) {
  return self->d_func();
}

//  const QLineSeriesPrivate *QLineSeries::d_func() const
extern "C" Q_DECL_EXPORT
const QLineSeriesPrivate *ritual_ZNK11QLineSeries6d_funcEv(
    const QLineSeries *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQLineSeries, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QLineSeries(
    QLineSeries *self,
    const char *key,
    void *call) {
  return static_cast<CuteQLineSeries *>(self)->take(key, call);
}

//  QAbstractSeries::SeriesType QLineSeries::type() const
extern "C" Q_DECL_EXPORT
QAbstractSeries::SeriesType ritual_own_ZNK11QLineSeries4typeEv(
    const QLineSeries *self) {
  return self->QLineSeries::type();
}

#endif  // QT_CONFIG(charts_line_chart)
#endif  // QT_CONFIG(charts_line_chart)
