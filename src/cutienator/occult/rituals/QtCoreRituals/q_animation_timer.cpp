//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qabstractanimation_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(animation)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qabstractanimation_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qabstractanimation.h"
#include "qanimationgroup.h"
#include <QtCore/qdebug.h>
#include "qabstractanimation_p.h"
#if defined(Q_OS_WASM)
#include <QtCore/private/qwasmanimationdriver_p.h>
#endif
#include <QtCore/qmath.h>
#include <QtCore/qcoreevent.h>
#include <QtCore/qnumeric.h>
#include <QtCore/qpointer.h>
#include <QtCore/qscopedvaluerollback.h>
#include <QtCore/q26numeric.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/corelib/animation/qabstractanimation.cpp, line 614, as _ZN15QAnimationTimer21restartAnimationTimerEv
inline void QAnimationTimer::restartAnimationTimer()
{
    if (runningLeafAnimations == 0 && !runningPauseAnimations.isEmpty())
        QUnifiedTimer::pauseAnimationTimer(this, closestPauseAnimationTimeToFinish());
    else if (isPaused)
        QUnifiedTimer::resumeAnimationTimer(this);
    else if (!isRegistered)
        QUnifiedTimer::startAnimationTimer(this);
}

//  from src/corelib/animation/qabstractanimation.cpp, line 584, as _ZN15QAnimationTimer20updateAnimationsTimeEx
inline void QAnimationTimer::updateAnimationsTime(qint64 delta)
{
    //setCurrentTime can get this called again while we're the for loop. At least with pauseAnimations
    if (insideTick)
        return;

    lastTick += delta;

    //we make sure we only call update time if the time has actually changed
    //it might happen in some cases that the time doesn't change because events are delayed
    //when the CPU load is high
    if (delta) {
        QScopedValueRollback<bool> guard(insideTick, true);
        for (currentAnimationIdx = 0; currentAnimationIdx < animations.size(); ++currentAnimationIdx) {
            QAbstractAnimation *animation = animations.at(currentAnimationIdx);
            qint64 elapsed = QAbstractAnimationPrivate::get(animation)->totalCurrentTime
                          + (animation->direction() == QAbstractAnimation::Forward ? delta : -delta);
            animation->setCurrentTime(q26::saturating_cast<int>(elapsed));
        }
        currentAnimationIdx = 0;
    }
}

//  from src/corelib/animation/qabstractanimation.cpp, line 624, as _ZN15QAnimationTimer15startAnimationsEv
inline void QAnimationTimer::startAnimations()
{
    if (!startAnimationPending)
        return;
    startAnimationPending = false;

    //force timer to update, which prevents large deltas for our newly added animations
    QUnifiedTimer::instance()->maybeUpdateAnimationsToCurrentTime();

    //we transfer the waiting animations into the "really running" state
    animations += animationsToStart;
    animationsToStart.clear();
    if (!animations.isEmpty())
        restartAnimationTimer();
}

//  from src/corelib/animation/qabstractanimation.cpp, line 640, as _ZN15QAnimationTimer9stopTimerEv
inline void QAnimationTimer::stopTimer()
{
    stopTimerPending = false;
    bool pendingStart = startAnimationPending && animationsToStart.size() > 0;
    if (animations.isEmpty() && !pendingStart) {
        QUnifiedTimer::resumeAnimationTimer(this);
        QUnifiedTimer::stopAnimationTimer(this);
        // invalidate the start reference time
        lastTick = 0;
    }
}

//  from src/corelib/animation/qabstractanimation.cpp, line 697, as _ZN15QAnimationTimer24registerRunningAnimationEP18QAbstractAnimation
inline void QAnimationTimer::registerRunningAnimation(QAbstractAnimation *animation)
{
    if (QAbstractAnimationPrivate::get(animation)->isGroup)
        return;

    if (QAbstractAnimationPrivate::get(animation)->isPause) {
        runningPauseAnimations << animation;
    } else
        runningLeafAnimations++;
}

//  from src/corelib/animation/qabstractanimation.cpp, line 708, as _ZN15QAnimationTimer26unregisterRunningAnimationEP18QAbstractAnimation
inline void QAnimationTimer::unregisterRunningAnimation(QAbstractAnimation *animation)
{
    if (QAbstractAnimationPrivate::get(animation)->isGroup)
        return;

    if (QAbstractAnimationPrivate::get(animation)->isPause)
        runningPauseAnimations.removeOne(animation);
    else
        runningLeafAnimations--;
    Q_ASSERT(runningLeafAnimations >= 0);
}
//  -----------------------------------------------------------------------

//  A QAnimationTimer that Python can take functions over in. Every QAnimationTimer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(animation)
typedef void (*CuteQAnimationTimerCall0)(const void *, int *);
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
typedef void (*CuteQAnimationTimerCall1)(const void *, qint64, int *);
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
typedef qsizetype (*CuteQAnimationTimerCall2)(const void *, int *);
#endif  // QT_CONFIG(animation)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAnimationTimerCall3)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAnimationTimerCall4)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAnimationTimerCall5)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAnimationTimerCall6)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAnimationTimerCall7)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAnimationTimerCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAnimationTimerCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQAnimationTimer : public QAnimationTimer {
public:
  using QAnimationTimer::QAnimationTimer;
  void *taken[10] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(animation)
    if (!std::strcmp(key, "_ZN23QAbstractAnimationTimer21restartAnimationTimerEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
    if (!std::strcmp(key, "_ZN23QAbstractAnimationTimer20updateAnimationsTimeEx")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
    if (!std::strcmp(key, "_ZNK23QAbstractAnimationTimer21runningAnimationCountEv")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(animation)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if QT_CONFIG(animation)
  //  void QAnimationTimer::restartAnimationTimer()
  void restartAnimationTimer() override {
    if (taken[0]) {
      int handled = 0;
      CuteQAnimationTimerCall0 call = reinterpret_cast<CuteQAnimationTimerCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QAnimationTimer::restartAnimationTimer();
  }
#endif  // QT_CONFIG(animation)

#if QT_CONFIG(animation)
  //  void QAnimationTimer::updateAnimationsTime(qint64 delta)
  void updateAnimationsTime(qint64 delta) override {
    if (taken[1]) {
      int handled = 0;
      CuteQAnimationTimerCall1 call = reinterpret_cast<CuteQAnimationTimerCall1>(taken[1]);
      call(this, delta, &handled);
      if (handled) return;
    }
    QAnimationTimer::updateAnimationsTime(delta);
  }
#endif  // QT_CONFIG(animation)

#if QT_CONFIG(animation)
  //  qsizetype QAnimationTimer::runningAnimationCount() const
  qsizetype runningAnimationCount() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQAnimationTimerCall2 call = reinterpret_cast<CuteQAnimationTimerCall2>(taken[2]);
      qsizetype given = call(this, &handled);
      if (handled) return given;
    }
    return QAnimationTimer::runningAnimationCount();
  }
#endif  // QT_CONFIG(animation)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQAnimationTimerCall3 call = reinterpret_cast<CuteQAnimationTimerCall3>(taken[3]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQAnimationTimerCall4 call = reinterpret_cast<CuteQAnimationTimerCall4>(taken[4]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQAnimationTimerCall5 call = reinterpret_cast<CuteQAnimationTimerCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQAnimationTimerCall6 call = reinterpret_cast<CuteQAnimationTimerCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQAnimationTimerCall7 call = reinterpret_cast<CuteQAnimationTimerCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[8]) {
      int handled = 0;
      CuteQAnimationTimerCall8 call = reinterpret_cast<CuteQAnimationTimerCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[9]) {
      int handled = 0;
      CuteQAnimationTimerCall9 call = reinterpret_cast<CuteQAnimationTimerCall9>(taken[9]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QAnimationTimer::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QAnimationTimer10metaObjectEv(
    const QAnimationTimer *self) {
  return self->metaObject();
}

//  void QAnimationTimer::restartAnimationTimer()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAnimationTimer21restartAnimationTimerEv(
    QAnimationTimer *self) {
  self->restartAnimationTimer();
}

//  void QAnimationTimer::updateAnimationsTime(qint64 delta)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAnimationTimer20updateAnimationsTimeEx(
    QAnimationTimer *self,
    qint64 delta) {
  self->updateAnimationsTime(delta);
}

//  qsizetype QAnimationTimer::runningAnimationCount() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK15QAnimationTimer21runningAnimationCountEv(
    const QAnimationTimer *self) {
  return self->runningAnimationCount();
}

//  void QAnimationTimer::startAnimations()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAnimationTimer15startAnimationsEv(QAnimationTimer *self) {
  self->startAnimations();
}

//  void QAnimationTimer::stopTimer()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAnimationTimer9stopTimerEv(QAnimationTimer *self) {
  self->stopTimer();
}

//  void QAnimationTimer::registerRunningAnimation(QAbstractAnimation
//      *animation)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAnimationTimer24registerRunningAnimationEP18QAbstractAnimation(
    QAnimationTimer *self,
    QAbstractAnimation *animation) {
  self->registerRunningAnimation(animation);
}

//  void QAnimationTimer::unregisterRunningAnimation(QAbstractAnimation
//      *animation)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAnimationTimer26unregisterRunningAnimationEP18QAbstractAnimation(
    QAnimationTimer *self,
    QAbstractAnimation *animation) {
  self->unregisterRunningAnimation(animation);
}

//  a Python function taken by a CuteQAnimationTimer, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAnimationTimer(
    QAnimationTimer *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAnimationTimer *>(self)->take(key, call);
}

//  void QAnimationTimer::updateAnimationsTime(qint64 delta)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QAnimationTimer20updateAnimationsTimeEx(
    QAnimationTimer *self,
    qint64 delta) {
  self->QAnimationTimer::updateAnimationsTime(delta);
}

//  qsizetype QAnimationTimer::runningAnimationCount() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_own_ZNK15QAnimationTimer21runningAnimationCountEv(
    const QAnimationTimer *self) {
  return self->QAnimationTimer::runningAnimationCount();
}

#endif  // QT_CONFIG(animation)
