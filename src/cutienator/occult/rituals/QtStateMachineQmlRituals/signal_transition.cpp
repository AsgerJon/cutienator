//  Written by dev_tooling.RitualGenerator from the records of
//  QtStateMachineQml/6.12.0/QtStateMachineQml/private/signaltransition_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtStateMachineQml/6.12.0/QtStateMachineQml/private/qstatemachineqmlglobals_p.h>
#include <QtStateMachineQml/QtStateMachineQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtStateMachineQml/6.12.0/QtStateMachineQml/private/signaltransition_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtQml/QtQml>
#include <QtQml/qqmlscriptstring.h>
#include <QtQml/qjsvalue.h>

//  const QMetaObject *SignalTransition::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16SignalTransition10metaObjectEv(
    const SignalTransition *self) {
  return self->metaObject();
}

//  QString SignalTransition::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16SignalTransition2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(SignalTransition::tr(s, c, n));
}

//  SignalTransition::SignalTransition(QState *parent)
extern "C" Q_DECL_EXPORT
SignalTransition *ritual_ZN16SignalTransitionC1EP6QState(QState *parent) {
  return new SignalTransition(parent);
}

//  QQmlScriptString SignalTransition::guard() const
extern "C" Q_DECL_EXPORT
QQmlScriptString *ritual_ZNK16SignalTransition5guardEv(
    const SignalTransition *self) {
  return new QQmlScriptString(self->guard());
}

//  void SignalTransition::setGuard(const QQmlScriptString &guard)
extern "C" Q_DECL_EXPORT
void ritual_ZN16SignalTransition8setGuardERK16QQmlScriptString(
    SignalTransition *self,
    const QQmlScriptString *guard) {
  self->setGuard(*guard);
}

//  bool SignalTransition::eventTest(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16SignalTransition9eventTestEP6QEvent(
    SignalTransition *self,
    QEvent *event) {
  return self->eventTest(event);
}

//  void SignalTransition::onTransition(QEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN16SignalTransition12onTransitionEP6QEvent(
    SignalTransition *self,
    QEvent *event) {
  self->onTransition(event);
}

//  const QJSValue &SignalTransition::signal()
extern "C" Q_DECL_EXPORT
QJSValue *ritual_ZN16SignalTransition6signalEv(SignalTransition *self) {
  return new QJSValue(self->signal());
}

//  void SignalTransition::setSignal(const QJSValue &signal)
extern "C" Q_DECL_EXPORT
void ritual_ZN16SignalTransition9setSignalERK8QJSValue(
    SignalTransition *self,
    const QJSValue *signal) {
  self->setSignal(*signal);
}

//  void SignalTransition::invoke()
extern "C" Q_DECL_EXPORT
void ritual_ZN16SignalTransition6invokeEv(SignalTransition *self) {
  self->invoke();
}

//  void SignalTransition::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN16SignalTransition10classBeginEv(SignalTransition *self) {
  self->classBegin();
}

//  void SignalTransition::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN16SignalTransition17componentCompleteEv(
    SignalTransition *self) {
  self->componentComplete();
}

//  void SignalTransition::connectTriggered()
extern "C" Q_DECL_EXPORT
void ritual_ZN16SignalTransition16connectTriggeredEv(
    SignalTransition *self) {
  self->connectTriggered();
}

//  SignalTransition as the QQmlParserStatus it is built on
extern "C" Q_DECL_EXPORT
QQmlParserStatus *ritual_cast_SignalTransition_QQmlParserStatus(
    SignalTransition *self) {
  return static_cast<QQmlParserStatus *>(self);
}

//  bool SignalTransition::eventTest(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN16SignalTransition9eventTestEP6QEvent(
    SignalTransition *self,
    QEvent *event) {
  return self->SignalTransition::eventTest(event);
}

//  void SignalTransition::onTransition(QEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16SignalTransition12onTransitionEP6QEvent(
    SignalTransition *self,
    QEvent *event) {
  self->SignalTransition::onTransition(event);
}

//  void SignalTransition::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16SignalTransition10classBeginEv(SignalTransition *self) {
  self->SignalTransition::classBegin();
}

//  void SignalTransition::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16SignalTransition17componentCompleteEv(
    SignalTransition *self) {
  self->SignalTransition::componentComplete();
}
