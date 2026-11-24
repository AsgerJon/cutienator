//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendercamera_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendercamera_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QSSGRenderCameraFieldOfView::QSSGRenderCameraFieldOfView(Orientation
//      orientation)
extern "C" Q_DECL_EXPORT
QSSGRenderCameraFieldOfView *ritual_ZN27QSSGRenderCameraFieldOfViewC1ENS_11OrientationE(
    QSSGRenderCameraFieldOfView::Orientation orientation) {
  return new QSSGRenderCameraFieldOfView(orientation);
}

//  QSSGRenderCameraFieldOfView::QSSGRenderCameraFieldOfView(const
//      QSSGRenderCameraFieldOfView &a0)
extern "C" Q_DECL_EXPORT
QSSGRenderCameraFieldOfView *ritual_ZN27QSSGRenderCameraFieldOfViewC1ERKS_(
    const QSSGRenderCameraFieldOfView *a0) {
  return new QSSGRenderCameraFieldOfView(*a0);
}

//  Orientation QSSGRenderCameraFieldOfView::orientation() const
extern "C" Q_DECL_EXPORT
QSSGRenderCameraFieldOfView::Orientation ritual_ZNK27QSSGRenderCameraFieldOfView11orientationEv(
    const QSSGRenderCameraFieldOfView *self) {
  return self->orientation();
}

//  float QSSGRenderCameraFieldOfView::degrees() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK27QSSGRenderCameraFieldOfView7degreesEv(
    const QSSGRenderCameraFieldOfView *self) {
  return self->degrees();
}

//  float QSSGRenderCameraFieldOfView::radians() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK27QSSGRenderCameraFieldOfView7radiansEv(
    const QSSGRenderCameraFieldOfView *self) {
  return self->radians();
}

//  void QSSGRenderCameraFieldOfView::setDegrees(float fov)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QSSGRenderCameraFieldOfView10setDegreesEf(
    QSSGRenderCameraFieldOfView *self,
    float fov) {
  self->setDegrees(fov);
}

//  QSSGRenderCameraFieldOfView
//      QSSGRenderCameraFieldOfView::asVerticalFov(float aspectRatio) const
extern "C" Q_DECL_EXPORT
QSSGRenderCameraFieldOfView *ritual_ZNK27QSSGRenderCameraFieldOfView13asVerticalFovEf(
    const QSSGRenderCameraFieldOfView *self,
    float aspectRatio) {
  return new QSSGRenderCameraFieldOfView(self->asVerticalFov(aspectRatio));
}

//  void QSSGRenderCameraFieldOfView::setRadians(float fov)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QSSGRenderCameraFieldOfView10setRadiansEf(
    QSSGRenderCameraFieldOfView *self,
    float fov) {
  self->setRadians(fov);
}

//  QSSGRenderCameraFieldOfView::QSSGRenderCameraFieldOfView(float fov,
//      FovValue value, Orientation angleOfView)
extern "C" Q_DECL_EXPORT
QSSGRenderCameraFieldOfView *ritual_ZN27QSSGRenderCameraFieldOfViewC1EfNS_8FovValueENS_11OrientationE(
    float fov,
    QSSGRenderCameraFieldOfView::FovValue value,
    QSSGRenderCameraFieldOfView::Orientation angleOfView) {
  return new QSSGRenderCameraFieldOfView(fov, value, angleOfView);
}

//  QSSGRenderCameraFieldOfView::~QSSGRenderCameraFieldOfView()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QSSGRenderCameraFieldOfViewD1Ev(
    QSSGRenderCameraFieldOfView *self) {
  delete self;
}
