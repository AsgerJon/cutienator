//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlCompiler/qqmlsa.h, Qt 6.12.0. Changes made here are lost.
#include <QtQmlCompiler/qqmlsa.h>
#include <QtCore/qstring.h>
#include <QtQmlCompiler/qqmlsasourcelocation.h>

//  BindingPrivate *QQmlSA::Binding::d_func()
extern "C" Q_DECL_EXPORT
QQmlSA::BindingPrivate *ritual_ZN6QQmlSA7Binding6d_funcEv(
    QQmlSA::Binding *self) {
  return self->d_func();
}

//  const BindingPrivate *QQmlSA::Binding::d_func() const
extern "C" Q_DECL_EXPORT
const QQmlSA::BindingPrivate *ritual_ZNK6QQmlSA7Binding6d_funcEv(
    const QQmlSA::Binding *self) {
  return self->d_func();
}

//  QQmlSA::Binding::Binding()
extern "C" Q_DECL_EXPORT
QQmlSA::Binding *ritual_ZN6QQmlSA7BindingC1Ev() {
  return new QQmlSA::Binding();
}

//  QQmlSA::Binding::Binding(const Binding &a0)
extern "C" Q_DECL_EXPORT
QQmlSA::Binding *ritual_ZN6QQmlSA7BindingC1ERKS0_(
    const QQmlSA::Binding *a0) {
  return new QQmlSA::Binding(*a0);
}

//  QQmlSA::Binding::Binding(Binding &&a0)
extern "C" Q_DECL_EXPORT
QQmlSA::Binding *ritual_ZN6QQmlSA7BindingC1EOS0_(QQmlSA::Binding *a0) {
  return new QQmlSA::Binding(std::move(*a0));
}

//  Binding &QQmlSA::Binding::operator=(const Binding &a0)
extern "C" Q_DECL_EXPORT
QQmlSA::Binding *ritual_ZN6QQmlSA7BindingaSERKS0_(
    QQmlSA::Binding *self,
    const QQmlSA::Binding *a0) {
  return &(self->operator=(*a0));
}

//  Binding &QQmlSA::Binding::operator=(Binding &&a0)
extern "C" Q_DECL_EXPORT
QQmlSA::Binding *ritual_ZN6QQmlSA7BindingaSEOS0_(
    QQmlSA::Binding *self,
    QQmlSA::Binding *a0) {
  return &(self->operator=(std::move(*a0)));
}

//  QQmlSA::Binding::~Binding()
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlSA7BindingD1Ev(QQmlSA::Binding *self) {
  delete self;
}

//  Element QQmlSA::Binding::groupType() const
extern "C" Q_DECL_EXPORT
QQmlSA::Element *ritual_ZNK6QQmlSA7Binding9groupTypeEv(
    const QQmlSA::Binding *self) {
  return new QQmlSA::Element(self->groupType());
}

//  Element QQmlSA::Binding::bindingScope() const
extern "C" Q_DECL_EXPORT
QQmlSA::Element *ritual_ZNK6QQmlSA7Binding12bindingScopeEv(
    const QQmlSA::Binding *self) {
  return new QQmlSA::Element(self->bindingScope());
}

//  BindingType QQmlSA::Binding::bindingType() const
extern "C" Q_DECL_EXPORT
QQmlSA::BindingType ritual_ZNK6QQmlSA7Binding11bindingTypeEv(
    const QQmlSA::Binding *self) {
  return self->bindingType();
}

//  QString QQmlSA::Binding::stringValue() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK6QQmlSA7Binding11stringValueEv(
    const QQmlSA::Binding *self) {
  return new QString(self->stringValue());
}

//  QString QQmlSA::Binding::propertyName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK6QQmlSA7Binding12propertyNameEv(
    const QQmlSA::Binding *self) {
  return new QString(self->propertyName());
}

//  bool QQmlSA::Binding::isAttached() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QQmlSA7Binding10isAttachedEv(const QQmlSA::Binding *self) {
  return self->isAttached();
}

//  Element QQmlSA::Binding::attachedType() const
extern "C" Q_DECL_EXPORT
QQmlSA::Element *ritual_ZNK6QQmlSA7Binding12attachedTypeEv(
    const QQmlSA::Binding *self) {
  return new QQmlSA::Element(self->attachedType());
}

#if QT_DEPRECATED_SINCE(6, 9)
//  Element QQmlSA::Binding::attachingType() const
extern "C" Q_DECL_EXPORT
QQmlSA::Element *ritual_ZNK6QQmlSA7Binding13attachingTypeEv(
    const QQmlSA::Binding *self) {
  return new QQmlSA::Element(self->attachingType());
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

//  QQmlSA::SourceLocation QQmlSA::Binding::sourceLocation() const
extern "C" Q_DECL_EXPORT
QQmlSA::SourceLocation *ritual_ZNK6QQmlSA7Binding14sourceLocationEv(
    const QQmlSA::Binding *self) {
  return new QQmlSA::SourceLocation(self->sourceLocation());
}

//  double QQmlSA::Binding::numberValue() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK6QQmlSA7Binding11numberValueEv(
    const QQmlSA::Binding *self) {
  return self->numberValue();
}

//  ScriptBindingKind QQmlSA::Binding::scriptKind() const
extern "C" Q_DECL_EXPORT
QQmlSA::ScriptBindingKind ritual_ZNK6QQmlSA7Binding10scriptKindEv(
    const QQmlSA::Binding *self) {
  return self->scriptKind();
}

//  bool QQmlSA::Binding::hasObject() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QQmlSA7Binding9hasObjectEv(const QQmlSA::Binding *self) {
  return self->hasObject();
}

//  Element QQmlSA::Binding::objectType() const
extern "C" Q_DECL_EXPORT
QQmlSA::Element *ritual_ZNK6QQmlSA7Binding10objectTypeEv(
    const QQmlSA::Binding *self) {
  return new QQmlSA::Element(self->objectType());
}

//  bool QQmlSA::Binding::hasUndefinedScriptValue() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QQmlSA7Binding23hasUndefinedScriptValueEv(
    const QQmlSA::Binding *self) {
  return self->hasUndefinedScriptValue();
}

//  bool QQmlSA::Binding::hasFunctionScriptValue() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QQmlSA7Binding22hasFunctionScriptValueEv(
    const QQmlSA::Binding *self) {
  return self->hasFunctionScriptValue();
}

//  bool operator==(const Binding &lhs, const Binding &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlSAeqERKNS_7BindingES2_(
    const QQmlSA::Binding *lhs,
    const QQmlSA::Binding *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const Binding &lhs, const Binding &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlSAneERKNS_7BindingES2_(
    const QQmlSA::Binding *lhs,
    const QQmlSA::Binding *rhs) {
  return operator!=(*lhs, *rhs);
}

//  bool QQmlSA::Binding::isLiteralBinding(BindingType a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlSA7Binding16isLiteralBindingENS_11BindingTypeE(
    QQmlSA::BindingType a0) {
  return QQmlSA::Binding::isLiteralBinding(a0);
}

//  bool QQmlSA::Binding::operatorEqualsImpl(const Binding &a0, const Binding
//      &a1)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlSA7Binding18operatorEqualsImplERKS0_S2_(
    const QQmlSA::Binding *a0,
    const QQmlSA::Binding *a1) {
  return QQmlSA::Binding::operatorEqualsImpl(*a0, *a1);
}
