//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4functionobject_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4functionobject_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4value_p.h>
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

//  from ../qtdeclarative/src/qml/jsruntime/qv4functionobject.cpp, line 711, as _ZN3QV44Heap13BoundFunction4initEPNS_14FunctionObjectERKNS_5ValueEPNS_10MemberDataE
namespace QV4 {
inline void Heap::BoundFunction::init(
        QV4::FunctionObject *target, const Value &boundThis, QV4::MemberData *boundArgs)
{
    ExecutionEngine *engine = target->engine();
    Scope s(engine);
    ScopedString name(s, engine->newString(QStringLiteral("__bound function__")));
    if (auto *js = target->as<QV4::JavaScriptFunctionObject>()) {
        ScopedContext ctx(s, js->scope());
        JavaScriptFunctionObject::init(ctx, js->function(), name);
    } else {
        Q_ASSERT(name);
        JavaScriptFunctionObject::init(engine->rootContext(), nullptr, name);
    }

    this->target.set(s.engine, target->d());
    this->boundArgs.set(s.engine, boundArgs ? boundArgs->d() : nullptr);
    this->boundThis.set(s.engine, boundThis);

    ScopedObject f(s, this);

    ScopedValue l(s, target->get(engine->id_length()));
    int len = l->toUInt32();
    if (boundArgs)
        len -= boundArgs->size();
    if (len < 0)
        len = 0;
    f->defineReadonlyConfigurableProperty(engine->id_length(), Value::fromInt32(len));

    ScopedProperty pd(s);
    pd->value = engine->thrower();
    pd->set = engine->thrower();
    f->insertMember(engine->id_arguments(), pd, Attr_Accessor|Attr_NotConfigurable|Attr_NotEnumerable);
    f->insertMember(engine->id_caller(), pd, Attr_Accessor|Attr_NotConfigurable|Attr_NotEnumerable);
}
}  // namespace QV4
//  -----------------------------------------------------------------------

//  void QV4::Heap::BoundFunction::markObjects(Heap::Base *b, MarkStack
//      *stack)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap13BoundFunction11markObjectsEPNS0_4BaseEPNS_9MarkStackE(
    QV4::Heap::Base *b,
    QV4::MarkStack *stack) {
  QV4::Heap::BoundFunction::markObjects(b, stack);
}

//  void QV4::Heap::BoundFunction::init(QV4::FunctionObject *target, const
//      Value &boundThis, QV4::MemberData *boundArgs)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap13BoundFunction4initEPNS_14FunctionObjectERKNS_5ValueEPNS_10MemberDataE(
    QV4::Heap::BoundFunction *self,
    QV4::FunctionObject *target,
    const QV4::Value *boundThis,
    QV4::MemberData *boundArgs) {
  self->init(target, *boundThis, boundArgs);
}

//  QV4::Heap::BoundFunction as the QV4::Heap::BoundFunctionData it is built
//      on
extern "C" Q_DECL_EXPORT
QV4::Heap::BoundFunctionData *ritual_cast_QV4_Heap_BoundFunction_QV4_Heap_BoundFunctionData(
    QV4::Heap::BoundFunction *self) {
  return static_cast<QV4::Heap::BoundFunctionData *>(self);
}
