//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4debugging_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/qtqmlglobal.h>
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#if !(!QT_CONFIG(qml_debug))
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4debugging_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QV4::Debugging::Debugger that Python can take functions over in. Every QV4::Debugging::Debugger
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !(!QT_CONFIG(qml_debug))
typedef bool (*CuteQV4_Debugging_DebuggerCall0)(const void *, int *);
#endif  // !(!QT_CONFIG(qml_debug))
#if !(!QT_CONFIG(qml_debug))
typedef void (*CuteQV4_Debugging_DebuggerCall1)(const void *, int *);
#endif  // !(!QT_CONFIG(qml_debug))
#if !(!QT_CONFIG(qml_debug))
typedef void (*CuteQV4_Debugging_DebuggerCall2)(const void *, int *);
#endif  // !(!QT_CONFIG(qml_debug))
#if !(!QT_CONFIG(qml_debug))
typedef void (*CuteQV4_Debugging_DebuggerCall3)(const void *, QV4::ReturnedValue, int *);
#endif  // !(!QT_CONFIG(qml_debug))
#if !(!QT_CONFIG(qml_debug))
typedef void (*CuteQV4_Debugging_DebuggerCall4)(const void *, int *);
#endif  // !(!QT_CONFIG(qml_debug))
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQV4_Debugging_DebuggerCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQV4_Debugging_DebuggerCall6)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQV4_Debugging_DebuggerCall7)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQV4_Debugging_DebuggerCall8)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQV4_Debugging_DebuggerCall9)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQV4_Debugging_DebuggerCall10)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQV4_Debugging_DebuggerCall11)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQV4_Debugging_Debugger : public QV4::Debugging::Debugger {
public:
  using QV4::Debugging::Debugger::Debugger;
  void *taken[12] = {};

  bool take(const char *key, void *call) {
#if !(!QT_CONFIG(qml_debug))
    if (!std::strcmp(key, "_ZNK3QV49Debugging8Debugger22pauseAtNextOpportunityEv")) {
      taken[0] = call;
      return true;
    }
#endif  // !(!QT_CONFIG(qml_debug))
#if !(!QT_CONFIG(qml_debug))
    if (!std::strcmp(key, "_ZN3QV49Debugging8Debugger23maybeBreakAtInstructionEv")) {
      taken[1] = call;
      return true;
    }
#endif  // !(!QT_CONFIG(qml_debug))
#if !(!QT_CONFIG(qml_debug))
    if (!std::strcmp(key, "_ZN3QV49Debugging8Debugger16enteringFunctionEv")) {
      taken[2] = call;
      return true;
    }
#endif  // !(!QT_CONFIG(qml_debug))
#if !(!QT_CONFIG(qml_debug))
    if (!std::strcmp(key, "_ZN3QV49Debugging8Debugger15leavingFunctionERKy")) {
      taken[3] = call;
      return true;
    }
#endif  // !(!QT_CONFIG(qml_debug))
#if !(!QT_CONFIG(qml_debug))
    if (!std::strcmp(key, "_ZN3QV49Debugging8Debugger12aboutToThrowEv")) {
      taken[4] = call;
      return true;
    }
#endif  // !(!QT_CONFIG(qml_debug))
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !(!QT_CONFIG(qml_debug))
  //  bool QV4::Debugging::Debugger::pauseAtNextOpportunity() const
  bool pauseAtNextOpportunity() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQV4_Debugging_DebuggerCall0 call = reinterpret_cast<CuteQV4_Debugging_DebuggerCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }
#endif  // !(!QT_CONFIG(qml_debug))

#if !(!QT_CONFIG(qml_debug))
  //  void QV4::Debugging::Debugger::maybeBreakAtInstruction()
  void maybeBreakAtInstruction() override {
    if (taken[1]) {
      int handled = 0;
      CuteQV4_Debugging_DebuggerCall1 call = reinterpret_cast<CuteQV4_Debugging_DebuggerCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
  }
#endif  // !(!QT_CONFIG(qml_debug))

#if !(!QT_CONFIG(qml_debug))
  //  void QV4::Debugging::Debugger::enteringFunction()
  void enteringFunction() override {
    if (taken[2]) {
      int handled = 0;
      CuteQV4_Debugging_DebuggerCall2 call = reinterpret_cast<CuteQV4_Debugging_DebuggerCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
  }
#endif  // !(!QT_CONFIG(qml_debug))

#if !(!QT_CONFIG(qml_debug))
  //  void QV4::Debugging::Debugger::leavingFunction(const ReturnedValue
  //      &retVal)
  void leavingFunction(const QV4::ReturnedValue &retVal) override {
    if (taken[3]) {
      int handled = 0;
      CuteQV4_Debugging_DebuggerCall3 call = reinterpret_cast<CuteQV4_Debugging_DebuggerCall3>(taken[3]);
      call(this, retVal, &handled);
      if (handled) return;
    }
  }
#endif  // !(!QT_CONFIG(qml_debug))

#if !(!QT_CONFIG(qml_debug))
  //  void QV4::Debugging::Debugger::aboutToThrow()
  void aboutToThrow() override {
    if (taken[4]) {
      int handled = 0;
      CuteQV4_Debugging_DebuggerCall4 call = reinterpret_cast<CuteQV4_Debugging_DebuggerCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
  }
#endif  // !(!QT_CONFIG(qml_debug))

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQV4_Debugging_DebuggerCall5 call = reinterpret_cast<CuteQV4_Debugging_DebuggerCall5>(taken[5]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQV4_Debugging_DebuggerCall6 call = reinterpret_cast<CuteQV4_Debugging_DebuggerCall6>(taken[6]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQV4_Debugging_DebuggerCall7 call = reinterpret_cast<CuteQV4_Debugging_DebuggerCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQV4_Debugging_DebuggerCall8 call = reinterpret_cast<CuteQV4_Debugging_DebuggerCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQV4_Debugging_DebuggerCall9 call = reinterpret_cast<CuteQV4_Debugging_DebuggerCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[10]) {
      int handled = 0;
      CuteQV4_Debugging_DebuggerCall10 call = reinterpret_cast<CuteQV4_Debugging_DebuggerCall10>(taken[10]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[11]) {
      int handled = 0;
      CuteQV4_Debugging_DebuggerCall11 call = reinterpret_cast<CuteQV4_Debugging_DebuggerCall11>(taken[11]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QV4::Debugging::Debugger::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK3QV49Debugging8Debugger10metaObjectEv(
    const QV4::Debugging::Debugger *self) {
  return self->metaObject();
}

//  QString QV4::Debugging::Debugger::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN3QV49Debugging8Debugger2trEPKcS3_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QV4::Debugging::Debugger::tr(s, c, n));
}

//  QV4::Debugging::Debugger::~Debugger()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV49Debugging8DebuggerD1Ev(QV4::Debugging::Debugger *self) {
  delete self;
}

//  bool QV4::Debugging::Debugger::pauseAtNextOpportunity() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV49Debugging8Debugger22pauseAtNextOpportunityEv(
    const QV4::Debugging::Debugger *self) {
  return self->pauseAtNextOpportunity();
}

//  void QV4::Debugging::Debugger::maybeBreakAtInstruction()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV49Debugging8Debugger23maybeBreakAtInstructionEv(
    QV4::Debugging::Debugger *self) {
  self->maybeBreakAtInstruction();
}

//  void QV4::Debugging::Debugger::enteringFunction()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV49Debugging8Debugger16enteringFunctionEv(
    QV4::Debugging::Debugger *self) {
  self->enteringFunction();
}

//  void QV4::Debugging::Debugger::leavingFunction(const ReturnedValue
//      &retVal)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV49Debugging8Debugger15leavingFunctionERKy(
    QV4::Debugging::Debugger *self,
    QV4::ReturnedValue retVal) {
  self->leavingFunction(retVal);
}

//  void QV4::Debugging::Debugger::aboutToThrow()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV49Debugging8Debugger12aboutToThrowEv(
    QV4::Debugging::Debugger *self) {
  self->aboutToThrow();
}

//  a Python function taken by a CuteQV4_Debugging_Debugger, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QV4_Debugging_Debugger(
    QV4::Debugging::Debugger *self,
    const char *key,
    void *call) {
  return static_cast<CuteQV4_Debugging_Debugger *>(self)->take(key, call);
}

#endif  // !(!QT_CONFIG(qml_debug))
