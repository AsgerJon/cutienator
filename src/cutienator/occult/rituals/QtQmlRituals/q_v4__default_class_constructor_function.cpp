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

//  from ../qtdeclarative/src/qml/jsruntime/qv4functionobject.cpp, line 655, as _ZN3QV431DefaultClassConstructorFunction24virtualCallAsConstructorEPKNS_14FunctionObjectEPKNS_5ValueEiS6_
namespace QV4 {
inline ReturnedValue DefaultClassConstructorFunction::virtualCallAsConstructor(const FunctionObject *f, const Value *argv, int argc, const Value *newTarget)
{
    const DefaultClassConstructorFunction *c = static_cast<const DefaultClassConstructorFunction *>(f);
    ExecutionEngine *v4 = f->engine();

    Scope scope(v4);

    if (!c->d()->isDerivedConstructor) {
        ScopedObject proto(scope, static_cast<const Object *>(newTarget)->get(scope.engine->id_prototype()));
        ScopedObject c(scope, scope.engine->newObject());
        c->setPrototypeUnchecked(proto);
        return c->asReturnedValue();
    }

    ScopedFunctionObject super(scope, f->getPrototypeOf());
    Q_ASSERT(super->isFunctionObject());

    JSTypesStackFrame frame;
    frame.init(nullptr, argv, argc);
    frame.setupJSFrame(v4->jsStackTop, *f, c->scope(),
                       Value::undefinedValue(),
                       newTarget ? *newTarget : Value::undefinedValue(), argc, argc);

    frame.push(v4);
    v4->jsStackTop += frame.requiredJSStackFrameSize(argc);

    // Do a super call
    ReturnedValue result = super->callAsConstructor(argv, argc, newTarget);
    ReturnedValue thisObject = frame.jsFrame->thisObject.asReturnedValue();

    frame.pop(v4);

    if (Q_UNLIKELY(v4->hasException))
        return Encode::undefined();
    else if (Value::fromReturnedValue(result).isObject())
        return result;
    else if (!Value::fromReturnedValue(result).isUndefined())
        return v4->throwTypeError();
    else if (Value::fromReturnedValue(thisObject).isEmpty()) {
        Scope scope(v4);
        ScopedString s(scope, v4->newString(QStringLiteral("this")));
        return v4->throwReferenceError(s);
    }

    return thisObject;
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4functionobject.cpp, line 702, as _ZN3QV431DefaultClassConstructorFunction11virtualCallEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue DefaultClassConstructorFunction::virtualCall(const FunctionObject *f, const Value *, const Value *, int)
{
    return f->engine()->throwTypeError(QStringLiteral("Cannot call a class constructor without |new|"));
}
}  // namespace QV4
//  -----------------------------------------------------------------------

//  void QV4::DefaultClassConstructorFunction::__dataTest()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV431DefaultClassConstructorFunction10__dataTestEv(
    QV4::DefaultClassConstructorFunction *self) {
  self->__dataTest();
}

//  QV4::Heap::DefaultClassConstructorFunction
//      *QV4::DefaultClassConstructorFunction::d_unchecked() const
extern "C" Q_DECL_EXPORT
QV4::Heap::DefaultClassConstructorFunction *ritual_ZNK3QV431DefaultClassConstructorFunction11d_uncheckedEv(
    const QV4::DefaultClassConstructorFunction *self) {
  return self->d_unchecked();
}

//  QV4::Heap::DefaultClassConstructorFunction
//      *QV4::DefaultClassConstructorFunction::d() const
extern "C" Q_DECL_EXPORT
QV4::Heap::DefaultClassConstructorFunction *ritual_ZNK3QV431DefaultClassConstructorFunction1dEv(
    const QV4::DefaultClassConstructorFunction *self) {
  return self->d();
}

//  Heap::ExecutionContext *QV4::DefaultClassConstructorFunction::scope()
//      const
extern "C" Q_DECL_EXPORT
QV4::Heap::ExecutionContext *ritual_ZNK3QV431DefaultClassConstructorFunction5scopeEv(
    const QV4::DefaultClassConstructorFunction *self) {
  return self->scope();
}

//  ReturnedValue
//      QV4::DefaultClassConstructorFunction::virtualCallAsConstructor(const
//      FunctionObject *a0, const Value *argv, int argc, const Value *a3)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV431DefaultClassConstructorFunction24virtualCallAsConstructorEPKNS_14FunctionObjectEPKNS_5ValueEiS6_(
    const QV4::FunctionObject *a0,
    const QV4::Value *argv,
    int argc,
    const QV4::Value *a3) {
  return QV4::DefaultClassConstructorFunction::virtualCallAsConstructor(
      a0,
      argv,
      argc,
      a3);
}

//  ReturnedValue QV4::DefaultClassConstructorFunction::virtualCall(const
//      FunctionObject *f, const Value *thisObject, const Value *argv, int
//      argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV431DefaultClassConstructorFunction11virtualCallEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *f,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::DefaultClassConstructorFunction::virtualCall(
      f,
      thisObject,
      argv,
      argc);
}
