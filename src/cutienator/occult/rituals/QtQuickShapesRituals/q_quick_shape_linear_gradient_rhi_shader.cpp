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
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quickshapes/qquickshapegenericrenderer.cpp, line 903, as _ZN34QQuickShapeLinearGradientRhiShaderC1Ei
inline QQuickShapeLinearGradientRhiShader::QQuickShapeLinearGradientRhiShader(int viewCount)
{
    setShaderFileName(VertexStage, QStringLiteral(":/qt-project.org/shapes/shaders_ng/lineargradient.vert.qsb"), viewCount);
    setShaderFileName(FragmentStage, QStringLiteral(":/qt-project.org/shapes/shaders_ng/lineargradient.frag.qsb"), viewCount);
}

//  from ../qtdeclarative/src/quickshapes/qquickshapegenericrenderer.cpp, line 909, as _ZN34QQuickShapeLinearGradientRhiShader17updateUniformDataERN17QSGMaterialShader11RenderStateEP11QSGMaterialS4_
inline bool QQuickShapeLinearGradientRhiShader::updateUniformData(RenderState &state,
                                                           QSGMaterial *newMaterial, QSGMaterial *oldMaterial)
{
    Q_ASSERT(oldMaterial == nullptr || newMaterial->type() == oldMaterial->type());
    QQuickShapeLinearGradientMaterial *m = static_cast<QQuickShapeLinearGradientMaterial *>(newMaterial);
    bool changed = false;
    QByteArray *buf = state.uniformData();
    Q_ASSERT(buf->size() >= 84 + 64);
    const int shaderMatrixCount = newMaterial->viewCount();
    const int matrixCount = qMin(state.projectionMatrixCount(), shaderMatrixCount);

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

    if (!oldMaterial || m_gradA.x() != node->m_gradient.a.x() || m_gradA.y() != node->m_gradient.a.y()) {
        m_gradA = QVector2D(node->m_gradient.a.x(), node->m_gradient.a.y());
        Q_ASSERT(sizeof(m_gradA) == 8);
        memcpy(buf->data() + 64 * shaderMatrixCount + 64, &m_gradA, 8);
        changed = true;
    }

    if (!oldMaterial || m_gradB.x() != node->m_gradient.b.x() || m_gradB.y() != node->m_gradient.b.y()) {
        m_gradB = QVector2D(node->m_gradient.b.x(), node->m_gradient.b.y());
        memcpy(buf->data() + 64 * shaderMatrixCount + 64 + 8, &m_gradB, 8);
        changed = true;
    }

    if (state.isOpacityDirty()) {
        const float opacity = state.opacity();
        memcpy(buf->data() + 64 * shaderMatrixCount + 64 + 8 + 8, &opacity, 4);
        changed = true;
    }

    return changed;
}

//  from ../qtdeclarative/src/quickshapes/qquickshapegenericrenderer.cpp, line 958, as _ZN34QQuickShapeLinearGradientRhiShader18updateSampledImageERN17QSGMaterialShader11RenderStateEiPP10QSGTextureP11QSGMaterialS7_
inline void QQuickShapeLinearGradientRhiShader::updateSampledImage(RenderState &state, int binding, QSGTexture **texture,
                                                            QSGMaterial *newMaterial, QSGMaterial *)
{
    if (binding != 1)
        return;

    QQuickShapeLinearGradientMaterial *m = static_cast<QQuickShapeLinearGradientMaterial *>(newMaterial);
    QQuickShapeGenericStrokeFillNode *node = m->node();
    const QSGGradientCacheKey cacheKey(node->m_gradient.stops, QGradient::Spread(node->m_gradient.spread));
    QSGTexture *t = QSGGradientCache::cacheForRhi(state.rhi())->get(cacheKey);
    t->commitTextureOperations(state.rhi(), state.resourceUpdateBatch());
    *texture = t;
}
//  -----------------------------------------------------------------------

//  QQuickShapeLinearGradientRhiShader::QQuickShapeLinearGradientRhiShader(in
//      t viewCount)
extern "C" Q_DECL_EXPORT
QQuickShapeLinearGradientRhiShader *ritual_ZN34QQuickShapeLinearGradientRhiShaderC1Ei(
    int viewCount) {
  return new QQuickShapeLinearGradientRhiShader(viewCount);
}

//  bool QQuickShapeLinearGradientRhiShader::updateUniformData(RenderState
//      &state, QSGMaterial *newMaterial, QSGMaterial *oldMaterial)
extern "C" Q_DECL_EXPORT
bool ritual_ZN34QQuickShapeLinearGradientRhiShader17updateUniformDataERN17QSGMaterialShader11RenderStateEP11QSGMaterialS4_(
    QQuickShapeLinearGradientRhiShader *self,
    QSGMaterialShader::RenderState *state,
    QSGMaterial *newMaterial,
    QSGMaterial *oldMaterial) {
  return self->updateUniformData(*state, newMaterial, oldMaterial);
}

//  void QQuickShapeLinearGradientRhiShader::updateSampledImage(RenderState
//      &state, int binding, QSGTexture **texture, QSGMaterial *newMaterial,
//      QSGMaterial *oldMaterial)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QQuickShapeLinearGradientRhiShader18updateSampledImageERN17QSGMaterialShader11RenderStateEiPP10QSGTextureP11QSGMaterialS7_(
    QQuickShapeLinearGradientRhiShader *self,
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
