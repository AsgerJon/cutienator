//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquicksmoothedanimation_p_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquicksmoothedanimation_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qdebug.h>
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

//  from ../qtdeclarative/src/quick/util/qquicksmoothedanimation.cpp, line 51, as _ZN18QSmoothedAnimationD1Ev
inline QSmoothedAnimation::~QSmoothedAnimation()
{
    delete delayedStopTimer;
    if (animationTemplate) {
        if (target.object()) {
            auto it = animationTemplate->activeAnimations.constFind(target);
            if (it != animationTemplate->activeAnimations.cend() && it.value() == this)
                animationTemplate->activeAnimations.erase(it);
        } else {
            //target is no longer valid, need to search linearly
            for (auto it = animationTemplate->activeAnimations.cbegin(); it != animationTemplate->activeAnimations.cend(); ++it) {
                if (it.value() == this) {
                    animationTemplate->activeAnimations.erase(it);
                    break;
                }
            }
        }
    }
}

//  from ../qtdeclarative/src/quick/util/qquicksmoothedanimation.cpp, line 106, as _ZNK18QSmoothedAnimation8durationEv
inline int QSmoothedAnimation::duration() const
{
    return -1;
}

//  from ../qtdeclarative/src/quick/util/qquicksmoothedanimation.cpp, line 71, as _ZN18QSmoothedAnimation7restartEv
inline void QSmoothedAnimation::restart()
{
    initialVelocity = trackVelocity;
    if (isRunning())
        init();
    else
        start();
}

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

//  from ../qtdeclarative/src/quick/util/qquicksmoothedanimation.cpp, line 80, as _ZN18QSmoothedAnimation17prepareForRestartEv
inline void QSmoothedAnimation::prepareForRestart()
{
    initialVelocity = trackVelocity;
    if (isRunning()) {
        //we are joining a new wrapper group while running, our times need to be restarted
        skipUpdate = true;
        init();
        lastTime = 0;
    } else {
        skipUpdate = false;
        //we'll be started when the group starts, which will force an init()
    }
}

//  from ../qtdeclarative/src/quick/util/qquicksmoothedanimation.cpp, line 205, as _ZN18QSmoothedAnimation17updateCurrentTimeEi
inline void QSmoothedAnimation::updateCurrentTime(int t)
{
    if (skipUpdate) {
        skipUpdate = false;
        return;
    }

    if (!isRunning() && !isPaused()) // This can happen if init() stops the animation in some cases
        return;

    qreal time_seconds = qreal(t - lastTime) / 1000.;

    qreal value = easeFollow(time_seconds);
    value *= (invert? -1.0: 1.0);
    QQmlPropertyPrivate::write(target, initialValue + value,
                                       QQmlPropertyData::BypassInterceptor
                                       | QQmlPropertyData::DontRemoveBinding);
}

//  from ../qtdeclarative/src/quick/util/qquicksmoothedanimation.cpp, line 94, as _ZN18QSmoothedAnimation11updateStateEN21QAbstractAnimationJob5StateES1_
inline void QSmoothedAnimation::updateState(QAbstractAnimationJob::State newState, QAbstractAnimationJob::State /*oldState*/)
{
    if (newState == QAbstractAnimationJob::Running)
        init();
}

//  from ../qtdeclarative/src/quick/util/qquicksmoothedanimation.cpp, line 277, as _ZNK18QSmoothedAnimation14debugAnimationE6QDebug
inline void QSmoothedAnimation::debugAnimation(QDebug d) const
{
    d << "SmoothedAnimationJob(" << Qt::hex << (const void *) this << Qt::dec << ")" << "duration:" << userDuration
      << "velocity:" << velocity << "target:" << target.object() << "property:" << target.name()
      << "to:" << to << "current velocity:" << trackVelocity;
}

//  from ../qtdeclarative/src/quick/util/qquicksmoothedanimation.cpp, line 181, as _ZN18QSmoothedAnimation10easeFollowEd
inline qreal QSmoothedAnimation::easeFollow(qreal time_seconds)
{
    qreal value;
    if (time_seconds < tp) {
        trackVelocity = vi + time_seconds * a;
        value = 0.5 * a * time_seconds * time_seconds + vi * time_seconds;
    } else if (time_seconds < td) {
        time_seconds -= tp;
        trackVelocity = vp;
        value = sp + time_seconds * vp;
    } else if (time_seconds < tf) {
        time_seconds -= td;
        trackVelocity = vp - time_seconds * a;
        value = sd - 0.5 * d * time_seconds * time_seconds + vp * time_seconds;
    } else {
        trackVelocity = 0;
        value = s;
        delayedStop();
    }

    // to normalize 's' between [0..1], divide 'value' by 's'
    return value;
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

//  from ../qtdeclarative/src/quick/util/qquicksmoothedanimation.cpp, line 100, as _ZN18QSmoothedAnimation11delayedStopEv
inline void QSmoothedAnimation::delayedStop()
{
    if (!delayedStopTimer->isActive())
        delayedStopTimer->start();
}
//  -----------------------------------------------------------------------

//  Only a class built on QSmoothedAnimation may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQSmoothedAnimation : QSmoothedAnimation {
  using QSmoothedAnimation::updateCurrentTime;
  using QSmoothedAnimation::updateState;
  using QSmoothedAnimation::debugAnimation;
};

//  A QSmoothedAnimation that Python can take functions over in. Every QSmoothedAnimation
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(qml_animation)
typedef int (*CuteQSmoothedAnimationCall0)(const void *, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQSmoothedAnimationCall1)(const void *, int, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQSmoothedAnimationCall2)(const void *, int, int, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQSmoothedAnimationCall3)(const void *, const QDebug *, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQSmoothedAnimationCall4)(const void *, int, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQSmoothedAnimationCall5)(const void *, int, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQSmoothedAnimationCall6)(const void *, int *);
#endif  // QT_CONFIG(qml_animation)
class CuteQSmoothedAnimation : public QSmoothedAnimation {
public:
  using QSmoothedAnimation::QSmoothedAnimation;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(qml_animation)
    if (!std::strcmp(key, "_ZNK21QAbstractAnimationJob8durationEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
    if (!std::strcmp(key, "_ZN21QAbstractAnimationJob17updateCurrentTimeEi")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
    if (!std::strcmp(key, "_ZN21QAbstractAnimationJob11updateStateENS_5StateES0_")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
    if (!std::strcmp(key, "_ZNK21QAbstractAnimationJob14debugAnimationE6QDebug")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
    if (!std::strcmp(key, "_ZN21QAbstractAnimationJob15updateLoopCountEi")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
    if (!std::strcmp(key, "_ZN21QAbstractAnimationJob15updateDirectionENS_9DirectionE")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
    if (!std::strcmp(key, "_ZN21QAbstractAnimationJob28topLevelAnimationLoopChangedEv")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_animation)
    return false;
  }

#if QT_CONFIG(qml_animation)
  //  int QSmoothedAnimation::duration() const
  int duration() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSmoothedAnimationCall0 call = reinterpret_cast<CuteQSmoothedAnimationCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QSmoothedAnimation::duration();
  }
#endif  // QT_CONFIG(qml_animation)

#if QT_CONFIG(qml_animation)
  //  void QSmoothedAnimation::updateCurrentTime(int a0)
  void updateCurrentTime(int a0) override {
    if (taken[1]) {
      int handled = 0;
      CuteQSmoothedAnimationCall1 call = reinterpret_cast<CuteQSmoothedAnimationCall1>(taken[1]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QSmoothedAnimation::updateCurrentTime(a0);
  }
#endif  // QT_CONFIG(qml_animation)

#if QT_CONFIG(qml_animation)
  //  void QSmoothedAnimation::updateState(QAbstractAnimationJob::State a0,
  //      QAbstractAnimationJob::State a1)
  void updateState(
      QAbstractAnimationJob::State a0,
      QAbstractAnimationJob::State a1) override {
    if (taken[2]) {
      int handled = 0;
      CuteQSmoothedAnimationCall2 call = reinterpret_cast<CuteQSmoothedAnimationCall2>(taken[2]);
      call(this, static_cast<int>(a0), static_cast<int>(a1), &handled);
      if (handled) return;
    }
    QSmoothedAnimation::updateState(a0, a1);
  }
#endif  // QT_CONFIG(qml_animation)

#if QT_CONFIG(qml_animation)
  //  void QSmoothedAnimation::debugAnimation(QDebug d) const
  void debugAnimation(QDebug d) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQSmoothedAnimationCall3 call = reinterpret_cast<CuteQSmoothedAnimationCall3>(taken[3]);
      call(this, &d, &handled);
      if (handled) return;
    }
    QSmoothedAnimation::debugAnimation(d);
  }
#endif  // QT_CONFIG(qml_animation)

#if QT_CONFIG(qml_animation)
  //  void QAbstractAnimationJob::updateLoopCount(int a0)
  void updateLoopCount(int a0) override {
    if (taken[4]) {
      int handled = 0;
      CuteQSmoothedAnimationCall4 call = reinterpret_cast<CuteQSmoothedAnimationCall4>(taken[4]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QAbstractAnimationJob::updateLoopCount(a0);
  }
#endif  // QT_CONFIG(qml_animation)

#if QT_CONFIG(qml_animation)
  //  void QAbstractAnimationJob::updateDirection(QAbstractAnimationJob::Di
  //      rection direction)
  void updateDirection(QAbstractAnimationJob::Direction direction) override {
    if (taken[5]) {
      int handled = 0;
      CuteQSmoothedAnimationCall5 call = reinterpret_cast<CuteQSmoothedAnimationCall5>(taken[5]);
      call(this, static_cast<int>(direction), &handled);
      if (handled) return;
    }
    QAbstractAnimationJob::updateDirection(direction);
  }
#endif  // QT_CONFIG(qml_animation)

#if QT_CONFIG(qml_animation)
  //  void QAbstractAnimationJob::topLevelAnimationLoopChanged()
  void topLevelAnimationLoopChanged() override {
    if (taken[6]) {
      int handled = 0;
      CuteQSmoothedAnimationCall6 call = reinterpret_cast<CuteQSmoothedAnimationCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractAnimationJob::topLevelAnimationLoopChanged();
  }
#endif  // QT_CONFIG(qml_animation)
};

//  QSmoothedAnimation::~QSmoothedAnimation()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QSmoothedAnimationD1Ev(QSmoothedAnimation *self) {
  delete self;
}

//  int QSmoothedAnimation::duration() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QSmoothedAnimation8durationEv(
    const QSmoothedAnimation *self) {
  return self->duration();
}

//  void QSmoothedAnimation::restart()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QSmoothedAnimation7restartEv(QSmoothedAnimation *self) {
  self->restart();
}

//  void QSmoothedAnimation::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QSmoothedAnimation4initEv(QSmoothedAnimation *self) {
  self->init();
}

//  void QSmoothedAnimation::prepareForRestart()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QSmoothedAnimation17prepareForRestartEv(
    QSmoothedAnimation *self) {
  self->prepareForRestart();
}

//  void QSmoothedAnimation::clearTemplate()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QSmoothedAnimation13clearTemplateEv(
    QSmoothedAnimation *self) {
  self->clearTemplate();
}

//  void QSmoothedAnimation::updateCurrentTime(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QSmoothedAnimation17updateCurrentTimeEi(
    QSmoothedAnimation *self,
    int a0) {
  self->updateCurrentTime(a0);
}

//  void QSmoothedAnimation::updateState(QAbstractAnimationJob::State a0,
//      QAbstractAnimationJob::State a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QSmoothedAnimation11updateStateEN21QAbstractAnimationJob5StateES1_(
    QSmoothedAnimation *self,
    QAbstractAnimationJob::State a0,
    QAbstractAnimationJob::State a1) {
  self->updateState(a0, a1);
}

//  void QSmoothedAnimation::debugAnimation(QDebug d) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK18QSmoothedAnimation14debugAnimationE6QDebug(
    const QSmoothedAnimation *self,
    const QDebug *d) {
  self->debugAnimation(*d);
}

//  qreal QSmoothedAnimation::easeFollow(qreal a0)
extern "C" Q_DECL_EXPORT
qreal ritual_ZN18QSmoothedAnimation10easeFollowEd(
    QSmoothedAnimation *self,
    qreal a0) {
  return self->easeFollow(a0);
}

//  bool QSmoothedAnimation::recalc()
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QSmoothedAnimation6recalcEv(QSmoothedAnimation *self) {
  return self->recalc();
}

//  void QSmoothedAnimation::delayedStop()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QSmoothedAnimation11delayedStopEv(QSmoothedAnimation *self) {
  self->delayedStop();
}

//  a Python function taken by a CuteQSmoothedAnimation, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSmoothedAnimation(
    QSmoothedAnimation *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSmoothedAnimation *>(self)->take(key, call);
}

//  int QSmoothedAnimation::duration() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK18QSmoothedAnimation8durationEv(
    const QSmoothedAnimation *self) {
  return self->QSmoothedAnimation::duration();
}

//  void QSmoothedAnimation::updateCurrentTime(int a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QSmoothedAnimation17updateCurrentTimeEi(
    QSmoothedAnimation *self,
    int a0) {
  static_cast<OwnQSmoothedAnimation *>(self)->OwnQSmoothedAnimation::updateCurrentTime(
      a0);
}

//  void QSmoothedAnimation::updateState(QAbstractAnimationJob::State a0,
//      QAbstractAnimationJob::State a1)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QSmoothedAnimation11updateStateEN21QAbstractAnimationJob5StateES1_(
    QSmoothedAnimation *self,
    QAbstractAnimationJob::State a0,
    QAbstractAnimationJob::State a1) {
  static_cast<OwnQSmoothedAnimation *>(self)->OwnQSmoothedAnimation::updateState(
      a0,
      a1);
}

//  void QSmoothedAnimation::debugAnimation(QDebug d) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK18QSmoothedAnimation14debugAnimationE6QDebug(
    const QSmoothedAnimation *self,
    const QDebug *d) {
  static_cast<const OwnQSmoothedAnimation *>(self)->OwnQSmoothedAnimation::debugAnimation(
      *d);
}
