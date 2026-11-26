//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/shaderimage_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/shaderimage_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/qnodeid.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/private/shaderimage_p.h>
#include <Qt3DRender/private/qshaderimage_p.h>
#include <Qt3DRender/qabstracttexture.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/render/materialsystem/shaderimage.cpp, line 15, as _ZN10Qt3DRender6Render11ShaderImageC1Ev
namespace Qt3DRender::Render {
inline ShaderImage::ShaderImage()
    : BackendNode(BackendNode::ReadOnly)
    , m_textureId()
    , m_mipLevel(0)
    , m_layer(0)
    , m_layered(false)
    , m_access(QShaderImage::ReadWrite)
    , m_format(QShaderImage::NoFormat)
{
}
}  // namespace Qt3DRender::Render

//  from ../qt3d/src/render/materialsystem/shaderimage.cpp, line 26, as _ZN10Qt3DRender6Render11ShaderImage7cleanupEv
namespace Qt3DRender::Render {
inline void ShaderImage::cleanup()
{
    QBackendNode::setEnabled(false);
    m_textureId = Qt3DCore::QNodeId();
    m_mipLevel = 0;
    m_layer = 0;
    m_layered = false;
    m_access = QShaderImage::ReadWrite;
    m_format = QShaderImage::NoFormat;
}
}  // namespace Qt3DRender::Render

//  from ../qt3d/src/render/materialsystem/shaderimage.cpp, line 37, as _ZN10Qt3DRender6Render11ShaderImage16syncFromFrontEndEPKN8Qt3DCore5QNodeEb
namespace Qt3DRender::Render {
inline void ShaderImage::syncFromFrontEnd(const Qt3DCore::QNode *frontEnd, bool firstTime)
{
    const QShaderImage *node = qobject_cast<const QShaderImage *>(frontEnd);
    if (!node)
        return;

    BackendNode::syncFromFrontEnd(frontEnd, firstTime);

    const Qt3DCore::QNodeId textureNodeId = Qt3DCore::qIdForNode(node->texture());
    if (textureNodeId != m_textureId) {
        m_textureId = textureNodeId;
        markDirty(AbstractRenderer::ParameterDirty);
    }

    if (node->mipLevel() != m_mipLevel) {
        m_mipLevel = node->mipLevel();
        markDirty(AbstractRenderer::ParameterDirty);
    }

    if (node->layer() != m_layer) {
        m_layer = node->layer();
        markDirty(AbstractRenderer::ParameterDirty);
    }

    if (node->layered() != m_layered) {
        m_layered = node->layered();
        markDirty(AbstractRenderer::ParameterDirty);
    }

    if (node->format() != m_format) {
        m_format = node->format();
        markDirty(AbstractRenderer::ParameterDirty);
    }
    if (node->access() != m_access) {
        m_access = node->access();
        markDirty(AbstractRenderer::ParameterDirty);
    }

}
}  // namespace Qt3DRender::Render
//  -----------------------------------------------------------------------

//  Qt3DRender::Render::ShaderImage::ShaderImage()
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::ShaderImage *ritual_ZN10Qt3DRender6Render11ShaderImageC1Ev() {
  return new Qt3DRender::Render::ShaderImage();
}

//  void Qt3DRender::Render::ShaderImage::cleanup()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render11ShaderImage7cleanupEv(
    Qt3DRender::Render::ShaderImage *self) {
  self->cleanup();
}

//  void Qt3DRender::Render::ShaderImage::syncFromFrontEnd(const
//      Qt3DCore::QNode *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render11ShaderImage16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DRender::Render::ShaderImage *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->syncFromFrontEnd(frontEnd, firstTime);
}

//  Qt3DCore::QNodeId Qt3DRender::Render::ShaderImage::textureId() const
extern "C" Q_DECL_EXPORT
Qt3DCore::QNodeId *ritual_ZNK10Qt3DRender6Render11ShaderImage9textureIdEv(
    const Qt3DRender::Render::ShaderImage *self) {
  return new Qt3DCore::QNodeId(self->textureId());
}

//  int Qt3DRender::Render::ShaderImage::mipLevel() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DRender6Render11ShaderImage8mipLevelEv(
    const Qt3DRender::Render::ShaderImage *self) {
  return self->mipLevel();
}

//  int Qt3DRender::Render::ShaderImage::layer() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DRender6Render11ShaderImage5layerEv(
    const Qt3DRender::Render::ShaderImage *self) {
  return self->layer();
}

//  bool Qt3DRender::Render::ShaderImage::layered() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DRender6Render11ShaderImage7layeredEv(
    const Qt3DRender::Render::ShaderImage *self) {
  return self->layered();
}

//  QShaderImage::Access Qt3DRender::Render::ShaderImage::access() const
extern "C" Q_DECL_EXPORT
Qt3DRender::QShaderImage::Access ritual_ZNK10Qt3DRender6Render11ShaderImage6accessEv(
    const Qt3DRender::Render::ShaderImage *self) {
  return self->access();
}

//  QShaderImage::ImageFormat Qt3DRender::Render::ShaderImage::format() const
extern "C" Q_DECL_EXPORT
Qt3DRender::QShaderImage::ImageFormat ritual_ZNK10Qt3DRender6Render11ShaderImage6formatEv(
    const Qt3DRender::Render::ShaderImage *self) {
  return self->format();
}

//  void Qt3DRender::Render::ShaderImage::syncFromFrontEnd(const
//      Qt3DCore::QNode *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10Qt3DRender6Render11ShaderImage16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DRender::Render::ShaderImage *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->Qt3DRender::Render::ShaderImage::syncFromFrontEnd(
      frontEnd,
      firstTime);
}
