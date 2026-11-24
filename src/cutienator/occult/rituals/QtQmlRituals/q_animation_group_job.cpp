//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qanimationgroupjob_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQml/qtqmlglobal.h>
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#if QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qanimationgroupjob_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qdebug.h>
#include <cstring>

//  Only a class built on QAnimationGroupJob may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQAnimationGroupJob : QAnimationGroupJob {
  using QAnimationGroupJob::topLevelAnimationLoopChanged;
  using QAnimationGroupJob::animationInserted;
  using QAnimationGroupJob::animationRemoved;
};

//  A QAnimationGroupJob that Python can take functions over in. Every QAnimationGroupJob
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(qml_animation)
typedef void (*CuteQAnimationGroupJobCall0)(const void *, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQAnimationGroupJobCall1)(const void *, QAbstractAnimationJob *, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQAnimationGroupJobCall2)(const void *, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQAnimationGroupJobCall3)(const void *, QAbstractAnimationJob *, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQAnimationGroupJobCall4)(const void *, QAbstractAnimationJob *, QAbstractAnimationJob *, QAbstractAnimationJob *, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef int (*CuteQAnimationGroupJobCall5)(const void *, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQAnimationGroupJobCall6)(const void *, int, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQAnimationGroupJobCall7)(const void *, int, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQAnimationGroupJobCall8)(const void *, int, int, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQAnimationGroupJobCall9)(const void *, int, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQAnimationGroupJobCall10)(const void *, const QDebug *, int *);
#endif  // QT_CONFIG(qml_animation)
class CuteQAnimationGroupJob : public QAnimationGroupJob {
public:
  using QAnimationGroupJob::QAnimationGroupJob;
  void *taken[11] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(qml_animation)
    if (!std::strcmp(key, "_ZN18QAnimationGroupJob5clearEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
    if (!std::strcmp(key, "_ZN18QAnimationGroupJob29uncontrolledAnimationFinishedEP21QAbstractAnimationJob")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
    if (!std::strcmp(key, "_ZN21QAbstractAnimationJob28topLevelAnimationLoopChangedEv")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
    if (!std::strcmp(key, "_ZN18QAnimationGroupJob17animationInsertedEP21QAbstractAnimationJob")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
    if (!std::strcmp(key, "_ZN18QAnimationGroupJob16animationRemovedEP21QAbstractAnimationJobS1_S1_")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
    if (!std::strcmp(key, "_ZNK21QAbstractAnimationJob8durationEv")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
    if (!std::strcmp(key, "_ZN21QAbstractAnimationJob17updateCurrentTimeEi")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
    if (!std::strcmp(key, "_ZN21QAbstractAnimationJob15updateLoopCountEi")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
    if (!std::strcmp(key, "_ZN21QAbstractAnimationJob11updateStateENS_5StateES0_")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
    if (!std::strcmp(key, "_ZN21QAbstractAnimationJob15updateDirectionENS_9DirectionE")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
    if (!std::strcmp(key, "_ZNK21QAbstractAnimationJob14debugAnimationE6QDebug")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_animation)
    return false;
  }

#if QT_CONFIG(qml_animation)
  //  void QAnimationGroupJob::clear()
  void clear() override {
    if (taken[0]) {
      int handled = 0;
      CuteQAnimationGroupJobCall0 call = reinterpret_cast<CuteQAnimationGroupJobCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QAnimationGroupJob::clear();
  }
#endif  // QT_CONFIG(qml_animation)

#if QT_CONFIG(qml_animation)
  //  void QAnimationGroupJob::uncontrolledAnimationFinished(QAbstractAnima
  //      tionJob *animation)
  void uncontrolledAnimationFinished(
      QAbstractAnimationJob *animation) override {
    if (taken[1]) {
      int handled = 0;
      CuteQAnimationGroupJobCall1 call = reinterpret_cast<CuteQAnimationGroupJobCall1>(taken[1]);
      call(this, animation, &handled);
      if (handled) return;
    }
    QAnimationGroupJob::uncontrolledAnimationFinished(animation);
  }
#endif  // QT_CONFIG(qml_animation)

#if QT_CONFIG(qml_animation)
  //  void QAnimationGroupJob::topLevelAnimationLoopChanged()
  void topLevelAnimationLoopChanged() override {
    if (taken[2]) {
      int handled = 0;
      CuteQAnimationGroupJobCall2 call = reinterpret_cast<CuteQAnimationGroupJobCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QAnimationGroupJob::topLevelAnimationLoopChanged();
  }
#endif  // QT_CONFIG(qml_animation)

#if QT_CONFIG(qml_animation)
  //  void QAnimationGroupJob::animationInserted(QAbstractAnimationJob *a0)
  void animationInserted(QAbstractAnimationJob *a0) override {
    if (taken[3]) {
      int handled = 0;
      CuteQAnimationGroupJobCall3 call = reinterpret_cast<CuteQAnimationGroupJobCall3>(taken[3]);
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
    if (taken[4]) {
      int handled = 0;
      CuteQAnimationGroupJobCall4 call = reinterpret_cast<CuteQAnimationGroupJobCall4>(taken[4]);
      call(this, a0, a1, a2, &handled);
      if (handled) return;
    }
    QAnimationGroupJob::animationRemoved(a0, a1, a2);
  }
#endif  // QT_CONFIG(qml_animation)

#if QT_CONFIG(qml_animation)
  //  int QAbstractAnimationJob::duration() const
  int duration() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQAnimationGroupJobCall5 call = reinterpret_cast<CuteQAnimationGroupJobCall5>(taken[5]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QAbstractAnimationJob::duration();
  }
#endif  // QT_CONFIG(qml_animation)

#if QT_CONFIG(qml_animation)
  //  void QAbstractAnimationJob::updateCurrentTime(int a0)
  void updateCurrentTime(int a0) override {
    if (taken[6]) {
      int handled = 0;
      CuteQAnimationGroupJobCall6 call = reinterpret_cast<CuteQAnimationGroupJobCall6>(taken[6]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QAbstractAnimationJob::updateCurrentTime(a0);
  }
#endif  // QT_CONFIG(qml_animation)

#if QT_CONFIG(qml_animation)
  //  void QAbstractAnimationJob::updateLoopCount(int a0)
  void updateLoopCount(int a0) override {
    if (taken[7]) {
      int handled = 0;
      CuteQAnimationGroupJobCall7 call = reinterpret_cast<CuteQAnimationGroupJobCall7>(taken[7]);
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
    if (taken[8]) {
      int handled = 0;
      CuteQAnimationGroupJobCall8 call = reinterpret_cast<CuteQAnimationGroupJobCall8>(taken[8]);
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
    if (taken[9]) {
      int handled = 0;
      CuteQAnimationGroupJobCall9 call = reinterpret_cast<CuteQAnimationGroupJobCall9>(taken[9]);
      call(this, static_cast<int>(direction), &handled);
      if (handled) return;
    }
    QAbstractAnimationJob::updateDirection(direction);
  }
#endif  // QT_CONFIG(qml_animation)

#if QT_CONFIG(qml_animation)
  //  void QAbstractAnimationJob::debugAnimation(QDebug d) const
  void debugAnimation(QDebug d) const override {
    if (taken[10]) {
      int handled = 0;
      CuteQAnimationGroupJobCall10 call = reinterpret_cast<CuteQAnimationGroupJobCall10>(taken[10]);
      call(this, &d, &handled);
      if (handled) return;
    }
    QAbstractAnimationJob::debugAnimation(d);
  }
#endif  // QT_CONFIG(qml_animation)
};

//  QAnimationGroupJob::QAnimationGroupJob()
extern "C" Q_DECL_EXPORT
QAnimationGroupJob *ritual_ZN18QAnimationGroupJobC1Ev() {
  return new CuteQAnimationGroupJob();
}

//  QAnimationGroupJob::~QAnimationGroupJob()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QAnimationGroupJobD1Ev(QAnimationGroupJob *self) {
  delete self;
}

//  void QAnimationGroupJob::appendAnimation(QAbstractAnimationJob
//      *animation)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QAnimationGroupJob15appendAnimationEP21QAbstractAnimationJob(
    QAnimationGroupJob *self,
    QAbstractAnimationJob *animation) {
  self->appendAnimation(animation);
}

//  void QAnimationGroupJob::prependAnimation(QAbstractAnimationJob
//      *animation)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QAnimationGroupJob16prependAnimationEP21QAbstractAnimationJob(
    QAnimationGroupJob *self,
    QAbstractAnimationJob *animation) {
  self->prependAnimation(animation);
}

//  void QAnimationGroupJob::removeAnimation(QAbstractAnimationJob
//      *animation)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QAnimationGroupJob15removeAnimationEP21QAbstractAnimationJob(
    QAnimationGroupJob *self,
    QAbstractAnimationJob *animation) {
  self->removeAnimation(animation);
}

//  void QAnimationGroupJob::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QAnimationGroupJob5clearEv(QAnimationGroupJob *self) {
  self->clear();
}

//  void
//      QAnimationGroupJob::uncontrolledAnimationFinished(QAbstractAnimationJ
//      ob *animation)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QAnimationGroupJob29uncontrolledAnimationFinishedEP21QAbstractAnimationJob(
    QAnimationGroupJob *self,
    QAbstractAnimationJob *animation) {
  self->uncontrolledAnimationFinished(animation);
}

//  void QAnimationGroupJob::topLevelAnimationLoopChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QAnimationGroupJob28topLevelAnimationLoopChangedEv(
    QAnimationGroupJob *self) {
  self->topLevelAnimationLoopChanged();
}

//  void QAnimationGroupJob::animationInserted(QAbstractAnimationJob *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QAnimationGroupJob17animationInsertedEP21QAbstractAnimationJob(
    QAnimationGroupJob *self,
    QAbstractAnimationJob *a0) {
  self->animationInserted(a0);
}

//  void QAnimationGroupJob::animationRemoved(QAbstractAnimationJob *a0,
//      QAbstractAnimationJob *a1, QAbstractAnimationJob *a2)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QAnimationGroupJob16animationRemovedEP21QAbstractAnimationJobS1_S1_(
    QAnimationGroupJob *self,
    QAbstractAnimationJob *a0,
    QAbstractAnimationJob *a1,
    QAbstractAnimationJob *a2) {
  self->animationRemoved(a0, a1, a2);
}

//  void QAnimationGroupJob::resetUncontrolledAnimationsFinishTime()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QAnimationGroupJob37resetUncontrolledAnimationsFinishTimeEv(
    QAnimationGroupJob *self) {
  self->resetUncontrolledAnimationsFinishTime();
}

//  void QAnimationGroupJob::resetUncontrolledAnimationFinishTime(QAbstractAn
//      imationJob *anim)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QAnimationGroupJob36resetUncontrolledAnimationFinishTimeEP21QAbstractAnimationJob(
    QAnimationGroupJob *self,
    QAbstractAnimationJob *anim) {
  self->resetUncontrolledAnimationFinishTime(anim);
}

//  int QAnimationGroupJob::uncontrolledAnimationFinishTime(const
//      QAbstractAnimationJob *anim) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QAnimationGroupJob31uncontrolledAnimationFinishTimeEPK21QAbstractAnimationJob(
    const QAnimationGroupJob *self,
    const QAbstractAnimationJob *anim) {
  return self->uncontrolledAnimationFinishTime(anim);
}

//  void QAnimationGroupJob::setUncontrolledAnimationFinishTime(QAbstractAnim
//      ationJob *anim, int time)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QAnimationGroupJob34setUncontrolledAnimationFinishTimeEP21QAbstractAnimationJobi(
    QAnimationGroupJob *self,
    QAbstractAnimationJob *anim,
    int time) {
  self->setUncontrolledAnimationFinishTime(anim, time);
}

//  void QAnimationGroupJob::debugChildren(QDebug d) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK18QAnimationGroupJob13debugChildrenE6QDebug(
    const QAnimationGroupJob *self,
    const QDebug *d) {
  self->debugChildren(*d);
}

//  void QAnimationGroupJob::ungroupChild(QAbstractAnimationJob *animation)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QAnimationGroupJob12ungroupChildEP21QAbstractAnimationJob(
    QAnimationGroupJob *self,
    QAbstractAnimationJob *animation) {
  self->ungroupChild(animation);
}

//  void QAnimationGroupJob::handleAnimationRemoved(QAbstractAnimationJob
//      *animation)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QAnimationGroupJob22handleAnimationRemovedEP21QAbstractAnimationJob(
    QAnimationGroupJob *self,
    QAbstractAnimationJob *animation) {
  self->handleAnimationRemoved(animation);
}

//  a Python function taken by a CuteQAnimationGroupJob, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAnimationGroupJob(
    QAnimationGroupJob *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAnimationGroupJob *>(self)->take(key, call);
}

//  void QAnimationGroupJob::clear()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QAnimationGroupJob5clearEv(QAnimationGroupJob *self) {
  self->QAnimationGroupJob::clear();
}

//  void
//      QAnimationGroupJob::uncontrolledAnimationFinished(QAbstractAnimationJ
//      ob *animation)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QAnimationGroupJob29uncontrolledAnimationFinishedEP21QAbstractAnimationJob(
    QAnimationGroupJob *self,
    QAbstractAnimationJob *animation) {
  self->QAnimationGroupJob::uncontrolledAnimationFinished(animation);
}

//  void QAnimationGroupJob::topLevelAnimationLoopChanged()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QAnimationGroupJob28topLevelAnimationLoopChangedEv(
    QAnimationGroupJob *self) {
  static_cast<OwnQAnimationGroupJob *>(self)->OwnQAnimationGroupJob::topLevelAnimationLoopChanged();
}

//  void QAnimationGroupJob::animationInserted(QAbstractAnimationJob *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QAnimationGroupJob17animationInsertedEP21QAbstractAnimationJob(
    QAnimationGroupJob *self,
    QAbstractAnimationJob *a0) {
  static_cast<OwnQAnimationGroupJob *>(self)->OwnQAnimationGroupJob::animationInserted(
      a0);
}

//  void QAnimationGroupJob::animationRemoved(QAbstractAnimationJob *a0,
//      QAbstractAnimationJob *a1, QAbstractAnimationJob *a2)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QAnimationGroupJob16animationRemovedEP21QAbstractAnimationJobS1_S1_(
    QAnimationGroupJob *self,
    QAbstractAnimationJob *a0,
    QAbstractAnimationJob *a1,
    QAbstractAnimationJob *a2) {
  static_cast<OwnQAnimationGroupJob *>(self)->OwnQAnimationGroupJob::animationRemoved(
      a0,
      a1,
      a2);
}

#endif  // QT_CONFIG(qml_animation)
#endif  // QT_CONFIG(qml_animation)
