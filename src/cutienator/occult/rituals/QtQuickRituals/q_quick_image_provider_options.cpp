//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickpixmap_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickpixmap_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qcolorspace.h>
#include <QtCore/qrect.h>

//  QQuickImageProviderOptions::QQuickImageProviderOptions()
extern "C" Q_DECL_EXPORT
QQuickImageProviderOptions *ritual_ZN26QQuickImageProviderOptionsC1Ev() {
  return new QQuickImageProviderOptions();
}

//  QQuickImageProviderOptions::~QQuickImageProviderOptions()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickImageProviderOptionsD1Ev(
    QQuickImageProviderOptions *self) {
  delete self;
}

//  QQuickImageProviderOptions::QQuickImageProviderOptions(const
//      QQuickImageProviderOptions &a0)
extern "C" Q_DECL_EXPORT
QQuickImageProviderOptions *ritual_ZN26QQuickImageProviderOptionsC1ERKS_(
    const QQuickImageProviderOptions *a0) {
  return new QQuickImageProviderOptions(*a0);
}

//  QQuickImageProviderOptions &QQuickImageProviderOptions::operator=(const
//      QQuickImageProviderOptions &a0)
extern "C" Q_DECL_EXPORT
QQuickImageProviderOptions *ritual_ZN26QQuickImageProviderOptionsaSERKS_(
    QQuickImageProviderOptions *self,
    const QQuickImageProviderOptions *a0) {
  return &(self->operator=(*a0));
}

//  bool QQuickImageProviderOptions::operator==(const
//      QQuickImageProviderOptions &a0) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK26QQuickImageProviderOptionseqERKS_(
    const QQuickImageProviderOptions *self,
    const QQuickImageProviderOptions *a0) {
  return self->operator==(*a0);
}

//  AutoTransform QQuickImageProviderOptions::autoTransform() const
extern "C" Q_DECL_EXPORT
QQuickImageProviderOptions::AutoTransform ritual_ZNK26QQuickImageProviderOptions13autoTransformEv(
    const QQuickImageProviderOptions *self) {
  return self->autoTransform();
}

//  void QQuickImageProviderOptions::setAutoTransform(AutoTransform
//      autoTransform)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickImageProviderOptions16setAutoTransformENS_13AutoTransformE(
    QQuickImageProviderOptions *self,
    QQuickImageProviderOptions::AutoTransform autoTransform) {
  self->setAutoTransform(autoTransform);
}

//  bool QQuickImageProviderOptions::preserveAspectRatioCrop() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK26QQuickImageProviderOptions23preserveAspectRatioCropEv(
    const QQuickImageProviderOptions *self) {
  return self->preserveAspectRatioCrop();
}

//  void QQuickImageProviderOptions::setPreserveAspectRatioCrop(bool
//      preserveAspectRatioCrop)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickImageProviderOptions26setPreserveAspectRatioCropEb(
    QQuickImageProviderOptions *self,
    bool preserveAspectRatioCrop) {
  self->setPreserveAspectRatioCrop(preserveAspectRatioCrop);
}

//  bool QQuickImageProviderOptions::preserveAspectRatioFit() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK26QQuickImageProviderOptions22preserveAspectRatioFitEv(
    const QQuickImageProviderOptions *self) {
  return self->preserveAspectRatioFit();
}

//  void QQuickImageProviderOptions::setPreserveAspectRatioFit(bool
//      preserveAspectRatioFit)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickImageProviderOptions25setPreserveAspectRatioFitEb(
    QQuickImageProviderOptions *self,
    bool preserveAspectRatioFit) {
  self->setPreserveAspectRatioFit(preserveAspectRatioFit);
}

//  QColorSpace QQuickImageProviderOptions::targetColorSpace() const
extern "C" Q_DECL_EXPORT
QColorSpace *ritual_ZNK26QQuickImageProviderOptions16targetColorSpaceEv(
    const QQuickImageProviderOptions *self) {
  return new QColorSpace(self->targetColorSpace());
}

//  void QQuickImageProviderOptions::setTargetColorSpace(const QColorSpace
//      &colorSpace)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickImageProviderOptions19setTargetColorSpaceERK11QColorSpace(
    QQuickImageProviderOptions *self,
    const QColorSpace *colorSpace) {
  self->setTargetColorSpace(*colorSpace);
}

//  QRectF QQuickImageProviderOptions::sourceClipRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK26QQuickImageProviderOptions14sourceClipRectEv(
    const QQuickImageProviderOptions *self) {
  return new QRectF(self->sourceClipRect());
}

//  void QQuickImageProviderOptions::setSourceClipRect(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickImageProviderOptions17setSourceClipRectERK6QRectF(
    QQuickImageProviderOptions *self,
    const QRectF *rect) {
  self->setSourceClipRect(*rect);
}
