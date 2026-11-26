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
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/jsruntime/qv4arraybuffer.cpp, line 82, as _ZN3QV415ArrayBufferCtor13method_isViewEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue ArrayBufferCtor::method_isView(const FunctionObject *, const Value *, const Value *argv, int argc)
{
    if (argc < 1)
        return Encode(false);

    if (argv[0].as<TypedArray>() ||
        argv[0].as<DataView>())
        return Encode(true);

    return Encode(false);
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

//  from ../qtdeclarative/src/qml/jsruntime/qv4arraybuffer.cpp, line 222, as _ZN3QV420ArrayBufferPrototype21method_get_byteLengthEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue ArrayBufferPrototype::method_get_byteLength(const FunctionObject *f, const Value *thisObject, const Value *, int)
{
    const ArrayBuffer *a = thisObject->as<ArrayBuffer>();
    if (!a || a->isSharedArrayBuffer())
        return f->engine()->throwTypeError();

    if (a->hasDetachedArrayData())
        return Encode(0);

    return Encode(a->arrayDataLength());
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4arraybuffer.cpp, line 234, as _ZN3QV420ArrayBufferPrototype12method_sliceEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue ArrayBufferPrototype::method_slice(const FunctionObject *b, const Value *thisObject, const Value *argv, int argc)
{
    return slice(b, thisObject, argv, argc, false);
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4arraybuffer.cpp, line 239, as _ZN3QV420ArrayBufferPrototype15method_toStringEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue ArrayBufferPrototype::method_toString(const FunctionObject *b, const Value *thisObject, const Value *, int)
{
    ExecutionEngine *v4 = b->engine();
    const ArrayBuffer *a = thisObject->as<ArrayBuffer>();
    if (!a)
        RETURN_UNDEFINED();
    return Encode(v4->newString(QString::fromUtf8(a->asByteArray())));
}
}  // namespace QV4
//  -----------------------------------------------------------------------

//  ReturnedValue QV4::ArrayBufferPrototype::method_get_byteLength(const
//      FunctionObject *a0, const Value *thisObject, const Value *argv, int
//      argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV420ArrayBufferPrototype21method_get_byteLengthEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::ArrayBufferPrototype::method_get_byteLength(
      a0,
      thisObject,
      argv,
      argc);
}

//  ReturnedValue QV4::ArrayBufferPrototype::method_slice(const
//      FunctionObject *a0, const Value *thisObject, const Value *argv, int
//      argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV420ArrayBufferPrototype12method_sliceEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::ArrayBufferPrototype::method_slice(a0, thisObject, argv, argc);
}

//  ReturnedValue QV4::ArrayBufferPrototype::method_toString(const
//      FunctionObject *a0, const Value *thisObject, const Value *argv, int
//      argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV420ArrayBufferPrototype15method_toStringEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::ArrayBufferPrototype::method_toString(
      a0,
      thisObject,
      argv,
      argc);
}
