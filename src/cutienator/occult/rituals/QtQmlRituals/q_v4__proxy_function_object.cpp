//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4proxy_p.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4proxy_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qv4proxy_p.h>
#include <QtQml/private/qv4symbol_p.h>
#include <QtQml/private/qv4jscall_p.h>
#include <QtQml/private/qv4objectproto_p.h>
#include <QtQml/private/qv4persistent_p.h>
#include <QtQml/private/qv4objectiterator_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/jsruntime/qv4proxy.cpp, line 682, as _ZN3QV419ProxyFunctionObject11virtualCallEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue ProxyFunctionObject::virtualCall(const FunctionObject *f, const Value *thisObject, const Value *argv, int argc)
{
    Scope scope(f);

    const ProxyObject *o = static_cast<const ProxyObject *>(f);
    if (!o->d()->handler)
        return scope.engine->throwTypeError();

    ScopedFunctionObject target(scope, o->d()->target);
    Q_ASSERT(target);
    ScopedObject handler(scope, o->d()->handler);
    ScopedString name(scope, scope.engine->newString(QStringLiteral("apply")));
    ScopedValue trap(scope, handler->get(name));

    if (scope.hasException())
        return Encode::undefined();
    if (trap->isNullOrUndefined())
        return checkedResult(scope.engine, target->call(thisObject, argv, argc));
    if (!trap->isFunctionObject())
        return scope.engine->throwTypeError();

    ScopedFunctionObject trapFunction(scope, trap);
    Value *arguments = scope.constructUndefined(3);
    arguments[0] = target;
    arguments[1] = thisObject ? *thisObject : Value::undefinedValue();
    arguments[2] = scope.engine->newArrayObject(argv, argc);
    return trapFunction->call(handler, arguments, 3);
}
}  // namespace QV4
//  -----------------------------------------------------------------------

//  void QV4::ProxyFunctionObject::__dataTest()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV419ProxyFunctionObject10__dataTestEv(
    QV4::ProxyFunctionObject *self) {
  self->__dataTest();
}

//  QV4::Heap::ProxyFunctionObject *QV4::ProxyFunctionObject::d_unchecked()
//      const
extern "C" Q_DECL_EXPORT
QV4::Heap::ProxyFunctionObject *ritual_ZNK3QV419ProxyFunctionObject11d_uncheckedEv(
    const QV4::ProxyFunctionObject *self) {
  return self->d_unchecked();
}

//  QV4::Heap::ProxyFunctionObject *QV4::ProxyFunctionObject::d() const
extern "C" Q_DECL_EXPORT
QV4::Heap::ProxyFunctionObject *ritual_ZNK3QV419ProxyFunctionObject1dEv(
    const QV4::ProxyFunctionObject *self) {
  return self->d();
}

//  Heap::InternalClass
//      *QV4::ProxyFunctionObject::defaultInternalClass(QV4::EngineBase *e)
extern "C" Q_DECL_EXPORT
QV4::Heap::InternalClass *ritual_ZN3QV419ProxyFunctionObject20defaultInternalClassEPNS_10EngineBaseE(
    QV4::EngineBase *e) {
  return QV4::ProxyFunctionObject::defaultInternalClass(e);
}

//  ReturnedValue QV4::ProxyFunctionObject::virtualCall(const FunctionObject
//      *f, const Value *thisObject, const Value *argv, int argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV419ProxyFunctionObject11virtualCallEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *f,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::ProxyFunctionObject::virtualCall(f, thisObject, argv, argc);
}
