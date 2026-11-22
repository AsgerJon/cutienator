//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qpolygon.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qpolygon.h>
#include <QtCore/qpoint.h>
#include <QtCore/qrect.h>
#include <QtCore/qvariant.h>
#include <QtCore/qlist.h>

//  QPolygon::QPolygon()
extern "C" Q_DECL_EXPORT
QPolygon *ritual_ZN8QPolygonC1Ev() {
  return new QPolygon();
}

//  QPolygon::QPolygon(const QList<QPoint> &v)
extern "C" Q_DECL_EXPORT
QPolygon *ritual_ZN8QPolygonC1ERK5QListI6QPointE(const QList<QPoint> *v) {
  return new QPolygon(*v);
}

//  QPolygon::QPolygon(const QRect &r, bool closed)
extern "C" Q_DECL_EXPORT
QPolygon *ritual_ZN8QPolygonC1ERK5QRectb(const QRect *r, bool closed) {
  return new QPolygon(*r, closed);
}

//  QVariant QPolygon::operator QVariant() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK8QPolygoncv8QVariantEv(const QPolygon *self) {
  return new QVariant(self->operator QVariant());
}

//  void QPolygon::translate(int dx, int dy)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPolygon9translateEii(QPolygon *self, int dx, int dy) {
  self->translate(dx, dy);
}

//  void QPolygon::translate(const QPoint &offset)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPolygon9translateERK6QPoint(
    QPolygon *self,
    const QPoint *offset) {
  self->translate(*offset);
}

//  QPolygon QPolygon::translated(int dx, int dy) const
extern "C" Q_DECL_EXPORT
QPolygon *ritual_ZNK8QPolygon10translatedEii(
    const QPolygon *self,
    int dx,
    int dy) {
  return new QPolygon(self->translated(dx, dy));
}

//  QPolygon QPolygon::translated(const QPoint &offset) const
extern "C" Q_DECL_EXPORT
QPolygon *ritual_ZNK8QPolygon10translatedERK6QPoint(
    const QPolygon *self,
    const QPoint *offset) {
  return new QPolygon(self->translated(*offset));
}

//  QRect QPolygon::boundingRect() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK8QPolygon12boundingRectEv(const QPolygon *self) {
  return new QRect(self->boundingRect());
}

//  void QPolygon::point(int i, int *x, int *y) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK8QPolygon5pointEiPiS0_(
    const QPolygon *self,
    int i,
    int *x,
    int *y) {
  self->point(i, x, y);
}

//  QPoint QPolygon::point(int i) const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK8QPolygon5pointEi(const QPolygon *self, int i) {
  return new QPoint(self->point(i));
}

//  void QPolygon::setPoint(int index, int x, int y)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPolygon8setPointEiii(
    QPolygon *self,
    int index,
    int x,
    int y) {
  self->setPoint(index, x, y);
}

//  void QPolygon::setPoint(int index, const QPoint &p)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPolygon8setPointEiRK6QPoint(
    QPolygon *self,
    int index,
    const QPoint *p) {
  self->setPoint(index, *p);
}

//  void QPolygon::putPoints(int index, int nPoints, const QPolygon &from,
//      int fromIndex)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPolygon9putPointsEiiRKS_i(
    QPolygon *self,
    int index,
    int nPoints,
    const QPolygon *from,
    int fromIndex) {
  self->putPoints(index, nPoints, *from, fromIndex);
}

//  bool QPolygon::containsPoint(const QPoint &pt, Qt::FillRule fillRule)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QPolygon13containsPointERK6QPointN2Qt8FillRuleE(
    const QPolygon *self,
    const QPoint *pt,
    Qt::FillRule fillRule) {
  return self->containsPoint(*pt, fillRule);
}

//  QPolygon QPolygon::united(const QPolygon &r) const
extern "C" Q_DECL_EXPORT
QPolygon *ritual_ZNK8QPolygon6unitedERKS_(
    const QPolygon *self,
    const QPolygon *r) {
  return new QPolygon(self->united(*r));
}

//  QPolygon QPolygon::intersected(const QPolygon &r) const
extern "C" Q_DECL_EXPORT
QPolygon *ritual_ZNK8QPolygon11intersectedERKS_(
    const QPolygon *self,
    const QPolygon *r) {
  return new QPolygon(self->intersected(*r));
}

//  QPolygon QPolygon::subtracted(const QPolygon &r) const
extern "C" Q_DECL_EXPORT
QPolygon *ritual_ZNK8QPolygon10subtractedERKS_(
    const QPolygon *self,
    const QPolygon *r) {
  return new QPolygon(self->subtracted(*r));
}

//  bool QPolygon::intersects(const QPolygon &r) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QPolygon10intersectsERKS_(
    const QPolygon *self,
    const QPolygon *r) {
  return self->intersects(*r);
}

//  QPolygonF QPolygon::toPolygonF() const
extern "C" Q_DECL_EXPORT
QPolygonF *ritual_ZNK8QPolygon10toPolygonFEv(const QPolygon *self) {
  return new QPolygonF(self->toPolygonF());
}

//  QPolygon::~QPolygon()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QPolygonD1Ev(QPolygon *self) {
  delete self;
}
