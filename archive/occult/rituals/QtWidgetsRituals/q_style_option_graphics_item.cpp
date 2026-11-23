//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qstyleoption.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qstyleoption.h>
#include <QtGui/qtransform.h>

//  QStyleOptionGraphicsItem::QStyleOptionGraphicsItem()
extern "C" Q_DECL_EXPORT
QStyleOptionGraphicsItem *ritual_ZN24QStyleOptionGraphicsItemC1Ev() {
  return new QStyleOptionGraphicsItem();
}

//  QStyleOptionGraphicsItem::QStyleOptionGraphicsItem(const
//      QStyleOptionGraphicsItem &other)
extern "C" Q_DECL_EXPORT
QStyleOptionGraphicsItem *ritual_ZN24QStyleOptionGraphicsItemC1ERKS_(
    const QStyleOptionGraphicsItem *other) {
  return new QStyleOptionGraphicsItem(*other);
}

//  qreal QStyleOptionGraphicsItem::levelOfDetailFromTransform(const
//      QTransform &worldTransform)
extern "C" Q_DECL_EXPORT
qreal ritual_ZN24QStyleOptionGraphicsItem26levelOfDetailFromTransformERK10QTransform(
    const QTransform *worldTransform) {
  return QStyleOptionGraphicsItem::levelOfDetailFromTransform(
      *worldTransform);
}

//  QStyleOptionGraphicsItem::QStyleOptionGraphicsItem(int version)
extern "C" Q_DECL_EXPORT
QStyleOptionGraphicsItem *ritual_ZN24QStyleOptionGraphicsItemC1Ei(
    int version) {
  return new QStyleOptionGraphicsItem(version);
}

//  QStyleOptionGraphicsItem::~QStyleOptionGraphicsItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QStyleOptionGraphicsItemD1Ev(
    QStyleOptionGraphicsItem *self) {
  delete self;
}
