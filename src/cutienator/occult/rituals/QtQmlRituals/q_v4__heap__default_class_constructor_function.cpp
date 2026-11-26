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

//  from ../qtdeclarative/src/qml/jsruntime/qv4functionobject.cpp, line 585, as _ZN3QV44Heap31DefaultClassConstructorFunction4initEPNS_16ExecutionContextE
namespace QV4 {
inline void Heap::DefaultClassConstructorFunction::init(QV4::ExecutionContext *scope)
{
    Scope s(scope->engine());
    FunctionObject::init(s.engine, nullptr);
    this->scope.set(s.engine, scope->d());
}
}  // namespace QV4
//  -----------------------------------------------------------------------

//  void QV4::Heap::DefaultClassConstructorFunction::markObjects(Heap::Base
//      *b, MarkStack *stack)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap31DefaultClassConstructorFunction11markObjectsEPNS0_4BaseEPNS_9MarkStackE(
    QV4::Heap::Base *b,
    QV4::MarkStack *stack) {
  QV4::Heap::DefaultClassConstructorFunction::markObjects(b, stack);
}

//  void
//      QV4::Heap::DefaultClassConstructorFunction::init(QV4::ExecutionContex
//      t *scope)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap31DefaultClassConstructorFunction4initEPNS_16ExecutionContextE(
    QV4::Heap::DefaultClassConstructorFunction *self,
    QV4::ExecutionContext *scope) {
  self->init(scope);
}

//  QV4::Heap::DefaultClassConstructorFunction as the
//      QV4::Heap::DefaultClassConstructorFunctionData it is built on
extern "C" Q_DECL_EXPORT
QV4::Heap::DefaultClassConstructorFunctionData *ritual_cast_QV4_Heap_DefaultClassConstructorFunction_QV4_Heap_DefaultClassConstructorFunctionData(
    QV4::Heap::DefaultClassConstructorFunction *self) {
  return static_cast<QV4::Heap::DefaultClassConstructorFunctionData *>(self);
}
