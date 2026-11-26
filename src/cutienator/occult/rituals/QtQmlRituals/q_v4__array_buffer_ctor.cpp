//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4arraybuffer_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4arraybuffer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qv4arraybuffer_p.h>
#include <QtQml/private/qv4typedarray_p.h>
#include <QtQml/private/qv4dataview_p.h>
#include <QtQml/private/qv4symbol_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/jsruntime/qv4arraybuffer.cpp, line 56, as _ZN3QV415ArrayBufferCtor24virtualCallAsConstructorEPKNS_14FunctionObjectEPKNS_5ValueEiS6_
namespace QV4 {
inline ReturnedValue ArrayBufferCtor::virtualCallAsConstructor(const FunctionObject *f, const Value *argv, int argc, const Value *newTarget)
{
    ExecutionEngine *v4 = f->engine();
    Scope scope(v4);

    ScopedValue l(scope, argc ? argv[0] : Value::undefinedValue());
    double dl = l->toInteger();
    if (v4->hasException)
        return Encode::undefined();
    uint len = (uint)qBound(0., dl, (double)UINT_MAX);
    if (len != dl)
        return v4->throwRangeError(QLatin1String("ArrayBuffer constructor: invalid length"));

    Scoped<ArrayBuffer> a(scope, v4->newArrayBuffer(len));
    if (newTarget->heapObject() != f->heapObject() && newTarget->isFunctionObject()) {
        const FunctionObject *nt = static_cast<const FunctionObject *>(newTarget);
        ScopedObject o(scope, nt->protoProperty());
        if (o)
            a->setPrototypeOf(o);
    }
    if (scope.hasException())
        return Encode::undefined();

    return a->asReturnedValue();
}
}  // namespace QV4
//  -----------------------------------------------------------------------

//  void QV4::ArrayBufferCtor::__dataTest()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV415ArrayBufferCtor10__dataTestEv(
    QV4::ArrayBufferCtor *self) {
  self->__dataTest();
}

//  QV4::Heap::ArrayBufferCtor *QV4::ArrayBufferCtor::d_unchecked() const
extern "C" Q_DECL_EXPORT
QV4::Heap::ArrayBufferCtor *ritual_ZNK3QV415ArrayBufferCtor11d_uncheckedEv(
    const QV4::ArrayBufferCtor *self) {
  return self->d_unchecked();
}

//  QV4::Heap::ArrayBufferCtor *QV4::ArrayBufferCtor::d() const
extern "C" Q_DECL_EXPORT
QV4::Heap::ArrayBufferCtor *ritual_ZNK3QV415ArrayBufferCtor1dEv(
    const QV4::ArrayBufferCtor *self) {
  return self->d();
}

//  ReturnedValue QV4::ArrayBufferCtor::virtualCallAsConstructor(const
//      FunctionObject *f, const Value *argv, int argc, const Value *a3)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV415ArrayBufferCtor24virtualCallAsConstructorEPKNS_14FunctionObjectEPKNS_5ValueEiS6_(
    const QV4::FunctionObject *f,
    const QV4::Value *argv,
    int argc,
    const QV4::Value *a3) {
  return QV4::ArrayBufferCtor::virtualCallAsConstructor(f, argv, argc, a3);
}
