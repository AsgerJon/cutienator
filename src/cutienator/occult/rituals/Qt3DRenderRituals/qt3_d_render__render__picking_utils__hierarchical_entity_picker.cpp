//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/pickboundingvolumeutils_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/pickboundingvolumeutils_p.h>
#include <Qt3DRender/6.12.0/Qt3DRender/private/qray3d_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/QHash>
#include <Qt3DCore/Qt3DCore>
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

//  from ../qt3d/src/render/jobs/pickboundingvolumeutils.cpp, line 729, as _ZN10Qt3DRender6Render12PickingUtils24HierarchicalEntityPickerC1ERKNS_10RayCasting6QRay3DEb
namespace Qt3DRender::Render::PickingUtils {
using namespace Qt3DRender::RayCasting;
inline HierarchicalEntityPicker::HierarchicalEntityPicker(const QRay3D &ray, bool requireObjectPicker)
    : m_ray(ray)
    , m_objectPickersRequired(requireObjectPicker)
{
}
}  // namespace Qt3DRender::Render::PickingUtils

//  from ../qt3d/src/render/jobs/pickboundingvolumeutils.cpp, line 735, as _ZN10Qt3DRender6Render12PickingUtils24HierarchicalEntityPicker17setLayerFilterIdsERK5QListIN8Qt3DCore7QNodeIdEE
namespace Qt3DRender::Render::PickingUtils {
using namespace Qt3DRender::RayCasting;
inline void HierarchicalEntityPicker::setLayerFilterIds(const Qt3DCore::QNodeIdVector &layerFilterIds)
{
    m_layerFilterIds = layerFilterIds;
}
}  // namespace Qt3DRender::Render::PickingUtils

//  from ../qt3d/src/render/jobs/pickboundingvolumeutils.cpp, line 740, as _ZN10Qt3DRender6Render12PickingUtils24HierarchicalEntityPicker11setLayerIdsERK5QListIN8Qt3DCore7QNodeIdEENS_18QAbstractRayCaster10FilterModeE
namespace Qt3DRender::Render::PickingUtils {
using namespace Qt3DRender::RayCasting;
inline void HierarchicalEntityPicker::setLayerIds(const Qt3DCore::QNodeIdVector &layerIds,
                                           QAbstractRayCaster::FilterMode mode)
{
    m_layerIds = layerIds;
    m_layerFilterMode = mode;
}
}  // namespace Qt3DRender::Render::PickingUtils
//  -----------------------------------------------------------------------

//  Qt3DRender::Render::PickingUtils::HierarchicalEntityPicker::HierarchicalE
//      ntityPicker(const RayCasting::QRay3D &ray, bool requireObjectPicker)
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::PickingUtils::HierarchicalEntityPicker *ritual_ZN10Qt3DRender6Render12PickingUtils24HierarchicalEntityPickerC1ERKNS_10RayCasting6QRay3DEb(
    const Qt3DRender::RayCasting::QRay3D *ray,
    bool requireObjectPicker) {
  return new Qt3DRender::Render::PickingUtils::HierarchicalEntityPicker(
      *ray,
      requireObjectPicker);
}

//  void Qt3DRender::Render::PickingUtils::HierarchicalEntityPicker::setLayer
//      FilterIds(const Qt3DCore::QNodeIdVector &layerFilterIds)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render12PickingUtils24HierarchicalEntityPicker17setLayerFilterIdsERK5QListIN8Qt3DCore7QNodeIdEE(
    Qt3DRender::Render::PickingUtils::HierarchicalEntityPicker *self,
    const Qt3DCore::QNodeIdVector *layerFilterIds) {
  self->setLayerFilterIds(*layerFilterIds);
}

//  void Qt3DRender::Render::PickingUtils::HierarchicalEntityPicker::setLayer
//      Ids(const Qt3DCore::QNodeIdVector &layerIds,
//      QAbstractRayCaster::FilterMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render12PickingUtils24HierarchicalEntityPicker11setLayerIdsERK5QListIN8Qt3DCore7QNodeIdEENS_18QAbstractRayCaster10FilterModeE(
    Qt3DRender::Render::PickingUtils::HierarchicalEntityPicker *self,
    const Qt3DCore::QNodeIdVector *layerIds,
    Qt3DRender::QAbstractRayCaster::FilterMode mode) {
  self->setLayerIds(*layerIds, mode);
}

//  HitList
//      Qt3DRender::Render::PickingUtils::HierarchicalEntityPicker::hits()
//      const
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::PickingUtils::HitList *ritual_ZNK10Qt3DRender6Render12PickingUtils24HierarchicalEntityPicker4hitsEv(
    const Qt3DRender::Render::PickingUtils::HierarchicalEntityPicker *self) {
  return new Qt3DRender::Render::PickingUtils::HitList(self->hits());
}

//  const std::vector<Entity *>
//      &Qt3DRender::Render::PickingUtils::HierarchicalEntityPicker::entities
//      () const
extern "C" Q_DECL_EXPORT
const std::vector<Qt3DRender::Render::Entity *> *ritual_ZNK10Qt3DRender6Render12PickingUtils24HierarchicalEntityPicker8entitiesEv(
    const Qt3DRender::Render::PickingUtils::HierarchicalEntityPicker *self) {
  return &(self->entities());
}

//  QHash<Qt3DCore::QNodeId, int> Qt3DRender::Render::PickingUtils::Hierarchi
//      calEntityPicker::entityToPriorityTable() const
extern "C" Q_DECL_EXPORT
QHash<Qt3DCore::QNodeId, int> *ritual_ZNK10Qt3DRender6Render12PickingUtils24HierarchicalEntityPicker21entityToPriorityTableEv(
    const Qt3DRender::Render::PickingUtils::HierarchicalEntityPicker *self) {
  return new QHash<Qt3DCore::QNodeId, int>(self->entityToPriorityTable());
}

//  Qt3DRender::Render::PickingUtils::HierarchicalEntityPicker::~Hierarchical
//      EntityPicker()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render12PickingUtils24HierarchicalEntityPickerD1Ev(
    Qt3DRender::Render::PickingUtils::HierarchicalEntityPicker *self) {
  delete self;
}

//  a Qt3DRender::Render::PickingUtils::HitList a ritual of
//      Qt3DRender::Render::PickingUtils::HierarchicalEntityPicker gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DRender_Render_PickingUtils_HierarchicalEntityPicker__Qt3DRender_Render_PickingUtils_HitList(
    Qt3DRender::Render::PickingUtils::HitList *self) {
  delete self;
}

//  a QHash<Qt3DCore::QNodeId, int> a ritual of
//      Qt3DRender::Render::PickingUtils::HierarchicalEntityPicker gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DRender_Render_PickingUtils_HierarchicalEntityPicker__QHash_Qt3DCore_QNodeId_int(
    QHash<Qt3DCore::QNodeId, int> *self) {
  delete self;
}
