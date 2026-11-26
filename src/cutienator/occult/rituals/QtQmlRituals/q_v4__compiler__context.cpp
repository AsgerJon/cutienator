//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4compilercontext_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4compilercontext_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmljssourcelocation_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
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

//  from ../qtdeclarative/src/qml/compiler/qv4compilercontext.cpp, line 41, as _ZNK3QV48Compiler7Context6Member16requiresTDZCheckERKN6QQmlJS14SourceLocationEb
namespace QV4::Compiler {
using namespace QV4;
using namespace QQmlJS::AST;
using namespace QQmlJS;
inline bool Context::Member::requiresTDZCheck(const SourceLocation &accessLocation, bool accessAcrossContextBoundaries) const
{
    if (!isLexicallyScoped())
        return false;

    if (accessAcrossContextBoundaries)
        return true;

    if (!accessLocation.isValid() || !declarationLocation.isValid())
        return true;

    return accessLocation.begin() < declarationLocation.end();
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

//  from ../qtdeclarative/src/qml/compiler/qv4compilercontext.cpp, line 95, as _ZN3QV48Compiler7Context11resolveNameERK7QStringRKN6QQmlJS14SourceLocationE
namespace QV4::Compiler {
using namespace QV4;
using namespace QQmlJS::AST;
using namespace QQmlJS;
inline Context::ResolvedName Context::resolveName(const QString &name, const QQmlJS::SourceLocation &accessLocation)
{
    int scope = 0;
    Context *c = this;

    ResolvedName result;

    while (c) {
        if (c->isWithBlock)
            return result;

        Context::Member m = c->findMember(name);
        if (!c->parent && m.index < 0)
            break;

        if (m.type != Context::UndefinedMember) {
            result.type = m.canEscape ? ResolvedName::Local : ResolvedName::Stack;
            result.memberType = m.type;
            result.scope = scope;
            result.index = m.index;
            result.isConst = (m.scope == VariableScope::Const);
            result.requiresTDZCheck = m.requiresTDZCheck(accessLocation, c != this) || c->isCaseBlock();
            if (c->isStrict && (name == QLatin1String("arguments") || name == QLatin1String("eval")))
                result.isArgOrEval = true;
            result.declarationLocation = m.declarationLocation;
            result.isInjected = m.isInjected;
            return result;
        }
        const int argIdx = c->findArgument(name, &result.isInjected);
        if (argIdx != -1) {
            if (c->argumentsCanEscape) {
                result.index = argIdx + c->locals.size();
                result.scope = scope;
                result.type = ResolvedName::Local;
                result.isConst = false;
                return result;
            } else {
                result.index = argIdx + sizeof(CallData) / sizeof(StaticValue) - 1;
                result.scope = 0;
                result.type = ResolvedName::Stack;
                result.isConst = false;
                return result;
            }
        }
        if (c->hasDirectEval) {
            Q_ASSERT(!c->isStrict && c->contextType != ContextType::Block);
            return result;
        }

        if (c->requiresExecutionContext)
            ++scope;
        c = c->parent;
    }

    if (!c)
        return result;

    if (c->contextType == ContextType::ESModule) {
        for (int i = 0; i < c->importEntries.size(); ++i) {
            if (c->importEntries.at(i).localName == name) {
                result.index = i;
                result.type = ResolvedName::Import;
                result.isConst = true;
                // We don't know at compile time whether the imported value is let/const or not.
                result.requiresTDZCheck = true;
                return result;
            }
        }
    }

    // ### can we relax the restrictions here?
    if (c->contextType == ContextType::Eval)
        return result;

    if (c->contextType == ContextType::Binding || c->contextType == ContextType::ScriptImportedByQML)
        result.type = ResolvedName::QmlGlobal;
    else
        result.type = ResolvedName::Global;
    return result;
}
}  // namespace QV4::Compiler
//  -----------------------------------------------------------------------

//  QV4::Compiler::Context::Context(Context *parent, ContextType type)
extern "C" Q_DECL_EXPORT
QV4::Compiler::Context *ritual_ZN3QV48Compiler7ContextC1EPS1_NS0_11ContextTypeE(
    QV4::Compiler::Context *parent,
    QV4::Compiler::ContextType type) {
  return new QV4::Compiler::Context(parent, type);
}

//  bool QV4::Compiler::Context::hasArgument(const QString &name) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV48Compiler7Context11hasArgumentERK7QString(
    const QV4::Compiler::Context *self,
    const QString *name) {
  return self->hasArgument(*name);
}

//  int QV4::Compiler::Context::findArgument(const QString &name, bool
//      *isInjected) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK3QV48Compiler7Context12findArgumentERK7QStringPb(
    const QV4::Compiler::Context *self,
    const QString *name,
    bool *isInjected) {
  return self->findArgument(*name, isInjected);
}

//  Member QV4::Compiler::Context::findMember(const QString &name) const
extern "C" Q_DECL_EXPORT
QV4::Compiler::Context::Member *ritual_ZNK3QV48Compiler7Context10findMemberERK7QString(
    const QV4::Compiler::Context *self,
    const QString *name) {
  return new QV4::Compiler::Context::Member(self->findMember(*name));
}

//  bool QV4::Compiler::Context::memberInfo(const QString &name, const Member
//      **m) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV48Compiler7Context10memberInfoERK7QStringPPKNS1_6MemberE(
    const QV4::Compiler::Context *self,
    const QString *name,
    const QV4::Compiler::Context::Member **m) {
  return self->memberInfo(*name, m);
}

//  bool QV4::Compiler::Context::requiresImplicitReturnValue() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV48Compiler7Context27requiresImplicitReturnValueEv(
    const QV4::Compiler::Context *self) {
  return self->requiresImplicitReturnValue();
}

//  void QV4::Compiler::Context::addUsedVariable(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV48Compiler7Context15addUsedVariableERK7QString(
    QV4::Compiler::Context *self,
    const QString *name) {
  self->addUsedVariable(*name);
}

//  bool QV4::Compiler::Context::addLocalVar(const QString &name, MemberType
//      contextType, QQmlJS::AST::VariableScope scope,
//      QQmlJS::AST::FunctionExpression *function, const
//      QQmlJS::SourceLocation &declarationLocation, bool isInjected)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler7Context11addLocalVarERK7QStringNS1_10MemberTypeEN6QQmlJS3AST13VariableScopeEPNS7_18FunctionExpressionERKNS6_14SourceLocationEb(
    QV4::Compiler::Context *self,
    const QString *name,
    QV4::Compiler::Context::MemberType contextType,
    QQmlJS::AST::VariableScope scope,
    QQmlJS::AST::FunctionExpression *function,
    const QQmlJS::SourceLocation *declarationLocation,
    bool isInjected) {
  return self->addLocalVar(
      *name,
      contextType,
      scope,
      function,
      *declarationLocation,
      isInjected);
}

//  ResolvedName QV4::Compiler::Context::resolveName(const QString &name,
//      const QQmlJS::SourceLocation &accessLocation)
extern "C" Q_DECL_EXPORT
QV4::Compiler::Context::ResolvedName *ritual_ZN3QV48Compiler7Context11resolveNameERK7QStringRKN6QQmlJS14SourceLocationE(
    QV4::Compiler::Context *self,
    const QString *name,
    const QQmlJS::SourceLocation *accessLocation) {
  return new QV4::Compiler::Context::ResolvedName(
      self->resolveName(
          *name,
          *accessLocation));
}

//  bool QV4::Compiler::Context::canHaveTailCalls() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV48Compiler7Context16canHaveTailCallsEv(
    const QV4::Compiler::Context *self) {
  return self->canHaveTailCalls();
}

//  bool QV4::Compiler::Context::isCaseBlock() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV48Compiler7Context11isCaseBlockEv(
    const QV4::Compiler::Context *self) {
  return self->isCaseBlock();
}
