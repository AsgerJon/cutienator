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
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/jsruntime/qv4functionobject.cpp, line 746, as _ZN3QV413BoundFunction11virtualCallEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue BoundFunction::virtualCall(const FunctionObject *fo, const Value *, const Value *argv, int argc)
{
    QV4::ExecutionEngine *v4 = fo->engine();
    if (v4->hasException)
        return Encode::undefined();

    const BoundFunction *f = static_cast<const BoundFunction *>(fo);
    Scope scope(v4);
    Scoped<MemberData> boundArgs(scope, f->boundArgs());
    ScopedFunctionObject target(scope, f->target());
    JSCallArguments jsCallData(scope, (boundArgs ? boundArgs->size() : 0) + argc);
    *jsCallData.thisObject = f->boundThis();
    Value *argp = jsCallData.args;
    if (boundArgs) {
        memcpy(argp, boundArgs->data(), boundArgs->size()*sizeof(Value));
        argp += boundArgs->size();
    }
    memcpy(argp, argv, argc*sizeof(Value));
    return checkedResult(v4, target->call(jsCallData));
}
}  // namespace QV4
//  -----------------------------------------------------------------------

//  void QV4::BoundFunction::__dataTest()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV413BoundFunction10__dataTestEv(QV4::BoundFunction *self) {
  self->__dataTest();
}

//  QV4::Heap::BoundFunction *QV4::BoundFunction::d_unchecked() const
extern "C" Q_DECL_EXPORT
QV4::Heap::BoundFunction *ritual_ZNK3QV413BoundFunction11d_uncheckedEv(
    const QV4::BoundFunction *self) {
  return self->d_unchecked();
}

//  QV4::Heap::BoundFunction *QV4::BoundFunction::d() const
extern "C" Q_DECL_EXPORT
QV4::Heap::BoundFunction *ritual_ZNK3QV413BoundFunction1dEv(
    const QV4::BoundFunction *self) {
  return self->d();
}

//  Heap::FunctionObject *QV4::BoundFunction::target() const
extern "C" Q_DECL_EXPORT
QV4::Heap::FunctionObject *ritual_ZNK3QV413BoundFunction6targetEv(
    const QV4::BoundFunction *self) {
  return self->target();
}

//  Value QV4::BoundFunction::boundThis() const
extern "C" Q_DECL_EXPORT
QV4::Value *ritual_ZNK3QV413BoundFunction9boundThisEv(
    const QV4::BoundFunction *self) {
  return new QV4::Value(self->boundThis());
}

//  Heap::MemberData *QV4::BoundFunction::boundArgs() const
extern "C" Q_DECL_EXPORT
QV4::Heap::MemberData *ritual_ZNK3QV413BoundFunction9boundArgsEv(
    const QV4::BoundFunction *self) {
  return self->boundArgs();
}

//  ReturnedValue QV4::BoundFunction::virtualCall(const FunctionObject *f,
//      const Value *thisObject, const Value *argv, int argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV413BoundFunction11virtualCallEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *f,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::BoundFunction::virtualCall(f, thisObject, argv, argc);
}
