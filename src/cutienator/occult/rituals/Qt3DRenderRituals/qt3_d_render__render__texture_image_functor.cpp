//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/textureimage_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/textureimage_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/qnodeid.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/private/textureimage_p.h>
#include <Qt3DRender/qtextureimage.h>
#include <Qt3DRender/private/managers_p.h>
#include <Qt3DRender/private/qabstracttextureimage_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/render/texture/textureimage.cpp, line 78, as _ZN10Qt3DRender6Render19TextureImageFunctorC1EPNS0_16AbstractRendererEPNS0_19TextureImageManagerE
namespace Qt3DRender::Render {
using namespace Qt3DCore;
inline TextureImageFunctor::TextureImageFunctor(AbstractRenderer *renderer,
                                         TextureImageManager *textureImageManager)
    : m_renderer(renderer)
    , m_textureImageManager(textureImageManager)
{
}
}  // namespace Qt3DRender::Render

//  from ../qt3d/src/render/texture/textureimage.cpp, line 85, as _ZNK10Qt3DRender6Render19TextureImageFunctor6createEN8Qt3DCore7QNodeIdE
namespace Qt3DRender::Render {
using namespace Qt3DCore;
inline Qt3DCore::QBackendNode *TextureImageFunctor::create(Qt3DCore::QNodeId id) const
{
    TextureImage *backend = m_textureImageManager->getOrCreateResource(id);
    backend->setRenderer(m_renderer);
    return backend;
}
}  // namespace Qt3DRender::Render

//  from ../qt3d/src/render/texture/textureimage.cpp, line 92, as _ZNK10Qt3DRender6Render19TextureImageFunctor3getEN8Qt3DCore7QNodeIdE
namespace Qt3DRender::Render {
using namespace Qt3DCore;
inline Qt3DCore::QBackendNode *TextureImageFunctor::get(Qt3DCore::QNodeId id) const
{
    return m_textureImageManager->lookupResource(id);
}
}  // namespace Qt3DRender::Render

//  from ../qt3d/src/render/texture/textureimage.cpp, line 97, as _ZNK10Qt3DRender6Render19TextureImageFunctor7destroyEN8Qt3DCore7QNodeIdE
namespace Qt3DRender::Render {
using namespace Qt3DCore;
inline void TextureImageFunctor::destroy(Qt3DCore::QNodeId id) const
{
    m_textureImageManager->releaseResource(id);
}
}  // namespace Qt3DRender::Render
//  -----------------------------------------------------------------------

//  Qt3DRender::Render::TextureImageFunctor::TextureImageFunctor(AbstractRend
//      erer *renderer, TextureImageManager *textureImageManager)
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::TextureImageFunctor *ritual_ZN10Qt3DRender6Render19TextureImageFunctorC1EPNS0_16AbstractRendererEPNS0_19TextureImageManagerE(
    Qt3DRender::Render::AbstractRenderer *renderer,
    Qt3DRender::Render::TextureImageManager *textureImageManager) {
  return new Qt3DRender::Render::TextureImageFunctor(
      renderer,
      textureImageManager);
}

//  Qt3DCore::QBackendNode
//      *Qt3DRender::Render::TextureImageFunctor::create(Qt3DCore::QNodeId
//      id) const
extern "C" Q_DECL_EXPORT
Qt3DCore::QBackendNode *ritual_ZNK10Qt3DRender6Render19TextureImageFunctor6createEN8Qt3DCore7QNodeIdE(
    const Qt3DRender::Render::TextureImageFunctor *self,
    const Qt3DCore::QNodeId *id) {
  return self->create(*id);
}

//  Qt3DCore::QBackendNode
//      *Qt3DRender::Render::TextureImageFunctor::get(Qt3DCore::QNodeId id)
//      const
extern "C" Q_DECL_EXPORT
Qt3DCore::QBackendNode *ritual_ZNK10Qt3DRender6Render19TextureImageFunctor3getEN8Qt3DCore7QNodeIdE(
    const Qt3DRender::Render::TextureImageFunctor *self,
    const Qt3DCore::QNodeId *id) {
  return self->get(*id);
}

//  void Qt3DRender::Render::TextureImageFunctor::destroy(Qt3DCore::QNodeId
//      id) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK10Qt3DRender6Render19TextureImageFunctor7destroyEN8Qt3DCore7QNodeIdE(
    const Qt3DRender::Render::TextureImageFunctor *self,
    const Qt3DCore::QNodeId *id) {
  self->destroy(*id);
}

//  Qt3DRender::Render::TextureImageFunctor::~TextureImageFunctor()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render19TextureImageFunctorD1Ev(
    Qt3DRender::Render::TextureImageFunctor *self) {
  delete self;
}
