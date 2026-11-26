//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/6.12.0/QtCharts/private/percentbarchartitem_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCharts/qchartglobal.h>
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#if QT_CONFIG(charts_bar_chart)
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#include <QtCharts/QtCharts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCharts/6.12.0/QtCharts/private/percentbarchartitem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtCore/qlist.h>

//  const QMetaObject *PercentBarChartItem::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19PercentBarChartItem10metaObjectEv(
    const PercentBarChartItem *self) {
  return self->metaObject();
}

//  void *PercentBarChartItem::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN19PercentBarChartItem11qt_metacastEPKc(
    PercentBarChartItem *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int PercentBarChartItem::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN19PercentBarChartItem11qt_metacallEN11QMetaObject4CallEiPPv(
    PercentBarChartItem *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString PercentBarChartItem::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19PercentBarChartItem2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(PercentBarChartItem::tr(s, c, n));
}

//  PercentBarChartItem::PercentBarChartItem(QAbstractBarSeries *series,
//      QGraphicsItem *item)
extern "C" Q_DECL_EXPORT
PercentBarChartItem *ritual_ZN19PercentBarChartItemC1EP18QAbstractBarSeriesP13QGraphicsItem(
    QAbstractBarSeries *series,
    QGraphicsItem *item) {
  return new PercentBarChartItem(series, item);
}

//  QString PercentBarChartItem::generateLabelText(int set, int category,
//      qreal value)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19PercentBarChartItem17generateLabelTextEiid(
    PercentBarChartItem *self,
    int set,
    int category,
    qreal value) {
  return new QString(self->generateLabelText(set, category, value));
}

//  void PercentBarChartItem::handleLabelsPositionChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19PercentBarChartItem27handleLabelsPositionChangedEv(
    PercentBarChartItem *self) {
  self->handleLabelsPositionChanged();
}

//  void PercentBarChartItem::positionLabels()
extern "C" Q_DECL_EXPORT
void ritual_ZN19PercentBarChartItem14positionLabelsEv(
    PercentBarChartItem *self) {
  self->positionLabels();
}

//  QList<QRectF> PercentBarChartItem::calculateLayout()
extern "C" Q_DECL_EXPORT
QList<QRectF> *ritual_ZN19PercentBarChartItem15calculateLayoutEv(
    PercentBarChartItem *self) {
  return new QList<QRectF>(self->calculateLayout());
}

//  void PercentBarChartItem::initializeLayout(int set, int category, int
//      layoutIndex, bool resetAnimation)
extern "C" Q_DECL_EXPORT
void ritual_ZN19PercentBarChartItem16initializeLayoutEiiib(
    PercentBarChartItem *self,
    int set,
    int category,
    int layoutIndex,
    bool resetAnimation) {
  self->initializeLayout(set, category, layoutIndex, resetAnimation);
}

//  void PercentBarChartItem::markLabelsDirty(QBarSet *barset, int index, int
//      count)
extern "C" Q_DECL_EXPORT
void ritual_ZN19PercentBarChartItem15markLabelsDirtyEP7QBarSetii(
    PercentBarChartItem *self,
    QBarSet *barset,
    int index,
    int count) {
  self->markLabelsDirty(barset, index, count);
}

//  QPointF PercentBarChartItem::topLeftPoint(int category, qreal barWidth,
//      qreal value)
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZN19PercentBarChartItem12topLeftPointEidd(
    PercentBarChartItem *self,
    int category,
    qreal barWidth,
    qreal value) {
  return new QPointF(self->topLeftPoint(category, barWidth, value));
}

//  QPointF PercentBarChartItem::bottomRightPoint(int category, qreal
//      barWidth, qreal value)
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZN19PercentBarChartItem16bottomRightPointEidd(
    PercentBarChartItem *self,
    int category,
    qreal barWidth,
    qreal value) {
  return new QPointF(self->bottomRightPoint(category, barWidth, value));
}

//  QString PercentBarChartItem::generateLabelText(int set, int category,
//      qreal value)
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZN19PercentBarChartItem17generateLabelTextEiid(
    PercentBarChartItem *self,
    int set,
    int category,
    qreal value) {
  return new QString(
      self->PercentBarChartItem::generateLabelText(
          set,
          category,
          value));
}

//  void PercentBarChartItem::positionLabels()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19PercentBarChartItem14positionLabelsEv(
    PercentBarChartItem *self) {
  self->PercentBarChartItem::positionLabels();
}

//  void PercentBarChartItem::initializeLayout(int set, int category, int
//      layoutIndex, bool resetAnimation)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19PercentBarChartItem16initializeLayoutEiiib(
    PercentBarChartItem *self,
    int set,
    int category,
    int layoutIndex,
    bool resetAnimation) {
  self->PercentBarChartItem::initializeLayout(
      set,
      category,
      layoutIndex,
      resetAnimation);
}

//  void PercentBarChartItem::markLabelsDirty(QBarSet *barset, int index, int
//      count)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19PercentBarChartItem15markLabelsDirtyEP7QBarSetii(
    PercentBarChartItem *self,
    QBarSet *barset,
    int index,
    int count) {
  self->PercentBarChartItem::markLabelsDirty(barset, index, count);
}

#endif  // QT_CONFIG(charts_bar_chart)
