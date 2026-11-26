//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickanimatorcontroller_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickanimatorcontroller_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/private/qquickanimatorcontroller_p.h>
#include <QtQuick/private/qquickitem_p.h>
#include <QtQuick/private/qsgrenderloop_p.h>
#include <QtQml/private/qanimationgroupjob_p.h>
#include <QtGui/qscreen.h>
#include <QtCore/qcoreapplication.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quick/util/qquickanimatorcontroller.cpp, line 28, as local:qquickanimatorcontroller.cpp:qquickanimator_invalidate_jobs
static void qquickanimator_invalidate_jobs(QAbstractAnimationJob *job)
{
    if (job->isRenderThreadJob()) {
        static_cast<QQuickAnimatorJob *>(job)->invalidate();
    } else if (job->isGroup()) {
        for (QAbstractAnimationJob *a : *static_cast<QAnimationGroupJob *>(job)->children())
            qquickanimator_invalidate_jobs(a);
    }
}

//  from ../qtdeclarative/src/quick/util/qquickanimatorcontroller.cpp, line 80, as local:qquickanimatorcontroller.cpp:qquickanimator_sync_before_start
static void qquickanimator_sync_before_start(QAbstractAnimationJob *job)
{
    if (job->isRenderThreadJob()) {
        static_cast<QQuickAnimatorJob *>(job)->preSync();
    } else if (job->isGroup()) {
        for (QAbstractAnimationJob *a : *static_cast<QAnimationGroupJob *>(job)->children())
            qquickanimator_sync_before_start(a);
    }
}

//  from ../qtdeclarative/src/quick/util/qquickanimatorcontroller.cpp, line 134, as _ZN24QQuickAnimatorController17animationFinishedEP21QAbstractAnimationJob
inline void QQuickAnimatorController::animationFinished(QAbstractAnimationJob *job)
{
     m_animationRoots.remove(job);
}

//  from ../qtdeclarative/src/quick/util/qquickanimatorcontroller.cpp, line 139, as _ZN24QQuickAnimatorController21animationStateChangedEP21QAbstractAnimationJobNS0_5StateES2_
inline void QQuickAnimatorController::animationStateChanged(QAbstractAnimationJob *job,
                                                     QAbstractAnimationJob::State newState,
                                                     QAbstractAnimationJob::State oldState)
{
    Q_ASSERT(job->isRenderThreadJob());
    QQuickAnimatorJob *animator = static_cast<QQuickAnimatorJob *>(job);
    if (newState == QAbstractAnimationJob::Running) {
        m_runningAnimators.insert(animator);
    } else if (oldState == QAbstractAnimationJob::Running) {
        animator->commit();
        m_runningAnimators.remove(animator);
    }
}

//  from ../qtdeclarative/src/quick/util/qquickanimatorcontroller.cpp, line 19, as _ZN24QQuickAnimatorControllerD1Ev
inline QQuickAnimatorController::~QQuickAnimatorController()
{
}

//  from ../qtdeclarative/src/quick/util/qquickanimatorcontroller.cpp, line 63, as _ZN24QQuickAnimatorController7advanceEv
inline void QQuickAnimatorController::advance()
{
    bool running = false;
    for (const QSharedPointer<QAbstractAnimationJob> &job : std::as_const(m_animationRoots)) {
        if (job->isRunning()) {
            running = true;
            break;
        }
    }

    for (QQuickAnimatorJob *job : std::as_const(m_runningAnimators))
        job->commit();

    if (running)
        m_window->update();
}

//  from ../qtdeclarative/src/quick/util/qquickanimatorcontroller.cpp, line 90, as _ZN24QQuickAnimatorController14beforeNodeSyncEv
inline void QQuickAnimatorController::beforeNodeSync()
{
    for (const QSharedPointer<QAbstractAnimationJob> &toPause : std::as_const(m_rootsPendingPause)) {
        toPause->pause();
        m_animationRoots.remove(toPause.data());
    }
    m_rootsPendingPause.clear();
    for (const QSharedPointer<QAbstractAnimationJob> &toStop : std::as_const(m_rootsPendingStop)) {
        toStop->stop();
        m_animationRoots.remove(toStop.data());
    }
    m_rootsPendingStop.clear();


    for (QQuickAnimatorJob *job : std::as_const(m_runningAnimators))
        job->preSync();

    // Start pending jobs
    for (const QSharedPointer<QAbstractAnimationJob> &job : std::as_const(m_rootsPendingStart)) {
        Q_ASSERT(!job->isRunning());

        // We want to make sure that presync is called before
        // updateAnimationTime is called the very first time, so before
        // starting a tree of jobs, we go through it and call preSync on all
        // its animators.
        qquickanimator_sync_before_start(job.data());

        // The start the job..
        job->start();
        m_animationRoots.insert(job.data(), job);
    }
    m_rootsPendingStart.clear();

    // Issue an update directly on the window to force another render pass.
    if (m_animationRoots.size())
        m_window->update();
}

//  from ../qtdeclarative/src/quick/util/qquickanimatorcontroller.cpp, line 128, as _ZN24QQuickAnimatorController13afterNodeSyncEv
inline void QQuickAnimatorController::afterNodeSync()
{
    for (QQuickAnimatorJob *job : std::as_const(m_runningAnimators))
        job->postSync();
}

//  from ../qtdeclarative/src/quick/util/qquickanimatorcontroller.cpp, line 154, as _ZN24QQuickAnimatorController11requestSyncEv
inline void QQuickAnimatorController::requestSync()
{
    // Force a "sync" pass as the newly started animation needs to sync properties from GUI.
    m_window->maybeUpdate();
}

//  from ../qtdeclarative/src/quick/util/qquickanimatorcontroller.cpp, line 175, as _ZN24QQuickAnimatorController5startERK14QSharedPointerI21QAbstractAnimationJobE
inline void QQuickAnimatorController::start(const QSharedPointer<QAbstractAnimationJob> &job)
{
    m_rootsPendingStart.insert(job);
    m_rootsPendingPause.remove(job);
    m_rootsPendingStop.remove(job);
    job->addAnimationChangeListener(this, QAbstractAnimationJob::Completion);
    start_helper(job.data());
    requestSync();
}

//  from ../qtdeclarative/src/quick/util/qquickanimatorcontroller.cpp, line 186, as _ZN24QQuickAnimatorController6cancelERK14QSharedPointerI21QAbstractAnimationJobE
inline void QQuickAnimatorController::cancel(const QSharedPointer<QAbstractAnimationJob> &job)
{
    m_rootsPendingStart.remove(job);
    m_rootsPendingPause.remove(job);
    m_rootsPendingStop.insert(job);
}

//  from ../qtdeclarative/src/quick/util/qquickanimatorcontroller.cpp, line 194, as _ZN24QQuickAnimatorController5pauseERK14QSharedPointerI21QAbstractAnimationJobE
inline void QQuickAnimatorController::pause(const QSharedPointer<QAbstractAnimationJob> &job)
{
    m_rootsPendingStart.remove(job);
    m_rootsPendingStop.remove(job);
    m_rootsPendingPause.insert(job);
}

//  from ../qtdeclarative/src/quick/util/qquickanimatorcontroller.cpp, line 162, as _ZN24QQuickAnimatorController12start_helperEP21QAbstractAnimationJob
inline void QQuickAnimatorController::start_helper(QAbstractAnimationJob *job)
{
    if (job->isRenderThreadJob()) {
        QQuickAnimatorJob *j = static_cast<QQuickAnimatorJob *>(job);
        j->addAnimationChangeListener(this, QAbstractAnimationJob::StateChange);
        j->initialize(this);
    } else if (job->isGroup()) {
        for (QAbstractAnimationJob *a : *static_cast<QAnimationGroupJob *>(job)->children())
            start_helper(a);
    }
}
//  -----------------------------------------------------------------------

//  A QQuickAnimatorController that Python can take functions over in. Every QQuickAnimatorController
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(qml_animation)
typedef void (*CuteQQuickAnimatorControllerCall0)(const void *, QAbstractAnimationJob *, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQQuickAnimatorControllerCall1)(const void *, QAbstractAnimationJob *, int, int, int *);
#endif  // QT_CONFIG(qml_animation)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickAnimatorControllerCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickAnimatorControllerCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickAnimatorControllerCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickAnimatorControllerCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickAnimatorControllerCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickAnimatorControllerCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickAnimatorControllerCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQQuickAnimatorControllerCall9)(const void *, QAbstractAnimationJob *, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQQuickAnimatorControllerCall10)(const void *, QAbstractAnimationJob *, int, int *);
#endif  // QT_CONFIG(qml_animation)
class CuteQQuickAnimatorController : public QQuickAnimatorController {
public:
  using QQuickAnimatorController::QQuickAnimatorController;
  void *taken[11] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(qml_animation)
    if (!std::strcmp(key, "_ZN27QAnimationJobChangeListener17animationFinishedEP21QAbstractAnimationJob")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
    if (!std::strcmp(key, "_ZN27QAnimationJobChangeListener21animationStateChangedEP21QAbstractAnimationJobNS0_5StateES2_")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_animation)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(qml_animation)
    if (!std::strcmp(key, "_ZN27QAnimationJobChangeListener27animationCurrentLoopChangedEP21QAbstractAnimationJob")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
    if (!std::strcmp(key, "_ZN27QAnimationJobChangeListener27animationCurrentTimeChangedEP21QAbstractAnimationJobi")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_animation)
    return false;
  }

#if QT_CONFIG(qml_animation)
  //  void
  //      QQuickAnimatorController::animationFinished(QAbstractAnimationJob
  //      *job)
  void animationFinished(QAbstractAnimationJob *job) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickAnimatorControllerCall0 call = reinterpret_cast<CuteQQuickAnimatorControllerCall0>(taken[0]);
      call(this, job, &handled);
      if (handled) return;
    }
    QQuickAnimatorController::animationFinished(job);
  }
#endif  // QT_CONFIG(qml_animation)

#if QT_CONFIG(qml_animation)
  //  void
  //      QQuickAnimatorController::animationStateChanged(QAbstractAnimatio
  //      nJob *job, QAbstractAnimationJob::State newState,
  //      QAbstractAnimationJob::State oldState)
  void animationStateChanged(
      QAbstractAnimationJob *job,
      QAbstractAnimationJob::State newState,
      QAbstractAnimationJob::State oldState) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickAnimatorControllerCall1 call = reinterpret_cast<CuteQQuickAnimatorControllerCall1>(taken[1]);
      call(this, job, static_cast<int>(newState), static_cast<int>(oldState), &handled);
      if (handled) return;
    }
    QQuickAnimatorController::animationStateChanged(job, newState, oldState);
  }
#endif  // QT_CONFIG(qml_animation)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickAnimatorControllerCall2 call = reinterpret_cast<CuteQQuickAnimatorControllerCall2>(taken[2]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickAnimatorControllerCall3 call = reinterpret_cast<CuteQQuickAnimatorControllerCall3>(taken[3]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickAnimatorControllerCall4 call = reinterpret_cast<CuteQQuickAnimatorControllerCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickAnimatorControllerCall5 call = reinterpret_cast<CuteQQuickAnimatorControllerCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickAnimatorControllerCall6 call = reinterpret_cast<CuteQQuickAnimatorControllerCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickAnimatorControllerCall7 call = reinterpret_cast<CuteQQuickAnimatorControllerCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickAnimatorControllerCall8 call = reinterpret_cast<CuteQQuickAnimatorControllerCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if QT_CONFIG(qml_animation)
  //  void QAnimationJobChangeListener::animationCurrentLoopChanged(QAbstra
  //      ctAnimationJob *a0)
  void animationCurrentLoopChanged(QAbstractAnimationJob *a0) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickAnimatorControllerCall9 call = reinterpret_cast<CuteQQuickAnimatorControllerCall9>(taken[9]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QAnimationJobChangeListener::animationCurrentLoopChanged(a0);
  }
#endif  // QT_CONFIG(qml_animation)

#if QT_CONFIG(qml_animation)
  //  void QAnimationJobChangeListener::animationCurrentTimeChanged(QAbstra
  //      ctAnimationJob *a0, int a1)
  void animationCurrentTimeChanged(
      QAbstractAnimationJob *a0,
      int a1) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickAnimatorControllerCall10 call = reinterpret_cast<CuteQQuickAnimatorControllerCall10>(taken[10]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QAnimationJobChangeListener::animationCurrentTimeChanged(a0, a1);
  }
#endif  // QT_CONFIG(qml_animation)
};

//  const QMetaObject *QQuickAnimatorController::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK24QQuickAnimatorController10metaObjectEv(
    const QQuickAnimatorController *self) {
  return self->metaObject();
}

//  void *QQuickAnimatorController::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN24QQuickAnimatorController11qt_metacastEPKc(
    QQuickAnimatorController *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickAnimatorController::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN24QQuickAnimatorController11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickAnimatorController *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QQuickAnimatorController::~QQuickAnimatorController()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickAnimatorControllerD1Ev(
    QQuickAnimatorController *self) {
  delete self;
}

//  void QQuickAnimatorController::advance()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickAnimatorController7advanceEv(
    QQuickAnimatorController *self) {
  self->advance();
}

//  void QQuickAnimatorController::beforeNodeSync()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickAnimatorController14beforeNodeSyncEv(
    QQuickAnimatorController *self) {
  self->beforeNodeSync();
}

//  void QQuickAnimatorController::afterNodeSync()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickAnimatorController13afterNodeSyncEv(
    QQuickAnimatorController *self) {
  self->afterNodeSync();
}

//  void QQuickAnimatorController::animationFinished(QAbstractAnimationJob
//      *job)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickAnimatorController17animationFinishedEP21QAbstractAnimationJob(
    QQuickAnimatorController *self,
    QAbstractAnimationJob *job) {
  self->animationFinished(job);
}

//  void
//      QQuickAnimatorController::animationStateChanged(QAbstractAnimationJob
//      *job, QAbstractAnimationJob::State newState,
//      QAbstractAnimationJob::State oldState)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickAnimatorController21animationStateChangedEP21QAbstractAnimationJobNS0_5StateES2_(
    QQuickAnimatorController *self,
    QAbstractAnimationJob *job,
    QAbstractAnimationJob::State newState,
    QAbstractAnimationJob::State oldState) {
  self->animationStateChanged(job, newState, oldState);
}

//  void QQuickAnimatorController::requestSync()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickAnimatorController11requestSyncEv(
    QQuickAnimatorController *self) {
  self->requestSync();
}

//  void QQuickAnimatorController::start(const
//      QSharedPointer<QAbstractAnimationJob> &job)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickAnimatorController5startERK14QSharedPointerI21QAbstractAnimationJobE(
    QQuickAnimatorController *self,
    const QSharedPointer<QAbstractAnimationJob> *job) {
  self->start(*job);
}

//  void QQuickAnimatorController::cancel(const
//      QSharedPointer<QAbstractAnimationJob> &job)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickAnimatorController6cancelERK14QSharedPointerI21QAbstractAnimationJobE(
    QQuickAnimatorController *self,
    const QSharedPointer<QAbstractAnimationJob> *job) {
  self->cancel(*job);
}

//  void QQuickAnimatorController::pause(const
//      QSharedPointer<QAbstractAnimationJob> &job)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickAnimatorController5pauseERK14QSharedPointerI21QAbstractAnimationJobE(
    QQuickAnimatorController *self,
    const QSharedPointer<QAbstractAnimationJob> *job) {
  self->pause(*job);
}

//  bool QQuickAnimatorController::isPendingStart(const
//      QSharedPointer<QAbstractAnimationJob> &job) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QQuickAnimatorController14isPendingStartERK14QSharedPointerI21QAbstractAnimationJobE(
    const QQuickAnimatorController *self,
    const QSharedPointer<QAbstractAnimationJob> *job) {
  return self->isPendingStart(*job);
}

//  void QQuickAnimatorController::lock()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickAnimatorController4lockEv(
    QQuickAnimatorController *self) {
  self->lock();
}

//  void QQuickAnimatorController::unlock()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickAnimatorController6unlockEv(
    QQuickAnimatorController *self) {
  self->unlock();
}

//  QQuickWindow *QQuickAnimatorController::window() const
extern "C" Q_DECL_EXPORT
QQuickWindow *ritual_ZNK24QQuickAnimatorController6windowEv(
    const QQuickAnimatorController *self) {
  return self->window();
}

//  void QQuickAnimatorController::start_helper(QAbstractAnimationJob *job)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickAnimatorController12start_helperEP21QAbstractAnimationJob(
    QQuickAnimatorController *self,
    QAbstractAnimationJob *job) {
  self->start_helper(job);
}

//  QQuickAnimatorController as the QAnimationJobChangeListener it is built
//      on
extern "C" Q_DECL_EXPORT
QAnimationJobChangeListener *ritual_cast_QQuickAnimatorController_QAnimationJobChangeListener(
    QQuickAnimatorController *self) {
  return static_cast<QAnimationJobChangeListener *>(self);
}

//  a Python function taken by a CuteQQuickAnimatorController, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickAnimatorController(
    QQuickAnimatorController *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickAnimatorController *>(self)->take(key, call);
}

//  void QQuickAnimatorController::animationFinished(QAbstractAnimationJob
//      *job)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QQuickAnimatorController17animationFinishedEP21QAbstractAnimationJob(
    QQuickAnimatorController *self,
    QAbstractAnimationJob *job) {
  self->QQuickAnimatorController::animationFinished(job);
}

//  void
//      QQuickAnimatorController::animationStateChanged(QAbstractAnimationJob
//      *job, QAbstractAnimationJob::State newState,
//      QAbstractAnimationJob::State oldState)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QQuickAnimatorController21animationStateChangedEP21QAbstractAnimationJobNS0_5StateES2_(
    QQuickAnimatorController *self,
    QAbstractAnimationJob *job,
    QAbstractAnimationJob::State newState,
    QAbstractAnimationJob::State oldState) {
  self->QQuickAnimatorController::animationStateChanged(
      job,
      newState,
      oldState);
}
