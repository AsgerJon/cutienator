//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgdefaultglyphnode_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgdefaultglyphnode_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qpoint.h>
#include <QtGui/qglyphrun.h>
#include <QtGui/qcolor.h>
#include <QtCore/qrect.h>
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
#include <QtQuick/private/qsgdefaultglyphnode_p.h>
#include <QtQuick/private/qsgdefaultglyphnode_p_p.h>
#include <QtGui/private/qrawfont_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

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

//  from ../qtdeclarative/src/quick/scenegraph/qsgdefaultglyphnode_p.cpp, line 313, as _ZN19QSGTextMaskMaterialC1EP16QSGRenderContextRK9QVector4DRK8QRawFontN11QFontEngine11GlyphFormatE
inline QSGTextMaskMaterial::QSGTextMaskMaterial(QSGRenderContext *rc, const QVector4D &color, const QRawFont &font, QFontEngine::GlyphFormat glyphFormat)
    : m_rc(qobject_cast<QSGDefaultRenderContext *>(rc))
    , m_texture(nullptr)
    , m_glyphCache(nullptr)
    , m_font(font)
    , m_color(color)
{
    init(glyphFormat);
}

//  from ../qtdeclarative/src/quick/scenegraph/qsgdefaultglyphnode_p.cpp, line 579, as _ZN21QSGStyledTextMaterialC1EP16QSGRenderContextRK8QRawFont
inline QSGStyledTextMaterial::QSGStyledTextMaterial(QSGRenderContext *rc, const QRawFont &font)
    : QSGTextMaskMaterial(rc, QVector4D(), font, QFontEngine::Format_A8)
{
}

//  from ../qtdeclarative/src/quick/scenegraph/qsgdefaultglyphnode_p.cpp, line 611, as _ZN23QSGOutlinedTextMaterialC1EP16QSGRenderContextRK8QRawFont
inline QSGOutlinedTextMaterial::QSGOutlinedTextMaterial(QSGRenderContext *rc, const QRawFont &font)
    : QSGStyledTextMaterial(rc, font)
{
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

//  from ../qtdeclarative/src/quick/scenegraph/qsgdefaultglyphnode_p.cpp, line 343, as _ZN19QSGTextMaskMaterial4initEN11QFontEngine11GlyphFormatE
inline void QSGTextMaskMaterial::init(QFontEngine::GlyphFormat glyphFormat)
{
    Q_ASSERT(m_font.isValid());

    setFlag(Blending, true);

    Q_ASSERT(m_rc);
    m_rhi = m_rc->rhi();

    updateCache(glyphFormat);
}

//  from ../qtdeclarative/src/quick/scenegraph/qsgdefaultglyphnode_p.cpp, line 513, as _ZNK19QSGTextMaskMaterial10glyphCacheEv
inline QTextureGlyphCache *QSGTextMaskMaterial::glyphCache() const
{
    return static_cast<QTextureGlyphCache *>(m_glyphCache.data());
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

//  from ../qtdeclarative/src/quick/scenegraph/qsgdefaultglyphnode.cpp, line 28, as _ZN19QSGDefaultGlyphNodeD1Ev
inline QSGDefaultGlyphNode::~QSGDefaultGlyphNode()
{
    cleanup();
}

//  from ../qtdeclarative/src/quick/scenegraph/qsgdefaultglyphnode.cpp, line 69, as _ZN19QSGDefaultGlyphNode9setGlyphsERK7QPointFRK9QGlyphRun
inline void QSGDefaultGlyphNode::setGlyphs(const QPointF &position, const QGlyphRun &glyphs)
{
    m_position = position;
    m_glyphs = glyphs;
    m_dirtyGeometry = true;

#ifdef QSG_RUNTIME_DESCRIPTION
    qsgnode_set_description(this, QLatin1String("glyphs"));
#endif
}

//  from ../qtdeclarative/src/quick/scenegraph/qsgdefaultglyphnode.cpp, line 60, as _ZN19QSGDefaultGlyphNode8setColorERK6QColor
inline void QSGDefaultGlyphNode::setColor(const QColor &color)
{
    m_color = color;
    if (material() != nullptr && !m_recycled) {
        static_cast<QSGTextMaskMaterial *>(material())->setColor(color);
        markDirty(DirtyMaterial);
    }
}

//  from ../qtdeclarative/src/quick/scenegraph/qsgdefaultglyphnode.cpp, line 80, as _ZN19QSGDefaultGlyphNode8setStyleEN10QQuickText9TextStyleE
inline void QSGDefaultGlyphNode::setStyle(QQuickText::TextStyle style)
{
    if (m_style == style)
        return;
    m_style = style;
}

//  from ../qtdeclarative/src/quick/scenegraph/qsgdefaultglyphnode.cpp, line 87, as _ZN19QSGDefaultGlyphNode13setStyleColorERK6QColor
inline void QSGDefaultGlyphNode::setStyleColor(const QColor &color)
{
    if (m_styleColor == color)
        return;
    m_styleColor = color;
}

//  from ../qtdeclarative/src/quick/scenegraph/qsgdefaultglyphnode.cpp, line 99, as _ZN19QSGDefaultGlyphNode6updateEv
inline void QSGDefaultGlyphNode::update()
{
    m_recycled = false;

    QRawFont font = m_glyphs.rawFont();
    QMargins margins(0, 0, 0, 0);

    const auto *fontEngine = QRawFontPrivate::get(font)->fontEngine;
    const bool isColorFont = fontEngine->glyphFormat == QFontEngine::Format_ARGB;

    QSGTextMaskMaterial *material = nullptr;
    if (m_style == QQuickText::Normal || isColorFont) {
        QFontEngine::GlyphFormat glyphFormat;

        // Don't try to override glyph format of color fonts
        if (isColorFont) {
            glyphFormat = QFontEngine::Format_None;
        } else {
            switch (m_preferredAntialiasingMode) {
            case GrayAntialiasing:
                glyphFormat = QFontEngine::Format_A8;
                break;
            case HighQualitySubPixelAntialiasing:
            case LowQualitySubPixelAntialiasing:
                glyphFormat = QFontEngine::Format_A32;
                break;
            default:
                glyphFormat = QFontEngine::Format_None;
                break;
            }
        }

        const auto rgbColor = m_color.toRgb();
        material = new QSGTextMaskMaterial(m_context, QVector4D(rgbColor.redF(), rgbColor.greenF(), rgbColor.blueF(), rgbColor.alphaF()), font, glyphFormat);
    } else if (m_style == QQuickText::Outline) {
        QSGOutlinedTextMaterial *m = new QSGOutlinedTextMaterial(m_context, font);
        m->setStyleColor(m_styleColor);
        margins = QMargins(1, 1, 1, 1);
        material = m;
    } else {
        QSGStyledTextMaterial *m = new QSGStyledTextMaterial(m_context, font);
        if (m_style == QQuickText::Sunken) {
            m->setStyleShift(QVector2D(0, -1));
            margins.setTop(1);
        } else if (m_style == QQuickText::Raised) {
            m->setStyleShift(QVector2D(0, 1));
            margins.setBottom(1);
        }
        m->setStyleColor(m_styleColor);
        material = m;
    }

    material->setColor(m_color);

    QRectF boundingRect;
    material->populate(m_position, m_glyphs.glyphIndexes(), m_glyphs.positions(), geometry(),
                       &boundingRect, &m_baseLine, margins);
    setBoundingRect(boundingRect);

    setMaterial(material);
    markDirty(DirtyGeometry);
}

//  from ../qtdeclarative/src/quick/scenegraph/qsgdefaultglyphnode.cpp, line 162, as _ZN19QSGDefaultGlyphNode10preprocessEv
inline void QSGDefaultGlyphNode::preprocess()
{
    qDeleteAll(m_nodesToDelete);
    m_nodesToDelete.clear();

    if (m_dirtyGeometry)
        updateGeometry();
}

//  from ../qtdeclarative/src/quick/scenegraph/qsgdefaultglyphnode.cpp, line 94, as _ZN19QSGDefaultGlyphNode28setPreferredAntialiasingModeEN12QSGGlyphNode16AntialiasingModeE
inline void QSGDefaultGlyphNode::setPreferredAntialiasingMode(AntialiasingMode mode)
{
    m_preferredAntialiasingMode = mode;
}

//  from ../qtdeclarative/src/quick/scenegraph/qsgdefaultglyphnode.cpp, line 42, as _ZN19QSGDefaultGlyphNode7recycleEv
inline void QSGDefaultGlyphNode::recycle()
{
    QSGGlyphNode::recycle();

    cleanup();

    m_glyphs = QGlyphRun{};
    m_position = QPointF{};
    m_color = QColor{};
    m_style = QQuickText::Normal;
    m_baseLine = QPointF{};
    m_geometry.allocate(0, 0);

    m_dirtyGeometry = true;
    m_preferredAntialiasingMode = DefaultAntialiasing;
    m_recycled = true;
}

//  from ../qtdeclarative/src/quick/scenegraph/qsgdefaultglyphnode.cpp, line 33, as _ZN19QSGDefaultGlyphNode7cleanupEv
inline void QSGDefaultGlyphNode::cleanup()
{
    if (m_glyphNodeType == SubGlyphNode)
        return;

    qDeleteAll(m_nodesToDelete);
    m_nodesToDelete.clear();
}
//  -----------------------------------------------------------------------

//  A QSGDefaultGlyphNode that Python can take functions over in. Every QSGDefaultGlyphNode
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQSGDefaultGlyphNodeCall0)(const void *, const QPointF *, const QGlyphRun *, int *);
typedef void (*CuteQSGDefaultGlyphNodeCall1)(const void *, const QColor *, int *);
typedef void (*CuteQSGDefaultGlyphNodeCall2)(const void *, int, int *);
typedef void (*CuteQSGDefaultGlyphNodeCall3)(const void *, const QColor *, int *);
typedef const QPointF * (*CuteQSGDefaultGlyphNodeCall4)(const void *, int *);
typedef void (*CuteQSGDefaultGlyphNodeCall5)(const void *, int *);
typedef void (*CuteQSGDefaultGlyphNodeCall6)(const void *, int *);
typedef void (*CuteQSGDefaultGlyphNodeCall7)(const void *, int, int *);
typedef void (*CuteQSGDefaultGlyphNodeCall8)(const void *, int *);
typedef const QRectF * (*CuteQSGDefaultGlyphNodeCall9)(const void *, int *);
typedef void (*CuteQSGDefaultGlyphNodeCall10)(const void *, const QRectF *, int *);
typedef void (*CuteQSGDefaultGlyphNodeCall11)(const void *, int, int *);
typedef void (*CuteQSGDefaultGlyphNodeCall12)(const void *, QSGNodeVisitorEx *, int *);
typedef bool (*CuteQSGDefaultGlyphNodeCall13)(const void *, int *);
class CuteQSGDefaultGlyphNode : public QSGDefaultGlyphNode {
public:
  using QSGDefaultGlyphNode::QSGDefaultGlyphNode;
  void *taken[14] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN12QSGGlyphNode9setGlyphsERK7QPointFRK9QGlyphRun")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QSGGlyphNode8setColorERK6QColor")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QSGGlyphNode8setStyleEN10QQuickText9TextStyleE")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QSGGlyphNode13setStyleColorERK6QColor")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QSGGlyphNode8baseLineEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QSGGlyphNode6updateEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QSGNode10preprocessEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QSGGlyphNode28setPreferredAntialiasingModeENS_16AntialiasingModeE")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QSGGlyphNode7recycleEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QSGGlyphNode12boundingRectEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QSGGlyphNode15setBoundingRectERK6QRectF")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QSGGlyphNode20setRenderTypeQualityEi")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QSGVisitableNode6acceptEP16QSGNodeVisitorEx")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QSGNode16isSubtreeBlockedEv")) {
      taken[13] = call;
      return true;
    }
    return false;
  }

  //  void QSGDefaultGlyphNode::setGlyphs(const QPointF &position, const
  //      QGlyphRun &glyphs)
  void setGlyphs(const QPointF &position, const QGlyphRun &glyphs) override {
    if (taken[0]) {
      int handled = 0;
      CuteQSGDefaultGlyphNodeCall0 call = reinterpret_cast<CuteQSGDefaultGlyphNodeCall0>(taken[0]);
      call(this, &position, &glyphs, &handled);
      if (handled) return;
    }
    QSGDefaultGlyphNode::setGlyphs(position, glyphs);
  }

  //  void QSGDefaultGlyphNode::setColor(const QColor &color)
  void setColor(const QColor &color) override {
    if (taken[1]) {
      int handled = 0;
      CuteQSGDefaultGlyphNodeCall1 call = reinterpret_cast<CuteQSGDefaultGlyphNodeCall1>(taken[1]);
      call(this, &color, &handled);
      if (handled) return;
    }
    QSGDefaultGlyphNode::setColor(color);
  }

  //  void QSGDefaultGlyphNode::setStyle(QQuickText::TextStyle a0)
  void setStyle(QQuickText::TextStyle a0) override {
    if (taken[2]) {
      int handled = 0;
      CuteQSGDefaultGlyphNodeCall2 call = reinterpret_cast<CuteQSGDefaultGlyphNodeCall2>(taken[2]);
      call(this, static_cast<int>(a0), &handled);
      if (handled) return;
    }
    QSGDefaultGlyphNode::setStyle(a0);
  }

  //  void QSGDefaultGlyphNode::setStyleColor(const QColor &a0)
  void setStyleColor(const QColor &a0) override {
    if (taken[3]) {
      int handled = 0;
      CuteQSGDefaultGlyphNodeCall3 call = reinterpret_cast<CuteQSGDefaultGlyphNodeCall3>(taken[3]);
      call(this, &a0, &handled);
      if (handled) return;
    }
    QSGDefaultGlyphNode::setStyleColor(a0);
  }

  //  QPointF QSGDefaultGlyphNode::baseLine() const
  QPointF baseLine() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQSGDefaultGlyphNodeCall4 call = reinterpret_cast<CuteQSGDefaultGlyphNodeCall4>(taken[4]);
      const QPointF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QSGDefaultGlyphNode::baseLine();
  }

  //  void QSGDefaultGlyphNode::update()
  void update() override {
    if (taken[5]) {
      int handled = 0;
      CuteQSGDefaultGlyphNodeCall5 call = reinterpret_cast<CuteQSGDefaultGlyphNodeCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    QSGDefaultGlyphNode::update();
  }

  //  void QSGDefaultGlyphNode::preprocess()
  void preprocess() override {
    if (taken[6]) {
      int handled = 0;
      CuteQSGDefaultGlyphNodeCall6 call = reinterpret_cast<CuteQSGDefaultGlyphNodeCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QSGDefaultGlyphNode::preprocess();
  }

  //  void
  //      QSGDefaultGlyphNode::setPreferredAntialiasingMode(AntialiasingMod
  //      e a0)
  void setPreferredAntialiasingMode(
      QSGGlyphNode::AntialiasingMode a0) override {
    if (taken[7]) {
      int handled = 0;
      CuteQSGDefaultGlyphNodeCall7 call = reinterpret_cast<CuteQSGDefaultGlyphNodeCall7>(taken[7]);
      call(this, static_cast<int>(a0), &handled);
      if (handled) return;
    }
    QSGDefaultGlyphNode::setPreferredAntialiasingMode(a0);
  }

  //  void QSGDefaultGlyphNode::recycle()
  void recycle() override {
    if (taken[8]) {
      int handled = 0;
      CuteQSGDefaultGlyphNodeCall8 call = reinterpret_cast<CuteQSGDefaultGlyphNodeCall8>(taken[8]);
      call(this, &handled);
      if (handled) return;
    }
    QSGDefaultGlyphNode::recycle();
  }

  //  QRectF QSGGlyphNode::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQSGDefaultGlyphNodeCall9 call = reinterpret_cast<CuteQSGDefaultGlyphNodeCall9>(taken[9]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QSGGlyphNode::boundingRect();
  }

  //  void QSGGlyphNode::setBoundingRect(const QRectF &bounds)
  void setBoundingRect(const QRectF &bounds) override {
    if (taken[10]) {
      int handled = 0;
      CuteQSGDefaultGlyphNodeCall10 call = reinterpret_cast<CuteQSGDefaultGlyphNodeCall10>(taken[10]);
      call(this, &bounds, &handled);
      if (handled) return;
    }
    QSGGlyphNode::setBoundingRect(bounds);
  }

  //  void QSGGlyphNode::setRenderTypeQuality(int renderTypeQuality)
  void setRenderTypeQuality(int renderTypeQuality) override {
    if (taken[11]) {
      int handled = 0;
      CuteQSGDefaultGlyphNodeCall11 call = reinterpret_cast<CuteQSGDefaultGlyphNodeCall11>(taken[11]);
      call(this, renderTypeQuality, &handled);
      if (handled) return;
    }
    QSGGlyphNode::setRenderTypeQuality(renderTypeQuality);
  }

  //  void QSGGlyphNode::accept(QSGNodeVisitorEx *visitor)
  void accept(QSGNodeVisitorEx *visitor) override {
    if (taken[12]) {
      int handled = 0;
      CuteQSGDefaultGlyphNodeCall12 call = reinterpret_cast<CuteQSGDefaultGlyphNodeCall12>(taken[12]);
      call(this, visitor, &handled);
      if (handled) return;
    }
    QSGGlyphNode::accept(visitor);
  }

  //  bool QSGNode::isSubtreeBlocked() const
  bool isSubtreeBlocked() const override {
    if (taken[13]) {
      int handled = 0;
      CuteQSGDefaultGlyphNodeCall13 call = reinterpret_cast<CuteQSGDefaultGlyphNodeCall13>(taken[13]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSGNode::isSubtreeBlocked();
  }
};

//  QSGDefaultGlyphNode::~QSGDefaultGlyphNode()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSGDefaultGlyphNodeD1Ev(QSGDefaultGlyphNode *self) {
  delete self;
}

//  void QSGDefaultGlyphNode::setGlyphs(const QPointF &position, const
//      QGlyphRun &glyphs)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSGDefaultGlyphNode9setGlyphsERK7QPointFRK9QGlyphRun(
    QSGDefaultGlyphNode *self,
    const QPointF *position,
    const QGlyphRun *glyphs) {
  self->setGlyphs(*position, *glyphs);
}

//  void QSGDefaultGlyphNode::setColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSGDefaultGlyphNode8setColorERK6QColor(
    QSGDefaultGlyphNode *self,
    const QColor *color) {
  self->setColor(*color);
}

//  void QSGDefaultGlyphNode::setStyle(QQuickText::TextStyle a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSGDefaultGlyphNode8setStyleEN10QQuickText9TextStyleE(
    QSGDefaultGlyphNode *self,
    QQuickText::TextStyle a0) {
  self->setStyle(a0);
}

//  void QSGDefaultGlyphNode::setStyleColor(const QColor &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSGDefaultGlyphNode13setStyleColorERK6QColor(
    QSGDefaultGlyphNode *self,
    const QColor *a0) {
  self->setStyleColor(*a0);
}

//  QPointF QSGDefaultGlyphNode::baseLine() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK19QSGDefaultGlyphNode8baseLineEv(
    const QSGDefaultGlyphNode *self) {
  return new QPointF(self->baseLine());
}

//  void QSGDefaultGlyphNode::update()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSGDefaultGlyphNode6updateEv(QSGDefaultGlyphNode *self) {
  self->update();
}

//  void QSGDefaultGlyphNode::preprocess()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSGDefaultGlyphNode10preprocessEv(
    QSGDefaultGlyphNode *self) {
  self->preprocess();
}

//  void QSGDefaultGlyphNode::setPreferredAntialiasingMode(AntialiasingMode
//      a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSGDefaultGlyphNode28setPreferredAntialiasingModeEN12QSGGlyphNode16AntialiasingModeE(
    QSGDefaultGlyphNode *self,
    QSGGlyphNode::AntialiasingMode a0) {
  self->setPreferredAntialiasingMode(a0);
}

//  void QSGDefaultGlyphNode::recycle()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSGDefaultGlyphNode7recycleEv(QSGDefaultGlyphNode *self) {
  self->recycle();
}

//  void QSGDefaultGlyphNode::cleanup()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSGDefaultGlyphNode7cleanupEv(QSGDefaultGlyphNode *self) {
  self->cleanup();
}

//  void QSGDefaultGlyphNode::setGlyphNodeType(DefaultGlyphNodeType type)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSGDefaultGlyphNode16setGlyphNodeTypeENS_20DefaultGlyphNodeTypeE(
    QSGDefaultGlyphNode *self,
    QSGDefaultGlyphNode::DefaultGlyphNodeType type) {
  self->setGlyphNodeType(type);
}

//  a Python function taken by a CuteQSGDefaultGlyphNode, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSGDefaultGlyphNode(
    QSGDefaultGlyphNode *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSGDefaultGlyphNode *>(self)->take(key, call);
}

//  void QSGDefaultGlyphNode::setGlyphs(const QPointF &position, const
//      QGlyphRun &glyphs)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QSGDefaultGlyphNode9setGlyphsERK7QPointFRK9QGlyphRun(
    QSGDefaultGlyphNode *self,
    const QPointF *position,
    const QGlyphRun *glyphs) {
  self->QSGDefaultGlyphNode::setGlyphs(*position, *glyphs);
}

//  void QSGDefaultGlyphNode::setStyle(QQuickText::TextStyle a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QSGDefaultGlyphNode8setStyleEN10QQuickText9TextStyleE(
    QSGDefaultGlyphNode *self,
    QQuickText::TextStyle a0) {
  self->QSGDefaultGlyphNode::setStyle(a0);
}

//  void QSGDefaultGlyphNode::setStyleColor(const QColor &a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QSGDefaultGlyphNode13setStyleColorERK6QColor(
    QSGDefaultGlyphNode *self,
    const QColor *a0) {
  self->QSGDefaultGlyphNode::setStyleColor(*a0);
}

//  QPointF QSGDefaultGlyphNode::baseLine() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_own_ZNK19QSGDefaultGlyphNode8baseLineEv(
    const QSGDefaultGlyphNode *self) {
  return new QPointF(self->QSGDefaultGlyphNode::baseLine());
}

//  void QSGDefaultGlyphNode::setPreferredAntialiasingMode(AntialiasingMode
//      a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QSGDefaultGlyphNode28setPreferredAntialiasingModeEN12QSGGlyphNode16AntialiasingModeE(
    QSGDefaultGlyphNode *self,
    QSGGlyphNode::AntialiasingMode a0) {
  self->QSGDefaultGlyphNode::setPreferredAntialiasingMode(a0);
}

//  void QSGDefaultGlyphNode::recycle()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QSGDefaultGlyphNode7recycleEv(
    QSGDefaultGlyphNode *self) {
  self->QSGDefaultGlyphNode::recycle();
}
