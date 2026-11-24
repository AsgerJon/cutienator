//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4function_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4function_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>

//  QV4::ExecutableCompilationUnit
//      *QV4::Function::executableCompilationUnit() const
extern "C" Q_DECL_EXPORT
QV4::ExecutableCompilationUnit *ritual_ZNK3QV48Function25executableCompilationUnitEv(
    const QV4::Function *self) {
  return self->executableCompilationUnit();
}

//  QV4::Heap::String *QV4::Function::runtimeString(uint i) const
extern "C" Q_DECL_EXPORT
QV4::Heap::String *ritual_ZNK3QV48Function13runtimeStringEj(
    const QV4::Function *self,
    uint i) {
  return self->runtimeString(i);
}

//  Function *QV4::Function::create(ExecutionEngine *engine,
//      ExecutableCompilationUnit *unit, const CompiledData::Function
//      *function, const QQmlPrivate::AOTCompiledFunction *aotFunction)
extern "C" Q_DECL_EXPORT
QV4::Function *ritual_ZN3QV48Function6createEPNS_15ExecutionEngineEPNS_25ExecutableCompilationUnitEPKNS_12CompiledData8FunctionEPKN11QQmlPrivate19AOTCompiledFunctionE(
    QV4::ExecutionEngine *engine,
    QV4::ExecutableCompilationUnit *unit,
    const QV4::CompiledData::Function *function,
    const QQmlPrivate::AOTCompiledFunction *aotFunction) {
  return QV4::Function::create(engine, unit, function, aotFunction);
}

//  Heap::String *QV4::Function::name() const
extern "C" Q_DECL_EXPORT
QV4::Heap::String *ritual_ZNK3QV48Function4nameEv(
    const QV4::Function *self) {
  return self->name();
}

//  QString QV4::Function::sourceFile() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK3QV48Function10sourceFileEv(const QV4::Function *self) {
  return new QString(self->sourceFile());
}

//  QUrl QV4::Function::finalUrl() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK3QV48Function8finalUrlEv(const QV4::Function *self) {
  return new QUrl(self->finalUrl());
}

//  bool QV4::Function::isStrict() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV48Function8isStrictEv(const QV4::Function *self) {
  return self->isStrict();
}

//  bool QV4::Function::isArrowFunction() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV48Function15isArrowFunctionEv(const QV4::Function *self) {
  return self->isArrowFunction();
}

//  bool QV4::Function::isGenerator() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV48Function11isGeneratorEv(const QV4::Function *self) {
  return self->isGenerator();
}

//  bool QV4::Function::isClosureWrapper() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV48Function16isClosureWrapperEv(const QV4::Function *self) {
  return self->isClosureWrapper();
}

//  Function *QV4::Function::nestedFunction() const
extern "C" Q_DECL_EXPORT
QV4::Function *ritual_ZNK3QV48Function14nestedFunctionEv(
    const QV4::Function *self) {
  return self->nestedFunction();
}

//  bool QV4::Function::isJittable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV48Function10isJittableEv(const QV4::Function *self) {
  return self->isJittable();
}
