//  Written by dev_tooling.RitualGenerator from the records of
//  QtStateMachine/qfinalstate.h, Qt 6.12.0. Changes made here are lost.
#include <QtStateMachine/qfinalstate.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QFinalState may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQFinalState : QFinalState {
  using QFinalState::onEntry;
  using QFinalState::onExit;
  using QFinalState::event;
};

//  A QFinalState that Python can take functions over in. Every QFinalState
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQFinalStateCall0)(const void *, QEvent *, int *);
typedef void (*CuteQFinalStateCall1)(const void *, QEvent *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQFinalStateCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQFinalStateCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQFinalStateCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQFinalStateCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQFinalStateCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQFinalStateCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQFinalStateCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQFinalState : public QFinalState {
public:
  using QFinalState::QFinalState;
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

  //  void QFinalState::onEntry(QEvent *event)
  void onEntry(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQFinalStateCall0 call = reinterpret_cast<CuteQFinalStateCall0>(taken[0]);
      call(this, event, &handled);
      if (handled) return;
    }
    QFinalState::onEntry(event);
  }

  //  void QFinalState::onExit(QEvent *event)
  void onExit(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQFinalStateCall1 call = reinterpret_cast<CuteQFinalStateCall1>(taken[1]);
      call(this, event, &handled);
      if (handled) return;
    }
    QFinalState::onExit(event);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QFinalState::event(QEvent *e)
  bool event(QEvent *e) override {
    if (taken[2]) {
      int handled = 0;
      CuteQFinalStateCall2 call = reinterpret_cast<CuteQFinalStateCall2>(taken[2]);
      bool given = call(this, e, &handled);
      if (handled) return given;
    }
    return QFinalState::event(e);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQFinalStateCall3 call = reinterpret_cast<CuteQFinalStateCall3>(taken[3]);
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
      CuteQFinalStateCall4 call = reinterpret_cast<CuteQFinalStateCall4>(taken[4]);
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
      CuteQFinalStateCall5 call = reinterpret_cast<CuteQFinalStateCall5>(taken[5]);
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
      CuteQFinalStateCall6 call = reinterpret_cast<CuteQFinalStateCall6>(taken[6]);
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
      CuteQFinalStateCall7 call = reinterpret_cast<CuteQFinalStateCall7>(taken[7]);
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
      CuteQFinalStateCall8 call = reinterpret_cast<CuteQFinalStateCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QFinalState::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK11QFinalState10metaObjectEv(
    const QFinalState *self) {
  return self->metaObject();
}

//  QString QFinalState::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11QFinalState2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QFinalState::tr(s, c, n));
}

//  QFinalState::QFinalState(QState *parent)
extern "C" Q_DECL_EXPORT
QFinalState *ritual_ZN11QFinalStateC1EP6QState(QState *parent) {
  return new CuteQFinalState(parent);
}

//  QFinalState::~QFinalState()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFinalStateD1Ev(QFinalState *self) {
  delete self;
}

//  void QFinalState::onEntry(QEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFinalState7onEntryEP6QEvent(
    QFinalState *self,
    QEvent *event) {
  self->onEntry(event);
}

//  void QFinalState::onExit(QEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFinalState6onExitEP6QEvent(
    QFinalState *self,
    QEvent *event) {
  self->onExit(event);
}

//  bool QFinalState::event(QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QFinalState5eventEP6QEvent(QFinalState *self, QEvent *e) {
  return self->event(e);
}

//  a Python function taken by a CuteQFinalState, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QFinalState(
    QFinalState *self,
    const char *key,
    void *call) {
  return static_cast<CuteQFinalState *>(self)->take(key, call);
}

//  void QFinalState::onEntry(QEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QFinalState7onEntryEP6QEvent(
    QFinalState *self,
    QEvent *event) {
  static_cast<OwnQFinalState *>(self)->OwnQFinalState::onEntry(event);
}

//  void QFinalState::onExit(QEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QFinalState6onExitEP6QEvent(
    QFinalState *self,
    QEvent *event) {
  static_cast<OwnQFinalState *>(self)->OwnQFinalState::onExit(event);
}

//  bool QFinalState::event(QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN11QFinalState5eventEP6QEvent(
    QFinalState *self,
    QEvent *e) {
  return static_cast<OwnQFinalState *>(self)->OwnQFinalState::event(e);
}
