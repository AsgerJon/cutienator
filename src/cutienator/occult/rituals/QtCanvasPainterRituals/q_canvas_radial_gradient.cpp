//  Written by dev_tooling.RitualGenerator from the records of
//  QtCanvasPainter/qcanvasradialgradient.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtCanvasPainter/qcanvasradialgradient.h>
#include <QtCore/qpoint.h>
#include <QtCanvasPainter/qcanvasbrush.h>

//  QCanvasRadialGradient::QCanvasRadialGradient()
extern "C" Q_DECL_EXPORT
QCanvasRadialGradient *ritual_ZN21QCanvasRadialGradientC1Ev() {
  return new QCanvasRadialGradient();
}

//  QCanvasRadialGradient::QCanvasRadialGradient(qreal centerX, qreal
//      centerY, qreal innerRadius, qreal outerRadius)
extern "C" Q_DECL_EXPORT
QCanvasRadialGradient *ritual_ZN21QCanvasRadialGradientC1Edddd(
    qreal centerX,
    qreal centerY,
    qreal innerRadius,
    qreal outerRadius) {
  return new QCanvasRadialGradient(
      centerX,
      centerY,
      innerRadius,
      outerRadius);
}

//  QCanvasRadialGradient::QCanvasRadialGradient(QPointF centerPosition,
//      qreal innerRadius, qreal outerRadius)
extern "C" Q_DECL_EXPORT
QCanvasRadialGradient *ritual_ZN21QCanvasRadialGradientC1E7QPointFdd(
    const QPointF *centerPosition,
    qreal innerRadius,
    qreal outerRadius) {
  return new QCanvasRadialGradient(
      *centerPosition,
      innerRadius,
      outerRadius);
}

//  QCanvasRadialGradient::QCanvasRadialGradient(qreal innerCenterX, qreal
//      innerCenterY, qreal innerRadius, qreal outerCenterX, qreal
//      outerCenterY, qreal outerRadius)
extern "C" Q_DECL_EXPORT
QCanvasRadialGradient *ritual_ZN21QCanvasRadialGradientC1Edddddd(
    qreal innerCenterX,
    qreal innerCenterY,
    qreal innerRadius,
    qreal outerCenterX,
    qreal outerCenterY,
    qreal outerRadius) {
  return new QCanvasRadialGradient(
      innerCenterX,
      innerCenterY,
      innerRadius,
      outerCenterX,
      outerCenterY,
      outerRadius);
}

//  QCanvasRadialGradient::QCanvasRadialGradient(QPointF innerCenterPosition,
//      qreal innerRadius, QPointF outerCenterPosition, qreal outerRadius)
extern "C" Q_DECL_EXPORT
QCanvasRadialGradient *ritual_ZN21QCanvasRadialGradientC1E7QPointFdS0_d(
    const QPointF *innerCenterPosition,
    qreal innerRadius,
    const QPointF *outerCenterPosition,
    qreal outerRadius) {
  return new QCanvasRadialGradient(
      *innerCenterPosition,
      innerRadius,
      *outerCenterPosition,
      outerRadius);
}

//  QCanvasRadialGradient::QCanvasRadialGradient(const QCanvasRadialGradient
//      &a0)
extern "C" Q_DECL_EXPORT
QCanvasRadialGradient *ritual_ZN21QCanvasRadialGradientC1ERKS_(
    const QCanvasRadialGradient *a0) {
  return new QCanvasRadialGradient(*a0);
}

//  QCanvasRadialGradient::~QCanvasRadialGradient()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QCanvasRadialGradientD1Ev(QCanvasRadialGradient *self) {
  delete self;
}

//  QPointF QCanvasRadialGradient::centerPosition() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK21QCanvasRadialGradient14centerPositionEv(
    const QCanvasRadialGradient *self) {
  return new QPointF(self->centerPosition());
}

//  void QCanvasRadialGradient::setCenterPosition(qreal x, qreal y)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QCanvasRadialGradient17setCenterPositionEdd(
    QCanvasRadialGradient *self,
    qreal x,
    qreal y) {
  self->setCenterPosition(x, y);
}

//  void QCanvasRadialGradient::setCenterPosition(QPointF center)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QCanvasRadialGradient17setCenterPositionE7QPointF(
    QCanvasRadialGradient *self,
    const QPointF *center) {
  self->setCenterPosition(*center);
}

//  QPointF QCanvasRadialGradient::innerCenterPosition() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK21QCanvasRadialGradient19innerCenterPositionEv(
    const QCanvasRadialGradient *self) {
  return new QPointF(self->innerCenterPosition());
}

//  void QCanvasRadialGradient::setInnerCenterPosition(qreal x, qreal y)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QCanvasRadialGradient22setInnerCenterPositionEdd(
    QCanvasRadialGradient *self,
    qreal x,
    qreal y) {
  self->setInnerCenterPosition(x, y);
}

//  void QCanvasRadialGradient::setInnerCenterPosition(QPointF center)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QCanvasRadialGradient22setInnerCenterPositionE7QPointF(
    QCanvasRadialGradient *self,
    const QPointF *center) {
  self->setInnerCenterPosition(*center);
}

//  QPointF QCanvasRadialGradient::outerCenterPosition() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK21QCanvasRadialGradient19outerCenterPositionEv(
    const QCanvasRadialGradient *self) {
  return new QPointF(self->outerCenterPosition());
}

//  void QCanvasRadialGradient::setOuterCenterPosition(qreal x, qreal y)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QCanvasRadialGradient22setOuterCenterPositionEdd(
    QCanvasRadialGradient *self,
    qreal x,
    qreal y) {
  self->setOuterCenterPosition(x, y);
}

//  void QCanvasRadialGradient::setOuterCenterPosition(QPointF center)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QCanvasRadialGradient22setOuterCenterPositionE7QPointF(
    QCanvasRadialGradient *self,
    const QPointF *center) {
  self->setOuterCenterPosition(*center);
}

//  qreal QCanvasRadialGradient::outerRadius() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK21QCanvasRadialGradient11outerRadiusEv(
    const QCanvasRadialGradient *self) {
  return self->outerRadius();
}

//  void QCanvasRadialGradient::setOuterRadius(qreal radius)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QCanvasRadialGradient14setOuterRadiusEd(
    QCanvasRadialGradient *self,
    qreal radius) {
  self->setOuterRadius(radius);
}

//  qreal QCanvasRadialGradient::innerRadius() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK21QCanvasRadialGradient11innerRadiusEv(
    const QCanvasRadialGradient *self) {
  return self->innerRadius();
}

//  void QCanvasRadialGradient::setInnerRadius(qreal radius)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QCanvasRadialGradient14setInnerRadiusEd(
    QCanvasRadialGradient *self,
    qreal radius) {
  self->setInnerRadius(radius);
}

//  QCanvasRadialGradient::QCanvasRadialGradient(const QCanvasBrush &brush)
extern "C" Q_DECL_EXPORT
QCanvasRadialGradient *ritual_ZN21QCanvasRadialGradientC1ERK12QCanvasBrush(
    const QCanvasBrush *brush) {
  return new QCanvasRadialGradient(*brush);
}
