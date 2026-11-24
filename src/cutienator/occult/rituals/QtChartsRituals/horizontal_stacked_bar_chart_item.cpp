//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/6.12.0/QtCharts/private/horizontalstackedbarchartitem_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCharts/qchartglobal.h>
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#if QT_CONFIG(charts_bar_chart)
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#include <QtCharts/QtCharts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCharts/6.12.0/QtCharts/private/horizontalstackedbarchartitem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtCore/qlist.h>

//  const QMetaObject *HorizontalStackedBarChartItem::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK29HorizontalStackedBarChartItem10metaObjectEv(
    const HorizontalStackedBarChartItem *self) {
  return self->metaObject();
}

//  QString HorizontalStackedBarChartItem::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN29HorizontalStackedBarChartItem2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(HorizontalStackedBarChartItem::tr(s, c, n));
}

//  HorizontalStackedBarChartItem::HorizontalStackedBarChartItem(QAbstractBar
//      Series *series, QGraphicsItem *item)
extern "C" Q_DECL_EXPORT
HorizontalStackedBarChartItem *ritual_ZN29HorizontalStackedBarChartItemC1EP18QAbstractBarSeriesP13QGraphicsItem(
    QAbstractBarSeries *series,
    QGraphicsItem *item) {
  return new HorizontalStackedBarChartItem(series, item);
}

//  QList<QRectF> HorizontalStackedBarChartItem::calculateLayout()
extern "C" Q_DECL_EXPORT
QList<QRectF> *ritual_ZN29HorizontalStackedBarChartItem15calculateLayoutEv(
    HorizontalStackedBarChartItem *self) {
  return new QList<QRectF>(self->calculateLayout());
}

//  void HorizontalStackedBarChartItem::initializeLayout(int set, int
//      category, int layoutIndex, bool resetAnimation)
extern "C" Q_DECL_EXPORT
void ritual_ZN29HorizontalStackedBarChartItem16initializeLayoutEiiib(
    HorizontalStackedBarChartItem *self,
    int set,
    int category,
    int layoutIndex,
    bool resetAnimation) {
  self->initializeLayout(set, category, layoutIndex, resetAnimation);
}

//  QPointF HorizontalStackedBarChartItem::topLeftPoint(int category, qreal
//      barWidth, qreal value)
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZN29HorizontalStackedBarChartItem12topLeftPointEidd(
    HorizontalStackedBarChartItem *self,
    int category,
    qreal barWidth,
    qreal value) {
  return new QPointF(self->topLeftPoint(category, barWidth, value));
}

//  QPointF HorizontalStackedBarChartItem::bottomRightPoint(int category,
//      qreal barWidth, qreal value)
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZN29HorizontalStackedBarChartItem16bottomRightPointEidd(
    HorizontalStackedBarChartItem *self,
    int category,
    qreal barWidth,
    qreal value) {
  return new QPointF(self->bottomRightPoint(category, barWidth, value));
}

//  void HorizontalStackedBarChartItem::initializeLayout(int set, int
//      category, int layoutIndex, bool resetAnimation)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN29HorizontalStackedBarChartItem16initializeLayoutEiiib(
    HorizontalStackedBarChartItem *self,
    int set,
    int category,
    int layoutIndex,
    bool resetAnimation) {
  self->HorizontalStackedBarChartItem::initializeLayout(
      set,
      category,
      layoutIndex,
      resetAnimation);
}

#endif  // QT_CONFIG(charts_bar_chart)
