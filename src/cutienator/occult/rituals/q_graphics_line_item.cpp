//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qgraphicsitem.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qgraphicsitem.h>
#include <QtCore/qline.h>
#include <QtGui/qpen.h>
#include <QtCore/qrect.h>
#include <QtGui/qpainterpath.h>
#include <QtCore/qpoint.h>

//  QGraphicsLineItem::QGraphicsLineItem(QGraphicsItem *parent)
extern "C" Q_DECL_EXPORT
QGraphicsLineItem *ritual_ZN17QGraphicsLineItemC1EP13QGraphicsItem(
    QGraphicsItem *parent) {
  return new QGraphicsLineItem(parent);
}

//  QGraphicsLineItem::QGraphicsLineItem(const QLineF &line, QGraphicsItem
//      *parent)
extern "C" Q_DECL_EXPORT
QGraphicsLineItem *ritual_ZN17QGraphicsLineItemC1ERK6QLineFP13QGraphicsItem(
    const QLineF *line,
    QGraphicsItem *parent) {
  return new QGraphicsLineItem(*line, parent);
}

//  QGraphicsLineItem::QGraphicsLineItem(qreal x1, qreal y1, qreal x2, qreal
//      y2, QGraphicsItem *parent)
extern "C" Q_DECL_EXPORT
QGraphicsLineItem *ritual_ZN17QGraphicsLineItemC1EddddP13QGraphicsItem(
    qreal x1,
    qreal y1,
    qreal x2,
    qreal y2,
    QGraphicsItem *parent) {
  return new QGraphicsLineItem(x1, y1, x2, y2, parent);
}

//  QGraphicsLineItem::~QGraphicsLineItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGraphicsLineItemD1Ev(QGraphicsLineItem *self) {
  delete self;
}

//  QPen QGraphicsLineItem::pen() const
extern "C" Q_DECL_EXPORT
QPen *ritual_ZNK17QGraphicsLineItem3penEv(const QGraphicsLineItem *self) {
  return new QPen(self->pen());
}

//  void QGraphicsLineItem::setPen(const QPen &pen)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGraphicsLineItem6setPenERK4QPen(
    QGraphicsLineItem *self,
    const QPen *pen) {
  self->setPen(*pen);
}

//  QLineF QGraphicsLineItem::line() const
extern "C" Q_DECL_EXPORT
QLineF *ritual_ZNK17QGraphicsLineItem4lineEv(const QGraphicsLineItem *self) {
  return new QLineF(self->line());
}

//  void QGraphicsLineItem::setLine(const QLineF &line)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGraphicsLineItem7setLineERK6QLineF(
    QGraphicsLineItem *self,
    const QLineF *line) {
  self->setLine(*line);
}

//  void QGraphicsLineItem::setLine(qreal x1, qreal y1, qreal x2, qreal y2)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGraphicsLineItem7setLineEdddd(
    QGraphicsLineItem *self,
    qreal x1,
    qreal y1,
    qreal x2,
    qreal y2) {
  self->setLine(x1, y1, x2, y2);
}

//  QRectF QGraphicsLineItem::boundingRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK17QGraphicsLineItem12boundingRectEv(
    const QGraphicsLineItem *self) {
  return new QRectF(self->boundingRect());
}

//  QPainterPath QGraphicsLineItem::shape() const
extern "C" Q_DECL_EXPORT
QPainterPath *ritual_ZNK17QGraphicsLineItem5shapeEv(
    const QGraphicsLineItem *self) {
  return new QPainterPath(self->shape());
}

//  bool QGraphicsLineItem::contains(const QPointF &point) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QGraphicsLineItem8containsERK7QPointF(
    const QGraphicsLineItem *self,
    const QPointF *point) {
  return self->contains(*point);
}

//  void QGraphicsLineItem::paint(QPainter *painter, const
//      QStyleOptionGraphicsItem *option, QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGraphicsLineItem5paintEP8QPainterPK24QStyleOptionGraphicsItemP7QWidget(
    QGraphicsLineItem *self,
    QPainter *painter,
    const QStyleOptionGraphicsItem *option,
    QWidget *widget) {
  self->paint(painter, option, widget);
}

//  bool QGraphicsLineItem::isObscuredBy(const QGraphicsItem *item) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QGraphicsLineItem12isObscuredByEPK13QGraphicsItem(
    const QGraphicsLineItem *self,
    const QGraphicsItem *item) {
  return self->isObscuredBy(item);
}

//  QPainterPath QGraphicsLineItem::opaqueArea() const
extern "C" Q_DECL_EXPORT
QPainterPath *ritual_ZNK17QGraphicsLineItem10opaqueAreaEv(
    const QGraphicsLineItem *self) {
  return new QPainterPath(self->opaqueArea());
}

//  int QGraphicsLineItem::type() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QGraphicsLineItem4typeEv(const QGraphicsLineItem *self) {
  return self->type();
}
