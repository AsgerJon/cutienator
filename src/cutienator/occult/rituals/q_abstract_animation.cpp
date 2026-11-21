//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qabstractanimation.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qabstractanimation.h>
#include <QtCore/qstring.h>

//  const QMetaObject *QAbstractAnimation::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QAbstractAnimation10metaObjectEv(
    const QAbstractAnimation *self) {
  return self->metaObject();
}

//  QString QAbstractAnimation::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QAbstractAnimation2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QAbstractAnimation::tr(s, c, n));
}

//  QAbstractAnimation::~QAbstractAnimation()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QAbstractAnimationD1Ev(QAbstractAnimation *self) {
  delete self;
}

//  State QAbstractAnimation::state() const
extern "C" Q_DECL_EXPORT
QAbstractAnimation::State ritual_ZNK18QAbstractAnimation5stateEv(
    const QAbstractAnimation *self) {
  return self->state();
}

//  QAnimationGroup *QAbstractAnimation::group() const
extern "C" Q_DECL_EXPORT
QAnimationGroup *ritual_ZNK18QAbstractAnimation5groupEv(
    const QAbstractAnimation *self) {
  return self->group();
}

//  Direction QAbstractAnimation::direction() const
extern "C" Q_DECL_EXPORT
QAbstractAnimation::Direction ritual_ZNK18QAbstractAnimation9directionEv(
    const QAbstractAnimation *self) {
  return self->direction();
}

//  void QAbstractAnimation::setDirection(Direction direction)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QAbstractAnimation12setDirectionENS_9DirectionE(
    QAbstractAnimation *self,
    QAbstractAnimation::Direction direction) {
  self->setDirection(direction);
}

//  int QAbstractAnimation::currentTime() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QAbstractAnimation11currentTimeEv(
    const QAbstractAnimation *self) {
  return self->currentTime();
}

//  int QAbstractAnimation::currentLoopTime() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QAbstractAnimation15currentLoopTimeEv(
    const QAbstractAnimation *self) {
  return self->currentLoopTime();
}

//  int QAbstractAnimation::loopCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QAbstractAnimation9loopCountEv(
    const QAbstractAnimation *self) {
  return self->loopCount();
}

//  void QAbstractAnimation::setLoopCount(int loopCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QAbstractAnimation12setLoopCountEi(
    QAbstractAnimation *self,
    int loopCount) {
  self->setLoopCount(loopCount);
}

//  int QAbstractAnimation::currentLoop() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QAbstractAnimation11currentLoopEv(
    const QAbstractAnimation *self) {
  return self->currentLoop();
}

//  int QAbstractAnimation::duration() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QAbstractAnimation8durationEv(
    const QAbstractAnimation *self) {
  return self->duration();
}

//  int QAbstractAnimation::totalDuration() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QAbstractAnimation13totalDurationEv(
    const QAbstractAnimation *self) {
  return self->totalDuration();
}

//  void QAbstractAnimation::start(QAbstractAnimation::DeletionPolicy policy)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QAbstractAnimation5startENS_14DeletionPolicyE(
    QAbstractAnimation *self,
    QAbstractAnimation::DeletionPolicy policy) {
  self->start(policy);
}

//  void QAbstractAnimation::pause()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QAbstractAnimation5pauseEv(QAbstractAnimation *self) {
  self->pause();
}

//  void QAbstractAnimation::resume()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QAbstractAnimation6resumeEv(QAbstractAnimation *self) {
  self->resume();
}

//  void QAbstractAnimation::setPaused(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QAbstractAnimation9setPausedEb(
    QAbstractAnimation *self,
    bool a0) {
  self->setPaused(a0);
}

//  void QAbstractAnimation::stop()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QAbstractAnimation4stopEv(QAbstractAnimation *self) {
  self->stop();
}

//  void QAbstractAnimation::setCurrentTime(int msecs)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QAbstractAnimation14setCurrentTimeEi(
    QAbstractAnimation *self,
    int msecs) {
  self->setCurrentTime(msecs);
}
