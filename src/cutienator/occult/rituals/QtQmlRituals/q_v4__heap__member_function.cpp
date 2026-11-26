//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4functionobject_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4functionobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qv4object_p.h>
#include <QtQml/private/qv4function_p.h>
#include <QtQml/private/qv4symbol_p.h>
#include <QtQml/private/qv4mm_p.h>
#include <QtQml/private/qv4scopedvalue_p.h>
#include <QtQml/private/qv4argumentsobject_p.h>
#include <QtQml/private/qqmljsengine_p.h>
#include <QtQml/private/qqmljsast_p.h>
#include <QtQml/private/qqmljavascriptexpression_p.h>
#include <QtQml/private/qqmlengine_p.h>
#include <QtQml/private/qv4runtimecodegen_p.h>
#include <QtCore/private/qlocale_tools_p.h>
#include <QtQml/private/qqmlbuiltinfunctions_p.h>
#include <QtQml/private/qv4jscall_p.h>
#include <QtQml/private/qv4vme_moth_p.h>
#include <QtQml/private/qv4alloca_p.h>
#include <QtCore/QDebug>
#include <algorithm>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/jsruntime/qv4functionobject.cpp, line 565, as _ZN3QV44Heap13ArrowFunction4initEPNS_16ExecutionContextEPNS_8FunctionEPNS_6StringE
namespace QV4 {
inline void Heap::ArrowFunction::init(QV4::ExecutionContext *scope, Function *function, QV4::String *n)
{
    Q_ASSERT(function);
    JavaScriptFunctionObject::init(scope, function, n);

    Scope s(scope);
    Q_ASSERT(internalClass && internalClass->verifyIndex(s.engine->id_length()->propertyKey(), Index_Length));
    setProperty(s.engine, Index_Length, Value::fromInt32(int(function->compiledFunction->length)));
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4functionobject.cpp, line 55, as _ZN3QV44Heap24JavaScriptFunctionObject4initEPNS_16ExecutionContextEPNS_8FunctionEPNS_6StringE
namespace QV4 {
inline void Heap::JavaScriptFunctionObject::init(
        QV4::ExecutionContext *scope, Function *function, QV4::String *n)
{
    Q_ASSERT(n || function);
    Scope s(scope->engine());
    ScopedString name(s, n ? n->d() : function->name());
    FunctionObject::init(s.engine, name);
    this->scope.set(s.engine, scope->d());
    setFunction(function);
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4functionobject.cpp, line 66, as _ZN3QV44Heap24JavaScriptFunctionObject11setFunctionEPNS_8FunctionE
namespace QV4 {
inline void Heap::JavaScriptFunctionObject::setFunction(Function *f)
{
    if (f) {
        function = f;
        function->executableCompilationUnit()->addref();
    }
}
}  // namespace QV4
//  -----------------------------------------------------------------------

//  void QV4::Heap::MemberFunction::markObjects(Heap::Base *b, MarkStack
//      *stack)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap14MemberFunction11markObjectsEPNS0_4BaseEPNS_9MarkStackE(
    QV4::Heap::Base *b,
    QV4::MarkStack *stack) {
  QV4::Heap::MemberFunction::markObjects(b, stack);
}

//  void QV4::Heap::MemberFunction::init(QV4::ExecutionContext *scope,
//      Function *function, QV4::String *name)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap14MemberFunction4initEPNS_16ExecutionContextEPNS_8FunctionEPNS_6StringE(
    QV4::Heap::MemberFunction *self,
    QV4::ExecutionContext *scope,
    QV4::Function *function,
    QV4::String *name) {
  self->init(scope, function, name);
}

//  QV4::Heap::MemberFunction as the QV4::Heap::MemberFunctionData it is
//      built on
extern "C" Q_DECL_EXPORT
QV4::Heap::MemberFunctionData *ritual_cast_QV4_Heap_MemberFunction_QV4_Heap_MemberFunctionData(
    QV4::Heap::MemberFunction *self) {
  return static_cast<QV4::Heap::MemberFunctionData *>(self);
}
