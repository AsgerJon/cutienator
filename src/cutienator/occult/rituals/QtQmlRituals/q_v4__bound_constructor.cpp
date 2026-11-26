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

//  from ../qtdeclarative/src/qml/jsruntime/qv4functionobject.cpp, line 769, as _ZN3QV416BoundConstructor24virtualCallAsConstructorEPKNS_14FunctionObjectEPKNS_5ValueEiS6_
namespace QV4 {
inline ReturnedValue BoundConstructor::virtualCallAsConstructor(
        const FunctionObject *fo, const Value *argv, int argc, const Value *)
{
    const BoundFunction *f = static_cast<const BoundFunction *>(fo);
    Scope scope(f->engine());

    if (scope.hasException())
        return Encode::undefined();

    Scoped<MemberData> boundArgs(scope, f->boundArgs());
    ScopedFunctionObject target(scope, f->target());
    JSCallArguments jsCallData(scope, (boundArgs ? boundArgs->size() : 0) + argc);
    Value *argp = jsCallData.args;
    if (boundArgs) {
        memcpy(argp, boundArgs->data(), boundArgs->size()*sizeof(Value));
        argp += boundArgs->size();
    }
    memcpy(argp, argv, argc*sizeof(Value));
    return target->callAsConstructor(jsCallData);
}
}  // namespace QV4
//  -----------------------------------------------------------------------

//  void QV4::BoundConstructor::__dataTest()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV416BoundConstructor10__dataTestEv(
    QV4::BoundConstructor *self) {
  self->__dataTest();
}

//  QV4::Heap::BoundConstructor *QV4::BoundConstructor::d_unchecked() const
extern "C" Q_DECL_EXPORT
QV4::Heap::BoundConstructor *ritual_ZNK3QV416BoundConstructor11d_uncheckedEv(
    const QV4::BoundConstructor *self) {
  return self->d_unchecked();
}

//  QV4::Heap::BoundConstructor *QV4::BoundConstructor::d() const
extern "C" Q_DECL_EXPORT
QV4::Heap::BoundConstructor *ritual_ZNK3QV416BoundConstructor1dEv(
    const QV4::BoundConstructor *self) {
  return self->d();
}

//  ReturnedValue QV4::BoundConstructor::virtualCallAsConstructor(const
//      FunctionObject *f, const Value *argv, int argc, const Value *a3)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV416BoundConstructor24virtualCallAsConstructorEPKNS_14FunctionObjectEPKNS_5ValueEiS6_(
    const QV4::FunctionObject *f,
    const QV4::Value *argv,
    int argc,
    const QV4::Value *a3) {
  return QV4::BoundConstructor::virtualCallAsConstructor(f, argv, argc, a3);
}
