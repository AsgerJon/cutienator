//  Written by dev_tooling.RitualGenerator from the records of
//  QtCanvasPainter/qcanvasboxgradient.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtCanvasPainter/qcanvasboxgradient.h>
#include <QtCore/qrect.h>
#include <QtCanvasPainter/qcanvasbrush.h>

//  QCanvasBoxGradient::QCanvasBoxGradient()
extern "C" Q_DECL_EXPORT
QCanvasBoxGradient *ritual_ZN18QCanvasBoxGradientC1Ev() {
  return new QCanvasBoxGradient();
}

//  QCanvasBoxGradient::QCanvasBoxGradient(qreal x, qreal y, qreal width,
//      qreal height)
extern "C" Q_DECL_EXPORT
QCanvasBoxGradient *ritual_ZN18QCanvasBoxGradientC1Edddd(
    qreal x,
    qreal y,
    qreal width,
    qreal height) {
  return new QCanvasBoxGradient(x, y, width, height);
}

//  QCanvasBoxGradient::QCanvasBoxGradient(const QRectF &rect)
extern "C" Q_DECL_EXPORT
QCanvasBoxGradient *ritual_ZN18QCanvasBoxGradientC1ERK6QRectF(
    const QRectF *rect) {
  return new QCanvasBoxGradient(*rect);
}

//  QCanvasBoxGradient::QCanvasBoxGradient(const QCanvasBoxGradient &a0)
extern "C" Q_DECL_EXPORT
QCanvasBoxGradient *ritual_ZN18QCanvasBoxGradientC1ERKS_(
    const QCanvasBoxGradient *a0) {
  return new QCanvasBoxGradient(*a0);
}

//  QCanvasBoxGradient &QCanvasBoxGradient::operator=(const
//      QCanvasBoxGradient &a0)
extern "C" Q_DECL_EXPORT
QCanvasBoxGradient *ritual_ZN18QCanvasBoxGradientaSERKS_(
    QCanvasBoxGradient *self,
    const QCanvasBoxGradient *a0) {
  return &(self->operator=(*a0));
}

//  QCanvasBoxGradient::QCanvasBoxGradient(QCanvasBoxGradient &&a0)
extern "C" Q_DECL_EXPORT
QCanvasBoxGradient *ritual_ZN18QCanvasBoxGradientC1EOS_(
    QCanvasBoxGradient *a0) {
  return new QCanvasBoxGradient(std::move(*a0));
}

//  QCanvasBoxGradient &QCanvasBoxGradient::operator=(QCanvasBoxGradient
//      &&a0)
extern "C" Q_DECL_EXPORT
QCanvasBoxGradient *ritual_ZN18QCanvasBoxGradientaSEOS_(
    QCanvasBoxGradient *self,
    QCanvasBoxGradient *a0) {
  return &(self->operator=(std::move(*a0)));
}

//  QCanvasBoxGradient::~QCanvasBoxGradient()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QCanvasBoxGradientD1Ev(QCanvasBoxGradient *self) {
  delete self;
}

//  void QCanvasBoxGradient::swap(QCanvasBoxGradient &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QCanvasBoxGradient4swapERS_(
    QCanvasBoxGradient *self,
    QCanvasBoxGradient *other) {
  self->swap(*other);
}

//  QRectF QCanvasBoxGradient::rect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK18QCanvasBoxGradient4rectEv(
    const QCanvasBoxGradient *self) {
  return new QRectF(self->rect());
}

//  void QCanvasBoxGradient::setRect(qreal x, qreal y, qreal width, qreal
//      height)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QCanvasBoxGradient7setRectEdddd(
    QCanvasBoxGradient *self,
    qreal x,
    qreal y,
    qreal width,
    qreal height) {
  self->setRect(x, y, width, height);
}

//  void QCanvasBoxGradient::setRect(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QCanvasBoxGradient7setRectERK6QRectF(
    QCanvasBoxGradient *self,
    const QRectF *rect) {
  self->setRect(*rect);
}

//  qreal QCanvasBoxGradient::feather() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK18QCanvasBoxGradient7featherEv(
    const QCanvasBoxGradient *self) {
  return self->feather();
}

//  void QCanvasBoxGradient::setFeather(qreal feather)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QCanvasBoxGradient10setFeatherEd(
    QCanvasBoxGradient *self,
    qreal feather) {
  self->setFeather(feather);
}

//  qreal QCanvasBoxGradient::radius() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK18QCanvasBoxGradient6radiusEv(
    const QCanvasBoxGradient *self) {
  return self->radius();
}

//  void QCanvasBoxGradient::setRadius(qreal radius)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QCanvasBoxGradient9setRadiusEd(
    QCanvasBoxGradient *self,
    qreal radius) {
  self->setRadius(radius);
}

//  QCanvasBoxGradient::QCanvasBoxGradient(const QCanvasBrush &brush)
extern "C" Q_DECL_EXPORT
QCanvasBoxGradient *ritual_ZN18QCanvasBoxGradientC1ERK12QCanvasBrush(
    const QCanvasBrush *brush) {
  return new QCanvasBoxGradient(*brush);
}
