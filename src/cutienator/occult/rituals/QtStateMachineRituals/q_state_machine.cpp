//  Written by dev_tooling.RitualGenerator from the records of
//  QtStateMachine/qstatemachine.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#include <QtStateMachine/qstatemachine.h>
#include <QtCore/qstring.h>
#if QT_CONFIG(animation)
#include <QtCore/qabstractanimation.h>
#endif
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>
#include <QtCore/QBindable>
#include <QtCore/QString>
#include <QtStateMachine/QState>
#include <QtCore/QSet>
#include <QtStateMachine/QAbstractState>

//  Only a class built on QStateMachine may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQStateMachine : QStateMachine {
  using QStateMachine::onEntry;
  using QStateMachine::onExit;
  using QStateMachine::beginSelectTransitions;
  using QStateMachine::endSelectTransitions;
  using QStateMachine::beginMicrostep;
  using QStateMachine::endMicrostep;
  using QStateMachine::event;
};

//  A QStateMachine that Python can take functions over in. Every QStateMachine
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQStateMachineCall0)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQStateMachineCall1)(const void *, QEvent *, int *);
typedef void (*CuteQStateMachineCall2)(const void *, QEvent *, int *);
typedef void (*CuteQStateMachineCall3)(const void *, QEvent *, int *);
typedef void (*CuteQStateMachineCall4)(const void *, QEvent *, int *);
typedef void (*CuteQStateMachineCall5)(const void *, QEvent *, int *);
typedef void (*CuteQStateMachineCall6)(const void *, QEvent *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQStateMachineCall7)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQStateMachineCall8)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQStateMachineCall9)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQStateMachineCall10)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQStateMachineCall11)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQStateMachineCall12)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQStateMachine : public QStateMachine {
public:
  using QStateMachine::QStateMachine;
  void *taken[13] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN14QAbstractState7onEntryEP6QEvent")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QAbstractState6onExitEP6QEvent")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QStateMachine22beginSelectTransitionsEP6QEvent")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QStateMachine20endSelectTransitionsEP6QEvent")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QStateMachine14beginMicrostepEP6QEvent")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QStateMachine12endMicrostepEP6QEvent")) {
      taken[6] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QStateMachine::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQStateMachineCall0 call = reinterpret_cast<CuteQStateMachineCall0>(taken[0]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QStateMachine::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QStateMachine::onEntry(QEvent *event)
  void onEntry(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQStateMachineCall1 call = reinterpret_cast<CuteQStateMachineCall1>(taken[1]);
      call(this, event, &handled);
      if (handled) return;
    }
    QStateMachine::onEntry(event);
  }

  //  void QStateMachine::onExit(QEvent *event)
  void onExit(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQStateMachineCall2 call = reinterpret_cast<CuteQStateMachineCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QStateMachine::onExit(event);
  }

  //  void QStateMachine::beginSelectTransitions(QEvent *event)
  void beginSelectTransitions(QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQStateMachineCall3 call = reinterpret_cast<CuteQStateMachineCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QStateMachine::beginSelectTransitions(event);
  }

  //  void QStateMachine::endSelectTransitions(QEvent *event)
  void endSelectTransitions(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQStateMachineCall4 call = reinterpret_cast<CuteQStateMachineCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QStateMachine::endSelectTransitions(event);
  }

  //  void QStateMachine::beginMicrostep(QEvent *event)
  void beginMicrostep(QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQStateMachineCall5 call = reinterpret_cast<CuteQStateMachineCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QStateMachine::beginMicrostep(event);
  }

  //  void QStateMachine::endMicrostep(QEvent *event)
  void endMicrostep(QEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQStateMachineCall6 call = reinterpret_cast<CuteQStateMachineCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QStateMachine::endMicrostep(event);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QStateMachine::event(QEvent *e)
  bool event(QEvent *e) override {
    if (taken[7]) {
      int handled = 0;
      CuteQStateMachineCall7 call = reinterpret_cast<CuteQStateMachineCall7>(taken[7]);
      bool given = call(this, e, &handled);
      if (handled) return given;
    }
    return QStateMachine::event(e);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQStateMachineCall8 call = reinterpret_cast<CuteQStateMachineCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQStateMachineCall9 call = reinterpret_cast<CuteQStateMachineCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQStateMachineCall10 call = reinterpret_cast<CuteQStateMachineCall10>(taken[10]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[11]) {
      int handled = 0;
      CuteQStateMachineCall11 call = reinterpret_cast<CuteQStateMachineCall11>(taken[11]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[12]) {
      int handled = 0;
      CuteQStateMachineCall12 call = reinterpret_cast<CuteQStateMachineCall12>(taken[12]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QStateMachine::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13QStateMachine10metaObjectEv(
    const QStateMachine *self) {
  return self->metaObject();
}

//  void *QStateMachine::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN13QStateMachine11qt_metacastEPKc(
    QStateMachine *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QStateMachine::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN13QStateMachine11qt_metacallEN11QMetaObject4CallEiPPv(
    QStateMachine *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QStateMachine::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13QStateMachine2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QStateMachine::tr(s, c, n));
}

//  QStateMachine::QStateMachine(QObject *parent)
extern "C" Q_DECL_EXPORT
QStateMachine *ritual_ZN13QStateMachineC1EP7QObject(QObject *parent) {
  return new CuteQStateMachine(parent);
}

//  QStateMachine::QStateMachine(QState::ChildMode childMode, QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QStateMachine *ritual_ZN13QStateMachineC1EN6QState9ChildModeEP7QObject(
    QState::ChildMode childMode,
    QObject *parent) {
  return new CuteQStateMachine(childMode, parent);
}

//  QStateMachine::~QStateMachine()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QStateMachineD1Ev(QStateMachine *self) {
  delete self;
}

//  void QStateMachine::addState(QAbstractState *state)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QStateMachine8addStateEP14QAbstractState(
    QStateMachine *self,
    QAbstractState *state) {
  self->addState(state);
}

//  void QStateMachine::removeState(QAbstractState *state)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QStateMachine11removeStateEP14QAbstractState(
    QStateMachine *self,
    QAbstractState *state) {
  self->removeState(state);
}

//  Error QStateMachine::error() const
extern "C" Q_DECL_EXPORT
QStateMachine::Error ritual_ZNK13QStateMachine5errorEv(
    const QStateMachine *self) {
  return self->error();
}

//  QString QStateMachine::errorString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13QStateMachine11errorStringEv(
    const QStateMachine *self) {
  return new QString(self->errorString());
}

//  void QStateMachine::clearError()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QStateMachine10clearErrorEv(QStateMachine *self) {
  self->clearError();
}

//  QBindable<QString> QStateMachine::bindableErrorString() const
extern "C" Q_DECL_EXPORT
QBindable<QString> *ritual_ZNK13QStateMachine19bindableErrorStringEv(
    const QStateMachine *self) {
  return new QBindable<QString>(self->bindableErrorString());
}

//  bool QStateMachine::isRunning() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QStateMachine9isRunningEv(const QStateMachine *self) {
  return self->isRunning();
}

#if QT_CONFIG(animation)
//  bool QStateMachine::isAnimated() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QStateMachine10isAnimatedEv(const QStateMachine *self) {
  return self->isAnimated();
}
#endif  // QT_CONFIG(animation)

#if QT_CONFIG(animation)
//  void QStateMachine::setAnimated(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QStateMachine11setAnimatedEb(
    QStateMachine *self,
    bool enabled) {
  self->setAnimated(enabled);
}
#endif  // QT_CONFIG(animation)

#if QT_CONFIG(animation)
//  QBindable<bool> QStateMachine::bindableAnimated()
extern "C" Q_DECL_EXPORT
QBindable<bool> *ritual_ZN13QStateMachine16bindableAnimatedEv(
    QStateMachine *self) {
  return new QBindable<bool>(self->bindableAnimated());
}
#endif  // QT_CONFIG(animation)

#if QT_CONFIG(animation)
//  void QStateMachine::addDefaultAnimation(QAbstractAnimation *animation)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QStateMachine19addDefaultAnimationEP18QAbstractAnimation(
    QStateMachine *self,
    QAbstractAnimation *animation) {
  self->addDefaultAnimation(animation);
}
#endif  // QT_CONFIG(animation)

#if QT_CONFIG(animation)
//  QList<QAbstractAnimation *> QStateMachine::defaultAnimations() const
extern "C" Q_DECL_EXPORT
QList<QAbstractAnimation *> *ritual_ZNK13QStateMachine17defaultAnimationsEv(
    const QStateMachine *self) {
  return new QList<QAbstractAnimation *>(self->defaultAnimations());
}
#endif  // QT_CONFIG(animation)

#if QT_CONFIG(animation)
//  void QStateMachine::removeDefaultAnimation(QAbstractAnimation *animation)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QStateMachine22removeDefaultAnimationEP18QAbstractAnimation(
    QStateMachine *self,
    QAbstractAnimation *animation) {
  self->removeDefaultAnimation(animation);
}
#endif  // QT_CONFIG(animation)

//  QState::RestorePolicy QStateMachine::globalRestorePolicy() const
extern "C" Q_DECL_EXPORT
QState::RestorePolicy ritual_ZNK13QStateMachine19globalRestorePolicyEv(
    const QStateMachine *self) {
  return self->globalRestorePolicy();
}

//  void QStateMachine::setGlobalRestorePolicy(QState::RestorePolicy
//      restorePolicy)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QStateMachine22setGlobalRestorePolicyEN6QState13RestorePolicyE(
    QStateMachine *self,
    QState::RestorePolicy restorePolicy) {
  self->setGlobalRestorePolicy(restorePolicy);
}

//  QBindable<QState::RestorePolicy>
//      QStateMachine::bindableGlobalRestorePolicy()
extern "C" Q_DECL_EXPORT
QBindable<QState::RestorePolicy> *ritual_ZN13QStateMachine27bindableGlobalRestorePolicyEv(
    QStateMachine *self) {
  return new QBindable<QState::RestorePolicy>(
      self->bindableGlobalRestorePolicy());
}

//  void QStateMachine::postEvent(QEvent *event, EventPriority priority)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QStateMachine9postEventEP6QEventNS_13EventPriorityE(
    QStateMachine *self,
    QEvent *event,
    QStateMachine::EventPriority priority) {
  self->postEvent(event, priority);
}

//  int QStateMachine::postDelayedEvent(QEvent *event, int delay)
extern "C" Q_DECL_EXPORT
int ritual_ZN13QStateMachine16postDelayedEventEP6QEventi(
    QStateMachine *self,
    QEvent *event,
    int delay) {
  return self->postDelayedEvent(event, delay);
}

//  bool QStateMachine::cancelDelayedEvent(int id)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QStateMachine18cancelDelayedEventEi(
    QStateMachine *self,
    int id) {
  return self->cancelDelayedEvent(id);
}

//  QSet<QAbstractState *> QStateMachine::configuration() const
extern "C" Q_DECL_EXPORT
QSet<QAbstractState *> *ritual_ZNK13QStateMachine13configurationEv(
    const QStateMachine *self) {
  return new QSet<QAbstractState *>(self->configuration());
}

//  bool QStateMachine::eventFilter(QObject *watched, QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QStateMachine11eventFilterEP7QObjectP6QEvent(
    QStateMachine *self,
    QObject *watched,
    QEvent *event) {
  return self->eventFilter(watched, event);
}

#if __has_include(<chrono>) || defined(Q_QDOC)
//  int QStateMachine::postDelayedEvent(QEvent *event,
//      std::chrono::milliseconds delay)
extern "C" Q_DECL_EXPORT
int ritual_ZN13QStateMachine16postDelayedEventEP6QEventNSt6chrono8durationIlSt5ratioILl1ELl1000EEEE(
    QStateMachine *self,
    QEvent *event,
    long long delay) {
  return self->postDelayedEvent(event, std::chrono::milliseconds(delay));
}
#endif  // __has_include(<chrono>) || defined(Q_QDOC)

//  void QStateMachine::start()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QStateMachine5startEv(QStateMachine *self) {
  self->start();
}

//  void QStateMachine::stop()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QStateMachine4stopEv(QStateMachine *self) {
  self->stop();
}

//  void QStateMachine::setRunning(bool running)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QStateMachine10setRunningEb(
    QStateMachine *self,
    bool running) {
  self->setRunning(running);
}

//  void QStateMachine::started(QPrivateSignal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QStateMachine7startedENS_14QPrivateSignalE(
    QStateMachine *self) {
  self->started(QStateMachine::QPrivateSignal());
}

//  void QStateMachine::stopped(QPrivateSignal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QStateMachine7stoppedENS_14QPrivateSignalE(
    QStateMachine *self) {
  self->stopped(QStateMachine::QPrivateSignal());
}

//  void QStateMachine::runningChanged(bool running)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QStateMachine14runningChangedEb(
    QStateMachine *self,
    bool running) {
  self->runningChanged(running);
}

//  void QStateMachine::onEntry(QEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QStateMachine7onEntryEP6QEvent(
    QStateMachine *self,
    QEvent *event) {
  self->onEntry(event);
}

//  void QStateMachine::onExit(QEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QStateMachine6onExitEP6QEvent(
    QStateMachine *self,
    QEvent *event) {
  self->onExit(event);
}

//  void QStateMachine::beginSelectTransitions(QEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QStateMachine22beginSelectTransitionsEP6QEvent(
    QStateMachine *self,
    QEvent *event) {
  self->beginSelectTransitions(event);
}

//  void QStateMachine::endSelectTransitions(QEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QStateMachine20endSelectTransitionsEP6QEvent(
    QStateMachine *self,
    QEvent *event) {
  self->endSelectTransitions(event);
}

//  void QStateMachine::beginMicrostep(QEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QStateMachine14beginMicrostepEP6QEvent(
    QStateMachine *self,
    QEvent *event) {
  self->beginMicrostep(event);
}

//  void QStateMachine::endMicrostep(QEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QStateMachine12endMicrostepEP6QEvent(
    QStateMachine *self,
    QEvent *event) {
  self->endMicrostep(event);
}

//  bool QStateMachine::event(QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QStateMachine5eventEP6QEvent(
    QStateMachine *self,
    QEvent *e) {
  return self->event(e);
}

//  QStateMachine::QStateMachine(QStateMachinePrivate &dd, QObject *parent)
extern "C" Q_DECL_EXPORT
QStateMachine *ritual_ZN13QStateMachineC1ER20QStateMachinePrivateP7QObject(
    QStateMachinePrivate *dd,
    QObject *parent) {
  return new CuteQStateMachine(*dd, parent);
}

//  QStateMachinePrivate *QStateMachine::d_func()
extern "C" Q_DECL_EXPORT
QStateMachinePrivate *ritual_ZN13QStateMachine6d_funcEv(
    QStateMachine *self) {
  return self->d_func();
}

//  const QStateMachinePrivate *QStateMachine::d_func() const
extern "C" Q_DECL_EXPORT
const QStateMachinePrivate *ritual_ZNK13QStateMachine6d_funcEv(
    const QStateMachine *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQStateMachine, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QStateMachine(
    QStateMachine *self,
    const char *key,
    void *call) {
  return static_cast<CuteQStateMachine *>(self)->take(key, call);
}

//  bool QStateMachine::eventFilter(QObject *watched, QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN13QStateMachine11eventFilterEP7QObjectP6QEvent(
    QStateMachine *self,
    QObject *watched,
    QEvent *event) {
  return self->QStateMachine::eventFilter(watched, event);
}

//  void QStateMachine::onEntry(QEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QStateMachine7onEntryEP6QEvent(
    QStateMachine *self,
    QEvent *event) {
  static_cast<OwnQStateMachine *>(self)->OwnQStateMachine::onEntry(event);
}

//  void QStateMachine::onExit(QEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QStateMachine6onExitEP6QEvent(
    QStateMachine *self,
    QEvent *event) {
  static_cast<OwnQStateMachine *>(self)->OwnQStateMachine::onExit(event);
}

//  void QStateMachine::beginSelectTransitions(QEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QStateMachine22beginSelectTransitionsEP6QEvent(
    QStateMachine *self,
    QEvent *event) {
  static_cast<OwnQStateMachine *>(self)->OwnQStateMachine::beginSelectTransitions(
      event);
}

//  void QStateMachine::endSelectTransitions(QEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QStateMachine20endSelectTransitionsEP6QEvent(
    QStateMachine *self,
    QEvent *event) {
  static_cast<OwnQStateMachine *>(self)->OwnQStateMachine::endSelectTransitions(
      event);
}

//  void QStateMachine::beginMicrostep(QEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QStateMachine14beginMicrostepEP6QEvent(
    QStateMachine *self,
    QEvent *event) {
  static_cast<OwnQStateMachine *>(self)->OwnQStateMachine::beginMicrostep(
      event);
}

//  void QStateMachine::endMicrostep(QEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QStateMachine12endMicrostepEP6QEvent(
    QStateMachine *self,
    QEvent *event) {
  static_cast<OwnQStateMachine *>(self)->OwnQStateMachine::endMicrostep(
      event);
}

//  bool QStateMachine::event(QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN13QStateMachine5eventEP6QEvent(
    QStateMachine *self,
    QEvent *e) {
  return static_cast<OwnQStateMachine *>(self)->OwnQStateMachine::event(e);
}

//  a QBindable<QString> a ritual of QStateMachine gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QStateMachine__QBindable_QString(QBindable<QString> *self) {
  delete self;
}

//  a QBindable<bool> a ritual of QStateMachine gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QStateMachine__QBindable_bool(QBindable<bool> *self) {
  delete self;
}

//  a QBindable<QState::RestorePolicy> a ritual of QStateMachine gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QStateMachine__QBindable_QState_RestorePolicy(
    QBindable<QState::RestorePolicy> *self) {
  delete self;
}

//  a QSet<QAbstractState *> a ritual of QStateMachine gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QStateMachine__QSet_QAbstractState(
    QSet<QAbstractState *> *self) {
  delete self;
}
