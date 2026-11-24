//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquicksmoothedanimation_p_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquicksmoothedanimation_p.h>
#include <QtQuick/6.12.0/QtQuick/private/qquicksmoothedanimation_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/private/qquicksmoothedanimation_p.h>
#include <QtQuick/private/qquicksmoothedanimation_p_p.h>
#include <QtQuick/private/qquickanimation_p_p.h>
#include <QtQml/private/qcontinuinganimationgroupjob_p.h>
#include <QtCore/qmath.h>
#include <QtQml/qqmlproperty.h>
#include <QtQml/private/qqmlproperty_p.h>
#include <QtQml/private/qqmlglobal_p.h>
#include <QtCore/qdebug.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quick/util/qquicksmoothedanimation.cpp, line 224, as _ZN18QSmoothedAnimation4initEv
inline void QSmoothedAnimation::init()
{
    if (velocity == 0) {
        stop();
        return;
    }

    if (delayedStopTimer->isActive())
        delayedStopTimer->stop();

    initialValue = target.read().toReal();
    lastTime = this->currentTime();

    if (to == initialValue) {
        stop();
        return;
    }

    bool hasReversed = trackVelocity != 0. &&
                      ((!invert) == ((initialValue - to) > 0));

    if (hasReversed) {
        switch (reversingMode) {
            default:
            case QQuickSmoothedAnimation::Eased:
                initialVelocity = -trackVelocity;
                break;
            case QQuickSmoothedAnimation::Sync:
                QQmlPropertyPrivate::write(target, to,
                                                   QQmlPropertyData::BypassInterceptor
                                                   | QQmlPropertyData::DontRemoveBinding);
                trackVelocity = 0;
                stop();
                return;
            case QQuickSmoothedAnimation::Immediate:
                initialVelocity = 0;
                break;
        }
    }

    trackVelocity = initialVelocity;

    invert = (to < initialValue);

    if (!recalc()) {
        QQmlPropertyPrivate::write(target, to,
                                           QQmlPropertyData::BypassInterceptor
                                           | QQmlPropertyData::DontRemoveBinding);
        stop();
        return;
    }
}

//  from ../qtdeclarative/src/quick/util/qquicksmoothedanimation.cpp, line 111, as _ZN18QSmoothedAnimation6recalcEv
inline bool QSmoothedAnimation::recalc()
{
    s = to - initialValue;
    vi = initialVelocity;

    s = (invert? -1.0: 1.0) * s;

    if (userDuration >= 0 && velocity > 0) {
        tf = s / velocity;
        if (tf > (userDuration / 1000.)) tf = (userDuration / 1000.);
    } else if (userDuration >= 0) {
        tf = userDuration / 1000.;
    } else if (velocity > 0) {
        tf = s / velocity;
    } else {
        return false;
    }

    finalDuration = qCeil(tf * 1000.0);

    if (maximumEasingTime == 0) {
        a = 0;
        d = 0;
        tp = 0;
        td = tf;
        vp = velocity;
        sp = 0;
        sd = s;
    } else if (maximumEasingTime != -1 && tf > (maximumEasingTime / 1000.)) {
        qreal met = maximumEasingTime / 1000.;
        /*       tp|       |td
         * vp_      _______
         *         /       \
         * vi_    /         \
         *                   \
         *                    \   _ 0
         *       |ta|      |ta|
         */
        qreal ta = met / 2.;
        a = (s - (vi * tf - 0.5 * vi * ta)) / (tf * ta - ta * ta);

        vp = vi + a * ta;
        d = vp / ta;
        tp = ta;
        sp = vi * ta + 0.5 * a * tp * tp;
        sd = sp + vp * (tf - 2 * ta);
        td = tf - ta;
    } else {
        qreal c1 = 0.25 * tf * tf;
        qreal c2 = 0.5 * vi * tf - s;
        qreal c3 = -0.25 * vi * vi;

        qreal a1 = (-c2 + qSqrt(c2 * c2 - 4 * c1 * c3)) / (2. * c1);

        qreal tp1 = 0.5 * tf - 0.5 * vi / a1;
        qreal vp1 = a1 * tp1 + vi;

        qreal sp1 = 0.5 * a1 * tp1 * tp1 + vi * tp1;

        a = a1;
        d = a1;
        tp = tp1;
        td = tp1;
        vp = vp1;
        sp = sp1;
        sd = sp1;
    }
    return true;
}

//  from ../qtdeclarative/src/quick/util/qquicksmoothedanimation.cpp, line 342, as _ZN30QQuickSmoothedAnimationPrivateD1Ev
inline QQuickSmoothedAnimationPrivate::~QQuickSmoothedAnimationPrivate()
{
    typedef QHash<QQmlProperty, QSmoothedAnimation* >::iterator ActiveAnimationsHashIt;

    delete anim;
    for (ActiveAnimationsHashIt it = activeAnimations.begin(), end = activeAnimations.end(); it != end; ++it)
        it.value()->clearTemplate();
}

//  from ../qtdeclarative/src/quick/util/qquicksmoothedanimation.cpp, line 351, as _ZN30QQuickSmoothedAnimationPrivate23updateRunningAnimationsEv
inline void QQuickSmoothedAnimationPrivate::updateRunningAnimations()
{
    for (QSmoothedAnimation *ease : std::as_const(activeAnimations)) {
        ease->maximumEasingTime = anim->maximumEasingTime;
        ease->reversingMode = anim->reversingMode;
        ease->velocity = anim->velocity;
        ease->userDuration = anim->userDuration;
        ease->init();
    }
}
//  -----------------------------------------------------------------------

//  A QQuickSmoothedAnimationPrivate that Python can take functions over in. Every QQuickSmoothedAnimationPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(qml_animation)
typedef void (*CuteQQuickSmoothedAnimationPrivateCall0)(const void *, QAbstractAnimationJob *, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQQuickSmoothedAnimationPrivateCall1)(const void *, QAbstractAnimationJob *, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQQuickSmoothedAnimationPrivateCall2)(const void *, QAbstractAnimationJob *, int, int, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQQuickSmoothedAnimationPrivateCall3)(const void *, QAbstractAnimationJob *, int, int *);
#endif  // QT_CONFIG(qml_animation)
class CuteQQuickSmoothedAnimationPrivate : public QQuickSmoothedAnimationPrivate {
public:
  using QQuickSmoothedAnimationPrivate::QQuickSmoothedAnimationPrivate;
  void *taken[4] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(qml_animation)
    if (!std::strcmp(key, "_ZN27QAnimationJobChangeListener27animationCurrentLoopChangedEP21QAbstractAnimationJob")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
    if (!std::strcmp(key, "_ZN27QAnimationJobChangeListener17animationFinishedEP21QAbstractAnimationJob")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
    if (!std::strcmp(key, "_ZN27QAnimationJobChangeListener21animationStateChangedEP21QAbstractAnimationJobNS0_5StateES2_")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
    if (!std::strcmp(key, "_ZN27QAnimationJobChangeListener27animationCurrentTimeChangedEP21QAbstractAnimationJobi")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_animation)
    return false;
  }

#if QT_CONFIG(qml_animation)
  //  void QQuickPropertyAnimationPrivate::animationCurrentLoopChanged(QAbs
  //      tractAnimationJob *job)
  void animationCurrentLoopChanged(QAbstractAnimationJob *job) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickSmoothedAnimationPrivateCall0 call = reinterpret_cast<CuteQQuickSmoothedAnimationPrivateCall0>(taken[0]);
      call(this, job, &handled);
      if (handled) return;
    }
    QQuickPropertyAnimationPrivate::animationCurrentLoopChanged(job);
  }
#endif  // QT_CONFIG(qml_animation)

#if QT_CONFIG(qml_animation)
  //  void QQuickAbstractAnimationPrivate::animationFinished(QAbstractAnima
  //      tionJob *a0)
  void animationFinished(QAbstractAnimationJob *a0) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickSmoothedAnimationPrivateCall1 call = reinterpret_cast<CuteQQuickSmoothedAnimationPrivateCall1>(taken[1]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickAbstractAnimationPrivate::animationFinished(a0);
  }
#endif  // QT_CONFIG(qml_animation)

#if QT_CONFIG(qml_animation)
  //  void QAnimationJobChangeListener::animationStateChanged(QAbstractAnim
  //      ationJob *a0, QAbstractAnimationJob::State a1,
  //      QAbstractAnimationJob::State a2)
  void animationStateChanged(
      QAbstractAnimationJob *a0,
      QAbstractAnimationJob::State a1,
      QAbstractAnimationJob::State a2) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickSmoothedAnimationPrivateCall2 call = reinterpret_cast<CuteQQuickSmoothedAnimationPrivateCall2>(taken[2]);
      call(this, a0, static_cast<int>(a1), static_cast<int>(a2), &handled);
      if (handled) return;
    }
    QAnimationJobChangeListener::animationStateChanged(a0, a1, a2);
  }
#endif  // QT_CONFIG(qml_animation)

#if QT_CONFIG(qml_animation)
  //  void QAnimationJobChangeListener::animationCurrentTimeChanged(QAbstra
  //      ctAnimationJob *a0, int a1)
  void animationCurrentTimeChanged(
      QAbstractAnimationJob *a0,
      int a1) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickSmoothedAnimationPrivateCall3 call = reinterpret_cast<CuteQQuickSmoothedAnimationPrivateCall3>(taken[3]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QAnimationJobChangeListener::animationCurrentTimeChanged(a0, a1);
  }
#endif  // QT_CONFIG(qml_animation)
};

//  QQuickSmoothedAnimation *QQuickSmoothedAnimationPrivate::q_func()
extern "C" Q_DECL_EXPORT
QQuickSmoothedAnimation *ritual_ZN30QQuickSmoothedAnimationPrivate6q_funcEv(
    QQuickSmoothedAnimationPrivate *self) {
  return self->q_func();
}

//  const QQuickSmoothedAnimation *QQuickSmoothedAnimationPrivate::q_func()
//      const
extern "C" Q_DECL_EXPORT
const QQuickSmoothedAnimation *ritual_ZNK30QQuickSmoothedAnimationPrivate6q_funcEv(
    const QQuickSmoothedAnimationPrivate *self) {
  return self->q_func();
}

//  QQuickSmoothedAnimationPrivate::~QQuickSmoothedAnimationPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuickSmoothedAnimationPrivateD1Ev(
    QQuickSmoothedAnimationPrivate *self) {
  delete self;
}

//  void QQuickSmoothedAnimationPrivate::updateRunningAnimations()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuickSmoothedAnimationPrivate23updateRunningAnimationsEv(
    QQuickSmoothedAnimationPrivate *self) {
  self->updateRunningAnimations();
}

//  a Python function taken by a CuteQQuickSmoothedAnimationPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickSmoothedAnimationPrivate(
    QQuickSmoothedAnimationPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickSmoothedAnimationPrivate *>(self)->take(key, call);
}
