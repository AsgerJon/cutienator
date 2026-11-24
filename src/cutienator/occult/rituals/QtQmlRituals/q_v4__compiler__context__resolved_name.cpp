//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4compilercontext_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4compilercontext_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  bool QV4::Compiler::Context::ResolvedName::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV48Compiler7Context12ResolvedName7isValidEv(
    const QV4::Compiler::Context::ResolvedName *self) {
  return self->isValid();
}

//  QV4::Compiler::Context::ResolvedName::~ResolvedName()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV48Compiler7Context12ResolvedNameD1Ev(
    QV4::Compiler::Context::ResolvedName *self) {
  delete self;
}
