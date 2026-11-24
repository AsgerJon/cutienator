//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/6.12.0/QtCharts/private/stackedbarchartitem_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCharts/qchartglobal.h>
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#if QT_CONFIG(charts_bar_chart)
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#include <QtCharts/QtCharts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCharts/6.12.0/QtCharts/private/stackedbarchartitem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtCore/qlist.h>

//  const QMetaObject *StackedBarChartItem::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19StackedBarChartItem10metaObjectEv(
    const StackedBarChartItem *self) {
  return self->metaObject();
}

//  QString StackedBarChartItem::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19StackedBarChartItem2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(StackedBarChartItem::tr(s, c, n));
}

//  StackedBarChartItem::StackedBarChartItem(QAbstractBarSeries *series,
//      QGraphicsItem *item)
extern "C" Q_DECL_EXPORT
StackedBarChartItem *ritual_ZN19StackedBarChartItemC1EP18QAbstractBarSeriesP13QGraphicsItem(
    QAbstractBarSeries *series,
    QGraphicsItem *item) {
  return new StackedBarChartItem(series, item);
}

//  void StackedBarChartItem::handleLabelsPositionChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19StackedBarChartItem27handleLabelsPositionChangedEv(
    StackedBarChartItem *self) {
  self->handleLabelsPositionChanged();
}

//  void StackedBarChartItem::positionLabels()
extern "C" Q_DECL_EXPORT
void ritual_ZN19StackedBarChartItem14positionLabelsEv(
    StackedBarChartItem *self) {
  self->positionLabels();
}

//  QList<QRectF> StackedBarChartItem::calculateLayout()
extern "C" Q_DECL_EXPORT
QList<QRectF> *ritual_ZN19StackedBarChartItem15calculateLayoutEv(
    StackedBarChartItem *self) {
  return new QList<QRectF>(self->calculateLayout());
}

//  void StackedBarChartItem::initializeLayout(int set, int category, int
//      layoutIndex, bool resetAnimation)
extern "C" Q_DECL_EXPORT
void ritual_ZN19StackedBarChartItem16initializeLayoutEiiib(
    StackedBarChartItem *self,
    int set,
    int category,
    int layoutIndex,
    bool resetAnimation) {
  self->initializeLayout(set, category, layoutIndex, resetAnimation);
}

//  QPointF StackedBarChartItem::topLeftPoint(int category, qreal barWidth,
//      qreal value)
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZN19StackedBarChartItem12topLeftPointEidd(
    StackedBarChartItem *self,
    int category,
    qreal barWidth,
    qreal value) {
  return new QPointF(self->topLeftPoint(category, barWidth, value));
}

//  QPointF StackedBarChartItem::bottomRightPoint(int category, qreal
//      barWidth, qreal value)
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZN19StackedBarChartItem16bottomRightPointEidd(
    StackedBarChartItem *self,
    int category,
    qreal barWidth,
    qreal value) {
  return new QPointF(self->bottomRightPoint(category, barWidth, value));
}

//  void StackedBarChartItem::positionLabels()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19StackedBarChartItem14positionLabelsEv(
    StackedBarChartItem *self) {
  self->StackedBarChartItem::positionLabels();
}

//  void StackedBarChartItem::initializeLayout(int set, int category, int
//      layoutIndex, bool resetAnimation)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19StackedBarChartItem16initializeLayoutEiiib(
    StackedBarChartItem *self,
    int set,
    int category,
    int layoutIndex,
    bool resetAnimation) {
  self->StackedBarChartItem::initializeLayout(
      set,
      category,
      layoutIndex,
      resetAnimation);
}

#endif  // QT_CONFIG(charts_bar_chart)
