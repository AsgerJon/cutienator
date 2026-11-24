//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qcontinuinganimationgroupjob_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQml/qtqmlglobal.h>
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#if QT_CONFIG(qml_animation)
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qcontinuinganimationgroupjob_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qdebug.h>
#include <cstring>

//  Only a class built on QContinuingAnimationGroupJob may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQContinuingAnimationGroupJob : QContinuingAnimationGroupJob {
  using QContinuingAnimationGroupJob::updateCurrentTime;
  using QContinuingAnimationGroupJob::updateState;
  using QContinuingAnimationGroupJob::updateDirection;
  using QContinuingAnimationGroupJob::uncontrolledAnimationFinished;
  using QContinuingAnimationGroupJob::debugAnimation;
};

//  A QContinuingAnimationGroupJob that Python can take functions over in. Every QContinuingAnimationGroupJob
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(qml_animation)
typedef int (*CuteQContinuingAnimationGroupJobCall0)(const void *, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQContinuingAnimationGroupJobCall1)(const void *, int, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQContinuingAnimationGroupJobCall2)(const void *, int, int, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQContinuingAnimationGroupJobCall3)(const void *, int, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQContinuingAnimationGroupJobCall4)(const void *, QAbstractAnimationJob *, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQContinuingAnimationGroupJobCall5)(const void *, const QDebug *, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQContinuingAnimationGroupJobCall6)(const void *, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQContinuingAnimationGroupJobCall7)(const void *, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQContinuingAnimationGroupJobCall8)(const void *, QAbstractAnimationJob *, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQContinuingAnimationGroupJobCall9)(const void *, QAbstractAnimationJob *, QAbstractAnimationJob *, QAbstractAnimationJob *, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQContinuingAnimationGroupJobCall10)(const void *, int, int *);
#endif  // QT_CONFIG(qml_animation)
class CuteQContinuingAnimationGroupJob : public QContinuingAnimationGroupJob {
public:
  using QContinuingAnimationGroupJob::QContinuingAnimationGroupJob;
  void *taken[11] = {};

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
    if (!std::strcmp(key, "_ZN21QAbstractAnimationJob11updateStateENS_5StateES0_")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
    if (!std::strcmp(key, "_ZN21QAbstractAnimationJob15updateDirectionENS_9DirectionE")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
    if (!std::strcmp(key, "_ZN18QAnimationGroupJob29uncontrolledAnimationFinishedEP21QAbstractAnimationJob")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
    if (!std::strcmp(key, "_ZNK21QAbstractAnimationJob14debugAnimationE6QDebug")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
    if (!std::strcmp(key, "_ZN18QAnimationGroupJob5clearEv")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
    if (!std::strcmp(key, "_ZN21QAbstractAnimationJob28topLevelAnimationLoopChangedEv")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
    if (!std::strcmp(key, "_ZN18QAnimationGroupJob17animationInsertedEP21QAbstractAnimationJob")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
    if (!std::strcmp(key, "_ZN18QAnimationGroupJob16animationRemovedEP21QAbstractAnimationJobS1_S1_")) {
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
    return false;
  }

#if QT_CONFIG(qml_animation)
  //  int QContinuingAnimationGroupJob::duration() const
  int duration() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQContinuingAnimationGroupJobCall0 call = reinterpret_cast<CuteQContinuingAnimationGroupJobCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QContinuingAnimationGroupJob::duration();
  }
#endif  // QT_CONFIG(qml_animation)

#if QT_CONFIG(qml_animation)
  //  void QContinuingAnimationGroupJob::updateCurrentTime(int currentTime)
  void updateCurrentTime(int currentTime) override {
    if (taken[1]) {
      int handled = 0;
      CuteQContinuingAnimationGroupJobCall1 call = reinterpret_cast<CuteQContinuingAnimationGroupJobCall1>(taken[1]);
      call(this, currentTime, &handled);
      if (handled) return;
    }
    QContinuingAnimationGroupJob::updateCurrentTime(currentTime);
  }
#endif  // QT_CONFIG(qml_animation)

#if QT_CONFIG(qml_animation)
  //  void QContinuingAnimationGroupJob::updateState(QAbstractAnimationJob:
  //      :State newState, QAbstractAnimationJob::State oldState)
  void updateState(
      QAbstractAnimationJob::State newState,
      QAbstractAnimationJob::State oldState) override {
    if (taken[2]) {
      int handled = 0;
      CuteQContinuingAnimationGroupJobCall2 call = reinterpret_cast<CuteQContinuingAnimationGroupJobCall2>(taken[2]);
      call(this, static_cast<int>(newState), static_cast<int>(oldState), &handled);
      if (handled) return;
    }
    QContinuingAnimationGroupJob::updateState(newState, oldState);
  }
#endif  // QT_CONFIG(qml_animation)

#if QT_CONFIG(qml_animation)
  //  void QContinuingAnimationGroupJob::updateDirection(QAbstractAnimation
  //      Job::Direction direction)
  void updateDirection(QAbstractAnimationJob::Direction direction) override {
    if (taken[3]) {
      int handled = 0;
      CuteQContinuingAnimationGroupJobCall3 call = reinterpret_cast<CuteQContinuingAnimationGroupJobCall3>(taken[3]);
      call(this, static_cast<int>(direction), &handled);
      if (handled) return;
    }
    QContinuingAnimationGroupJob::updateDirection(direction);
  }
#endif  // QT_CONFIG(qml_animation)

#if QT_CONFIG(qml_animation)
  //  void QContinuingAnimationGroupJob::uncontrolledAnimationFinished(QAbs
  //      tractAnimationJob *animation)
  void uncontrolledAnimationFinished(
      QAbstractAnimationJob *animation) override {
    if (taken[4]) {
      int handled = 0;
      CuteQContinuingAnimationGroupJobCall4 call = reinterpret_cast<CuteQContinuingAnimationGroupJobCall4>(taken[4]);
      call(this, animation, &handled);
      if (handled) return;
    }
    QContinuingAnimationGroupJob::uncontrolledAnimationFinished(animation);
  }
#endif  // QT_CONFIG(qml_animation)

#if QT_CONFIG(qml_animation)
  //  void QContinuingAnimationGroupJob::debugAnimation(QDebug d) const
  void debugAnimation(QDebug d) const override {
    if (taken[5]) {
      int handled = 0;
      CuteQContinuingAnimationGroupJobCall5 call = reinterpret_cast<CuteQContinuingAnimationGroupJobCall5>(taken[5]);
      call(this, &d, &handled);
      if (handled) return;
    }
    QContinuingAnimationGroupJob::debugAnimation(d);
  }
#endif  // QT_CONFIG(qml_animation)

#if QT_CONFIG(qml_animation)
  //  void QAnimationGroupJob::clear()
  void clear() override {
    if (taken[6]) {
      int handled = 0;
      CuteQContinuingAnimationGroupJobCall6 call = reinterpret_cast<CuteQContinuingAnimationGroupJobCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QAnimationGroupJob::clear();
  }
#endif  // QT_CONFIG(qml_animation)

#if QT_CONFIG(qml_animation)
  //  void QAnimationGroupJob::topLevelAnimationLoopChanged()
  void topLevelAnimationLoopChanged() override {
    if (taken[7]) {
      int handled = 0;
      CuteQContinuingAnimationGroupJobCall7 call = reinterpret_cast<CuteQContinuingAnimationGroupJobCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
    QAnimationGroupJob::topLevelAnimationLoopChanged();
  }
#endif  // QT_CONFIG(qml_animation)

#if QT_CONFIG(qml_animation)
  //  void QAnimationGroupJob::animationInserted(QAbstractAnimationJob *a0)
  void animationInserted(QAbstractAnimationJob *a0) override {
    if (taken[8]) {
      int handled = 0;
      CuteQContinuingAnimationGroupJobCall8 call = reinterpret_cast<CuteQContinuingAnimationGroupJobCall8>(taken[8]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QAnimationGroupJob::animationInserted(a0);
  }
#endif  // QT_CONFIG(qml_animation)

#if QT_CONFIG(qml_animation)
  //  void QAnimationGroupJob::animationRemoved(QAbstractAnimationJob *a0,
  //      QAbstractAnimationJob *a1, QAbstractAnimationJob *a2)
  void animationRemoved(
      QAbstractAnimationJob *a0,
      QAbstractAnimationJob *a1,
      QAbstractAnimationJob *a2) override {
    if (taken[9]) {
      int handled = 0;
      CuteQContinuingAnimationGroupJobCall9 call = reinterpret_cast<CuteQContinuingAnimationGroupJobCall9>(taken[9]);
      call(this, a0, a1, a2, &handled);
      if (handled) return;
    }
    QAnimationGroupJob::animationRemoved(a0, a1, a2);
  }
#endif  // QT_CONFIG(qml_animation)

#if QT_CONFIG(qml_animation)
  //  void QAbstractAnimationJob::updateLoopCount(int a0)
  void updateLoopCount(int a0) override {
    if (taken[10]) {
      int handled = 0;
      CuteQContinuingAnimationGroupJobCall10 call = reinterpret_cast<CuteQContinuingAnimationGroupJobCall10>(taken[10]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QAbstractAnimationJob::updateLoopCount(a0);
  }
#endif  // QT_CONFIG(qml_animation)
};

//  QContinuingAnimationGroupJob::QContinuingAnimationGroupJob()
extern "C" Q_DECL_EXPORT
QContinuingAnimationGroupJob *ritual_ZN28QContinuingAnimationGroupJobC1Ev() {
  return new CuteQContinuingAnimationGroupJob();
}

//  QContinuingAnimationGroupJob::~QContinuingAnimationGroupJob()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QContinuingAnimationGroupJobD1Ev(
    QContinuingAnimationGroupJob *self) {
  delete self;
}

//  int QContinuingAnimationGroupJob::duration() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK28QContinuingAnimationGroupJob8durationEv(
    const QContinuingAnimationGroupJob *self) {
  return self->duration();
}

//  void QContinuingAnimationGroupJob::updateCurrentTime(int currentTime)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QContinuingAnimationGroupJob17updateCurrentTimeEi(
    QContinuingAnimationGroupJob *self,
    int currentTime) {
  self->updateCurrentTime(currentTime);
}

//  void
//      QContinuingAnimationGroupJob::updateState(QAbstractAnimationJob::Stat
//      e newState, QAbstractAnimationJob::State oldState)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QContinuingAnimationGroupJob11updateStateEN21QAbstractAnimationJob5StateES1_(
    QContinuingAnimationGroupJob *self,
    QAbstractAnimationJob::State newState,
    QAbstractAnimationJob::State oldState) {
  self->updateState(newState, oldState);
}

//  void QContinuingAnimationGroupJob::updateDirection(QAbstractAnimationJob:
//      :Direction direction)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QContinuingAnimationGroupJob15updateDirectionEN21QAbstractAnimationJob9DirectionE(
    QContinuingAnimationGroupJob *self,
    QAbstractAnimationJob::Direction direction) {
  self->updateDirection(direction);
}

//  void QContinuingAnimationGroupJob::uncontrolledAnimationFinished(QAbstrac
//      tAnimationJob *animation)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QContinuingAnimationGroupJob29uncontrolledAnimationFinishedEP21QAbstractAnimationJob(
    QContinuingAnimationGroupJob *self,
    QAbstractAnimationJob *animation) {
  self->uncontrolledAnimationFinished(animation);
}

//  void QContinuingAnimationGroupJob::debugAnimation(QDebug d) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK28QContinuingAnimationGroupJob14debugAnimationE6QDebug(
    const QContinuingAnimationGroupJob *self,
    const QDebug *d) {
  self->debugAnimation(*d);
}

//  a Python function taken by a CuteQContinuingAnimationGroupJob, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QContinuingAnimationGroupJob(
    QContinuingAnimationGroupJob *self,
    const char *key,
    void *call) {
  return static_cast<CuteQContinuingAnimationGroupJob *>(self)->take(key, call);
}

//  int QContinuingAnimationGroupJob::duration() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK28QContinuingAnimationGroupJob8durationEv(
    const QContinuingAnimationGroupJob *self) {
  return self->QContinuingAnimationGroupJob::duration();
}

//  void QContinuingAnimationGroupJob::updateCurrentTime(int currentTime)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN28QContinuingAnimationGroupJob17updateCurrentTimeEi(
    QContinuingAnimationGroupJob *self,
    int currentTime) {
  static_cast<OwnQContinuingAnimationGroupJob *>(self)->OwnQContinuingAnimationGroupJob::updateCurrentTime(
      currentTime);
}

//  void
//      QContinuingAnimationGroupJob::updateState(QAbstractAnimationJob::Stat
//      e newState, QAbstractAnimationJob::State oldState)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN28QContinuingAnimationGroupJob11updateStateEN21QAbstractAnimationJob5StateES1_(
    QContinuingAnimationGroupJob *self,
    QAbstractAnimationJob::State newState,
    QAbstractAnimationJob::State oldState) {
  static_cast<OwnQContinuingAnimationGroupJob *>(self)->OwnQContinuingAnimationGroupJob::updateState(
      newState,
      oldState);
}

//  void QContinuingAnimationGroupJob::updateDirection(QAbstractAnimationJob:
//      :Direction direction)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN28QContinuingAnimationGroupJob15updateDirectionEN21QAbstractAnimationJob9DirectionE(
    QContinuingAnimationGroupJob *self,
    QAbstractAnimationJob::Direction direction) {
  static_cast<OwnQContinuingAnimationGroupJob *>(self)->OwnQContinuingAnimationGroupJob::updateDirection(
      direction);
}

//  void QContinuingAnimationGroupJob::uncontrolledAnimationFinished(QAbstrac
//      tAnimationJob *animation)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN28QContinuingAnimationGroupJob29uncontrolledAnimationFinishedEP21QAbstractAnimationJob(
    QContinuingAnimationGroupJob *self,
    QAbstractAnimationJob *animation) {
  static_cast<OwnQContinuingAnimationGroupJob *>(self)->OwnQContinuingAnimationGroupJob::uncontrolledAnimationFinished(
      animation);
}

//  void QContinuingAnimationGroupJob::debugAnimation(QDebug d) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK28QContinuingAnimationGroupJob14debugAnimationE6QDebug(
    const QContinuingAnimationGroupJob *self,
    const QDebug *d) {
  static_cast<const OwnQContinuingAnimationGroupJob *>(self)->OwnQContinuingAnimationGroupJob::debugAnimation(
      *d);
}

#endif  // QT_CONFIG(qml_animation)
