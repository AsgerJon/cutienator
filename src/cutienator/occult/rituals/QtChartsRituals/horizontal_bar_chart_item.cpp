//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/6.12.0/QtCharts/private/horizontalbarchartitem_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCharts/qchartglobal.h>
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#if QT_CONFIG(charts_bar_chart)
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#include <QtCharts/QtCharts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCharts/6.12.0/QtCharts/private/horizontalbarchartitem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtCore/qlist.h>

//  const QMetaObject *HorizontalBarChartItem::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK22HorizontalBarChartItem10metaObjectEv(
    const HorizontalBarChartItem *self) {
  return self->metaObject();
}

//  QString HorizontalBarChartItem::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN22HorizontalBarChartItem2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(HorizontalBarChartItem::tr(s, c, n));
}

//  HorizontalBarChartItem::HorizontalBarChartItem(QAbstractBarSeries
//      *series, QGraphicsItem *item)
extern "C" Q_DECL_EXPORT
HorizontalBarChartItem *ritual_ZN22HorizontalBarChartItemC1EP18QAbstractBarSeriesP13QGraphicsItem(
    QAbstractBarSeries *series,
    QGraphicsItem *item) {
  return new HorizontalBarChartItem(series, item);
}

//  QList<QRectF> HorizontalBarChartItem::calculateLayout()
extern "C" Q_DECL_EXPORT
QList<QRectF> *ritual_ZN22HorizontalBarChartItem15calculateLayoutEv(
    HorizontalBarChartItem *self) {
  return new QList<QRectF>(self->calculateLayout());
}

//  void HorizontalBarChartItem::initializeLayout(int set, int category, int
//      layoutIndex, bool resetAnimation)
extern "C" Q_DECL_EXPORT
void ritual_ZN22HorizontalBarChartItem16initializeLayoutEiiib(
    HorizontalBarChartItem *self,
    int set,
    int category,
    int layoutIndex,
    bool resetAnimation) {
  self->initializeLayout(set, category, layoutIndex, resetAnimation);
}

//  QPointF HorizontalBarChartItem::topLeftPoint(int set, int setCount, int
//      category, qreal barWidth, qreal value)
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZN22HorizontalBarChartItem12topLeftPointEiiidd(
    HorizontalBarChartItem *self,
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

//  QPointF HorizontalBarChartItem::bottomRightPoint(int set, int setCount,
//      int category, qreal barWidth, qreal value)
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZN22HorizontalBarChartItem16bottomRightPointEiiidd(
    HorizontalBarChartItem *self,
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

//  void HorizontalBarChartItem::initializeLayout(int set, int category, int
//      layoutIndex, bool resetAnimation)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22HorizontalBarChartItem16initializeLayoutEiiib(
    HorizontalBarChartItem *self,
    int set,
    int category,
    int layoutIndex,
    bool resetAnimation) {
  self->HorizontalBarChartItem::initializeLayout(
      set,
      category,
      layoutIndex,
      resetAnimation);
}

#endif  // QT_CONFIG(charts_bar_chart)
