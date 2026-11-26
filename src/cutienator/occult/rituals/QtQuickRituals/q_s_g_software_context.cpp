//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgsoftwarecontext_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: added are 4 rituals that lean on what moc
//  writes for a class of the part Qt keeps to itself, whose ritual file
//  carries moc's output, drafted by a copy of the generator that lets those
//  names through. A copy of a meta-object is a second one: 'qobject_cast'
//  between it and Qt's own does not match. Kept as it is when the generator
//  runs again.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgsoftwarecontext_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qsurfaceformat.h>
#include <QtCore/qsize.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/private/qsgsoftwarecontext_p.h>
#include <QtQuick/private/qsgsoftwareinternalrectanglenode_p.h>
#include <QtQuick/private/qsgsoftwareinternalimagenode_p.h>
#include <QtQuick/private/qsgsoftwarepainternode_p.h>
#include <QtQuick/private/qsgsoftwarepixmaptexture_p.h>
#include <QtQuick/private/qsgsoftwareglyphnode_p.h>
#include <QtQuick/private/qsgsoftwarepublicnodes_p.h>
#include <QtQuick/private/qsgsoftwarelayer_p.h>
#include <QtQuick/private/qsgsoftwarerenderer_p.h>
#if QT_CONFIG(quick_sprite)
#include <QtQuick/private/qsgsoftwarespritenode_p.h>
#endif
#include <QtCore/QCoreApplication>
#include <QtCore/QElapsedTimer>
#include <QtGui/QWindow>
#include <QtQuick/private/qquickwindow_p.h>
#include <QtQuick/private/qquickitem_p.h>
#include <QtQuick/private/qsgsoftwareinternalrectanglenode_p.h>
#include <QtCore/qmath.h>
#include <QtGui/QPainter>
#include <QtQuick/private/qsgsoftwareinternalimagenode_p.h>
#include <QtQuick/private/qsgsoftwarepixmaptexture_p.h>
#include <QtQuick/private/qsgsoftwarelayer_p.h>
#include <QtGui/QPainter>
#include <QtCore/qmath.h>
#include <QtQuick/private/qsgsoftwarepainternode_p.h>
#include <QtQuick/private/qsgsoftwarepixmaptexture_p.h>
#include <QtCore/qmath.h>
#include <QtQuick/private/qsgsoftwareglyphnode_p.h>
#include <QtGui/private/qrawfont_p.h>
#include <QtQuick/private/qsgsoftwarelayer_p.h>
#include <QtQuick/private/qsgsoftwarecontext_p.h>
#include <QtQuick/private/qsgsoftwarepixmaprenderer_p.h>
#include <QtQuick/private/qsgsoftwarepublicnodes_p.h>
#include <QtQuick/private/qsgsoftwarelayer_p.h>
#include <QtQuick/private/qsgsoftwarepixmaptexture_p.h>
#include <QtQuick/private/qsgsoftwareinternalimagenode_p.h>
#include <QtQuick/private/qsgplaintexture_p.h>
#include <QtQuick/private/qsgsoftwarespritenode_p.h>
#include <QtQuick/private/qsgsoftwarepixmaptexture_p.h>
#include <QtGui/QPainter>
#include <QtQuick/private/qsgsoftwarepixmaptexture_p.h>
#include <QtQuick/private/qsgcontext_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwareglyphnode.cpp, line 20, as local:qsgsoftwareglyphnode.cpp:calculateBoundingRect
namespace {
inline QRectF calculateBoundingRect(const QPointF &position, const QGlyphRun &glyphs)
{
    QFixed minX;
    QFixed minY;
    QFixed maxX;
    QFixed maxY;

    QRawFontPrivate *rawFontD = QRawFontPrivate::get(glyphs.rawFont());
    QFontEngine *fontEngine = rawFontD->fontEngine;

    QFontEngine::GlyphFormat glyphFormat = fontEngine->glyphFormat != QFontEngine::Format_None ? fontEngine->glyphFormat : QFontEngine::Format_A32;

    int margin = fontEngine->glyphMargin(glyphFormat);

    const QList<uint> glyphIndexes = glyphs.glyphIndexes();
    const QList<QPointF> glyphPositions = glyphs.positions();
    for (int i = 0, n = qMin(glyphIndexes.size(), glyphPositions.size()); i < n; ++i) {
        glyph_metrics_t gm = fontEngine->alphaMapBoundingBox(glyphIndexes.at(i), QFixedPoint(), QTransform(), glyphFormat);

        gm.x += QFixed::fromReal(glyphPositions.at(i).x()) - margin;
        gm.y += QFixed::fromReal(glyphPositions.at(i).y()) - margin;

        if (i == 0) {
            minX = gm.x;
            minY = gm.y;
            maxX = gm.x + gm.width;
            maxY = gm.y + gm.height;
        } else {
            minX = qMin(gm.x, minX);
            minY = qMin(gm.y, minY);
            maxX = qMax(gm.x + gm.width, maxX);
            maxY = qMax(gm.y + gm.height, maxY);
        }
    }

    QRectF boundingRect(QPointF(minX.toReal(), minY.toReal()), QPointF(maxX.toReal(), maxY.toReal()));
    return boundingRect.translated(position - QPointF(0.0, glyphs.rawFont().ascent()));
}
}  // namespace

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwareinternalrectanglenode.cpp, line 70, as local:qsgsoftwareinternalrectanglenode.cpp:interpolateStop
static QGradientStop interpolateStop(const QGradientStop &firstStop, const QGradientStop &secondStop, double newPos)
{
    double distance = secondStop.first - firstStop.first;
    double distanceDelta = newPos - firstStop.first;
    double modifierValue = distanceDelta / distance;
    const auto firstStopRgbColor = firstStop.second.toRgb();
    const auto secondStopRgbColor = secondStop.second.toRgb();
    int redDelta = (secondStopRgbColor.red() - firstStopRgbColor.red()) * modifierValue;
    int greenDelta = (secondStopRgbColor.green() - firstStopRgbColor.green()) * modifierValue;
    int blueDelta = (secondStopRgbColor.blue() - firstStopRgbColor.blue()) * modifierValue;
    int alphaDelta = (secondStopRgbColor.alpha() - firstStopRgbColor.alpha()) * modifierValue;

    QGradientStop newStop;
    newStop.first = newPos;
    newStop.second = QColor(firstStopRgbColor.red() + redDelta,
                            firstStopRgbColor.green() + greenDelta,
                            firstStopRgbColor.blue() + blueDelta,
                            firstStopRgbColor.alpha() + alphaDelta);

    return newStop;
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarecontext.cpp, line 69, as _ZN18QSGSoftwareContext11createLayerEP16QSGRenderContext
inline QSGLayer *QSGSoftwareContext::createLayer(QSGRenderContext *renderContext)
{
    return new QSGSoftwareLayer(renderContext);
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarecontext.cpp, line 56, as _ZN18QSGSoftwareContext15createGlyphNodeEP16QSGRenderContextN11QSGTextNode10RenderTypeE
inline QSGGlyphNode *QSGSoftwareContext::createGlyphNode(QSGRenderContext *rc, QSGTextNode::RenderType renderType)
{
    Q_UNUSED(rc);
    Q_UNUSED(renderType);
    return new QSGSoftwareGlyphNode();
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarecontext.cpp, line 145, as _ZN18QSGSoftwareContext15createImageNodeEv
inline QSGImageNode *QSGSoftwareContext::createImageNode()
{
    return new QSGSoftwareImageNode;
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarecontext.cpp, line 156, as _ZN18QSGSoftwareContext16createSpriteNodeEv
#if QT_CONFIG(quick_sprite)
inline QSGSpriteNode *QSGSoftwareContext::createSpriteNode()
{
    return new QSGSoftwareSpriteNode;
}
#endif  // QT_CONFIG(quick_sprite)

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarecontext.cpp, line 51, as _ZN18QSGSoftwareContext17createPainterNodeEP17QQuickPaintedItem
inline QSGPainterNode *QSGSoftwareContext::createPainterNode(QQuickPaintedItem *item)
{
    return new QSGSoftwarePainterNode(item);
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarecontext.cpp, line 134, as _ZN18QSGSoftwareContext17rendererInterfaceEP16QSGRenderContext
inline QSGRendererInterface *QSGSoftwareContext::rendererInterface(QSGRenderContext *renderContext)
{
    Q_UNUSED(renderContext);
    return this;
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarecontext.cpp, line 150, as _ZN18QSGSoftwareContext19createNinePatchNodeEv
inline QSGNinePatchNode *QSGSoftwareContext::createNinePatchNode()
{
    return new QSGSoftwareNinePatchNode;
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarecontext.cpp, line 140, as _ZN18QSGSoftwareContext19createRectangleNodeEv
inline QSGRectangleNode *QSGSoftwareContext::createRectangleNode()
{
    return new QSGSoftwareRectangleNode;
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarecontext.cpp, line 63, as _ZN18QSGSoftwareContext21processTextRenderTypeEN11QSGTextNode10RenderTypeE
inline QSGTextNode::RenderType QSGSoftwareContext::processTextRenderType(QSGTextNode::RenderType renderType)
{
    Q_UNUSED(renderType);
    return QSGTextNode::NativeRendering;
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarecontext.cpp, line 45, as _ZN18QSGSoftwareContext23createInternalImageNodeEP16QSGRenderContext
inline QSGInternalImageNode *QSGSoftwareContext::createInternalImageNode(QSGRenderContext *renderContext)
{
    Q_UNUSED(renderContext);
    return new QSGSoftwareInternalImageNode();
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarecontext.cpp, line 40, as _ZN18QSGSoftwareContext27createInternalRectangleNodeEv
inline QSGInternalRectangleNode *QSGSoftwareContext::createInternalRectangleNode()
{
    return new QSGSoftwareInternalRectangleNode();
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarecontext.cpp, line 28, as _ZN24QSGSoftwareRenderContextC1EP10QSGContext
inline QSGSoftwareRenderContext::QSGSoftwareRenderContext(QSGContext *ctx)
    : QSGRenderContext(ctx)
    , m_initialized(false)
    , m_activePainter(nullptr)
{
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarecontext.cpp, line 167, as _ZNK18QSGSoftwareContext10shaderTypeEv
inline QSGRendererInterface::ShaderType QSGSoftwareContext::shaderType() const
{
    return UnknownShadingLanguage;
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarecontext.cpp, line 182, as _ZNK18QSGSoftwareContext11getResourceEP12QQuickWindowN20QSGRendererInterface8ResourceE
inline void *QSGSoftwareContext::getResource(QQuickWindow *window, Resource resource) const
{
    if (!window)
        return nullptr;

    auto cd = QQuickWindowPrivate::get(window);

    if (resource == PainterResource)
        return window->isSceneGraphInitialized() ? static_cast<QSGSoftwareRenderContext *>(cd->context)->m_activePainter : nullptr;
    else if (resource == RedirectPaintDevice)
        return cd->redirect.rt.sw.paintDevice;

    return nullptr;
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarecontext.cpp, line 162, as _ZNK18QSGSoftwareContext11graphicsApiEv
inline QSGRendererInterface::GraphicsApi QSGSoftwareContext::graphicsApi() const
{
    return Software;
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarecontext.cpp, line 177, as _ZNK18QSGSoftwareContext16shaderSourceTypeEv
inline QSGRendererInterface::ShaderSourceTypes QSGSoftwareContext::shaderSourceType() const
{
    return {};
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarecontext.cpp, line 74, as _ZNK18QSGSoftwareContext20defaultSurfaceFormatEv
inline QSurfaceFormat QSGSoftwareContext::defaultSurfaceFormat() const
{
    QSurfaceFormat format = QSurfaceFormat::defaultFormat();
    format.setRenderableType(QSurfaceFormat::DefaultRenderableType);
    format.setMajorVersion(0);
    format.setMinorVersion(0);
    if (QQuickWindow::hasDefaultAlphaBuffer())
        format.setAlphaBufferSize(8);
    return format;
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarecontext.cpp, line 172, as _ZNK18QSGSoftwareContext21shaderCompilationTypeEv
inline QSGRendererInterface::ShaderCompilationTypes QSGSoftwareContext::shaderCompilationType() const
{
    return {};
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwareinternalrectanglenode.cpp, line 12, as _ZN32QSGSoftwareInternalRectangleNodeC1Ev
inline QSGSoftwareInternalRectangleNode::QSGSoftwareInternalRectangleNode()
    : m_penWidth(0)
    , m_radius(0)
    , m_topLeftRadius(0)
    , m_topRightRadius(0)
    , m_bottomLeftRadius(0)
    , m_bottomRightRadius(0)
    , m_devicePixelRatio(1)
    , m_vertical(true)
    , m_cornerPixmapIsDirty(true)
    , m_isTopLeftRadiusSet(false)
    , m_isTopRightRadiusSet(false)
    , m_isBottomLeftRadiusSet(false)
    , m_isBottomRightRadiusSet(false)
{
    m_pen.setJoinStyle(Qt::MiterJoin);
    m_pen.setMiterLimit(0);
    setMaterial((QSGMaterial*)1);
    setGeometry((QSGGeometry*)1);
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwareinternalimagenode.cpp, line 276, as _ZN28QSGSoftwareInternalImageNodeC1Ev
inline QSGSoftwareInternalImageNode::QSGSoftwareInternalImageNode()
    : m_innerSourceRect(0, 0, 1, 1)
    , m_subSourceRect(0, 0, 1, 1)
    , m_texture(nullptr)
    , m_mirrorHorizontally(false)
    , m_mirrorVertically(false)
    , m_textureIsLayer(false)
    , m_smooth(true)
    , m_tileHorizontal(false)
    , m_tileVertical(false)
    , m_cachedMirroredPixmapIsDirty(false)
{
    setMaterial((QSGMaterial*)1);
    setGeometry((QSGGeometry*)1);
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarepainternode.cpp, line 11, as _ZN22QSGSoftwarePainterNodeC1EP17QQuickPaintedItem
inline QSGSoftwarePainterNode::QSGSoftwarePainterNode(QQuickPaintedItem *item)
    : QSGPainterNode()
    , m_preferredRenderTarget(QQuickPaintedItem::Image)
    , m_item(item)
    , m_texture(nullptr)
    , m_dirtyContents(false)
    , m_opaquePainting(false)
    , m_linear_filtering(false)
    , m_mipmapping(false)
    , m_smoothPainting(false)
    , m_fastFBOResizing(false)
    , m_fillColor(Qt::transparent)
    , m_contentsScale(1.0)
    , m_dirtyGeometry(false)
{
    setMaterial((QSGMaterial*)1);
    setGeometry((QSGGeometry*)1);
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwareglyphnode.cpp, line 10, as _ZN20QSGSoftwareGlyphNodeC1Ev
inline QSGSoftwareGlyphNode::QSGSoftwareGlyphNode()
    : QSGGlyphNode(QSGTextNode::NativeRendering)
    , m_geometry(QSGGeometry::defaultAttributes_TexturedPoint2D(), 0)
    , m_style(QQuickText::Normal)
{
    setMaterial((QSGMaterial*)1);
    setGeometry(&m_geometry);
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarelayer.cpp, line 12, as _ZN16QSGSoftwareLayerC1EP16QSGRenderContext
inline QSGSoftwareLayer::QSGSoftwareLayer(QSGRenderContext *renderContext)
    : QSGLayer(*(new QSGTexturePrivate(this)))
    , m_item(nullptr)
    , m_context(renderContext)
    , m_renderer(nullptr)
    , m_device_pixel_ratio(1)
    , m_mirrorHorizontal(false)
    , m_mirrorVertical(true)
    , m_live(true)
    , m_grab(true)
    , m_recursive(false)
    , m_dirtyTexture(true)
{

}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarepublicnodes.cpp, line 13, as _ZN24QSGSoftwareRectangleNodeC1Ev
inline QSGSoftwareRectangleNode::QSGSoftwareRectangleNode()
    : m_color(QColor(255, 255, 255))
{
    setMaterial((QSGMaterial*)1);
    setGeometry((QSGGeometry*)1);
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarepublicnodes.cpp, line 25, as _ZN20QSGSoftwareImageNodeC1Ev
inline QSGSoftwareImageNode::QSGSoftwareImageNode()
    : m_texture(nullptr),
      m_owns(false),
      m_filtering(QSGTexture::None),
      m_transformMode(NoTransform),
      m_cachedMirroredPixmapIsDirty(false)
{
    setMaterial((QSGMaterial*)1);
    setGeometry((QSGGeometry*)1);
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarepublicnodes.cpp, line 117, as _ZN24QSGSoftwareNinePatchNodeC1Ev
inline QSGSoftwareNinePatchNode::QSGSoftwareNinePatchNode()
{
    setMaterial((QSGMaterial*)1);
    setGeometry((QSGGeometry*)1);
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarespritenode.cpp, line 11, as _ZN21QSGSoftwareSpriteNodeC1Ev
inline QSGSoftwareSpriteNode::QSGSoftwareSpriteNode()
{
    setMaterial((QSGMaterial*)1);
    setGeometry((QSGGeometry*)1);
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwareinternalrectanglenode.cpp, line 33, as _ZN32QSGSoftwareInternalRectangleNode7setRectERK6QRectF
inline void QSGSoftwareInternalRectangleNode::setRect(const QRectF &rect)
{
    QRect alignedRect = rect.toAlignedRect();
    if (m_rect != alignedRect) {
        m_rect = alignedRect;
        markDirty(DirtyMaterial);
    }
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwareinternalrectanglenode.cpp, line 42, as _ZN32QSGSoftwareInternalRectangleNode8setColorERK6QColor
inline void QSGSoftwareInternalRectangleNode::setColor(const QColor &color)
{
    if (m_color != color) {
        m_color = color;
        m_cornerPixmapIsDirty = true;
        markDirty(DirtyMaterial);
    }
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwareinternalrectanglenode.cpp, line 51, as _ZN32QSGSoftwareInternalRectangleNode11setPenColorERK6QColor
inline void QSGSoftwareInternalRectangleNode::setPenColor(const QColor &color)
{
    if (m_penColor != color) {
        m_penColor = color;
        m_cornerPixmapIsDirty = true;
        markDirty(DirtyMaterial);
    }
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwareinternalrectanglenode.cpp, line 60, as _ZN32QSGSoftwareInternalRectangleNode11setPenWidthEd
inline void QSGSoftwareInternalRectangleNode::setPenWidth(qreal width)
{
    if (m_penWidth != width) {
        m_penWidth = width;
        m_cornerPixmapIsDirty = true;
        markDirty(DirtyMaterial);
    }
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwareinternalrectanglenode.cpp, line 165, as _ZN32QSGSoftwareInternalRectangleNode19setGradientVerticalEb
inline void QSGSoftwareInternalRectangleNode::setGradientVertical(bool vertical)
{
    if (m_vertical != vertical) {
        m_vertical = vertical;
        m_cornerPixmapIsDirty = true;
        markDirty(DirtyMaterial);
    }
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwareinternalrectanglenode.cpp, line 174, as _ZN32QSGSoftwareInternalRectangleNode9setRadiusEd
inline void QSGSoftwareInternalRectangleNode::setRadius(qreal radius)
{
    if (m_radius == radius)
        return;
    m_radius = radius;
    m_cornerPixmapIsDirty = true;
    markDirty(DirtyMaterial);
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwareinternalrectanglenode.cpp, line 183, as _ZN32QSGSoftwareInternalRectangleNode16setTopLeftRadiusEd
inline void QSGSoftwareInternalRectangleNode::setTopLeftRadius(qreal radius)
{
    if (m_isTopLeftRadiusSet && m_topLeftRadius == radius)
        return;
    m_isTopLeftRadiusSet = true;
    m_topLeftRadius = radius;
    m_cornerPixmapIsDirty = true;
    markDirty(DirtyMaterial);
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwareinternalrectanglenode.cpp, line 193, as _ZN32QSGSoftwareInternalRectangleNode17setTopRightRadiusEd
inline void QSGSoftwareInternalRectangleNode::setTopRightRadius(qreal radius)
{
    if (m_isTopRightRadiusSet && m_topRightRadius == radius)
        return;
    m_isTopRightRadiusSet = true;
    m_topRightRadius = radius;
    m_cornerPixmapIsDirty = true;
    markDirty(DirtyMaterial);
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwareinternalrectanglenode.cpp, line 203, as _ZN32QSGSoftwareInternalRectangleNode19setBottomLeftRadiusEd
inline void QSGSoftwareInternalRectangleNode::setBottomLeftRadius(qreal radius)
{
    if (m_isBottomLeftRadiusSet && m_bottomLeftRadius == radius)
        return;
    m_isBottomLeftRadiusSet = true;
    m_bottomLeftRadius = radius;
    m_cornerPixmapIsDirty = true;
    markDirty(DirtyMaterial);
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwareinternalrectanglenode.cpp, line 213, as _ZN32QSGSoftwareInternalRectangleNode20setBottomRightRadiusEd
inline void QSGSoftwareInternalRectangleNode::setBottomRightRadius(qreal radius)
{
    if (m_isBottomRightRadiusSet && m_bottomRightRadius == radius)
        return;
    m_isBottomRightRadiusSet = true;
    m_bottomRightRadius = radius;
    m_cornerPixmapIsDirty = true;
    markDirty(DirtyMaterial);
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwareinternalrectanglenode.cpp, line 223, as _ZN32QSGSoftwareInternalRectangleNode18resetTopLeftRadiusEv
inline void QSGSoftwareInternalRectangleNode::resetTopLeftRadius()
{
    if (!m_isTopLeftRadiusSet)
        return;
    m_isTopLeftRadiusSet = false;
    m_cornerPixmapIsDirty = true;
    markDirty(DirtyMaterial);
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwareinternalrectanglenode.cpp, line 232, as _ZN32QSGSoftwareInternalRectangleNode19resetTopRightRadiusEv
inline void QSGSoftwareInternalRectangleNode::resetTopRightRadius()
{
    if (!m_isTopRightRadiusSet)
        return;
    m_isTopRightRadiusSet = false;
    m_cornerPixmapIsDirty = true;
    markDirty(DirtyMaterial);
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwareinternalrectanglenode.cpp, line 241, as _ZN32QSGSoftwareInternalRectangleNode21resetBottomLeftRadiusEv
inline void QSGSoftwareInternalRectangleNode::resetBottomLeftRadius()
{
    if (!m_isBottomLeftRadiusSet)
        return;
    m_isBottomLeftRadiusSet = false;
    m_cornerPixmapIsDirty = true;
    markDirty(DirtyMaterial);
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwareinternalrectanglenode.cpp, line 250, as _ZN32QSGSoftwareInternalRectangleNode22resetBottomRightRadiusEv
inline void QSGSoftwareInternalRectangleNode::resetBottomRightRadius()
{
    if (!m_isBottomRightRadiusSet)
        return;
    m_isBottomRightRadiusSet = false;
    m_cornerPixmapIsDirty = true;
    markDirty(DirtyMaterial);
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwareinternalrectanglenode.cpp, line 259, as _ZN32QSGSoftwareInternalRectangleNode10setAlignedEb
inline void QSGSoftwareInternalRectangleNode::setAligned(bool /*aligned*/)
{
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwareinternalrectanglenode.cpp, line 263, as _ZN32QSGSoftwareInternalRectangleNode6updateEv
inline void QSGSoftwareInternalRectangleNode::update()
{
    if (!m_penWidth || m_penColor == Qt::transparent) {
        m_pen = Qt::NoPen;
    } else {
        m_pen = QPen(m_penColor);
        m_pen.setWidthF(m_penWidth);
    }

    if (!m_stops.isEmpty()) {
        QLinearGradient gradient(QPoint(0,0), QPoint(m_vertical ? 0 : m_rect.width(), m_vertical ? m_rect.height() : 0));
        gradient.setStops(m_stops);
        m_brush = QBrush(gradient);
    } else {
        m_brush = QBrush(m_color);
    }

    if (m_cornerPixmapIsDirty) {
        generateCornerPixmap();
        m_cornerPixmapIsDirty = false;
    }
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwareinternalimagenode.cpp, line 293, as _ZN28QSGSoftwareInternalImageNode13setTargetRectERK6QRectF
inline void QSGSoftwareInternalImageNode::setTargetRect(const QRectF &rect)
{
    if (rect == m_targetRect)
        return;
    m_targetRect = rect;
    markDirty(DirtyGeometry);
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwareinternalimagenode.cpp, line 301, as _ZN28QSGSoftwareInternalImageNode18setInnerTargetRectERK6QRectF
inline void QSGSoftwareInternalImageNode::setInnerTargetRect(const QRectF &rect)
{
    if (rect == m_innerTargetRect)
        return;
    m_innerTargetRect = rect;
    markDirty(DirtyGeometry);
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwareinternalimagenode.cpp, line 309, as _ZN28QSGSoftwareInternalImageNode18setInnerSourceRectERK6QRectF
inline void QSGSoftwareInternalImageNode::setInnerSourceRect(const QRectF &rect)
{
    if (rect == m_innerSourceRect)
        return;
    m_innerSourceRect = rect;
    markDirty(DirtyGeometry);
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwareinternalimagenode.cpp, line 317, as _ZN28QSGSoftwareInternalImageNode16setSubSourceRectERK6QRectF
inline void QSGSoftwareInternalImageNode::setSubSourceRect(const QRectF &rect)
{
    if (rect == m_subSourceRect)
        return;
    m_subSourceRect = rect;
    markDirty(DirtyGeometry);
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwareinternalimagenode.cpp, line 325, as _ZN28QSGSoftwareInternalImageNode10setTextureEP10QSGTexture
inline void QSGSoftwareInternalImageNode::setTexture(QSGTexture *texture)
{
    m_texture = texture;
    m_cachedMirroredPixmapIsDirty = true;
    m_textureIsLayer = static_cast<bool>(qobject_cast<QSGSoftwareLayer*>(texture));
    markDirty(DirtyMaterial);
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwareinternalimagenode.cpp, line 333, as _ZN28QSGSoftwareInternalImageNode9setMirrorEbb
inline void QSGSoftwareInternalImageNode::setMirror(bool mirrorHorizontally, bool mirrorVertically)
{
    if (mirrorHorizontally == m_mirrorHorizontally && mirrorVertically == m_mirrorVertically)
        return;
    m_mirrorHorizontally = mirrorHorizontally;
    m_mirrorVertically = mirrorVertically;
    m_cachedMirroredPixmapIsDirty = true;
    markDirty(DirtyMaterial);
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwareinternalimagenode.cpp, line 343, as _ZN28QSGSoftwareInternalImageNode18setMipmapFilteringEN10QSGTexture9FilteringE
inline void QSGSoftwareInternalImageNode::setMipmapFiltering(QSGTexture::Filtering /*filtering*/)
{
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwareinternalimagenode.cpp, line 347, as _ZN28QSGSoftwareInternalImageNode12setFilteringEN10QSGTexture9FilteringE
inline void QSGSoftwareInternalImageNode::setFiltering(QSGTexture::Filtering filtering)
{
    bool smooth = (filtering == QSGTexture::Linear);
    if (smooth == m_smooth)
        return;

    m_smooth = smooth;
    markDirty(DirtyMaterial);
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwareinternalimagenode.cpp, line 357, as _ZN28QSGSoftwareInternalImageNode21setHorizontalWrapModeEN10QSGTexture8WrapModeE
inline void QSGSoftwareInternalImageNode::setHorizontalWrapMode(QSGTexture::WrapMode wrapMode)
{
    bool tileHorizontal = (wrapMode == QSGTexture::Repeat);
    if (tileHorizontal == m_tileHorizontal)
        return;

    m_tileHorizontal = tileHorizontal;
    markDirty(DirtyMaterial);
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwareinternalimagenode.cpp, line 367, as _ZN28QSGSoftwareInternalImageNode19setVerticalWrapModeEN10QSGTexture8WrapModeE
inline void QSGSoftwareInternalImageNode::setVerticalWrapMode(QSGTexture::WrapMode wrapMode)
{
    bool tileVertical = (wrapMode == QSGTexture::Repeat);
    if (tileVertical == m_tileVertical)
        return;

    m_tileVertical = (wrapMode == QSGTexture::Repeat);
    markDirty(DirtyMaterial);
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwareinternalimagenode.cpp, line 377, as _ZN28QSGSoftwareInternalImageNode6updateEv
inline void QSGSoftwareInternalImageNode::update()
{
    updateCachedMirroredPixmap();
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwareinternalimagenode.cpp, line 382, as _ZN28QSGSoftwareInternalImageNode10preprocessEv
inline void QSGSoftwareInternalImageNode::preprocess()
{
    bool doDirty = false;
    QSGLayer *t = qobject_cast<QSGLayer *>(m_texture);
    if (t) {
        doDirty = t->updateTexture();
        markDirty(DirtyGeometry);
    }
    if (doDirty)
        markDirty(DirtyMaterial);
    m_cachedMirroredPixmapIsDirty = doDirty;
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarepainternode.cpp, line 30, as _ZN22QSGSoftwarePainterNodeD1Ev
inline QSGSoftwarePainterNode::~QSGSoftwarePainterNode()
{
    delete m_texture;
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarepainternode.cpp, line 35, as _ZN22QSGSoftwarePainterNode24setPreferredRenderTargetEN17QQuickPaintedItem12RenderTargetE
inline void QSGSoftwarePainterNode::setPreferredRenderTarget(QQuickPaintedItem::RenderTarget target)
{
    if (m_preferredRenderTarget == target)
        return;

    m_preferredRenderTarget = target;
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarepainternode.cpp, line 43, as _ZN22QSGSoftwarePainterNode7setSizeERK5QSize
inline void QSGSoftwarePainterNode::setSize(const QSize &size)
{
    if (size == m_size)
        return;

    m_size = size;

    m_dirtyGeometry = true;
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarepainternode.cpp, line 53, as _ZN22QSGSoftwarePainterNode8setDirtyERK5QRect
inline void QSGSoftwarePainterNode::setDirty(const QRect &dirtyRect)
{
    m_dirtyContents = true;
    m_dirtyRect = dirtyRect;
    markDirty(DirtyMaterial);
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarepainternode.cpp, line 60, as _ZN22QSGSoftwarePainterNode17setOpaquePaintingEb
inline void QSGSoftwarePainterNode::setOpaquePainting(bool opaque)
{
    if (opaque == m_opaquePainting)
        return;

    m_opaquePainting = opaque;
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarepainternode.cpp, line 68, as _ZN22QSGSoftwarePainterNode18setLinearFilteringEb
inline void QSGSoftwarePainterNode::setLinearFiltering(bool linearFiltering)
{
    if (linearFiltering == m_linear_filtering)
        return;

    m_linear_filtering = linearFiltering;
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarepainternode.cpp, line 76, as _ZN22QSGSoftwarePainterNode13setMipmappingEb
inline void QSGSoftwarePainterNode::setMipmapping(bool mipmapping)
{
    if (mipmapping == m_mipmapping)
        return;

    m_mipmapping = mipmapping;
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarepainternode.cpp, line 84, as _ZN22QSGSoftwarePainterNode17setSmoothPaintingEb
inline void QSGSoftwarePainterNode::setSmoothPainting(bool s)
{
    if (s == m_smoothPainting)
        return;

    m_smoothPainting = s;
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarepainternode.cpp, line 92, as _ZN22QSGSoftwarePainterNode12setFillColorERK6QColor
inline void QSGSoftwarePainterNode::setFillColor(const QColor &c)
{
    if (c == m_fillColor)
        return;

    m_fillColor = c;
    markDirty(DirtyMaterial);
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarepainternode.cpp, line 101, as _ZN22QSGSoftwarePainterNode16setContentsScaleEd
inline void QSGSoftwarePainterNode::setContentsScale(qreal s)
{
    if (s == m_contentsScale)
        return;

    m_contentsScale = s;
    markDirty(DirtyMaterial);
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarepainternode.cpp, line 110, as _ZN22QSGSoftwarePainterNode18setFastFBOResizingEb
inline void QSGSoftwarePainterNode::setFastFBOResizing(bool dynamic)
{
    m_fastFBOResizing = dynamic;
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarepainternode.cpp, line 115, as _ZNK22QSGSoftwarePainterNode7toImageEv
inline QImage QSGSoftwarePainterNode::toImage() const
{
    return m_pixmap.toImage();
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarepainternode.cpp, line 120, as _ZN22QSGSoftwarePainterNode6updateEv
inline void QSGSoftwarePainterNode::update()
{
    if (m_dirtyGeometry) {
        m_pixmap = QPixmap(m_textureSize);
        if (!m_opaquePainting)
            m_pixmap.fill(Qt::transparent);

        if (m_texture)
            delete m_texture;
        m_texture = new QSGSoftwarePixmapTexture(m_pixmap);
    }

    if (m_dirtyContents)
        paint();

    m_dirtyGeometry = false;
    m_dirtyContents = false;
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarepainternode.cpp, line 190, as _ZN22QSGSoftwarePainterNode14setTextureSizeERK5QSize
inline void QSGSoftwarePainterNode::setTextureSize(const QSize &size)
{
    if (size == m_textureSize)
        return;

    m_textureSize = size;
    m_dirtyGeometry = true;
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwareglyphnode.cpp, line 60, as _ZN20QSGSoftwareGlyphNode9setGlyphsERK7QPointFRK9QGlyphRun
inline void QSGSoftwareGlyphNode::setGlyphs(const QPointF &position, const QGlyphRun &glyphs)
{
    m_position = position;
    m_glyphRun = glyphs;
    // Decorations handled by text node
    m_glyphRun.setOverline(false);
    m_glyphRun.setStrikeOut(false);
    m_glyphRun.setUnderline(false);

    recalculateBoundingRect();
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwareglyphnode.cpp, line 82, as _ZN20QSGSoftwareGlyphNode8setColorERK6QColor
inline void QSGSoftwareGlyphNode::setColor(const QColor &color)
{
    m_color = color;
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwareglyphnode.cpp, line 87, as _ZN20QSGSoftwareGlyphNode8setStyleEN10QQuickText9TextStyleE
inline void QSGSoftwareGlyphNode::setStyle(QQuickText::TextStyle style)
{
    m_style = style;

    recalculateBoundingRect();
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwareglyphnode.cpp, line 94, as _ZN20QSGSoftwareGlyphNode13setStyleColorERK6QColor
inline void QSGSoftwareGlyphNode::setStyleColor(const QColor &color)
{
    m_styleColor = color;
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwareglyphnode.cpp, line 99, as _ZNK20QSGSoftwareGlyphNode8baseLineEv
inline QPointF QSGSoftwareGlyphNode::baseLine() const
{
    return QPointF();
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwareglyphnode.cpp, line 104, as _ZN20QSGSoftwareGlyphNode28setPreferredAntialiasingModeEN12QSGGlyphNode16AntialiasingModeE
inline void QSGSoftwareGlyphNode::setPreferredAntialiasingMode(QSGGlyphNode::AntialiasingMode)
{
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwareglyphnode.cpp, line 108, as _ZN20QSGSoftwareGlyphNode6updateEv
inline void QSGSoftwareGlyphNode::update()
{
    if (m_recycled) {
        markDirty(DirtyGeometry);
        m_recycled = false;
    }
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwareglyphnode.cpp, line 148, as _ZN20QSGSoftwareGlyphNode7recycleEv
inline void QSGSoftwareGlyphNode::recycle()
{
    QSGGlyphNode::recycle();
    m_position = QPointF{};
    m_glyphRun = QGlyphRun{};
    m_color = QColor{};
    m_geometry.allocate(0, 0);
    m_style = QQuickText::Normal;
    m_styleColor = QColor{};
    m_recycled = true;
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarepublicnodes.cpp, line 36, as _ZN20QSGSoftwareImageNodeD1Ev
inline QSGSoftwareImageNode::~QSGSoftwareImageNode()
{
    if (m_owns)
        delete m_texture;
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarepublicnodes.cpp, line 42, as _ZN20QSGSoftwareImageNode10setTextureEP10QSGTexture
inline void QSGSoftwareImageNode::setTexture(QSGTexture *texture)
{
    if (m_owns)
        delete m_texture;

    m_texture = texture; markDirty(DirtyMaterial);
    m_cachedMirroredPixmapIsDirty = true;
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarepublicnodes.cpp, line 51, as _ZN20QSGSoftwareImageNode30setTextureCoordinatesTransformE6QFlagsIN12QSGImageNode31TextureCoordinatesTransformFlagEE
inline void QSGSoftwareImageNode::setTextureCoordinatesTransform(QSGImageNode::TextureCoordinatesTransformMode transformNode)
{
    if (m_transformMode == transformNode)
        return;

    m_transformMode = transformNode;
    m_cachedMirroredPixmapIsDirty = true;

    markDirty(DirtyGeometry);
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarepublicnodes.cpp, line 123, as _ZN24QSGSoftwareNinePatchNode10setTextureEP10QSGTexture
inline void QSGSoftwareNinePatchNode::setTexture(QSGTexture *texture)
{
    QSGSoftwarePixmapTexture *pt = qobject_cast<QSGSoftwarePixmapTexture*>(texture);
    if (!pt) {
        qWarning() << "Image used with invalid texture format.";
    } else {
        m_pixmap = pt->pixmap();
        markDirty(DirtyMaterial);
    }
    delete texture;
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarepublicnodes.cpp, line 135, as _ZN24QSGSoftwareNinePatchNode9setBoundsERK6QRectF
inline void QSGSoftwareNinePatchNode::setBounds(const QRectF &bounds)
{
    if (m_bounds == bounds)
        return;

    m_bounds = bounds;
    markDirty(DirtyGeometry);
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarepublicnodes.cpp, line 144, as _ZN24QSGSoftwareNinePatchNode19setDevicePixelRatioEd
inline void QSGSoftwareNinePatchNode::setDevicePixelRatio(qreal ratio)
{
    if (m_pixelRatio == ratio)
        return;

    m_pixelRatio = ratio;
    markDirty(DirtyGeometry);
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarepublicnodes.cpp, line 153, as _ZN24QSGSoftwareNinePatchNode10setPaddingEdddd
inline void QSGSoftwareNinePatchNode::setPadding(qreal left, qreal top, qreal right, qreal bottom)
{
    QMargins margins(qRound(left), qRound(top), qRound(right), qRound(bottom));
    if (m_margins == margins)
        return;

    m_margins = QMargins(qRound(left), qRound(top), qRound(right), qRound(bottom));
    markDirty(DirtyGeometry);
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarepublicnodes.cpp, line 163, as _ZN24QSGSoftwareNinePatchNode6updateEv
inline void QSGSoftwareNinePatchNode::update()
{
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarespritenode.cpp, line 17, as _ZN21QSGSoftwareSpriteNodeD1Ev
inline QSGSoftwareSpriteNode::~QSGSoftwareSpriteNode()
{
    delete m_texture;
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarespritenode.cpp, line 22, as _ZN21QSGSoftwareSpriteNode10setTextureEP10QSGTexture
inline void QSGSoftwareSpriteNode::setTexture(QSGTexture *texture)
{
    m_texture = qobject_cast<QSGSoftwarePixmapTexture*>(texture);
    markDirty(DirtyMaterial);
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarespritenode.cpp, line 28, as _ZN21QSGSoftwareSpriteNode7setTimeEf
inline void QSGSoftwareSpriteNode::setTime(float time)
{
    if (m_time != time) {
        m_time = time;
        markDirty(DirtyMaterial);
    }
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarespritenode.cpp, line 36, as _ZN21QSGSoftwareSpriteNode10setSourceAERK6QPoint
inline void QSGSoftwareSpriteNode::setSourceA(const QPoint &source)
{
    if (m_sourceA != source) {
        m_sourceA = source;
        markDirty(DirtyMaterial);
    }
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarespritenode.cpp, line 44, as _ZN21QSGSoftwareSpriteNode10setSourceBERK6QPoint
inline void QSGSoftwareSpriteNode::setSourceB(const QPoint &source)
{
    if (m_sourceB != source) {
        m_sourceB = source;
        markDirty(DirtyMaterial);
    }
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarespritenode.cpp, line 52, as _ZN21QSGSoftwareSpriteNode13setSpriteSizeERK5QSize
inline void QSGSoftwareSpriteNode::setSpriteSize(const QSize &size)
{
    if (m_spriteSize != size) {
        m_spriteSize = size;
        markDirty(DirtyMaterial);
    }
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarespritenode.cpp, line 60, as _ZN21QSGSoftwareSpriteNode12setSheetSizeERK5QSize
inline void QSGSoftwareSpriteNode::setSheetSize(const QSize &size)
{
    if (m_sheetSize != size) {
        m_sheetSize = size;
        markDirty(DirtyMaterial);
    }
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarespritenode.cpp, line 68, as _ZN21QSGSoftwareSpriteNode7setSizeERK6QSizeF
inline void QSGSoftwareSpriteNode::setSize(const QSizeF &size)
{
    if (m_size != size) {
        m_size = size;
        markDirty(DirtyGeometry);
    }
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarespritenode.cpp, line 76, as _ZN21QSGSoftwareSpriteNode12setFilteringEN10QSGTexture9FilteringE
inline void QSGSoftwareSpriteNode::setFiltering(QSGTexture::Filtering filtering)
{
    Q_UNUSED(filtering);
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarespritenode.cpp, line 81, as _ZN21QSGSoftwareSpriteNode6updateEv
inline void QSGSoftwareSpriteNode::update()
{
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwareinternalimagenode.cpp, line 459, as _ZN28QSGSoftwareInternalImageNode26updateCachedMirroredPixmapEv
inline void QSGSoftwareInternalImageNode::updateCachedMirroredPixmap()
{
    if (m_cachedMirroredPixmapIsDirty) {
        if (m_mirrorHorizontally || m_mirrorVertically || m_textureIsLayer) {
            QTransform transform(
                (m_mirrorHorizontally ? -1 : 1), 0,
                0                              , (m_textureIsLayer ? -1 : 1) * (m_mirrorVertically ? -1 : 1),
                0                              , 0
                );
            m_cachedMirroredPixmap = pixmap().transformed(transform);
        } else {
            //Cleanup cached pixmap if necessary
            if (!m_cachedMirroredPixmap.isNull())
                m_cachedMirroredPixmap = QPixmap();
        }
        m_cachedMirroredPixmapIsDirty = false;
    }
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarepainternode.cpp, line 147, as _ZN22QSGSoftwarePainterNode5paintEv
inline void QSGSoftwarePainterNode::paint()
{
    QRect dirtyRect = m_dirtyRect.isNull() ? QRect(0, 0, m_size.width(), m_size.height()) : m_dirtyRect;

    QPainter painter;

    painter.begin(&m_pixmap);
    if (m_smoothPainting) {
        painter.setRenderHints(QPainter::Antialiasing | QPainter::TextAntialiasing | QPainter::SmoothPixmapTransform);
    }

    QRect clipRect;

    if (m_contentsScale == 1) {
        qreal scaleX = m_textureSize.width() / (qreal) m_size.width();
        qreal scaleY = m_textureSize.height() / (qreal) m_size.height();
        painter.scale(scaleX, scaleY);
        clipRect = dirtyRect;
    } else {
        painter.scale(m_contentsScale, m_contentsScale);

        QRect sclip(qFloor(dirtyRect.x()/m_contentsScale),
                    qFloor(dirtyRect.y()/m_contentsScale),
                    qCeil(dirtyRect.width()/m_contentsScale+dirtyRect.x()/m_contentsScale-qFloor(dirtyRect.x()/m_contentsScale)),
                    qCeil(dirtyRect.height()/m_contentsScale+dirtyRect.y()/m_contentsScale-qFloor(dirtyRect.y()/m_contentsScale)));

        clipRect = sclip;
    }

    if (!m_dirtyRect.isNull())
        painter.setClipRect(clipRect);

    painter.setCompositionMode(QPainter::CompositionMode_Source);
    painter.fillRect(clipRect, m_fillColor);
    painter.setCompositionMode(QPainter::CompositionMode_SourceOver);

    m_item->paint(&painter);
    painter.end();

    m_dirtyRect = QRect();
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarepixmaptexture.cpp, line 23, as _ZN24QSGSoftwarePixmapTextureC1ERK7QPixmap
inline QSGSoftwarePixmapTexture::QSGSoftwarePixmapTexture(const QPixmap &pixmap)
    : m_pixmap(pixmap)
{
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwareglyphnode.cpp, line 72, as _ZN20QSGSoftwareGlyphNode23recalculateBoundingRectEv
inline void QSGSoftwareGlyphNode::recalculateBoundingRect()
{
    int x1Offset = m_style == QQuickText::Outline ? -1 : 0;
    int x2Offset = m_style == QQuickText::Outline ? 1 : 0;
    int y1Offset = m_style == QQuickText::Outline || m_style == QQuickText::Sunken ? -1 : 0;
    int y2Offset = m_style == QQuickText::Outline || m_style == QQuickText::Raised ? 1 : 0;

    m_bounding_rect = calculateBoundingRect(m_position, m_glyphRun).adjusted(x1Offset, y1Offset, x2Offset, y2Offset);
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwareinternalimagenode.cpp, line 448, as _ZNK28QSGSoftwareInternalImageNode6pixmapEv
inline const QPixmap &QSGSoftwareInternalImageNode::pixmap() const
{
    if (QSGSoftwarePixmapTexture *pt = qobject_cast<QSGSoftwarePixmapTexture*>(m_texture))
        return pt->pixmap();
    if (QSGSoftwareLayer *layer = qobject_cast<QSGSoftwareLayer*>(m_texture))
        return layer->pixmap();
    Q_ASSERT(m_texture == nullptr);
    static const QPixmap nullPixmap;
    return nullPixmap;
}
//  -----------------------------------------------------------------------

//  A QSGSoftwareContext that Python can take functions over in. Every QSGSoftwareContext
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQSGSoftwareContextCall0)(const void *, int *);
typedef void * (*CuteQSGSoftwareContextCall1)(const void *, int *);
typedef void * (*CuteQSGSoftwareContextCall2)(const void *, QSGRenderContext *, int *);
typedef void * (*CuteQSGSoftwareContextCall3)(const void *, QQuickPaintedItem *, int *);
typedef void * (*CuteQSGSoftwareContextCall4)(const void *, QSGRenderContext *, int, int *);
typedef void * (*CuteQSGSoftwareContextCall5)(const void *, QSGRenderContext *, int *);
typedef const QSurfaceFormat * (*CuteQSGSoftwareContextCall6)(const void *, int *);
typedef void * (*CuteQSGSoftwareContextCall7)(const void *, QSGRenderContext *, int *);
typedef void * (*CuteQSGSoftwareContextCall8)(const void *, int *);
typedef void * (*CuteQSGSoftwareContextCall9)(const void *, int *);
typedef void * (*CuteQSGSoftwareContextCall10)(const void *, int *);
#if QT_CONFIG(quick_sprite)
typedef void * (*CuteQSGSoftwareContextCall11)(const void *, int *);
#endif  // QT_CONFIG(quick_sprite)
typedef int (*CuteQSGSoftwareContextCall12)(const void *, int, int *);
typedef int (*CuteQSGSoftwareContextCall13)(const void *, int *);
typedef int (*CuteQSGSoftwareContextCall14)(const void *, int *);
typedef int (*CuteQSGSoftwareContextCall15)(const void *, int *);
typedef int (*CuteQSGSoftwareContextCall16)(const void *, int *);
typedef void * (*CuteQSGSoftwareContextCall17)(const void *, QQuickWindow *, int, int *);
typedef void (*CuteQSGSoftwareContextCall18)(const void *, QSGRenderContext *, int *);
typedef void (*CuteQSGSoftwareContextCall19)(const void *, QSGRenderContext *, int *);
typedef void * (*CuteQSGSoftwareContextCall20)(const void *, QSGRenderContext *, int *);
typedef void * (*CuteQSGSoftwareContextCall21)(const void *, int *);
typedef void * (*CuteQSGSoftwareContextCall22)(const void *, QSGRenderContext *, int *);
typedef void * (*CuteQSGSoftwareContextCall23)(const void *, QObject *, int *);
typedef float (*CuteQSGSoftwareContextCall24)(const void *, QAnimationDriver *, int *);
typedef bool (*CuteQSGSoftwareContextCall25)(const void *, QAnimationDriver *, int *);
typedef const QSize * (*CuteQSGSoftwareContextCall26)(const void *, int *);
typedef void * (*CuteQSGSoftwareContextCall27)(const void *, QSGRenderContext *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSGSoftwareContextCall28)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSGSoftwareContextCall29)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGSoftwareContextCall30)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGSoftwareContextCall31)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGSoftwareContextCall32)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGSoftwareContextCall33)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGSoftwareContextCall34)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQSGSoftwareContext : public QSGSoftwareContext {
public:
  using QSGSoftwareContext::QSGSoftwareContext;
  void *taken[35] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN10QSGContext19createRenderContextEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSGContext27createInternalRectangleNodeEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSGContext23createInternalImageNodeEP16QSGRenderContext")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSGContext17createPainterNodeEP17QQuickPaintedItem")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSGContext15createGlyphNodeEP16QSGRenderContextN11QSGTextNode10RenderTypeE")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSGContext11createLayerEP16QSGRenderContext")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QSGContext20defaultSurfaceFormatEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSGContext17rendererInterfaceEP16QSGRenderContext")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSGContext19createRectangleNodeEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSGContext15createImageNodeEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSGContext19createNinePatchNodeEv")) {
      taken[10] = call;
      return true;
    }
#if QT_CONFIG(quick_sprite)
    if (!std::strcmp(key, "_ZN10QSGContext16createSpriteNodeEv")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_sprite)
    if (!std::strcmp(key, "_ZN10QSGContext21processTextRenderTypeEN11QSGTextNode10RenderTypeE")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QSGRendererInterface11graphicsApiEv")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QSGRendererInterface10shaderTypeEv")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QSGRendererInterface21shaderCompilationTypeEv")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QSGRendererInterface16shaderSourceTypeEv")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QSGRendererInterface11getResourceEP12QQuickWindowNS_8ResourceE")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSGContext24renderContextInitializedEP16QSGRenderContext")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSGContext24renderContextInvalidatedEP16QSGRenderContext")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSGContext22createInternalTextNodeEP16QSGRenderContext")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSGContext34createGuiThreadShaderEffectManagerEv")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSGContext22createShaderEffectNodeEP16QSGRenderContext")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSGContext21createAnimationDriverEP7QObject")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSGContext31vsyncIntervalForAnimationDriverEP16QAnimationDriver")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSGContext16isVSyncDependentEP16QAnimationDriver")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QSGContext14minimumFBOSizeEv")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSGContext14createTextNodeEP16QSGRenderContext")) {
      taken[27] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[28] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[29] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[30] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[31] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[32] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[33] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[34] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  QSGRenderContext *QSGSoftwareContext::createRenderContext()
  QSGRenderContext *createRenderContext() override {
    if (taken[0]) {
      int handled = 0;
      CuteQSGSoftwareContextCall0 call = reinterpret_cast<CuteQSGSoftwareContextCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGRenderContext *>(given);
    }
    return QSGSoftwareContext::createRenderContext();
  }

  //  QSGInternalRectangleNode
  //      *QSGSoftwareContext::createInternalRectangleNode()
  QSGInternalRectangleNode *createInternalRectangleNode() override {
    if (taken[1]) {
      int handled = 0;
      CuteQSGSoftwareContextCall1 call = reinterpret_cast<CuteQSGSoftwareContextCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGInternalRectangleNode *>(given);
    }
    return QSGSoftwareContext::createInternalRectangleNode();
  }

  //  QSGInternalImageNode
  //      *QSGSoftwareContext::createInternalImageNode(QSGRenderContext
  //      *renderContext)
  QSGInternalImageNode *createInternalImageNode(
      QSGRenderContext *renderContext) override {
    if (taken[2]) {
      int handled = 0;
      CuteQSGSoftwareContextCall2 call = reinterpret_cast<CuteQSGSoftwareContextCall2>(taken[2]);
      void * given = call(this, renderContext, &handled);
      if (handled) return static_cast<QSGInternalImageNode *>(given);
    }
    return QSGSoftwareContext::createInternalImageNode(renderContext);
  }

  //  QSGPainterNode
  //      *QSGSoftwareContext::createPainterNode(QQuickPaintedItem *item)
  QSGPainterNode *createPainterNode(QQuickPaintedItem *item) override {
    if (taken[3]) {
      int handled = 0;
      CuteQSGSoftwareContextCall3 call = reinterpret_cast<CuteQSGSoftwareContextCall3>(taken[3]);
      void * given = call(this, item, &handled);
      if (handled) return static_cast<QSGPainterNode *>(given);
    }
    return QSGSoftwareContext::createPainterNode(item);
  }

  //  QSGGlyphNode *QSGSoftwareContext::createGlyphNode(QSGRenderContext
  //      *rc, QSGTextNode::RenderType renderType)
  QSGGlyphNode *createGlyphNode(
      QSGRenderContext *rc,
      QSGTextNode::RenderType renderType) override {
    if (taken[4]) {
      int handled = 0;
      CuteQSGSoftwareContextCall4 call = reinterpret_cast<CuteQSGSoftwareContextCall4>(taken[4]);
      void * given = call(this, rc, static_cast<int>(renderType), &handled);
      if (handled) return static_cast<QSGGlyphNode *>(given);
    }
    return QSGSoftwareContext::createGlyphNode(rc, renderType);
  }

  //  QSGLayer *QSGSoftwareContext::createLayer(QSGRenderContext
  //      *renderContext)
  QSGLayer *createLayer(QSGRenderContext *renderContext) override {
    if (taken[5]) {
      int handled = 0;
      CuteQSGSoftwareContextCall5 call = reinterpret_cast<CuteQSGSoftwareContextCall5>(taken[5]);
      void * given = call(this, renderContext, &handled);
      if (handled) return static_cast<QSGLayer *>(given);
    }
    return QSGSoftwareContext::createLayer(renderContext);
  }

  //  QSurfaceFormat QSGSoftwareContext::defaultSurfaceFormat() const
  QSurfaceFormat defaultSurfaceFormat() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQSGSoftwareContextCall6 call = reinterpret_cast<CuteQSGSoftwareContextCall6>(taken[6]);
      const QSurfaceFormat * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QSGSoftwareContext::defaultSurfaceFormat();
  }

  //  QSGRendererInterface
  //      *QSGSoftwareContext::rendererInterface(QSGRenderContext
  //      *renderContext)
  QSGRendererInterface *rendererInterface(
      QSGRenderContext *renderContext) override {
    if (taken[7]) {
      int handled = 0;
      CuteQSGSoftwareContextCall7 call = reinterpret_cast<CuteQSGSoftwareContextCall7>(taken[7]);
      void * given = call(this, renderContext, &handled);
      if (handled) return static_cast<QSGRendererInterface *>(given);
    }
    return QSGSoftwareContext::rendererInterface(renderContext);
  }

  //  QSGRectangleNode *QSGSoftwareContext::createRectangleNode()
  QSGRectangleNode *createRectangleNode() override {
    if (taken[8]) {
      int handled = 0;
      CuteQSGSoftwareContextCall8 call = reinterpret_cast<CuteQSGSoftwareContextCall8>(taken[8]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGRectangleNode *>(given);
    }
    return QSGSoftwareContext::createRectangleNode();
  }

  //  QSGImageNode *QSGSoftwareContext::createImageNode()
  QSGImageNode *createImageNode() override {
    if (taken[9]) {
      int handled = 0;
      CuteQSGSoftwareContextCall9 call = reinterpret_cast<CuteQSGSoftwareContextCall9>(taken[9]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGImageNode *>(given);
    }
    return QSGSoftwareContext::createImageNode();
  }

  //  QSGNinePatchNode *QSGSoftwareContext::createNinePatchNode()
  QSGNinePatchNode *createNinePatchNode() override {
    if (taken[10]) {
      int handled = 0;
      CuteQSGSoftwareContextCall10 call = reinterpret_cast<CuteQSGSoftwareContextCall10>(taken[10]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGNinePatchNode *>(given);
    }
    return QSGSoftwareContext::createNinePatchNode();
  }

#if QT_CONFIG(quick_sprite)
  //  QSGSpriteNode *QSGSoftwareContext::createSpriteNode()
  QSGSpriteNode *createSpriteNode() override {
    if (taken[11]) {
      int handled = 0;
      CuteQSGSoftwareContextCall11 call = reinterpret_cast<CuteQSGSoftwareContextCall11>(taken[11]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGSpriteNode *>(given);
    }
    return QSGSoftwareContext::createSpriteNode();
  }
#endif  // QT_CONFIG(quick_sprite)

  //  QSGTextNode::RenderType
  //      QSGSoftwareContext::processTextRenderType(QSGTextNode::RenderType
  //      renderType)
  QSGTextNode::RenderType processTextRenderType(
      QSGTextNode::RenderType renderType) override {
    if (taken[12]) {
      int handled = 0;
      CuteQSGSoftwareContextCall12 call = reinterpret_cast<CuteQSGSoftwareContextCall12>(taken[12]);
      int given = call(this, static_cast<int>(renderType), &handled);
      if (handled) return static_cast<QSGTextNode::RenderType>(given);
    }
    return QSGSoftwareContext::processTextRenderType(renderType);
  }

  //  GraphicsApi QSGSoftwareContext::graphicsApi() const
  QSGRendererInterface::GraphicsApi graphicsApi() const override {
    if (taken[13]) {
      int handled = 0;
      CuteQSGSoftwareContextCall13 call = reinterpret_cast<CuteQSGSoftwareContextCall13>(taken[13]);
      int given = call(this, &handled);
      if (handled) return static_cast<QSGRendererInterface::GraphicsApi>(given);
    }
    return QSGSoftwareContext::graphicsApi();
  }

  //  ShaderType QSGSoftwareContext::shaderType() const
  QSGRendererInterface::ShaderType shaderType() const override {
    if (taken[14]) {
      int handled = 0;
      CuteQSGSoftwareContextCall14 call = reinterpret_cast<CuteQSGSoftwareContextCall14>(taken[14]);
      int given = call(this, &handled);
      if (handled) return static_cast<QSGRendererInterface::ShaderType>(given);
    }
    return QSGSoftwareContext::shaderType();
  }

  //  ShaderCompilationTypes QSGSoftwareContext::shaderCompilationType()
  //      const
  QSGRendererInterface::ShaderCompilationTypes shaderCompilationType() const override {
    if (taken[15]) {
      int handled = 0;
      CuteQSGSoftwareContextCall15 call = reinterpret_cast<CuteQSGSoftwareContextCall15>(taken[15]);
      int given = call(this, &handled);
      if (handled) return QFlags<QSGRendererInterface::ShaderCompilationType>::fromInt(given);
    }
    return QSGSoftwareContext::shaderCompilationType();
  }

  //  ShaderSourceTypes QSGSoftwareContext::shaderSourceType() const
  QSGRendererInterface::ShaderSourceTypes shaderSourceType() const override {
    if (taken[16]) {
      int handled = 0;
      CuteQSGSoftwareContextCall16 call = reinterpret_cast<CuteQSGSoftwareContextCall16>(taken[16]);
      int given = call(this, &handled);
      if (handled) return QFlags<QSGRendererInterface::ShaderSourceType>::fromInt(given);
    }
    return QSGSoftwareContext::shaderSourceType();
  }

  //  void *QSGSoftwareContext::getResource(QQuickWindow *window, Resource
  //      resource) const
  void *getResource(
      QQuickWindow *window,
      QSGRendererInterface::Resource resource) const override {
    if (taken[17]) {
      int handled = 0;
      CuteQSGSoftwareContextCall17 call = reinterpret_cast<CuteQSGSoftwareContextCall17>(taken[17]);
      void * given = call(this, window, static_cast<int>(resource), &handled);
      if (handled) return static_cast<void *>(given);
    }
    return QSGSoftwareContext::getResource(window, resource);
  }

  //  void QSGContext::renderContextInitialized(QSGRenderContext
  //      *renderContext)
  void renderContextInitialized(QSGRenderContext *renderContext) override {
    if (taken[18]) {
      int handled = 0;
      CuteQSGSoftwareContextCall18 call = reinterpret_cast<CuteQSGSoftwareContextCall18>(taken[18]);
      call(this, renderContext, &handled);
      if (handled) return;
    }
    QSGContext::renderContextInitialized(renderContext);
  }

  //  void QSGContext::renderContextInvalidated(QSGRenderContext
  //      *renderContext)
  void renderContextInvalidated(QSGRenderContext *renderContext) override {
    if (taken[19]) {
      int handled = 0;
      CuteQSGSoftwareContextCall19 call = reinterpret_cast<CuteQSGSoftwareContextCall19>(taken[19]);
      call(this, renderContext, &handled);
      if (handled) return;
    }
    QSGContext::renderContextInvalidated(renderContext);
  }

  //  QSGInternalTextNode
  //      *QSGContext::createInternalTextNode(QSGRenderContext
  //      *renderContext)
  QSGInternalTextNode *createInternalTextNode(
      QSGRenderContext *renderContext) override {
    if (taken[20]) {
      int handled = 0;
      CuteQSGSoftwareContextCall20 call = reinterpret_cast<CuteQSGSoftwareContextCall20>(taken[20]);
      void * given = call(this, renderContext, &handled);
      if (handled) return static_cast<QSGInternalTextNode *>(given);
    }
    return QSGContext::createInternalTextNode(renderContext);
  }

  //  QSGGuiThreadShaderEffectManager
  //      *QSGContext::createGuiThreadShaderEffectManager()
  QSGGuiThreadShaderEffectManager *createGuiThreadShaderEffectManager() override {
    if (taken[21]) {
      int handled = 0;
      CuteQSGSoftwareContextCall21 call = reinterpret_cast<CuteQSGSoftwareContextCall21>(taken[21]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGGuiThreadShaderEffectManager *>(given);
    }
    return QSGContext::createGuiThreadShaderEffectManager();
  }

  //  QSGShaderEffectNode
  //      *QSGContext::createShaderEffectNode(QSGRenderContext
  //      *renderContext)
  QSGShaderEffectNode *createShaderEffectNode(
      QSGRenderContext *renderContext) override {
    if (taken[22]) {
      int handled = 0;
      CuteQSGSoftwareContextCall22 call = reinterpret_cast<CuteQSGSoftwareContextCall22>(taken[22]);
      void * given = call(this, renderContext, &handled);
      if (handled) return static_cast<QSGShaderEffectNode *>(given);
    }
    return QSGContext::createShaderEffectNode(renderContext);
  }

  //  QAnimationDriver *QSGContext::createAnimationDriver(QObject *parent)
  QAnimationDriver *createAnimationDriver(QObject *parent) override {
    if (taken[23]) {
      int handled = 0;
      CuteQSGSoftwareContextCall23 call = reinterpret_cast<CuteQSGSoftwareContextCall23>(taken[23]);
      void * given = call(this, parent, &handled);
      if (handled) return static_cast<QAnimationDriver *>(given);
    }
    return QSGContext::createAnimationDriver(parent);
  }

  //  float QSGContext::vsyncIntervalForAnimationDriver(QAnimationDriver
  //      *driver)
  float vsyncIntervalForAnimationDriver(QAnimationDriver *driver) override {
    if (taken[24]) {
      int handled = 0;
      CuteQSGSoftwareContextCall24 call = reinterpret_cast<CuteQSGSoftwareContextCall24>(taken[24]);
      float given = call(this, driver, &handled);
      if (handled) return given;
    }
    return QSGContext::vsyncIntervalForAnimationDriver(driver);
  }

  //  bool QSGContext::isVSyncDependent(QAnimationDriver *driver)
  bool isVSyncDependent(QAnimationDriver *driver) override {
    if (taken[25]) {
      int handled = 0;
      CuteQSGSoftwareContextCall25 call = reinterpret_cast<CuteQSGSoftwareContextCall25>(taken[25]);
      bool given = call(this, driver, &handled);
      if (handled) return given;
    }
    return QSGContext::isVSyncDependent(driver);
  }

  //  QSize QSGContext::minimumFBOSize() const
  QSize minimumFBOSize() const override {
    if (taken[26]) {
      int handled = 0;
      CuteQSGSoftwareContextCall26 call = reinterpret_cast<CuteQSGSoftwareContextCall26>(taken[26]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QSGContext::minimumFBOSize();
  }

  //  QSGTextNode *QSGContext::createTextNode(QSGRenderContext
  //      *renderContext)
  QSGTextNode *createTextNode(QSGRenderContext *renderContext) override {
    if (taken[27]) {
      int handled = 0;
      CuteQSGSoftwareContextCall27 call = reinterpret_cast<CuteQSGSoftwareContextCall27>(taken[27]);
      void * given = call(this, renderContext, &handled);
      if (handled) return static_cast<QSGTextNode *>(given);
    }
    return QSGContext::createTextNode(renderContext);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQSGSoftwareContextCall28 call = reinterpret_cast<CuteQSGSoftwareContextCall28>(taken[28]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQSGSoftwareContextCall29 call = reinterpret_cast<CuteQSGSoftwareContextCall29>(taken[29]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      CuteQSGSoftwareContextCall30 call = reinterpret_cast<CuteQSGSoftwareContextCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteQSGSoftwareContextCall31 call = reinterpret_cast<CuteQSGSoftwareContextCall31>(taken[31]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[32]) {
      int handled = 0;
      CuteQSGSoftwareContextCall32 call = reinterpret_cast<CuteQSGSoftwareContextCall32>(taken[32]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[33]) {
      int handled = 0;
      CuteQSGSoftwareContextCall33 call = reinterpret_cast<CuteQSGSoftwareContextCall33>(taken[33]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[34]) {
      int handled = 0;
      CuteQSGSoftwareContextCall34 call = reinterpret_cast<CuteQSGSoftwareContextCall34>(taken[34]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QSGSoftwareContext::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QSGSoftwareContext10metaObjectEv(
    const QSGSoftwareContext *self) {
  return self->metaObject();
}

//  void *QSGSoftwareContext::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN18QSGSoftwareContext11qt_metacastEPKc(
    QSGSoftwareContext *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QSGSoftwareContext::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN18QSGSoftwareContext11qt_metacallEN11QMetaObject4CallEiPPv(
    QSGSoftwareContext *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QSGRenderContext *QSGSoftwareContext::createRenderContext()
extern "C" Q_DECL_EXPORT
QSGRenderContext *ritual_ZN18QSGSoftwareContext19createRenderContextEv(
    QSGSoftwareContext *self) {
  return self->createRenderContext();
}

//  QSGInternalRectangleNode
//      *QSGSoftwareContext::createInternalRectangleNode()
extern "C" Q_DECL_EXPORT
QSGInternalRectangleNode *ritual_ZN18QSGSoftwareContext27createInternalRectangleNodeEv(
    QSGSoftwareContext *self) {
  return self->createInternalRectangleNode();
}

//  QSGInternalImageNode
//      *QSGSoftwareContext::createInternalImageNode(QSGRenderContext
//      *renderContext)
extern "C" Q_DECL_EXPORT
QSGInternalImageNode *ritual_ZN18QSGSoftwareContext23createInternalImageNodeEP16QSGRenderContext(
    QSGSoftwareContext *self,
    QSGRenderContext *renderContext) {
  return self->createInternalImageNode(renderContext);
}

//  QSGPainterNode *QSGSoftwareContext::createPainterNode(QQuickPaintedItem
//      *item)
extern "C" Q_DECL_EXPORT
QSGPainterNode *ritual_ZN18QSGSoftwareContext17createPainterNodeEP17QQuickPaintedItem(
    QSGSoftwareContext *self,
    QQuickPaintedItem *item) {
  return self->createPainterNode(item);
}

//  QSGGlyphNode *QSGSoftwareContext::createGlyphNode(QSGRenderContext *rc,
//      QSGTextNode::RenderType renderType)
extern "C" Q_DECL_EXPORT
QSGGlyphNode *ritual_ZN18QSGSoftwareContext15createGlyphNodeEP16QSGRenderContextN11QSGTextNode10RenderTypeE(
    QSGSoftwareContext *self,
    QSGRenderContext *rc,
    QSGTextNode::RenderType renderType) {
  return self->createGlyphNode(rc, renderType);
}

//  QSGLayer *QSGSoftwareContext::createLayer(QSGRenderContext
//      *renderContext)
extern "C" Q_DECL_EXPORT
QSGLayer *ritual_ZN18QSGSoftwareContext11createLayerEP16QSGRenderContext(
    QSGSoftwareContext *self,
    QSGRenderContext *renderContext) {
  return self->createLayer(renderContext);
}

//  QSurfaceFormat QSGSoftwareContext::defaultSurfaceFormat() const
extern "C" Q_DECL_EXPORT
QSurfaceFormat *ritual_ZNK18QSGSoftwareContext20defaultSurfaceFormatEv(
    const QSGSoftwareContext *self) {
  return new QSurfaceFormat(self->defaultSurfaceFormat());
}

//  QSGRendererInterface
//      *QSGSoftwareContext::rendererInterface(QSGRenderContext
//      *renderContext)
extern "C" Q_DECL_EXPORT
QSGRendererInterface *ritual_ZN18QSGSoftwareContext17rendererInterfaceEP16QSGRenderContext(
    QSGSoftwareContext *self,
    QSGRenderContext *renderContext) {
  return self->rendererInterface(renderContext);
}

//  QSGRectangleNode *QSGSoftwareContext::createRectangleNode()
extern "C" Q_DECL_EXPORT
QSGRectangleNode *ritual_ZN18QSGSoftwareContext19createRectangleNodeEv(
    QSGSoftwareContext *self) {
  return self->createRectangleNode();
}

//  QSGImageNode *QSGSoftwareContext::createImageNode()
extern "C" Q_DECL_EXPORT
QSGImageNode *ritual_ZN18QSGSoftwareContext15createImageNodeEv(
    QSGSoftwareContext *self) {
  return self->createImageNode();
}

//  QSGNinePatchNode *QSGSoftwareContext::createNinePatchNode()
extern "C" Q_DECL_EXPORT
QSGNinePatchNode *ritual_ZN18QSGSoftwareContext19createNinePatchNodeEv(
    QSGSoftwareContext *self) {
  return self->createNinePatchNode();
}

#if QT_CONFIG(quick_sprite)
//  QSGSpriteNode *QSGSoftwareContext::createSpriteNode()
extern "C" Q_DECL_EXPORT
QSGSpriteNode *ritual_ZN18QSGSoftwareContext16createSpriteNodeEv(
    QSGSoftwareContext *self) {
  return self->createSpriteNode();
}
#endif  // QT_CONFIG(quick_sprite)

//  QSGTextNode::RenderType
//      QSGSoftwareContext::processTextRenderType(QSGTextNode::RenderType
//      renderType)
extern "C" Q_DECL_EXPORT
QSGTextNode::RenderType ritual_ZN18QSGSoftwareContext21processTextRenderTypeEN11QSGTextNode10RenderTypeE(
    QSGSoftwareContext *self,
    QSGTextNode::RenderType renderType) {
  return self->processTextRenderType(renderType);
}

//  GraphicsApi QSGSoftwareContext::graphicsApi() const
extern "C" Q_DECL_EXPORT
QSGRendererInterface::GraphicsApi ritual_ZNK18QSGSoftwareContext11graphicsApiEv(
    const QSGSoftwareContext *self) {
  return self->graphicsApi();
}

//  ShaderType QSGSoftwareContext::shaderType() const
extern "C" Q_DECL_EXPORT
QSGRendererInterface::ShaderType ritual_ZNK18QSGSoftwareContext10shaderTypeEv(
    const QSGSoftwareContext *self) {
  return self->shaderType();
}

//  ShaderCompilationTypes QSGSoftwareContext::shaderCompilationType() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QSGSoftwareContext21shaderCompilationTypeEv(
    const QSGSoftwareContext *self) {
  return static_cast<int>(self->shaderCompilationType().toInt());
}

//  ShaderSourceTypes QSGSoftwareContext::shaderSourceType() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QSGSoftwareContext16shaderSourceTypeEv(
    const QSGSoftwareContext *self) {
  return static_cast<int>(self->shaderSourceType().toInt());
}

//  void *QSGSoftwareContext::getResource(QQuickWindow *window, Resource
//      resource) const
extern "C" Q_DECL_EXPORT
void *ritual_ZNK18QSGSoftwareContext11getResourceEP12QQuickWindowN20QSGRendererInterface8ResourceE(
    const QSGSoftwareContext *self,
    QQuickWindow *window,
    QSGRendererInterface::Resource resource) {
  return self->getResource(window, resource);
}

//  QSGSoftwareContext as the QSGRendererInterface it is built on
extern "C" Q_DECL_EXPORT
QSGRendererInterface *ritual_cast_QSGSoftwareContext_QSGRendererInterface(
    QSGSoftwareContext *self) {
  return static_cast<QSGRendererInterface *>(self);
}

//  a Python function taken by a CuteQSGSoftwareContext, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSGSoftwareContext(
    QSGSoftwareContext *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSGSoftwareContext *>(self)->take(key, call);
}

//  QSGRenderContext *QSGSoftwareContext::createRenderContext()
extern "C" Q_DECL_EXPORT
QSGRenderContext *ritual_own_ZN18QSGSoftwareContext19createRenderContextEv(
    QSGSoftwareContext *self) {
  return self->QSGSoftwareContext::createRenderContext();
}

//  QSGPainterNode *QSGSoftwareContext::createPainterNode(QQuickPaintedItem
//      *item)
extern "C" Q_DECL_EXPORT
QSGPainterNode *ritual_own_ZN18QSGSoftwareContext17createPainterNodeEP17QQuickPaintedItem(
    QSGSoftwareContext *self,
    QQuickPaintedItem *item) {
  return self->QSGSoftwareContext::createPainterNode(item);
}

//  QSGGlyphNode *QSGSoftwareContext::createGlyphNode(QSGRenderContext *rc,
//      QSGTextNode::RenderType renderType)
extern "C" Q_DECL_EXPORT
QSGGlyphNode *ritual_own_ZN18QSGSoftwareContext15createGlyphNodeEP16QSGRenderContextN11QSGTextNode10RenderTypeE(
    QSGSoftwareContext *self,
    QSGRenderContext *rc,
    QSGTextNode::RenderType renderType) {
  return self->QSGSoftwareContext::createGlyphNode(rc, renderType);
}

//  QSurfaceFormat QSGSoftwareContext::defaultSurfaceFormat() const
extern "C" Q_DECL_EXPORT
QSurfaceFormat *ritual_own_ZNK18QSGSoftwareContext20defaultSurfaceFormatEv(
    const QSGSoftwareContext *self) {
  return new QSurfaceFormat(
      self->QSGSoftwareContext::defaultSurfaceFormat());
}

//  QSGRendererInterface
//      *QSGSoftwareContext::rendererInterface(QSGRenderContext
//      *renderContext)
extern "C" Q_DECL_EXPORT
QSGRendererInterface *ritual_own_ZN18QSGSoftwareContext17rendererInterfaceEP16QSGRenderContext(
    QSGSoftwareContext *self,
    QSGRenderContext *renderContext) {
  return self->QSGSoftwareContext::rendererInterface(renderContext);
}

//  QSGRectangleNode *QSGSoftwareContext::createRectangleNode()
extern "C" Q_DECL_EXPORT
QSGRectangleNode *ritual_own_ZN18QSGSoftwareContext19createRectangleNodeEv(
    QSGSoftwareContext *self) {
  return self->QSGSoftwareContext::createRectangleNode();
}

//  QSGImageNode *QSGSoftwareContext::createImageNode()
extern "C" Q_DECL_EXPORT
QSGImageNode *ritual_own_ZN18QSGSoftwareContext15createImageNodeEv(
    QSGSoftwareContext *self) {
  return self->QSGSoftwareContext::createImageNode();
}

//  QSGNinePatchNode *QSGSoftwareContext::createNinePatchNode()
extern "C" Q_DECL_EXPORT
QSGNinePatchNode *ritual_own_ZN18QSGSoftwareContext19createNinePatchNodeEv(
    QSGSoftwareContext *self) {
  return self->QSGSoftwareContext::createNinePatchNode();
}

#if QT_CONFIG(quick_sprite)
//  QSGSpriteNode *QSGSoftwareContext::createSpriteNode()
extern "C" Q_DECL_EXPORT
QSGSpriteNode *ritual_own_ZN18QSGSoftwareContext16createSpriteNodeEv(
    QSGSoftwareContext *self) {
  return self->QSGSoftwareContext::createSpriteNode();
}
#endif  // QT_CONFIG(quick_sprite)

//  QSGTextNode::RenderType
//      QSGSoftwareContext::processTextRenderType(QSGTextNode::RenderType
//      renderType)
extern "C" Q_DECL_EXPORT
QSGTextNode::RenderType ritual_own_ZN18QSGSoftwareContext21processTextRenderTypeEN11QSGTextNode10RenderTypeE(
    QSGSoftwareContext *self,
    QSGTextNode::RenderType renderType) {
  return self->QSGSoftwareContext::processTextRenderType(renderType);
}

//  GraphicsApi QSGSoftwareContext::graphicsApi() const
extern "C" Q_DECL_EXPORT
QSGRendererInterface::GraphicsApi ritual_own_ZNK18QSGSoftwareContext11graphicsApiEv(
    const QSGSoftwareContext *self) {
  return self->QSGSoftwareContext::graphicsApi();
}

//  ShaderType QSGSoftwareContext::shaderType() const
extern "C" Q_DECL_EXPORT
QSGRendererInterface::ShaderType ritual_own_ZNK18QSGSoftwareContext10shaderTypeEv(
    const QSGSoftwareContext *self) {
  return self->QSGSoftwareContext::shaderType();
}

//  ShaderCompilationTypes QSGSoftwareContext::shaderCompilationType() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK18QSGSoftwareContext21shaderCompilationTypeEv(
    const QSGSoftwareContext *self) {
  return static_cast<int>(
      self->QSGSoftwareContext::shaderCompilationType().toInt());
}

//  ShaderSourceTypes QSGSoftwareContext::shaderSourceType() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK18QSGSoftwareContext16shaderSourceTypeEv(
    const QSGSoftwareContext *self) {
  return static_cast<int>(
      self->QSGSoftwareContext::shaderSourceType().toInt());
}

//  void *QSGSoftwareContext::getResource(QQuickWindow *window, Resource
//      resource) const
extern "C" Q_DECL_EXPORT
void *ritual_own_ZNK18QSGSoftwareContext11getResourceEP12QQuickWindowN20QSGRendererInterface8ResourceE(
    const QSGSoftwareContext *self,
    QQuickWindow *window,
    QSGRendererInterface::Resource resource) {
  return self->QSGSoftwareContext::getResource(window, resource);
}
