//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qbrush.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qbrush.h>
#include <QtCore/qpoint.h>

//  QConicalGradient::QConicalGradient()
extern "C" Q_DECL_EXPORT
QConicalGradient *ritual_ZN16QConicalGradientC1Ev() {
  return new QConicalGradient();
}

//  QConicalGradient::QConicalGradient(const QPointF &center, qreal
//      startAngle)
extern "C" Q_DECL_EXPORT
QConicalGradient *ritual_ZN16QConicalGradientC1ERK7QPointFd(
    const QPointF *center,
    qreal startAngle) {
  return new QConicalGradient(*center, startAngle);
}

//  QConicalGradient::QConicalGradient(qreal cx, qreal cy, qreal startAngle)
extern "C" Q_DECL_EXPORT
QConicalGradient *ritual_ZN16QConicalGradientC1Eddd(
    qreal cx,
    qreal cy,
    qreal startAngle) {
  return new QConicalGradient(cx, cy, startAngle);
}

//  QConicalGradient::~QConicalGradient()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QConicalGradientD1Ev(QConicalGradient *self) {
  delete self;
}

//  QPointF QConicalGradient::center() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK16QConicalGradient6centerEv(
    const QConicalGradient *self) {
  return new QPointF(self->center());
}

//  void QConicalGradient::setCenter(const QPointF &center)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QConicalGradient9setCenterERK7QPointF(
    QConicalGradient *self,
    const QPointF *center) {
  self->setCenter(*center);
}

//  void QConicalGradient::setCenter(qreal x, qreal y)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QConicalGradient9setCenterEdd(
    QConicalGradient *self,
    qreal x,
    qreal y) {
  self->setCenter(x, y);
}

//  qreal QConicalGradient::angle() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK16QConicalGradient5angleEv(const QConicalGradient *self) {
  return self->angle();
}

//  void QConicalGradient::setAngle(qreal angle)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QConicalGradient8setAngleEd(
    QConicalGradient *self,
    qreal angle) {
  self->setAngle(angle);
}
