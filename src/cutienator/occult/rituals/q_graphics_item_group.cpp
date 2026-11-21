//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qgraphicsitem.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qgraphicsitem.h>
#include <QtCore/qrect.h>
#include <QtGui/qpainterpath.h>

//  QGraphicsItemGroup::QGraphicsItemGroup(QGraphicsItem *parent)
extern "C" Q_DECL_EXPORT
QGraphicsItemGroup *ritual_ZN18QGraphicsItemGroupC1EP13QGraphicsItem(
    QGraphicsItem *parent) {
  return new QGraphicsItemGroup(parent);
}

//  QGraphicsItemGroup::~QGraphicsItemGroup()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QGraphicsItemGroupD1Ev(QGraphicsItemGroup *self) {
  delete self;
}

//  void QGraphicsItemGroup::addToGroup(QGraphicsItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QGraphicsItemGroup10addToGroupEP13QGraphicsItem(
    QGraphicsItemGroup *self,
    QGraphicsItem *item) {
  self->addToGroup(item);
}

//  void QGraphicsItemGroup::removeFromGroup(QGraphicsItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QGraphicsItemGroup15removeFromGroupEP13QGraphicsItem(
    QGraphicsItemGroup *self,
    QGraphicsItem *item) {
  self->removeFromGroup(item);
}

//  QRectF QGraphicsItemGroup::boundingRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK18QGraphicsItemGroup12boundingRectEv(
    const QGraphicsItemGroup *self) {
  return new QRectF(self->boundingRect());
}

//  void QGraphicsItemGroup::paint(QPainter *painter, const
//      QStyleOptionGraphicsItem *option, QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QGraphicsItemGroup5paintEP8QPainterPK24QStyleOptionGraphicsItemP7QWidget(
    QGraphicsItemGroup *self,
    QPainter *painter,
    const QStyleOptionGraphicsItem *option,
    QWidget *widget) {
  self->paint(painter, option, widget);
}

//  bool QGraphicsItemGroup::isObscuredBy(const QGraphicsItem *item) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QGraphicsItemGroup12isObscuredByEPK13QGraphicsItem(
    const QGraphicsItemGroup *self,
    const QGraphicsItem *item) {
  return self->isObscuredBy(item);
}

//  QPainterPath QGraphicsItemGroup::opaqueArea() const
extern "C" Q_DECL_EXPORT
QPainterPath *ritual_ZNK18QGraphicsItemGroup10opaqueAreaEv(
    const QGraphicsItemGroup *self) {
  return new QPainterPath(self->opaqueArea());
}

//  int QGraphicsItemGroup::type() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QGraphicsItemGroup4typeEv(const QGraphicsItemGroup *self) {
  return self->type();
}
