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

//  from ../qtdeclarative/src/qml/jsruntime/qv4proxy.cpp, line 758, as _ZN3QV45Proxy16method_revocableEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue Proxy::method_revocable(const FunctionObject *f, const Value *, const Value *argv, int argc)
{
    Scope scope(f);
    ScopedObject proxy(scope, Proxy::virtualCallAsConstructor(f, argv, argc, f));
    if (scope.hasException())
        return Encode::undefined();
    Q_ASSERT(proxy);

    ScopedString revoke(scope, scope.engine->newString(QStringLiteral("revoke")));
    ScopedFunctionObject revoker(
            scope,
            scope.engine->memoryManager->allocate<DynamicFunctionObject>(
                    scope.engine, nullptr, method_revoke));
    revoker->defineReadonlyConfigurableProperty(scope.engine->id_length(), Value::fromInt32(0));
    revoker->defineDefaultProperty(scope.engine->symbol_revokableProxy(), proxy);

    ScopedObject o(scope, scope.engine->newObject());
    ScopedString p(scope, scope.engine->newString(QStringLiteral("proxy")));
    o->defineDefaultProperty(p, proxy);
    o->defineDefaultProperty(revoke, revoker);
    return o->asReturnedValue();
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4functionobject.cpp, line 80, as _ZN3QV44Heap21DynamicFunctionObject4initEPNS_15ExecutionEngineEPNS_6StringEPFyPKNS_14FunctionObjectEPKNS_5ValueESB_iE
namespace QV4 {
inline void Heap::DynamicFunctionObject::init(
        QV4::ExecutionEngine *engine, QV4::String *name, VTable::Call call)
{
    FunctionObject::init(engine, name);
    jsCall = call;
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4proxy.cpp, line 781, as _ZN3QV45Proxy13method_revokeEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue Proxy::method_revoke(const FunctionObject *f, const Value *, const Value *, int)
{
    Scope scope(f);
    ScopedObject o(scope, f->get(scope.engine->symbol_revokableProxy()));
    Q_ASSERT(o);
    ProxyObject *proxy = o->cast<ProxyObject>();

    proxy->d()->target.set(scope.engine, nullptr);
    proxy->d()->handler.set(scope.engine, nullptr);
    return Encode::undefined();
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4proxy.cpp, line 723, as _ZN3QV45Proxy24virtualCallAsConstructorEPKNS_14FunctionObjectEPKNS_5ValueEiS6_
namespace QV4 {
inline ReturnedValue Proxy::virtualCallAsConstructor(const FunctionObject *f, const Value *argv, int argc, const Value *)
{
    Scope scope(f);
    if (argc < 2 || !argv[0].isObject() || !argv[1].isObject())
        return scope.engine->throwTypeError();

    const Object *target = static_cast<const Object *>(argv);
    const Object *handler = static_cast<const Object *>(argv + 1);
    if (const ProxyObject *ptarget = target->as<ProxyObject>())
        if (!ptarget->d()->handler)
            return scope.engine->throwTypeError();
    if (const ProxyObject *phandler = handler->as<ProxyObject>())
        if (!phandler->d()->handler)
            return scope.engine->throwTypeError();

    const FunctionObject *targetFunction = target->as<FunctionObject>();
    if (!targetFunction) {
        return scope.engine->memoryManager->allocate<ProxyObject>(target, handler)
                ->asReturnedValue();
    }

    if (targetFunction->isConstructor()) {
        return scope.engine->memoryManager->allocate<ProxyConstructorObject>(
                                                  targetFunction, handler)->asReturnedValue();
    }

    return scope.engine->memoryManager->allocate<ProxyFunctionObject>(targetFunction, handler)
            ->asReturnedValue();
}
}  // namespace QV4
//  -----------------------------------------------------------------------

//  void QV4::Heap::Proxy::markObjects(Heap::Base *b, MarkStack *stack)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap5Proxy11markObjectsEPNS0_4BaseEPNS_9MarkStackE(
    QV4::Heap::Base *b,
    QV4::MarkStack *stack) {
  QV4::Heap::Proxy::markObjects(b, stack);
}

//  QV4::Heap::Proxy as the QV4::Heap::ProxyData it is built on
extern "C" Q_DECL_EXPORT
QV4::Heap::ProxyData *ritual_cast_QV4_Heap_Proxy_QV4_Heap_ProxyData(
    QV4::Heap::Proxy *self) {
  return static_cast<QV4::Heap::ProxyData *>(self);
}
