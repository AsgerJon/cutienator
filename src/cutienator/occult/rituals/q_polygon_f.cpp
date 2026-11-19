//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qpolygon.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qpolygon.h>
#include <QtCore/qrect.h>
#include <QtCore/qvariant.h>
#include <QtCore/qpoint.h>

//  QPolygonF::QPolygonF()
extern "C" Q_DECL_EXPORT
QPolygonF *ritual_ZN9QPolygonFC1Ev() {
  return new QPolygonF();
}

//  QPolygonF::QPolygonF(const QRectF &r)
extern "C" Q_DECL_EXPORT
QPolygonF *ritual_ZN9QPolygonFC1ERK6QRectF(const QRectF *r) {
  return new QPolygonF(*r);
}

//  QPolygonF::QPolygonF(const QPolygon &a)
extern "C" Q_DECL_EXPORT
QPolygonF *ritual_ZN9QPolygonFC1ERK8QPolygon(const QPolygon *a) {
  return new QPolygonF(*a);
}

//  QVariant QPolygonF::operator QVariant() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK9QPolygonFcv8QVariantEv(const QPolygonF *self) {
  return new QVariant(self->operator QVariant());
}

//  void QPolygonF::translate(qreal dx, qreal dy)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QPolygonF9translateEdd(QPolygonF *self, qreal dx, qreal dy) {
  self->translate(dx, dy);
}

//  void QPolygonF::translate(const QPointF &offset)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QPolygonF9translateERK7QPointF(
    QPolygonF *self,
    const QPointF *offset) {
  self->translate(*offset);
}

//  QPolygonF QPolygonF::translated(qreal dx, qreal dy) const
extern "C" Q_DECL_EXPORT
QPolygonF *ritual_ZNK9QPolygonF10translatedEdd(
    const QPolygonF *self,
    qreal dx,
    qreal dy) {
  return new QPolygonF(self->translated(dx, dy));
}

//  QPolygonF QPolygonF::translated(const QPointF &offset) const
extern "C" Q_DECL_EXPORT
QPolygonF *ritual_ZNK9QPolygonF10translatedERK7QPointF(
    const QPolygonF *self,
    const QPointF *offset) {
  return new QPolygonF(self->translated(*offset));
}

//  QPolygon QPolygonF::toPolygon() const
extern "C" Q_DECL_EXPORT
QPolygon *ritual_ZNK9QPolygonF9toPolygonEv(const QPolygonF *self) {
  return new QPolygon(self->toPolygon());
}

//  bool QPolygonF::isClosed() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QPolygonF8isClosedEv(const QPolygonF *self) {
  return self->isClosed();
}

//  QRectF QPolygonF::boundingRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK9QPolygonF12boundingRectEv(const QPolygonF *self) {
  return new QRectF(self->boundingRect());
}

//  bool QPolygonF::containsPoint(const QPointF &pt, Qt::FillRule fillRule)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QPolygonF13containsPointERK7QPointFN2Qt8FillRuleE(
    const QPolygonF *self,
    const QPointF *pt,
    Qt::FillRule fillRule) {
  return self->containsPoint(*pt, fillRule);
}

//  QPolygonF QPolygonF::united(const QPolygonF &r) const
extern "C" Q_DECL_EXPORT
QPolygonF *ritual_ZNK9QPolygonF6unitedERKS_(
    const QPolygonF *self,
    const QPolygonF *r) {
  return new QPolygonF(self->united(*r));
}

//  QPolygonF QPolygonF::intersected(const QPolygonF &r) const
extern "C" Q_DECL_EXPORT
QPolygonF *ritual_ZNK9QPolygonF11intersectedERKS_(
    const QPolygonF *self,
    const QPolygonF *r) {
  return new QPolygonF(self->intersected(*r));
}

//  QPolygonF QPolygonF::subtracted(const QPolygonF &r) const
extern "C" Q_DECL_EXPORT
QPolygonF *ritual_ZNK9QPolygonF10subtractedERKS_(
    const QPolygonF *self,
    const QPolygonF *r) {
  return new QPolygonF(self->subtracted(*r));
}

//  bool QPolygonF::intersects(const QPolygonF &r) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QPolygonF10intersectsERKS_(
    const QPolygonF *self,
    const QPolygonF *r) {
  return self->intersects(*r);
}

//  QPolygonF::~QPolygonF()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QPolygonFD1Ev(QPolygonF *self) {
  delete self;
}
