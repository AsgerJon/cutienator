//  Written by dev_tooling.RitualGenerator from the records of
//  QtCanvasPainter/qcanvaslineargradient.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtCanvasPainter/qcanvaslineargradient.h>
#include <QtCore/qpoint.h>
#include <QtCanvasPainter/qcanvasbrush.h>

//  QCanvasLinearGradient::QCanvasLinearGradient()
extern "C" Q_DECL_EXPORT
QCanvasLinearGradient *ritual_ZN21QCanvasLinearGradientC1Ev() {
  return new QCanvasLinearGradient();
}

//  QCanvasLinearGradient::QCanvasLinearGradient(qreal startX, qreal startY,
//      qreal endX, qreal endY)
extern "C" Q_DECL_EXPORT
QCanvasLinearGradient *ritual_ZN21QCanvasLinearGradientC1Edddd(
    qreal startX,
    qreal startY,
    qreal endX,
    qreal endY) {
  return new QCanvasLinearGradient(startX, startY, endX, endY);
}

//  QCanvasLinearGradient::QCanvasLinearGradient(QPointF start, QPointF end)
extern "C" Q_DECL_EXPORT
QCanvasLinearGradient *ritual_ZN21QCanvasLinearGradientC1E7QPointFS0_(
    const QPointF *start,
    const QPointF *end) {
  return new QCanvasLinearGradient(*start, *end);
}

//  QCanvasLinearGradient::QCanvasLinearGradient(const QCanvasLinearGradient
//      &a0)
extern "C" Q_DECL_EXPORT
QCanvasLinearGradient *ritual_ZN21QCanvasLinearGradientC1ERKS_(
    const QCanvasLinearGradient *a0) {
  return new QCanvasLinearGradient(*a0);
}

//  QCanvasLinearGradient &QCanvasLinearGradient::operator=(const
//      QCanvasLinearGradient &a0)
extern "C" Q_DECL_EXPORT
QCanvasLinearGradient *ritual_ZN21QCanvasLinearGradientaSERKS_(
    QCanvasLinearGradient *self,
    const QCanvasLinearGradient *a0) {
  return &(self->operator=(*a0));
}

//  QCanvasLinearGradient::QCanvasLinearGradient(QCanvasLinearGradient &&a0)
extern "C" Q_DECL_EXPORT
QCanvasLinearGradient *ritual_ZN21QCanvasLinearGradientC1EOS_(
    QCanvasLinearGradient *a0) {
  return new QCanvasLinearGradient(std::move(*a0));
}

//  QCanvasLinearGradient
//      &QCanvasLinearGradient::operator=(QCanvasLinearGradient &&a0)
extern "C" Q_DECL_EXPORT
QCanvasLinearGradient *ritual_ZN21QCanvasLinearGradientaSEOS_(
    QCanvasLinearGradient *self,
    QCanvasLinearGradient *a0) {
  return &(self->operator=(std::move(*a0)));
}

//  QCanvasLinearGradient::~QCanvasLinearGradient()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QCanvasLinearGradientD1Ev(QCanvasLinearGradient *self) {
  delete self;
}

//  void QCanvasLinearGradient::swap(QCanvasLinearGradient &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QCanvasLinearGradient4swapERS_(
    QCanvasLinearGradient *self,
    QCanvasLinearGradient *other) {
  self->swap(*other);
}

//  QPointF QCanvasLinearGradient::startPosition() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK21QCanvasLinearGradient13startPositionEv(
    const QCanvasLinearGradient *self) {
  return new QPointF(self->startPosition());
}

//  void QCanvasLinearGradient::setStartPosition(qreal x, qreal y)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QCanvasLinearGradient16setStartPositionEdd(
    QCanvasLinearGradient *self,
    qreal x,
    qreal y) {
  self->setStartPosition(x, y);
}

//  void QCanvasLinearGradient::setStartPosition(QPointF start)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QCanvasLinearGradient16setStartPositionE7QPointF(
    QCanvasLinearGradient *self,
    const QPointF *start) {
  self->setStartPosition(*start);
}

//  QPointF QCanvasLinearGradient::endPosition() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK21QCanvasLinearGradient11endPositionEv(
    const QCanvasLinearGradient *self) {
  return new QPointF(self->endPosition());
}

//  void QCanvasLinearGradient::setEndPosition(qreal x, qreal y)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QCanvasLinearGradient14setEndPositionEdd(
    QCanvasLinearGradient *self,
    qreal x,
    qreal y) {
  self->setEndPosition(x, y);
}

//  void QCanvasLinearGradient::setEndPosition(QPointF end)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QCanvasLinearGradient14setEndPositionE7QPointF(
    QCanvasLinearGradient *self,
    const QPointF *end) {
  self->setEndPosition(*end);
}

//  QCanvasLinearGradient::QCanvasLinearGradient(const QCanvasBrush &brush)
extern "C" Q_DECL_EXPORT
QCanvasLinearGradient *ritual_ZN21QCanvasLinearGradientC1ERK12QCanvasBrush(
    const QCanvasBrush *brush) {
  return new QCanvasLinearGradient(*brush);
}
