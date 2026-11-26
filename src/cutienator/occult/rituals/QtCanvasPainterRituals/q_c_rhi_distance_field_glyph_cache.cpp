//  Written by dev_tooling.RitualGenerator from the records of QtCanvasPainte
//  r/6.12.0/QtCanvasPainter/private/qcrhidistancefieldglyphcache_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCanvasPainter/QtCanvasPainter>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCanvasPainter/6.12.0/QtCanvasPainter/private/qcrhidistancefieldglyphcache_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qrawfont.h>
#include <QtCore/qsize.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCanvasPainter/private/qcareaallocator_p.h>
#include <QtCanvasPainter/private/qcrhidistancefieldglyphcache_p.h>
#include <QtGui/private/qrawfont_p.h>
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

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcrhidistancefieldglyphcache.cpp, line 11, as local:qcrhidistancefieldglyphcache.cpp:RHI_DISTANCEFIELD_GLYPH_CACHE_PADDING
#define RHI_DISTANCEFIELD_GLYPH_CACHE_PADDING 2

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcrhidistancefieldglyphcache.cpp, line 18, as local:qcrhidistancefieldglyphcache.cpp:QC_SOLID_TILE_SIZE
static constexpr int QC_SOLID_TILE_SIZE = 4;

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcareaallocator.cpp, line 48, as _ZN15QCAreaAllocatorD1Ev
inline QCAreaAllocator::~QCAreaAllocator()
{
    delete m_root;
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

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcareaallocator.cpp, line 42, as _ZN15QCAreaAllocatorC1E5QSize
inline QCAreaAllocator::QCAreaAllocator(QSize size)
    : m_size(size)
{
    m_root = new QCAreaAllocatorNode(nullptr);
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

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcrhidistancefieldglyphcache.cpp, line 22, as _ZN28QCRhiDistanceFieldGlyphCacheC1EP4QRhi
inline QCRhiDistanceFieldGlyphCache::QCRhiDistanceFieldGlyphCache(QRhi *rhi)
    : m_rhi(rhi)
    , m_pendingGlyphs(64)
{
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

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcrhidistancefieldglyphcache.cpp, line 143, as _ZN28QCRhiDistanceFieldGlyphCache13createTextureEPNS_11TextureInfoEii
inline void QCRhiDistanceFieldGlyphCache::createTexture(TextureInfo *texInfo, int width, int height)
{
    QByteArray zeroBuf(width * height, 0);
    createTexture(texInfo, width, height, zeroBuf.constData());
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcrhidistancefieldglyphcache.cpp, line 149, as _ZN28QCRhiDistanceFieldGlyphCache13createTextureEPNS_11TextureInfoEiiPKv
inline void QCRhiDistanceFieldGlyphCache::createTexture(
    TextureInfo *texInfo, int width, int height, const void *pixels)
{
    Q_ASSERT(m_batch);
    if (useTextureResizeWorkaround() && texInfo->image.isNull()) {
        texInfo->image = QDistanceField(width, height);
        memcpy(texInfo->image.bits(), pixels, width * height);
    }

    texInfo->texture = m_rhi->newTexture(
        QRhiTexture::RED_OR_ALPHA8, QSize(width, height), 1, QRhiTexture::UsedAsTransferSource);
    texInfo->texture->setName("QCDistanceFieldAtlas");

    if (texInfo->texture->create()) {
        QRhiTextureSubresourceUploadDescription subresDesc(pixels, width * height);
        subresDesc.setSourceSize(QSize(width, height));
        m_batch->uploadTexture(texInfo->texture, QRhiTextureUploadEntry(0, 0, subresDesc));
    } else {
        qWarning("Failed to create distance field glyph cache");
    }

    texInfo->size = QSize(width, height);
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcrhidistancefieldglyphcache.cpp, line 173, as _ZN28QCRhiDistanceFieldGlyphCache13resizeTextureEPNS_11TextureInfoEii
inline void QCRhiDistanceFieldGlyphCache::resizeTexture(TextureInfo *texInfo, int width, int height)
{
    if (!ensureUpdateBatch())
        return;

    int oldWidth = texInfo->size.width();
    int oldHeight = texInfo->size.height();
    if (width == oldWidth && height == oldHeight)
        return;

    QRhiTexture *oldTexture = texInfo->texture;
    createTexture(texInfo, width, height);

    if (!oldTexture)
        return;

    updateRhiTexture(oldTexture, texInfo->texture, texInfo->size);

    if (useTextureResizeWorkaround()) {
        QRhiTextureSubresourceUploadDescription
            subresDesc(texInfo->image.constBits(), oldWidth * oldHeight);
        subresDesc.setSourceSize(QSize(oldWidth, oldHeight));
        m_batch->uploadTexture(texInfo->texture, QRhiTextureUploadEntry(0, 0, subresDesc));
        texInfo->image = texInfo->image.copy(0, 0, width, height);
    } else {
        m_batch->copyTexture(texInfo->texture, oldTexture);
    }

    oldTexture->deleteLater();
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcrhidistancefieldglyphcache.cpp, line 605, as _ZN28QCRhiDistanceFieldGlyphCache15referenceGlyphsERK15QVarLengthArrayIjLx16EE
inline void QCRhiDistanceFieldGlyphCache::referenceGlyphs(const QVarLengthArray<glyph_t, 16> &glyphs)
{
    for (glyph_t glyph : glyphs)
        m_unusedGlyphs.remove(glyph);
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcrhidistancefieldglyphcache.cpp, line 622, as _ZN28QCRhiDistanceFieldGlyphCache22optimizeAfterRenderingEv
inline void QCRhiDistanceFieldGlyphCache::optimizeAfterRendering()
{
    releaseGlyphs(m_referencedPrevFrame);
    m_referencedPrevFrame.swap(m_referencedThisFrame);
    m_referencedThisFrame.clear();
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

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcrhidistancefieldglyphcache.cpp, line 346, as _ZNK28QCRhiDistanceFieldGlyphCache14maxTextureSizeEv
inline int QCRhiDistanceFieldGlyphCache::maxTextureSize() const
{
    return m_maxTextureSize;
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcrhidistancefieldglyphcache.cpp, line 359, as _ZN28QCRhiDistanceFieldGlyphCache18markGlyphsToRenderERK5QListIjE
inline void QCRhiDistanceFieldGlyphCache::markGlyphsToRender(const QList<glyph_t> &glyphs)
{
    int count = glyphs.size();
    for (int i = 0; i < count; ++i)
        m_pendingGlyphs.add(glyphs.at(i));
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

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcrhidistancefieldglyphcache.cpp, line 366, as _ZNK28QCRhiDistanceFieldGlyphCache26useTextureResizeWorkaroundEv
inline bool QCRhiDistanceFieldGlyphCache::useTextureResizeWorkaround() const
{
    return m_rhi->backend() == QRhi::OpenGLES2;
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcrhidistancefieldglyphcache.cpp, line 371, as _ZN28QCRhiDistanceFieldGlyphCache16updateRhiTextureEP11QRhiTextureS1_5QSize
inline void QCRhiDistanceFieldGlyphCache::updateRhiTexture(
    QRhiTexture *oldTex, QRhiTexture *newTex, QSize newTexSize)
{
    int count = m_textures.size();
    for (int i = 0; i < count; ++i) {
        TextureInfo &tex = m_textures[i];
        if (tex.texture == oldTex) {
            tex.texture = newTex;
            tex.size = newTexSize;
            return;
        }
    }
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

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcrhidistancefieldglyphcache.cpp, line 42, as _ZN28QCRhiDistanceFieldGlyphCache17ensureUpdateBatchEv
inline bool QCRhiDistanceFieldGlyphCache::ensureUpdateBatch()
{
    if (!m_batch)
        m_batch = m_rhi->nextResourceUpdateBatch();
    if (!m_batch)
        qWarning("QCRhiDistanceFieldGlyphCache: could not allocate QRhiResourceUpdateBatch");
    return !!m_batch;
}
//  -----------------------------------------------------------------------

//  QCRhiDistanceFieldGlyphCache::QCRhiDistanceFieldGlyphCache(QRhi *rhi)
extern "C" Q_DECL_EXPORT
QCRhiDistanceFieldGlyphCache *ritual_ZN28QCRhiDistanceFieldGlyphCacheC1EP4QRhi(
    QRhi *rhi) {
  return new QCRhiDistanceFieldGlyphCache(rhi);
}

//  QCRhiDistanceFieldGlyphCache::~QCRhiDistanceFieldGlyphCache()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QCRhiDistanceFieldGlyphCacheD1Ev(
    QCRhiDistanceFieldGlyphCache *self) {
  delete self;
}

//  void QCRhiDistanceFieldGlyphCache::setRawFont(const QRawFont &font)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QCRhiDistanceFieldGlyphCache10setRawFontERK8QRawFont(
    QCRhiDistanceFieldGlyphCache *self,
    const QRawFont *font) {
  self->setRawFont(*font);
}

//  void QCRhiDistanceFieldGlyphCache::createTexture(TextureInfo *texInfo,
//      int width, int height)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QCRhiDistanceFieldGlyphCache13createTextureEPNS_11TextureInfoEii(
    QCRhiDistanceFieldGlyphCache *self,
    QCRhiDistanceFieldGlyphCache::TextureInfo *texInfo,
    int width,
    int height) {
  self->createTexture(texInfo, width, height);
}

//  void QCRhiDistanceFieldGlyphCache::createTexture(TextureInfo *texInfo,
//      int width, int height, const void *pixels)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QCRhiDistanceFieldGlyphCache13createTextureEPNS_11TextureInfoEiiPKv(
    QCRhiDistanceFieldGlyphCache *self,
    QCRhiDistanceFieldGlyphCache::TextureInfo *texInfo,
    int width,
    int height,
    const void *pixels) {
  self->createTexture(texInfo, width, height, pixels);
}

//  void QCRhiDistanceFieldGlyphCache::resizeTexture(TextureInfo *texInfo,
//      int width, int height)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QCRhiDistanceFieldGlyphCache13resizeTextureEPNS_11TextureInfoEii(
    QCRhiDistanceFieldGlyphCache *self,
    QCRhiDistanceFieldGlyphCache::TextureInfo *texInfo,
    int width,
    int height) {
  self->resizeTexture(texInfo, width, height);
}

//  void QCRhiDistanceFieldGlyphCache::referenceGlyphs(const
//      QVarLengthArray<glyph_t, 16> &glyphs)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QCRhiDistanceFieldGlyphCache15referenceGlyphsERK15QVarLengthArrayIjLx16EE(
    QCRhiDistanceFieldGlyphCache *self,
    const QVarLengthArray<glyph_t, 16> *glyphs) {
  self->referenceGlyphs(*glyphs);
}

//  void QCRhiDistanceFieldGlyphCache::optimizeAfterRendering()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QCRhiDistanceFieldGlyphCache22optimizeAfterRenderingEv(
    QCRhiDistanceFieldGlyphCache *self) {
  self->optimizeAfterRendering();
}

//  void QCRhiDistanceFieldGlyphCache::commitResourceUpdate(QRhiResourceUpdat
//      eBatch *batch)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QCRhiDistanceFieldGlyphCache20commitResourceUpdateEP23QRhiResourceUpdateBatch(
    QCRhiDistanceFieldGlyphCache *self,
    QRhiResourceUpdateBatch *batch) {
  self->commitResourceUpdate(batch);
}

//  QList<TextureInfo> &QCRhiDistanceFieldGlyphCache::getTextures()
extern "C" Q_DECL_EXPORT
QList<QCRhiDistanceFieldGlyphCache::TextureInfo> *ritual_ZN28QCRhiDistanceFieldGlyphCache11getTexturesEv(
    QCRhiDistanceFieldGlyphCache *self) {
  return &(self->getTextures());
}

//  const QList<TextureInfo> &QCRhiDistanceFieldGlyphCache::getTextures()
//      const
extern "C" Q_DECL_EXPORT
const QList<QCRhiDistanceFieldGlyphCache::TextureInfo> *ritual_ZNK28QCRhiDistanceFieldGlyphCache11getTexturesEv(
    const QCRhiDistanceFieldGlyphCache *self) {
  return &(self->getTextures());
}

//  TexCoord QCRhiDistanceFieldGlyphCache::solidTileTexCoord() const
extern "C" Q_DECL_EXPORT
QCRhiDistanceFieldGlyphCache::TexCoord *ritual_ZNK28QCRhiDistanceFieldGlyphCache17solidTileTexCoordEv(
    const QCRhiDistanceFieldGlyphCache *self) {
  return new QCRhiDistanceFieldGlyphCache::TexCoord(
      self->solidTileTexCoord());
}

//  void QCRhiDistanceFieldGlyphCache::ensureSolidTileTexture()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QCRhiDistanceFieldGlyphCache22ensureSolidTileTextureEv(
    QCRhiDistanceFieldGlyphCache *self) {
  self->ensureSolidTileTexture();
}

//  void QCRhiDistanceFieldGlyphCache::uploadSolidTileIfNeeded()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QCRhiDistanceFieldGlyphCache23uploadSolidTileIfNeededEv(
    QCRhiDistanceFieldGlyphCache *self) {
  self->uploadSolidTileIfNeeded();
}

//  int QCRhiDistanceFieldGlyphCache::maxTextureSize() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK28QCRhiDistanceFieldGlyphCache14maxTextureSizeEv(
    const QCRhiDistanceFieldGlyphCache *self) {
  return self->maxTextureSize();
}

//  void QCRhiDistanceFieldGlyphCache::markGlyphsToRender(const
//      QList<glyph_t> &glyphs)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QCRhiDistanceFieldGlyphCache18markGlyphsToRenderERK5QListIjE(
    QCRhiDistanceFieldGlyphCache *self,
    const QList<glyph_t> *glyphs) {
  self->markGlyphsToRender(*glyphs);
}

//  void QCRhiDistanceFieldGlyphCache::releaseGlyphs(const QSet<glyph_t>
//      &glyphs)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QCRhiDistanceFieldGlyphCache13releaseGlyphsERK4QSetIjE(
    QCRhiDistanceFieldGlyphCache *self,
    const QSet<glyph_t> *glyphs) {
  self->releaseGlyphs(*glyphs);
}

//  bool QCRhiDistanceFieldGlyphCache::useTextureResizeWorkaround() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK28QCRhiDistanceFieldGlyphCache26useTextureResizeWorkaroundEv(
    const QCRhiDistanceFieldGlyphCache *self) {
  return self->useTextureResizeWorkaround();
}

//  void QCRhiDistanceFieldGlyphCache::updateRhiTexture(QRhiTexture *oldTex,
//      QRhiTexture *newTex, QSize newTexSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QCRhiDistanceFieldGlyphCache16updateRhiTextureEP11QRhiTextureS1_5QSize(
    QCRhiDistanceFieldGlyphCache *self,
    QRhiTexture *oldTex,
    QRhiTexture *newTex,
    const QSize *newTexSize) {
  self->updateRhiTexture(oldTex, newTex, *newTexSize);
}

//  Metrics QCRhiDistanceFieldGlyphCache::glyphMetrics(const GlyphData &gd,
//      qreal pixelSize) const
extern "C" Q_DECL_EXPORT
QCRhiDistanceFieldGlyphCache::Metrics *ritual_ZNK28QCRhiDistanceFieldGlyphCache12glyphMetricsERKNS_9GlyphDataEd(
    const QCRhiDistanceFieldGlyphCache *self,
    const QCRhiDistanceFieldGlyphCache::GlyphData *gd,
    qreal pixelSize) {
  return new QCRhiDistanceFieldGlyphCache::Metrics(
      self->glyphMetrics(
          *gd,
          pixelSize));
}

//  qreal QCRhiDistanceFieldGlyphCache::fontScale(qreal pixelSize) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK28QCRhiDistanceFieldGlyphCache9fontScaleEd(
    const QCRhiDistanceFieldGlyphCache *self,
    qreal pixelSize) {
  return self->fontScale(pixelSize);
}

//  qreal QCRhiDistanceFieldGlyphCache::distanceFieldRadius() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK28QCRhiDistanceFieldGlyphCache19distanceFieldRadiusEv(
    const QCRhiDistanceFieldGlyphCache *self) {
  return self->distanceFieldRadius();
}

//  TextureInfo *QCRhiDistanceFieldGlyphCache::textureInfo(int index)
extern "C" Q_DECL_EXPORT
QCRhiDistanceFieldGlyphCache::TextureInfo *ritual_ZN28QCRhiDistanceFieldGlyphCache11textureInfoEi(
    QCRhiDistanceFieldGlyphCache *self,
    int index) {
  return self->textureInfo(index);
}

//  bool QCRhiDistanceFieldGlyphCache::ensureUpdateBatch()
extern "C" Q_DECL_EXPORT
bool ritual_ZN28QCRhiDistanceFieldGlyphCache17ensureUpdateBatchEv(
    QCRhiDistanceFieldGlyphCache *self) {
  return self->ensureUpdateBatch();
}
