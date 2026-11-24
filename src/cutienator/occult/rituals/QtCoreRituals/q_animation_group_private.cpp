//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qanimationgroup_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(animation)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/qanimationgroup.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qanimationgroup_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qanimationgroup.h"
#include <QtCore/qdebug.h>
#include <QtCore/qcoreevent.h>
#include "qanimationgroup_p.h"
#include <algorithm>
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

//  from src/corelib/animation/qanimationgroup.cpp, line 268, as _ZN22QAnimationGroupPrivate5clearEb
inline void QAnimationGroupPrivate::clear(bool onDestruction)
{
    const QList<QAbstractAnimation *> animationsCopy = animations; // taking a copy
    animations.clear();
    // Clearing backwards so the indices doesn't change while we remove animations.
    for (qsizetype i = animationsCopy.size() - 1; i >= 0; --i) {
        QAbstractAnimation *animation = animationsCopy.at(i);
        animation->setParent(nullptr);
        QAbstractAnimationPrivate::get(animation)->group = nullptr;
        // If we are in ~QAnimationGroup() it is not safe to called the virtual
        // animationRemoved method, which can still be a method in a
        // QAnimationGroupPrivate derived class that assumes q_ptr is still
        // a valid derived class of QAnimationGroup.
        if (!onDestruction)
            animationRemoved(i, animation);
        delete animation;
    }
}
//  -----------------------------------------------------------------------

//  A QAnimationGroupPrivate that Python can take functions over in. Every QAnimationGroupPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(animation)
typedef void (*CuteQAnimationGroupPrivateCall0)(const void *, qsizetype, int *);
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
typedef void (*CuteQAnimationGroupPrivateCall1)(const void *, qsizetype, QAbstractAnimation *, int *);
#endif  // QT_CONFIG(animation)
class CuteQAnimationGroupPrivate : public QAnimationGroupPrivate {
public:
  using QAnimationGroupPrivate::QAnimationGroupPrivate;
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
  //  void QAnimationGroupPrivate::animationInsertedAt(qsizetype a0)
  void animationInsertedAt(qsizetype a0) override {
    if (taken[0]) {
      int handled = 0;
      CuteQAnimationGroupPrivateCall0 call = reinterpret_cast<CuteQAnimationGroupPrivateCall0>(taken[0]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QAnimationGroupPrivate::animationInsertedAt(a0);
  }
#endif  // QT_CONFIG(animation)

#if QT_CONFIG(animation)
  //  void QAnimationGroupPrivate::animationRemoved(qsizetype a0,
  //      QAbstractAnimation *a1)
  void animationRemoved(qsizetype a0, QAbstractAnimation *a1) override {
    if (taken[1]) {
      int handled = 0;
      CuteQAnimationGroupPrivateCall1 call = reinterpret_cast<CuteQAnimationGroupPrivateCall1>(taken[1]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QAnimationGroupPrivate::animationRemoved(a0, a1);
  }
#endif  // QT_CONFIG(animation)
};

//  QAnimationGroup *QAnimationGroupPrivate::q_func()
extern "C" Q_DECL_EXPORT
QAnimationGroup *ritual_ZN22QAnimationGroupPrivate6q_funcEv(
    QAnimationGroupPrivate *self) {
  return self->q_func();
}

//  const QAnimationGroup *QAnimationGroupPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QAnimationGroup *ritual_ZNK22QAnimationGroupPrivate6q_funcEv(
    const QAnimationGroupPrivate *self) {
  return self->q_func();
}

//  void QAnimationGroupPrivate::animationInsertedAt(qsizetype a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QAnimationGroupPrivate19animationInsertedAtEx(
    QAnimationGroupPrivate *self,
    qsizetype a0) {
  self->animationInsertedAt(a0);
}

//  void QAnimationGroupPrivate::animationRemoved(qsizetype a0,
//      QAbstractAnimation *a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QAnimationGroupPrivate16animationRemovedExP18QAbstractAnimation(
    QAnimationGroupPrivate *self,
    qsizetype a0,
    QAbstractAnimation *a1) {
  self->animationRemoved(a0, a1);
}

//  void QAnimationGroupPrivate::clear(bool onDestruction)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QAnimationGroupPrivate5clearEb(
    QAnimationGroupPrivate *self,
    bool onDestruction) {
  self->clear(onDestruction);
}

//  void QAnimationGroupPrivate::disconnectUncontrolledAnimation(QAbstractAni
//      mation *anim)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QAnimationGroupPrivate31disconnectUncontrolledAnimationEP18QAbstractAnimation(
    QAnimationGroupPrivate *self,
    QAbstractAnimation *anim) {
  self->disconnectUncontrolledAnimation(anim);
}

//  void
//      QAnimationGroupPrivate::connectUncontrolledAnimation(QAbstractAnimati
//      on *anim)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QAnimationGroupPrivate28connectUncontrolledAnimationEP18QAbstractAnimation(
    QAnimationGroupPrivate *self,
    QAbstractAnimation *anim) {
  self->connectUncontrolledAnimation(anim);
}

//  a Python function taken by a CuteQAnimationGroupPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAnimationGroupPrivate(
    QAnimationGroupPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAnimationGroupPrivate *>(self)->take(key, call);
}

//  void QAnimationGroupPrivate::animationInsertedAt(qsizetype a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QAnimationGroupPrivate19animationInsertedAtEx(
    QAnimationGroupPrivate *self,
    qsizetype a0) {
  self->QAnimationGroupPrivate::animationInsertedAt(a0);
}

//  void QAnimationGroupPrivate::animationRemoved(qsizetype a0,
//      QAbstractAnimation *a1)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QAnimationGroupPrivate16animationRemovedExP18QAbstractAnimation(
    QAnimationGroupPrivate *self,
    qsizetype a0,
    QAbstractAnimation *a1) {
  self->QAnimationGroupPrivate::animationRemoved(a0, a1);
}

#endif  // QT_CONFIG(animation)
