//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qgraphicsitem.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qgraphicsitem.h>
#include <QtGui/qpixmap.h>
#include <QtCore/qpoint.h>
#include <QtCore/qrect.h>
#include <QtGui/qpainterpath.h>

//  QGraphicsPixmapItem::QGraphicsPixmapItem(QGraphicsItem *parent)
extern "C" Q_DECL_EXPORT
QGraphicsPixmapItem *ritual_ZN19QGraphicsPixmapItemC1EP13QGraphicsItem(
    QGraphicsItem *parent) {
  return new QGraphicsPixmapItem(parent);
}

//  QGraphicsPixmapItem::QGraphicsPixmapItem(const QPixmap &pixmap,
//      QGraphicsItem *parent)
extern "C" Q_DECL_EXPORT
QGraphicsPixmapItem *ritual_ZN19QGraphicsPixmapItemC1ERK7QPixmapP13QGraphicsItem(
    const QPixmap *pixmap,
    QGraphicsItem *parent) {
  return new QGraphicsPixmapItem(*pixmap, parent);
}

//  QGraphicsPixmapItem::~QGraphicsPixmapItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphicsPixmapItemD1Ev(QGraphicsPixmapItem *self) {
  delete self;
}

//  QPixmap QGraphicsPixmapItem::pixmap() const
extern "C" Q_DECL_EXPORT
QPixmap *ritual_ZNK19QGraphicsPixmapItem6pixmapEv(
    const QGraphicsPixmapItem *self) {
  return new QPixmap(self->pixmap());
}

//  void QGraphicsPixmapItem::setPixmap(const QPixmap &pixmap)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphicsPixmapItem9setPixmapERK7QPixmap(
    QGraphicsPixmapItem *self,
    const QPixmap *pixmap) {
  self->setPixmap(*pixmap);
}

//  Qt::TransformationMode QGraphicsPixmapItem::transformationMode() const
extern "C" Q_DECL_EXPORT
Qt::TransformationMode ritual_ZNK19QGraphicsPixmapItem18transformationModeEv(
    const QGraphicsPixmapItem *self) {
  return self->transformationMode();
}

//  void QGraphicsPixmapItem::setTransformationMode(Qt::TransformationMode
//      mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphicsPixmapItem21setTransformationModeEN2Qt18TransformationModeE(
    QGraphicsPixmapItem *self,
    Qt::TransformationMode mode) {
  self->setTransformationMode(mode);
}

//  QPointF QGraphicsPixmapItem::offset() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK19QGraphicsPixmapItem6offsetEv(
    const QGraphicsPixmapItem *self) {
  return new QPointF(self->offset());
}

//  void QGraphicsPixmapItem::setOffset(const QPointF &offset)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphicsPixmapItem9setOffsetERK7QPointF(
    QGraphicsPixmapItem *self,
    const QPointF *offset) {
  self->setOffset(*offset);
}

//  void QGraphicsPixmapItem::setOffset(qreal x, qreal y)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphicsPixmapItem9setOffsetEdd(
    QGraphicsPixmapItem *self,
    qreal x,
    qreal y) {
  self->setOffset(x, y);
}

//  QRectF QGraphicsPixmapItem::boundingRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK19QGraphicsPixmapItem12boundingRectEv(
    const QGraphicsPixmapItem *self) {
  return new QRectF(self->boundingRect());
}

//  QPainterPath QGraphicsPixmapItem::shape() const
extern "C" Q_DECL_EXPORT
QPainterPath *ritual_ZNK19QGraphicsPixmapItem5shapeEv(
    const QGraphicsPixmapItem *self) {
  return new QPainterPath(self->shape());
}

//  bool QGraphicsPixmapItem::contains(const QPointF &point) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QGraphicsPixmapItem8containsERK7QPointF(
    const QGraphicsPixmapItem *self,
    const QPointF *point) {
  return self->contains(*point);
}

//  void QGraphicsPixmapItem::paint(QPainter *painter, const
//      QStyleOptionGraphicsItem *option, QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphicsPixmapItem5paintEP8QPainterPK24QStyleOptionGraphicsItemP7QWidget(
    QGraphicsPixmapItem *self,
    QPainter *painter,
    const QStyleOptionGraphicsItem *option,
    QWidget *widget) {
  self->paint(painter, option, widget);
}

//  bool QGraphicsPixmapItem::isObscuredBy(const QGraphicsItem *item) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QGraphicsPixmapItem12isObscuredByEPK13QGraphicsItem(
    const QGraphicsPixmapItem *self,
    const QGraphicsItem *item) {
  return self->isObscuredBy(item);
}

//  QPainterPath QGraphicsPixmapItem::opaqueArea() const
extern "C" Q_DECL_EXPORT
QPainterPath *ritual_ZNK19QGraphicsPixmapItem10opaqueAreaEv(
    const QGraphicsPixmapItem *self) {
  return new QPainterPath(self->opaqueArea());
}

//  int QGraphicsPixmapItem::type() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QGraphicsPixmapItem4typeEv(const QGraphicsPixmapItem *self) {
  return self->type();
}

//  ShapeMode QGraphicsPixmapItem::shapeMode() const
extern "C" Q_DECL_EXPORT
QGraphicsPixmapItem::ShapeMode ritual_ZNK19QGraphicsPixmapItem9shapeModeEv(
    const QGraphicsPixmapItem *self) {
  return self->shapeMode();
}

//  void QGraphicsPixmapItem::setShapeMode(ShapeMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphicsPixmapItem12setShapeModeENS_9ShapeModeE(
    QGraphicsPixmapItem *self,
    QGraphicsPixmapItem::ShapeMode mode) {
  self->setShapeMode(mode);
}
