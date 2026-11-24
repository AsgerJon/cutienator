//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickanimation_p_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickanimation_p.h>
#include <QtQuick/6.12.0/QtQuick/private/qquickanimation_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QQuickPropertyAnimationPrivate that Python can take functions over in. Every QQuickPropertyAnimationPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(qml_animation)
typedef void (*CuteQQuickPropertyAnimationPrivateCall0)(const void *, QAbstractAnimationJob *, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQQuickPropertyAnimationPrivateCall1)(const void *, QAbstractAnimationJob *, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQQuickPropertyAnimationPrivateCall2)(const void *, QAbstractAnimationJob *, int, int, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQQuickPropertyAnimationPrivateCall3)(const void *, QAbstractAnimationJob *, int, int *);
#endif  // QT_CONFIG(qml_animation)
class CuteQQuickPropertyAnimationPrivate : public QQuickPropertyAnimationPrivate {
public:
  using QQuickPropertyAnimationPrivate::QQuickPropertyAnimationPrivate;
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
      CuteQQuickPropertyAnimationPrivateCall0 call = reinterpret_cast<CuteQQuickPropertyAnimationPrivateCall0>(taken[0]);
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
      CuteQQuickPropertyAnimationPrivateCall1 call = reinterpret_cast<CuteQQuickPropertyAnimationPrivateCall1>(taken[1]);
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
      CuteQQuickPropertyAnimationPrivateCall2 call = reinterpret_cast<CuteQQuickPropertyAnimationPrivateCall2>(taken[2]);
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
      CuteQQuickPropertyAnimationPrivateCall3 call = reinterpret_cast<CuteQQuickPropertyAnimationPrivateCall3>(taken[3]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QAnimationJobChangeListener::animationCurrentTimeChanged(a0, a1);
  }
#endif  // QT_CONFIG(qml_animation)
};

//  QQuickPropertyAnimation *QQuickPropertyAnimationPrivate::q_func()
extern "C" Q_DECL_EXPORT
QQuickPropertyAnimation *ritual_ZN30QQuickPropertyAnimationPrivate6q_funcEv(
    QQuickPropertyAnimationPrivate *self) {
  return self->q_func();
}

//  const QQuickPropertyAnimation *QQuickPropertyAnimationPrivate::q_func()
//      const
extern "C" Q_DECL_EXPORT
const QQuickPropertyAnimation *ritual_ZNK30QQuickPropertyAnimationPrivate6q_funcEv(
    const QQuickPropertyAnimationPrivate *self) {
  return self->q_func();
}

//  QQuickPropertyAnimationPrivate::QQuickPropertyAnimationPrivate()
extern "C" Q_DECL_EXPORT
QQuickPropertyAnimationPrivate *ritual_ZN30QQuickPropertyAnimationPrivateC1Ev() {
  return new CuteQQuickPropertyAnimationPrivate();
}

//  void QQuickPropertyAnimationPrivate::animationCurrentLoopChanged(QAbstrac
//      tAnimationJob *job)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuickPropertyAnimationPrivate27animationCurrentLoopChangedEP21QAbstractAnimationJob(
    QQuickPropertyAnimationPrivate *self,
    QAbstractAnimationJob *job) {
  self->animationCurrentLoopChanged(job);
}

//  a Python function taken by a CuteQQuickPropertyAnimationPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickPropertyAnimationPrivate(
    QQuickPropertyAnimationPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickPropertyAnimationPrivate *>(self)->take(key, call);
}

//  void QQuickPropertyAnimationPrivate::animationCurrentLoopChanged(QAbstrac
//      tAnimationJob *job)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN30QQuickPropertyAnimationPrivate27animationCurrentLoopChangedEP21QAbstractAnimationJob(
    QQuickPropertyAnimationPrivate *self,
    QAbstractAnimationJob *job) {
  self->QQuickPropertyAnimationPrivate::animationCurrentLoopChanged(job);
}
