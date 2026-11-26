//  Written by dev_tooling.RitualGenerator from the records of
//  QtGraphs/qsplineseries.h, Qt 6.12.0. Changes made here are lost.
#include <QtGraphs/qgraphsglobal.h>
#if (QT_CONFIG(graphs_2d)) && (!(!QT_CONFIG(graphs_2d_area) && !QT_CONFIG(graphs_2d_bar) && !QT_CONFIG(graphs_2d_donut_pie) && !QT_CONFIG(graphs_2d_line) && !QT_CONFIG(graphs_2d_scatter) && !QT_CONFIG(graphs_2d_spline) && !QT_CONFIG(graphs_2d_custom))) && (QT_CONFIG(graphs_2d_spline))
#include <QtGraphs/QtGraphs>
#include <QtGraphs/qsplineseries.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QSplineSeries may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQSplineSeries : QSplineSeries {
  using QSplineSeries::componentComplete;
};

//  A QSplineSeries that Python can take functions over in. Every QSplineSeries
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQSplineSeriesCall0)(const void *, int *);
typedef void (*CuteQSplineSeriesCall1)(const void *, int *);
typedef void (*CuteQSplineSeriesCall2)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSplineSeriesCall3)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSplineSeriesCall4)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSplineSeriesCall5)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSplineSeriesCall6)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSplineSeriesCall7)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSplineSeriesCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSplineSeriesCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQSplineSeries : public QSplineSeries {
public:
  using QSplineSeries::QSplineSeries;
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

  //  void QSplineSeries::componentComplete()
  void componentComplete() override {
    if (taken[1]) {
      int handled = 0;
      CuteQSplineSeriesCall1 call = reinterpret_cast<CuteQSplineSeriesCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QSplineSeries::componentComplete();
  }

  //  void QAbstractSeries::classBegin()
  void classBegin() override {
    if (taken[2]) {
      int handled = 0;
      CuteQSplineSeriesCall2 call = reinterpret_cast<CuteQSplineSeriesCall2>(taken[2]);
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
      CuteQSplineSeriesCall3 call = reinterpret_cast<CuteQSplineSeriesCall3>(taken[3]);
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
      CuteQSplineSeriesCall4 call = reinterpret_cast<CuteQSplineSeriesCall4>(taken[4]);
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
      CuteQSplineSeriesCall5 call = reinterpret_cast<CuteQSplineSeriesCall5>(taken[5]);
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
      CuteQSplineSeriesCall6 call = reinterpret_cast<CuteQSplineSeriesCall6>(taken[6]);
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
      CuteQSplineSeriesCall7 call = reinterpret_cast<CuteQSplineSeriesCall7>(taken[7]);
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
      CuteQSplineSeriesCall8 call = reinterpret_cast<CuteQSplineSeriesCall8>(taken[8]);
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
      CuteQSplineSeriesCall9 call = reinterpret_cast<CuteQSplineSeriesCall9>(taken[9]);
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

//  void *QSplineSeries::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN13QSplineSeries11qt_metacastEPKc(
    QSplineSeries *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QSplineSeries::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN13QSplineSeries11qt_metacallEN11QMetaObject4CallEiPPv(
    QSplineSeries *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
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

//  qreal QSplineSeries::width() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK13QSplineSeries5widthEv(const QSplineSeries *self) {
  return self->width();
}

//  void QSplineSeries::setWidth(qreal newWidth)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSplineSeries8setWidthEd(
    QSplineSeries *self,
    qreal newWidth) {
  self->setWidth(newWidth);
}

//  Qt::PenCapStyle QSplineSeries::capStyle() const
extern "C" Q_DECL_EXPORT
Qt::PenCapStyle ritual_ZNK13QSplineSeries8capStyleEv(
    const QSplineSeries *self) {
  return self->capStyle();
}

//  void QSplineSeries::setCapStyle(Qt::PenCapStyle newCapStyle)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSplineSeries11setCapStyleEN2Qt11PenCapStyleE(
    QSplineSeries *self,
    Qt::PenCapStyle newCapStyle) {
  self->setCapStyle(newCapStyle);
}

//  bool QSplineSeries::isOptimized() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QSplineSeries11isOptimizedEv(const QSplineSeries *self) {
  return self->isOptimized();
}

//  void QSplineSeries::setOptimized(bool optimized)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSplineSeries12setOptimizedEb(
    QSplineSeries *self,
    bool optimized) {
  self->setOptimized(optimized);
}

//  QList<QPointF> &QSplineSeries::getControlPoints()
extern "C" Q_DECL_EXPORT
QList<QPointF> *ritual_ZN13QSplineSeries16getControlPointsEv(
    QSplineSeries *self) {
  return &(self->getControlPoints());
}

//  void QSplineSeries::widthChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSplineSeries12widthChangedEv(QSplineSeries *self) {
  self->widthChanged();
}

//  void QSplineSeries::capStyleChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSplineSeries15capStyleChangedEv(QSplineSeries *self) {
  self->capStyleChanged();
}

//  void QSplineSeries::optimizedChanged(bool newOptimized)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSplineSeries16optimizedChangedEb(
    QSplineSeries *self,
    bool newOptimized) {
  self->optimizedChanged(newOptimized);
}

//  QSplineSeries::QSplineSeries(QSplineSeriesPrivate &dd, QObject *parent)
extern "C" Q_DECL_EXPORT
QSplineSeries *ritual_ZN13QSplineSeriesC1ER20QSplineSeriesPrivateP7QObject(
    QSplineSeriesPrivate *dd,
    QObject *parent) {
  return new CuteQSplineSeries(*dd, parent);
}

//  void QSplineSeries::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSplineSeries17componentCompleteEv(QSplineSeries *self) {
  self->componentComplete();
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

//  void QSplineSeries::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QSplineSeries17componentCompleteEv(QSplineSeries *self) {
  static_cast<OwnQSplineSeries *>(self)->OwnQSplineSeries::componentComplete();
}

#endif  // (QT_CONFIG(graphs_2d)) && (!(!QT_CONFIG(graphs_2d_area) && !QT_CONFIG(graphs_2d_bar) && !QT_CONFIG(graphs_2d_donut_pie) && !QT_CONFIG(graphs_2d_line) && !QT_CONFIG(graphs_2d_scatter) && !QT_CONFIG(graphs_2d_spline) && !QT_CONFIG(graphs_2d_custom))) && (QT_CONFIG(graphs_2d_spline))
