//  Written by dev_tooling.RitualGenerator from the records of Qt3DQuickScene
//  3D/6.12.0/Qt3DQuickScene3D/private/scene3dsgmaterialshader_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <Qt3DQuickScene3D/Qt3DQuickScene3D>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DQuickScene3D/6.12.0/Qt3DQuickScene3D/private/scene3dsgmaterialshader_p.h>
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

//  from ../qt3d/src/quick3d/quick3dscene3d/scene3dsgmaterialshader.cpp, line 16, as local:scene3dsgmaterialshader.cpp:isPowerOfTwo
namespace {
inline bool isPowerOfTwo(int x)
{
    // Assumption: x >= 1
    return x == (x & -x);
}
}  // namespace

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

//  from ../qt3d/src/quick3d/quick3dscene3d/scene3dsgmaterialshader.cpp, line 49, as _ZN10Qt3DRender23Scene3DSGMaterialShader17updateUniformDataERN17QSGMaterialShader11RenderStateEP11QSGMaterialS5_
namespace Qt3DRender {
inline bool Scene3DSGMaterialShader::updateUniformData(QSGMaterialShader::RenderState &state,
                                                QSGMaterial *newMaterial,
                                                QSGMaterial *oldMaterial)
{
    //    layout(std140, binding = 0) uniform buf {
    //        mat4 qt_Matrix;   // offset 0, sizeof(float) * 16
    //        float qt_Opacity; // offset sizeof(float) * 16, sizeof(float)
    //        bool visible;     // offset sizeof(float) * 17, sizeof(float)
    //    };

    QByteArray *buf = state.uniformData();
    Q_ASSERT(buf->size() >= int(18 * sizeof(float)));
    Scene3DSGMaterial *tx = static_cast<Scene3DSGMaterial *>(newMaterial);
    Scene3DSGMaterial *oldTx = static_cast<Scene3DSGMaterial *>(oldMaterial);

    bool updateMade = false;

    if (state.isMatrixDirty()) {
        const QMatrix4x4 &m = state.combinedMatrix();
        memcpy(buf->data(), m.constData(), 16 * sizeof(float));
        updateMade = true;
    }

    if (state.isOpacityDirty()) {
        const float opacity = state.opacity();
        memcpy(buf->data() + 16 * sizeof(float), &opacity, sizeof(float));
        updateMade = true;
    }

    if (oldTx == nullptr || oldTx->visible() != tx->visible()) {
        const float value = tx->visible() ? 1.0f : -1.0f;
        memcpy(buf->data() + 17 * sizeof(float), &value, sizeof(float));
        updateMade = true;
    }

    return updateMade;
}
}  // namespace Qt3DRender

//  from ../qt3d/src/quick3d/quick3dscene3d/scene3dsgmaterialshader.cpp, line 87, as _ZN10Qt3DRender23Scene3DSGMaterialShader18updateSampledImageERN17QSGMaterialShader11RenderStateEiPP10QSGTextureP11QSGMaterialS8_
namespace Qt3DRender {
inline void Scene3DSGMaterialShader::updateSampledImage(QSGMaterialShader::RenderState &state,
                                                 int binding,
                                                 QSGTexture **texture,
                                                 QSGMaterial *newMaterial,
                                                 QSGMaterial *oldMaterial)
{
    Q_UNUSED(state);
    Q_UNUSED(binding);
    Scene3DSGMaterial *tx = static_cast<Scene3DSGMaterial *>(newMaterial);
    Scene3DSGMaterial *oldTx = static_cast<Scene3DSGMaterial *>(oldMaterial);
    QSGTexture *t = tx->texture();

    if (t != nullptr) {
        // TODO QT6 FIXME
        //        bool npotSupported = const_cast<QOpenGLContext *>(state.context())
        //                ->functions()->hasOpenGLFeature(QOpenGLFunctions::NPOTTextureRepeat);
        bool npotSupported = true;
        if (!npotSupported) {
            const QSize size = t->textureSize();
            const bool isNpot = !isPowerOfTwo(size.width()) || !isPowerOfTwo(size.height());
            if (isNpot) {
                t->setHorizontalWrapMode(QSGTexture::ClampToEdge);
                t->setVerticalWrapMode(QSGTexture::ClampToEdge);
            }
        }

        if (oldTx == nullptr || oldTx->texture() != t)
            *texture = t;
    }
}
}  // namespace Qt3DRender
//  -----------------------------------------------------------------------

//  Qt3DRender::Scene3DSGMaterialShader::Scene3DSGMaterialShader()
extern "C" Q_DECL_EXPORT
Qt3DRender::Scene3DSGMaterialShader *ritual_ZN10Qt3DRender23Scene3DSGMaterialShaderC1Ev() {
  return new Qt3DRender::Scene3DSGMaterialShader();
}

//  bool Qt3DRender::Scene3DSGMaterialShader::updateUniformData(RenderState
//      &state, QSGMaterial *newMaterial, QSGMaterial *oldMaterial)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10Qt3DRender23Scene3DSGMaterialShader17updateUniformDataERN17QSGMaterialShader11RenderStateEP11QSGMaterialS5_(
    Qt3DRender::Scene3DSGMaterialShader *self,
    QSGMaterialShader::RenderState *state,
    QSGMaterial *newMaterial,
    QSGMaterial *oldMaterial) {
  return self->updateUniformData(*state, newMaterial, oldMaterial);
}

//  void Qt3DRender::Scene3DSGMaterialShader::updateSampledImage(RenderState
//      &state, int binding, QSGTexture **texture, QSGMaterial *newMaterial,
//      QSGMaterial *oldMaterial)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender23Scene3DSGMaterialShader18updateSampledImageERN17QSGMaterialShader11RenderStateEiPP10QSGTextureP11QSGMaterialS8_(
    Qt3DRender::Scene3DSGMaterialShader *self,
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
