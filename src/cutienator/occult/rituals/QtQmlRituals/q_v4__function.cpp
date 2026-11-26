//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4function_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4function_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlglobal_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qlist.h>

//  QV4::Function::Function(ExecutionEngine *engine,
//      ExecutableCompilationUnit *unit, const CompiledData::Function
//      *function, const QQmlPrivate::AOTCompiledFunction *aotFunction)
extern "C" Q_DECL_EXPORT
QV4::Function *ritual_ZN3QV48FunctionC1EPNS_15ExecutionEngineEPNS_25ExecutableCompilationUnitEPKNS_12CompiledData8FunctionEPKN11QQmlPrivate19AOTCompiledFunctionE(
    QV4::ExecutionEngine *engine,
    QV4::ExecutableCompilationUnit *unit,
    const QV4::CompiledData::Function *function,
    const QQmlPrivate::AOTCompiledFunction *aotFunction) {
  return new QV4::Function(engine, unit, function, aotFunction);
}

//  QV4::Function::~Function()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV48FunctionD1Ev(QV4::Function *self) {
  delete self;
}

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

//  bool QV4::Function::call(QObject *thisObject, void **a, const QMetaType
//      *types, int argc, ExecutionContext *context)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Function4callEP7QObjectPPvPK9QMetaTypeiPNS_16ExecutionContextE(
    QV4::Function *self,
    QObject *thisObject,
    void **a,
    const QMetaType *types,
    int argc,
    QV4::ExecutionContext *context) {
  return self->call(thisObject, a, types, argc, context);
}

//  ReturnedValue QV4::Function::call(const Value *thisObject, const Value
//      *argv, int argc, ExecutionContext *context)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV48Function4callEPKNS_5ValueES3_iPNS_16ExecutionContextE(
    QV4::Function *self,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc,
    QV4::ExecutionContext *context) {
  return self->call(thisObject, argv, argc, context);
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

//  void QV4::Function::destroy()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV48Function7destroyEv(QV4::Function *self) {
  self->destroy();
}

//  void QV4::Function::mark(QV4::MarkStack *ms)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV48Function4markEPNS_9MarkStackE(
    QV4::Function *self,
    QV4::MarkStack *ms) {
  self->mark(ms);
}

//  void QV4::Function::updateInternalClass(ExecutionEngine *engine, const
//      QList<QByteArray> &parameters)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV48Function19updateInternalClassEPNS_15ExecutionEngineERK5QListI10QByteArrayE(
    QV4::Function *self,
    QV4::ExecutionEngine *engine,
    const QList<QByteArray> *parameters) {
  self->updateInternalClass(engine, *parameters);
}

//  Heap::String *QV4::Function::name() const
extern "C" Q_DECL_EXPORT
QV4::Heap::String *ritual_ZNK3QV48Function4nameEv(
    const QV4::Function *self) {
  return self->name();
}

//  QString QV4::Function::prettyName(const Function *function, const void
//      *address)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN3QV48Function10prettyNameEPKS0_PKv(
    const QV4::Function *function,
    const void *address) {
  return new QString(QV4::Function::prettyName(function, address));
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

//  QQmlSourceLocation QV4::Function::sourceLocation() const
extern "C" Q_DECL_EXPORT
QQmlSourceLocation *ritual_ZNK3QV48Function14sourceLocationEv(
    const QV4::Function *self) {
  return new QQmlSourceLocation(self->sourceLocation());
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
