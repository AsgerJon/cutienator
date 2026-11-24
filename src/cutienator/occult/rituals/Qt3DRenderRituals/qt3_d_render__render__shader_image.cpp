//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/shaderimage_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/shaderimage_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/qnodeid.h>

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
