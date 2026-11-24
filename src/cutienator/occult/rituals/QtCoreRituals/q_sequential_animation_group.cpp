//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qsequentialanimationgroup.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtCore/qglobal.h>
#if QT_CONFIG(animation)
#if QT_CONFIG(animation)
#include <QtCore/qsequentialanimationgroup.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QSequentialAnimationGroup may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQSequentialAnimationGroup : QSequentialAnimationGroup {
  using QSequentialAnimationGroup::event;
  using QSequentialAnimationGroup::updateCurrentTime;
  using QSequentialAnimationGroup::updateState;
  using QSequentialAnimationGroup::updateDirection;
};

//  A QSequentialAnimationGroup that Python can take functions over in. Every QSequentialAnimationGroup
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(animation)
typedef int (*CuteQSequentialAnimationGroupCall0)(const void *, int *);
#endif  // QT_CONFIG(animation)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(animation)
typedef bool (*CuteQSequentialAnimationGroupCall1)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(animation)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(animation)
typedef void (*CuteQSequentialAnimationGroupCall2)(const void *, int, int *);
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
typedef void (*CuteQSequentialAnimationGroupCall3)(const void *, int, int, int *);
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
typedef void (*CuteQSequentialAnimationGroupCall4)(const void *, int, int *);
#endif  // QT_CONFIG(animation)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSequentialAnimationGroupCall5)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSequentialAnimationGroupCall6)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSequentialAnimationGroupCall7)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSequentialAnimationGroupCall8)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSequentialAnimationGroupCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSequentialAnimationGroupCall10)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQSequentialAnimationGroup : public QSequentialAnimationGroup {
public:
  using QSequentialAnimationGroup::QSequentialAnimationGroup;
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
  //  int QSequentialAnimationGroup::duration() const
  int duration() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSequentialAnimationGroupCall0 call = reinterpret_cast<CuteQSequentialAnimationGroupCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QSequentialAnimationGroup::duration();
  }
#endif  // QT_CONFIG(animation)

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(animation)
  //  bool QSequentialAnimationGroup::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQSequentialAnimationGroupCall1 call = reinterpret_cast<CuteQSequentialAnimationGroupCall1>(taken[1]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QSequentialAnimationGroup::event(event);
  }
#endif  // QT_CONFIG(animation)
#endif  // !defined(QT_NO_QOBJECT)

#if QT_CONFIG(animation)
  //  void QSequentialAnimationGroup::updateCurrentTime(int a0)
  void updateCurrentTime(int a0) override {
    if (taken[2]) {
      int handled = 0;
      CuteQSequentialAnimationGroupCall2 call = reinterpret_cast<CuteQSequentialAnimationGroupCall2>(taken[2]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QSequentialAnimationGroup::updateCurrentTime(a0);
  }
#endif  // QT_CONFIG(animation)

#if QT_CONFIG(animation)
  //  void QSequentialAnimationGroup::updateState(QAbstractAnimation::State
  //      newState, QAbstractAnimation::State oldState)
  void updateState(
      QAbstractAnimation::State newState,
      QAbstractAnimation::State oldState) override {
    if (taken[3]) {
      int handled = 0;
      CuteQSequentialAnimationGroupCall3 call = reinterpret_cast<CuteQSequentialAnimationGroupCall3>(taken[3]);
      call(this, static_cast<int>(newState), static_cast<int>(oldState), &handled);
      if (handled) return;
    }
    QSequentialAnimationGroup::updateState(newState, oldState);
  }
#endif  // QT_CONFIG(animation)

#if QT_CONFIG(animation)
  //  void QSequentialAnimationGroup::updateDirection(QAbstractAnimation::D
  //      irection direction)
  void updateDirection(QAbstractAnimation::Direction direction) override {
    if (taken[4]) {
      int handled = 0;
      CuteQSequentialAnimationGroupCall4 call = reinterpret_cast<CuteQSequentialAnimationGroupCall4>(taken[4]);
      call(this, static_cast<int>(direction), &handled);
      if (handled) return;
    }
    QSequentialAnimationGroup::updateDirection(direction);
  }
#endif  // QT_CONFIG(animation)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQSequentialAnimationGroupCall5 call = reinterpret_cast<CuteQSequentialAnimationGroupCall5>(taken[5]);
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
      CuteQSequentialAnimationGroupCall6 call = reinterpret_cast<CuteQSequentialAnimationGroupCall6>(taken[6]);
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
      CuteQSequentialAnimationGroupCall7 call = reinterpret_cast<CuteQSequentialAnimationGroupCall7>(taken[7]);
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
      CuteQSequentialAnimationGroupCall8 call = reinterpret_cast<CuteQSequentialAnimationGroupCall8>(taken[8]);
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
      CuteQSequentialAnimationGroupCall9 call = reinterpret_cast<CuteQSequentialAnimationGroupCall9>(taken[9]);
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
      CuteQSequentialAnimationGroupCall10 call = reinterpret_cast<CuteQSequentialAnimationGroupCall10>(taken[10]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QSequentialAnimationGroup::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK25QSequentialAnimationGroup10metaObjectEv(
    const QSequentialAnimationGroup *self) {
  return self->metaObject();
}

//  QString QSequentialAnimationGroup::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN25QSequentialAnimationGroup2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QSequentialAnimationGroup::tr(s, c, n));
}

//  QSequentialAnimationGroup::QSequentialAnimationGroup(QObject *parent)
extern "C" Q_DECL_EXPORT
QSequentialAnimationGroup *ritual_ZN25QSequentialAnimationGroupC1EP7QObject(
    QObject *parent) {
  return new CuteQSequentialAnimationGroup(parent);
}

//  QSequentialAnimationGroup::~QSequentialAnimationGroup()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QSequentialAnimationGroupD1Ev(
    QSequentialAnimationGroup *self) {
  delete self;
}

//  QPauseAnimation *QSequentialAnimationGroup::addPause(int msecs)
extern "C" Q_DECL_EXPORT
QPauseAnimation *ritual_ZN25QSequentialAnimationGroup8addPauseEi(
    QSequentialAnimationGroup *self,
    int msecs) {
  return self->addPause(msecs);
}

//  QPauseAnimation *QSequentialAnimationGroup::insertPause(int index, int
//      msecs)
extern "C" Q_DECL_EXPORT
QPauseAnimation *ritual_ZN25QSequentialAnimationGroup11insertPauseEii(
    QSequentialAnimationGroup *self,
    int index,
    int msecs) {
  return self->insertPause(index, msecs);
}

//  QAbstractAnimation *QSequentialAnimationGroup::currentAnimation() const
extern "C" Q_DECL_EXPORT
QAbstractAnimation *ritual_ZNK25QSequentialAnimationGroup16currentAnimationEv(
    const QSequentialAnimationGroup *self) {
  return self->currentAnimation();
}

//  int QSequentialAnimationGroup::duration() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK25QSequentialAnimationGroup8durationEv(
    const QSequentialAnimationGroup *self) {
  return self->duration();
}

//  bool QSequentialAnimationGroup::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN25QSequentialAnimationGroup5eventEP6QEvent(
    QSequentialAnimationGroup *self,
    QEvent *event) {
  return self->event(event);
}

//  void QSequentialAnimationGroup::updateCurrentTime(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QSequentialAnimationGroup17updateCurrentTimeEi(
    QSequentialAnimationGroup *self,
    int a0) {
  self->updateCurrentTime(a0);
}

//  void QSequentialAnimationGroup::updateState(QAbstractAnimation::State
//      newState, QAbstractAnimation::State oldState)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QSequentialAnimationGroup11updateStateEN18QAbstractAnimation5StateES1_(
    QSequentialAnimationGroup *self,
    QAbstractAnimation::State newState,
    QAbstractAnimation::State oldState) {
  self->updateState(newState, oldState);
}

//  void
//      QSequentialAnimationGroup::updateDirection(QAbstractAnimation::Direct
//      ion direction)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QSequentialAnimationGroup15updateDirectionEN18QAbstractAnimation9DirectionE(
    QSequentialAnimationGroup *self,
    QAbstractAnimation::Direction direction) {
  self->updateDirection(direction);
}

//  QSequentialAnimationGroupPrivate *QSequentialAnimationGroup::d_func()
extern "C" Q_DECL_EXPORT
QSequentialAnimationGroupPrivate *ritual_ZN25QSequentialAnimationGroup6d_funcEv(
    QSequentialAnimationGroup *self) {
  return self->d_func();
}

//  const QSequentialAnimationGroupPrivate
//      *QSequentialAnimationGroup::d_func() const
extern "C" Q_DECL_EXPORT
const QSequentialAnimationGroupPrivate *ritual_ZNK25QSequentialAnimationGroup6d_funcEv(
    const QSequentialAnimationGroup *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQSequentialAnimationGroup, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSequentialAnimationGroup(
    QSequentialAnimationGroup *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSequentialAnimationGroup *>(self)->take(key, call);
}

//  int QSequentialAnimationGroup::duration() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK25QSequentialAnimationGroup8durationEv(
    const QSequentialAnimationGroup *self) {
  return self->QSequentialAnimationGroup::duration();
}

//  bool QSequentialAnimationGroup::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN25QSequentialAnimationGroup5eventEP6QEvent(
    QSequentialAnimationGroup *self,
    QEvent *event) {
  return static_cast<OwnQSequentialAnimationGroup *>(self)->OwnQSequentialAnimationGroup::event(
      event);
}

//  void QSequentialAnimationGroup::updateCurrentTime(int a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN25QSequentialAnimationGroup17updateCurrentTimeEi(
    QSequentialAnimationGroup *self,
    int a0) {
  static_cast<OwnQSequentialAnimationGroup *>(self)->OwnQSequentialAnimationGroup::updateCurrentTime(
      a0);
}

//  void QSequentialAnimationGroup::updateState(QAbstractAnimation::State
//      newState, QAbstractAnimation::State oldState)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN25QSequentialAnimationGroup11updateStateEN18QAbstractAnimation5StateES1_(
    QSequentialAnimationGroup *self,
    QAbstractAnimation::State newState,
    QAbstractAnimation::State oldState) {
  static_cast<OwnQSequentialAnimationGroup *>(self)->OwnQSequentialAnimationGroup::updateState(
      newState,
      oldState);
}

//  void
//      QSequentialAnimationGroup::updateDirection(QAbstractAnimation::Direct
//      ion direction)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN25QSequentialAnimationGroup15updateDirectionEN18QAbstractAnimation9DirectionE(
    QSequentialAnimationGroup *self,
    QAbstractAnimation::Direction direction) {
  static_cast<OwnQSequentialAnimationGroup *>(self)->OwnQSequentialAnimationGroup::updateDirection(
      direction);
}

#endif  // QT_CONFIG(animation)
#endif  // QT_CONFIG(animation)
