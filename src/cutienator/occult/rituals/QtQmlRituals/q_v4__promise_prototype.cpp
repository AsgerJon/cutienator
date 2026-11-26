//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4promiseobject_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4promiseobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/QCoreApplication>
#include <QtQml/private/qv4promiseobject_p.h>
#include <QtQml/private/qv4symbol_p.h>
#include <QtQml/private/qv4jscall_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/jsruntime/qv4promiseobject.cpp, line 45, as local:qv4promiseobject.cpp:dropException
namespace {
inline void dropException(QV4::ExecutionEngine* e)
{
    e->hasException = false;
}
}  // namespace

//  from ../qtdeclarative/src/qml/jsruntime/qv4promiseobject.cpp, line 877, as _ZN3QV416PromisePrototype12method_catchEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
using namespace QV4::Promise;
inline ReturnedValue PromisePrototype::method_catch(const FunctionObject *f, const Value *thisObject, const Value *argv, int argc)
{
    Scope scope(f);
    Scoped<Object> promise(scope);
    if (thisObject->isObject()) {
        promise.setPointer(thisObject->as<Object>());
    } else if (thisObject->isBoolean()) {
        promise = scope.engine->newBooleanObject(thisObject->toBoolean());
    } else if (thisObject->isInteger() || thisObject->isDouble()) {
        promise = scope.engine->newNumberObject(thisObject->toInteger());
    } else if (thisObject->isString()) {
        ScopedString scopedString(scope, thisObject->toString(scope.engine));
        promise = scope.engine->newStringObject(scopedString);
    } else {
        THROW_TYPE_ERROR();
    }

    ScopedValue onRejected(scope);
    if (argc < 1) {
        onRejected = Encode::undefined();
    } else {
        onRejected = argv[0];
    }

    JSCallArguments jsCallData(scope, 2);
    jsCallData.args[0] = Encode::undefined();
    jsCallData.args[1] = onRejected;
    jsCallData.thisObject = promise;

    ScopedString thenName(scope, scope.engine->newIdentifier(QStringLiteral("then")));
    ScopedFunctionObject then(scope, promise->get(thenName));
    if (!then || scope.hasException())
        THROW_TYPE_ERROR();

    return then->call(jsCallData);
}
}  // namespace QV4
//  -----------------------------------------------------------------------

//  ReturnedValue QV4::PromisePrototype::method_catch(const FunctionObject
//      *f, const Value *thisObject, const Value *argv, int argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV416PromisePrototype12method_catchEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *f,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::PromisePrototype::method_catch(f, thisObject, argv, argc);
}
