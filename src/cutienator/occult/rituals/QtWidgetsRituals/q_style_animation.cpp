//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qstyleanimation_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtWidgets/QtWidgets>
#include <QtWidgets/6.12.0/QtWidgets/private/qstyleanimation_p.h>
#include <QtCore/qstring.h>
#include <QtCore/qdatetime.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QStyleAnimation may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQStyleAnimation : QStyleAnimation {
  using QStyleAnimation::isUpdateNeeded;
  using QStyleAnimation::updateCurrentTime;
};

//  A QStyleAnimation that Python can take functions over in. Every QStyleAnimation
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQStyleAnimationCall0)(const void *, int *);
typedef bool (*CuteQStyleAnimationCall1)(const void *, int *);
typedef void (*CuteQStyleAnimationCall2)(const void *, int, int *);
typedef bool (*CuteQStyleAnimationCall3)(const void *, QEvent *, int *);
typedef void (*CuteQStyleAnimationCall4)(const void *, int, int, int *);
typedef void (*CuteQStyleAnimationCall5)(const void *, int, int *);
typedef bool (*CuteQStyleAnimationCall6)(const void *, QObject *, QEvent *, int *);
typedef void (*CuteQStyleAnimationCall7)(const void *, QTimerEvent *, int *);
typedef void (*CuteQStyleAnimationCall8)(const void *, QChildEvent *, int *);
typedef void (*CuteQStyleAnimationCall9)(const void *, QEvent *, int *);
typedef void (*CuteQStyleAnimationCall10)(const void *, const QMetaMethod *, int *);
typedef void (*CuteQStyleAnimationCall11)(const void *, const QMetaMethod *, int *);
class CuteQStyleAnimation : public QStyleAnimation {
public:
  using QStyleAnimation::QStyleAnimation;
  void *taken[12] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK18QAbstractAnimation8durationEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QStyleAnimation14isUpdateNeededEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QAbstractAnimation17updateCurrentTimeEi")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QAbstractAnimation11updateStateENS_5StateES0_")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QAbstractAnimation15updateDirectionENS_9DirectionE")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[11] = call;
      return true;
    }
    return false;
  }

  //  int QStyleAnimation::duration() const
  int duration() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQStyleAnimationCall0 call = reinterpret_cast<CuteQStyleAnimationCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QStyleAnimation::duration();
  }

  //  bool QStyleAnimation::isUpdateNeeded() const
  bool isUpdateNeeded() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQStyleAnimationCall1 call = reinterpret_cast<CuteQStyleAnimationCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QStyleAnimation::isUpdateNeeded();
  }

  //  void QStyleAnimation::updateCurrentTime(int time)
  void updateCurrentTime(int time) override {
    if (taken[2]) {
      int handled = 0;
      CuteQStyleAnimationCall2 call = reinterpret_cast<CuteQStyleAnimationCall2>(taken[2]);
      call(this, time, &handled);
      if (handled) return;
    }
    QStyleAnimation::updateCurrentTime(time);
  }

  //  bool QAbstractAnimation::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQStyleAnimationCall3 call = reinterpret_cast<CuteQStyleAnimationCall3>(taken[3]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QAbstractAnimation::event(event);
  }

  //  void QAbstractAnimation::updateState(QAbstractAnimation::State
  //      newState, QAbstractAnimation::State oldState)
  void updateState(
      QAbstractAnimation::State newState,
      QAbstractAnimation::State oldState) override {
    if (taken[4]) {
      int handled = 0;
      CuteQStyleAnimationCall4 call = reinterpret_cast<CuteQStyleAnimationCall4>(taken[4]);
      call(this, static_cast<int>(newState), static_cast<int>(oldState), &handled);
      if (handled) return;
    }
    QAbstractAnimation::updateState(newState, oldState);
  }

  //  void
  //      QAbstractAnimation::updateDirection(QAbstractAnimation::Direction
  //      direction)
  void updateDirection(QAbstractAnimation::Direction direction) override {
    if (taken[5]) {
      int handled = 0;
      CuteQStyleAnimationCall5 call = reinterpret_cast<CuteQStyleAnimationCall5>(taken[5]);
      call(this, static_cast<int>(direction), &handled);
      if (handled) return;
    }
    QAbstractAnimation::updateDirection(direction);
  }

  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQStyleAnimationCall6 call = reinterpret_cast<CuteQStyleAnimationCall6>(taken[6]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }

  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQStyleAnimationCall7 call = reinterpret_cast<CuteQStyleAnimationCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }

  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQStyleAnimationCall8 call = reinterpret_cast<CuteQStyleAnimationCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }

  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQStyleAnimationCall9 call = reinterpret_cast<CuteQStyleAnimationCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }

  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[10]) {
      int handled = 0;
      CuteQStyleAnimationCall10 call = reinterpret_cast<CuteQStyleAnimationCall10>(taken[10]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }

  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[11]) {
      int handled = 0;
      CuteQStyleAnimationCall11 call = reinterpret_cast<CuteQStyleAnimationCall11>(taken[11]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
};

//  const QMetaObject *QStyleAnimation::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QStyleAnimation10metaObjectEv(
    const QStyleAnimation *self) {
  return self->metaObject();
}

//  QString QStyleAnimation::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QStyleAnimation2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QStyleAnimation::tr(s, c, n));
}

//  QStyleAnimation::QStyleAnimation(QObject *target)
extern "C" Q_DECL_EXPORT
QStyleAnimation *ritual_ZN15QStyleAnimationC1EP7QObject(QObject *target) {
  return new CuteQStyleAnimation(target);
}

//  QStyleAnimation::~QStyleAnimation()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QStyleAnimationD1Ev(QStyleAnimation *self) {
  delete self;
}

//  QObject *QStyleAnimation::target() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK15QStyleAnimation6targetEv(const QStyleAnimation *self) {
  return self->target();
}

//  int QStyleAnimation::duration() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QStyleAnimation8durationEv(const QStyleAnimation *self) {
  return self->duration();
}

//  void QStyleAnimation::setDuration(int duration)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QStyleAnimation11setDurationEi(
    QStyleAnimation *self,
    int duration) {
  self->setDuration(duration);
}

//  int QStyleAnimation::delay() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QStyleAnimation5delayEv(const QStyleAnimation *self) {
  return self->delay();
}

//  void QStyleAnimation::setDelay(int delay)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QStyleAnimation8setDelayEi(
    QStyleAnimation *self,
    int delay) {
  self->setDelay(delay);
}

//  QTime QStyleAnimation::startTime() const
extern "C" Q_DECL_EXPORT
QTime *ritual_ZNK15QStyleAnimation9startTimeEv(const QStyleAnimation *self) {
  return new QTime(self->startTime());
}

//  void QStyleAnimation::setStartTime(QTime time)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QStyleAnimation12setStartTimeE5QTime(
    QStyleAnimation *self,
    const QTime *time) {
  self->setStartTime(*time);
}

//  FrameRate QStyleAnimation::frameRate() const
extern "C" Q_DECL_EXPORT
QStyleAnimation::FrameRate ritual_ZNK15QStyleAnimation9frameRateEv(
    const QStyleAnimation *self) {
  return self->frameRate();
}

//  void QStyleAnimation::setFrameRate(FrameRate fps)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QStyleAnimation12setFrameRateENS_9FrameRateE(
    QStyleAnimation *self,
    QStyleAnimation::FrameRate fps) {
  self->setFrameRate(fps);
}

//  void QStyleAnimation::updateTarget()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QStyleAnimation12updateTargetEv(QStyleAnimation *self) {
  self->updateTarget();
}

//  void QStyleAnimation::start()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QStyleAnimation5startEv(QStyleAnimation *self) {
  self->start();
}

//  bool QStyleAnimation::isUpdateNeeded() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QStyleAnimation14isUpdateNeededEv(
    const QStyleAnimation *self) {
  return self->isUpdateNeeded();
}

//  void QStyleAnimation::updateCurrentTime(int time)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QStyleAnimation17updateCurrentTimeEi(
    QStyleAnimation *self,
    int time) {
  self->updateCurrentTime(time);
}

//  a Python function taken by a CuteQStyleAnimation, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QStyleAnimation(
    QStyleAnimation *self,
    const char *key,
    void *call) {
  return static_cast<CuteQStyleAnimation *>(self)->take(key, call);
}

//  int QStyleAnimation::duration() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK15QStyleAnimation8durationEv(const QStyleAnimation *self) {
  return self->QStyleAnimation::duration();
}

//  bool QStyleAnimation::isUpdateNeeded() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK15QStyleAnimation14isUpdateNeededEv(
    const QStyleAnimation *self) {
  return static_cast<const OwnQStyleAnimation *>(self)->OwnQStyleAnimation::isUpdateNeeded();
}

//  void QStyleAnimation::updateCurrentTime(int time)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QStyleAnimation17updateCurrentTimeEi(
    QStyleAnimation *self,
    int time) {
  static_cast<OwnQStyleAnimation *>(self)->OwnQStyleAnimation::updateCurrentTime(
      time);
}
