//  Written by hand on 2026-11-25 from QtStateMachine/qeventtransition.h,
//  Qt 6.12.0, the same text on every system. Kept as it is when the
//  generator runs again. Not written: the 'bindable...' functions,
//  which give a template, a 'QBindable'.
//  Not written either: the two protected constructors, which take a
//  'QEventTransitionPrivate &'.
#include <QtStateMachine/qstatemachineglobal.h>
#include <QtStateMachine/6.12.0/QtStateMachine/private/qstatemachineglobal_p.h>
#if QT_CONFIG(qeventtransition)
#include <QtStateMachine/qeventtransition.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QEventTransition may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQEventTransition : QEventTransition {
  using QEventTransition::eventTest;
  using QEventTransition::onTransition;
  using QEventTransition::event;
};

//  A QEventTransition that Python can take functions over in. Every
//  QEventTransition Python makes is one. Each function below asks the
//  Python function handed over for it, and runs Qt's own without
//  one.
typedef bool (*CuteQEventTransitionCall0)(const void *, QEvent *, int *);
typedef void (*CuteQEventTransitionCall1)(const void *, QEvent *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQEventTransitionCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQEventTransitionCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQEventTransitionCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQEventTransitionCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQEventTransitionCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQEventTransitionCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQEventTransitionCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQEventTransition : public QEventTransition {
public:
  using QEventTransition::QEventTransition;
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

  //  bool QEventTransition::eventTest(QEvent *event)
  bool eventTest(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQEventTransitionCall0 call = reinterpret_cast<CuteQEventTransitionCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QEventTransition::eventTest(event);
  }

  //  void QEventTransition::onTransition(QEvent *event)
  void onTransition(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQEventTransitionCall1 call = reinterpret_cast<CuteQEventTransitionCall1>(taken[1]);
      call(this, event, &handled);
      if (handled) return;
    }
    QEventTransition::onTransition(event);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QEventTransition::event(QEvent *e)
  bool event(QEvent *e) override {
    if (taken[2]) {
      int handled = 0;
      CuteQEventTransitionCall2 call = reinterpret_cast<CuteQEventTransitionCall2>(taken[2]);
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
      CuteQEventTransitionCall3 call = reinterpret_cast<CuteQEventTransitionCall3>(taken[3]);
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
      CuteQEventTransitionCall4 call = reinterpret_cast<CuteQEventTransitionCall4>(taken[4]);
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
      CuteQEventTransitionCall5 call = reinterpret_cast<CuteQEventTransitionCall5>(taken[5]);
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
      CuteQEventTransitionCall6 call = reinterpret_cast<CuteQEventTransitionCall6>(taken[6]);
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
      CuteQEventTransitionCall7 call = reinterpret_cast<CuteQEventTransitionCall7>(taken[7]);
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
      CuteQEventTransitionCall8 call = reinterpret_cast<CuteQEventTransitionCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QEventTransition::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QEventTransition10metaObjectEv(
    const QEventTransition *self) {
  return self->metaObject();
}

//  QString QEventTransition::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QEventTransition2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QEventTransition::tr(s, c, n));
}

//  QEventTransition::QEventTransition(QState *sourceState)
extern "C" Q_DECL_EXPORT
QEventTransition *ritual_ZN16QEventTransitionC1EP6QState(
    QState *sourceState) {
  return new CuteQEventTransition(sourceState);
}

//  QEventTransition::QEventTransition(QObject *object, QEvent::Type type,
//      QState *sourceState)
extern "C" Q_DECL_EXPORT
QEventTransition *ritual_ZN16QEventTransitionC1EP7QObjectN6QEvent4TypeEP6QState(
    QObject *object,
    QEvent::Type type,
    QState *sourceState) {
  return new CuteQEventTransition(object, type, sourceState);
}

//  QEventTransition::~QEventTransition()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QEventTransitionD1Ev(QEventTransition *self) {
  delete self;
}

//  QObject *QEventTransition::eventSource() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK16QEventTransition11eventSourceEv(
    const QEventTransition *self) {
  return self->eventSource();
}

//  void QEventTransition::setEventSource(QObject *object)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QEventTransition14setEventSourceEP7QObject(
    QEventTransition *self,
    QObject *object) {
  self->setEventSource(object);
}

//  QEvent::Type QEventTransition::eventType() const
extern "C" Q_DECL_EXPORT
QEvent::Type ritual_ZNK16QEventTransition9eventTypeEv(
    const QEventTransition *self) {
  return self->eventType();
}

//  void QEventTransition::setEventType(QEvent::Type type)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QEventTransition12setEventTypeEN6QEvent4TypeE(
    QEventTransition *self,
    QEvent::Type type) {
  self->setEventType(type);
}

//  bool QEventTransition::eventTest(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QEventTransition9eventTestEP6QEvent(
    QEventTransition *self,
    QEvent *event) {
  return self->eventTest(event);
}

//  void QEventTransition::onTransition(QEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QEventTransition12onTransitionEP6QEvent(
    QEventTransition *self,
    QEvent *event) {
  self->onTransition(event);
}

//  bool QEventTransition::event(QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QEventTransition5eventEP6QEvent(
    QEventTransition *self,
    QEvent *e) {
  return self->event(e);
}

//  a Python function taken by a CuteQEventTransition, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QEventTransition(
    QEventTransition *self,
    const char *key,
    void *call) {
  return static_cast<CuteQEventTransition *>(self)->take(key, call);
}

//  bool QEventTransition::eventTest(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN16QEventTransition9eventTestEP6QEvent(
    QEventTransition *self,
    QEvent *event) {
  return static_cast<OwnQEventTransition *>(self)->OwnQEventTransition::eventTest(
      event);
}

//  void QEventTransition::onTransition(QEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QEventTransition12onTransitionEP6QEvent(
    QEventTransition *self,
    QEvent *event) {
  static_cast<OwnQEventTransition *>(self)->OwnQEventTransition::onTransition(
      event);
}

//  bool QEventTransition::event(QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN16QEventTransition5eventEP6QEvent(
    QEventTransition *self,
    QEvent *e) {
  return static_cast<OwnQEventTransition *>(self)->OwnQEventTransition::event(
      e);
}

#endif  // QT_CONFIG(qeventtransition)
