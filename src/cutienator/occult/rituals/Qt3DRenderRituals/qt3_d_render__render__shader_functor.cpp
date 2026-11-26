//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/shader_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/shader_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/qnodeid.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/private/shader_p.h>
#include <Qt3DRender/private/renderlogging_p.h>
#include <QtCore/QFile>
#include <QtGui/QOpenGLContext>
#include <QtOpenGL/QOpenGLShaderProgram>
#include <QtCore/QMutexLocker>
#include <Qt3DRender/qshaderprogram.h>
#include <Qt3DRender/private/attachmentpack_p.h>
#include <Qt3DRender/private/qshaderprogram_p.h>
#include <Qt3DRender/private/stringtoint_p.h>
#include <Qt3DRender/private/managers_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/render/materialsystem/shader.cpp, line 154, as _ZN10Qt3DRender6Render13ShaderFunctorC1EPNS0_16AbstractRendererEPNS0_13ShaderManagerE
namespace Qt3DRender::Render {
using namespace Qt3DCore;
inline ShaderFunctor::ShaderFunctor(AbstractRenderer *renderer, ShaderManager *manager)
    : m_renderer(renderer)
    , m_shaderManager(manager)
{
}
}  // namespace Qt3DRender::Render

//  from ../qt3d/src/render/materialsystem/shader.cpp, line 160, as _ZNK10Qt3DRender6Render13ShaderFunctor6createEN8Qt3DCore7QNodeIdE
namespace Qt3DRender::Render {
using namespace Qt3DCore;
inline QBackendNode *ShaderFunctor::create(QNodeId id) const
{
    Shader *backend = m_shaderManager->getOrCreateResource(id);
    // Remove from the list of ids to destroy in case we were added to it
    m_shaderManager->removeShaderIdFromIdsToCleanup(id);
    backend->setRenderer(m_renderer);
    return backend;
}
}  // namespace Qt3DRender::Render

//  from ../qt3d/src/render/materialsystem/shader.cpp, line 169, as _ZNK10Qt3DRender6Render13ShaderFunctor3getEN8Qt3DCore7QNodeIdE
namespace Qt3DRender::Render {
using namespace Qt3DCore;
inline QBackendNode *ShaderFunctor::get(QNodeId id) const
{
    // If we are marked for destruction, return nullptr so that
    // if we were to be recreated, create would be called again
    if (m_shaderManager->hasShaderIdToCleanup(id))
        return nullptr;
    return m_shaderManager->lookupResource(id);
}
}  // namespace Qt3DRender::Render

//  from ../qt3d/src/render/materialsystem/shader.cpp, line 178, as _ZNK10Qt3DRender6Render13ShaderFunctor7destroyEN8Qt3DCore7QNodeIdE
namespace Qt3DRender::Render {
using namespace Qt3DCore;
inline void ShaderFunctor::destroy(QNodeId id) const
{
    // We only add ourselves to the dirty list
    // The actual removal needs to be performed after we have
    // destroyed the associated APIShader in the RenderThread
    if (m_shaderManager->lookupResource(id))
        m_shaderManager->addShaderIdToCleanup(id);
}
}  // namespace Qt3DRender::Render
//  -----------------------------------------------------------------------

//  Qt3DRender::Render::ShaderFunctor::ShaderFunctor(AbstractRenderer
//      *renderer, ShaderManager *manager)
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::ShaderFunctor *ritual_ZN10Qt3DRender6Render13ShaderFunctorC1EPNS0_16AbstractRendererEPNS0_13ShaderManagerE(
    Qt3DRender::Render::AbstractRenderer *renderer,
    Qt3DRender::Render::ShaderManager *manager) {
  return new Qt3DRender::Render::ShaderFunctor(renderer, manager);
}

//  Qt3DCore::QBackendNode
//      *Qt3DRender::Render::ShaderFunctor::create(Qt3DCore::QNodeId id)
//      const
extern "C" Q_DECL_EXPORT
Qt3DCore::QBackendNode *ritual_ZNK10Qt3DRender6Render13ShaderFunctor6createEN8Qt3DCore7QNodeIdE(
    const Qt3DRender::Render::ShaderFunctor *self,
    const Qt3DCore::QNodeId *id) {
  return self->create(*id);
}

//  Qt3DCore::QBackendNode
//      *Qt3DRender::Render::ShaderFunctor::get(Qt3DCore::QNodeId id) const
extern "C" Q_DECL_EXPORT
Qt3DCore::QBackendNode *ritual_ZNK10Qt3DRender6Render13ShaderFunctor3getEN8Qt3DCore7QNodeIdE(
    const Qt3DRender::Render::ShaderFunctor *self,
    const Qt3DCore::QNodeId *id) {
  return self->get(*id);
}

//  void Qt3DRender::Render::ShaderFunctor::destroy(Qt3DCore::QNodeId id)
//      const
extern "C" Q_DECL_EXPORT
void ritual_ZNK10Qt3DRender6Render13ShaderFunctor7destroyEN8Qt3DCore7QNodeIdE(
    const Qt3DRender::Render::ShaderFunctor *self,
    const Qt3DCore::QNodeId *id) {
  self->destroy(*id);
}

//  Qt3DRender::Render::ShaderFunctor::~ShaderFunctor()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render13ShaderFunctorD1Ev(
    Qt3DRender::Render::ShaderFunctor *self) {
  delete self;
}
