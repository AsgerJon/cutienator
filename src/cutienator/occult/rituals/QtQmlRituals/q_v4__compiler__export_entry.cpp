//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4compilercontext_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4compilercontext_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  bool QV4::Compiler::ExportEntry::lessThan(const ExportEntry &lhs, const
//      ExportEntry &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler11ExportEntry8lessThanERKS1_S3_(
    const QV4::Compiler::ExportEntry *lhs,
    const QV4::Compiler::ExportEntry *rhs) {
  return QV4::Compiler::ExportEntry::lessThan(*lhs, *rhs);
}

//  QV4::Compiler::ExportEntry::~ExportEntry()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV48Compiler11ExportEntryD1Ev(
    QV4::Compiler::ExportEntry *self) {
  delete self;
}
