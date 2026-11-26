//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/transform_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-25: Qt's 'Matrix4x4' is the SSE class
//  Qt3DCore::Matrix4x4_SSE where __SSE2__ is defined and QMatrix4x4
//  elsewhere (the compiler refused a QMatrix4x4 made from the SSE
//  class); the ritual hands the alias 'Matrix4x4', as Qt writes it, so
//  that it is right for both. Kept as it is when the generator runs
//  again.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/transform_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qmatrix4x4.h>

//  bool Qt3DRender::Render::Transform::hasViewMatrix() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DRender6Render9Transform13hasViewMatrixEv(
    const Qt3DRender::Render::Transform *self) {
  return self->hasViewMatrix();
}

//  const Matrix4x4 &Qt3DRender::Render::Transform::viewMatrix() const
extern "C" Q_DECL_EXPORT
Matrix4x4 *ritual_ZNK10Qt3DRender6Render9Transform10viewMatrixEv(
    const Qt3DRender::Render::Transform *self) {
  return new Matrix4x4(self->viewMatrix());
}
