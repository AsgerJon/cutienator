//  Written by dev_tooling.RitualGenerator from the records of
//  QtLottie/6.12.0/QtLottie/private/qlottiegradientholder_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtLottie/QtLottie>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLottie/6.12.0/QtLottie/private/qlottiegradientholder_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qpoint.h>

//  QGradient *QLottieGradientHolderContent::value() const
extern "C" Q_DECL_EXPORT
QGradient *ritual_ZNK28QLottieGradientHolderContent5valueEv(
    const QLottieGradientHolderContent *self) {
  return self->value();
}

//  QGradient::Type QLottieGradientHolderContent::gradientType() const
extern "C" Q_DECL_EXPORT
QGradient::Type ritual_ZNK28QLottieGradientHolderContent12gradientTypeEv(
    const QLottieGradientHolderContent *self) {
  return self->gradientType();
}

//  QPointF QLottieGradientHolderContent::startPoint() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK28QLottieGradientHolderContent10startPointEv(
    const QLottieGradientHolderContent *self) {
  return new QPointF(self->startPoint());
}

//  QPointF QLottieGradientHolderContent::endPoint() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK28QLottieGradientHolderContent8endPointEv(
    const QLottieGradientHolderContent *self) {
  return new QPointF(self->endPoint());
}

//  qreal QLottieGradientHolderContent::highlightLength() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK28QLottieGradientHolderContent15highlightLengthEv(
    const QLottieGradientHolderContent *self) {
  return self->highlightLength();
}

//  qreal QLottieGradientHolderContent::highlightAngle() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK28QLottieGradientHolderContent14highlightAngleEv(
    const QLottieGradientHolderContent *self) {
  return self->highlightAngle();
}

//  void QLottieGradientHolderContent::setGradient(qreal opacity)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QLottieGradientHolderContent11setGradientEd(
    QLottieGradientHolderContent *self,
    qreal opacity) {
  self->setGradient(opacity);
}

//  void QLottieGradientHolderContent::updateGradientProperties(int frame)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QLottieGradientHolderContent24updateGradientPropertiesEi(
    QLottieGradientHolderContent *self,
    int frame) {
  self->updateGradientProperties(frame);
}

//  QLottieGradientHolderContent::~QLottieGradientHolderContent()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QLottieGradientHolderContentD1Ev(
    QLottieGradientHolderContent *self) {
  delete self;
}
