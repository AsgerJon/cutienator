//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgsoftwarethreadedrenderloop_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgsoftwarethreadedrenderloop_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qimage.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qsgsoftwarethreadedrenderloop_p.h"
#include "qsgsoftwarecontext_p.h"
#include "qsgsoftwarerenderer_p.h"
#include <private/qsgrenderer_p.h>
#include <private/qquickwindow_p.h>
#include <private/qquickitem_p.h>
#include <private/qquickprofiler_p.h>
#include <private/qquickanimatorcontroller_p.h>
#include <private/qquickprofiler_p.h>
#include <private/qqmldebugserviceinterfaces_p.h>
#include <private/qqmldebugconnector_p.h>
#include <qpa/qplatformbackingstore.h>
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

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarethreadedrenderloop.cpp, line 507, as _ZN29QSGSoftwareThreadedRenderLoop9windowForEP12QQuickWindow
inline QSGSoftwareThreadedRenderLoop::WindowData *QSGSoftwareThreadedRenderLoop::windowFor(QQuickWindow *window)
{
    for (const auto &t : std::as_const(m_windows)) {
        if (t.window == window)
            return const_cast<WindowData *>(&t);
    }
    return nullptr;
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarethreadedrenderloop.cpp, line 656, as _ZN29QSGSoftwareThreadedRenderLoop11maybeUpdateEP12QQuickWindow
inline void QSGSoftwareThreadedRenderLoop::maybeUpdate(QQuickWindow *window)
{
    WindowData *w = windowFor(window);
    if (w)
        scheduleUpdate(w);
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

//  void QSGSoftwareThreadedRenderLoop::maybeUpdate(QQuickWindow *window)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QSGSoftwareThreadedRenderLoop11maybeUpdateEP12QQuickWindow(
    QSGSoftwareThreadedRenderLoop *self,
    QQuickWindow *window) {
  self->maybeUpdate(window);
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

//  a Python function taken by a CuteQSGSoftwareThreadedRenderLoop, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSGSoftwareThreadedRenderLoop(
    QSGSoftwareThreadedRenderLoop *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSGSoftwareThreadedRenderLoop *>(self)->take(key, call);
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
