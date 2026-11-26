//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgtexturematerial_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgtexturematerial_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QSGOpaqueTextureMaterialRhiShader::QSGOpaqueTextureMaterialRhiShader(int
//      viewCount)
extern "C" Q_DECL_EXPORT
QSGOpaqueTextureMaterialRhiShader *ritual_ZN33QSGOpaqueTextureMaterialRhiShaderC1Ei(
    int viewCount) {
  return new QSGOpaqueTextureMaterialRhiShader(viewCount);
}

//  bool QSGOpaqueTextureMaterialRhiShader::updateUniformData(RenderState
//      &state, QSGMaterial *newMaterial, QSGMaterial *oldMaterial)
extern "C" Q_DECL_EXPORT
bool ritual_ZN33QSGOpaqueTextureMaterialRhiShader17updateUniformDataERN17QSGMaterialShader11RenderStateEP11QSGMaterialS4_(
    QSGOpaqueTextureMaterialRhiShader *self,
    QSGMaterialShader::RenderState *state,
    QSGMaterial *newMaterial,
    QSGMaterial *oldMaterial) {
  return self->updateUniformData(*state, newMaterial, oldMaterial);
}

//  void QSGOpaqueTextureMaterialRhiShader::updateSampledImage(RenderState
//      &state, int binding, QSGTexture **texture, QSGMaterial *newMaterial,
//      QSGMaterial *oldMaterial)
extern "C" Q_DECL_EXPORT
void ritual_ZN33QSGOpaqueTextureMaterialRhiShader18updateSampledImageERN17QSGMaterialShader11RenderStateEiPP10QSGTextureP11QSGMaterialS7_(
    QSGOpaqueTextureMaterialRhiShader *self,
    QSGMaterialShader::RenderState *state,
    int binding,
    QSGTexture **texture,
    QSGMaterial *newMaterial,
    QSGMaterial *oldMaterial) {
  self->updateSampledImage(
      *state,
      binding,
      texture,
      newMaterial,
      oldMaterial);
}
