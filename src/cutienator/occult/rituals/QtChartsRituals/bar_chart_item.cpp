//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/6.12.0/QtCharts/private/barchartitem_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#include <QtCharts/QtCharts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCharts/6.12.0/QtCharts/private/barchartitem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtCore/qlist.h>

//  const QMetaObject *BarChartItem::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK12BarChartItem10metaObjectEv(
    const BarChartItem *self) {
  return self->metaObject();
}

//  QString BarChartItem::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN12BarChartItem2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(BarChartItem::tr(s, c, n));
}

//  BarChartItem::BarChartItem(QAbstractBarSeries *series, QGraphicsItem
//      *item)
extern "C" Q_DECL_EXPORT
BarChartItem *ritual_ZN12BarChartItemC1EP18QAbstractBarSeriesP13QGraphicsItem(
    QAbstractBarSeries *series,
    QGraphicsItem *item) {
  return new BarChartItem(series, item);
}

//  void BarChartItem::handleLabelsPositionChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN12BarChartItem27handleLabelsPositionChangedEv(
    BarChartItem *self) {
  self->handleLabelsPositionChanged();
}

//  void BarChartItem::positionLabels()
extern "C" Q_DECL_EXPORT
void ritual_ZN12BarChartItem14positionLabelsEv(BarChartItem *self) {
  self->positionLabels();
}

//  QList<QRectF> BarChartItem::calculateLayout()
extern "C" Q_DECL_EXPORT
QList<QRectF> *ritual_ZN12BarChartItem15calculateLayoutEv(
    BarChartItem *self) {
  return new QList<QRectF>(self->calculateLayout());
}

//  void BarChartItem::initializeLayout(int set, int category, int
//      layoutIndex, bool resetAnimation)
extern "C" Q_DECL_EXPORT
void ritual_ZN12BarChartItem16initializeLayoutEiiib(
    BarChartItem *self,
    int set,
    int category,
    int layoutIndex,
    bool resetAnimation) {
  self->initializeLayout(set, category, layoutIndex, resetAnimation);
}

//  QPointF BarChartItem::topLeftPoint(int set, int setCount, int category,
//      qreal barWidth, qreal value)
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZN12BarChartItem12topLeftPointEiiidd(
    BarChartItem *self,
    int set,
    int setCount,
    int category,
    qreal barWidth,
    qreal value) {
  return new QPointF(
      self->topLeftPoint(
          set,
          setCount,
          category,
          barWidth,
          value));
}

//  QPointF BarChartItem::bottomRightPoint(int set, int setCount, int
//      category, qreal barWidth, qreal value)
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZN12BarChartItem16bottomRightPointEiiidd(
    BarChartItem *self,
    int set,
    int setCount,
    int category,
    qreal barWidth,
    qreal value) {
  return new QPointF(
      self->bottomRightPoint(
          set,
          setCount,
          category,
          barWidth,
          value));
}

//  void BarChartItem::positionLabels()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12BarChartItem14positionLabelsEv(BarChartItem *self) {
  self->BarChartItem::positionLabels();
}

//  void BarChartItem::initializeLayout(int set, int category, int
//      layoutIndex, bool resetAnimation)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12BarChartItem16initializeLayoutEiiib(
    BarChartItem *self,
    int set,
    int category,
    int layoutIndex,
    bool resetAnimation) {
  self->BarChartItem::initializeLayout(
      set,
      category,
      layoutIndex,
      resetAnimation);
}
