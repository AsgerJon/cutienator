//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qgraphicsitem.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qgraphicsitem.h>
#include <QtGui/qpen.h>
#include <QtGui/qbrush.h>
#include <QtGui/qpainterpath.h>

//  QAbstractGraphicsShapeItem::~QAbstractGraphicsShapeItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QAbstractGraphicsShapeItemD1Ev(
    QAbstractGraphicsShapeItem *self) {
  delete self;
}

//  QPen QAbstractGraphicsShapeItem::pen() const
extern "C" Q_DECL_EXPORT
QPen *ritual_ZNK26QAbstractGraphicsShapeItem3penEv(
    const QAbstractGraphicsShapeItem *self) {
  return new QPen(self->pen());
}

//  void QAbstractGraphicsShapeItem::setPen(const QPen &pen)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QAbstractGraphicsShapeItem6setPenERK4QPen(
    QAbstractGraphicsShapeItem *self,
    const QPen *pen) {
  self->setPen(*pen);
}

//  QBrush QAbstractGraphicsShapeItem::brush() const
extern "C" Q_DECL_EXPORT
QBrush *ritual_ZNK26QAbstractGraphicsShapeItem5brushEv(
    const QAbstractGraphicsShapeItem *self) {
  return new QBrush(self->brush());
}

//  void QAbstractGraphicsShapeItem::setBrush(const QBrush &brush)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QAbstractGraphicsShapeItem8setBrushERK6QBrush(
    QAbstractGraphicsShapeItem *self,
    const QBrush *brush) {
  self->setBrush(*brush);
}

//  bool QAbstractGraphicsShapeItem::isObscuredBy(const QGraphicsItem *item)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK26QAbstractGraphicsShapeItem12isObscuredByEPK13QGraphicsItem(
    const QAbstractGraphicsShapeItem *self,
    const QGraphicsItem *item) {
  return self->isObscuredBy(item);
}

//  QPainterPath QAbstractGraphicsShapeItem::opaqueArea() const
extern "C" Q_DECL_EXPORT
QPainterPath *ritual_ZNK26QAbstractGraphicsShapeItem10opaqueAreaEv(
    const QAbstractGraphicsShapeItem *self) {
  return new QPainterPath(self->opaqueArea());
}
