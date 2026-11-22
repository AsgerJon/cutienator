//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qgraphicsitem.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qgraphicsitem.h>
#include <QtCore/qrect.h>
#include <QtGui/qpainterpath.h>
#include <QtCore/qpoint.h>

//  QGraphicsEllipseItem::QGraphicsEllipseItem(QGraphicsItem *parent)
extern "C" Q_DECL_EXPORT
QGraphicsEllipseItem *ritual_ZN20QGraphicsEllipseItemC1EP13QGraphicsItem(
    QGraphicsItem *parent) {
  return new QGraphicsEllipseItem(parent);
}

//  QGraphicsEllipseItem::QGraphicsEllipseItem(const QRectF &rect,
//      QGraphicsItem *parent)
extern "C" Q_DECL_EXPORT
QGraphicsEllipseItem *ritual_ZN20QGraphicsEllipseItemC1ERK6QRectFP13QGraphicsItem(
    const QRectF *rect,
    QGraphicsItem *parent) {
  return new QGraphicsEllipseItem(*rect, parent);
}

//  QGraphicsEllipseItem::QGraphicsEllipseItem(qreal x, qreal y, qreal w,
//      qreal h, QGraphicsItem *parent)
extern "C" Q_DECL_EXPORT
QGraphicsEllipseItem *ritual_ZN20QGraphicsEllipseItemC1EddddP13QGraphicsItem(
    qreal x,
    qreal y,
    qreal w,
    qreal h,
    QGraphicsItem *parent) {
  return new QGraphicsEllipseItem(x, y, w, h, parent);
}

//  QGraphicsEllipseItem::~QGraphicsEllipseItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QGraphicsEllipseItemD1Ev(QGraphicsEllipseItem *self) {
  delete self;
}

//  QRectF QGraphicsEllipseItem::rect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK20QGraphicsEllipseItem4rectEv(
    const QGraphicsEllipseItem *self) {
  return new QRectF(self->rect());
}

//  void QGraphicsEllipseItem::setRect(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QGraphicsEllipseItem7setRectERK6QRectF(
    QGraphicsEllipseItem *self,
    const QRectF *rect) {
  self->setRect(*rect);
}

//  void QGraphicsEllipseItem::setRect(qreal x, qreal y, qreal w, qreal h)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QGraphicsEllipseItem7setRectEdddd(
    QGraphicsEllipseItem *self,
    qreal x,
    qreal y,
    qreal w,
    qreal h) {
  self->setRect(x, y, w, h);
}

//  int QGraphicsEllipseItem::startAngle() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QGraphicsEllipseItem10startAngleEv(
    const QGraphicsEllipseItem *self) {
  return self->startAngle();
}

//  void QGraphicsEllipseItem::setStartAngle(int angle)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QGraphicsEllipseItem13setStartAngleEi(
    QGraphicsEllipseItem *self,
    int angle) {
  self->setStartAngle(angle);
}

//  int QGraphicsEllipseItem::spanAngle() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QGraphicsEllipseItem9spanAngleEv(
    const QGraphicsEllipseItem *self) {
  return self->spanAngle();
}

//  void QGraphicsEllipseItem::setSpanAngle(int angle)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QGraphicsEllipseItem12setSpanAngleEi(
    QGraphicsEllipseItem *self,
    int angle) {
  self->setSpanAngle(angle);
}

//  QRectF QGraphicsEllipseItem::boundingRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK20QGraphicsEllipseItem12boundingRectEv(
    const QGraphicsEllipseItem *self) {
  return new QRectF(self->boundingRect());
}

//  QPainterPath QGraphicsEllipseItem::shape() const
extern "C" Q_DECL_EXPORT
QPainterPath *ritual_ZNK20QGraphicsEllipseItem5shapeEv(
    const QGraphicsEllipseItem *self) {
  return new QPainterPath(self->shape());
}

//  bool QGraphicsEllipseItem::contains(const QPointF &point) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QGraphicsEllipseItem8containsERK7QPointF(
    const QGraphicsEllipseItem *self,
    const QPointF *point) {
  return self->contains(*point);
}

//  void QGraphicsEllipseItem::paint(QPainter *painter, const
//      QStyleOptionGraphicsItem *option, QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QGraphicsEllipseItem5paintEP8QPainterPK24QStyleOptionGraphicsItemP7QWidget(
    QGraphicsEllipseItem *self,
    QPainter *painter,
    const QStyleOptionGraphicsItem *option,
    QWidget *widget) {
  self->paint(painter, option, widget);
}

//  bool QGraphicsEllipseItem::isObscuredBy(const QGraphicsItem *item) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QGraphicsEllipseItem12isObscuredByEPK13QGraphicsItem(
    const QGraphicsEllipseItem *self,
    const QGraphicsItem *item) {
  return self->isObscuredBy(item);
}

//  QPainterPath QGraphicsEllipseItem::opaqueArea() const
extern "C" Q_DECL_EXPORT
QPainterPath *ritual_ZNK20QGraphicsEllipseItem10opaqueAreaEv(
    const QGraphicsEllipseItem *self) {
  return new QPainterPath(self->opaqueArea());
}

//  int QGraphicsEllipseItem::type() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QGraphicsEllipseItem4typeEv(
    const QGraphicsEllipseItem *self) {
  return self->type();
}
