//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qtransform.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtransform.h>
#include <QtCore/qvariant.h>
#include <QtCore/qpoint.h>
#include <QtCore/qline.h>
#include <QtGui/qpolygon.h>
#include <QtGui/qregion.h>
#include <QtGui/qpainterpath.h>
#include <QtCore/qrect.h>

//  QTransform::QTransform(Qt::Initialization a0)
extern "C" Q_DECL_EXPORT
QTransform *ritual_ZN10QTransformC1EN2Qt14InitializationE(
    Qt::Initialization a0) {
  return new QTransform(a0);
}

//  QTransform::QTransform()
extern "C" Q_DECL_EXPORT
QTransform *ritual_ZN10QTransformC1Ev() {
  return new QTransform();
}

//  QTransform::QTransform(qreal h11, qreal h12, qreal h13, qreal h21, qreal
//      h22, qreal h23, qreal h31, qreal h32, qreal h33)
extern "C" Q_DECL_EXPORT
QTransform *ritual_ZN10QTransformC1Eddddddddd(
    qreal h11,
    qreal h12,
    qreal h13,
    qreal h21,
    qreal h22,
    qreal h23,
    qreal h31,
    qreal h32,
    qreal h33) {
  return new QTransform(h11, h12, h13, h21, h22, h23, h31, h32, h33);
}

//  QTransform::QTransform(qreal h11, qreal h12, qreal h21, qreal h22, qreal
//      dx, qreal dy)
extern "C" Q_DECL_EXPORT
QTransform *ritual_ZN10QTransformC1Edddddd(
    qreal h11,
    qreal h12,
    qreal h21,
    qreal h22,
    qreal dx,
    qreal dy) {
  return new QTransform(h11, h12, h21, h22, dx, dy);
}

//  QTransform::QTransform(const QTransform &other)
extern "C" Q_DECL_EXPORT
QTransform *ritual_ZN10QTransformC1ERKS_(const QTransform *other) {
  return new QTransform(*other);
}

//  bool QTransform::isAffine() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QTransform8isAffineEv(const QTransform *self) {
  return self->isAffine();
}

//  bool QTransform::isIdentity() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QTransform10isIdentityEv(const QTransform *self) {
  return self->isIdentity();
}

//  bool QTransform::isInvertible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QTransform12isInvertibleEv(const QTransform *self) {
  return self->isInvertible();
}

//  bool QTransform::isScaling() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QTransform9isScalingEv(const QTransform *self) {
  return self->isScaling();
}

//  bool QTransform::isRotating() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QTransform10isRotatingEv(const QTransform *self) {
  return self->isRotating();
}

//  bool QTransform::isTranslating() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QTransform13isTranslatingEv(const QTransform *self) {
  return self->isTranslating();
}

//  TransformationType QTransform::type() const
extern "C" Q_DECL_EXPORT
QTransform::TransformationType ritual_ZNK10QTransform4typeEv(
    const QTransform *self) {
  return self->type();
}

//  qreal QTransform::determinant() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK10QTransform11determinantEv(const QTransform *self) {
  return self->determinant();
}

//  qreal QTransform::m11() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK10QTransform3m11Ev(const QTransform *self) {
  return self->m11();
}

//  qreal QTransform::m12() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK10QTransform3m12Ev(const QTransform *self) {
  return self->m12();
}

//  qreal QTransform::m13() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK10QTransform3m13Ev(const QTransform *self) {
  return self->m13();
}

//  qreal QTransform::m21() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK10QTransform3m21Ev(const QTransform *self) {
  return self->m21();
}

//  qreal QTransform::m22() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK10QTransform3m22Ev(const QTransform *self) {
  return self->m22();
}

//  qreal QTransform::m23() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK10QTransform3m23Ev(const QTransform *self) {
  return self->m23();
}

//  qreal QTransform::m31() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK10QTransform3m31Ev(const QTransform *self) {
  return self->m31();
}

//  qreal QTransform::m32() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK10QTransform3m32Ev(const QTransform *self) {
  return self->m32();
}

//  qreal QTransform::m33() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK10QTransform3m33Ev(const QTransform *self) {
  return self->m33();
}

//  qreal QTransform::dx() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK10QTransform2dxEv(const QTransform *self) {
  return self->dx();
}

//  qreal QTransform::dy() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK10QTransform2dyEv(const QTransform *self) {
  return self->dy();
}

//  void QTransform::setMatrix(qreal m11, qreal m12, qreal m13, qreal m21,
//      qreal m22, qreal m23, qreal m31, qreal m32, qreal m33)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTransform9setMatrixEddddddddd(
    QTransform *self,
    qreal m11,
    qreal m12,
    qreal m13,
    qreal m21,
    qreal m22,
    qreal m23,
    qreal m31,
    qreal m32,
    qreal m33) {
  self->setMatrix(m11, m12, m13, m21, m22, m23, m31, m32, m33);
}

//  QTransform QTransform::inverted(bool *invertible) const
extern "C" Q_DECL_EXPORT
QTransform *ritual_ZNK10QTransform8invertedEPb(
    const QTransform *self,
    bool *invertible) {
  return new QTransform(self->inverted(invertible));
}

//  QTransform QTransform::adjoint() const
extern "C" Q_DECL_EXPORT
QTransform *ritual_ZNK10QTransform7adjointEv(const QTransform *self) {
  return new QTransform(self->adjoint());
}

//  QTransform QTransform::transposed() const
extern "C" Q_DECL_EXPORT
QTransform *ritual_ZNK10QTransform10transposedEv(const QTransform *self) {
  return new QTransform(self->transposed());
}

//  bool QTransform::operator==(const QTransform &a0) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QTransformeqERKS_(
    const QTransform *self,
    const QTransform *a0) {
  return self->operator==(*a0);
}

//  bool QTransform::operator!=(const QTransform &a0) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QTransformneERKS_(
    const QTransform *self,
    const QTransform *a0) {
  return self->operator!=(*a0);
}

//  QTransform QTransform::operator*(const QTransform &o) const
extern "C" Q_DECL_EXPORT
QTransform *ritual_ZNK10QTransformmlERKS_(
    const QTransform *self,
    const QTransform *o) {
  return new QTransform(self->operator*(*o));
}

//  QVariant QTransform::operator QVariant() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK10QTransformcv8QVariantEv(const QTransform *self) {
  return new QVariant(self->operator QVariant());
}

//  void QTransform::reset()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTransform5resetEv(QTransform *self) {
  self->reset();
}

//  QPoint QTransform::map(const QPoint &p) const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK10QTransform3mapERK6QPoint(
    const QTransform *self,
    const QPoint *p) {
  return new QPoint(self->map(*p));
}

//  QPointF QTransform::map(const QPointF &p) const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK10QTransform3mapERK7QPointF(
    const QTransform *self,
    const QPointF *p) {
  return new QPointF(self->map(*p));
}

//  QLine QTransform::map(const QLine &l) const
extern "C" Q_DECL_EXPORT
QLine *ritual_ZNK10QTransform3mapERK5QLine(
    const QTransform *self,
    const QLine *l) {
  return new QLine(self->map(*l));
}

//  QLineF QTransform::map(const QLineF &l) const
extern "C" Q_DECL_EXPORT
QLineF *ritual_ZNK10QTransform3mapERK6QLineF(
    const QTransform *self,
    const QLineF *l) {
  return new QLineF(self->map(*l));
}

//  QPolygonF QTransform::map(const QPolygonF &a) const
extern "C" Q_DECL_EXPORT
QPolygonF *ritual_ZNK10QTransform3mapERK9QPolygonF(
    const QTransform *self,
    const QPolygonF *a) {
  return new QPolygonF(self->map(*a));
}

//  QPolygon QTransform::map(const QPolygon &a) const
extern "C" Q_DECL_EXPORT
QPolygon *ritual_ZNK10QTransform3mapERK8QPolygon(
    const QTransform *self,
    const QPolygon *a) {
  return new QPolygon(self->map(*a));
}

//  QRegion QTransform::map(const QRegion &r) const
extern "C" Q_DECL_EXPORT
QRegion *ritual_ZNK10QTransform3mapERK7QRegion(
    const QTransform *self,
    const QRegion *r) {
  return new QRegion(self->map(*r));
}

//  QPainterPath QTransform::map(const QPainterPath &p) const
extern "C" Q_DECL_EXPORT
QPainterPath *ritual_ZNK10QTransform3mapERK12QPainterPath(
    const QTransform *self,
    const QPainterPath *p) {
  return new QPainterPath(self->map(*p));
}

//  QPolygon QTransform::mapToPolygon(const QRect &r) const
extern "C" Q_DECL_EXPORT
QPolygon *ritual_ZNK10QTransform12mapToPolygonERK5QRect(
    const QTransform *self,
    const QRect *r) {
  return new QPolygon(self->mapToPolygon(*r));
}

//  QRect QTransform::mapRect(const QRect &a0) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK10QTransform7mapRectERK5QRect(
    const QTransform *self,
    const QRect *a0) {
  return new QRect(self->mapRect(*a0));
}

//  QRectF QTransform::mapRect(const QRectF &a0) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK10QTransform7mapRectERK6QRectF(
    const QTransform *self,
    const QRectF *a0) {
  return new QRectF(self->mapRect(*a0));
}

//  void QTransform::map(int x, int y, int *tx, int *ty) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK10QTransform3mapEiiPiS0_(
    const QTransform *self,
    int x,
    int y,
    int *tx,
    int *ty) {
  self->map(x, y, tx, ty);
}

//  void QTransform::map(qreal x, qreal y, qreal *tx, qreal *ty) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK10QTransform3mapEddPdS0_(
    const QTransform *self,
    qreal x,
    qreal y,
    qreal *tx,
    qreal *ty) {
  self->map(x, y, tx, ty);
}

//  QTransform QTransform::fromTranslate(qreal dx, qreal dy)
extern "C" Q_DECL_EXPORT
QTransform *ritual_ZN10QTransform13fromTranslateEdd(qreal dx, qreal dy) {
  return new QTransform(QTransform::fromTranslate(dx, dy));
}

//  QTransform QTransform::fromScale(qreal dx, qreal dy)
extern "C" Q_DECL_EXPORT
QTransform *ritual_ZN10QTransform9fromScaleEdd(qreal dx, qreal dy) {
  return new QTransform(QTransform::fromScale(dx, dy));
}

//  QTransform::~QTransform()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTransformD1Ev(QTransform *self) {
  delete self;
}
