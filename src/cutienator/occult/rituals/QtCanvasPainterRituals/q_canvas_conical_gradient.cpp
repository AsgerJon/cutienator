//  Written by dev_tooling.RitualGenerator from the records of
//  QtCanvasPainter/qcanvasconicalgradient.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtCanvasPainter/qcanvasconicalgradient.h>
#include <QtCore/qpoint.h>
#include <QtCanvasPainter/qcanvasbrush.h>

//  QCanvasConicalGradient::QCanvasConicalGradient()
extern "C" Q_DECL_EXPORT
QCanvasConicalGradient *ritual_ZN22QCanvasConicalGradientC1Ev() {
  return new QCanvasConicalGradient();
}

//  QCanvasConicalGradient::QCanvasConicalGradient(qreal centerX, qreal
//      centerY, qreal startAngle)
extern "C" Q_DECL_EXPORT
QCanvasConicalGradient *ritual_ZN22QCanvasConicalGradientC1Eddd(
    qreal centerX,
    qreal centerY,
    qreal startAngle) {
  return new QCanvasConicalGradient(centerX, centerY, startAngle);
}

//  QCanvasConicalGradient::QCanvasConicalGradient(QPointF center, qreal
//      startAngle)
extern "C" Q_DECL_EXPORT
QCanvasConicalGradient *ritual_ZN22QCanvasConicalGradientC1E7QPointFd(
    const QPointF *center,
    qreal startAngle) {
  return new QCanvasConicalGradient(*center, startAngle);
}

//  QCanvasConicalGradient::QCanvasConicalGradient(const
//      QCanvasConicalGradient &a0)
extern "C" Q_DECL_EXPORT
QCanvasConicalGradient *ritual_ZN22QCanvasConicalGradientC1ERKS_(
    const QCanvasConicalGradient *a0) {
  return new QCanvasConicalGradient(*a0);
}

//  QCanvasConicalGradient &QCanvasConicalGradient::operator=(const
//      QCanvasConicalGradient &a0)
extern "C" Q_DECL_EXPORT
QCanvasConicalGradient *ritual_ZN22QCanvasConicalGradientaSERKS_(
    QCanvasConicalGradient *self,
    const QCanvasConicalGradient *a0) {
  return &(self->operator=(*a0));
}

//  QCanvasConicalGradient::QCanvasConicalGradient(QCanvasConicalGradient
//      &&a0)
extern "C" Q_DECL_EXPORT
QCanvasConicalGradient *ritual_ZN22QCanvasConicalGradientC1EOS_(
    QCanvasConicalGradient *a0) {
  return new QCanvasConicalGradient(std::move(*a0));
}

//  QCanvasConicalGradient
//      &QCanvasConicalGradient::operator=(QCanvasConicalGradient &&a0)
extern "C" Q_DECL_EXPORT
QCanvasConicalGradient *ritual_ZN22QCanvasConicalGradientaSEOS_(
    QCanvasConicalGradient *self,
    QCanvasConicalGradient *a0) {
  return &(self->operator=(std::move(*a0)));
}

//  QCanvasConicalGradient::~QCanvasConicalGradient()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QCanvasConicalGradientD1Ev(QCanvasConicalGradient *self) {
  delete self;
}

//  void QCanvasConicalGradient::swap(QCanvasConicalGradient &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QCanvasConicalGradient4swapERS_(
    QCanvasConicalGradient *self,
    QCanvasConicalGradient *other) {
  self->swap(*other);
}

//  QPointF QCanvasConicalGradient::centerPosition() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK22QCanvasConicalGradient14centerPositionEv(
    const QCanvasConicalGradient *self) {
  return new QPointF(self->centerPosition());
}

//  void QCanvasConicalGradient::setCenterPosition(qreal x, qreal y)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QCanvasConicalGradient17setCenterPositionEdd(
    QCanvasConicalGradient *self,
    qreal x,
    qreal y) {
  self->setCenterPosition(x, y);
}

//  void QCanvasConicalGradient::setCenterPosition(QPointF center)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QCanvasConicalGradient17setCenterPositionE7QPointF(
    QCanvasConicalGradient *self,
    const QPointF *center) {
  self->setCenterPosition(*center);
}

//  qreal QCanvasConicalGradient::startAngle() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK22QCanvasConicalGradient10startAngleEv(
    const QCanvasConicalGradient *self) {
  return self->startAngle();
}

//  void QCanvasConicalGradient::setStartAngle(qreal angle)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QCanvasConicalGradient13setStartAngleEd(
    QCanvasConicalGradient *self,
    qreal angle) {
  self->setStartAngle(angle);
}

//  QCanvasConicalGradient::QCanvasConicalGradient(const QCanvasBrush &brush)
extern "C" Q_DECL_EXPORT
QCanvasConicalGradient *ritual_ZN22QCanvasConicalGradientC1ERK12QCanvasBrush(
    const QCanvasBrush *brush) {
  return new QCanvasConicalGradient(*brush);
}
