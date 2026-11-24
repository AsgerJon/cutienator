//  Written by dev_tooling.RitualGenerator from the records of
//  QtCanvasPainter/6.12.0/QtCanvasPainter/private/qcrhicolorglyphcache_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCanvasPainter/QtCanvasPainter>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCanvasPainter/6.12.0/QtCanvasPainter/private/qcrhicolorglyphcache_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCanvasPainter/private/qcareaallocator_p.h>
#include <QtCanvasPainter/private/qcrhicolorglyphcache_p.h>
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
