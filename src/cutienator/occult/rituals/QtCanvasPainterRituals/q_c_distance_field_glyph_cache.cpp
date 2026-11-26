//  Written by dev_tooling.RitualGenerator from the records of QtCanvasPainte
//  r/6.12.0/QtCanvasPainter/private/qcdistancefieldglyphcache_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCanvasPainter/QtCanvasPainter>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCanvasPainter/6.12.0/QtCanvasPainter/private/qctextlayout_p.h>
#include <QtCanvasPainter/6.12.0/QtCanvasPainter/private/qcdistancefieldglyphcache_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qrawfont.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCanvasPainter/private/qcrhicolorglyphcache_p.h>
#include <QtGui/private/qrawfont_p.h>
#include <QtCanvasPainter/private/qcrhidistancefieldglyphcache_p.h>
#include <QtGui/private/qrawfont_p.h>
#include <QtCanvasPainter/private/qctextlayout_p.h>
#include <QtGui/QTransform>
#include <QtCanvasPainter/private/qcdistancefieldglyphcache_p.h>
#include <QtCanvasPainter/private/qcanvaspainter_p.h>
#include <QtGui/private/qrawfont_p.h>
#include <cmath>
#include <QtCanvasPainter/private/qcareaallocator_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
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

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcrhidistancefieldglyphcache.cpp, line 11, as local:qcrhidistancefieldglyphcache.cpp:RHI_DISTANCEFIELD_GLYPH_CACHE_PADDING
#define RHI_DISTANCEFIELD_GLYPH_CACHE_PADDING 2

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcrhidistancefieldglyphcache.cpp, line 18, as local:qcrhidistancefieldglyphcache.cpp:QC_SOLID_TILE_SIZE
static constexpr int QC_SOLID_TILE_SIZE = 4;

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcrhicolorglyphcache.cpp, line 20, as _ZN20QCRhiColorGlyphCacheD1Ev
inline QCRhiColorGlyphCache::~QCRhiColorGlyphCache()
{
    if (m_batch)
        m_batch->release();
    if (m_atlas)
        m_atlas->deleteLater();
    delete m_allocator;
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcrhidistancefieldglyphcache.cpp, line 28, as _ZN28QCRhiDistanceFieldGlyphCacheD1Ev
inline QCRhiDistanceFieldGlyphCache::~QCRhiDistanceFieldGlyphCache()
{
    if (m_batch)
        m_batch->release();

    for (auto i = 0; i < m_textures.size(); ++i) {
        if (auto *texture = m_textures[i].texture)
            texture->deleteLater();
    }

    if (m_areaAllocator != nullptr)
        delete m_areaAllocator;
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qctextlayout.cpp, line 48, as _ZN12QCTextLayout26calculateVerticalAlignmentEN14QCanvasPainter12TextBaselineERK6QRectFRK13QFontMetricsFS4_
inline float QCTextLayout::calculateVerticalAlignment(QCanvasPainter::TextBaseline baseline, const QRectF &rect,
                                               const QFontMetricsF &metrics, const QRectF &layoutRect)
{
    float offset = 0;
    switch (baseline) {
    case QCanvasPainter::TextBaseline::Top:
        break;
    case QCanvasPainter::TextBaseline::Hanging:
        offset = -metrics.height() + metrics.ascent();
        break;
    case QCanvasPainter::TextBaseline::Middle:
        offset = rect.height() * 0.5 - layoutRect.height() * 0.5;
        break;
    case QCanvasPainter::TextBaseline::Alphabetic:
        offset = rect.height() - layoutRect.height() + metrics.descent();
        break;
    case QCanvasPainter::TextBaseline::Bottom:
        offset = rect.height() - layoutRect.height();
        break;
    }

    return offset;
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

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcrhicolorglyphcache.cpp, line 14, as _ZN20QCRhiColorGlyphCacheC1EP4QRhi
inline QCRhiColorGlyphCache::QCRhiColorGlyphCache(QRhi *rhi)
    : m_rhi(rhi)
{
    m_batch = rhi->nextResourceUpdateBatch();
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcdistancefieldglyphcache.cpp, line 27, as _ZN25QCDistanceFieldGlyphCache17generateGlyphRunsERK7QStringRK6QRectFRK5QFontRK13QFontMetricsFP7QCStateN14QCanvasPainter9TextAlignE
inline QList<QGlyphRun> QCDistanceFieldGlyphCache::generateGlyphRuns(
    const QString &text, const QRectF &rect, const QFont &font,
    const QFontMetricsF &metrics, QCState *state, QCanvasPainter::TextAlign alignment)
{
    QTextOption option;
    // Emoji parsing is left enabled so that color-emoji sequences are grouped
    // into their own QGlyphRun(s) backed by a color (Format_ARGB) font engine.
    // generate() detects those runs and routes them to the color glyph atlas
    // instead of the SDF cache, so they render with their native colors.
    option.setWrapMode(QCTextLayout::convertToQtWrapMode(state->textWrapMode));
    option.setAlignment(QCTextLayout::convertToQtAlignment(alignment));
    option.setTextDirection(QCTextLayout::convertToQtDirection(state->textDirection));
    m_layout.clearLayout();
    m_layout.setTextOption(option);
    m_layout.setFont(font);
    m_layout.setText(text);
    const int leading = metrics.leading();
    float layoutHeight = 0;
    m_layout.beginLayout();
    while (true) {
        QTextLine line = m_layout.createLine();
        if (!line.isValid())
            break;

        line.setLineWidth(rect.width());
        layoutHeight += leading;
        line.setPosition(QPointF(0, layoutHeight));
        layoutHeight += line.height() + state->textLineHeight;
    }
    m_layout.endLayout();
    return m_layout.glyphRuns();
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcdistancefieldglyphcache.cpp, line 425, as _ZN25QCDistanceFieldGlyphCache7FontKeyC1ERK8QRawFont
inline QCDistanceFieldGlyphCache::FontKey::FontKey(const QRawFont &font)
{
    QFontEngine *fe = QRawFontPrivate::get(font)->fontEngine;
    if (fe != nullptr)
        faceId = fe->faceId();
    style = font.style();
    weight = font.weight();
    if (faceId.filename.isEmpty()) {
        familyName = font.familyName();
        styleName = font.styleName();
    }
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcrhidistancefieldglyphcache.cpp, line 480, as _ZN28QCRhiDistanceFieldGlyphCache10setRawFontERK8QRawFont
inline void QCRhiDistanceFieldGlyphCache::setRawFont(const QRawFont &font)
{
    if (m_referenceFont == font)
        return;

    Q_ASSERT(font.isValid());

    auto it = m_rawFontCache.find(font);
    if (it == m_rawFontCache.end()) {
        auto refFont = ReferenceFont{};
        refFont.mutatedFont = font;
        QRawFontPrivate *fontD = QRawFontPrivate::get(font);
        refFont.glyphCount = fontD->fontEngine->glyphCount();

        refFont.doubleGlyphResolution = qt_fontHasNarrowOutlines(font)
                                        && refFont.glyphCount < QT_DISTANCEFIELD_HIGHGLYPHCOUNT();

        refFont.pixelSize = QT_DISTANCEFIELD_BASEFONTSIZE(refFont.doubleGlyphResolution)
                            * QT_DISTANCEFIELD_SCALE(refFont.doubleGlyphResolution);

        // we set the same pixel size as used by the distance field internally.
        // this allows us to call pathForGlyph once and reuse the result.
        refFont.mutatedFont.setPixelSize(refFont.pixelSize);
        it = m_rawFontCache.insert(font, refFont);
    }

    m_currentReferenceFont = it.value();
    m_referenceFont = font;

    Q_ASSERT(m_referenceFont.isValid());
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcrhidistancefieldglyphcache.cpp, line 233, as _ZN28QCRhiDistanceFieldGlyphCache16generateVerticesEP15QVarLengthArrayINS_15TexturedPoint2DELx256EEPS0_IjLx384EERK10QTransformP6QRectF
inline void QCRhiDistanceFieldGlyphCache::generateVertices(
    VertexList *verts,
    IndexList *indices,
    const QTransform &transform,
    QRectF *boundingRect)
{
    if (!verts || !indices)
        return;

    const QList<quint32> indexes = m_glyphs.glyphIndexes();
    const QList<QPointF> positions = m_glyphs.positions();
    qreal fontPixelSize = m_glyphs.rawFont().pixelSize();

    const qsizetype maxIndexCount = (std::numeric_limits<quint16>::max() - 1)
                                    / 4; // 16383 (see below: 0xFFFF is not allowed)
    const auto likelyGlyphCount = qMin(indexes.size(), maxIndexCount);
    verts->reserve(likelyGlyphCount * 4);
    indices->reserve(likelyGlyphCount * 6);

    qreal maxTexMargin = distanceFieldRadius();
    qreal fScale = fontScale(fontPixelSize);
    qreal margin = 2;
    qreal texMargin = margin / fScale;
    if (texMargin > maxTexMargin) {
        texMargin = maxTexMargin;
        margin = maxTexMargin * fScale;
    }

    for (int i = 0; i < indexes.size(); ++i) {
        const int glyphIndex = indexes.at(i);
        GlyphData &gd = glyphData(glyphIndex);
        TexCoord c = gd.texCoord;

        if (c.isNull())
            continue;

        const QPointF position = positions.at(i);
        Metrics metrics = glyphMetrics(gd, fontPixelSize);

        if (!metrics.isNull() && !c.isNull()) {
            metrics.width += margin * 2;
            metrics.height += margin * 2;
            metrics.baselineX -= margin;
            metrics.baselineY += margin;
            c.xMargin -= texMargin;
            c.yMargin -= texMargin;
            c.width += texMargin * 2;
            c.height += texMargin * 2;
        }

        qreal x = position.x() + metrics.baselineX + m_position.x();
        qreal y = position.y() - metrics.baselineY + m_position.y();

        *boundingRect |= QRectF(x, y, metrics.width, metrics.height);

        float cx1 = x;
        float cx2 = x + metrics.width;
        float cy1 = y;
        float cy2 = y + metrics.height;

        float tx1 = c.x + c.xMargin;
        float tx2 = tx1 + c.width;
        float ty1 = c.y + c.yMargin;
        float ty2 = ty1 + c.height;

        qsizetype baseIndex = verts->size();

        // transform
        auto p1 = QPointF{cx1, cy1};
        auto p2 = QPointF{cx2, cy1};
        auto p3 = QPointF{cx1, cy2};
        auto p4 = QPointF{cx2, cy2};

        if (!transform.isIdentity()) {
            p1 = transform.map(p1);
            p2 = transform.map(p2);
            p3 = transform.map(p3);
            p4 = transform.map(p4);
        }

        TexturedPoint2D v1;
        v1.set(p1.x(), p1.y(), tx1, ty1);
        TexturedPoint2D v2;
        v2.set(p2.x(), p2.y(), tx2, ty1);
        TexturedPoint2D v3;
        v3.set(p3.x(), p3.y(), tx1, ty2);
        TexturedPoint2D v4;
        v4.set(p4.x(), p4.y(), tx2, ty2);

        verts->append(v1);
        verts->append(v2);
        verts->append(v3);
        verts->append(v4);

        indices->append(baseIndex + 0);
        indices->append(baseIndex + 2);
        indices->append(baseIndex + 3);
        indices->append(baseIndex + 3);
        indices->append(baseIndex + 1);
        indices->append(baseIndex + 0);
    }
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcrhidistancefieldglyphcache.cpp, line 125, as _ZN28QCRhiDistanceFieldGlyphCache22ensureSolidTileTextureEv
inline void QCRhiDistanceFieldGlyphCache::ensureSolidTileTexture()
{
    if (!ensureUpdateBatch())
        return;
    ensureSolidTile();
    if (!m_solidTileTexture)
        return;

    // When real glyphs were stored, storeGlyphs() already created the atlas
    // texture; otherwise it does not exist yet, so create it sized to the
    // reserved tile area. The 0xFF texels are flushed by uploadSolidTileIfNeeded().
    if (!m_solidTileTexture->texture) {
        const QRect area = m_solidTileTexture->allocatedArea;
        createTexture(m_solidTileTexture, area.width(), area.height());
    }
    uploadSolidTileIfNeeded();
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcrhidistancefieldglyphcache.cpp, line 447, as _ZN28QCRhiDistanceFieldGlyphCache6updateEv
inline void QCRhiDistanceFieldGlyphCache::update()
{
    m_populatingGlyphs.clear();

    if (!m_pendingGlyphs.isEmpty()) {
        QList<QDistanceField> distanceFields;
        const int pendingGlyphsSize = m_pendingGlyphs.size();
        distanceFields.reserve(pendingGlyphsSize);
        for (int i = 0; i < pendingGlyphsSize; ++i) {
            GlyphData &gd = glyphData(m_pendingGlyphs.at(i));

            QSize size = QSize(
                qCeil(gd.texCoord.width + gd.texCoord.xMargin * 2),
                qCeil(gd.texCoord.height + gd.texCoord.yMargin * 2));

            distanceFields.append(QDistanceField(
                size,
                gd.path,
                m_pendingGlyphs.at(i),
                m_currentReferenceFont.doubleGlyphResolution));
            gd.path = QPainterPath(); // no longer needed, so release memory used by the painter path
        }

        m_pendingGlyphs.reset();

        storeGlyphs(distanceFields);
    }

    // The texture exists by now if any glyphs ever populated it; flush the
    // solid-tile bytes into it on the first call after allocation.
    uploadSolidTileIfNeeded();
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcrhidistancefieldglyphcache.cpp, line 51, as _ZN28QCRhiDistanceFieldGlyphCache9addGlyphsE7QPointFRK9QGlyphRun
inline bool QCRhiDistanceFieldGlyphCache::addGlyphs(
    QPointF position, const QGlyphRun &glyphs)
{
    if (!ensureUpdateBatch())
        return false;
    // Reserve the solid tile before the run's glyphs so the area allocator
    // packs it next to the very first glyph rather than mid-atlas. The actual
    // texel upload happens in update() once the texture has been created.
    ensureSolidTile();
    return setGlyphs(position + QPointF(0, glyphs.rawFont().ascent()), glyphs);
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcrhidistancefieldglyphcache.cpp, line 22, as _ZN28QCRhiDistanceFieldGlyphCacheC1EP4QRhi
inline QCRhiDistanceFieldGlyphCache::QCRhiDistanceFieldGlyphCache(QRhi *rhi)
    : m_rhi(rhi)
    , m_pendingGlyphs(64)
{
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcrhidistancefieldglyphcache.cpp, line 336, as _ZN28QCRhiDistanceFieldGlyphCache20commitResourceUpdateEP23QRhiResourceUpdateBatch
inline void QCRhiDistanceFieldGlyphCache::commitResourceUpdate(QRhiResourceUpdateBatch *batch)
{
    if (!m_batch)
        return;

    batch->merge(m_batch);
    m_batch->release();
    m_batch = nullptr;
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

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcrhidistancefieldglyphcache.cpp, line 622, as _ZN28QCRhiDistanceFieldGlyphCache22optimizeAfterRenderingEv
inline void QCRhiDistanceFieldGlyphCache::optimizeAfterRendering()
{
    releaseGlyphs(m_referencedPrevFrame);
    m_referencedPrevFrame.swap(m_referencedThisFrame);
    m_referencedThisFrame.clear();
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcareaallocator.cpp, line 48, as _ZN15QCAreaAllocatorD1Ev
inline QCAreaAllocator::~QCAreaAllocator()
{
    delete m_root;
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qctextlayout.cpp, line 11, as _ZN12QCTextLayout19convertToQtWrapModeEN14QCanvasPainter8WrapModeE
inline QTextOption::WrapMode QCTextLayout::convertToQtWrapMode(QCanvasPainter::WrapMode mode)
{
    switch (mode) {
    case QCanvasPainter::WrapMode::NoWrap:
        return QTextOption::NoWrap;
        break;
    case QCanvasPainter::WrapMode::Wrap:
        return QTextOption::WrapAtWordBoundaryOrAnywhere;
        break;
    case QCanvasPainter::WrapMode::WordWrap:
        return QTextOption::WordWrap;
        break;
    case QCanvasPainter::WrapMode::WrapAnywhere:
        return QTextOption::WrapAnywhere;
        break;
    }
    return QTextOption::NoWrap;
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qctextlayout.cpp, line 30, as _ZN12QCTextLayout20convertToQtAlignmentEN14QCanvasPainter9TextAlignE
inline Qt::Alignment QCTextLayout::convertToQtAlignment(QCanvasPainter::TextAlign alignment)
{
    switch (alignment) {
    case QCanvasPainter::TextAlign::Left:
        return Qt::AlignLeft;
        break;
    case QCanvasPainter::TextAlign::Center:
        return Qt::AlignCenter;
        break;
    case QCanvasPainter::TextAlign::Right:
        return Qt::AlignRight;
        break;
    default:
        break;
    }
    return Qt::AlignLeft;
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qctextlayout.cpp, line 101, as _ZN12QCTextLayout20convertToQtDirectionEN14QCanvasPainter13TextDirectionE
inline Qt::LayoutDirection QCTextLayout::convertToQtDirection(QCanvasPainter::TextDirection direction)
{
    switch (direction) {
    case QCanvasPainter::TextDirection::LeftToRight:
        return Qt::LeftToRight;
    case QCanvasPainter::TextDirection::RightToLeft:
        return Qt::RightToLeft;
    case QCanvasPainter::TextDirection::Inherit:
        return QGuiApplication::layoutDirection();
    case QCanvasPainter::TextDirection::Auto:
        return Qt::LayoutDirectionAuto;
    }
    Q_UNREACHABLE_RETURN(Qt::LayoutDirectionAuto);
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcrhidistancefieldglyphcache.cpp, line 629, as _ZN28QCRhiDistanceFieldGlyphCache11storeGlyphsERK5QListI14QDistanceFieldE
inline void QCRhiDistanceFieldGlyphCache::storeGlyphs(const QList<QDistanceField> &glyphs)
{
    if (!ensureUpdateBatch())
        return;

    typedef QHash<TextureInfo *, QList<glyph_t>> GlyphTextureHash;

    GlyphTextureHash glyphTextures;

    for (int i = 0; i < glyphs.size(); ++i) {
        QDistanceField glyph = glyphs.at(i);
        glyph_t glyphIndex = glyph.glyph();
        TexCoord c = glyphData(glyphIndex).texCoord;
        TextureInfo *texInfo = m_glyphsTexture.value(glyphIndex);

        resizeTexture(texInfo, texInfo->allocatedArea.width(), texInfo->allocatedArea.height());

        glyphTextures[texInfo].append(glyphIndex);

        int padding = texInfo->padding;
        int expectedWidth = qCeil(c.width + c.xMargin * 2);
        glyph = glyph.copy(
            -padding, -padding, expectedWidth + padding * 2, glyph.height() + padding * 2);

        if (useTextureResizeWorkaround()) {
            uchar *inBits = glyph.scanLine(0);
            uchar *outBits = texInfo->image.scanLine(int(c.y) - padding) + int(c.x) - padding;
            for (int y = 0; y < glyph.height(); ++y) {
                memcpy(outBits, inBits, glyph.width());
                inBits += glyph.width();
                outBits += texInfo->image.width();
            }
        }

        QRhiTextureSubresourceUploadDescription
            subresDesc(glyph.constBits(), glyph.width() * glyph.height());
        subresDesc.setSourceSize(QSize(glyph.width(), glyph.height()));
        subresDesc.setDestinationTopLeft(QPoint(c.x - padding, c.y - padding));
        texInfo->uploads.append(QRhiTextureUploadEntry(0, 0, subresDesc));
    }

    for (int i = 0; i < glyphs.size(); ++i) {
        TextureInfo *texInfo = m_glyphsTexture.value(glyphs.at(i).glyph());
        if (!texInfo->uploads.isEmpty()) {
            QRhiTextureUploadDescription desc;
            desc.setEntries(texInfo->uploads.cbegin(), texInfo->uploads.cend());
            m_batch->uploadTexture(texInfo->texture, desc);
            texInfo->uploads.clear();
        }
    }

    for (auto i = glyphTextures.constBegin(), cend = glyphTextures.constEnd(); i != cend; ++i) {
        TextureInfo t;
        t.texture = i.key()->texture;
        t.size = i.key()->size;
        setGlyphTexture(i.value(), t);
    }
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcrhidistancefieldglyphcache.cpp, line 143, as _ZN28QCRhiDistanceFieldGlyphCache13createTextureEPNS_11TextureInfoEii
inline void QCRhiDistanceFieldGlyphCache::createTexture(TextureInfo *texInfo, int width, int height)
{
    QByteArray zeroBuf(width * height, 0);
    createTexture(texInfo, width, height, zeroBuf.constData());
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcrhidistancefieldglyphcache.cpp, line 63, as _ZN28QCRhiDistanceFieldGlyphCache15ensureSolidTileEv
inline void QCRhiDistanceFieldGlyphCache::ensureSolidTile()
{
    if (m_solidTileTexCoord.isValid())
        return;
    if (!ensureUpdateBatch())
        return;

    if (m_areaAllocator == nullptr)
        m_areaAllocator = new QCAreaAllocator(
            QSize(maxTextureSize(), m_maxTextureCount * maxTextureSize()));

    QRect alloc = m_areaAllocator->allocate(QSize(QC_SOLID_TILE_SIZE, QC_SOLID_TILE_SIZE));
    if (alloc.isNull())
        return;

    TextureInfo *tex = textureInfo(alloc.y() / maxTextureSize());
    alloc = QRect(alloc.x(), alloc.y() % maxTextureSize(), alloc.width(), alloc.height());
    tex->allocatedArea |= alloc;
    if (tex->padding < 0)
        tex->padding = RHI_DISTANCEFIELD_GLYPH_CACHE_PADDING;

    m_solidTileTexCoord.x = alloc.x();
    m_solidTileTexCoord.y = alloc.y();
    m_solidTileTexCoord.width = alloc.width();
    m_solidTileTexCoord.height = alloc.height();
    m_solidTileTexture = tex;
    m_solidTileUploadPending = true;
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcrhidistancefieldglyphcache.cpp, line 42, as _ZN28QCRhiDistanceFieldGlyphCache17ensureUpdateBatchEv
inline bool QCRhiDistanceFieldGlyphCache::ensureUpdateBatch()
{
    if (!m_batch)
        m_batch = m_rhi->nextResourceUpdateBatch();
    if (!m_batch)
        qWarning("QCRhiDistanceFieldGlyphCache: could not allocate QRhiResourceUpdateBatch");
    return !!m_batch;
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcrhidistancefieldglyphcache.cpp, line 92, as _ZN28QCRhiDistanceFieldGlyphCache23uploadSolidTileIfNeededEv
inline void QCRhiDistanceFieldGlyphCache::uploadSolidTileIfNeeded()
{
    if (!m_solidTileUploadPending)
        return;
    if (!m_solidTileTexture || !m_solidTileTexture->texture)
        return;
    if (!ensureUpdateBatch())
        return;

    const int w = int(m_solidTileTexCoord.width);
    const int h = int(m_solidTileTexCoord.height);
    const int x = int(m_solidTileTexCoord.x);
    const int y = int(m_solidTileTexCoord.y);

    QByteArray bytes(w * h, char(0xFF));
    QRhiTextureSubresourceUploadDescription subresDesc(bytes.constData(), bytes.size());
    subresDesc.setSourceSize(QSize(w, h));
    subresDesc.setDestinationTopLeft(QPoint(x, y));
    m_batch->uploadTexture(m_solidTileTexture->texture, QRhiTextureUploadEntry(0, 0, subresDesc));

    // Mirror the write into the CPU shadow image so the tile survives a
    // resizeTexture() that goes through the OpenGL ES2 copy path.
    if (useTextureResizeWorkaround() && !m_solidTileTexture->image.isNull()) {
        uchar *out = m_solidTileTexture->image.scanLine(y) + x;
        for (int row = 0; row < h; ++row) {
            memset(out, 0xFF, w);
            out += m_solidTileTexture->image.width();
        }
    }

    m_solidTileUploadPending = false;
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcrhidistancefieldglyphcache.cpp, line 688, as _ZN28QCRhiDistanceFieldGlyphCache9glyphDataEj
inline QCRhiDistanceFieldGlyphCache::GlyphData &QCRhiDistanceFieldGlyphCache::glyphData(glyph_t glyph)
{
    auto data = m_glyphsData.find(glyph);
    if (data == m_glyphsData.end()) {
        GlyphData &gd = emptyData(glyph);
        gd.path = m_currentReferenceFont.mutatedFont.pathForGlyph(glyph);
        // need bounding rect in base font size scale
        qreal scaleFactor = qreal(1) / QT_DISTANCEFIELD_SCALE(m_currentReferenceFont.doubleGlyphResolution);
        QTransform scaleDown;
        scaleDown.scale(scaleFactor, scaleFactor);
        gd.boundingRect = scaleDown.mapRect(gd.path.boundingRect());
        return gd;
    }
    return data.value();
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcrhidistancefieldglyphcache.cpp, line 204, as _ZN28QCRhiDistanceFieldGlyphCache9setGlyphsE7QPointFRK9QGlyphRun
inline bool QCRhiDistanceFieldGlyphCache::setGlyphs(QPointF position, const QGlyphRun &glyphs)
{
    QRawFont font = glyphs.rawFont();
    m_position = QPointF(position.x(), position.y() - font.ascent());
    m_glyphs = glyphs;
    return populate(glyphs.glyphIndexes());
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcrhidistancefieldglyphcache.cpp, line 385, as _ZNK28QCRhiDistanceFieldGlyphCache12glyphMetricsERKNS_9GlyphDataEd
inline QCRhiDistanceFieldGlyphCache::Metrics QCRhiDistanceFieldGlyphCache::glyphMetrics(
    const GlyphData &gd, qreal pixelSize) const
{
    qreal scale = fontScale(pixelSize);

    Metrics m;
    m.width = gd.boundingRect.width() * scale;
    m.height = gd.boundingRect.height() * scale;
    m.baselineX = gd.boundingRect.x() * scale;
    m.baselineY = -gd.boundingRect.y() * scale;

    return m;
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcrhidistancefieldglyphcache.cpp, line 399, as _ZNK28QCRhiDistanceFieldGlyphCache9fontScaleEd
inline qreal QCRhiDistanceFieldGlyphCache::fontScale(qreal pixelSize) const
{
    return pixelSize
           / QT_DISTANCEFIELD_BASEFONTSIZE(m_currentReferenceFont.doubleGlyphResolution);
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

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcrhidistancefieldglyphcache.cpp, line 611, as _ZN28QCRhiDistanceFieldGlyphCache13releaseGlyphsERK4QSetIjE
inline void QCRhiDistanceFieldGlyphCache::releaseGlyphs(const QSet<glyph_t> &glyphs)
{
    for (glyph_t glyph : glyphs) {
        auto it = m_glyphsData.find(glyph);
        if (it == m_glyphsData.end())
            continue;
        if (it->ref > 0 && --it->ref == 0)
            m_unusedGlyphs.insert(glyph);
    }
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcareaallocator.cpp, line 53, as _ZN15QCAreaAllocator8allocateE5QSize
inline QRect QCAreaAllocator::allocate(QSize size)
{
    QPoint point;
    bool result = allocateInNode(size, point, QRect(QPoint(0, 0), m_size), m_root);
    return result ? QRect(point, size) : QRect();
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcareaallocator.cpp, line 42, as _ZN15QCAreaAllocatorC1E5QSize
inline QCAreaAllocator::QCAreaAllocator(QSize size)
    : m_size(size)
{
    m_root = new QCAreaAllocatorNode(nullptr);
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcdistancefieldglyphcache.cpp, line 20, as _ZN25QCDistanceFieldGlyphCacheD1Ev
inline QCDistanceFieldGlyphCache::~QCDistanceFieldGlyphCache()
{
    for (auto &cache : std::as_const(m_glyphCaches))
        delete cache;
    delete m_colorCache;
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcdistancefieldglyphcache.cpp, line 349, as _ZN25QCDistanceFieldGlyphCache21commitResourceUpdatesEP23QRhiResourceUpdateBatchPNS_11FontKeyDataE
inline void QCDistanceFieldGlyphCache::commitResourceUpdates(QRhiResourceUpdateBatch *batch,
                                                      FontKeyData *data)
{
    if (data)
        data->nativeGlyphCache.commitResourceUpdate(batch);
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcdistancefieldglyphcache.cpp, line 356, as _ZN25QCDistanceFieldGlyphCache21commitResourceUpdatesEP23QRhiResourceUpdateBatch
inline void QCDistanceFieldGlyphCache::commitResourceUpdates(QRhiResourceUpdateBatch *batch)
{
    for (auto it = m_glyphCaches.begin(); it != m_glyphCaches.end(); ++it)
        it.value()->nativeGlyphCache.commitResourceUpdate(batch);
    if (m_colorCache && !m_colorCache->isEmpty())
        m_colorCache->commitResourceUpdate(batch);
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcdistancefieldglyphcache.cpp, line 364, as _ZNK25QCDistanceFieldGlyphCache18getCurrentTexturesEPKNS_11FontKeyDataE
inline QRhiTexture *QCDistanceFieldGlyphCache::getCurrentTextures(const FontKeyData *data) const
{
    if (!data)
        return nullptr;

    const auto l = data->nativeGlyphCache.getTextures();

    if (l.size() == 0)
        return nullptr;

    return l.constFirst().texture;
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcdistancefieldglyphcache.cpp, line 377, as _ZNK25QCDistanceFieldGlyphCache14getOldTexturesEPKNS_11FontKeyDataE
inline QRhiTexture *QCDistanceFieldGlyphCache::getOldTextures(const FontKeyData *data) const
{
    return data ? data->prevTextureState : nullptr;
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcdistancefieldglyphcache.cpp, line 382, as _ZN25QCDistanceFieldGlyphCache13setOldTextureEPNS_11FontKeyDataEP11QRhiTexture
inline void QCDistanceFieldGlyphCache::setOldTexture(FontKeyData *data, QRhiTexture *tex)
{
    if (data)
        data->prevTextureState = tex;
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcdistancefieldglyphcache.cpp, line 388, as _ZN25QCDistanceFieldGlyphCache27optimizeCacheAfterRenderingEv
inline void QCDistanceFieldGlyphCache::optimizeCacheAfterRendering()
{
    for (auto it = m_glyphCaches.begin(); it != m_glyphCaches.end(); ++it)
        it.value()->nativeGlyphCache.optimizeAfterRendering();

    if (m_colorCache)
        m_colorCache->optimizeAfterRendering();

#ifdef QCPAINTER_CACHE_GLYPH_RUNS
#ifdef QCPAINTER_GLYPH_RUNS_CACHE_SIZE
    const int maxGlyphRuns = QCPAINTER_GLYPH_RUNS_CACHE_SIZE;
#else
    const int maxGlyphRuns = 1024;
#endif
    if (m_glyphRunCache.size() > maxGlyphRuns) {
        int eraseCount = 0;
        // First remove the ones which have been used only few times.
        // These can come when e.g. animating letterSpacing.
        erase_if(m_glyphRunCache, [&eraseCount](const QHash<GlyphCacheKey, GlyphCacheValue>::iterator it) {
            if (it->usageCounter < 5) {
                eraseCount++;
                return true;
            }
            return false;
        });
        // In the rare case where this isn't enough, clear the whole cache.
        const int cleanedMaxGlyphRuns = 0.9 * maxGlyphRuns;
        if (m_glyphRunCache.size() > cleanedMaxGlyphRuns) {
            eraseCount += m_glyphRunCache.size();
            m_glyphRunCache.clear();
        }
        qCDebug(QC_INFO) << "Max text glyph cache size" << maxGlyphRuns
                         << "reached. Removing" << eraseCount << "elements.";
    }
#endif
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcdistancefieldglyphcache.cpp, line 60, as _ZN25QCDistanceFieldGlyphCache14fontKeyDataForERK8QRawFont
inline QCDistanceFieldGlyphCache::FontKeyData *QCDistanceFieldGlyphCache::fontKeyDataFor(const QRawFont &rFont)
{
    QFontEngine *fe = QRawFontPrivate::get(rFont)->fontEngine;
    if (fe == m_lastFontEngine && m_lastFontKeyData)
        return m_lastFontKeyData;

    FontKey key(rFont);
    auto it = m_glyphCaches.find(key);
    if (it == m_glyphCaches.end())
        it = m_glyphCaches.insert(key, new FontKeyData{ nullptr, QCRhiDistanceFieldGlyphCache(m_rhi)});

    m_lastFontEngine = fe;
    m_lastFontKeyData = it.value();
    return m_lastFontKeyData;
}
//  -----------------------------------------------------------------------

//  QCDistanceFieldGlyphCache::~QCDistanceFieldGlyphCache()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QCDistanceFieldGlyphCacheD1Ev(
    QCDistanceFieldGlyphCache *self) {
  delete self;
}

//  void
//      QCDistanceFieldGlyphCache::commitResourceUpdates(QRhiResourceUpdateBa
//      tch *batch, FontKeyData *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QCDistanceFieldGlyphCache21commitResourceUpdatesEP23QRhiResourceUpdateBatchPNS_11FontKeyDataE(
    QCDistanceFieldGlyphCache *self,
    QRhiResourceUpdateBatch *batch,
    QCDistanceFieldGlyphCache::FontKeyData *data) {
  self->commitResourceUpdates(batch, data);
}

//  void
//      QCDistanceFieldGlyphCache::commitResourceUpdates(QRhiResourceUpdateBa
//      tch *batch)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QCDistanceFieldGlyphCache21commitResourceUpdatesEP23QRhiResourceUpdateBatch(
    QCDistanceFieldGlyphCache *self,
    QRhiResourceUpdateBatch *batch) {
  self->commitResourceUpdates(batch);
}

//  QRhiTexture *QCDistanceFieldGlyphCache::getCurrentTextures(const
//      FontKeyData *data) const
extern "C" Q_DECL_EXPORT
QRhiTexture *ritual_ZNK25QCDistanceFieldGlyphCache18getCurrentTexturesEPKNS_11FontKeyDataE(
    const QCDistanceFieldGlyphCache *self,
    const QCDistanceFieldGlyphCache::FontKeyData *data) {
  return self->getCurrentTextures(data);
}

//  QRhiTexture *QCDistanceFieldGlyphCache::getOldTextures(const FontKeyData
//      *data) const
extern "C" Q_DECL_EXPORT
QRhiTexture *ritual_ZNK25QCDistanceFieldGlyphCache14getOldTexturesEPKNS_11FontKeyDataE(
    const QCDistanceFieldGlyphCache *self,
    const QCDistanceFieldGlyphCache::FontKeyData *data) {
  return self->getOldTextures(data);
}

//  void QCDistanceFieldGlyphCache::setOldTexture(FontKeyData *data,
//      QRhiTexture *tex)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QCDistanceFieldGlyphCache13setOldTextureEPNS_11FontKeyDataEP11QRhiTexture(
    QCDistanceFieldGlyphCache *self,
    QCDistanceFieldGlyphCache::FontKeyData *data,
    QRhiTexture *tex) {
  self->setOldTexture(data, tex);
}

//  void QCDistanceFieldGlyphCache::optimizeCacheAfterRendering()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QCDistanceFieldGlyphCache27optimizeCacheAfterRenderingEv(
    QCDistanceFieldGlyphCache *self) {
  self->optimizeCacheAfterRendering();
}

//  const QCRhiDistanceFieldGlyphCache::VertexList
//      &QCDistanceFieldGlyphCache::colorVertices() const
extern "C" Q_DECL_EXPORT
const QCRhiDistanceFieldGlyphCache::VertexList *ritual_ZNK25QCDistanceFieldGlyphCache13colorVerticesEv(
    const QCDistanceFieldGlyphCache *self) {
  return &(self->colorVertices());
}

//  const QCRhiDistanceFieldGlyphCache::IndexList
//      &QCDistanceFieldGlyphCache::colorIndices() const
extern "C" Q_DECL_EXPORT
const QCRhiDistanceFieldGlyphCache::IndexList *ritual_ZNK25QCDistanceFieldGlyphCache12colorIndicesEv(
    const QCDistanceFieldGlyphCache *self) {
  return &(self->colorIndices());
}

//  QRhiTexture *QCDistanceFieldGlyphCache::colorGlyphTexture() const
extern "C" Q_DECL_EXPORT
QRhiTexture *ritual_ZNK25QCDistanceFieldGlyphCache17colorGlyphTextureEv(
    const QCDistanceFieldGlyphCache *self) {
  return self->colorGlyphTexture();
}

//  QRhiTexture *QCDistanceFieldGlyphCache::prevColorGlyphTexture() const
extern "C" Q_DECL_EXPORT
QRhiTexture *ritual_ZNK25QCDistanceFieldGlyphCache21prevColorGlyphTextureEv(
    const QCDistanceFieldGlyphCache *self) {
  return self->prevColorGlyphTexture();
}

//  void QCDistanceFieldGlyphCache::setPrevColorGlyphTexture(QRhiTexture
//      *tex)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QCDistanceFieldGlyphCache24setPrevColorGlyphTextureEP11QRhiTexture(
    QCDistanceFieldGlyphCache *self,
    QRhiTexture *tex) {
  self->setPrevColorGlyphTexture(tex);
}

//  FontKeyData *QCDistanceFieldGlyphCache::fontKeyDataFor(const QRawFont
//      &rFont)
extern "C" Q_DECL_EXPORT
QCDistanceFieldGlyphCache::FontKeyData *ritual_ZN25QCDistanceFieldGlyphCache14fontKeyDataForERK8QRawFont(
    QCDistanceFieldGlyphCache *self,
    const QRawFont *rFont) {
  return self->fontKeyDataFor(*rFont);
}

//  bool operator==(const FontKey &f1, const FontKey &f2)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRKN25QCDistanceFieldGlyphCache7FontKeyES2_(
    const QCDistanceFieldGlyphCache::FontKey *f1,
    const QCDistanceFieldGlyphCache::FontKey *f2) {
  return operator==(*f1, *f2);
}
