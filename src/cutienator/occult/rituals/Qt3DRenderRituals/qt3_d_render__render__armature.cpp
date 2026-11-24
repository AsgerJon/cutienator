//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/armature_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/armature_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/qnodeid.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/uniform_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt3DCore::QNodeId Qt3DRender::Render::Armature::skeletonId() const
extern "C" Q_DECL_EXPORT
Qt3DCore::QNodeId *ritual_ZNK10Qt3DRender6Render8Armature10skeletonIdEv(
    const Qt3DRender::Render::Armature *self) {
  return new Qt3DCore::QNodeId(self->skeletonId());
}

//  const UniformValue
//      &Qt3DRender::Render::Armature::skinningPaletteUniform() const
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::UniformValue *ritual_ZNK10Qt3DRender6Render8Armature22skinningPaletteUniformEv(
    const Qt3DRender::Render::Armature *self) {
  return new Qt3DRender::Render::UniformValue(
      self->skinningPaletteUniform());
}

//  void Qt3DRender::Render::Armature::syncFromFrontEnd(const Qt3DCore::QNode
//      *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10Qt3DRender6Render8Armature16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DRender::Render::Armature *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->Qt3DRender::Render::Armature::syncFromFrontEnd(frontEnd, firstTime);
}
