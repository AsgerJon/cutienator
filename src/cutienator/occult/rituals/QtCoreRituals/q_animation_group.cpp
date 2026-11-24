//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qanimationgroup.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#if QT_CONFIG(animation)
#if QT_CONFIG(animation)
#include <QtCore/qanimationgroup.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QAnimationGroup may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQAnimationGroup : QAnimationGroup {
  using QAnimationGroup::event;
};

//  A QAnimationGroup that Python can take functions over in. Every QAnimationGroup
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(animation)
typedef bool (*CuteQAnimationGroupCall0)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(animation)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(animation)
typedef int (*CuteQAnimationGroupCall1)(const void *, int *);
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
typedef void (*CuteQAnimationGroupCall2)(const void *, int, int *);
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
typedef void (*CuteQAnimationGroupCall3)(const void *, int, int, int *);
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
typedef void (*CuteQAnimationGroupCall4)(const void *, int, int *);
#endif  // QT_CONFIG(animation)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAnimationGroupCall5)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAnimationGroupCall6)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAnimationGroupCall7)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAnimationGroupCall8)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAnimationGroupCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAnimationGroupCall10)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQAnimationGroup : public QAnimationGroup {
public:
  using QAnimationGroup::QAnimationGroup;
  void *taken[11] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(animation)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(animation)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(animation)
    if (!std::strcmp(key, "_ZNK18QAbstractAnimation8durationEv")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(animation)
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

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(animation)
  //  bool QAnimationGroup::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQAnimationGroupCall0 call = reinterpret_cast<CuteQAnimationGroupCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QAnimationGroup::event(event);
  }
#endif  // QT_CONFIG(animation)
#endif  // !defined(QT_NO_QOBJECT)

#if QT_CONFIG(animation)
  //  int QAbstractAnimation::duration() const
  int duration() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQAnimationGroupCall1 call = reinterpret_cast<CuteQAnimationGroupCall1>(taken[1]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }
#endif  // QT_CONFIG(animation)

#if QT_CONFIG(animation)
  //  void QAbstractAnimation::updateCurrentTime(int currentTime)
  void updateCurrentTime(int currentTime) override {
    if (taken[2]) {
      int handled = 0;
      CuteQAnimationGroupCall2 call = reinterpret_cast<CuteQAnimationGroupCall2>(taken[2]);
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
      CuteQAnimationGroupCall3 call = reinterpret_cast<CuteQAnimationGroupCall3>(taken[3]);
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
      CuteQAnimationGroupCall4 call = reinterpret_cast<CuteQAnimationGroupCall4>(taken[4]);
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
      CuteQAnimationGroupCall5 call = reinterpret_cast<CuteQAnimationGroupCall5>(taken[5]);
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
      CuteQAnimationGroupCall6 call = reinterpret_cast<CuteQAnimationGroupCall6>(taken[6]);
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
      CuteQAnimationGroupCall7 call = reinterpret_cast<CuteQAnimationGroupCall7>(taken[7]);
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
      CuteQAnimationGroupCall8 call = reinterpret_cast<CuteQAnimationGroupCall8>(taken[8]);
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
      CuteQAnimationGroupCall9 call = reinterpret_cast<CuteQAnimationGroupCall9>(taken[9]);
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
      CuteQAnimationGroupCall10 call = reinterpret_cast<CuteQAnimationGroupCall10>(taken[10]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QAnimationGroup::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QAnimationGroup10metaObjectEv(
    const QAnimationGroup *self) {
  return self->metaObject();
}

//  QString QAnimationGroup::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QAnimationGroup2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QAnimationGroup::tr(s, c, n));
}

//  QAnimationGroup::~QAnimationGroup()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAnimationGroupD1Ev(QAnimationGroup *self) {
  delete self;
}

//  QAbstractAnimation *QAnimationGroup::animationAt(int index) const
extern "C" Q_DECL_EXPORT
QAbstractAnimation *ritual_ZNK15QAnimationGroup11animationAtEi(
    const QAnimationGroup *self,
    int index) {
  return self->animationAt(index);
}

//  int QAnimationGroup::animationCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QAnimationGroup14animationCountEv(
    const QAnimationGroup *self) {
  return self->animationCount();
}

//  int QAnimationGroup::indexOfAnimation(QAbstractAnimation *animation)
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QAnimationGroup16indexOfAnimationEP18QAbstractAnimation(
    const QAnimationGroup *self,
    QAbstractAnimation *animation) {
  return self->indexOfAnimation(animation);
}

//  void QAnimationGroup::addAnimation(QAbstractAnimation *animation)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAnimationGroup12addAnimationEP18QAbstractAnimation(
    QAnimationGroup *self,
    QAbstractAnimation *animation) {
  self->addAnimation(animation);
}

//  void QAnimationGroup::insertAnimation(int index, QAbstractAnimation
//      *animation)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAnimationGroup15insertAnimationEiP18QAbstractAnimation(
    QAnimationGroup *self,
    int index,
    QAbstractAnimation *animation) {
  self->insertAnimation(index, animation);
}

//  void QAnimationGroup::removeAnimation(QAbstractAnimation *animation)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAnimationGroup15removeAnimationEP18QAbstractAnimation(
    QAnimationGroup *self,
    QAbstractAnimation *animation) {
  self->removeAnimation(animation);
}

//  QAbstractAnimation *QAnimationGroup::takeAnimation(int index)
extern "C" Q_DECL_EXPORT
QAbstractAnimation *ritual_ZN15QAnimationGroup13takeAnimationEi(
    QAnimationGroup *self,
    int index) {
  return self->takeAnimation(index);
}

//  void QAnimationGroup::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAnimationGroup5clearEv(QAnimationGroup *self) {
  self->clear();
}

//  bool QAnimationGroup::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QAnimationGroup5eventEP6QEvent(
    QAnimationGroup *self,
    QEvent *event) {
  return self->event(event);
}

//  QAnimationGroupPrivate *QAnimationGroup::d_func()
extern "C" Q_DECL_EXPORT
QAnimationGroupPrivate *ritual_ZN15QAnimationGroup6d_funcEv(
    QAnimationGroup *self) {
  return self->d_func();
}

//  const QAnimationGroupPrivate *QAnimationGroup::d_func() const
extern "C" Q_DECL_EXPORT
const QAnimationGroupPrivate *ritual_ZNK15QAnimationGroup6d_funcEv(
    const QAnimationGroup *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQAnimationGroup, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAnimationGroup(
    QAnimationGroup *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAnimationGroup *>(self)->take(key, call);
}

//  bool QAnimationGroup::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN15QAnimationGroup5eventEP6QEvent(
    QAnimationGroup *self,
    QEvent *event) {
  return static_cast<OwnQAnimationGroup *>(self)->OwnQAnimationGroup::event(
      event);
}

#endif  // QT_CONFIG(animation)
#endif  // QT_CONFIG(animation)
