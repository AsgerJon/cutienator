//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgthreadedrenderloop_p.h, Qt 6.12.0.
//  Changes made here are lost.
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
#include <qpa/qwindowsysteminterface.h>
#include <QtQuick/QQuickWindow>
#include <private/qquickwindow_p.h>
#include <private/qquickitem_p.h>
#include <QtGui/qpa/qplatformwindow_p.h>
#include <QtQuick/private/qsgrenderer_p.h>
#include "qsgthreadedrenderloop_p.h"
#include "qsgrhisupport_p.h"
#include <private/qquickanimatorcontroller_p.h>
#include <private/qquickprofiler_p.h>
#include <private/qqmldebugserviceinterfaces_p.h>
#include <private/qqmldebugconnector_p.h>
#include <private/qsgrhishadereffectnode_p.h>
#include <private/qsgdefaultrendercontext_p.h>
#ifdef Q_OS_DARWIN
#include <QtCore/private/qcore_mac_p.h>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quick/scenegraph/qsgthreadedrenderloop.cpp, line 107, as _ZN21QSGThreadedRenderLoop9windowForEP12QQuickWindow
inline QSGThreadedRenderLoop::Window *QSGThreadedRenderLoop::windowFor(QQuickWindow *window)
{
    for (const auto &t : std::as_const(m_windows)) {
        if (t.window == window)
            return const_cast<Window *>(&t);
    }
    return nullptr;
}

//  from ../qtdeclarative/src/quick/scenegraph/qsgthreadedrenderloop.cpp, line 1023, as _ZN21QSGThreadedRenderLoopD1Ev
inline QSGThreadedRenderLoop::~QSGThreadedRenderLoop()
{
    qDeleteAll(pendingRenderContexts);
    delete sg;
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

//  from ../qtdeclarative/src/quick/scenegraph/qsgthreadedrenderloop.cpp, line 1416, as _ZN21QSGThreadedRenderLoop11maybeUpdateEP12QQuickWindow
inline void QSGThreadedRenderLoop::maybeUpdate(QQuickWindow *window)
{
    Window *w = windowFor(window);
    if (w)
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

//  from ../qtdeclarative/src/quick/scenegraph/qsgthreadedrenderloop.cpp, line 1061, as _ZNK21QSGThreadedRenderLoop20interleaveIncubationEv
inline bool QSGThreadedRenderLoop::interleaveIncubation() const
{
    return m_animation_driver->isRunning() && anyoneShowing();
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

//  void QSGThreadedRenderLoop::exposureChanged(QQuickWindow *window)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSGThreadedRenderLoop15exposureChangedEP12QQuickWindow(
    QSGThreadedRenderLoop *self,
    QQuickWindow *window) {
  self->exposureChanged(window);
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

//  bool QSGThreadedRenderLoop::interleaveIncubation() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QSGThreadedRenderLoop20interleaveIncubationEv(
    const QSGThreadedRenderLoop *self) {
  return self->interleaveIncubation();
}

//  bool QSGThreadedRenderLoop::anyoneShowing() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QSGThreadedRenderLoop13anyoneShowingEv(
    const QSGThreadedRenderLoop *self) {
  return self->anyoneShowing();
}

//  void QSGThreadedRenderLoop::releaseSwapchain(QQuickWindow *window)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSGThreadedRenderLoop16releaseSwapchainEP12QQuickWindow(
    QSGThreadedRenderLoop *self,
    QQuickWindow *window) {
  self->releaseSwapchain(window);
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

//  bool QSGThreadedRenderLoop::interleaveIncubation() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK21QSGThreadedRenderLoop20interleaveIncubationEv(
    const QSGThreadedRenderLoop *self) {
  return self->QSGThreadedRenderLoop::interleaveIncubation();
}
