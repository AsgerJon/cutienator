//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/texture_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/texture_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/qnodeid.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/private/texture_p.h>
#include <QtCore/QDebug>
#include <QtGui/QOpenGLFunctions>
#include <QtOpenGL/QOpenGLTexture>
#include <Qt3DRender/private/texture_p.h>
#include <Qt3DRender/private/qabstracttexture_p.h>
#include <Qt3DRender/private/managers_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/render/texture/texture.cpp, line 162, as _ZN10Qt3DRender6Render14TextureFunctorC1EPNS0_16AbstractRendererEPNS0_14TextureManagerE
namespace Qt3DRender::Render {
using namespace Qt3DCore;
inline TextureFunctor::TextureFunctor(AbstractRenderer *renderer,
                               TextureManager *textureNodeManager)
    : m_renderer(renderer)
    , m_textureNodeManager(textureNodeManager)
{
}
}  // namespace Qt3DRender::Render

//  from ../qt3d/src/render/texture/texture.cpp, line 169, as _ZNK10Qt3DRender6Render14TextureFunctor6createEN8Qt3DCore7QNodeIdE
namespace Qt3DRender::Render {
using namespace Qt3DCore;
inline Qt3DCore::QBackendNode *TextureFunctor::create(Qt3DCore::QNodeId id) const
{
    Texture *backend = m_textureNodeManager->getOrCreateResource(id);
    backend->setRenderer(m_renderer);
    // Remove id from cleanupList if for some reason we were in the dirty list of texture
    // (Can happen when a node destroyed is followed by a node created change
    // in the same loop, when changing parent for instance)
    m_textureNodeManager->removeTextureIdToCleanup(id);
    return backend;
}
}  // namespace Qt3DRender::Render

//  from ../qt3d/src/render/texture/texture.cpp, line 180, as _ZNK10Qt3DRender6Render14TextureFunctor3getEN8Qt3DCore7QNodeIdE
namespace Qt3DRender::Render {
using namespace Qt3DCore;
inline Qt3DCore::QBackendNode *TextureFunctor::get(Qt3DCore::QNodeId id) const
{
    return m_textureNodeManager->lookupResource(id);
}
}  // namespace Qt3DRender::Render

//  from ../qt3d/src/render/texture/texture.cpp, line 185, as _ZNK10Qt3DRender6Render14TextureFunctor7destroyEN8Qt3DCore7QNodeIdE
namespace Qt3DRender::Render {
using namespace Qt3DCore;
inline void TextureFunctor::destroy(Qt3DCore::QNodeId id) const
{
    m_textureNodeManager->addTextureIdToCleanup(id);
    // We add ourselves to the dirty list to tell the shared texture managers
    // in the renderer that this texture has been destroyed
    m_textureNodeManager->releaseResource(id);
}
}  // namespace Qt3DRender::Render
//  -----------------------------------------------------------------------

//  Qt3DRender::Render::TextureFunctor::TextureFunctor(AbstractRenderer
//      *renderer, TextureManager *textureNodeManager)
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::TextureFunctor *ritual_ZN10Qt3DRender6Render14TextureFunctorC1EPNS0_16AbstractRendererEPNS0_14TextureManagerE(
    Qt3DRender::Render::AbstractRenderer *renderer,
    Qt3DRender::Render::TextureManager *textureNodeManager) {
  return new Qt3DRender::Render::TextureFunctor(
      renderer,
      textureNodeManager);
}

//  Qt3DCore::QBackendNode
//      *Qt3DRender::Render::TextureFunctor::create(Qt3DCore::QNodeId id)
//      const
extern "C" Q_DECL_EXPORT
Qt3DCore::QBackendNode *ritual_ZNK10Qt3DRender6Render14TextureFunctor6createEN8Qt3DCore7QNodeIdE(
    const Qt3DRender::Render::TextureFunctor *self,
    const Qt3DCore::QNodeId *id) {
  return self->create(*id);
}

//  Qt3DCore::QBackendNode
//      *Qt3DRender::Render::TextureFunctor::get(Qt3DCore::QNodeId id) const
extern "C" Q_DECL_EXPORT
Qt3DCore::QBackendNode *ritual_ZNK10Qt3DRender6Render14TextureFunctor3getEN8Qt3DCore7QNodeIdE(
    const Qt3DRender::Render::TextureFunctor *self,
    const Qt3DCore::QNodeId *id) {
  return self->get(*id);
}

//  void Qt3DRender::Render::TextureFunctor::destroy(Qt3DCore::QNodeId id)
//      const
extern "C" Q_DECL_EXPORT
void ritual_ZNK10Qt3DRender6Render14TextureFunctor7destroyEN8Qt3DCore7QNodeIdE(
    const Qt3DRender::Render::TextureFunctor *self,
    const Qt3DCore::QNodeId *id) {
  self->destroy(*id);
}

//  Qt3DRender::Render::TextureFunctor::~TextureFunctor()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render14TextureFunctorD1Ev(
    Qt3DRender::Render::TextureFunctor *self) {
  delete self;
}
