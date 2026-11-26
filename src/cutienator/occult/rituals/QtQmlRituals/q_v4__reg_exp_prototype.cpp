//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4regexpobject_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4regexpobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qv4regexpobject_p.h>
#include <QtQml/private/qv4mm_p.h>
#include <QtQml/private/qv4scopedvalue_p.h>
#include <QtQml/private/qv4jscall_p.h>
#include <QtQml/private/qv4symbol_p.h>
#include <QtCore/private/qlocale_tools_p.h>
#include <QtCore/QDebug>
#if QT_CONFIG(regularexpression)
#include <QtCore/qregularexpression.h>
#endif
#include <cassert>
#include <typeinfo>
#include <iostream>
#include <QtQml/private/qv4alloca_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/jsruntime/qv4regexpobject.cpp, line 519, as local:qv4regexpobject.cpp:advanceStringIndex
static int advanceStringIndex(int index, const QString &str, bool unicode)
{
    if (unicode) {
        if (index < str.size() - 1 &&
            str.at(index).isHighSurrogate() &&
            str.at(index + 1).isLowSurrogate())
            ++index;
    }
    ++index;
    return index;
}

//  from ../qtdeclarative/src/qml/jsruntime/qv4regexpobject.cpp, line 439, as _ZN3QV415RegExpPrototype11method_execEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue RegExpPrototype::method_exec(const FunctionObject *b, const Value *thisObject, const Value *argv, int argc)
{
    Scope scope(b);
    Scoped<RegExpObject> r(scope, thisObject->as<RegExpObject>());
    if (!r)
        return scope.engine->throwTypeError();

    ScopedValue arg(scope, argc ? argv[0] : Value::undefinedValue());
    ScopedString str(scope, arg->toString(scope.engine));
    if (scope.hasException())
        RETURN_UNDEFINED();

    return  r->builtinExec(scope.engine, str);
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4regexpobject.cpp, line 454, as _ZN3QV415RegExpPrototype16method_get_flagsEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue RegExpPrototype::method_get_flags(const FunctionObject *f, const Value *thisObject, const Value *, int)
{
    Scope scope(f);
    ScopedObject o(scope, thisObject);
    if (!o)
        return scope.engine->throwTypeError();

    QString result;
    ScopedValue v(scope);
    v = o->get(scope.engine->id_global());
    if (scope.hasException())
        return Encode::undefined();
    if (v->toBoolean())
        result += QLatin1Char('g');
    v = o->get(scope.engine->id_ignoreCase());
    if (scope.hasException())
        return Encode::undefined();
    if (v->toBoolean())
        result += QLatin1Char('i');
    v = o->get(scope.engine->id_multiline());
    if (scope.hasException())
        return Encode::undefined();
    if (v->toBoolean())
        result += QLatin1Char('m');
    v = o->get(scope.engine->id_unicode());
    if (scope.hasException())
        return Encode::undefined();
    if (v->toBoolean())
        result += QLatin1Char('u');
    v = o->get(scope.engine->id_sticky());
    if (scope.hasException())
        return Encode::undefined();
    if (v->toBoolean())
        result += QLatin1Char('y');
    return scope.engine->newString(result)->asReturnedValue();
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4regexpobject.cpp, line 704, as _ZN3QV415RegExpPrototype13method_searchEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue RegExpPrototype::method_search(const FunctionObject *f, const Value *thisObject, const Value *argv, int argc)
{
    Scope scope(f);
    ScopedObject rx(scope, thisObject);
    if (!rx)
        return scope.engine->throwTypeError();

    ScopedString s(scope, (argc ? argv[0] : Value::undefinedValue()).toString(scope.engine));
    if (scope.hasException())
        return Encode::undefined();

    ScopedValue previousLastIndex(scope, rx->get(scope.engine->id_lastIndex()));
    if (previousLastIndex->toNumber() != 0) {
        if (!rx->put(scope.engine->id_lastIndex(), Value::fromInt32(0)))
            return scope.engine->throwTypeError();
    }

    ScopedValue result(scope, exec(scope.engine, rx, s));
    if (scope.hasException())
        return Encode::undefined();

    ScopedValue currentLastIndex(scope, rx->get(scope.engine->id_lastIndex()));
    if (!currentLastIndex->sameValue(previousLastIndex)) {
        if (!rx->put(scope.engine->id_lastIndex(), previousLastIndex))
            return scope.engine->throwTypeError();
    }

    if (result->isNull())
        return Encode(-1);
    ScopedObject o(scope, result);
    Q_ASSERT(o);
    return o->get(scope.engine->id_index());
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4regexpobject.cpp, line 739, as _ZN3QV415RegExpPrototype17method_get_sourceEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue RegExpPrototype::method_get_source(const FunctionObject *f, const Value *thisObject, const Value *, int)
{
    Scope scope(f);
    Scoped<RegExpObject> re(scope, thisObject);
    if (!re) {
        if (thisObject->sameValue(*scope.engine->regExpPrototype()))
            return scope.engine->newString(QStringLiteral("(?:)"))->asReturnedValue();
        return scope.engine->throwTypeError();
    }

    return scope.engine->newString(re->toString())->asReturnedValue();
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4regexpobject.cpp, line 862, as _ZN3QV415RegExpPrototype11method_testEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue RegExpPrototype::method_test(const FunctionObject *b, const Value *thisObject, const Value *argv, int argc)
{
    Value res = Value::fromReturnedValue(method_exec(b, thisObject, argv, argc));
    return Encode(!res.isNull());
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4regexpobject.cpp, line 868, as _ZN3QV415RegExpPrototype15method_toStringEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue RegExpPrototype::method_toString(const FunctionObject *b, const Value *thisObject, const Value *, int)
{
    Scope scope(b);
    const Object *r = thisObject->as<Object>();
    if (!r)
        return scope.engine->throwTypeError();

    ScopedValue v(scope);
    v = r->get(scope.engine->id_source());
    ScopedString source(scope, v->toString(scope.engine));
    if (scope.hasException())
        return Encode::undefined();
    v = r->get(scope.engine->id_flags());
    ScopedString flags(scope, v->toString(scope.engine));
    if (scope.hasException())
        return Encode::undefined();

    QString result = QLatin1Char('/') + source->toQString() + QLatin1Char('/') + flags->toQString();
    return Encode(scope.engine->newString(result));
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4regexpobject.cpp, line 903, as _ZN3QV415RegExpPrototype14method_compileEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue RegExpPrototype::method_compile(const FunctionObject *b, const Value *thisObject, const Value *argv, int argc)
{
    Scope scope(b);
    Scoped<RegExpObject> r(scope, thisObject->as<RegExpObject>());
    if (!r)
        return scope.engine->throwTypeError();

    Scoped<RegExpObject> re(scope, scope.engine->regExpCtor()->callAsConstructor(argv, argc));
    if (re) // Otherwise the regexp constructor should have thrown an exception
        r->d()->value.set(scope.engine, re->value());
    return Encode::undefined();
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4regexpobject.cpp, line 927, as _ZN3QV415RegExpPrototype20method_get_lastParenEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue RegExpPrototype::method_get_lastParen(const FunctionObject *b, const Value *, const Value *, int)
{
    Scope scope(b);
    ScopedArrayObject lastMatch(scope, static_cast<RegExpCtor*>(scope.engine->regExpCtor())->lastMatch());
    ScopedValue res(scope, lastMatch ? lastMatch->get(lastMatch->getLength() - 1) : Encode::undefined());
    if (res->isUndefined())
        res = scope.engine->newString();
    return res->asReturnedValue();
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4regexpobject.cpp, line 937, as _ZN3QV415RegExpPrototype16method_get_inputEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue RegExpPrototype::method_get_input(const FunctionObject *b, const Value *, const Value *, int)
{
    return static_cast<RegExpCtor*>(b->engine()->regExpCtor())->lastInput()->asReturnedValue();
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4regexpobject.cpp, line 420, as _ZN3QV415RegExpPrototype4execEPNS_15ExecutionEngineEPKNS_6ObjectEPKNS_6StringE
namespace QV4 {
inline ReturnedValue RegExpPrototype::exec(ExecutionEngine *engine, const Object *o, const String *s)
{
    Scope scope(engine);
    ScopedString key(scope, scope.engine->newString(QStringLiteral("exec")));
    ScopedFunctionObject exec(scope, o->get(key));
    if (exec) {
        ScopedValue result(scope, exec->call(o, s, 1));
        if (scope.hasException())
            RETURN_UNDEFINED();
        if (!result->isNull() && !result->isObject())
            return scope.engine->throwTypeError();
        return result->asReturnedValue();
    }
    Scoped<RegExpObject> re(scope, o);
    if (!re)
        return scope.engine->throwTypeError();
    return re->builtinExec(engine, s);
}
}  // namespace QV4
//  -----------------------------------------------------------------------

//  ReturnedValue QV4::RegExpPrototype::method_exec(const FunctionObject *a0,
//      const Value *thisObject, const Value *argv, int argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV415RegExpPrototype11method_execEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::RegExpPrototype::method_exec(a0, thisObject, argv, argc);
}

//  ReturnedValue QV4::RegExpPrototype::method_get_flags(const FunctionObject
//      *a0, const Value *thisObject, const Value *argv, int argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV415RegExpPrototype16method_get_flagsEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::RegExpPrototype::method_get_flags(a0, thisObject, argv, argc);
}

//  ReturnedValue QV4::RegExpPrototype::method_search(const FunctionObject
//      *a0, const Value *thisObject, const Value *argv, int argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV415RegExpPrototype13method_searchEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::RegExpPrototype::method_search(a0, thisObject, argv, argc);
}

//  ReturnedValue QV4::RegExpPrototype::method_get_source(const
//      FunctionObject *a0, const Value *thisObject, const Value *argv, int
//      argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV415RegExpPrototype17method_get_sourceEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::RegExpPrototype::method_get_source(a0, thisObject, argv, argc);
}

//  ReturnedValue QV4::RegExpPrototype::method_test(const FunctionObject *a0,
//      const Value *thisObject, const Value *argv, int argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV415RegExpPrototype11method_testEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::RegExpPrototype::method_test(a0, thisObject, argv, argc);
}

//  ReturnedValue QV4::RegExpPrototype::method_toString(const FunctionObject
//      *a0, const Value *thisObject, const Value *argv, int argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV415RegExpPrototype15method_toStringEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::RegExpPrototype::method_toString(a0, thisObject, argv, argc);
}

//  ReturnedValue QV4::RegExpPrototype::method_compile(const FunctionObject
//      *a0, const Value *thisObject, const Value *argv, int argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV415RegExpPrototype14method_compileEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::RegExpPrototype::method_compile(a0, thisObject, argv, argc);
}

//  ReturnedValue QV4::RegExpPrototype::method_get_lastParen(const
//      FunctionObject *a0, const Value *thisObject, const Value *argv, int
//      argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV415RegExpPrototype20method_get_lastParenEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::RegExpPrototype::method_get_lastParen(
      a0,
      thisObject,
      argv,
      argc);
}

//  ReturnedValue QV4::RegExpPrototype::method_get_input(const FunctionObject
//      *a0, const Value *thisObject, const Value *argv, int argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV415RegExpPrototype16method_get_inputEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::RegExpPrototype::method_get_input(a0, thisObject, argv, argc);
}

//  ReturnedValue QV4::RegExpPrototype::exec(ExecutionEngine *engine, const
//      Object *o, const String *s)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV415RegExpPrototype4execEPNS_15ExecutionEngineEPKNS_6ObjectEPKNS_6StringE(
    QV4::ExecutionEngine *engine,
    const QV4::Object *o,
    const QV4::String *s) {
  return QV4::RegExpPrototype::exec(engine, o, s);
}
