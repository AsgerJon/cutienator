//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljsfunctioninitializer_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtQmlCompiler/QtQmlCompiler>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljsfunctioninitializer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4compileddata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlirbuilder_p.h>
#include <QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljscompilepass_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QQmlJSFunctionInitializer::QQmlJSFunctionInitializer(const
//      QQmlJSTypeResolver *typeResolver, const QV4::CompiledData::Location
//      &objectLocation, const QV4::CompiledData::Location &scopeLocation,
//      QQmlJSLogger *logger)
extern "C" Q_DECL_EXPORT
QQmlJSFunctionInitializer *ritual_ZN25QQmlJSFunctionInitializerC1EPK18QQmlJSTypeResolverRKN3QV412CompiledData8LocationES7_P12QQmlJSLogger(
    const QQmlJSTypeResolver *typeResolver,
    const QV4::CompiledData::Location *objectLocation,
    const QV4::CompiledData::Location *scopeLocation,
    QQmlJSLogger *logger) {
  return new QQmlJSFunctionInitializer(
      typeResolver,
      *objectLocation,
      *scopeLocation,
      logger);
}

//  QQmlJSCompilePass::Function QQmlJSFunctionInitializer::run(const
//      QV4::Compiler::Context *context, const QString &propertyName,
//      QQmlJS::AST::Node *astNode, const QmlIR::Binding &irBinding)
extern "C" Q_DECL_EXPORT
QQmlJSCompilePass::Function *ritual_ZN25QQmlJSFunctionInitializer3runEPKN3QV48Compiler7ContextERK7QStringPN6QQmlJS3AST4NodeERKN5QmlIR7BindingE(
    QQmlJSFunctionInitializer *self,
    const QV4::Compiler::Context *context,
    const QString *propertyName,
    QQmlJS::AST::Node *astNode,
    const QmlIR::Binding *irBinding) {
  return new QQmlJSCompilePass::Function(
      self->run(
          context,
          *propertyName,
          astNode,
          *irBinding));
}

//  QQmlJSCompilePass::Function QQmlJSFunctionInitializer::run(const
//      QV4::Compiler::Context *context, const QString &functionName,
//      QQmlJS::AST::Node *astNode)
extern "C" Q_DECL_EXPORT
QQmlJSCompilePass::Function *ritual_ZN25QQmlJSFunctionInitializer3runEPKN3QV48Compiler7ContextERK7QStringPN6QQmlJS3AST4NodeE(
    QQmlJSFunctionInitializer *self,
    const QV4::Compiler::Context *context,
    const QString *functionName,
    QQmlJS::AST::Node *astNode) {
  return new QQmlJSCompilePass::Function(
      self->run(
          context,
          *functionName,
          astNode));
}

//  void QQmlJSFunctionInitializer::populateSignature(const
//      QV4::Compiler::Context *context, QQmlJS::AST::FunctionExpression
//      *ast, QQmlJSCompilePass::Function *function)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQmlJSFunctionInitializer17populateSignatureEPKN3QV48Compiler7ContextEPN6QQmlJS3AST18FunctionExpressionEPN17QQmlJSCompilePass8FunctionE(
    QQmlJSFunctionInitializer *self,
    const QV4::Compiler::Context *context,
    QQmlJS::AST::FunctionExpression *ast,
    QQmlJSCompilePass::Function *function) {
  self->populateSignature(context, ast, function);
}
