//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4codegen_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4codegen_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QV4::Compiler::Codegen::RegisterScope::RegisterScope(Codegen *cg)
extern "C" Q_DECL_EXPORT
QV4::Compiler::Codegen::RegisterScope *ritual_ZN3QV48Compiler7Codegen13RegisterScopeC1EPS1_(
    QV4::Compiler::Codegen *cg) {
  return new QV4::Compiler::Codegen::RegisterScope(cg);
}

//  QV4::Compiler::Codegen::RegisterScope::~RegisterScope()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV48Compiler7Codegen13RegisterScopeD1Ev(
    QV4::Compiler::Codegen::RegisterScope *self) {
  delete self;
}
