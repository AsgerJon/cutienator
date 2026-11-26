//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/6.12.0/QtCharts/private/splinechartitem_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCharts/qchartglobal.h>
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#if QT_CONFIG(charts_spline_chart)
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#include <QtCharts/QtCharts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCharts/6.12.0/QtCharts/private/splinechartitem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtGui/qpainterpath.h>
#include <QtCore/qpoint.h>
#include <QtCore/qlist.h>
#include <QtCore/QList>

//  Only a class built on SplineChartItem may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnSplineChartItem : SplineChartItem {
  using SplineChartItem::updateGeometry;
  using SplineChartItem::mousePressEvent;
  using SplineChartItem::hoverEnterEvent;
  using SplineChartItem::hoverMoveEvent;
  using SplineChartItem::hoverLeaveEvent;
  using SplineChartItem::mouseReleaseEvent;
  using SplineChartItem::mouseDoubleClickEvent;
};

//  const QMetaObject *SplineChartItem::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15SplineChartItem10metaObjectEv(
    const SplineChartItem *self) {
  return self->metaObject();
}

//  void *SplineChartItem::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN15SplineChartItem11qt_metacastEPKc(
    SplineChartItem *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int SplineChartItem::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN15SplineChartItem11qt_metacallEN11QMetaObject4CallEiPPv(
    SplineChartItem *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString SplineChartItem::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15SplineChartItem2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(SplineChartItem::tr(s, c, n));
}

//  SplineChartItem::SplineChartItem(QSplineSeries *series, QGraphicsItem
//      *item)
extern "C" Q_DECL_EXPORT
SplineChartItem *ritual_ZN15SplineChartItemC1EP13QSplineSeriesP13QGraphicsItem(
    QSplineSeries *series,
    QGraphicsItem *item) {
  return new SplineChartItem(series, item);
}

//  QRectF SplineChartItem::boundingRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK15SplineChartItem12boundingRectEv(
    const SplineChartItem *self) {
  return new QRectF(self->boundingRect());
}

//  void SplineChartItem::paint(QPainter *painter, const
//      QStyleOptionGraphicsItem *option, QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN15SplineChartItem5paintEP8QPainterPK24QStyleOptionGraphicsItemP7QWidget(
    SplineChartItem *self,
    QPainter *painter,
    const QStyleOptionGraphicsItem *option,
    QWidget *widget) {
  self->paint(painter, option, widget);
}

//  QPainterPath SplineChartItem::shape() const
extern "C" Q_DECL_EXPORT
QPainterPath *ritual_ZNK15SplineChartItem5shapeEv(
    const SplineChartItem *self) {
  return new QPainterPath(self->shape());
}

//  void SplineChartItem::setControlGeometryPoints(const QList<QPointF>
//      &points)
extern "C" Q_DECL_EXPORT
void ritual_ZN15SplineChartItem24setControlGeometryPointsERK5QListI7QPointFE(
    SplineChartItem *self,
    const QList<QPointF> *points) {
  self->setControlGeometryPoints(*points);
}

//  QList<QPointF> SplineChartItem::controlGeometryPoints() const
extern "C" Q_DECL_EXPORT
QList<QPointF> *ritual_ZNK15SplineChartItem21controlGeometryPointsEv(
    const SplineChartItem *self) {
  return new QList<QPointF>(self->controlGeometryPoints());
}

//  void SplineChartItem::setAnimation(SplineAnimation *animation)
extern "C" Q_DECL_EXPORT
void ritual_ZN15SplineChartItem12setAnimationEP15SplineAnimation(
    SplineChartItem *self,
    SplineAnimation *animation) {
  self->setAnimation(animation);
}

//  ChartAnimation *SplineChartItem::animation() const
extern "C" Q_DECL_EXPORT
ChartAnimation *ritual_ZNK15SplineChartItem9animationEv(
    const SplineChartItem *self) {
  return self->animation();
}

//  void SplineChartItem::handleSeriesUpdated()
extern "C" Q_DECL_EXPORT
void ritual_ZN15SplineChartItem19handleSeriesUpdatedEv(
    SplineChartItem *self) {
  self->handleSeriesUpdated();
}

//  void SplineChartItem::updateGeometry()
extern "C" Q_DECL_EXPORT
void ritual_ZN15SplineChartItem14updateGeometryEv(SplineChartItem *self) {
  self->updateGeometry();
}

//  QList<QPointF> SplineChartItem::calculateControlPoints(const
//      QList<QPointF> &points)
extern "C" Q_DECL_EXPORT
QList<QPointF> *ritual_ZN15SplineChartItem22calculateControlPointsERK5QListI7QPointFE(
    SplineChartItem *self,
    const QList<QPointF> *points) {
  return new QList<QPointF>(self->calculateControlPoints(*points));
}

//  QList<qreal> SplineChartItem::firstControlPoints(const QList<qreal>
//      &list)
extern "C" Q_DECL_EXPORT
QList<qreal> *ritual_ZN15SplineChartItem18firstControlPointsERK5QListIdE(
    SplineChartItem *self,
    const QList<qreal> *list) {
  return new QList<qreal>(self->firstControlPoints(*list));
}

//  void SplineChartItem::updateChart(const QList<QPointF> &oldPoints, const
//      QList<QPointF> &newPoints, int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN15SplineChartItem11updateChartERK5QListI7QPointFES4_i(
    SplineChartItem *self,
    const QList<QPointF> *oldPoints,
    const QList<QPointF> *newPoints,
    int index) {
  self->updateChart(*oldPoints, *newPoints, index);
}

//  void SplineChartItem::mousePressEvent(QGraphicsSceneMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN15SplineChartItem15mousePressEventEP24QGraphicsSceneMouseEvent(
    SplineChartItem *self,
    QGraphicsSceneMouseEvent *event) {
  self->mousePressEvent(event);
}

//  void SplineChartItem::hoverEnterEvent(QGraphicsSceneHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN15SplineChartItem15hoverEnterEventEP24QGraphicsSceneHoverEvent(
    SplineChartItem *self,
    QGraphicsSceneHoverEvent *event) {
  self->hoverEnterEvent(event);
}

//  void SplineChartItem::hoverMoveEvent(QGraphicsSceneHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN15SplineChartItem14hoverMoveEventEP24QGraphicsSceneHoverEvent(
    SplineChartItem *self,
    QGraphicsSceneHoverEvent *event) {
  self->hoverMoveEvent(event);
}

//  void SplineChartItem::hoverLeaveEvent(QGraphicsSceneHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN15SplineChartItem15hoverLeaveEventEP24QGraphicsSceneHoverEvent(
    SplineChartItem *self,
    QGraphicsSceneHoverEvent *event) {
  self->hoverLeaveEvent(event);
}

//  void SplineChartItem::mouseReleaseEvent(QGraphicsSceneMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN15SplineChartItem17mouseReleaseEventEP24QGraphicsSceneMouseEvent(
    SplineChartItem *self,
    QGraphicsSceneMouseEvent *event) {
  self->mouseReleaseEvent(event);
}

//  void SplineChartItem::mouseDoubleClickEvent(QGraphicsSceneMouseEvent
//      *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN15SplineChartItem21mouseDoubleClickEventEP24QGraphicsSceneMouseEvent(
    SplineChartItem *self,
    QGraphicsSceneMouseEvent *event) {
  self->mouseDoubleClickEvent(event);
}

//  QRectF SplineChartItem::boundingRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_own_ZNK15SplineChartItem12boundingRectEv(
    const SplineChartItem *self) {
  return new QRectF(self->SplineChartItem::boundingRect());
}

//  void SplineChartItem::paint(QPainter *painter, const
//      QStyleOptionGraphicsItem *option, QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15SplineChartItem5paintEP8QPainterPK24QStyleOptionGraphicsItemP7QWidget(
    SplineChartItem *self,
    QPainter *painter,
    const QStyleOptionGraphicsItem *option,
    QWidget *widget) {
  self->SplineChartItem::paint(painter, option, widget);
}

//  QPainterPath SplineChartItem::shape() const
extern "C" Q_DECL_EXPORT
QPainterPath *ritual_own_ZNK15SplineChartItem5shapeEv(
    const SplineChartItem *self) {
  return new QPainterPath(self->SplineChartItem::shape());
}

//  ChartAnimation *SplineChartItem::animation() const
extern "C" Q_DECL_EXPORT
ChartAnimation *ritual_own_ZNK15SplineChartItem9animationEv(
    const SplineChartItem *self) {
  return self->SplineChartItem::animation();
}

//  void SplineChartItem::handleSeriesUpdated()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15SplineChartItem19handleSeriesUpdatedEv(
    SplineChartItem *self) {
  self->SplineChartItem::handleSeriesUpdated();
}

//  void SplineChartItem::updateGeometry()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15SplineChartItem14updateGeometryEv(
    SplineChartItem *self) {
  static_cast<OwnSplineChartItem *>(self)->OwnSplineChartItem::updateGeometry();
}

//  void SplineChartItem::mousePressEvent(QGraphicsSceneMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15SplineChartItem15mousePressEventEP24QGraphicsSceneMouseEvent(
    SplineChartItem *self,
    QGraphicsSceneMouseEvent *event) {
  static_cast<OwnSplineChartItem *>(self)->OwnSplineChartItem::mousePressEvent(
      event);
}

//  void SplineChartItem::hoverEnterEvent(QGraphicsSceneHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15SplineChartItem15hoverEnterEventEP24QGraphicsSceneHoverEvent(
    SplineChartItem *self,
    QGraphicsSceneHoverEvent *event) {
  static_cast<OwnSplineChartItem *>(self)->OwnSplineChartItem::hoverEnterEvent(
      event);
}

//  void SplineChartItem::hoverMoveEvent(QGraphicsSceneHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15SplineChartItem14hoverMoveEventEP24QGraphicsSceneHoverEvent(
    SplineChartItem *self,
    QGraphicsSceneHoverEvent *event) {
  static_cast<OwnSplineChartItem *>(self)->OwnSplineChartItem::hoverMoveEvent(
      event);
}

//  void SplineChartItem::hoverLeaveEvent(QGraphicsSceneHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15SplineChartItem15hoverLeaveEventEP24QGraphicsSceneHoverEvent(
    SplineChartItem *self,
    QGraphicsSceneHoverEvent *event) {
  static_cast<OwnSplineChartItem *>(self)->OwnSplineChartItem::hoverLeaveEvent(
      event);
}

//  void SplineChartItem::mouseReleaseEvent(QGraphicsSceneMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15SplineChartItem17mouseReleaseEventEP24QGraphicsSceneMouseEvent(
    SplineChartItem *self,
    QGraphicsSceneMouseEvent *event) {
  static_cast<OwnSplineChartItem *>(self)->OwnSplineChartItem::mouseReleaseEvent(
      event);
}

//  void SplineChartItem::mouseDoubleClickEvent(QGraphicsSceneMouseEvent
//      *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15SplineChartItem21mouseDoubleClickEventEP24QGraphicsSceneMouseEvent(
    SplineChartItem *self,
    QGraphicsSceneMouseEvent *event) {
  static_cast<OwnSplineChartItem *>(self)->OwnSplineChartItem::mouseDoubleClickEvent(
      event);
}

//  a QList<qreal> a ritual of SplineChartItem gave
extern "C" Q_DECL_EXPORT
void ritual_drop_SplineChartItem__QList_qreal(QList<qreal> *self) {
  delete self;
}

#endif  // QT_CONFIG(charts_spline_chart)
