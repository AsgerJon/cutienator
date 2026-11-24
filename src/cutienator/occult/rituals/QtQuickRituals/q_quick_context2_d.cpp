//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickcontext2d_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(quick_canvas)
#if QT_CONFIG(quick_canvas)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickcontext2d_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qsize.h>
#include <QtCore/qrect.h>
#include <QtGui/qimage.h>
#include <QtCore/qpoint.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/private/qquickcontext2dtexture_p.h>
#include <QtQuick/private/qquickcontext2dtile_p.h>
#include <QtQuick/private/qquickcanvasitem_p.h>
#include <QtQuick/private/qsgplaintexture_p.h>
#include <QtQuick/private/qquickcontext2dcommandbuffer_p.h>
#include <QtCore/QThread>
#include <QtGui/QGuiApplication>
#include <QtQuick/private/qquickcontext2dcommandbuffer_p.h>
#include <QtQuick/private/qquickcanvasitem_p.h>
#include <QtQml/qqml.h>
#include <QtCore/QMutex>
#include <QtQuick/qsgtexture.h>
#include <QtGui/QPaintEngine>
#include <QtQuick/private/qquickcontext2d_p.h>
#include <QtQuick/private/qquickcontext2dcommandbuffer_p.h>
#include <QtQuick/private/qquickcanvasitem_p.h>
#include <QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/private/qquickcontext2dtexture_p.h>
#if QT_CONFIG(quick_shadereffect)
#include <QtQuick/private/qquickshadereffectsource_p.h>
#endif
#include <QtQuick/qsgrendererinterface.h>
#include <QtQuick/private/qsgcontext_p.h>
#include <QtGui/private/qguisvg_p.h>
#if QT_CONFIG(quick_path)
#include <QtQuick/private/qquickpath_p.h>
#endif
#include <QtQml/qqmlinfo.h>
#include <QtQml/qqmlengine.h>
#include <QtQml/private/qv4domerrors_p.h>
#include <QtQml/private/qv4engine_p.h>
#include <QtQml/private/qv4object_p.h>
#include <QtQml/private/qv4qobjectwrapper_p.h>
#include <QtQuick/private/qquickwindow_p.h>
#include <QtQml/private/qv4value_p.h>
#include <QtQml/private/qv4functionobject_p.h>
#include <QtQml/private/qv4objectproto_p.h>
#include <QtQml/private/qv4scopedvalue_p.h>
#include <QtCore/private/qlocale_tools_p.h>
#include <QtCore/qmath.h>
#include <QtCore/qvector.h>
#include <QtCore/private/qnumeric_p.h>
#include <QtCore/QRunnable>
#include <QtGui/qguiapplication.h>
#include <QtGui/private/qguiapplication_p.h>
#include <QtGui/qpa/qplatformintegration.h>
#include <QtQuick/private/qsgdefaultrendercontext_p.h>
#include <QtCore/qpointer.h>
#include <cmath>
#if defined(Q_OS_QNX) || defined(Q_OS_ANDROID)
#include <ctype.h>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quick/items/context2d/qquickcontext2dtexture.cpp, line 129, as _ZN22QQuickContext2DTexture13canvasChangedERK5QSizeS2_RK5QRectS5_bb
inline void QQuickContext2DTexture::canvasChanged(const QSize& canvasSize, const QSize& tileSize, const QRect& canvasWindow, const QRect& dirtyRect, bool smooth, bool antialiasing)
{
    QSize ts = tileSize;
    if (ts.width() > canvasSize.width())
        ts.setWidth(canvasSize.width());

    if (ts.height() > canvasSize.height())
        ts.setHeight(canvasSize.height());

    setCanvasSize(canvasSize);
    setTileSize(ts);
    setCanvasWindow(canvasWindow);

    if (canvasSize == canvasWindow.size()) {
        m_tiledCanvas = false;
    } else {
        m_tiledCanvas = true;
    }

    if (dirtyRect.isValid())
        setDirtyRect(dirtyRect);

    setSmooth(smooth);
    setAntialiasing(antialiasing);
}

//  from ../qtdeclarative/src/quick/items/context2d/qquickcontext2dtexture.cpp, line 183, as _ZN22QQuickContext2DTexture5paintEP28QQuickContext2DCommandBuffer
inline void QQuickContext2DTexture::paint(QQuickContext2DCommandBuffer *ccb)
{
    QQuickContext2D::mutex.lock();
    if (canvasDestroyed()) {
        delete ccb;
        QQuickContext2D::mutex.unlock();
        return;
    }
    QQuickContext2D::mutex.unlock();
    if (!m_tiledCanvas) {
        paintWithoutTiles(ccb);
        delete ccb;
        return;
    }

    QRect tiledRegion = createTiles(m_canvasWindow.intersected(QRect(QPoint(0, 0), m_canvasSize)));
    if (!tiledRegion.isEmpty()) {
        QRect dirtyRect;
        for (QQuickContext2DTile* tile : std::as_const(m_tiles)) {
            if (tile->dirty()) {
                if (dirtyRect.isEmpty())
                    dirtyRect = tile->rect();
                else
                    dirtyRect |= tile->rect();
            }
        }

        if (beginPainting()) {
            QQuickContext2D::State oldState = m_state;
            for (QQuickContext2DTile* tile : std::as_const(m_tiles)) {
                if (tile->dirty()) {
                    ccb->replay(tile->createPainter(m_smooth, m_antialiasing), oldState, scaleFactor());
                    tile->drawFinished();
                    tile->markDirty(false);
                }
                compositeTile(tile);
            }
            endPainting();
            m_state = oldState;
            markDirtyTexture();
        }
    }
    delete ccb;
}

//  from ../qtdeclarative/src/quick/items/context2d/qquickcontext2dcommandbuffer.cpp, line 437, as _ZN28QQuickContext2DCommandBufferC1Ev
inline QQuickContext2DCommandBuffer::QQuickContext2DCommandBuffer()
    : cmdIdx(0)
    , intIdx(0)
    , boolIdx(0)
    , realIdx(0)
    , rectIdx(0)
    , colorIdx(0)
    , matrixIdx(0)
    , brushIdx(0)
    , pathIdx(0)
    , imageIdx(0)
    , pixmapIdx(0)
{
    static bool registered = false;
    if (!registered) {
        qRegisterMetaType<QQuickContext2DCommandBuffer*>("QQuickContext2DCommandBuffer*");
        registered = true;
    }
}

//  from ../qtdeclarative/src/quick/items/context2d/qquickcontext2dtexture.cpp, line 56, as _ZN22QQuickContext2DTexture11setTileSizeERK5QSize
inline bool QQuickContext2DTexture::setTileSize(const QSize &size)
{
    if (m_tileSize != size) {
        m_tileSize = size;
        return true;
    }
    return false;
}

//  from ../qtdeclarative/src/quick/items/context2d/qquickcontext2dtexture.cpp, line 113, as _ZN22QQuickContext2DTexture12setDirtyRectERK5QRect
inline bool QQuickContext2DTexture::setDirtyRect(const QRect &r)
{
    bool doDirty = false;
    if (m_tiledCanvas) {
        for (QQuickContext2DTile* t : std::as_const(m_tiles)) {
            bool dirty = t->rect().intersected(r).isValid();
            t->markDirty(dirty);
            if (dirty)
                doDirty = true;
        }
    } else {
        doDirty = m_canvasWindow.intersected(r).isValid();
    }
    return doDirty;
}

//  from ../qtdeclarative/src/quick/items/context2d/qquickcontext2dtexture.cpp, line 47, as _ZN22QQuickContext2DTexture13setCanvasSizeERK5QSize
inline bool QQuickContext2DTexture::setCanvasSize(const QSize &size)
{
    if (m_canvasSize != size) {
        m_canvasSize = size;
        return true;
    }
    return false;
}

//  from ../qtdeclarative/src/quick/items/context2d/qquickcontext2dtexture.cpp, line 70, as _ZN22QQuickContext2DTexture15setAntialiasingEb
inline void QQuickContext2DTexture::setAntialiasing(bool antialiasing)
{
    m_antialiasing = antialiasing;
}

//  from ../qtdeclarative/src/quick/items/context2d/qquickcontext2dtexture.cpp, line 65, as _ZN22QQuickContext2DTexture9setSmoothEb
inline void QQuickContext2DTexture::setSmooth(bool smooth)
{
    m_smooth = smooth;
}

//  from ../qtdeclarative/src/quick/items/context2d/qquickcontext2d.cpp, line 4257, as _ZN15QQuickContext2DD1Ev
inline QQuickContext2D::~QQuickContext2D()
{
    mutex.lock();
    m_texture->setItem(nullptr);
    delete m_buffer;
    m_texture->deleteLater();

    mutex.unlock();
}

//  from ../qtdeclarative/src/quick/items/context2d/qquickcontext2d.cpp, line 4272, as _ZNK15QQuickContext2D12contextNamesEv
inline QStringList QQuickContext2D::contextNames() const
{
    return QStringList() << QStringLiteral("2d");
}

//  from ../qtdeclarative/src/quick/items/context2d/qquickcontext2d.cpp, line 4277, as _ZN15QQuickContext2D4initEP16QQuickCanvasItemRK4QMapI7QString8QVariantE
inline void QQuickContext2D::init(QQuickCanvasItem *canvasItem, const QVariantMap &args)
{
    Q_UNUSED(args);

    m_canvas = canvasItem;
    m_renderTarget = canvasItem->renderTarget();
    m_renderStrategy = canvasItem->renderStrategy();

    // Disable threaded background rendering if the platform has issues with it
    if (m_renderTarget == QQuickCanvasItem::FramebufferObject
            && m_renderStrategy == QQuickCanvasItem::Threaded
            && !QGuiApplicationPrivate::platformIntegration()->hasCapability(QPlatformIntegration::ThreadedOpenGL)) {
        m_renderTarget = QQuickCanvasItem::Image;
    }

    // Disable framebuffer object based rendering always in Qt 6. It
    // is not implemented in the new RHI-based graphics stack, but the
    // enum value is still present. Switch to Image instead.
    if (m_renderTarget == QQuickCanvasItem::FramebufferObject)
        m_renderTarget = QQuickCanvasItem::Image;

    m_texture = new QQuickContext2DImageTexture;

    m_texture->setItem(canvasItem);
    m_texture->setCanvasWindow(canvasItem->canvasWindow().toRect());
    m_texture->setTileSize(canvasItem->tileSize());
    m_texture->setCanvasSize(canvasItem->canvasSize().toSize());
    m_texture->setSmooth(canvasItem->smooth());
    m_texture->setAntialiasing(canvasItem->antialiasing());
    m_texture->setOnCustomThread(m_renderStrategy == QQuickCanvasItem::Threaded);
    m_thread = QThread::currentThread();

    QThread *renderThread = m_thread;
    if (m_renderStrategy == QQuickCanvasItem::Threaded)
        renderThread = QQuickContext2DRenderThread::instance(qmlEngine(canvasItem));
    if (renderThread && renderThread != QThread::currentThread())
        m_texture->moveToThread(renderThread);
    connect(m_texture, SIGNAL(textureChanged()), SIGNAL(textureChanged()));

    reset();
}

//  from ../qtdeclarative/src/quick/items/context2d/qquickcontext2d.cpp, line 4319, as _ZN15QQuickContext2D7prepareERK5QSizeS2_RK5QRectS5_bb
inline void QQuickContext2D::prepare(const QSize& canvasSize, const QSize& tileSize, const QRect& canvasWindow, const QRect& dirtyRect, bool smooth, bool antialiasing)
{
    if (m_texture->thread() == QThread::currentThread()) {
        m_texture->canvasChanged(canvasSize, tileSize, canvasWindow, dirtyRect, smooth, antialiasing);
    } else {
        QEvent *e =  new QQuickContext2DTexture::CanvasChangeEvent(canvasSize,
                                                                   tileSize,
                                                                   canvasWindow,
                                                                   dirtyRect,
                                                                   smooth,
                                                                   antialiasing);
        QCoreApplication::postEvent(m_texture, e);
    }
}

//  from ../qtdeclarative/src/quick/items/context2d/qquickcontext2d.cpp, line 4334, as _ZN15QQuickContext2D5flushEv
inline void QQuickContext2D::flush()
{
    if (m_buffer) {
        if (m_texture->thread() == QThread::currentThread())
            m_texture->paint(m_buffer);
        else
            QCoreApplication::postEvent(m_texture, new QQuickContext2DTexture::PaintEvent(m_buffer));
    }
    m_buffer = new QQuickContext2DCommandBuffer();
}

//  from ../qtdeclarative/src/quick/items/context2d/qquickcontext2d.cpp, line 4345, as _ZNK15QQuickContext2D7textureEv
inline QQuickContext2DTexture *QQuickContext2D::texture() const
{
    return m_texture;
}

//  from ../qtdeclarative/src/quick/items/context2d/qquickcontext2d.cpp, line 4350, as _ZN15QQuickContext2D7toImageERK6QRectF
inline QImage QQuickContext2D::toImage(const QRectF& bounds)
{
    if (m_texture->thread() == QThread::currentThread()) {
            flush();
            m_texture->grabImage(bounds);
    } else if (m_renderStrategy == QQuickCanvasItem::Cooperative) {
        qWarning() << "Pixel readback is not supported in Cooperative mode, please try Threaded or Immediate mode";
        return QImage();
    } else {
        flush();
        QCoreApplication::postEvent(m_texture, new QEvent(QEvent::Type(QEvent::User + 10)));
        QMetaObject::invokeMethod(m_texture,
                                  "grabImage",
                                  Qt::BlockingQueuedConnection,
                                  Q_ARG(QRectF, bounds));
    }
    QImage img = m_grabbedImage;
    m_grabbedImage = QImage();
    m_grabbed = false;
    return img;
}

//  from ../qtdeclarative/src/quick/items/context2d/qquickcontext2d.cpp, line 4267, as _ZNK15QQuickContext2D7v4valueEv
inline QV4::ReturnedValue QQuickContext2D::v4value() const
{
    return m_v4value.value();
}

//  from ../qtdeclarative/src/quick/items/context2d/qquickcontext2d.cpp, line 4488, as _ZNK15QQuickContext2D8v4EngineEv
inline QV4::ExecutionEngine *QQuickContext2D::v4Engine() const
{
    return m_v4engine;
}

//  from ../qtdeclarative/src/quick/items/context2d/qquickcontext2d.cpp, line 4413, as _ZN15QQuickContext2D8popStateEv
inline void QQuickContext2D::popState()
{
    if (m_stateStack.isEmpty())
        return;

    QQuickContext2D::State newState = m_stateStack.pop();

    if (state.matrix != newState.matrix)
        buffer()->updateMatrix(newState.matrix);

    if (newState.globalAlpha != state.globalAlpha)
        buffer()->setGlobalAlpha(newState.globalAlpha);

    if (newState.globalCompositeOperation != state.globalCompositeOperation)
        buffer()->setGlobalCompositeOperation(newState.globalCompositeOperation);

    if (newState.fillStyle != state.fillStyle)
        buffer()->setFillStyle(newState.fillStyle);

    if (newState.strokeStyle != state.strokeStyle)
        buffer()->setStrokeStyle(newState.strokeStyle);

    if (newState.lineWidth != state.lineWidth)
        buffer()->setLineWidth(newState.lineWidth);

    if (newState.lineCap != state.lineCap)
        buffer()->setLineCap(newState.lineCap);

    if (newState.lineJoin != state.lineJoin)
        buffer()->setLineJoin(newState.lineJoin);

    if (newState.miterLimit != state.miterLimit)
        buffer()->setMiterLimit(newState.miterLimit);

    if (newState.clip != state.clip || newState.clipPath != state.clipPath)
        buffer()->clip(newState.clip, newState.clipPath);

    if (newState.shadowBlur != state.shadowBlur)
        buffer()->setShadowBlur(newState.shadowBlur);

    if (newState.shadowColor != state.shadowColor)
        buffer()->setShadowColor(newState.shadowColor);

    if (newState.shadowOffsetX != state.shadowOffsetX)
        buffer()->setShadowOffsetX(newState.shadowOffsetX);

    if (newState.shadowOffsetY != state.shadowOffsetY)
        buffer()->setShadowOffsetY(newState.shadowOffsetY);

    if (newState.lineDash != state.lineDash)
        buffer()->setLineDash(newState.lineDash);

    m_path = state.matrix.map(m_path);
    state = newState;
    m_path = state.matrix.inverted().map(m_path);
}

//  from ../qtdeclarative/src/quick/items/context2d/qquickcontext2d.cpp, line 4469, as _ZN15QQuickContext2D9pushStateEv
inline void QQuickContext2D::pushState()
{
    m_stateStack.push(state);
}

//  from ../qtdeclarative/src/quick/items/context2d/qquickcontext2d.cpp, line 4474, as _ZN15QQuickContext2D5resetEv
inline void QQuickContext2D::reset()
{
    QQuickContext2D::State newState;

    m_path = QPainterPath();

    newState.clipPath.setFillRule(Qt::WindingFill);

    m_stateStack.clear();
    m_stateStack.push(newState);
    popState();
    m_buffer->clearRect(QRectF(0, 0, m_canvas->width(), m_canvas->height()));
}

//  from ../qtdeclarative/src/quick/items/context2d/qquickcontext2d.cpp, line 3774, as _ZN15QQuickContext2D4fillEv
inline void QQuickContext2D::fill()
{
    if (!state.invertibleCTM)
        return;

    if (!m_path.elementCount())
        return;

    m_path.setFillRule(state.fillRule);
    buffer()->fill(m_path);
}

//  from ../qtdeclarative/src/quick/items/context2d/qquickcontext2d.cpp, line 3786, as _ZN15QQuickContext2D4clipEv
inline void QQuickContext2D::clip()
{
    if (!state.invertibleCTM)
        return;

    QPainterPath clipPath = m_path;
    clipPath.closeSubpath();
    if (state.clip) {
        state.clipPath = clipPath.intersected(state.clipPath);
    } else {
        state.clip = true;
        state.clipPath = clipPath;
    }
    buffer()->clip(state.clip, state.clipPath);
}

//  from ../qtdeclarative/src/quick/items/context2d/qquickcontext2d.cpp, line 3802, as _ZN15QQuickContext2D6strokeEv
inline void QQuickContext2D::stroke()
{
    if (!state.invertibleCTM)
        return;

    if (!m_path.elementCount())
        return;

    buffer()->stroke(m_path);
}

//  from ../qtdeclarative/src/quick/items/context2d/qquickcontext2d.cpp, line 3813, as _ZN15QQuickContext2D8fillRectEdddd
inline void QQuickContext2D::fillRect(qreal x, qreal y, qreal w, qreal h)
{
    if (!state.invertibleCTM)
        return;

    if (!qt_is_finite(x) || !qt_is_finite(y) || !qt_is_finite(w) || !qt_is_finite(h))
        return;

    buffer()->fillRect(QRectF(x, y, w, h));
}

//  from ../qtdeclarative/src/quick/items/context2d/qquickcontext2d.cpp, line 3824, as _ZN15QQuickContext2D10strokeRectEdddd
inline void QQuickContext2D::strokeRect(qreal x, qreal y, qreal w, qreal h)
{
    if (!state.invertibleCTM)
        return;

    if (!qt_is_finite(x) || !qt_is_finite(y) || !qt_is_finite(w) || !qt_is_finite(h))
        return;

    buffer()->strokeRect(QRectF(x, y, w, h));
}

//  from ../qtdeclarative/src/quick/items/context2d/qquickcontext2d.cpp, line 3835, as _ZN15QQuickContext2D9clearRectEdddd
inline void QQuickContext2D::clearRect(qreal x, qreal y, qreal w, qreal h)
{
    if (!state.invertibleCTM)
        return;

    if (!qt_is_finite(x) || !qt_is_finite(y) || !qt_is_finite(w) || !qt_is_finite(h))
        return;

    buffer()->clearRect(QRectF(x, y, w, h));
}

//  from ../qtdeclarative/src/quick/items/context2d/qquickcontext2d.cpp, line 3655, as _ZN15QQuickContext2D5scaleEdd
inline void QQuickContext2D::scale(qreal x,  qreal y)
{
    if (!state.invertibleCTM)
        return;

    if (!qt_is_finite(x) || !qt_is_finite(y))
        return;

    QTransform newTransform = state.matrix;
    newTransform.scale(x, y);

    if (!newTransform.isInvertible()) {
        state.invertibleCTM = false;
        return;
    }

    state.matrix = newTransform;
    buffer()->updateMatrix(state.matrix);
    m_path = QTransform().scale(1.0 / x, 1.0 / y).map(m_path);
}

//  from ../qtdeclarative/src/quick/items/context2d/qquickcontext2d.cpp, line 3676, as _ZN15QQuickContext2D6rotateEd
inline void QQuickContext2D::rotate(qreal angle)
{
    if (!state.invertibleCTM)
        return;

    if (!qt_is_finite(angle))
        return;

    QTransform newTransform =state.matrix;
    newTransform.rotate(qRadiansToDegrees(angle));

    if (!newTransform.isInvertible()) {
        state.invertibleCTM = false;
        return;
    }

    state.matrix = newTransform;
    buffer()->updateMatrix(state.matrix);
    m_path = QTransform().rotate(-qRadiansToDegrees(angle)).map(m_path);
}

//  from ../qtdeclarative/src/quick/items/context2d/qquickcontext2d.cpp, line 3697, as _ZN15QQuickContext2D5shearEdd
inline void QQuickContext2D::shear(qreal h, qreal v)
{
    if (!state.invertibleCTM)
        return;

    if (!qt_is_finite(h) || !qt_is_finite(v))
        return ;

    QTransform newTransform = state.matrix;
    newTransform.shear(h, v);

    if (!newTransform.isInvertible()) {
        state.invertibleCTM = false;
        return;
    }

    state.matrix = newTransform;
    buffer()->updateMatrix(state.matrix);
    m_path = QTransform().shear(-h, -v).map(m_path);
}

//  from ../qtdeclarative/src/quick/items/context2d/qquickcontext2d.cpp, line 3718, as _ZN15QQuickContext2D9translateEdd
inline void QQuickContext2D::translate(qreal x, qreal y)
{
    if (!state.invertibleCTM)
        return;

    if (!qt_is_finite(x) || !qt_is_finite(y))
        return ;

    QTransform newTransform = state.matrix;
    newTransform.translate(x, y);

    if (!newTransform.isInvertible()) {
        state.invertibleCTM = false;
        return;
    }

    state.matrix = newTransform;
    buffer()->updateMatrix(state.matrix);
    m_path = QTransform().translate(-x, -y).map(m_path);
}

//  from ../qtdeclarative/src/quick/items/context2d/qquickcontext2d.cpp, line 3739, as _ZN15QQuickContext2D9transformEdddddd
inline void QQuickContext2D::transform(qreal a, qreal b, qreal c, qreal d, qreal e, qreal f)
{
    if (!state.invertibleCTM)
        return;

    if (!qt_is_finite(a) || !qt_is_finite(b) || !qt_is_finite(c) || !qt_is_finite(d) || !qt_is_finite(e) || !qt_is_finite(f))
        return;

    QTransform transform(a, b, c, d, e, f);
    QTransform newTransform = state.matrix * transform;

    if (!newTransform.isInvertible()) {
        state.invertibleCTM = false;
        return;
    }
    state.matrix = newTransform;
    buffer()->updateMatrix(state.matrix);
    m_path = transform.inverted().map(m_path);
}

//  from ../qtdeclarative/src/quick/items/context2d/qquickcontext2d.cpp, line 3759, as _ZN15QQuickContext2D12setTransformEdddddd
inline void QQuickContext2D::setTransform(qreal a, qreal b, qreal c, qreal d, qreal e, qreal f)
{
    if (!qt_is_finite(a) || !qt_is_finite(b) || !qt_is_finite(c) || !qt_is_finite(d) || !qt_is_finite(e) || !qt_is_finite(f))
        return;

    QTransform ctm = state.matrix;
    if (!ctm.isInvertible())
        return;

    state.matrix = ctm.inverted() * state.matrix;
    m_path = ctm.map(m_path);
    state.invertibleCTM = true;
    transform(a, b, c, d, e, f);
}

//  from ../qtdeclarative/src/quick/items/context2d/qquickcontext2d.cpp, line 3862, as _ZN15QQuickContext2D9beginPathEv
inline void QQuickContext2D::beginPath()
{
    if (!m_path.elementCount())
        return;
    m_path = QPainterPath();
}

//  from ../qtdeclarative/src/quick/items/context2d/qquickcontext2d.cpp, line 3869, as _ZN15QQuickContext2D9closePathEv
inline void QQuickContext2D::closePath()
{
    if (!m_path.elementCount())
        return;

    QRectF boundRect = m_path.boundingRect();
    if (boundRect.width() || boundRect.height())
        m_path.closeSubpath();
    //FIXME:QPainterPath set the current point to (0,0) after close subpath
    //should be the first point of the previous subpath
}

//  from ../qtdeclarative/src/quick/items/context2d/qquickcontext2d.cpp, line 3881, as _ZN15QQuickContext2D6moveToEdd
inline void QQuickContext2D::moveTo( qreal x, qreal y)
{
    if (!state.invertibleCTM)
        return;

    //FIXME: moveTo should not close the previous subpath
    m_path.moveTo(QPointF(x, y));
}

//  from ../qtdeclarative/src/quick/items/context2d/qquickcontext2d.cpp, line 3890, as _ZN15QQuickContext2D6lineToEdd
inline void QQuickContext2D::lineTo( qreal x, qreal y)
{
    if (!state.invertibleCTM)
        return;

    QPointF pt(x, y);

    if (!m_path.elementCount())
        m_path.moveTo(pt);
    else if (m_path.currentPosition() != pt)
        m_path.lineTo(pt);
}

//  from ../qtdeclarative/src/quick/items/context2d/qquickcontext2d.cpp, line 3903, as _ZN15QQuickContext2D16quadraticCurveToEdddd
inline void QQuickContext2D::quadraticCurveTo(qreal cpx, qreal cpy,
                                           qreal x, qreal y)
{
    if (!state.invertibleCTM)
        return;

    if (!m_path.elementCount())
        m_path.moveTo(QPointF(cpx, cpy));

    QPointF pt(x, y);
    if (m_path.currentPosition() != pt)
        m_path.quadTo(QPointF(cpx, cpy), pt);
}

//  from ../qtdeclarative/src/quick/items/context2d/qquickcontext2d.cpp, line 3917, as _ZN15QQuickContext2D13bezierCurveToEdddddd
inline void QQuickContext2D::bezierCurveTo(qreal cp1x, qreal cp1y,
                                        qreal cp2x, qreal cp2y,
                                        qreal x, qreal y)
{
    if (!state.invertibleCTM)
        return;

    if (!m_path.elementCount())
        m_path.moveTo(QPointF(cp1x, cp1y));

    QPointF pt(x, y);
    if (m_path.currentPosition() != pt)
        m_path.cubicTo(QPointF(cp1x, cp1y), QPointF(cp2x, cp2y),  pt);
}

//  from ../qtdeclarative/src/quick/items/context2d/qquickcontext2d.cpp, line 3985, as _ZN15QQuickContext2D5arcToEddddd
inline void QQuickContext2D::arcTo(qreal x1, qreal y1,
                                qreal x2, qreal y2,
                                qreal radius)
{
    if (!state.invertibleCTM)
        return;

    if (!qt_is_finite(x1) || !qt_is_finite(y1) || !qt_is_finite(x2) || !qt_is_finite(y2) || !qt_is_finite(radius))
        return;

    QPointF st(x1, y1);
    QPointF end(x2, y2);

    if (!m_path.elementCount())
        m_path.moveTo(st);
    else if (st == m_path.currentPosition() || st == end || !radius)
        lineTo(x1, y1);
    else
        addArcTo(st, end, radius);
 }

void QQuickContext2D::rect(qreal x, qreal y, qreal w, qreal h)
{
    if (!state.invertibleCTM)
        return;
    if (!qt_is_finite(x) || !qt_is_finite(y) || !qt_is_finite(w) || !qt_is_finite(h))
        return;

    if (!w && !h) {
        m_path.moveTo(x, y);
        return;
    }
    m_path.addRect(x, y, w, h);
}

//  from ../qtdeclarative/src/quick/items/context2d/qquickcontext2d.cpp, line 4020, as _ZN15QQuickContext2D11roundedRectEdddddd
inline void QQuickContext2D::roundedRect(qreal x, qreal y,
                               qreal w, qreal h,
                               qreal xr, qreal yr)
{
    if (!state.invertibleCTM)
        return;

    if (!qt_is_finite(x) || !qt_is_finite(y) || !qt_is_finite(w) || !qt_is_finite(h) || !qt_is_finite(xr) || !qt_is_finite(yr))
        return;

    if (!w && !h) {
        m_path.moveTo(x, y);
        return;
    }
    m_path.addRoundedRect(QRectF(x, y, w, h), xr, yr, Qt::AbsoluteSize);
}

//  from ../qtdeclarative/src/quick/items/context2d/qquickcontext2d.cpp, line 4037, as _ZN15QQuickContext2D7ellipseEdddd
inline void QQuickContext2D::ellipse(qreal x, qreal y,
                           qreal w, qreal h)
{
    if (!state.invertibleCTM)
        return;

    if (!qt_is_finite(x) || !qt_is_finite(y) || !qt_is_finite(w) || !qt_is_finite(h))
        return;

    if (!w && !h) {
        m_path.moveTo(x, y);
        return;
    }

    m_path.addEllipse(x, y, w, h);
}

//  from ../qtdeclarative/src/quick/items/context2d/qquickcontext2d.cpp, line 4054, as _ZN15QQuickContext2D4textERK7QStringdd
inline void QQuickContext2D::text(const QString& str, qreal x, qreal y)
{
    if (!state.invertibleCTM)
        return;

    QPainterPath path;
    path.addText(x, y, state.font, str);
    m_path.addPath(path);
}

//  from ../qtdeclarative/src/quick/items/context2d/qquickcontext2d.cpp, line 4064, as _ZN15QQuickContext2D3arcEdddddb
inline void QQuickContext2D::arc(qreal xc, qreal yc, qreal radius, qreal sar, qreal ear, bool antiClockWise)
{
    if (!state.invertibleCTM)
        return;

    if (!qt_is_finite(xc) || !qt_is_finite(yc) || !qt_is_finite(sar) || !qt_is_finite(ear) || !qt_is_finite(radius))
        return;

    if (sar == ear)
        return;


    //### HACK

    // In Qt we don't switch the coordinate system for degrees
    // and still use the 0,0 as bottom left for degrees so we need
    // to switch
    sar = -sar;
    ear = -ear;
    antiClockWise = !antiClockWise;
    //end hack

    float sa = qRadiansToDegrees(sar);
    float ea = qRadiansToDegrees(ear);

    double span = 0;

    double xs     = xc - radius;
    double ys     = yc - radius;
    double width  = radius*2;
    double height = radius*2;
    if ((!antiClockWise && (ea - sa >= 360)) || (antiClockWise && (sa - ea >= 360)))
        // If the anticlockwise argument is false and endAngle-startAngle is equal to or greater than 2*PI, or, if the
        // anticlockwise argument is true and startAngle-endAngle is equal to or greater than 2*PI, then the arc is the whole
        // circumference of this circle.
        span = 360;
    else {
        if (!antiClockWise && (ea < sa)) {
            span += 360;
        } else if (antiClockWise && (sa < ea)) {
            span -= 360;
        }
        //### this is also due to switched coordinate system
        // we would end up with a 0 span instead of 360
        if (!(qFuzzyCompare(span + (ea - sa) + 1, 1) &&
              qFuzzyCompare(qAbs(span), 360))) {
            span   += ea - sa;
        }
    }

    // If the path is empty, move to where the arc will start to avoid painting a line from (0,0)
    if (!m_path.elementCount())
        m_path.arcMoveTo(xs, ys, width, height, sa);
    else if (!radius) {
        m_path.lineTo(xc, yc);
        return;
    }

    m_path.arcTo(xs, ys, width, height, sa, span);
}

//  from ../qtdeclarative/src/quick/items/context2d/qquickcontext2d.cpp, line 3932, as _ZN15QQuickContext2D8addArcToERK7QPointFS2_d
inline void QQuickContext2D::addArcTo(const QPointF& p1, const QPointF& p2, qreal radius)
{
    QPointF p0(m_path.currentPosition());

    QPointF p1p0((p0.x() - p1.x()), (p0.y() - p1.y()));
    QPointF p1p2((p2.x() - p1.x()), (p2.y() - p1.y()));
    qreal p1p0_length = std::hypot(p1p0.x(), p1p0.y());
    qreal p1p2_length = std::hypot(p1p2.x(), p1p2.y());

    qreal cos_phi = QPointF::dotProduct(p1p0, p1p2) / (p1p0_length * p1p2_length);

    // The points p0, p1, and p2 are on the same straight line (HTML5, 4.8.11.1.8)
    // We could have used areCollinear() here, but since we're reusing
    // the variables computed above later on we keep this logic.
    if (qFuzzyCompare(std::abs(cos_phi), qreal(1.0))) {
        m_path.lineTo(p1);
        return;
    }

    qreal tangent = radius / std::tan(std::acos(cos_phi) / 2);
    qreal factor_p1p0 = tangent / p1p0_length;
    QPointF t_p1p0((p1.x() + factor_p1p0 * p1p0.x()), (p1.y() + factor_p1p0 * p1p0.y()));

    QPointF orth_p1p0(p1p0.y(), -p1p0.x());
    qreal orth_p1p0_length = std::hypot(orth_p1p0.x(), orth_p1p0.y());
    qreal factor_ra = radius / orth_p1p0_length;

    // angle between orth_p1p0 and p1p2 to get the right vector orthographic to p1p0
    qreal cos_alpha = QPointF::dotProduct(orth_p1p0, p1p2) / (orth_p1p0_length * p1p2_length);
    if (cos_alpha < 0.f)
        orth_p1p0 = QPointF(-orth_p1p0.x(), -orth_p1p0.y());

    QPointF p((t_p1p0.x() + factor_ra * orth_p1p0.x()), (t_p1p0.y() + factor_ra * orth_p1p0.y()));

    // calculate angles for addArc
    orth_p1p0 = QPointF(-orth_p1p0.x(), -orth_p1p0.y());
    qreal sa = std::atan2(orth_p1p0.y(), orth_p1p0.x());

    // anticlockwise logic
    bool anticlockwise = false;

    qreal factor_p1p2 = tangent / p1p2_length;
    QPointF t_p1p2((p1.x() + factor_p1p2 * p1p2.x()), (p1.y() + factor_p1p2 * p1p2.y()));
    QPointF orth_p1p2((t_p1p2.x() - p.x()), (t_p1p2.y() - p.y()));
    qreal ea = std::atan2(orth_p1p2.y(), orth_p1p2.x());
    if ((sa > ea) && ((sa - ea) < M_PI))
        anticlockwise = true;
    if ((sa < ea) && ((ea - sa) > M_PI))
        anticlockwise = true;

    arc(p.x(), p.y(), radius, sa, ea, anticlockwise);
}

//  from ../qtdeclarative/src/quick/items/context2d/qquickcontext2d.cpp, line 4166, as _ZN15QQuickContext2D15setGrabbedImageERK6QImage
inline void QQuickContext2D::setGrabbedImage(const QImage& grab)
{
    m_grabbedImage = grab;
    m_grabbed = true;
}
//  -----------------------------------------------------------------------

//  A QQuickContext2D that Python can take functions over in. Every QQuickContext2D
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(quick_canvas)
typedef void (*CuteQQuickContext2DCall0)(const void *, const QSize *, const QSize *, const QRect *, const QRect *, bool, bool, int *);
#endif  // QT_CONFIG(quick_canvas)
#if QT_CONFIG(quick_canvas)
typedef void (*CuteQQuickContext2DCall1)(const void *, int *);
#endif  // QT_CONFIG(quick_canvas)
#if QT_CONFIG(quick_canvas)
typedef const QImage * (*CuteQQuickContext2DCall2)(const void *, const QRectF *, int *);
#endif  // QT_CONFIG(quick_canvas)
#if QT_CONFIG(quick_canvas)
typedef QV4::ReturnedValue (*CuteQQuickContext2DCall3)(const void *, int *);
#endif  // QT_CONFIG(quick_canvas)
#if QT_CONFIG(quick_canvas)
typedef void * (*CuteQQuickContext2DCall4)(const void *, int *);
#endif  // QT_CONFIG(quick_canvas)
#if QT_CONFIG(quick_canvas)
typedef void (*CuteQQuickContext2DCall5)(const void *, QV4::ExecutionEngine *, int *);
#endif  // QT_CONFIG(quick_canvas)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickContext2DCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickContext2DCall7)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickContext2DCall8)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickContext2DCall9)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickContext2DCall10)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickContext2DCall11)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickContext2DCall12)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickContext2D : public QQuickContext2D {
public:
  using QQuickContext2D::QQuickContext2D;
  void *taken[13] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(quick_canvas)
    if (!std::strcmp(key, "_ZN19QQuickCanvasContext7prepareERK5QSizeS2_RK5QRectS5_bb")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_canvas)
#if QT_CONFIG(quick_canvas)
    if (!std::strcmp(key, "_ZN19QQuickCanvasContext5flushEv")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_canvas)
#if QT_CONFIG(quick_canvas)
    if (!std::strcmp(key, "_ZN19QQuickCanvasContext7toImageERK6QRectF")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_canvas)
#if QT_CONFIG(quick_canvas)
    if (!std::strcmp(key, "_ZNK19QQuickCanvasContext7v4valueEv")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_canvas)
#if QT_CONFIG(quick_canvas)
    if (!std::strcmp(key, "_ZNK19QQuickCanvasContext8v4EngineEv")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_canvas)
#if QT_CONFIG(quick_canvas)
    if (!std::strcmp(key, "_ZN19QQuickCanvasContext11setV4EngineEPN3QV415ExecutionEngineE")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_canvas)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if QT_CONFIG(quick_canvas)
  //  void QQuickContext2D::prepare(const QSize &canvasSize, const QSize
  //      &tileSize, const QRect &canvasWindow, const QRect &dirtyRect,
  //      bool smooth, bool antialiasing)
  void prepare(
      const QSize &canvasSize,
      const QSize &tileSize,
      const QRect &canvasWindow,
      const QRect &dirtyRect,
      bool smooth,
      bool antialiasing) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickContext2DCall0 call = reinterpret_cast<CuteQQuickContext2DCall0>(taken[0]);
      call(this, &canvasSize, &tileSize, &canvasWindow, &dirtyRect, smooth, antialiasing, &handled);
      if (handled) return;
    }
    QQuickContext2D::prepare(canvasSize, tileSize, canvasWindow, dirtyRect, smooth, antialiasing);
  }
#endif  // QT_CONFIG(quick_canvas)

#if QT_CONFIG(quick_canvas)
  //  void QQuickContext2D::flush()
  void flush() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickContext2DCall1 call = reinterpret_cast<CuteQQuickContext2DCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickContext2D::flush();
  }
#endif  // QT_CONFIG(quick_canvas)

#if QT_CONFIG(quick_canvas)
  //  QImage QQuickContext2D::toImage(const QRectF &bounds)
  QImage toImage(const QRectF &bounds) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickContext2DCall2 call = reinterpret_cast<CuteQQuickContext2DCall2>(taken[2]);
      const QImage * given = call(this, &bounds, &handled);
      if (handled && given) return *given;
    }
    return QQuickContext2D::toImage(bounds);
  }
#endif  // QT_CONFIG(quick_canvas)

#if QT_CONFIG(quick_canvas)
  //  QV4::ReturnedValue QQuickContext2D::v4value() const
  QV4::ReturnedValue v4value() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickContext2DCall3 call = reinterpret_cast<CuteQQuickContext2DCall3>(taken[3]);
      QV4::ReturnedValue given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickContext2D::v4value();
  }
#endif  // QT_CONFIG(quick_canvas)

#if QT_CONFIG(quick_canvas)
  //  QV4::ExecutionEngine *QQuickContext2D::v4Engine() const
  QV4::ExecutionEngine *v4Engine() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickContext2DCall4 call = reinterpret_cast<CuteQQuickContext2DCall4>(taken[4]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QV4::ExecutionEngine *>(given);
    }
    return QQuickContext2D::v4Engine();
  }
#endif  // QT_CONFIG(quick_canvas)

#if QT_CONFIG(quick_canvas)
  //  void QQuickContext2D::setV4Engine(QV4::ExecutionEngine *eng)
  void setV4Engine(QV4::ExecutionEngine *eng) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickContext2DCall5 call = reinterpret_cast<CuteQQuickContext2DCall5>(taken[5]);
      call(this, eng, &handled);
      if (handled) return;
    }
    QQuickContext2D::setV4Engine(eng);
  }
#endif  // QT_CONFIG(quick_canvas)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickContext2DCall6 call = reinterpret_cast<CuteQQuickContext2DCall6>(taken[6]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickContext2DCall7 call = reinterpret_cast<CuteQQuickContext2DCall7>(taken[7]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickContext2DCall8 call = reinterpret_cast<CuteQQuickContext2DCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickContext2DCall9 call = reinterpret_cast<CuteQQuickContext2DCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickContext2DCall10 call = reinterpret_cast<CuteQQuickContext2DCall10>(taken[10]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickContext2DCall11 call = reinterpret_cast<CuteQQuickContext2DCall11>(taken[11]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickContext2DCall12 call = reinterpret_cast<CuteQQuickContext2DCall12>(taken[12]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickContext2D::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QQuickContext2D10metaObjectEv(
    const QQuickContext2D *self) {
  return self->metaObject();
}

//  QQuickContext2D::~QQuickContext2D()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickContext2DD1Ev(QQuickContext2D *self) {
  delete self;
}

//  QStringList QQuickContext2D::contextNames() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK15QQuickContext2D12contextNamesEv(
    const QQuickContext2D *self) {
  return new QList<QString>(self->contextNames());
}

//  void QQuickContext2D::init(QQuickCanvasItem *canvasItem, const
//      QVariantMap &args)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickContext2D4initEP16QQuickCanvasItemRK4QMapI7QString8QVariantE(
    QQuickContext2D *self,
    QQuickCanvasItem *canvasItem,
    const QMap<QString, QVariant> *args) {
  self->init(canvasItem, *args);
}

//  void QQuickContext2D::prepare(const QSize &canvasSize, const QSize
//      &tileSize, const QRect &canvasWindow, const QRect &dirtyRect, bool
//      smooth, bool antialiasing)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickContext2D7prepareERK5QSizeS2_RK5QRectS5_bb(
    QQuickContext2D *self,
    const QSize *canvasSize,
    const QSize *tileSize,
    const QRect *canvasWindow,
    const QRect *dirtyRect,
    bool smooth,
    bool antialiasing) {
  self->prepare(
      *canvasSize,
      *tileSize,
      *canvasWindow,
      *dirtyRect,
      smooth,
      antialiasing);
}

//  void QQuickContext2D::flush()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickContext2D5flushEv(QQuickContext2D *self) {
  self->flush();
}

//  QThread *QQuickContext2D::thread() const
extern "C" Q_DECL_EXPORT
QThread *ritual_ZNK15QQuickContext2D6threadEv(const QQuickContext2D *self) {
  return self->thread();
}

//  QQuickContext2DTexture *QQuickContext2D::texture() const
extern "C" Q_DECL_EXPORT
QQuickContext2DTexture *ritual_ZNK15QQuickContext2D7textureEv(
    const QQuickContext2D *self) {
  return self->texture();
}

//  QImage QQuickContext2D::toImage(const QRectF &bounds)
extern "C" Q_DECL_EXPORT
QImage *ritual_ZN15QQuickContext2D7toImageERK6QRectF(
    QQuickContext2D *self,
    const QRectF *bounds) {
  return new QImage(self->toImage(*bounds));
}

//  QV4::ReturnedValue QQuickContext2D::v4value() const
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZNK15QQuickContext2D7v4valueEv(
    const QQuickContext2D *self) {
  return self->v4value();
}

//  QV4::ExecutionEngine *QQuickContext2D::v4Engine() const
extern "C" Q_DECL_EXPORT
QV4::ExecutionEngine *ritual_ZNK15QQuickContext2D8v4EngineEv(
    const QQuickContext2D *self) {
  return self->v4Engine();
}

//  QQuickCanvasItem *QQuickContext2D::canvas() const
extern "C" Q_DECL_EXPORT
QQuickCanvasItem *ritual_ZNK15QQuickContext2D6canvasEv(
    const QQuickContext2D *self) {
  return self->canvas();
}

//  QQuickContext2DCommandBuffer *QQuickContext2D::buffer() const
extern "C" Q_DECL_EXPORT
QQuickContext2DCommandBuffer *ritual_ZNK15QQuickContext2D6bufferEv(
    const QQuickContext2D *self) {
  return self->buffer();
}

//  bool QQuickContext2D::bufferValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QQuickContext2D11bufferValidEv(
    const QQuickContext2D *self) {
  return self->bufferValid();
}

//  void QQuickContext2D::popState()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickContext2D8popStateEv(QQuickContext2D *self) {
  self->popState();
}

//  void QQuickContext2D::pushState()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickContext2D9pushStateEv(QQuickContext2D *self) {
  self->pushState();
}

//  void QQuickContext2D::reset()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickContext2D5resetEv(QQuickContext2D *self) {
  self->reset();
}

//  void QQuickContext2D::fill()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickContext2D4fillEv(QQuickContext2D *self) {
  self->fill();
}

//  void QQuickContext2D::clip()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickContext2D4clipEv(QQuickContext2D *self) {
  self->clip();
}

//  void QQuickContext2D::stroke()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickContext2D6strokeEv(QQuickContext2D *self) {
  self->stroke();
}

//  void QQuickContext2D::fillRect(qreal x, qreal y, qreal w, qreal h)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickContext2D8fillRectEdddd(
    QQuickContext2D *self,
    qreal x,
    qreal y,
    qreal w,
    qreal h) {
  self->fillRect(x, y, w, h);
}

//  void QQuickContext2D::strokeRect(qreal x, qreal y, qreal w, qreal h)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickContext2D10strokeRectEdddd(
    QQuickContext2D *self,
    qreal x,
    qreal y,
    qreal w,
    qreal h) {
  self->strokeRect(x, y, w, h);
}

//  void QQuickContext2D::clearRect(qreal x, qreal y, qreal w, qreal h)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickContext2D9clearRectEdddd(
    QQuickContext2D *self,
    qreal x,
    qreal y,
    qreal w,
    qreal h) {
  self->clearRect(x, y, w, h);
}

//  void QQuickContext2D::scale(qreal x, qreal y)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickContext2D5scaleEdd(
    QQuickContext2D *self,
    qreal x,
    qreal y) {
  self->scale(x, y);
}

//  void QQuickContext2D::rotate(qreal angle)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickContext2D6rotateEd(
    QQuickContext2D *self,
    qreal angle) {
  self->rotate(angle);
}

//  void QQuickContext2D::shear(qreal h, qreal v)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickContext2D5shearEdd(
    QQuickContext2D *self,
    qreal h,
    qreal v) {
  self->shear(h, v);
}

//  void QQuickContext2D::translate(qreal x, qreal y)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickContext2D9translateEdd(
    QQuickContext2D *self,
    qreal x,
    qreal y) {
  self->translate(x, y);
}

//  void QQuickContext2D::transform(qreal a, qreal b, qreal c, qreal d, qreal
//      e, qreal f)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickContext2D9transformEdddddd(
    QQuickContext2D *self,
    qreal a,
    qreal b,
    qreal c,
    qreal d,
    qreal e,
    qreal f) {
  self->transform(a, b, c, d, e, f);
}

//  void QQuickContext2D::setTransform(qreal a, qreal b, qreal c, qreal d,
//      qreal e, qreal f)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickContext2D12setTransformEdddddd(
    QQuickContext2D *self,
    qreal a,
    qreal b,
    qreal c,
    qreal d,
    qreal e,
    qreal f) {
  self->setTransform(a, b, c, d, e, f);
}

//  void QQuickContext2D::beginPath()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickContext2D9beginPathEv(QQuickContext2D *self) {
  self->beginPath();
}

//  void QQuickContext2D::closePath()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickContext2D9closePathEv(QQuickContext2D *self) {
  self->closePath();
}

//  void QQuickContext2D::moveTo(qreal x, qreal y)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickContext2D6moveToEdd(
    QQuickContext2D *self,
    qreal x,
    qreal y) {
  self->moveTo(x, y);
}

//  void QQuickContext2D::lineTo(qreal x, qreal y)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickContext2D6lineToEdd(
    QQuickContext2D *self,
    qreal x,
    qreal y) {
  self->lineTo(x, y);
}

//  void QQuickContext2D::quadraticCurveTo(qreal cpx, qreal cpy, qreal x,
//      qreal y)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickContext2D16quadraticCurveToEdddd(
    QQuickContext2D *self,
    qreal cpx,
    qreal cpy,
    qreal x,
    qreal y) {
  self->quadraticCurveTo(cpx, cpy, x, y);
}

//  void QQuickContext2D::bezierCurveTo(qreal cp1x, qreal cp1y, qreal cp2x,
//      qreal cp2y, qreal x, qreal y)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickContext2D13bezierCurveToEdddddd(
    QQuickContext2D *self,
    qreal cp1x,
    qreal cp1y,
    qreal cp2x,
    qreal cp2y,
    qreal x,
    qreal y) {
  self->bezierCurveTo(cp1x, cp1y, cp2x, cp2y, x, y);
}

//  void QQuickContext2D::arcTo(qreal x1, qreal y1, qreal x2, qreal y2, qreal
//      radius)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickContext2D5arcToEddddd(
    QQuickContext2D *self,
    qreal x1,
    qreal y1,
    qreal x2,
    qreal y2,
    qreal radius) {
  self->arcTo(x1, y1, x2, y2, radius);
}

//  void QQuickContext2D::roundedRect(qreal x, qreal y, qreal w, qreal h,
//      qreal xr, qreal yr)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickContext2D11roundedRectEdddddd(
    QQuickContext2D *self,
    qreal x,
    qreal y,
    qreal w,
    qreal h,
    qreal xr,
    qreal yr) {
  self->roundedRect(x, y, w, h, xr, yr);
}

//  void QQuickContext2D::ellipse(qreal x, qreal y, qreal w, qreal h)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickContext2D7ellipseEdddd(
    QQuickContext2D *self,
    qreal x,
    qreal y,
    qreal w,
    qreal h) {
  self->ellipse(x, y, w, h);
}

//  void QQuickContext2D::text(const QString &str, qreal x, qreal y)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickContext2D4textERK7QStringdd(
    QQuickContext2D *self,
    const QString *str,
    qreal x,
    qreal y) {
  self->text(*str, x, y);
}

//  void QQuickContext2D::arc(qreal x, qreal y, qreal radius, qreal
//      startAngle, qreal endAngle, bool anticlockwise)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickContext2D3arcEdddddb(
    QQuickContext2D *self,
    qreal x,
    qreal y,
    qreal radius,
    qreal startAngle,
    qreal endAngle,
    bool anticlockwise) {
  self->arc(x, y, radius, startAngle, endAngle, anticlockwise);
}

//  void QQuickContext2D::addArcTo(const QPointF &p1, const QPointF &p2,
//      qreal radius)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickContext2D8addArcToERK7QPointFS2_d(
    QQuickContext2D *self,
    const QPointF *p1,
    const QPointF *p2,
    qreal radius) {
  self->addArcTo(*p1, *p2, radius);
}

//  QSurface *QQuickContext2D::surface() const
extern "C" Q_DECL_EXPORT
QSurface *ritual_ZNK15QQuickContext2D7surfaceEv(
    const QQuickContext2D *self) {
  return self->surface();
}

//  void QQuickContext2D::setGrabbedImage(const QImage &grab)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickContext2D15setGrabbedImageERK6QImage(
    QQuickContext2D *self,
    const QImage *grab) {
  self->setGrabbedImage(*grab);
}

//  a Python function taken by a CuteQQuickContext2D, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickContext2D(
    QQuickContext2D *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickContext2D *>(self)->take(key, call);
}

//  QImage QQuickContext2D::toImage(const QRectF &bounds)
extern "C" Q_DECL_EXPORT
QImage *ritual_own_ZN15QQuickContext2D7toImageERK6QRectF(
    QQuickContext2D *self,
    const QRectF *bounds) {
  return new QImage(self->QQuickContext2D::toImage(*bounds));
}

//  QV4::ReturnedValue QQuickContext2D::v4value() const
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_own_ZNK15QQuickContext2D7v4valueEv(
    const QQuickContext2D *self) {
  return self->QQuickContext2D::v4value();
}

//  QV4::ExecutionEngine *QQuickContext2D::v4Engine() const
extern "C" Q_DECL_EXPORT
QV4::ExecutionEngine *ritual_own_ZNK15QQuickContext2D8v4EngineEv(
    const QQuickContext2D *self) {
  return self->QQuickContext2D::v4Engine();
}

#endif  // QT_CONFIG(quick_canvas)
#endif  // QT_CONFIG(quick_canvas)
