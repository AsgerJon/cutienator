//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/6.12.0/QtCharts/private/linearrowitem_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#include <QtCharts/QtCharts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCharts/6.12.0/QtCharts/private/linearrowitem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <QtGui/qpainterpath.h>

//  Only a class built on LineArrowItem may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnLineArrowItem : LineArrowItem {
  using LineArrowItem::mousePressEvent;
  using LineArrowItem::boundingRect;
  using LineArrowItem::shape;
};

//  LineArrowItem::LineArrowItem(ChartAxisElement *axis, QGraphicsItem
//      *parent)
extern "C" Q_DECL_EXPORT
LineArrowItem *ritual_ZN13LineArrowItemC1EP16ChartAxisElementP13QGraphicsItem(
    ChartAxisElement *axis,
    QGraphicsItem *parent) {
  return new LineArrowItem(axis, parent);
}

//  void LineArrowItem::mousePressEvent(QGraphicsSceneMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN13LineArrowItem15mousePressEventEP24QGraphicsSceneMouseEvent(
    LineArrowItem *self,
    QGraphicsSceneMouseEvent *event) {
  self->mousePressEvent(event);
}

//  QRectF LineArrowItem::boundingRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK13LineArrowItem12boundingRectEv(
    const LineArrowItem *self) {
  return new QRectF(self->boundingRect());
}

//  QPainterPath LineArrowItem::shape() const
extern "C" Q_DECL_EXPORT
QPainterPath *ritual_ZNK13LineArrowItem5shapeEv(const LineArrowItem *self) {
  return new QPainterPath(self->shape());
}

//  void LineArrowItem::mousePressEvent(QGraphicsSceneMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13LineArrowItem15mousePressEventEP24QGraphicsSceneMouseEvent(
    LineArrowItem *self,
    QGraphicsSceneMouseEvent *event) {
  static_cast<OwnLineArrowItem *>(self)->OwnLineArrowItem::mousePressEvent(
      event);
}

//  QRectF LineArrowItem::boundingRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_own_ZNK13LineArrowItem12boundingRectEv(
    const LineArrowItem *self) {
  return new QRectF(
      static_cast<const OwnLineArrowItem *>(self)->OwnLineArrowItem::boundingRect());
}

//  QPainterPath LineArrowItem::shape() const
extern "C" Q_DECL_EXPORT
QPainterPath *ritual_own_ZNK13LineArrowItem5shapeEv(
    const LineArrowItem *self) {
  return new QPainterPath(
      static_cast<const OwnLineArrowItem *>(self)->OwnLineArrowItem::shape());
}
