//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DQuickScene3D/6.12.0/Qt3DQuickScene3D/private/scene3dsgmaterial_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <Qt3DQuickScene3D/Qt3DQuickScene3D>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DQuickScene3D/6.12.0/Qt3DQuickScene3D/private/scene3dsgmaterial_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DQuickScene3D/private/scene3dsgmaterialshader_p.h>
#include <QtGui/qopenglcontext.h>
#include <QtGui/qopenglfunctions.h>
#include <QtGui/qsurfaceformat.h>
#include <Qt3DQuickScene3D/private/scene3dsgmaterial_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/quick3d/quick3dscene3d/scene3dsgmaterialshader.cpp, line 39, as _ZN10Qt3DRender23Scene3DSGMaterialShaderC1Ev
namespace Qt3DRender {
inline Scene3DSGMaterialShader::Scene3DSGMaterialShader()
    : QSGMaterialShader()
{
    // Generated with qsb, we target all GL version Qt3D can handle
    // qsb -b --glsl "460,450,440,430,420,410,400,330,150,130,120,320 es,300 es,100 es" --hlsl 50 --msl 12 -o scene3dmaterial.vert.qsb scene3dmaterial.vert
    // qsb --glsl "460,450,440,430,420,410,400,330,150,130,120,320 es,300 es,100 es" --hlsl 50 --msl 12 -o scene3dmaterial.frag.qsb scene3dmaterial.frag
    setShaderFileName(VertexStage, QLatin1String(":/shaders/scene3dmaterial.vert.qsb"));
    setShaderFileName(FragmentStage, QLatin1String(":/shaders/scene3dmaterial.frag.qsb"));
}
}  // namespace Qt3DRender
//  -----------------------------------------------------------------------

//  void Qt3DRender::Scene3DSGMaterial::setTexture(QSGTexture *texture)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender17Scene3DSGMaterial10setTextureEP10QSGTexture(
    Qt3DRender::Scene3DSGMaterial *self,
    QSGTexture *texture) {
  self->setTexture(texture);
}

//  QSGTexture *Qt3DRender::Scene3DSGMaterial::texture() const
extern "C" Q_DECL_EXPORT
QSGTexture *ritual_ZNK10Qt3DRender17Scene3DSGMaterial7textureEv(
    const Qt3DRender::Scene3DSGMaterial *self) {
  return self->texture();
}

//  void Qt3DRender::Scene3DSGMaterial::show()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender17Scene3DSGMaterial4showEv(
    Qt3DRender::Scene3DSGMaterial *self) {
  self->show();
}

//  bool Qt3DRender::Scene3DSGMaterial::visible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DRender17Scene3DSGMaterial7visibleEv(
    const Qt3DRender::Scene3DSGMaterial *self) {
  return self->visible();
}
