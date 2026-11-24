//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/6.12.0/QtCharts/private/horizontalpercentbarchartitem_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCharts/qchartglobal.h>
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#if QT_CONFIG(charts_bar_chart)
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#include <QtCharts/QtCharts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCharts/6.12.0/QtCharts/private/horizontalpercentbarchartitem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtCore/qlist.h>

//  const QMetaObject *HorizontalPercentBarChartItem::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK29HorizontalPercentBarChartItem10metaObjectEv(
    const HorizontalPercentBarChartItem *self) {
  return self->metaObject();
}

//  QString HorizontalPercentBarChartItem::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN29HorizontalPercentBarChartItem2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(HorizontalPercentBarChartItem::tr(s, c, n));
}

//  HorizontalPercentBarChartItem::HorizontalPercentBarChartItem(QAbstractBar
//      Series *series, QGraphicsItem *item)
extern "C" Q_DECL_EXPORT
HorizontalPercentBarChartItem *ritual_ZN29HorizontalPercentBarChartItemC1EP18QAbstractBarSeriesP13QGraphicsItem(
    QAbstractBarSeries *series,
    QGraphicsItem *item) {
  return new HorizontalPercentBarChartItem(series, item);
}

//  QString HorizontalPercentBarChartItem::generateLabelText(int set, int
//      category, qreal value)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN29HorizontalPercentBarChartItem17generateLabelTextEiid(
    HorizontalPercentBarChartItem *self,
    int set,
    int category,
    qreal value) {
  return new QString(self->generateLabelText(set, category, value));
}

//  QList<QRectF> HorizontalPercentBarChartItem::calculateLayout()
extern "C" Q_DECL_EXPORT
QList<QRectF> *ritual_ZN29HorizontalPercentBarChartItem15calculateLayoutEv(
    HorizontalPercentBarChartItem *self) {
  return new QList<QRectF>(self->calculateLayout());
}

//  void HorizontalPercentBarChartItem::initializeLayout(int set, int
//      category, int layoutIndex, bool resetAnimation)
extern "C" Q_DECL_EXPORT
void ritual_ZN29HorizontalPercentBarChartItem16initializeLayoutEiiib(
    HorizontalPercentBarChartItem *self,
    int set,
    int category,
    int layoutIndex,
    bool resetAnimation) {
  self->initializeLayout(set, category, layoutIndex, resetAnimation);
}

//  void HorizontalPercentBarChartItem::markLabelsDirty(QBarSet *barset, int
//      index, int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN29HorizontalPercentBarChartItem15markLabelsDirtyEP7QBarSetii(
    HorizontalPercentBarChartItem *self,
    QBarSet *barset,
    int index,
    int count) {
  self->markLabelsDirty(barset, index, count);
}

//  QPointF HorizontalPercentBarChartItem::topLeftPoint(int category, qreal
//      barWidth, qreal value)
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZN29HorizontalPercentBarChartItem12topLeftPointEidd(
    HorizontalPercentBarChartItem *self,
    int category,
    qreal barWidth,
    qreal value) {
  return new QPointF(self->topLeftPoint(category, barWidth, value));
}

//  QPointF HorizontalPercentBarChartItem::bottomRightPoint(int category,
//      qreal barWidth, qreal value)
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZN29HorizontalPercentBarChartItem16bottomRightPointEidd(
    HorizontalPercentBarChartItem *self,
    int category,
    qreal barWidth,
    qreal value) {
  return new QPointF(self->bottomRightPoint(category, barWidth, value));
}

//  QString HorizontalPercentBarChartItem::generateLabelText(int set, int
//      category, qreal value)
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZN29HorizontalPercentBarChartItem17generateLabelTextEiid(
    HorizontalPercentBarChartItem *self,
    int set,
    int category,
    qreal value) {
  return new QString(
      self->HorizontalPercentBarChartItem::generateLabelText(
          set,
          category,
          value));
}

//  void HorizontalPercentBarChartItem::initializeLayout(int set, int
//      category, int layoutIndex, bool resetAnimation)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN29HorizontalPercentBarChartItem16initializeLayoutEiiib(
    HorizontalPercentBarChartItem *self,
    int set,
    int category,
    int layoutIndex,
    bool resetAnimation) {
  self->HorizontalPercentBarChartItem::initializeLayout(
      set,
      category,
      layoutIndex,
      resetAnimation);
}

//  void HorizontalPercentBarChartItem::markLabelsDirty(QBarSet *barset, int
//      index, int count)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN29HorizontalPercentBarChartItem15markLabelsDirtyEP7QBarSetii(
    HorizontalPercentBarChartItem *self,
    QBarSet *barset,
    int index,
    int count) {
  self->HorizontalPercentBarChartItem::markLabelsDirty(barset, index, count);
}

#endif  // QT_CONFIG(charts_bar_chart)
