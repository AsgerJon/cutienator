//  Written by dev_tooling.RitualGenerator from the records of
//  QtStateMachine/qhistorystate.h, Qt 6.12.0. Changes made here are lost.
#include <QtStateMachine/qhistorystate.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QHistoryState may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQHistoryState : QHistoryState {
  using QHistoryState::onEntry;
  using QHistoryState::onExit;
  using QHistoryState::event;
};

//  A QHistoryState that Python can take functions over in. Every QHistoryState
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQHistoryStateCall0)(const void *, QEvent *, int *);
typedef void (*CuteQHistoryStateCall1)(const void *, QEvent *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQHistoryStateCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQHistoryStateCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHistoryStateCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHistoryStateCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHistoryStateCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHistoryStateCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHistoryStateCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQHistoryState : public QHistoryState {
public:
  using QHistoryState::QHistoryState;
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

  //  void QHistoryState::onEntry(QEvent *event)
  void onEntry(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQHistoryStateCall0 call = reinterpret_cast<CuteQHistoryStateCall0>(taken[0]);
      call(this, event, &handled);
      if (handled) return;
    }
    QHistoryState::onEntry(event);
  }

  //  void QHistoryState::onExit(QEvent *event)
  void onExit(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQHistoryStateCall1 call = reinterpret_cast<CuteQHistoryStateCall1>(taken[1]);
      call(this, event, &handled);
      if (handled) return;
    }
    QHistoryState::onExit(event);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QHistoryState::event(QEvent *e)
  bool event(QEvent *e) override {
    if (taken[2]) {
      int handled = 0;
      CuteQHistoryStateCall2 call = reinterpret_cast<CuteQHistoryStateCall2>(taken[2]);
      bool given = call(this, e, &handled);
      if (handled) return given;
    }
    return QHistoryState::event(e);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQHistoryStateCall3 call = reinterpret_cast<CuteQHistoryStateCall3>(taken[3]);
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
      CuteQHistoryStateCall4 call = reinterpret_cast<CuteQHistoryStateCall4>(taken[4]);
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
      CuteQHistoryStateCall5 call = reinterpret_cast<CuteQHistoryStateCall5>(taken[5]);
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
      CuteQHistoryStateCall6 call = reinterpret_cast<CuteQHistoryStateCall6>(taken[6]);
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
      CuteQHistoryStateCall7 call = reinterpret_cast<CuteQHistoryStateCall7>(taken[7]);
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
      CuteQHistoryStateCall8 call = reinterpret_cast<CuteQHistoryStateCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QHistoryState::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13QHistoryState10metaObjectEv(
    const QHistoryState *self) {
  return self->metaObject();
}

//  QString QHistoryState::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13QHistoryState2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QHistoryState::tr(s, c, n));
}

//  QHistoryState::QHistoryState(QState *parent)
extern "C" Q_DECL_EXPORT
QHistoryState *ritual_ZN13QHistoryStateC1EP6QState(QState *parent) {
  return new CuteQHistoryState(parent);
}

//  QHistoryState::QHistoryState(HistoryType type, QState *parent)
extern "C" Q_DECL_EXPORT
QHistoryState *ritual_ZN13QHistoryStateC1ENS_11HistoryTypeEP6QState(
    QHistoryState::HistoryType type,
    QState *parent) {
  return new CuteQHistoryState(type, parent);
}

//  QHistoryState::~QHistoryState()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QHistoryStateD1Ev(QHistoryState *self) {
  delete self;
}

//  QAbstractTransition *QHistoryState::defaultTransition() const
extern "C" Q_DECL_EXPORT
QAbstractTransition *ritual_ZNK13QHistoryState17defaultTransitionEv(
    const QHistoryState *self) {
  return self->defaultTransition();
}

//  void QHistoryState::setDefaultTransition(QAbstractTransition *transition)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QHistoryState20setDefaultTransitionEP19QAbstractTransition(
    QHistoryState *self,
    QAbstractTransition *transition) {
  self->setDefaultTransition(transition);
}

//  QAbstractState *QHistoryState::defaultState() const
extern "C" Q_DECL_EXPORT
QAbstractState *ritual_ZNK13QHistoryState12defaultStateEv(
    const QHistoryState *self) {
  return self->defaultState();
}

//  void QHistoryState::setDefaultState(QAbstractState *state)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QHistoryState15setDefaultStateEP14QAbstractState(
    QHistoryState *self,
    QAbstractState *state) {
  self->setDefaultState(state);
}

//  HistoryType QHistoryState::historyType() const
extern "C" Q_DECL_EXPORT
QHistoryState::HistoryType ritual_ZNK13QHistoryState11historyTypeEv(
    const QHistoryState *self) {
  return self->historyType();
}

//  void QHistoryState::setHistoryType(HistoryType type)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QHistoryState14setHistoryTypeENS_11HistoryTypeE(
    QHistoryState *self,
    QHistoryState::HistoryType type) {
  self->setHistoryType(type);
}

//  void QHistoryState::onEntry(QEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QHistoryState7onEntryEP6QEvent(
    QHistoryState *self,
    QEvent *event) {
  self->onEntry(event);
}

//  void QHistoryState::onExit(QEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QHistoryState6onExitEP6QEvent(
    QHistoryState *self,
    QEvent *event) {
  self->onExit(event);
}

//  bool QHistoryState::event(QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QHistoryState5eventEP6QEvent(
    QHistoryState *self,
    QEvent *e) {
  return self->event(e);
}

//  a Python function taken by a CuteQHistoryState, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QHistoryState(
    QHistoryState *self,
    const char *key,
    void *call) {
  return static_cast<CuteQHistoryState *>(self)->take(key, call);
}

//  void QHistoryState::onEntry(QEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QHistoryState7onEntryEP6QEvent(
    QHistoryState *self,
    QEvent *event) {
  static_cast<OwnQHistoryState *>(self)->OwnQHistoryState::onEntry(event);
}

//  void QHistoryState::onExit(QEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QHistoryState6onExitEP6QEvent(
    QHistoryState *self,
    QEvent *event) {
  static_cast<OwnQHistoryState *>(self)->OwnQHistoryState::onExit(event);
}

//  bool QHistoryState::event(QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN13QHistoryState5eventEP6QEvent(
    QHistoryState *self,
    QEvent *e) {
  return static_cast<OwnQHistoryState *>(self)->OwnQHistoryState::event(e);
}
