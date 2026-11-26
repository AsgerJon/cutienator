//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgtexturematerial_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgtexturematerial_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/private/qsgtexturematerial_p.h>
#include <QtQuick/private/qsgtexture_p.h>
#include <QtGui/rhi/qrhi.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quick/scenegraph/util/qsgtexturematerial.cpp, line 343, as _ZN27QSGTextureMaterialRhiShaderC1Ei
inline QSGTextureMaterialRhiShader::QSGTextureMaterialRhiShader(int viewCount)
    : QSGOpaqueTextureMaterialRhiShader(viewCount)
{
    setShaderFileName(VertexStage, QStringLiteral(":/qt-project.org/scenegraph/shaders_ng/texture.vert.qsb"), viewCount);
    setShaderFileName(FragmentStage, QStringLiteral(":/qt-project.org/scenegraph/shaders_ng/texture.frag.qsb"), viewCount);
}

//  from ../qtdeclarative/src/quick/scenegraph/util/qsgtexturematerial.cpp, line 350, as _ZN27QSGTextureMaterialRhiShader17updateUniformDataERN17QSGMaterialShader11RenderStateEP11QSGMaterialS4_
inline bool QSGTextureMaterialRhiShader::updateUniformData(RenderState &state, QSGMaterial *newMaterial, QSGMaterial *oldMaterial)
{
    bool changed = false;
    QByteArray *buf = state.uniformData();
    const int shaderMatrixCount = newMaterial->viewCount();

    if (state.isOpacityDirty()) {
        const float opacity = state.opacity();
        memcpy(buf->data() + 64 * shaderMatrixCount, &opacity, 4);
        changed = true;
    }

    changed |= QSGOpaqueTextureMaterialRhiShader::updateUniformData(state, newMaterial, oldMaterial);

    return changed;
}
//  -----------------------------------------------------------------------

//  QSGTextureMaterialRhiShader::QSGTextureMaterialRhiShader(int viewCount)
extern "C" Q_DECL_EXPORT
QSGTextureMaterialRhiShader *ritual_ZN27QSGTextureMaterialRhiShaderC1Ei(
    int viewCount) {
  return new QSGTextureMaterialRhiShader(viewCount);
}

//  bool QSGTextureMaterialRhiShader::updateUniformData(RenderState &state,
//      QSGMaterial *newMaterial, QSGMaterial *oldMaterial)
extern "C" Q_DECL_EXPORT
bool ritual_ZN27QSGTextureMaterialRhiShader17updateUniformDataERN17QSGMaterialShader11RenderStateEP11QSGMaterialS4_(
    QSGTextureMaterialRhiShader *self,
    QSGMaterialShader::RenderState *state,
    QSGMaterial *newMaterial,
    QSGMaterial *oldMaterial) {
  return self->updateUniformData(*state, newMaterial, oldMaterial);
}
