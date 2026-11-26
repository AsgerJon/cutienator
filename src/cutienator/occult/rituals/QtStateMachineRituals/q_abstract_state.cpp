//  Written by dev_tooling.RitualGenerator from the records of
//  QtStateMachine/qabstractstate.h, Qt 6.12.0. Changes made here are lost.
#include <QtStateMachine/qabstractstate.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>
#include <QtCore/QBindable>

//  Only a class built on QAbstractState may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQAbstractState : QAbstractState {
  using QAbstractState::event;
};

//  A QAbstractState that Python can take functions over in. Every QAbstractState
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQAbstractStateCall0)(const void *, QEvent *, int *);
typedef void (*CuteQAbstractStateCall1)(const void *, QEvent *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAbstractStateCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAbstractStateCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractStateCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractStateCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractStateCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractStateCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractStateCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQAbstractState : public QAbstractState {
public:
  using QAbstractState::QAbstractState;
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

  //  void QAbstractState::onEntry(QEvent *event)
  void onEntry(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQAbstractStateCall0 call = reinterpret_cast<CuteQAbstractStateCall0>(taken[0]);
      call(this, event, &handled);
      if (handled) return;
    }
  }

  //  void QAbstractState::onExit(QEvent *event)
  void onExit(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQAbstractStateCall1 call = reinterpret_cast<CuteQAbstractStateCall1>(taken[1]);
      call(this, event, &handled);
      if (handled) return;
    }
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QAbstractState::event(QEvent *e)
  bool event(QEvent *e) override {
    if (taken[2]) {
      int handled = 0;
      CuteQAbstractStateCall2 call = reinterpret_cast<CuteQAbstractStateCall2>(taken[2]);
      bool given = call(this, e, &handled);
      if (handled) return given;
    }
    return QAbstractState::event(e);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQAbstractStateCall3 call = reinterpret_cast<CuteQAbstractStateCall3>(taken[3]);
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
      CuteQAbstractStateCall4 call = reinterpret_cast<CuteQAbstractStateCall4>(taken[4]);
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
      CuteQAbstractStateCall5 call = reinterpret_cast<CuteQAbstractStateCall5>(taken[5]);
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
      CuteQAbstractStateCall6 call = reinterpret_cast<CuteQAbstractStateCall6>(taken[6]);
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
      CuteQAbstractStateCall7 call = reinterpret_cast<CuteQAbstractStateCall7>(taken[7]);
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
      CuteQAbstractStateCall8 call = reinterpret_cast<CuteQAbstractStateCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QAbstractState::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14QAbstractState10metaObjectEv(
    const QAbstractState *self) {
  return self->metaObject();
}

//  void *QAbstractState::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN14QAbstractState11qt_metacastEPKc(
    QAbstractState *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QAbstractState::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN14QAbstractState11qt_metacallEN11QMetaObject4CallEiPPv(
    QAbstractState *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QAbstractState::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QAbstractState2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QAbstractState::tr(s, c, n));
}

//  QAbstractState::~QAbstractState()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QAbstractStateD1Ev(QAbstractState *self) {
  delete self;
}

//  QState *QAbstractState::parentState() const
extern "C" Q_DECL_EXPORT
QState *ritual_ZNK14QAbstractState11parentStateEv(
    const QAbstractState *self) {
  return self->parentState();
}

//  QStateMachine *QAbstractState::machine() const
extern "C" Q_DECL_EXPORT
QStateMachine *ritual_ZNK14QAbstractState7machineEv(
    const QAbstractState *self) {
  return self->machine();
}

//  bool QAbstractState::active() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QAbstractState6activeEv(const QAbstractState *self) {
  return self->active();
}

//  QBindable<bool> QAbstractState::bindableActive()
extern "C" Q_DECL_EXPORT
QBindable<bool> *ritual_ZN14QAbstractState14bindableActiveEv(
    QAbstractState *self) {
  return new QBindable<bool>(self->bindableActive());
}

//  void QAbstractState::entered(QPrivateSignal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QAbstractState7enteredENS_14QPrivateSignalE(
    QAbstractState *self) {
  self->entered(QAbstractState::QPrivateSignal());
}

//  void QAbstractState::exited(QPrivateSignal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QAbstractState6exitedENS_14QPrivateSignalE(
    QAbstractState *self) {
  self->exited(QAbstractState::QPrivateSignal());
}

//  void QAbstractState::activeChanged(bool active)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QAbstractState13activeChangedEb(
    QAbstractState *self,
    bool active) {
  self->activeChanged(active);
}

//  QAbstractState::QAbstractState(QState *parent)
extern "C" Q_DECL_EXPORT
QAbstractState *ritual_ZN14QAbstractStateC1EP6QState(QState *parent) {
  return new CuteQAbstractState(parent);
}

//  void QAbstractState::onEntry(QEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QAbstractState7onEntryEP6QEvent(
    QAbstractState *self,
    QEvent *event) {
  self->onEntry(event);
}

//  void QAbstractState::onExit(QEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QAbstractState6onExitEP6QEvent(
    QAbstractState *self,
    QEvent *event) {
  self->onExit(event);
}

//  bool QAbstractState::event(QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QAbstractState5eventEP6QEvent(
    QAbstractState *self,
    QEvent *e) {
  return self->event(e);
}

//  QAbstractState::QAbstractState(QAbstractStatePrivate &dd, QState *parent)
extern "C" Q_DECL_EXPORT
QAbstractState *ritual_ZN14QAbstractStateC1ER21QAbstractStatePrivateP6QState(
    QAbstractStatePrivate *dd,
    QState *parent) {
  return new CuteQAbstractState(*dd, parent);
}

//  QAbstractStatePrivate *QAbstractState::d_func()
extern "C" Q_DECL_EXPORT
QAbstractStatePrivate *ritual_ZN14QAbstractState6d_funcEv(
    QAbstractState *self) {
  return self->d_func();
}

//  const QAbstractStatePrivate *QAbstractState::d_func() const
extern "C" Q_DECL_EXPORT
const QAbstractStatePrivate *ritual_ZNK14QAbstractState6d_funcEv(
    const QAbstractState *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQAbstractState, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAbstractState(
    QAbstractState *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAbstractState *>(self)->take(key, call);
}

//  bool QAbstractState::event(QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN14QAbstractState5eventEP6QEvent(
    QAbstractState *self,
    QEvent *e) {
  return static_cast<OwnQAbstractState *>(self)->OwnQAbstractState::event(e);
}

//  QList<QAbstractState *>::QList()
extern "C" Q_DECL_EXPORT
QList<QAbstractState *> *ritual_list_make_QAbstractState_ptr() {
  return new QList<QAbstractState *>();
}

//  void QList<QAbstractState *>::append(const QAbstractState * &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QAbstractState_ptr(
    QList<QAbstractState *> *self,
    QAbstractState *element) {
  self->append(element);
}

//  qsizetype QList<QAbstractState *>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QAbstractState_ptr(
    const QList<QAbstractState *> *self) {
  return self->size();
}

//  const QAbstractState * &QList<QAbstractState *>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QAbstractState *ritual_list_at_QAbstractState_ptr(
    const QList<QAbstractState *> *self,
    long long index) {
  return self->at(index);
}

//  QList<QAbstractState *>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QAbstractState_ptr(QList<QAbstractState *> *self) {
  delete self;
}

//  a QBindable<bool> a ritual of QAbstractState gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QAbstractState__QBindable_bool(QBindable<bool> *self) {
  delete self;
}
