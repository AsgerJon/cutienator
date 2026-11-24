//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgsoftwarecontext_p.h, Qt 6.12.0. Changes
//  made here are lost.
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
#include <QtQuick/private/qsgsoftwarelayer_p.h>
#include <QtQuick/private/qsgsoftwarecontext_p.h>
#include <QtQuick/private/qsgsoftwarepixmaprenderer_p.h>
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
#include <QtQuick/private/qsgsoftwarepublicnodes_p.h>
#include <QtQuick/private/qsgsoftwarelayer_p.h>
#include <QtQuick/private/qsgsoftwarepixmaptexture_p.h>
#include <QtQuick/private/qsgsoftwareinternalimagenode_p.h>
#include <QtQuick/private/qsgplaintexture_p.h>
#include <QtQuick/private/qsgsoftwarespritenode_p.h>
#include <QtQuick/private/qsgsoftwarepixmaptexture_p.h>
#include <QtGui/QPainter>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

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

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarecontext.cpp, line 28, as _ZN24QSGSoftwareRenderContextC1EP10QSGContext
inline QSGSoftwareRenderContext::QSGSoftwareRenderContext(QSGContext *ctx)
    : QSGRenderContext(ctx)
    , m_initialized(false)
    , m_activePainter(nullptr)
{
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

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarecontext.cpp, line 40, as _ZN18QSGSoftwareContext27createInternalRectangleNodeEv
inline QSGInternalRectangleNode *QSGSoftwareContext::createInternalRectangleNode()
{
    return new QSGSoftwareInternalRectangleNode();
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarecontext.cpp, line 45, as _ZN18QSGSoftwareContext23createInternalImageNodeEP16QSGRenderContext
inline QSGInternalImageNode *QSGSoftwareContext::createInternalImageNode(QSGRenderContext *renderContext)
{
    Q_UNUSED(renderContext);
    return new QSGSoftwareInternalImageNode();
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarecontext.cpp, line 51, as _ZN18QSGSoftwareContext17createPainterNodeEP17QQuickPaintedItem
inline QSGPainterNode *QSGSoftwareContext::createPainterNode(QQuickPaintedItem *item)
{
    return new QSGSoftwarePainterNode(item);
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarecontext.cpp, line 56, as _ZN18QSGSoftwareContext15createGlyphNodeEP16QSGRenderContextN11QSGTextNode10RenderTypeE
inline QSGGlyphNode *QSGSoftwareContext::createGlyphNode(QSGRenderContext *rc, QSGTextNode::RenderType renderType)
{
    Q_UNUSED(rc);
    Q_UNUSED(renderType);
    return new QSGSoftwareGlyphNode();
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarecontext.cpp, line 69, as _ZN18QSGSoftwareContext11createLayerEP16QSGRenderContext
inline QSGLayer *QSGSoftwareContext::createLayer(QSGRenderContext *renderContext)
{
    return new QSGSoftwareLayer(renderContext);
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

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarecontext.cpp, line 134, as _ZN18QSGSoftwareContext17rendererInterfaceEP16QSGRenderContext
inline QSGRendererInterface *QSGSoftwareContext::rendererInterface(QSGRenderContext *renderContext)
{
    Q_UNUSED(renderContext);
    return this;
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarecontext.cpp, line 140, as _ZN18QSGSoftwareContext19createRectangleNodeEv
inline QSGRectangleNode *QSGSoftwareContext::createRectangleNode()
{
    return new QSGSoftwareRectangleNode;
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarecontext.cpp, line 145, as _ZN18QSGSoftwareContext15createImageNodeEv
inline QSGImageNode *QSGSoftwareContext::createImageNode()
{
    return new QSGSoftwareImageNode;
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarecontext.cpp, line 150, as _ZN18QSGSoftwareContext19createNinePatchNodeEv
inline QSGNinePatchNode *QSGSoftwareContext::createNinePatchNode()
{
    return new QSGSoftwareNinePatchNode;
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarecontext.cpp, line 156, as _ZN18QSGSoftwareContext16createSpriteNodeEv
#if QT_CONFIG(quick_sprite)
inline QSGSpriteNode *QSGSoftwareContext::createSpriteNode()
{
    return new QSGSoftwareSpriteNode;
}
#endif  // QT_CONFIG(quick_sprite)

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarecontext.cpp, line 63, as _ZN18QSGSoftwareContext21processTextRenderTypeEN11QSGTextNode10RenderTypeE
inline QSGTextNode::RenderType QSGSoftwareContext::processTextRenderType(QSGTextNode::RenderType renderType)
{
    Q_UNUSED(renderType);
    return QSGTextNode::NativeRendering;
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarecontext.cpp, line 162, as _ZNK18QSGSoftwareContext11graphicsApiEv
inline QSGRendererInterface::GraphicsApi QSGSoftwareContext::graphicsApi() const
{
    return Software;
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarecontext.cpp, line 167, as _ZNK18QSGSoftwareContext10shaderTypeEv
inline QSGRendererInterface::ShaderType QSGSoftwareContext::shaderType() const
{
    return UnknownShadingLanguage;
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarecontext.cpp, line 172, as _ZNK18QSGSoftwareContext21shaderCompilationTypeEv
inline QSGRendererInterface::ShaderCompilationTypes QSGSoftwareContext::shaderCompilationType() const
{
    return {};
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarecontext.cpp, line 177, as _ZNK18QSGSoftwareContext16shaderSourceTypeEv
inline QSGRendererInterface::ShaderSourceTypes QSGSoftwareContext::shaderSourceType() const
{
    return {};
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
typedef void (*CuteQSGSoftwareContextCall17)(const void *, QSGRenderContext *, int *);
typedef void (*CuteQSGSoftwareContextCall18)(const void *, QSGRenderContext *, int *);
typedef void * (*CuteQSGSoftwareContextCall19)(const void *, QSGRenderContext *, int *);
typedef void * (*CuteQSGSoftwareContextCall20)(const void *, int *);
typedef void * (*CuteQSGSoftwareContextCall21)(const void *, QSGRenderContext *, int *);
typedef void * (*CuteQSGSoftwareContextCall22)(const void *, QObject *, int *);
typedef float (*CuteQSGSoftwareContextCall23)(const void *, QAnimationDriver *, int *);
typedef bool (*CuteQSGSoftwareContextCall24)(const void *, QAnimationDriver *, int *);
typedef const QSize * (*CuteQSGSoftwareContextCall25)(const void *, int *);
typedef void * (*CuteQSGSoftwareContextCall26)(const void *, QSGRenderContext *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSGSoftwareContextCall27)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSGSoftwareContextCall28)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGSoftwareContextCall29)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGSoftwareContextCall30)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGSoftwareContextCall31)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGSoftwareContextCall32)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGSoftwareContextCall33)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQSGSoftwareContext : public QSGSoftwareContext {
public:
  using QSGSoftwareContext::QSGSoftwareContext;
  void *taken[34] = {};

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
    if (!std::strcmp(key, "_ZN10QSGContext24renderContextInitializedEP16QSGRenderContext")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSGContext24renderContextInvalidatedEP16QSGRenderContext")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSGContext22createInternalTextNodeEP16QSGRenderContext")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSGContext34createGuiThreadShaderEffectManagerEv")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSGContext22createShaderEffectNodeEP16QSGRenderContext")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSGContext21createAnimationDriverEP7QObject")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSGContext31vsyncIntervalForAnimationDriverEP16QAnimationDriver")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSGContext16isVSyncDependentEP16QAnimationDriver")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QSGContext14minimumFBOSizeEv")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QSGContext14createTextNodeEP16QSGRenderContext")) {
      taken[26] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[27] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[28] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[29] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[30] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[31] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[32] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[33] = call;
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

  //  void QSGContext::renderContextInitialized(QSGRenderContext
  //      *renderContext)
  void renderContextInitialized(QSGRenderContext *renderContext) override {
    if (taken[17]) {
      int handled = 0;
      CuteQSGSoftwareContextCall17 call = reinterpret_cast<CuteQSGSoftwareContextCall17>(taken[17]);
      call(this, renderContext, &handled);
      if (handled) return;
    }
    QSGContext::renderContextInitialized(renderContext);
  }

  //  void QSGContext::renderContextInvalidated(QSGRenderContext
  //      *renderContext)
  void renderContextInvalidated(QSGRenderContext *renderContext) override {
    if (taken[18]) {
      int handled = 0;
      CuteQSGSoftwareContextCall18 call = reinterpret_cast<CuteQSGSoftwareContextCall18>(taken[18]);
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
    if (taken[19]) {
      int handled = 0;
      CuteQSGSoftwareContextCall19 call = reinterpret_cast<CuteQSGSoftwareContextCall19>(taken[19]);
      void * given = call(this, renderContext, &handled);
      if (handled) return static_cast<QSGInternalTextNode *>(given);
    }
    return QSGContext::createInternalTextNode(renderContext);
  }

  //  QSGGuiThreadShaderEffectManager
  //      *QSGContext::createGuiThreadShaderEffectManager()
  QSGGuiThreadShaderEffectManager *createGuiThreadShaderEffectManager() override {
    if (taken[20]) {
      int handled = 0;
      CuteQSGSoftwareContextCall20 call = reinterpret_cast<CuteQSGSoftwareContextCall20>(taken[20]);
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
    if (taken[21]) {
      int handled = 0;
      CuteQSGSoftwareContextCall21 call = reinterpret_cast<CuteQSGSoftwareContextCall21>(taken[21]);
      void * given = call(this, renderContext, &handled);
      if (handled) return static_cast<QSGShaderEffectNode *>(given);
    }
    return QSGContext::createShaderEffectNode(renderContext);
  }

  //  QAnimationDriver *QSGContext::createAnimationDriver(QObject *parent)
  QAnimationDriver *createAnimationDriver(QObject *parent) override {
    if (taken[22]) {
      int handled = 0;
      CuteQSGSoftwareContextCall22 call = reinterpret_cast<CuteQSGSoftwareContextCall22>(taken[22]);
      void * given = call(this, parent, &handled);
      if (handled) return static_cast<QAnimationDriver *>(given);
    }
    return QSGContext::createAnimationDriver(parent);
  }

  //  float QSGContext::vsyncIntervalForAnimationDriver(QAnimationDriver
  //      *driver)
  float vsyncIntervalForAnimationDriver(QAnimationDriver *driver) override {
    if (taken[23]) {
      int handled = 0;
      CuteQSGSoftwareContextCall23 call = reinterpret_cast<CuteQSGSoftwareContextCall23>(taken[23]);
      float given = call(this, driver, &handled);
      if (handled) return given;
    }
    return QSGContext::vsyncIntervalForAnimationDriver(driver);
  }

  //  bool QSGContext::isVSyncDependent(QAnimationDriver *driver)
  bool isVSyncDependent(QAnimationDriver *driver) override {
    if (taken[24]) {
      int handled = 0;
      CuteQSGSoftwareContextCall24 call = reinterpret_cast<CuteQSGSoftwareContextCall24>(taken[24]);
      bool given = call(this, driver, &handled);
      if (handled) return given;
    }
    return QSGContext::isVSyncDependent(driver);
  }

  //  QSize QSGContext::minimumFBOSize() const
  QSize minimumFBOSize() const override {
    if (taken[25]) {
      int handled = 0;
      CuteQSGSoftwareContextCall25 call = reinterpret_cast<CuteQSGSoftwareContextCall25>(taken[25]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QSGContext::minimumFBOSize();
  }

  //  QSGTextNode *QSGContext::createTextNode(QSGRenderContext
  //      *renderContext)
  QSGTextNode *createTextNode(QSGRenderContext *renderContext) override {
    if (taken[26]) {
      int handled = 0;
      CuteQSGSoftwareContextCall26 call = reinterpret_cast<CuteQSGSoftwareContextCall26>(taken[26]);
      void * given = call(this, renderContext, &handled);
      if (handled) return static_cast<QSGTextNode *>(given);
    }
    return QSGContext::createTextNode(renderContext);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQSGSoftwareContextCall27 call = reinterpret_cast<CuteQSGSoftwareContextCall27>(taken[27]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQSGSoftwareContextCall28 call = reinterpret_cast<CuteQSGSoftwareContextCall28>(taken[28]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQSGSoftwareContextCall29 call = reinterpret_cast<CuteQSGSoftwareContextCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      CuteQSGSoftwareContextCall30 call = reinterpret_cast<CuteQSGSoftwareContextCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteQSGSoftwareContextCall31 call = reinterpret_cast<CuteQSGSoftwareContextCall31>(taken[31]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[32]) {
      int handled = 0;
      CuteQSGSoftwareContextCall32 call = reinterpret_cast<CuteQSGSoftwareContextCall32>(taken[32]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[33]) {
      int handled = 0;
      CuteQSGSoftwareContextCall33 call = reinterpret_cast<CuteQSGSoftwareContextCall33>(taken[33]);
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
