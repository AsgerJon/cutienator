//  Written by dev_tooling.RitualGenerator from the records of
//  QtStateMachineQml/6.12.0/QtStateMachineQml/private/timeouttransition_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtStateMachineQml/6.12.0/QtStateMachineQml/private/qstatemachineqmlglobals_p.h>
#include <QtStateMachineQml/QtStateMachineQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtStateMachineQml/6.12.0/QtStateMachineQml/private/timeouttransition_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#include <QtCore/QBindable>

//  A TimeoutTransition that Python can take functions over in. Every TimeoutTransition
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteTimeoutTransitionCall0)(const void *, int *);
typedef void (*CuteTimeoutTransitionCall1)(const void *, int *);
typedef bool (*CuteTimeoutTransitionCall2)(const void *, QEvent *, int *);
typedef void (*CuteTimeoutTransitionCall3)(const void *, QEvent *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteTimeoutTransitionCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteTimeoutTransitionCall5)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteTimeoutTransitionCall6)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteTimeoutTransitionCall7)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteTimeoutTransitionCall8)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteTimeoutTransitionCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteTimeoutTransitionCall10)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteTimeoutTransition : public TimeoutTransition {
public:
  using TimeoutTransition::TimeoutTransition;
  void *taken[11] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QAbstractTransition9eventTestEP6QEvent")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QAbstractTransition12onTransitionEP6QEvent")) {
      taken[3] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void TimeoutTransition::classBegin()
  void classBegin() override {
    if (taken[0]) {
      int handled = 0;
      CuteTimeoutTransitionCall0 call = reinterpret_cast<CuteTimeoutTransitionCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    TimeoutTransition::classBegin();
  }

  //  void TimeoutTransition::componentComplete()
  void componentComplete() override {
    if (taken[1]) {
      int handled = 0;
      CuteTimeoutTransitionCall1 call = reinterpret_cast<CuteTimeoutTransitionCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    TimeoutTransition::componentComplete();
  }

  //  bool QSignalTransition::eventTest(QEvent *event)
  bool eventTest(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteTimeoutTransitionCall2 call = reinterpret_cast<CuteTimeoutTransitionCall2>(taken[2]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QSignalTransition::eventTest(event);
  }

  //  void QSignalTransition::onTransition(QEvent *event)
  void onTransition(QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteTimeoutTransitionCall3 call = reinterpret_cast<CuteTimeoutTransitionCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QSignalTransition::onTransition(event);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QSignalTransition::event(QEvent *e)
  bool event(QEvent *e) override {
    if (taken[4]) {
      int handled = 0;
      CuteTimeoutTransitionCall4 call = reinterpret_cast<CuteTimeoutTransitionCall4>(taken[4]);
      bool given = call(this, e, &handled);
      if (handled) return given;
    }
    return QSignalTransition::event(e);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteTimeoutTransitionCall5 call = reinterpret_cast<CuteTimeoutTransitionCall5>(taken[5]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteTimeoutTransitionCall6 call = reinterpret_cast<CuteTimeoutTransitionCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteTimeoutTransitionCall7 call = reinterpret_cast<CuteTimeoutTransitionCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteTimeoutTransitionCall8 call = reinterpret_cast<CuteTimeoutTransitionCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[9]) {
      int handled = 0;
      CuteTimeoutTransitionCall9 call = reinterpret_cast<CuteTimeoutTransitionCall9>(taken[9]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[10]) {
      int handled = 0;
      CuteTimeoutTransitionCall10 call = reinterpret_cast<CuteTimeoutTransitionCall10>(taken[10]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *TimeoutTransition::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17TimeoutTransition10metaObjectEv(
    const TimeoutTransition *self) {
  return self->metaObject();
}

//  void *TimeoutTransition::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN17TimeoutTransition11qt_metacastEPKc(
    TimeoutTransition *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int TimeoutTransition::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN17TimeoutTransition11qt_metacallEN11QMetaObject4CallEiPPv(
    TimeoutTransition *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString TimeoutTransition::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17TimeoutTransition2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(TimeoutTransition::tr(s, c, n));
}

//  TimeoutTransition::TimeoutTransition(QState *parent)
extern "C" Q_DECL_EXPORT
TimeoutTransition *ritual_ZN17TimeoutTransitionC1EP6QState(QState *parent) {
  return new CuteTimeoutTransition(parent);
}

//  TimeoutTransition::~TimeoutTransition()
extern "C" Q_DECL_EXPORT
void ritual_ZN17TimeoutTransitionD1Ev(TimeoutTransition *self) {
  delete self;
}

//  int TimeoutTransition::timeout() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17TimeoutTransition7timeoutEv(const TimeoutTransition *self) {
  return self->timeout();
}

//  void TimeoutTransition::setTimeout(int timeout)
extern "C" Q_DECL_EXPORT
void ritual_ZN17TimeoutTransition10setTimeoutEi(
    TimeoutTransition *self,
    int timeout) {
  self->setTimeout(timeout);
}

//  QBindable<int> TimeoutTransition::bindableTimeout()
extern "C" Q_DECL_EXPORT
QBindable<int> *ritual_ZN17TimeoutTransition15bindableTimeoutEv(
    TimeoutTransition *self) {
  return new QBindable<int>(self->bindableTimeout());
}

//  void TimeoutTransition::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN17TimeoutTransition10classBeginEv(TimeoutTransition *self) {
  self->classBegin();
}

//  void TimeoutTransition::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN17TimeoutTransition17componentCompleteEv(
    TimeoutTransition *self) {
  self->componentComplete();
}

//  TimeoutTransition as the QQmlParserStatus it is built on
extern "C" Q_DECL_EXPORT
QQmlParserStatus *ritual_cast_TimeoutTransition_QQmlParserStatus(
    TimeoutTransition *self) {
  return static_cast<QQmlParserStatus *>(self);
}

//  a Python function taken by a CuteTimeoutTransition, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_TimeoutTransition(
    TimeoutTransition *self,
    const char *key,
    void *call) {
  return static_cast<CuteTimeoutTransition *>(self)->take(key, call);
}

//  void TimeoutTransition::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17TimeoutTransition10classBeginEv(
    TimeoutTransition *self) {
  self->TimeoutTransition::classBegin();
}

//  void TimeoutTransition::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17TimeoutTransition17componentCompleteEv(
    TimeoutTransition *self) {
  self->TimeoutTransition::componentComplete();
}

//  a QBindable<int> a ritual of TimeoutTransition gave
extern "C" Q_DECL_EXPORT
void ritual_drop_TimeoutTransition__QBindable_int(QBindable<int> *self) {
  delete self;
}
