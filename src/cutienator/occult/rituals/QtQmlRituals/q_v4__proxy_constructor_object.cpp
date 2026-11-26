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

//  from ../qtdeclarative/src/qml/jsruntime/qv4proxy.cpp, line 649, as _ZN3QV422ProxyConstructorObject24virtualCallAsConstructorEPKNS_14FunctionObjectEPKNS_5ValueEiS6_
namespace QV4 {
inline ReturnedValue ProxyConstructorObject::virtualCallAsConstructor(
        const FunctionObject *f, const Value *argv, int argc, const Value *newTarget)
{
    Scope scope(f);
    const ProxyObject *o = static_cast<const ProxyObject *>(f);
    if (!o->d()->handler)
        return scope.engine->throwTypeError();

    ScopedFunctionObject target(scope, o->d()->target);
    Q_ASSERT(target);
    ScopedObject handler(scope, o->d()->handler);
    ScopedString name(scope, scope.engine->newString(QStringLiteral("construct")));
    ScopedValue trap(scope, handler->get(name));

    if (scope.hasException())
        return Encode::undefined();
    if (trap->isNullOrUndefined())
        return target->callAsConstructor(argv, argc, newTarget);
    if (!trap->isFunctionObject())
        return scope.engine->throwTypeError();

    ScopedFunctionObject trapFunction(scope, trap);
    Value *arguments = scope.constructUndefined(3);
    arguments[0] = target;
    arguments[1] = scope.engine->newArrayObject(argv, argc);
    arguments[2] = newTarget ? *newTarget : Value::undefinedValue();
    ScopedObject result(scope, trapFunction->call(handler, arguments, 3));

    if (!result)
        return scope.engine->throwTypeError();
    return result->asReturnedValue();
}
}  // namespace QV4
//  -----------------------------------------------------------------------

//  void QV4::ProxyConstructorObject::__dataTest()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV422ProxyConstructorObject10__dataTestEv(
    QV4::ProxyConstructorObject *self) {
  self->__dataTest();
}

//  QV4::Heap::ProxyConstructorObject
//      *QV4::ProxyConstructorObject::d_unchecked() const
extern "C" Q_DECL_EXPORT
QV4::Heap::ProxyConstructorObject *ritual_ZNK3QV422ProxyConstructorObject11d_uncheckedEv(
    const QV4::ProxyConstructorObject *self) {
  return self->d_unchecked();
}

//  QV4::Heap::ProxyConstructorObject *QV4::ProxyConstructorObject::d() const
extern "C" Q_DECL_EXPORT
QV4::Heap::ProxyConstructorObject *ritual_ZNK3QV422ProxyConstructorObject1dEv(
    const QV4::ProxyConstructorObject *self) {
  return self->d();
}

//  ReturnedValue QV4::ProxyConstructorObject::virtualCallAsConstructor(const
//      FunctionObject *f, const Value *argv, int argc, const Value *a3)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV422ProxyConstructorObject24virtualCallAsConstructorEPKNS_14FunctionObjectEPKNS_5ValueEiS6_(
    const QV4::FunctionObject *f,
    const QV4::Value *argv,
    int argc,
    const QV4::Value *a3) {
  return QV4::ProxyConstructorObject::virtualCallAsConstructor(
      f,
      argv,
      argc,
      a3);
}
