//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlbuiltinfunctions_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlbuiltinfunctions_p.h>
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
#include <QtQml/private/qqmlbuiltinfunctions_p.h>
#include <QtQml/private/qqmlcomponent_p.h>
#include <QtQml/private/qqmldebugconnector_p.h>
#include <QtQml/private/qqmldebugserviceinterfaces_p.h>
#include <QtQml/private/qqmldelayedcallqueue_p.h>
#include <QtQml/private/qqmlengine_p.h>
#include <QtQml/private/qqmlloggingcategorybase_p.h>
#include <QtQml/private/qqmlplatform_p.h>
#include <QtQml/private/qqmlstringconverters_p.h>
#include <QtQml/private/qv4dateobject_p.h>
#include <QtQml/private/qv4domerrors_p.h>
#include <QtQml/private/qv4engine_p.h>
#include <QtQml/private/qv4functionobject_p.h>
#include <QtQml/private/qv4include_p.h>
#include <QtQml/private/qv4mm_p.h>
#include <QtQml/private/qv4qobjectwrapper_p.h>
#include <QtQml/private/qv4sequenceobject_p.h>
#include <QtQml/private/qv4stackframe_p.h>
#include <QtQml/qqmlfile.h>
#include <QtCore/qcoreapplication.h>
#include <QtCore/qcryptographichash.h>
#include <QtCore/qdatetime.h>
#include <QtCore/qfileinfo.h>
#include <QtCore/qloggingcategory.h>
#include <QtCore/qpoint.h>
#include <QtCore/qrect.h>
#include <QtCore/qsize.h>
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtCore/qvarlengtharray.h>
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

//  from ../qtdeclarative/src/qml/qml/qqmlbuiltinfunctions.cpp, line 1828, as _ZN3QV44Heap19QQmlBindingFunction4initEPKNS_24JavaScriptFunctionObjectE
namespace QV4 {
inline void Heap::QQmlBindingFunction::init(const QV4::JavaScriptFunctionObject *bindingFunction)
{
    Scope scope(bindingFunction->engine());
    ScopedContext context(scope, bindingFunction->scope());
    JavaScriptFunctionObject::init(context, bindingFunction->function());
    this->bindingFunction.set(internalClass->engine, bindingFunction->d());
}
}  // namespace QV4
//  -----------------------------------------------------------------------

//  void QV4::Heap::QQmlBindingFunction::markObjects(Heap::Base *b, MarkStack
//      *stack)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap19QQmlBindingFunction11markObjectsEPNS0_4BaseEPNS_9MarkStackE(
    QV4::Heap::Base *b,
    QV4::MarkStack *stack) {
  QV4::Heap::QQmlBindingFunction::markObjects(b, stack);
}

//  void QV4::Heap::QQmlBindingFunction::init(const
//      QV4::JavaScriptFunctionObject *bindingFunction)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap19QQmlBindingFunction4initEPKNS_24JavaScriptFunctionObjectE(
    QV4::Heap::QQmlBindingFunction *self,
    const QV4::JavaScriptFunctionObject *bindingFunction) {
  self->init(bindingFunction);
}

//  QV4::Heap::QQmlBindingFunction as the QV4::Heap::QQmlBindingFunctionData
//      it is built on
extern "C" Q_DECL_EXPORT
QV4::Heap::QQmlBindingFunctionData *ritual_cast_QV4_Heap_QQmlBindingFunction_QV4_Heap_QQmlBindingFunctionData(
    QV4::Heap::QQmlBindingFunction *self) {
  return static_cast<QV4::Heap::QQmlBindingFunctionData *>(self);
}
