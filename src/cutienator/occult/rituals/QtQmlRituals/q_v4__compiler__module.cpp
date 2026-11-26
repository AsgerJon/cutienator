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
//  -----------------------------------------------------------------------

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

//  Context *QV4::Compiler::Module::newContext(QQmlJS::AST::Node *node,
//      Context *parent, ContextType compilationMode)
extern "C" Q_DECL_EXPORT
QV4::Compiler::Context *ritual_ZN3QV48Compiler6Module10newContextEPN6QQmlJS3AST4NodeEPNS0_7ContextENS0_11ContextTypeE(
    QV4::Compiler::Module *self,
    QQmlJS::AST::Node *node,
    QV4::Compiler::Context *parent,
    QV4::Compiler::ContextType compilationMode) {
  return self->newContext(node, parent, compilationMode);
}
