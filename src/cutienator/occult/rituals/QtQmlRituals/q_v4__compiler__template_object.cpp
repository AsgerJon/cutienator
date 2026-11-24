//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4compilercontext_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4compilercontext_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  bool QV4::Compiler::TemplateObject::operator==(const TemplateObject
//      &other)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler14TemplateObjecteqERKS1_(
    QV4::Compiler::TemplateObject *self,
    const QV4::Compiler::TemplateObject *other) {
  return self->operator==(*other);
}

//  QV4::Compiler::TemplateObject::~TemplateObject()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV48Compiler14TemplateObjectD1Ev(
    QV4::Compiler::TemplateObject *self) {
  delete self;
}
