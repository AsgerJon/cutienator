//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qsequentialanimationgroup_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-25: completed by hand: indexForCurrentTime
//  (Qt's code taken from its source) and animationRemoved (a virtual
//  function, called through the object). Kept as it is when the generator
//  runs again.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(animation)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/qsequentialanimationgroup.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qsequentialanimationgroup_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qsequentialanimationgroup.h"
#include "qsequentialanimationgroup_p.h"
#include "qpauseanimation.h"
#include <QtCore/qdebug.h>
#include <QtCore/qnumeric.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/corelib/animation/qsequentialanimationgroup.cpp, line 80, as _ZNK32QSequentialAnimationGroupPrivate28animationActualTotalDurationEi
inline int QSequentialAnimationGroupPrivate::animationActualTotalDuration(int index) const
{
    QAbstractAnimation *anim = animations.at(index);
    int ret = anim->totalDuration();
    if (ret == -1 && actualDuration.size() > index)
        ret = actualDuration.at(index); //we can try the actual duration there
    return ret;
}

//  from src/corelib/animation/qsequentialanimationgroup.cpp, line 415, as _ZN32QSequentialAnimationGroupPrivate19setCurrentAnimationEib
inline void QSequentialAnimationGroupPrivate::setCurrentAnimation(int index, bool intermediate)
{
    Q_Q(QSequentialAnimationGroup);
    // currentAnimation.removeBindingUnlessInWrapper()
    // is not necessary here, since it is read only

    index = qMin(index, animations.size() - 1);

    if (index == -1) {
        Q_ASSERT(animations.isEmpty());
        currentAnimationIndex = -1;
        currentAnimation = nullptr;
        return;
    }

    // need these two checks below because this func can be called after the current animation
    // has been removed
    if (index == currentAnimationIndex && animations.at(index) == currentAnimation)
        return;

    // stop the old current animation
    if (currentAnimation)
        currentAnimation->stop();

    currentAnimationIndex = index;
    currentAnimation = animations.at(index);

    emit q->currentAnimationChanged(currentAnimation);

    activateCurrentAnimation(intermediate);
}

//  from src/corelib/animation/qsequentialanimationgroup.cpp, line 447, as _ZN32QSequentialAnimationGroupPrivate24activateCurrentAnimationEb
inline void QSequentialAnimationGroupPrivate::activateCurrentAnimation(bool intermediate)
{
    if (!currentAnimation || state == QSequentialAnimationGroup::Stopped)
        return;

    currentAnimation->stop();

    // we ensure the direction is consistent with the group's direction
    currentAnimation->setDirection(direction);

    // connects to the finish signal of uncontrolled animations
    if (currentAnimation->totalDuration() == -1)
        connectUncontrolledAnimation(currentAnimation);

    currentAnimation->start();
    if (!intermediate && state == QSequentialAnimationGroup::Paused)
        currentAnimation->pause();
}

//  from src/corelib/animation/qsequentialanimationgroup.cpp, line 497, as _ZN32QSequentialAnimationGroupPrivate19animationInsertedAtEx
inline void QSequentialAnimationGroupPrivate::animationInsertedAt(qsizetype index)
{
    if (currentAnimation == nullptr) {
        setCurrentAnimation(0); // initialize the current animation
        Q_ASSERT(currentAnimation);
    }

    if (currentAnimationIndex == index
        && currentAnimation->currentTime() == 0 && currentAnimation->currentLoop() == 0) {
            //in this case we simply insert an animation before the current one has actually started
            setCurrentAnimation(index);
    }

    //we update currentAnimationIndex in case it has changed (the animation pointer is still valid)
    currentAnimationIndex = animations.indexOf(currentAnimation);

    if (index < currentAnimationIndex || currentLoop != 0) {
        qWarning("QSequentialGroup::insertAnimation only supports to add animations after the current one.");
        return; //we're not affected because it is added after the current one
    }
}

//  from src/corelib/animation/qsequentialanimationgroup.cpp, line 65, as _ZNK32QSequentialAnimationGroupPrivate5atEndEv
inline bool QSequentialAnimationGroupPrivate::atEnd() const
{
    // we try to detect if we're at the end of the group
    //this is true if the following conditions are true:
    // 1. we're in the last loop
    // 2. the direction is forward
    // 3. the current animation is the last one
    // 4. the current animation has reached its end
    const int animTotalCurrentTime = QAbstractAnimationPrivate::get(currentAnimation)->totalCurrentTime;
    return (currentLoop == loopCount - 1
        && direction == QAbstractAnimation::Forward
        && currentAnimation == animations.last()
        && animTotalCurrentTime == animationActualTotalDuration(currentAnimationIndex));
}

//  from src/corelib/animation/qsequentialanimationgroup.cpp, line 123, as _ZN32QSequentialAnimationGroupPrivate7restartEv
inline void QSequentialAnimationGroupPrivate::restart()
{
    // restarting the group by making the first/last animation the current one
    if (direction == QAbstractAnimation::Forward) {
        lastLoop = 0;
        if (currentAnimationIndex == 0)
            activateCurrentAnimation();
        else
            setCurrentAnimation(0);
    } else { // direction == QAbstractAnimation::Backward
        lastLoop = loopCount - 1;
        int index = animations.size() - 1;
        if (currentAnimationIndex == index)
            activateCurrentAnimation();
        else
            setCurrentAnimation(index);
    }
}

//  from src/corelib/animation/qsequentialanimationgroup.cpp, line 180, as _ZN32QSequentialAnimationGroupPrivate14rewindForwardsERKNS_14AnimationIndexE
inline void QSequentialAnimationGroupPrivate::rewindForwards(const AnimationIndex &newAnimationIndex)
{
    if (lastLoop > currentLoop) {
        // we need to fast rewind to the beginning
        for (int i = currentAnimationIndex; i >= 0 ; --i) {
            QAbstractAnimation *anim = animations.at(i);
            setCurrentAnimation(i, true);
            anim->setCurrentTime(0);
        }
        // this will make sure the current animation is reset to the end
        if (animations.size() == 1)
            // we need to force activation because setCurrentAnimation will have no effect
            activateCurrentAnimation();
        else
            setCurrentAnimation(animations.size() - 1, true);
    }

    // and now we need to fast rewind from the current position to
    for (int i = currentAnimationIndex; i > newAnimationIndex.index; --i) {
        QAbstractAnimation *anim = animations.at(i);
        setCurrentAnimation(i, true);
        anim->setCurrentTime(0);
    }
    // setting the new current animation will happen later
}

//  from src/corelib/animation/qsequentialanimationgroup.cpp, line 148, as _ZN32QSequentialAnimationGroupPrivate15advanceForwardsERKNS_14AnimationIndexE
inline void QSequentialAnimationGroupPrivate::advanceForwards(const AnimationIndex &newAnimationIndex)
{
    if (lastLoop < currentLoop) {
        // we need to fast forward to the end
        for (int i = currentAnimationIndex; i < animations.size(); ++i) {
            QAbstractAnimation *anim = animations.at(i);
            setCurrentAnimation(i, true);
            anim->setCurrentTime(animationActualTotalDuration(i));
        }
        // this will make sure the current animation is reset to the beginning
        if (animations.size() == 1)
            // we need to force activation because setCurrentAnimation will have no effect
            activateCurrentAnimation();
        else
            setCurrentAnimation(0, true);
    }

    // and now we need to fast forward from the current position to
    for (int i = currentAnimationIndex; i < newAnimationIndex.index; ++i) {     //### WRONG,
        QAbstractAnimation *anim = animations.at(i);
        setCurrentAnimation(i, true);
        anim->setCurrentTime(animationActualTotalDuration(i));
    }
    // setting the new current animation will happen later
}

//  from src/corelib/animation/qsequentialanimationgroup.cpp, line 466, as _ZN32QSequentialAnimationGroupPrivate32_q_uncontrolledAnimationFinishedEv
inline void QSequentialAnimationGroupPrivate::_q_uncontrolledAnimationFinished()
{
    Q_Q(QSequentialAnimationGroup);
    Q_ASSERT(qobject_cast<QAbstractAnimation *>(q->sender()) == currentAnimation);

    // we trust the duration returned by the animation
    while (actualDuration.size() < (currentAnimationIndex + 1))
        actualDuration.append(-1);
    actualDuration[currentAnimationIndex] = currentAnimation->currentTime();

    disconnectUncontrolledAnimation(currentAnimation);

    if ((direction == QAbstractAnimation::Forward && currentAnimation == animations.last())
        || (direction == QAbstractAnimation::Backward && currentAnimationIndex == 0)) {
        // we don't handle looping of a group with undefined duration
        q->stop();
    } else if (direction == QAbstractAnimation::Forward) {
        // set the current animation to be the next one
        setCurrentAnimation(currentAnimationIndex + 1);
    } else {
        // set the current animation to be the previous one
        setCurrentAnimation(currentAnimationIndex - 1);
    }
}
//  from src/corelib/animation/qsequentialanimationgroup.cpp, line 53, as the helper of indexForCurrentTime
namespace {
int addSaturating(int a, int b)
{
    int r;
    if (qAddOverflow(a, b, &r))
        return std::numeric_limits<int>::max();
    return r;
}
} // namespace

//  from src/corelib/animation/qsequentialanimationgroup.cpp, line 89, as _ZNK32QSequentialAnimationGroupPrivate19indexForCurrentTimeEv
inline QSequentialAnimationGroupPrivate::AnimationIndex QSequentialAnimationGroupPrivate::indexForCurrentTime() const
{
    Q_ASSERT(!animations.isEmpty());

    AnimationIndex ret;
    int duration = 0;

    for (int i = 0; i < animations.size(); ++i) {
        duration = animationActualTotalDuration(i);

        // 'animation' is the current animation if one of these reasons is true:
        // 1. it's duration is undefined
        // 2. it ends after msecs
        // 3. it is the last animation (this can happen in case there is at least 1 uncontrolled animation)
        // 4. it ends exactly in msecs and the direction is backwards
        const int offsetPlusDuration = addSaturating(ret.timeOffset, duration);
        if (duration == -1 || currentTime < offsetPlusDuration
            || (currentTime == offsetPlusDuration && direction == QAbstractAnimation::Backward)) {
            ret.index = i;
            return ret;
        }

        // 'animation' has a non-null defined duration and is not the one at time 'msecs'.
        ret.timeOffset = offsetPlusDuration;
    }

    // this can only happen when one of those conditions is true:
    // 1. the duration of the group is undefined and we passed its actual duration
    // 2. there are only 0-duration animations in the group
    ret.timeOffset -= duration;
    ret.index = animations.size() - 1;
    return ret;
}

//  -----------------------------------------------------------------------

//  A QSequentialAnimationGroupPrivate that Python can take functions over in. Every QSequentialAnimationGroupPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(animation)
typedef void (*CuteQSequentialAnimationGroupPrivateCall0)(const void *, qsizetype, int *);
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
typedef void (*CuteQSequentialAnimationGroupPrivateCall1)(const void *, qsizetype, QAbstractAnimation *, int *);
#endif  // QT_CONFIG(animation)
class CuteQSequentialAnimationGroupPrivate : public QSequentialAnimationGroupPrivate {
public:
  using QSequentialAnimationGroupPrivate::QSequentialAnimationGroupPrivate;
  void *taken[2] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(animation)
    if (!std::strcmp(key, "_ZN22QAnimationGroupPrivate19animationInsertedAtEx")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
    if (!std::strcmp(key, "_ZN22QAnimationGroupPrivate16animationRemovedExP18QAbstractAnimation")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(animation)
    return false;
  }

#if QT_CONFIG(animation)
  //  void QSequentialAnimationGroupPrivate::animationInsertedAt(qsizetype
  //      index)
  void animationInsertedAt(qsizetype index) override {
    if (taken[0]) {
      int handled = 0;
      CuteQSequentialAnimationGroupPrivateCall0 call = reinterpret_cast<CuteQSequentialAnimationGroupPrivateCall0>(taken[0]);
      call(this, index, &handled);
      if (handled) return;
    }
    QSequentialAnimationGroupPrivate::animationInsertedAt(index);
  }
#endif  // QT_CONFIG(animation)

#if QT_CONFIG(animation)
  //  void QSequentialAnimationGroupPrivate::animationRemoved(qsizetype
  //      index, QAbstractAnimation *anim)
  void animationRemoved(qsizetype index, QAbstractAnimation *anim) override {
    if (taken[1]) {
      int handled = 0;
      CuteQSequentialAnimationGroupPrivateCall1 call = reinterpret_cast<CuteQSequentialAnimationGroupPrivateCall1>(taken[1]);
      call(this, index, anim, &handled);
      if (handled) return;
    }
    QSequentialAnimationGroupPrivate::animationRemoved(index, anim);
  }
#endif  // QT_CONFIG(animation)
};

//  QSequentialAnimationGroup *QSequentialAnimationGroupPrivate::q_func()
extern "C" Q_DECL_EXPORT
QSequentialAnimationGroup *ritual_ZN32QSequentialAnimationGroupPrivate6q_funcEv(
    QSequentialAnimationGroupPrivate *self) {
  return self->q_func();
}

//  const QSequentialAnimationGroup
//      *QSequentialAnimationGroupPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QSequentialAnimationGroup *ritual_ZNK32QSequentialAnimationGroupPrivate6q_funcEv(
    const QSequentialAnimationGroupPrivate *self) {
  return self->q_func();
}

//  int QSequentialAnimationGroupPrivate::animationActualTotalDuration(int
//      index) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK32QSequentialAnimationGroupPrivate28animationActualTotalDurationEi(
    const QSequentialAnimationGroupPrivate *self,
    int index) {
  return self->animationActualTotalDuration(index);
}

//  void QSequentialAnimationGroupPrivate::setCurrentAnimation(int index,
//      bool intermediate)
extern "C" Q_DECL_EXPORT
void ritual_ZN32QSequentialAnimationGroupPrivate19setCurrentAnimationEib(
    QSequentialAnimationGroupPrivate *self,
    int index,
    bool intermediate) {
  self->setCurrentAnimation(index, intermediate);
}

//  void QSequentialAnimationGroupPrivate::activateCurrentAnimation(bool
//      intermediate)
extern "C" Q_DECL_EXPORT
void ritual_ZN32QSequentialAnimationGroupPrivate24activateCurrentAnimationEb(
    QSequentialAnimationGroupPrivate *self,
    bool intermediate) {
  self->activateCurrentAnimation(intermediate);
}

//  void QSequentialAnimationGroupPrivate::animationInsertedAt(qsizetype
//      index)
extern "C" Q_DECL_EXPORT
void ritual_ZN32QSequentialAnimationGroupPrivate19animationInsertedAtEx(
    QSequentialAnimationGroupPrivate *self,
    qsizetype index) {
  self->animationInsertedAt(index);
}

//  bool QSequentialAnimationGroupPrivate::atEnd() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK32QSequentialAnimationGroupPrivate5atEndEv(
    const QSequentialAnimationGroupPrivate *self) {
  return self->atEnd();
}

//  void QSequentialAnimationGroupPrivate::restart()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QSequentialAnimationGroupPrivate7restartEv(
    QSequentialAnimationGroupPrivate *self) {
  self->restart();
}

//  void QSequentialAnimationGroupPrivate::rewindForwards(const
//      AnimationIndex &newAnimationIndex)
extern "C" Q_DECL_EXPORT
void ritual_ZN32QSequentialAnimationGroupPrivate14rewindForwardsERKNS_14AnimationIndexE(
    QSequentialAnimationGroupPrivate *self,
    const QSequentialAnimationGroupPrivate::AnimationIndex *newAnimationIndex) {
  self->rewindForwards(*newAnimationIndex);
}

//  void QSequentialAnimationGroupPrivate::advanceForwards(const
//      AnimationIndex &newAnimationIndex)
extern "C" Q_DECL_EXPORT
void ritual_ZN32QSequentialAnimationGroupPrivate15advanceForwardsERKNS_14AnimationIndexE(
    QSequentialAnimationGroupPrivate *self,
    const QSequentialAnimationGroupPrivate::AnimationIndex *newAnimationIndex) {
  self->advanceForwards(*newAnimationIndex);
}

//  void QSequentialAnimationGroupPrivate::_q_uncontrolledAnimationFinished()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QSequentialAnimationGroupPrivate32_q_uncontrolledAnimationFinishedEv(
    QSequentialAnimationGroupPrivate *self) {
  self->_q_uncontrolledAnimationFinished();
}

//  a Python function taken by a CuteQSequentialAnimationGroupPrivate, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSequentialAnimationGroupPrivate(
    QSequentialAnimationGroupPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSequentialAnimationGroupPrivate *>(self)->take(key, call);
}

//  void QSequentialAnimationGroupPrivate::animationInsertedAt(qsizetype
//      index)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN32QSequentialAnimationGroupPrivate19animationInsertedAtEx(
    QSequentialAnimationGroupPrivate *self,
    qsizetype index) {
  self->QSequentialAnimationGroupPrivate::animationInsertedAt(index);
}

//  QSequentialAnimationGroupPrivate::AnimationIndex
//      QSequentialAnimationGroupPrivate::indexForCurrentTime() const
extern "C" Q_DECL_EXPORT
QSequentialAnimationGroupPrivate::AnimationIndex * ritual_ZNK32QSequentialAnimationGroupPrivate19indexForCurrentTimeEv(
    const QSequentialAnimationGroupPrivate *self) {
  return new QSequentialAnimationGroupPrivate::AnimationIndex(self->indexForCurrentTime());
}

//  void QSequentialAnimationGroupPrivate::animationRemoved(qsizet
//      ype index, QAbstractAnimation *anim)
extern "C" Q_DECL_EXPORT
void ritual_ZN32QSequentialAnimationGroupPrivate16animationRemovedExP18QAbstractAnimation(
    QSequentialAnimationGroupPrivate *self,
    qsizetype index,
    QAbstractAnimation *anim) {
  self->animationRemoved(index, anim);
}

#endif  // QT_CONFIG(animation)
