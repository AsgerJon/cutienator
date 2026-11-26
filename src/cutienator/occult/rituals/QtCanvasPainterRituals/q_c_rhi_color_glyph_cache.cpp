//  Written by dev_tooling.RitualGenerator from the records of
//  QtCanvasPainter/6.12.0/QtCanvasPainter/private/qcrhicolorglyphcache_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCanvasPainter/QtCanvasPainter>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCanvasPainter/6.12.0/QtCanvasPainter/private/qcrhicolorglyphcache_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qpoint.h>
#include <QtGui/qglyphrun.h>
#include <QtGui/qcolor.h>
#include <QtGui/qtransform.h>
#include <QtCore/qsize.h>
#include <QtCore/qrect.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCanvasPainter/private/qcareaallocator_p.h>
#include <QtCanvasPainter/private/qcrhicolorglyphcache_p.h>
#include <QtGui/private/qrawfont_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcareaallocator.cpp, line 10, as local:qcareaallocator.cpp:QCAreaAllocatorNode
struct QCAreaAllocatorNode
{
    enum class SplitType { VerticalSplit, HorizontalSplit };

    QCAreaAllocatorNode(QCAreaAllocatorNode *parent);
    ~QCAreaAllocatorNode();
    inline bool isLeaf();

    QCAreaAllocatorNode *parent = nullptr;
    QCAreaAllocatorNode *left = nullptr;
    QCAreaAllocatorNode *right = nullptr;
    int split; // only valid for inner nodes.
    SplitType splitType;
    bool isOccupied = false; // only valid for leaf nodes.
};

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcareaallocator.cpp, line 26, as local:qcareaallocator.cpp:QCAreaAllocatorNode::QCAreaAllocatorNode
inline QCAreaAllocatorNode::QCAreaAllocatorNode(QCAreaAllocatorNode *parent)
    : parent(parent)
{}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcareaallocator.cpp, line 30, as local:qcareaallocator.cpp:QCAreaAllocatorNode::~QCAreaAllocatorNode
inline QCAreaAllocatorNode::~QCAreaAllocatorNode()
{
    delete left;
    delete right;
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcareaallocator.cpp, line 36, as local:qcareaallocator.cpp:QCAreaAllocatorNode::isLeaf
inline bool QCAreaAllocatorNode::isLeaf()
{
    Q_ASSERT((left != nullptr) == (right != nullptr));
    return !left;
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcrhicolorglyphcache.cpp, line 12, as local:qcrhicolorglyphcache.cpp:QC_COLOR_GLYPH_PADDING
static constexpr int QC_COLOR_GLYPH_PADDING = 1;

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcrhicolorglyphcache.cpp, line 104, as local:qcrhicolorglyphcache.cpp:allocationRect
static inline QRect allocationRect(const QRect &atlasRect)
{
    return QRect(atlasRect.x() - QC_COLOR_GLYPH_PADDING,
                 atlasRect.y() - QC_COLOR_GLYPH_PADDING,
                 atlasRect.width() + QC_COLOR_GLYPH_PADDING * 2,
                 atlasRect.height() + QC_COLOR_GLYPH_PADDING * 2);
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcareaallocator.cpp, line 48, as _ZN15QCAreaAllocatorD1Ev
inline QCAreaAllocator::~QCAreaAllocator()
{
    delete m_root;
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcrhicolorglyphcache.cpp, line 140, as _ZN20QCRhiColorGlyphCache11ensureGlyphERKNS_8GlyphKeyEP11QFontEngine6QColorRK10QTransform
inline const QCRhiColorGlyphCache::GlyphData &
QCRhiColorGlyphCache::ensureGlyph(const GlyphKey &key, QFontEngine *fe,
                                  QColor color, const QTransform &rasterTransform)
{
    auto it = m_glyphs.find(key);
    if (it != m_glyphs.end()) {
        if (it->valid)
            referenceGlyph(key, it.value());
        return it.value();
    }

    GlyphData gd;

    ensureAtlas();
    if (!m_atlas)
        return m_invalidGlyph;

    // The bitmap is already in Format_ARGB32_Premultiplied for color fonts.
    QImage bitmap = fe->bitmapForGlyph(key.glyph, QFixedPoint(), rasterTransform, color);
    if (bitmap.isNull())
        return *m_glyphs.insert(key, gd); // permanently invalid: no color bitmap for this glyph

    if (bitmap.format() != QImage::Format_RGBA8888_Premultiplied)
        bitmap = bitmap.convertToFormat(QImage::Format_RGBA8888_Premultiplied);

    const QSize glyphSize = bitmap.size();
    const QSize allocSize(glyphSize.width() + QC_COLOR_GLYPH_PADDING * 2,
                          glyphSize.height() + QC_COLOR_GLYPH_PADDING * 2);
    QRect alloc = m_allocator->allocate(allocSize);
    if (alloc.isNull())
        alloc = evictUntilAllocated(allocSize);
    if (alloc.isNull()) {
        qWarning("Color glyph atlas full; emoji glyph dropped");
        return m_invalidGlyph;
    }

    // The allocator hands out positions across the full (max) coordinate space;
    // grow the physical texture to cover this allocation before uploading into
    // it. The allocation is bounded by m_maxAtlasSize, so the grow always
    // succeeds in reaching it.
    const int required = qMax(alloc.x() + alloc.width(), alloc.y() + alloc.height());
    if (required > m_atlasSize)
        growAtlas(required);

    const QPoint dst = alloc.topLeft() + QPoint(QC_COLOR_GLYPH_PADDING, QC_COLOR_GLYPH_PADDING);

    QRhiTextureSubresourceUploadDescription subres(bitmap.constBits(), bitmap.sizeInBytes());
    subres.setSourceSize(glyphSize);
    subres.setDestinationTopLeft(dst);
    m_batch->uploadTexture(m_atlas, QRhiTextureUploadEntry(0, 0, subres));

    if (useTextureResizeWorkaround()) {
        const int bytesPerRow = glyphSize.width() * 4;
        for (int row = 0; row < glyphSize.height(); ++row) {
            memcpy(m_atlasImage.scanLine(dst.y() + row) + dst.x() * 4,
                   bitmap.constScanLine(row),
                   bytesPerRow);
        }
    }

    // Bearing: where the bitmap's top-left sits relative to the glyph pen
    // position on the baseline (alphaMapBoundingBox returns this offset).
    const glyph_metrics_t gm =
        fe->alphaMapBoundingBox(key.glyph, QFixedPoint(), rasterTransform,
                                QFontEngine::Format_ARGB);

    gd.atlasRect = QRect(dst, glyphSize);
    gd.bearing = QPointF(gm.x.toReal(), gm.y.toReal());
    gd.valid = true;
    GlyphData &stored = *m_glyphs.insert(key, gd);
    referenceGlyph(key, stored);
    return stored;
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcareaallocator.cpp, line 42, as _ZN15QCAreaAllocatorC1E5QSize
inline QCAreaAllocator::QCAreaAllocator(QSize size)
    : m_size(size)
{
    m_root = new QCAreaAllocatorNode(nullptr);
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcareaallocator.cpp, line 60, as _ZN15QCAreaAllocator10deallocateE5QRect
inline bool QCAreaAllocator::deallocate(QRect rect)
{
    return deallocateInNode(rect.topLeft(), m_root);
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcareaallocator.cpp, line 53, as _ZN15QCAreaAllocator8allocateE5QSize
inline QRect QCAreaAllocator::allocate(QSize size)
{
    QPoint point;
    bool result = allocateInNode(size, point, QRect(QPoint(0, 0), m_size), m_root);
    return result ? QRect(point, size) : QRect();
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcareaallocator.cpp, line 65, as _ZN15QCAreaAllocator14allocateInNodeE5QSizeR6QPoint5QRectP19QCAreaAllocatorNode
inline bool QCAreaAllocator::allocateInNode(
    QSize size, QPoint &result, QRect currentRect, QCAreaAllocatorNode *node)
{
    if (size.width() > currentRect.width() || size.height() > currentRect.height())
        return false;

    if (node->isLeaf()) {
        if (node->isOccupied)
            return false;
        const int maxMargin = 2;
        if (size.width() + maxMargin >= currentRect.width()
            && size.height() + maxMargin >= currentRect.height()) {
            // Snug fit, occupy entire rectangle.
            node->isOccupied = true;
            result = currentRect.topLeft();
            return true;
        }
        // TODO: Reuse nodes.
        // Split node.
        node->left = new QCAreaAllocatorNode(node);
        node->right = new QCAreaAllocatorNode(node);
        QRect splitRect = currentRect;
        if ((currentRect.width() - size.width()) * currentRect.height()
            < (currentRect.height() - size.height()) * currentRect.width()) {
            node->splitType = QCAreaAllocatorNode::SplitType::HorizontalSplit;
            node->split = currentRect.top() + size.height();
            splitRect.setHeight(size.height());
        } else {
            node->splitType = QCAreaAllocatorNode::SplitType::VerticalSplit;
            node->split = currentRect.left() + size.width();
            splitRect.setWidth(size.width());
        }
        return allocateInNode(size, result, splitRect, node->left);
    } else {
        // TODO: avoid unnecessary recursion.
        //  has been split.
        QRect leftRect = currentRect;
        QRect rightRect = currentRect;
        if (node->splitType == QCAreaAllocatorNode::SplitType::HorizontalSplit) {
            leftRect.setHeight(node->split - leftRect.top());
            rightRect.setTop(node->split);
        } else {
            leftRect.setWidth(node->split - leftRect.left());
            rightRect.setLeft(node->split);
        }
        if (allocateInNode(size, result, leftRect, node->left))
            return true;
        if (allocateInNode(size, result, rightRect, node->right))
            return true;
        return false;
    }
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcareaallocator.cpp, line 118, as _ZN15QCAreaAllocator16deallocateInNodeE6QPointP19QCAreaAllocatorNode
inline bool QCAreaAllocator::deallocateInNode(QPoint pos, QCAreaAllocatorNode *node)
{
    while (!node->isLeaf()) {
        //  has been split.
        int cmp = node->splitType == QCAreaAllocatorNode::SplitType::HorizontalSplit ? pos.y()
                                                                                    : pos.x();
        node = cmp < node->split ? node->left : node->right;
    }
    if (!node->isOccupied)
        return false;
    node->isOccupied = false;
    mergeNodeWithNeighbors(node);
    return true;
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcareaallocator.cpp, line 133, as _ZN15QCAreaAllocator22mergeNodeWithNeighborsEP19QCAreaAllocatorNode
inline void QCAreaAllocator::mergeNodeWithNeighbors(QCAreaAllocatorNode *node)
{
    bool done = false;
    QCAreaAllocatorNode *parent = nullptr;
    QCAreaAllocatorNode *current = nullptr;
    QCAreaAllocatorNode *sibling;
    while (!done) {
        Q_ASSERT(node->isLeaf());
        Q_ASSERT(!node->isOccupied);
        if (node->parent == nullptr)
            return; // No neighbors.

        QCAreaAllocatorNode::SplitType splitType = QCAreaAllocatorNode::SplitType(
            node->parent->splitType);
        done = true;

        // Merge with left neighbor.
        current = node;
        parent = current->parent;
        while (parent && current == parent->left && parent->splitType == splitType) {
            current = parent;
            parent = parent->parent;
        }

        if (parent && parent->splitType == splitType) {
            Q_ASSERT(current == parent->right);
            Q_ASSERT(parent->left);

            QCAreaAllocatorNode *neighbor = parent->left;
            while (neighbor->right && neighbor->splitType == splitType)
                neighbor = neighbor->right;

            if (neighbor->isLeaf() && neighbor->parent->splitType == splitType
                && !neighbor->isOccupied) {
                // Left neighbor can be merged.
                parent->split = neighbor->parent->split;

                parent = neighbor->parent;
                sibling = neighbor == parent->left ? parent->right : parent->left;
                QCAreaAllocatorNode **nodeRef = &m_root;
                if (parent->parent) {
                    if (parent == parent->parent->left)
                        nodeRef = &parent->parent->left;
                    else
                        nodeRef = &parent->parent->right;
                }
                sibling->parent = parent->parent;
                *nodeRef = sibling;
                parent->left = parent->right = nullptr;
                delete parent;
                delete neighbor;
                done = false;
            }
        }

        // Merge with right neighbor.
        current = node;
        parent = current->parent;
        while (parent && current == parent->right && parent->splitType == splitType) {
            current = parent;
            parent = parent->parent;
        }

        if (parent && parent->splitType == splitType) {
            Q_ASSERT(current == parent->left);
            Q_ASSERT(parent->right);

            QCAreaAllocatorNode *neighbor = parent->right;
            while (neighbor->left && neighbor->splitType == splitType)
                neighbor = neighbor->left;

            if (neighbor->isLeaf() && neighbor->parent->splitType == splitType
                && !neighbor->isOccupied) {
                // Right neighbor can be merged.
                parent->split = neighbor->parent->split;

                parent = neighbor->parent;
                sibling = neighbor == parent->left ? parent->right : parent->left;
                QCAreaAllocatorNode **nodeRef = &m_root;
                if (parent->parent) {
                    if (parent == parent->parent->left)
                        nodeRef = &parent->parent->left;
                    else
                        nodeRef = &parent->parent->right;
                }
                sibling->parent = parent->parent;
                *nodeRef = sibling;
                parent->left = parent->right = nullptr;
                delete parent;
                delete neighbor;
                done = false;
            }
        }
    } // end while (!done)
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcrhicolorglyphcache.cpp, line 14, as _ZN20QCRhiColorGlyphCacheC1EP4QRhi
inline QCRhiColorGlyphCache::QCRhiColorGlyphCache(QRhi *rhi)
    : m_rhi(rhi)
{
    m_batch = rhi->nextResourceUpdateBatch();
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcrhicolorglyphcache.cpp, line 20, as _ZN20QCRhiColorGlyphCacheD1Ev
inline QCRhiColorGlyphCache::~QCRhiColorGlyphCache()
{
    if (m_batch)
        m_batch->release();
    if (m_atlas)
        m_atlas->deleteLater();
    delete m_allocator;
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcrhicolorglyphcache.cpp, line 232, as _ZN20QCRhiColorGlyphCache11addGlyphRunE7QPointFRK9QGlyphRun6QColorRK10QTransformfP15QVarLengthArrayIN28QCRhiDistanceFieldGlyphCache15TexturedPoint2DELx256EEPS8_IjLx384EE
inline void QCRhiColorGlyphCache::addGlyphRun(QPointF glyphPos,
                                       const QGlyphRun &run,
                                       QColor color,
                                       const QTransform &transform,
                                       float devicePixelRatio,
                                       QCRhiDistanceFieldGlyphCache::VertexList *verts,
                                       QCRhiDistanceFieldGlyphCache::IndexList *indices)
{
    const QRawFont rawFont = run.rawFont();
    QFontEngine *fe = QRawFontPrivate::get(rawFont)->fontEngine;
    if (!fe || !fe->isColorFont())
        return;

    const QList<quint32> glyphIndexes = run.glyphIndexes();
    const QList<QPointF> positions = run.positions();
    const int count = qMin(glyphIndexes.size(), positions.size());

    const QFontEngine::FaceId faceId = fe->faceId();
    const int pixelSize = qRound(rawFont.pixelSize());
    // The color participates in the key because COLR fonts can have layers
    // painted in the text ("foreground") color.
    const QRgb rgba = color.rgba();

    // Rasterize at the device pixel ratio so the bitmaps match the physical
    // resolution of the render target; the quads below stay in logical
    // coordinates and the projection scales them back up. The painter
    // transform is still only applied to the quad corners (consistent with
    // the SDF path), so a scaling transform does reduce sharpness.
    qreal scale = devicePixelRatio > 0.0f ? devicePixelRatio : 1.0;
    QTransform rasterTransform = QTransform::fromScale(scale, scale);
    if (!fe->supportsTransformation(rasterTransform)) {
        scale = 1.0;
        rasterTransform = QTransform();
    }

    for (int i = 0; i < count; ++i) {
        const GlyphKey key{ faceId, glyphIndexes.at(i), pixelSize, float(scale), rgba };
        const GlyphData &gd = ensureGlyph(key, fe, color, rasterTransform);
        if (!gd.valid)
            continue;

        // Pen position on the baseline for this glyph, then offset by the
        // bearing. The bitmap and its metrics are in device pixels; divide by
        // the rasterization scale to get back to logical coordinates.
        const QPointF pen = glyphPos + positions.at(i);
        const qreal x = pen.x() + gd.bearing.x() / scale;
        const qreal y = pen.y() + gd.bearing.y() / scale;
        const qreal w = gd.atlasRect.width() / scale;
        const qreal h = gd.atlasRect.height() / scale;

        QPointF p1(x,     y);
        QPointF p2(x + w, y);
        QPointF p3(x,     y + h);
        QPointF p4(x + w, y + h);
        if (!transform.isIdentity()) {
            p1 = transform.map(p1);
            p2 = transform.map(p2);
            p3 = transform.map(p3);
            p4 = transform.map(p4);
        }

        // Texture coords in atlas texels (shader divides by textureSize()).
        const float tx1 = gd.atlasRect.x();
        const float ty1 = gd.atlasRect.y();
        const float tx2 = tx1 + float(gd.atlasRect.width());
        const float ty2 = ty1 + float(gd.atlasRect.height());

        const uint32_t base = uint32_t(verts->size());
        QCRhiDistanceFieldGlyphCache::TexturedPoint2D v;
        v.set(float(p1.x()), float(p1.y()), tx1, ty1); verts->append(v);
        v.set(float(p2.x()), float(p2.y()), tx2, ty1); verts->append(v);
        v.set(float(p3.x()), float(p3.y()), tx1, ty2); verts->append(v);
        v.set(float(p4.x()), float(p4.y()), tx2, ty2); verts->append(v);

        indices->append(base + 0);
        indices->append(base + 2);
        indices->append(base + 3);
        indices->append(base + 3);
        indices->append(base + 1);
        indices->append(base + 0);
    }
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcrhicolorglyphcache.cpp, line 315, as _ZN20QCRhiColorGlyphCache20commitResourceUpdateEP23QRhiResourceUpdateBatch
inline void QCRhiColorGlyphCache::commitResourceUpdate(QRhiResourceUpdateBatch *batch)
{
    batch->merge(m_batch);
    m_batch->release();
    m_batch = m_rhi->nextResourceUpdateBatch();
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcrhicolorglyphcache.cpp, line 225, as _ZN20QCRhiColorGlyphCache22optimizeAfterRenderingEv
inline void QCRhiColorGlyphCache::optimizeAfterRendering()
{
    releaseGlyphs(m_referencedPrevFrame);
    m_referencedPrevFrame.swap(m_referencedThisFrame);
    m_referencedThisFrame.clear();
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcrhicolorglyphcache.cpp, line 34, as _ZN20QCRhiColorGlyphCache11ensureAtlasEv
inline void QCRhiColorGlyphCache::ensureAtlas()
{
    if (m_atlas)
        return;

    m_maxAtlasSize = qMin(2048, m_rhi->resourceLimit(QRhi::TextureSizeMax));
    m_atlasSize = qMin(256, m_maxAtlasSize);
    m_atlas = m_rhi->newTexture(QRhiTexture::RGBA8, QSize(m_atlasSize, m_atlasSize), 1,
                                QRhiTexture::UsedAsTransferSource);
    m_atlas->setName("QCColorGlyphAtlas");
    if (!m_atlas->create()) {
        qWarning("Failed to create color glyph atlas");
        delete m_atlas;
        m_atlas = nullptr;
        return;
    }

    const QByteArray zeroBuf(m_atlasSize * m_atlasSize * 4, 0);
    QRhiTextureSubresourceUploadDescription zeroSubres(zeroBuf.constData(), zeroBuf.size());
    zeroSubres.setSourceSize(QSize(m_atlasSize, m_atlasSize));
    m_batch->uploadTexture(m_atlas, QRhiTextureUploadEntry(0, 0, zeroSubres));

    m_allocator = new QCAreaAllocator(QSize(m_maxAtlasSize, m_maxAtlasSize));

    if (useTextureResizeWorkaround()) {
        m_atlasImage = QImage(m_atlasSize, m_atlasSize, QImage::Format_RGBA8888_Premultiplied);
        m_atlasImage.fill(Qt::transparent);
    }
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcrhicolorglyphcache.cpp, line 64, as _ZN20QCRhiColorGlyphCache9growAtlasEi
inline void QCRhiColorGlyphCache::growAtlas(int requiredSize)
{
    int newSize = m_atlasSize;
    while (newSize < requiredSize)
        newSize *= 2;
    newSize = qMin(newSize, m_maxAtlasSize);
    if (newSize == m_atlasSize)
        return;

    QRhiTexture *newAtlas = m_rhi->newTexture(QRhiTexture::RGBA8, QSize(newSize, newSize), 1,
                                              QRhiTexture::UsedAsTransferSource);
    newAtlas->setName("QCColorGlyphAtlas");
    if (!newAtlas->create()) {
        qWarning("Failed to grow color glyph atlas");
        delete newAtlas;
        return;
    }

    if (useTextureResizeWorkaround()) {
        // Enlarge the CPU shadow first (the area outside the old image is
        // filled with transparent black) and upload it in full, so the region
        // beyond the old size does not stay undefined in the new texture.
        m_atlasImage = m_atlasImage.copy(0, 0, newSize, newSize);
        QRhiTextureSubresourceUploadDescription subres(m_atlasImage.constBits(),
                                                       m_atlasImage.sizeInBytes());
        subres.setSourceSize(QSize(newSize, newSize));
        m_batch->uploadTexture(newAtlas, QRhiTextureUploadEntry(0, 0, subres));
    } else {
        const QByteArray zeroBuf(newSize * newSize * 4, 0);
        QRhiTextureSubresourceUploadDescription zeroSubres(zeroBuf.constData(), zeroBuf.size());
        zeroSubres.setSourceSize(QSize(newSize, newSize));
        m_batch->uploadTexture(newAtlas, QRhiTextureUploadEntry(0, 0, zeroSubres));
        m_batch->copyTexture(newAtlas, m_atlas);
    }

    m_atlas->deleteLater();
    m_atlas = newAtlas;
    m_atlasSize = newSize;
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcrhicolorglyphcache.cpp, line 29, as _ZNK20QCRhiColorGlyphCache26useTextureResizeWorkaroundEv
inline bool QCRhiColorGlyphCache::useTextureResizeWorkaround() const
{
    return m_rhi->backend() == QRhi::OpenGLES2;
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcrhicolorglyphcache.cpp, line 112, as _ZN20QCRhiColorGlyphCache14referenceGlyphERKNS_8GlyphKeyERNS_9GlyphDataE
inline void QCRhiColorGlyphCache::referenceGlyph(const GlyphKey &key, GlyphData &gd)
{
    // Count one use per frame, so a glyph drawn many times in a frame is not
    // weighted more heavily than one drawn once (matches the SDF cache).
    if (!m_referencedThisFrame.contains(key)) {
        ++gd.ref;
        m_referencedThisFrame.insert(key);
    }
    m_unusedGlyphs.remove(key);
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcrhicolorglyphcache.cpp, line 125, as _ZN20QCRhiColorGlyphCache19evictUntilAllocatedERK5QSize
inline QRect QCRhiColorGlyphCache::evictUntilAllocated(const QSize &allocSize)
{
    QRect alloc;
    while (alloc.isNull() && !m_unusedGlyphs.isEmpty()) {
        const GlyphKey unused = *m_unusedGlyphs.constBegin();
        auto it = m_glyphs.constFind(unused);
        if (it != m_glyphs.constEnd() && it->valid)
            m_allocator->deallocate(allocationRect(it->atlasRect));
        m_unusedGlyphs.remove(unused);
        m_glyphs.remove(unused);
        alloc = m_allocator->allocate(allocSize);
    }
    return alloc;
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcrhicolorglyphcache.cpp, line 214, as _ZN20QCRhiColorGlyphCache13releaseGlyphsERK4QSetINS_8GlyphKeyEE
inline void QCRhiColorGlyphCache::releaseGlyphs(const QSet<GlyphKey> &glyphs)
{
    for (const GlyphKey &key : glyphs) {
        auto it = m_glyphs.find(key);
        if (it == m_glyphs.end())
            continue;
        if (it->ref > 0 && --it->ref == 0)
            m_unusedGlyphs.insert(key);
    }
}
//  -----------------------------------------------------------------------

//  QCRhiColorGlyphCache::QCRhiColorGlyphCache(QRhi *rhi)
extern "C" Q_DECL_EXPORT
QCRhiColorGlyphCache *ritual_ZN20QCRhiColorGlyphCacheC1EP4QRhi(QRhi *rhi) {
  return new QCRhiColorGlyphCache(rhi);
}

//  QCRhiColorGlyphCache::~QCRhiColorGlyphCache()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QCRhiColorGlyphCacheD1Ev(QCRhiColorGlyphCache *self) {
  delete self;
}

//  void QCRhiColorGlyphCache::addGlyphRun(QPointF glyphPos, const QGlyphRun
//      &run, QColor color, const QTransform &transform, float
//      devicePixelRatio, QCRhiDistanceFieldGlyphCache::VertexList *verts,
//      QCRhiDistanceFieldGlyphCache::IndexList *indices)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QCRhiColorGlyphCache11addGlyphRunE7QPointFRK9QGlyphRun6QColorRK10QTransformfP15QVarLengthArrayIN28QCRhiDistanceFieldGlyphCache15TexturedPoint2DELx256EEPS8_IjLx384EE(
    QCRhiColorGlyphCache *self,
    const QPointF *glyphPos,
    const QGlyphRun *run,
    const QColor *color,
    const QTransform *transform,
    float devicePixelRatio,
    QCRhiDistanceFieldGlyphCache::VertexList *verts,
    QCRhiDistanceFieldGlyphCache::IndexList *indices) {
  self->addGlyphRun(
      *glyphPos,
      *run,
      *color,
      *transform,
      devicePixelRatio,
      verts,
      indices);
}

//  void QCRhiColorGlyphCache::commitResourceUpdate(QRhiResourceUpdateBatch
//      *batch)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QCRhiColorGlyphCache20commitResourceUpdateEP23QRhiResourceUpdateBatch(
    QCRhiColorGlyphCache *self,
    QRhiResourceUpdateBatch *batch) {
  self->commitResourceUpdate(batch);
}

//  void QCRhiColorGlyphCache::optimizeAfterRendering()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QCRhiColorGlyphCache22optimizeAfterRenderingEv(
    QCRhiColorGlyphCache *self) {
  self->optimizeAfterRendering();
}

//  QRhiTexture *QCRhiColorGlyphCache::texture() const
extern "C" Q_DECL_EXPORT
QRhiTexture *ritual_ZNK20QCRhiColorGlyphCache7textureEv(
    const QCRhiColorGlyphCache *self) {
  return self->texture();
}

//  bool QCRhiColorGlyphCache::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QCRhiColorGlyphCache7isEmptyEv(
    const QCRhiColorGlyphCache *self) {
  return self->isEmpty();
}

//  void QCRhiColorGlyphCache::ensureAtlas()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QCRhiColorGlyphCache11ensureAtlasEv(
    QCRhiColorGlyphCache *self) {
  self->ensureAtlas();
}

//  void QCRhiColorGlyphCache::growAtlas(int requiredSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QCRhiColorGlyphCache9growAtlasEi(
    QCRhiColorGlyphCache *self,
    int requiredSize) {
  self->growAtlas(requiredSize);
}

//  bool QCRhiColorGlyphCache::useTextureResizeWorkaround() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QCRhiColorGlyphCache26useTextureResizeWorkaroundEv(
    const QCRhiColorGlyphCache *self) {
  return self->useTextureResizeWorkaround();
}

//  void QCRhiColorGlyphCache::referenceGlyph(const GlyphKey &key, GlyphData
//      &gd)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QCRhiColorGlyphCache14referenceGlyphERKNS_8GlyphKeyERNS_9GlyphDataE(
    QCRhiColorGlyphCache *self,
    const QCRhiColorGlyphCache::GlyphKey *key,
    QCRhiColorGlyphCache::GlyphData *gd) {
  self->referenceGlyph(*key, *gd);
}

//  QRect QCRhiColorGlyphCache::evictUntilAllocated(const QSize &allocSize)
extern "C" Q_DECL_EXPORT
QRect *ritual_ZN20QCRhiColorGlyphCache19evictUntilAllocatedERK5QSize(
    QCRhiColorGlyphCache *self,
    const QSize *allocSize) {
  return new QRect(self->evictUntilAllocated(*allocSize));
}

//  void QCRhiColorGlyphCache::releaseGlyphs(const QSet<GlyphKey> &glyphs)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QCRhiColorGlyphCache13releaseGlyphsERK4QSetINS_8GlyphKeyEE(
    QCRhiColorGlyphCache *self,
    const QSet<QCRhiColorGlyphCache::GlyphKey> *glyphs) {
  self->releaseGlyphs(*glyphs);
}
