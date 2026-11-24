//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickanimation_p_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickanimation_p.h>
#include <QtQuick/6.12.0/QtQuick/private/qquickanimation_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qquickanimation_p.h"
#include "qquickanimation_p_p.h"
#include "qquickanimatorjob_p.h"
#include <private/qquickstatechangescript_p.h>
#include <private/qqmlcontext_p.h>
#include <qqmlpropertyvaluesource.h>
#include <qqml.h>
#include <qqmlinfo.h>
#include <qqmlexpression.h>
#include <private/qqmlstringconverters_p.h>
#include <private/qqmlglobal_p.h>
#include <private/qqmlmetatype_p.h>
#include <private/qqmlvaluetype_p.h>
#include <private/qqmlproperty_p.h>
#include <private/qqmlengine_p.h>
#include <qvariant.h>
#include <qcolor.h>
#include <qfile.h>
#include "private/qparallelanimationgroupjob_p.h"
#include "private/qsequentialanimationgroupjob_p.h"
#include <QtCore/qset.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtCore/qsize.h>
#include <QtCore/qmath.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quick/util/qquickanimation.cpp, line 1761, as _ZN27QQuickAnimationGroupPrivate22restartFromCurrentLoopEv
inline void QQuickAnimationGroupPrivate::restartFromCurrentLoop()
{
    Q_Q(QQuickAnimationGroup);
    if (!animationDirty)
        return;

    animationDirty = false;

    Q_ASSERT(animationInstance);
    const int currentLoop = animationInstance->currentLoop();

    QSignalBlocker signalBlocker(q);
    q->stop();
    q->start();

    Q_ASSERT(animationInstance);
    // Restarting adjusts animationInstance's loopCount
    // Since we just want to start it from this loop,
    // it will be restored again.
    if (loopCount != -1)
        animationInstance->setLoopCount(loopCount - currentLoop);
}

//  from ../qtdeclarative/src/quick/util/qquickanimation.cpp, line 1784, as _ZN27QQuickAnimationGroupPrivate27animationCurrentLoopChangedEP21QAbstractAnimationJob
inline void QQuickAnimationGroupPrivate::animationCurrentLoopChanged(QAbstractAnimationJob *)
{
    if (!animationDirty)
        return;
    restartFromCurrentLoop();
}
//  -----------------------------------------------------------------------

//  A QQuickAnimationGroupPrivate that Python can take functions over in. Every QQuickAnimationGroupPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(qml_animation)
typedef void (*CuteQQuickAnimationGroupPrivateCall0)(const void *, QAbstractAnimationJob *, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQQuickAnimationGroupPrivateCall1)(const void *, QAbstractAnimationJob *, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQQuickAnimationGroupPrivateCall2)(const void *, QAbstractAnimationJob *, int, int, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQQuickAnimationGroupPrivateCall3)(const void *, QAbstractAnimationJob *, int, int *);
#endif  // QT_CONFIG(qml_animation)
class CuteQQuickAnimationGroupPrivate : public QQuickAnimationGroupPrivate {
public:
  using QQuickAnimationGroupPrivate::QQuickAnimationGroupPrivate;
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
  //  void QQuickAnimationGroupPrivate::animationCurrentLoopChanged(QAbstra
  //      ctAnimationJob *job)
  void animationCurrentLoopChanged(QAbstractAnimationJob *job) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickAnimationGroupPrivateCall0 call = reinterpret_cast<CuteQQuickAnimationGroupPrivateCall0>(taken[0]);
      call(this, job, &handled);
      if (handled) return;
    }
    QQuickAnimationGroupPrivate::animationCurrentLoopChanged(job);
  }
#endif  // QT_CONFIG(qml_animation)

#if QT_CONFIG(qml_animation)
  //  void QQuickAbstractAnimationPrivate::animationFinished(QAbstractAnima
  //      tionJob *a0)
  void animationFinished(QAbstractAnimationJob *a0) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickAnimationGroupPrivateCall1 call = reinterpret_cast<CuteQQuickAnimationGroupPrivateCall1>(taken[1]);
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
      CuteQQuickAnimationGroupPrivateCall2 call = reinterpret_cast<CuteQQuickAnimationGroupPrivateCall2>(taken[2]);
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
      CuteQQuickAnimationGroupPrivateCall3 call = reinterpret_cast<CuteQQuickAnimationGroupPrivateCall3>(taken[3]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QAnimationJobChangeListener::animationCurrentTimeChanged(a0, a1);
  }
#endif  // QT_CONFIG(qml_animation)
};

//  QQuickAnimationGroup *QQuickAnimationGroupPrivate::q_func()
extern "C" Q_DECL_EXPORT
QQuickAnimationGroup *ritual_ZN27QQuickAnimationGroupPrivate6q_funcEv(
    QQuickAnimationGroupPrivate *self) {
  return self->q_func();
}

//  const QQuickAnimationGroup *QQuickAnimationGroupPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QQuickAnimationGroup *ritual_ZNK27QQuickAnimationGroupPrivate6q_funcEv(
    const QQuickAnimationGroupPrivate *self) {
  return self->q_func();
}

//  QQuickAnimationGroupPrivate::QQuickAnimationGroupPrivate()
extern "C" Q_DECL_EXPORT
QQuickAnimationGroupPrivate *ritual_ZN27QQuickAnimationGroupPrivateC1Ev() {
  return new CuteQQuickAnimationGroupPrivate();
}

//  void QQuickAnimationGroupPrivate::restartFromCurrentLoop()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuickAnimationGroupPrivate22restartFromCurrentLoopEv(
    QQuickAnimationGroupPrivate *self) {
  self->restartFromCurrentLoop();
}

//  void QQuickAnimationGroupPrivate::animationCurrentLoopChanged(QAbstractAn
//      imationJob *job)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuickAnimationGroupPrivate27animationCurrentLoopChangedEP21QAbstractAnimationJob(
    QQuickAnimationGroupPrivate *self,
    QAbstractAnimationJob *job) {
  self->animationCurrentLoopChanged(job);
}

//  a Python function taken by a CuteQQuickAnimationGroupPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickAnimationGroupPrivate(
    QQuickAnimationGroupPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickAnimationGroupPrivate *>(self)->take(key, call);
}

//  void QQuickAnimationGroupPrivate::animationCurrentLoopChanged(QAbstractAn
//      imationJob *job)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN27QQuickAnimationGroupPrivate27animationCurrentLoopChangedEP21QAbstractAnimationJob(
    QQuickAnimationGroupPrivate *self,
    QAbstractAnimationJob *job) {
  self->QQuickAnimationGroupPrivate::animationCurrentLoopChanged(job);
}
