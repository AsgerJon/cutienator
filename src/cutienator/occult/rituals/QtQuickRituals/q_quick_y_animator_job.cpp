//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickanimatorjob_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickanimatorjob_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qdebug.h>
#include <cstring>

//  A QQuickYAnimatorJob that Python can take functions over in. Every QQuickYAnimatorJob
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(qml_animation)
typedef void (*CuteQQuickYAnimatorJobCall0)(const void *, int, int *);
#endif  // QT_CONFIG(qml_animation)
typedef void (*CuteQQuickYAnimatorJobCall1)(const void *, int *);
typedef void (*CuteQQuickYAnimatorJobCall2)(const void *, int *);
typedef void (*CuteQQuickYAnimatorJobCall3)(const void *, int *);
typedef void (*CuteQQuickYAnimatorJobCall4)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickYAnimatorJobCall5)(const void *, int *);
#if QT_CONFIG(qml_animation)
typedef int (*CuteQQuickYAnimatorJobCall6)(const void *, int *);
#endif  // QT_CONFIG(qml_animation)
typedef void (*CuteQQuickYAnimatorJobCall7)(const void *, QQuickAnimatorController *, int *);
typedef void (*CuteQQuickYAnimatorJobCall8)(const void *, int *);
#if QT_CONFIG(qml_animation)
typedef void (*CuteQQuickYAnimatorJobCall9)(const void *, const QDebug *, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQQuickYAnimatorJobCall10)(const void *, int, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQQuickYAnimatorJobCall11)(const void *, int, int, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQQuickYAnimatorJobCall12)(const void *, int, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQQuickYAnimatorJobCall13)(const void *, int *);
#endif  // QT_CONFIG(qml_animation)
class CuteQQuickYAnimatorJob : public QQuickYAnimatorJob {
public:
  using QQuickYAnimatorJob::QQuickYAnimatorJob;
  void *taken[14] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(qml_animation)
    if (!std::strcmp(key, "_ZN21QAbstractAnimationJob17updateCurrentTimeEi")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_animation)
    if (!std::strcmp(key, "_ZN17QQuickAnimatorJob9writeBackEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickAnimatorJob6commitEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickAnimatorJob7preSyncEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickAnimatorJob9setTargetEP10QQuickItem")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickAnimatorJob10invalidateEv")) {
      taken[5] = call;
      return true;
    }
#if QT_CONFIG(qml_animation)
    if (!std::strcmp(key, "_ZNK21QAbstractAnimationJob8durationEv")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_animation)
    if (!std::strcmp(key, "_ZN17QQuickAnimatorJob10initializeEP24QQuickAnimatorController")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickAnimatorJob8postSyncEv")) {
      taken[8] = call;
      return true;
    }
#if QT_CONFIG(qml_animation)
    if (!std::strcmp(key, "_ZNK21QAbstractAnimationJob14debugAnimationE6QDebug")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
    if (!std::strcmp(key, "_ZN21QAbstractAnimationJob15updateLoopCountEi")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
    if (!std::strcmp(key, "_ZN21QAbstractAnimationJob11updateStateENS_5StateES0_")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
    if (!std::strcmp(key, "_ZN21QAbstractAnimationJob15updateDirectionENS_9DirectionE")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
    if (!std::strcmp(key, "_ZN21QAbstractAnimationJob28topLevelAnimationLoopChangedEv")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_animation)
    return false;
  }

#if QT_CONFIG(qml_animation)
  //  void QQuickYAnimatorJob::updateCurrentTime(int time)
  void updateCurrentTime(int time) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickYAnimatorJobCall0 call = reinterpret_cast<CuteQQuickYAnimatorJobCall0>(taken[0]);
      call(this, time, &handled);
      if (handled) return;
    }
    QQuickYAnimatorJob::updateCurrentTime(time);
  }
#endif  // QT_CONFIG(qml_animation)

  //  void QQuickYAnimatorJob::writeBack()
  void writeBack() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickYAnimatorJobCall1 call = reinterpret_cast<CuteQQuickYAnimatorJobCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickYAnimatorJob::writeBack();
  }

  //  void QQuickTransformAnimatorJob::commit()
  void commit() override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickYAnimatorJobCall2 call = reinterpret_cast<CuteQQuickYAnimatorJobCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickTransformAnimatorJob::commit();
  }

  //  void QQuickTransformAnimatorJob::preSync()
  void preSync() override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickYAnimatorJobCall3 call = reinterpret_cast<CuteQQuickYAnimatorJobCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickTransformAnimatorJob::preSync();
  }

  //  void QQuickTransformAnimatorJob::setTarget(QQuickItem *item)
  void setTarget(QQuickItem *item) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickYAnimatorJobCall4 call = reinterpret_cast<CuteQQuickYAnimatorJobCall4>(taken[4]);
      call(this, item, &handled);
      if (handled) return;
    }
    QQuickTransformAnimatorJob::setTarget(item);
  }

  //  void QQuickTransformAnimatorJob::invalidate()
  void invalidate() override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickYAnimatorJobCall5 call = reinterpret_cast<CuteQQuickYAnimatorJobCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickTransformAnimatorJob::invalidate();
  }

#if QT_CONFIG(qml_animation)
  //  int QQuickAnimatorJob::duration() const
  int duration() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickYAnimatorJobCall6 call = reinterpret_cast<CuteQQuickYAnimatorJobCall6>(taken[6]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickAnimatorJob::duration();
  }
#endif  // QT_CONFIG(qml_animation)

  //  void QQuickAnimatorJob::initialize(QQuickAnimatorController
  //      *controller)
  void initialize(QQuickAnimatorController *controller) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickYAnimatorJobCall7 call = reinterpret_cast<CuteQQuickYAnimatorJobCall7>(taken[7]);
      call(this, controller, &handled);
      if (handled) return;
    }
    QQuickAnimatorJob::initialize(controller);
  }

  //  void QQuickAnimatorJob::postSync()
  void postSync() override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickYAnimatorJobCall8 call = reinterpret_cast<CuteQQuickYAnimatorJobCall8>(taken[8]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickAnimatorJob::postSync();
  }

#if QT_CONFIG(qml_animation)
  //  void QQuickAnimatorJob::debugAnimation(QDebug d) const
  void debugAnimation(QDebug d) const override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickYAnimatorJobCall9 call = reinterpret_cast<CuteQQuickYAnimatorJobCall9>(taken[9]);
      call(this, &d, &handled);
      if (handled) return;
    }
    QQuickAnimatorJob::debugAnimation(d);
  }
#endif  // QT_CONFIG(qml_animation)

#if QT_CONFIG(qml_animation)
  //  void QAbstractAnimationJob::updateLoopCount(int a0)
  void updateLoopCount(int a0) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickYAnimatorJobCall10 call = reinterpret_cast<CuteQQuickYAnimatorJobCall10>(taken[10]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QAbstractAnimationJob::updateLoopCount(a0);
  }
#endif  // QT_CONFIG(qml_animation)

#if QT_CONFIG(qml_animation)
  //  void QAbstractAnimationJob::updateState(QAbstractAnimationJob::State
  //      newState, QAbstractAnimationJob::State oldState)
  void updateState(
      QAbstractAnimationJob::State newState,
      QAbstractAnimationJob::State oldState) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickYAnimatorJobCall11 call = reinterpret_cast<CuteQQuickYAnimatorJobCall11>(taken[11]);
      call(this, static_cast<int>(newState), static_cast<int>(oldState), &handled);
      if (handled) return;
    }
    QAbstractAnimationJob::updateState(newState, oldState);
  }
#endif  // QT_CONFIG(qml_animation)

#if QT_CONFIG(qml_animation)
  //  void QAbstractAnimationJob::updateDirection(QAbstractAnimationJob::Di
  //      rection direction)
  void updateDirection(QAbstractAnimationJob::Direction direction) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickYAnimatorJobCall12 call = reinterpret_cast<CuteQQuickYAnimatorJobCall12>(taken[12]);
      call(this, static_cast<int>(direction), &handled);
      if (handled) return;
    }
    QAbstractAnimationJob::updateDirection(direction);
  }
#endif  // QT_CONFIG(qml_animation)

#if QT_CONFIG(qml_animation)
  //  void QAbstractAnimationJob::topLevelAnimationLoopChanged()
  void topLevelAnimationLoopChanged() override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickYAnimatorJobCall13 call = reinterpret_cast<CuteQQuickYAnimatorJobCall13>(taken[13]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractAnimationJob::topLevelAnimationLoopChanged();
  }
#endif  // QT_CONFIG(qml_animation)
};

//  void QQuickYAnimatorJob::updateCurrentTime(int time)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickYAnimatorJob17updateCurrentTimeEi(
    QQuickYAnimatorJob *self,
    int time) {
  self->updateCurrentTime(time);
}

//  void QQuickYAnimatorJob::writeBack()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickYAnimatorJob9writeBackEv(QQuickYAnimatorJob *self) {
  self->writeBack();
}

//  a Python function taken by a CuteQQuickYAnimatorJob, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickYAnimatorJob(
    QQuickYAnimatorJob *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickYAnimatorJob *>(self)->take(key, call);
}

//  void QQuickYAnimatorJob::updateCurrentTime(int time)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QQuickYAnimatorJob17updateCurrentTimeEi(
    QQuickYAnimatorJob *self,
    int time) {
  self->QQuickYAnimatorJob::updateCurrentTime(time);
}

//  void QQuickYAnimatorJob::writeBack()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QQuickYAnimatorJob9writeBackEv(
    QQuickYAnimatorJob *self) {
  self->QQuickYAnimatorJob::writeBack();
}
