//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/rendersettings_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/rendersettings_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/qnodeid.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/private/rendersettings_p.h>
#include <Qt3DRender/QFrameGraphNode>
#include <Qt3DRender/private/abstractrenderer_p.h>
#include <Qt3DRender/private/qrendersettings_p.h>
#include <Qt3DRender/private/qrendercapabilities_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/render/backend/rendersettings.cpp, line 72, as _ZN10Qt3DRender6Render21RenderSettingsFunctorC1EPNS0_16AbstractRendererE
namespace Qt3DRender::Render {
using namespace Qt3DCore;
inline RenderSettingsFunctor::RenderSettingsFunctor(AbstractRenderer *renderer)
    : m_renderer(renderer)
{
}
}  // namespace Qt3DRender::Render

//  from ../qt3d/src/render/backend/rendersettings.cpp, line 77, as _ZNK10Qt3DRender6Render21RenderSettingsFunctor6createEN8Qt3DCore7QNodeIdE
namespace Qt3DRender::Render {
using namespace Qt3DCore;
inline Qt3DCore::QBackendNode *RenderSettingsFunctor::create(Qt3DCore::QNodeId) const
{
    if (m_renderer->settings() != nullptr) {
        qWarning() << "Renderer settings already exists";
        return nullptr;
    }

    RenderSettings *settings = new RenderSettings;
    settings->setRenderer(m_renderer);
    m_renderer->setSettings(settings);
    return settings;
}
}  // namespace Qt3DRender::Render

//  from ../qt3d/src/render/backend/rendersettings.cpp, line 90, as _ZNK10Qt3DRender6Render21RenderSettingsFunctor3getEN8Qt3DCore7QNodeIdE
namespace Qt3DRender::Render {
using namespace Qt3DCore;
inline Qt3DCore::QBackendNode *RenderSettingsFunctor::get(Qt3DCore::QNodeId id) const
{
    Q_UNUSED(id);
    return m_renderer->settings();
}
}  // namespace Qt3DRender::Render

//  from ../qt3d/src/render/backend/rendersettings.cpp, line 96, as _ZNK10Qt3DRender6Render21RenderSettingsFunctor7destroyEN8Qt3DCore7QNodeIdE
namespace Qt3DRender::Render {
using namespace Qt3DCore;
inline void RenderSettingsFunctor::destroy(Qt3DCore::QNodeId id) const
{
    Q_UNUSED(id);
    // Deletes the old settings object
    auto settings = m_renderer->settings();
    if (settings && settings->peerId() == id) {
        m_renderer->setSettings(nullptr);
        delete settings;
    }
}
}  // namespace Qt3DRender::Render
//  -----------------------------------------------------------------------

//  Qt3DRender::Render::RenderSettingsFunctor::RenderSettingsFunctor(Abstract
//      Renderer *renderer)
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::RenderSettingsFunctor *ritual_ZN10Qt3DRender6Render21RenderSettingsFunctorC1EPNS0_16AbstractRendererE(
    Qt3DRender::Render::AbstractRenderer *renderer) {
  return new Qt3DRender::Render::RenderSettingsFunctor(renderer);
}

//  Qt3DCore::QBackendNode
//      *Qt3DRender::Render::RenderSettingsFunctor::create(Qt3DCore::QNodeId
//      id) const
extern "C" Q_DECL_EXPORT
Qt3DCore::QBackendNode *ritual_ZNK10Qt3DRender6Render21RenderSettingsFunctor6createEN8Qt3DCore7QNodeIdE(
    const Qt3DRender::Render::RenderSettingsFunctor *self,
    const Qt3DCore::QNodeId *id) {
  return self->create(*id);
}

//  Qt3DCore::QBackendNode
//      *Qt3DRender::Render::RenderSettingsFunctor::get(Qt3DCore::QNodeId id)
//      const
extern "C" Q_DECL_EXPORT
Qt3DCore::QBackendNode *ritual_ZNK10Qt3DRender6Render21RenderSettingsFunctor3getEN8Qt3DCore7QNodeIdE(
    const Qt3DRender::Render::RenderSettingsFunctor *self,
    const Qt3DCore::QNodeId *id) {
  return self->get(*id);
}

//  void Qt3DRender::Render::RenderSettingsFunctor::destroy(Qt3DCore::QNodeId
//      id) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK10Qt3DRender6Render21RenderSettingsFunctor7destroyEN8Qt3DCore7QNodeIdE(
    const Qt3DRender::Render::RenderSettingsFunctor *self,
    const Qt3DCore::QNodeId *id) {
  self->destroy(*id);
}

//  Qt3DRender::Render::RenderSettingsFunctor::~RenderSettingsFunctor()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render21RenderSettingsFunctorD1Ev(
    Qt3DRender::Render::RenderSettingsFunctor *self) {
  delete self;
}

//  Qt3DCore::QBackendNode
//      *Qt3DRender::Render::RenderSettingsFunctor::create(Qt3DCore::QNodeId
//      id) const
extern "C" Q_DECL_EXPORT
Qt3DCore::QBackendNode *ritual_own_ZNK10Qt3DRender6Render21RenderSettingsFunctor6createEN8Qt3DCore7QNodeIdE(
    const Qt3DRender::Render::RenderSettingsFunctor *self,
    const Qt3DCore::QNodeId *id) {
  return self->Qt3DRender::Render::RenderSettingsFunctor::create(*id);
}

//  Qt3DCore::QBackendNode
//      *Qt3DRender::Render::RenderSettingsFunctor::get(Qt3DCore::QNodeId id)
//      const
extern "C" Q_DECL_EXPORT
Qt3DCore::QBackendNode *ritual_own_ZNK10Qt3DRender6Render21RenderSettingsFunctor3getEN8Qt3DCore7QNodeIdE(
    const Qt3DRender::Render::RenderSettingsFunctor *self,
    const Qt3DCore::QNodeId *id) {
  return self->Qt3DRender::Render::RenderSettingsFunctor::get(*id);
}

//  void Qt3DRender::Render::RenderSettingsFunctor::destroy(Qt3DCore::QNodeId
//      id) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK10Qt3DRender6Render21RenderSettingsFunctor7destroyEN8Qt3DCore7QNodeIdE(
    const Qt3DRender::Render::RenderSettingsFunctor *self,
    const Qt3DCore::QNodeId *id) {
  self->Qt3DRender::Render::RenderSettingsFunctor::destroy(*id);
}
