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
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

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

//  void QV4::Heap::JavaScriptFunctionObject::markObjects(Heap::Base *b,
//      MarkStack *stack)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap24JavaScriptFunctionObject11markObjectsEPNS0_4BaseEPNS_9MarkStackE(
    QV4::Heap::Base *b,
    QV4::MarkStack *stack) {
  QV4::Heap::JavaScriptFunctionObject::markObjects(b, stack);
}

//  void QV4::Heap::JavaScriptFunctionObject::init(QV4::ExecutionContext
//      *scope, QV4::Function *function, QV4::String *n)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap24JavaScriptFunctionObject4initEPNS_16ExecutionContextEPNS_8FunctionEPNS_6StringE(
    QV4::Heap::JavaScriptFunctionObject *self,
    QV4::ExecutionContext *scope,
    QV4::Function *function,
    QV4::String *n) {
  self->init(scope, function, n);
}

//  void QV4::Heap::JavaScriptFunctionObject::destroy()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap24JavaScriptFunctionObject7destroyEv(
    QV4::Heap::JavaScriptFunctionObject *self) {
  self->destroy();
}

//  void QV4::Heap::JavaScriptFunctionObject::setFunction(Function *f)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap24JavaScriptFunctionObject11setFunctionEPNS_8FunctionE(
    QV4::Heap::JavaScriptFunctionObject *self,
    QV4::Function *f) {
  self->setFunction(f);
}

//  unsigned int QV4::Heap::JavaScriptFunctionObject::formalParameterCount()
extern "C" Q_DECL_EXPORT
unsigned int ritual_ZN3QV44Heap24JavaScriptFunctionObject20formalParameterCountEv(
    QV4::Heap::JavaScriptFunctionObject *self) {
  return self->formalParameterCount();
}

//  unsigned int QV4::Heap::JavaScriptFunctionObject::varCount()
extern "C" Q_DECL_EXPORT
unsigned int ritual_ZN3QV44Heap24JavaScriptFunctionObject8varCountEv(
    QV4::Heap::JavaScriptFunctionObject *self) {
  return self->varCount();
}

//  QV4::Heap::JavaScriptFunctionObject as the
//      QV4::Heap::JavaScriptFunctionObjectData it is built on
extern "C" Q_DECL_EXPORT
QV4::Heap::JavaScriptFunctionObjectData *ritual_cast_QV4_Heap_JavaScriptFunctionObject_QV4_Heap_JavaScriptFunctionObjectData(
    QV4::Heap::JavaScriptFunctionObject *self) {
  return static_cast<QV4::Heap::JavaScriptFunctionObjectData *>(self);
}
