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

//  from ../qtdeclarative/src/qml/jsruntime/qv4functionobject.cpp, line 448, as _ZN3QV414ScriptFunction24virtualCallAsConstructorEPKNS_14FunctionObjectEPKNS_5ValueEiS6_
namespace QV4 {
inline ReturnedValue ScriptFunction::virtualCallAsConstructor(const FunctionObject *fo, const Value *argv, int argc, const Value *newTarget)
{
    ExecutionEngine *v4 = fo->engine();
    const ScriptFunction *f = static_cast<const ScriptFunction *>(fo);
    Q_ASSERT(newTarget->isFunctionObject());
    const FunctionObject *nt = static_cast<const FunctionObject *>(newTarget);

    Scope scope(v4);
    Scoped<InternalClass> ic(scope);
    if (nt->d() == f->d()) {
        ic = f->classForConstructor();
    } else {
        ScopedObject o(scope, nt->protoProperty());
        ic = scope.engine->internalClasses(EngineBase::Class_Object);
        if (o)
            ic = ic->changePrototype(o->d());
    }
    ScopedValue thisObject(scope, v4->memoryManager->allocObject<Object>(ic));

    JSTypesStackFrame frame;
    frame.init(f->function(), argv, argc);
    frame.setupJSFrame(v4->jsStackTop, *f, f->scope(),
                       thisObject,
                       newTarget ? *newTarget : Value::undefinedValue());

    frame.push(v4);
    v4->jsStackTop += frame.requiredJSStackFrameSize();

    ReturnedValue result = Moth::VME::exec(&frame, v4);

    frame.pop(v4);

    if (Q_UNLIKELY(v4->hasException))
        return Encode::undefined();
    else if (!Value::fromReturnedValue(result).isObject())
        return thisObject->asReturnedValue();
    return result;
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4functionobject.cpp, line 646, as _ZN3QV419ConstructorFunction11virtualCallEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue ConstructorFunction::virtualCall(const FunctionObject *f, const Value *, const Value *, int)
{
    return f->engine()->throwTypeError(QStringLiteral("Cannot call a class constructor without |new|"));
}
}  // namespace QV4
//  -----------------------------------------------------------------------

//  void QV4::ConstructorFunction::__dataTest()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV419ConstructorFunction10__dataTestEv(
    QV4::ConstructorFunction *self) {
  self->__dataTest();
}

//  QV4::Heap::ConstructorFunction *QV4::ConstructorFunction::d_unchecked()
//      const
extern "C" Q_DECL_EXPORT
QV4::Heap::ConstructorFunction *ritual_ZNK3QV419ConstructorFunction11d_uncheckedEv(
    const QV4::ConstructorFunction *self) {
  return self->d_unchecked();
}

//  QV4::Heap::ConstructorFunction *QV4::ConstructorFunction::d() const
extern "C" Q_DECL_EXPORT
QV4::Heap::ConstructorFunction *ritual_ZNK3QV419ConstructorFunction1dEv(
    const QV4::ConstructorFunction *self) {
  return self->d();
}

//  Heap::InternalClass
//      *QV4::ConstructorFunction::defaultInternalClass(QV4::EngineBase *e)
extern "C" Q_DECL_EXPORT
QV4::Heap::InternalClass *ritual_ZN3QV419ConstructorFunction20defaultInternalClassEPNS_10EngineBaseE(
    QV4::EngineBase *e) {
  return QV4::ConstructorFunction::defaultInternalClass(e);
}

//  ReturnedValue QV4::ConstructorFunction::virtualCall(const FunctionObject
//      *f, const Value *thisObject, const Value *argv, int argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV419ConstructorFunction11virtualCallEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *f,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::ConstructorFunction::virtualCall(f, thisObject, argv, argc);
}
