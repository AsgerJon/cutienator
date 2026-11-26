//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/technique_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/technique_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/qnodeid.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/private/technique_p.h>
#include <Qt3DRender/qrenderpass.h>
#include <Qt3DRender/qparameter.h>
#include <Qt3DRender/qtechnique.h>
#include <Qt3DRender/qgraphicsapifilter.h>
#include <Qt3DRender/private/filterkey_p.h>
#include <Qt3DRender/private/qtechnique_p.h>
#include <Qt3DRender/private/shader_p.h>
#include <Qt3DCore/private/qchangearbiter_p.h>
#include <Qt3DRender/private/managers_p.h>
#include <Qt3DRender/private/techniquemanager_p.h>
#include <Qt3DRender/private/nodemanagers_p.h>
#include <QtCore/QDebug>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/render/materialsystem/technique.cpp, line 183, as _ZN10Qt3DRender6Render16TechniqueFunctorC1EPNS0_16AbstractRendererEPNS0_12NodeManagersE
namespace Qt3DRender::Render {
using namespace Qt3DCore;
inline TechniqueFunctor::TechniqueFunctor(AbstractRenderer *renderer, NodeManagers *manager)
    : m_manager(manager)
    , m_renderer(renderer)
{
}
}  // namespace Qt3DRender::Render

//  from ../qt3d/src/render/materialsystem/technique.cpp, line 189, as _ZNK10Qt3DRender6Render16TechniqueFunctor6createEN8Qt3DCore7QNodeIdE
namespace Qt3DRender::Render {
using namespace Qt3DCore;
inline QBackendNode *TechniqueFunctor::create(Qt3DCore::QNodeId id) const
{
    Technique *technique = m_manager->techniqueManager()->getOrCreateResource(id);
    technique->setNodeManager(m_manager);
    technique->setRenderer(m_renderer);
    return technique;
}
}  // namespace Qt3DRender::Render

//  from ../qt3d/src/render/materialsystem/technique.cpp, line 197, as _ZNK10Qt3DRender6Render16TechniqueFunctor3getEN8Qt3DCore7QNodeIdE
namespace Qt3DRender::Render {
using namespace Qt3DCore;
inline QBackendNode *TechniqueFunctor::get(QNodeId id) const
{
    return m_manager->techniqueManager()->lookupResource(id);
}
}  // namespace Qt3DRender::Render

//  from ../qt3d/src/render/materialsystem/technique.cpp, line 202, as _ZNK10Qt3DRender6Render16TechniqueFunctor7destroyEN8Qt3DCore7QNodeIdE
namespace Qt3DRender::Render {
using namespace Qt3DCore;
inline void TechniqueFunctor::destroy(QNodeId id) const
{
    m_manager->techniqueManager()->releaseResource(id);

}
}  // namespace Qt3DRender::Render
//  -----------------------------------------------------------------------

//  Qt3DRender::Render::TechniqueFunctor::TechniqueFunctor(AbstractRenderer
//      *renderer, NodeManagers *manager)
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::TechniqueFunctor *ritual_ZN10Qt3DRender6Render16TechniqueFunctorC1EPNS0_16AbstractRendererEPNS0_12NodeManagersE(
    Qt3DRender::Render::AbstractRenderer *renderer,
    Qt3DRender::Render::NodeManagers *manager) {
  return new Qt3DRender::Render::TechniqueFunctor(renderer, manager);
}

//  Qt3DCore::QBackendNode
//      *Qt3DRender::Render::TechniqueFunctor::create(Qt3DCore::QNodeId id)
//      const
extern "C" Q_DECL_EXPORT
Qt3DCore::QBackendNode *ritual_ZNK10Qt3DRender6Render16TechniqueFunctor6createEN8Qt3DCore7QNodeIdE(
    const Qt3DRender::Render::TechniqueFunctor *self,
    const Qt3DCore::QNodeId *id) {
  return self->create(*id);
}

//  Qt3DCore::QBackendNode
//      *Qt3DRender::Render::TechniqueFunctor::get(Qt3DCore::QNodeId id)
//      const
extern "C" Q_DECL_EXPORT
Qt3DCore::QBackendNode *ritual_ZNK10Qt3DRender6Render16TechniqueFunctor3getEN8Qt3DCore7QNodeIdE(
    const Qt3DRender::Render::TechniqueFunctor *self,
    const Qt3DCore::QNodeId *id) {
  return self->get(*id);
}

//  void Qt3DRender::Render::TechniqueFunctor::destroy(Qt3DCore::QNodeId id)
//      const
extern "C" Q_DECL_EXPORT
void ritual_ZNK10Qt3DRender6Render16TechniqueFunctor7destroyEN8Qt3DCore7QNodeIdE(
    const Qt3DRender::Render::TechniqueFunctor *self,
    const Qt3DCore::QNodeId *id) {
  self->destroy(*id);
}

//  Qt3DRender::Render::TechniqueFunctor::~TechniqueFunctor()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render16TechniqueFunctorD1Ev(
    Qt3DRender::Render::TechniqueFunctor *self) {
  delete self;
}

//  Qt3DCore::QBackendNode
//      *Qt3DRender::Render::TechniqueFunctor::create(Qt3DCore::QNodeId id)
//      const
extern "C" Q_DECL_EXPORT
Qt3DCore::QBackendNode *ritual_own_ZNK10Qt3DRender6Render16TechniqueFunctor6createEN8Qt3DCore7QNodeIdE(
    const Qt3DRender::Render::TechniqueFunctor *self,
    const Qt3DCore::QNodeId *id) {
  return self->Qt3DRender::Render::TechniqueFunctor::create(*id);
}

//  Qt3DCore::QBackendNode
//      *Qt3DRender::Render::TechniqueFunctor::get(Qt3DCore::QNodeId id)
//      const
extern "C" Q_DECL_EXPORT
Qt3DCore::QBackendNode *ritual_own_ZNK10Qt3DRender6Render16TechniqueFunctor3getEN8Qt3DCore7QNodeIdE(
    const Qt3DRender::Render::TechniqueFunctor *self,
    const Qt3DCore::QNodeId *id) {
  return self->Qt3DRender::Render::TechniqueFunctor::get(*id);
}

//  void Qt3DRender::Render::TechniqueFunctor::destroy(Qt3DCore::QNodeId id)
//      const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK10Qt3DRender6Render16TechniqueFunctor7destroyEN8Qt3DCore7QNodeIdE(
    const Qt3DRender::Render::TechniqueFunctor *self,
    const Qt3DCore::QNodeId *id) {
  self->Qt3DRender::Render::TechniqueFunctor::destroy(*id);
}
