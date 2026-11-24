//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/qsgsimplerectnode.h, Qt 6.12.0. Changes made here are lost.
#include <QtQuick/QtQuick>
#include <QtQuick/qsgsimplerectnode.h>
#include <QtCore/qrect.h>
#include <QtGui/qcolor.h>

//  QSGSimpleRectNode::QSGSimpleRectNode(const QRectF &rect, const QColor
//      &color)
extern "C" Q_DECL_EXPORT
QSGSimpleRectNode *ritual_ZN17QSGSimpleRectNodeC1ERK6QRectFRK6QColor(
    const QRectF *rect,
    const QColor *color) {
  return new QSGSimpleRectNode(*rect, *color);
}

//  QSGSimpleRectNode::QSGSimpleRectNode()
extern "C" Q_DECL_EXPORT
QSGSimpleRectNode *ritual_ZN17QSGSimpleRectNodeC1Ev() {
  return new QSGSimpleRectNode();
}

//  void QSGSimpleRectNode::setRect(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSGSimpleRectNode7setRectERK6QRectF(
    QSGSimpleRectNode *self,
    const QRectF *rect) {
  self->setRect(*rect);
}

//  void QSGSimpleRectNode::setRect(qreal x, qreal y, qreal w, qreal h)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSGSimpleRectNode7setRectEdddd(
    QSGSimpleRectNode *self,
    qreal x,
    qreal y,
    qreal w,
    qreal h) {
  self->setRect(x, y, w, h);
}

//  QRectF QSGSimpleRectNode::rect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK17QSGSimpleRectNode4rectEv(const QSGSimpleRectNode *self) {
  return new QRectF(self->rect());
}

//  void QSGSimpleRectNode::setColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSGSimpleRectNode8setColorERK6QColor(
    QSGSimpleRectNode *self,
    const QColor *color) {
  self->setColor(*color);
}

//  QColor QSGSimpleRectNode::color() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK17QSGSimpleRectNode5colorEv(
    const QSGSimpleRectNode *self) {
  return new QColor(self->color());
}
