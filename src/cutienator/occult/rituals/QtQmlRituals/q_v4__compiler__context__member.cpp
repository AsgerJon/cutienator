//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4compilercontext_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4compilercontext_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  bool QV4::Compiler::Context::Member::isLexicallyScoped() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV48Compiler7Context6Member17isLexicallyScopedEv(
    const QV4::Compiler::Context::Member *self) {
  return self->isLexicallyScoped();
}

//  QV4::Compiler::Context::Member::~Member()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV48Compiler7Context6MemberD1Ev(
    QV4::Compiler::Context::Member *self) {
  delete self;
}
