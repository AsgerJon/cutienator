//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendercamera_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendercamera_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QSSGRenderCamera::ClipPlanes::ClipPlanes()
extern "C" Q_DECL_EXPORT
QSSGRenderCamera::ClipPlanes *ritual_ZN16QSSGRenderCamera10ClipPlanesC1Ev() {
  return new QSSGRenderCamera::ClipPlanes();
}

//  QSSGRenderCamera::ClipPlanes::ClipPlanes(float n, float f)
extern "C" Q_DECL_EXPORT
QSSGRenderCamera::ClipPlanes *ritual_ZN16QSSGRenderCamera10ClipPlanesC1Eff(
    float n,
    float f) {
  return new QSSGRenderCamera::ClipPlanes(n, f);
}

//  float QSSGRenderCamera::ClipPlanes::clipNear() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK16QSSGRenderCamera10ClipPlanes8clipNearEv(
    const QSSGRenderCamera::ClipPlanes *self) {
  return self->clipNear();
}

//  float QSSGRenderCamera::ClipPlanes::clipFar() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK16QSSGRenderCamera10ClipPlanes7clipFarEv(
    const QSSGRenderCamera::ClipPlanes *self) {
  return self->clipFar();
}

//  void QSSGRenderCamera::ClipPlanes::setClipNear(float n)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSSGRenderCamera10ClipPlanes11setClipNearEf(
    QSSGRenderCamera::ClipPlanes *self,
    float n) {
  self->setClipNear(n);
}

//  void QSSGRenderCamera::ClipPlanes::setClipFar(float f)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSSGRenderCamera10ClipPlanes10setClipFarEf(
    QSSGRenderCamera::ClipPlanes *self,
    float f) {
  self->setClipFar(f);
}

//  QSSGRenderCamera::ClipPlanes::~ClipPlanes()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSSGRenderCamera10ClipPlanesD1Ev(
    QSSGRenderCamera::ClipPlanes *self) {
  delete self;
}
