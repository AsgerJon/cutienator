//  Written by dev_tooling.RitualGenerator from the records of
//  QtGraphs/qabstractseries.h, Qt 6.12.0. Changes made here are lost.
#include <QtGraphs/qgraphsglobal.h>
#if !(!QT_CONFIG(graphs_2d_area) && !QT_CONFIG(graphs_2d_bar) && !QT_CONFIG(graphs_2d_donut_pie) && !QT_CONFIG(graphs_2d_line) && !QT_CONFIG(graphs_2d_scatter) && !QT_CONFIG(graphs_2d_spline) && !QT_CONFIG(graphs_2d_custom))
#include <QtGraphs/QtGraphs>
#include <QtGraphs/qabstractseries.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  Only a class built on QAbstractSeries may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQAbstractSeries : QAbstractSeries {
  using QAbstractSeries::classBegin;
  using QAbstractSeries::componentComplete;
};

//  A QAbstractSeries that Python can take functions over in. Every QAbstractSeries
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQAbstractSeriesCall0)(const void *, int *);
typedef void (*CuteQAbstractSeriesCall1)(const void *, int *);
typedef int (*CuteQAbstractSeriesCall2)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAbstractSeriesCall3)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAbstractSeriesCall4)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractSeriesCall5)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractSeriesCall6)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractSeriesCall7)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractSeriesCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractSeriesCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQAbstractSeries : public QAbstractSeries {
public:
  using QAbstractSeries::QAbstractSeries;
  void *taken[10] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QAbstractSeries4typeEv")) {
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

  //  void QAbstractSeries::classBegin()
  void classBegin() override {
    if (taken[0]) {
      int handled = 0;
      CuteQAbstractSeriesCall0 call = reinterpret_cast<CuteQAbstractSeriesCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractSeries::classBegin();
  }

  //  void QAbstractSeries::componentComplete()
  void componentComplete() override {
    if (taken[1]) {
      int handled = 0;
      CuteQAbstractSeriesCall1 call = reinterpret_cast<CuteQAbstractSeriesCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractSeries::componentComplete();
  }

  //  SeriesType QAbstractSeries::type() const
  QAbstractSeries::SeriesType type() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQAbstractSeriesCall2 call = reinterpret_cast<CuteQAbstractSeriesCall2>(taken[2]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAbstractSeries::SeriesType>(given);
    }
    return {};
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQAbstractSeriesCall3 call = reinterpret_cast<CuteQAbstractSeriesCall3>(taken[3]);
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
      CuteQAbstractSeriesCall4 call = reinterpret_cast<CuteQAbstractSeriesCall4>(taken[4]);
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
      CuteQAbstractSeriesCall5 call = reinterpret_cast<CuteQAbstractSeriesCall5>(taken[5]);
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
      CuteQAbstractSeriesCall6 call = reinterpret_cast<CuteQAbstractSeriesCall6>(taken[6]);
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
      CuteQAbstractSeriesCall7 call = reinterpret_cast<CuteQAbstractSeriesCall7>(taken[7]);
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
      CuteQAbstractSeriesCall8 call = reinterpret_cast<CuteQAbstractSeriesCall8>(taken[8]);
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
      CuteQAbstractSeriesCall9 call = reinterpret_cast<CuteQAbstractSeriesCall9>(taken[9]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QAbstractSeries::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QAbstractSeries10metaObjectEv(
    const QAbstractSeries *self) {
  return self->metaObject();
}

//  QString QAbstractSeries::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QAbstractSeries2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QAbstractSeries::tr(s, c, n));
}

//  QAbstractSeriesPrivate *QAbstractSeries::d_func()
extern "C" Q_DECL_EXPORT
QAbstractSeriesPrivate *ritual_ZN15QAbstractSeries6d_funcEv(
    QAbstractSeries *self) {
  return self->d_func();
}

//  const QAbstractSeriesPrivate *QAbstractSeries::d_func() const
extern "C" Q_DECL_EXPORT
const QAbstractSeriesPrivate *ritual_ZNK15QAbstractSeries6d_funcEv(
    const QAbstractSeries *self) {
  return self->d_func();
}

//  void QAbstractSeries::qt_qmlMarker_anonymous()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractSeries22qt_qmlMarker_anonymousEv(
    QAbstractSeries *self) {
  self->qt_qmlMarker_anonymous();
}

//  void QAbstractSeries::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractSeries10classBeginEv(QAbstractSeries *self) {
  self->classBegin();
}

//  void QAbstractSeries::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractSeries17componentCompleteEv(QAbstractSeries *self) {
  self->componentComplete();
}

//  QAbstractSeries::~QAbstractSeries()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractSeriesD1Ev(QAbstractSeries *self) {
  delete self;
}

//  SeriesType QAbstractSeries::type() const
extern "C" Q_DECL_EXPORT
QAbstractSeries::SeriesType ritual_ZNK15QAbstractSeries4typeEv(
    const QAbstractSeries *self) {
  return self->type();
}

//  QString QAbstractSeries::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QAbstractSeries4nameEv(const QAbstractSeries *self) {
  return new QString(self->name());
}

//  void QAbstractSeries::setName(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractSeries7setNameERK7QString(
    QAbstractSeries *self,
    const QString *name) {
  self->setName(*name);
}

//  bool QAbstractSeries::isVisible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QAbstractSeries9isVisibleEv(const QAbstractSeries *self) {
  return self->isVisible();
}

//  void QAbstractSeries::setVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractSeries10setVisibleEb(
    QAbstractSeries *self,
    bool visible) {
  self->setVisible(visible);
}

//  bool QAbstractSeries::isSelectable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QAbstractSeries12isSelectableEv(
    const QAbstractSeries *self) {
  return self->isSelectable();
}

//  void QAbstractSeries::setSelectable(bool selectable)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractSeries13setSelectableEb(
    QAbstractSeries *self,
    bool selectable) {
  self->setSelectable(selectable);
}

//  qreal QAbstractSeries::opacity() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QAbstractSeries7opacityEv(const QAbstractSeries *self) {
  return self->opacity();
}

//  void QAbstractSeries::setOpacity(qreal opacity)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractSeries10setOpacityEd(
    QAbstractSeries *self,
    qreal opacity) {
  self->setOpacity(opacity);
}

//  qreal QAbstractSeries::valuesMultiplier() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QAbstractSeries16valuesMultiplierEv(
    const QAbstractSeries *self) {
  return self->valuesMultiplier();
}

//  void QAbstractSeries::setValuesMultiplier(qreal valuesMultiplier)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractSeries19setValuesMultiplierEd(
    QAbstractSeries *self,
    qreal valuesMultiplier) {
  self->setValuesMultiplier(valuesMultiplier);
}

//  QGraphsView *QAbstractSeries::graph() const
extern "C" Q_DECL_EXPORT
QGraphsView *ritual_ZNK15QAbstractSeries5graphEv(
    const QAbstractSeries *self) {
  return self->graph();
}

//  void QAbstractSeries::setGraph(QGraphsView *graph)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractSeries8setGraphEP11QGraphsView(
    QAbstractSeries *self,
    QGraphsView *graph) {
  self->setGraph(graph);
}

//  const QList<QLegendData> QAbstractSeries::legendData() const
extern "C" Q_DECL_EXPORT
QList<QLegendData> *ritual_ZNK15QAbstractSeries10legendDataEv(
    const QAbstractSeries *self) {
  return new QList<QLegendData>(self->legendData());
}

//  void QAbstractSeries::show()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractSeries4showEv(QAbstractSeries *self) {
  self->show();
}

//  void QAbstractSeries::hide()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractSeries4hideEv(QAbstractSeries *self) {
  self->hide();
}

//  bool QAbstractSeries::isHoverable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QAbstractSeries11isHoverableEv(
    const QAbstractSeries *self) {
  return self->isHoverable();
}

//  void QAbstractSeries::setHoverable(bool newHoverable)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractSeries12setHoverableEb(
    QAbstractSeries *self,
    bool newHoverable) {
  self->setHoverable(newHoverable);
}

//  bool QAbstractSeries::hasLoaded() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QAbstractSeries9hasLoadedEv(const QAbstractSeries *self) {
  return self->hasLoaded();
}

//  bool QAbstractSeries::isHovered() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QAbstractSeries9isHoveredEv(const QAbstractSeries *self) {
  return self->isHovered();
}

//  void QAbstractSeries::setHovered(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractSeries10setHoveredEb(
    QAbstractSeries *self,
    bool enabled) {
  self->setHovered(enabled);
}

//  QAbstractAxis *QAbstractSeries::axisX() const
extern "C" Q_DECL_EXPORT
QAbstractAxis *ritual_ZNK15QAbstractSeries5axisXEv(
    const QAbstractSeries *self) {
  return self->axisX();
}

//  void QAbstractSeries::setAxisX(QAbstractAxis *newAxisX)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractSeries8setAxisXEP13QAbstractAxis(
    QAbstractSeries *self,
    QAbstractAxis *newAxisX) {
  self->setAxisX(newAxisX);
}

//  QAbstractAxis *QAbstractSeries::axisY() const
extern "C" Q_DECL_EXPORT
QAbstractAxis *ritual_ZNK15QAbstractSeries5axisYEv(
    const QAbstractSeries *self) {
  return self->axisY();
}

//  void QAbstractSeries::setAxisY(QAbstractAxis *newAxisY)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractSeries8setAxisYEP13QAbstractAxis(
    QAbstractSeries *self,
    QAbstractAxis *newAxisY) {
  self->setAxisY(newAxisY);
}

//  int QAbstractSeries::zValue() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QAbstractSeries6zValueEv(const QAbstractSeries *self) {
  return self->zValue();
}

//  void QAbstractSeries::setZValue(int newDrawOrder)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractSeries9setZValueEi(
    QAbstractSeries *self,
    int newDrawOrder) {
  self->setZValue(newDrawOrder);
}

//  QAbstractSeries as the QQmlParserStatus it is built on
extern "C" Q_DECL_EXPORT
QQmlParserStatus *ritual_cast_QAbstractSeries_QQmlParserStatus(
    QAbstractSeries *self) {
  return static_cast<QQmlParserStatus *>(self);
}

//  a Python function taken by a CuteQAbstractSeries, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAbstractSeries(
    QAbstractSeries *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAbstractSeries *>(self)->take(key, call);
}

//  void QAbstractSeries::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QAbstractSeries10classBeginEv(QAbstractSeries *self) {
  static_cast<OwnQAbstractSeries *>(self)->OwnQAbstractSeries::classBegin();
}

//  void QAbstractSeries::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QAbstractSeries17componentCompleteEv(
    QAbstractSeries *self) {
  static_cast<OwnQAbstractSeries *>(self)->OwnQAbstractSeries::componentComplete();
}

#endif  // !(!QT_CONFIG(graphs_2d_area) && !QT_CONFIG(graphs_2d_bar) && !QT_CONFIG(graphs_2d_donut_pie) && !QT_CONFIG(graphs_2d_line) && !QT_CONFIG(graphs_2d_scatter) && !QT_CONFIG(graphs_2d_spline) && !QT_CONFIG(graphs_2d_custom))
