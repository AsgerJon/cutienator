//  Written by dev_tooling.RitualGenerator from the records of
//  QtStateMachine/qsignaltransition.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtStateMachine/qsignaltransition.h>
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#include <QtCore/QBindable>
#include <QtCore/QObject>
#include <QtCore/QByteArray>

//  Only a class built on QSignalTransition may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQSignalTransition : QSignalTransition {
  using QSignalTransition::eventTest;
  using QSignalTransition::onTransition;
  using QSignalTransition::event;
};

//  A QSignalTransition that Python can take functions over in. Every QSignalTransition
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQSignalTransitionCall0)(const void *, QEvent *, int *);
typedef void (*CuteQSignalTransitionCall1)(const void *, QEvent *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSignalTransitionCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSignalTransitionCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSignalTransitionCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSignalTransitionCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSignalTransitionCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSignalTransitionCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSignalTransitionCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQSignalTransition : public QSignalTransition {
public:
  using QSignalTransition::QSignalTransition;
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

  //  bool QSignalTransition::eventTest(QEvent *event)
  bool eventTest(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQSignalTransitionCall0 call = reinterpret_cast<CuteQSignalTransitionCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QSignalTransition::eventTest(event);
  }

  //  void QSignalTransition::onTransition(QEvent *event)
  void onTransition(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQSignalTransitionCall1 call = reinterpret_cast<CuteQSignalTransitionCall1>(taken[1]);
      call(this, event, &handled);
      if (handled) return;
    }
    QSignalTransition::onTransition(event);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QSignalTransition::event(QEvent *e)
  bool event(QEvent *e) override {
    if (taken[2]) {
      int handled = 0;
      CuteQSignalTransitionCall2 call = reinterpret_cast<CuteQSignalTransitionCall2>(taken[2]);
      bool given = call(this, e, &handled);
      if (handled) return given;
    }
    return QSignalTransition::event(e);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQSignalTransitionCall3 call = reinterpret_cast<CuteQSignalTransitionCall3>(taken[3]);
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
      CuteQSignalTransitionCall4 call = reinterpret_cast<CuteQSignalTransitionCall4>(taken[4]);
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
      CuteQSignalTransitionCall5 call = reinterpret_cast<CuteQSignalTransitionCall5>(taken[5]);
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
      CuteQSignalTransitionCall6 call = reinterpret_cast<CuteQSignalTransitionCall6>(taken[6]);
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
      CuteQSignalTransitionCall7 call = reinterpret_cast<CuteQSignalTransitionCall7>(taken[7]);
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
      CuteQSignalTransitionCall8 call = reinterpret_cast<CuteQSignalTransitionCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QSignalTransition::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QSignalTransition10metaObjectEv(
    const QSignalTransition *self) {
  return self->metaObject();
}

//  void *QSignalTransition::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN17QSignalTransition11qt_metacastEPKc(
    QSignalTransition *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QSignalTransition::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN17QSignalTransition11qt_metacallEN11QMetaObject4CallEiPPv(
    QSignalTransition *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QSignalTransition::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QSignalTransition2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QSignalTransition::tr(s, c, n));
}

//  QSignalTransition::QSignalTransition(QState *sourceState)
extern "C" Q_DECL_EXPORT
QSignalTransition *ritual_ZN17QSignalTransitionC1EP6QState(
    QState *sourceState) {
  return new CuteQSignalTransition(sourceState);
}

//  QSignalTransition::QSignalTransition(const QObject *sender, const char
//      *signal, QState *sourceState)
extern "C" Q_DECL_EXPORT
QSignalTransition *ritual_ZN17QSignalTransitionC1EPK7QObjectPKcP6QState(
    const QObject *sender,
    const char *signal,
    QState *sourceState) {
  return new CuteQSignalTransition(sender, signal, sourceState);
}

//  QSignalTransition::~QSignalTransition()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSignalTransitionD1Ev(QSignalTransition *self) {
  delete self;
}

//  const QObject *QSignalTransition::senderObject() const
extern "C" Q_DECL_EXPORT
const QObject *ritual_ZNK17QSignalTransition12senderObjectEv(
    const QSignalTransition *self) {
  return self->senderObject();
}

//  void QSignalTransition::setSenderObject(const QObject *sender)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSignalTransition15setSenderObjectEPK7QObject(
    QSignalTransition *self,
    const QObject *sender) {
  self->setSenderObject(sender);
}

//  QBindable<const QObject *> QSignalTransition::bindableSenderObject()
extern "C" Q_DECL_EXPORT
QBindable<const QObject *> *ritual_ZN17QSignalTransition20bindableSenderObjectEv(
    QSignalTransition *self) {
  return new QBindable<const QObject *>(self->bindableSenderObject());
}

//  QByteArray QSignalTransition::signal() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK17QSignalTransition6signalEv(
    const QSignalTransition *self) {
  return new QByteArray(self->signal());
}

//  void QSignalTransition::setSignal(const QByteArray &signal)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSignalTransition9setSignalERK10QByteArray(
    QSignalTransition *self,
    const QByteArray *signal) {
  self->setSignal(*signal);
}

//  QBindable<QByteArray> QSignalTransition::bindableSignal()
extern "C" Q_DECL_EXPORT
QBindable<QByteArray> *ritual_ZN17QSignalTransition14bindableSignalEv(
    QSignalTransition *self) {
  return new QBindable<QByteArray>(self->bindableSignal());
}

//  bool QSignalTransition::eventTest(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QSignalTransition9eventTestEP6QEvent(
    QSignalTransition *self,
    QEvent *event) {
  return self->eventTest(event);
}

//  void QSignalTransition::onTransition(QEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSignalTransition12onTransitionEP6QEvent(
    QSignalTransition *self,
    QEvent *event) {
  self->onTransition(event);
}

//  bool QSignalTransition::event(QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QSignalTransition5eventEP6QEvent(
    QSignalTransition *self,
    QEvent *e) {
  return self->event(e);
}

//  void QSignalTransition::senderObjectChanged(QPrivateSignal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSignalTransition19senderObjectChangedENS_14QPrivateSignalE(
    QSignalTransition *self) {
  self->senderObjectChanged(QSignalTransition::QPrivateSignal());
}

//  void QSignalTransition::signalChanged(QPrivateSignal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSignalTransition13signalChangedENS_14QPrivateSignalE(
    QSignalTransition *self) {
  self->signalChanged(QSignalTransition::QPrivateSignal());
}

//  QSignalTransitionPrivate *QSignalTransition::d_func()
extern "C" Q_DECL_EXPORT
QSignalTransitionPrivate *ritual_ZN17QSignalTransition6d_funcEv(
    QSignalTransition *self) {
  return self->d_func();
}

//  const QSignalTransitionPrivate *QSignalTransition::d_func() const
extern "C" Q_DECL_EXPORT
const QSignalTransitionPrivate *ritual_ZNK17QSignalTransition6d_funcEv(
    const QSignalTransition *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQSignalTransition, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSignalTransition(
    QSignalTransition *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSignalTransition *>(self)->take(key, call);
}

//  bool QSignalTransition::eventTest(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN17QSignalTransition9eventTestEP6QEvent(
    QSignalTransition *self,
    QEvent *event) {
  return static_cast<OwnQSignalTransition *>(self)->OwnQSignalTransition::eventTest(
      event);
}

//  void QSignalTransition::onTransition(QEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QSignalTransition12onTransitionEP6QEvent(
    QSignalTransition *self,
    QEvent *event) {
  static_cast<OwnQSignalTransition *>(self)->OwnQSignalTransition::onTransition(
      event);
}

//  bool QSignalTransition::event(QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN17QSignalTransition5eventEP6QEvent(
    QSignalTransition *self,
    QEvent *e) {
  return static_cast<OwnQSignalTransition *>(self)->OwnQSignalTransition::event(
      e);
}

//  a QBindable<const QObject *> a ritual of QSignalTransition gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QSignalTransition__QBindable_const_QObject(
    QBindable<const QObject *> *self) {
  delete self;
}

//  a QBindable<QByteArray> a ritual of QSignalTransition gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QSignalTransition__QBindable_QByteArray(
    QBindable<QByteArray> *self) {
  delete self;
}
