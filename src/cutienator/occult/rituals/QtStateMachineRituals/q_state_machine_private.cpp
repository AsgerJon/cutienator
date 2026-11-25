//  Written by hand on 2026-11-25 from
//  QtStateMachine/6.12.0/QtStateMachine/private/qstatemachine_p.h,
//  Qt 6.12.0, as the Qt of macOS and of Windows install it, and that
//  of Linux alike. Kept as it is when the generator runs again.
//  Not written: 'removeConflictingTransitions', 'microstep',
//  'selectTransitions', 'computeExitSet', 'computeExitSet_Unordered',
//  'computeEntrySet' and 'getTransitionDomain', which take a
//  'CalculationCache *', a struct Qt's headers name and never write
//  out; and 'exitStates', 'enterStates', 'addDescendantStatesToEnter',
//  'addAncestorStatesToEnter', 'restorablesToPropertyList',
//  'computePendingRestorables', 'computePropertyAssignments',
//  'terminateActiveAnimations' and 'initializeAnimations', which take
//  or give a 'QSet' or a 'QHash'.
#include <QtStateMachine/qstatemachineglobal.h>
#include <QtStateMachine/6.12.0/QtStateMachine/private/qstatemachineglobal_p.h>
#if QT_CONFIG(statemachine)
#include <QtStateMachine/qstatemachine.h>
#include <QtStateMachine/6.12.0/QtStateMachine/private/qstatemachine_p.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qlist.h>
#include <QtCore/qvariant.h>
#include <cstring>

//  A QStateMachinePrivate that Python can take functions over in. Every
//  QStateMachinePrivate Python makes is one. Each function below asks the
//  Python function handed over for it, and runs Qt's own without
//  one.
typedef void (*CuteQStateMachinePrivateCall0)(const void *, int *);
typedef void (*CuteQStateMachinePrivateCall1)(const void *, bool, int *);
typedef void (*CuteQStateMachinePrivateCall2)(const void *, int *);
typedef void (*CuteQStateMachinePrivateCall3)(const void *, bool, int *);
typedef void (*CuteQStateMachinePrivateCall4)(const void *, int *);
typedef void (*CuteQStateMachinePrivateCall5)(const void *, QState *, QFinalState *, int *);
typedef void (*CuteQStateMachinePrivateCall6)(const void *, int *);
class CuteQStateMachinePrivate : public QStateMachinePrivate {
public:
  using QStateMachinePrivate::QStateMachinePrivate;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN20QStateMachinePrivate11noMicrostepEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QStateMachinePrivate22processedPendingEventsEb")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QStateMachinePrivate14beginMacrostepEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QStateMachinePrivate12endMacrostepEb")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QStateMachinePrivate15exitInterpreterEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QStateMachinePrivate17emitStateFinishedEP6QStateP11QFinalState")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QStateMachinePrivate11startupHookEv")) {
      taken[6] = call;
      return true;
    }
    return false;
  }

  //  void QStateMachinePrivate::noMicrostep()
  void noMicrostep() override {
    if (taken[0]) {
      int handled = 0;
      CuteQStateMachinePrivateCall0 call = reinterpret_cast<CuteQStateMachinePrivateCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QStateMachinePrivate::noMicrostep();
  }

  //  void QStateMachinePrivate::processedPendingEvents(bool didChange)
  void processedPendingEvents(bool didChange) override {
    if (taken[1]) {
      int handled = 0;
      CuteQStateMachinePrivateCall1 call = reinterpret_cast<CuteQStateMachinePrivateCall1>(taken[1]);
      call(this, didChange, &handled);
      if (handled) return;
    }
    QStateMachinePrivate::processedPendingEvents(didChange);
  }

  //  void QStateMachinePrivate::beginMacrostep()
  void beginMacrostep() override {
    if (taken[2]) {
      int handled = 0;
      CuteQStateMachinePrivateCall2 call = reinterpret_cast<CuteQStateMachinePrivateCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QStateMachinePrivate::beginMacrostep();
  }

  //  void QStateMachinePrivate::endMacrostep(bool didChange)
  void endMacrostep(bool didChange) override {
    if (taken[3]) {
      int handled = 0;
      CuteQStateMachinePrivateCall3 call = reinterpret_cast<CuteQStateMachinePrivateCall3>(taken[3]);
      call(this, didChange, &handled);
      if (handled) return;
    }
    QStateMachinePrivate::endMacrostep(didChange);
  }

  //  void QStateMachinePrivate::exitInterpreter()
  void exitInterpreter() override {
    if (taken[4]) {
      int handled = 0;
      CuteQStateMachinePrivateCall4 call = reinterpret_cast<CuteQStateMachinePrivateCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QStateMachinePrivate::exitInterpreter();
  }

  //  void QStateMachinePrivate::emitStateFinished(QState *forState,
  //      QFinalState *guiltyState)
  void emitStateFinished(QState *forState, QFinalState *guiltyState) override {
    if (taken[5]) {
      int handled = 0;
      CuteQStateMachinePrivateCall5 call = reinterpret_cast<CuteQStateMachinePrivateCall5>(taken[5]);
      call(this, forState, guiltyState, &handled);
      if (handled) return;
    }
    QStateMachinePrivate::emitStateFinished(forState, guiltyState);
  }

  //  void QStateMachinePrivate::startupHook()
  void startupHook() override {
    if (taken[6]) {
      int handled = 0;
      CuteQStateMachinePrivateCall6 call = reinterpret_cast<CuteQStateMachinePrivateCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QStateMachinePrivate::startupHook();
  }
};

//  QStateMachinePrivate::QStateMachinePrivate()
extern "C" Q_DECL_EXPORT
QStateMachinePrivate *ritual_ZN20QStateMachinePrivateC1Ev() {
  return new CuteQStateMachinePrivate();
}

//  QStateMachinePrivate::~QStateMachinePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QStateMachinePrivateD1Ev(QStateMachinePrivate *self) {
  delete self;
}

//  QStateMachinePrivate *QStateMachinePrivate::get(QStateMachine *q)
extern "C" Q_DECL_EXPORT
QStateMachinePrivate *ritual_ZN20QStateMachinePrivate3getEP13QStateMachine(
    QStateMachine *q) {
  return QStateMachinePrivate::get(q);
}

//  QState *QStateMachinePrivate::findLCA(const QList<QAbstractState *>
//      &states, bool onlyCompound)
extern "C" Q_DECL_EXPORT
QState *ritual_ZN20QStateMachinePrivate7findLCAERK5QListIP14QAbstractStateEb(
    QStateMachinePrivate *self,
    const QList<QAbstractState *> *states,
    bool onlyCompound) {
  return self->findLCA(*states, onlyCompound);
}

//  QState *QStateMachinePrivate::findLCCA(const QList<QAbstractState *>
//      &states)
extern "C" Q_DECL_EXPORT
QState *ritual_ZN20QStateMachinePrivate8findLCCAERK5QListIP14QAbstractStateE(
    QStateMachinePrivate *self,
    const QList<QAbstractState *> *states) {
  return self->findLCCA(*states);
}

//  bool
//      QStateMachinePrivate::transitionStateEntryLessThan(QAbstractTransitio
//      n *t1, QAbstractTransition *t2)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QStateMachinePrivate28transitionStateEntryLessThanEP19QAbstractTransitionS1_(
    QAbstractTransition *t1,
    QAbstractTransition *t2) {
  return QStateMachinePrivate::transitionStateEntryLessThan(t1, t2);
}

//  bool QStateMachinePrivate::stateEntryLessThan(QAbstractState *s1,
//      QAbstractState *s2)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QStateMachinePrivate18stateEntryLessThanEP14QAbstractStateS1_(
    QAbstractState *s1,
    QAbstractState *s2) {
  return QStateMachinePrivate::stateEntryLessThan(s1, s2);
}

//  bool QStateMachinePrivate::stateExitLessThan(QAbstractState *s1,
//      QAbstractState *s2)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QStateMachinePrivate17stateExitLessThanEP14QAbstractStateS1_(
    QAbstractState *s1,
    QAbstractState *s2) {
  return QStateMachinePrivate::stateExitLessThan(s1, s2);
}

//  QAbstractState *QStateMachinePrivate::findErrorState(QAbstractState
//      *context)
extern "C" Q_DECL_EXPORT
QAbstractState *ritual_ZN20QStateMachinePrivate14findErrorStateEP14QAbstractState(
    QStateMachinePrivate *self,
    QAbstractState *context) {
  return self->findErrorState(context);
}

//  void QStateMachinePrivate::setError(QStateMachine::Error error,
//      QAbstractState *currentContext)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QStateMachinePrivate8setErrorEN13QStateMachine5ErrorEP14QAbstractState(
    QStateMachinePrivate *self,
    QStateMachine::Error error,
    QAbstractState *currentContext) {
  self->setError(error, currentContext);
}

//  void QStateMachinePrivate::_q_start()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QStateMachinePrivate8_q_startEv(QStateMachinePrivate *self) {
  self->_q_start();
}

//  void QStateMachinePrivate::_q_process()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QStateMachinePrivate10_q_processEv(
    QStateMachinePrivate *self) {
  self->_q_process();
}

#if QT_CONFIG(animation)
//  void QStateMachinePrivate::_q_animationFinished()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QStateMachinePrivate20_q_animationFinishedEv(
    QStateMachinePrivate *self) {
  self->_q_animationFinished();
}
#endif  // QT_CONFIG(animation)

//  void QStateMachinePrivate::_q_startDelayedEventTimer(int id, int delay)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QStateMachinePrivate25_q_startDelayedEventTimerEii(
    QStateMachinePrivate *self,
    int id,
    int delay) {
  self->_q_startDelayedEventTimer(id, delay);
}

//  void QStateMachinePrivate::_q_killDelayedEventTimer(int id, int timerId)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QStateMachinePrivate24_q_killDelayedEventTimerEii(
    QStateMachinePrivate *self,
    int id,
    int timerId) {
  self->_q_killDelayedEventTimer(id, timerId);
}

//  QState *QStateMachinePrivate::rootState() const
extern "C" Q_DECL_EXPORT
QState *ritual_ZNK20QStateMachinePrivate9rootStateEv(
    const QStateMachinePrivate *self) {
  return self->rootState();
}

//  void QStateMachinePrivate::clearHistory()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QStateMachinePrivate12clearHistoryEv(
    QStateMachinePrivate *self) {
  self->clearHistory();
}

//  QAbstractTransition *QStateMachinePrivate::createInitialTransition()
//      const
extern "C" Q_DECL_EXPORT
QAbstractTransition *ritual_ZNK20QStateMachinePrivate23createInitialTransitionEv(
    const QStateMachinePrivate *self) {
  return self->createInitialTransition();
}

//  void QStateMachinePrivate::noMicrostep()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QStateMachinePrivate11noMicrostepEv(
    QStateMachinePrivate *self) {
  self->noMicrostep();
}

//  void QStateMachinePrivate::processedPendingEvents(bool didChange)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QStateMachinePrivate22processedPendingEventsEb(
    QStateMachinePrivate *self,
    bool didChange) {
  self->processedPendingEvents(didChange);
}

//  void QStateMachinePrivate::beginMacrostep()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QStateMachinePrivate14beginMacrostepEv(
    QStateMachinePrivate *self) {
  self->beginMacrostep();
}

//  void QStateMachinePrivate::endMacrostep(bool didChange)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QStateMachinePrivate12endMacrostepEb(
    QStateMachinePrivate *self,
    bool didChange) {
  self->endMacrostep(didChange);
}

//  void QStateMachinePrivate::exitInterpreter()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QStateMachinePrivate15exitInterpreterEv(
    QStateMachinePrivate *self) {
  self->exitInterpreter();
}

//  void QStateMachinePrivate::executeTransitionContent(QEvent *event, const
//      QList<QAbstractTransition *> &transitionList)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QStateMachinePrivate24executeTransitionContentEP6QEventRK5QListIP19QAbstractTransitionE(
    QStateMachinePrivate *self,
    QEvent *event,
    const QList<QAbstractTransition *> *transitionList) {
  self->executeTransitionContent(event, *transitionList);
}

//  QState *QStateMachinePrivate::toStandardState(QAbstractState *state)
extern "C" Q_DECL_EXPORT
QState *ritual_ZN20QStateMachinePrivate15toStandardStateEP14QAbstractState(
    QAbstractState *state) {
  return QStateMachinePrivate::toStandardState(state);
}

//  const QState *QStateMachinePrivate::toStandardState(const QAbstractState
//      *state)
extern "C" Q_DECL_EXPORT
const QState *ritual_ZN20QStateMachinePrivate15toStandardStateEPK14QAbstractState(
    const QAbstractState *state) {
  return QStateMachinePrivate::toStandardState(state);
}

//  QFinalState *QStateMachinePrivate::toFinalState(QAbstractState *state)
extern "C" Q_DECL_EXPORT
QFinalState *ritual_ZN20QStateMachinePrivate12toFinalStateEP14QAbstractState(
    QAbstractState *state) {
  return QStateMachinePrivate::toFinalState(state);
}

//  QHistoryState *QStateMachinePrivate::toHistoryState(QAbstractState
//      *state)
extern "C" Q_DECL_EXPORT
QHistoryState *ritual_ZN20QStateMachinePrivate14toHistoryStateEP14QAbstractState(
    QAbstractState *state) {
  return QStateMachinePrivate::toHistoryState(state);
}

//  bool QStateMachinePrivate::isInFinalState(QAbstractState *s) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QStateMachinePrivate14isInFinalStateEP14QAbstractState(
    const QStateMachinePrivate *self,
    QAbstractState *s) {
  return self->isInFinalState(s);
}

//  bool QStateMachinePrivate::isFinal(const QAbstractState *s)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QStateMachinePrivate7isFinalEPK14QAbstractState(
    const QAbstractState *s) {
  return QStateMachinePrivate::isFinal(s);
}

//  bool QStateMachinePrivate::isParallel(const QAbstractState *s)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QStateMachinePrivate10isParallelEPK14QAbstractState(
    const QAbstractState *s) {
  return QStateMachinePrivate::isParallel(s);
}

//  bool QStateMachinePrivate::isCompound(const QAbstractState *s) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QStateMachinePrivate10isCompoundEPK14QAbstractState(
    const QStateMachinePrivate *self,
    const QAbstractState *s) {
  return self->isCompound(s);
}

//  bool QStateMachinePrivate::isAtomic(const QAbstractState *s) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QStateMachinePrivate8isAtomicEPK14QAbstractState(
    const QStateMachinePrivate *self,
    const QAbstractState *s) {
  return self->isAtomic(s);
}

//  void QStateMachinePrivate::goToState(QAbstractState *targetState)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QStateMachinePrivate9goToStateEP14QAbstractState(
    QStateMachinePrivate *self,
    QAbstractState *targetState) {
  self->goToState(targetState);
}

//  void QStateMachinePrivate::registerTransitions(QAbstractState *state)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QStateMachinePrivate19registerTransitionsEP14QAbstractState(
    QStateMachinePrivate *self,
    QAbstractState *state) {
  self->registerTransitions(state);
}

//  void QStateMachinePrivate::maybeRegisterTransition(QAbstractTransition
//      *transition)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QStateMachinePrivate23maybeRegisterTransitionEP19QAbstractTransition(
    QStateMachinePrivate *self,
    QAbstractTransition *transition) {
  self->maybeRegisterTransition(transition);
}

//  void QStateMachinePrivate::registerTransition(QAbstractTransition
//      *transition)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QStateMachinePrivate18registerTransitionEP19QAbstractTransition(
    QStateMachinePrivate *self,
    QAbstractTransition *transition) {
  self->registerTransition(transition);
}

//  void
//      QStateMachinePrivate::maybeRegisterSignalTransition(QSignalTransition
//      *transition)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QStateMachinePrivate29maybeRegisterSignalTransitionEP17QSignalTransition(
    QStateMachinePrivate *self,
    QSignalTransition *transition) {
  self->maybeRegisterSignalTransition(transition);
}

//  void QStateMachinePrivate::registerSignalTransition(QSignalTransition
//      *transition)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QStateMachinePrivate24registerSignalTransitionEP17QSignalTransition(
    QStateMachinePrivate *self,
    QSignalTransition *transition) {
  self->registerSignalTransition(transition);
}

//  void QStateMachinePrivate::unregisterSignalTransition(QSignalTransition
//      *transition)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QStateMachinePrivate26unregisterSignalTransitionEP17QSignalTransition(
    QStateMachinePrivate *self,
    QSignalTransition *transition) {
  self->unregisterSignalTransition(transition);
}

//  void QStateMachinePrivate::registerMultiThreadedSignalTransitions()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QStateMachinePrivate38registerMultiThreadedSignalTransitionsEv(
    QStateMachinePrivate *self) {
  self->registerMultiThreadedSignalTransitions();
}

#if QT_CONFIG(qeventtransition)
//  void QStateMachinePrivate::maybeRegisterEventTransition(QEventTransition
//      *transition)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QStateMachinePrivate28maybeRegisterEventTransitionEP16QEventTransition(
    QStateMachinePrivate *self,
    QEventTransition *transition) {
  self->maybeRegisterEventTransition(transition);
}
#endif  // QT_CONFIG(qeventtransition)

#if QT_CONFIG(qeventtransition)
//  void QStateMachinePrivate::registerEventTransition(QEventTransition
//      *transition)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QStateMachinePrivate23registerEventTransitionEP16QEventTransition(
    QStateMachinePrivate *self,
    QEventTransition *transition) {
  self->registerEventTransition(transition);
}
#endif  // QT_CONFIG(qeventtransition)

#if QT_CONFIG(qeventtransition)
//  void QStateMachinePrivate::unregisterEventTransition(QEventTransition
//      *transition)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QStateMachinePrivate25unregisterEventTransitionEP16QEventTransition(
    QStateMachinePrivate *self,
    QEventTransition *transition) {
  self->unregisterEventTransition(transition);
}
#endif  // QT_CONFIG(qeventtransition)

#if QT_CONFIG(qeventtransition)
//  void QStateMachinePrivate::handleFilteredEvent(QObject *watched, QEvent
//      *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QStateMachinePrivate19handleFilteredEventEP7QObjectP6QEvent(
    QStateMachinePrivate *self,
    QObject *watched,
    QEvent *event) {
  self->handleFilteredEvent(watched, event);
}
#endif  // QT_CONFIG(qeventtransition)

//  void QStateMachinePrivate::unregisterTransition(QAbstractTransition
//      *transition)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QStateMachinePrivate20unregisterTransitionEP19QAbstractTransition(
    QStateMachinePrivate *self,
    QAbstractTransition *transition) {
  self->unregisterTransition(transition);
}

//  void QStateMachinePrivate::unregisterAllTransitions()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QStateMachinePrivate24unregisterAllTransitionsEv(
    QStateMachinePrivate *self) {
  self->unregisterAllTransitions();
}

//  void QStateMachinePrivate::handleTransitionSignal(QObject *sender, int
//      signalIndex, void **args)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QStateMachinePrivate22handleTransitionSignalEP7QObjectiPPv(
    QStateMachinePrivate *self,
    QObject *sender,
    int signalIndex,
    void **args) {
  self->handleTransitionSignal(sender, signalIndex, args);
}

//  void QStateMachinePrivate::postInternalEvent(QEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QStateMachinePrivate17postInternalEventEP6QEvent(
    QStateMachinePrivate *self,
    QEvent *e) {
  self->postInternalEvent(e);
}

//  void QStateMachinePrivate::postExternalEvent(QEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QStateMachinePrivate17postExternalEventEP6QEvent(
    QStateMachinePrivate *self,
    QEvent *e) {
  self->postExternalEvent(e);
}

//  QEvent *QStateMachinePrivate::dequeueInternalEvent()
extern "C" Q_DECL_EXPORT
QEvent *ritual_ZN20QStateMachinePrivate20dequeueInternalEventEv(
    QStateMachinePrivate *self) {
  return self->dequeueInternalEvent();
}

//  QEvent *QStateMachinePrivate::dequeueExternalEvent()
extern "C" Q_DECL_EXPORT
QEvent *ritual_ZN20QStateMachinePrivate20dequeueExternalEventEv(
    QStateMachinePrivate *self) {
  return self->dequeueExternalEvent();
}

//  bool QStateMachinePrivate::isInternalEventQueueEmpty()
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QStateMachinePrivate25isInternalEventQueueEmptyEv(
    QStateMachinePrivate *self) {
  return self->isInternalEventQueueEmpty();
}

//  bool QStateMachinePrivate::isExternalEventQueueEmpty()
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QStateMachinePrivate25isExternalEventQueueEmptyEv(
    QStateMachinePrivate *self) {
  return self->isExternalEventQueueEmpty();
}

//  void QStateMachinePrivate::processEvents(QStateMachinePrivate::EventProce
//      ssingMode processingMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QStateMachinePrivate13processEventsENS_19EventProcessingModeE(
    QStateMachinePrivate *self,
    QStateMachinePrivate::EventProcessingMode processingMode) {
  self->processEvents(processingMode);
}

//  void QStateMachinePrivate::cancelAllDelayedEvents()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QStateMachinePrivate22cancelAllDelayedEventsEv(
    QStateMachinePrivate *self) {
  self->cancelAllDelayedEvents();
}

//  void QStateMachinePrivate::emitStateFinished(QState *forState,
//      QFinalState *guiltyState)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QStateMachinePrivate17emitStateFinishedEP6QStateP11QFinalState(
    QStateMachinePrivate *self,
    QState *forState,
    QFinalState *guiltyState) {
  self->emitStateFinished(forState, guiltyState);
}

//  void QStateMachinePrivate::startupHook()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QStateMachinePrivate11startupHookEv(
    QStateMachinePrivate *self) {
  self->startupHook();
}

#if !defined(QT_NO_PROPERTIES)
//  bool QStateMachinePrivate::hasRestorable(QAbstractState *state, QObject
//      *object, const QByteArray &propertyName) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QStateMachinePrivate13hasRestorableEP14QAbstractStateP7QObjectRK10QByteArray(
    const QStateMachinePrivate *self,
    QAbstractState *state,
    QObject *object,
    const QByteArray *propertyName) {
  return self->hasRestorable(state, object, *propertyName);
}
#endif  // !defined(QT_NO_PROPERTIES)

#if !defined(QT_NO_PROPERTIES)
//  QVariant QStateMachinePrivate::savedValueForRestorable(const
//      QList<QAbstractState *> &exitedStates_sorted, QObject *object, const
//      QByteArray &propertyName) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK20QStateMachinePrivate23savedValueForRestorableERK5QListIP14QAbstractStateEP7QObjectRK10QByteArray(
    const QStateMachinePrivate *self,
    const QList<QAbstractState *> *exitedStates_sorted,
    QObject *object,
    const QByteArray *propertyName) {
  return new QVariant(self->savedValueForRestorable(
      *exitedStates_sorted, object, *propertyName));
}
#endif  // !defined(QT_NO_PROPERTIES)

#if !defined(QT_NO_PROPERTIES)
//  void QStateMachinePrivate::registerRestorable(QAbstractState *state,
//      QObject *object, const QByteArray &propertyName, const QVariant
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QStateMachinePrivate18registerRestorableEP14QAbstractStateP7QObjectRK10QByteArrayRK8QVariant(
    QStateMachinePrivate *self,
    QAbstractState *state,
    QObject *object,
    const QByteArray *propertyName,
    const QVariant *value) {
  self->registerRestorable(state, object, *propertyName, *value);
}
#endif  // !defined(QT_NO_PROPERTIES)

#if !defined(QT_NO_PROPERTIES)
//  void QStateMachinePrivate::unregisterRestorables(const
//      QList<QAbstractState *> &states, QObject *object, const QByteArray
//      &propertyName)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QStateMachinePrivate21unregisterRestorablesERK5QListIP14QAbstractStateEP7QObjectRK10QByteArray(
    QStateMachinePrivate *self,
    const QList<QAbstractState *> *states,
    QObject *object,
    const QByteArray *propertyName) {
  self->unregisterRestorables(*states, object, *propertyName);
}
#endif  // !defined(QT_NO_PROPERTIES)

#if QT_CONFIG(animation)
//  InitializeAnimationResult
//      QStateMachinePrivate::initializeAnimation(QAbstractAnimation
//      *abstractAnimation, const QPropertyAssignment &prop)
extern "C" Q_DECL_EXPORT
QStateMachinePrivate::InitializeAnimationResult *ritual_ZN20QStateMachinePrivate19initializeAnimationEP18QAbstractAnimationRK19QPropertyAssignment(
    QStateMachinePrivate *self,
    QAbstractAnimation *abstractAnimation,
    const QPropertyAssignment *prop) {
  return new QStateMachinePrivate::InitializeAnimationResult(
      self->initializeAnimation(abstractAnimation, *prop));
}
#endif  // QT_CONFIG(animation)

#if QT_CONFIG(animation)
//  QList<QAbstractAnimation *> QStateMachinePrivate::selectAnimations(const
//      QList<QAbstractTransition *> &transitionList) const
extern "C" Q_DECL_EXPORT
QList<QAbstractAnimation *> *ritual_ZNK20QStateMachinePrivate16selectAnimationsERK5QListIP19QAbstractTransitionE(
    const QStateMachinePrivate *self,
    const QList<QAbstractTransition *> *transitionList) {
  return new QList<QAbstractAnimation *>(
      self->selectAnimations(*transitionList));
}
#endif  // QT_CONFIG(animation)

//  QStateMachine *QStateMachinePrivate::q_func()
extern "C" Q_DECL_EXPORT
QStateMachine *ritual_ZN20QStateMachinePrivate6q_funcEv(
    QStateMachinePrivate *self) {
  return self->q_func();
}

//  const QStateMachine *QStateMachinePrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QStateMachine *ritual_ZNK20QStateMachinePrivate6q_funcEv(
    const QStateMachinePrivate *self) {
  return self->q_func();
}

//  a Python function taken by a CuteQStateMachinePrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QStateMachinePrivate(
    QStateMachinePrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQStateMachinePrivate *>(self)->take(key, call);
}

//  void QStateMachinePrivate::noMicrostep()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QStateMachinePrivate11noMicrostepEv(
    QStateMachinePrivate *self) {
  self->QStateMachinePrivate::noMicrostep();
}

//  void QStateMachinePrivate::processedPendingEvents(bool didChange)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QStateMachinePrivate22processedPendingEventsEb(
    QStateMachinePrivate *self,
    bool didChange) {
  self->QStateMachinePrivate::processedPendingEvents(didChange);
}

//  void QStateMachinePrivate::beginMacrostep()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QStateMachinePrivate14beginMacrostepEv(
    QStateMachinePrivate *self) {
  self->QStateMachinePrivate::beginMacrostep();
}

//  void QStateMachinePrivate::endMacrostep(bool didChange)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QStateMachinePrivate12endMacrostepEb(
    QStateMachinePrivate *self,
    bool didChange) {
  self->QStateMachinePrivate::endMacrostep(didChange);
}

//  void QStateMachinePrivate::exitInterpreter()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QStateMachinePrivate15exitInterpreterEv(
    QStateMachinePrivate *self) {
  self->QStateMachinePrivate::exitInterpreter();
}

//  void QStateMachinePrivate::emitStateFinished(QState *forState,
//      QFinalState *guiltyState)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QStateMachinePrivate17emitStateFinishedEP6QStateP11QFinalState(
    QStateMachinePrivate *self,
    QState *forState,
    QFinalState *guiltyState) {
  self->QStateMachinePrivate::emitStateFinished(forState, guiltyState);
}

//  void QStateMachinePrivate::startupHook()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QStateMachinePrivate11startupHookEv(
    QStateMachinePrivate *self) {
  self->QStateMachinePrivate::startupHook();
}

#endif  // QT_CONFIG(statemachine)
