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

//  from ../qtdeclarative/src/quickshapes/qquickshapegenericrenderer.cpp, line 1173, as _ZN35QQuickShapeConicalGradientRhiShaderC1Ei
inline QQuickShapeConicalGradientRhiShader::QQuickShapeConicalGradientRhiShader(int viewCount)
{
    setShaderFileName(VertexStage, QStringLiteral(":/qt-project.org/shapes/shaders_ng/conicalgradient.vert.qsb"), viewCount);
    setShaderFileName(FragmentStage, QStringLiteral(":/qt-project.org/shapes/shaders_ng/conicalgradient.frag.qsb"), viewCount);
}

//  from ../qtdeclarative/src/quickshapes/qquickshapegenericrenderer.cpp, line 1179, as _ZN35QQuickShapeConicalGradientRhiShader17updateUniformDataERN17QSGMaterialShader11RenderStateEP11QSGMaterialS4_
inline bool QQuickShapeConicalGradientRhiShader::updateUniformData(RenderState &state,
                                                            QSGMaterial *newMaterial, QSGMaterial *oldMaterial)
{
    Q_ASSERT(oldMaterial == nullptr || newMaterial->type() == oldMaterial->type());
    QQuickShapeConicalGradientMaterial *m = static_cast<QQuickShapeConicalGradientMaterial *>(newMaterial);
    bool changed = false;
    QByteArray *buf = state.uniformData();
    Q_ASSERT(buf->size() >= 80 + 64);
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

    const QPointF centerPoint = node->m_gradient.a;
    const float angle = -qDegreesToRadians(node->m_gradient.v0);

    if (!oldMaterial || m_centerPoint.x() != centerPoint.x() || m_centerPoint.y() != centerPoint.y()) {
        m_centerPoint = QVector2D(centerPoint.x(), centerPoint.y());
        Q_ASSERT(sizeof(m_centerPoint) == 8);
        memcpy(buf->data() + 64 * shaderMatrixCount + 64, &m_centerPoint, 8);
        changed = true;
    }

    if (!oldMaterial || m_angle != angle) {
        m_angle = angle;
        memcpy(buf->data() + 64 * shaderMatrixCount + 64 + 8, &m_angle, 4);
        changed = true;
    }

    if (state.isOpacityDirty()) {
        const float opacity = state.opacity();
        memcpy(buf->data() + 64 * shaderMatrixCount + 64 + 8 + 4, &opacity, 4);
        changed = true;
    }

    return changed;
}

//  from ../qtdeclarative/src/quickshapes/qquickshapegenericrenderer.cpp, line 1231, as _ZN35QQuickShapeConicalGradientRhiShader18updateSampledImageERN17QSGMaterialShader11RenderStateEiPP10QSGTextureP11QSGMaterialS7_
inline void QQuickShapeConicalGradientRhiShader::updateSampledImage(RenderState &state, int binding, QSGTexture **texture,
                                                             QSGMaterial *newMaterial, QSGMaterial *)
{
    if (binding != 1)
        return;

    QQuickShapeConicalGradientMaterial *m = static_cast<QQuickShapeConicalGradientMaterial *>(newMaterial);
    QQuickShapeGenericStrokeFillNode *node = m->node();
    const QSGGradientCacheKey cacheKey(node->m_gradient.stops, QGradient::Spread(node->m_gradient.spread));
    QSGTexture *t = QSGGradientCache::cacheForRhi(state.rhi())->get(cacheKey);
    t->commitTextureOperations(state.rhi(), state.resourceUpdateBatch());
    *texture = t;
}
//  -----------------------------------------------------------------------

//  QQuickShapeConicalGradientRhiShader::QQuickShapeConicalGradientRhiShader(
//      int viewCount)
extern "C" Q_DECL_EXPORT
QQuickShapeConicalGradientRhiShader *ritual_ZN35QQuickShapeConicalGradientRhiShaderC1Ei(
    int viewCount) {
  return new QQuickShapeConicalGradientRhiShader(viewCount);
}

//  bool QQuickShapeConicalGradientRhiShader::updateUniformData(RenderState
//      &state, QSGMaterial *newMaterial, QSGMaterial *oldMaterial)
extern "C" Q_DECL_EXPORT
bool ritual_ZN35QQuickShapeConicalGradientRhiShader17updateUniformDataERN17QSGMaterialShader11RenderStateEP11QSGMaterialS4_(
    QQuickShapeConicalGradientRhiShader *self,
    QSGMaterialShader::RenderState *state,
    QSGMaterial *newMaterial,
    QSGMaterial *oldMaterial) {
  return self->updateUniformData(*state, newMaterial, oldMaterial);
}

//  void QQuickShapeConicalGradientRhiShader::updateSampledImage(RenderState
//      &state, int binding, QSGTexture **texture, QSGMaterial *newMaterial,
//      QSGMaterial *oldMaterial)
extern "C" Q_DECL_EXPORT
void ritual_ZN35QQuickShapeConicalGradientRhiShader18updateSampledImageERN17QSGMaterialShader11RenderStateEiPP10QSGTextureP11QSGMaterialS7_(
    QQuickShapeConicalGradientRhiShader *self,
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
