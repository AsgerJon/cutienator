//  Written by dev_tooling.RitualGenerator from the records of QtQuickShapes/
//  6.12.0/QtQuickShapes/private/qquickshapegenericrenderer_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuickShapes/6.12.0/QtQuickShapes/private/qquickshapesglobal_p.h>
#include <QtQuickShapes/QtQuickShapes>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickShapes/6.12.0/QtQuickShapes/private/qquickshapegenericrenderer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickShapes/private/qquickshapegenericrenderer_p.h>
#include <QtGui/private/qtriangulator_p.h>
#include <QtGui/private/qtriangulatingstroker_p.h>
#include <rhi/qrhi.h>
#include <QSGVertexColorMaterial>
#include <QSGTextureProvider>
#include <private/qsgplaintexture_p.h>
#include <QtQuick/private/qsggradientcache_p.h>
#if QT_CONFIG(thread)
#include <QtCore/QThreadPool>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quickshapes/qquickshapegenericrenderer.cpp, line 1295, as _ZN31QQuickShapeTextureFillRhiShaderC1Ei
inline QQuickShapeTextureFillRhiShader::QQuickShapeTextureFillRhiShader(int viewCount)
{
    setShaderFileName(VertexStage, QStringLiteral(":/qt-project.org/shapes/shaders_ng/texturefill.vert.qsb"), viewCount);
    setShaderFileName(FragmentStage, QStringLiteral(":/qt-project.org/shapes/shaders_ng/texturefill.frag.qsb"), viewCount);
}

//  from ../qtdeclarative/src/quickshapes/qquickshapegenericrenderer.cpp, line 1301, as _ZN31QQuickShapeTextureFillRhiShader17updateUniformDataERN17QSGMaterialShader11RenderStateEP11QSGMaterialS4_
inline bool QQuickShapeTextureFillRhiShader::updateUniformData(RenderState &state,
                                                        QSGMaterial *newMaterial, QSGMaterial *oldMaterial)
{
    Q_ASSERT(oldMaterial == nullptr || newMaterial->type() == oldMaterial->type());
    QQuickShapeTextureFillMaterial *m = static_cast<QQuickShapeTextureFillMaterial *>(newMaterial);
    bool changed = false;
    QByteArray *buf = state.uniformData();
    const int shaderMatrixCount = newMaterial->viewCount();
    const int matrixCount = qMin(state.projectionMatrixCount(), shaderMatrixCount);
    Q_ASSERT(buf->size() >= 64 * shaderMatrixCount + 64 + 8 + 4);

    if (state.isMatrixDirty()) {
        for (int viewIndex = 0; viewIndex < matrixCount; ++viewIndex) {
            const QMatrix4x4 m = state.combinedMatrix();
            memcpy(buf->data() + 64 * viewIndex, m.constData(), 64);
            changed = true;
        }
    }

    QQuickShapeGenericStrokeFillNode *node = m->node();

    if (!oldMaterial || m_fillTransform != node->m_fillTransform) {
        memcpy(buf->data() + 64 * shaderMatrixCount, node->m_fillTransform.invertedData(), 64);
        m_fillTransform = node->m_fillTransform;
        changed = true;
    }

    const QSizeF boundsSize = node->m_fillTextureProvider != nullptr && node->m_fillTextureProvider->texture() != nullptr
        ? node->m_fillTextureProvider->texture()->textureSize()
        : QSizeF(0, 0);


    const QVector2D boundsVector(boundsSize.width() / state.devicePixelRatio(),
                                 boundsSize.height() / state.devicePixelRatio());
    if (!oldMaterial || m_boundsSize != boundsVector) {
        m_boundsSize = boundsVector;
        Q_ASSERT(sizeof(m_boundsSize) == 8);
        memcpy(buf->data() + 64 * shaderMatrixCount + 64, &m_boundsSize, 8);
        changed = true;
    }

    if (state.isOpacityDirty()) {
        const float opacity = state.opacity();
        memcpy(buf->data() + 64 * shaderMatrixCount + 64 + 8, &opacity, 4);
        changed = true;
    }

    return changed;
}

//  from ../qtdeclarative/src/quickshapes/qquickshapegenericrenderer.cpp, line 1351, as _ZN31QQuickShapeTextureFillRhiShader18updateSampledImageERN17QSGMaterialShader11RenderStateEiPP10QSGTextureP11QSGMaterialS7_
inline void QQuickShapeTextureFillRhiShader::updateSampledImage(RenderState &state, int binding, QSGTexture **texture,
                                                         QSGMaterial *newMaterial, QSGMaterial *)
{
    if (binding != 1)
        return;

    QQuickShapeTextureFillMaterial *m = static_cast<QQuickShapeTextureFillMaterial *>(newMaterial);
    QQuickShapeGenericStrokeFillNode *node = m->node();
    if (node->m_fillTextureProvider != nullptr) {
        QSGTexture *providedTexture = node->m_fillTextureProvider->texture();
        if (providedTexture != nullptr) {
            if (providedTexture->isAtlasTexture()) {
                // Create a non-atlas copy to make texture coordinate wrapping work. This
                // texture copy is owned by the QSGTexture so memory is managed with the original
                // texture provider.
                QSGTexture *newTexture = providedTexture->removedFromAtlas(state.resourceUpdateBatch());
                if (newTexture != nullptr)
                    providedTexture = newTexture;
            }

            providedTexture->commitTextureOperations(state.rhi(), state.resourceUpdateBatch());
            *texture = providedTexture;
            return;
        }
    }

    if (m->dummyTexture() == nullptr) {
        QSGPlainTexture *dummyTexture = new QSGPlainTexture;
        dummyTexture->setFiltering(QSGTexture::Nearest);
        dummyTexture->setHorizontalWrapMode(QSGTexture::Repeat);
        dummyTexture->setVerticalWrapMode(QSGTexture::Repeat);
        QImage img(128, 128, QImage::Format_ARGB32_Premultiplied);
        img.fill(0);
        dummyTexture->setImage(img);
        dummyTexture->commitTextureOperations(state.rhi(), state.resourceUpdateBatch());

        m->setDummyTexture(dummyTexture);
    }

    *texture = m->dummyTexture();
}
//  -----------------------------------------------------------------------

//  QQuickShapeTextureFillRhiShader::QQuickShapeTextureFillRhiShader(int
//      viewCount)
extern "C" Q_DECL_EXPORT
QQuickShapeTextureFillRhiShader *ritual_ZN31QQuickShapeTextureFillRhiShaderC1Ei(
    int viewCount) {
  return new QQuickShapeTextureFillRhiShader(viewCount);
}

//  bool QQuickShapeTextureFillRhiShader::updateUniformData(RenderState
//      &state, QSGMaterial *newMaterial, QSGMaterial *oldMaterial)
extern "C" Q_DECL_EXPORT
bool ritual_ZN31QQuickShapeTextureFillRhiShader17updateUniformDataERN17QSGMaterialShader11RenderStateEP11QSGMaterialS4_(
    QQuickShapeTextureFillRhiShader *self,
    QSGMaterialShader::RenderState *state,
    QSGMaterial *newMaterial,
    QSGMaterial *oldMaterial) {
  return self->updateUniformData(*state, newMaterial, oldMaterial);
}

//  void QQuickShapeTextureFillRhiShader::updateSampledImage(RenderState
//      &state, int binding, QSGTexture **texture, QSGMaterial *newMaterial,
//      QSGMaterial *oldMaterial)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQuickShapeTextureFillRhiShader18updateSampledImageERN17QSGMaterialShader11RenderStateEiPP10QSGTextureP11QSGMaterialS7_(
    QQuickShapeTextureFillRhiShader *self,
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
