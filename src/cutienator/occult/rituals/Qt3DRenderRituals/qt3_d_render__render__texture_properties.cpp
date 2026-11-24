//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/texture_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/texture_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  bool Qt3DRender::Render::TextureProperties::operator==(const
//      TextureProperties &o) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DRender6Render17TexturePropertieseqERKS1_(
    const Qt3DRender::Render::TextureProperties *self,
    const Qt3DRender::Render::TextureProperties *o) {
  return self->operator==(*o);
}

//  bool Qt3DRender::Render::TextureProperties::operator!=(const
//      TextureProperties &o) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DRender6Render17TexturePropertiesneERKS1_(
    const Qt3DRender::Render::TextureProperties *self,
    const Qt3DRender::Render::TextureProperties *o) {
  return self->operator!=(*o);
}

//  Qt3DRender::Render::TextureProperties::~TextureProperties()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render17TexturePropertiesD1Ev(
    Qt3DRender::Render::TextureProperties *self) {
  delete self;
}
