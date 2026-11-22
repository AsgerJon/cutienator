//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qgraphicsitem.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qgraphicsitem.h>
#include <QtGui/qpainterpath.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>

//  QGraphicsPathItem::QGraphicsPathItem(QGraphicsItem *parent)
extern "C" Q_DECL_EXPORT
QGraphicsPathItem *ritual_ZN17QGraphicsPathItemC1EP13QGraphicsItem(
    QGraphicsItem *parent) {
  return new QGraphicsPathItem(parent);
}

//  QGraphicsPathItem::QGraphicsPathItem(const QPainterPath &path,
//      QGraphicsItem *parent)
extern "C" Q_DECL_EXPORT
QGraphicsPathItem *ritual_ZN17QGraphicsPathItemC1ERK12QPainterPathP13QGraphicsItem(
    const QPainterPath *path,
    QGraphicsItem *parent) {
  return new QGraphicsPathItem(*path, parent);
}

//  QGraphicsPathItem::~QGraphicsPathItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGraphicsPathItemD1Ev(QGraphicsPathItem *self) {
  delete self;
}

//  QPainterPath QGraphicsPathItem::path() const
extern "C" Q_DECL_EXPORT
QPainterPath *ritual_ZNK17QGraphicsPathItem4pathEv(
    const QGraphicsPathItem *self) {
  return new QPainterPath(self->path());
}

//  void QGraphicsPathItem::setPath(const QPainterPath &path)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGraphicsPathItem7setPathERK12QPainterPath(
    QGraphicsPathItem *self,
    const QPainterPath *path) {
  self->setPath(*path);
}

//  QRectF QGraphicsPathItem::boundingRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK17QGraphicsPathItem12boundingRectEv(
    const QGraphicsPathItem *self) {
  return new QRectF(self->boundingRect());
}

//  QPainterPath QGraphicsPathItem::shape() const
extern "C" Q_DECL_EXPORT
QPainterPath *ritual_ZNK17QGraphicsPathItem5shapeEv(
    const QGraphicsPathItem *self) {
  return new QPainterPath(self->shape());
}

//  bool QGraphicsPathItem::contains(const QPointF &point) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QGraphicsPathItem8containsERK7QPointF(
    const QGraphicsPathItem *self,
    const QPointF *point) {
  return self->contains(*point);
}

//  void QGraphicsPathItem::paint(QPainter *painter, const
//      QStyleOptionGraphicsItem *option, QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGraphicsPathItem5paintEP8QPainterPK24QStyleOptionGraphicsItemP7QWidget(
    QGraphicsPathItem *self,
    QPainter *painter,
    const QStyleOptionGraphicsItem *option,
    QWidget *widget) {
  self->paint(painter, option, widget);
}

//  bool QGraphicsPathItem::isObscuredBy(const QGraphicsItem *item) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QGraphicsPathItem12isObscuredByEPK13QGraphicsItem(
    const QGraphicsPathItem *self,
    const QGraphicsItem *item) {
  return self->isObscuredBy(item);
}

//  QPainterPath QGraphicsPathItem::opaqueArea() const
extern "C" Q_DECL_EXPORT
QPainterPath *ritual_ZNK17QGraphicsPathItem10opaqueAreaEv(
    const QGraphicsPathItem *self) {
  return new QPainterPath(self->opaqueArea());
}

//  int QGraphicsPathItem::type() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QGraphicsPathItem4typeEv(const QGraphicsPathItem *self) {
  return self->type();
}
