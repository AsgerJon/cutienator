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

//  from ../qtdeclarative/src/qml/jsruntime/qv4arraybuffer.cpp, line 141, as _ZN3QV426SharedArrayBufferPrototype4initEPNS_15ExecutionEngineEPNS_6ObjectE
namespace QV4 {
inline void SharedArrayBufferPrototype::init(ExecutionEngine *engine, Object *ctor)
{
    Scope scope(engine);
    ScopedObject o(scope);
    ctor->defineReadonlyConfigurableProperty(engine->id_length(), Value::fromInt32(1));
    ctor->defineReadonlyProperty(engine->id_prototype(), (o = this));
    ctor->addSymbolSpecies();

    defineDefaultProperty(engine->id_constructor(), (o = ctor));
    defineAccessorProperty(QStringLiteral("byteLength"), method_get_byteLength, nullptr);
    defineDefaultProperty(QStringLiteral("slice"), method_slice, 2);
    ScopedString name(scope, engine->newString(QStringLiteral("SharedArrayBuffer")));
    defineReadonlyConfigurableProperty(scope.engine->symbol_toStringTag(), name);
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4arraybuffer.cpp, line 156, as _ZN3QV426SharedArrayBufferPrototype21method_get_byteLengthEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue SharedArrayBufferPrototype::method_get_byteLength(const FunctionObject *b, const Value *thisObject, const Value *, int)
{
    const SharedArrayBuffer *a = thisObject->as<SharedArrayBuffer>();
    if (!a || a->hasDetachedArrayData() || !a->isSharedArrayBuffer())
        return b->engine()->throwTypeError();

    return Encode(a->arrayDataLength());
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4arraybuffer.cpp, line 165, as _ZN3QV426SharedArrayBufferPrototype12method_sliceEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue SharedArrayBufferPrototype::method_slice(const FunctionObject *b, const Value *thisObject, const Value *argv, int argc)
{
    return slice(b, thisObject, argv, argc, true);
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4arraybuffer.cpp, line 170, as _ZN3QV426SharedArrayBufferPrototype5sliceEPKNS_14FunctionObjectEPKNS_5ValueES6_ib
namespace QV4 {
inline ReturnedValue SharedArrayBufferPrototype::slice(const FunctionObject *b, const Value *thisObject, const Value *argv, int argc, bool shared)
{
    Scope scope(b);
    const SharedArrayBuffer *a = thisObject->as<SharedArrayBuffer>();
    if (!a || a->hasDetachedArrayData() || (a->isSharedArrayBuffer() != shared))
        return scope.engine->throwTypeError();

    const uint aDataLength = a->arrayDataLength();

    double start = argc > 0 ? argv[0].toInteger() : 0;
    double end = (argc < 2 || argv[1].isUndefined()) ? aDataLength : argv[1].toInteger();
    if (scope.hasException())
        return QV4::Encode::undefined();

    double first = (start < 0) ? qMax(aDataLength + start, 0.) : qMin(start, double(aDataLength));
    double final = (end < 0) ? qMax(aDataLength + end, 0.) : qMin(end, double(aDataLength));

    const FunctionObject *constructor = a->speciesConstructor(scope, shared ? scope.engine->sharedArrayBufferCtor() : scope.engine->arrayBufferCtor());
    if (!constructor)
        return scope.engine->throwTypeError();

    double newLen = qMax(final - first, 0.);
    ScopedValue argument(scope, QV4::Encode(newLen));
    QV4::Scoped<SharedArrayBuffer> newBuffer(scope, constructor->callAsConstructor(argument, 1));
    if (!newBuffer || newBuffer->arrayDataLength() < newLen ||
        newBuffer->hasDetachedArrayData() || (newBuffer->isSharedArrayBuffer() != shared) ||
        newBuffer->sameValue(*a) ||
        a->hasDetachedArrayData())
        return scope.engine->throwTypeError();

    memcpy(newBuffer->arrayData(), a->constArrayData() + (uint)first, newLen);
    return newBuffer->asReturnedValue();
}
}  // namespace QV4
//  -----------------------------------------------------------------------

//  void QV4::SharedArrayBufferPrototype::init(ExecutionEngine *engine,
//      Object *ctor)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV426SharedArrayBufferPrototype4initEPNS_15ExecutionEngineEPNS_6ObjectE(
    QV4::SharedArrayBufferPrototype *self,
    QV4::ExecutionEngine *engine,
    QV4::Object *ctor) {
  self->init(engine, ctor);
}

//  ReturnedValue
//      QV4::SharedArrayBufferPrototype::method_get_byteLength(const
//      FunctionObject *a0, const Value *thisObject, const Value *argv, int
//      argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV426SharedArrayBufferPrototype21method_get_byteLengthEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::SharedArrayBufferPrototype::method_get_byteLength(
      a0,
      thisObject,
      argv,
      argc);
}

//  ReturnedValue QV4::SharedArrayBufferPrototype::method_slice(const
//      FunctionObject *a0, const Value *thisObject, const Value *argv, int
//      argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV426SharedArrayBufferPrototype12method_sliceEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::SharedArrayBufferPrototype::method_slice(
      a0,
      thisObject,
      argv,
      argc);
}

//  ReturnedValue QV4::SharedArrayBufferPrototype::slice(const FunctionObject
//      *b, const Value *thisObject, const Value *argv, int argc, bool
//      shared)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV426SharedArrayBufferPrototype5sliceEPKNS_14FunctionObjectEPKNS_5ValueES6_ib(
    const QV4::FunctionObject *b,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc,
    bool shared) {
  return QV4::SharedArrayBufferPrototype::slice(
      b,
      thisObject,
      argv,
      argc,
      shared);
}
