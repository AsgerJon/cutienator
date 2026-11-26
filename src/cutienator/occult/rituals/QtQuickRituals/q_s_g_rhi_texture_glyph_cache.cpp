//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgrhitextureglyphcache_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgrhitextureglyphcache_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qtransform.h>
#include <QtGui/qcolor.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qtextureglyphcache_p.h>
#include <QtGui/6.12.0/QtGui/private/qfixed_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/private/qsgrhitextureglyphcache_p.h>
#include <QtQuick/private/qsgdefaultrendercontext_p.h>
#include <QtGui/qrgb.h>
#include <QtGui/private/qdrawhelper_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quick/scenegraph/qsgrhitextureglyphcache.cpp, line 12, as _ZN23QSGRhiTextureGlyphCacheC1EP23QSGDefaultRenderContextN11QFontEngine11GlyphFormatERK10QTransformRK6QColor
inline QSGRhiTextureGlyphCache::QSGRhiTextureGlyphCache(QSGDefaultRenderContext *rc,
                                                 QFontEngine::GlyphFormat format, const QTransform &matrix,
                                                 const QColor &color)
    : QImageTextureGlyphCache(format, matrix, color),
      m_rc(rc),
      m_rhi(rc->rhi())
{
    // Some OpenGL implementations, for instance macOS, have issues with
    // GL_ALPHA render targets. Similarly, BGRA may be problematic on GLES 2.0.
    // So stick with plain image uploads on GL.
    m_resizeWithTextureCopy = m_rhi->backend() != QRhi::OpenGLES2;
}

//  from ../qtdeclarative/src/quick/scenegraph/qsgrhitextureglyphcache.cpp, line 25, as _ZN23QSGRhiTextureGlyphCacheD1Ev
inline QSGRhiTextureGlyphCache::~QSGRhiTextureGlyphCache()
{
    m_rc->deferredReleaseGlyphCacheTexture(m_texture);
}

//  from ../qtdeclarative/src/quick/scenegraph/qsgrhitextureglyphcache.cpp, line 54, as _ZN23QSGRhiTextureGlyphCache17createTextureDataEii
inline void QSGRhiTextureGlyphCache::createTextureData(int width, int height)
{
    width = qMax(128, width);
    height = qMax(32, height);

    if (!m_resizeWithTextureCopy)
        QImageTextureGlyphCache::createTextureData(width, height);

    m_size = QSize(width, height);
}

//  from ../qtdeclarative/src/quick/scenegraph/qsgrhitextureglyphcache.cpp, line 65, as _ZN23QSGRhiTextureGlyphCache17resizeTextureDataEii
inline void QSGRhiTextureGlyphCache::resizeTextureData(int width, int height)
{
    width = qMax(128, width);
    height = qMax(32, height);

    if (m_size.width() >= width && m_size.height() >= height)
        return;

    m_size = QSize(width, height);

    if (m_texture) {
        QRhiTexture *t = createEmptyTexture(m_texture->format());
        if (!t)
            return;

        QRhiResourceUpdateBatch *resourceUpdates = m_rc->glyphCacheResourceUpdates();
        if (m_resizeWithTextureCopy) {
            resourceUpdates->copyTexture(t, m_texture);
        } else {
            QImageTextureGlyphCache::resizeTextureData(width, height);
            QImage img = image();
            prepareGlyphImage(&img);
            QRhiTextureSubresourceUploadDescription subresDesc(img);
            const QSize oldSize = m_texture->pixelSize();
            subresDesc.setSourceSize(QSize(qMin(oldSize.width(), width), qMin(oldSize.height(), height)));
            resourceUpdates->uploadTexture(t, QRhiTextureUploadEntry(0, 0, subresDesc));
        }

        m_rc->deferredReleaseGlyphCacheTexture(m_texture);
        m_texture = t;
    }
}

//  from ../qtdeclarative/src/quick/scenegraph/qsgrhitextureglyphcache.cpp, line 98, as _ZN23QSGRhiTextureGlyphCache16beginFillTextureEv
inline void QSGRhiTextureGlyphCache::beginFillTexture()
{
    Q_ASSERT(m_uploads.isEmpty());
}

//  from ../qtdeclarative/src/quick/scenegraph/qsgrhitextureglyphcache.cpp, line 152, as _ZN23QSGRhiTextureGlyphCache11fillTextureERKN18QTextureGlyphCache5CoordEjRK11QFixedPoint
inline void QSGRhiTextureGlyphCache::fillTexture(const Coord &c, glyph_t glyph, const QFixedPoint &subPixelPosition)
{
    QRhiTextureSubresourceUploadDescription subresDesc;
    QImage mask;

    if (!m_resizeWithTextureCopy) {
        QImageTextureGlyphCache::fillTexture(c, glyph, subPixelPosition);
        // Explicitly copy() here to avoid fillTexture detaching the *entire* image() when
        // it is still referenced by QRhiTextureSubresourceUploadDescription.
        mask = image().copy(QRect(c.x, c.y, c.w, c.h));
    } else {
        mask = textureMapForGlyph(glyph, subPixelPosition);
    }

    prepareGlyphImage(&mask);

    subresDesc.setImage(mask);
    subresDesc.setDestinationTopLeft(QPoint(c.x, c.y));
    m_uploads.append(QRhiTextureUploadEntry(0, 0, subresDesc));
}

//  from ../qtdeclarative/src/quick/scenegraph/qsgrhitextureglyphcache.cpp, line 173, as _ZN23QSGRhiTextureGlyphCache14endFillTextureEv
inline void QSGRhiTextureGlyphCache::endFillTexture()
{
    if (m_uploads.isEmpty())
        return;

    if (!m_texture) {
        QRhiTexture::Format texFormat;
        if (m_format == QFontEngine::Format_A32 || m_format == QFontEngine::Format_ARGB)
            texFormat = m_bgra ? QRhiTexture::BGRA8 : QRhiTexture::RGBA8;
        else // should be R8, but there is the OpenGL ES 2.0 nonsense
            texFormat = QRhiTexture::RED_OR_ALPHA8;

        m_texture = createEmptyTexture(texFormat);
        if (!m_texture)
            return;
    }

    QRhiResourceUpdateBatch *resourceUpdates = m_rc->glyphCacheResourceUpdates();
    QRhiTextureUploadDescription desc;
    desc.setEntries(m_uploads.cbegin(), m_uploads.cend());
    resourceUpdates->uploadTexture(m_texture, desc);
    m_uploads.clear();
}

//  from ../qtdeclarative/src/quick/scenegraph/qsgrhitextureglyphcache.cpp, line 197, as _ZNK23QSGRhiTextureGlyphCache12glyphPaddingEv
inline int QSGRhiTextureGlyphCache::glyphPadding() const
{
    if (m_format == QFontEngine::Format_Mono)
        return 8;
    else
        return 1;
}

//  from ../qtdeclarative/src/quick/scenegraph/qsgrhitextureglyphcache.cpp, line 205, as _ZNK23QSGRhiTextureGlyphCache15maxTextureWidthEv
inline int QSGRhiTextureGlyphCache::maxTextureWidth() const
{
    return m_rhi->resourceLimit(QRhi::TextureSizeMax);
}

//  from ../qtdeclarative/src/quick/scenegraph/qsgrhitextureglyphcache.cpp, line 210, as _ZNK23QSGRhiTextureGlyphCache16maxTextureHeightEv
inline int QSGRhiTextureGlyphCache::maxTextureHeight() const
{
    if (!m_resizeWithTextureCopy)
        return qMin(1024, m_rhi->resourceLimit(QRhi::TextureSizeMax));

    return m_rhi->resourceLimit(QRhi::TextureSizeMax);
}

//  from ../qtdeclarative/src/quick/scenegraph/qsgrhitextureglyphcache.cpp, line 218, as _ZN23QSGRhiTextureGlyphCache21commitResourceUpdatesEP23QRhiResourceUpdateBatch
inline void QSGRhiTextureGlyphCache::commitResourceUpdates(QRhiResourceUpdateBatch *mergeInto)
{
    if (QRhiResourceUpdateBatch *resourceUpdates = m_rc->maybeGlyphCacheResourceUpdates()) {
        mergeInto->merge(resourceUpdates);
        m_rc->resetGlyphCacheResources();
    }
}

//  from ../qtdeclarative/src/quick/scenegraph/qsgrhitextureglyphcache.cpp, line 226, as _ZNK23QSGRhiTextureGlyphCache29eightBitFormatIsAlphaSwizzledEv
inline bool QSGRhiTextureGlyphCache::eightBitFormatIsAlphaSwizzled() const
{
    // return true when the shaders for 8-bit formats need .a instead of .r
    // when sampling the texture
    return !m_rhi->isFeatureSupported(QRhi::RedOrAlpha8IsRed);
}

//  from ../qtdeclarative/src/quick/scenegraph/qsgrhitextureglyphcache.cpp, line 103, as _ZN23QSGRhiTextureGlyphCache17prepareGlyphImageEP6QImage
inline void QSGRhiTextureGlyphCache::prepareGlyphImage(QImage *img)
{
    const int maskWidth = img->width();
    const int maskHeight = img->height();
#if Q_BYTE_ORDER != Q_BIG_ENDIAN
    const bool supportsBgra = m_rhi->isTextureFormatSupported(QRhiTexture::BGRA8);
#endif
    m_bgra = false;

    if (img->format() == QImage::Format_Mono) {
        *img = std::move(*img).convertToFormat(QImage::Format_Grayscale8);
    } else if (img->format() == QImage::Format_RGB32 || img->format() == QImage::Format_ARGB32_Premultiplied) {
        // We need to make the alpha component equal to the average of the RGB values.
        // This is needed when drawing sub-pixel antialiased text on translucent targets.
        if (img->format() == QImage::Format_RGB32
#if Q_BYTE_ORDER != Q_BIG_ENDIAN
            || !supportsBgra
#endif
        ) {
            for (int y = 0; y < maskHeight; ++y) {
                QRgb *src = reinterpret_cast<QRgb *>(img->scanLine(y));
                for (int x = 0; x < maskWidth; ++x) {
                    QRgb &rgb = src[x];

                    if (img->format() == QImage::Format_RGB32) {
                        int r = qRed(rgb);
                        int g = qGreen(rgb);
                        int b = qBlue(rgb);
                        int avg = (r + g + b + 1) / 3; // "+1" for rounding.
                        rgb = qRgba(r, g, b, avg);
                    }

#if Q_BYTE_ORDER != Q_BIG_ENDIAN
                    if (!supportsBgra) {
                        // swizzle the bits to accommodate for the RGBA upload.
                        rgb = ARGB2RGBA(rgb);
                        m_bgra = false;
                    }
#endif
                }
            }
        }
#if Q_BYTE_ORDER != Q_BIG_ENDIAN
        if (supportsBgra)
            m_bgra = true;
#endif
    }
}

//  from ../qtdeclarative/src/quick/scenegraph/qsgrhitextureglyphcache.cpp, line 30, as _ZN23QSGRhiTextureGlyphCache18createEmptyTextureEN11QRhiTexture6FormatE
inline QRhiTexture *QSGRhiTextureGlyphCache::createEmptyTexture(QRhiTexture::Format format)
{
    QRhiTexture *t = m_rhi->newTexture(format, m_size, 1, QRhiTexture::UsedAsTransferSource);
    if (!t->create()) {
        qWarning("Failed to build new glyph cache texture of size %dx%d", m_size.width(), m_size.height());
        return nullptr;
    }

    QRhiResourceUpdateBatch *resourceUpdates = m_rc->glyphCacheResourceUpdates();

    // The new texture must be cleared to 0 always, this cannot be avoided
    // otherwise artifacts will occur around the glyphs.
    QByteArray data;
    if (format == QRhiTexture::RED_OR_ALPHA8)
        data.fill(0, m_size.width() * m_size.height());
    else
        data.fill(0, m_size.width() * m_size.height() * 4);
    QRhiTextureSubresourceUploadDescription subresDesc(data.constData(), data.size());
    subresDesc.setSourceSize(m_size);
    resourceUpdates->uploadTexture(t, QRhiTextureUploadEntry(0, 0, subresDesc));

    return t;
}
//  -----------------------------------------------------------------------

//  A QSGRhiTextureGlyphCache that Python can take functions over in. Every QSGRhiTextureGlyphCache
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQSGRhiTextureGlyphCacheCall0)(const void *, int, int, int *);
typedef void (*CuteQSGRhiTextureGlyphCacheCall1)(const void *, int, int, int *);
typedef void (*CuteQSGRhiTextureGlyphCacheCall2)(const void *, int *);
typedef void (*CuteQSGRhiTextureGlyphCacheCall3)(const void *, const QTextureGlyphCache::Coord *, glyph_t, const QFixedPoint *, int *);
typedef void (*CuteQSGRhiTextureGlyphCacheCall4)(const void *, int *);
typedef int (*CuteQSGRhiTextureGlyphCacheCall5)(const void *, int *);
typedef int (*CuteQSGRhiTextureGlyphCacheCall6)(const void *, int *);
typedef int (*CuteQSGRhiTextureGlyphCacheCall7)(const void *, int *);
class CuteQSGRhiTextureGlyphCache : public QSGRhiTextureGlyphCache {
public:
  using QSGRhiTextureGlyphCache::QSGRhiTextureGlyphCache;
  CuteQSGRhiTextureGlyphCache(const QSGRhiTextureGlyphCache & other) : QSGRhiTextureGlyphCache(other) {}
  void *taken[8] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN18QTextureGlyphCache17createTextureDataEii")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QTextureGlyphCache17resizeTextureDataEii")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QTextureGlyphCache16beginFillTextureEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QTextureGlyphCache11fillTextureERKNS_5CoordEjRK11QFixedPoint")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QTextureGlyphCache14endFillTextureEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QTextureGlyphCache12glyphPaddingEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QTextureGlyphCache15maxTextureWidthEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QTextureGlyphCache16maxTextureHeightEv")) {
      taken[7] = call;
      return true;
    }
    return false;
  }

  //  void QSGRhiTextureGlyphCache::createTextureData(int width, int
  //      height)
  void createTextureData(int width, int height) override {
    if (taken[0]) {
      int handled = 0;
      CuteQSGRhiTextureGlyphCacheCall0 call = reinterpret_cast<CuteQSGRhiTextureGlyphCacheCall0>(taken[0]);
      call(this, width, height, &handled);
      if (handled) return;
    }
    QSGRhiTextureGlyphCache::createTextureData(width, height);
  }

  //  void QSGRhiTextureGlyphCache::resizeTextureData(int width, int
  //      height)
  void resizeTextureData(int width, int height) override {
    if (taken[1]) {
      int handled = 0;
      CuteQSGRhiTextureGlyphCacheCall1 call = reinterpret_cast<CuteQSGRhiTextureGlyphCacheCall1>(taken[1]);
      call(this, width, height, &handled);
      if (handled) return;
    }
    QSGRhiTextureGlyphCache::resizeTextureData(width, height);
  }

  //  void QSGRhiTextureGlyphCache::beginFillTexture()
  void beginFillTexture() override {
    if (taken[2]) {
      int handled = 0;
      CuteQSGRhiTextureGlyphCacheCall2 call = reinterpret_cast<CuteQSGRhiTextureGlyphCacheCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QSGRhiTextureGlyphCache::beginFillTexture();
  }

  //  void QSGRhiTextureGlyphCache::fillTexture(const Coord &c, glyph_t
  //      glyph, const QFixedPoint &subPixelPosition)
  void fillTexture(
      const QTextureGlyphCache::Coord &c,
      glyph_t glyph,
      const QFixedPoint &subPixelPosition) override {
    if (taken[3]) {
      int handled = 0;
      CuteQSGRhiTextureGlyphCacheCall3 call = reinterpret_cast<CuteQSGRhiTextureGlyphCacheCall3>(taken[3]);
      call(this, &c, glyph, &subPixelPosition, &handled);
      if (handled) return;
    }
    QSGRhiTextureGlyphCache::fillTexture(c, glyph, subPixelPosition);
  }

  //  void QSGRhiTextureGlyphCache::endFillTexture()
  void endFillTexture() override {
    if (taken[4]) {
      int handled = 0;
      CuteQSGRhiTextureGlyphCacheCall4 call = reinterpret_cast<CuteQSGRhiTextureGlyphCacheCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QSGRhiTextureGlyphCache::endFillTexture();
  }

  //  int QSGRhiTextureGlyphCache::glyphPadding() const
  int glyphPadding() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQSGRhiTextureGlyphCacheCall5 call = reinterpret_cast<CuteQSGRhiTextureGlyphCacheCall5>(taken[5]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QSGRhiTextureGlyphCache::glyphPadding();
  }

  //  int QSGRhiTextureGlyphCache::maxTextureWidth() const
  int maxTextureWidth() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQSGRhiTextureGlyphCacheCall6 call = reinterpret_cast<CuteQSGRhiTextureGlyphCacheCall6>(taken[6]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QSGRhiTextureGlyphCache::maxTextureWidth();
  }

  //  int QSGRhiTextureGlyphCache::maxTextureHeight() const
  int maxTextureHeight() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQSGRhiTextureGlyphCacheCall7 call = reinterpret_cast<CuteQSGRhiTextureGlyphCacheCall7>(taken[7]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QSGRhiTextureGlyphCache::maxTextureHeight();
  }
};

//  QSGRhiTextureGlyphCache::QSGRhiTextureGlyphCache(QSGDefaultRenderContext
//      *rc, QFontEngine::GlyphFormat format, const QTransform &matrix, const
//      QColor &color)
extern "C" Q_DECL_EXPORT
QSGRhiTextureGlyphCache *ritual_ZN23QSGRhiTextureGlyphCacheC1EP23QSGDefaultRenderContextN11QFontEngine11GlyphFormatERK10QTransformRK6QColor(
    QSGDefaultRenderContext *rc,
    QFontEngine::GlyphFormat format,
    const QTransform *matrix,
    const QColor *color) {
  return new CuteQSGRhiTextureGlyphCache(rc, format, *matrix, *color);
}

//  QSGRhiTextureGlyphCache::~QSGRhiTextureGlyphCache()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QSGRhiTextureGlyphCacheD1Ev(QSGRhiTextureGlyphCache *self) {
  delete self;
}

//  void QSGRhiTextureGlyphCache::createTextureData(int width, int height)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QSGRhiTextureGlyphCache17createTextureDataEii(
    QSGRhiTextureGlyphCache *self,
    int width,
    int height) {
  self->createTextureData(width, height);
}

//  void QSGRhiTextureGlyphCache::resizeTextureData(int width, int height)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QSGRhiTextureGlyphCache17resizeTextureDataEii(
    QSGRhiTextureGlyphCache *self,
    int width,
    int height) {
  self->resizeTextureData(width, height);
}

//  void QSGRhiTextureGlyphCache::beginFillTexture()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QSGRhiTextureGlyphCache16beginFillTextureEv(
    QSGRhiTextureGlyphCache *self) {
  self->beginFillTexture();
}

//  void QSGRhiTextureGlyphCache::fillTexture(const Coord &c, glyph_t glyph,
//      const QFixedPoint &subPixelPosition)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QSGRhiTextureGlyphCache11fillTextureERKN18QTextureGlyphCache5CoordEjRK11QFixedPoint(
    QSGRhiTextureGlyphCache *self,
    const QTextureGlyphCache::Coord *c,
    glyph_t glyph,
    const QFixedPoint *subPixelPosition) {
  self->fillTexture(*c, glyph, *subPixelPosition);
}

//  void QSGRhiTextureGlyphCache::endFillTexture()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QSGRhiTextureGlyphCache14endFillTextureEv(
    QSGRhiTextureGlyphCache *self) {
  self->endFillTexture();
}

//  int QSGRhiTextureGlyphCache::glyphPadding() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK23QSGRhiTextureGlyphCache12glyphPaddingEv(
    const QSGRhiTextureGlyphCache *self) {
  return self->glyphPadding();
}

//  int QSGRhiTextureGlyphCache::maxTextureWidth() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK23QSGRhiTextureGlyphCache15maxTextureWidthEv(
    const QSGRhiTextureGlyphCache *self) {
  return self->maxTextureWidth();
}

//  int QSGRhiTextureGlyphCache::maxTextureHeight() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK23QSGRhiTextureGlyphCache16maxTextureHeightEv(
    const QSGRhiTextureGlyphCache *self) {
  return self->maxTextureHeight();
}

//  QRhiTexture *QSGRhiTextureGlyphCache::texture() const
extern "C" Q_DECL_EXPORT
QRhiTexture *ritual_ZNK23QSGRhiTextureGlyphCache7textureEv(
    const QSGRhiTextureGlyphCache *self) {
  return self->texture();
}

//  void
//      QSGRhiTextureGlyphCache::commitResourceUpdates(QRhiResourceUpdateBatc
//      h *mergeInto)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QSGRhiTextureGlyphCache21commitResourceUpdatesEP23QRhiResourceUpdateBatch(
    QSGRhiTextureGlyphCache *self,
    QRhiResourceUpdateBatch *mergeInto) {
  self->commitResourceUpdates(mergeInto);
}

//  int QSGRhiTextureGlyphCache::width() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK23QSGRhiTextureGlyphCache5widthEv(
    const QSGRhiTextureGlyphCache *self) {
  return self->width();
}

//  int QSGRhiTextureGlyphCache::height() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK23QSGRhiTextureGlyphCache6heightEv(
    const QSGRhiTextureGlyphCache *self) {
  return self->height();
}

//  bool QSGRhiTextureGlyphCache::eightBitFormatIsAlphaSwizzled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QSGRhiTextureGlyphCache29eightBitFormatIsAlphaSwizzledEv(
    const QSGRhiTextureGlyphCache *self) {
  return self->eightBitFormatIsAlphaSwizzled();
}

//  void QSGRhiTextureGlyphCache::prepareGlyphImage(QImage *img)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QSGRhiTextureGlyphCache17prepareGlyphImageEP6QImage(
    QSGRhiTextureGlyphCache *self,
    QImage *img) {
  self->prepareGlyphImage(img);
}

//  QRhiTexture
//      *QSGRhiTextureGlyphCache::createEmptyTexture(QRhiTexture::Format
//      format)
extern "C" Q_DECL_EXPORT
QRhiTexture *ritual_ZN23QSGRhiTextureGlyphCache18createEmptyTextureEN11QRhiTexture6FormatE(
    QSGRhiTextureGlyphCache *self,
    QRhiTexture::Format format) {
  return self->createEmptyTexture(format);
}

//  a Python function taken by a CuteQSGRhiTextureGlyphCache, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSGRhiTextureGlyphCache(
    QSGRhiTextureGlyphCache *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSGRhiTextureGlyphCache *>(self)->take(key, call);
}

//  void QSGRhiTextureGlyphCache::createTextureData(int width, int height)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QSGRhiTextureGlyphCache17createTextureDataEii(
    QSGRhiTextureGlyphCache *self,
    int width,
    int height) {
  self->QSGRhiTextureGlyphCache::createTextureData(width, height);
}

//  void QSGRhiTextureGlyphCache::resizeTextureData(int width, int height)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QSGRhiTextureGlyphCache17resizeTextureDataEii(
    QSGRhiTextureGlyphCache *self,
    int width,
    int height) {
  self->QSGRhiTextureGlyphCache::resizeTextureData(width, height);
}

//  void QSGRhiTextureGlyphCache::beginFillTexture()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QSGRhiTextureGlyphCache16beginFillTextureEv(
    QSGRhiTextureGlyphCache *self) {
  self->QSGRhiTextureGlyphCache::beginFillTexture();
}

//  void QSGRhiTextureGlyphCache::fillTexture(const Coord &c, glyph_t glyph,
//      const QFixedPoint &subPixelPosition)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QSGRhiTextureGlyphCache11fillTextureERKN18QTextureGlyphCache5CoordEjRK11QFixedPoint(
    QSGRhiTextureGlyphCache *self,
    const QTextureGlyphCache::Coord *c,
    glyph_t glyph,
    const QFixedPoint *subPixelPosition) {
  self->QSGRhiTextureGlyphCache::fillTexture(*c, glyph, *subPixelPosition);
}

//  void QSGRhiTextureGlyphCache::endFillTexture()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QSGRhiTextureGlyphCache14endFillTextureEv(
    QSGRhiTextureGlyphCache *self) {
  self->QSGRhiTextureGlyphCache::endFillTexture();
}

//  int QSGRhiTextureGlyphCache::glyphPadding() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK23QSGRhiTextureGlyphCache12glyphPaddingEv(
    const QSGRhiTextureGlyphCache *self) {
  return self->QSGRhiTextureGlyphCache::glyphPadding();
}

//  int QSGRhiTextureGlyphCache::maxTextureWidth() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK23QSGRhiTextureGlyphCache15maxTextureWidthEv(
    const QSGRhiTextureGlyphCache *self) {
  return self->QSGRhiTextureGlyphCache::maxTextureWidth();
}

//  int QSGRhiTextureGlyphCache::maxTextureHeight() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK23QSGRhiTextureGlyphCache16maxTextureHeightEv(
    const QSGRhiTextureGlyphCache *self) {
  return self->QSGRhiTextureGlyphCache::maxTextureHeight();
}
