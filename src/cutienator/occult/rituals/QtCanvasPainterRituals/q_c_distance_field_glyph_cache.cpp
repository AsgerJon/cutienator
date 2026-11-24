//  Written by dev_tooling.RitualGenerator from the records of QtCanvasPainte
//  r/6.12.0/QtCanvasPainter/private/qcdistancefieldglyphcache_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCanvasPainter/QtCanvasPainter>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCanvasPainter/6.12.0/QtCanvasPainter/private/qcdistancefieldglyphcache_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qrawfont.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qcrhicolorglyphcache_p.h"
#include <QtGui/private/qrawfont_p.h>
#include "qcrhidistancefieldglyphcache_p.h"
#include <QtGui/private/qrawfont_p.h>
#include "qcdistancefieldglyphcache_p.h"
#include "qcanvaspainter_p.h"
#include <private/qrawfont_p.h>
#include <cmath>
#include "qcareaallocator_p.h"
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

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

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcrhidistancefieldglyphcache.cpp, line 22, as _ZN28QCRhiDistanceFieldGlyphCacheC1EP4QRhi
inline QCRhiDistanceFieldGlyphCache::QCRhiDistanceFieldGlyphCache(QRhi *rhi)
    : m_rhi(rhi)
    , m_pendingGlyphs(64)
{
}

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcareaallocator.cpp, line 48, as _ZN15QCAreaAllocatorD1Ev
inline QCAreaAllocator::~QCAreaAllocator()
{
    delete m_root;
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
