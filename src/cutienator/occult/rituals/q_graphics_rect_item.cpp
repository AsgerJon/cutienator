//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qgraphicsitem.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qgraphicsitem.h>
#include <QtCore/qrect.h>
#include <QtGui/qpainterpath.h>
#include <QtCore/qpoint.h>

//  QGraphicsRectItem::QGraphicsRectItem(QGraphicsItem *parent)
extern "C" Q_DECL_EXPORT
QGraphicsRectItem *ritual_ZN17QGraphicsRectItemC1EP13QGraphicsItem(
    QGraphicsItem *parent) {
  return new QGraphicsRectItem(parent);
}

//  QGraphicsRectItem::QGraphicsRectItem(const QRectF &rect, QGraphicsItem
//      *parent)
extern "C" Q_DECL_EXPORT
QGraphicsRectItem *ritual_ZN17QGraphicsRectItemC1ERK6QRectFP13QGraphicsItem(
    const QRectF *rect,
    QGraphicsItem *parent) {
  return new QGraphicsRectItem(*rect, parent);
}

//  QGraphicsRectItem::QGraphicsRectItem(qreal x, qreal y, qreal w, qreal h,
//      QGraphicsItem *parent)
extern "C" Q_DECL_EXPORT
QGraphicsRectItem *ritual_ZN17QGraphicsRectItemC1EddddP13QGraphicsItem(
    qreal x,
    qreal y,
    qreal w,
    qreal h,
    QGraphicsItem *parent) {
  return new QGraphicsRectItem(x, y, w, h, parent);
}

//  QGraphicsRectItem::~QGraphicsRectItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGraphicsRectItemD1Ev(QGraphicsRectItem *self) {
  delete self;
}

//  QRectF QGraphicsRectItem::rect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK17QGraphicsRectItem4rectEv(const QGraphicsRectItem *self) {
  return new QRectF(self->rect());
}

//  void QGraphicsRectItem::setRect(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGraphicsRectItem7setRectERK6QRectF(
    QGraphicsRectItem *self,
    const QRectF *rect) {
  self->setRect(*rect);
}

//  void QGraphicsRectItem::setRect(qreal x, qreal y, qreal w, qreal h)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGraphicsRectItem7setRectEdddd(
    QGraphicsRectItem *self,
    qreal x,
    qreal y,
    qreal w,
    qreal h) {
  self->setRect(x, y, w, h);
}

//  QRectF QGraphicsRectItem::boundingRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK17QGraphicsRectItem12boundingRectEv(
    const QGraphicsRectItem *self) {
  return new QRectF(self->boundingRect());
}

//  QPainterPath QGraphicsRectItem::shape() const
extern "C" Q_DECL_EXPORT
QPainterPath *ritual_ZNK17QGraphicsRectItem5shapeEv(
    const QGraphicsRectItem *self) {
  return new QPainterPath(self->shape());
}

//  bool QGraphicsRectItem::contains(const QPointF &point) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QGraphicsRectItem8containsERK7QPointF(
    const QGraphicsRectItem *self,
    const QPointF *point) {
  return self->contains(*point);
}

//  void QGraphicsRectItem::paint(QPainter *painter, const
//      QStyleOptionGraphicsItem *option, QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGraphicsRectItem5paintEP8QPainterPK24QStyleOptionGraphicsItemP7QWidget(
    QGraphicsRectItem *self,
    QPainter *painter,
    const QStyleOptionGraphicsItem *option,
    QWidget *widget) {
  self->paint(painter, option, widget);
}

//  bool QGraphicsRectItem::isObscuredBy(const QGraphicsItem *item) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QGraphicsRectItem12isObscuredByEPK13QGraphicsItem(
    const QGraphicsRectItem *self,
    const QGraphicsItem *item) {
  return self->isObscuredBy(item);
}

//  QPainterPath QGraphicsRectItem::opaqueArea() const
extern "C" Q_DECL_EXPORT
QPainterPath *ritual_ZNK17QGraphicsRectItem10opaqueAreaEv(
    const QGraphicsRectItem *self) {
  return new QPainterPath(self->opaqueArea());
}

//  int QGraphicsRectItem::type() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QGraphicsRectItem4typeEv(const QGraphicsRectItem *self) {
  return self->type();
}
