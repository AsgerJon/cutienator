//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4compileddata_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4compileddata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  void QV4::CompiledData::Binding::clearFlags()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV412CompiledData7Binding10clearFlagsEv(
    QV4::CompiledData::Binding *self) {
  self->clearFlags();
}

//  void QV4::CompiledData::Binding::setFlag(Flag flag)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV412CompiledData7Binding7setFlagENS1_4FlagE(
    QV4::CompiledData::Binding *self,
    QV4::CompiledData::Binding::Flag flag) {
  self->setFlag(flag);
}

//  bool QV4::CompiledData::Binding::hasFlag(Flag flag) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV412CompiledData7Binding7hasFlagENS1_4FlagE(
    const QV4::CompiledData::Binding *self,
    QV4::CompiledData::Binding::Flag flag) {
  return self->hasFlag(flag);
}

//  Flags QV4::CompiledData::Binding::flags() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK3QV412CompiledData7Binding5flagsEv(
    const QV4::CompiledData::Binding *self) {
  return static_cast<int>(self->flags().toInt());
}

//  void QV4::CompiledData::Binding::setType(Type type)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV412CompiledData7Binding7setTypeENS1_4TypeE(
    QV4::CompiledData::Binding *self,
    QV4::CompiledData::Binding::Type type) {
  self->setType(type);
}

//  Type QV4::CompiledData::Binding::type() const
extern "C" Q_DECL_EXPORT
QV4::CompiledData::Binding::Type ritual_ZNK3QV412CompiledData7Binding4typeEv(
    const QV4::CompiledData::Binding *self) {
  return self->type();
}

//  bool QV4::CompiledData::Binding::hasSignalHandlerBindingFlag() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV412CompiledData7Binding27hasSignalHandlerBindingFlagEv(
    const QV4::CompiledData::Binding *self) {
  return self->hasSignalHandlerBindingFlag();
}

//  bool QV4::CompiledData::Binding::isValueBinding() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV412CompiledData7Binding14isValueBindingEv(
    const QV4::CompiledData::Binding *self) {
  return self->isValueBinding();
}

//  bool QV4::CompiledData::Binding::isValueBindingNoAlias() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV412CompiledData7Binding21isValueBindingNoAliasEv(
    const QV4::CompiledData::Binding *self) {
  return self->isValueBindingNoAlias();
}

//  bool QV4::CompiledData::Binding::isValueBindingToAlias() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV412CompiledData7Binding21isValueBindingToAliasEv(
    const QV4::CompiledData::Binding *self) {
  return self->isValueBindingToAlias();
}

//  bool QV4::CompiledData::Binding::isSignalHandler() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV412CompiledData7Binding15isSignalHandlerEv(
    const QV4::CompiledData::Binding *self) {
  return self->isSignalHandler();
}

//  bool QV4::CompiledData::Binding::isAttachedProperty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV412CompiledData7Binding18isAttachedPropertyEv(
    const QV4::CompiledData::Binding *self) {
  return self->isAttachedProperty();
}

//  bool QV4::CompiledData::Binding::isGroupProperty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV412CompiledData7Binding15isGroupPropertyEv(
    const QV4::CompiledData::Binding *self) {
  return self->isGroupProperty();
}

//  bool QV4::CompiledData::Binding::isFunctionExpression() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV412CompiledData7Binding20isFunctionExpressionEv(
    const QV4::CompiledData::Binding *self) {
  return self->isFunctionExpression();
}

//  QString QV4::CompiledData::Binding::escapedString(const QString &string)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN3QV412CompiledData7Binding13escapedStringERK7QString(
    const QString *string) {
  return new QString(QV4::CompiledData::Binding::escapedString(*string));
}

//  bool QV4::CompiledData::Binding::isTranslationBinding() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV412CompiledData7Binding20isTranslationBindingEv(
    const QV4::CompiledData::Binding *self) {
  return self->isTranslationBinding();
}

//  bool QV4::CompiledData::Binding::evaluatesToString() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV412CompiledData7Binding17evaluatesToStringEv(
    const QV4::CompiledData::Binding *self) {
  return self->evaluatesToString();
}

//  bool QV4::CompiledData::Binding::isNumberBinding() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV412CompiledData7Binding15isNumberBindingEv(
    const QV4::CompiledData::Binding *self) {
  return self->isNumberBinding();
}

//  bool QV4::CompiledData::Binding::valueAsBoolean() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV412CompiledData7Binding14valueAsBooleanEv(
    const QV4::CompiledData::Binding *self) {
  return self->valueAsBoolean();
}

//  QV4::CompiledData::Binding::~Binding()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV412CompiledData7BindingD1Ev(
    QV4::CompiledData::Binding *self) {
  delete self;
}
