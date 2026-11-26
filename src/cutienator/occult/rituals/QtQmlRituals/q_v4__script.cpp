//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4script_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4script_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/QString>

//  QQmlRefPointer<QV4::CompiledData::CompilationUnit>
//      QV4::Script::precompile(QV4::Compiler::Module *module, QQmlJS::Engine
//      *jsEngine, Compiler::JSUnitGenerator *unitGenerator, const QString
//      &fileName, const QString &source, QList<QQmlError> *reportedErrors,
//      QV4::Compiler::ContextType contextType, InheritContext
//      inheritContext)
extern "C" Q_DECL_EXPORT
QQmlRefPointer<QV4::CompiledData::CompilationUnit> *ritual_ZN3QV46Script10precompileEPNS_8Compiler6ModuleEPN6QQmlJS6EngineEPNS1_15JSUnitGeneratorERK7QStringSB_P5QListI9QQmlErrorENS1_11ContextTypeENS0_14InheritContextE(
    QV4::Compiler::Module *module,
    QQmlJS::Engine *jsEngine,
    QV4::Compiler::JSUnitGenerator *unitGenerator,
    const QString *fileName,
    const QString *source,
    QList<QQmlError> *reportedErrors,
    QV4::Compiler::ContextType contextType,
    QV4::Script::InheritContext inheritContext) {
  return new QQmlRefPointer<QV4::CompiledData::CompilationUnit>(
      QV4::Script::precompile(
          module,
          jsEngine,
          unitGenerator,
          *fileName,
          *source,
          reportedErrors,
          contextType,
          inheritContext));
}

//  QV4::Script::Script(ExecutionContext *scope, QV4::Compiler::ContextType
//      mode, const QString &sourceCode, const QString &source, int line)
extern "C" Q_DECL_EXPORT
QV4::Script *ritual_ZN3QV46ScriptC1EPNS_16ExecutionContextENS_8Compiler11ContextTypeERK7QStringS7_i(
    QV4::ExecutionContext *scope,
    QV4::Compiler::ContextType mode,
    const QString *sourceCode,
    const QString *source,
    int line) {
  return new QV4::Script(scope, mode, *sourceCode, *source, line);
}

//  QV4::Script::Script(ExecutionEngine *engine, QmlContext *qml, bool
//      parseAsBinding, const QString &sourceCode, const QString &source, int
//      line)
extern "C" Q_DECL_EXPORT
QV4::Script *ritual_ZN3QV46ScriptC1EPNS_15ExecutionEngineEPNS_10QmlContextEbRK7QStringS7_i(
    QV4::ExecutionEngine *engine,
    QV4::QmlContext *qml,
    bool parseAsBinding,
    const QString *sourceCode,
    const QString *source,
    int line) {
  return new QV4::Script(
      engine,
      qml,
      parseAsBinding,
      *sourceCode,
      *source,
      line);
}

//  QV4::Script::Script(ExecutionEngine *engine, QmlContext *qml, const
//      QQmlRefPointer<ExecutableCompilationUnit> &compilationUnit)
extern "C" Q_DECL_EXPORT
QV4::Script *ritual_ZN3QV46ScriptC1EPNS_15ExecutionEngineEPNS_10QmlContextERK14QQmlRefPointerINS_25ExecutableCompilationUnitEE(
    QV4::ExecutionEngine *engine,
    QV4::QmlContext *qml,
    const QQmlRefPointer<QV4::ExecutableCompilationUnit> *compilationUnit) {
  return new QV4::Script(engine, qml, *compilationUnit);
}

//  QV4::Script::~Script()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV46ScriptD1Ev(QV4::Script *self) {
  delete self;
}

//  void QV4::Script::setStrictMode(bool strictMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV46Script13setStrictModeEb(
    QV4::Script *self,
    bool strictMode) {
  self->setStrictMode(strictMode);
}

//  void QV4::Script::setInheritContext(bool inheritContext)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV46Script17setInheritContextEb(
    QV4::Script *self,
    bool inheritContext) {
  self->setInheritContext(inheritContext);
}

//  void QV4::Script::setParseAsBinding(bool parseAsBinding)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV46Script17setParseAsBindingEb(
    QV4::Script *self,
    bool parseAsBinding) {
  self->setParseAsBinding(parseAsBinding);
}

//  QQmlRefPointer<ExecutableCompilationUnit> QV4::Script::compilationUnit()
//      const
extern "C" Q_DECL_EXPORT
QQmlRefPointer<QV4::ExecutableCompilationUnit> *ritual_ZNK3QV46Script15compilationUnitEv(
    const QV4::Script *self) {
  return new QQmlRefPointer<QV4::ExecutableCompilationUnit>(
      self->compilationUnit());
}

//  void QV4::Script::parse()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV46Script5parseEv(QV4::Script *self) {
  self->parse();
}

//  ReturnedValue QV4::Script::run(const QV4::Value *thisObject)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV46Script3runEPKNS_5ValueE(
    QV4::Script *self,
    const QV4::Value *thisObject) {
  return self->run(thisObject);
}

//  Function *QV4::Script::function()
extern "C" Q_DECL_EXPORT
QV4::Function *ritual_ZN3QV46Script8functionEv(QV4::Script *self) {
  return self->function();
}

//  a QQmlRefPointer<QV4::CompiledData::CompilationUnit> a ritual of
//      QV4::Script gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QV4_Script__QQmlRefPointer_QV4_CompiledData_CompilationUnit(
    QQmlRefPointer<QV4::CompiledData::CompilationUnit> *self) {
  delete self;
}

//  a QQmlRefPointer<QV4::ExecutableCompilationUnit> a ritual of QV4::Script
//      gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QV4_Script__QQmlRefPointer_QV4_ExecutableCompilationUnit(
    QQmlRefPointer<QV4::ExecutableCompilationUnit> *self) {
  delete self;
}
