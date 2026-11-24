//  Written by dev_tooling.RitualGenerator from the records of QtPositioningQ
//  uick/6.12.0/QtPositioningQuick/private/qquickgeocoordinateanimation_p_p.h
//  , Qt 6.12.0. Changes made here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtPositioningQuick/6.12.0/QtPositioningQuick/private/qpositioningquickglobal_p.h>
#include <QtPositioningQuick/QtPositioningQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtPositioningQuick/6.12.0/QtPositioningQuick/private/qquickgeocoordinateanimation_p.h>
#include <QtPositioningQuick/6.12.0/QtPositioningQuick/private/qquickgeocoordinateanimation_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QQuickGeoCoordinateAnimationPrivate that Python can take functions over in. Every QQuickGeoCoordinateAnimationPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(qml_animation)
typedef void (*CuteQQuickGeoCoordinateAnimationPrivateCall0)(const void *, QAbstractAnimationJob *, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQQuickGeoCoordinateAnimationPrivateCall1)(const void *, QAbstractAnimationJob *, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQQuickGeoCoordinateAnimationPrivateCall2)(const void *, QAbstractAnimationJob *, int, int, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQQuickGeoCoordinateAnimationPrivateCall3)(const void *, QAbstractAnimationJob *, int, int *);
#endif  // QT_CONFIG(qml_animation)
class CuteQQuickGeoCoordinateAnimationPrivate : public QQuickGeoCoordinateAnimationPrivate {
public:
  using QQuickGeoCoordinateAnimationPrivate::QQuickGeoCoordinateAnimationPrivate;
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
      CuteQQuickGeoCoordinateAnimationPrivateCall0 call = reinterpret_cast<CuteQQuickGeoCoordinateAnimationPrivateCall0>(taken[0]);
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
      CuteQQuickGeoCoordinateAnimationPrivateCall1 call = reinterpret_cast<CuteQQuickGeoCoordinateAnimationPrivateCall1>(taken[1]);
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
      CuteQQuickGeoCoordinateAnimationPrivateCall2 call = reinterpret_cast<CuteQQuickGeoCoordinateAnimationPrivateCall2>(taken[2]);
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
      CuteQQuickGeoCoordinateAnimationPrivateCall3 call = reinterpret_cast<CuteQQuickGeoCoordinateAnimationPrivateCall3>(taken[3]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QAnimationJobChangeListener::animationCurrentTimeChanged(a0, a1);
  }
#endif  // QT_CONFIG(qml_animation)
};

//  QQuickGeoCoordinateAnimation
//      *QQuickGeoCoordinateAnimationPrivate::q_func()
extern "C" Q_DECL_EXPORT
QQuickGeoCoordinateAnimation *ritual_ZN35QQuickGeoCoordinateAnimationPrivate6q_funcEv(
    QQuickGeoCoordinateAnimationPrivate *self) {
  return self->q_func();
}

//  const QQuickGeoCoordinateAnimation
//      *QQuickGeoCoordinateAnimationPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QQuickGeoCoordinateAnimation *ritual_ZNK35QQuickGeoCoordinateAnimationPrivate6q_funcEv(
    const QQuickGeoCoordinateAnimationPrivate *self) {
  return self->q_func();
}

//  void QQuickGeoCoordinateAnimationPrivate::setDirection(QQuickGeoCoordinat
//      eAnimation::Direction direction)
extern "C" Q_DECL_EXPORT
void ritual_ZN35QQuickGeoCoordinateAnimationPrivate12setDirectionEN28QQuickGeoCoordinateAnimation9DirectionE(
    QQuickGeoCoordinateAnimationPrivate *self,
    QQuickGeoCoordinateAnimation::Direction direction) {
  self->setDirection(direction);
}

//  void QQuickGeoCoordinateAnimationPrivate::directionChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN35QQuickGeoCoordinateAnimationPrivate16directionChangedEv(
    QQuickGeoCoordinateAnimationPrivate *self) {
  self->directionChanged();
}

//  a Python function taken by a CuteQQuickGeoCoordinateAnimationPrivate, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickGeoCoordinateAnimationPrivate(
    QQuickGeoCoordinateAnimationPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickGeoCoordinateAnimationPrivate *>(self)->take(key, call);
}
