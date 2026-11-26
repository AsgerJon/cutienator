//  Written by dev_tooling.RitualGenerator from the records of
//  QtStateMachine/qstate.h, Qt 6.12.0. Changes made here are lost.
#include <QtStateMachine/qstate.h>
#include <QtCore/qstring.h>
#include <QtStateMachine/qabstracttransition.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>
#include <QtCore/QBindable>
#include <QtStateMachine/QAbstractState>
#include <QtStateMachine/QState>

//  Only a class built on QState may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQState : QState {
  using QState::onEntry;
  using QState::onExit;
  using QState::event;
};

//  A QState that Python can take functions over in. Every QState
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQStateCall0)(const void *, QEvent *, int *);
typedef void (*CuteQStateCall1)(const void *, QEvent *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQStateCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQStateCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQStateCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQStateCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQStateCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQStateCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQStateCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQState : public QState {
public:
  using QState::QState;
  void *taken[9] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN14QAbstractState7onEntryEP6QEvent")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QAbstractState6onExitEP6QEvent")) {
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

  //  void QState::onEntry(QEvent *event)
  void onEntry(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQStateCall0 call = reinterpret_cast<CuteQStateCall0>(taken[0]);
      call(this, event, &handled);
      if (handled) return;
    }
    QState::onEntry(event);
  }

  //  void QState::onExit(QEvent *event)
  void onExit(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQStateCall1 call = reinterpret_cast<CuteQStateCall1>(taken[1]);
      call(this, event, &handled);
      if (handled) return;
    }
    QState::onExit(event);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QState::event(QEvent *e)
  bool event(QEvent *e) override {
    if (taken[2]) {
      int handled = 0;
      CuteQStateCall2 call = reinterpret_cast<CuteQStateCall2>(taken[2]);
      bool given = call(this, e, &handled);
      if (handled) return given;
    }
    return QState::event(e);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQStateCall3 call = reinterpret_cast<CuteQStateCall3>(taken[3]);
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
      CuteQStateCall4 call = reinterpret_cast<CuteQStateCall4>(taken[4]);
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
      CuteQStateCall5 call = reinterpret_cast<CuteQStateCall5>(taken[5]);
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
      CuteQStateCall6 call = reinterpret_cast<CuteQStateCall6>(taken[6]);
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
      CuteQStateCall7 call = reinterpret_cast<CuteQStateCall7>(taken[7]);
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
      CuteQStateCall8 call = reinterpret_cast<CuteQStateCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QState::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK6QState10metaObjectEv(const QState *self) {
  return self->metaObject();
}

//  void *QState::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN6QState11qt_metacastEPKc(QState *self, const char *a0) {
  return self->qt_metacast(a0);
}

//  int QState::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN6QState11qt_metacallEN11QMetaObject4CallEiPPv(
    QState *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QState::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN6QState2trEPKcS1_i(const char *s, const char *c, int n) {
  return new QString(QState::tr(s, c, n));
}

//  QState::QState(QState *parent)
extern "C" Q_DECL_EXPORT
QState *ritual_ZN6QStateC1EPS_(QState *parent) {
  return new CuteQState(parent);
}

//  QState::QState(ChildMode childMode, QState *parent)
extern "C" Q_DECL_EXPORT
QState *ritual_ZN6QStateC1ENS_9ChildModeEPS_(
    QState::ChildMode childMode,
    QState *parent) {
  return new CuteQState(childMode, parent);
}

//  QState::~QState()
extern "C" Q_DECL_EXPORT
void ritual_ZN6QStateD1Ev(QState *self) {
  delete self;
}

//  QAbstractState *QState::errorState() const
extern "C" Q_DECL_EXPORT
QAbstractState *ritual_ZNK6QState10errorStateEv(const QState *self) {
  return self->errorState();
}

//  void QState::setErrorState(QAbstractState *state)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QState13setErrorStateEP14QAbstractState(
    QState *self,
    QAbstractState *state) {
  self->setErrorState(state);
}

//  QBindable<QAbstractState *> QState::bindableErrorState()
extern "C" Q_DECL_EXPORT
QBindable<QAbstractState *> *ritual_ZN6QState18bindableErrorStateEv(
    QState *self) {
  return new QBindable<QAbstractState *>(self->bindableErrorState());
}

//  void QState::addTransition(QAbstractTransition *transition)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QState13addTransitionEP19QAbstractTransition(
    QState *self,
    QAbstractTransition *transition) {
  self->addTransition(transition);
}

//  QSignalTransition *QState::addTransition(const QObject *sender, const
//      char *signal, QAbstractState *target)
extern "C" Q_DECL_EXPORT
QSignalTransition *ritual_ZN6QState13addTransitionEPK7QObjectPKcP14QAbstractState(
    QState *self,
    const QObject *sender,
    const char *signal,
    QAbstractState *target) {
  return self->addTransition(sender, signal, target);
}

//  QAbstractTransition *QState::addTransition(QAbstractState *target)
extern "C" Q_DECL_EXPORT
QAbstractTransition *ritual_ZN6QState13addTransitionEP14QAbstractState(
    QState *self,
    QAbstractState *target) {
  return self->addTransition(target);
}

//  void QState::removeTransition(QAbstractTransition *transition)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QState16removeTransitionEP19QAbstractTransition(
    QState *self,
    QAbstractTransition *transition) {
  self->removeTransition(transition);
}

//  QList<QAbstractTransition *> QState::transitions() const
extern "C" Q_DECL_EXPORT
QList<QAbstractTransition *> *ritual_ZNK6QState11transitionsEv(
    const QState *self) {
  return new QList<QAbstractTransition *>(self->transitions());
}

//  QAbstractState *QState::initialState() const
extern "C" Q_DECL_EXPORT
QAbstractState *ritual_ZNK6QState12initialStateEv(const QState *self) {
  return self->initialState();
}

//  void QState::setInitialState(QAbstractState *state)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QState15setInitialStateEP14QAbstractState(
    QState *self,
    QAbstractState *state) {
  self->setInitialState(state);
}

//  QBindable<QAbstractState *> QState::bindableInitialState()
extern "C" Q_DECL_EXPORT
QBindable<QAbstractState *> *ritual_ZN6QState20bindableInitialStateEv(
    QState *self) {
  return new QBindable<QAbstractState *>(self->bindableInitialState());
}

//  ChildMode QState::childMode() const
extern "C" Q_DECL_EXPORT
QState::ChildMode ritual_ZNK6QState9childModeEv(const QState *self) {
  return self->childMode();
}

//  void QState::setChildMode(ChildMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QState12setChildModeENS_9ChildModeE(
    QState *self,
    QState::ChildMode mode) {
  self->setChildMode(mode);
}

//  QBindable<QState::ChildMode> QState::bindableChildMode()
extern "C" Q_DECL_EXPORT
QBindable<QState::ChildMode> *ritual_ZN6QState17bindableChildModeEv(
    QState *self) {
  return new QBindable<QState::ChildMode>(self->bindableChildMode());
}

#if !defined(QT_NO_PROPERTIES)
//  void QState::assignProperty(QObject *object, const char *name, const
//      QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QState14assignPropertyEP7QObjectPKcRK8QVariant(
    QState *self,
    QObject *object,
    const char *name,
    const QVariant *value) {
  self->assignProperty(object, name, *value);
}
#endif  // !defined(QT_NO_PROPERTIES)

//  void QState::finished(QPrivateSignal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QState8finishedENS_14QPrivateSignalE(QState *self) {
  self->finished(QState::QPrivateSignal());
}

//  void QState::propertiesAssigned(QPrivateSignal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QState18propertiesAssignedENS_14QPrivateSignalE(
    QState *self) {
  self->propertiesAssigned(QState::QPrivateSignal());
}

//  void QState::childModeChanged(QPrivateSignal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QState16childModeChangedENS_14QPrivateSignalE(QState *self) {
  self->childModeChanged(QState::QPrivateSignal());
}

//  void QState::initialStateChanged(QPrivateSignal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QState19initialStateChangedENS_14QPrivateSignalE(
    QState *self) {
  self->initialStateChanged(QState::QPrivateSignal());
}

//  void QState::errorStateChanged(QPrivateSignal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QState17errorStateChangedENS_14QPrivateSignalE(QState *self) {
  self->errorStateChanged(QState::QPrivateSignal());
}

//  void QState::onEntry(QEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QState7onEntryEP6QEvent(QState *self, QEvent *event) {
  self->onEntry(event);
}

//  void QState::onExit(QEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QState6onExitEP6QEvent(QState *self, QEvent *event) {
  self->onExit(event);
}

//  bool QState::event(QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QState5eventEP6QEvent(QState *self, QEvent *e) {
  return self->event(e);
}

//  QState::QState(QStatePrivate &dd, QState *parent)
extern "C" Q_DECL_EXPORT
QState *ritual_ZN6QStateC1ER13QStatePrivatePS_(
    QStatePrivate *dd,
    QState *parent) {
  return new CuteQState(*dd, parent);
}

//  QStatePrivate *QState::d_func()
extern "C" Q_DECL_EXPORT
QStatePrivate *ritual_ZN6QState6d_funcEv(QState *self) {
  return self->d_func();
}

//  const QStatePrivate *QState::d_func() const
extern "C" Q_DECL_EXPORT
const QStatePrivate *ritual_ZNK6QState6d_funcEv(const QState *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQState, for the function named by the
//      key
extern "C" Q_DECL_EXPORT
bool ritual_take_QState(QState *self, const char *key, void *call) {
  return static_cast<CuteQState *>(self)->take(key, call);
}

//  void QState::onEntry(QEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QState7onEntryEP6QEvent(QState *self, QEvent *event) {
  static_cast<OwnQState *>(self)->OwnQState::onEntry(event);
}

//  void QState::onExit(QEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QState6onExitEP6QEvent(QState *self, QEvent *event) {
  static_cast<OwnQState *>(self)->OwnQState::onExit(event);
}

//  bool QState::event(QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QState5eventEP6QEvent(QState *self, QEvent *e) {
  return static_cast<OwnQState *>(self)->OwnQState::event(e);
}

//  a QBindable<QAbstractState *> a ritual of QState gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QState__QBindable_QAbstractState(
    QBindable<QAbstractState *> *self) {
  delete self;
}

//  a QBindable<QState::ChildMode> a ritual of QState gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QState__QBindable_QState_ChildMode(
    QBindable<QState::ChildMode> *self) {
  delete self;
}
