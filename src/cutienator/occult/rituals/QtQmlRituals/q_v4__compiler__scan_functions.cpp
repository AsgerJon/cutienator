//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4compilerscanfunctions_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4compilerscanfunctions_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void QV4::Compiler::ScanFunctions::handleTopLevelFunctionFormals(QQmlJS::
//      AST::FunctionExpression *node)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV48Compiler13ScanFunctions29handleTopLevelFunctionFormalsEPN6QQmlJS3AST18FunctionExpressionE(
    QV4::Compiler::ScanFunctions *self,
    QQmlJS::AST::FunctionExpression *node) {
  self->handleTopLevelFunctionFormals(node);
}

//  QV4::Compiler::ScanFunctions::~ScanFunctions()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV48Compiler13ScanFunctionsD1Ev(
    QV4::Compiler::ScanFunctions *self) {
  delete self;
}
