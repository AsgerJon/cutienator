//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qsequentialanimationgroupjob_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQml/qtqmlglobal.h>
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#if QT_CONFIG(qml_animation)
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qsequentialanimationgroupjob_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qdebug.h>
#include <cstring>

//  Only a class built on QSequentialAnimationGroupJob may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQSequentialAnimationGroupJob : QSequentialAnimationGroupJob {
  using QSequentialAnimationGroupJob::updateCurrentTime;
  using QSequentialAnimationGroupJob::updateState;
  using QSequentialAnimationGroupJob::updateDirection;
  using QSequentialAnimationGroupJob::uncontrolledAnimationFinished;
  using QSequentialAnimationGroupJob::debugAnimation;
};

//  A QSequentialAnimationGroupJob that Python can take functions over in. Every QSequentialAnimationGroupJob
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(qml_animation)
typedef int (*CuteQSequentialAnimationGroupJobCall0)(const void *, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQSequentialAnimationGroupJobCall1)(const void *, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQSequentialAnimationGroupJobCall2)(const void *, int, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQSequentialAnimationGroupJobCall3)(const void *, int, int, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQSequentialAnimationGroupJobCall4)(const void *, int, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQSequentialAnimationGroupJobCall5)(const void *, QAbstractAnimationJob *, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQSequentialAnimationGroupJobCall6)(const void *, const QDebug *, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQSequentialAnimationGroupJobCall7)(const void *, QAbstractAnimationJob *, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQSequentialAnimationGroupJobCall8)(const void *, QAbstractAnimationJob *, QAbstractAnimationJob *, QAbstractAnimationJob *, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQSequentialAnimationGroupJobCall9)(const void *, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQSequentialAnimationGroupJobCall10)(const void *, int, int *);
#endif  // QT_CONFIG(qml_animation)
class CuteQSequentialAnimationGroupJob : public QSequentialAnimationGroupJob {
public:
  using QSequentialAnimationGroupJob::QSequentialAnimationGroupJob;
  void *taken[11] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(qml_animation)
    if (!std::strcmp(key, "_ZNK21QAbstractAnimationJob8durationEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
    if (!std::strcmp(key, "_ZN18QAnimationGroupJob5clearEv")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
    if (!std::strcmp(key, "_ZN21QAbstractAnimationJob17updateCurrentTimeEi")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
    if (!std::strcmp(key, "_ZN21QAbstractAnimationJob11updateStateENS_5StateES0_")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
    if (!std::strcmp(key, "_ZN21QAbstractAnimationJob15updateDirectionENS_9DirectionE")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
    if (!std::strcmp(key, "_ZN18QAnimationGroupJob29uncontrolledAnimationFinishedEP21QAbstractAnimationJob")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
    if (!std::strcmp(key, "_ZNK21QAbstractAnimationJob14debugAnimationE6QDebug")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
    if (!std::strcmp(key, "_ZN18QAnimationGroupJob17animationInsertedEP21QAbstractAnimationJob")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
    if (!std::strcmp(key, "_ZN18QAnimationGroupJob16animationRemovedEP21QAbstractAnimationJobS1_S1_")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
    if (!std::strcmp(key, "_ZN21QAbstractAnimationJob28topLevelAnimationLoopChangedEv")) {
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
  //  int QSequentialAnimationGroupJob::duration() const
  int duration() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSequentialAnimationGroupJobCall0 call = reinterpret_cast<CuteQSequentialAnimationGroupJobCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QSequentialAnimationGroupJob::duration();
  }
#endif  // QT_CONFIG(qml_animation)

#if QT_CONFIG(qml_animation)
  //  void QSequentialAnimationGroupJob::clear()
  void clear() override {
    if (taken[1]) {
      int handled = 0;
      CuteQSequentialAnimationGroupJobCall1 call = reinterpret_cast<CuteQSequentialAnimationGroupJobCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QSequentialAnimationGroupJob::clear();
  }
#endif  // QT_CONFIG(qml_animation)

#if QT_CONFIG(qml_animation)
  //  void QSequentialAnimationGroupJob::updateCurrentTime(int a0)
  void updateCurrentTime(int a0) override {
    if (taken[2]) {
      int handled = 0;
      CuteQSequentialAnimationGroupJobCall2 call = reinterpret_cast<CuteQSequentialAnimationGroupJobCall2>(taken[2]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QSequentialAnimationGroupJob::updateCurrentTime(a0);
  }
#endif  // QT_CONFIG(qml_animation)

#if QT_CONFIG(qml_animation)
  //  void QSequentialAnimationGroupJob::updateState(QAbstractAnimationJob:
  //      :State newState, QAbstractAnimationJob::State oldState)
  void updateState(
      QAbstractAnimationJob::State newState,
      QAbstractAnimationJob::State oldState) override {
    if (taken[3]) {
      int handled = 0;
      CuteQSequentialAnimationGroupJobCall3 call = reinterpret_cast<CuteQSequentialAnimationGroupJobCall3>(taken[3]);
      call(this, static_cast<int>(newState), static_cast<int>(oldState), &handled);
      if (handled) return;
    }
    QSequentialAnimationGroupJob::updateState(newState, oldState);
  }
#endif  // QT_CONFIG(qml_animation)

#if QT_CONFIG(qml_animation)
  //  void QSequentialAnimationGroupJob::updateDirection(QAbstractAnimation
  //      Job::Direction direction)
  void updateDirection(QAbstractAnimationJob::Direction direction) override {
    if (taken[4]) {
      int handled = 0;
      CuteQSequentialAnimationGroupJobCall4 call = reinterpret_cast<CuteQSequentialAnimationGroupJobCall4>(taken[4]);
      call(this, static_cast<int>(direction), &handled);
      if (handled) return;
    }
    QSequentialAnimationGroupJob::updateDirection(direction);
  }
#endif  // QT_CONFIG(qml_animation)

#if QT_CONFIG(qml_animation)
  //  void QSequentialAnimationGroupJob::uncontrolledAnimationFinished(QAbs
  //      tractAnimationJob *animation)
  void uncontrolledAnimationFinished(
      QAbstractAnimationJob *animation) override {
    if (taken[5]) {
      int handled = 0;
      CuteQSequentialAnimationGroupJobCall5 call = reinterpret_cast<CuteQSequentialAnimationGroupJobCall5>(taken[5]);
      call(this, animation, &handled);
      if (handled) return;
    }
    QSequentialAnimationGroupJob::uncontrolledAnimationFinished(animation);
  }
#endif  // QT_CONFIG(qml_animation)

#if QT_CONFIG(qml_animation)
  //  void QSequentialAnimationGroupJob::debugAnimation(QDebug d) const
  void debugAnimation(QDebug d) const override {
    if (taken[6]) {
      int handled = 0;
      CuteQSequentialAnimationGroupJobCall6 call = reinterpret_cast<CuteQSequentialAnimationGroupJobCall6>(taken[6]);
      call(this, &d, &handled);
      if (handled) return;
    }
    QSequentialAnimationGroupJob::debugAnimation(d);
  }
#endif  // QT_CONFIG(qml_animation)

#if QT_CONFIG(qml_animation)
  //  void
  //      QSequentialAnimationGroupJob::animationInserted(QAbstractAnimatio
  //      nJob *anim)
  void animationInserted(QAbstractAnimationJob *anim) override {
    if (taken[7]) {
      int handled = 0;
      CuteQSequentialAnimationGroupJobCall7 call = reinterpret_cast<CuteQSequentialAnimationGroupJobCall7>(taken[7]);
      call(this, anim, &handled);
      if (handled) return;
    }
    QSequentialAnimationGroupJob::animationInserted(anim);
  }
#endif  // QT_CONFIG(qml_animation)

#if QT_CONFIG(qml_animation)
  //  void
  //      QSequentialAnimationGroupJob::animationRemoved(QAbstractAnimation
  //      Job *anim, QAbstractAnimationJob *a1, QAbstractAnimationJob *a2)
  void animationRemoved(
      QAbstractAnimationJob *anim,
      QAbstractAnimationJob *a1,
      QAbstractAnimationJob *a2) override {
    if (taken[8]) {
      int handled = 0;
      CuteQSequentialAnimationGroupJobCall8 call = reinterpret_cast<CuteQSequentialAnimationGroupJobCall8>(taken[8]);
      call(this, anim, a1, a2, &handled);
      if (handled) return;
    }
    QSequentialAnimationGroupJob::animationRemoved(anim, a1, a2);
  }
#endif  // QT_CONFIG(qml_animation)

#if QT_CONFIG(qml_animation)
  //  void QAnimationGroupJob::topLevelAnimationLoopChanged()
  void topLevelAnimationLoopChanged() override {
    if (taken[9]) {
      int handled = 0;
      CuteQSequentialAnimationGroupJobCall9 call = reinterpret_cast<CuteQSequentialAnimationGroupJobCall9>(taken[9]);
      call(this, &handled);
      if (handled) return;
    }
    QAnimationGroupJob::topLevelAnimationLoopChanged();
  }
#endif  // QT_CONFIG(qml_animation)

#if QT_CONFIG(qml_animation)
  //  void QAbstractAnimationJob::updateLoopCount(int a0)
  void updateLoopCount(int a0) override {
    if (taken[10]) {
      int handled = 0;
      CuteQSequentialAnimationGroupJobCall10 call = reinterpret_cast<CuteQSequentialAnimationGroupJobCall10>(taken[10]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QAbstractAnimationJob::updateLoopCount(a0);
  }
#endif  // QT_CONFIG(qml_animation)
};

//  QSequentialAnimationGroupJob::QSequentialAnimationGroupJob()
extern "C" Q_DECL_EXPORT
QSequentialAnimationGroupJob *ritual_ZN28QSequentialAnimationGroupJobC1Ev() {
  return new CuteQSequentialAnimationGroupJob();
}

//  QSequentialAnimationGroupJob::~QSequentialAnimationGroupJob()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QSequentialAnimationGroupJobD1Ev(
    QSequentialAnimationGroupJob *self) {
  delete self;
}

//  int QSequentialAnimationGroupJob::duration() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK28QSequentialAnimationGroupJob8durationEv(
    const QSequentialAnimationGroupJob *self) {
  return self->duration();
}

//  QAbstractAnimationJob *QSequentialAnimationGroupJob::currentAnimation()
//      const
extern "C" Q_DECL_EXPORT
QAbstractAnimationJob *ritual_ZNK28QSequentialAnimationGroupJob16currentAnimationEv(
    const QSequentialAnimationGroupJob *self) {
  return self->currentAnimation();
}

//  void QSequentialAnimationGroupJob::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QSequentialAnimationGroupJob5clearEv(
    QSequentialAnimationGroupJob *self) {
  self->clear();
}

//  void QSequentialAnimationGroupJob::updateCurrentTime(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QSequentialAnimationGroupJob17updateCurrentTimeEi(
    QSequentialAnimationGroupJob *self,
    int a0) {
  self->updateCurrentTime(a0);
}

//  void
//      QSequentialAnimationGroupJob::updateState(QAbstractAnimationJob::Stat
//      e newState, QAbstractAnimationJob::State oldState)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QSequentialAnimationGroupJob11updateStateEN21QAbstractAnimationJob5StateES1_(
    QSequentialAnimationGroupJob *self,
    QAbstractAnimationJob::State newState,
    QAbstractAnimationJob::State oldState) {
  self->updateState(newState, oldState);
}

//  void QSequentialAnimationGroupJob::updateDirection(QAbstractAnimationJob:
//      :Direction direction)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QSequentialAnimationGroupJob15updateDirectionEN21QAbstractAnimationJob9DirectionE(
    QSequentialAnimationGroupJob *self,
    QAbstractAnimationJob::Direction direction) {
  self->updateDirection(direction);
}

//  void QSequentialAnimationGroupJob::uncontrolledAnimationFinished(QAbstrac
//      tAnimationJob *animation)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QSequentialAnimationGroupJob29uncontrolledAnimationFinishedEP21QAbstractAnimationJob(
    QSequentialAnimationGroupJob *self,
    QAbstractAnimationJob *animation) {
  self->uncontrolledAnimationFinished(animation);
}

//  void QSequentialAnimationGroupJob::debugAnimation(QDebug d) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK28QSequentialAnimationGroupJob14debugAnimationE6QDebug(
    const QSequentialAnimationGroupJob *self,
    const QDebug *d) {
  self->debugAnimation(*d);
}

//  int QSequentialAnimationGroupJob::animationActualTotalDuration(const
//      QAbstractAnimationJob *anim) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK28QSequentialAnimationGroupJob28animationActualTotalDurationEPK21QAbstractAnimationJob(
    const QSequentialAnimationGroupJob *self,
    const QAbstractAnimationJob *anim) {
  return self->animationActualTotalDuration(anim);
}

//  void QSequentialAnimationGroupJob::setCurrentAnimation(const
//      QAbstractAnimationJob *anim, bool intermediate)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QSequentialAnimationGroupJob19setCurrentAnimationEPK21QAbstractAnimationJobb(
    QSequentialAnimationGroupJob *self,
    const QAbstractAnimationJob *anim,
    bool intermediate) {
  self->setCurrentAnimation(anim, intermediate);
}

//  void QSequentialAnimationGroupJob::activateCurrentAnimation(bool
//      intermediate)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QSequentialAnimationGroupJob24activateCurrentAnimationEb(
    QSequentialAnimationGroupJob *self,
    bool intermediate) {
  self->activateCurrentAnimation(intermediate);
}

//  void
//      QSequentialAnimationGroupJob::animationInserted(QAbstractAnimationJob
//      *anim)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QSequentialAnimationGroupJob17animationInsertedEP21QAbstractAnimationJob(
    QSequentialAnimationGroupJob *self,
    QAbstractAnimationJob *anim) {
  self->animationInserted(anim);
}

//  void QSequentialAnimationGroupJob::animationRemoved(QAbstractAnimationJob
//      *anim, QAbstractAnimationJob *a1, QAbstractAnimationJob *a2)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QSequentialAnimationGroupJob16animationRemovedEP21QAbstractAnimationJobS1_S1_(
    QSequentialAnimationGroupJob *self,
    QAbstractAnimationJob *anim,
    QAbstractAnimationJob *a1,
    QAbstractAnimationJob *a2) {
  self->animationRemoved(anim, a1, a2);
}

//  bool QSequentialAnimationGroupJob::atEnd() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK28QSequentialAnimationGroupJob5atEndEv(
    const QSequentialAnimationGroupJob *self) {
  return self->atEnd();
}

//  void QSequentialAnimationGroupJob::restart()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QSequentialAnimationGroupJob7restartEv(
    QSequentialAnimationGroupJob *self) {
  self->restart();
}

//  a Python function taken by a CuteQSequentialAnimationGroupJob, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSequentialAnimationGroupJob(
    QSequentialAnimationGroupJob *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSequentialAnimationGroupJob *>(self)->take(key, call);
}

//  int QSequentialAnimationGroupJob::duration() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK28QSequentialAnimationGroupJob8durationEv(
    const QSequentialAnimationGroupJob *self) {
  return self->QSequentialAnimationGroupJob::duration();
}

//  void QSequentialAnimationGroupJob::clear()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN28QSequentialAnimationGroupJob5clearEv(
    QSequentialAnimationGroupJob *self) {
  self->QSequentialAnimationGroupJob::clear();
}

//  void QSequentialAnimationGroupJob::updateCurrentTime(int a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN28QSequentialAnimationGroupJob17updateCurrentTimeEi(
    QSequentialAnimationGroupJob *self,
    int a0) {
  static_cast<OwnQSequentialAnimationGroupJob *>(self)->OwnQSequentialAnimationGroupJob::updateCurrentTime(
      a0);
}

//  void
//      QSequentialAnimationGroupJob::updateState(QAbstractAnimationJob::Stat
//      e newState, QAbstractAnimationJob::State oldState)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN28QSequentialAnimationGroupJob11updateStateEN21QAbstractAnimationJob5StateES1_(
    QSequentialAnimationGroupJob *self,
    QAbstractAnimationJob::State newState,
    QAbstractAnimationJob::State oldState) {
  static_cast<OwnQSequentialAnimationGroupJob *>(self)->OwnQSequentialAnimationGroupJob::updateState(
      newState,
      oldState);
}

//  void QSequentialAnimationGroupJob::updateDirection(QAbstractAnimationJob:
//      :Direction direction)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN28QSequentialAnimationGroupJob15updateDirectionEN21QAbstractAnimationJob9DirectionE(
    QSequentialAnimationGroupJob *self,
    QAbstractAnimationJob::Direction direction) {
  static_cast<OwnQSequentialAnimationGroupJob *>(self)->OwnQSequentialAnimationGroupJob::updateDirection(
      direction);
}

//  void QSequentialAnimationGroupJob::uncontrolledAnimationFinished(QAbstrac
//      tAnimationJob *animation)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN28QSequentialAnimationGroupJob29uncontrolledAnimationFinishedEP21QAbstractAnimationJob(
    QSequentialAnimationGroupJob *self,
    QAbstractAnimationJob *animation) {
  static_cast<OwnQSequentialAnimationGroupJob *>(self)->OwnQSequentialAnimationGroupJob::uncontrolledAnimationFinished(
      animation);
}

//  void QSequentialAnimationGroupJob::debugAnimation(QDebug d) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK28QSequentialAnimationGroupJob14debugAnimationE6QDebug(
    const QSequentialAnimationGroupJob *self,
    const QDebug *d) {
  static_cast<const OwnQSequentialAnimationGroupJob *>(self)->OwnQSequentialAnimationGroupJob::debugAnimation(
      *d);
}

//  void
//      QSequentialAnimationGroupJob::animationInserted(QAbstractAnimationJob
//      *anim)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN28QSequentialAnimationGroupJob17animationInsertedEP21QAbstractAnimationJob(
    QSequentialAnimationGroupJob *self,
    QAbstractAnimationJob *anim) {
  self->QSequentialAnimationGroupJob::animationInserted(anim);
}

//  void QSequentialAnimationGroupJob::animationRemoved(QAbstractAnimationJob
//      *anim, QAbstractAnimationJob *a1, QAbstractAnimationJob *a2)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN28QSequentialAnimationGroupJob16animationRemovedEP21QAbstractAnimationJobS1_S1_(
    QSequentialAnimationGroupJob *self,
    QAbstractAnimationJob *anim,
    QAbstractAnimationJob *a1,
    QAbstractAnimationJob *a2) {
  self->QSequentialAnimationGroupJob::animationRemoved(anim, a1, a2);
}

#endif  // QT_CONFIG(qml_animation)
