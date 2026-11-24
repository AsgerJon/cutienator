//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qfixed_p.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qfixed_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qpoint.h>

//  QFixedPoint::QFixedPoint()
extern "C" Q_DECL_EXPORT
QFixedPoint *ritual_ZN11QFixedPointC1Ev() {
  return new QFixedPoint();
}

//  QFixedPoint::QFixedPoint(QFixed _x, QFixed _y)
extern "C" Q_DECL_EXPORT
QFixedPoint *ritual_ZN11QFixedPointC1E6QFixedS0_(
    const QFixed *_x,
    const QFixed *_y) {
  return new QFixedPoint(*_x, *_y);
}

//  QPointF QFixedPoint::toPointF() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK11QFixedPoint8toPointFEv(const QFixedPoint *self) {
  return new QPointF(self->toPointF());
}

//  QFixedPoint QFixedPoint::fromPointF(const QPointF &p)
extern "C" Q_DECL_EXPORT
QFixedPoint *ritual_ZN11QFixedPoint10fromPointFERK7QPointF(
    const QPointF *p) {
  return new QFixedPoint(QFixedPoint::fromPointF(*p));
}

//  bool QFixedPoint::operator==(const QFixedPoint &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QFixedPointeqERKS_(
    const QFixedPoint *self,
    const QFixedPoint *other) {
  return self->operator==(*other);
}

//  QFixedPoint::~QFixedPoint()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFixedPointD1Ev(QFixedPoint *self) {
  delete self;
}
