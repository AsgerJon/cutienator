//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/pickboundingvolumeutils_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/pickboundingvolumeutils_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  HitList Qt3DRender::Render::PickingUtils::EntityCollisionGathererFunctor:
//      :computeHits(const std::vector<Entity *> &entities,
//      Qt3DRender::QPickingSettings::PickResultMode mode)
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::PickingUtils::HitList *ritual_ZN10Qt3DRender6Render12PickingUtils30EntityCollisionGathererFunctor11computeHitsERKSt6vectorIPNS0_6EntityESaIS5_EENS_16QPickingSettings14PickResultModeE(
    Qt3DRender::Render::PickingUtils::EntityCollisionGathererFunctor *self,
    const std::vector<Qt3DRender::Render::Entity *> *entities,
    Qt3DRender::QPickingSettings::PickResultMode mode) {
  return new Qt3DRender::Render::PickingUtils::HitList(
      self->computeHits(
          *entities,
          mode));
}

//  HitList Qt3DRender::Render::PickingUtils::EntityCollisionGathererFunctor:
//      :pick(const Entity *entity) const
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::PickingUtils::HitList *ritual_ZNK10Qt3DRender6Render12PickingUtils30EntityCollisionGathererFunctor4pickEPKNS0_6EntityE(
    const Qt3DRender::Render::PickingUtils::EntityCollisionGathererFunctor *self,
    const Qt3DRender::Render::Entity *entity) {
  return new Qt3DRender::Render::PickingUtils::HitList(self->pick(entity));
}

//  Qt3DRender::Render::PickingUtils::EntityCollisionGathererFunctor::~Entity
//      CollisionGathererFunctor()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render12PickingUtils30EntityCollisionGathererFunctorD1Ev(
    Qt3DRender::Render::PickingUtils::EntityCollisionGathererFunctor *self) {
  delete self;
}

//  a Qt3DRender::Render::PickingUtils::HitList a ritual of
//      Qt3DRender::Render::PickingUtils::EntityCollisionGathererFunctor gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DRender_Render_PickingUtils_EntityCollisionGathererFunctor__Qt3DRender_Render_PickingUtils_HitList(
    Qt3DRender::Render::PickingUtils::HitList *self) {
  delete self;
}
