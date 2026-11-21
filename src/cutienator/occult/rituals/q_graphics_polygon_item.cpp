//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qgraphicsitem.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qgraphicsitem.h>
#include <QtGui/qpolygon.h>
#include <QtCore/qrect.h>
#include <QtGui/qpainterpath.h>
#include <QtCore/qpoint.h>

//  QGraphicsPolygonItem::QGraphicsPolygonItem(QGraphicsItem *parent)
extern "C" Q_DECL_EXPORT
QGraphicsPolygonItem *ritual_ZN20QGraphicsPolygonItemC1EP13QGraphicsItem(
    QGraphicsItem *parent) {
  return new QGraphicsPolygonItem(parent);
}

//  QGraphicsPolygonItem::QGraphicsPolygonItem(const QPolygonF &polygon,
//      QGraphicsItem *parent)
extern "C" Q_DECL_EXPORT
QGraphicsPolygonItem *ritual_ZN20QGraphicsPolygonItemC1ERK9QPolygonFP13QGraphicsItem(
    const QPolygonF *polygon,
    QGraphicsItem *parent) {
  return new QGraphicsPolygonItem(*polygon, parent);
}

//  QGraphicsPolygonItem::~QGraphicsPolygonItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QGraphicsPolygonItemD1Ev(QGraphicsPolygonItem *self) {
  delete self;
}

//  QPolygonF QGraphicsPolygonItem::polygon() const
extern "C" Q_DECL_EXPORT
QPolygonF *ritual_ZNK20QGraphicsPolygonItem7polygonEv(
    const QGraphicsPolygonItem *self) {
  return new QPolygonF(self->polygon());
}

//  void QGraphicsPolygonItem::setPolygon(const QPolygonF &polygon)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QGraphicsPolygonItem10setPolygonERK9QPolygonF(
    QGraphicsPolygonItem *self,
    const QPolygonF *polygon) {
  self->setPolygon(*polygon);
}

//  Qt::FillRule QGraphicsPolygonItem::fillRule() const
extern "C" Q_DECL_EXPORT
Qt::FillRule ritual_ZNK20QGraphicsPolygonItem8fillRuleEv(
    const QGraphicsPolygonItem *self) {
  return self->fillRule();
}

//  void QGraphicsPolygonItem::setFillRule(Qt::FillRule rule)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QGraphicsPolygonItem11setFillRuleEN2Qt8FillRuleE(
    QGraphicsPolygonItem *self,
    Qt::FillRule rule) {
  self->setFillRule(rule);
}

//  QRectF QGraphicsPolygonItem::boundingRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK20QGraphicsPolygonItem12boundingRectEv(
    const QGraphicsPolygonItem *self) {
  return new QRectF(self->boundingRect());
}

//  QPainterPath QGraphicsPolygonItem::shape() const
extern "C" Q_DECL_EXPORT
QPainterPath *ritual_ZNK20QGraphicsPolygonItem5shapeEv(
    const QGraphicsPolygonItem *self) {
  return new QPainterPath(self->shape());
}

//  bool QGraphicsPolygonItem::contains(const QPointF &point) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QGraphicsPolygonItem8containsERK7QPointF(
    const QGraphicsPolygonItem *self,
    const QPointF *point) {
  return self->contains(*point);
}

//  void QGraphicsPolygonItem::paint(QPainter *painter, const
//      QStyleOptionGraphicsItem *option, QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QGraphicsPolygonItem5paintEP8QPainterPK24QStyleOptionGraphicsItemP7QWidget(
    QGraphicsPolygonItem *self,
    QPainter *painter,
    const QStyleOptionGraphicsItem *option,
    QWidget *widget) {
  self->paint(painter, option, widget);
}

//  bool QGraphicsPolygonItem::isObscuredBy(const QGraphicsItem *item) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QGraphicsPolygonItem12isObscuredByEPK13QGraphicsItem(
    const QGraphicsPolygonItem *self,
    const QGraphicsItem *item) {
  return self->isObscuredBy(item);
}

//  QPainterPath QGraphicsPolygonItem::opaqueArea() const
extern "C" Q_DECL_EXPORT
QPainterPath *ritual_ZNK20QGraphicsPolygonItem10opaqueAreaEv(
    const QGraphicsPolygonItem *self) {
  return new QPainterPath(self->opaqueArea());
}

//  int QGraphicsPolygonItem::type() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QGraphicsPolygonItem4typeEv(
    const QGraphicsPolygonItem *self) {
  return self->type();
}
