//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgthreadedrenderloop_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/qglobal.h>
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(thread)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgthreadedrenderloop_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qimage.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/QMutex>
#include <QtCore/QWaitCondition>
#include <QtCore/QAnimationDriver>
#include <QtCore/QQueue>
#include <QtCore/QTimer>
#include <QtGui/QGuiApplication>
#include <QtGui/QScreen>
#include <QtGui/QOffscreenSurface>
#include <QtGui/qpa/qwindowsysteminterface.h>
#include <QtQuick/QQuickWindow>
#include <QtQuick/private/qquickwindow_p.h>
#include <QtQuick/private/qquickitem_p.h>
#include <QtGui/qpa/qplatformwindow_p.h>
#include <QtQuick/private/qsgrenderer_p.h>
#include <QtQuick/private/qsgthreadedrenderloop_p.h>
#include <QtQuick/private/qsgrhisupport_p.h>
#include <QtQuick/private/qquickanimatorcontroller_p.h>
#include <QtQuick/private/qquickprofiler_p.h>
#include <QtQml/private/qqmldebugserviceinterfaces_p.h>
#include <QtQml/private/qqmldebugconnector_p.h>
#include <QtQuick/private/qsgrhishadereffectnode_p.h>
#include <QtQuick/private/qsgdefaultrendercontext_p.h>
#ifdef Q_OS_DARWIN
#include <QtCore/private/qcore_mac_p.h>
#endif
#include <QtCore/qloggingcategory.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quick/scenegraph/qsgthreadedrenderloop.cpp, line 99, as local:qsgthreadedrenderloop.cpp:QSG_RT_PAD
#define QSG_RT_PAD "                    (RT) %s"

//  from ../qtdeclarative/src/quick/scenegraph/qsgthreadedrenderloop.cpp, line 116, as local:qsgthreadedrenderloop.cpp:WMWindowEvent
class WMWindowEvent : public QEvent
{
public:
    WMWindowEvent(QQuickWindow *c, QEvent::Type type) : QEvent(type), window(c) { }
    QQuickWindow *window;
};

//  from ../qtdeclarative/src/quick/scenegraph/qsgthreadedrenderloop.cpp, line 123, as local:qsgthreadedrenderloop.cpp:WMTryReleaseEvent
class WMTryReleaseEvent : public WMWindowEvent
{
public:
    WMTryReleaseEvent(QQuickWindow *win, bool destroy, bool needsFallbackSurface)
        : WMWindowEvent(win, QEvent::Type(WM_TryRelease))
        , inDestructor(destroy)
        , needsFallback(needsFallbackSurface)
    {}

    bool inDestructor;
    bool needsFallback;
};

//  from ../qtdeclarative/src/quick/scenegraph/qsgthreadedrenderloop.cpp, line 155, as local:qsgthreadedrenderloop.cpp:WMGrabEvent
class WMGrabEvent : public WMWindowEvent
{
public:
    WMGrabEvent(QQuickWindow *c, QImage *result) :
        WMWindowEvent(c, QEvent::Type(WM_Grab)), image(result) {}
    QImage *image;
};

//  from ../qtdeclarative/src/quick/scenegraph/qsgthreadedrenderloop.cpp, line 163, as local:qsgthreadedrenderloop.cpp:WMJobEvent
class WMJobEvent : public WMWindowEvent
{
public:
    WMJobEvent(QQuickWindow *c, QRunnable *postedJob)
        : WMWindowEvent(c, QEvent::Type(WM_PostJob)), job(postedJob) {}
    ~WMJobEvent() { delete job; }
    QRunnable *job;
};

//  from ../qtdeclarative/src/quick/scenegraph/qsgthreadedrenderloop.cpp, line 172, as local:qsgthreadedrenderloop.cpp:WMReleaseSwapchainEvent
class WMReleaseSwapchainEvent : public WMWindowEvent
{
public:
    WMReleaseSwapchainEvent(QQuickWindow *c) :
        WMWindowEvent(c, QEvent::Type(WM_ReleaseSwapchain)) { }
};

//  from ../qtdeclarative/src/quick/scenegraph/qsgthreadedrenderloop.cpp, line 179, as local:qsgthreadedrenderloop.cpp:QSGRenderThreadEventQueue
class QSGRenderThreadEventQueue : public QQueue<QEvent *>
{
public:
    QSGRenderThreadEventQueue()
        : waiting(false)
    {
    }

    void addEvent(QEvent *e) {
        mutex.lock();
        enqueue(e);
        if (waiting)
            condition.wakeOne();
        mutex.unlock();
    }

    QEvent *takeEvent(bool wait) {
        mutex.lock();
        if (size() == 0 && wait) {
            waiting = true;
            condition.wait(&mutex);
            waiting = false;
        }
        QEvent *e = dequeue();
        mutex.unlock();
        return e;
    }

    bool hasMoreEvents() {
        mutex.lock();
        bool has = !isEmpty();
        mutex.unlock();
        return has;
    }

private:
    QMutex mutex;
    QWaitCondition condition;
    bool waiting;
};

//  from ../qtdeclarative/src/quick/scenegraph/qsgthreadedrenderloop.cpp, line 221, as local:qsgthreadedrenderloop.cpp:QSGRenderThread
#if defined(Q_OS_LINUX)
class QSGRenderThread : public QThread
{
    Q_OBJECT
public:
    QSGRenderThread(QSGThreadedRenderLoop *w, QSGRenderContext *renderContext)
        : wm(w)
        , rhi(nullptr)
        , ownRhi(true)
        , offscreenSurface(nullptr)
        , animatorDriver(nullptr)
        , pendingUpdate(0)
        , sleeping(false)
        , active(false)
        , window(nullptr)
        , stopEventProcessing(false)
    {
        sgrc = static_cast<QSGDefaultRenderContext *>(renderContext);
#if defined(Q_OS_QNX) || defined(Q_OS_INTEGRITY)
        // The render thread requires a larger stack than the default (256k).
        setStackSize(1024 * 1024);
#endif
    }

    ~QSGRenderThread()
    {
        delete sgrc;
        delete offscreenSurface;
    }

    void invalidateGraphics(QQuickWindow *window, bool inDestructor);

    bool event(QEvent *) override;
    void run() override;

    void syncAndRender();
    void sync(bool inExpose);

    void requestRepaint()
    {
        if (sleeping)
            stopEventProcessing = true;
        if (window)
            pendingUpdate |= RepaintRequest;
    }

    void processEventsAndWaitForMore();
    void processEvents();
    void postEvent(QEvent *e);

public:
    enum {
        SyncRequest         = 0x01,
        RepaintRequest      = 0x02,
        ExposeRequest       = 0x04 | RepaintRequest | SyncRequest
    };

    void ensureRhi();
    void teardownGraphics();
    void handleDeviceLoss();

    QSGThreadedRenderLoop *wm;
    QRhi *rhi;
    bool ownRhi;
    QSGDefaultRenderContext *sgrc;
    QOffscreenSurface *offscreenSurface;

    QAnimationDriver *animatorDriver;

    uint pendingUpdate;
    bool sleeping;

    volatile bool active;

    QMutex mutex;
    QWaitCondition waitCondition;

    QElapsedTimer m_threadTimeBetweenRenders;

    QQuickWindow *window; // Will be 0 when window is not exposed
    QSize windowSize;
    float dpr = 1;
    QRhiSwapChainProxyData scProxyData;
    int rhiSampleCount = 1;
    bool rhiDeviceLost = false;
    bool rhiDoomed = false;
    bool guiNotifiedAboutRhiFailure = false;
    bool swRastFallbackDueToSwapchainFailure = false;

    // Local event queue stuff...
    bool stopEventProcessing;
    QSGRenderThreadEventQueue eventQueue;
};
#endif  // defined(Q_OS_LINUX)

//  from ../qtdeclarative/src/quick/scenegraph/qsgthreadedrenderloop.cpp, line 579, as local:qsgthreadedrenderloop.cpp:QSGRenderThread::teardownGraphics
inline void QSGRenderThread::teardownGraphics()
{
    QQuickWindowPrivate *wd = QQuickWindowPrivate::get(window);
    wd->cleanupNodesOnShutdown();
    sgrc->invalidate();
    wm->releaseSwapchain(window);
    if (ownRhi)
        QSGRhiSupport::instance()->destroyRhi(rhi, {});
    rhi = nullptr;
    wd->rhi = nullptr;
}

//  from ../qtdeclarative/src/quick/scenegraph/qsgthreadedrenderloop.cpp, line 591, as local:qsgthreadedrenderloop.cpp:QSGRenderThread::handleDeviceLoss
inline void QSGRenderThread::handleDeviceLoss()
{
    if (!rhi || !rhi->isDeviceLost())
        return;

    qWarning("Graphics device lost, cleaning up scenegraph and releasing RHI");
    teardownGraphics();
    rhiDeviceLost = true;
}

//  from ../qtdeclarative/src/quick/scenegraph/qsgthreadedrenderloop.cpp, line 849, as local:qsgthreadedrenderloop.cpp:QSGRenderThread::postEvent
inline void QSGRenderThread::postEvent(QEvent *e)
{
    eventQueue.addEvent(e);
}

//  from ../qtdeclarative/src/quick/scenegraph/qsgthreadedrenderloop.cpp, line 879, as local:qsgthreadedrenderloop.cpp:QSGRenderThread::ensureRhi
inline void QSGRenderThread::ensureRhi()
{
    if (!rhi) {
        if (rhiDoomed) // no repeated attempts if the initial attempt failed
            return;
        QSGRhiSupport *rhiSupport = QSGRhiSupport::instance();
        const bool forcePreferSwRenderer = swRastFallbackDueToSwapchainFailure;
        QSGRhiSupport::RhiCreateResult rhiResult = rhiSupport->createRhi(window, offscreenSurface, forcePreferSwRenderer);
        rhi = rhiResult.rhi;
        ownRhi = rhiResult.own;
        if (rhi) {
            rhiDeviceLost = false;
            rhiSampleCount = rhiSupport->chooseSampleCountForWindowWithRhi(window, rhi);
        } else {
            if (!rhiDeviceLost) {
                rhiDoomed = true;
                qWarning("Failed to create QRhi on the render thread; scenegraph is not functional");
            }
            // otherwise no error, will retry on a subsequent rendering attempt
            return;
        }
    }
    if (!sgrc->rhi() && windowSize.width() > 0 && windowSize.height() > 0) {
        // We need to guarantee that sceneGraphInitialized is emitted
        // with a context current, if running with OpenGL.
        rhi->makeThreadLocalNativeContextCurrent();
        QSGDefaultRenderContext::InitParams rcParams;
        rcParams.rhi = rhi;
        rcParams.sampleCount = rhiSampleCount;
        rcParams.initialSurfacePixelSize = windowSize * qreal(dpr);
        rcParams.maybeSurface = window;
        sgrc->initialize(&rcParams);
    }
    QQuickWindowPrivate *cd = QQuickWindowPrivate::get(window);
    if (rhi && !cd->swapchain) {
        cd->rhi = rhi;
        QRhiSwapChain::Flags flags = QRhiSwapChain::UsedAsTransferSource; // may be used in a grab
        const QSurfaceFormat requestedFormat = window->requestedFormat();

        // QQ is always premul alpha. Decide based on alphaBufferSize in
        // requestedFormat(). (the platform plugin can override format() but
        // what matters here is what the application wanted, hence using the
        // requested one)
        const bool alpha = requestedFormat.alphaBufferSize() > 0;
        if (alpha)
            flags |= QRhiSwapChain::SurfaceHasPreMulAlpha;

        // Request NoVSync if swap interval was set to 0 (either by the app or
        // by QSG_NO_VSYNC). What this means in practice is another question,
        // but at least we tried.
        if (requestedFormat.swapInterval() == 0) {
            qCDebug(QSG_LOG_INFO, "Swap interval is 0, attempting to disable vsync when presenting.");
            flags |= QRhiSwapChain::NoVSync;
        }

        cd->swapchain = rhi->newSwapChain();
        static bool depthBufferEnabled = qEnvironmentVariableIsEmpty("QSG_NO_DEPTH_BUFFER");
        if (depthBufferEnabled) {
            cd->depthStencilForSwapchain = rhi->newRenderBuffer(QRhiRenderBuffer::DepthStencil,
                                                                QSize(),
                                                                rhiSampleCount,
                                                                QRhiRenderBuffer::UsedWithSwapChainOnly);
            cd->swapchain->setDepthStencil(cd->depthStencilForSwapchain);
        }
        cd->swapchain->setWindow(window);
        cd->swapchain->setProxyData(scProxyData);
        QSGRhiSupport::instance()->applySwapChainFormat(cd->swapchain, window);
        qCDebug(QSG_LOG_INFO, "MSAA sample count for the swapchain is %d. Alpha channel requested = %s.",
                rhiSampleCount, alpha ? "yes" : "no");
        cd->swapchain->setSampleCount(rhiSampleCount);
        cd->swapchain->setFlags(flags);
        cd->rpDescForSwapchain = cd->swapchain->newCompatibleRenderPassDescriptor();
        cd->swapchain->setRenderPassDescriptor(cd->rpDescForSwapchain);
    }
}

//  from ../qtdeclarative/src/quick/scenegraph/qsgthreadedrenderloop.cpp, line 1378, as _ZN21QSGThreadedRenderLoop11eventFilterEP7QObjectP6QEvent
inline bool QSGThreadedRenderLoop::eventFilter(QObject *watched, QEvent *event)
{
    switch (event->type()) {
    case QEvent::PlatformSurface:
        // this is the proper time to tear down the swapchain (while the native window and surface are still around)
        if (static_cast<QPlatformSurfaceEvent *>(event)->surfaceEventType() == QPlatformSurfaceEvent::SurfaceAboutToBeDestroyed) {
            QQuickWindow *window = qobject_cast<QQuickWindow *>(watched);
            if (window) {
                Window *w = windowFor(window);
                if (w && w->thread->isRunning()) {
                    w->thread->mutex.lock();
                    w->thread->postEvent(new WMReleaseSwapchainEvent(window));
                    w->thread->waitCondition.wait(&w->thread->mutex);
                    w->thread->mutex.unlock();
                }
            }
            // keep this filter on the window - needed for uncommon but valid
            // sequences of calls like window->destroy(); window->show();
        }
        break;
    default:
        break;
    }
    return QObject::eventFilter(watched, event);
}

//  from ../qtdeclarative/src/quick/scenegraph/qsgcontext.cpp, line 50, as _Z18QSG_LOG_RENDERLOOPv
inline const QLoggingCategory &QSG_LOG_RENDERLOOP()
{
    static const QLoggingCategory category("qt.scenegraph.renderloop");
    return category;
}

//  from ../qtdeclarative/src/quick/scenegraph/qsgthreadedrenderloop.cpp, line 1151, as _ZN21QSGThreadedRenderLoop4hideEP12QQuickWindow
inline void QSGThreadedRenderLoop::hide(QQuickWindow *window)
{
    qCDebug(QSG_LOG_RENDERLOOP) << "hide()" << window;

    if (window->isExposed())
        handleObscurity(windowFor(window));

    releaseResources(window);
}

//  from ../qtdeclarative/src/quick/scenegraph/qsgthreadedrenderloop.cpp, line 1161, as _ZN21QSGThreadedRenderLoop6resizeEP12QQuickWindow
inline void QSGThreadedRenderLoop::resize(QQuickWindow *window)
{
    qCDebug(QSG_LOG_RENDERLOOP) << "resize()" << window;

    Window *w = windowFor(window);
    if (!w)
        return;

    w->psTimeAccumulator = 0.0f;
    w->psTimeSampleCount = 0;
}

//  from ../qtdeclarative/src/quick/scenegraph/qsgthreadedrenderloop.cpp, line 1178, as _ZN21QSGThreadedRenderLoop15windowDestroyedEP12QQuickWindow
inline void QSGThreadedRenderLoop::windowDestroyed(QQuickWindow *window)
{
    qCDebug(QSG_LOG_RENDERLOOP) << "begin windowDestroyed()" << window;

    Window *w = windowFor(window);
    if (!w)
        return;

    handleObscurity(w);
    releaseResources(w, true);

    QSGRenderThread *thread = w->thread;
    while (thread->isRunning())
        QThread::yieldCurrentThread();
    Q_ASSERT(thread->thread() == QThread::currentThread());
    delete thread;

    for (int i=0; i<m_windows.size(); ++i) {
        if (m_windows.at(i).window == window) {
            m_windows.removeAt(i);
            break;
        }
    }

    // Now that we altered the window list, we may need to stop the animation
    // timer even if we didn't via handleObscurity. This covers the case where
    // we destroy a visible & exposed QQuickWindow.
    startOrStopAnimationTimer();

    qCDebug(QSG_LOG_RENDERLOOP) << "done windowDestroyed()" << window;
}

//  from ../qtdeclarative/src/quick/scenegraph/qsgthreadedrenderloop.cpp, line 1222, as _ZN21QSGThreadedRenderLoop15exposureChangedEP12QQuickWindow
inline void QSGThreadedRenderLoop::exposureChanged(QQuickWindow *window)
{
    qCDebug(QSG_LOG_RENDERLOOP) << "exposureChanged()" << window;

    // This is tricker than used to be. We want to detect having an empty
    // surface size (which may be the case even when window->size() is
    // non-empty, on some platforms with some graphics APIs!) as well as the
    // case when the window just became "newly exposed" (e.g. after a
    // minimize-restore on Windows, or when switching between fully obscured -
    // not fully obscured on macOS)
    QQuickWindowPrivate *wd = QQuickWindowPrivate::get(window);
    if (!window->isExposed())
        wd->hasRenderableSwapchain = false;

    bool skipThisExpose = false;
    if (window->isExposed() && wd->hasActiveSwapchain && wd->swapchain->surfacePixelSize().isEmpty()) {
        wd->hasRenderableSwapchain = false;
        skipThisExpose = true;
    }

    if (window->isExposed() && !wd->hasRenderableSwapchain && wd->hasActiveSwapchain
            && !wd->swapchain->surfacePixelSize().isEmpty())
    {
        wd->hasRenderableSwapchain = true;
        wd->swapchainJustBecameRenderable = true;
    }

    if (window->isExposed()) {
        if (!skipThisExpose)
            handleExposure(window);
    } else {
        Window *w = windowFor(window);
        if (w)
            handleObscurity(w);
    }
}

//  from ../qtdeclarative/src/quick/scenegraph/qsgthreadedrenderloop.cpp, line 1793, as _ZN21QSGThreadedRenderLoop4grabEP12QQuickWindow
inline QImage QSGThreadedRenderLoop::grab(QQuickWindow *window)
{
    qCDebug(QSG_LOG_RENDERLOOP) << "grab()" << window;

    Window *w = windowFor(window);
    Q_ASSERT(w);

    if (!w->thread->isRunning())
        return QImage();

    if (!window->handle())
        window->create();

    qCDebug(QSG_LOG_RENDERLOOP, "- polishing items");
    QQuickWindowPrivate *d = QQuickWindowPrivate::get(window);
    m_inPolish = true;
    d->polishItems();
    m_inPolish = false;

    QImage result;
    w->thread->mutex.lock();
    m_lockedForSync = true;
    qCDebug(QSG_LOG_RENDERLOOP, "- posting grab event");
    w->thread->postEvent(new WMGrabEvent(window, &result));
    w->thread->waitCondition.wait(&w->thread->mutex);
    m_lockedForSync = false;
    w->thread->mutex.unlock();

    qCDebug(QSG_LOG_RENDERLOOP, "- grab complete");

    return result;
}

//  from ../qtdeclarative/src/quick/scenegraph/qsgthreadedrenderloop.cpp, line 1468, as _ZN21QSGThreadedRenderLoop6updateEP12QQuickWindow
inline void QSGThreadedRenderLoop::update(QQuickWindow *window)
{
    Window *w = windowFor(window);
    if (!w)
        return;

    const bool isRenderThread = QThread::currentThread() == w->thread;

    if (QPlatformWindow *platformWindow = window->handle()) {
        // If the window is being resized we don't want to schedule unthrottled
        // updates on the render thread, as this will starve the main thread
        // from getting drawables for displaying the updated window size.
        if (isRenderThread && !platformWindow->allowsIndependentThreadedRendering()) {
            // In most cases the window will already have update requested
            // due to the animator triggering a sync, but just in case we
            // schedule an update request on the main thread explicitly.
            qCDebug(QSG_LOG_RENDERLOOP) << "window is resizing. update on window" << w->window;
            QTimer::singleShot(0, window, &QWindow::requestUpdate);
            return;
        }
    }

    if (isRenderThread) {
       qCDebug(QSG_LOG_RENDERLOOP) << "update on window - on render thread" << w->window;
       w->thread->requestRepaint();
       return;
    }

    qCDebug(QSG_LOG_RENDERLOOP) << "update on window" << w->window;
    // We set forceRenderPass because we want to make sure the QQuickWindow
    // actually does a full render pass after the next sync.
    w->forceRenderPass = true;
    maybeUpdate(w);
}

//  from ../qtdeclarative/src/quick/scenegraph/qsgthreadedrenderloop.cpp, line 1404, as _ZN21QSGThreadedRenderLoop19handleUpdateRequestEP12QQuickWindow
inline void QSGThreadedRenderLoop::handleUpdateRequest(QQuickWindow *window)
{
    qCDebug(QSG_LOG_RENDERLOOP) <<  "- update request" << window;
    if (!QQuickWindowPrivate::get(window)->updatesEnabled) {
        qCDebug(QSG_LOG_RENDERLOOP, "- updatesEnabled is false, abort");
        return;
    }
    Window *w = windowFor(window);
    if (w)
        polishAndSync(w);
}

//  from ../qtdeclarative/src/quick/scenegraph/qsgthreadedrenderloop.cpp, line 1046, as _ZNK21QSGThreadedRenderLoop17sceneGraphContextEv
inline QSGContext *QSGThreadedRenderLoop::sceneGraphContext() const
{
    return sg;
}

//  from ../qtdeclarative/src/quick/scenegraph/qsgthreadedrenderloop.cpp, line 1029, as _ZNK21QSGThreadedRenderLoop19createRenderContextEP10QSGContext
inline QSGRenderContext *QSGThreadedRenderLoop::createRenderContext(QSGContext *sg) const
{
    auto context = sg->createRenderContext();
    pendingRenderContexts.insert(context);
    return context;
}

//  from ../qtdeclarative/src/quick/scenegraph/qsgthreadedrenderloop.cpp, line 1041, as _ZNK21QSGThreadedRenderLoop15animationDriverEv
inline QAnimationDriver *QSGThreadedRenderLoop::animationDriver() const
{
    return m_animation_driver;
}

//  from ../qtdeclarative/src/quick/scenegraph/qsgthreadedrenderloop.cpp, line 1504, as _ZN21QSGThreadedRenderLoop16releaseResourcesEP12QQuickWindow
inline void QSGThreadedRenderLoop::releaseResources(QQuickWindow *window)
{
    Window *w = windowFor(window);
    if (w)
        releaseResources(w, false);
}

//  from ../qtdeclarative/src/quick/scenegraph/qsgthreadedrenderloop.cpp, line 1758, as _ZN21QSGThreadedRenderLoop5eventEP6QEvent
inline bool QSGThreadedRenderLoop::event(QEvent *e)
{
    switch ((int) e->type()) {

    case QEvent::Timer: {
        Q_ASSERT(sg->isVSyncDependent(m_animation_driver));
        QTimerEvent *te = static_cast<QTimerEvent *>(e);
        if (te->timerId() == m_animation_timer) {
            qCDebug(QSG_LOG_RENDERLOOP, "- ticking non-render thread timer");
            m_animation_driver->advance();
            emit timeToIncubate();
            return true;
        }
        break;
    }

    default:
        break;
    }

    return QObject::event(e);
}

//  from ../qtdeclarative/src/quick/scenegraph/qsgthreadedrenderloop.cpp, line 1830, as _ZN21QSGThreadedRenderLoop7postJobEP12QQuickWindowP9QRunnable
inline void QSGThreadedRenderLoop::postJob(QQuickWindow *window, QRunnable *job)
{
    Window *w = windowFor(window);
    if (w && w->thread && w->thread->window)
        w->thread->postEvent(new WMJobEvent(window, job));
    else
        delete job;
}

//  from ../qtdeclarative/src/quick/scenegraph/qsgthreadedrenderloop.cpp, line 1061, as _ZNK21QSGThreadedRenderLoop20interleaveIncubationEv
inline bool QSGThreadedRenderLoop::interleaveIncubation() const
{
    return m_animation_driver->isRunning() && anyoneShowing();
}

//  from ../qtdeclarative/src/quick/scenegraph/qsgthreadedrenderloop.cpp, line 1359, as _ZN21QSGThreadedRenderLoop15handleObscurityEPNS_6WindowE
inline void QSGThreadedRenderLoop::handleObscurity(Window *w)
{
    if (!w)
        return;

    qCDebug(QSG_LOG_RENDERLOOP) << "handleObscurity()" << w->window;
    if (w->thread->isRunning()) {
        if (!QQuickWindowPrivate::get(w->window)->updatesEnabled) {
            qCDebug(QSG_LOG_RENDERLOOP, "- updatesEnabled is false, abort");
            return;
        }
        w->thread->mutex.lock();
        w->thread->postEvent(new WMWindowEvent(w->window, QEvent::Type(WM_Obscure)));
        w->thread->waitCondition.wait(&w->thread->mutex);
        w->thread->mutex.unlock();
    }
    startOrStopAnimationTimer();
}

//  from ../qtdeclarative/src/quick/scenegraph/qsgthreadedrenderloop.cpp, line 1515, as _ZN21QSGThreadedRenderLoop16releaseResourcesEPNS_6WindowEb
inline void QSGThreadedRenderLoop::releaseResources(Window *w, bool inDestructor)
{
    qCDebug(QSG_LOG_RENDERLOOP) << "releaseResources()" << (inDestructor ? "in destructor" : "in api-call") << w->window;

    w->thread->mutex.lock();
    if (w->thread->isRunning() && w->thread->active) {
        QQuickWindow *window = w->window;

        // The platform window might have been destroyed before
        // hide/release/windowDestroyed is called, so we may need to have a
        // fallback surface to perform the cleanup of the scene graph and the
        // RHI resources.

        qCDebug(QSG_LOG_RENDERLOOP, "- posting release request to render thread");
        w->thread->postEvent(new WMTryReleaseEvent(window, inDestructor, window->handle() == nullptr));
        w->thread->waitCondition.wait(&w->thread->mutex);

        // Avoid a shutdown race condition.
        // If SG is invalidated and 'active' becomes false, the thread's run()
        // method will exit. handleExposure() relies on QThread::isRunning() (because it
        // potentially needs to start the thread again) and our mutex cannot be used to
        // track the thread stopping, so we wait a few nanoseconds extra so the thread
        // can exit properly.
        if (!w->thread->active) {
            qCDebug(QSG_LOG_RENDERLOOP) << " - waiting for render thread to exit" << w->window;
            w->thread->wait();
            qCDebug(QSG_LOG_RENDERLOOP) << " - render thread finished" << w->window;
        }
    }
    w->thread->mutex.unlock();
}

//  from ../qtdeclarative/src/quick/scenegraph/qsgthreadedrenderloop.cpp, line 1263, as _ZN21QSGThreadedRenderLoop14handleExposureEP12QQuickWindow
inline void QSGThreadedRenderLoop::handleExposure(QQuickWindow *window)
{
    qCDebug(QSG_LOG_RENDERLOOP) << "handleExposure()" << window;

    Window *w = windowFor(window);
    if (!w) {
        qCDebug(QSG_LOG_RENDERLOOP, "- adding window to list");
        Window win;
        win.window = window;
        win.actualWindowFormat = window->format();
        auto renderContext = QQuickWindowPrivate::get(window)->context;
        // The thread assumes ownership, so we don't need to delete it later.
        pendingRenderContexts.remove(renderContext);
        win.thread = new QSGRenderThread(this, renderContext);
        win.updateDuringSync = false;
        win.forceRenderPass = true; // also covered by polishAndSync(inExpose=true), but doesn't hurt
        win.badVSync = false;
        win.timeBetweenPolishAndSyncs.start();
        win.psTimeAccumulator = 0.0f;
        win.psTimeSampleCount = 0;
        m_windows << win;
        w = &m_windows.last();
    } else {
        if (!QQuickWindowPrivate::get(window)->updatesEnabled) {
            qCDebug(QSG_LOG_RENDERLOOP, "- updatesEnabled is false, abort");
            return;
        }
    }

#ifndef QT_NO_DEBUG
    if (w->window->width() <= 0 || w->window->height() <= 0
        || (w->window->isTopLevel() && !w->window->geometry().intersects(w->window->screen()->availableGeometry()))) {
        qWarning().noquote().nospace() << "QSGThreadedRenderLoop: expose event received for window "
            << w->window << " with invalid geometry: " << w->window->geometry()
            << " on " << w->window->screen();
    }
#endif

    // Because we are going to bind a GL context to it, make sure it
    // is created.
    if (!w->window->handle())
        w->window->create();

    // Start render thread if it is not running
    if (!w->thread->isRunning()) {
        qCDebug(QSG_LOG_RENDERLOOP, "- starting render thread");

        // set this early as we'll be rendering shortly anyway and this avoids
        // specialcasing exposure in polishAndSync.
        w->thread->window = window;

        if (!w->thread->rhi) {
            QSGRhiSupport *rhiSupport = QSGRhiSupport::instance();
            if (!w->thread->offscreenSurface)
                w->thread->offscreenSurface = rhiSupport->maybeCreateOffscreenSurface(window);
            w->thread->scProxyData = QRhi::updateSwapChainProxyData(rhiSupport->rhiBackend(), window);
            window->installEventFilter(this);
        }

        QQuickAnimatorController *controller
                = QQuickWindowPrivate::get(w->window)->animationController.get();
        if (controller->thread() != w->thread)
            controller->moveToThread(w->thread);

        w->thread->active = true;
        if (w->thread->thread() == QThread::currentThread()) {
            w->thread->sgrc->moveToThread(w->thread);
            w->thread->moveToThread(w->thread);
        }
        w->thread->start();
        if (!w->thread->isRunning())
            qFatal("Render thread failed to start, aborting application.");

    } else {
        qCDebug(QSG_LOG_RENDERLOOP, "- render thread already running");

        // set w->thread->window here too, but using an event so it's thread-safe
        w->thread->mutex.lock();
        w->thread->postEvent(new WMWindowEvent(w->window, QEvent::Type(WM_Exposed)));
        w->thread->waitCondition.wait(&w->thread->mutex);
        w->thread->mutex.unlock();
    }

    polishAndSync(w, true);
    qCDebug(QSG_LOG_RENDERLOOP, "- done with handleExposure()");

    startOrStopAnimationTimer();
}

//  from ../qtdeclarative/src/quick/scenegraph/qsgthreadedrenderloop.cpp, line 1023, as _ZN21QSGThreadedRenderLoopD1Ev
inline QSGThreadedRenderLoop::~QSGThreadedRenderLoop()
{
    qDeleteAll(pendingRenderContexts);
    delete sg;
}

//  from ../qtdeclarative/src/quick/scenegraph/qsgthreadedrenderloop.cpp, line 107, as _ZN21QSGThreadedRenderLoop9windowForEP12QQuickWindow
inline QSGThreadedRenderLoop::Window *QSGThreadedRenderLoop::windowFor(QQuickWindow *window)
{
    for (const auto &t : std::as_const(m_windows)) {
        if (t.window == window)
            return const_cast<Window *>(&t);
    }
    return nullptr;
}

//  from ../qtdeclarative/src/quick/scenegraph/qsgthreadedrenderloop.cpp, line 1051, as _ZNK21QSGThreadedRenderLoop13anyoneShowingEv
inline bool QSGThreadedRenderLoop::anyoneShowing() const
{
    for (int i=0; i<m_windows.size(); ++i) {
        QQuickWindow *c = m_windows.at(i).window;
        if (c->isVisible() && c->isExposed())
            return true;
    }
    return false;
}

//  from ../qtdeclarative/src/quick/scenegraph/qsgthreadedrenderloop.cpp, line 1082, as _ZN21QSGThreadedRenderLoop25startOrStopAnimationTimerEv
inline void QSGThreadedRenderLoop::startOrStopAnimationTimer()
{
    if (!sg->isVSyncDependent(m_animation_driver))
        return;

    int exposedWindows = 0;
    int unthrottledWindows = 0;
    int badVSync = 0;
    const Window *theOne = nullptr;
    for (int i=0; i<m_windows.size(); ++i) {
        const Window &w = m_windows.at(i);
        if (w.window->isVisible() && w.window->isExposed()) {
            ++exposedWindows;
            theOne = &w;
            if (w.actualWindowFormat.swapInterval() == 0)
                ++unthrottledWindows;
            if (w.badVSync)
                ++badVSync;
        }
    }

    // Best case: with 1 exposed windows we can advance regular animations in
    // polishAndSync() and rely on being throttled to vsync. (no normal system
    // timer needed)
    //
    // Special case: with no windows exposed (e.g. on Windows: all of them are
    // minimized) run a normal system timer to make non-visual animation
    // functional still.
    //
    // Not so ideal case: with more than one window exposed we have to use the
    // same path as the no-windows case since polishAndSync() is now called
    // potentially for multiple windows over time so it cannot take care of
    // advancing the animation driver anymore.
    //
    // On top, another case: a window with vsync disabled should disable all the
    // good stuff and go with the system timer.
    //
    // Similarly, if there is at least one window where we determined that
    // vsync based blocking is not working as expected, that should make us
    // choose the timer based way.

    const bool canUseVSyncBasedAnimation = exposedWindows == 1 && unthrottledWindows == 0 && badVSync == 0;

    if (m_animation_timer != 0 && (canUseVSyncBasedAnimation || !m_animation_driver->isRunning())) {
        qCDebug(QSG_LOG_RENDERLOOP, "*** Stopping system (not vsync-based) animation timer (exposedWindows=%d unthrottledWindows=%d badVSync=%d)",
                exposedWindows, unthrottledWindows, badVSync);
        killTimer(m_animation_timer);
        m_animation_timer = 0;
        // If animations are running, make sure we keep on animating
        if (m_animation_driver->isRunning())
            postUpdateRequest(const_cast<Window *>(theOne));
    } else if (m_animation_timer == 0 && !canUseVSyncBasedAnimation && m_animation_driver->isRunning()) {
        qCDebug(QSG_LOG_RENDERLOOP, "*** Starting system (not vsync-based) animation timer (exposedWindows=%d unthrottledWindows=%d badVSync=%d)",
                exposedWindows, unthrottledWindows, badVSync);
        m_animation_timer = startTimer(int(sg->vsyncIntervalForAnimationDriver(m_animation_driver)));
    }
}

//  from ../qtdeclarative/src/quick/scenegraph/qsgthreadedrenderloop.cpp, line 1036, as _ZN21QSGThreadedRenderLoop17postUpdateRequestEPNS_6WindowE
inline void QSGThreadedRenderLoop::postUpdateRequest(Window *w)
{
    w->window->requestUpdate();
}

//  from ../qtdeclarative/src/quick/scenegraph/qsgthreadedrenderloop.cpp, line 1210, as _ZN21QSGThreadedRenderLoop16releaseSwapchainEP12QQuickWindow
inline void QSGThreadedRenderLoop::releaseSwapchain(QQuickWindow *window)
{
    QQuickWindowPrivate *wd = QQuickWindowPrivate::get(window);
    delete wd->rpDescForSwapchain;
    wd->rpDescForSwapchain = nullptr;
    delete wd->swapchain;
    wd->swapchain = nullptr;
    delete wd->depthStencilForSwapchain;
    wd->depthStencilForSwapchain = nullptr;
    wd->hasActiveSwapchain = wd->hasRenderableSwapchain = wd->swapchainJustBecameRenderable = false;
}
//  -----------------------------------------------------------------------

//  A QSGThreadedRenderLoop that Python can take functions over in. Every QSGThreadedRenderLoop
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQSGThreadedRenderLoopCall0)(const void *, QQuickWindow *, int *);
typedef void (*CuteQSGThreadedRenderLoopCall1)(const void *, QQuickWindow *, int *);
typedef void (*CuteQSGThreadedRenderLoopCall2)(const void *, QQuickWindow *, int *);
typedef void (*CuteQSGThreadedRenderLoopCall3)(const void *, QQuickWindow *, int *);
typedef void (*CuteQSGThreadedRenderLoopCall4)(const void *, QQuickWindow *, int *);
typedef const QImage * (*CuteQSGThreadedRenderLoopCall5)(const void *, QQuickWindow *, int *);
typedef void (*CuteQSGThreadedRenderLoopCall6)(const void *, QQuickWindow *, int *);
typedef void (*CuteQSGThreadedRenderLoopCall7)(const void *, QQuickWindow *, int *);
typedef void (*CuteQSGThreadedRenderLoopCall8)(const void *, QQuickWindow *, int *);
typedef void * (*CuteQSGThreadedRenderLoopCall9)(const void *, int *);
typedef void * (*CuteQSGThreadedRenderLoopCall10)(const void *, QSGContext *, int *);
typedef void * (*CuteQSGThreadedRenderLoopCall11)(const void *, int *);
typedef void (*CuteQSGThreadedRenderLoopCall12)(const void *, QQuickWindow *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSGThreadedRenderLoopCall13)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGThreadedRenderLoopCall14)(const void *, QQuickWindow *, QRunnable *, int *);
typedef bool (*CuteQSGThreadedRenderLoopCall15)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSGThreadedRenderLoopCall16)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef int (*CuteQSGThreadedRenderLoopCall17)(const void *, int *);
typedef int (*CuteQSGThreadedRenderLoopCall18)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGThreadedRenderLoopCall19)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGThreadedRenderLoopCall20)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGThreadedRenderLoopCall21)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGThreadedRenderLoopCall22)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGThreadedRenderLoopCall23)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQSGThreadedRenderLoop : public QSGThreadedRenderLoop {
public:
  using QSGThreadedRenderLoop::QSGThreadedRenderLoop;
  void *taken[24] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN13QSGRenderLoop4showEP12QQuickWindow")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QSGRenderLoop4hideEP12QQuickWindow")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QSGRenderLoop6resizeEP12QQuickWindow")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QSGRenderLoop15windowDestroyedEP12QQuickWindow")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QSGRenderLoop15exposureChangedEP12QQuickWindow")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QSGRenderLoop4grabEP12QQuickWindow")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QSGRenderLoop6updateEP12QQuickWindow")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QSGRenderLoop11maybeUpdateEP12QQuickWindow")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QSGRenderLoop19handleUpdateRequestEP12QQuickWindow")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK13QSGRenderLoop17sceneGraphContextEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK13QSGRenderLoop19createRenderContextEP10QSGContext")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK13QSGRenderLoop15animationDriverEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QSGRenderLoop16releaseResourcesEP12QQuickWindow")) {
      taken[12] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[13] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN13QSGRenderLoop7postJobEP12QQuickWindowP9QRunnable")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK13QSGRenderLoop20interleaveIncubationEv")) {
      taken[15] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[16] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZNK13QSGRenderLoop17windowSurfaceTypeEv")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK13QSGRenderLoop5flagsEv")) {
      taken[18] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[19] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[20] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[21] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[22] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[23] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QSGThreadedRenderLoop::show(QQuickWindow *a0)
  void show(QQuickWindow *a0) override {
    if (taken[0]) {
      int handled = 0;
      CuteQSGThreadedRenderLoopCall0 call = reinterpret_cast<CuteQSGThreadedRenderLoopCall0>(taken[0]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QSGThreadedRenderLoop::show(a0);
  }

  //  void QSGThreadedRenderLoop::hide(QQuickWindow *a0)
  void hide(QQuickWindow *a0) override {
    if (taken[1]) {
      int handled = 0;
      CuteQSGThreadedRenderLoopCall1 call = reinterpret_cast<CuteQSGThreadedRenderLoopCall1>(taken[1]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QSGThreadedRenderLoop::hide(a0);
  }

  //  void QSGThreadedRenderLoop::resize(QQuickWindow *window)
  void resize(QQuickWindow *window) override {
    if (taken[2]) {
      int handled = 0;
      CuteQSGThreadedRenderLoopCall2 call = reinterpret_cast<CuteQSGThreadedRenderLoopCall2>(taken[2]);
      call(this, window, &handled);
      if (handled) return;
    }
    QSGThreadedRenderLoop::resize(window);
  }

  //  void QSGThreadedRenderLoop::windowDestroyed(QQuickWindow *window)
  void windowDestroyed(QQuickWindow *window) override {
    if (taken[3]) {
      int handled = 0;
      CuteQSGThreadedRenderLoopCall3 call = reinterpret_cast<CuteQSGThreadedRenderLoopCall3>(taken[3]);
      call(this, window, &handled);
      if (handled) return;
    }
    QSGThreadedRenderLoop::windowDestroyed(window);
  }

  //  void QSGThreadedRenderLoop::exposureChanged(QQuickWindow *window)
  void exposureChanged(QQuickWindow *window) override {
    if (taken[4]) {
      int handled = 0;
      CuteQSGThreadedRenderLoopCall4 call = reinterpret_cast<CuteQSGThreadedRenderLoopCall4>(taken[4]);
      call(this, window, &handled);
      if (handled) return;
    }
    QSGThreadedRenderLoop::exposureChanged(window);
  }

  //  QImage QSGThreadedRenderLoop::grab(QQuickWindow *a0)
  QImage grab(QQuickWindow *a0) override {
    if (taken[5]) {
      int handled = 0;
      CuteQSGThreadedRenderLoopCall5 call = reinterpret_cast<CuteQSGThreadedRenderLoopCall5>(taken[5]);
      const QImage * given = call(this, a0, &handled);
      if (handled && given) return *given;
    }
    return QSGThreadedRenderLoop::grab(a0);
  }

  //  void QSGThreadedRenderLoop::update(QQuickWindow *window)
  void update(QQuickWindow *window) override {
    if (taken[6]) {
      int handled = 0;
      CuteQSGThreadedRenderLoopCall6 call = reinterpret_cast<CuteQSGThreadedRenderLoopCall6>(taken[6]);
      call(this, window, &handled);
      if (handled) return;
    }
    QSGThreadedRenderLoop::update(window);
  }

  //  void QSGThreadedRenderLoop::maybeUpdate(QQuickWindow *window)
  void maybeUpdate(QQuickWindow *window) override {
    if (taken[7]) {
      int handled = 0;
      CuteQSGThreadedRenderLoopCall7 call = reinterpret_cast<CuteQSGThreadedRenderLoopCall7>(taken[7]);
      call(this, window, &handled);
      if (handled) return;
    }
    QSGThreadedRenderLoop::maybeUpdate(window);
  }

  //  void QSGThreadedRenderLoop::handleUpdateRequest(QQuickWindow *window)
  void handleUpdateRequest(QQuickWindow *window) override {
    if (taken[8]) {
      int handled = 0;
      CuteQSGThreadedRenderLoopCall8 call = reinterpret_cast<CuteQSGThreadedRenderLoopCall8>(taken[8]);
      call(this, window, &handled);
      if (handled) return;
    }
    QSGThreadedRenderLoop::handleUpdateRequest(window);
  }

  //  QSGContext *QSGThreadedRenderLoop::sceneGraphContext() const
  QSGContext *sceneGraphContext() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQSGThreadedRenderLoopCall9 call = reinterpret_cast<CuteQSGThreadedRenderLoopCall9>(taken[9]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGContext *>(given);
    }
    return QSGThreadedRenderLoop::sceneGraphContext();
  }

  //  QSGRenderContext
  //      *QSGThreadedRenderLoop::createRenderContext(QSGContext *a0) const
  QSGRenderContext *createRenderContext(QSGContext *a0) const override {
    if (taken[10]) {
      int handled = 0;
      CuteQSGThreadedRenderLoopCall10 call = reinterpret_cast<CuteQSGThreadedRenderLoopCall10>(taken[10]);
      void * given = call(this, a0, &handled);
      if (handled) return static_cast<QSGRenderContext *>(given);
    }
    return QSGThreadedRenderLoop::createRenderContext(a0);
  }

  //  QAnimationDriver *QSGThreadedRenderLoop::animationDriver() const
  QAnimationDriver *animationDriver() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQSGThreadedRenderLoopCall11 call = reinterpret_cast<CuteQSGThreadedRenderLoopCall11>(taken[11]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAnimationDriver *>(given);
    }
    return QSGThreadedRenderLoop::animationDriver();
  }

  //  void QSGThreadedRenderLoop::releaseResources(QQuickWindow *window)
  void releaseResources(QQuickWindow *window) override {
    if (taken[12]) {
      int handled = 0;
      CuteQSGThreadedRenderLoopCall12 call = reinterpret_cast<CuteQSGThreadedRenderLoopCall12>(taken[12]);
      call(this, window, &handled);
      if (handled) return;
    }
    QSGThreadedRenderLoop::releaseResources(window);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QSGThreadedRenderLoop::event(QEvent *a0)
  bool event(QEvent *a0) override {
    if (taken[13]) {
      int handled = 0;
      CuteQSGThreadedRenderLoopCall13 call = reinterpret_cast<CuteQSGThreadedRenderLoopCall13>(taken[13]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QSGThreadedRenderLoop::event(a0);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QSGThreadedRenderLoop::postJob(QQuickWindow *window, QRunnable
  //      *job)
  void postJob(QQuickWindow *window, QRunnable *job) override {
    if (taken[14]) {
      int handled = 0;
      CuteQSGThreadedRenderLoopCall14 call = reinterpret_cast<CuteQSGThreadedRenderLoopCall14>(taken[14]);
      call(this, window, job, &handled);
      if (handled) return;
    }
    QSGThreadedRenderLoop::postJob(window, job);
  }

  //  bool QSGThreadedRenderLoop::interleaveIncubation() const
  bool interleaveIncubation() const override {
    if (taken[15]) {
      int handled = 0;
      CuteQSGThreadedRenderLoopCall15 call = reinterpret_cast<CuteQSGThreadedRenderLoopCall15>(taken[15]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSGThreadedRenderLoop::interleaveIncubation();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QSGThreadedRenderLoop::eventFilter(QObject *watched, QEvent
  //      *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQSGThreadedRenderLoopCall16 call = reinterpret_cast<CuteQSGThreadedRenderLoopCall16>(taken[16]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QSGThreadedRenderLoop::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  QSurface::SurfaceType QSGRenderLoop::windowSurfaceType() const
  QSurface::SurfaceType windowSurfaceType() const override {
    if (taken[17]) {
      int handled = 0;
      CuteQSGThreadedRenderLoopCall17 call = reinterpret_cast<CuteQSGThreadedRenderLoopCall17>(taken[17]);
      int given = call(this, &handled);
      if (handled) return static_cast<QSurface::SurfaceType>(given);
    }
    return QSGRenderLoop::windowSurfaceType();
  }

  //  int QSGRenderLoop::flags() const
  int flags() const override {
    if (taken[18]) {
      int handled = 0;
      CuteQSGThreadedRenderLoopCall18 call = reinterpret_cast<CuteQSGThreadedRenderLoopCall18>(taken[18]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QSGRenderLoop::flags();
  }

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQSGThreadedRenderLoopCall19 call = reinterpret_cast<CuteQSGThreadedRenderLoopCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQSGThreadedRenderLoopCall20 call = reinterpret_cast<CuteQSGThreadedRenderLoopCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQSGThreadedRenderLoopCall21 call = reinterpret_cast<CuteQSGThreadedRenderLoopCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[22]) {
      int handled = 0;
      CuteQSGThreadedRenderLoopCall22 call = reinterpret_cast<CuteQSGThreadedRenderLoopCall22>(taken[22]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[23]) {
      int handled = 0;
      CuteQSGThreadedRenderLoopCall23 call = reinterpret_cast<CuteQSGThreadedRenderLoopCall23>(taken[23]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QSGThreadedRenderLoop::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21QSGThreadedRenderLoop10metaObjectEv(
    const QSGThreadedRenderLoop *self) {
  return self->metaObject();
}

//  void *QSGThreadedRenderLoop::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN21QSGThreadedRenderLoop11qt_metacastEPKc(
    QSGThreadedRenderLoop *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QSGThreadedRenderLoop::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN21QSGThreadedRenderLoop11qt_metacallEN11QMetaObject4CallEiPPv(
    QSGThreadedRenderLoop *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QSGThreadedRenderLoop::~QSGThreadedRenderLoop()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSGThreadedRenderLoopD1Ev(QSGThreadedRenderLoop *self) {
  delete self;
}

//  void QSGThreadedRenderLoop::show(QQuickWindow *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSGThreadedRenderLoop4showEP12QQuickWindow(
    QSGThreadedRenderLoop *self,
    QQuickWindow *a0) {
  self->show(a0);
}

//  void QSGThreadedRenderLoop::hide(QQuickWindow *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSGThreadedRenderLoop4hideEP12QQuickWindow(
    QSGThreadedRenderLoop *self,
    QQuickWindow *a0) {
  self->hide(a0);
}

//  void QSGThreadedRenderLoop::resize(QQuickWindow *window)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSGThreadedRenderLoop6resizeEP12QQuickWindow(
    QSGThreadedRenderLoop *self,
    QQuickWindow *window) {
  self->resize(window);
}

//  void QSGThreadedRenderLoop::windowDestroyed(QQuickWindow *window)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSGThreadedRenderLoop15windowDestroyedEP12QQuickWindow(
    QSGThreadedRenderLoop *self,
    QQuickWindow *window) {
  self->windowDestroyed(window);
}

//  void QSGThreadedRenderLoop::exposureChanged(QQuickWindow *window)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSGThreadedRenderLoop15exposureChangedEP12QQuickWindow(
    QSGThreadedRenderLoop *self,
    QQuickWindow *window) {
  self->exposureChanged(window);
}

//  QImage QSGThreadedRenderLoop::grab(QQuickWindow *a0)
extern "C" Q_DECL_EXPORT
QImage *ritual_ZN21QSGThreadedRenderLoop4grabEP12QQuickWindow(
    QSGThreadedRenderLoop *self,
    QQuickWindow *a0) {
  return new QImage(self->grab(a0));
}

//  void QSGThreadedRenderLoop::update(QQuickWindow *window)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSGThreadedRenderLoop6updateEP12QQuickWindow(
    QSGThreadedRenderLoop *self,
    QQuickWindow *window) {
  self->update(window);
}

//  void QSGThreadedRenderLoop::maybeUpdate(QQuickWindow *window)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSGThreadedRenderLoop11maybeUpdateEP12QQuickWindow(
    QSGThreadedRenderLoop *self,
    QQuickWindow *window) {
  self->maybeUpdate(window);
}

//  void QSGThreadedRenderLoop::handleUpdateRequest(QQuickWindow *window)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSGThreadedRenderLoop19handleUpdateRequestEP12QQuickWindow(
    QSGThreadedRenderLoop *self,
    QQuickWindow *window) {
  self->handleUpdateRequest(window);
}

//  QSGContext *QSGThreadedRenderLoop::sceneGraphContext() const
extern "C" Q_DECL_EXPORT
QSGContext *ritual_ZNK21QSGThreadedRenderLoop17sceneGraphContextEv(
    const QSGThreadedRenderLoop *self) {
  return self->sceneGraphContext();
}

//  QSGRenderContext *QSGThreadedRenderLoop::createRenderContext(QSGContext
//      *a0) const
extern "C" Q_DECL_EXPORT
QSGRenderContext *ritual_ZNK21QSGThreadedRenderLoop19createRenderContextEP10QSGContext(
    const QSGThreadedRenderLoop *self,
    QSGContext *a0) {
  return self->createRenderContext(a0);
}

//  QAnimationDriver *QSGThreadedRenderLoop::animationDriver() const
extern "C" Q_DECL_EXPORT
QAnimationDriver *ritual_ZNK21QSGThreadedRenderLoop15animationDriverEv(
    const QSGThreadedRenderLoop *self) {
  return self->animationDriver();
}

//  void QSGThreadedRenderLoop::releaseResources(QQuickWindow *window)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSGThreadedRenderLoop16releaseResourcesEP12QQuickWindow(
    QSGThreadedRenderLoop *self,
    QQuickWindow *window) {
  self->releaseResources(window);
}

//  bool QSGThreadedRenderLoop::event(QEvent *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QSGThreadedRenderLoop5eventEP6QEvent(
    QSGThreadedRenderLoop *self,
    QEvent *a0) {
  return self->event(a0);
}

//  void QSGThreadedRenderLoop::postJob(QQuickWindow *window, QRunnable *job)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSGThreadedRenderLoop7postJobEP12QQuickWindowP9QRunnable(
    QSGThreadedRenderLoop *self,
    QQuickWindow *window,
    QRunnable *job) {
  self->postJob(window, job);
}

//  bool QSGThreadedRenderLoop::interleaveIncubation() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QSGThreadedRenderLoop20interleaveIncubationEv(
    const QSGThreadedRenderLoop *self) {
  return self->interleaveIncubation();
}

//  void QSGThreadedRenderLoop::animationStarted()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSGThreadedRenderLoop16animationStartedEv(
    QSGThreadedRenderLoop *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QSGThreadedRenderLoop")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "animationStarted()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "animationStarted()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QSGThreadedRenderLoop::animationStopped()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSGThreadedRenderLoop16animationStoppedEv(
    QSGThreadedRenderLoop *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QSGThreadedRenderLoop")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "animationStopped()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "animationStopped()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  Window *QSGThreadedRenderLoop::windowFor(QQuickWindow *window)
extern "C" Q_DECL_EXPORT
QSGThreadedRenderLoop::Window *ritual_ZN21QSGThreadedRenderLoop9windowForEP12QQuickWindow(
    QSGThreadedRenderLoop *self,
    QQuickWindow *window) {
  return self->windowFor(window);
}

//  bool QSGThreadedRenderLoop::anyoneShowing() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QSGThreadedRenderLoop13anyoneShowingEv(
    const QSGThreadedRenderLoop *self) {
  return self->anyoneShowing();
}

//  void QSGThreadedRenderLoop::startOrStopAnimationTimer()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSGThreadedRenderLoop25startOrStopAnimationTimerEv(
    QSGThreadedRenderLoop *self) {
  self->startOrStopAnimationTimer();
}

//  void QSGThreadedRenderLoop::postUpdateRequest(Window *w)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSGThreadedRenderLoop17postUpdateRequestEPNS_6WindowE(
    QSGThreadedRenderLoop *self,
    QSGThreadedRenderLoop::Window *w) {
  self->postUpdateRequest(w);
}

//  void QSGThreadedRenderLoop::releaseSwapchain(QQuickWindow *window)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSGThreadedRenderLoop16releaseSwapchainEP12QQuickWindow(
    QSGThreadedRenderLoop *self,
    QQuickWindow *window) {
  self->releaseSwapchain(window);
}

//  bool QSGThreadedRenderLoop::eventFilter(QObject *watched, QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QSGThreadedRenderLoop11eventFilterEP7QObjectP6QEvent(
    QSGThreadedRenderLoop *self,
    QObject *watched,
    QEvent *event) {
  return self->eventFilter(watched, event);
}

//  a Python function taken by a CuteQSGThreadedRenderLoop, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSGThreadedRenderLoop(
    QSGThreadedRenderLoop *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSGThreadedRenderLoop *>(self)->take(key, call);
}

//  void QSGThreadedRenderLoop::show(QQuickWindow *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QSGThreadedRenderLoop4showEP12QQuickWindow(
    QSGThreadedRenderLoop *self,
    QQuickWindow *a0) {
  self->QSGThreadedRenderLoop::show(a0);
}

//  void QSGThreadedRenderLoop::hide(QQuickWindow *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QSGThreadedRenderLoop4hideEP12QQuickWindow(
    QSGThreadedRenderLoop *self,
    QQuickWindow *a0) {
  self->QSGThreadedRenderLoop::hide(a0);
}

//  void QSGThreadedRenderLoop::resize(QQuickWindow *window)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QSGThreadedRenderLoop6resizeEP12QQuickWindow(
    QSGThreadedRenderLoop *self,
    QQuickWindow *window) {
  self->QSGThreadedRenderLoop::resize(window);
}

//  void QSGThreadedRenderLoop::windowDestroyed(QQuickWindow *window)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QSGThreadedRenderLoop15windowDestroyedEP12QQuickWindow(
    QSGThreadedRenderLoop *self,
    QQuickWindow *window) {
  self->QSGThreadedRenderLoop::windowDestroyed(window);
}

//  QImage QSGThreadedRenderLoop::grab(QQuickWindow *a0)
extern "C" Q_DECL_EXPORT
QImage *ritual_own_ZN21QSGThreadedRenderLoop4grabEP12QQuickWindow(
    QSGThreadedRenderLoop *self,
    QQuickWindow *a0) {
  return new QImage(self->QSGThreadedRenderLoop::grab(a0));
}

//  QSGContext *QSGThreadedRenderLoop::sceneGraphContext() const
extern "C" Q_DECL_EXPORT
QSGContext *ritual_own_ZNK21QSGThreadedRenderLoop17sceneGraphContextEv(
    const QSGThreadedRenderLoop *self) {
  return self->QSGThreadedRenderLoop::sceneGraphContext();
}

//  QSGRenderContext *QSGThreadedRenderLoop::createRenderContext(QSGContext
//      *a0) const
extern "C" Q_DECL_EXPORT
QSGRenderContext *ritual_own_ZNK21QSGThreadedRenderLoop19createRenderContextEP10QSGContext(
    const QSGThreadedRenderLoop *self,
    QSGContext *a0) {
  return self->QSGThreadedRenderLoop::createRenderContext(a0);
}

//  QAnimationDriver *QSGThreadedRenderLoop::animationDriver() const
extern "C" Q_DECL_EXPORT
QAnimationDriver *ritual_own_ZNK21QSGThreadedRenderLoop15animationDriverEv(
    const QSGThreadedRenderLoop *self) {
  return self->QSGThreadedRenderLoop::animationDriver();
}

//  void QSGThreadedRenderLoop::releaseResources(QQuickWindow *window)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QSGThreadedRenderLoop16releaseResourcesEP12QQuickWindow(
    QSGThreadedRenderLoop *self,
    QQuickWindow *window) {
  self->QSGThreadedRenderLoop::releaseResources(window);
}

//  bool QSGThreadedRenderLoop::event(QEvent *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN21QSGThreadedRenderLoop5eventEP6QEvent(
    QSGThreadedRenderLoop *self,
    QEvent *a0) {
  return self->QSGThreadedRenderLoop::event(a0);
}

//  void QSGThreadedRenderLoop::postJob(QQuickWindow *window, QRunnable *job)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QSGThreadedRenderLoop7postJobEP12QQuickWindowP9QRunnable(
    QSGThreadedRenderLoop *self,
    QQuickWindow *window,
    QRunnable *job) {
  self->QSGThreadedRenderLoop::postJob(window, job);
}

//  bool QSGThreadedRenderLoop::interleaveIncubation() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK21QSGThreadedRenderLoop20interleaveIncubationEv(
    const QSGThreadedRenderLoop *self) {
  return self->QSGThreadedRenderLoop::interleaveIncubation();
}

//  bool QSGThreadedRenderLoop::eventFilter(QObject *watched, QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN21QSGThreadedRenderLoop11eventFilterEP7QObjectP6QEvent(
    QSGThreadedRenderLoop *self,
    QObject *watched,
    QEvent *event) {
  return self->QSGThreadedRenderLoop::eventFilter(watched, event);
}

#endif  // QT_CONFIG(thread)
