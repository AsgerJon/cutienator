//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4compilercontext_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4compilercontext_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  QV4::Compiler::Context::Context(Context *parent, ContextType type)
extern "C" Q_DECL_EXPORT
QV4::Compiler::Context *ritual_ZN3QV48Compiler7ContextC1EPS1_NS0_11ContextTypeE(
    QV4::Compiler::Context *parent,
    QV4::Compiler::ContextType type) {
  return new QV4::Compiler::Context(parent, type);
}

//  bool QV4::Compiler::Context::hasArgument(const QString &name) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV48Compiler7Context11hasArgumentERK7QString(
    const QV4::Compiler::Context *self,
    const QString *name) {
  return self->hasArgument(*name);
}

//  int QV4::Compiler::Context::findArgument(const QString &name, bool
//      *isInjected) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK3QV48Compiler7Context12findArgumentERK7QStringPb(
    const QV4::Compiler::Context *self,
    const QString *name,
    bool *isInjected) {
  return self->findArgument(*name, isInjected);
}

//  Member QV4::Compiler::Context::findMember(const QString &name) const
extern "C" Q_DECL_EXPORT
QV4::Compiler::Context::Member *ritual_ZNK3QV48Compiler7Context10findMemberERK7QString(
    const QV4::Compiler::Context *self,
    const QString *name) {
  return new QV4::Compiler::Context::Member(self->findMember(*name));
}

//  bool QV4::Compiler::Context::requiresImplicitReturnValue() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV48Compiler7Context27requiresImplicitReturnValueEv(
    const QV4::Compiler::Context *self) {
  return self->requiresImplicitReturnValue();
}

//  void QV4::Compiler::Context::addUsedVariable(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV48Compiler7Context15addUsedVariableERK7QString(
    QV4::Compiler::Context *self,
    const QString *name) {
  self->addUsedVariable(*name);
}

//  bool QV4::Compiler::Context::canHaveTailCalls() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV48Compiler7Context16canHaveTailCallsEv(
    const QV4::Compiler::Context *self) {
  return self->canHaveTailCalls();
}

//  bool QV4::Compiler::Context::isCaseBlock() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV48Compiler7Context11isCaseBlockEv(
    const QV4::Compiler::Context *self) {
  return self->isCaseBlock();
}
