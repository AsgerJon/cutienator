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

//  from ../qtdeclarative/src/quickshapes/qquickshapegenericrenderer.cpp, line 891, as _ZN33QQuickShapeGenericMaterialFactory17createTextureFillEP12QQuickWindowP32QQuickShapeGenericStrokeFillNode
inline QSGMaterial *QQuickShapeGenericMaterialFactory::createTextureFill(QQuickWindow *window,
                                                                  QQuickShapeGenericStrokeFillNode *node)
{
    QSGRendererInterface::GraphicsApi api = window->rendererInterface()->graphicsApi();

    if (api == QSGRendererInterface::OpenGL || QSGRendererInterface::isApiRhiBased(api))
        return new QQuickShapeTextureFillMaterial(node);

    qWarning("Texture fill material: Unsupported graphics API %d", api);
    return nullptr;
}

//  from ../qtdeclarative/src/quickshapes/qquickshapegenericrenderer.cpp, line 844, as _ZN33QQuickShapeGenericMaterialFactory17createVertexColorEP12QQuickWindow
inline QSGMaterial *QQuickShapeGenericMaterialFactory::createVertexColor(QQuickWindow *window)
{
    QSGRendererInterface::GraphicsApi api = window->rendererInterface()->graphicsApi();

    if (api == QSGRendererInterface::OpenGL || QSGRendererInterface::isApiRhiBased(api))
        return new QSGVertexColorMaterial;

    qWarning("Vertex-color material: Unsupported graphics API %d", api);
    return nullptr;
}

//  from ../qtdeclarative/src/quickshapes/qquickshapegenericrenderer.cpp, line 855, as _ZN33QQuickShapeGenericMaterialFactory20createLinearGradientEP12QQuickWindowP32QQuickShapeGenericStrokeFillNode
inline QSGMaterial *QQuickShapeGenericMaterialFactory::createLinearGradient(QQuickWindow *window,
                                                                     QQuickShapeGenericStrokeFillNode *node)
{
    QSGRendererInterface::GraphicsApi api = window->rendererInterface()->graphicsApi();

    if (api == QSGRendererInterface::OpenGL || QSGRendererInterface::isApiRhiBased(api))
        return new QQuickShapeLinearGradientMaterial(node);

    qWarning("Linear gradient material: Unsupported graphics API %d", api);
    return nullptr;
}

//  from ../qtdeclarative/src/quickshapes/qquickshapegenericrenderer.cpp, line 867, as _ZN33QQuickShapeGenericMaterialFactory20createRadialGradientEP12QQuickWindowP32QQuickShapeGenericStrokeFillNode
inline QSGMaterial *QQuickShapeGenericMaterialFactory::createRadialGradient(QQuickWindow *window,
                                                                     QQuickShapeGenericStrokeFillNode *node)
{
    QSGRendererInterface::GraphicsApi api = window->rendererInterface()->graphicsApi();

    if (api == QSGRendererInterface::OpenGL || QSGRendererInterface::isApiRhiBased(api))
        return new QQuickShapeRadialGradientMaterial(node);

    qWarning("Radial gradient material: Unsupported graphics API %d", api);
    return nullptr;
}

//  from ../qtdeclarative/src/quickshapes/qquickshapegenericrenderer.cpp, line 879, as _ZN33QQuickShapeGenericMaterialFactory21createConicalGradientEP12QQuickWindowP32QQuickShapeGenericStrokeFillNode
inline QSGMaterial *QQuickShapeGenericMaterialFactory::createConicalGradient(QQuickWindow *window,
                                                                      QQuickShapeGenericStrokeFillNode *node)
{
    QSGRendererInterface::GraphicsApi api = window->rendererInterface()->graphicsApi();

    if (api == QSGRendererInterface::OpenGL || QSGRendererInterface::isApiRhiBased(api))
        return new QQuickShapeConicalGradientMaterial(node);

    qWarning("Conical gradient material: Unsupported graphics API %d", api);
    return nullptr;
}

//  from ../qtdeclarative/src/quickshapes/qquickshapegenericrenderer.cpp, line 85, as _ZN32QQuickShapeGenericStrokeFillNode10preprocessEv
inline void QQuickShapeGenericStrokeFillNode::preprocess()
{
    if (m_fillTextureProvider != nullptr) {
        if (QSGDynamicTexture *texture = qobject_cast<QSGDynamicTexture *>(m_fillTextureProvider->texture()))
            texture->updateTexture();
    }
}

//  from ../qtdeclarative/src/quickshapes/qquickshapegenericrenderer.cpp, line 1393, as _ZN30QQuickShapeTextureFillMaterialD1Ev
inline QQuickShapeTextureFillMaterial::~QQuickShapeTextureFillMaterial()
{
    delete m_dummyTexture;
}

//  from ../qtdeclarative/src/quickshapes/qquickshapegenericrenderer.cpp, line 1398, as _ZNK30QQuickShapeTextureFillMaterial4typeEv
inline QSGMaterialType *QQuickShapeTextureFillMaterial::type() const
{
    static QSGMaterialType type;
    return &type;
}

//  from ../qtdeclarative/src/quickshapes/qquickshapegenericrenderer.cpp, line 1404, as _ZNK30QQuickShapeTextureFillMaterial7compareEPK11QSGMaterial
inline int QQuickShapeTextureFillMaterial::compare(const QSGMaterial *other) const
{
    Q_ASSERT(other && type() == other->type());
    const QQuickShapeTextureFillMaterial *m = static_cast<const QQuickShapeTextureFillMaterial *>(other);

    QQuickShapeGenericStrokeFillNode *a = node();
    QQuickShapeGenericStrokeFillNode *b = m->node();
    Q_ASSERT(a && b);
    if (a == b)
        return 0;

    if (int d = a->m_fillTransform.compareTo(b->m_fillTransform))
        return d;

    const qintptr diff = qintptr(a->m_fillTextureProvider) - qintptr(b->m_fillTextureProvider);
    return diff < 0 ? -1 : (diff > 0 ? 1 : 0);
}

//  from ../qtdeclarative/src/quickshapes/qquickshapegenericrenderer.cpp, line 1422, as _ZNK30QQuickShapeTextureFillMaterial12createShaderEN20QSGRendererInterface10RenderModeE
inline QSGMaterialShader *QQuickShapeTextureFillMaterial::createShader(QSGRendererInterface::RenderMode renderMode) const
{
    Q_UNUSED(renderMode);
    return new QQuickShapeTextureFillRhiShader(viewCount());
}

//  from ../qtdeclarative/src/quickshapes/qquickshapegenericrenderer.cpp, line 972, as _ZNK33QQuickShapeLinearGradientMaterial4typeEv
inline QSGMaterialType *QQuickShapeLinearGradientMaterial::type() const
{
    static QSGMaterialType type;
    return &type;
}

//  from ../qtdeclarative/src/quickshapes/qquickshapegenericrenderer.cpp, line 978, as _ZNK33QQuickShapeLinearGradientMaterial7compareEPK11QSGMaterial
inline int QQuickShapeLinearGradientMaterial::compare(const QSGMaterial *other) const
{
    Q_ASSERT(other && type() == other->type());
    const QQuickShapeLinearGradientMaterial *m = static_cast<const QQuickShapeLinearGradientMaterial *>(other);

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

//  from ../qtdeclarative/src/quickshapes/qquickshapegenericrenderer.cpp, line 1020, as _ZNK33QQuickShapeLinearGradientMaterial12createShaderEN20QSGRendererInterface10RenderModeE
inline QSGMaterialShader *QQuickShapeLinearGradientMaterial::createShader(QSGRendererInterface::RenderMode renderMode) const
{
    Q_UNUSED(renderMode);
    return new QQuickShapeLinearGradientRhiShader(viewCount());
}

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

//  from ../qtdeclarative/src/quickshapes/qquickshapegenericrenderer.cpp, line 1245, as _ZNK34QQuickShapeConicalGradientMaterial4typeEv
inline QSGMaterialType *QQuickShapeConicalGradientMaterial::type() const
{
    static QSGMaterialType type;
    return &type;
}

//  from ../qtdeclarative/src/quickshapes/qquickshapegenericrenderer.cpp, line 1251, as _ZNK34QQuickShapeConicalGradientMaterial7compareEPK11QSGMaterial
inline int QQuickShapeConicalGradientMaterial::compare(const QSGMaterial *other) const
{
    Q_ASSERT(other && type() == other->type());
    const QQuickShapeConicalGradientMaterial *m = static_cast<const QQuickShapeConicalGradientMaterial *>(other);

    QQuickShapeGenericStrokeFillNode *a = node();
    QQuickShapeGenericStrokeFillNode *b = m->node();
    Q_ASSERT(a && b);
    if (a == b)
        return 0;

    const QSGGradientCache::GradientDesc *ga = &a->m_gradient;
    const QSGGradientCache::GradientDesc *gb = &b->m_gradient;

    if (int d = ga->a.x() - gb->a.x())
        return d;
    if (int d = ga->a.y() - gb->a.y())
        return d;

    if (int d = ga->v0 - gb->v0)
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

//  from ../qtdeclarative/src/quickshapes/qquickshapegenericrenderer.cpp, line 1289, as _ZNK34QQuickShapeConicalGradientMaterial12createShaderEN20QSGRendererInterface10RenderModeE
inline QSGMaterialShader *QQuickShapeConicalGradientMaterial::createShader(QSGRendererInterface::RenderMode renderMode) const
{
    Q_UNUSED(renderMode);
    return new QQuickShapeConicalGradientRhiShader(viewCount());
}

//  from ../qtdeclarative/src/quickshapes/qquickshapegenericrenderer.cpp, line 1295, as _ZN31QQuickShapeTextureFillRhiShaderC1Ei
inline QQuickShapeTextureFillRhiShader::QQuickShapeTextureFillRhiShader(int viewCount)
{
    setShaderFileName(VertexStage, QStringLiteral(":/qt-project.org/shapes/shaders_ng/texturefill.vert.qsb"), viewCount);
    setShaderFileName(FragmentStage, QStringLiteral(":/qt-project.org/shapes/shaders_ng/texturefill.frag.qsb"), viewCount);
}

//  from ../qtdeclarative/src/quickshapes/qquickshapegenericrenderer.cpp, line 903, as _ZN34QQuickShapeLinearGradientRhiShaderC1Ei
inline QQuickShapeLinearGradientRhiShader::QQuickShapeLinearGradientRhiShader(int viewCount)
{
    setShaderFileName(VertexStage, QStringLiteral(":/qt-project.org/shapes/shaders_ng/lineargradient.vert.qsb"), viewCount);
    setShaderFileName(FragmentStage, QStringLiteral(":/qt-project.org/shapes/shaders_ng/lineargradient.frag.qsb"), viewCount);
}

//  from ../qtdeclarative/src/quickshapes/qquickshapegenericrenderer.cpp, line 1026, as _ZN34QQuickShapeRadialGradientRhiShaderC1Ei
inline QQuickShapeRadialGradientRhiShader::QQuickShapeRadialGradientRhiShader(int viewCount)
{
    setShaderFileName(VertexStage, QStringLiteral(":/qt-project.org/shapes/shaders_ng/radialgradient.vert.qsb"), viewCount);
    setShaderFileName(FragmentStage, QStringLiteral(":/qt-project.org/shapes/shaders_ng/radialgradient.frag.qsb"), viewCount);
}

//  from ../qtdeclarative/src/quickshapes/qquickshapegenericrenderer.cpp, line 1173, as _ZN35QQuickShapeConicalGradientRhiShaderC1Ei
inline QQuickShapeConicalGradientRhiShader::QQuickShapeConicalGradientRhiShader(int viewCount)
{
    setShaderFileName(VertexStage, QStringLiteral(":/qt-project.org/shapes/shaders_ng/conicalgradient.vert.qsb"), viewCount);
    setShaderFileName(FragmentStage, QStringLiteral(":/qt-project.org/shapes/shaders_ng/conicalgradient.frag.qsb"), viewCount);
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

//  from ../qtdeclarative/src/quickshapes/qquickshapegenericrenderer.cpp, line 56, as _ZN32QQuickShapeGenericStrokeFillNode16activateMaterialEP12QQuickWindowNS_8MaterialE
inline void QQuickShapeGenericStrokeFillNode::activateMaterial(QQuickWindow *window, Material m)
{
    switch (m) {
    case MatSolidColor:
        // Use vertexcolor material. Items with different colors remain batchable
        // this way, at the expense of having to provide per-vertex color values.
        m_material.reset(QQuickShapeGenericMaterialFactory::createVertexColor(window));
        break;
    case MatLinearGradient:
        m_material.reset(QQuickShapeGenericMaterialFactory::createLinearGradient(window, this));
        break;
    case MatRadialGradient:
        m_material.reset(QQuickShapeGenericMaterialFactory::createRadialGradient(window, this));
        break;
    case MatConicalGradient:
        m_material.reset(QQuickShapeGenericMaterialFactory::createConicalGradient(window, this));
        break;
    case MatTextureFill:
        m_material.reset(QQuickShapeGenericMaterialFactory::createTextureFill(window, this));
        break;
    default:
        qWarning("Unknown material %d", m);
        return;
    }

    if (material() != m_material.data())
        setMaterial(m_material.data());
}
//  -----------------------------------------------------------------------

//  const QMetaObject *QQuickShapeGenericStrokeFillNode::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK32QQuickShapeGenericStrokeFillNode10metaObjectEv(
    const QQuickShapeGenericStrokeFillNode *self) {
  return self->metaObject();
}

//  void *QQuickShapeGenericStrokeFillNode::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN32QQuickShapeGenericStrokeFillNode11qt_metacastEPKc(
    QQuickShapeGenericStrokeFillNode *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickShapeGenericStrokeFillNode::qt_metacall(QMetaObject::Call a0,
//      int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN32QQuickShapeGenericStrokeFillNode11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickShapeGenericStrokeFillNode *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  void QQuickShapeGenericStrokeFillNode::activateMaterial(QQuickWindow
//      *window, Material m)
extern "C" Q_DECL_EXPORT
void ritual_ZN32QQuickShapeGenericStrokeFillNode16activateMaterialEP12QQuickWindowNS_8MaterialE(
    QQuickShapeGenericStrokeFillNode *self,
    QQuickWindow *window,
    QQuickShapeGenericStrokeFillNode::Material m) {
  self->activateMaterial(window, m);
}

//  void QQuickShapeGenericStrokeFillNode::preprocess()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QQuickShapeGenericStrokeFillNode10preprocessEv(
    QQuickShapeGenericStrokeFillNode *self) {
  self->preprocess();
}

//  void QQuickShapeGenericStrokeFillNode::handleTextureChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QQuickShapeGenericStrokeFillNode20handleTextureChangedEv(
    QQuickShapeGenericStrokeFillNode *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickShapeGenericStrokeFillNode")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "handleTextureChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "handleTextureChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickShapeGenericStrokeFillNode::handleTextureProviderDestroyed()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QQuickShapeGenericStrokeFillNode30handleTextureProviderDestroyedEv(
    QQuickShapeGenericStrokeFillNode *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickShapeGenericStrokeFillNode")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "handleTextureProviderDestroyed()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "handleTextureProviderDestroyed()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  QQuickShapeGenericStrokeFillNode as the QSGGeometryNode it is built on
extern "C" Q_DECL_EXPORT
QSGGeometryNode *ritual_cast_QQuickShapeGenericStrokeFillNode_QSGGeometryNode(
    QQuickShapeGenericStrokeFillNode *self) {
  return static_cast<QSGGeometryNode *>(self);
}

//  void QQuickShapeGenericStrokeFillNode::preprocess()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN32QQuickShapeGenericStrokeFillNode10preprocessEv(
    QQuickShapeGenericStrokeFillNode *self) {
  self->QQuickShapeGenericStrokeFillNode::preprocess();
}
