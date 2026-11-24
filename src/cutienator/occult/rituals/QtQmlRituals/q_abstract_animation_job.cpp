//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qabstractanimationjob_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQml/qtqmlglobal.h>
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#if QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qabstractanimationjob_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qdebug.h>
#include <cstring>

//  Only a class built on QAbstractAnimationJob may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQAbstractAnimationJob : QAbstractAnimationJob {
  using QAbstractAnimationJob::updateCurrentTime;
  using QAbstractAnimationJob::updateLoopCount;
  using QAbstractAnimationJob::updateState;
  using QAbstractAnimationJob::updateDirection;
  using QAbstractAnimationJob::topLevelAnimationLoopChanged;
  using QAbstractAnimationJob::debugAnimation;
};

//  A QAbstractAnimationJob that Python can take functions over in. Every QAbstractAnimationJob
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(qml_animation)
typedef int (*CuteQAbstractAnimationJobCall0)(const void *, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQAbstractAnimationJobCall1)(const void *, int, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQAbstractAnimationJobCall2)(const void *, int, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQAbstractAnimationJobCall3)(const void *, int, int, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQAbstractAnimationJobCall4)(const void *, int, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQAbstractAnimationJobCall5)(const void *, int *);
#endif  // QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQAbstractAnimationJobCall6)(const void *, const QDebug *, int *);
#endif  // QT_CONFIG(qml_animation)
class CuteQAbstractAnimationJob : public QAbstractAnimationJob {
public:
  using QAbstractAnimationJob::QAbstractAnimationJob;
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
    if (!std::strcmp(key, "_ZN21QAbstractAnimationJob15updateLoopCountEi")) {
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
    if (!std::strcmp(key, "_ZN21QAbstractAnimationJob28topLevelAnimationLoopChangedEv")) {
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
    return false;
  }

#if QT_CONFIG(qml_animation)
  //  int QAbstractAnimationJob::duration() const
  int duration() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQAbstractAnimationJobCall0 call = reinterpret_cast<CuteQAbstractAnimationJobCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QAbstractAnimationJob::duration();
  }
#endif  // QT_CONFIG(qml_animation)

#if QT_CONFIG(qml_animation)
  //  void QAbstractAnimationJob::updateCurrentTime(int a0)
  void updateCurrentTime(int a0) override {
    if (taken[1]) {
      int handled = 0;
      CuteQAbstractAnimationJobCall1 call = reinterpret_cast<CuteQAbstractAnimationJobCall1>(taken[1]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QAbstractAnimationJob::updateCurrentTime(a0);
  }
#endif  // QT_CONFIG(qml_animation)

#if QT_CONFIG(qml_animation)
  //  void QAbstractAnimationJob::updateLoopCount(int a0)
  void updateLoopCount(int a0) override {
    if (taken[2]) {
      int handled = 0;
      CuteQAbstractAnimationJobCall2 call = reinterpret_cast<CuteQAbstractAnimationJobCall2>(taken[2]);
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
    if (taken[3]) {
      int handled = 0;
      CuteQAbstractAnimationJobCall3 call = reinterpret_cast<CuteQAbstractAnimationJobCall3>(taken[3]);
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
    if (taken[4]) {
      int handled = 0;
      CuteQAbstractAnimationJobCall4 call = reinterpret_cast<CuteQAbstractAnimationJobCall4>(taken[4]);
      call(this, static_cast<int>(direction), &handled);
      if (handled) return;
    }
    QAbstractAnimationJob::updateDirection(direction);
  }
#endif  // QT_CONFIG(qml_animation)

#if QT_CONFIG(qml_animation)
  //  void QAbstractAnimationJob::topLevelAnimationLoopChanged()
  void topLevelAnimationLoopChanged() override {
    if (taken[5]) {
      int handled = 0;
      CuteQAbstractAnimationJobCall5 call = reinterpret_cast<CuteQAbstractAnimationJobCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractAnimationJob::topLevelAnimationLoopChanged();
  }
#endif  // QT_CONFIG(qml_animation)

#if QT_CONFIG(qml_animation)
  //  void QAbstractAnimationJob::debugAnimation(QDebug d) const
  void debugAnimation(QDebug d) const override {
    if (taken[6]) {
      int handled = 0;
      CuteQAbstractAnimationJobCall6 call = reinterpret_cast<CuteQAbstractAnimationJobCall6>(taken[6]);
      call(this, &d, &handled);
      if (handled) return;
    }
    QAbstractAnimationJob::debugAnimation(d);
  }
#endif  // QT_CONFIG(qml_animation)
};

//  QAbstractAnimationJob::QAbstractAnimationJob()
extern "C" Q_DECL_EXPORT
QAbstractAnimationJob *ritual_ZN21QAbstractAnimationJobC1Ev() {
  return new CuteQAbstractAnimationJob();
}

//  QAbstractAnimationJob::~QAbstractAnimationJob()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QAbstractAnimationJobD1Ev(QAbstractAnimationJob *self) {
  delete self;
}

//  QAnimationGroupJob *QAbstractAnimationJob::group() const
extern "C" Q_DECL_EXPORT
QAnimationGroupJob *ritual_ZNK21QAbstractAnimationJob5groupEv(
    const QAbstractAnimationJob *self) {
  return self->group();
}

//  int QAbstractAnimationJob::loopCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QAbstractAnimationJob9loopCountEv(
    const QAbstractAnimationJob *self) {
  return self->loopCount();
}

//  void QAbstractAnimationJob::setLoopCount(int loopCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QAbstractAnimationJob12setLoopCountEi(
    QAbstractAnimationJob *self,
    int loopCount) {
  self->setLoopCount(loopCount);
}

//  int QAbstractAnimationJob::totalDuration() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QAbstractAnimationJob13totalDurationEv(
    const QAbstractAnimationJob *self) {
  return self->totalDuration();
}

//  int QAbstractAnimationJob::duration() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QAbstractAnimationJob8durationEv(
    const QAbstractAnimationJob *self) {
  return self->duration();
}

//  QAbstractAnimationJob::Direction QAbstractAnimationJob::direction() const
extern "C" Q_DECL_EXPORT
QAbstractAnimationJob::Direction ritual_ZNK21QAbstractAnimationJob9directionEv(
    const QAbstractAnimationJob *self) {
  return self->direction();
}

//  void QAbstractAnimationJob::setDirection(QAbstractAnimationJob::Direction
//      direction)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QAbstractAnimationJob12setDirectionENS_9DirectionE(
    QAbstractAnimationJob *self,
    QAbstractAnimationJob::Direction direction) {
  self->setDirection(direction);
}

//  int QAbstractAnimationJob::currentTime() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QAbstractAnimationJob11currentTimeEv(
    const QAbstractAnimationJob *self) {
  return self->currentTime();
}

//  int QAbstractAnimationJob::currentLoopTime() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QAbstractAnimationJob15currentLoopTimeEv(
    const QAbstractAnimationJob *self) {
  return self->currentLoopTime();
}

//  int QAbstractAnimationJob::currentLoop() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QAbstractAnimationJob11currentLoopEv(
    const QAbstractAnimationJob *self) {
  return self->currentLoop();
}

//  QAbstractAnimationJob::State QAbstractAnimationJob::state() const
extern "C" Q_DECL_EXPORT
QAbstractAnimationJob::State ritual_ZNK21QAbstractAnimationJob5stateEv(
    const QAbstractAnimationJob *self) {
  return self->state();
}

//  bool QAbstractAnimationJob::isRunning()
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QAbstractAnimationJob9isRunningEv(
    QAbstractAnimationJob *self) {
  return self->isRunning();
}

//  bool QAbstractAnimationJob::isStopped()
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QAbstractAnimationJob9isStoppedEv(
    QAbstractAnimationJob *self) {
  return self->isStopped();
}

//  bool QAbstractAnimationJob::isPaused()
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QAbstractAnimationJob8isPausedEv(
    QAbstractAnimationJob *self) {
  return self->isPaused();
}

//  void QAbstractAnimationJob::setDisableUserControl()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QAbstractAnimationJob21setDisableUserControlEv(
    QAbstractAnimationJob *self) {
  self->setDisableUserControl();
}

//  void QAbstractAnimationJob::setEnableUserControl()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QAbstractAnimationJob20setEnableUserControlEv(
    QAbstractAnimationJob *self) {
  self->setEnableUserControl();
}

//  bool QAbstractAnimationJob::userControlDisabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QAbstractAnimationJob19userControlDisabledEv(
    const QAbstractAnimationJob *self) {
  return self->userControlDisabled();
}

//  void QAbstractAnimationJob::setCurrentTime(int msecs)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QAbstractAnimationJob14setCurrentTimeEi(
    QAbstractAnimationJob *self,
    int msecs) {
  self->setCurrentTime(msecs);
}

//  void QAbstractAnimationJob::start()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QAbstractAnimationJob5startEv(QAbstractAnimationJob *self) {
  self->start();
}

//  void QAbstractAnimationJob::pause()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QAbstractAnimationJob5pauseEv(QAbstractAnimationJob *self) {
  self->pause();
}

//  void QAbstractAnimationJob::resume()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QAbstractAnimationJob6resumeEv(QAbstractAnimationJob *self) {
  self->resume();
}

//  void QAbstractAnimationJob::stop()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QAbstractAnimationJob4stopEv(QAbstractAnimationJob *self) {
  self->stop();
}

//  void QAbstractAnimationJob::complete()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QAbstractAnimationJob8completeEv(
    QAbstractAnimationJob *self) {
  self->complete();
}

//  void QAbstractAnimationJob::addAnimationChangeListener(QAnimationJobChang
//      eListener *listener, QAbstractAnimationJob::ChangeTypes a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QAbstractAnimationJob26addAnimationChangeListenerEP27QAnimationJobChangeListener6QFlagsINS_10ChangeTypeEE(
    QAbstractAnimationJob *self,
    QAnimationJobChangeListener *listener,
    int a1) {
  self->addAnimationChangeListener(
      listener,
      QFlags<QAbstractAnimationJob::ChangeType>::fromInt(a1));
}

//  void QAbstractAnimationJob::removeAnimationChangeListener(QAnimationJobCh
//      angeListener *listener, QAbstractAnimationJob::ChangeTypes a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QAbstractAnimationJob29removeAnimationChangeListenerEP27QAnimationJobChangeListener6QFlagsINS_10ChangeTypeEE(
    QAbstractAnimationJob *self,
    QAnimationJobChangeListener *listener,
    int a1) {
  self->removeAnimationChangeListener(
      listener,
      QFlags<QAbstractAnimationJob::ChangeType>::fromInt(a1));
}

//  bool QAbstractAnimationJob::isGroup() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QAbstractAnimationJob7isGroupEv(
    const QAbstractAnimationJob *self) {
  return self->isGroup();
}

//  bool QAbstractAnimationJob::isRenderThreadJob() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QAbstractAnimationJob17isRenderThreadJobEv(
    const QAbstractAnimationJob *self) {
  return self->isRenderThreadJob();
}

//  bool QAbstractAnimationJob::isRenderThreadProxy() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QAbstractAnimationJob19isRenderThreadProxyEv(
    const QAbstractAnimationJob *self) {
  return self->isRenderThreadProxy();
}

//  void QAbstractAnimationJob::updateCurrentTime(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QAbstractAnimationJob17updateCurrentTimeEi(
    QAbstractAnimationJob *self,
    int a0) {
  self->updateCurrentTime(a0);
}

//  void QAbstractAnimationJob::updateLoopCount(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QAbstractAnimationJob15updateLoopCountEi(
    QAbstractAnimationJob *self,
    int a0) {
  self->updateLoopCount(a0);
}

//  void QAbstractAnimationJob::updateState(QAbstractAnimationJob::State
//      newState, QAbstractAnimationJob::State oldState)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QAbstractAnimationJob11updateStateENS_5StateES0_(
    QAbstractAnimationJob *self,
    QAbstractAnimationJob::State newState,
    QAbstractAnimationJob::State oldState) {
  self->updateState(newState, oldState);
}

//  void
//      QAbstractAnimationJob::updateDirection(QAbstractAnimationJob::Directi
//      on direction)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QAbstractAnimationJob15updateDirectionENS_9DirectionE(
    QAbstractAnimationJob *self,
    QAbstractAnimationJob::Direction direction) {
  self->updateDirection(direction);
}

//  void QAbstractAnimationJob::topLevelAnimationLoopChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QAbstractAnimationJob28topLevelAnimationLoopChangedEv(
    QAbstractAnimationJob *self) {
  self->topLevelAnimationLoopChanged();
}

//  void QAbstractAnimationJob::debugAnimation(QDebug d) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK21QAbstractAnimationJob14debugAnimationE6QDebug(
    const QAbstractAnimationJob *self,
    const QDebug *d) {
  self->debugAnimation(*d);
}

//  void QAbstractAnimationJob::fireTopLevelAnimationLoopChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QAbstractAnimationJob32fireTopLevelAnimationLoopChangedEv(
    QAbstractAnimationJob *self) {
  self->fireTopLevelAnimationLoopChanged();
}

//  void QAbstractAnimationJob::setState(QAbstractAnimationJob::State state)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QAbstractAnimationJob8setStateENS_5StateE(
    QAbstractAnimationJob *self,
    QAbstractAnimationJob::State state) {
  self->setState(state);
}

//  void QAbstractAnimationJob::finished()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QAbstractAnimationJob8finishedEv(
    QAbstractAnimationJob *self) {
  self->finished();
}

//  void QAbstractAnimationJob::stateChanged(QAbstractAnimationJob::State
//      newState, QAbstractAnimationJob::State oldState)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QAbstractAnimationJob12stateChangedENS_5StateES0_(
    QAbstractAnimationJob *self,
    QAbstractAnimationJob::State newState,
    QAbstractAnimationJob::State oldState) {
  self->stateChanged(newState, oldState);
}

//  void QAbstractAnimationJob::currentLoopChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QAbstractAnimationJob18currentLoopChangedEv(
    QAbstractAnimationJob *self) {
  self->currentLoopChanged();
}

//  void QAbstractAnimationJob::currentTimeChanged(int currentTime)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QAbstractAnimationJob18currentTimeChangedEi(
    QAbstractAnimationJob *self,
    int currentTime) {
  self->currentTimeChanged(currentTime);
}

//  QDebug operator<<(QDebug a0, const QAbstractAnimationJob *job)
extern "C" Q_DECL_EXPORT
QDebug *ritual_Zls6QDebugPK21QAbstractAnimationJob(
    const QDebug *a0,
    const QAbstractAnimationJob *job) {
  return new QDebug(operator<<(*a0, job));
}

//  a Python function taken by a CuteQAbstractAnimationJob, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAbstractAnimationJob(
    QAbstractAnimationJob *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAbstractAnimationJob *>(self)->take(key, call);
}

//  int QAbstractAnimationJob::duration() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK21QAbstractAnimationJob8durationEv(
    const QAbstractAnimationJob *self) {
  return self->QAbstractAnimationJob::duration();
}

//  void QAbstractAnimationJob::updateCurrentTime(int a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QAbstractAnimationJob17updateCurrentTimeEi(
    QAbstractAnimationJob *self,
    int a0) {
  static_cast<OwnQAbstractAnimationJob *>(self)->OwnQAbstractAnimationJob::updateCurrentTime(
      a0);
}

//  void QAbstractAnimationJob::updateLoopCount(int a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QAbstractAnimationJob15updateLoopCountEi(
    QAbstractAnimationJob *self,
    int a0) {
  static_cast<OwnQAbstractAnimationJob *>(self)->OwnQAbstractAnimationJob::updateLoopCount(
      a0);
}

//  void QAbstractAnimationJob::updateState(QAbstractAnimationJob::State
//      newState, QAbstractAnimationJob::State oldState)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QAbstractAnimationJob11updateStateENS_5StateES0_(
    QAbstractAnimationJob *self,
    QAbstractAnimationJob::State newState,
    QAbstractAnimationJob::State oldState) {
  static_cast<OwnQAbstractAnimationJob *>(self)->OwnQAbstractAnimationJob::updateState(
      newState,
      oldState);
}

//  void
//      QAbstractAnimationJob::updateDirection(QAbstractAnimationJob::Directi
//      on direction)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QAbstractAnimationJob15updateDirectionENS_9DirectionE(
    QAbstractAnimationJob *self,
    QAbstractAnimationJob::Direction direction) {
  static_cast<OwnQAbstractAnimationJob *>(self)->OwnQAbstractAnimationJob::updateDirection(
      direction);
}

//  void QAbstractAnimationJob::topLevelAnimationLoopChanged()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QAbstractAnimationJob28topLevelAnimationLoopChangedEv(
    QAbstractAnimationJob *self) {
  static_cast<OwnQAbstractAnimationJob *>(self)->OwnQAbstractAnimationJob::topLevelAnimationLoopChanged();
}

//  void QAbstractAnimationJob::debugAnimation(QDebug d) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK21QAbstractAnimationJob14debugAnimationE6QDebug(
    const QAbstractAnimationJob *self,
    const QDebug *d) {
  static_cast<const OwnQAbstractAnimationJob *>(self)->OwnQAbstractAnimationJob::debugAnimation(
      *d);
}

#endif  // QT_CONFIG(qml_animation)
#endif  // QT_CONFIG(qml_animation)
