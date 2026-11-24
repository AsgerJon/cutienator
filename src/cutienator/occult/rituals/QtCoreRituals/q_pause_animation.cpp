//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qpauseanimation.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#if QT_CONFIG(animation)
#if QT_CONFIG(animation)
#include <QtCore/qpauseanimation.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QPauseAnimation may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQPauseAnimation : QPauseAnimation {
  using QPauseAnimation::event;
  using QPauseAnimation::updateCurrentTime;
};

//  A QPauseAnimation that Python can take functions over in. Every QPauseAnimation
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(animation)
typedef int (*CuteQPauseAnimationCall0)(const void *, int *);
#endif  // QT_CONFIG(animation)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(animation)
typedef bool (*CuteQPauseAnimationCall1)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(animation)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(animation)
typedef void (*CuteQPauseAnimationCall2)(const void *, int, int *);
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
typedef void (*CuteQPauseAnimationCall3)(const void *, int, int, int *);
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
typedef void (*CuteQPauseAnimationCall4)(const void *, int, int *);
#endif  // QT_CONFIG(animation)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPauseAnimationCall5)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPauseAnimationCall6)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPauseAnimationCall7)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPauseAnimationCall8)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPauseAnimationCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPauseAnimationCall10)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQPauseAnimation : public QPauseAnimation {
public:
  using QPauseAnimation::QPauseAnimation;
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
  //  int QPauseAnimation::duration() const
  int duration() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQPauseAnimationCall0 call = reinterpret_cast<CuteQPauseAnimationCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QPauseAnimation::duration();
  }
#endif  // QT_CONFIG(animation)

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(animation)
  //  bool QPauseAnimation::event(QEvent *e)
  bool event(QEvent *e) override {
    if (taken[1]) {
      int handled = 0;
      CuteQPauseAnimationCall1 call = reinterpret_cast<CuteQPauseAnimationCall1>(taken[1]);
      bool given = call(this, e, &handled);
      if (handled) return given;
    }
    return QPauseAnimation::event(e);
  }
#endif  // QT_CONFIG(animation)
#endif  // !defined(QT_NO_QOBJECT)

#if QT_CONFIG(animation)
  //  void QPauseAnimation::updateCurrentTime(int a0)
  void updateCurrentTime(int a0) override {
    if (taken[2]) {
      int handled = 0;
      CuteQPauseAnimationCall2 call = reinterpret_cast<CuteQPauseAnimationCall2>(taken[2]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QPauseAnimation::updateCurrentTime(a0);
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
      CuteQPauseAnimationCall3 call = reinterpret_cast<CuteQPauseAnimationCall3>(taken[3]);
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
      CuteQPauseAnimationCall4 call = reinterpret_cast<CuteQPauseAnimationCall4>(taken[4]);
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
      CuteQPauseAnimationCall5 call = reinterpret_cast<CuteQPauseAnimationCall5>(taken[5]);
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
      CuteQPauseAnimationCall6 call = reinterpret_cast<CuteQPauseAnimationCall6>(taken[6]);
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
      CuteQPauseAnimationCall7 call = reinterpret_cast<CuteQPauseAnimationCall7>(taken[7]);
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
      CuteQPauseAnimationCall8 call = reinterpret_cast<CuteQPauseAnimationCall8>(taken[8]);
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
      CuteQPauseAnimationCall9 call = reinterpret_cast<CuteQPauseAnimationCall9>(taken[9]);
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
      CuteQPauseAnimationCall10 call = reinterpret_cast<CuteQPauseAnimationCall10>(taken[10]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QPauseAnimation::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QPauseAnimation10metaObjectEv(
    const QPauseAnimation *self) {
  return self->metaObject();
}

//  QString QPauseAnimation::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QPauseAnimation2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QPauseAnimation::tr(s, c, n));
}

//  QPauseAnimation::QPauseAnimation(QObject *parent)
extern "C" Q_DECL_EXPORT
QPauseAnimation *ritual_ZN15QPauseAnimationC1EP7QObject(QObject *parent) {
  return new CuteQPauseAnimation(parent);
}

//  QPauseAnimation::QPauseAnimation(int msecs, QObject *parent)
extern "C" Q_DECL_EXPORT
QPauseAnimation *ritual_ZN15QPauseAnimationC1EiP7QObject(
    int msecs,
    QObject *parent) {
  return new CuteQPauseAnimation(msecs, parent);
}

//  QPauseAnimation::~QPauseAnimation()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QPauseAnimationD1Ev(QPauseAnimation *self) {
  delete self;
}

//  int QPauseAnimation::duration() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QPauseAnimation8durationEv(const QPauseAnimation *self) {
  return self->duration();
}

//  void QPauseAnimation::setDuration(int msecs)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QPauseAnimation11setDurationEi(
    QPauseAnimation *self,
    int msecs) {
  self->setDuration(msecs);
}

//  bool QPauseAnimation::event(QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QPauseAnimation5eventEP6QEvent(
    QPauseAnimation *self,
    QEvent *e) {
  return self->event(e);
}

//  void QPauseAnimation::updateCurrentTime(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QPauseAnimation17updateCurrentTimeEi(
    QPauseAnimation *self,
    int a0) {
  self->updateCurrentTime(a0);
}

//  a Python function taken by a CuteQPauseAnimation, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPauseAnimation(
    QPauseAnimation *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPauseAnimation *>(self)->take(key, call);
}

//  int QPauseAnimation::duration() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK15QPauseAnimation8durationEv(const QPauseAnimation *self) {
  return self->QPauseAnimation::duration();
}

//  bool QPauseAnimation::event(QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN15QPauseAnimation5eventEP6QEvent(
    QPauseAnimation *self,
    QEvent *e) {
  return static_cast<OwnQPauseAnimation *>(self)->OwnQPauseAnimation::event(
      e);
}

//  void QPauseAnimation::updateCurrentTime(int a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QPauseAnimation17updateCurrentTimeEi(
    QPauseAnimation *self,
    int a0) {
  static_cast<OwnQPauseAnimation *>(self)->OwnQPauseAnimation::updateCurrentTime(
      a0);
}

#endif  // QT_CONFIG(animation)
#endif  // QT_CONFIG(animation)
