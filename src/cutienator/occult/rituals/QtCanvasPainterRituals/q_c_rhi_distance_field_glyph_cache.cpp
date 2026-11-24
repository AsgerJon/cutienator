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

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcareaallocator.cpp, line 48, as _ZN15QCAreaAllocatorD1Ev
inline QCAreaAllocator::~QCAreaAllocator()
{
    delete m_root;
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

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcrhidistancefieldglyphcache.cpp, line 212, as _ZN28QCRhiDistanceFieldGlyphCache15setGlyphTextureERK5QListIjERKNS_11TextureInfoE
inline void QCRhiDistanceFieldGlyphCache::setGlyphTexture(
    const QList<glyph_t> &glyphs, const TextureInfo &tex)
{
    int i = m_textures.indexOf(tex);
    if (i == -1) {
        m_textures.append(tex);
        i = m_textures.size() - 1;
    } else {
        m_textures[i].size = tex.size;
    }
    TextureInfo *texture = &(m_textures[i]);

    int count = glyphs.size();

    for (int j = 0; j < count; ++j) {
        glyph_t glyphIndex = glyphs.at(j);
        GlyphData &gd = glyphData(glyphIndex);
        gd.texture = texture;
    }
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

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcrhidistancefieldglyphcache.cpp, line 405, as _ZN28QCRhiDistanceFieldGlyphCache8populateERK5QListIjE
inline bool QCRhiDistanceFieldGlyphCache::populate(const QList<glyph_t> &glyphs)
{
    QVarLengthArray<glyph_t, 16> referencedGlyphs;
    QVarLengthArray<glyph_t, 16> newGlyphs;
    int count = glyphs.size();

    const auto glyphCount = m_currentReferenceFont.glyphCount;

    for (int i = 0; i < count; ++i) {
        glyph_t glyphIndex = glyphs.at(i);
        if ((int) glyphIndex >= glyphCount && glyphCount > 0) {
            qWarning("Warning: distance-field glyph is not available with index %d", glyphIndex);
            continue;
        }

        GlyphData &gd = glyphData(glyphIndex);
        if (!m_referencedThisFrame.contains(glyphIndex)) {
            ++gd.ref;
            m_referencedThisFrame.insert(glyphIndex);
        }
        referencedGlyphs.append(glyphIndex);

        if (gd.texCoord.isValid() || m_populatingGlyphs.contains(glyphIndex))
            continue;

        m_populatingGlyphs.insert(glyphIndex);

        if (gd.boundingRect.isEmpty()) {
            gd.texCoord.width = 0;
            gd.texCoord.height = 0;
        } else {
            newGlyphs.append(glyphIndex);
        }
    }

    referenceGlyphs(referencedGlyphs);
    if (!newGlyphs.isEmpty())
        requestGlyphs(newGlyphs);

    return newGlyphs.size() > 0;
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

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcrhidistancefieldglyphcache.cpp, line 351, as _ZN28QCRhiDistanceFieldGlyphCache9emptyDataEj
inline QCRhiDistanceFieldGlyphCache::GlyphData &QCRhiDistanceFieldGlyphCache::emptyData(glyph_t glyph)
{
    GlyphData gd;
    gd.texture = &s_emptyTexture;
    auto it = m_glyphsData.insert(glyph, gd);
    return it.value();
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcrhidistancefieldglyphcache.cpp, line 605, as _ZN28QCRhiDistanceFieldGlyphCache15referenceGlyphsERK15QVarLengthArrayIjLx16EE
inline void QCRhiDistanceFieldGlyphCache::referenceGlyphs(const QVarLengthArray<glyph_t, 16> &glyphs)
{
    for (glyph_t glyph : glyphs)
        m_unusedGlyphs.remove(glyph);
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

//  TexCoord QCRhiDistanceFieldGlyphCache::solidTileTexCoord() const
extern "C" Q_DECL_EXPORT
QCRhiDistanceFieldGlyphCache::TexCoord *ritual_ZNK28QCRhiDistanceFieldGlyphCache17solidTileTexCoordEv(
    const QCRhiDistanceFieldGlyphCache *self) {
  return new QCRhiDistanceFieldGlyphCache::TexCoord(
      self->solidTileTexCoord());
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
