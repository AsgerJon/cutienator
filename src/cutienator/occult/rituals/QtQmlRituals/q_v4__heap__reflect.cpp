//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4reflect_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4reflect_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qv4reflect_p.h>
#include <QtQml/private/qv4runtimeapi_p.h>
#include <QtQml/private/qv4objectproto_p.h>
#include <QtQml/private/qv4propertykey_p.h>
#include <QtQml/private/qv4objectiterator_p.h>
#include <QtQml/private/qv4propertykey_p.h>
#include <QtCore/qstring.h>
#include <QtQml/private/qv4string_p.h>
#include <QtQml/private/qv4engine_p.h>
#include <QtQml/private/qv4scopedvalue_p.h>
#include <QtQml/private/qv4mm_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::Literals::StringLiterals;

//  from ../qtdeclarative/src/qml/jsruntime/qv4reflect.cpp, line 123, as _ZN3QV47Reflect10method_getEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue Reflect::method_get(const FunctionObject *f, const Value *, const Value *argv, int argc)
{
    Scope scope(f);
    if (!argc || !argv[0].isObject())
        return scope.engine->throwTypeError();

    ScopedObject o(scope, static_cast<const Object *>(argv));
    Value undef = Value::undefinedValue();
    const Value *index = argc > 1 ? &argv[1] : &undef;
    ScopedPropertyKey name(scope, index->toPropertyKey(scope.engine));
    if (scope.hasException())
        return Encode::undefined();
    ScopedValue receiver(scope, argc > 2 ? argv[2] : *o);

    return Encode(o->get(name, receiver));
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4reflect.cpp, line 158, as _ZN3QV47Reflect10method_hasEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue Reflect::method_has(const FunctionObject *f, const Value *, const Value *argv, int argc)
{
    Scope scope(f);
    if (!argc || !argv[0].isObject())
        return scope.engine->throwTypeError();

    ScopedObject o(scope, static_cast<const Object *>(argv));
    Value undef = Value::undefinedValue();
    const Value *index = argc > 1 ? &argv[1] : &undef;

    ScopedPropertyKey name(scope, index->toPropertyKey(scope.engine));
    if (scope.hasException())
        return false;

    return Encode(o->hasProperty(name));
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4reflect.cpp, line 225, as _ZN3QV47Reflect10method_setEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue Reflect::method_set(const FunctionObject *f, const Value *, const Value *argv, int argc)
{
    Scope scope(f);
    if (!argc || !argv[0].isObject())
        return scope.engine->throwTypeError();

    ScopedObject o(scope, static_cast<const Object *>(argv));
    Value undef = Value::undefinedValue();
    const Value *index = argc > 1 ? &argv[1] : &undef;
    const Value &val = argc > 2 ? argv[2] : undef;
    ScopedValue receiver(scope, argc >3 ? argv[3] : argv[0]);

    ScopedPropertyKey propertyKey(scope, index->toPropertyKey(scope.engine));
    if (scope.hasException())
        return false;
    bool result = o->put(propertyKey, val, receiver);
    return Encode(result);
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4reflect.cpp, line 185, as _ZN3QV47Reflect14method_ownKeysEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue Reflect::method_ownKeys(const FunctionObject *f, const Value *, const Value *argv, int argc)
{
    if (!argc || !argv[0].isObject())
        return f->engine()->throwTypeError();

    Scope scope(f);
    if (!argc)
        return scope.engine->throwTypeError();

    ScopedObject O(scope, argv[0].toObject(scope.engine));
    if (!O)
        return Encode::undefined();

    ScopedArrayObject keys(scope, scope.engine->newArrayObject());

    ObjectIterator it(scope, O, ObjectIterator::WithSymbols);
    ScopedPropertyKey key(scope);
    ScopedValue v(scope);
    while (1) {
        key = it.next();
        if (!key->isValid())
            break;
        v = key->toStringOrSymbol(scope.engine);
        keys->push_back(v);
    }

    return keys->asReturnedValue();

}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4reflect.cpp, line 175, as _ZN3QV47Reflect19method_isExtensibleEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue Reflect::method_isExtensible(const FunctionObject *f, const Value *, const Value *argv, int argc)
{
    if (!argc || !argv[0].isObject())
        return f->engine()->throwTypeError();

    const Object *o = static_cast<const Object *>(argv);
    return Encode(o->isExtensible());
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4reflect.cpp, line 90, as _ZN3QV47Reflect21method_definePropertyEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue Reflect::method_defineProperty(const FunctionObject *f, const Value *, const Value *argv, int argc)
{
    Scope scope(f);
    if (!argc || !argv[0].isObject())
        return scope.engine->throwTypeError();

    ScopedObject O(scope, argv[0]);
    ScopedPropertyKey name(scope, (argc > 1 ? argv[1] : Value::undefinedValue()).toPropertyKey(scope.engine));
    if (scope.hasException())
        return QV4::Encode::undefined();

    ScopedValue attributes(scope, argc > 2 ? argv[2] : Value::undefinedValue());
    ScopedProperty pd(scope);
    PropertyAttributes attrs;
    ObjectPrototype::toPropertyDescriptor(scope.engine, attributes, pd, &attrs);
    if (scope.hasException())
        return QV4::Encode::undefined();

    bool result = O->defineOwnProperty(name, pd, attrs);

    return Encode(result);
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4reflect.cpp, line 113, as _ZN3QV47Reflect21method_deletePropertyEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue Reflect::method_deleteProperty(const FunctionObject *f, const Value *, const Value *argv, int argc)
{
    ExecutionEngine *e = f->engine();
    if (!argc || !argv[0].isObject())
        return e->throwTypeError();

    bool result =  Runtime::DeleteProperty_NoThrow::call(e, argv[0], argc > 1 ? argv[1] : Value::undefinedValue());
    return Encode(result);
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4reflect.cpp, line 148, as _ZN3QV47Reflect21method_getPrototypeOfEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue Reflect::method_getPrototypeOf(const FunctionObject *f, const Value *, const Value *argv, int argc)
{
    if (!argc || !argv[0].isObject())
        return f->engine()->throwTypeError();

    const Object *o = static_cast<const Object *>(argv);
    Heap::Object *p = o->getPrototypeOf();
    return (p ? p->asReturnedValue() : Encode::null());
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4reflect.cpp, line 244, as _ZN3QV47Reflect21method_setPrototypeOfEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue Reflect::method_setPrototypeOf(const FunctionObject *f, const Value *, const Value *argv, int argc)
{
    if (argc < 2 || !argv[0].isObject() || (!argv[1].isNull() && !argv[1].isObject()))
        return f->engine()->throwTypeError();

    Scope scope(f);
    ScopedObject o(scope, static_cast<const Object *>(argv));
    const Object *proto = argv[1].isNull() ? nullptr : static_cast<const Object *>(argv + 1);
    return Encode(o->setPrototypeOf(proto));
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4reflect.cpp, line 215, as _ZN3QV47Reflect24method_preventExtensionsEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue Reflect::method_preventExtensions(const FunctionObject *f, const Value *, const Value *argv, int argc)
{
    Scope scope(f);
    if (!argc || !argv[0].isObject())
        return scope.engine->throwTypeError();

    ScopedObject o(scope, static_cast<const Object *>(argv));
    return Encode(o->preventExtensions());
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4reflect.cpp, line 140, as _ZN3QV47Reflect31method_getOwnPropertyDescriptorEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue Reflect::method_getOwnPropertyDescriptor(const FunctionObject *f, const Value *thisObject, const Value *argv, int argc)
{
    if (!argc || !argv[0].isObject())
        return f->engine()->throwTypeError();

    return ObjectPrototype::method_getOwnPropertyDescriptor(f, thisObject, argv, argc);
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4propertykey.cpp, line 15, as _ZN3QV411PropertyKey16toStringOrSymbolEPNS_15ExecutionEngineE
inline QV4::Heap::StringOrSymbol *QV4::PropertyKey::toStringOrSymbol(QV4::ExecutionEngine *e)
{
    if (isArrayIndex())
        return Value::fromUInt32(asArrayIndex()).toString(e);
    return asStringOrSymbol();
}
//  -----------------------------------------------------------------------
