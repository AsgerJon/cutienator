//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qparallelanimationgroup_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(animation)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/qparallelanimationgroup.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qparallelanimationgroup_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qanimationgroup.h"
#include <QtCore/qdebug.h>
#include <QtCore/qcoreevent.h>
#include "qanimationgroup_p.h"
#include <algorithm>
#include "qparallelanimationgroup.h"
#include "qparallelanimationgroup_p.h"
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/corelib/animation/qanimationgroup.cpp, line 287, as _ZN22QAnimationGroupPrivate16animationRemovedExP18QAbstractAnimation
inline void QAnimationGroupPrivate::animationRemoved(qsizetype index, QAbstractAnimation *)
{
    Q_Q(QAnimationGroup);
    Q_UNUSED(index);
    if (animations.isEmpty()) {
        currentTime = 0;
        q->stop();
    }
}

//  from src/corelib/animation/qparallelanimationgroup.cpp, line 219, as _ZNK30QParallelAnimationGroupPrivate20shouldAnimationStartEP18QAbstractAnimationb
inline bool QParallelAnimationGroupPrivate::shouldAnimationStart(QAbstractAnimation *animation, bool startIfAtEnd) const
{
    const int dura = animation->totalDuration();
    if (dura == -1)
        return !isUncontrolledAnimationFinished(animation);
    if (startIfAtEnd)
        return currentTime <= dura;
    if (direction == QAbstractAnimation::Forward)
        return currentTime < dura;
    else //direction == QAbstractAnimation::Backward
        return currentTime && currentTime <= dura;
}

//  from src/corelib/animation/qparallelanimationgroup.cpp, line 232, as _ZN30QParallelAnimationGroupPrivate15applyGroupStateEP18QAbstractAnimation
inline void QParallelAnimationGroupPrivate::applyGroupState(QAbstractAnimation *animation)
{
    switch (state)
    {
    case QAbstractAnimation::Running:
        animation->start();
        break;
    case QAbstractAnimation::Paused:
        animation->pause();
        break;
    case QAbstractAnimation::Stopped:
    default:
        break;
    }
}

//  from src/corelib/animation/qparallelanimationgroup.cpp, line 249, as _ZNK30QParallelAnimationGroupPrivate31isUncontrolledAnimationFinishedEP18QAbstractAnimation
inline bool QParallelAnimationGroupPrivate::isUncontrolledAnimationFinished(QAbstractAnimation *anim) const
{
    return uncontrolledFinishTime.value(anim, -1) >= 0;
}

//  from src/corelib/animation/qparallelanimationgroup.cpp, line 209, as _ZN30QParallelAnimationGroupPrivate29connectUncontrolledAnimationsEv
inline void QParallelAnimationGroupPrivate::connectUncontrolledAnimations()
{
    for (auto animation : std::as_const(animations)) {
        if (animation->duration() == -1 || animation->loopCount() < 0) {
            uncontrolledFinishTime[animation] = -1;
            connectUncontrolledAnimation(animation);
        }
    }
}

//  from src/corelib/animation/qparallelanimationgroup.cpp, line 254, as _ZN30QParallelAnimationGroupPrivate16animationRemovedExP18QAbstractAnimation
inline void QParallelAnimationGroupPrivate::animationRemoved(qsizetype index, QAbstractAnimation *anim)
{
    QAnimationGroupPrivate::animationRemoved(index, anim);
    disconnectUncontrolledAnimation(anim);
    uncontrolledFinishTime.remove(anim);
}
//  -----------------------------------------------------------------------

//  A QParallelAnimationGroupPrivate that Python can take functions over in. Every QParallelAnimationGroupPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(animation)
typedef void (*CuteQParallelAnimationGroupPrivateCall0)(const void *, qsizetype, QAbstractAnimation *, int *);
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
typedef void (*CuteQParallelAnimationGroupPrivateCall1)(const void *, qsizetype, int *);
#endif  // QT_CONFIG(animation)
class CuteQParallelAnimationGroupPrivate : public QParallelAnimationGroupPrivate {
public:
  using QParallelAnimationGroupPrivate::QParallelAnimationGroupPrivate;
  void *taken[2] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(animation)
    if (!std::strcmp(key, "_ZN22QAnimationGroupPrivate16animationRemovedExP18QAbstractAnimation")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
    if (!std::strcmp(key, "_ZN22QAnimationGroupPrivate19animationInsertedAtEx")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(animation)
    return false;
  }

#if QT_CONFIG(animation)
  //  void QParallelAnimationGroupPrivate::animationRemoved(qsizetype
  //      index, QAbstractAnimation *a1)
  void animationRemoved(qsizetype index, QAbstractAnimation *a1) override {
    if (taken[0]) {
      int handled = 0;
      CuteQParallelAnimationGroupPrivateCall0 call = reinterpret_cast<CuteQParallelAnimationGroupPrivateCall0>(taken[0]);
      call(this, index, a1, &handled);
      if (handled) return;
    }
    QParallelAnimationGroupPrivate::animationRemoved(index, a1);
  }
#endif  // QT_CONFIG(animation)

#if QT_CONFIG(animation)
  //  void QAnimationGroupPrivate::animationInsertedAt(qsizetype a0)
  void animationInsertedAt(qsizetype a0) override {
    if (taken[1]) {
      int handled = 0;
      CuteQParallelAnimationGroupPrivateCall1 call = reinterpret_cast<CuteQParallelAnimationGroupPrivateCall1>(taken[1]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QAnimationGroupPrivate::animationInsertedAt(a0);
  }
#endif  // QT_CONFIG(animation)
};

//  QParallelAnimationGroup *QParallelAnimationGroupPrivate::q_func()
extern "C" Q_DECL_EXPORT
QParallelAnimationGroup *ritual_ZN30QParallelAnimationGroupPrivate6q_funcEv(
    QParallelAnimationGroupPrivate *self) {
  return self->q_func();
}

//  const QParallelAnimationGroup *QParallelAnimationGroupPrivate::q_func()
//      const
extern "C" Q_DECL_EXPORT
const QParallelAnimationGroup *ritual_ZNK30QParallelAnimationGroupPrivate6q_funcEv(
    const QParallelAnimationGroupPrivate *self) {
  return self->q_func();
}

//  bool
//      QParallelAnimationGroupPrivate::shouldAnimationStart(QAbstractAnimati
//      on *animation, bool startIfAtEnd) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK30QParallelAnimationGroupPrivate20shouldAnimationStartEP18QAbstractAnimationb(
    const QParallelAnimationGroupPrivate *self,
    QAbstractAnimation *animation,
    bool startIfAtEnd) {
  return self->shouldAnimationStart(animation, startIfAtEnd);
}

//  void QParallelAnimationGroupPrivate::applyGroupState(QAbstractAnimation
//      *animation)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QParallelAnimationGroupPrivate15applyGroupStateEP18QAbstractAnimation(
    QParallelAnimationGroupPrivate *self,
    QAbstractAnimation *animation) {
  self->applyGroupState(animation);
}

//  bool QParallelAnimationGroupPrivate::isUncontrolledAnimationFinished(QAbs
//      tractAnimation *anim) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK30QParallelAnimationGroupPrivate31isUncontrolledAnimationFinishedEP18QAbstractAnimation(
    const QParallelAnimationGroupPrivate *self,
    QAbstractAnimation *anim) {
  return self->isUncontrolledAnimationFinished(anim);
}

//  void QParallelAnimationGroupPrivate::connectUncontrolledAnimations()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QParallelAnimationGroupPrivate29connectUncontrolledAnimationsEv(
    QParallelAnimationGroupPrivate *self) {
  self->connectUncontrolledAnimations();
}

//  void QParallelAnimationGroupPrivate::animationRemoved(qsizetype index,
//      QAbstractAnimation *a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QParallelAnimationGroupPrivate16animationRemovedExP18QAbstractAnimation(
    QParallelAnimationGroupPrivate *self,
    qsizetype index,
    QAbstractAnimation *a1) {
  self->animationRemoved(index, a1);
}

//  a Python function taken by a CuteQParallelAnimationGroupPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QParallelAnimationGroupPrivate(
    QParallelAnimationGroupPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQParallelAnimationGroupPrivate *>(self)->take(key, call);
}

//  void QParallelAnimationGroupPrivate::animationRemoved(qsizetype index,
//      QAbstractAnimation *a1)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN30QParallelAnimationGroupPrivate16animationRemovedExP18QAbstractAnimation(
    QParallelAnimationGroupPrivate *self,
    qsizetype index,
    QAbstractAnimation *a1) {
  self->QParallelAnimationGroupPrivate::animationRemoved(index, a1);
}

#endif  // QT_CONFIG(animation)
