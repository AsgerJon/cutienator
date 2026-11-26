//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgsoftwarerenderloop_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgsoftwarerenderloop_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qimage.h>
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
#include <QtQuick/private/qsgsoftwarerenderloop_p.h>
#include <QtQuick/private/qsgsoftwarecontext_p.h>
#include <QtCore/QCoreApplication>
#include <QtQuick/private/qquickwindow_p.h>
#include <QtQuick/private/qquickitem_p.h>
#include <QtCore/QElapsedTimer>
#include <QtQuick/private/qquickanimatorcontroller_p.h>
#include <QtQuick/private/qquickprofiler_p.h>
#include <QtQuick/private/qsgsoftwarerenderer_p.h>
#include <QtGui/qpa/qplatformbackingstore.h>
#include <QtGui/QBackingStore>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarecontext.cpp, line 35, as _ZN18QSGSoftwareContextC1EP7QObject
inline QSGSoftwareContext::QSGSoftwareContext(QObject *parent)
    : QSGContext(parent)
{
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarerenderloop.cpp, line 232, as _ZN21QSGSoftwareRenderLoop11maybeUpdateEP12QQuickWindow
inline void QSGSoftwareRenderLoop::maybeUpdate(QQuickWindow *window)
{
    if (!m_windows.contains(window))
        return;

    m_windows[window].updatePending = true;
    window->requestUpdate();
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarerenderloop.cpp, line 40, as _ZN21QSGSoftwareRenderLoop4showEP12QQuickWindow
inline void QSGSoftwareRenderLoop::show(QQuickWindow *window)
{
    WindowData data;
    data.updatePending = false;
    data.grabOnly = false;
    m_windows[window] = data;

    if (m_backingStores[window] == nullptr) {
        m_backingStores[window] = new QBackingStore(window);
    }

    maybeUpdate(window);
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarerenderloop.cpp, line 54, as _ZN21QSGSoftwareRenderLoop4hideEP12QQuickWindow
inline void QSGSoftwareRenderLoop::hide(QQuickWindow *window)
{
    QQuickWindowPrivate *cd = QQuickWindowPrivate::get(window);
    cd->fireAboutToStop();
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarerenderloop.cpp, line 60, as _ZN21QSGSoftwareRenderLoop15windowDestroyedEP12QQuickWindow
inline void QSGSoftwareRenderLoop::windowDestroyed(QQuickWindow *window)
{
    m_windows.remove(window);
    delete m_backingStores[window];
    m_backingStores.remove(window);
    hide(window);

    QQuickWindowPrivate *d = QQuickWindowPrivate::get(window);
    d->cleanupNodesOnShutdown();

    if (m_windows.size() == 0) {
        rc->invalidate();
    }

    d->animationController.reset();
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarerenderloop.cpp, line 196, as _ZN21QSGSoftwareRenderLoop15exposureChangedEP12QQuickWindow
inline void QSGSoftwareRenderLoop::exposureChanged(QQuickWindow *window)
{
    if (window->isExposed()) {
        m_windows[window].updatePending = true;
        renderWindow(window, true);
    }
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarerenderloop.cpp, line 204, as _ZN21QSGSoftwareRenderLoop4grabEP12QQuickWindow
inline QImage QSGSoftwareRenderLoop::grab(QQuickWindow *window)
{
    //If the window was never shown, create a new backing store
    if (!m_backingStores.contains(window)) {
        m_backingStores[window] = new QBackingStore(window);
        // Call create on window to make sure platform window is created
        window->create();
    }

    //If there is no WindowData, add one
    if (!m_windows.contains(window)) {
        WindowData data;
        data.updatePending = false;
        m_windows[window] = data;
    }

    m_windows[window].grabOnly = true;

    renderWindow(window);

    QImage grabbed = grabContent;
    grabbed.detach();
    grabContent = QImage();
    return grabbed;
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarerenderloop.cpp, line 254, as _ZN21QSGSoftwareRenderLoop19handleUpdateRequestEP12QQuickWindow
inline void QSGSoftwareRenderLoop::handleUpdateRequest(QQuickWindow *window)
{
    renderWindow(window);
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarerenderloop.cpp, line 241, as _ZNK21QSGSoftwareRenderLoop17windowSurfaceTypeEv
inline QSurface::SurfaceType QSGSoftwareRenderLoop::windowSurfaceType() const
{
    return QSurface::RasterSurface;
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarerenderloop.cpp, line 248, as _ZNK21QSGSoftwareRenderLoop17sceneGraphContextEv
inline QSGContext *QSGSoftwareRenderLoop::sceneGraphContext() const
{
    return sg;
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarerenderloop.cpp, line 34, as _ZN21QSGSoftwareRenderLoopD1Ev
inline QSGSoftwareRenderLoop::~QSGSoftwareRenderLoop()
{
    delete rc;
    delete sg;
}
//  -----------------------------------------------------------------------

//  A QSGSoftwareRenderLoop that Python can take functions over in. Every QSGSoftwareRenderLoop
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQSGSoftwareRenderLoopCall0)(const void *, QQuickWindow *, int *);
typedef void (*CuteQSGSoftwareRenderLoopCall1)(const void *, QQuickWindow *, int *);
typedef void (*CuteQSGSoftwareRenderLoopCall2)(const void *, QQuickWindow *, int *);
typedef void (*CuteQSGSoftwareRenderLoopCall3)(const void *, QQuickWindow *, int *);
typedef const QImage * (*CuteQSGSoftwareRenderLoopCall4)(const void *, QQuickWindow *, int *);
typedef void (*CuteQSGSoftwareRenderLoopCall5)(const void *, QQuickWindow *, int *);
typedef void (*CuteQSGSoftwareRenderLoopCall6)(const void *, QQuickWindow *, int *);
typedef void (*CuteQSGSoftwareRenderLoopCall7)(const void *, QQuickWindow *, int *);
typedef void (*CuteQSGSoftwareRenderLoopCall8)(const void *, QQuickWindow *, int *);
typedef int (*CuteQSGSoftwareRenderLoopCall9)(const void *, int *);
typedef void * (*CuteQSGSoftwareRenderLoopCall10)(const void *, int *);
typedef void * (*CuteQSGSoftwareRenderLoopCall11)(const void *, int *);
typedef void * (*CuteQSGSoftwareRenderLoopCall12)(const void *, QSGContext *, int *);
typedef void (*CuteQSGSoftwareRenderLoopCall13)(const void *, QQuickWindow *, int *);
typedef void (*CuteQSGSoftwareRenderLoopCall14)(const void *, QQuickWindow *, QRunnable *, int *);
typedef bool (*CuteQSGSoftwareRenderLoopCall15)(const void *, int *);
typedef int (*CuteQSGSoftwareRenderLoopCall16)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSGSoftwareRenderLoopCall17)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSGSoftwareRenderLoopCall18)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGSoftwareRenderLoopCall19)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGSoftwareRenderLoopCall20)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGSoftwareRenderLoopCall21)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGSoftwareRenderLoopCall22)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGSoftwareRenderLoopCall23)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQSGSoftwareRenderLoop : public QSGSoftwareRenderLoop {
public:
  using QSGSoftwareRenderLoop::QSGSoftwareRenderLoop;
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
    if (!std::strcmp(key, "_ZN13QSGRenderLoop15windowDestroyedEP12QQuickWindow")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QSGRenderLoop15exposureChangedEP12QQuickWindow")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QSGRenderLoop4grabEP12QQuickWindow")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QSGRenderLoop11maybeUpdateEP12QQuickWindow")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QSGRenderLoop6updateEP12QQuickWindow")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QSGRenderLoop19handleUpdateRequestEP12QQuickWindow")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QSGRenderLoop16releaseResourcesEP12QQuickWindow")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK13QSGRenderLoop17windowSurfaceTypeEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK13QSGRenderLoop15animationDriverEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK13QSGRenderLoop17sceneGraphContextEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK13QSGRenderLoop19createRenderContextEP10QSGContext")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QSGRenderLoop6resizeEP12QQuickWindow")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QSGRenderLoop7postJobEP12QQuickWindowP9QRunnable")) {
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

  //  void QSGSoftwareRenderLoop::show(QQuickWindow *window)
  void show(QQuickWindow *window) override {
    if (taken[0]) {
      int handled = 0;
      CuteQSGSoftwareRenderLoopCall0 call = reinterpret_cast<CuteQSGSoftwareRenderLoopCall0>(taken[0]);
      call(this, window, &handled);
      if (handled) return;
    }
    QSGSoftwareRenderLoop::show(window);
  }

  //  void QSGSoftwareRenderLoop::hide(QQuickWindow *window)
  void hide(QQuickWindow *window) override {
    if (taken[1]) {
      int handled = 0;
      CuteQSGSoftwareRenderLoopCall1 call = reinterpret_cast<CuteQSGSoftwareRenderLoopCall1>(taken[1]);
      call(this, window, &handled);
      if (handled) return;
    }
    QSGSoftwareRenderLoop::hide(window);
  }

  //  void QSGSoftwareRenderLoop::windowDestroyed(QQuickWindow *window)
  void windowDestroyed(QQuickWindow *window) override {
    if (taken[2]) {
      int handled = 0;
      CuteQSGSoftwareRenderLoopCall2 call = reinterpret_cast<CuteQSGSoftwareRenderLoopCall2>(taken[2]);
      call(this, window, &handled);
      if (handled) return;
    }
    QSGSoftwareRenderLoop::windowDestroyed(window);
  }

  //  void QSGSoftwareRenderLoop::exposureChanged(QQuickWindow *window)
  void exposureChanged(QQuickWindow *window) override {
    if (taken[3]) {
      int handled = 0;
      CuteQSGSoftwareRenderLoopCall3 call = reinterpret_cast<CuteQSGSoftwareRenderLoopCall3>(taken[3]);
      call(this, window, &handled);
      if (handled) return;
    }
    QSGSoftwareRenderLoop::exposureChanged(window);
  }

  //  QImage QSGSoftwareRenderLoop::grab(QQuickWindow *window)
  QImage grab(QQuickWindow *window) override {
    if (taken[4]) {
      int handled = 0;
      CuteQSGSoftwareRenderLoopCall4 call = reinterpret_cast<CuteQSGSoftwareRenderLoopCall4>(taken[4]);
      const QImage * given = call(this, window, &handled);
      if (handled && given) return *given;
    }
    return QSGSoftwareRenderLoop::grab(window);
  }

  //  void QSGSoftwareRenderLoop::maybeUpdate(QQuickWindow *window)
  void maybeUpdate(QQuickWindow *window) override {
    if (taken[5]) {
      int handled = 0;
      CuteQSGSoftwareRenderLoopCall5 call = reinterpret_cast<CuteQSGSoftwareRenderLoopCall5>(taken[5]);
      call(this, window, &handled);
      if (handled) return;
    }
    QSGSoftwareRenderLoop::maybeUpdate(window);
  }

  //  void QSGSoftwareRenderLoop::update(QQuickWindow *window)
  void update(QQuickWindow *window) override {
    if (taken[6]) {
      int handled = 0;
      CuteQSGSoftwareRenderLoopCall6 call = reinterpret_cast<CuteQSGSoftwareRenderLoopCall6>(taken[6]);
      call(this, window, &handled);
      if (handled) return;
    }
    QSGSoftwareRenderLoop::update(window);
  }

  //  void QSGSoftwareRenderLoop::handleUpdateRequest(QQuickWindow *a0)
  void handleUpdateRequest(QQuickWindow *a0) override {
    if (taken[7]) {
      int handled = 0;
      CuteQSGSoftwareRenderLoopCall7 call = reinterpret_cast<CuteQSGSoftwareRenderLoopCall7>(taken[7]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QSGSoftwareRenderLoop::handleUpdateRequest(a0);
  }

  //  void QSGSoftwareRenderLoop::releaseResources(QQuickWindow *a0)
  void releaseResources(QQuickWindow *a0) override {
    if (taken[8]) {
      int handled = 0;
      CuteQSGSoftwareRenderLoopCall8 call = reinterpret_cast<CuteQSGSoftwareRenderLoopCall8>(taken[8]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QSGSoftwareRenderLoop::releaseResources(a0);
  }

  //  QSurface::SurfaceType QSGSoftwareRenderLoop::windowSurfaceType()
  //      const
  QSurface::SurfaceType windowSurfaceType() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQSGSoftwareRenderLoopCall9 call = reinterpret_cast<CuteQSGSoftwareRenderLoopCall9>(taken[9]);
      int given = call(this, &handled);
      if (handled) return static_cast<QSurface::SurfaceType>(given);
    }
    return QSGSoftwareRenderLoop::windowSurfaceType();
  }

  //  QAnimationDriver *QSGSoftwareRenderLoop::animationDriver() const
  QAnimationDriver *animationDriver() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQSGSoftwareRenderLoopCall10 call = reinterpret_cast<CuteQSGSoftwareRenderLoopCall10>(taken[10]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAnimationDriver *>(given);
    }
    return QSGSoftwareRenderLoop::animationDriver();
  }

  //  QSGContext *QSGSoftwareRenderLoop::sceneGraphContext() const
  QSGContext *sceneGraphContext() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQSGSoftwareRenderLoopCall11 call = reinterpret_cast<CuteQSGSoftwareRenderLoopCall11>(taken[11]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGContext *>(given);
    }
    return QSGSoftwareRenderLoop::sceneGraphContext();
  }

  //  QSGRenderContext
  //      *QSGSoftwareRenderLoop::createRenderContext(QSGContext *a0) const
  QSGRenderContext *createRenderContext(QSGContext *a0) const override {
    if (taken[12]) {
      int handled = 0;
      CuteQSGSoftwareRenderLoopCall12 call = reinterpret_cast<CuteQSGSoftwareRenderLoopCall12>(taken[12]);
      void * given = call(this, a0, &handled);
      if (handled) return static_cast<QSGRenderContext *>(given);
    }
    return QSGSoftwareRenderLoop::createRenderContext(a0);
  }

  //  void QSGRenderLoop::resize(QQuickWindow *a0)
  void resize(QQuickWindow *a0) override {
    if (taken[13]) {
      int handled = 0;
      CuteQSGSoftwareRenderLoopCall13 call = reinterpret_cast<CuteQSGSoftwareRenderLoopCall13>(taken[13]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QSGRenderLoop::resize(a0);
  }

  //  void QSGRenderLoop::postJob(QQuickWindow *window, QRunnable *job)
  void postJob(QQuickWindow *window, QRunnable *job) override {
    if (taken[14]) {
      int handled = 0;
      CuteQSGSoftwareRenderLoopCall14 call = reinterpret_cast<CuteQSGSoftwareRenderLoopCall14>(taken[14]);
      call(this, window, job, &handled);
      if (handled) return;
    }
    QSGRenderLoop::postJob(window, job);
  }

  //  bool QSGRenderLoop::interleaveIncubation() const
  bool interleaveIncubation() const override {
    if (taken[15]) {
      int handled = 0;
      CuteQSGSoftwareRenderLoopCall15 call = reinterpret_cast<CuteQSGSoftwareRenderLoopCall15>(taken[15]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSGRenderLoop::interleaveIncubation();
  }

  //  int QSGRenderLoop::flags() const
  int flags() const override {
    if (taken[16]) {
      int handled = 0;
      CuteQSGSoftwareRenderLoopCall16 call = reinterpret_cast<CuteQSGSoftwareRenderLoopCall16>(taken[16]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QSGRenderLoop::flags();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQSGSoftwareRenderLoopCall17 call = reinterpret_cast<CuteQSGSoftwareRenderLoopCall17>(taken[17]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQSGSoftwareRenderLoopCall18 call = reinterpret_cast<CuteQSGSoftwareRenderLoopCall18>(taken[18]);
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
      CuteQSGSoftwareRenderLoopCall19 call = reinterpret_cast<CuteQSGSoftwareRenderLoopCall19>(taken[19]);
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
      CuteQSGSoftwareRenderLoopCall20 call = reinterpret_cast<CuteQSGSoftwareRenderLoopCall20>(taken[20]);
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
      CuteQSGSoftwareRenderLoopCall21 call = reinterpret_cast<CuteQSGSoftwareRenderLoopCall21>(taken[21]);
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
      CuteQSGSoftwareRenderLoopCall22 call = reinterpret_cast<CuteQSGSoftwareRenderLoopCall22>(taken[22]);
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
      CuteQSGSoftwareRenderLoopCall23 call = reinterpret_cast<CuteQSGSoftwareRenderLoopCall23>(taken[23]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QSGSoftwareRenderLoop::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21QSGSoftwareRenderLoop10metaObjectEv(
    const QSGSoftwareRenderLoop *self) {
  return self->metaObject();
}

//  void *QSGSoftwareRenderLoop::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN21QSGSoftwareRenderLoop11qt_metacastEPKc(
    QSGSoftwareRenderLoop *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QSGSoftwareRenderLoop::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN21QSGSoftwareRenderLoop11qt_metacallEN11QMetaObject4CallEiPPv(
    QSGSoftwareRenderLoop *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QSGSoftwareRenderLoop::~QSGSoftwareRenderLoop()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSGSoftwareRenderLoopD1Ev(QSGSoftwareRenderLoop *self) {
  delete self;
}

//  void QSGSoftwareRenderLoop::show(QQuickWindow *window)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSGSoftwareRenderLoop4showEP12QQuickWindow(
    QSGSoftwareRenderLoop *self,
    QQuickWindow *window) {
  self->show(window);
}

//  void QSGSoftwareRenderLoop::hide(QQuickWindow *window)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSGSoftwareRenderLoop4hideEP12QQuickWindow(
    QSGSoftwareRenderLoop *self,
    QQuickWindow *window) {
  self->hide(window);
}

//  void QSGSoftwareRenderLoop::windowDestroyed(QQuickWindow *window)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSGSoftwareRenderLoop15windowDestroyedEP12QQuickWindow(
    QSGSoftwareRenderLoop *self,
    QQuickWindow *window) {
  self->windowDestroyed(window);
}

//  void QSGSoftwareRenderLoop::exposureChanged(QQuickWindow *window)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSGSoftwareRenderLoop15exposureChangedEP12QQuickWindow(
    QSGSoftwareRenderLoop *self,
    QQuickWindow *window) {
  self->exposureChanged(window);
}

//  QImage QSGSoftwareRenderLoop::grab(QQuickWindow *window)
extern "C" Q_DECL_EXPORT
QImage *ritual_ZN21QSGSoftwareRenderLoop4grabEP12QQuickWindow(
    QSGSoftwareRenderLoop *self,
    QQuickWindow *window) {
  return new QImage(self->grab(window));
}

//  void QSGSoftwareRenderLoop::maybeUpdate(QQuickWindow *window)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSGSoftwareRenderLoop11maybeUpdateEP12QQuickWindow(
    QSGSoftwareRenderLoop *self,
    QQuickWindow *window) {
  self->maybeUpdate(window);
}

//  void QSGSoftwareRenderLoop::update(QQuickWindow *window)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSGSoftwareRenderLoop6updateEP12QQuickWindow(
    QSGSoftwareRenderLoop *self,
    QQuickWindow *window) {
  self->update(window);
}

//  void QSGSoftwareRenderLoop::handleUpdateRequest(QQuickWindow *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSGSoftwareRenderLoop19handleUpdateRequestEP12QQuickWindow(
    QSGSoftwareRenderLoop *self,
    QQuickWindow *a0) {
  self->handleUpdateRequest(a0);
}

//  void QSGSoftwareRenderLoop::releaseResources(QQuickWindow *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSGSoftwareRenderLoop16releaseResourcesEP12QQuickWindow(
    QSGSoftwareRenderLoop *self,
    QQuickWindow *a0) {
  self->releaseResources(a0);
}

//  QSurface::SurfaceType QSGSoftwareRenderLoop::windowSurfaceType() const
extern "C" Q_DECL_EXPORT
QSurface::SurfaceType ritual_ZNK21QSGSoftwareRenderLoop17windowSurfaceTypeEv(
    const QSGSoftwareRenderLoop *self) {
  return self->windowSurfaceType();
}

//  QAnimationDriver *QSGSoftwareRenderLoop::animationDriver() const
extern "C" Q_DECL_EXPORT
QAnimationDriver *ritual_ZNK21QSGSoftwareRenderLoop15animationDriverEv(
    const QSGSoftwareRenderLoop *self) {
  return self->animationDriver();
}

//  QSGContext *QSGSoftwareRenderLoop::sceneGraphContext() const
extern "C" Q_DECL_EXPORT
QSGContext *ritual_ZNK21QSGSoftwareRenderLoop17sceneGraphContextEv(
    const QSGSoftwareRenderLoop *self) {
  return self->sceneGraphContext();
}

//  QSGRenderContext *QSGSoftwareRenderLoop::createRenderContext(QSGContext
//      *a0) const
extern "C" Q_DECL_EXPORT
QSGRenderContext *ritual_ZNK21QSGSoftwareRenderLoop19createRenderContextEP10QSGContext(
    const QSGSoftwareRenderLoop *self,
    QSGContext *a0) {
  return self->createRenderContext(a0);
}

//  a Python function taken by a CuteQSGSoftwareRenderLoop, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSGSoftwareRenderLoop(
    QSGSoftwareRenderLoop *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSGSoftwareRenderLoop *>(self)->take(key, call);
}

//  void QSGSoftwareRenderLoop::show(QQuickWindow *window)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QSGSoftwareRenderLoop4showEP12QQuickWindow(
    QSGSoftwareRenderLoop *self,
    QQuickWindow *window) {
  self->QSGSoftwareRenderLoop::show(window);
}

//  void QSGSoftwareRenderLoop::hide(QQuickWindow *window)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QSGSoftwareRenderLoop4hideEP12QQuickWindow(
    QSGSoftwareRenderLoop *self,
    QQuickWindow *window) {
  self->QSGSoftwareRenderLoop::hide(window);
}

//  void QSGSoftwareRenderLoop::windowDestroyed(QQuickWindow *window)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QSGSoftwareRenderLoop15windowDestroyedEP12QQuickWindow(
    QSGSoftwareRenderLoop *self,
    QQuickWindow *window) {
  self->QSGSoftwareRenderLoop::windowDestroyed(window);
}

//  void QSGSoftwareRenderLoop::maybeUpdate(QQuickWindow *window)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QSGSoftwareRenderLoop11maybeUpdateEP12QQuickWindow(
    QSGSoftwareRenderLoop *self,
    QQuickWindow *window) {
  self->QSGSoftwareRenderLoop::maybeUpdate(window);
}

//  void QSGSoftwareRenderLoop::update(QQuickWindow *window)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QSGSoftwareRenderLoop6updateEP12QQuickWindow(
    QSGSoftwareRenderLoop *self,
    QQuickWindow *window) {
  self->QSGSoftwareRenderLoop::update(window);
}

//  void QSGSoftwareRenderLoop::releaseResources(QQuickWindow *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QSGSoftwareRenderLoop16releaseResourcesEP12QQuickWindow(
    QSGSoftwareRenderLoop *self,
    QQuickWindow *a0) {
  self->QSGSoftwareRenderLoop::releaseResources(a0);
}

//  QSurface::SurfaceType QSGSoftwareRenderLoop::windowSurfaceType() const
extern "C" Q_DECL_EXPORT
QSurface::SurfaceType ritual_own_ZNK21QSGSoftwareRenderLoop17windowSurfaceTypeEv(
    const QSGSoftwareRenderLoop *self) {
  return self->QSGSoftwareRenderLoop::windowSurfaceType();
}

//  QAnimationDriver *QSGSoftwareRenderLoop::animationDriver() const
extern "C" Q_DECL_EXPORT
QAnimationDriver *ritual_own_ZNK21QSGSoftwareRenderLoop15animationDriverEv(
    const QSGSoftwareRenderLoop *self) {
  return self->QSGSoftwareRenderLoop::animationDriver();
}

//  QSGContext *QSGSoftwareRenderLoop::sceneGraphContext() const
extern "C" Q_DECL_EXPORT
QSGContext *ritual_own_ZNK21QSGSoftwareRenderLoop17sceneGraphContextEv(
    const QSGSoftwareRenderLoop *self) {
  return self->QSGSoftwareRenderLoop::sceneGraphContext();
}

//  QSGRenderContext *QSGSoftwareRenderLoop::createRenderContext(QSGContext
//      *a0) const
extern "C" Q_DECL_EXPORT
QSGRenderContext *ritual_own_ZNK21QSGSoftwareRenderLoop19createRenderContextEP10QSGContext(
    const QSGSoftwareRenderLoop *self,
    QSGContext *a0) {
  return self->QSGSoftwareRenderLoop::createRenderContext(a0);
}
