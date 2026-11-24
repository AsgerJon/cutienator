//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendercamera_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendercamera_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QSSGRenderCamera::Magnification::Magnification()
extern "C" Q_DECL_EXPORT
QSSGRenderCamera::Magnification *ritual_ZN16QSSGRenderCamera13MagnificationC1Ev() {
  return new QSSGRenderCamera::Magnification();
}

//  QSSGRenderCamera::Magnification::Magnification(float h, float v)
extern "C" Q_DECL_EXPORT
QSSGRenderCamera::Magnification *ritual_ZN16QSSGRenderCamera13MagnificationC1Eff(
    float h,
    float v) {
  return new QSSGRenderCamera::Magnification(h, v);
}

//  float QSSGRenderCamera::Magnification::horizontal() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK16QSSGRenderCamera13Magnification10horizontalEv(
    const QSSGRenderCamera::Magnification *self) {
  return self->horizontal();
}

//  float QSSGRenderCamera::Magnification::vertical() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK16QSSGRenderCamera13Magnification8verticalEv(
    const QSSGRenderCamera::Magnification *self) {
  return self->vertical();
}

//  void QSSGRenderCamera::Magnification::setHorizontal(float h)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSSGRenderCamera13Magnification13setHorizontalEf(
    QSSGRenderCamera::Magnification *self,
    float h) {
  self->setHorizontal(h);
}

//  void QSSGRenderCamera::Magnification::setVertical(float v)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSSGRenderCamera13Magnification11setVerticalEf(
    QSSGRenderCamera::Magnification *self,
    float v) {
  self->setVertical(v);
}

//  QSSGRenderCamera::Magnification::~Magnification()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSSGRenderCamera13MagnificationD1Ev(
    QSSGRenderCamera::Magnification *self) {
  delete self;
}
