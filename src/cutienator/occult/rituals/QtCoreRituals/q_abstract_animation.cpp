//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qabstractanimation.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#if QT_CONFIG(animation)
#include <QtCore/qabstractanimation.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QAbstractAnimation may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQAbstractAnimation : QAbstractAnimation {
  using QAbstractAnimation::event;
  using QAbstractAnimation::updateState;
  using QAbstractAnimation::updateDirection;
};

//  A QAbstractAnimation that Python can take functions over in. Every QAbstractAnimation
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(animation)
typedef int (*CuteQAbstractAnimationCall0)(const void *, int *);
#endif  // QT_CONFIG(animation)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(animation)
typedef bool (*CuteQAbstractAnimationCall1)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(animation)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(animation)
typedef void (*CuteQAbstractAnimationCall2)(const void *, int, int *);
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
typedef void (*CuteQAbstractAnimationCall3)(const void *, int, int, int *);
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
typedef void (*CuteQAbstractAnimationCall4)(const void *, int, int *);
#endif  // QT_CONFIG(animation)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAbstractAnimationCall5)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractAnimationCall6)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractAnimationCall7)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractAnimationCall8)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractAnimationCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractAnimationCall10)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQAbstractAnimation : public QAbstractAnimation {
public:
  using QAbstractAnimation::QAbstractAnimation;
  void *taken[11] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(animation)
    if (!std::strcmp(key, "_ZNK18QAbstractAnimation8durationEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(animation)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(animation)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(animation)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(animation)
    if (!std::strcmp(key, "_ZN18QAbstractAnimation17updateCurrentTimeEi")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
    if (!std::strcmp(key, "_ZN18QAbstractAnimation11updateStateENS_5StateES0_")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
    if (!std::strcmp(key, "_ZN18QAbstractAnimation15updateDirectionENS_9DirectionE")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(animation)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if QT_CONFIG(animation)
  //  int QAbstractAnimation::duration() const
  int duration() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQAbstractAnimationCall0 call = reinterpret_cast<CuteQAbstractAnimationCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }
#endif  // QT_CONFIG(animation)

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(animation)
  //  bool QAbstractAnimation::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQAbstractAnimationCall1 call = reinterpret_cast<CuteQAbstractAnimationCall1>(taken[1]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QAbstractAnimation::event(event);
  }
#endif  // QT_CONFIG(animation)
#endif  // !defined(QT_NO_QOBJECT)

#if QT_CONFIG(animation)
  //  void QAbstractAnimation::updateCurrentTime(int currentTime)
  void updateCurrentTime(int currentTime) override {
    if (taken[2]) {
      int handled = 0;
      CuteQAbstractAnimationCall2 call = reinterpret_cast<CuteQAbstractAnimationCall2>(taken[2]);
      call(this, currentTime, &handled);
      if (handled) return;
    }
  }
#endif  // QT_CONFIG(animation)

#if QT_CONFIG(animation)
  //  void QAbstractAnimation::updateState(QAbstractAnimation::State
  //      newState, QAbstractAnimation::State oldState)
  void updateState(
      QAbstractAnimation::State newState,
      QAbstractAnimation::State oldState) override {
    if (taken[3]) {
      int handled = 0;
      CuteQAbstractAnimationCall3 call = reinterpret_cast<CuteQAbstractAnimationCall3>(taken[3]);
      call(this, static_cast<int>(newState), static_cast<int>(oldState), &handled);
      if (handled) return;
    }
    QAbstractAnimation::updateState(newState, oldState);
  }
#endif  // QT_CONFIG(animation)

#if QT_CONFIG(animation)
  //  void
  //      QAbstractAnimation::updateDirection(QAbstractAnimation::Direction
  //      direction)
  void updateDirection(QAbstractAnimation::Direction direction) override {
    if (taken[4]) {
      int handled = 0;
      CuteQAbstractAnimationCall4 call = reinterpret_cast<CuteQAbstractAnimationCall4>(taken[4]);
      call(this, static_cast<int>(direction), &handled);
      if (handled) return;
    }
    QAbstractAnimation::updateDirection(direction);
  }
#endif  // QT_CONFIG(animation)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQAbstractAnimationCall5 call = reinterpret_cast<CuteQAbstractAnimationCall5>(taken[5]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQAbstractAnimationCall6 call = reinterpret_cast<CuteQAbstractAnimationCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQAbstractAnimationCall7 call = reinterpret_cast<CuteQAbstractAnimationCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQAbstractAnimationCall8 call = reinterpret_cast<CuteQAbstractAnimationCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[9]) {
      int handled = 0;
      CuteQAbstractAnimationCall9 call = reinterpret_cast<CuteQAbstractAnimationCall9>(taken[9]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[10]) {
      int handled = 0;
      CuteQAbstractAnimationCall10 call = reinterpret_cast<CuteQAbstractAnimationCall10>(taken[10]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

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

//  bool QAbstractAnimation::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QAbstractAnimation5eventEP6QEvent(
    QAbstractAnimation *self,
    QEvent *event) {
  return self->event(event);
}

//  void QAbstractAnimation::updateCurrentTime(int currentTime)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QAbstractAnimation17updateCurrentTimeEi(
    QAbstractAnimation *self,
    int currentTime) {
  self->updateCurrentTime(currentTime);
}

//  void QAbstractAnimation::updateState(QAbstractAnimation::State newState,
//      QAbstractAnimation::State oldState)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QAbstractAnimation11updateStateENS_5StateES0_(
    QAbstractAnimation *self,
    QAbstractAnimation::State newState,
    QAbstractAnimation::State oldState) {
  self->updateState(newState, oldState);
}

//  void QAbstractAnimation::updateDirection(QAbstractAnimation::Direction
//      direction)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QAbstractAnimation15updateDirectionENS_9DirectionE(
    QAbstractAnimation *self,
    QAbstractAnimation::Direction direction) {
  self->updateDirection(direction);
}

//  QAbstractAnimationPrivate *QAbstractAnimation::d_func()
extern "C" Q_DECL_EXPORT
QAbstractAnimationPrivate *ritual_ZN18QAbstractAnimation6d_funcEv(
    QAbstractAnimation *self) {
  return self->d_func();
}

//  const QAbstractAnimationPrivate *QAbstractAnimation::d_func() const
extern "C" Q_DECL_EXPORT
const QAbstractAnimationPrivate *ritual_ZNK18QAbstractAnimation6d_funcEv(
    const QAbstractAnimation *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQAbstractAnimation, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAbstractAnimation(
    QAbstractAnimation *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAbstractAnimation *>(self)->take(key, call);
}

//  bool QAbstractAnimation::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN18QAbstractAnimation5eventEP6QEvent(
    QAbstractAnimation *self,
    QEvent *event) {
  return static_cast<OwnQAbstractAnimation *>(self)->OwnQAbstractAnimation::event(
      event);
}

//  void QAbstractAnimation::updateState(QAbstractAnimation::State newState,
//      QAbstractAnimation::State oldState)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QAbstractAnimation11updateStateENS_5StateES0_(
    QAbstractAnimation *self,
    QAbstractAnimation::State newState,
    QAbstractAnimation::State oldState) {
  static_cast<OwnQAbstractAnimation *>(self)->OwnQAbstractAnimation::updateState(
      newState,
      oldState);
}

//  void QAbstractAnimation::updateDirection(QAbstractAnimation::Direction
//      direction)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QAbstractAnimation15updateDirectionENS_9DirectionE(
    QAbstractAnimation *self,
    QAbstractAnimation::Direction direction) {
  static_cast<OwnQAbstractAnimation *>(self)->OwnQAbstractAnimation::updateDirection(
      direction);
}

#endif  // QT_CONFIG(animation)
