//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4typedarray_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4typedarray_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qv4typedarray_p.h>
#include <QtQml/private/qv4arrayiterator_p.h>
#include <QtQml/private/qv4arraybuffer_p.h>
#include <QtQml/private/qv4symbol_p.h>
#include <QtQml/private/qv4runtime_p.h>
#include <QtCore/qatomic.h>
#include <cmath>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/jsruntime/qv4typedarray.cpp, line 594, as _ZN3QV428IntrinsicTypedArrayPrototype17method_get_bufferEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue IntrinsicTypedArrayPrototype::method_get_buffer(const FunctionObject *b, const Value *thisObject, const Value *, int)
{
    ExecutionEngine *v4 = b->engine();
    const TypedArray *v = thisObject->as<TypedArray>();
    if (!v)
        return v4->throwTypeError();

    return v->d()->buffer->asReturnedValue();
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4typedarray.cpp, line 604, as _ZN3QV428IntrinsicTypedArrayPrototype21method_get_byteLengthEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue IntrinsicTypedArrayPrototype::method_get_byteLength(const FunctionObject *b, const Value *thisObject, const Value *, int)
{
    ExecutionEngine *v4 = b->engine();
    const TypedArray *v = thisObject->as<TypedArray>();
    if (!v)
        return v4->throwTypeError();

    if (v->hasDetachedArrayData())
        return Encode(0);

    return Encode(v->byteLength());
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4typedarray.cpp, line 617, as _ZN3QV428IntrinsicTypedArrayPrototype21method_get_byteOffsetEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue IntrinsicTypedArrayPrototype::method_get_byteOffset(const FunctionObject *b, const Value *thisObject, const Value *, int)
{
    ExecutionEngine *v4 = b->engine();
    const TypedArray *v = thisObject->as<TypedArray>();
    if (!v)
        return v4->throwTypeError();

    if (v->hasDetachedArrayData())
        return Encode(0);

    return Encode(v->byteOffset());
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4typedarray.cpp, line 630, as _ZN3QV428IntrinsicTypedArrayPrototype17method_get_lengthEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue IntrinsicTypedArrayPrototype::method_get_length(const FunctionObject *b, const Value *thisObject, const Value *, int)
{
    ExecutionEngine *v4 = b->engine();
    const TypedArray *v = thisObject->as<TypedArray>();
    if (!v)
        return v4->throwTypeError();

    if (v->hasDetachedArrayData())
        return Encode(0);

    return Encode(v->length());
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4typedarray.cpp, line 643, as _ZN3QV428IntrinsicTypedArrayPrototype17method_copyWithinEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue IntrinsicTypedArrayPrototype::method_copyWithin(const FunctionObject *f, const Value *thisObject, const Value *argv, int argc)
{
    Scope scope(f);
    Scoped<TypedArray> instance(scope, thisObject);
    if (!instance || instance->hasDetachedArrayData())
        return scope.engine->throwTypeError();

    if (!argc)
        return instance->asReturnedValue();

    const double len = instance->length();
    Q_ASSERT(std::isfinite(len));

    const double target = argv[0].toInteger();

    const double start = (argc > 1)
            ? argv[1].toInteger()
            : 0;

    const double end = (argc > 2 && !argv[2].isUndefined())
            ? argv[2].toInteger()
            : len;

    const double fin = end < 0
            ? std::max(len + end, 0.0)
            : std::min(end, len);

    const qsizetype from = start < 0
            ? std::max(len + start, 0.0)
            : std::min(start, len);

    const qsizetype to = target < 0
            ? std::max(len + target, 0.0)
            : std::min(target, len);

    const qsizetype count = std::min(fin - from, len - to);

    if (count <= 0)
        return instance->asReturnedValue();

    if (from != to) {
        int elementSize = instance->bytesPerElement();
        char *data = instance->arrayData() + instance->byteOffset();
        memmove(data + to * elementSize, data + from * elementSize, count * elementSize);
    }

    return instance->asReturnedValue();
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4typedarray.cpp, line 704, as _ZN3QV428IntrinsicTypedArrayPrototype12method_everyEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue IntrinsicTypedArrayPrototype::method_every(const FunctionObject *b, const Value *thisObject, const Value *argv, int argc)
{
    Scope scope(b);
    Scoped<TypedArray> v(scope, thisObject);
    if (!v || v->hasDetachedArrayData())
        return scope.engine->throwTypeError();

    uint len = v->length();

    if (!argc || !argv->isFunctionObject())
        THROW_TYPE_ERROR();
    const FunctionObject *callback = static_cast<const FunctionObject *>(argv);

    ScopedValue that(scope, argc > 1 ? argv[1] : Value::undefinedValue());
    ScopedValue r(scope);
    Value *arguments = scope.constructUndefined(3);

    const char *data = v->constArrayData();
    uint bytesPerElement = v->bytesPerElement();
    uint byteOffset = v->byteOffset();

    bool ok = true;
    for (uint k = 0; ok && k < len; ++k) {
        if (v->hasDetachedArrayData())
            return scope.engine->throwTypeError();

        arguments[0] = v->d()->type->read(data + byteOffset + k * bytesPerElement);

        arguments[1] = Value::fromDouble(k);
        arguments[2] = v;
        r = callback->call(that, arguments, 3);
        CHECK_EXCEPTION();
        ok = r->toBoolean();
    }
    return Encode(ok);
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4typedarray.cpp, line 741, as _ZN3QV428IntrinsicTypedArrayPrototype11method_fillEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue IntrinsicTypedArrayPrototype::method_fill(const FunctionObject *b, const Value *thisObject, const Value *argv, int argc)
{
    Scope scope(b);
    Scoped<TypedArray> v(scope, thisObject);
    if (!v || v->hasDetachedArrayData())
        return scope.engine->throwTypeError();

    uint len = v->length();
    double dlen = len;
    double relativeStart = argc > 1 ? argv[1].toInteger() : 0.;
    double relativeEnd = len;
    if (argc > 2 && !argv[2].isUndefined())
        relativeEnd = argv[2].toInteger();

    uint k = 0;
    uint fin = 0;

    if (relativeStart < 0) {
        k = static_cast<uint>(std::max(len+relativeStart, 0.));
    } else {
        k = static_cast<uint>(std::min(relativeStart, dlen));
    }

    if (relativeEnd < 0) {
        fin = static_cast<uint>(std::max(len + relativeEnd, 0.));
    } else {
        fin = static_cast<uint>(std::min(relativeEnd, dlen));
    }

    if (scope.hasException() || v->hasDetachedArrayData())
        return scope.engine->throwTypeError();

    char *data = v->arrayData();
    uint bytesPerElement = v->bytesPerElement();
    uint byteOffset = v->byteOffset();

    Value value;
    if (!argc)
        value.setDouble(std::numeric_limits<double>::quiet_NaN());
    else if (argv[0].isNumber())
        value = argv[0];
    else
        value.setDouble(argv[0].toNumber());

    while (k < fin) {
        v->d()->type->write(data + byteOffset + k * bytesPerElement, value);
        k++;
    }

    return v.asReturnedValue();
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4typedarray.cpp, line 859, as _ZN3QV428IntrinsicTypedArrayPrototype11method_findEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue IntrinsicTypedArrayPrototype::method_find(const FunctionObject *b, const Value *thisObject, const Value *argv, int argc)
{
    Scope scope(b);
    Scoped<TypedArray> v(scope, thisObject);
    if (!v || v->hasDetachedArrayData())
        return scope.engine->throwTypeError();

    uint len = v->length();

    if (!argc || !argv[0].isFunctionObject())
        THROW_TYPE_ERROR();
    const FunctionObject *callback = static_cast<const FunctionObject *>(argv);

    ScopedValue result(scope);
    Value *arguments = scope.constructUndefined(3);

    ScopedValue that(scope, argc > 1 ? argv[1] : Value::undefinedValue());

    for (uint k = 0; k < len; ++k) {
        if (v->hasDetachedArrayData())
            return scope.engine->throwTypeError();
        arguments[0] = v->get(k);
        CHECK_EXCEPTION();

        arguments[1] = Value::fromDouble(k);
        arguments[2] = v;
        result = callback->call(that, arguments, 3);

        CHECK_EXCEPTION();
        if (result->toBoolean())
            return arguments[0].asReturnedValue();
    }

    RETURN_UNDEFINED();
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4typedarray.cpp, line 895, as _ZN3QV428IntrinsicTypedArrayPrototype16method_findIndexEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue IntrinsicTypedArrayPrototype::method_findIndex(const FunctionObject *b, const Value *thisObject, const Value *argv, int argc)
{
    Scope scope(b);
    Scoped<TypedArray> v(scope, thisObject);
    if (!v || v->hasDetachedArrayData())
        return scope.engine->throwTypeError();

    uint len = v->length();

    if (!argc || !argv[0].isFunctionObject())
        THROW_TYPE_ERROR();
    const FunctionObject *callback = static_cast<const FunctionObject *>(argv);

    ScopedValue result(scope);
    Value *arguments = scope.constructUndefined(3);

    ScopedValue that(scope, argc > 1 ? argv[1] : Value::undefinedValue());

    for (uint k = 0; k < len; ++k) {
        if (v->hasDetachedArrayData())
            return scope.engine->throwTypeError();
        arguments[0] = v->get(k);
        CHECK_EXCEPTION();

        arguments[1] = Value::fromDouble(k);
        arguments[2] = v;
        result = callback->call(that, arguments, 3);

        CHECK_EXCEPTION();
        if (result->toBoolean())
            return Encode(k);
    }

    return Encode(-1);
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4typedarray.cpp, line 931, as _ZN3QV428IntrinsicTypedArrayPrototype14method_forEachEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue IntrinsicTypedArrayPrototype::method_forEach(const FunctionObject *b, const Value *thisObject, const Value *argv, int argc)
{
    Scope scope(b);
    Scoped<TypedArray> v(scope, thisObject);
    if (!v || v->hasDetachedArrayData())
        return scope.engine->throwTypeError();

    uint len = v->length();

    if (!argc || !argv->isFunctionObject())
        THROW_TYPE_ERROR();
    const FunctionObject *callback = static_cast<const FunctionObject *>(argv);

    ScopedValue that(scope, argc > 1 ? argv[1] : Value::undefinedValue());
    Value *arguments = scope.constructUndefined(3);

    for (uint k = 0; k < len; ++k) {
        if (v->hasDetachedArrayData())
            return scope.engine->throwTypeError();
        bool exists;
        arguments[0] = v->get(k, &exists);
        if (!exists)
            continue;

        arguments[1] = Value::fromDouble(k);
        arguments[2] = v;
        callback->call(that, arguments, 3);
    }
    RETURN_UNDEFINED();
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4typedarray.cpp, line 963, as _ZN3QV428IntrinsicTypedArrayPrototype15method_includesEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue IntrinsicTypedArrayPrototype::method_includes(const FunctionObject *b, const Value *thisObject, const Value *argv, int argc)
{
    Scope scope(b);
    Scoped<TypedArray> v(scope, thisObject);
    if (!v || v->hasDetachedArrayData())
        return scope.engine->throwTypeError();

    uint len = v->length();
    if (len == 0) {
        return Encode(false);
    }

    double n = 0;
    if (argc > 1 && !argv[1].isUndefined()) {
        n = argv[1].toInteger();
    }

    double k = 0;
    if (n >= 0) {
        k = n;
    } else {
        k = len + n;
        if (k < 0) {
            k = 0;
        }
    }

    while (k < len) {
        ScopedValue val(scope, v->get(k));
        if (val->sameValueZero(argv[0])) {
            return Encode(true);
        }
        k++;
    }

    return Encode(false);
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4typedarray.cpp, line 1001, as _ZN3QV428IntrinsicTypedArrayPrototype14method_indexOfEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue IntrinsicTypedArrayPrototype::method_indexOf(const FunctionObject *b, const Value *thisObject, const Value *argv, int argc)
{
    Scope scope(b);
    Scoped<TypedArray> v(scope, thisObject);
    if (!v || v->hasDetachedArrayData())
        return scope.engine->throwTypeError();

    uint len = v->length();
    if (!len)
        return Encode(-1);

    ScopedValue searchValue(scope, argc ? argv[0] : Value::undefinedValue());
    uint fromIndex = 0;

    if (argc >= 2) {
        double f = argv[1].toInteger();
        CHECK_EXCEPTION();
        if (f >= len)
            return Encode(-1);
        if (f < 0)
            f = qMax(len + f, 0.);
        fromIndex = (uint) f;
    }

    if (v->isStringObject()) {
        ScopedValue value(scope);
        for (uint k = fromIndex; k < len; ++k) {
            bool exists;
            value = v->get(k, &exists);
            if (exists && RuntimeHelpers::strictEqual(value, searchValue))
                return Encode(k);
        }
        return Encode(-1);
    }

    ScopedValue value(scope);

    for (uint i = fromIndex; i < len; ++i) {
        bool exists;
        value = v->get(i, &exists);
        CHECK_EXCEPTION();
        if (exists && RuntimeHelpers::strictEqual(value, searchValue))
            return Encode(i);
    }
    return Encode(-1);
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4typedarray.cpp, line 1048, as _ZN3QV428IntrinsicTypedArrayPrototype11method_joinEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue IntrinsicTypedArrayPrototype::method_join(
        const FunctionObject *functionObject, const Value *thisObject, const Value *argv, int argc)
{
    Scope scope(functionObject);
    Scoped<TypedArray> typedArray(scope, thisObject);
    if (!typedArray || typedArray->hasDetachedArrayData())
        return scope.engine->throwTypeError();

    // We cannot optimize the resolution of the argument away if length is 0.
    // It may have side effects.
    ScopedValue argument(scope, argc ? argv[0] : Value::undefinedValue());
    const QString separator = argument->isUndefined()
            ? QStringLiteral(",")
            : argument->toQString();

    const quint32 length = typedArray->length();
    if (!length)
        return Encode(scope.engine->newString());

    QString result;

    ScopedString name(scope, scope.engine->newString(QStringLiteral("0")));
    ScopedValue value(scope, typedArray->get(name));
    if (!value->isNullOrUndefined())
        result = value->toQString();

    for (quint32 i = 1; i < length; ++i) {
        result += separator;

        name = Value::fromDouble(i).toString(scope.engine);
        value = typedArray->get(name);
        CHECK_EXCEPTION();

        if (!value->isNullOrUndefined())
            result += value->toQString();
    }

    return Encode(scope.engine->newString(result));
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4typedarray.cpp, line 1101, as _ZN3QV428IntrinsicTypedArrayPrototype18method_lastIndexOfEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue IntrinsicTypedArrayPrototype::method_lastIndexOf(const FunctionObject *b, const Value *thisObject, const Value *argv, int argc)
{
    Scope scope(b);
    Scoped<TypedArray> instance(scope, thisObject);
    if (!instance || instance->hasDetachedArrayData())
        return scope.engine->throwTypeError();

    uint len = instance->length();
    if (!len)
        return Encode(-1);

    ScopedValue searchValue(scope);
    uint fromIndex = len;

    if (argc >= 1)
        searchValue = argv[0];
    else
        searchValue = Value::undefinedValue();

    if (argc >= 2) {
        double f = argv[1].toInteger();
        CHECK_EXCEPTION();
        if (f > 0)
            f = qMin(f, (double)(len - 1));
        else if (f < 0) {
            f = len + f;
            if (f < 0)
                return Encode(-1);
        }
        fromIndex = (uint) f + 1;
    }

    ScopedValue value(scope);
    for (uint k = fromIndex; k > 0;) {
        --k;
        bool exists;
        value = instance->get(k, &exists);
        if (exists && RuntimeHelpers::strictEqual(value, searchValue))
            return Encode(k);
    }
    return Encode(-1);
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4typedarray.cpp, line 1180, as _ZN3QV428IntrinsicTypedArrayPrototype13method_reduceEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue IntrinsicTypedArrayPrototype::method_reduce(const FunctionObject *b, const Value *thisObject, const Value *argv, int argc)
{
    Scope scope(b);
    Scoped<TypedArray> instance(scope, thisObject);
    if (!instance || instance->hasDetachedArrayData())
        return scope.engine->throwTypeError();

    uint len = instance->length();

    if (!argc || !argv->isFunctionObject())
        THROW_TYPE_ERROR();
    const FunctionObject *callback = static_cast<const FunctionObject *>(argv);

    uint k = 0;
    ScopedValue acc(scope);
    ScopedValue v(scope);

    if (argc > 1) {
        acc = argv[1];
    } else {
        bool kPresent = false;
        while (k < len && !kPresent) {
            v = instance->get(k, &kPresent);
            if (kPresent)
                acc = v;
            ++k;
        }
        if (!kPresent)
            THROW_TYPE_ERROR();
    }

    Value *arguments = scope.constructUndefined(4);

    while (k < len) {
        if (instance->hasDetachedArrayData())
            return scope.engine->throwTypeError();
        bool kPresent;
        v = instance->get(k, &kPresent);
        if (kPresent) {
            arguments[0] = acc;
            arguments[1] = v;
            arguments[2] = Value::fromDouble(k);
            arguments[3] = instance;
            acc = callback->call(nullptr, arguments, 4);
            CHECK_EXCEPTION();
        }
        ++k;
    }
    return acc->asReturnedValue();
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4typedarray.cpp, line 1231, as _ZN3QV428IntrinsicTypedArrayPrototype18method_reduceRightEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue IntrinsicTypedArrayPrototype::method_reduceRight(const FunctionObject *b, const Value *thisObject, const Value *argv, int argc)
{
    Scope scope(b);
    Scoped<TypedArray> instance(scope, thisObject);
    if (!instance || instance->hasDetachedArrayData())
        return scope.engine->throwTypeError();

    uint len = instance->length();

    if (!argc || !argv->isFunctionObject())
        THROW_TYPE_ERROR();
    const FunctionObject *callback = static_cast<const FunctionObject *>(argv);

    if (len == 0) {
        if (argc == 1)
            THROW_TYPE_ERROR();
        return argv[1].asReturnedValue();
    }

    uint k = len;
    ScopedValue acc(scope);
    ScopedValue v(scope);
    if (argc > 1) {
        acc = argv[1];
    } else {
        bool kPresent = false;
        while (k > 0 && !kPresent) {
            v = instance->get(k - 1, &kPresent);
            if (kPresent)
                acc = v;
            --k;
        }
        if (!kPresent)
            THROW_TYPE_ERROR();
    }

    Value *arguments = scope.constructUndefined(4);

    while (k > 0) {
        if (instance->hasDetachedArrayData())
            return scope.engine->throwTypeError();
        bool kPresent;
        v = instance->get(k - 1, &kPresent);
        if (kPresent) {
            arguments[0] = acc;
            arguments[1] = v;
            arguments[2] = Value::fromDouble(k - 1);
            arguments[3] = instance;
            acc = callback->call(nullptr, arguments, 4);
            CHECK_EXCEPTION();
        }
        --k;
    }
    return acc->asReturnedValue();
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4typedarray.cpp, line 1287, as _ZN3QV428IntrinsicTypedArrayPrototype14method_reverseEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue IntrinsicTypedArrayPrototype::method_reverse(const FunctionObject *b, const Value *thisObject, const Value *, int)
{
    Scope scope(b);
    Scoped<TypedArray> instance(scope, thisObject);
    if (!instance || instance->hasDetachedArrayData())
        return scope.engine->throwTypeError();

    uint length = instance->length();

    int lo = 0, hi = length - 1;

    ScopedValue lval(scope);
    ScopedValue hval(scope);
    for (; lo < hi; ++lo, --hi) {
        bool loExists, hiExists;
        lval = instance->get(lo, &loExists);
        hval = instance->get(hi, &hiExists);
        Q_ASSERT(hiExists && loExists);
        bool ok;
        ok = instance->put(lo, hval);
        Q_ASSERT(ok);
        ok = instance->put(hi, lval);
        Q_ASSERT(ok);
    }
    return instance->asReturnedValue();
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4typedarray.cpp, line 1314, as _ZN3QV428IntrinsicTypedArrayPrototype11method_someEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue IntrinsicTypedArrayPrototype::method_some(const FunctionObject *b, const Value *thisObject, const Value *argv, int argc)
{
    Scope scope(b);
    Scoped<TypedArray> instance(scope, thisObject);
    if (!instance || instance->hasDetachedArrayData())
        return scope.engine->throwTypeError();

    uint len = instance->length();

    if (!argc || !argv->isFunctionObject())
        THROW_TYPE_ERROR();
    const FunctionObject *callback = static_cast<const FunctionObject *>(argv);

    ScopedValue that(scope, argc > 1 ? argv[1] : Value::undefinedValue());
    ScopedValue result(scope);
    Value *arguments = scope.constructUndefined(3);

    for (uint k = 0; k < len; ++k) {
        if (instance->hasDetachedArrayData())
            return scope.engine->throwTypeError();
        bool exists;
        arguments[0] = instance->get(k, &exists);
        if (!exists)
            continue;

        arguments[1] = Value::fromDouble(k);
        arguments[2] = instance;
        result = callback->call(that, arguments, 3);
        CHECK_EXCEPTION();
        if (result->toBoolean())
            return Encode(true);
    }
    return Encode(false);
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4typedarray.cpp, line 1362, as _ZN3QV428IntrinsicTypedArrayPrototype10method_setEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue IntrinsicTypedArrayPrototype::method_set(const FunctionObject *b, const Value *thisObject, const Value *argv, int argc)
{
    Scope scope(b);
    Scoped<TypedArray> a(scope, *thisObject);
    if (!a)
        return scope.engine->throwTypeError();
    Scoped<ArrayBuffer> buffer(scope, a->d()->buffer);

    double doffset = argc >= 2 ? argv[1].toInteger() : 0;
    if (scope.hasException())
        RETURN_UNDEFINED();
    if (!buffer || buffer->hasDetachedArrayData())
        return scope.engine->throwTypeError();

    if (doffset < 0 || doffset >= UINT_MAX)
        RETURN_RESULT(scope.engine->throwRangeError(QStringLiteral("TypedArray.set: out of range")));
    uint offset = (uint)doffset;
    uint elementSize = a->bytesPerElement();

    Scoped<TypedArray> srcTypedArray(scope, argv[0]);
    if (!srcTypedArray) {
        // src is a regular object
        ScopedObject o(scope, argv[0].toObject(scope.engine));
        if (scope.hasException() || !o)
            return scope.engine->throwTypeError();

        double len = ScopedValue(scope, o->get(scope.engine->id_length()))->toNumber();
        uint l = (uint)len;
        if (scope.hasException() || l != len)
            return scope.engine->throwTypeError();

        const uint aLength = a->length();
        if (offset > aLength || l > aLength - offset)
            RETURN_RESULT(scope.engine->throwRangeError(QStringLiteral("TypedArray.set: out of range")));

        uint idx = 0;
        if (buffer->hasDetachedArrayData())
            return scope.engine->throwTypeError();
        char *b = buffer->arrayData() + a->byteOffset() + offset*elementSize;
        ScopedValue val(scope);
        while (idx < l) {
            val = o->get(idx);
            if (scope.hasException())
                return Encode::undefined();
            val = val->convertedToNumber();
            if (scope.hasException() || buffer->hasDetachedArrayData())
                return scope.engine->throwTypeError();
            a->d()->type->write(b, val);
            if (scope.hasException())
                RETURN_UNDEFINED();
            ++idx;
            b += elementSize;
        }
        RETURN_UNDEFINED();
    }

    // src is a typed array
    Scoped<ArrayBuffer> srcBuffer(scope, srcTypedArray->d()->buffer);
    if (!srcBuffer || srcBuffer->hasDetachedArrayData())
        return scope.engine->throwTypeError();

    uint l = srcTypedArray->length();

    const uint aLength = a->length();
    if (offset > aLength || l > aLength - offset)
        RETURN_RESULT(scope.engine->throwRangeError(QStringLiteral("TypedArray.set: out of range")));

    char *dest = buffer->arrayData() + a->byteOffset() + offset*elementSize;
    const char *src = srcBuffer->d()->constArrayData() + srcTypedArray->byteOffset();
    if (srcTypedArray->d()->type == a->d()->type) {
        // same type of typed arrays, use memmove (as srcbuffer and buffer could be the same)
        memmove(dest, src, srcTypedArray->byteLength());
        RETURN_UNDEFINED();
    }

    char *srcCopy = nullptr;
    if (buffer->d() == srcBuffer->d()) {
        // same buffer, need to take a temporary copy, to not run into problems
        srcCopy = new char[srcTypedArray->byteLength()];
        memcpy(srcCopy, src, srcTypedArray->byteLength());
        src = srcCopy;
    }

    // typed arrays of different kind, need to manually loop
    uint srcElementSize = srcTypedArray->bytesPerElement();
    TypedArrayOperations::Read read = srcTypedArray->d()->type->read;
    TypedArrayOperations::Write write = a->d()->type->write;
    for (uint i = 0; i < l; ++i) {
        Value val;
        val.setRawValue(read(src + i*srcElementSize));
        write(dest + i*elementSize, val);
    }

    if (srcCopy)
        delete [] srcCopy;

    RETURN_UNDEFINED();
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4typedarray.cpp, line 1508, as _ZN3QV428IntrinsicTypedArrayPrototype15method_subarrayEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue IntrinsicTypedArrayPrototype::method_subarray(const FunctionObject *builtin, const Value *thisObject, const Value *argv, int argc)
{
    Scope scope(builtin);
    Scoped<TypedArray> a(scope, *thisObject);

    if (!a)
        return scope.engine->throwTypeError();

    Scoped<ArrayBuffer> buffer(scope, a->d()->buffer);
    Q_ASSERT(buffer);

    int len = a->length();
    double b = argc > 0 ? argv[0].toInteger() : 0;
    if (b < 0)
        b = len + b;
    uint begin = (uint)qBound(0., b, (double)len);

    double e = argc < 2 || argv[1].isUndefined() ? len : argv[1].toInteger();
    if (e < 0)
        e = len + e;
    uint end = (uint)qBound(0., e, (double)len);
    if (end < begin)
        end = begin;

    if (scope.hasException())
        RETURN_UNDEFINED();

    int newLen = end - begin;

    ScopedFunctionObject constructor(scope, a->speciesConstructor(scope, scope.engine->typedArrayCtors + a->d()->arrayType));
    if (!constructor)
        return scope.engine->throwTypeError();

    Value *arguments = scope.constructUndefined(3);
    arguments[0] = buffer;
    arguments[1] = Encode(a->byteOffset() + begin * a->bytesPerElement());
    arguments[2] = Encode(newLen);
    a = constructor->callAsConstructor(arguments, 3);
    if (!a || a->hasDetachedArrayData())
        return scope.engine->throwTypeError();
    return a->asReturnedValue();
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4typedarray.cpp, line 1551, as _ZN3QV428IntrinsicTypedArrayPrototype21method_toLocaleStringEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue IntrinsicTypedArrayPrototype::method_toLocaleString(const FunctionObject *b, const Value *thisObject, const Value *, int)
{
    Scope scope(b);
    Scoped<TypedArray> instance(scope, thisObject);
    if (!instance || instance->hasDetachedArrayData())
        return scope.engine->throwTypeError();

    uint len = instance->length();
    const QString separator = QStringLiteral(",");

    QString R;

    ScopedValue v(scope);
    ScopedString s(scope);

    ScopedPropertyKey tolocaleString(scope, scope.engine->id_toLocaleString()->toPropertyKey());
    Q_ASSERT(!scope.engine->hasException);

    for (uint k = 0; k < len; ++k) {
        if (instance->hasDetachedArrayData())
            return scope.engine->throwTypeError();
        if (k)
            R += separator;

        v = instance->get(k);
        Q_ASSERT(!v->isNullOrUndefined()); // typed array cannot hold null or undefined

        ScopedObject valueAsObject(scope, v->toObject(scope.engine));
        Q_ASSERT(valueAsObject); // only null or undefined cannot be converted to object

        ScopedFunctionObject function(scope, valueAsObject->get(tolocaleString));
        if (!function)
            return scope.engine->throwTypeError();

        v = function->call(valueAsObject, nullptr, 0);
        if (scope.hasException())
            return Encode::undefined();

        s = v->toString(scope.engine);
        if (scope.hasException())
            return Encode::undefined();

        R += s->toQString();
    }
    return scope.engine->newString(R)->asReturnedValue();
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4typedarray.cpp, line 1598, as _ZN3QV428IntrinsicTypedArrayPrototype22method_get_toStringTagEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue IntrinsicTypedArrayPrototype::method_get_toStringTag(const FunctionObject *, const Value *thisObject, const Value *, int)
{
    const TypedArray *a = thisObject->as<TypedArray>();
    if (!a)
        return Encode::undefined();

    return a->engine()->newString(QString::fromLatin1(a->d()->type->name))->asReturnedValue();
}
}  // namespace QV4
//  -----------------------------------------------------------------------

//  void QV4::IntrinsicTypedArrayPrototype::__dataTest()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV428IntrinsicTypedArrayPrototype10__dataTestEv(
    QV4::IntrinsicTypedArrayPrototype *self) {
  self->__dataTest();
}

//  QV4::Heap::IntrinsicTypedArrayPrototype
//      *QV4::IntrinsicTypedArrayPrototype::d_unchecked() const
extern "C" Q_DECL_EXPORT
QV4::Heap::IntrinsicTypedArrayPrototype *ritual_ZNK3QV428IntrinsicTypedArrayPrototype11d_uncheckedEv(
    const QV4::IntrinsicTypedArrayPrototype *self) {
  return self->d_unchecked();
}

//  QV4::Heap::IntrinsicTypedArrayPrototype
//      *QV4::IntrinsicTypedArrayPrototype::d() const
extern "C" Q_DECL_EXPORT
QV4::Heap::IntrinsicTypedArrayPrototype *ritual_ZNK3QV428IntrinsicTypedArrayPrototype1dEv(
    const QV4::IntrinsicTypedArrayPrototype *self) {
  return self->d();
}

//  QV4::Object
//      *QV4::IntrinsicTypedArrayPrototype::defaultPrototype(QV4::ExecutionEn
//      gine *e)
extern "C" Q_DECL_EXPORT
QV4::Object *ritual_ZN3QV428IntrinsicTypedArrayPrototype16defaultPrototypeEPNS_15ExecutionEngineE(
    QV4::ExecutionEngine *e) {
  return QV4::IntrinsicTypedArrayPrototype::defaultPrototype(e);
}

//  ReturnedValue QV4::IntrinsicTypedArrayPrototype::method_get_buffer(const
//      FunctionObject *a0, const Value *thisObject, const Value *argv, int
//      argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV428IntrinsicTypedArrayPrototype17method_get_bufferEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::IntrinsicTypedArrayPrototype::method_get_buffer(
      a0,
      thisObject,
      argv,
      argc);
}

//  ReturnedValue
//      QV4::IntrinsicTypedArrayPrototype::method_get_byteLength(const
//      FunctionObject *a0, const Value *thisObject, const Value *argv, int
//      argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV428IntrinsicTypedArrayPrototype21method_get_byteLengthEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::IntrinsicTypedArrayPrototype::method_get_byteLength(
      a0,
      thisObject,
      argv,
      argc);
}

//  ReturnedValue
//      QV4::IntrinsicTypedArrayPrototype::method_get_byteOffset(const
//      FunctionObject *a0, const Value *thisObject, const Value *argv, int
//      argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV428IntrinsicTypedArrayPrototype21method_get_byteOffsetEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::IntrinsicTypedArrayPrototype::method_get_byteOffset(
      a0,
      thisObject,
      argv,
      argc);
}

//  ReturnedValue QV4::IntrinsicTypedArrayPrototype::method_get_length(const
//      FunctionObject *a0, const Value *thisObject, const Value *argv, int
//      argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV428IntrinsicTypedArrayPrototype17method_get_lengthEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::IntrinsicTypedArrayPrototype::method_get_length(
      a0,
      thisObject,
      argv,
      argc);
}

//  ReturnedValue QV4::IntrinsicTypedArrayPrototype::method_copyWithin(const
//      FunctionObject *a0, const Value *thisObject, const Value *argv, int
//      argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV428IntrinsicTypedArrayPrototype17method_copyWithinEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::IntrinsicTypedArrayPrototype::method_copyWithin(
      a0,
      thisObject,
      argv,
      argc);
}

//  ReturnedValue QV4::IntrinsicTypedArrayPrototype::method_every(const
//      FunctionObject *a0, const Value *thisObject, const Value *argv, int
//      argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV428IntrinsicTypedArrayPrototype12method_everyEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::IntrinsicTypedArrayPrototype::method_every(
      a0,
      thisObject,
      argv,
      argc);
}

//  ReturnedValue QV4::IntrinsicTypedArrayPrototype::method_fill(const
//      FunctionObject *a0, const Value *thisObject, const Value *argv, int
//      argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV428IntrinsicTypedArrayPrototype11method_fillEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::IntrinsicTypedArrayPrototype::method_fill(
      a0,
      thisObject,
      argv,
      argc);
}

//  ReturnedValue QV4::IntrinsicTypedArrayPrototype::method_find(const
//      FunctionObject *a0, const Value *thisObject, const Value *argv, int
//      argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV428IntrinsicTypedArrayPrototype11method_findEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::IntrinsicTypedArrayPrototype::method_find(
      a0,
      thisObject,
      argv,
      argc);
}

//  ReturnedValue QV4::IntrinsicTypedArrayPrototype::method_findIndex(const
//      FunctionObject *a0, const Value *thisObject, const Value *argv, int
//      argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV428IntrinsicTypedArrayPrototype16method_findIndexEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::IntrinsicTypedArrayPrototype::method_findIndex(
      a0,
      thisObject,
      argv,
      argc);
}

//  ReturnedValue QV4::IntrinsicTypedArrayPrototype::method_forEach(const
//      FunctionObject *a0, const Value *thisObject, const Value *argv, int
//      argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV428IntrinsicTypedArrayPrototype14method_forEachEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::IntrinsicTypedArrayPrototype::method_forEach(
      a0,
      thisObject,
      argv,
      argc);
}

//  ReturnedValue QV4::IntrinsicTypedArrayPrototype::method_includes(const
//      FunctionObject *a0, const Value *thisObject, const Value *argv, int
//      argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV428IntrinsicTypedArrayPrototype15method_includesEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::IntrinsicTypedArrayPrototype::method_includes(
      a0,
      thisObject,
      argv,
      argc);
}

//  ReturnedValue QV4::IntrinsicTypedArrayPrototype::method_indexOf(const
//      FunctionObject *a0, const Value *thisObject, const Value *argv, int
//      argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV428IntrinsicTypedArrayPrototype14method_indexOfEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::IntrinsicTypedArrayPrototype::method_indexOf(
      a0,
      thisObject,
      argv,
      argc);
}

//  ReturnedValue QV4::IntrinsicTypedArrayPrototype::method_join(const
//      FunctionObject *a0, const Value *thisObject, const Value *argv, int
//      argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV428IntrinsicTypedArrayPrototype11method_joinEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::IntrinsicTypedArrayPrototype::method_join(
      a0,
      thisObject,
      argv,
      argc);
}

//  ReturnedValue QV4::IntrinsicTypedArrayPrototype::method_lastIndexOf(const
//      FunctionObject *a0, const Value *thisObject, const Value *argv, int
//      argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV428IntrinsicTypedArrayPrototype18method_lastIndexOfEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::IntrinsicTypedArrayPrototype::method_lastIndexOf(
      a0,
      thisObject,
      argv,
      argc);
}

//  ReturnedValue QV4::IntrinsicTypedArrayPrototype::method_reduce(const
//      FunctionObject *a0, const Value *thisObject, const Value *argv, int
//      argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV428IntrinsicTypedArrayPrototype13method_reduceEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::IntrinsicTypedArrayPrototype::method_reduce(
      a0,
      thisObject,
      argv,
      argc);
}

//  ReturnedValue QV4::IntrinsicTypedArrayPrototype::method_reduceRight(const
//      FunctionObject *a0, const Value *thisObject, const Value *argv, int
//      argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV428IntrinsicTypedArrayPrototype18method_reduceRightEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::IntrinsicTypedArrayPrototype::method_reduceRight(
      a0,
      thisObject,
      argv,
      argc);
}

//  ReturnedValue QV4::IntrinsicTypedArrayPrototype::method_reverse(const
//      FunctionObject *a0, const Value *thisObject, const Value *argv, int
//      argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV428IntrinsicTypedArrayPrototype14method_reverseEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::IntrinsicTypedArrayPrototype::method_reverse(
      a0,
      thisObject,
      argv,
      argc);
}

//  ReturnedValue QV4::IntrinsicTypedArrayPrototype::method_some(const
//      FunctionObject *a0, const Value *thisObject, const Value *argv, int
//      argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV428IntrinsicTypedArrayPrototype11method_someEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::IntrinsicTypedArrayPrototype::method_some(
      a0,
      thisObject,
      argv,
      argc);
}

//  ReturnedValue QV4::IntrinsicTypedArrayPrototype::method_set(const
//      FunctionObject *a0, const Value *thisObject, const Value *argv, int
//      argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV428IntrinsicTypedArrayPrototype10method_setEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::IntrinsicTypedArrayPrototype::method_set(
      a0,
      thisObject,
      argv,
      argc);
}

//  ReturnedValue QV4::IntrinsicTypedArrayPrototype::method_subarray(const
//      FunctionObject *a0, const Value *thisObject, const Value *argv, int
//      argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV428IntrinsicTypedArrayPrototype15method_subarrayEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::IntrinsicTypedArrayPrototype::method_subarray(
      a0,
      thisObject,
      argv,
      argc);
}

//  ReturnedValue
//      QV4::IntrinsicTypedArrayPrototype::method_toLocaleString(const
//      FunctionObject *a0, const Value *thisObject, const Value *argv, int
//      argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV428IntrinsicTypedArrayPrototype21method_toLocaleStringEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::IntrinsicTypedArrayPrototype::method_toLocaleString(
      a0,
      thisObject,
      argv,
      argc);
}

//  ReturnedValue
//      QV4::IntrinsicTypedArrayPrototype::method_get_toStringTag(const
//      FunctionObject *a0, const Value *thisObject, const Value *argv, int
//      argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV428IntrinsicTypedArrayPrototype22method_get_toStringTagEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::IntrinsicTypedArrayPrototype::method_get_toStringTag(
      a0,
      thisObject,
      argv,
      argc);
}
