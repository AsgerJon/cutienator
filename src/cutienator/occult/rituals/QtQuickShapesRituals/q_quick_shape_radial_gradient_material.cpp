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

//  from ../qtdeclarative/src/quickshapes/qquickshapegenericrenderer.cpp, line 1114, as _ZNK33QQuickShapeRadialGradientMaterial4typeEv
inline QSGMaterialType *QQuickShapeRadialGradientMaterial::type() const
{
    static QSGMaterialType type;
    return &type;
}

//  from ../qtdeclarative/src/quickshapes/qquickshapegenericrenderer.cpp, line 1120, as _ZNK33QQuickShapeRadialGradientMaterial7compareEPK11QSGMaterial
inline int QQuickShapeRadialGradientMaterial::compare(const QSGMaterial *other) const
{
    Q_ASSERT(other && type() == other->type());
    const QQuickShapeRadialGradientMaterial *m = static_cast<const QQuickShapeRadialGradientMaterial *>(other);

    QQuickShapeGenericStrokeFillNode *a = node();
    QQuickShapeGenericStrokeFillNode *b = m->node();
    Q_ASSERT(a && b);
    if (a == b)
        return 0;

    const QSGGradientCache::GradientDesc *ga = &a->m_gradient;
    const QSGGradientCache::GradientDesc *gb = &b->m_gradient;

    if (int d = ga->spread - gb->spread)
        return d;

    if (int d = ga->a.x() - gb->a.x())
        return d;
    if (int d = ga->a.y() - gb->a.y())
        return d;
    if (int d = ga->b.x() - gb->b.x())
        return d;
    if (int d = ga->b.y() - gb->b.y())
        return d;

    if (int d = ga->v0 - gb->v0)
        return d;
    if (int d = ga->v1 - gb->v1)
        return d;

    if (int d = ga->stops.size() - gb->stops.size())
        return d;

    for (int i = 0; i < ga->stops.size(); ++i) {
        if (int d = ga->stops[i].first - gb->stops[i].first)
            return d;
        if (int d = ga->stops[i].second.rgba() - gb->stops[i].second.rgba())
            return d;
    }

    if (int d = a->m_fillTransform.compareTo(b->m_fillTransform))
        return d;

    return 0;
}

//  from ../qtdeclarative/src/quickshapes/qquickshapegenericrenderer.cpp, line 1167, as _ZNK33QQuickShapeRadialGradientMaterial12createShaderEN20QSGRendererInterface10RenderModeE
inline QSGMaterialShader *QQuickShapeRadialGradientMaterial::createShader(QSGRendererInterface::RenderMode renderMode) const
{
    Q_UNUSED(renderMode);
    return new QQuickShapeRadialGradientRhiShader(viewCount());
}

//  from ../qtdeclarative/src/quickshapes/qquickshapegenericrenderer.cpp, line 1026, as _ZN34QQuickShapeRadialGradientRhiShaderC1Ei
inline QQuickShapeRadialGradientRhiShader::QQuickShapeRadialGradientRhiShader(int viewCount)
{
    setShaderFileName(VertexStage, QStringLiteral(":/qt-project.org/shapes/shaders_ng/radialgradient.vert.qsb"), viewCount);
    setShaderFileName(FragmentStage, QStringLiteral(":/qt-project.org/shapes/shaders_ng/radialgradient.frag.qsb"), viewCount);
}

//  from ../qtdeclarative/src/quickshapes/qquickshapegenericrenderer.cpp, line 1032, as _ZN34QQuickShapeRadialGradientRhiShader17updateUniformDataERN17QSGMaterialShader11RenderStateEP11QSGMaterialS4_
inline bool QQuickShapeRadialGradientRhiShader::updateUniformData(RenderState &state,
                                                           QSGMaterial *newMaterial, QSGMaterial *oldMaterial)
{
    Q_ASSERT(oldMaterial == nullptr || newMaterial->type() == oldMaterial->type());
    QQuickShapeRadialGradientMaterial *m = static_cast<QQuickShapeRadialGradientMaterial *>(newMaterial);
    bool changed = false;
    QByteArray *buf = state.uniformData();
    Q_ASSERT(buf->size() >= 92 + 64);
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
    const QPointF focalPoint = node->m_gradient.b;
    const QPointF focalToCenter = centerPoint - focalPoint;
    const float centerRadius = node->m_gradient.v0;
    const float focalRadius = node->m_gradient.v1;

    if (!oldMaterial || m_focalPoint.x() != focalPoint.x() || m_focalPoint.y() != focalPoint.y()) {
        m_focalPoint = QVector2D(focalPoint.x(), focalPoint.y());
        Q_ASSERT(sizeof(m_focalPoint) == 8);
        memcpy(buf->data() + 64 * shaderMatrixCount + 64, &m_focalPoint, 8);
        changed = true;
    }

    if (!oldMaterial || m_focalToCenter.x() != focalToCenter.x() || m_focalToCenter.y() != focalToCenter.y()) {
        m_focalToCenter = QVector2D(focalToCenter.x(), focalToCenter.y());
        Q_ASSERT(sizeof(m_focalToCenter) == 8);
        memcpy(buf->data() + 64 * shaderMatrixCount + 64 + 8, &m_focalToCenter, 8);
        changed = true;
    }

    if (!oldMaterial || m_centerRadius != centerRadius) {
        m_centerRadius = centerRadius;
        memcpy(buf->data() + 64 * shaderMatrixCount + 64 + 8 + 8, &m_centerRadius, 4);
        changed = true;
    }

    if (!oldMaterial || m_focalRadius != focalRadius) {
        m_focalRadius = focalRadius;
        memcpy(buf->data() + 64 * shaderMatrixCount + 64 + 8 + 8 + 4, &m_focalRadius, 4);
        changed = true;
    }

    if (state.isOpacityDirty()) {
        const float opacity = state.opacity();
        memcpy(buf->data() + 64 * shaderMatrixCount + 64 + 8 + 8 + 4 + 4, &opacity, 4);
        changed = true;
    }

    return changed;
}

//  from ../qtdeclarative/src/quickshapes/qquickshapegenericrenderer.cpp, line 1100, as _ZN34QQuickShapeRadialGradientRhiShader18updateSampledImageERN17QSGMaterialShader11RenderStateEiPP10QSGTextureP11QSGMaterialS7_
inline void QQuickShapeRadialGradientRhiShader::updateSampledImage(RenderState &state, int binding, QSGTexture **texture,
                                                            QSGMaterial *newMaterial, QSGMaterial *)
{
    if (binding != 1)
        return;

    QQuickShapeRadialGradientMaterial *m = static_cast<QQuickShapeRadialGradientMaterial *>(newMaterial);
    QQuickShapeGenericStrokeFillNode *node = m->node();
    const QSGGradientCacheKey cacheKey(node->m_gradient.stops, QGradient::Spread(node->m_gradient.spread));
    QSGTexture *t = QSGGradientCache::cacheForRhi(state.rhi())->get(cacheKey);
    t->commitTextureOperations(state.rhi(), state.resourceUpdateBatch());
    *texture = t;
}
//  -----------------------------------------------------------------------

//  QQuickShapeRadialGradientMaterial::QQuickShapeRadialGradientMaterial(QQui
//      ckShapeGenericStrokeFillNode *node)
extern "C" Q_DECL_EXPORT
QQuickShapeRadialGradientMaterial *ritual_ZN33QQuickShapeRadialGradientMaterialC1EP32QQuickShapeGenericStrokeFillNode(
    QQuickShapeGenericStrokeFillNode *node) {
  return new QQuickShapeRadialGradientMaterial(node);
}

//  QSGMaterialType *QQuickShapeRadialGradientMaterial::type() const
extern "C" Q_DECL_EXPORT
QSGMaterialType *ritual_ZNK33QQuickShapeRadialGradientMaterial4typeEv(
    const QQuickShapeRadialGradientMaterial *self) {
  return self->type();
}

//  int QQuickShapeRadialGradientMaterial::compare(const QSGMaterial *other)
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK33QQuickShapeRadialGradientMaterial7compareEPK11QSGMaterial(
    const QQuickShapeRadialGradientMaterial *self,
    const QSGMaterial *other) {
  return self->compare(other);
}

//  QSGMaterialShader *QQuickShapeRadialGradientMaterial::createShader(QSGRen
//      dererInterface::RenderMode renderMode) const
extern "C" Q_DECL_EXPORT
QSGMaterialShader *ritual_ZNK33QQuickShapeRadialGradientMaterial12createShaderEN20QSGRendererInterface10RenderModeE(
    const QQuickShapeRadialGradientMaterial *self,
    QSGRendererInterface::RenderMode renderMode) {
  return self->createShader(renderMode);
}

//  QQuickShapeGenericStrokeFillNode
//      *QQuickShapeRadialGradientMaterial::node() const
extern "C" Q_DECL_EXPORT
QQuickShapeGenericStrokeFillNode *ritual_ZNK33QQuickShapeRadialGradientMaterial4nodeEv(
    const QQuickShapeRadialGradientMaterial *self) {
  return self->node();
}

//  QSGMaterialType *QQuickShapeRadialGradientMaterial::type() const
extern "C" Q_DECL_EXPORT
QSGMaterialType *ritual_own_ZNK33QQuickShapeRadialGradientMaterial4typeEv(
    const QQuickShapeRadialGradientMaterial *self) {
  return self->QQuickShapeRadialGradientMaterial::type();
}

//  int QQuickShapeRadialGradientMaterial::compare(const QSGMaterial *other)
//      const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK33QQuickShapeRadialGradientMaterial7compareEPK11QSGMaterial(
    const QQuickShapeRadialGradientMaterial *self,
    const QSGMaterial *other) {
  return self->QQuickShapeRadialGradientMaterial::compare(other);
}
