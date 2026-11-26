//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgsoftwarethreadedrenderloop_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(thread)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgsoftwarethreadedrenderloop_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qimage.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/private/qsgsoftwarethreadedrenderloop_p.h>
#include <QtQuick/private/qsgsoftwarecontext_p.h>
#include <QtQuick/private/qsgsoftwarerenderer_p.h>
#include <QtQuick/private/qsgrenderer_p.h>
#include <QtQuick/private/qquickwindow_p.h>
#include <QtQuick/private/qquickitem_p.h>
#include <QtQuick/private/qquickprofiler_p.h>
#include <QtQuick/private/qquickanimatorcontroller_p.h>
#include <QtQuick/private/qquickprofiler_p.h>
#include <QtQml/private/qqmldebugserviceinterfaces_p.h>
#include <QtQml/private/qqmldebugconnector_p.h>
#include <QtGui/qpa/qplatformbackingstore.h>
#include <QtCore/QQueue>
#include <QtCore/QElapsedTimer>
#include <QtCore/QThread>
#include <QtCore/QMutex>
#include <QtCore/QWaitCondition>
#include <QtGui/QGuiApplication>
#include <QtGui/QBackingStore>
#include <QtQuick/QQuickWindow>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarethreadedrenderloop.cpp, line 35, as local:qsgsoftwarethreadedrenderloop.cpp:QSGSoftwareWindowEvent
Q_STATIC_LOGGING_CATEGORY(QSG_RASTER_LOG_RENDERLOOP,          "qt.scenegraph.renderloop")

class QSGSoftwareWindowEvent : public QEvent
{
public:
    QSGSoftwareWindowEvent(QQuickWindow *c, QEvent::Type type) : QEvent(type), window(c) { }
    QQuickWindow *window;
};

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarethreadedrenderloop.cpp, line 44, as local:qsgsoftwarethreadedrenderloop.cpp:QSGSoftwareTryReleaseEvent
class QSGSoftwareTryReleaseEvent : public QSGSoftwareWindowEvent
{
public:
    QSGSoftwareTryReleaseEvent(QQuickWindow *win, bool destroy)
        : QSGSoftwareWindowEvent(win, QEvent::Type(WM_TryRelease)), destroying(destroy) { }
    bool destroying;
};

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarethreadedrenderloop.cpp, line 67, as local:qsgsoftwarethreadedrenderloop.cpp:QSGSoftwareGrabEvent
class QSGSoftwareGrabEvent : public QSGSoftwareWindowEvent
{
public:
    QSGSoftwareGrabEvent(QQuickWindow *c, QImage *result)
        : QSGSoftwareWindowEvent(c, QEvent::Type(WM_Grab)), image(result) { }
    QImage *image;
};

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarethreadedrenderloop.cpp, line 75, as local:qsgsoftwarethreadedrenderloop.cpp:QSGSoftwareJobEvent
class QSGSoftwareJobEvent : public QSGSoftwareWindowEvent
{
public:
    QSGSoftwareJobEvent(QQuickWindow *c, QRunnable *postedJob)
        : QSGSoftwareWindowEvent(c, QEvent::Type(WM_PostJob)), job(postedJob) { }
    ~QSGSoftwareJobEvent() { delete job; }
    QRunnable *job;
};

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarethreadedrenderloop.cpp, line 84, as local:qsgsoftwarethreadedrenderloop.cpp:QSGSoftwareEventQueue
class QSGSoftwareEventQueue : public QQueue<QEvent *>
{
public:
    void addEvent(QEvent *e) {
        mutex.lock();
        enqueue(e);
        if (waiting)
            condition.wakeOne();
        mutex.unlock();
    }

    QEvent *takeEvent(bool wait) {
        mutex.lock();
        if (isEmpty() && wait) {
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
    bool waiting = false;
};

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarethreadedrenderloop.cpp, line 120, as local:qsgsoftwarethreadedrenderloop.cpp:qsgrl_animation_interval
static inline int qsgrl_animation_interval()
{
    const qreal refreshRate = QGuiApplication::primaryScreen() ? QGuiApplication::primaryScreen()->refreshRate() : 0;
    return refreshRate < 1 ? 16 : int(1000 / refreshRate);
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarethreadedrenderloop.cpp, line 126, as local:qsgsoftwarethreadedrenderloop.cpp:QSGSoftwareRenderThread
class QSGSoftwareRenderThread : public QThread
{
    Q_OBJECT
public:
    QSGSoftwareRenderThread(QSGSoftwareThreadedRenderLoop *rl, QSGRenderContext *renderContext)
        : renderLoop(rl)
    {
        rc = static_cast<QSGSoftwareRenderContext *>(renderContext);
        vsyncDelta = qsgrl_animation_interval();
    }

    ~QSGSoftwareRenderThread()
    {
        delete rc;
    }

    bool event(QEvent *e) override;
    void run() override;

    void syncAndRender();
    void sync(bool inExpose);

    void requestRepaint()
    {
        if (sleeping)
            stopEventProcessing = true;
        if (exposedWindow)
            pendingUpdate |= RepaintRequest;
    }

    void processEventsAndWaitForMore();
    void processEvents();
    void postEvent(QEvent *e);

    enum UpdateRequest {
        SyncRequest         = 0x01,
        RepaintRequest      = 0x02,
        ExposeRequest       = 0x04 | RepaintRequest | SyncRequest
    };

    QSGSoftwareThreadedRenderLoop *renderLoop;
    QSGSoftwareRenderContext *rc;
    QAnimationDriver *rtAnim = nullptr;
    volatile bool active = false;
    uint pendingUpdate = 0;
    bool sleeping = false;
    bool syncResultedInChanges = false;
    float vsyncDelta;
    QMutex mutex;
    QWaitCondition waitCondition;
    QQuickWindow *exposedWindow = nullptr;
    QBackingStore *backingStore = nullptr;
    bool stopEventProcessing = false;
    QSGSoftwareEventQueue eventQueue;
    QElapsedTimer renderThrottleTimer;
    qint64 syncTime;
    qint64 renderTime;
    qint64 sinceLastTime;

public slots:
    void onSceneGraphChanged() {
        syncResultedInChanges = true;
    }
};

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarethreadedrenderloop.cpp, line 314, as local:qsgsoftwarethreadedrenderloop.cpp:QSGSoftwareRenderThread::postEvent
inline void QSGSoftwareRenderThread::postEvent(QEvent *e)
{
    eventQueue.addEvent(e);
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarethreadedrenderloop.cpp, line 319, as local:qsgsoftwarethreadedrenderloop.cpp:QSGSoftwareRenderThread::processEvents
inline void QSGSoftwareRenderThread::processEvents()
{
    while (eventQueue.hasMoreEvents()) {
        QEvent *e = eventQueue.takeEvent(false);
        event(e);
        delete e;
    }
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarethreadedrenderloop.cpp, line 328, as local:qsgsoftwarethreadedrenderloop.cpp:QSGSoftwareRenderThread::processEventsAndWaitForMore
inline void QSGSoftwareRenderThread::processEventsAndWaitForMore()
{
    stopEventProcessing = false;
    while (!stopEventProcessing) {
        QEvent *e = eventQueue.takeEvent(true);
        event(e);
        delete e;
    }
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarethreadedrenderloop.cpp, line 533, as _ZN29QSGSoftwareThreadedRenderLoop4showEP12QQuickWindow
inline void QSGSoftwareThreadedRenderLoop::show(QQuickWindow *window)
{
    qCDebug(QSG_RASTER_LOG_RENDERLOOP) << "show" << window;
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarethreadedrenderloop.cpp, line 538, as _ZN29QSGSoftwareThreadedRenderLoop4hideEP12QQuickWindow
inline void QSGSoftwareThreadedRenderLoop::hide(QQuickWindow *window)
{
    qCDebug(QSG_RASTER_LOG_RENDERLOOP) << "hide" << window;

    if (window->isExposed())
        handleObscurity(windowFor(window));

    releaseResources(window);
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarethreadedrenderloop.cpp, line 548, as _ZN29QSGSoftwareThreadedRenderLoop6resizeEP12QQuickWindow
inline void QSGSoftwareThreadedRenderLoop::resize(QQuickWindow *window)
{
    if (!window->isExposed() || window->size().isEmpty())
        return;

    qCDebug(QSG_RASTER_LOG_RENDERLOOP) << "resize" << window << window->size();
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarethreadedrenderloop.cpp, line 556, as _ZN29QSGSoftwareThreadedRenderLoop15windowDestroyedEP12QQuickWindow
inline void QSGSoftwareThreadedRenderLoop::windowDestroyed(QQuickWindow *window)
{
    qCDebug(QSG_RASTER_LOG_RENDERLOOP) << "window destroyed" << window;

    WindowData *w = windowFor(window);
    if (!w)
        return;

    handleObscurity(w);
    handleResourceRelease(w, true);

    QSGSoftwareRenderThread *thread = w->thread;
    while (thread->isRunning())
        QThread::yieldCurrentThread();

    Q_ASSERT(thread->thread() == QThread::currentThread());
    delete thread;

    for (int i = 0; i < m_windows.size(); ++i) {
        if (m_windows.at(i).window == window) {
            m_windows.removeAt(i);
            break;
        }
    }

    // Now that we altered the window list, we may need to stop the animation
    // timer even if we didn't via handleObscurity. This covers the case where
    // we destroy a visible & exposed QQuickWindow.
    startOrStopAnimationTimer();
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarethreadedrenderloop.cpp, line 587, as _ZN29QSGSoftwareThreadedRenderLoop15exposureChangedEP12QQuickWindow
inline void QSGSoftwareThreadedRenderLoop::exposureChanged(QQuickWindow *window)
{
    qCDebug(QSG_RASTER_LOG_RENDERLOOP) << "exposure changed" << window;

    if (window->isExposed()) {
        handleExposure(window);
    } else {
        WindowData *w = windowFor(window);
        if (w)
            handleObscurity(w);
    }
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarethreadedrenderloop.cpp, line 600, as _ZN29QSGSoftwareThreadedRenderLoop4grabEP12QQuickWindow
inline QImage QSGSoftwareThreadedRenderLoop::grab(QQuickWindow *window)
{
    qCDebug(QSG_RASTER_LOG_RENDERLOOP) << "grab" << window;

    WindowData *w = windowFor(window);
    // Have to support invisible (but created()'ed) windows as well.
    // Unlike with GL, leaving that case for QQuickWindow to handle is not feasible.
    const bool tempExpose = !w;
    if (tempExpose) {
        handleExposure(window);
        w = windowFor(window);
        Q_ASSERT(w);
    }

    if (!w->thread->isRunning())
        return QImage();

    if (!window->handle())
        window->create();

    QQuickWindowPrivate *wd = QQuickWindowPrivate::get(window);
    wd->polishItems();

    QImage result;
    w->thread->mutex.lock();
    lockedForSync = true;
    w->thread->postEvent(new QSGSoftwareGrabEvent(window, &result));
    w->thread->waitCondition.wait(&w->thread->mutex);
    lockedForSync = false;
    w->thread->mutex.unlock();

    result.setDevicePixelRatio(window->effectiveDevicePixelRatio());

    if (tempExpose)
        handleObscurity(w);

    return result;
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarethreadedrenderloop.cpp, line 639, as _ZN29QSGSoftwareThreadedRenderLoop6updateEP12QQuickWindow
inline void QSGSoftwareThreadedRenderLoop::update(QQuickWindow *window)
{
    WindowData *w = windowFor(window);
    if (!w)
        return;

    if (w->thread == QThread::currentThread()) {
        w->thread->requestRepaint();
        return;
    }

    // We set forceRenderPass because we want to make sure the QQuickWindow
    // actually does a full render pass after the next sync.
    w->forceRenderPass = true;
    scheduleUpdate(w);
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarethreadedrenderloop.cpp, line 656, as _ZN29QSGSoftwareThreadedRenderLoop11maybeUpdateEP12QQuickWindow
inline void QSGSoftwareThreadedRenderLoop::maybeUpdate(QQuickWindow *window)
{
    WindowData *w = windowFor(window);
    if (w)
        scheduleUpdate(w);
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarethreadedrenderloop.cpp, line 663, as _ZN29QSGSoftwareThreadedRenderLoop19handleUpdateRequestEP12QQuickWindow
inline void QSGSoftwareThreadedRenderLoop::handleUpdateRequest(QQuickWindow *window)
{
    qCDebug(QSG_RASTER_LOG_RENDERLOOP) << "handleUpdateRequest" << window;

    WindowData *w = windowFor(window);
    if (w)
        polishAndSync(w, false);
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarethreadedrenderloop.cpp, line 672, as _ZNK29QSGSoftwareThreadedRenderLoop15animationDriverEv
inline QAnimationDriver *QSGSoftwareThreadedRenderLoop::animationDriver() const
{
    return m_anim;
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarethreadedrenderloop.cpp, line 677, as _ZNK29QSGSoftwareThreadedRenderLoop17sceneGraphContextEv
inline QSGContext *QSGSoftwareThreadedRenderLoop::sceneGraphContext() const
{
    return m_sg;
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarethreadedrenderloop.cpp, line 682, as _ZNK29QSGSoftwareThreadedRenderLoop19createRenderContextEP10QSGContext
inline QSGRenderContext *QSGSoftwareThreadedRenderLoop::createRenderContext(QSGContext *) const
{
    return m_sg->createRenderContext();
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarethreadedrenderloop.cpp, line 687, as _ZN29QSGSoftwareThreadedRenderLoop16releaseResourcesEP12QQuickWindow
inline void QSGSoftwareThreadedRenderLoop::releaseResources(QQuickWindow *window)
{
    qCDebug(QSG_RASTER_LOG_RENDERLOOP) << "releaseResources" << window;

    WindowData *w = windowFor(window);
    if (w)
        handleResourceRelease(w, false);
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarethreadedrenderloop.cpp, line 696, as _ZN29QSGSoftwareThreadedRenderLoop7postJobEP12QQuickWindowP9QRunnable
inline void QSGSoftwareThreadedRenderLoop::postJob(QQuickWindow *window, QRunnable *job)
{
    WindowData *w = windowFor(window);
    if (w && w->thread && w->thread->exposedWindow)
        w->thread->postEvent(new QSGSoftwareJobEvent(window, job));
    else
        delete job;
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarethreadedrenderloop.cpp, line 705, as _ZNK29QSGSoftwareThreadedRenderLoop17windowSurfaceTypeEv
inline QSurface::SurfaceType QSGSoftwareThreadedRenderLoop::windowSurfaceType() const
{
    return QSurface::RasterSurface;
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarethreadedrenderloop.cpp, line 710, as _ZNK29QSGSoftwareThreadedRenderLoop20interleaveIncubationEv
inline bool QSGSoftwareThreadedRenderLoop::interleaveIncubation() const
{
    bool somethingVisible = false;
    for (const WindowData &w : m_windows) {
        if (w.window->isVisible() && w.window->isExposed()) {
            somethingVisible = true;
            break;
        }
    }
    return somethingVisible && m_anim->isRunning();
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarethreadedrenderloop.cpp, line 722, as _ZNK29QSGSoftwareThreadedRenderLoop5flagsEv
inline int QSGSoftwareThreadedRenderLoop::flags() const
{
    return SupportsGrabWithoutExpose;
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarethreadedrenderloop.cpp, line 727, as _ZN29QSGSoftwareThreadedRenderLoop5eventEP6QEvent
inline bool QSGSoftwareThreadedRenderLoop::event(QEvent *e)
{
    if (e->type() == QEvent::Timer) {
        QTimerEvent *te = static_cast<QTimerEvent *>(e);
        if (te->timerId() == animationTimer) {
            m_anim->advance();
            emit timeToIncubate();
            return true;
        }
    }

    return QObject::event(e);
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarethreadedrenderloop.cpp, line 836, as _ZN29QSGSoftwareThreadedRenderLoop15handleObscurityEPNS_10WindowDataE
inline void QSGSoftwareThreadedRenderLoop::handleObscurity(QSGSoftwareThreadedRenderLoop::WindowData *w)
{
    qCDebug(QSG_RASTER_LOG_RENDERLOOP) << "handleObscurity" << w->window;

    if (w->thread->isRunning()) {
        w->thread->mutex.lock();
        w->thread->postEvent(new QSGSoftwareWindowEvent(w->window, QEvent::Type(WM_Obscure)));
        w->thread->waitCondition.wait(&w->thread->mutex);
        w->thread->mutex.unlock();
    }

    startOrStopAnimationTimer();
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarethreadedrenderloop.cpp, line 872, as _ZN29QSGSoftwareThreadedRenderLoop21handleResourceReleaseEPNS_10WindowDataEb
inline void QSGSoftwareThreadedRenderLoop::handleResourceRelease(QSGSoftwareThreadedRenderLoop::WindowData *w, bool destroying)
{
    qCDebug(QSG_RASTER_LOG_RENDERLOOP) << "handleResourceRelease" << (destroying ? "destroying" : "hide/releaseResources") << w->window;

    w->thread->mutex.lock();
    if (w->thread->isRunning() && w->thread->active) {
        QQuickWindow *window = w->window;

        // Note that window->handle() is typically null by this time because
        // the platform window is already destroyed. This should not be a
        // problem for the D3D cleanup.

        w->thread->postEvent(new QSGSoftwareTryReleaseEvent(window, destroying));
        w->thread->waitCondition.wait(&w->thread->mutex);

        // Avoid a shutdown race condition.
        // If SG is invalidated and 'active' becomes false, the thread's run()
        // method will exit. handleExposure() relies on QThread::isRunning() (because it
        // potentially needs to start the thread again) and our mutex cannot be used to
        // track the thread stopping, so we wait a few nanoseconds extra so the thread
        // can exit properly.
        if (!w->thread->active)
            w->thread->wait();
    }
    w->thread->mutex.unlock();
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarethreadedrenderloop.cpp, line 778, as _ZN29QSGSoftwareThreadedRenderLoop14handleExposureEP12QQuickWindow
inline void QSGSoftwareThreadedRenderLoop::handleExposure(QQuickWindow *window)
{
    qCDebug(QSG_RASTER_LOG_RENDERLOOP) << "handleExposure" << window;

    WindowData *w = windowFor(window);
    if (!w) {
        qCDebug(QSG_RASTER_LOG_RENDERLOOP, "adding window to list");
        WindowData win;
        win.window = window;
        QSGRenderContext *rc = QQuickWindowPrivate::get(window)->context; // will transfer ownership
        win.thread = new QSGSoftwareRenderThread(this, rc);
        win.updateDuringSync = false;
        win.forceRenderPass = true; // also covered by polishAndSync(inExpose=true), but doesn't hurt
        m_windows.append(win);
        w = &m_windows.last();
    }

    // set this early as we'll be rendering shortly anyway and this avoids
    // special casing exposure in polishAndSync.
    w->thread->exposedWindow = window;

    if (w->window->size().isEmpty()
        || (w->window->isTopLevel() && !w->window->geometry().intersects(w->window->screen()->availableGeometry()))) {
#ifndef QT_NO_DEBUG
        qWarning().noquote().nospace() << "QSGSotwareThreadedRenderLoop: expose event received for window "
            << w->window << " with invalid geometry: " << w->window->geometry()
            << " on " << w->window->screen();
#endif
    }

    if (!w->window->handle())
        w->window->create();

    // Start render thread if it is not running
    if (!w->thread->isRunning()) {
        qCDebug(QSG_RASTER_LOG_RENDERLOOP, "starting render thread");
        // Push a few things to the render thread.
        QQuickAnimatorController *controller
                = QQuickWindowPrivate::get(w->window)->animationController.get();
        if (controller->thread() != w->thread)
            controller->moveToThread(w->thread);
        if (w->thread->thread() == QThread::currentThread()) {
            w->thread->rc->moveToThread(w->thread);
            w->thread->moveToThread(w->thread);
        }

        w->thread->active = true;
        w->thread->start();

        if (!w->thread->isRunning())
            qFatal("Render thread failed to start, aborting application.");
    }

    polishAndSync(w, true);

    startOrStopAnimationTimer();
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarethreadedrenderloop.cpp, line 850, as _ZN29QSGSoftwareThreadedRenderLoop14scheduleUpdateEPNS_10WindowDataE
inline void QSGSoftwareThreadedRenderLoop::scheduleUpdate(QSGSoftwareThreadedRenderLoop::WindowData *w)
{
    if (!QCoreApplication::instance())
        return;

    if (!w || !w->thread->isRunning())
        return;

    QThread *current = QThread::currentThread();
    if (current != QCoreApplication::instance()->thread() && (current != w->thread || !lockedForSync)) {
        qWarning() << "Updates can only be scheduled from GUI thread or from QQuickItem::updatePaintNode()";
        return;
    }

    if (current == w->thread) {
        w->updateDuringSync = true;
        return;
    }

    w->window->requestUpdate();
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarethreadedrenderloop.cpp, line 507, as _ZN29QSGSoftwareThreadedRenderLoop9windowForEP12QQuickWindow
inline QSGSoftwareThreadedRenderLoop::WindowData *QSGSoftwareThreadedRenderLoop::windowFor(QQuickWindow *window)
{
    for (const auto &t : std::as_const(m_windows)) {
        if (t.window == window)
            return const_cast<WindowData *>(&t);
    }
    return nullptr;
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarethreadedrenderloop.cpp, line 754, as _ZN29QSGSoftwareThreadedRenderLoop25startOrStopAnimationTimerEv
inline void QSGSoftwareThreadedRenderLoop::startOrStopAnimationTimer()
{
    int exposedWindowCount = 0;
    const WindowData *exposed = nullptr;

    for (int i = 0; i < m_windows.size(); ++i) {
        const WindowData &w(m_windows[i]);
        if (w.window->isVisible() && w.window->isExposed()) {
            ++exposedWindowCount;
            exposed = &w;
        }
    }

    if (animationTimer && (exposedWindowCount == 1 || !m_anim->isRunning())) {
        killTimer(animationTimer);
        animationTimer = 0;
        // If animations are running, make sure we keep on animating
        if (m_anim->isRunning())
            exposed->window->requestUpdate();
    } else if (!animationTimer && exposedWindowCount != 1 && m_anim->isRunning()) {
        animationTimer = startTimer(qsgrl_animation_interval());
    }
}
//  -----------------------------------------------------------------------

//  A QSGSoftwareThreadedRenderLoop that Python can take functions over in. Every QSGSoftwareThreadedRenderLoop
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQSGSoftwareThreadedRenderLoopCall0)(const void *, QQuickWindow *, int *);
typedef void (*CuteQSGSoftwareThreadedRenderLoopCall1)(const void *, QQuickWindow *, int *);
typedef void (*CuteQSGSoftwareThreadedRenderLoopCall2)(const void *, QQuickWindow *, int *);
typedef void (*CuteQSGSoftwareThreadedRenderLoopCall3)(const void *, QQuickWindow *, int *);
typedef void (*CuteQSGSoftwareThreadedRenderLoopCall4)(const void *, QQuickWindow *, int *);
typedef const QImage * (*CuteQSGSoftwareThreadedRenderLoopCall5)(const void *, QQuickWindow *, int *);
typedef void (*CuteQSGSoftwareThreadedRenderLoopCall6)(const void *, QQuickWindow *, int *);
typedef void (*CuteQSGSoftwareThreadedRenderLoopCall7)(const void *, QQuickWindow *, int *);
typedef void (*CuteQSGSoftwareThreadedRenderLoopCall8)(const void *, QQuickWindow *, int *);
typedef void * (*CuteQSGSoftwareThreadedRenderLoopCall9)(const void *, int *);
typedef void * (*CuteQSGSoftwareThreadedRenderLoopCall10)(const void *, int *);
typedef void * (*CuteQSGSoftwareThreadedRenderLoopCall11)(const void *, QSGContext *, int *);
typedef void (*CuteQSGSoftwareThreadedRenderLoopCall12)(const void *, QQuickWindow *, int *);
typedef void (*CuteQSGSoftwareThreadedRenderLoopCall13)(const void *, QQuickWindow *, QRunnable *, int *);
typedef int (*CuteQSGSoftwareThreadedRenderLoopCall14)(const void *, int *);
typedef bool (*CuteQSGSoftwareThreadedRenderLoopCall15)(const void *, int *);
typedef int (*CuteQSGSoftwareThreadedRenderLoopCall16)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSGSoftwareThreadedRenderLoopCall17)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSGSoftwareThreadedRenderLoopCall18)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGSoftwareThreadedRenderLoopCall19)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGSoftwareThreadedRenderLoopCall20)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGSoftwareThreadedRenderLoopCall21)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGSoftwareThreadedRenderLoopCall22)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGSoftwareThreadedRenderLoopCall23)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQSGSoftwareThreadedRenderLoop : public QSGSoftwareThreadedRenderLoop {
public:
  using QSGSoftwareThreadedRenderLoop::QSGSoftwareThreadedRenderLoop;
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
    if (!std::strcmp(key, "_ZNK13QSGRenderLoop15animationDriverEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK13QSGRenderLoop17sceneGraphContextEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK13QSGRenderLoop19createRenderContextEP10QSGContext")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QSGRenderLoop16releaseResourcesEP12QQuickWindow")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QSGRenderLoop7postJobEP12QQuickWindowP9QRunnable")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK13QSGRenderLoop17windowSurfaceTypeEv")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK13QSGRenderLoop20interleaveIncubationEv")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK13QSGRenderLoop5flagsEv")) {
      taken[16] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[17] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[18] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
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

  //  void QSGSoftwareThreadedRenderLoop::show(QQuickWindow *window)
  void show(QQuickWindow *window) override {
    if (taken[0]) {
      int handled = 0;
      CuteQSGSoftwareThreadedRenderLoopCall0 call = reinterpret_cast<CuteQSGSoftwareThreadedRenderLoopCall0>(taken[0]);
      call(this, window, &handled);
      if (handled) return;
    }
    QSGSoftwareThreadedRenderLoop::show(window);
  }

  //  void QSGSoftwareThreadedRenderLoop::hide(QQuickWindow *window)
  void hide(QQuickWindow *window) override {
    if (taken[1]) {
      int handled = 0;
      CuteQSGSoftwareThreadedRenderLoopCall1 call = reinterpret_cast<CuteQSGSoftwareThreadedRenderLoopCall1>(taken[1]);
      call(this, window, &handled);
      if (handled) return;
    }
    QSGSoftwareThreadedRenderLoop::hide(window);
  }

  //  void QSGSoftwareThreadedRenderLoop::resize(QQuickWindow *window)
  void resize(QQuickWindow *window) override {
    if (taken[2]) {
      int handled = 0;
      CuteQSGSoftwareThreadedRenderLoopCall2 call = reinterpret_cast<CuteQSGSoftwareThreadedRenderLoopCall2>(taken[2]);
      call(this, window, &handled);
      if (handled) return;
    }
    QSGSoftwareThreadedRenderLoop::resize(window);
  }

  //  void QSGSoftwareThreadedRenderLoop::windowDestroyed(QQuickWindow
  //      *window)
  void windowDestroyed(QQuickWindow *window) override {
    if (taken[3]) {
      int handled = 0;
      CuteQSGSoftwareThreadedRenderLoopCall3 call = reinterpret_cast<CuteQSGSoftwareThreadedRenderLoopCall3>(taken[3]);
      call(this, window, &handled);
      if (handled) return;
    }
    QSGSoftwareThreadedRenderLoop::windowDestroyed(window);
  }

  //  void QSGSoftwareThreadedRenderLoop::exposureChanged(QQuickWindow
  //      *window)
  void exposureChanged(QQuickWindow *window) override {
    if (taken[4]) {
      int handled = 0;
      CuteQSGSoftwareThreadedRenderLoopCall4 call = reinterpret_cast<CuteQSGSoftwareThreadedRenderLoopCall4>(taken[4]);
      call(this, window, &handled);
      if (handled) return;
    }
    QSGSoftwareThreadedRenderLoop::exposureChanged(window);
  }

  //  QImage QSGSoftwareThreadedRenderLoop::grab(QQuickWindow *window)
  QImage grab(QQuickWindow *window) override {
    if (taken[5]) {
      int handled = 0;
      CuteQSGSoftwareThreadedRenderLoopCall5 call = reinterpret_cast<CuteQSGSoftwareThreadedRenderLoopCall5>(taken[5]);
      const QImage * given = call(this, window, &handled);
      if (handled && given) return *given;
    }
    return QSGSoftwareThreadedRenderLoop::grab(window);
  }

  //  void QSGSoftwareThreadedRenderLoop::update(QQuickWindow *window)
  void update(QQuickWindow *window) override {
    if (taken[6]) {
      int handled = 0;
      CuteQSGSoftwareThreadedRenderLoopCall6 call = reinterpret_cast<CuteQSGSoftwareThreadedRenderLoopCall6>(taken[6]);
      call(this, window, &handled);
      if (handled) return;
    }
    QSGSoftwareThreadedRenderLoop::update(window);
  }

  //  void QSGSoftwareThreadedRenderLoop::maybeUpdate(QQuickWindow *window)
  void maybeUpdate(QQuickWindow *window) override {
    if (taken[7]) {
      int handled = 0;
      CuteQSGSoftwareThreadedRenderLoopCall7 call = reinterpret_cast<CuteQSGSoftwareThreadedRenderLoopCall7>(taken[7]);
      call(this, window, &handled);
      if (handled) return;
    }
    QSGSoftwareThreadedRenderLoop::maybeUpdate(window);
  }

  //  void QSGSoftwareThreadedRenderLoop::handleUpdateRequest(QQuickWindow
  //      *window)
  void handleUpdateRequest(QQuickWindow *window) override {
    if (taken[8]) {
      int handled = 0;
      CuteQSGSoftwareThreadedRenderLoopCall8 call = reinterpret_cast<CuteQSGSoftwareThreadedRenderLoopCall8>(taken[8]);
      call(this, window, &handled);
      if (handled) return;
    }
    QSGSoftwareThreadedRenderLoop::handleUpdateRequest(window);
  }

  //  QAnimationDriver *QSGSoftwareThreadedRenderLoop::animationDriver()
  //      const
  QAnimationDriver *animationDriver() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQSGSoftwareThreadedRenderLoopCall9 call = reinterpret_cast<CuteQSGSoftwareThreadedRenderLoopCall9>(taken[9]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAnimationDriver *>(given);
    }
    return QSGSoftwareThreadedRenderLoop::animationDriver();
  }

  //  QSGContext *QSGSoftwareThreadedRenderLoop::sceneGraphContext() const
  QSGContext *sceneGraphContext() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQSGSoftwareThreadedRenderLoopCall10 call = reinterpret_cast<CuteQSGSoftwareThreadedRenderLoopCall10>(taken[10]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGContext *>(given);
    }
    return QSGSoftwareThreadedRenderLoop::sceneGraphContext();
  }

  //  QSGRenderContext
  //      *QSGSoftwareThreadedRenderLoop::createRenderContext(QSGContext
  //      *a0) const
  QSGRenderContext *createRenderContext(QSGContext *a0) const override {
    if (taken[11]) {
      int handled = 0;
      CuteQSGSoftwareThreadedRenderLoopCall11 call = reinterpret_cast<CuteQSGSoftwareThreadedRenderLoopCall11>(taken[11]);
      void * given = call(this, a0, &handled);
      if (handled) return static_cast<QSGRenderContext *>(given);
    }
    return QSGSoftwareThreadedRenderLoop::createRenderContext(a0);
  }

  //  void QSGSoftwareThreadedRenderLoop::releaseResources(QQuickWindow
  //      *window)
  void releaseResources(QQuickWindow *window) override {
    if (taken[12]) {
      int handled = 0;
      CuteQSGSoftwareThreadedRenderLoopCall12 call = reinterpret_cast<CuteQSGSoftwareThreadedRenderLoopCall12>(taken[12]);
      call(this, window, &handled);
      if (handled) return;
    }
    QSGSoftwareThreadedRenderLoop::releaseResources(window);
  }

  //  void QSGSoftwareThreadedRenderLoop::postJob(QQuickWindow *window,
  //      QRunnable *job)
  void postJob(QQuickWindow *window, QRunnable *job) override {
    if (taken[13]) {
      int handled = 0;
      CuteQSGSoftwareThreadedRenderLoopCall13 call = reinterpret_cast<CuteQSGSoftwareThreadedRenderLoopCall13>(taken[13]);
      call(this, window, job, &handled);
      if (handled) return;
    }
    QSGSoftwareThreadedRenderLoop::postJob(window, job);
  }

  //  QSurface::SurfaceType
  //      QSGSoftwareThreadedRenderLoop::windowSurfaceType() const
  QSurface::SurfaceType windowSurfaceType() const override {
    if (taken[14]) {
      int handled = 0;
      CuteQSGSoftwareThreadedRenderLoopCall14 call = reinterpret_cast<CuteQSGSoftwareThreadedRenderLoopCall14>(taken[14]);
      int given = call(this, &handled);
      if (handled) return static_cast<QSurface::SurfaceType>(given);
    }
    return QSGSoftwareThreadedRenderLoop::windowSurfaceType();
  }

  //  bool QSGSoftwareThreadedRenderLoop::interleaveIncubation() const
  bool interleaveIncubation() const override {
    if (taken[15]) {
      int handled = 0;
      CuteQSGSoftwareThreadedRenderLoopCall15 call = reinterpret_cast<CuteQSGSoftwareThreadedRenderLoopCall15>(taken[15]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSGSoftwareThreadedRenderLoop::interleaveIncubation();
  }

  //  int QSGSoftwareThreadedRenderLoop::flags() const
  int flags() const override {
    if (taken[16]) {
      int handled = 0;
      CuteQSGSoftwareThreadedRenderLoopCall16 call = reinterpret_cast<CuteQSGSoftwareThreadedRenderLoopCall16>(taken[16]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QSGSoftwareThreadedRenderLoop::flags();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QSGSoftwareThreadedRenderLoop::event(QEvent *e)
  bool event(QEvent *e) override {
    if (taken[17]) {
      int handled = 0;
      CuteQSGSoftwareThreadedRenderLoopCall17 call = reinterpret_cast<CuteQSGSoftwareThreadedRenderLoopCall17>(taken[17]);
      bool given = call(this, e, &handled);
      if (handled) return given;
    }
    return QSGSoftwareThreadedRenderLoop::event(e);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQSGSoftwareThreadedRenderLoopCall18 call = reinterpret_cast<CuteQSGSoftwareThreadedRenderLoopCall18>(taken[18]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQSGSoftwareThreadedRenderLoopCall19 call = reinterpret_cast<CuteQSGSoftwareThreadedRenderLoopCall19>(taken[19]);
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
      CuteQSGSoftwareThreadedRenderLoopCall20 call = reinterpret_cast<CuteQSGSoftwareThreadedRenderLoopCall20>(taken[20]);
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
      CuteQSGSoftwareThreadedRenderLoopCall21 call = reinterpret_cast<CuteQSGSoftwareThreadedRenderLoopCall21>(taken[21]);
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
      CuteQSGSoftwareThreadedRenderLoopCall22 call = reinterpret_cast<CuteQSGSoftwareThreadedRenderLoopCall22>(taken[22]);
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
      CuteQSGSoftwareThreadedRenderLoopCall23 call = reinterpret_cast<CuteQSGSoftwareThreadedRenderLoopCall23>(taken[23]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QSGSoftwareThreadedRenderLoop::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK29QSGSoftwareThreadedRenderLoop10metaObjectEv(
    const QSGSoftwareThreadedRenderLoop *self) {
  return self->metaObject();
}

//  void *QSGSoftwareThreadedRenderLoop::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN29QSGSoftwareThreadedRenderLoop11qt_metacastEPKc(
    QSGSoftwareThreadedRenderLoop *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QSGSoftwareThreadedRenderLoop::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN29QSGSoftwareThreadedRenderLoop11qt_metacallEN11QMetaObject4CallEiPPv(
    QSGSoftwareThreadedRenderLoop *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  void QSGSoftwareThreadedRenderLoop::show(QQuickWindow *window)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QSGSoftwareThreadedRenderLoop4showEP12QQuickWindow(
    QSGSoftwareThreadedRenderLoop *self,
    QQuickWindow *window) {
  self->show(window);
}

//  void QSGSoftwareThreadedRenderLoop::hide(QQuickWindow *window)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QSGSoftwareThreadedRenderLoop4hideEP12QQuickWindow(
    QSGSoftwareThreadedRenderLoop *self,
    QQuickWindow *window) {
  self->hide(window);
}

//  void QSGSoftwareThreadedRenderLoop::resize(QQuickWindow *window)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QSGSoftwareThreadedRenderLoop6resizeEP12QQuickWindow(
    QSGSoftwareThreadedRenderLoop *self,
    QQuickWindow *window) {
  self->resize(window);
}

//  void QSGSoftwareThreadedRenderLoop::windowDestroyed(QQuickWindow *window)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QSGSoftwareThreadedRenderLoop15windowDestroyedEP12QQuickWindow(
    QSGSoftwareThreadedRenderLoop *self,
    QQuickWindow *window) {
  self->windowDestroyed(window);
}

//  void QSGSoftwareThreadedRenderLoop::exposureChanged(QQuickWindow *window)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QSGSoftwareThreadedRenderLoop15exposureChangedEP12QQuickWindow(
    QSGSoftwareThreadedRenderLoop *self,
    QQuickWindow *window) {
  self->exposureChanged(window);
}

//  QImage QSGSoftwareThreadedRenderLoop::grab(QQuickWindow *window)
extern "C" Q_DECL_EXPORT
QImage *ritual_ZN29QSGSoftwareThreadedRenderLoop4grabEP12QQuickWindow(
    QSGSoftwareThreadedRenderLoop *self,
    QQuickWindow *window) {
  return new QImage(self->grab(window));
}

//  void QSGSoftwareThreadedRenderLoop::update(QQuickWindow *window)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QSGSoftwareThreadedRenderLoop6updateEP12QQuickWindow(
    QSGSoftwareThreadedRenderLoop *self,
    QQuickWindow *window) {
  self->update(window);
}

//  void QSGSoftwareThreadedRenderLoop::maybeUpdate(QQuickWindow *window)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QSGSoftwareThreadedRenderLoop11maybeUpdateEP12QQuickWindow(
    QSGSoftwareThreadedRenderLoop *self,
    QQuickWindow *window) {
  self->maybeUpdate(window);
}

//  void QSGSoftwareThreadedRenderLoop::handleUpdateRequest(QQuickWindow
//      *window)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QSGSoftwareThreadedRenderLoop19handleUpdateRequestEP12QQuickWindow(
    QSGSoftwareThreadedRenderLoop *self,
    QQuickWindow *window) {
  self->handleUpdateRequest(window);
}

//  QAnimationDriver *QSGSoftwareThreadedRenderLoop::animationDriver() const
extern "C" Q_DECL_EXPORT
QAnimationDriver *ritual_ZNK29QSGSoftwareThreadedRenderLoop15animationDriverEv(
    const QSGSoftwareThreadedRenderLoop *self) {
  return self->animationDriver();
}

//  QSGContext *QSGSoftwareThreadedRenderLoop::sceneGraphContext() const
extern "C" Q_DECL_EXPORT
QSGContext *ritual_ZNK29QSGSoftwareThreadedRenderLoop17sceneGraphContextEv(
    const QSGSoftwareThreadedRenderLoop *self) {
  return self->sceneGraphContext();
}

//  QSGRenderContext
//      *QSGSoftwareThreadedRenderLoop::createRenderContext(QSGContext *a0)
//      const
extern "C" Q_DECL_EXPORT
QSGRenderContext *ritual_ZNK29QSGSoftwareThreadedRenderLoop19createRenderContextEP10QSGContext(
    const QSGSoftwareThreadedRenderLoop *self,
    QSGContext *a0) {
  return self->createRenderContext(a0);
}

//  void QSGSoftwareThreadedRenderLoop::releaseResources(QQuickWindow
//      *window)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QSGSoftwareThreadedRenderLoop16releaseResourcesEP12QQuickWindow(
    QSGSoftwareThreadedRenderLoop *self,
    QQuickWindow *window) {
  self->releaseResources(window);
}

//  void QSGSoftwareThreadedRenderLoop::postJob(QQuickWindow *window,
//      QRunnable *job)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QSGSoftwareThreadedRenderLoop7postJobEP12QQuickWindowP9QRunnable(
    QSGSoftwareThreadedRenderLoop *self,
    QQuickWindow *window,
    QRunnable *job) {
  self->postJob(window, job);
}

//  QSurface::SurfaceType QSGSoftwareThreadedRenderLoop::windowSurfaceType()
//      const
extern "C" Q_DECL_EXPORT
QSurface::SurfaceType ritual_ZNK29QSGSoftwareThreadedRenderLoop17windowSurfaceTypeEv(
    const QSGSoftwareThreadedRenderLoop *self) {
  return self->windowSurfaceType();
}

//  bool QSGSoftwareThreadedRenderLoop::interleaveIncubation() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK29QSGSoftwareThreadedRenderLoop20interleaveIncubationEv(
    const QSGSoftwareThreadedRenderLoop *self) {
  return self->interleaveIncubation();
}

//  int QSGSoftwareThreadedRenderLoop::flags() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK29QSGSoftwareThreadedRenderLoop5flagsEv(
    const QSGSoftwareThreadedRenderLoop *self) {
  return self->flags();
}

//  bool QSGSoftwareThreadedRenderLoop::event(QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_ZN29QSGSoftwareThreadedRenderLoop5eventEP6QEvent(
    QSGSoftwareThreadedRenderLoop *self,
    QEvent *e) {
  return self->event(e);
}

//  void QSGSoftwareThreadedRenderLoop::onAnimationStarted()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QSGSoftwareThreadedRenderLoop18onAnimationStartedEv(
    QSGSoftwareThreadedRenderLoop *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QSGSoftwareThreadedRenderLoop")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "onAnimationStarted()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "onAnimationStarted()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QSGSoftwareThreadedRenderLoop::onAnimationStopped()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QSGSoftwareThreadedRenderLoop18onAnimationStoppedEv(
    QSGSoftwareThreadedRenderLoop *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QSGSoftwareThreadedRenderLoop")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "onAnimationStopped()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "onAnimationStopped()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  WindowData *QSGSoftwareThreadedRenderLoop::windowFor(QQuickWindow
//      *window)
extern "C" Q_DECL_EXPORT
QSGSoftwareThreadedRenderLoop::WindowData *ritual_ZN29QSGSoftwareThreadedRenderLoop9windowForEP12QQuickWindow(
    QSGSoftwareThreadedRenderLoop *self,
    QQuickWindow *window) {
  return self->windowFor(window);
}

//  void QSGSoftwareThreadedRenderLoop::startOrStopAnimationTimer()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QSGSoftwareThreadedRenderLoop25startOrStopAnimationTimerEv(
    QSGSoftwareThreadedRenderLoop *self) {
  self->startOrStopAnimationTimer();
}

//  a Python function taken by a CuteQSGSoftwareThreadedRenderLoop, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSGSoftwareThreadedRenderLoop(
    QSGSoftwareThreadedRenderLoop *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSGSoftwareThreadedRenderLoop *>(self)->take(key, call);
}

//  void QSGSoftwareThreadedRenderLoop::show(QQuickWindow *window)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN29QSGSoftwareThreadedRenderLoop4showEP12QQuickWindow(
    QSGSoftwareThreadedRenderLoop *self,
    QQuickWindow *window) {
  self->QSGSoftwareThreadedRenderLoop::show(window);
}

//  void QSGSoftwareThreadedRenderLoop::hide(QQuickWindow *window)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN29QSGSoftwareThreadedRenderLoop4hideEP12QQuickWindow(
    QSGSoftwareThreadedRenderLoop *self,
    QQuickWindow *window) {
  self->QSGSoftwareThreadedRenderLoop::hide(window);
}

//  void QSGSoftwareThreadedRenderLoop::resize(QQuickWindow *window)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN29QSGSoftwareThreadedRenderLoop6resizeEP12QQuickWindow(
    QSGSoftwareThreadedRenderLoop *self,
    QQuickWindow *window) {
  self->QSGSoftwareThreadedRenderLoop::resize(window);
}

//  void QSGSoftwareThreadedRenderLoop::windowDestroyed(QQuickWindow *window)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN29QSGSoftwareThreadedRenderLoop15windowDestroyedEP12QQuickWindow(
    QSGSoftwareThreadedRenderLoop *self,
    QQuickWindow *window) {
  self->QSGSoftwareThreadedRenderLoop::windowDestroyed(window);
}

//  void QSGSoftwareThreadedRenderLoop::update(QQuickWindow *window)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN29QSGSoftwareThreadedRenderLoop6updateEP12QQuickWindow(
    QSGSoftwareThreadedRenderLoop *self,
    QQuickWindow *window) {
  self->QSGSoftwareThreadedRenderLoop::update(window);
}

//  void QSGSoftwareThreadedRenderLoop::maybeUpdate(QQuickWindow *window)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN29QSGSoftwareThreadedRenderLoop11maybeUpdateEP12QQuickWindow(
    QSGSoftwareThreadedRenderLoop *self,
    QQuickWindow *window) {
  self->QSGSoftwareThreadedRenderLoop::maybeUpdate(window);
}

//  QAnimationDriver *QSGSoftwareThreadedRenderLoop::animationDriver() const
extern "C" Q_DECL_EXPORT
QAnimationDriver *ritual_own_ZNK29QSGSoftwareThreadedRenderLoop15animationDriverEv(
    const QSGSoftwareThreadedRenderLoop *self) {
  return self->QSGSoftwareThreadedRenderLoop::animationDriver();
}

//  QSGContext *QSGSoftwareThreadedRenderLoop::sceneGraphContext() const
extern "C" Q_DECL_EXPORT
QSGContext *ritual_own_ZNK29QSGSoftwareThreadedRenderLoop17sceneGraphContextEv(
    const QSGSoftwareThreadedRenderLoop *self) {
  return self->QSGSoftwareThreadedRenderLoop::sceneGraphContext();
}

//  QSGRenderContext
//      *QSGSoftwareThreadedRenderLoop::createRenderContext(QSGContext *a0)
//      const
extern "C" Q_DECL_EXPORT
QSGRenderContext *ritual_own_ZNK29QSGSoftwareThreadedRenderLoop19createRenderContextEP10QSGContext(
    const QSGSoftwareThreadedRenderLoop *self,
    QSGContext *a0) {
  return self->QSGSoftwareThreadedRenderLoop::createRenderContext(a0);
}

//  void QSGSoftwareThreadedRenderLoop::releaseResources(QQuickWindow
//      *window)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN29QSGSoftwareThreadedRenderLoop16releaseResourcesEP12QQuickWindow(
    QSGSoftwareThreadedRenderLoop *self,
    QQuickWindow *window) {
  self->QSGSoftwareThreadedRenderLoop::releaseResources(window);
}

//  void QSGSoftwareThreadedRenderLoop::postJob(QQuickWindow *window,
//      QRunnable *job)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN29QSGSoftwareThreadedRenderLoop7postJobEP12QQuickWindowP9QRunnable(
    QSGSoftwareThreadedRenderLoop *self,
    QQuickWindow *window,
    QRunnable *job) {
  self->QSGSoftwareThreadedRenderLoop::postJob(window, job);
}

//  QSurface::SurfaceType QSGSoftwareThreadedRenderLoop::windowSurfaceType()
//      const
extern "C" Q_DECL_EXPORT
QSurface::SurfaceType ritual_own_ZNK29QSGSoftwareThreadedRenderLoop17windowSurfaceTypeEv(
    const QSGSoftwareThreadedRenderLoop *self) {
  return self->QSGSoftwareThreadedRenderLoop::windowSurfaceType();
}

//  bool QSGSoftwareThreadedRenderLoop::interleaveIncubation() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK29QSGSoftwareThreadedRenderLoop20interleaveIncubationEv(
    const QSGSoftwareThreadedRenderLoop *self) {
  return self->QSGSoftwareThreadedRenderLoop::interleaveIncubation();
}

//  int QSGSoftwareThreadedRenderLoop::flags() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK29QSGSoftwareThreadedRenderLoop5flagsEv(
    const QSGSoftwareThreadedRenderLoop *self) {
  return self->QSGSoftwareThreadedRenderLoop::flags();
}

//  bool QSGSoftwareThreadedRenderLoop::event(QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN29QSGSoftwareThreadedRenderLoop5eventEP6QEvent(
    QSGSoftwareThreadedRenderLoop *self,
    QEvent *e) {
  return self->QSGSoftwareThreadedRenderLoop::event(e);
}

#endif  // QT_CONFIG(thread)
