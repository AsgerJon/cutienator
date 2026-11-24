//  Written by dev_tooling.RitualGenerator from the records of
//  QtGraphs/qlineseries.h, Qt 6.12.0. Changes made here are lost.
#include <QtGraphs/qgraphsglobal.h>
#if (!(!QT_CONFIG(graphs_2d_area) && !QT_CONFIG(graphs_2d_bar) && !QT_CONFIG(graphs_2d_donut_pie) && !QT_CONFIG(graphs_2d_line) && !QT_CONFIG(graphs_2d_scatter) && !QT_CONFIG(graphs_2d_spline) && !QT_CONFIG(graphs_2d_custom))) && (QT_CONFIG(graphs_2d_line) || QT_CONFIG(graphs_2d_area))
#include <QtGraphs/QtGraphs>
#include <QtGraphs/qlineseries.h>
#include <QtCore/qstring.h>
#include <QtCore/qpoint.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QLineSeries may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQLineSeries : QLineSeries {
  using QLineSeries::componentComplete;
};

//  A QLineSeries that Python can take functions over in. Every QLineSeries
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQLineSeriesCall0)(const void *, int *);
typedef void (*CuteQLineSeriesCall1)(const void *, int *);
typedef void (*CuteQLineSeriesCall2)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQLineSeriesCall3)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQLineSeriesCall4)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLineSeriesCall5)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLineSeriesCall6)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLineSeriesCall7)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLineSeriesCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLineSeriesCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQLineSeries : public QLineSeries {
public:
  using QLineSeries::QLineSeries;
  void *taken[10] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK15QAbstractSeries4typeEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
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

  //  void QLineSeries::componentComplete()
  void componentComplete() override {
    if (taken[1]) {
      int handled = 0;
      CuteQLineSeriesCall1 call = reinterpret_cast<CuteQLineSeriesCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QLineSeries::componentComplete();
  }

  //  void QAbstractSeries::classBegin()
  void classBegin() override {
    if (taken[2]) {
      int handled = 0;
      CuteQLineSeriesCall2 call = reinterpret_cast<CuteQLineSeriesCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractSeries::classBegin();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQLineSeriesCall3 call = reinterpret_cast<CuteQLineSeriesCall3>(taken[3]);
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
      CuteQLineSeriesCall4 call = reinterpret_cast<CuteQLineSeriesCall4>(taken[4]);
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
      CuteQLineSeriesCall5 call = reinterpret_cast<CuteQLineSeriesCall5>(taken[5]);
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
      CuteQLineSeriesCall6 call = reinterpret_cast<CuteQLineSeriesCall6>(taken[6]);
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
      CuteQLineSeriesCall7 call = reinterpret_cast<CuteQLineSeriesCall7>(taken[7]);
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
      CuteQLineSeriesCall8 call = reinterpret_cast<CuteQLineSeriesCall8>(taken[8]);
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
      CuteQLineSeriesCall9 call = reinterpret_cast<CuteQLineSeriesCall9>(taken[9]);
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

//  qreal QLineSeries::width() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK11QLineSeries5widthEv(const QLineSeries *self) {
  return self->width();
}

//  void QLineSeries::setWidth(qreal newWidth)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QLineSeries8setWidthEd(QLineSeries *self, qreal newWidth) {
  self->setWidth(newWidth);
}

//  Qt::PenCapStyle QLineSeries::capStyle() const
extern "C" Q_DECL_EXPORT
Qt::PenCapStyle ritual_ZNK11QLineSeries8capStyleEv(const QLineSeries *self) {
  return self->capStyle();
}

//  void QLineSeries::setCapStyle(Qt::PenCapStyle newCapStyle)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QLineSeries11setCapStyleEN2Qt11PenCapStyleE(
    QLineSeries *self,
    Qt::PenCapStyle newCapStyle) {
  self->setCapStyle(newCapStyle);
}

//  Qt::PenJoinStyle QLineSeries::joinStyle() const
extern "C" Q_DECL_EXPORT
Qt::PenJoinStyle ritual_ZNK11QLineSeries9joinStyleEv(
    const QLineSeries *self) {
  return self->joinStyle();
}

//  void QLineSeries::setJoinStyle(Qt::PenJoinStyle newJoinStyle)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QLineSeries12setJoinStyleEN2Qt12PenJoinStyleE(
    QLineSeries *self,
    Qt::PenJoinStyle newJoinStyle) {
  self->setJoinStyle(newJoinStyle);
}

//  QLineSeries::LineStyle QLineSeries::lineStyle() const
extern "C" Q_DECL_EXPORT
QLineSeries::LineStyle ritual_ZNK11QLineSeries9lineStyleEv(
    const QLineSeries *self) {
  return self->lineStyle();
}

//  void QLineSeries::setLineStyle(QLineSeries::LineStyle newLineStyle)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QLineSeries12setLineStyleENS_9LineStyleE(
    QLineSeries *self,
    QLineSeries::LineStyle newLineStyle) {
  self->setLineStyle(newLineStyle);
}

//  QLineSeries::StrokeStyle QLineSeries::strokeStyle() const
extern "C" Q_DECL_EXPORT
QLineSeries::StrokeStyle ritual_ZNK11QLineSeries11strokeStyleEv(
    const QLineSeries *self) {
  return self->strokeStyle();
}

//  void QLineSeries::setStrokeStyle(QLineSeries::StrokeStyle newStrokeStyle)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QLineSeries14setStrokeStyleENS_11StrokeStyleE(
    QLineSeries *self,
    QLineSeries::StrokeStyle newStrokeStyle) {
  self->setStrokeStyle(newStrokeStyle);
}

//  qreal QLineSeries::dashOffset() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK11QLineSeries10dashOffsetEv(const QLineSeries *self) {
  return self->dashOffset();
}

//  void QLineSeries::setDashOffset(qreal newDashOffset)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QLineSeries13setDashOffsetEd(
    QLineSeries *self,
    qreal newDashOffset) {
  self->setDashOffset(newDashOffset);
}

//  QPointF QLineSeries::dataPointCoordinatesAt(qreal x, qreal y)
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZN11QLineSeries22dataPointCoordinatesAtEdd(
    QLineSeries *self,
    qreal x,
    qreal y) {
  return new QPointF(self->dataPointCoordinatesAt(x, y));
}

//  void QLineSeries::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QLineSeries17componentCompleteEv(QLineSeries *self) {
  self->componentComplete();
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

//  void QLineSeries::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QLineSeries17componentCompleteEv(QLineSeries *self) {
  static_cast<OwnQLineSeries *>(self)->OwnQLineSeries::componentComplete();
}

#endif  // (!(!QT_CONFIG(graphs_2d_area) && !QT_CONFIG(graphs_2d_bar) && !QT_CONFIG(graphs_2d_donut_pie) && !QT_CONFIG(graphs_2d_line) && !QT_CONFIG(graphs_2d_scatter) && !QT_CONFIG(graphs_2d_spline) && !QT_CONFIG(graphs_2d_custom))) && (QT_CONFIG(graphs_2d_line) || QT_CONFIG(graphs_2d_area))
