//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgdefaultglyphnode_p_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgdefaultglyphnode_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qcolor.h>
#include <QtGui/qvectornd.h>
#include <QtCore/qpoint.h>
#include <QtCore/qmargins.h>
#include <QtCore/qlist.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/private/qsgdefaultglyphnode_p_p.h>
#include <QtQuick/private/qsgmaterialshader_p.h>
#include <QtGui/private/qguiapplication_p.h>
#include <QtGui/qpa/qplatformintegration.h>
#include <QtGui/private/qfontengine_p.h>
#include <QtQuick/qquickwindow.h>
#include <QtQuick/private/qsgtexture_p.h>
#include <QtQuick/private/qsgdefaultrendercontext_p.h>
#include <QtGui/private/qrawfont_p.h>
#include <QtCore/qmath.h>
#include <QtQuick/private/qsgrhitextureglyphcache_p.h>
#include <QtQuick/private/qsgdefaultrendercontext_p.h>
#include <QtGui/qrgb.h>
#include <QtGui/private/qdrawhelper_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quick/scenegraph/qsgdefaultglyphnode_p.cpp, line 539, as local:qsgdefaultglyphnode_p.cpp:qsg_colorDiff
static inline int qsg_colorDiff(const QVector4D &a, const QVector4D &b)
{
    if (a.x() != b.x())
        return a.x() > b.x() ? 1 : -1;
    if (a.y() != b.y())
        return a.y() > b.y() ? 1 : -1;
    if (a.z() != b.z())
        return a.z() > b.z() ? 1 : -1;
    if (a.w() != b.w())
        return a.w() > b.w() ? 1 : -1;
    return 0;
}

//  from ../qtdeclarative/src/quick/scenegraph/qsgdefaultglyphnode_p.cpp, line 323, as _ZN19QSGTextMaskMaterialD2Ev
inline QSGTextMaskMaterial::~QSGTextMaskMaterial()
{
    if (m_retainedFontEngine != nullptr)
        m_rc->unregisterFontengineForCleanup(m_retainedFontEngine);
    delete m_texture;
}

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

//  from ../qtdeclarative/src/quick/scenegraph/qsgdefaultglyphnode_p.cpp, line 499, as _ZNK19QSGTextMaskMaterial4typeEv
inline QSGMaterialType *QSGTextMaskMaterial::type() const
{
    static QSGMaterialType argb, rgb, gray;
    switch (glyphCache()->glyphFormat()) {
    case QFontEngine::Format_ARGB:
        return &argb;
    case QFontEngine::Format_A32:
        return &rgb;
    case QFontEngine::Format_A8:
    default:
        return &gray;
    }
}

//  from ../qtdeclarative/src/quick/scenegraph/qsgdefaultglyphnode_p.cpp, line 552, as _ZNK19QSGTextMaskMaterial7compareEPK11QSGMaterial
inline int QSGTextMaskMaterial::compare(const QSGMaterial *o) const
{
    Q_ASSERT(o && type() == o->type());
    const QSGTextMaskMaterial *other = static_cast<const QSGTextMaskMaterial *>(o);
    if (m_glyphCache != other->m_glyphCache)
        return m_glyphCache.data() < other->m_glyphCache.data() ? -1 : 1;
    return qsg_colorDiff(m_color, other->m_color);
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

//  from ../qtdeclarative/src/quick/scenegraph/qsgdefaultglyphnode_p.cpp, line 330, as _ZN19QSGTextMaskMaterial8setColorERK9QVector4D
inline void QSGTextMaskMaterial::setColor(const QVector4D &color)
{
    if (m_color == color)
        return;

    m_color = color;

    // If it is an RGB cache, then the pen color is actually part of the cache key
    // so it has to be updated
    if (m_glyphCache != nullptr && m_glyphCache->glyphFormat() == QFontEngine::Format_ARGB)
        updateCache(QFontEngine::Format_ARGB);
}

//  from ../qtdeclarative/src/quick/scenegraph/qsgdefaultglyphnode_p.cpp, line 355, as _ZN19QSGTextMaskMaterial11updateCacheEN11QFontEngine11GlyphFormatE
inline void QSGTextMaskMaterial::updateCache(QFontEngine::GlyphFormat glyphFormat)
{
    // The following piece of code will read/write to the font engine's caches,
    // potentially from different threads. However, this is safe because this
    // code is only called from QQuickItem::updatePaintNode() which is called
    // only when the GUI is blocked, and multiple threads will call it in
    // sequence. See also QSGRenderContext::invalidate

    QRawFontPrivate *fontD = QRawFontPrivate::get(m_font);
    if (QFontEngine *fontEngine = fontD->fontEngine) {
        if (glyphFormat == QFontEngine::Format_None) {
            glyphFormat = fontEngine->glyphFormat != QFontEngine::Format_None
                        ? fontEngine->glyphFormat
                        : QFontEngine::Format_A32;
        }

        qreal devicePixelRatio;
        void *cacheKey;
        Q_ASSERT(m_rhi);
        Q_ASSERT(m_rc);
        cacheKey = m_rc;
        // Get the dpr the modern way. This value retrieved via the
        // rendercontext matches what RenderState::devicePixelRatio()
        // exposes to the material shaders later on.
        devicePixelRatio = m_rc->currentDevicePixelRatio();

        QTransform glyphCacheTransform = QTransform::fromScale(devicePixelRatio, devicePixelRatio);
        if (!fontEngine->supportsTransformation(glyphCacheTransform))
            glyphCacheTransform = QTransform();

        QColor color = glyphFormat == QFontEngine::Format_ARGB ? QColor::fromRgbF(m_color.x(), m_color.y(), m_color.z(), m_color.w()) : QColor();
        m_glyphCache = fontEngine->glyphCache(cacheKey, glyphFormat, glyphCacheTransform, color);
        if (!m_glyphCache || int(m_glyphCache->glyphFormat()) != glyphFormat) {
            m_glyphCache = new QSGRhiTextureGlyphCache(m_rc, glyphFormat, glyphCacheTransform, color);
            fontEngine->setGlyphCache(cacheKey, m_glyphCache.data());
            if (m_retainedFontEngine != nullptr)
                m_rc->unregisterFontengineForCleanup(m_retainedFontEngine);

            // Note: This is reference counted by the render context, so it will stay alive until
            // we release that reference
            m_retainedFontEngine = fontEngine;
            m_rc->registerFontengineForCleanup(fontEngine);
        }
    }
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

//  from ../qtdeclarative/src/quick/scenegraph/qsgdefaultglyphnode_p.cpp, line 561, as _ZN19QSGTextMaskMaterial14ensureUpToDateEv
inline bool QSGTextMaskMaterial::ensureUpToDate()
{
    QSGRhiTextureGlyphCache *gc = rhiGlyphCache();
    QSize glyphCacheSize(gc->width(), gc->height());
    if (glyphCacheSize != m_size) {
        if (m_texture)
            delete m_texture;
        m_texture = new QSGPlainTexture;
        m_texture->setTexture(gc->texture());
        m_texture->setTextureSize(QSize(gc->width(), gc->height()));
        m_texture->setOwnsTexture(false);
        m_size = glyphCacheSize;
        return true;
    }
    return false;
}

//  from ../qtdeclarative/src/quick/scenegraph/qsgdefaultglyphnode_p.cpp, line 513, as _ZNK19QSGTextMaskMaterial10glyphCacheEv
inline QTextureGlyphCache *QSGTextMaskMaterial::glyphCache() const
{
    return static_cast<QTextureGlyphCache *>(m_glyphCache.data());
}

//  from ../qtdeclarative/src/quick/scenegraph/qsgdefaultglyphnode_p.cpp, line 518, as _ZNK19QSGTextMaskMaterial13rhiGlyphCacheEv
inline QSGRhiTextureGlyphCache *QSGTextMaskMaterial::rhiGlyphCache() const
{
    return static_cast<QSGRhiTextureGlyphCache *>(glyphCache());
}

//  from ../qtdeclarative/src/quick/scenegraph/qsgdefaultglyphnode_p.cpp, line 401, as _ZN19QSGTextMaskMaterial8populateERK7QPointFRK5QListIjERKS3_IS0_EP11QSGGeometryP6QRectFPS0_RK8QMargins
inline void QSGTextMaskMaterial::populate(const QPointF &p,
                                   const QList<quint32> &glyphIndexes,
                                   const QList<QPointF> &glyphPositions,
                                   QSGGeometry *geometry,
                                   QRectF *boundingRect,
                                   QPointF *baseLine,
                                   const QMargins &margins)
{
    Q_ASSERT(m_font.isValid());
    QPointF position(p.x(), p.y() - m_font.ascent());
    QList<QFixedPoint> fixedPointPositions;
    const int glyphPositionsSize = glyphPositions.size();
    fixedPointPositions.reserve(glyphPositionsSize);
    for (int i=0; i < glyphPositionsSize; ++i)
        fixedPointPositions.append(QFixedPoint::fromPointF(position + glyphPositions.at(i)));

    QTextureGlyphCache *cache = glyphCache();

    QRawFontPrivate *fontD = QRawFontPrivate::get(m_font);
    cache->populate(fontD->fontEngine,
                    glyphIndexes.size(),
                    glyphIndexes.constData(),
                    fixedPointPositions.data(),
                    QPainter::RenderHints(),
                    true);
    cache->fillInPendingGlyphs();

    int margin = fontD->fontEngine->glyphMargin(cache->glyphFormat());

    qreal glyphCacheScaleX = cache->transform().m11();
    qreal glyphCacheScaleY = cache->transform().m22();
    qreal glyphCacheInverseScaleX = 1.0 / glyphCacheScaleX;
    qreal glyphCacheInverseScaleY = 1.0 / glyphCacheScaleY;
    qreal scaledMargin = margin * glyphCacheInverseScaleX;

    Q_ASSERT(geometry->indexType() ==  QSGGeometry::UnsignedShortType);
    geometry->allocate(glyphIndexes.size() * 4, glyphIndexes.size() * 6);
    QVector4D *vp = (QVector4D *)geometry->vertexDataAsTexturedPoint2D();
    Q_ASSERT(geometry->sizeOfVertex() == sizeof(QVector4D));
    ushort *ip = geometry->indexDataAsUShort();

    bool supportsSubPixelPositions = fontD->fontEngine->supportsHorizontalSubPixelPositions();
    for (int i=0; i<glyphIndexes.size(); ++i) {
         QPointF glyphPosition = glyphPositions.at(i) + position;
         QFixedPoint fixedPointPosition = fixedPointPositions.at(i);

         QFixed subPixelPosition;
         if (supportsSubPixelPositions)
             subPixelPosition = fontD->fontEngine->subPixelPositionForX(QFixed::fromReal(fixedPointPosition.x.toReal() * glyphCacheScaleX));

         QTextureGlyphCache::GlyphAndSubPixelPosition glyph(glyphIndexes.at(i),
                                                            QFixedPoint(subPixelPosition, 0));
         const QTextureGlyphCache::Coord &c = cache->coords.value(glyph);

         // On a retina screen the glyph positions are not pre-scaled (as opposed to
         // eg. the raster paint engine). To ensure that we get the same behavior as
         // the raster engine (and CoreText itself) when it comes to rounding of the
         // coordinates, we need to apply the scale factor before rounding, and then
         // apply the inverse scale to get back to the coordinate system of the node.

         qreal x = (qFloor(glyphPosition.x() * glyphCacheScaleX) * glyphCacheInverseScaleX) +
                        (c.baseLineX * glyphCacheInverseScaleX) - scaledMargin;
         qreal y = (qRound(glyphPosition.y() * glyphCacheScaleY) * glyphCacheInverseScaleY) -
                        (c.baseLineY * glyphCacheInverseScaleY) - scaledMargin;

         qreal w = c.w * glyphCacheInverseScaleX;
         qreal h = c.h * glyphCacheInverseScaleY;

         *boundingRect |= QRectF(x + scaledMargin, y + scaledMargin, w, h);

         float cx1 = x - margins.left();
         float cx2 = x + w + margins.right();
         float cy1 = y - margins.top();
         float cy2 = y + h + margins.bottom();

         float tx1 = c.x - margins.left();
         float tx2 = c.x + c.w + margins.right();
         float ty1 = c.y - margins.top();
         float ty2 = c.y + c.h + margins.bottom();

         if (baseLine->isNull())
             *baseLine = glyphPosition;

         vp[4 * i + 0] = QVector4D(cx1, cy1, tx1, ty1);
         vp[4 * i + 1] = QVector4D(cx2, cy1, tx2, ty1);
         vp[4 * i + 2] = QVector4D(cx1, cy2, tx1, ty2);
         vp[4 * i + 3] = QVector4D(cx2, cy2, tx2, ty2);

         int o = i * 4;
         ip[6 * i + 0] = o + 0;
         ip[6 * i + 1] = o + 2;
         ip[6 * i + 2] = o + 3;
         ip[6 * i + 3] = o + 3;
         ip[6 * i + 4] = o + 1;
         ip[6 * i + 5] = o + 0;
    }
}
//  -----------------------------------------------------------------------

//  A QSGTextMaskMaterial that Python can take functions over in. Every QSGTextMaskMaterial
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQSGTextMaskMaterialCall0)(const void *, int *);
typedef void * (*CuteQSGTextMaskMaterialCall1)(const void *, int, int *);
typedef int (*CuteQSGTextMaskMaterialCall2)(const void *, const QSGMaterial *, int *);
class CuteQSGTextMaskMaterial : public QSGTextMaskMaterial {
public:
  using QSGTextMaskMaterial::QSGTextMaskMaterial;
  void *taken[3] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK11QSGMaterial4typeEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QSGMaterial12createShaderEN20QSGRendererInterface10RenderModeE")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QSGMaterial7compareEPKS_")) {
      taken[2] = call;
      return true;
    }
    return false;
  }

  //  QSGMaterialType *QSGTextMaskMaterial::type() const
  QSGMaterialType *type() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSGTextMaskMaterialCall0 call = reinterpret_cast<CuteQSGTextMaskMaterialCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGMaterialType *>(given);
    }
    return QSGTextMaskMaterial::type();
  }

  //  QSGMaterialShader
  //      *QSGTextMaskMaterial::createShader(QSGRendererInterface::RenderMo
  //      de renderMode) const
  QSGMaterialShader *createShader(
      QSGRendererInterface::RenderMode renderMode) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQSGTextMaskMaterialCall1 call = reinterpret_cast<CuteQSGTextMaskMaterialCall1>(taken[1]);
      void * given = call(this, static_cast<int>(renderMode), &handled);
      if (handled) return static_cast<QSGMaterialShader *>(given);
    }
    return QSGTextMaskMaterial::createShader(renderMode);
  }

  //  int QSGTextMaskMaterial::compare(const QSGMaterial *other) const
  int compare(const QSGMaterial *other) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQSGTextMaskMaterialCall2 call = reinterpret_cast<CuteQSGTextMaskMaterialCall2>(taken[2]);
      int given = call(this, other, &handled);
      if (handled) return given;
    }
    return QSGTextMaskMaterial::compare(other);
  }
};

//  QSGTextMaskMaterial::~QSGTextMaskMaterial()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSGTextMaskMaterialD1Ev(QSGTextMaskMaterial *self) {
  delete self;
}

//  QSGMaterialType *QSGTextMaskMaterial::type() const
extern "C" Q_DECL_EXPORT
QSGMaterialType *ritual_ZNK19QSGTextMaskMaterial4typeEv(
    const QSGTextMaskMaterial *self) {
  return self->type();
}

//  QSGMaterialShader
//      *QSGTextMaskMaterial::createShader(QSGRendererInterface::RenderMode
//      renderMode) const
extern "C" Q_DECL_EXPORT
QSGMaterialShader *ritual_ZNK19QSGTextMaskMaterial12createShaderEN20QSGRendererInterface10RenderModeE(
    const QSGTextMaskMaterial *self,
    QSGRendererInterface::RenderMode renderMode) {
  return self->createShader(renderMode);
}

//  int QSGTextMaskMaterial::compare(const QSGMaterial *other) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QSGTextMaskMaterial7compareEPK11QSGMaterial(
    const QSGTextMaskMaterial *self,
    const QSGMaterial *other) {
  return self->compare(other);
}

//  void QSGTextMaskMaterial::setColor(const QColor &c)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSGTextMaskMaterial8setColorERK6QColor(
    QSGTextMaskMaterial *self,
    const QColor *c) {
  self->setColor(*c);
}

//  const QVector4D &QSGTextMaskMaterial::color() const
extern "C" Q_DECL_EXPORT
QVector4D *ritual_ZNK19QSGTextMaskMaterial5colorEv(
    const QSGTextMaskMaterial *self) {
  return new QVector4D(self->color());
}

//  QSGTexture *QSGTextMaskMaterial::texture() const
extern "C" Q_DECL_EXPORT
QSGTexture *ritual_ZNK19QSGTextMaskMaterial7textureEv(
    const QSGTextMaskMaterial *self) {
  return self->texture();
}

//  bool QSGTextMaskMaterial::ensureUpToDate()
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QSGTextMaskMaterial14ensureUpToDateEv(
    QSGTextMaskMaterial *self) {
  return self->ensureUpToDate();
}

//  QTextureGlyphCache *QSGTextMaskMaterial::glyphCache() const
extern "C" Q_DECL_EXPORT
QTextureGlyphCache *ritual_ZNK19QSGTextMaskMaterial10glyphCacheEv(
    const QSGTextMaskMaterial *self) {
  return self->glyphCache();
}

//  QSGRhiTextureGlyphCache *QSGTextMaskMaterial::rhiGlyphCache() const
extern "C" Q_DECL_EXPORT
QSGRhiTextureGlyphCache *ritual_ZNK19QSGTextMaskMaterial13rhiGlyphCacheEv(
    const QSGTextMaskMaterial *self) {
  return self->rhiGlyphCache();
}

//  void QSGTextMaskMaterial::populate(const QPointF &position, const
//      QList<quint32> &glyphIndexes, const QList<QPointF> &glyphPositions,
//      QSGGeometry *geometry, QRectF *boundingRect, QPointF *baseLine, const
//      QMargins &margins)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSGTextMaskMaterial8populateERK7QPointFRK5QListIjERKS3_IS0_EP11QSGGeometryP6QRectFPS0_RK8QMargins(
    QSGTextMaskMaterial *self,
    const QPointF *position,
    const QList<quint32> *glyphIndexes,
    const QList<QPointF> *glyphPositions,
    QSGGeometry *geometry,
    QRectF *boundingRect,
    QPointF *baseLine,
    const QMargins *margins) {
  self->populate(
      *position,
      *glyphIndexes,
      *glyphPositions,
      geometry,
      boundingRect,
      baseLine,
      *margins);
}

//  a Python function taken by a CuteQSGTextMaskMaterial, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSGTextMaskMaterial(
    QSGTextMaskMaterial *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSGTextMaskMaterial *>(self)->take(key, call);
}

//  QSGMaterialType *QSGTextMaskMaterial::type() const
extern "C" Q_DECL_EXPORT
QSGMaterialType *ritual_own_ZNK19QSGTextMaskMaterial4typeEv(
    const QSGTextMaskMaterial *self) {
  return self->QSGTextMaskMaterial::type();
}

//  int QSGTextMaskMaterial::compare(const QSGMaterial *other) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK19QSGTextMaskMaterial7compareEPK11QSGMaterial(
    const QSGTextMaskMaterial *self,
    const QSGMaterial *other) {
  return self->QSGTextMaskMaterial::compare(other);
}
