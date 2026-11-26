//  Written by dev_tooling.RitualGenerator from the records of QtQuickShapes/
//  6.12.0/QtQuickShapes/private/qquickshapegenericrenderer_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuickShapes/6.12.0/QtQuickShapes/private/qquickshapesglobal_p.h>
#include <QtQuickShapes/QtQuickShapes>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickShapes/6.12.0/QtQuickShapes/private/qquickshapegenericrenderer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qpainterpath.h>
#include <QtGui/qcolor.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgtransform_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
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

//  from ../qtdeclarative/src/quickshapes/qquickshapegenericrenderer.cpp, line 21, as local:qquickshapegenericrenderer.cpp:ColoredVertex
struct ColoredVertex // must match QSGGeometry::ColoredPoint2D
{
    float x, y;
    QQuickShapeGenericRenderer::Color4ub color;
    void set(float nx, float ny, QQuickShapeGenericRenderer::Color4ub ncolor)
    {
        x = nx; y = ny; color = ncolor;
    }
};

//  from ../qtdeclarative/src/quickshapes/qquickshapegenericrenderer.cpp, line 31, as local:qquickshapegenericrenderer.cpp:colorToColor4ub
static inline QQuickShapeGenericRenderer::Color4ub colorToColor4ub(const QColor &c)
{
    float r, g, b, a;
    c.getRgbF(&r, &g, &b, &a);
    QQuickShapeGenericRenderer::Color4ub color = {
        uchar(qRound(r * a * 255)),
        uchar(qRound(g * a * 255)),
        uchar(qRound(b * a * 255)),
        uchar(qRound(a * 255))
    };
    return color;
}

//  from ../qtdeclarative/src/quickshapes/qquickshapegenericrenderer.cpp, line 214, as local:qquickshapegenericrenderer.cpp:copyGenericGradient
static QQuickAbstractPathRenderer::FillGradientType
    copyGenericGradient(const QQuickShapeGradient *gradient, QSGGradientCache::GradientDesc *dst)
{
    Q_ASSERT(dst != nullptr);
    if (gradient == nullptr)
        return QQuickAbstractPathRenderer::NoGradient;

    dst->stops = gradient->gradientStops(); // sorted
    dst->spread = QGradient::Spread(gradient->spread());
    if (const QQuickShapeLinearGradient *g  = qobject_cast<const QQuickShapeLinearGradient *>(gradient)) {
        dst->a = QPointF(g->x1(), g->y1());
        dst->b = QPointF(g->x2(), g->y2());

        return QQuickAbstractPathRenderer::LinearGradient;
    } else if (const QQuickShapeRadialGradient *g = qobject_cast<const QQuickShapeRadialGradient *>(gradient)) {
        dst->a = QPointF(g->centerX(), g->centerY());
        dst->b = QPointF(g->focalX(), g->focalY());
        dst->v0 = g->centerRadius();
        dst->v1 = g->focalRadius();

        return QQuickAbstractPathRenderer::RadialGradient;
    } else if (const QQuickShapeConicalGradient *g = qobject_cast<const QQuickShapeConicalGradient *>(gradient)) {
        dst->a = QPointF(g->centerX(), g->centerY());
        dst->v0 = g->angle();

        return QQuickAbstractPathRenderer::ConicalGradient;
    }

    Q_UNREACHABLE_RETURN(QQuickAbstractPathRenderer::NoGradient);
}

//  from ../qtdeclarative/src/quickshapes/qquickshapegenericrenderer.cpp, line 556, as _ZN26QQuickShapeGenericRenderer10updateNodeEv
inline void QQuickShapeGenericRenderer::updateNode()
{
    if (!m_rootNode || !m_accDirty)
        return;

    // Is it now safe to query the rhi backend
    if (!m_rhiBackendInitialized) {
        auto findRHIBackend = [](QQuickItem *item) -> QRhi * {
            if (auto *w = item->window()) {
                if (auto *rhi = QQuickWindowPrivate::get(w)->rhi)
                    return rhi;
            }
            return nullptr;
        };
        auto *rhi = findRHIBackend(m_item);
        if (rhi != nullptr) {
            m_rhiBackendInitialized = true;
            m_supportsElementIndexUint = rhi->isFeatureSupported(QRhi::ElementIndexUint);
        }
    }

//                     [   m_rootNode   ]
//                     /       /        /
// #0          [  fill  ] [  stroke  ] [   next   ]
//                                    /     /      |
// #1                       [  fill  ] [  stroke  ] [   next   ]
//                                                 /      /     |
// #2                                     [  fill  ] [ stroke ] [  next  ]
//                                                                 ...
// ...

    QQuickShapeGenericNode **nodePtr = &m_rootNode;
    QQuickShapeGenericNode *prevNode = nullptr;

    for (ShapePathData &d : m_sp) {
        if (!*nodePtr) {
            Q_ASSERT(prevNode);
            *nodePtr = new QQuickShapeGenericNode;
            prevNode->m_next = *nodePtr;
            prevNode->appendChildNode(*nodePtr);
        }

        QQuickShapeGenericNode *node = *nodePtr;

        if (m_accDirty & DirtyList) {
            d.effectiveDirty |= DirtyFillGeom | DirtyStrokeGeom | DirtyColor | DirtyFillGradient
                              | DirtyFillTransform | DirtyFillTexture | DirtyStrokeGradient;
        }

        if (!d.effectiveDirty) {
            prevNode = node;
            nodePtr = &node->m_next;
            continue;
        }

        if (d.fillColor.a == 0) {
            delete node->m_fillNode;
            node->m_fillNode = nullptr;
        } else if (!node->m_fillNode) {
            node->m_fillNode = new QQuickShapeGenericStrokeFillNode(m_item->window());
            if (node->m_strokeNode)
                node->removeChildNode(node->m_strokeNode);
            node->appendChildNode(node->m_fillNode);
            if (node->m_strokeNode)
                node->appendChildNode(node->m_strokeNode);
            d.effectiveDirty |= DirtyFillGeom;
        }

        if (d.strokeWidth <= 0.0f || d.strokeColor.a == 0) {
            delete node->m_strokeNode;
            node->m_strokeNode = nullptr;
        } else if (!node->m_strokeNode) {
            node->m_strokeNode = new QQuickShapeGenericStrokeFillNode(m_item->window());
            node->appendChildNode(node->m_strokeNode);
            d.effectiveDirty |= DirtyStrokeGeom;
        }

        updateFillNode(&d, node);
        updateStrokeNode(&d, node);

        d.effectiveDirty = 0;

        prevNode = node;
        nodePtr = &node->m_next;
    }

    if (*nodePtr && prevNode) {
        prevNode->removeChildNode(*nodePtr);
        delete *nodePtr;
        *nodePtr = nullptr;
    }

    if (m_sp.isEmpty()) {
        delete m_rootNode->m_fillNode;
        m_rootNode->m_fillNode = nullptr;
        delete m_rootNode->m_strokeNode;
        m_rootNode->m_strokeNode = nullptr;
        delete m_rootNode->m_next;
        m_rootNode->m_next = nullptr;
    }

    m_accDirty = 0;
}

//  from ../qtdeclarative/src/quickshapes/qquickshapegenericrenderer.cpp, line 195, as _ZN26QQuickShapeGenericRenderer11setCapStyleEiN15QQuickShapePath8CapStyleE
inline void QQuickShapeGenericRenderer::setCapStyle(int index, QQuickShapePath::CapStyle capStyle)
{
    ShapePathData &d(m_sp[index]);
    d.pen.setCapStyle(Qt::PenCapStyle(capStyle));
    d.syncDirty |= DirtyStrokeGeom;
}

//  from ../qtdeclarative/src/quickshapes/qquickshapegenericrenderer.cpp, line 180, as _ZN26QQuickShapeGenericRenderer11setFillRuleEiN15QQuickShapePath8FillRuleE
inline void QQuickShapeGenericRenderer::setFillRule(int index, QQuickShapePath::FillRule fillRule)
{
    ShapePathData &d(m_sp[index]);
    d.fillRule = Qt::FillRule(fillRule);
    d.syncDirty |= DirtyFillGeom;
}

//  from ../qtdeclarative/src/quickshapes/qquickshapegenericrenderer.cpp, line 169, as _ZN26QQuickShapeGenericRenderer12setFillColorEiRK6QColor
inline void QQuickShapeGenericRenderer::setFillColor(int index, const QColor &color)
{
    ShapePathData &d(m_sp[index]);
    const bool wasTransparent = d.fillColor.a == 0;
    d.fillColor = colorToColor4ub(color);
    const bool isTransparent = d.fillColor.a == 0;
    d.syncDirty |= DirtyColor;
    if (wasTransparent && !isTransparent)
        d.syncDirty |= DirtyFillGeom;
}

//  from ../qtdeclarative/src/quickshapes/qquickshapegenericrenderer.cpp, line 187, as _ZN26QQuickShapeGenericRenderer12setJoinStyleEiN15QQuickShapePath9JoinStyleEi
inline void QQuickShapeGenericRenderer::setJoinStyle(int index, QQuickShapePath::JoinStyle joinStyle, int miterLimit)
{
    ShapePathData &d(m_sp[index]);
    d.pen.setJoinStyle(Qt::PenJoinStyle(joinStyle));
    d.pen.setMiterLimit(miterLimit);
    d.syncDirty |= DirtyStrokeGeom;
}

//  from ../qtdeclarative/src/quickshapes/qquickshapegenericrenderer.cpp, line 202, as _ZN26QQuickShapeGenericRenderer14setStrokeStyleEiN15QQuickShapePath11StrokeStyleEdRK5QListIdE
inline void QQuickShapeGenericRenderer::setStrokeStyle(int index, QQuickShapePath::StrokeStyle strokeStyle,
                                                   qreal dashOffset, const QList<qreal> &dashPattern)
{
    ShapePathData &d(m_sp[index]);
    d.pen.setStyle(Qt::PenStyle(strokeStyle));
    if (strokeStyle == QQuickShapePath::DashLine) {
        d.pen.setDashPattern(dashPattern);
        d.pen.setDashOffset(dashOffset);
    }
    d.syncDirty |= DirtyStrokeGeom;
}

//  from ../qtdeclarative/src/quickshapes/qquickshapegenericrenderer.cpp, line 151, as _ZN26QQuickShapeGenericRenderer14setStrokeWidthEid
inline void QQuickShapeGenericRenderer::setStrokeWidth(int index, qreal w)
{
    ShapePathData &d(m_sp[index]);
    d.strokeWidth = w;
    if (w > 0.0f)
        d.pen.setWidthF(w);
    d.syncDirty |= DirtyStrokeGeom;
}

//  from ../qtdeclarative/src/quickshapes/qquickshapegenericrenderer.cpp, line 245, as _ZN26QQuickShapeGenericRenderer15setFillGradientEiP19QQuickShapeGradient
inline void QQuickShapeGenericRenderer::setFillGradient(int index, QQuickShapeGradient *gradient)
{
    ShapePathData &d(m_sp[index]);
    d.fillGradientActive = copyGenericGradient(gradient, &d.fillGradient);
    d.syncDirty |= DirtyFillGradient;
}

//  from ../qtdeclarative/src/quickshapes/qquickshapegenericrenderer.cpp, line 314, as _ZN26QQuickShapeGenericRenderer16setAsyncCallbackEPFvPvES0_
inline void QQuickShapeGenericRenderer::setAsyncCallback(void (*callback)(void *), void *data)
{
    m_asyncCallback = callback;
    m_asyncCallbackData = data;
}

//  from ../qtdeclarative/src/quickshapes/qquickshapegenericrenderer.cpp, line 285, as _ZN26QQuickShapeGenericRenderer16setFillTransformEiRK12QSGTransform
inline void QQuickShapeGenericRenderer::setFillTransform(int index, const QSGTransform &transform)
{
    ShapePathData &d(m_sp[index]);
    d.fillTransform = transform;
    d.syncDirty |= DirtyFillTransform;
}

//  from ../qtdeclarative/src/quickshapes/qquickshapegenericrenderer.cpp, line 272, as _ZN26QQuickShapeGenericRenderer17handleSceneChangeEP12QQuickWindow
inline void QQuickShapeGenericRenderer::handleSceneChange(QQuickWindow *window)
{
    for (auto &pathData : m_sp) {
        if (pathData.fillTextureProviderItem != nullptr) {
            if (window == nullptr)
                QQuickItemPrivate::get(pathData.fillTextureProviderItem)->derefWindow();
            else
                QQuickItemPrivate::get(pathData.fillTextureProviderItem)->refWindow(window);
        }
    }
}

//  from ../qtdeclarative/src/quickshapes/qquickshapegenericrenderer.cpp, line 160, as _ZN26QQuickShapeGenericRenderer17setCosmeticStrokeEib
inline void QQuickShapeGenericRenderer::setCosmeticStroke(int index, bool c)
{
    ShapePathData &d(m_sp[index]);
    d.pen.setCosmetic(c);
    d.syncDirty |= DirtyStrokeGeom;
    // as long as the stroke is cosmetic,
    // QQuickShape::itemChange triggers re-triangulation whenever scale changes
}

//  from ../qtdeclarative/src/quickshapes/qquickshapegenericrenderer.cpp, line 292, as _ZN26QQuickShapeGenericRenderer21setTriangulationScaleEid
inline void QQuickShapeGenericRenderer::setTriangulationScale(int index, qreal scale)
{
    ShapePathData &d(m_sp[index]);
    d.triangulationScale = scale;
    d.syncDirty |= DirtyStrokeGeom;
}

//  from ../qtdeclarative/src/quickshapes/qquickshapegenericrenderer.cpp, line 259, as _ZN26QQuickShapeGenericRenderer22setFillTextureProviderEiP10QQuickItem
inline void QQuickShapeGenericRenderer::setFillTextureProvider(int index, QQuickItem *textureProviderItem)
{
    ShapePathData &d(m_sp[index]);
    if ((d.fillTextureProviderItem == nullptr) != (textureProviderItem == nullptr))
        d.syncDirty |= DirtyFillGeom;
    if (d.fillTextureProviderItem != nullptr)
        QQuickItemPrivate::get(d.fillTextureProviderItem)->derefWindow();
    d.fillTextureProviderItem = textureProviderItem;
    if (d.fillTextureProviderItem != nullptr)
        QQuickItemPrivate::get(d.fillTextureProviderItem)->refWindow(m_item->window());
    d.syncDirty |= DirtyFillTexture;
}

//  from ../qtdeclarative/src/quickshapes/qquickshapegenericrenderer.cpp, line 133, as _ZN26QQuickShapeGenericRenderer7setPathEiRK12QPainterPath6QFlagsIN15QQuickShapePath8PathHintEE
inline void QQuickShapeGenericRenderer::setPath(int index, const QPainterPath &path, QQuickShapePath::PathHints)
{
    ShapePathData &d(m_sp[index]);
    d.path = path;
    d.syncDirty |= DirtyFillGeom | DirtyStrokeGeom;
}

//  from ../qtdeclarative/src/quickshapes/qquickshapegenericrenderer.cpp, line 117, as _ZN26QQuickShapeGenericRenderer9beginSyncEiPb
inline void QQuickShapeGenericRenderer::beginSync(int totalCount, bool *countChanged)
{
    for (int i = totalCount; i < m_sp.size(); i++) // Handle removal of paths
        setFillTextureProvider(i, nullptr); // deref window

    if (m_sp.size() != totalCount) {
        m_sp.resize(totalCount);
        m_accDirty |= DirtyList;
        *countChanged = true;
    } else {
        *countChanged = false;
    }
    for (ShapePathData &d : m_sp)
        d.syncDirty = 0;
}

//  from ../qtdeclarative/src/quickshapes/qquickshapegenericrenderer.cpp, line 699, as _ZN26QQuickShapeGenericRenderer14updateFillNodeEPNS_13ShapePathDataEP22QQuickShapeGenericNode
inline void QQuickShapeGenericRenderer::updateFillNode(ShapePathData *d, QQuickShapeGenericNode *node)
{
    if (!node->m_fillNode)
        return;
    if (!(d->effectiveDirty & (DirtyFillGeom | DirtyColor | DirtyFillGradient | DirtyFillTransform | DirtyFillTexture)))
        return;

    // Make a copy of the data that will be accessed by the material on
    // the render thread. This must be done even when we bail out below.
    QQuickShapeGenericStrokeFillNode *n = node->m_fillNode;
    updateShadowDataInNode(d, n);

    QSGGeometry *g = n->geometry();
    if (d->fillVertices.isEmpty()) {
        if (g->vertexCount() || g->indexCount()) {
            g->allocate(0, 0);
            n->markDirty(QSGNode::DirtyGeometry);
        }
        return;
    }

    if (d->fillGradientActive) {
        QQuickShapeGenericStrokeFillNode::Material gradMat;
        switch (d->fillGradientActive) {
        case LinearGradient:
            gradMat = QQuickShapeGenericStrokeFillNode::MatLinearGradient;
            break;
        case RadialGradient:
            gradMat = QQuickShapeGenericStrokeFillNode::MatRadialGradient;
            break;
        case ConicalGradient:
            gradMat = QQuickShapeGenericStrokeFillNode::MatConicalGradient;
            break;
        default:
            Q_UNREACHABLE_RETURN();
        }
        n->activateMaterial(m_item->window(), gradMat);
        if (d->effectiveDirty & (DirtyFillGradient | DirtyFillTransform)) {
            // Gradients are implemented via a texture-based material.
            n->markDirty(QSGNode::DirtyMaterial);
            // stop here if only the gradient or filltransform changed; no need to touch the geometry
            if (!(d->effectiveDirty & DirtyFillGeom))
                return;
        }
    } else if (d->fillTextureProviderItem != nullptr) {
        n->activateMaterial(m_item->window(), QQuickShapeGenericStrokeFillNode::MatTextureFill);
        if (d->effectiveDirty & DirtyFillTexture)
            n->markDirty(QSGNode::DirtyMaterial);
    } else {
        n->activateMaterial(m_item->window(), QQuickShapeGenericStrokeFillNode::MatSolidColor);
        // fast path for updating only color values when no change in vertex positions
        if ((d->effectiveDirty & DirtyColor) && !(d->effectiveDirty & DirtyFillGeom) && d->fillTextureProviderItem == nullptr) {
            ColoredVertex *vdst = reinterpret_cast<ColoredVertex *>(g->vertexData());
            for (int i = 0; i < g->vertexCount(); ++i)
                vdst[i].set(vdst[i].x, vdst[i].y, d->fillColor);
            n->markDirty(QSGNode::DirtyGeometry);
            return;
        }
    }

    const int indexCount = d->indexType == QSGGeometry::UnsignedShortType
            ? d->fillIndices.size() * 2 : d->fillIndices.size();
    if (g->indexType() != d->indexType) {
        g = new QSGGeometry(QSGGeometry::defaultAttributes_ColoredPoint2D(),
                            d->fillVertices.size(), indexCount, d->indexType);
        n->setGeometry(g);
    } else {
        g->allocate(d->fillVertices.size(), indexCount);
    }
    g->setDrawingMode(QSGGeometry::DrawTriangles);

    memcpy(g->vertexData(), d->fillVertices.constData(), g->vertexCount() * g->sizeOfVertex());
    memcpy(g->indexData(), d->fillIndices.constData(), g->indexCount() * g->sizeOfIndex());

    n->markDirty(QSGNode::DirtyGeometry);
}

//  from ../qtdeclarative/src/quickshapes/qquickshapegenericrenderer.cpp, line 776, as _ZN26QQuickShapeGenericRenderer16updateStrokeNodeEPNS_13ShapePathDataEP22QQuickShapeGenericNode
inline void QQuickShapeGenericRenderer::updateStrokeNode(ShapePathData *d, QQuickShapeGenericNode *node)
{
    if (!node->m_strokeNode)
        return;
    if (!(d->effectiveDirty & (DirtyStrokeGeom | DirtyColor | DirtyStrokeGradient)))
        return;

    QQuickShapeGenericStrokeFillNode *n = node->m_strokeNode;
    if (d->strokeGradientActive) {
        if (d->effectiveDirty & DirtyStrokeGradient)
            n->m_gradient = d->strokeGradient;
    }

    QSGGeometry *g = n->geometry();
    if (d->strokeVertices.isEmpty()) {
        if (g->vertexCount() || g->indexCount()) {
            g->allocate(0, 0);
            n->markDirty(QSGNode::DirtyGeometry);
        }
        return;
    }

    n->markDirty(QSGNode::DirtyGeometry);

    // Async loading runs update once, bails out above, then updates again once
    // ready. Set the material dirty then. This is in-line with fill where the
    // first activateMaterial() achieves the same.
    if (!g->vertexCount())
        n->markDirty(QSGNode::DirtyMaterial);

    if (d->strokeGradientActive) {
        QQuickShapeGenericStrokeFillNode::Material gradMat;
        switch (d->strokeGradientActive) {
        case LinearGradient:
            gradMat = QQuickShapeGenericStrokeFillNode::MatLinearGradient;
            break;
        case RadialGradient:
            gradMat = QQuickShapeGenericStrokeFillNode::MatRadialGradient;
            break;
        case ConicalGradient:
            gradMat = QQuickShapeGenericStrokeFillNode::MatConicalGradient;
            break;
        default:
            Q_UNREACHABLE_RETURN();
        }
        n->activateMaterial(m_item->window(), gradMat);
        if (d->effectiveDirty & DirtyStrokeGradient) {
            // Gradients are implemented via a texture-based material.
            n->markDirty(QSGNode::DirtyMaterial);
            // stop here if only the gradient changed; no need to touch the geometry
            if (!(d->effectiveDirty & DirtyStrokeGeom))
                return;
        }
    } else {
        n->activateMaterial(m_item->window(), QQuickShapeGenericStrokeFillNode::MatSolidColor);
        if ((d->effectiveDirty & DirtyColor) && !(d->effectiveDirty & DirtyStrokeGeom)) {
            ColoredVertex *vdst = reinterpret_cast<ColoredVertex *>(g->vertexData());
            for (int i = 0; i < g->vertexCount(); ++i)
                vdst[i].set(vdst[i].x, vdst[i].y, d->strokeColor);
            return;
        }
    }

    g->allocate(d->strokeVertices.size(), 0);
    g->setDrawingMode(QSGGeometry::DrawTriangleStrip);
    memcpy(g->vertexData(), d->strokeVertices.constData(), g->vertexCount() * g->sizeOfVertex());
}

//  from ../qtdeclarative/src/quickshapes/qquickshapegenericrenderer.cpp, line 44, as _ZN32QQuickShapeGenericStrokeFillNodeC1EP12QQuickWindow
inline QQuickShapeGenericStrokeFillNode::QQuickShapeGenericStrokeFillNode(QQuickWindow *window)
    : m_material(nullptr)
{
    setFlag(QSGNode::OwnsGeometry, true);
    setFlag(QSGNode::UsePreprocess, true);
    setGeometry(new QSGGeometry(QSGGeometry::defaultAttributes_ColoredPoint2D(), 0, 0));
    activateMaterial(window, MatSolidColor);
#ifdef QSG_RUNTIME_DESCRIPTION
    qsgnode_set_description(this, QLatin1String("stroke-fill"));
#endif
}

//  from ../qtdeclarative/src/quickshapes/qquickshapegenericrenderer.cpp, line 660, as _ZN26QQuickShapeGenericRenderer22updateShadowDataInNodeEPNS_13ShapePathDataEP32QQuickShapeGenericStrokeFillNode
inline void QQuickShapeGenericRenderer::updateShadowDataInNode(ShapePathData *d, QQuickShapeGenericStrokeFillNode *n)
{
    if (d->fillGradientActive) {
        if (d->effectiveDirty & DirtyFillGradient)
            n->m_gradient = d->fillGradient;
    }

    if (d->effectiveDirty & DirtyFillTexture) {
        bool needsUpdate = d->fillTextureProviderItem == nullptr && n->m_fillTextureProvider != nullptr;
        if (!needsUpdate
            && d->fillTextureProviderItem != nullptr
            && n->m_fillTextureProvider != d->fillTextureProviderItem->textureProvider()) {
            needsUpdate = true;
        }

        if (needsUpdate) {
            if (n->m_fillTextureProvider != nullptr) {
                QObject::disconnect(n->m_fillTextureProvider, &QSGTextureProvider::textureChanged,
                                    n, &QQuickShapeGenericStrokeFillNode::handleTextureChanged);
                QObject::disconnect(n->m_fillTextureProvider, &QSGTextureProvider::destroyed,
                                    n, &QQuickShapeGenericStrokeFillNode::handleTextureProviderDestroyed);
            }

            n->m_fillTextureProvider = d->fillTextureProviderItem == nullptr
                                           ? nullptr
                                           : d->fillTextureProviderItem->textureProvider();

            if (n->m_fillTextureProvider != nullptr) {
                QObject::connect(n->m_fillTextureProvider, &QSGTextureProvider::textureChanged,
                                 n, &QQuickShapeGenericStrokeFillNode::handleTextureChanged);
                QObject::connect(n->m_fillTextureProvider, &QSGTextureProvider::destroyed,
                                 n, &QQuickShapeGenericStrokeFillNode::handleTextureProviderDestroyed);
            }
        }
    }
    if (d->effectiveDirty & DirtyFillTransform)
        n->m_fillTransform = d->fillTransform;
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

//  from ../qtdeclarative/src/quickshapes/qquickshapegenericrenderer.cpp, line 104, as _ZN26QQuickShapeGenericRendererD1Ev
inline QQuickShapeGenericRenderer::~QQuickShapeGenericRenderer()
{
    for (ShapePathData &d : m_sp) {
        if (d.pendingFill)
            d.pendingFill->orphaned = true;
        if (d.pendingStroke)
            d.pendingStroke->orphaned = true;
    }
}

//  from ../qtdeclarative/src/quickshapes/qquickshapegenericrenderer.cpp, line 547, as _ZN26QQuickShapeGenericRenderer11setRootNodeEP22QQuickShapeGenericNode
inline void QQuickShapeGenericRenderer::setRootNode(QQuickShapeGenericNode *node)
{
    if (m_rootNode != node) {
        m_rootNode = node;
        m_accDirty |= DirtyList;
    }
}

//  from ../qtdeclarative/src/quickshapes/qquickshapegenericrenderer.cpp, line 476, as _ZN26QQuickShapeGenericRenderer15triangulateFillERK12QPainterPathRKNS_8Color4ubEP5QListIN11QSGGeometry14ColoredPoint2DEEPS6_IjEPNS7_4TypeEbd
inline void QQuickShapeGenericRenderer::triangulateFill(const QPainterPath &path,
                                                 const Color4ub &fillColor,
                                                 VertexContainerType *fillVertices,
                                                 IndexContainerType *fillIndices,
                                                 QSGGeometry::Type *indexType,
                                                 bool supportsElementIndexUint,
                                                 qreal triangulationScale)
{
    const QVectorPath &vp = qtVectorPathForPath(path);

    QTriangleSet ts = qTriangulate(vp, QTransform::fromScale(triangulationScale, triangulationScale), 1, supportsElementIndexUint);
    const int vertexCount = ts.vertices.size() / 2; // just a qreal vector with x,y hence the / 2
    fillVertices->resize(vertexCount);
    ColoredVertex *vdst = reinterpret_cast<ColoredVertex *>(fillVertices->data());
    const qreal *vsrc = ts.vertices.constData();
    for (int i = 0; i < vertexCount; ++i)
        vdst[i].set(vsrc[i * 2] / triangulationScale, vsrc[i * 2 + 1] / triangulationScale, fillColor);

    size_t indexByteSize;
    if (ts.indices.type() == QVertexIndexVector::UnsignedShort) {
        *indexType = QSGGeometry::UnsignedShortType;
        // fillIndices is still QList<quint32>. Just resize to N/2 and pack
        // the N quint16s into it.
        fillIndices->resize(ts.indices.size() / 2);
        indexByteSize = ts.indices.size() * sizeof(quint16);
    } else {
        *indexType = QSGGeometry::UnsignedIntType;
        fillIndices->resize(ts.indices.size());
        indexByteSize = ts.indices.size() * sizeof(quint32);
    }
    memcpy(fillIndices->data(), ts.indices.data(), indexByteSize);
}

//  from ../qtdeclarative/src/quickshapes/qquickshapegenericrenderer.cpp, line 462, as _ZN26QQuickShapeGenericRenderer20maybeUpdateAsyncItemEv
inline void QQuickShapeGenericRenderer::maybeUpdateAsyncItem()
{
    for (const ShapePathData &d : std::as_const(m_sp)) {
        if (d.pendingFill || d.pendingStroke)
            return;
    }
    m_accDirty |= DirtyFillGeom | DirtyStrokeGeom;
    m_item->update();
    if (m_asyncCallback)
        m_asyncCallback(m_asyncCallbackData);
}
//  -----------------------------------------------------------------------

//  A QQuickShapeGenericRenderer that Python can take functions over in. Every QQuickShapeGenericRenderer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickShapeGenericRendererCall0)(const void *, int, const QPainterPath *, int, int *);
typedef void (*CuteQQuickShapeGenericRendererCall1)(const void *, int, const QColor *, int *);
typedef void (*CuteQQuickShapeGenericRendererCall2)(const void *, int, qreal, int *);
typedef void (*CuteQQuickShapeGenericRendererCall3)(const void *, int, bool, int *);
typedef void (*CuteQQuickShapeGenericRendererCall4)(const void *, int, const QColor *, int *);
typedef void (*CuteQQuickShapeGenericRendererCall5)(const void *, int, int, int *);
typedef void (*CuteQQuickShapeGenericRendererCall6)(const void *, int, int, int, int *);
typedef void (*CuteQQuickShapeGenericRendererCall7)(const void *, int, int, int *);
typedef void (*CuteQQuickShapeGenericRendererCall8)(const void *, int, QQuickShapeGradient *, int *);
typedef void (*CuteQQuickShapeGenericRendererCall9)(const void *, int, QQuickShapeGradient *, int *);
typedef void (*CuteQQuickShapeGenericRendererCall10)(const void *, int, QQuickItem *, int *);
typedef void (*CuteQQuickShapeGenericRendererCall11)(const void *, int, const QSGTransform *, int *);
typedef void (*CuteQQuickShapeGenericRendererCall12)(const void *, int, qreal, int *);
typedef void (*CuteQQuickShapeGenericRendererCall13)(const void *, bool, int *);
typedef int (*CuteQQuickShapeGenericRendererCall14)(const void *, int *);
typedef void (*CuteQQuickShapeGenericRendererCall15)(const void *, QQuickWindow *, int *);
typedef void (*CuteQQuickShapeGenericRendererCall16)(const void *, int *);
typedef void (*CuteQQuickShapeGenericRendererCall17)(const void *, int, const QQuickPath *, int *);
class CuteQQuickShapeGenericRenderer : public QQuickShapeGenericRenderer {
public:
  using QQuickShapeGenericRenderer::QQuickShapeGenericRenderer;
  CuteQQuickShapeGenericRenderer(const QQuickShapeGenericRenderer & other) : QQuickShapeGenericRenderer(other) {}
  void *taken[18] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN26QQuickAbstractPathRenderer7setPathEiRK12QPainterPath6QFlagsIN15QQuickShapePath8PathHintEE")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN26QQuickAbstractPathRenderer14setStrokeColorEiRK6QColor")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN26QQuickAbstractPathRenderer14setStrokeWidthEid")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN26QQuickAbstractPathRenderer17setCosmeticStrokeEib")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN26QQuickAbstractPathRenderer12setFillColorEiRK6QColor")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN26QQuickAbstractPathRenderer11setFillRuleEiN15QQuickShapePath8FillRuleE")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN26QQuickAbstractPathRenderer12setJoinStyleEiN15QQuickShapePath9JoinStyleEi")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN26QQuickAbstractPathRenderer11setCapStyleEiN15QQuickShapePath8CapStyleE")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN26QQuickAbstractPathRenderer15setFillGradientEiP19QQuickShapeGradient")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN26QQuickAbstractPathRenderer17setStrokeGradientEiP19QQuickShapeGradient")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN26QQuickAbstractPathRenderer22setFillTextureProviderEiP10QQuickItem")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN26QQuickAbstractPathRenderer16setFillTransformEiRK12QSGTransform")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN26QQuickAbstractPathRenderer21setTriangulationScaleEid")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN26QQuickAbstractPathRenderer7endSyncEb")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK26QQuickAbstractPathRenderer5flagsEv")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN26QQuickAbstractPathRenderer17handleSceneChangeEP12QQuickWindow")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN26QQuickAbstractPathRenderer10updateNodeEv")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN26QQuickAbstractPathRenderer7setPathEiPK10QQuickPath")) {
      taken[17] = call;
      return true;
    }
    return false;
  }

  //  void QQuickShapeGenericRenderer::setPath(int index, const
  //      QPainterPath &path, QQuickShapePath::PathHints pathHints)
  void setPath(
      int index,
      const QPainterPath &path,
      QQuickShapePath::PathHints pathHints) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickShapeGenericRendererCall0 call = reinterpret_cast<CuteQQuickShapeGenericRendererCall0>(taken[0]);
      call(this, index, &path, static_cast<int>(pathHints.toInt()), &handled);
      if (handled) return;
    }
    QQuickShapeGenericRenderer::setPath(index, path, pathHints);
  }

  //  void QQuickShapeGenericRenderer::setStrokeColor(int index, const
  //      QColor &color)
  void setStrokeColor(int index, const QColor &color) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickShapeGenericRendererCall1 call = reinterpret_cast<CuteQQuickShapeGenericRendererCall1>(taken[1]);
      call(this, index, &color, &handled);
      if (handled) return;
    }
    QQuickShapeGenericRenderer::setStrokeColor(index, color);
  }

  //  void QQuickShapeGenericRenderer::setStrokeWidth(int index, qreal w)
  void setStrokeWidth(int index, qreal w) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickShapeGenericRendererCall2 call = reinterpret_cast<CuteQQuickShapeGenericRendererCall2>(taken[2]);
      call(this, index, w, &handled);
      if (handled) return;
    }
    QQuickShapeGenericRenderer::setStrokeWidth(index, w);
  }

  //  void QQuickShapeGenericRenderer::setCosmeticStroke(int index, bool c)
  void setCosmeticStroke(int index, bool c) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickShapeGenericRendererCall3 call = reinterpret_cast<CuteQQuickShapeGenericRendererCall3>(taken[3]);
      call(this, index, c, &handled);
      if (handled) return;
    }
    QQuickShapeGenericRenderer::setCosmeticStroke(index, c);
  }

  //  void QQuickShapeGenericRenderer::setFillColor(int index, const QColor
  //      &color)
  void setFillColor(int index, const QColor &color) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickShapeGenericRendererCall4 call = reinterpret_cast<CuteQQuickShapeGenericRendererCall4>(taken[4]);
      call(this, index, &color, &handled);
      if (handled) return;
    }
    QQuickShapeGenericRenderer::setFillColor(index, color);
  }

  //  void QQuickShapeGenericRenderer::setFillRule(int index,
  //      QQuickShapePath::FillRule fillRule)
  void setFillRule(int index, QQuickShapePath::FillRule fillRule) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickShapeGenericRendererCall5 call = reinterpret_cast<CuteQQuickShapeGenericRendererCall5>(taken[5]);
      call(this, index, static_cast<int>(fillRule), &handled);
      if (handled) return;
    }
    QQuickShapeGenericRenderer::setFillRule(index, fillRule);
  }

  //  void QQuickShapeGenericRenderer::setJoinStyle(int index,
  //      QQuickShapePath::JoinStyle joinStyle, int miterLimit)
  void setJoinStyle(
      int index,
      QQuickShapePath::JoinStyle joinStyle,
      int miterLimit) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickShapeGenericRendererCall6 call = reinterpret_cast<CuteQQuickShapeGenericRendererCall6>(taken[6]);
      call(this, index, static_cast<int>(joinStyle), miterLimit, &handled);
      if (handled) return;
    }
    QQuickShapeGenericRenderer::setJoinStyle(index, joinStyle, miterLimit);
  }

  //  void QQuickShapeGenericRenderer::setCapStyle(int index,
  //      QQuickShapePath::CapStyle capStyle)
  void setCapStyle(int index, QQuickShapePath::CapStyle capStyle) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickShapeGenericRendererCall7 call = reinterpret_cast<CuteQQuickShapeGenericRendererCall7>(taken[7]);
      call(this, index, static_cast<int>(capStyle), &handled);
      if (handled) return;
    }
    QQuickShapeGenericRenderer::setCapStyle(index, capStyle);
  }

  //  void QQuickShapeGenericRenderer::setFillGradient(int index,
  //      QQuickShapeGradient *gradient)
  void setFillGradient(int index, QQuickShapeGradient *gradient) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickShapeGenericRendererCall8 call = reinterpret_cast<CuteQQuickShapeGenericRendererCall8>(taken[8]);
      call(this, index, gradient, &handled);
      if (handled) return;
    }
    QQuickShapeGenericRenderer::setFillGradient(index, gradient);
  }

  //  void QQuickShapeGenericRenderer::setStrokeGradient(int index,
  //      QQuickShapeGradient *gradient)
  void setStrokeGradient(int index, QQuickShapeGradient *gradient) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickShapeGenericRendererCall9 call = reinterpret_cast<CuteQQuickShapeGenericRendererCall9>(taken[9]);
      call(this, index, gradient, &handled);
      if (handled) return;
    }
    QQuickShapeGenericRenderer::setStrokeGradient(index, gradient);
  }

  //  void QQuickShapeGenericRenderer::setFillTextureProvider(int index,
  //      QQuickItem *textureProviderItem)
  void setFillTextureProvider(
      int index,
      QQuickItem *textureProviderItem) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickShapeGenericRendererCall10 call = reinterpret_cast<CuteQQuickShapeGenericRendererCall10>(taken[10]);
      call(this, index, textureProviderItem, &handled);
      if (handled) return;
    }
    QQuickShapeGenericRenderer::setFillTextureProvider(index, textureProviderItem);
  }

  //  void QQuickShapeGenericRenderer::setFillTransform(int index, const
  //      QSGTransform &transform)
  void setFillTransform(int index, const QSGTransform &transform) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickShapeGenericRendererCall11 call = reinterpret_cast<CuteQQuickShapeGenericRendererCall11>(taken[11]);
      call(this, index, &transform, &handled);
      if (handled) return;
    }
    QQuickShapeGenericRenderer::setFillTransform(index, transform);
  }

  //  void QQuickShapeGenericRenderer::setTriangulationScale(int index,
  //      qreal scale)
  void setTriangulationScale(int index, qreal scale) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickShapeGenericRendererCall12 call = reinterpret_cast<CuteQQuickShapeGenericRendererCall12>(taken[12]);
      call(this, index, scale, &handled);
      if (handled) return;
    }
    QQuickShapeGenericRenderer::setTriangulationScale(index, scale);
  }

  //  void QQuickShapeGenericRenderer::endSync(bool async)
  void endSync(bool async) override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickShapeGenericRendererCall13 call = reinterpret_cast<CuteQQuickShapeGenericRendererCall13>(taken[13]);
      call(this, async, &handled);
      if (handled) return;
    }
    QQuickShapeGenericRenderer::endSync(async);
  }

  //  Flags QQuickShapeGenericRenderer::flags() const
  QQuickAbstractPathRenderer::Flags flags() const override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickShapeGenericRendererCall14 call = reinterpret_cast<CuteQQuickShapeGenericRendererCall14>(taken[14]);
      int given = call(this, &handled);
      if (handled) return QFlags<QQuickAbstractPathRenderer::Flag>::fromInt(given);
    }
    return QQuickShapeGenericRenderer::flags();
  }

  //  void QQuickShapeGenericRenderer::handleSceneChange(QQuickWindow
  //      *window)
  void handleSceneChange(QQuickWindow *window) override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickShapeGenericRendererCall15 call = reinterpret_cast<CuteQQuickShapeGenericRendererCall15>(taken[15]);
      call(this, window, &handled);
      if (handled) return;
    }
    QQuickShapeGenericRenderer::handleSceneChange(window);
  }

  //  void QQuickShapeGenericRenderer::updateNode()
  void updateNode() override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickShapeGenericRendererCall16 call = reinterpret_cast<CuteQQuickShapeGenericRendererCall16>(taken[16]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickShapeGenericRenderer::updateNode();
  }

  //  void QQuickAbstractPathRenderer::setPath(int index, const QQuickPath
  //      *path)
  void setPath(int index, const QQuickPath *path) override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickShapeGenericRendererCall17 call = reinterpret_cast<CuteQQuickShapeGenericRendererCall17>(taken[17]);
      call(this, index, path, &handled);
      if (handled) return;
    }
    QQuickAbstractPathRenderer::setPath(index, path);
  }
};

//  QQuickShapeGenericRenderer::~QQuickShapeGenericRenderer()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickShapeGenericRendererD1Ev(
    QQuickShapeGenericRenderer *self) {
  delete self;
}

//  void QQuickShapeGenericRenderer::beginSync(int totalCount, bool
//      *countChanged)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickShapeGenericRenderer9beginSyncEiPb(
    QQuickShapeGenericRenderer *self,
    int totalCount,
    bool *countChanged) {
  self->beginSync(totalCount, countChanged);
}

//  void QQuickShapeGenericRenderer::setPath(int index, const QPainterPath
//      &path, QQuickShapePath::PathHints pathHints)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickShapeGenericRenderer7setPathEiRK12QPainterPath6QFlagsIN15QQuickShapePath8PathHintEE(
    QQuickShapeGenericRenderer *self,
    int index,
    const QPainterPath *path,
    int pathHints) {
  self->setPath(
      index,
      *path,
      QFlags<QQuickShapePath::PathHint>::fromInt(pathHints));
}

//  void QQuickShapeGenericRenderer::setStrokeColor(int index, const QColor
//      &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickShapeGenericRenderer14setStrokeColorEiRK6QColor(
    QQuickShapeGenericRenderer *self,
    int index,
    const QColor *color) {
  self->setStrokeColor(index, *color);
}

//  void QQuickShapeGenericRenderer::setStrokeWidth(int index, qreal w)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickShapeGenericRenderer14setStrokeWidthEid(
    QQuickShapeGenericRenderer *self,
    int index,
    qreal w) {
  self->setStrokeWidth(index, w);
}

//  void QQuickShapeGenericRenderer::setCosmeticStroke(int index, bool c)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickShapeGenericRenderer17setCosmeticStrokeEib(
    QQuickShapeGenericRenderer *self,
    int index,
    bool c) {
  self->setCosmeticStroke(index, c);
}

//  void QQuickShapeGenericRenderer::setFillColor(int index, const QColor
//      &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickShapeGenericRenderer12setFillColorEiRK6QColor(
    QQuickShapeGenericRenderer *self,
    int index,
    const QColor *color) {
  self->setFillColor(index, *color);
}

//  void QQuickShapeGenericRenderer::setFillRule(int index,
//      QQuickShapePath::FillRule fillRule)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickShapeGenericRenderer11setFillRuleEiN15QQuickShapePath8FillRuleE(
    QQuickShapeGenericRenderer *self,
    int index,
    QQuickShapePath::FillRule fillRule) {
  self->setFillRule(index, fillRule);
}

//  void QQuickShapeGenericRenderer::setJoinStyle(int index,
//      QQuickShapePath::JoinStyle joinStyle, int miterLimit)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickShapeGenericRenderer12setJoinStyleEiN15QQuickShapePath9JoinStyleEi(
    QQuickShapeGenericRenderer *self,
    int index,
    QQuickShapePath::JoinStyle joinStyle,
    int miterLimit) {
  self->setJoinStyle(index, joinStyle, miterLimit);
}

//  void QQuickShapeGenericRenderer::setCapStyle(int index,
//      QQuickShapePath::CapStyle capStyle)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickShapeGenericRenderer11setCapStyleEiN15QQuickShapePath8CapStyleE(
    QQuickShapeGenericRenderer *self,
    int index,
    QQuickShapePath::CapStyle capStyle) {
  self->setCapStyle(index, capStyle);
}

//  void QQuickShapeGenericRenderer::setStrokeStyle(int index,
//      QQuickShapePath::StrokeStyle strokeStyle, qreal dashOffset, const
//      QList<qreal> &dashPattern)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickShapeGenericRenderer14setStrokeStyleEiN15QQuickShapePath11StrokeStyleEdRK5QListIdE(
    QQuickShapeGenericRenderer *self,
    int index,
    QQuickShapePath::StrokeStyle strokeStyle,
    qreal dashOffset,
    const QList<qreal> *dashPattern) {
  self->setStrokeStyle(index, strokeStyle, dashOffset, *dashPattern);
}

//  void QQuickShapeGenericRenderer::setFillGradient(int index,
//      QQuickShapeGradient *gradient)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickShapeGenericRenderer15setFillGradientEiP19QQuickShapeGradient(
    QQuickShapeGenericRenderer *self,
    int index,
    QQuickShapeGradient *gradient) {
  self->setFillGradient(index, gradient);
}

//  void QQuickShapeGenericRenderer::setStrokeGradient(int index,
//      QQuickShapeGradient *gradient)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickShapeGenericRenderer17setStrokeGradientEiP19QQuickShapeGradient(
    QQuickShapeGenericRenderer *self,
    int index,
    QQuickShapeGradient *gradient) {
  self->setStrokeGradient(index, gradient);
}

//  void QQuickShapeGenericRenderer::setFillTextureProvider(int index,
//      QQuickItem *textureProviderItem)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickShapeGenericRenderer22setFillTextureProviderEiP10QQuickItem(
    QQuickShapeGenericRenderer *self,
    int index,
    QQuickItem *textureProviderItem) {
  self->setFillTextureProvider(index, textureProviderItem);
}

//  void QQuickShapeGenericRenderer::setFillTransform(int index, const
//      QSGTransform &transform)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickShapeGenericRenderer16setFillTransformEiRK12QSGTransform(
    QQuickShapeGenericRenderer *self,
    int index,
    const QSGTransform *transform) {
  self->setFillTransform(index, *transform);
}

//  void QQuickShapeGenericRenderer::setTriangulationScale(int index, qreal
//      scale)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickShapeGenericRenderer21setTriangulationScaleEid(
    QQuickShapeGenericRenderer *self,
    int index,
    qreal scale) {
  self->setTriangulationScale(index, scale);
}

//  void QQuickShapeGenericRenderer::endSync(bool async)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickShapeGenericRenderer7endSyncEb(
    QQuickShapeGenericRenderer *self,
    bool async) {
  self->endSync(async);
}

//  void QQuickShapeGenericRenderer::setAsyncCallback(void (*)(void *) a0,
//      void *a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickShapeGenericRenderer16setAsyncCallbackEPFvPvES0_(
    QQuickShapeGenericRenderer *self,
    void *a0,
    void *a1) {
  self->setAsyncCallback(reinterpret_cast<void (*)(void *)>(a0), a1);
}

//  Flags QQuickShapeGenericRenderer::flags() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK26QQuickShapeGenericRenderer5flagsEv(
    const QQuickShapeGenericRenderer *self) {
  return static_cast<int>(self->flags().toInt());
}

//  void QQuickShapeGenericRenderer::handleSceneChange(QQuickWindow *window)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickShapeGenericRenderer17handleSceneChangeEP12QQuickWindow(
    QQuickShapeGenericRenderer *self,
    QQuickWindow *window) {
  self->handleSceneChange(window);
}

//  void QQuickShapeGenericRenderer::updateNode()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickShapeGenericRenderer10updateNodeEv(
    QQuickShapeGenericRenderer *self) {
  self->updateNode();
}

//  void QQuickShapeGenericRenderer::setRootNode(QQuickShapeGenericNode
//      *node)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickShapeGenericRenderer11setRootNodeEP22QQuickShapeGenericNode(
    QQuickShapeGenericRenderer *self,
    QQuickShapeGenericNode *node) {
  self->setRootNode(node);
}

//  void QQuickShapeGenericRenderer::triangulateFill(const QPainterPath
//      &path, const Color4ub &fillColor, VertexContainerType *fillVertices,
//      IndexContainerType *fillIndices, QSGGeometry::Type *indexType, bool
//      supportsElementIndexUint, qreal triangulationScale)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickShapeGenericRenderer15triangulateFillERK12QPainterPathRKNS_8Color4ubEP5QListIN11QSGGeometry14ColoredPoint2DEEPS6_IjEPNS7_4TypeEbd(
    const QPainterPath *path,
    const QQuickShapeGenericRenderer::Color4ub *fillColor,
    QQuickShapeGenericRenderer::VertexContainerType *fillVertices,
    QQuickShapeGenericRenderer::IndexContainerType *fillIndices,
    QSGGeometry::Type *indexType,
    bool supportsElementIndexUint,
    qreal triangulationScale) {
  QQuickShapeGenericRenderer::triangulateFill(
      *path,
      *fillColor,
      fillVertices,
      fillIndices,
      indexType,
      supportsElementIndexUint,
      triangulationScale);
}

//  void QQuickShapeGenericRenderer::maybeUpdateAsyncItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickShapeGenericRenderer20maybeUpdateAsyncItemEv(
    QQuickShapeGenericRenderer *self) {
  self->maybeUpdateAsyncItem();
}

//  a Python function taken by a CuteQQuickShapeGenericRenderer, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickShapeGenericRenderer(
    QQuickShapeGenericRenderer *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickShapeGenericRenderer *>(self)->take(key, call);
}

//  void QQuickShapeGenericRenderer::setPath(int index, const QPainterPath
//      &path, QQuickShapePath::PathHints pathHints)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN26QQuickShapeGenericRenderer7setPathEiRK12QPainterPath6QFlagsIN15QQuickShapePath8PathHintEE(
    QQuickShapeGenericRenderer *self,
    int index,
    const QPainterPath *path,
    int pathHints) {
  self->QQuickShapeGenericRenderer::setPath(
      index,
      *path,
      QFlags<QQuickShapePath::PathHint>::fromInt(pathHints));
}

//  void QQuickShapeGenericRenderer::setStrokeWidth(int index, qreal w)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN26QQuickShapeGenericRenderer14setStrokeWidthEid(
    QQuickShapeGenericRenderer *self,
    int index,
    qreal w) {
  self->QQuickShapeGenericRenderer::setStrokeWidth(index, w);
}

//  void QQuickShapeGenericRenderer::setCosmeticStroke(int index, bool c)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN26QQuickShapeGenericRenderer17setCosmeticStrokeEib(
    QQuickShapeGenericRenderer *self,
    int index,
    bool c) {
  self->QQuickShapeGenericRenderer::setCosmeticStroke(index, c);
}

//  void QQuickShapeGenericRenderer::setFillColor(int index, const QColor
//      &color)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN26QQuickShapeGenericRenderer12setFillColorEiRK6QColor(
    QQuickShapeGenericRenderer *self,
    int index,
    const QColor *color) {
  self->QQuickShapeGenericRenderer::setFillColor(index, *color);
}

//  void QQuickShapeGenericRenderer::setFillRule(int index,
//      QQuickShapePath::FillRule fillRule)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN26QQuickShapeGenericRenderer11setFillRuleEiN15QQuickShapePath8FillRuleE(
    QQuickShapeGenericRenderer *self,
    int index,
    QQuickShapePath::FillRule fillRule) {
  self->QQuickShapeGenericRenderer::setFillRule(index, fillRule);
}

//  void QQuickShapeGenericRenderer::setJoinStyle(int index,
//      QQuickShapePath::JoinStyle joinStyle, int miterLimit)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN26QQuickShapeGenericRenderer12setJoinStyleEiN15QQuickShapePath9JoinStyleEi(
    QQuickShapeGenericRenderer *self,
    int index,
    QQuickShapePath::JoinStyle joinStyle,
    int miterLimit) {
  self->QQuickShapeGenericRenderer::setJoinStyle(
      index,
      joinStyle,
      miterLimit);
}

//  void QQuickShapeGenericRenderer::setCapStyle(int index,
//      QQuickShapePath::CapStyle capStyle)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN26QQuickShapeGenericRenderer11setCapStyleEiN15QQuickShapePath8CapStyleE(
    QQuickShapeGenericRenderer *self,
    int index,
    QQuickShapePath::CapStyle capStyle) {
  self->QQuickShapeGenericRenderer::setCapStyle(index, capStyle);
}

//  void QQuickShapeGenericRenderer::setFillGradient(int index,
//      QQuickShapeGradient *gradient)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN26QQuickShapeGenericRenderer15setFillGradientEiP19QQuickShapeGradient(
    QQuickShapeGenericRenderer *self,
    int index,
    QQuickShapeGradient *gradient) {
  self->QQuickShapeGenericRenderer::setFillGradient(index, gradient);
}

//  void QQuickShapeGenericRenderer::setFillTextureProvider(int index,
//      QQuickItem *textureProviderItem)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN26QQuickShapeGenericRenderer22setFillTextureProviderEiP10QQuickItem(
    QQuickShapeGenericRenderer *self,
    int index,
    QQuickItem *textureProviderItem) {
  self->QQuickShapeGenericRenderer::setFillTextureProvider(
      index,
      textureProviderItem);
}

//  void QQuickShapeGenericRenderer::setFillTransform(int index, const
//      QSGTransform &transform)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN26QQuickShapeGenericRenderer16setFillTransformEiRK12QSGTransform(
    QQuickShapeGenericRenderer *self,
    int index,
    const QSGTransform *transform) {
  self->QQuickShapeGenericRenderer::setFillTransform(index, *transform);
}

//  void QQuickShapeGenericRenderer::setTriangulationScale(int index, qreal
//      scale)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN26QQuickShapeGenericRenderer21setTriangulationScaleEid(
    QQuickShapeGenericRenderer *self,
    int index,
    qreal scale) {
  self->QQuickShapeGenericRenderer::setTriangulationScale(index, scale);
}

//  Flags QQuickShapeGenericRenderer::flags() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK26QQuickShapeGenericRenderer5flagsEv(
    const QQuickShapeGenericRenderer *self) {
  return static_cast<int>(self->QQuickShapeGenericRenderer::flags().toInt());
}

//  void QQuickShapeGenericRenderer::handleSceneChange(QQuickWindow *window)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN26QQuickShapeGenericRenderer17handleSceneChangeEP12QQuickWindow(
    QQuickShapeGenericRenderer *self,
    QQuickWindow *window) {
  self->QQuickShapeGenericRenderer::handleSceneChange(window);
}
