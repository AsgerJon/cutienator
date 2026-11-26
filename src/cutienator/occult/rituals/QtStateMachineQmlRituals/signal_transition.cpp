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
#include <QtCore/QBindable>
#include <QtQml/QQmlScriptString>
#include <QtQml/QJSValue>

//  const QMetaObject *SignalTransition::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16SignalTransition10metaObjectEv(
    const SignalTransition *self) {
  return self->metaObject();
}

//  void *SignalTransition::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN16SignalTransition11qt_metacastEPKc(
    SignalTransition *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int SignalTransition::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN16SignalTransition11qt_metacallEN11QMetaObject4CallEiPPv(
    SignalTransition *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
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

//  QBindable<QQmlScriptString> SignalTransition::bindableGuard()
extern "C" Q_DECL_EXPORT
QBindable<QQmlScriptString> *ritual_ZN16SignalTransition13bindableGuardEv(
    SignalTransition *self) {
  return new QBindable<QQmlScriptString>(self->bindableGuard());
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

//  QBindable<QJSValue> SignalTransition::bindableSignal()
extern "C" Q_DECL_EXPORT
QBindable<QJSValue> *ritual_ZN16SignalTransition14bindableSignalEv(
    SignalTransition *self) {
  return new QBindable<QJSValue>(self->bindableSignal());
}

//  void SignalTransition::invoke()
extern "C" Q_DECL_EXPORT
void ritual_ZN16SignalTransition6invokeEv(SignalTransition *self) {
  self->invoke();
}

//  void SignalTransition::guardChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16SignalTransition12guardChangedEv(SignalTransition *self) {
  self->guardChanged();
}

//  void SignalTransition::invokeYourself()
extern "C" Q_DECL_EXPORT
void ritual_ZN16SignalTransition14invokeYourselfEv(SignalTransition *self) {
  self->invokeYourself();
}

//  void SignalTransition::qmlSignalChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16SignalTransition16qmlSignalChangedEv(
    SignalTransition *self) {
  self->qmlSignalChanged();
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

//  size_t SignalTransition::_qt_property_m_signal_offset()
extern "C" Q_DECL_EXPORT
size_t ritual_ZN16SignalTransition28_qt_property_m_signal_offsetEv() {
  return SignalTransition::_qt_property_m_signal_offset();
}

//  size_t SignalTransition::_qt_property_m_guard_offset()
extern "C" Q_DECL_EXPORT
size_t ritual_ZN16SignalTransition27_qt_property_m_guard_offsetEv() {
  return SignalTransition::_qt_property_m_guard_offset();
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

//  a QBindable<QQmlScriptString> a ritual of SignalTransition gave
extern "C" Q_DECL_EXPORT
void ritual_drop_SignalTransition__QBindable_QQmlScriptString(
    QBindable<QQmlScriptString> *self) {
  delete self;
}

//  a QBindable<QJSValue> a ritual of SignalTransition gave
extern "C" Q_DECL_EXPORT
void ritual_drop_SignalTransition__QBindable_QJSValue(
    QBindable<QJSValue> *self) {
  delete self;
}
