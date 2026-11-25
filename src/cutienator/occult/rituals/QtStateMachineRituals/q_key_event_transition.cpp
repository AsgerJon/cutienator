//  Written by hand on 2026-11-25 from QtStateMachine/qkeyeventtransition.h,
//  Qt 6.12.0, the same text on every system. Kept as it is when the
//  generator runs again. Not written: the 'bindable...' functions,
//  which give a template, a 'QBindable'.
#include <QtStateMachine/qstatemachineglobal.h>
#include <QtStateMachine/6.12.0/QtStateMachine/private/qstatemachineglobal_p.h>
#if QT_CONFIG(qeventtransition)
#include <QtStateMachine/qkeyeventtransition.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QKeyEventTransition may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQKeyEventTransition : QKeyEventTransition {
  using QKeyEventTransition::eventTest;
  using QKeyEventTransition::onTransition;
};

//  A QKeyEventTransition that Python can take functions over in. Every
//  QKeyEventTransition Python makes is one. Each function below asks the
//  Python function handed over for it, and runs Qt's own without
//  one.
typedef bool (*CuteQKeyEventTransitionCall0)(const void *, QEvent *, int *);
typedef void (*CuteQKeyEventTransitionCall1)(const void *, QEvent *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQKeyEventTransitionCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQKeyEventTransitionCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQKeyEventTransitionCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQKeyEventTransitionCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQKeyEventTransitionCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQKeyEventTransitionCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQKeyEventTransitionCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQKeyEventTransition : public QKeyEventTransition {
public:
  using QKeyEventTransition::QKeyEventTransition;
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

  //  bool QKeyEventTransition::eventTest(QEvent *event)
  bool eventTest(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQKeyEventTransitionCall0 call = reinterpret_cast<CuteQKeyEventTransitionCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QKeyEventTransition::eventTest(event);
  }

  //  void QKeyEventTransition::onTransition(QEvent *event)
  void onTransition(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQKeyEventTransitionCall1 call = reinterpret_cast<CuteQKeyEventTransitionCall1>(taken[1]);
      call(this, event, &handled);
      if (handled) return;
    }
    QKeyEventTransition::onTransition(event);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QEventTransition::event(QEvent *e)
  bool event(QEvent *e) override {
    if (taken[2]) {
      int handled = 0;
      CuteQKeyEventTransitionCall2 call = reinterpret_cast<CuteQKeyEventTransitionCall2>(taken[2]);
      bool given = call(this, e, &handled);
      if (handled) return given;
    }
    return QEventTransition::event(e);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQKeyEventTransitionCall3 call = reinterpret_cast<CuteQKeyEventTransitionCall3>(taken[3]);
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
      CuteQKeyEventTransitionCall4 call = reinterpret_cast<CuteQKeyEventTransitionCall4>(taken[4]);
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
      CuteQKeyEventTransitionCall5 call = reinterpret_cast<CuteQKeyEventTransitionCall5>(taken[5]);
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
      CuteQKeyEventTransitionCall6 call = reinterpret_cast<CuteQKeyEventTransitionCall6>(taken[6]);
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
      CuteQKeyEventTransitionCall7 call = reinterpret_cast<CuteQKeyEventTransitionCall7>(taken[7]);
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
      CuteQKeyEventTransitionCall8 call = reinterpret_cast<CuteQKeyEventTransitionCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QKeyEventTransition::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19QKeyEventTransition10metaObjectEv(
    const QKeyEventTransition *self) {
  return self->metaObject();
}

//  QString QKeyEventTransition::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19QKeyEventTransition2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QKeyEventTransition::tr(s, c, n));
}

//  QKeyEventTransition::QKeyEventTransition(QState *sourceState)
extern "C" Q_DECL_EXPORT
QKeyEventTransition *ritual_ZN19QKeyEventTransitionC1EP6QState(
    QState *sourceState) {
  return new CuteQKeyEventTransition(sourceState);
}

//  QKeyEventTransition::QKeyEventTransition(QObject *object, QEvent::Type
//      type, int key, QState *sourceState)
extern "C" Q_DECL_EXPORT
QKeyEventTransition *ritual_ZN19QKeyEventTransitionC1EP7QObjectN6QEvent4TypeEiP6QState(
    QObject *object,
    QEvent::Type type,
    int key,
    QState *sourceState) {
  return new CuteQKeyEventTransition(object, type, key, sourceState);
}

//  QKeyEventTransition::~QKeyEventTransition()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QKeyEventTransitionD1Ev(QKeyEventTransition *self) {
  delete self;
}

//  int QKeyEventTransition::key() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QKeyEventTransition3keyEv(const QKeyEventTransition *self) {
  return self->key();
}

//  void QKeyEventTransition::setKey(int key)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QKeyEventTransition6setKeyEi(
    QKeyEventTransition *self,
    int key) {
  self->setKey(key);
}

//  Qt::KeyboardModifiers QKeyEventTransition::modifierMask() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QKeyEventTransition12modifierMaskEv(
    const QKeyEventTransition *self) {
  return static_cast<int>(self->modifierMask().toInt());
}

//  void QKeyEventTransition::setModifierMask(Qt::KeyboardModifiers
//      modifiers)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QKeyEventTransition15setModifierMaskE6QFlagsIN2Qt16KeyboardModifierEE(
    QKeyEventTransition *self,
    int modifiers) {
  self->setModifierMask(
      QFlags<Qt::KeyboardModifier>::fromInt(modifiers));
}

//  bool QKeyEventTransition::eventTest(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QKeyEventTransition9eventTestEP6QEvent(
    QKeyEventTransition *self,
    QEvent *event) {
  return self->eventTest(event);
}

//  void QKeyEventTransition::onTransition(QEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QKeyEventTransition12onTransitionEP6QEvent(
    QKeyEventTransition *self,
    QEvent *event) {
  self->onTransition(event);
}

//  a Python function taken by a CuteQKeyEventTransition, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QKeyEventTransition(
    QKeyEventTransition *self,
    const char *key,
    void *call) {
  return static_cast<CuteQKeyEventTransition *>(self)->take(key, call);
}

//  bool QKeyEventTransition::eventTest(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN19QKeyEventTransition9eventTestEP6QEvent(
    QKeyEventTransition *self,
    QEvent *event) {
  return static_cast<OwnQKeyEventTransition *>(self)->OwnQKeyEventTransition::eventTest(
      event);
}

//  void QKeyEventTransition::onTransition(QEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QKeyEventTransition12onTransitionEP6QEvent(
    QKeyEventTransition *self,
    QEvent *event) {
  static_cast<OwnQKeyEventTransition *>(self)->OwnQKeyEventTransition::onTransition(
      event);
}

#endif  // QT_CONFIG(qeventtransition)
