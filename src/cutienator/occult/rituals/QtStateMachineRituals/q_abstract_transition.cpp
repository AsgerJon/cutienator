//  Written by dev_tooling.RitualGenerator from the records of
//  QtStateMachine/qabstracttransition.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtCore/qglobal.h>
#include <QtStateMachine/qabstracttransition.h>
#include <QtCore/qstring.h>
#include <QtStateMachine/qabstractstate.h>
#include <QtCore/qabstractanimation.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  Only a class built on QAbstractTransition may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQAbstractTransition : QAbstractTransition {
  using QAbstractTransition::event;
};

//  A QAbstractTransition that Python can take functions over in. Every QAbstractTransition
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQAbstractTransitionCall0)(const void *, QEvent *, int *);
typedef void (*CuteQAbstractTransitionCall1)(const void *, QEvent *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAbstractTransitionCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAbstractTransitionCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractTransitionCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractTransitionCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractTransitionCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractTransitionCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractTransitionCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQAbstractTransition : public QAbstractTransition {
public:
  using QAbstractTransition::QAbstractTransition;
  void *taken[9] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN19QAbstractTransition9eventTestEP6QEvent")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QAbstractTransition12onTransitionEP6QEvent")) {
      taken[1] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  bool QAbstractTransition::eventTest(QEvent *event)
  bool eventTest(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQAbstractTransitionCall0 call = reinterpret_cast<CuteQAbstractTransitionCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QAbstractTransition::onTransition(QEvent *event)
  void onTransition(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQAbstractTransitionCall1 call = reinterpret_cast<CuteQAbstractTransitionCall1>(taken[1]);
      call(this, event, &handled);
      if (handled) return;
    }
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QAbstractTransition::event(QEvent *e)
  bool event(QEvent *e) override {
    if (taken[2]) {
      int handled = 0;
      CuteQAbstractTransitionCall2 call = reinterpret_cast<CuteQAbstractTransitionCall2>(taken[2]);
      bool given = call(this, e, &handled);
      if (handled) return given;
    }
    return QAbstractTransition::event(e);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQAbstractTransitionCall3 call = reinterpret_cast<CuteQAbstractTransitionCall3>(taken[3]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQAbstractTransitionCall4 call = reinterpret_cast<CuteQAbstractTransitionCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQAbstractTransitionCall5 call = reinterpret_cast<CuteQAbstractTransitionCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQAbstractTransitionCall6 call = reinterpret_cast<CuteQAbstractTransitionCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[7]) {
      int handled = 0;
      CuteQAbstractTransitionCall7 call = reinterpret_cast<CuteQAbstractTransitionCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[8]) {
      int handled = 0;
      CuteQAbstractTransitionCall8 call = reinterpret_cast<CuteQAbstractTransitionCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QAbstractTransition::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19QAbstractTransition10metaObjectEv(
    const QAbstractTransition *self) {
  return self->metaObject();
}

//  QString QAbstractTransition::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19QAbstractTransition2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QAbstractTransition::tr(s, c, n));
}

//  QAbstractTransition::~QAbstractTransition()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QAbstractTransitionD1Ev(QAbstractTransition *self) {
  delete self;
}

//  QState *QAbstractTransition::sourceState() const
extern "C" Q_DECL_EXPORT
QState *ritual_ZNK19QAbstractTransition11sourceStateEv(
    const QAbstractTransition *self) {
  return self->sourceState();
}

//  QAbstractState *QAbstractTransition::targetState() const
extern "C" Q_DECL_EXPORT
QAbstractState *ritual_ZNK19QAbstractTransition11targetStateEv(
    const QAbstractTransition *self) {
  return self->targetState();
}

//  void QAbstractTransition::setTargetState(QAbstractState *target)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QAbstractTransition14setTargetStateEP14QAbstractState(
    QAbstractTransition *self,
    QAbstractState *target) {
  self->setTargetState(target);
}

//  QList<QAbstractState *> QAbstractTransition::targetStates() const
extern "C" Q_DECL_EXPORT
QList<QAbstractState *> *ritual_ZNK19QAbstractTransition12targetStatesEv(
    const QAbstractTransition *self) {
  return new QList<QAbstractState *>(self->targetStates());
}

//  void QAbstractTransition::setTargetStates(const QList<QAbstractState *>
//      &targets)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QAbstractTransition15setTargetStatesERK5QListIP14QAbstractStateE(
    QAbstractTransition *self,
    const QList<QAbstractState *> *targets) {
  self->setTargetStates(*targets);
}

//  TransitionType QAbstractTransition::transitionType() const
extern "C" Q_DECL_EXPORT
QAbstractTransition::TransitionType ritual_ZNK19QAbstractTransition14transitionTypeEv(
    const QAbstractTransition *self) {
  return self->transitionType();
}

//  void QAbstractTransition::setTransitionType(TransitionType type)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QAbstractTransition17setTransitionTypeENS_14TransitionTypeE(
    QAbstractTransition *self,
    QAbstractTransition::TransitionType type) {
  self->setTransitionType(type);
}

//  QStateMachine *QAbstractTransition::machine() const
extern "C" Q_DECL_EXPORT
QStateMachine *ritual_ZNK19QAbstractTransition7machineEv(
    const QAbstractTransition *self) {
  return self->machine();
}

#if QT_CONFIG(animation)
//  void QAbstractTransition::addAnimation(QAbstractAnimation *animation)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QAbstractTransition12addAnimationEP18QAbstractAnimation(
    QAbstractTransition *self,
    QAbstractAnimation *animation) {
  self->addAnimation(animation);
}
#endif  // QT_CONFIG(animation)

#if QT_CONFIG(animation)
//  void QAbstractTransition::removeAnimation(QAbstractAnimation *animation)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QAbstractTransition15removeAnimationEP18QAbstractAnimation(
    QAbstractTransition *self,
    QAbstractAnimation *animation) {
  self->removeAnimation(animation);
}
#endif  // QT_CONFIG(animation)

#if QT_CONFIG(animation)
//  QList<QAbstractAnimation *> QAbstractTransition::animations() const
extern "C" Q_DECL_EXPORT
QList<QAbstractAnimation *> *ritual_ZNK19QAbstractTransition10animationsEv(
    const QAbstractTransition *self) {
  return new QList<QAbstractAnimation *>(self->animations());
}
#endif  // QT_CONFIG(animation)

//  bool QAbstractTransition::eventTest(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QAbstractTransition9eventTestEP6QEvent(
    QAbstractTransition *self,
    QEvent *event) {
  return self->eventTest(event);
}

//  void QAbstractTransition::onTransition(QEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QAbstractTransition12onTransitionEP6QEvent(
    QAbstractTransition *self,
    QEvent *event) {
  self->onTransition(event);
}

//  bool QAbstractTransition::event(QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QAbstractTransition5eventEP6QEvent(
    QAbstractTransition *self,
    QEvent *e) {
  return self->event(e);
}

//  a Python function taken by a CuteQAbstractTransition, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAbstractTransition(
    QAbstractTransition *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAbstractTransition *>(self)->take(key, call);
}

//  bool QAbstractTransition::event(QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN19QAbstractTransition5eventEP6QEvent(
    QAbstractTransition *self,
    QEvent *e) {
  return static_cast<OwnQAbstractTransition *>(self)->OwnQAbstractTransition::event(
      e);
}

//  QList<QAbstractTransition *>::QList()
extern "C" Q_DECL_EXPORT
QList<QAbstractTransition *> *ritual_list_make_QAbstractTransition_ptr() {
  return new QList<QAbstractTransition *>();
}

//  void QList<QAbstractTransition *>::append(const QAbstractTransition *
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QAbstractTransition_ptr(
    QList<QAbstractTransition *> *self,
    QAbstractTransition *element) {
  self->append(element);
}

//  qsizetype QList<QAbstractTransition *>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QAbstractTransition_ptr(
    const QList<QAbstractTransition *> *self) {
  return self->size();
}

//  const QAbstractTransition * &QList<QAbstractTransition *>::at(qsizetype
//      i) const
extern "C" Q_DECL_EXPORT
QAbstractTransition *ritual_list_at_QAbstractTransition_ptr(
    const QList<QAbstractTransition *> *self,
    long long index) {
  return self->at(index);
}

//  QList<QAbstractTransition *>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QAbstractTransition_ptr(
    QList<QAbstractTransition *> *self) {
  delete self;
}
