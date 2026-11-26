//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickanimator_p_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickanimator_p.h>
#include <QtQuick/6.12.0/QtQuick/private/qquickanimator_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/private/qquickanimator_p_p.h>
#include <QtQuick/private/qquickanimatorjob_p.h>
#include <QtQuick/private/qquickitem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quick/util/qquickanimator.cpp, line 185, as _ZN21QQuickAnimatorPrivate5applyEP17QQuickAnimatorJobRK7QStringR5QListI17QQuickStateActionERS5_I12QQmlPropertyEP7QObject
inline void QQuickAnimatorPrivate::apply(QQuickAnimatorJob *job,
                                     const QString &propertyName,
                                     QQuickStateActions &actions,
                                     QQmlProperties &modified,
                                     QObject *defaultTarget)
{

    if (actions.size()) {
        for (int i=0; i<actions.size(); ++i) {
            QQuickStateAction &action = actions[i];
            if (action.property.name() != propertyName)
                continue;
            modified << action.property;

            job->setTarget(qobject_cast<QQuickItem *>(action.property.object()));

            if (fromIsDefined)
                job->setFrom(from);
            else if (action.fromValue.isValid())
                job->setFrom(action.fromValue.toReal());
            else
                job->setFrom(action.property.read().toReal());

            if (toIsDefined)
                job->setTo(to);
            else if (action.toValue.isValid())
                job->setTo(action.toValue.toReal());
            else
                job->setTo(action.property.read().toReal());

            // This magic line is in sync with what PropertyAnimation does
            // and prevents the animation to end up in the "completeList"
            // which forces action.toValue to be written directly to
            // the item when a transition is cancelled.
            action.fromValue = action.toValue;
       }
    }

    if (modified.isEmpty()) {
        job->setTarget(target);
        if (fromIsDefined)
            job->setFrom(from);
        job->setTo(to);
    }

    if (!job->target()) {
        if (defaultProperty.object())
            job->setTarget(qobject_cast<QQuickItem *>(defaultProperty.object()));
        else
            job->setTarget(qobject_cast<QQuickItem *>(defaultTarget));
    }

    if (modified.isEmpty() && !fromIsDefined && job->target())
        job->setFrom(job->target()->property(propertyName.toLatin1()).toReal());

    job->setDuration(duration);
    job->setLoopCount(loopCount);
    job->setEasingCurve(easing);
}
//  -----------------------------------------------------------------------

//  A QQuickAnimatorPrivate that Python can take functions over in. Every QQuickAnimatorPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(qml_animation)
typedef void (*CuteQQuickAnimatorPrivateCall0)(const void *, QAbstractAnimationJob *, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQQuickAnimatorPrivateCall1)(const void *, QAbstractAnimationJob *, int, int, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQQuickAnimatorPrivateCall2)(const void *, QAbstractAnimationJob *, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQQuickAnimatorPrivateCall3)(const void *, QAbstractAnimationJob *, int, int *);
#endif  // QT_CONFIG(qml_animation)
class CuteQQuickAnimatorPrivate : public QQuickAnimatorPrivate {
public:
  using QQuickAnimatorPrivate::QQuickAnimatorPrivate;
  void *taken[4] = {};

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
#if QT_CONFIG(qml_animation)
    if (!std::strcmp(key, "_ZN27QAnimationJobChangeListener27animationCurrentLoopChangedEP21QAbstractAnimationJob")) {
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
  //  void QQuickAbstractAnimationPrivate::animationFinished(QAbstractAnima
  //      tionJob *a0)
  void animationFinished(QAbstractAnimationJob *a0) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickAnimatorPrivateCall0 call = reinterpret_cast<CuteQQuickAnimatorPrivateCall0>(taken[0]);
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
    if (taken[1]) {
      int handled = 0;
      CuteQQuickAnimatorPrivateCall1 call = reinterpret_cast<CuteQQuickAnimatorPrivateCall1>(taken[1]);
      call(this, a0, static_cast<int>(a1), static_cast<int>(a2), &handled);
      if (handled) return;
    }
    QAnimationJobChangeListener::animationStateChanged(a0, a1, a2);
  }
#endif  // QT_CONFIG(qml_animation)

#if QT_CONFIG(qml_animation)
  //  void QAnimationJobChangeListener::animationCurrentLoopChanged(QAbstra
  //      ctAnimationJob *a0)
  void animationCurrentLoopChanged(QAbstractAnimationJob *a0) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickAnimatorPrivateCall2 call = reinterpret_cast<CuteQQuickAnimatorPrivateCall2>(taken[2]);
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
    if (taken[3]) {
      int handled = 0;
      CuteQQuickAnimatorPrivateCall3 call = reinterpret_cast<CuteQQuickAnimatorPrivateCall3>(taken[3]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QAnimationJobChangeListener::animationCurrentTimeChanged(a0, a1);
  }
#endif  // QT_CONFIG(qml_animation)
};

//  QQuickAnimator *QQuickAnimatorPrivate::q_func()
extern "C" Q_DECL_EXPORT
QQuickAnimator *ritual_ZN21QQuickAnimatorPrivate6q_funcEv(
    QQuickAnimatorPrivate *self) {
  return self->q_func();
}

//  const QQuickAnimator *QQuickAnimatorPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QQuickAnimator *ritual_ZNK21QQuickAnimatorPrivate6q_funcEv(
    const QQuickAnimatorPrivate *self) {
  return self->q_func();
}

//  QQuickAnimatorPrivate::QQuickAnimatorPrivate()
extern "C" Q_DECL_EXPORT
QQuickAnimatorPrivate *ritual_ZN21QQuickAnimatorPrivateC1Ev() {
  return new CuteQQuickAnimatorPrivate();
}

//  void QQuickAnimatorPrivate::apply(QQuickAnimatorJob *job, const QString
//      &propertyName, QQuickStateActions &actions, QQmlProperties &modified,
//      QObject *defaultTarget)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickAnimatorPrivate5applyEP17QQuickAnimatorJobRK7QStringR5QListI17QQuickStateActionERS5_I12QQmlPropertyEP7QObject(
    QQuickAnimatorPrivate *self,
    QQuickAnimatorJob *job,
    const QString *propertyName,
    QQuickStateActions *actions,
    QQmlProperties *modified,
    QObject *defaultTarget) {
  self->apply(job, *propertyName, *actions, *modified, defaultTarget);
}

//  a Python function taken by a CuteQQuickAnimatorPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickAnimatorPrivate(
    QQuickAnimatorPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickAnimatorPrivate *>(self)->take(key, call);
}
