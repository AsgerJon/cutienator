//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/pickboundingvolumeutils_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/pickboundingvolumeutils_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/private/pickboundingvolumeutils_p.h>
#include <Qt3DRender/private/geometryrenderer_p.h>
#include <Qt3DRender/private/framegraphnode_p.h>
#include <Qt3DRender/private/cameralens_p.h>
#include <Qt3DRender/private/cameraselectornode_p.h>
#include <Qt3DRender/private/viewportnode_p.h>
#include <Qt3DRender/private/rendersurfaceselector_p.h>
#include <Qt3DRender/private/triangleboundingvolume_p.h>
#include <Qt3DRender/private/nodemanagers_p.h>
#include <Qt3DRender/private/sphere_p.h>
#include <Qt3DRender/private/entity_p.h>
#include <Qt3DRender/private/trianglesvisitor_p.h>
#include <Qt3DRender/private/segmentsvisitor_p.h>
#include <Qt3DRender/private/pointsvisitor_p.h>
#include <Qt3DRender/private/layer_p.h>
#include <Qt3DRender/private/layerfilternode_p.h>
#include <Qt3DRender/private/rendersettings_p.h>
#include <Qt3DRender/private/filterlayerentityjob_p.h>
#include <vector>
#include <algorithm>
#include <functional>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/render/jobs/pickboundingvolumeutils.cpp, line 477, as _ZNK10Qt3DRender6Render12PickingUtils32AbstractCollisionGathererFunctor13rayHitsEntityEPKNS0_6EntityE
namespace Qt3DRender::Render::PickingUtils {
using namespace Qt3DRender::RayCasting;
inline bool AbstractCollisionGathererFunctor::rayHitsEntity(const Entity *entity) const
{
    QRayCastingService rayCasting;
    const QCollisionQueryResult::Hit queryResult = rayCasting.query(m_ray, entity->worldBoundingVolume());
    return queryResult.m_distance >= 0.f;
}
}  // namespace Qt3DRender::Render::PickingUtils

//  from ../qt3d/src/render/jobs/pickboundingvolumeutils.cpp, line 484, as _ZN10Qt3DRender6Render12PickingUtils32AbstractCollisionGathererFunctor8sortHitsERSt6vectorINS_10RayCasting21QCollisionQueryResult3HitESaIS6_EE
namespace Qt3DRender::Render::PickingUtils {
using namespace Qt3DRender::RayCasting;
inline void AbstractCollisionGathererFunctor::sortHits(HitList &results)
{
    auto compareHitsDistance = [](const HitList::value_type &a,
                                  const HitList::value_type &b) {
        return a.m_distance < b.m_distance;
    };
    std::sort(results.begin(), results.end(), compareHitsDistance);
}
}  // namespace Qt3DRender::Render::PickingUtils
//  -----------------------------------------------------------------------

//  Qt3DRender::Render::PickingUtils::AbstractCollisionGathererFunctor::~Abst
//      ractCollisionGathererFunctor()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render12PickingUtils32AbstractCollisionGathererFunctorD1Ev(
    Qt3DRender::Render::PickingUtils::AbstractCollisionGathererFunctor *self) {
  delete self;
}

//  HitList Qt3DRender::Render::PickingUtils::AbstractCollisionGathererFuncto
//      r::computeHits(const std::vector<Entity *> &entities,
//      Qt3DRender::QPickingSettings::PickResultMode mode)
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::PickingUtils::HitList *ritual_ZN10Qt3DRender6Render12PickingUtils32AbstractCollisionGathererFunctor11computeHitsERKSt6vectorIPNS0_6EntityESaIS5_EENS_16QPickingSettings14PickResultModeE(
    Qt3DRender::Render::PickingUtils::AbstractCollisionGathererFunctor *self,
    const std::vector<Qt3DRender::Render::Entity *> *entities,
    Qt3DRender::QPickingSettings::PickResultMode mode) {
  return new Qt3DRender::Render::PickingUtils::HitList(
      self->computeHits(
          *entities,
          mode));
}

//  HitList Qt3DRender::Render::PickingUtils::AbstractCollisionGathererFuncto
//      r::pick(const Entity *entity) const
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::PickingUtils::HitList *ritual_ZNK10Qt3DRender6Render12PickingUtils32AbstractCollisionGathererFunctor4pickEPKNS0_6EntityE(
    const Qt3DRender::Render::PickingUtils::AbstractCollisionGathererFunctor *self,
    const Qt3DRender::Render::Entity *entity) {
  return new Qt3DRender::Render::PickingUtils::HitList(self->pick(entity));
}

//  bool Qt3DRender::Render::PickingUtils::AbstractCollisionGathererFunctor::
//      rayHitsEntity(const Entity *entity) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DRender6Render12PickingUtils32AbstractCollisionGathererFunctor13rayHitsEntityEPKNS0_6EntityE(
    const Qt3DRender::Render::PickingUtils::AbstractCollisionGathererFunctor *self,
    const Qt3DRender::Render::Entity *entity) {
  return self->rayHitsEntity(entity);
}

//  void Qt3DRender::Render::PickingUtils::AbstractCollisionGathererFunctor::
//      sortHits(HitList &results)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render12PickingUtils32AbstractCollisionGathererFunctor8sortHitsERSt6vectorINS_10RayCasting21QCollisionQueryResult3HitESaIS6_EE(
    Qt3DRender::Render::PickingUtils::HitList *results) {
  Qt3DRender::Render::PickingUtils::AbstractCollisionGathererFunctor::sortHits(
      *results);
}

//  a Qt3DRender::Render::PickingUtils::HitList a ritual of
//      Qt3DRender::Render::PickingUtils::AbstractCollisionGathererFunctor
//      gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DRender_Render_PickingUtils_AbstractCollisionGathererFunctor__Qt3DRender_Render_PickingUtils_HitList(
    Qt3DRender::Render::PickingUtils::HitList *self) {
  delete self;
}
