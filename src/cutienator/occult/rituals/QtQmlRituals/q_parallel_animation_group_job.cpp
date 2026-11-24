//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qparallelanimationgroupjob_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQml/qtqmlglobal.h>
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#if QT_CONFIG(qml_animation)
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qparallelanimationgroupjob_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qdebug.h>
#include <cstring>

//  Only a class built on QParallelAnimationGroupJob may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQParallelAnimationGroupJob : QParallelAnimationGroupJob {
  using QParallelAnimationGroupJob::updateCurrentTime;
  using QParallelAnimationGroupJob::updateState;
  using QParallelAnimationGroupJob::updateDirection;
  using QParallelAnimationGroupJob::uncontrolledAnimationFinished;
  using QParallelAnimationGroupJob::debugAnimation;
};

//  A QParallelAnimationGroupJob that Python can take functions over in. Every QParallelAnimationGroupJob
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(qml_animation)
typedef int (*CuteQParallelAnimationGroupJobCall0)(const void *, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQParallelAnimationGroupJobCall1)(const void *, int, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQParallelAnimationGroupJobCall2)(const void *, int, int, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQParallelAnimationGroupJobCall3)(const void *, int, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQParallelAnimationGroupJobCall4)(const void *, QAbstractAnimationJob *, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQParallelAnimationGroupJobCall5)(const void *, const QDebug *, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQParallelAnimationGroupJobCall6)(const void *, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQParallelAnimationGroupJobCall7)(const void *, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQParallelAnimationGroupJobCall8)(const void *, QAbstractAnimationJob *, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQParallelAnimationGroupJobCall9)(const void *, QAbstractAnimationJob *, QAbstractAnimationJob *, QAbstractAnimationJob *, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQParallelAnimationGroupJobCall10)(const void *, int, int *);
#endif  // QT_CONFIG(qml_animation)
class CuteQParallelAnimationGroupJob : public QParallelAnimationGroupJob {
public:
  using QParallelAnimationGroupJob::QParallelAnimationGroupJob;
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
  //  int QParallelAnimationGroupJob::duration() const
  int duration() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQParallelAnimationGroupJobCall0 call = reinterpret_cast<CuteQParallelAnimationGroupJobCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QParallelAnimationGroupJob::duration();
  }
#endif  // QT_CONFIG(qml_animation)

#if QT_CONFIG(qml_animation)
  //  void QParallelAnimationGroupJob::updateCurrentTime(int currentTime)
  void updateCurrentTime(int currentTime) override {
    if (taken[1]) {
      int handled = 0;
      CuteQParallelAnimationGroupJobCall1 call = reinterpret_cast<CuteQParallelAnimationGroupJobCall1>(taken[1]);
      call(this, currentTime, &handled);
      if (handled) return;
    }
    QParallelAnimationGroupJob::updateCurrentTime(currentTime);
  }
#endif  // QT_CONFIG(qml_animation)

#if QT_CONFIG(qml_animation)
  //  void
  //      QParallelAnimationGroupJob::updateState(QAbstractAnimationJob::St
  //      ate newState, QAbstractAnimationJob::State oldState)
  void updateState(
      QAbstractAnimationJob::State newState,
      QAbstractAnimationJob::State oldState) override {
    if (taken[2]) {
      int handled = 0;
      CuteQParallelAnimationGroupJobCall2 call = reinterpret_cast<CuteQParallelAnimationGroupJobCall2>(taken[2]);
      call(this, static_cast<int>(newState), static_cast<int>(oldState), &handled);
      if (handled) return;
    }
    QParallelAnimationGroupJob::updateState(newState, oldState);
  }
#endif  // QT_CONFIG(qml_animation)

#if QT_CONFIG(qml_animation)
  //  void QParallelAnimationGroupJob::updateDirection(QAbstractAnimationJo
  //      b::Direction direction)
  void updateDirection(QAbstractAnimationJob::Direction direction) override {
    if (taken[3]) {
      int handled = 0;
      CuteQParallelAnimationGroupJobCall3 call = reinterpret_cast<CuteQParallelAnimationGroupJobCall3>(taken[3]);
      call(this, static_cast<int>(direction), &handled);
      if (handled) return;
    }
    QParallelAnimationGroupJob::updateDirection(direction);
  }
#endif  // QT_CONFIG(qml_animation)

#if QT_CONFIG(qml_animation)
  //  void QParallelAnimationGroupJob::uncontrolledAnimationFinished(QAbstr
  //      actAnimationJob *animation)
  void uncontrolledAnimationFinished(
      QAbstractAnimationJob *animation) override {
    if (taken[4]) {
      int handled = 0;
      CuteQParallelAnimationGroupJobCall4 call = reinterpret_cast<CuteQParallelAnimationGroupJobCall4>(taken[4]);
      call(this, animation, &handled);
      if (handled) return;
    }
    QParallelAnimationGroupJob::uncontrolledAnimationFinished(animation);
  }
#endif  // QT_CONFIG(qml_animation)

#if QT_CONFIG(qml_animation)
  //  void QParallelAnimationGroupJob::debugAnimation(QDebug d) const
  void debugAnimation(QDebug d) const override {
    if (taken[5]) {
      int handled = 0;
      CuteQParallelAnimationGroupJobCall5 call = reinterpret_cast<CuteQParallelAnimationGroupJobCall5>(taken[5]);
      call(this, &d, &handled);
      if (handled) return;
    }
    QParallelAnimationGroupJob::debugAnimation(d);
  }
#endif  // QT_CONFIG(qml_animation)

#if QT_CONFIG(qml_animation)
  //  void QAnimationGroupJob::clear()
  void clear() override {
    if (taken[6]) {
      int handled = 0;
      CuteQParallelAnimationGroupJobCall6 call = reinterpret_cast<CuteQParallelAnimationGroupJobCall6>(taken[6]);
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
      CuteQParallelAnimationGroupJobCall7 call = reinterpret_cast<CuteQParallelAnimationGroupJobCall7>(taken[7]);
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
      CuteQParallelAnimationGroupJobCall8 call = reinterpret_cast<CuteQParallelAnimationGroupJobCall8>(taken[8]);
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
      CuteQParallelAnimationGroupJobCall9 call = reinterpret_cast<CuteQParallelAnimationGroupJobCall9>(taken[9]);
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
      CuteQParallelAnimationGroupJobCall10 call = reinterpret_cast<CuteQParallelAnimationGroupJobCall10>(taken[10]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QAbstractAnimationJob::updateLoopCount(a0);
  }
#endif  // QT_CONFIG(qml_animation)
};

//  QParallelAnimationGroupJob::QParallelAnimationGroupJob()
extern "C" Q_DECL_EXPORT
QParallelAnimationGroupJob *ritual_ZN26QParallelAnimationGroupJobC1Ev() {
  return new CuteQParallelAnimationGroupJob();
}

//  QParallelAnimationGroupJob::~QParallelAnimationGroupJob()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QParallelAnimationGroupJobD1Ev(
    QParallelAnimationGroupJob *self) {
  delete self;
}

//  int QParallelAnimationGroupJob::duration() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK26QParallelAnimationGroupJob8durationEv(
    const QParallelAnimationGroupJob *self) {
  return self->duration();
}

//  void QParallelAnimationGroupJob::updateCurrentTime(int currentTime)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QParallelAnimationGroupJob17updateCurrentTimeEi(
    QParallelAnimationGroupJob *self,
    int currentTime) {
  self->updateCurrentTime(currentTime);
}

//  void QParallelAnimationGroupJob::updateState(QAbstractAnimationJob::State
//      newState, QAbstractAnimationJob::State oldState)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QParallelAnimationGroupJob11updateStateEN21QAbstractAnimationJob5StateES1_(
    QParallelAnimationGroupJob *self,
    QAbstractAnimationJob::State newState,
    QAbstractAnimationJob::State oldState) {
  self->updateState(newState, oldState);
}

//  void QParallelAnimationGroupJob::updateDirection(QAbstractAnimationJob::D
//      irection direction)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QParallelAnimationGroupJob15updateDirectionEN21QAbstractAnimationJob9DirectionE(
    QParallelAnimationGroupJob *self,
    QAbstractAnimationJob::Direction direction) {
  self->updateDirection(direction);
}

//  void QParallelAnimationGroupJob::uncontrolledAnimationFinished(QAbstractA
//      nimationJob *animation)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QParallelAnimationGroupJob29uncontrolledAnimationFinishedEP21QAbstractAnimationJob(
    QParallelAnimationGroupJob *self,
    QAbstractAnimationJob *animation) {
  self->uncontrolledAnimationFinished(animation);
}

//  void QParallelAnimationGroupJob::debugAnimation(QDebug d) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK26QParallelAnimationGroupJob14debugAnimationE6QDebug(
    const QParallelAnimationGroupJob *self,
    const QDebug *d) {
  self->debugAnimation(*d);
}

//  bool
//      QParallelAnimationGroupJob::shouldAnimationStart(QAbstractAnimationJo
//      b *animation, bool startIfAtEnd) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK26QParallelAnimationGroupJob20shouldAnimationStartEP21QAbstractAnimationJobb(
    const QParallelAnimationGroupJob *self,
    QAbstractAnimationJob *animation,
    bool startIfAtEnd) {
  return self->shouldAnimationStart(animation, startIfAtEnd);
}

//  void QParallelAnimationGroupJob::applyGroupState(QAbstractAnimationJob
//      *animation)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QParallelAnimationGroupJob15applyGroupStateEP21QAbstractAnimationJob(
    QParallelAnimationGroupJob *self,
    QAbstractAnimationJob *animation) {
  self->applyGroupState(animation);
}

//  a Python function taken by a CuteQParallelAnimationGroupJob, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QParallelAnimationGroupJob(
    QParallelAnimationGroupJob *self,
    const char *key,
    void *call) {
  return static_cast<CuteQParallelAnimationGroupJob *>(self)->take(key, call);
}

//  int QParallelAnimationGroupJob::duration() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK26QParallelAnimationGroupJob8durationEv(
    const QParallelAnimationGroupJob *self) {
  return self->QParallelAnimationGroupJob::duration();
}

//  void QParallelAnimationGroupJob::updateCurrentTime(int currentTime)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN26QParallelAnimationGroupJob17updateCurrentTimeEi(
    QParallelAnimationGroupJob *self,
    int currentTime) {
  static_cast<OwnQParallelAnimationGroupJob *>(self)->OwnQParallelAnimationGroupJob::updateCurrentTime(
      currentTime);
}

//  void QParallelAnimationGroupJob::updateState(QAbstractAnimationJob::State
//      newState, QAbstractAnimationJob::State oldState)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN26QParallelAnimationGroupJob11updateStateEN21QAbstractAnimationJob5StateES1_(
    QParallelAnimationGroupJob *self,
    QAbstractAnimationJob::State newState,
    QAbstractAnimationJob::State oldState) {
  static_cast<OwnQParallelAnimationGroupJob *>(self)->OwnQParallelAnimationGroupJob::updateState(
      newState,
      oldState);
}

//  void QParallelAnimationGroupJob::updateDirection(QAbstractAnimationJob::D
//      irection direction)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN26QParallelAnimationGroupJob15updateDirectionEN21QAbstractAnimationJob9DirectionE(
    QParallelAnimationGroupJob *self,
    QAbstractAnimationJob::Direction direction) {
  static_cast<OwnQParallelAnimationGroupJob *>(self)->OwnQParallelAnimationGroupJob::updateDirection(
      direction);
}

//  void QParallelAnimationGroupJob::uncontrolledAnimationFinished(QAbstractA
//      nimationJob *animation)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN26QParallelAnimationGroupJob29uncontrolledAnimationFinishedEP21QAbstractAnimationJob(
    QParallelAnimationGroupJob *self,
    QAbstractAnimationJob *animation) {
  static_cast<OwnQParallelAnimationGroupJob *>(self)->OwnQParallelAnimationGroupJob::uncontrolledAnimationFinished(
      animation);
}

//  void QParallelAnimationGroupJob::debugAnimation(QDebug d) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK26QParallelAnimationGroupJob14debugAnimationE6QDebug(
    const QParallelAnimationGroupJob *self,
    const QDebug *d) {
  static_cast<const OwnQParallelAnimationGroupJob *>(self)->OwnQParallelAnimationGroupJob::debugAnimation(
      *d);
}

#endif  // QT_CONFIG(qml_animation)
