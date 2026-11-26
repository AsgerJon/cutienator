//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qpolygon.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qpolygon.h>
#include <QtCore/qpoint.h>
#include <QtCore/qrect.h>
#include <QtCore/qvariant.h>
#include <QtCore/qlist.h>

//  QPolygonF::QPolygonF()
extern "C" Q_DECL_EXPORT
QPolygonF *ritual_ZN9QPolygonFC1Ev() {
  return new QPolygonF();
}

//  QPolygonF::QPolygonF(const QList<QPointF> &v)
extern "C" Q_DECL_EXPORT
QPolygonF *ritual_ZN9QPolygonFC1ERK5QListI7QPointFE(
    const QList<QPointF> *v) {
  return new QPolygonF(*v);
}

//  QPolygonF::QPolygonF(QList<QPointF> &&v)
extern "C" Q_DECL_EXPORT
QPolygonF *ritual_ZN9QPolygonFC1EO5QListI7QPointFE(QList<QPointF> *v) {
  return new QPolygonF(std::move(*v));
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

//  void QPolygonF::swap(QPolygonF &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QPolygonF4swapERS_(QPolygonF *self, QPolygonF *other) {
  self->swap(*other);
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

//  QList<QPolygonF>::QList()
extern "C" Q_DECL_EXPORT
QList<QPolygonF> *ritual_list_make_QPolygonF() {
  return new QList<QPolygonF>();
}

//  void QList<QPolygonF>::append(const QPolygonF &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QPolygonF(
    QList<QPolygonF> *self,
    const QPolygonF *element) {
  self->append(*element);
}

//  qsizetype QList<QPolygonF>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QPolygonF(const QList<QPolygonF> *self) {
  return self->size();
}

//  const QPolygonF &QList<QPolygonF>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QPolygonF *ritual_list_at_QPolygonF(
    const QList<QPolygonF> *self,
    long long index) {
  return new QPolygonF(self->at(index));
}

//  QList<QPolygonF>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QPolygonF(QList<QPolygonF> *self) {
  delete self;
}
