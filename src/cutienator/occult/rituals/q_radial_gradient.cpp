//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qbrush.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qbrush.h>
#include <QtCore/qpoint.h>

//  QRadialGradient::QRadialGradient()
extern "C" Q_DECL_EXPORT
QRadialGradient *ritual_ZN15QRadialGradientC1Ev() {
  return new QRadialGradient();
}

//  QRadialGradient::QRadialGradient(const QPointF &center, qreal radius,
//      const QPointF &focalPoint)
extern "C" Q_DECL_EXPORT
QRadialGradient *ritual_ZN15QRadialGradientC1ERK7QPointFdS2_(
    const QPointF *center,
    qreal radius,
    const QPointF *focalPoint) {
  return new QRadialGradient(*center, radius, *focalPoint);
}

//  QRadialGradient::QRadialGradient(qreal cx, qreal cy, qreal radius, qreal
//      fx, qreal fy)
extern "C" Q_DECL_EXPORT
QRadialGradient *ritual_ZN15QRadialGradientC1Eddddd(
    qreal cx,
    qreal cy,
    qreal radius,
    qreal fx,
    qreal fy) {
  return new QRadialGradient(cx, cy, radius, fx, fy);
}

//  QRadialGradient::QRadialGradient(const QPointF &center, qreal radius)
extern "C" Q_DECL_EXPORT
QRadialGradient *ritual_ZN15QRadialGradientC1ERK7QPointFd(
    const QPointF *center,
    qreal radius) {
  return new QRadialGradient(*center, radius);
}

//  QRadialGradient::QRadialGradient(qreal cx, qreal cy, qreal radius)
extern "C" Q_DECL_EXPORT
QRadialGradient *ritual_ZN15QRadialGradientC1Eddd(
    qreal cx,
    qreal cy,
    qreal radius) {
  return new QRadialGradient(cx, cy, radius);
}

//  QRadialGradient::QRadialGradient(const QPointF &center, qreal
//      centerRadius, const QPointF &focalPoint, qreal focalRadius)
extern "C" Q_DECL_EXPORT
QRadialGradient *ritual_ZN15QRadialGradientC1ERK7QPointFdS2_d(
    const QPointF *center,
    qreal centerRadius,
    const QPointF *focalPoint,
    qreal focalRadius) {
  return new QRadialGradient(
      *center,
      centerRadius,
      *focalPoint,
      focalRadius);
}

//  QRadialGradient::QRadialGradient(qreal cx, qreal cy, qreal centerRadius,
//      qreal fx, qreal fy, qreal focalRadius)
extern "C" Q_DECL_EXPORT
QRadialGradient *ritual_ZN15QRadialGradientC1Edddddd(
    qreal cx,
    qreal cy,
    qreal centerRadius,
    qreal fx,
    qreal fy,
    qreal focalRadius) {
  return new QRadialGradient(cx, cy, centerRadius, fx, fy, focalRadius);
}

//  QRadialGradient::~QRadialGradient()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QRadialGradientD1Ev(QRadialGradient *self) {
  delete self;
}

//  QPointF QRadialGradient::center() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK15QRadialGradient6centerEv(const QRadialGradient *self) {
  return new QPointF(self->center());
}

//  void QRadialGradient::setCenter(const QPointF &center)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QRadialGradient9setCenterERK7QPointF(
    QRadialGradient *self,
    const QPointF *center) {
  self->setCenter(*center);
}

//  void QRadialGradient::setCenter(qreal x, qreal y)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QRadialGradient9setCenterEdd(
    QRadialGradient *self,
    qreal x,
    qreal y) {
  self->setCenter(x, y);
}

//  QPointF QRadialGradient::focalPoint() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK15QRadialGradient10focalPointEv(
    const QRadialGradient *self) {
  return new QPointF(self->focalPoint());
}

//  void QRadialGradient::setFocalPoint(const QPointF &focalPoint)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QRadialGradient13setFocalPointERK7QPointF(
    QRadialGradient *self,
    const QPointF *focalPoint) {
  self->setFocalPoint(*focalPoint);
}

//  void QRadialGradient::setFocalPoint(qreal x, qreal y)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QRadialGradient13setFocalPointEdd(
    QRadialGradient *self,
    qreal x,
    qreal y) {
  self->setFocalPoint(x, y);
}

//  qreal QRadialGradient::radius() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QRadialGradient6radiusEv(const QRadialGradient *self) {
  return self->radius();
}

//  void QRadialGradient::setRadius(qreal radius)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QRadialGradient9setRadiusEd(
    QRadialGradient *self,
    qreal radius) {
  self->setRadius(radius);
}

//  qreal QRadialGradient::centerRadius() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QRadialGradient12centerRadiusEv(
    const QRadialGradient *self) {
  return self->centerRadius();
}

//  void QRadialGradient::setCenterRadius(qreal radius)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QRadialGradient15setCenterRadiusEd(
    QRadialGradient *self,
    qreal radius) {
  self->setCenterRadius(radius);
}

//  qreal QRadialGradient::focalRadius() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QRadialGradient11focalRadiusEv(
    const QRadialGradient *self) {
  return self->focalRadius();
}

//  void QRadialGradient::setFocalRadius(qreal radius)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QRadialGradient14setFocalRadiusEd(
    QRadialGradient *self,
    qreal radius) {
  self->setFocalRadius(radius);
}
