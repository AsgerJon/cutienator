//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qpauseanimationjob_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQml/qtqmlglobal.h>
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#if QT_CONFIG(qml_animation)
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qpauseanimationjob_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qdebug.h>
#include <cstring>

//  Only a class built on QPauseAnimationJob may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQPauseAnimationJob : QPauseAnimationJob {
  using QPauseAnimationJob::updateCurrentTime;
  using QPauseAnimationJob::debugAnimation;
};

//  A QPauseAnimationJob that Python can take functions over in. Every QPauseAnimationJob
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(qml_animation)
typedef int (*CuteQPauseAnimationJobCall0)(const void *, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQPauseAnimationJobCall1)(const void *, int, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQPauseAnimationJobCall2)(const void *, const QDebug *, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQPauseAnimationJobCall3)(const void *, int, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQPauseAnimationJobCall4)(const void *, int, int, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQPauseAnimationJobCall5)(const void *, int, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQPauseAnimationJobCall6)(const void *, int *);
#endif  // QT_CONFIG(qml_animation)
class CuteQPauseAnimationJob : public QPauseAnimationJob {
public:
  using QPauseAnimationJob::QPauseAnimationJob;
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
    if (!std::strcmp(key, "_ZNK21QAbstractAnimationJob14debugAnimationE6QDebug")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
    if (!std::strcmp(key, "_ZN21QAbstractAnimationJob15updateLoopCountEi")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
    if (!std::strcmp(key, "_ZN21QAbstractAnimationJob11updateStateENS_5StateES0_")) {
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
  //  int QPauseAnimationJob::duration() const
  int duration() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQPauseAnimationJobCall0 call = reinterpret_cast<CuteQPauseAnimationJobCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QPauseAnimationJob::duration();
  }
#endif  // QT_CONFIG(qml_animation)

#if QT_CONFIG(qml_animation)
  //  void QPauseAnimationJob::updateCurrentTime(int a0)
  void updateCurrentTime(int a0) override {
    if (taken[1]) {
      int handled = 0;
      CuteQPauseAnimationJobCall1 call = reinterpret_cast<CuteQPauseAnimationJobCall1>(taken[1]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QPauseAnimationJob::updateCurrentTime(a0);
  }
#endif  // QT_CONFIG(qml_animation)

#if QT_CONFIG(qml_animation)
  //  void QPauseAnimationJob::debugAnimation(QDebug d) const
  void debugAnimation(QDebug d) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQPauseAnimationJobCall2 call = reinterpret_cast<CuteQPauseAnimationJobCall2>(taken[2]);
      call(this, &d, &handled);
      if (handled) return;
    }
    QPauseAnimationJob::debugAnimation(d);
  }
#endif  // QT_CONFIG(qml_animation)

#if QT_CONFIG(qml_animation)
  //  void QAbstractAnimationJob::updateLoopCount(int a0)
  void updateLoopCount(int a0) override {
    if (taken[3]) {
      int handled = 0;
      CuteQPauseAnimationJobCall3 call = reinterpret_cast<CuteQPauseAnimationJobCall3>(taken[3]);
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
    if (taken[4]) {
      int handled = 0;
      CuteQPauseAnimationJobCall4 call = reinterpret_cast<CuteQPauseAnimationJobCall4>(taken[4]);
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
    if (taken[5]) {
      int handled = 0;
      CuteQPauseAnimationJobCall5 call = reinterpret_cast<CuteQPauseAnimationJobCall5>(taken[5]);
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
      CuteQPauseAnimationJobCall6 call = reinterpret_cast<CuteQPauseAnimationJobCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractAnimationJob::topLevelAnimationLoopChanged();
  }
#endif  // QT_CONFIG(qml_animation)
};

//  QPauseAnimationJob::QPauseAnimationJob(int duration)
extern "C" Q_DECL_EXPORT
QPauseAnimationJob *ritual_ZN18QPauseAnimationJobC1Ei(int duration) {
  return new CuteQPauseAnimationJob(duration);
}

//  QPauseAnimationJob::~QPauseAnimationJob()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QPauseAnimationJobD1Ev(QPauseAnimationJob *self) {
  delete self;
}

//  int QPauseAnimationJob::duration() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QPauseAnimationJob8durationEv(
    const QPauseAnimationJob *self) {
  return self->duration();
}

//  void QPauseAnimationJob::setDuration(int msecs)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QPauseAnimationJob11setDurationEi(
    QPauseAnimationJob *self,
    int msecs) {
  self->setDuration(msecs);
}

//  void QPauseAnimationJob::updateCurrentTime(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QPauseAnimationJob17updateCurrentTimeEi(
    QPauseAnimationJob *self,
    int a0) {
  self->updateCurrentTime(a0);
}

//  void QPauseAnimationJob::debugAnimation(QDebug d) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK18QPauseAnimationJob14debugAnimationE6QDebug(
    const QPauseAnimationJob *self,
    const QDebug *d) {
  self->debugAnimation(*d);
}

//  a Python function taken by a CuteQPauseAnimationJob, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPauseAnimationJob(
    QPauseAnimationJob *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPauseAnimationJob *>(self)->take(key, call);
}

//  int QPauseAnimationJob::duration() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK18QPauseAnimationJob8durationEv(
    const QPauseAnimationJob *self) {
  return self->QPauseAnimationJob::duration();
}

//  void QPauseAnimationJob::updateCurrentTime(int a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QPauseAnimationJob17updateCurrentTimeEi(
    QPauseAnimationJob *self,
    int a0) {
  static_cast<OwnQPauseAnimationJob *>(self)->OwnQPauseAnimationJob::updateCurrentTime(
      a0);
}

//  void QPauseAnimationJob::debugAnimation(QDebug d) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK18QPauseAnimationJob14debugAnimationE6QDebug(
    const QPauseAnimationJob *self,
    const QDebug *d) {
  static_cast<const OwnQPauseAnimationJob *>(self)->OwnQPauseAnimationJob::debugAnimation(
      *d);
}

#endif  // QT_CONFIG(qml_animation)
