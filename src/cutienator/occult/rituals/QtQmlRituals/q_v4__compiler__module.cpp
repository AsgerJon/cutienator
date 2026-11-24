//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4compilercontext_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4compilercontext_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  QV4::Compiler::Module::Module(const QString &fileName, const QString
//      &finalUrl, bool debugMode)
extern "C" Q_DECL_EXPORT
QV4::Compiler::Module *ritual_ZN3QV48Compiler6ModuleC1ERK7QStringS4_b(
    const QString *fileName,
    const QString *finalUrl,
    bool debugMode) {
  return new QV4::Compiler::Module(*fileName, *finalUrl, debugMode);
}

//  QV4::Compiler::Module::~Module()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV48Compiler6ModuleD1Ev(QV4::Compiler::Module *self) {
  delete self;
}
