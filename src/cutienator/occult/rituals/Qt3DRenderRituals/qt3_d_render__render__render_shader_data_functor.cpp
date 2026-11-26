//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/shaderdata_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/shaderdata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/qnodeid.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/private/shaderdata_p.h>
#include <Qt3DRender/qshaderdata.h>
#include <Qt3DRender/private/qshaderdata_p.h>
#include <QtCore/QMetaProperty>
#include <QtCore/QMetaObject>
#include <Qt3DCore/private/qbackendnode_p.h>
#include <Qt3DRender/private/managers_p.h>
#include <Qt3DRender/private/nodemanagers_p.h>
#include <Qt3DRender/private/stringtoint_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/render/materialsystem/shaderdata.cpp, line 228, as _ZN10Qt3DRender6Render23RenderShaderDataFunctorC1EPNS0_16AbstractRendererEPNS0_12NodeManagersE
namespace Qt3DRender::Render {
using namespace Qt3DCore;
inline RenderShaderDataFunctor::RenderShaderDataFunctor(AbstractRenderer *renderer, NodeManagers *managers)
    : m_managers(managers)
    , m_renderer(renderer)
{
}
}  // namespace Qt3DRender::Render

//  from ../qt3d/src/render/materialsystem/shaderdata.cpp, line 234, as _ZNK10Qt3DRender6Render23RenderShaderDataFunctor6createEN8Qt3DCore7QNodeIdE
namespace Qt3DRender::Render {
using namespace Qt3DCore;
inline Qt3DCore::QBackendNode *RenderShaderDataFunctor::create(Qt3DCore::QNodeId id) const
{
    ShaderData *backend = m_managers->shaderDataManager()->getOrCreateResource(id);
    backend->setManagers(m_managers);
    backend->setRenderer(m_renderer);
    return backend;
}
}  // namespace Qt3DRender::Render

//  from ../qt3d/src/render/materialsystem/shaderdata.cpp, line 242, as _ZNK10Qt3DRender6Render23RenderShaderDataFunctor3getEN8Qt3DCore7QNodeIdE
namespace Qt3DRender::Render {
using namespace Qt3DCore;
inline Qt3DCore::QBackendNode *RenderShaderDataFunctor::get(Qt3DCore::QNodeId id) const
{
    return m_managers->shaderDataManager()->lookupResource(id);
}
}  // namespace Qt3DRender::Render

//  from ../qt3d/src/render/materialsystem/shaderdata.cpp, line 247, as _ZNK10Qt3DRender6Render23RenderShaderDataFunctor7destroyEN8Qt3DCore7QNodeIdE
namespace Qt3DRender::Render {
using namespace Qt3DCore;
inline void RenderShaderDataFunctor::destroy(Qt3DCore::QNodeId id) const
{
    m_managers->shaderDataManager()->releaseResource(id);
}
}  // namespace Qt3DRender::Render
//  -----------------------------------------------------------------------

//  Qt3DRender::Render::RenderShaderDataFunctor::RenderShaderDataFunctor(Abst
//      ractRenderer *renderer, NodeManagers *managers)
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::RenderShaderDataFunctor *ritual_ZN10Qt3DRender6Render23RenderShaderDataFunctorC1EPNS0_16AbstractRendererEPNS0_12NodeManagersE(
    Qt3DRender::Render::AbstractRenderer *renderer,
    Qt3DRender::Render::NodeManagers *managers) {
  return new Qt3DRender::Render::RenderShaderDataFunctor(renderer, managers);
}

//  Qt3DCore::QBackendNode
//      *Qt3DRender::Render::RenderShaderDataFunctor::create(Qt3DCore::QNodeI
//      d id) const
extern "C" Q_DECL_EXPORT
Qt3DCore::QBackendNode *ritual_ZNK10Qt3DRender6Render23RenderShaderDataFunctor6createEN8Qt3DCore7QNodeIdE(
    const Qt3DRender::Render::RenderShaderDataFunctor *self,
    const Qt3DCore::QNodeId *id) {
  return self->create(*id);
}

//  Qt3DCore::QBackendNode
//      *Qt3DRender::Render::RenderShaderDataFunctor::get(Qt3DCore::QNodeId
//      id) const
extern "C" Q_DECL_EXPORT
Qt3DCore::QBackendNode *ritual_ZNK10Qt3DRender6Render23RenderShaderDataFunctor3getEN8Qt3DCore7QNodeIdE(
    const Qt3DRender::Render::RenderShaderDataFunctor *self,
    const Qt3DCore::QNodeId *id) {
  return self->get(*id);
}

//  void
//      Qt3DRender::Render::RenderShaderDataFunctor::destroy(Qt3DCore::QNodeI
//      d id) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK10Qt3DRender6Render23RenderShaderDataFunctor7destroyEN8Qt3DCore7QNodeIdE(
    const Qt3DRender::Render::RenderShaderDataFunctor *self,
    const Qt3DCore::QNodeId *id) {
  self->destroy(*id);
}

//  Qt3DRender::Render::RenderShaderDataFunctor::~RenderShaderDataFunctor()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render23RenderShaderDataFunctorD1Ev(
    Qt3DRender::Render::RenderShaderDataFunctor *self) {
  delete self;
}
