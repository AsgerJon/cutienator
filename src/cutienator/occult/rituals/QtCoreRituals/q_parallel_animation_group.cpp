//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qparallelanimationgroup.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#if QT_CONFIG(animation)
#include <QtCore/qparallelanimationgroup.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QParallelAnimationGroup may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQParallelAnimationGroup : QParallelAnimationGroup {
  using QParallelAnimationGroup::event;
  using QParallelAnimationGroup::updateCurrentTime;
  using QParallelAnimationGroup::updateState;
  using QParallelAnimationGroup::updateDirection;
};

//  A QParallelAnimationGroup that Python can take functions over in. Every QParallelAnimationGroup
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(animation)
typedef int (*CuteQParallelAnimationGroupCall0)(const void *, int *);
#endif  // QT_CONFIG(animation)
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(animation)
typedef bool (*CuteQParallelAnimationGroupCall1)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(animation)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(animation)
typedef void (*CuteQParallelAnimationGroupCall2)(const void *, int, int *);
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
typedef void (*CuteQParallelAnimationGroupCall3)(const void *, int, int, int *);
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
typedef void (*CuteQParallelAnimationGroupCall4)(const void *, int, int *);
#endif  // QT_CONFIG(animation)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQParallelAnimationGroupCall5)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQParallelAnimationGroupCall6)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQParallelAnimationGroupCall7)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQParallelAnimationGroupCall8)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQParallelAnimationGroupCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQParallelAnimationGroupCall10)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQParallelAnimationGroup : public QParallelAnimationGroup {
public:
  using QParallelAnimationGroup::QParallelAnimationGroup;
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
  //  int QParallelAnimationGroup::duration() const
  int duration() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQParallelAnimationGroupCall0 call = reinterpret_cast<CuteQParallelAnimationGroupCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QParallelAnimationGroup::duration();
  }
#endif  // QT_CONFIG(animation)

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(animation)
  //  bool QParallelAnimationGroup::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQParallelAnimationGroupCall1 call = reinterpret_cast<CuteQParallelAnimationGroupCall1>(taken[1]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QParallelAnimationGroup::event(event);
  }
#endif  // QT_CONFIG(animation)
#endif  // !defined(QT_NO_QOBJECT)

#if QT_CONFIG(animation)
  //  void QParallelAnimationGroup::updateCurrentTime(int currentTime)
  void updateCurrentTime(int currentTime) override {
    if (taken[2]) {
      int handled = 0;
      CuteQParallelAnimationGroupCall2 call = reinterpret_cast<CuteQParallelAnimationGroupCall2>(taken[2]);
      call(this, currentTime, &handled);
      if (handled) return;
    }
    QParallelAnimationGroup::updateCurrentTime(currentTime);
  }
#endif  // QT_CONFIG(animation)

#if QT_CONFIG(animation)
  //  void QParallelAnimationGroup::updateState(QAbstractAnimation::State
  //      newState, QAbstractAnimation::State oldState)
  void updateState(
      QAbstractAnimation::State newState,
      QAbstractAnimation::State oldState) override {
    if (taken[3]) {
      int handled = 0;
      CuteQParallelAnimationGroupCall3 call = reinterpret_cast<CuteQParallelAnimationGroupCall3>(taken[3]);
      call(this, static_cast<int>(newState), static_cast<int>(oldState), &handled);
      if (handled) return;
    }
    QParallelAnimationGroup::updateState(newState, oldState);
  }
#endif  // QT_CONFIG(animation)

#if QT_CONFIG(animation)
  //  void QParallelAnimationGroup::updateDirection(QAbstractAnimation::Dir
  //      ection direction)
  void updateDirection(QAbstractAnimation::Direction direction) override {
    if (taken[4]) {
      int handled = 0;
      CuteQParallelAnimationGroupCall4 call = reinterpret_cast<CuteQParallelAnimationGroupCall4>(taken[4]);
      call(this, static_cast<int>(direction), &handled);
      if (handled) return;
    }
    QParallelAnimationGroup::updateDirection(direction);
  }
#endif  // QT_CONFIG(animation)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQParallelAnimationGroupCall5 call = reinterpret_cast<CuteQParallelAnimationGroupCall5>(taken[5]);
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
      CuteQParallelAnimationGroupCall6 call = reinterpret_cast<CuteQParallelAnimationGroupCall6>(taken[6]);
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
      CuteQParallelAnimationGroupCall7 call = reinterpret_cast<CuteQParallelAnimationGroupCall7>(taken[7]);
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
      CuteQParallelAnimationGroupCall8 call = reinterpret_cast<CuteQParallelAnimationGroupCall8>(taken[8]);
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
      CuteQParallelAnimationGroupCall9 call = reinterpret_cast<CuteQParallelAnimationGroupCall9>(taken[9]);
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
      CuteQParallelAnimationGroupCall10 call = reinterpret_cast<CuteQParallelAnimationGroupCall10>(taken[10]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QParallelAnimationGroup::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK23QParallelAnimationGroup10metaObjectEv(
    const QParallelAnimationGroup *self) {
  return self->metaObject();
}

//  QString QParallelAnimationGroup::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN23QParallelAnimationGroup2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QParallelAnimationGroup::tr(s, c, n));
}

//  QParallelAnimationGroup::QParallelAnimationGroup(QObject *parent)
extern "C" Q_DECL_EXPORT
QParallelAnimationGroup *ritual_ZN23QParallelAnimationGroupC1EP7QObject(
    QObject *parent) {
  return new CuteQParallelAnimationGroup(parent);
}

//  QParallelAnimationGroup::~QParallelAnimationGroup()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QParallelAnimationGroupD1Ev(QParallelAnimationGroup *self) {
  delete self;
}

//  int QParallelAnimationGroup::duration() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK23QParallelAnimationGroup8durationEv(
    const QParallelAnimationGroup *self) {
  return self->duration();
}

//  bool QParallelAnimationGroup::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN23QParallelAnimationGroup5eventEP6QEvent(
    QParallelAnimationGroup *self,
    QEvent *event) {
  return self->event(event);
}

//  void QParallelAnimationGroup::updateCurrentTime(int currentTime)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QParallelAnimationGroup17updateCurrentTimeEi(
    QParallelAnimationGroup *self,
    int currentTime) {
  self->updateCurrentTime(currentTime);
}

//  void QParallelAnimationGroup::updateState(QAbstractAnimation::State
//      newState, QAbstractAnimation::State oldState)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QParallelAnimationGroup11updateStateEN18QAbstractAnimation5StateES1_(
    QParallelAnimationGroup *self,
    QAbstractAnimation::State newState,
    QAbstractAnimation::State oldState) {
  self->updateState(newState, oldState);
}

//  void
//      QParallelAnimationGroup::updateDirection(QAbstractAnimation::Directio
//      n direction)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QParallelAnimationGroup15updateDirectionEN18QAbstractAnimation9DirectionE(
    QParallelAnimationGroup *self,
    QAbstractAnimation::Direction direction) {
  self->updateDirection(direction);
}

//  QParallelAnimationGroupPrivate *QParallelAnimationGroup::d_func()
extern "C" Q_DECL_EXPORT
QParallelAnimationGroupPrivate *ritual_ZN23QParallelAnimationGroup6d_funcEv(
    QParallelAnimationGroup *self) {
  return self->d_func();
}

//  const QParallelAnimationGroupPrivate *QParallelAnimationGroup::d_func()
//      const
extern "C" Q_DECL_EXPORT
const QParallelAnimationGroupPrivate *ritual_ZNK23QParallelAnimationGroup6d_funcEv(
    const QParallelAnimationGroup *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQParallelAnimationGroup, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QParallelAnimationGroup(
    QParallelAnimationGroup *self,
    const char *key,
    void *call) {
  return static_cast<CuteQParallelAnimationGroup *>(self)->take(key, call);
}

//  int QParallelAnimationGroup::duration() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK23QParallelAnimationGroup8durationEv(
    const QParallelAnimationGroup *self) {
  return self->QParallelAnimationGroup::duration();
}

//  bool QParallelAnimationGroup::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN23QParallelAnimationGroup5eventEP6QEvent(
    QParallelAnimationGroup *self,
    QEvent *event) {
  return static_cast<OwnQParallelAnimationGroup *>(self)->OwnQParallelAnimationGroup::event(
      event);
}

//  void QParallelAnimationGroup::updateCurrentTime(int currentTime)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QParallelAnimationGroup17updateCurrentTimeEi(
    QParallelAnimationGroup *self,
    int currentTime) {
  static_cast<OwnQParallelAnimationGroup *>(self)->OwnQParallelAnimationGroup::updateCurrentTime(
      currentTime);
}

//  void QParallelAnimationGroup::updateState(QAbstractAnimation::State
//      newState, QAbstractAnimation::State oldState)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QParallelAnimationGroup11updateStateEN18QAbstractAnimation5StateES1_(
    QParallelAnimationGroup *self,
    QAbstractAnimation::State newState,
    QAbstractAnimation::State oldState) {
  static_cast<OwnQParallelAnimationGroup *>(self)->OwnQParallelAnimationGroup::updateState(
      newState,
      oldState);
}

//  void
//      QParallelAnimationGroup::updateDirection(QAbstractAnimation::Directio
//      n direction)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QParallelAnimationGroup15updateDirectionEN18QAbstractAnimation9DirectionE(
    QParallelAnimationGroup *self,
    QAbstractAnimation::Direction direction) {
  static_cast<OwnQParallelAnimationGroup *>(self)->OwnQParallelAnimationGroup::updateDirection(
      direction);
}

#endif  // QT_CONFIG(animation)
