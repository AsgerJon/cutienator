//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickitemanimation_p_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(quick_path)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickitemanimation_p.h>
#include <QtQuick/6.12.0/QtQuick/private/qquickitemanimation_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QQuickPathAnimationPrivate that Python can take functions over in. Every QQuickPathAnimationPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(qml_animation)
typedef void (*CuteQQuickPathAnimationPrivateCall0)(const void *, QAbstractAnimationJob *, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQQuickPathAnimationPrivateCall1)(const void *, QAbstractAnimationJob *, int, int, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQQuickPathAnimationPrivateCall2)(const void *, QAbstractAnimationJob *, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQQuickPathAnimationPrivateCall3)(const void *, QAbstractAnimationJob *, int, int *);
#endif  // QT_CONFIG(qml_animation)
class CuteQQuickPathAnimationPrivate : public QQuickPathAnimationPrivate {
public:
  using QQuickPathAnimationPrivate::QQuickPathAnimationPrivate;
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
      CuteQQuickPathAnimationPrivateCall0 call = reinterpret_cast<CuteQQuickPathAnimationPrivateCall0>(taken[0]);
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
      CuteQQuickPathAnimationPrivateCall1 call = reinterpret_cast<CuteQQuickPathAnimationPrivateCall1>(taken[1]);
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
      CuteQQuickPathAnimationPrivateCall2 call = reinterpret_cast<CuteQQuickPathAnimationPrivateCall2>(taken[2]);
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
      CuteQQuickPathAnimationPrivateCall3 call = reinterpret_cast<CuteQQuickPathAnimationPrivateCall3>(taken[3]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QAnimationJobChangeListener::animationCurrentTimeChanged(a0, a1);
  }
#endif  // QT_CONFIG(qml_animation)
};

//  QQuickPathAnimation *QQuickPathAnimationPrivate::q_func()
extern "C" Q_DECL_EXPORT
QQuickPathAnimation *ritual_ZN26QQuickPathAnimationPrivate6q_funcEv(
    QQuickPathAnimationPrivate *self) {
  return self->q_func();
}

//  const QQuickPathAnimation *QQuickPathAnimationPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QQuickPathAnimation *ritual_ZNK26QQuickPathAnimationPrivate6q_funcEv(
    const QQuickPathAnimationPrivate *self) {
  return self->q_func();
}

//  QQuickPathAnimationPrivate::QQuickPathAnimationPrivate()
extern "C" Q_DECL_EXPORT
QQuickPathAnimationPrivate *ritual_ZN26QQuickPathAnimationPrivateC1Ev() {
  return new CuteQQuickPathAnimationPrivate();
}

//  a Python function taken by a CuteQQuickPathAnimationPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickPathAnimationPrivate(
    QQuickPathAnimationPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickPathAnimationPrivate *>(self)->take(key, call);
}

#endif  // QT_CONFIG(quick_path)
