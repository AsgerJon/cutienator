//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4compilerscanfunctions_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4compilerscanfunctions_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qstringview.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmljssourcelocation_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
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
#include <QtQml/private/qv4codegen_p.h>
#include <QtQml/private/qv4compilercontext_p.h>
#include <QtQml/private/qv4bytecodegenerator_p.h>
#include <QtQml/private/qv4calldata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/compiler/qv4compilerscanfunctions.cpp, line 723, as local:qv4compilerscanfunctions.cpp:Iteration
enum class Iteration { Continue, Break };

//  from ../qtdeclarative/src/qml/compiler/qv4compilerscanfunctions.cpp, line 113, as _ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST7ProgramE
namespace QV4::Compiler {
using namespace QV4;
using namespace QQmlJS;
using namespace QQmlJS::AST;
inline bool ScanFunctions::visit(Program *ast)
{
    enterEnvironment(ast, defaultProgramType, QStringLiteral("%ProgramCode"));
    checkDirectivePrologue(ast->statements);
    return true;
}
}  // namespace QV4::Compiler

//  from ../qtdeclarative/src/qml/compiler/qv4compilerscanfunctions.cpp, line 120, as _ZN3QV48Compiler13ScanFunctions8endVisitEPN6QQmlJS3AST7ProgramE
namespace QV4::Compiler {
using namespace QV4;
using namespace QQmlJS;
using namespace QQmlJS::AST;
inline void ScanFunctions::endVisit(Program *)
{
    leaveEnvironment();
}
}  // namespace QV4::Compiler

//  from ../qtdeclarative/src/qml/compiler/qv4compilerscanfunctions.cpp, line 125, as _ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST8ESModuleE
namespace QV4::Compiler {
using namespace QV4;
using namespace QQmlJS;
using namespace QQmlJS::AST;
inline bool ScanFunctions::visit(ESModule *ast)
{
    enterEnvironment(ast, defaultProgramType, QStringLiteral("%ModuleCode"));
    Q_ASSERT(_context);
    _context->isStrict = true;
    return true;
}
}  // namespace QV4::Compiler

//  from ../qtdeclarative/src/qml/compiler/qv4compilerscanfunctions.cpp, line 133, as _ZN3QV48Compiler13ScanFunctions8endVisitEPN6QQmlJS3AST8ESModuleE
namespace QV4::Compiler {
using namespace QV4;
using namespace QQmlJS;
using namespace QQmlJS::AST;
inline void ScanFunctions::endVisit(ESModule *)
{
    leaveEnvironment();
}
}  // namespace QV4::Compiler

//  from ../qtdeclarative/src/qml/compiler/qv4compilerscanfunctions.cpp, line 280, as _ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST14CallExpressionE
namespace QV4::Compiler {
using namespace QV4;
using namespace QQmlJS;
using namespace QQmlJS::AST;
inline bool ScanFunctions::visit(CallExpression *ast)
{
    Q_ASSERT(_context);
    if (!_context->hasDirectEval) {
        if (IdentifierExpression *id = cast<IdentifierExpression *>(ast->base)) {
            if (id->name == QLatin1String("eval")) {
                if (_context->usesArgumentsObject == Context::UsesArgumentsObject::Unknown)
                    _context->usesArgumentsObject = Context::UsesArgumentsObject::Used;
                _context->hasDirectEval = true;
            }
        }
    }
    return true;
}
}  // namespace QV4::Compiler

//  from ../qtdeclarative/src/qml/compiler/qv4compilerscanfunctions.cpp, line 295, as _ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST14PatternElementE
namespace QV4::Compiler {
using namespace QV4;
using namespace QQmlJS;
using namespace QQmlJS::AST;
inline bool ScanFunctions::visit(PatternElement *ast)
{
    Q_ASSERT(_context);
    if (!ast->isVariableDeclaration())
        return true;

    BoundNames names;
    ast->boundNames(&names);

    QQmlJS::SourceLocation declarationLocation = ast->firstSourceLocation();
    if (_context->lastBlockInitializerLocation.isValid()) {
        declarationLocation.length = _context->lastBlockInitializerLocation.end()
                - declarationLocation.offset;
    } else {
        declarationLocation.length = ast->lastSourceLocation().end() - declarationLocation.offset;
    }

    for (const auto &name : std::as_const(names)) {
        if (_context->isStrict && (name.id == QLatin1String("eval") || name.id == QLatin1String("arguments")))
            _cg->throwSyntaxError(ast->identifierToken, QStringLiteral("Variable name may not be eval or arguments in strict mode"));
        checkName(QStringView(name.id), ast->identifierToken);
        if (name.id == QLatin1String("arguments"))
            _context->usesArgumentsObject = Context::UsesArgumentsObject::NotUsed;
        if (ast->scope == VariableScope::Const && !ast->initializer && !ast->isForDeclaration && !ast->destructuringPattern()) {
            _cg->throwSyntaxError(ast->identifierToken, QStringLiteral("Missing initializer in const declaration"));
            return false;
        }
        if (!_context->addLocalVar(name.id, ast->initializer ? Context::VariableDefinition : Context::VariableDeclaration, ast->scope,
                                   /*function*/nullptr, declarationLocation)) {
            _cg->throwSyntaxError(ast->identifierToken, QStringLiteral("Identifier %1 has already been declared").arg(name.id));
            return false;
        }
    }
    return true;
}
}  // namespace QV4::Compiler

//  from ../qtdeclarative/src/qml/compiler/qv4compilerscanfunctions.cpp, line 331, as _ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST20IdentifierExpressionE
namespace QV4::Compiler {
using namespace QV4;
using namespace QQmlJS;
using namespace QQmlJS::AST;
inline bool ScanFunctions::visit(IdentifierExpression *ast)
{
    Q_ASSERT(_context);
    checkName(ast->name, ast->identifierToken);
    if (_context->usesArgumentsObject == Context::UsesArgumentsObject::Unknown && ast->name == QLatin1String("arguments"))
        _context->usesArgumentsObject = Context::UsesArgumentsObject::Used;
    _context->addUsedVariable(ast->name.toString());
    return true;
}
}  // namespace QV4::Compiler

//  from ../qtdeclarative/src/qml/compiler/qv4compilerscanfunctions.cpp, line 341, as _ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST19ExpressionStatementE
namespace QV4::Compiler {
using namespace QV4;
using namespace QQmlJS;
using namespace QQmlJS::AST;
inline bool ScanFunctions::visit(ExpressionStatement *ast)
{
    if (FunctionExpression* expr = AST::cast<AST::FunctionExpression*>(ast->expression)) {
        if (!_allowFuncDecls)
            _cg->throwSyntaxError(expr->functionToken, QStringLiteral("conditional function or closure declaration"));

        if (!enterFunction(expr, expr->identifierToken.length > 0
                                ? FunctionNameContext::Inner
                                : FunctionNameContext::None)) {
            return false;
        }
        Node::accept(expr->formals, this);
        Node::accept(expr->body, this);
        leaveEnvironment();
        return false;
    } else {
        SourceLocation firstToken = ast->firstSourceLocation();
        if (QStringView{_sourceCode}.mid(firstToken.offset, firstToken.length) == QLatin1String("function")) {
            _cg->throwSyntaxError(firstToken, QStringLiteral("unexpected token"));
        }
    }
    return true;
}
}  // namespace QV4::Compiler

//  from ../qtdeclarative/src/qml/compiler/qv4compilerscanfunctions.cpp, line 365, as _ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST18FunctionExpressionE
namespace QV4::Compiler {
using namespace QV4;
using namespace QQmlJS;
using namespace QQmlJS::AST;
inline bool ScanFunctions::visit(FunctionExpression *ast)
{
    return enterFunction(ast, ast->identifierToken.length > 0
                                ? FunctionNameContext::Inner
                                : FunctionNameContext::None);
}
}  // namespace QV4::Compiler

//  from ../qtdeclarative/src/qml/compiler/qv4compilerscanfunctions.cpp, line 407, as _ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST15TemplateLiteralE
namespace QV4::Compiler {
using namespace QV4;
using namespace QQmlJS;
using namespace QQmlJS::AST;
inline bool ScanFunctions::visit(TemplateLiteral *ast)
{
    while (ast) {
        if (ast->expression)
            Node::accept(ast->expression, this);
        ast = ast->next;
    }
    return true;

}
}  // namespace QV4::Compiler

//  from ../qtdeclarative/src/qml/compiler/qv4compilerscanfunctions.cpp, line 418, as _ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST12SuperLiteralE
namespace QV4::Compiler {
using namespace QV4;
using namespace QQmlJS;
using namespace QQmlJS::AST;
inline bool ScanFunctions::visit(SuperLiteral *)
{
    Q_ASSERT(_context);
    Context *c = _context;
    bool needContext = false;
    while (c->contextType == ContextType::Block || c->isArrowFunction) {
        needContext |= c->isArrowFunction;
        c = c->parent;
    }

    c->requiresExecutionContext |= needContext;

    return false;
}
}  // namespace QV4::Compiler

//  from ../qtdeclarative/src/qml/compiler/qv4compilerscanfunctions.cpp, line 433, as _ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST21FieldMemberExpressionE
namespace QV4::Compiler {
using namespace QV4;
using namespace QQmlJS;
using namespace QQmlJS::AST;
inline bool ScanFunctions::visit(FieldMemberExpression *ast)
{
    if (AST::IdentifierExpression *id = AST::cast<AST::IdentifierExpression *>(ast->base)) {
        if (id->name == QLatin1String("new")) {
            // new.target
            if (ast->name != QLatin1String("target")) {
                _cg->throwSyntaxError(ast->identifierToken, QLatin1String("Expected 'target' after 'new.'."));
                return false;
            }
            Q_ASSERT(_context);
            Context *c = _context;
            bool needContext = false;
            while (c->contextType == ContextType::Block || c->isArrowFunction) {
                needContext |= c->isArrowFunction;
                c = c->parent;
            }
            c->requiresExecutionContext |= needContext;
            c->innerFunctionAccessesNewTarget |= needContext;

            return false;
        }
    }

    return true;
}
}  // namespace QV4::Compiler

//  from ../qtdeclarative/src/qml/compiler/qv4compilerscanfunctions.cpp, line 459, as _ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST12ArrayPatternE
namespace QV4::Compiler {
using namespace QV4;
using namespace QQmlJS;
using namespace QQmlJS::AST;
inline bool ScanFunctions::visit(ArrayPattern *ast)
{
    for (PatternElementList *it = ast->elements; it; it = it->next)
        Node::accept(it->element, this);

    return false;
}
}  // namespace QV4::Compiler

//  from ../qtdeclarative/src/qml/compiler/qv4compilerscanfunctions.cpp, line 475, as _ZN3QV48Compiler13ScanFunctions8endVisitEPN6QQmlJS3AST18FunctionExpressionE
namespace QV4::Compiler {
using namespace QV4;
using namespace QQmlJS;
using namespace QQmlJS::AST;
inline void ScanFunctions::endVisit(FunctionExpression *)
{
    leaveEnvironment();
}
}  // namespace QV4::Compiler

//  from ../qtdeclarative/src/qml/compiler/qv4compilerscanfunctions.cpp, line 480, as _ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST13ObjectPatternE
namespace QV4::Compiler {
using namespace QV4;
using namespace QQmlJS;
using namespace QQmlJS::AST;
inline bool ScanFunctions::visit(ObjectPattern *ast)
{
    TemporaryBoolAssignment allowFuncDecls(_allowFuncDecls, true);
    Node::accept(ast->properties, this);
    return false;
}
}  // namespace QV4::Compiler

//  from ../qtdeclarative/src/qml/compiler/qv4compilerscanfunctions.cpp, line 487, as _ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST15PatternPropertyE
namespace QV4::Compiler {
using namespace QV4;
using namespace QQmlJS;
using namespace QQmlJS::AST;
inline bool ScanFunctions::visit(PatternProperty *ast)
{
    Q_UNUSED(ast);
    // ### Shouldn't be required anymore
//    if (ast->type == PatternProperty::Getter || ast->type == PatternProperty::Setter) {
//        TemporaryBoolAssignment allowFuncDecls(_allowFuncDecls, true);
//        return enterFunction(ast, QString(), ast->formals, ast->functionBody, /*enterName */ false);
//    }
    return true;
}
}  // namespace QV4::Compiler

//  from ../qtdeclarative/src/qml/compiler/qv4compilerscanfunctions.cpp, line 498, as _ZN3QV48Compiler13ScanFunctions8endVisitEPN6QQmlJS3AST15PatternPropertyE
namespace QV4::Compiler {
using namespace QV4;
using namespace QQmlJS;
using namespace QQmlJS::AST;
inline void ScanFunctions::endVisit(PatternProperty *)
{
    // ###
//    if (ast->type == PatternProperty::Getter || ast->type == PatternProperty::Setter)
//        leaveEnvironment();
}
}  // namespace QV4::Compiler

//  from ../qtdeclarative/src/qml/compiler/qv4compilerscanfunctions.cpp, line 505, as _ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST19FunctionDeclarationE
namespace QV4::Compiler {
using namespace QV4;
using namespace QQmlJS;
using namespace QQmlJS::AST;
inline bool ScanFunctions::visit(FunctionDeclaration *ast)
{
    return enterFunction(ast, FunctionNameContext::Outer);
}
}  // namespace QV4::Compiler

//  from ../qtdeclarative/src/qml/compiler/qv4compilerscanfunctions.cpp, line 510, as _ZN3QV48Compiler13ScanFunctions8endVisitEPN6QQmlJS3AST19FunctionDeclarationE
namespace QV4::Compiler {
using namespace QV4;
using namespace QQmlJS;
using namespace QQmlJS::AST;
inline void ScanFunctions::endVisit(FunctionDeclaration *)
{
    leaveEnvironment();
}
}  // namespace QV4::Compiler

//  from ../qtdeclarative/src/qml/compiler/qv4compilerscanfunctions.cpp, line 372, as _ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST15ClassExpressionE
namespace QV4::Compiler {
using namespace QV4;
using namespace QQmlJS;
using namespace QQmlJS::AST;
inline bool ScanFunctions::visit(ClassExpression *ast)
{
    enterEnvironment(ast, ContextType::Block, QStringLiteral("%Class"));
    Q_ASSERT(_context);
    _context->isStrict = true;
    _context->hasNestedFunctions = true;
    if (!ast->name.isEmpty())
        _context->addLocalVar(ast->name.toString(), Context::VariableDefinition, AST::VariableScope::Const);
    return true;
}
}  // namespace QV4::Compiler

//  from ../qtdeclarative/src/qml/compiler/qv4compilerscanfunctions.cpp, line 383, as _ZN3QV48Compiler13ScanFunctions8endVisitEPN6QQmlJS3AST15ClassExpressionE
namespace QV4::Compiler {
using namespace QV4;
using namespace QQmlJS;
using namespace QQmlJS::AST;
inline void ScanFunctions::endVisit(ClassExpression *)
{
    leaveEnvironment();
}
}  // namespace QV4::Compiler

//  from ../qtdeclarative/src/qml/compiler/qv4compilerscanfunctions.cpp, line 388, as _ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST16ClassDeclarationE
namespace QV4::Compiler {
using namespace QV4;
using namespace QQmlJS;
using namespace QQmlJS::AST;
inline bool ScanFunctions::visit(ClassDeclaration *ast)
{
    Q_ASSERT(_context);
    if (!ast->name.isEmpty())
        _context->addLocalVar(ast->name.toString(), Context::VariableDeclaration, AST::VariableScope::Let);

    enterEnvironment(ast, ContextType::Block, QStringLiteral("%Class"));
    _context->isStrict = true;
    _context->hasNestedFunctions = true;
    if (!ast->name.isEmpty())
        _context->addLocalVar(ast->name.toString(), Context::VariableDefinition, AST::VariableScope::Const);
    return true;
}
}  // namespace QV4::Compiler

//  from ../qtdeclarative/src/qml/compiler/qv4compilerscanfunctions.cpp, line 402, as _ZN3QV48Compiler13ScanFunctions8endVisitEPN6QQmlJS3AST16ClassDeclarationE
namespace QV4::Compiler {
using namespace QV4;
using namespace QQmlJS;
using namespace QQmlJS::AST;
inline void ScanFunctions::endVisit(ClassDeclaration *)
{
    leaveEnvironment();
}
}  // namespace QV4::Compiler

//  from ../qtdeclarative/src/qml/compiler/qv4compilerscanfunctions.cpp, line 515, as _ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST16DoWhileStatementE
namespace QV4::Compiler {
using namespace QV4;
using namespace QQmlJS;
using namespace QQmlJS::AST;
inline bool ScanFunctions::visit(DoWhileStatement *ast) {
    {
        TemporaryBoolAssignment allowFuncDecls(_allowFuncDecls, !_context->isStrict);
        Node::accept(ast->statement, this);
    }
    Node::accept(ast->expression, this);
    return false;
}
}  // namespace QV4::Compiler

//  from ../qtdeclarative/src/qml/compiler/qv4compilerscanfunctions.cpp, line 524, as _ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST12ForStatementE
namespace QV4::Compiler {
using namespace QV4;
using namespace QQmlJS;
using namespace QQmlJS::AST;
inline bool ScanFunctions::visit(ForStatement *ast) {
    enterEnvironment(ast, ContextType::Block, QStringLiteral("%For"));
    Node::accept(ast->initialiser, this);
    Node::accept(ast->declarations, this);
    Node::accept(ast->condition, this);
    Node::accept(ast->expression, this);

    TemporaryBoolAssignment allowFuncDecls(_allowFuncDecls, !_context->isStrict);
    Node::accept(ast->statement, this);

    return false;
}
}  // namespace QV4::Compiler

//  from ../qtdeclarative/src/qml/compiler/qv4compilerscanfunctions.cpp, line 537, as _ZN3QV48Compiler13ScanFunctions8endVisitEPN6QQmlJS3AST12ForStatementE
namespace QV4::Compiler {
using namespace QV4;
using namespace QQmlJS;
using namespace QQmlJS::AST;
inline void ScanFunctions::endVisit(ForStatement *)
{
    leaveEnvironment();
}
}  // namespace QV4::Compiler

//  from ../qtdeclarative/src/qml/compiler/qv4compilerscanfunctions.cpp, line 542, as _ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST16ForEachStatementE
namespace QV4::Compiler {
using namespace QV4;
using namespace QQmlJS;
using namespace QQmlJS::AST;
inline bool ScanFunctions::visit(ForEachStatement *ast)
{
    enterEnvironment(ast, ContextType::Block, QStringLiteral("%Foreach"));
    if (ast->expression) {
        Q_ASSERT(_context);
        _context->lastBlockInitializerLocation = ast->expression->lastSourceLocation();
    }
    Node::accept(ast->lhs, this);
    Node::accept(ast->expression, this);

    TemporaryBoolAssignment allowFuncDecls(_allowFuncDecls, !_context->isStrict);
    Node::accept(ast->statement, this);

    return false;
}
}  // namespace QV4::Compiler

//  from ../qtdeclarative/src/qml/compiler/qv4compilerscanfunctions.cpp, line 558, as _ZN3QV48Compiler13ScanFunctions8endVisitEPN6QQmlJS3AST16ForEachStatementE
namespace QV4::Compiler {
using namespace QV4;
using namespace QQmlJS;
using namespace QQmlJS::AST;
inline void ScanFunctions::endVisit(ForEachStatement *)
{
    leaveEnvironment();
}
}  // namespace QV4::Compiler

//  from ../qtdeclarative/src/qml/compiler/qv4compilerscanfunctions.cpp, line 563, as _ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST14ThisExpressionE
namespace QV4::Compiler {
using namespace QV4;
using namespace QQmlJS;
using namespace QQmlJS::AST;
inline bool ScanFunctions::visit(ThisExpression *)
{
    Q_ASSERT(_context);
    _context->usesThis = true;
    return false;
}
}  // namespace QV4::Compiler

//  from ../qtdeclarative/src/qml/compiler/qv4compilerscanfunctions.cpp, line 570, as _ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST5BlockE
namespace QV4::Compiler {
using namespace QV4;
using namespace QQmlJS;
using namespace QQmlJS::AST;
inline bool ScanFunctions::visit(Block *ast)
{
    TemporaryBoolAssignment allowFuncDecls(_allowFuncDecls, _context->isStrict ? false : _allowFuncDecls);
    enterEnvironment(ast, ContextType::Block, QStringLiteral("%Block"));
    Node::accept(ast->statements, this);
    return false;
}
}  // namespace QV4::Compiler

//  from ../qtdeclarative/src/qml/compiler/qv4compilerscanfunctions.cpp, line 578, as _ZN3QV48Compiler13ScanFunctions8endVisitEPN6QQmlJS3AST5BlockE
namespace QV4::Compiler {
using namespace QV4;
using namespace QQmlJS;
using namespace QQmlJS::AST;
inline void ScanFunctions::endVisit(Block *)
{
    leaveEnvironment();
}
}  // namespace QV4::Compiler

//  from ../qtdeclarative/src/qml/compiler/qv4compilerscanfunctions.cpp, line 583, as _ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST9CaseBlockE
namespace QV4::Compiler {
using namespace QV4;
using namespace QQmlJS;
using namespace QQmlJS::AST;
inline bool ScanFunctions::visit(CaseBlock *ast)
{
    enterEnvironment(ast, ContextType::Block, QStringLiteral("%CaseBlock"));
    return true;
}
}  // namespace QV4::Compiler

//  from ../qtdeclarative/src/qml/compiler/qv4compilerscanfunctions.cpp, line 589, as _ZN3QV48Compiler13ScanFunctions8endVisitEPN6QQmlJS3AST9CaseBlockE
namespace QV4::Compiler {
using namespace QV4;
using namespace QQmlJS;
using namespace QQmlJS::AST;
inline void ScanFunctions::endVisit(CaseBlock *)
{
    leaveEnvironment();
}
}  // namespace QV4::Compiler

//  from ../qtdeclarative/src/qml/compiler/qv4compilerscanfunctions.cpp, line 594, as _ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST5CatchE
namespace QV4::Compiler {
using namespace QV4;
using namespace QQmlJS;
using namespace QQmlJS::AST;
inline bool ScanFunctions::visit(Catch *ast)
{
    Q_ASSERT(_context);
    TemporaryBoolAssignment allowFuncDecls(_allowFuncDecls, _context->isStrict ? false : _allowFuncDecls);
    enterEnvironment(ast, ContextType::Block, QStringLiteral("%CatchBlock"));
    _context->isCatchBlock = true;
    QString caughtVar = ast->patternElement->bindingIdentifier.toString();
    if (caughtVar.isEmpty())
        caughtVar = QStringLiteral("@caught");
    _context->addLocalVar(caughtVar, Context::MemberType::VariableDefinition, VariableScope::Let);

    _context->caughtVariable = caughtVar;
    if (_context->isStrict &&
        (caughtVar == QLatin1String("eval") || caughtVar == QLatin1String("arguments"))) {
        _cg->throwSyntaxError(ast->identifierToken, QStringLiteral("Catch variable name may not be eval or arguments in strict mode"));
        return false;
    }
    Node::accept(ast->patternElement, this);
    // skip the block statement
    Node::accept(ast->statement->statements, this);
    return false;
}
}  // namespace QV4::Compiler

//  from ../qtdeclarative/src/qml/compiler/qv4compilerscanfunctions.cpp, line 617, as _ZN3QV48Compiler13ScanFunctions8endVisitEPN6QQmlJS3AST5CatchE
namespace QV4::Compiler {
using namespace QV4;
using namespace QQmlJS;
using namespace QQmlJS::AST;
inline void ScanFunctions::endVisit(Catch *)
{
    leaveEnvironment();
}
}  // namespace QV4::Compiler

//  from ../qtdeclarative/src/qml/compiler/qv4compilerscanfunctions.cpp, line 622, as _ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST13WithStatementE
namespace QV4::Compiler {
using namespace QV4;
using namespace QQmlJS;
using namespace QQmlJS::AST;
inline bool ScanFunctions::visit(WithStatement *ast)
{
    Q_ASSERT(_context);
    Node::accept(ast->expression, this);

    TemporaryBoolAssignment allowFuncDecls(_allowFuncDecls, _context->isStrict ? false : _allowFuncDecls);
    enterEnvironment(ast, ContextType::Block, QStringLiteral("%WithBlock"));
    _context->isWithBlock = true;

    if (_context->isStrict) {
        _cg->throwSyntaxError(ast->withToken, QStringLiteral("'with' statement is not allowed in strict mode"));
        return false;
    }
    Node::accept(ast->statement, this);

    return false;
}
}  // namespace QV4::Compiler

//  from ../qtdeclarative/src/qml/compiler/qv4compilerscanfunctions.cpp, line 640, as _ZN3QV48Compiler13ScanFunctions8endVisitEPN6QQmlJS3AST13WithStatementE
namespace QV4::Compiler {
using namespace QV4;
using namespace QQmlJS;
using namespace QQmlJS::AST;
inline void ScanFunctions::endVisit(WithStatement *)
{
    leaveEnvironment();
}
}  // namespace QV4::Compiler

//  from ../qtdeclarative/src/qml/compiler/qv4compilerscanfunctions.cpp, line 950, as _ZN3QV48Compiler13ScanFunctions24throwRecursionDepthErrorEv
namespace QV4::Compiler {
using namespace QV4;
using namespace QQmlJS;
using namespace QQmlJS::AST;
inline void ScanFunctions::throwRecursionDepthError()
{
    _cg->throwRecursionDepthError();
}
}  // namespace QV4::Compiler

//  from ../qtdeclarative/src/qml/compiler/qv4compilercontext.cpp, line 18, as _ZN3QV48Compiler6Module10newContextEPN6QQmlJS3AST4NodeEPNS0_7ContextENS0_11ContextTypeE
namespace QV4::Compiler {
using namespace QV4;
using namespace QQmlJS::AST;
using namespace QQmlJS;
inline Context *Module::newContext(Node *node, Context *parent, ContextType contextType)
{
    Q_ASSERT(!contextMap.contains(node));

    Context *c = new Context(parent, contextType);
    if (node) {
        SourceLocation loc = node->firstSourceLocation();
        c->line = loc.startLine;
        c->column = loc.startColumn;
    }

    contextMap.insert(node, c);

    if (!parent)
        rootContext = c;
    else {
        parent->nestedContexts.append(c);
        c->isStrict = parent->isStrict;
    }

    return c;
}
}  // namespace QV4::Compiler

//  from ../qtdeclarative/src/qml/compiler/qv4compilercontext.cpp, line 55, as _ZN3QV48Compiler7Context11addLocalVarERK7QStringNS1_10MemberTypeEN6QQmlJS3AST13VariableScopeEPNS7_18FunctionExpressionERKNS6_14SourceLocationEb
namespace QV4::Compiler {
using namespace QV4;
using namespace QQmlJS::AST;
using namespace QQmlJS;
inline bool Context::addLocalVar(
        const QString &name, Context::MemberType type, VariableScope scope,
        FunctionExpression *function, const QQmlJS::SourceLocation &declarationLocation,
        bool isInjected)
{
    // ### can this happen?
    if (name.isEmpty())
        return true;

    if (type != FunctionDefinition) {
        if (formals && formals->containsName(name))
            return (scope == VariableScope::Var);
    }
    if (!isCatchBlock || name != caughtVariable) {
        MemberMap::iterator it = members.find(name);
        if (it != members.end()) {
            if (scope != VariableScope::Var || (*it).scope != VariableScope::Var)
                return false;
            if ((*it).type <= type) {
                (*it).type = type;
                (*it).function = function;
            }
            return true;
        }
    }

    // hoist var declarations to the function level
    if (contextType == ContextType::Block && (scope == VariableScope::Var && type != MemberType::FunctionDefinition))
        return parent->addLocalVar(name, type, scope, function, declarationLocation);

    Member m;
    m.type = type;
    m.function = function;
    m.scope = scope;
    m.declarationLocation = declarationLocation;
    m.isInjected = isInjected;
    members.insert(name, m);
    return true;
}
}  // namespace QV4::Compiler

//  from ../qtdeclarative/src/qml/compiler/qv4compilerscanfunctions.cpp, line 47, as _ZN3QV48Compiler13ScanFunctions22enterGlobalEnvironmentENS0_11ContextTypeE
namespace QV4::Compiler {
using namespace QV4;
using namespace QQmlJS;
using namespace QQmlJS::AST;
inline void ScanFunctions::enterGlobalEnvironment(ContextType compilationMode)
{
    enterEnvironment(astNodeForGlobalEnvironment, compilationMode, QStringLiteral("%GlobalCode"));
}
}  // namespace QV4::Compiler

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

//  from ../qtdeclarative/src/qml/compiler/qv4compilerscanfunctions.cpp, line 70, as _ZN3QV48Compiler13ScanFunctions22checkDirectivePrologueEPN6QQmlJS3AST13StatementListE
namespace QV4::Compiler {
using namespace QV4;
using namespace QQmlJS;
using namespace QQmlJS::AST;
inline void ScanFunctions::checkDirectivePrologue(StatementList *ast)
{
    Q_ASSERT(_context);
    for (StatementList *it = ast; it; it = it->next) {
        if (ExpressionStatement *expr = cast<ExpressionStatement *>(it->statement)) {
            if (StringLiteral *strLit = cast<StringLiteral *>(expr->expression)) {
                // Use the source code, because the StringLiteral's
                // value might have escape sequences in it, which is not
                // allowed.
                if (strLit->literalToken.length < 2)
                    continue;
                QStringView str = QStringView{_sourceCode}.mid(strLit->literalToken.offset + 1, strLit->literalToken.length - 2);
                if (str == QLatin1String("use strict")) {
                    _context->isStrict = true;
                } else {
                    // TODO: give a warning.
                }
                continue;
            }
        }

        break;
    }
}
}  // namespace QV4::Compiler

//  from ../qtdeclarative/src/qml/compiler/qv4compilerscanfunctions.cpp, line 95, as _ZN3QV48Compiler13ScanFunctions9checkNameE11QStringViewRKN6QQmlJS14SourceLocationE
namespace QV4::Compiler {
using namespace QV4;
using namespace QQmlJS;
using namespace QQmlJS::AST;
inline void ScanFunctions::checkName(QStringView name, const QQmlJS::SourceLocation &loc)
{
    Q_ASSERT(_context);
    if (_context->isStrict) {
        if (name == QLatin1String("implements")
                || name == QLatin1String("interface")
                || name == QLatin1String("let")
                || name == QLatin1String("package")
                || name == QLatin1String("private")
                || name == QLatin1String("protected")
                || name == QLatin1String("public")
                || name == QLatin1String("static")
                || name == QLatin1String("yield")) {
            _cg->throwSyntaxError(loc, QStringLiteral("Unexpected strict mode reserved word"));
        }
    }
}
}  // namespace QV4::Compiler

//  from ../qtdeclarative/src/qml/compiler/qv4compilerscanfunctions.cpp, line 467, as _ZN3QV48Compiler13ScanFunctions13enterFunctionEPN6QQmlJS3AST18FunctionExpressionENS1_19FunctionNameContextE
namespace QV4::Compiler {
using namespace QV4;
using namespace QQmlJS;
using namespace QQmlJS::AST;
inline bool ScanFunctions::enterFunction(FunctionExpression *ast, FunctionNameContext nameContext)
{
    Q_ASSERT(_context);
    if (_context->isStrict && (ast->name == QLatin1String("eval") || ast->name == QLatin1String("arguments")))
        _cg->throwSyntaxError(ast->identifierToken, QStringLiteral("Function name may not be eval or arguments in strict mode"));
    return enterFunction(ast, ast->name.toString(), ast->formals, ast->body, nameContext);
}
}  // namespace QV4::Compiler

//  from ../qtdeclarative/src/qml/compiler/qv4compilerscanfunctions.cpp, line 645, as _ZN3QV48Compiler13ScanFunctions13enterFunctionEPN6QQmlJS3AST4NodeERK7QStringPNS3_19FormalParameterListEPNS3_13StatementListENS1_19FunctionNameContextE
namespace QV4::Compiler {
using namespace QV4;
using namespace QQmlJS;
using namespace QQmlJS::AST;
inline bool ScanFunctions::enterFunction(
        Node *ast, const QString &name, FormalParameterList *formals, StatementList *body,
        FunctionNameContext nameContext)
{
    Context *outerContext = _context;
    enterEnvironment(ast, ContextType::Function, name);

    FunctionExpression *expr = AST::cast<FunctionExpression *>(ast);
    if (!expr)
        expr = AST::cast<FunctionDeclaration *>(ast);
    if (outerContext) {
        outerContext->hasNestedFunctions = true;
        // The identifier of a function expression cannot be referenced from the enclosing environment.
        if (nameContext == FunctionNameContext::Outer) {
            if (!outerContext->addLocalVar(name, Context::FunctionDefinition, VariableScope::Var,
                                           expr, expr->identifierToken)) {
                _cg->throwSyntaxError(ast->firstSourceLocation(), QStringLiteral("Identifier %1 has already been declared").arg(name));
                return false;
            }
            outerContext->addLocalVar(name, Context::FunctionDefinition, VariableScope::Var, expr);
        }
        if (name == QLatin1String("arguments"))
            outerContext->usesArgumentsObject = Context::UsesArgumentsObject::NotUsed;
    }

    Q_ASSERT(_context);
    _context->name = name;
    if (formals && formals->containsName(QStringLiteral("arguments")))
        _context->usesArgumentsObject = Context::UsesArgumentsObject::NotUsed;
    if (expr) {
        if (expr->isArrowFunction)
            _context->isArrowFunction = true;
        else if (expr->isGenerator)
            _context->isGenerator = true;

        if (expr->typeAnnotation)
            _context->returnType = expr->typeAnnotation->type;
    }


    if (nameContext == FunctionNameContext::Inner
            && (!name.isEmpty() && (!formals || !formals->containsName(name)))) {
        _context->addLocalVar(name, Context::ThisFunctionName, VariableScope::Var);
    }
    _context->formals = formals;

    if (body && !_context->isStrict)
        checkDirectivePrologue(body);

    bool isSimpleParameterList = formals && formals->isSimpleParameterList();

    _context->arguments = formals ? formals->formals() : BoundNames();

    const BoundNames boundNames = formals ? formals->boundNames() : BoundNames();
    for (int i = 0; i < boundNames.size(); ++i) {
        const auto &arg = boundNames.at(i);
        if (_context->isStrict || !isSimpleParameterList) {
            bool duplicate = (boundNames.indexOf(arg.id, i + 1) != -1);
            if (duplicate) {
                _cg->throwSyntaxError(formals->firstSourceLocation(), QStringLiteral("Duplicate parameter name '%1' is not allowed.").arg(arg.id));
                return false;
            }
        }
        if (_context->isStrict) {
            if (arg.id == QLatin1String("eval") || arg.id == QLatin1String("arguments")) {
                _cg->throwSyntaxError(formals->firstSourceLocation(), QStringLiteral("'%1' cannot be used as parameter name in strict mode").arg(arg.id));
                return false;
            }
        }
        if (!_context->arguments.contains(arg.id)) {
            _context->addLocalVar(arg.id, Context::VariableDefinition, VariableScope::Var, nullptr,
                                  QQmlJS::SourceLocation(), arg.isInjected());
        }
    }

    return true;
}
}  // namespace QV4::Compiler
//  -----------------------------------------------------------------------

//  Only a class built on QV4::Compiler::ScanFunctions may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQV4_Compiler_ScanFunctions : QV4::Compiler::ScanFunctions {
  using QV4::Compiler::ScanFunctions::visit;
  using QV4::Compiler::ScanFunctions::endVisit;
  using QV4::Compiler::ScanFunctions::throwRecursionDepthError;
};

//  void QV4::Compiler::ScanFunctions::handleTopLevelFunctionFormals(QQmlJS::
//      AST::FunctionExpression *node)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV48Compiler13ScanFunctions29handleTopLevelFunctionFormalsEPN6QQmlJS3AST18FunctionExpressionE(
    QV4::Compiler::ScanFunctions *self,
    QQmlJS::AST::FunctionExpression *node) {
  self->handleTopLevelFunctionFormals(node);
}

//  void QV4::Compiler::ScanFunctions::enterGlobalEnvironment(ContextType
//      compilationMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV48Compiler13ScanFunctions22enterGlobalEnvironmentENS0_11ContextTypeE(
    QV4::Compiler::ScanFunctions *self,
    QV4::Compiler::ContextType compilationMode) {
  self->enterGlobalEnvironment(compilationMode);
}

//  void QV4::Compiler::ScanFunctions::enterEnvironment(QQmlJS::AST::Node
//      *node, ContextType compilationMode, const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV48Compiler13ScanFunctions16enterEnvironmentEPN6QQmlJS3AST4NodeENS0_11ContextTypeERK7QString(
    QV4::Compiler::ScanFunctions *self,
    QQmlJS::AST::Node *node,
    QV4::Compiler::ContextType compilationMode,
    const QString *name) {
  self->enterEnvironment(node, compilationMode, *name);
}

//  void QV4::Compiler::ScanFunctions::leaveEnvironment()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV48Compiler13ScanFunctions16leaveEnvironmentEv(
    QV4::Compiler::ScanFunctions *self) {
  self->leaveEnvironment();
}

//  void QV4::Compiler::ScanFunctions::enterQmlFunction(QQmlJS::AST::Function
//      Expression *ast)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV48Compiler13ScanFunctions16enterQmlFunctionEPN6QQmlJS3AST18FunctionExpressionE(
    QV4::Compiler::ScanFunctions *self,
    QQmlJS::AST::FunctionExpression *ast) {
  self->enterQmlFunction(ast);
}

//  void QV4::Compiler::ScanFunctions::checkDirectivePrologue(QQmlJS::AST::St
//      atementList *ast)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV48Compiler13ScanFunctions22checkDirectivePrologueEPN6QQmlJS3AST13StatementListE(
    QV4::Compiler::ScanFunctions *self,
    QQmlJS::AST::StatementList *ast) {
  self->checkDirectivePrologue(ast);
}

//  void QV4::Compiler::ScanFunctions::checkName(QStringView name, const
//      QQmlJS::SourceLocation &loc)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV48Compiler13ScanFunctions9checkNameE11QStringViewRKN6QQmlJS14SourceLocationE(
    QV4::Compiler::ScanFunctions *self,
    const QString *name,
    const QQmlJS::SourceLocation *loc) {
  self->checkName(QStringView(*name), *loc);
}

//  bool QV4::Compiler::ScanFunctions::visit(QQmlJS::AST::Program *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST7ProgramE(
    QV4::Compiler::ScanFunctions *self,
    QQmlJS::AST::Program *ast) {
  return self->visit(ast);
}

//  void QV4::Compiler::ScanFunctions::endVisit(QQmlJS::AST::Program *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV48Compiler13ScanFunctions8endVisitEPN6QQmlJS3AST7ProgramE(
    QV4::Compiler::ScanFunctions *self,
    QQmlJS::AST::Program *a0) {
  self->endVisit(a0);
}

//  bool QV4::Compiler::ScanFunctions::visit(QQmlJS::AST::ESModule *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST8ESModuleE(
    QV4::Compiler::ScanFunctions *self,
    QQmlJS::AST::ESModule *ast) {
  return self->visit(ast);
}

//  void QV4::Compiler::ScanFunctions::endVisit(QQmlJS::AST::ESModule *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV48Compiler13ScanFunctions8endVisitEPN6QQmlJS3AST8ESModuleE(
    QV4::Compiler::ScanFunctions *self,
    QQmlJS::AST::ESModule *a0) {
  self->endVisit(a0);
}

//  bool QV4::Compiler::ScanFunctions::visit(QQmlJS::AST::ExportDeclaration
//      *declaration)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST17ExportDeclarationE(
    QV4::Compiler::ScanFunctions *self,
    QQmlJS::AST::ExportDeclaration *declaration) {
  return self->visit(declaration);
}

//  bool QV4::Compiler::ScanFunctions::visit(QQmlJS::AST::ImportDeclaration
//      *declaration)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST17ImportDeclarationE(
    QV4::Compiler::ScanFunctions *self,
    QQmlJS::AST::ImportDeclaration *declaration) {
  return self->visit(declaration);
}

//  bool QV4::Compiler::ScanFunctions::visit(QQmlJS::AST::CallExpression
//      *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST14CallExpressionE(
    QV4::Compiler::ScanFunctions *self,
    QQmlJS::AST::CallExpression *ast) {
  return self->visit(ast);
}

//  bool QV4::Compiler::ScanFunctions::visit(QQmlJS::AST::PatternElement
//      *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST14PatternElementE(
    QV4::Compiler::ScanFunctions *self,
    QQmlJS::AST::PatternElement *ast) {
  return self->visit(ast);
}

//  bool
//      QV4::Compiler::ScanFunctions::visit(QQmlJS::AST::IdentifierExpression
//      *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST20IdentifierExpressionE(
    QV4::Compiler::ScanFunctions *self,
    QQmlJS::AST::IdentifierExpression *ast) {
  return self->visit(ast);
}

//  bool QV4::Compiler::ScanFunctions::visit(QQmlJS::AST::ExpressionStatement
//      *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST19ExpressionStatementE(
    QV4::Compiler::ScanFunctions *self,
    QQmlJS::AST::ExpressionStatement *ast) {
  return self->visit(ast);
}

//  bool QV4::Compiler::ScanFunctions::visit(QQmlJS::AST::FunctionExpression
//      *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST18FunctionExpressionE(
    QV4::Compiler::ScanFunctions *self,
    QQmlJS::AST::FunctionExpression *ast) {
  return self->visit(ast);
}

//  bool QV4::Compiler::ScanFunctions::visit(QQmlJS::AST::TemplateLiteral
//      *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST15TemplateLiteralE(
    QV4::Compiler::ScanFunctions *self,
    QQmlJS::AST::TemplateLiteral *ast) {
  return self->visit(ast);
}

//  bool QV4::Compiler::ScanFunctions::visit(QQmlJS::AST::SuperLiteral *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST12SuperLiteralE(
    QV4::Compiler::ScanFunctions *self,
    QQmlJS::AST::SuperLiteral *a0) {
  return self->visit(a0);
}

//  bool
//      QV4::Compiler::ScanFunctions::visit(QQmlJS::AST::FieldMemberExpressio
//      n *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST21FieldMemberExpressionE(
    QV4::Compiler::ScanFunctions *self,
    QQmlJS::AST::FieldMemberExpression *a0) {
  return self->visit(a0);
}

//  bool QV4::Compiler::ScanFunctions::visit(QQmlJS::AST::ArrayPattern *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST12ArrayPatternE(
    QV4::Compiler::ScanFunctions *self,
    QQmlJS::AST::ArrayPattern *a0) {
  return self->visit(a0);
}

//  bool QV4::Compiler::ScanFunctions::enterFunction(QQmlJS::AST::FunctionExp
//      ression *ast, FunctionNameContext nameContext)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler13ScanFunctions13enterFunctionEPN6QQmlJS3AST18FunctionExpressionENS1_19FunctionNameContextE(
    QV4::Compiler::ScanFunctions *self,
    QQmlJS::AST::FunctionExpression *ast,
    QV4::Compiler::ScanFunctions::FunctionNameContext nameContext) {
  return self->enterFunction(ast, nameContext);
}

//  void
//      QV4::Compiler::ScanFunctions::endVisit(QQmlJS::AST::FunctionExpressio
//      n *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV48Compiler13ScanFunctions8endVisitEPN6QQmlJS3AST18FunctionExpressionE(
    QV4::Compiler::ScanFunctions *self,
    QQmlJS::AST::FunctionExpression *a0) {
  self->endVisit(a0);
}

//  bool QV4::Compiler::ScanFunctions::visit(QQmlJS::AST::ObjectPattern *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST13ObjectPatternE(
    QV4::Compiler::ScanFunctions *self,
    QQmlJS::AST::ObjectPattern *ast) {
  return self->visit(ast);
}

//  bool QV4::Compiler::ScanFunctions::visit(QQmlJS::AST::PatternProperty
//      *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST15PatternPropertyE(
    QV4::Compiler::ScanFunctions *self,
    QQmlJS::AST::PatternProperty *ast) {
  return self->visit(ast);
}

//  void QV4::Compiler::ScanFunctions::endVisit(QQmlJS::AST::PatternProperty
//      *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV48Compiler13ScanFunctions8endVisitEPN6QQmlJS3AST15PatternPropertyE(
    QV4::Compiler::ScanFunctions *self,
    QQmlJS::AST::PatternProperty *a0) {
  self->endVisit(a0);
}

//  bool QV4::Compiler::ScanFunctions::visit(QQmlJS::AST::FunctionDeclaration
//      *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST19FunctionDeclarationE(
    QV4::Compiler::ScanFunctions *self,
    QQmlJS::AST::FunctionDeclaration *ast) {
  return self->visit(ast);
}

//  void
//      QV4::Compiler::ScanFunctions::endVisit(QQmlJS::AST::FunctionDeclarati
//      on *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV48Compiler13ScanFunctions8endVisitEPN6QQmlJS3AST19FunctionDeclarationE(
    QV4::Compiler::ScanFunctions *self,
    QQmlJS::AST::FunctionDeclaration *a0) {
  self->endVisit(a0);
}

//  bool QV4::Compiler::ScanFunctions::visit(QQmlJS::AST::ClassExpression
//      *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST15ClassExpressionE(
    QV4::Compiler::ScanFunctions *self,
    QQmlJS::AST::ClassExpression *ast) {
  return self->visit(ast);
}

//  void QV4::Compiler::ScanFunctions::endVisit(QQmlJS::AST::ClassExpression
//      *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV48Compiler13ScanFunctions8endVisitEPN6QQmlJS3AST15ClassExpressionE(
    QV4::Compiler::ScanFunctions *self,
    QQmlJS::AST::ClassExpression *a0) {
  self->endVisit(a0);
}

//  bool QV4::Compiler::ScanFunctions::visit(QQmlJS::AST::ClassDeclaration
//      *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST16ClassDeclarationE(
    QV4::Compiler::ScanFunctions *self,
    QQmlJS::AST::ClassDeclaration *ast) {
  return self->visit(ast);
}

//  void QV4::Compiler::ScanFunctions::endVisit(QQmlJS::AST::ClassDeclaration
//      *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV48Compiler13ScanFunctions8endVisitEPN6QQmlJS3AST16ClassDeclarationE(
    QV4::Compiler::ScanFunctions *self,
    QQmlJS::AST::ClassDeclaration *a0) {
  self->endVisit(a0);
}

//  bool QV4::Compiler::ScanFunctions::visit(QQmlJS::AST::DoWhileStatement
//      *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST16DoWhileStatementE(
    QV4::Compiler::ScanFunctions *self,
    QQmlJS::AST::DoWhileStatement *ast) {
  return self->visit(ast);
}

//  bool QV4::Compiler::ScanFunctions::visit(QQmlJS::AST::ForStatement *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST12ForStatementE(
    QV4::Compiler::ScanFunctions *self,
    QQmlJS::AST::ForStatement *ast) {
  return self->visit(ast);
}

//  void QV4::Compiler::ScanFunctions::endVisit(QQmlJS::AST::ForStatement
//      *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV48Compiler13ScanFunctions8endVisitEPN6QQmlJS3AST12ForStatementE(
    QV4::Compiler::ScanFunctions *self,
    QQmlJS::AST::ForStatement *a0) {
  self->endVisit(a0);
}

//  bool QV4::Compiler::ScanFunctions::visit(QQmlJS::AST::ForEachStatement
//      *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST16ForEachStatementE(
    QV4::Compiler::ScanFunctions *self,
    QQmlJS::AST::ForEachStatement *ast) {
  return self->visit(ast);
}

//  void QV4::Compiler::ScanFunctions::endVisit(QQmlJS::AST::ForEachStatement
//      *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV48Compiler13ScanFunctions8endVisitEPN6QQmlJS3AST16ForEachStatementE(
    QV4::Compiler::ScanFunctions *self,
    QQmlJS::AST::ForEachStatement *a0) {
  self->endVisit(a0);
}

//  bool QV4::Compiler::ScanFunctions::visit(QQmlJS::AST::ThisExpression
//      *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST14ThisExpressionE(
    QV4::Compiler::ScanFunctions *self,
    QQmlJS::AST::ThisExpression *ast) {
  return self->visit(ast);
}

//  bool QV4::Compiler::ScanFunctions::visit(QQmlJS::AST::Block *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST5BlockE(
    QV4::Compiler::ScanFunctions *self,
    QQmlJS::AST::Block *ast) {
  return self->visit(ast);
}

//  void QV4::Compiler::ScanFunctions::endVisit(QQmlJS::AST::Block *ast)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV48Compiler13ScanFunctions8endVisitEPN6QQmlJS3AST5BlockE(
    QV4::Compiler::ScanFunctions *self,
    QQmlJS::AST::Block *ast) {
  self->endVisit(ast);
}

//  bool QV4::Compiler::ScanFunctions::visit(QQmlJS::AST::CaseBlock *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST9CaseBlockE(
    QV4::Compiler::ScanFunctions *self,
    QQmlJS::AST::CaseBlock *ast) {
  return self->visit(ast);
}

//  void QV4::Compiler::ScanFunctions::endVisit(QQmlJS::AST::CaseBlock *ast)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV48Compiler13ScanFunctions8endVisitEPN6QQmlJS3AST9CaseBlockE(
    QV4::Compiler::ScanFunctions *self,
    QQmlJS::AST::CaseBlock *ast) {
  self->endVisit(ast);
}

//  bool QV4::Compiler::ScanFunctions::visit(QQmlJS::AST::Catch *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST5CatchE(
    QV4::Compiler::ScanFunctions *self,
    QQmlJS::AST::Catch *ast) {
  return self->visit(ast);
}

//  void QV4::Compiler::ScanFunctions::endVisit(QQmlJS::AST::Catch *ast)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV48Compiler13ScanFunctions8endVisitEPN6QQmlJS3AST5CatchE(
    QV4::Compiler::ScanFunctions *self,
    QQmlJS::AST::Catch *ast) {
  self->endVisit(ast);
}

//  bool QV4::Compiler::ScanFunctions::visit(QQmlJS::AST::WithStatement *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST13WithStatementE(
    QV4::Compiler::ScanFunctions *self,
    QQmlJS::AST::WithStatement *ast) {
  return self->visit(ast);
}

//  void QV4::Compiler::ScanFunctions::endVisit(QQmlJS::AST::WithStatement
//      *ast)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV48Compiler13ScanFunctions8endVisitEPN6QQmlJS3AST13WithStatementE(
    QV4::Compiler::ScanFunctions *self,
    QQmlJS::AST::WithStatement *ast) {
  self->endVisit(ast);
}

//  void QV4::Compiler::ScanFunctions::throwRecursionDepthError()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV48Compiler13ScanFunctions24throwRecursionDepthErrorEv(
    QV4::Compiler::ScanFunctions *self) {
  self->throwRecursionDepthError();
}

//  bool QV4::Compiler::ScanFunctions::enterFunction(QQmlJS::AST::Node *ast,
//      const QString &name, QQmlJS::AST::FormalParameterList *formals,
//      QQmlJS::AST::StatementList *body, FunctionNameContext nameContext)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler13ScanFunctions13enterFunctionEPN6QQmlJS3AST4NodeERK7QStringPNS3_19FormalParameterListEPNS3_13StatementListENS1_19FunctionNameContextE(
    QV4::Compiler::ScanFunctions *self,
    QQmlJS::AST::Node *ast,
    const QString *name,
    QQmlJS::AST::FormalParameterList *formals,
    QQmlJS::AST::StatementList *body,
    QV4::Compiler::ScanFunctions::FunctionNameContext nameContext) {
  return self->enterFunction(ast, *name, formals, body, nameContext);
}

//  QV4::Compiler::ScanFunctions::~ScanFunctions()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV48Compiler13ScanFunctionsD1Ev(
    QV4::Compiler::ScanFunctions *self) {
  delete self;
}

//  bool QV4::Compiler::ScanFunctions::visit(QQmlJS::AST::Program *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST7ProgramE(
    QV4::Compiler::ScanFunctions *self,
    QQmlJS::AST::Program *ast) {
  return static_cast<OwnQV4_Compiler_ScanFunctions *>(self)->OwnQV4_Compiler_ScanFunctions::visit(
      ast);
}

//  void QV4::Compiler::ScanFunctions::endVisit(QQmlJS::AST::Program *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN3QV48Compiler13ScanFunctions8endVisitEPN6QQmlJS3AST7ProgramE(
    QV4::Compiler::ScanFunctions *self,
    QQmlJS::AST::Program *a0) {
  static_cast<OwnQV4_Compiler_ScanFunctions *>(self)->OwnQV4_Compiler_ScanFunctions::endVisit(
      a0);
}

//  bool QV4::Compiler::ScanFunctions::visit(QQmlJS::AST::ESModule *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST8ESModuleE(
    QV4::Compiler::ScanFunctions *self,
    QQmlJS::AST::ESModule *ast) {
  return static_cast<OwnQV4_Compiler_ScanFunctions *>(self)->OwnQV4_Compiler_ScanFunctions::visit(
      ast);
}

//  void QV4::Compiler::ScanFunctions::endVisit(QQmlJS::AST::ESModule *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN3QV48Compiler13ScanFunctions8endVisitEPN6QQmlJS3AST8ESModuleE(
    QV4::Compiler::ScanFunctions *self,
    QQmlJS::AST::ESModule *a0) {
  static_cast<OwnQV4_Compiler_ScanFunctions *>(self)->OwnQV4_Compiler_ScanFunctions::endVisit(
      a0);
}

//  bool QV4::Compiler::ScanFunctions::visit(QQmlJS::AST::CallExpression
//      *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST14CallExpressionE(
    QV4::Compiler::ScanFunctions *self,
    QQmlJS::AST::CallExpression *ast) {
  return static_cast<OwnQV4_Compiler_ScanFunctions *>(self)->OwnQV4_Compiler_ScanFunctions::visit(
      ast);
}

//  bool QV4::Compiler::ScanFunctions::visit(QQmlJS::AST::PatternElement
//      *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST14PatternElementE(
    QV4::Compiler::ScanFunctions *self,
    QQmlJS::AST::PatternElement *ast) {
  return static_cast<OwnQV4_Compiler_ScanFunctions *>(self)->OwnQV4_Compiler_ScanFunctions::visit(
      ast);
}

//  bool
//      QV4::Compiler::ScanFunctions::visit(QQmlJS::AST::IdentifierExpression
//      *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST20IdentifierExpressionE(
    QV4::Compiler::ScanFunctions *self,
    QQmlJS::AST::IdentifierExpression *ast) {
  return static_cast<OwnQV4_Compiler_ScanFunctions *>(self)->OwnQV4_Compiler_ScanFunctions::visit(
      ast);
}

//  bool QV4::Compiler::ScanFunctions::visit(QQmlJS::AST::ExpressionStatement
//      *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST19ExpressionStatementE(
    QV4::Compiler::ScanFunctions *self,
    QQmlJS::AST::ExpressionStatement *ast) {
  return static_cast<OwnQV4_Compiler_ScanFunctions *>(self)->OwnQV4_Compiler_ScanFunctions::visit(
      ast);
}

//  bool QV4::Compiler::ScanFunctions::visit(QQmlJS::AST::FunctionExpression
//      *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST18FunctionExpressionE(
    QV4::Compiler::ScanFunctions *self,
    QQmlJS::AST::FunctionExpression *ast) {
  return static_cast<OwnQV4_Compiler_ScanFunctions *>(self)->OwnQV4_Compiler_ScanFunctions::visit(
      ast);
}

//  bool QV4::Compiler::ScanFunctions::visit(QQmlJS::AST::TemplateLiteral
//      *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST15TemplateLiteralE(
    QV4::Compiler::ScanFunctions *self,
    QQmlJS::AST::TemplateLiteral *ast) {
  return static_cast<OwnQV4_Compiler_ScanFunctions *>(self)->OwnQV4_Compiler_ScanFunctions::visit(
      ast);
}

//  bool QV4::Compiler::ScanFunctions::visit(QQmlJS::AST::SuperLiteral *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST12SuperLiteralE(
    QV4::Compiler::ScanFunctions *self,
    QQmlJS::AST::SuperLiteral *a0) {
  return static_cast<OwnQV4_Compiler_ScanFunctions *>(self)->OwnQV4_Compiler_ScanFunctions::visit(
      a0);
}

//  bool
//      QV4::Compiler::ScanFunctions::visit(QQmlJS::AST::FieldMemberExpressio
//      n *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST21FieldMemberExpressionE(
    QV4::Compiler::ScanFunctions *self,
    QQmlJS::AST::FieldMemberExpression *a0) {
  return static_cast<OwnQV4_Compiler_ScanFunctions *>(self)->OwnQV4_Compiler_ScanFunctions::visit(
      a0);
}

//  bool QV4::Compiler::ScanFunctions::visit(QQmlJS::AST::ArrayPattern *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST12ArrayPatternE(
    QV4::Compiler::ScanFunctions *self,
    QQmlJS::AST::ArrayPattern *a0) {
  return static_cast<OwnQV4_Compiler_ScanFunctions *>(self)->OwnQV4_Compiler_ScanFunctions::visit(
      a0);
}

//  void
//      QV4::Compiler::ScanFunctions::endVisit(QQmlJS::AST::FunctionExpressio
//      n *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN3QV48Compiler13ScanFunctions8endVisitEPN6QQmlJS3AST18FunctionExpressionE(
    QV4::Compiler::ScanFunctions *self,
    QQmlJS::AST::FunctionExpression *a0) {
  static_cast<OwnQV4_Compiler_ScanFunctions *>(self)->OwnQV4_Compiler_ScanFunctions::endVisit(
      a0);
}

//  bool QV4::Compiler::ScanFunctions::visit(QQmlJS::AST::ObjectPattern *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST13ObjectPatternE(
    QV4::Compiler::ScanFunctions *self,
    QQmlJS::AST::ObjectPattern *ast) {
  return static_cast<OwnQV4_Compiler_ScanFunctions *>(self)->OwnQV4_Compiler_ScanFunctions::visit(
      ast);
}

//  bool QV4::Compiler::ScanFunctions::visit(QQmlJS::AST::PatternProperty
//      *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST15PatternPropertyE(
    QV4::Compiler::ScanFunctions *self,
    QQmlJS::AST::PatternProperty *ast) {
  return static_cast<OwnQV4_Compiler_ScanFunctions *>(self)->OwnQV4_Compiler_ScanFunctions::visit(
      ast);
}

//  void QV4::Compiler::ScanFunctions::endVisit(QQmlJS::AST::PatternProperty
//      *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN3QV48Compiler13ScanFunctions8endVisitEPN6QQmlJS3AST15PatternPropertyE(
    QV4::Compiler::ScanFunctions *self,
    QQmlJS::AST::PatternProperty *a0) {
  static_cast<OwnQV4_Compiler_ScanFunctions *>(self)->OwnQV4_Compiler_ScanFunctions::endVisit(
      a0);
}

//  bool QV4::Compiler::ScanFunctions::visit(QQmlJS::AST::FunctionDeclaration
//      *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST19FunctionDeclarationE(
    QV4::Compiler::ScanFunctions *self,
    QQmlJS::AST::FunctionDeclaration *ast) {
  return static_cast<OwnQV4_Compiler_ScanFunctions *>(self)->OwnQV4_Compiler_ScanFunctions::visit(
      ast);
}

//  void
//      QV4::Compiler::ScanFunctions::endVisit(QQmlJS::AST::FunctionDeclarati
//      on *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN3QV48Compiler13ScanFunctions8endVisitEPN6QQmlJS3AST19FunctionDeclarationE(
    QV4::Compiler::ScanFunctions *self,
    QQmlJS::AST::FunctionDeclaration *a0) {
  static_cast<OwnQV4_Compiler_ScanFunctions *>(self)->OwnQV4_Compiler_ScanFunctions::endVisit(
      a0);
}

//  bool QV4::Compiler::ScanFunctions::visit(QQmlJS::AST::ClassExpression
//      *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST15ClassExpressionE(
    QV4::Compiler::ScanFunctions *self,
    QQmlJS::AST::ClassExpression *ast) {
  return static_cast<OwnQV4_Compiler_ScanFunctions *>(self)->OwnQV4_Compiler_ScanFunctions::visit(
      ast);
}

//  void QV4::Compiler::ScanFunctions::endVisit(QQmlJS::AST::ClassExpression
//      *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN3QV48Compiler13ScanFunctions8endVisitEPN6QQmlJS3AST15ClassExpressionE(
    QV4::Compiler::ScanFunctions *self,
    QQmlJS::AST::ClassExpression *a0) {
  static_cast<OwnQV4_Compiler_ScanFunctions *>(self)->OwnQV4_Compiler_ScanFunctions::endVisit(
      a0);
}

//  bool QV4::Compiler::ScanFunctions::visit(QQmlJS::AST::ClassDeclaration
//      *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST16ClassDeclarationE(
    QV4::Compiler::ScanFunctions *self,
    QQmlJS::AST::ClassDeclaration *ast) {
  return static_cast<OwnQV4_Compiler_ScanFunctions *>(self)->OwnQV4_Compiler_ScanFunctions::visit(
      ast);
}

//  void QV4::Compiler::ScanFunctions::endVisit(QQmlJS::AST::ClassDeclaration
//      *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN3QV48Compiler13ScanFunctions8endVisitEPN6QQmlJS3AST16ClassDeclarationE(
    QV4::Compiler::ScanFunctions *self,
    QQmlJS::AST::ClassDeclaration *a0) {
  static_cast<OwnQV4_Compiler_ScanFunctions *>(self)->OwnQV4_Compiler_ScanFunctions::endVisit(
      a0);
}

//  bool QV4::Compiler::ScanFunctions::visit(QQmlJS::AST::DoWhileStatement
//      *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST16DoWhileStatementE(
    QV4::Compiler::ScanFunctions *self,
    QQmlJS::AST::DoWhileStatement *ast) {
  return static_cast<OwnQV4_Compiler_ScanFunctions *>(self)->OwnQV4_Compiler_ScanFunctions::visit(
      ast);
}

//  bool QV4::Compiler::ScanFunctions::visit(QQmlJS::AST::ForStatement *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST12ForStatementE(
    QV4::Compiler::ScanFunctions *self,
    QQmlJS::AST::ForStatement *ast) {
  return static_cast<OwnQV4_Compiler_ScanFunctions *>(self)->OwnQV4_Compiler_ScanFunctions::visit(
      ast);
}

//  void QV4::Compiler::ScanFunctions::endVisit(QQmlJS::AST::ForStatement
//      *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN3QV48Compiler13ScanFunctions8endVisitEPN6QQmlJS3AST12ForStatementE(
    QV4::Compiler::ScanFunctions *self,
    QQmlJS::AST::ForStatement *a0) {
  static_cast<OwnQV4_Compiler_ScanFunctions *>(self)->OwnQV4_Compiler_ScanFunctions::endVisit(
      a0);
}

//  bool QV4::Compiler::ScanFunctions::visit(QQmlJS::AST::ForEachStatement
//      *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST16ForEachStatementE(
    QV4::Compiler::ScanFunctions *self,
    QQmlJS::AST::ForEachStatement *ast) {
  return static_cast<OwnQV4_Compiler_ScanFunctions *>(self)->OwnQV4_Compiler_ScanFunctions::visit(
      ast);
}

//  void QV4::Compiler::ScanFunctions::endVisit(QQmlJS::AST::ForEachStatement
//      *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN3QV48Compiler13ScanFunctions8endVisitEPN6QQmlJS3AST16ForEachStatementE(
    QV4::Compiler::ScanFunctions *self,
    QQmlJS::AST::ForEachStatement *a0) {
  static_cast<OwnQV4_Compiler_ScanFunctions *>(self)->OwnQV4_Compiler_ScanFunctions::endVisit(
      a0);
}

//  bool QV4::Compiler::ScanFunctions::visit(QQmlJS::AST::ThisExpression
//      *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST14ThisExpressionE(
    QV4::Compiler::ScanFunctions *self,
    QQmlJS::AST::ThisExpression *ast) {
  return static_cast<OwnQV4_Compiler_ScanFunctions *>(self)->OwnQV4_Compiler_ScanFunctions::visit(
      ast);
}

//  bool QV4::Compiler::ScanFunctions::visit(QQmlJS::AST::Block *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST5BlockE(
    QV4::Compiler::ScanFunctions *self,
    QQmlJS::AST::Block *ast) {
  return static_cast<OwnQV4_Compiler_ScanFunctions *>(self)->OwnQV4_Compiler_ScanFunctions::visit(
      ast);
}

//  void QV4::Compiler::ScanFunctions::endVisit(QQmlJS::AST::Block *ast)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN3QV48Compiler13ScanFunctions8endVisitEPN6QQmlJS3AST5BlockE(
    QV4::Compiler::ScanFunctions *self,
    QQmlJS::AST::Block *ast) {
  static_cast<OwnQV4_Compiler_ScanFunctions *>(self)->OwnQV4_Compiler_ScanFunctions::endVisit(
      ast);
}

//  bool QV4::Compiler::ScanFunctions::visit(QQmlJS::AST::CaseBlock *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST9CaseBlockE(
    QV4::Compiler::ScanFunctions *self,
    QQmlJS::AST::CaseBlock *ast) {
  return static_cast<OwnQV4_Compiler_ScanFunctions *>(self)->OwnQV4_Compiler_ScanFunctions::visit(
      ast);
}

//  void QV4::Compiler::ScanFunctions::endVisit(QQmlJS::AST::CaseBlock *ast)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN3QV48Compiler13ScanFunctions8endVisitEPN6QQmlJS3AST9CaseBlockE(
    QV4::Compiler::ScanFunctions *self,
    QQmlJS::AST::CaseBlock *ast) {
  static_cast<OwnQV4_Compiler_ScanFunctions *>(self)->OwnQV4_Compiler_ScanFunctions::endVisit(
      ast);
}

//  bool QV4::Compiler::ScanFunctions::visit(QQmlJS::AST::Catch *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST5CatchE(
    QV4::Compiler::ScanFunctions *self,
    QQmlJS::AST::Catch *ast) {
  return static_cast<OwnQV4_Compiler_ScanFunctions *>(self)->OwnQV4_Compiler_ScanFunctions::visit(
      ast);
}

//  void QV4::Compiler::ScanFunctions::endVisit(QQmlJS::AST::Catch *ast)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN3QV48Compiler13ScanFunctions8endVisitEPN6QQmlJS3AST5CatchE(
    QV4::Compiler::ScanFunctions *self,
    QQmlJS::AST::Catch *ast) {
  static_cast<OwnQV4_Compiler_ScanFunctions *>(self)->OwnQV4_Compiler_ScanFunctions::endVisit(
      ast);
}

//  bool QV4::Compiler::ScanFunctions::visit(QQmlJS::AST::WithStatement *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN3QV48Compiler13ScanFunctions5visitEPN6QQmlJS3AST13WithStatementE(
    QV4::Compiler::ScanFunctions *self,
    QQmlJS::AST::WithStatement *ast) {
  return static_cast<OwnQV4_Compiler_ScanFunctions *>(self)->OwnQV4_Compiler_ScanFunctions::visit(
      ast);
}

//  void QV4::Compiler::ScanFunctions::endVisit(QQmlJS::AST::WithStatement
//      *ast)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN3QV48Compiler13ScanFunctions8endVisitEPN6QQmlJS3AST13WithStatementE(
    QV4::Compiler::ScanFunctions *self,
    QQmlJS::AST::WithStatement *ast) {
  static_cast<OwnQV4_Compiler_ScanFunctions *>(self)->OwnQV4_Compiler_ScanFunctions::endVisit(
      ast);
}

//  void QV4::Compiler::ScanFunctions::throwRecursionDepthError()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN3QV48Compiler13ScanFunctions24throwRecursionDepthErrorEv(
    QV4::Compiler::ScanFunctions *self) {
  static_cast<OwnQV4_Compiler_ScanFunctions *>(self)->OwnQV4_Compiler_ScanFunctions::throwRecursionDepthError();
}
