//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4runtimecodegen_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4runtimecodegen_p.h>
#include <QtQml/6.12.0/QtQml/private/qqmljssourcelocation_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qv4engine_p.h>
#include <QtQml/private/qv4runtimecodegen_p.h>
#include <QtQml/private/qv4compilerscanfunctions_p.h>
#include <QtQml/private/qv4compilerscanfunctions_p.h>
#include <QtCore/QCoreApplication>
#include <QtCore/QStringList>
#include <QtCore/QSet>
#include <QtCore/QBuffer>
#include <QtCore/QBitArray>
#include <QtCore/QStack>
#include <QtQml/private/qqmljsast_p.h>
#include <QtQml/private/qv4compilercontext_p.h>
#include <QtQml/private/qv4codegen_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/jsruntime/qv4runtimecodegen.cpp, line 31, as _ZN3QV414RuntimeCodegen16throwSyntaxErrorERKN6QQmlJS14SourceLocationERK7QString
namespace QV4 {
using namespace QQmlJS;
inline void RuntimeCodegen::throwSyntaxError(const SourceLocation &loc, const QString &detail)
{
    if (hasError())
        return;

    Codegen::throwSyntaxError(loc, detail);
    engine->throwSyntaxError(detail, _module->fileName, loc.startLine, loc.startColumn);
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4runtimecodegen.cpp, line 40, as _ZN3QV414RuntimeCodegen19throwReferenceErrorERKN6QQmlJS14SourceLocationERK7QString
namespace QV4 {
using namespace QQmlJS;
inline void RuntimeCodegen::throwReferenceError(const SourceLocation &loc, const QString &detail)
{
    if (hasError())
        return;

    Codegen::throwReferenceError(loc, detail);
    engine->throwReferenceError(detail, _module->fileName, loc.startLine, loc.startColumn);
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/compiler/qv4compilerscanfunctions.cpp, line 52, as _ZN3QV48Compiler13ScanFunctions16enterEnvironmentEPN6QQmlJS3AST4NodeENS0_11ContextTypeERK7QString
namespace QV4::Compiler {
using namespace QV4;
using namespace QQmlJS;
using namespace QQmlJS::AST;
inline void ScanFunctions::enterEnvironment(Node *node, ContextType compilationMode, const QString &name)
{
    Context *c = _cg->_module->contextMap.value(node);
    if (!c)
        c = _cg->_module->newContext(node, _context, compilationMode);
    if (!c->isStrict)
        c->isStrict = _cg->_strictMode;
    c->name = name;
    _contextStack.append(c);
    _context = c;
}
}  // namespace QV4::Compiler

//  from ../qtdeclarative/src/qml/compiler/qv4compilerscanfunctions.cpp, line 64, as _ZN3QV48Compiler13ScanFunctions16leaveEnvironmentEv
namespace QV4::Compiler {
using namespace QV4;
using namespace QQmlJS;
using namespace QQmlJS::AST;
inline void ScanFunctions::leaveEnvironment()
{
    _contextStack.pop();
    _context = _contextStack.isEmpty() ? nullptr : _contextStack.top();
}
}  // namespace QV4::Compiler

//  from ../qtdeclarative/src/qml/compiler/qv4compilerscanfunctions.cpp, line 29, as _ZN3QV48Compiler13ScanFunctionsC1EPNS0_7CodegenERK7QStringNS0_11ContextTypeE
namespace QV4::Compiler {
using namespace QV4;
using namespace QQmlJS;
using namespace QQmlJS::AST;
inline ScanFunctions::ScanFunctions(Codegen *cg, const QString &sourceCode, ContextType defaultProgramType)
    : QQmlJS::AST::Visitor(cg->recursionDepth())
    , _cg(cg)
    , _sourceCode(sourceCode)
    , _context(nullptr)
    , _allowFuncDecls(true)
    , defaultProgramType(defaultProgramType)
{
}
}  // namespace QV4::Compiler
//  -----------------------------------------------------------------------

//  QV4::RuntimeCodegen::RuntimeCodegen(ExecutionEngine *engine,
//      Compiler::JSUnitGenerator *jsUnitGenerator, bool strict)
extern "C" Q_DECL_EXPORT
QV4::RuntimeCodegen *ritual_ZN3QV414RuntimeCodegenC1EPNS_15ExecutionEngineEPNS_8Compiler15JSUnitGeneratorEb(
    QV4::ExecutionEngine *engine,
    QV4::Compiler::JSUnitGenerator *jsUnitGenerator,
    bool strict) {
  return new QV4::RuntimeCodegen(engine, jsUnitGenerator, strict);
}

//  void QV4::RuntimeCodegen::throwSyntaxError(const QQmlJS::SourceLocation
//      &loc, const QString &detail)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV414RuntimeCodegen16throwSyntaxErrorERKN6QQmlJS14SourceLocationERK7QString(
    QV4::RuntimeCodegen *self,
    const QQmlJS::SourceLocation *loc,
    const QString *detail) {
  self->throwSyntaxError(*loc, *detail);
}

//  void QV4::RuntimeCodegen::throwReferenceError(const
//      QQmlJS::SourceLocation &loc, const QString &detail)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV414RuntimeCodegen19throwReferenceErrorERKN6QQmlJS14SourceLocationERK7QString(
    QV4::RuntimeCodegen *self,
    const QQmlJS::SourceLocation *loc,
    const QString *detail) {
  self->throwReferenceError(*loc, *detail);
}

//  void QV4::RuntimeCodegen::throwSyntaxError(const QQmlJS::SourceLocation
//      &loc, const QString &detail)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN3QV414RuntimeCodegen16throwSyntaxErrorERKN6QQmlJS14SourceLocationERK7QString(
    QV4::RuntimeCodegen *self,
    const QQmlJS::SourceLocation *loc,
    const QString *detail) {
  self->QV4::RuntimeCodegen::throwSyntaxError(*loc, *detail);
}

//  void QV4::RuntimeCodegen::throwReferenceError(const
//      QQmlJS::SourceLocation &loc, const QString &detail)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN3QV414RuntimeCodegen19throwReferenceErrorERKN6QQmlJS14SourceLocationERK7QString(
    QV4::RuntimeCodegen *self,
    const QQmlJS::SourceLocation *loc,
    const QString *detail) {
  self->QV4::RuntimeCodegen::throwReferenceError(*loc, *detail);
}
