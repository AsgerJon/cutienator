//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4compilercontext_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4compilercontext_p.h>
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
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
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
//  -----------------------------------------------------------------------

//  bool QV4::Compiler::Context::Member::isLexicallyScoped() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV48Compiler7Context6Member17isLexicallyScopedEv(
    const QV4::Compiler::Context::Member *self) {
  return self->isLexicallyScoped();
}

//  bool QV4::Compiler::Context::Member::requiresTDZCheck(const
//      QQmlJS::SourceLocation &accessLocation, bool
//      accessAcrossContextBoundaries) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV48Compiler7Context6Member16requiresTDZCheckERKN6QQmlJS14SourceLocationEb(
    const QV4::Compiler::Context::Member *self,
    const QQmlJS::SourceLocation *accessLocation,
    bool accessAcrossContextBoundaries) {
  return self->requiresTDZCheck(
      *accessLocation,
      accessAcrossContextBoundaries);
}

//  QV4::Compiler::Context::Member::~Member()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV48Compiler7Context6MemberD1Ev(
    QV4::Compiler::Context::Member *self) {
  delete self;
}
