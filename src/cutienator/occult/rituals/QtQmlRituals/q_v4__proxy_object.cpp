//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4proxy_p.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4proxy_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4propertykey_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4value_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4global_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qv4propertykey_p.h>
#include <QtCore/qstring.h>
#include <QtQml/private/qv4string_p.h>
#include <QtQml/private/qv4engine_p.h>
#include <QtQml/private/qv4scopedvalue_p.h>
#include <QtQml/private/qv4mm_p.h>
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

using namespace Qt::Literals::StringLiterals;

//  from ../qtdeclarative/src/qml/jsruntime/qv4propertykey.cpp, line 15, as _ZN3QV411PropertyKey16toStringOrSymbolEPNS_15ExecutionEngineE
inline QV4::Heap::StringOrSymbol *QV4::PropertyKey::toStringOrSymbol(QV4::ExecutionEngine *e)
{
    if (isArrayIndex())
        return Value::fromUInt32(asArrayIndex()).toString(e);
    return asStringOrSymbol();
}

//  from ../qtdeclarative/src/qml/jsruntime/qv4proxy.cpp, line 36, as _ZN3QV411ProxyObject10virtualGetEPKNS_7ManagedENS_11PropertyKeyEPKNS_5ValueEPb
namespace QV4 {
inline ReturnedValue ProxyObject::virtualGet(const Managed *m, PropertyKey id, const Value *receiver, bool *hasProperty)
{
    Scope scope(m);
    const ProxyObject *o = static_cast<const ProxyObject *>(m);
    if (!o->d()->handler)
        return scope.engine->throwTypeError();

    ScopedObject target(scope, o->d()->target);
    Q_ASSERT(target);
    ScopedObject handler(scope, o->d()->handler);
    ScopedValue trap(scope, handler->get(scope.engine->id_get()));
    if (scope.hasException())
        return Encode::undefined();
    if (trap->isNullOrUndefined())
        return target->get(id, receiver, hasProperty);
    if (!trap->isFunctionObject())
        return scope.engine->throwTypeError();
    if (hasProperty)
        *hasProperty = true;

    Value *args = scope.constructUndefined(3);
    args[0] = target;
    args[1] = id.toStringOrSymbol(scope.engine);
    args[2] = *receiver;
    JSCallData cdata(handler, args, 3);

    ScopedValue trapResult(scope, static_cast<const FunctionObject *>(trap.ptr)->call(cdata));
    if (scope.hasException())
        return Encode::undefined();
    ScopedProperty targetDesc(scope);
    PropertyAttributes attributes = target->getOwnProperty(id, targetDesc);
    if (attributes != Attr_Invalid && !attributes.isConfigurable()) {
        if (attributes.isData() && !attributes.isWritable()) {
            if (!trapResult->sameValue(targetDesc->value))
                return scope.engine->throwTypeError();
        }
        if (attributes.isAccessor() && targetDesc->value.isUndefined()) {
            if (!trapResult->isUndefined())
                return scope.engine->throwTypeError();
        }
   }
    return trapResult->asReturnedValue();
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4proxy.cpp, line 80, as _ZN3QV411ProxyObject10virtualPutEPNS_7ManagedENS_11PropertyKeyERKNS_5ValueEPS4_
namespace QV4 {
inline bool ProxyObject::virtualPut(Managed *m, PropertyKey id, const Value &value, Value *receiver)
{
    Scope scope(m);
    const ProxyObject *o = static_cast<const ProxyObject *>(m);
    if (!o->d()->handler)
        return scope.engine->throwTypeError();

    ScopedObject target(scope, o->d()->target);
    Q_ASSERT(target);
    ScopedObject handler(scope, o->d()->handler);
    ScopedValue trap(scope, handler->get(scope.engine->id_set()));
    if (scope.hasException())
        return Encode::undefined();
    if (trap->isNullOrUndefined())
        return target->put(id, value, receiver);
    if (!trap->isFunctionObject())
        return scope.engine->throwTypeError();

    Value *args = scope.constructUndefined(4);
    args[0] = target;
    args[1] = id.toStringOrSymbol(scope.engine);
    args[2] = value;
    args[3] = *receiver;
    JSCallData cdata(handler, args, 4);

    ScopedValue trapResult(scope, static_cast<const FunctionObject *>(trap.ptr)->call(cdata));
    if (scope.hasException() || !trapResult->toBoolean())
        return false;
    ScopedProperty targetDesc(scope);
    PropertyAttributes attributes = target->getOwnProperty(id, targetDesc);
    if (attributes != Attr_Invalid && !attributes.isConfigurable()) {
        if (attributes.isData() && !attributes.isWritable()) {
            if (!value.sameValue(targetDesc->value))
                return scope.engine->throwTypeError();
        }
        if (attributes.isAccessor() && targetDesc->set.isUndefined())
            return scope.engine->throwTypeError();
    }
    return true;
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4proxy.cpp, line 121, as _ZN3QV411ProxyObject21virtualDeletePropertyEPNS_7ManagedENS_11PropertyKeyE
namespace QV4 {
inline bool ProxyObject::virtualDeleteProperty(Managed *m, PropertyKey id)
{
    Scope scope(m);
    const ProxyObject *o = static_cast<const ProxyObject *>(m);
    if (!o->d()->handler)
        return scope.engine->throwTypeError();

    ScopedObject target(scope, o->d()->target);
    Q_ASSERT(target);
    ScopedObject handler(scope, o->d()->handler);
    ScopedString deleteProp(scope, scope.engine->newString(QStringLiteral("deleteProperty")));
    ScopedValue trap(scope, handler->get(deleteProp));
    if (scope.hasException())
        return Encode::undefined();
    if (trap->isNullOrUndefined())
        return target->deleteProperty(id);
    if (!trap->isFunctionObject())
        return scope.engine->throwTypeError();

    Value *args = scope.constructUndefined(3);
    args[0] = target;
    args[1] = id.toStringOrSymbol(scope.engine);
    args[2] = o->d(); // ### fix receiver handling
    JSCallData cdata(handler, args, 3);

    ScopedValue trapResult(scope, static_cast<const FunctionObject *>(trap.ptr)->call(cdata));
    if (scope.hasException() || !trapResult->toBoolean())
        return false;
    ScopedProperty targetDesc(scope);
    PropertyAttributes attributes = target->getOwnProperty(id, targetDesc);
    if (attributes == Attr_Invalid)
        return true;
    if (!attributes.isConfigurable())
        return scope.engine->throwTypeError();
    return true;
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4proxy.cpp, line 158, as _ZN3QV411ProxyObject18virtualHasPropertyEPKNS_7ManagedENS_11PropertyKeyE
namespace QV4 {
inline bool ProxyObject::virtualHasProperty(const Managed *m, PropertyKey id)
{
    Scope scope(m);
    const ProxyObject *o = static_cast<const ProxyObject *>(m);
    if (!o->d()->handler)
        return scope.engine->throwTypeError();

    ScopedObject target(scope, o->d()->target);
    Q_ASSERT(target);
    ScopedObject handler(scope, o->d()->handler);
    ScopedString hasProp(scope, scope.engine->newString(QStringLiteral("has")));
    ScopedValue trap(scope, handler->get(hasProp));
    if (scope.hasException())
        return Encode::undefined();
    if (trap->isNullOrUndefined())
        return target->hasProperty(id);
    if (!trap->isFunctionObject())
        return scope.engine->throwTypeError();

    Value *args = scope.constructUndefined(2);
    args[0] = target;
    args[1] = id.isArrayIndex() ? Value::fromUInt32(id.asArrayIndex()).toString(scope.engine) : id.asStringOrSymbol();
    JSCallData cdata(handler, args, 2);

    ScopedValue trapResult(scope, static_cast<const FunctionObject *>(trap.ptr)->call(cdata));
    if (scope.hasException())
        return false;
    bool result = trapResult->toBoolean();
    if (!result) {
        ScopedProperty targetDesc(scope);
        PropertyAttributes attributes = target->getOwnProperty(id, targetDesc);
        if (attributes != Attr_Invalid) {
            if (!attributes.isConfigurable() || !target->isExtensible())
                return scope.engine->throwTypeError();
        }
    }
    return result;
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4proxy.cpp, line 197, as _ZN3QV411ProxyObject21virtualGetOwnPropertyEPKNS_7ManagedENS_11PropertyKeyEPNS_8PropertyE
namespace QV4 {
inline PropertyAttributes ProxyObject::virtualGetOwnProperty(const Managed *m, PropertyKey id, Property *p)
{
    Scope scope(m);
    const ProxyObject *o = static_cast<const ProxyObject *>(m);
    if (!o->d()->handler) {
        scope.engine->throwTypeError();
        return Attr_Invalid;
    }

    ScopedObject target(scope, o->d()->target);
    Q_ASSERT(target);
    ScopedObject handler(scope, o->d()->handler);
    ScopedString deleteProp(scope, scope.engine->newString(QStringLiteral("getOwnPropertyDescriptor")));
    ScopedValue trap(scope, handler->get(deleteProp));
    if (scope.hasException())
        return Attr_Invalid;
    if (trap->isNullOrUndefined())
        return target->getOwnProperty(id, p);
    if (!trap->isFunctionObject()) {
        scope.engine->throwTypeError();
        return Attr_Invalid;
    }

    Value *args = scope.constructUndefined(2);
    args[0] = target;
    args[1] = id.isArrayIndex() ? Value::fromUInt32(id.asArrayIndex()).toString(scope.engine) : id.asStringOrSymbol();
    JSCallData cdata(handler, args, 2);

    ScopedValue trapResult(scope, static_cast<const FunctionObject *>(trap.ptr)->call(cdata));
    if (scope.hasException())
        return Attr_Invalid;
    if (!trapResult->isObject() && !trapResult->isUndefined()) {
        scope.engine->throwTypeError();
        return Attr_Invalid;
    }

    ScopedProperty targetDesc(scope);
    PropertyAttributes targetAttributes = target->getOwnProperty(id, targetDesc);
    if (trapResult->isUndefined()) {
        if (p)
            p->value = Encode::undefined();
        if (targetAttributes == Attr_Invalid) {
            return Attr_Invalid;
        }
        if (!targetAttributes.isConfigurable() || !target->isExtensible()) {
            scope.engine->throwTypeError();
            return Attr_Invalid;
        }
        return Attr_Invalid;
    }

    //bool extensibleTarget = target->isExtensible();
    ScopedProperty resultDesc(scope);
    PropertyAttributes resultAttributes;
    ObjectPrototype::toPropertyDescriptor(scope.engine, trapResult, resultDesc, &resultAttributes);
    resultDesc->completed(&resultAttributes);

    if (!targetDesc->isCompatible(targetAttributes, resultDesc, resultAttributes)) {
        scope.engine->throwTypeError();
        return Attr_Invalid;
    }

    if (!resultAttributes.isConfigurable()) {
        if (targetAttributes == Attr_Invalid || targetAttributes.isConfigurable()) {
            scope.engine->throwTypeError();
            return Attr_Invalid;
        }
    }

    if (p) {
        p->value = resultDesc->value;
        p->set = resultDesc->set;
    }
    return resultAttributes;
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4proxy.cpp, line 273, as _ZN3QV411ProxyObject24virtualDefineOwnPropertyEPNS_7ManagedENS_11PropertyKeyEPKNS_8PropertyENS_18PropertyAttributesE
namespace QV4 {
inline bool ProxyObject::virtualDefineOwnProperty(Managed *m, PropertyKey id, const Property *p, PropertyAttributes attrs)
{
    Scope scope(m);
    const ProxyObject *o = static_cast<const ProxyObject *>(m);
    if (!o->d()->handler) {
        scope.engine->throwTypeError();
        return false;
    }

    ScopedObject target(scope, o->d()->target);
    Q_ASSERT(target);
    ScopedObject handler(scope, o->d()->handler);
    ScopedString prop(scope, scope.engine->newString(QStringLiteral("defineProperty")));
    ScopedValue trap(scope, handler->get(prop));
    if (scope.hasException())
        return false;
    if (trap->isNullOrUndefined())
        return target->defineOwnProperty(id, p, attrs);
    if (!trap->isFunctionObject()) {
        scope.engine->throwTypeError();
        return false;
    }

    Value *args = scope.constructUndefined(3);
    args[0] = target;
    args[1] = id.isArrayIndex() ? Value::fromUInt32(id.asArrayIndex()).toString(scope.engine) : id.asStringOrSymbol();
    args[2] = ObjectPrototype::fromPropertyDescriptor(scope.engine, p, attrs);
    JSCallData cdata(handler, args, 3);

    ScopedValue trapResult(scope, static_cast<const FunctionObject *>(trap.ptr)->call(cdata));
    bool result = !scope.hasException() && trapResult->toBoolean();
    if (!result)
        return false;

    ScopedProperty targetDesc(scope);
    PropertyAttributes targetAttributes = target->getOwnProperty(id, targetDesc);
    bool extensibleTarget = target->isExtensible();
    bool settingConfigFalse = attrs.hasConfigurable() && !attrs.isConfigurable();
    if (targetAttributes == Attr_Invalid) {
        if (!extensibleTarget || settingConfigFalse) {
            scope.engine->throwTypeError();
            return false;
        }
    } else {
        if (!targetDesc->isCompatible(targetAttributes, p, attrs)) {
            scope.engine->throwTypeError();
            return false;
        }
        if (settingConfigFalse && targetAttributes.isConfigurable()) {
            scope.engine->throwTypeError();
            return false;
        }
    }

    return true;
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4proxy.cpp, line 330, as _ZN3QV411ProxyObject19virtualIsExtensibleEPKNS_7ManagedE
namespace QV4 {
inline bool ProxyObject::virtualIsExtensible(const Managed *m)
{
    Scope scope(m);
    const ProxyObject *o = static_cast<const ProxyObject *>(m);
    if (!o->d()->handler)
        return scope.engine->throwTypeError();

    ScopedObject target(scope, o->d()->target);
    Q_ASSERT(target);
    ScopedObject handler(scope, o->d()->handler);
    ScopedString hasProp(scope, scope.engine->newString(QStringLiteral("isExtensible")));
    ScopedValue trap(scope, handler->get(hasProp));
    if (scope.hasException())
        return Encode::undefined();
    if (trap->isNullOrUndefined())
        return target->isExtensible();
    if (!trap->isFunctionObject())
        return scope.engine->throwTypeError();

    Value *args = scope.constructUndefined(1);
    args[0] = target;
    JSCallData cdata(handler, args, 1);

    ScopedValue trapResult(scope, static_cast<const FunctionObject *>(trap.ptr)->call(cdata));
    if (scope.hasException())
        return false;
    bool result = trapResult->toBoolean();
    if (result != target->isExtensible()) {
        scope.engine->throwTypeError();
        return false;
    }
    return result;
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4proxy.cpp, line 364, as _ZN3QV411ProxyObject24virtualPreventExtensionsEPNS_7ManagedE
namespace QV4 {
inline bool ProxyObject::virtualPreventExtensions(Managed *m)
{
    Scope scope(m);
    const ProxyObject *o = static_cast<const ProxyObject *>(m);
    if (!o->d()->handler)
        return scope.engine->throwTypeError();

    ScopedObject target(scope, o->d()->target);
    Q_ASSERT(target);
    ScopedObject handler(scope, o->d()->handler);
    ScopedString hasProp(scope, scope.engine->newString(QStringLiteral("preventExtensions")));
    ScopedValue trap(scope, handler->get(hasProp));
    if (scope.hasException())
        return Encode::undefined();
    if (trap->isNullOrUndefined())
        return target->preventExtensions();
    if (!trap->isFunctionObject())
        return scope.engine->throwTypeError();

    Value *args = scope.constructUndefined(1);
    args[0] = target;
    JSCallData cdata(handler, args, 1);

    ScopedValue trapResult(scope, static_cast<const FunctionObject *>(trap.ptr)->call(cdata));
    if (scope.hasException())
        return false;
    bool result = trapResult->toBoolean();
    if (result && target->isExtensible()) {
        scope.engine->throwTypeError();
        return false;
    }
    return result;
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4proxy.cpp, line 398, as _ZN3QV411ProxyObject21virtualGetPrototypeOfEPKNS_7ManagedE
namespace QV4 {
inline Heap::Object *ProxyObject::virtualGetPrototypeOf(const Managed *m)
{
    Scope scope(m);
    const ProxyObject *o = static_cast<const ProxyObject *>(m);
    if (!o->d()->handler) {
        scope.engine->throwTypeError();
        return nullptr;
    }

    ScopedObject target(scope, o->d()->target);
    Q_ASSERT(target);
    ScopedObject handler(scope, o->d()->handler);
    ScopedString name(scope, scope.engine->newString(QStringLiteral("getPrototypeOf")));
    ScopedValue trap(scope, handler->get(name));
    if (scope.hasException())
        return nullptr;
    if (trap->isNullOrUndefined())
        return target->getPrototypeOf();
    if (!trap->isFunctionObject()) {
        scope.engine->throwTypeError();
        return nullptr;
    }

    Value *args = scope.constructUndefined(1);
    args[0] = target;
    JSCallData cdata(handler, args, 1);

    ScopedValue trapResult(scope, static_cast<const FunctionObject *>(trap.ptr)->call(cdata));
    if (scope.hasException())
        return nullptr;
    if (!trapResult->isNull() && !trapResult->isObject()) {
        scope.engine->throwTypeError();
        return nullptr;
    }
    Heap::Object *proto = trapResult->isNull() ? nullptr : static_cast<Heap::Object *>(trapResult->heapObject());
    if (!target->isExtensible()) {
        Heap::Object *targetProto = target->getPrototypeOf();
        if (proto != targetProto) {
            scope.engine->throwTypeError();
            return nullptr;
        }
    }
    return proto;
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4proxy.cpp, line 443, as _ZN3QV411ProxyObject21virtualSetPrototypeOfEPNS_7ManagedEPKNS_6ObjectE
namespace QV4 {
inline bool ProxyObject::virtualSetPrototypeOf(Managed *m, const Object *p)
{
    Scope scope(m);
    const ProxyObject *o = static_cast<const ProxyObject *>(m);
    if (!o->d()->handler) {
        scope.engine->throwTypeError();
        return false;
    }

    ScopedObject target(scope, o->d()->target);
    Q_ASSERT(target);
    ScopedObject handler(scope, o->d()->handler);
    ScopedString name(scope, scope.engine->newString(QStringLiteral("setPrototypeOf")));
    ScopedValue trap(scope, handler->get(name));
    if (scope.hasException())
        return false;
    if (trap->isNullOrUndefined())
        return target->setPrototypeOf(p);
    if (!trap->isFunctionObject()) {
        scope.engine->throwTypeError();
        return false;
    }

    Value *args = scope.constructUndefined(2);
    args[0] = target;
    args[1] = p ? p->asReturnedValue() : Encode::null();
    JSCallData cdata(handler, args, 2);

    ScopedValue trapResult(scope, static_cast<const FunctionObject *>(trap.ptr)->call(cdata));
    bool result = !scope.hasException() && trapResult->toBoolean();
    if (!result)
        return false;
    if (!target->isExtensible()) {
        Heap::Object *targetProto = target->getPrototypeOf();
        if (p->d() != targetProto) {
            scope.engine->throwTypeError();
            return false;
        }
    }
    return true;
}
}  // namespace QV4
//  -----------------------------------------------------------------------

//  void QV4::ProxyObject::__dataTest()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV411ProxyObject10__dataTestEv(QV4::ProxyObject *self) {
  self->__dataTest();
}

//  QV4::Heap::ProxyObject *QV4::ProxyObject::d_unchecked() const
extern "C" Q_DECL_EXPORT
QV4::Heap::ProxyObject *ritual_ZNK3QV411ProxyObject11d_uncheckedEv(
    const QV4::ProxyObject *self) {
  return self->d_unchecked();
}

//  QV4::Heap::ProxyObject *QV4::ProxyObject::d() const
extern "C" Q_DECL_EXPORT
QV4::Heap::ProxyObject *ritual_ZNK3QV411ProxyObject1dEv(
    const QV4::ProxyObject *self) {
  return self->d();
}

//  Heap::InternalClass
//      *QV4::ProxyObject::defaultInternalClass(QV4::EngineBase *e)
extern "C" Q_DECL_EXPORT
QV4::Heap::InternalClass *ritual_ZN3QV411ProxyObject20defaultInternalClassEPNS_10EngineBaseE(
    QV4::EngineBase *e) {
  return QV4::ProxyObject::defaultInternalClass(e);
}

//  ReturnedValue QV4::ProxyObject::virtualGet(const Managed *m, PropertyKey
//      id, const Value *receiver, bool *hasProperty)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV411ProxyObject10virtualGetEPKNS_7ManagedENS_11PropertyKeyEPKNS_5ValueEPb(
    const QV4::Managed *m,
    const QV4::PropertyKey *id,
    const QV4::Value *receiver,
    bool *hasProperty) {
  return QV4::ProxyObject::virtualGet(m, *id, receiver, hasProperty);
}

//  bool QV4::ProxyObject::virtualPut(Managed *m, PropertyKey id, const Value
//      &value, Value *receiver)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV411ProxyObject10virtualPutEPNS_7ManagedENS_11PropertyKeyERKNS_5ValueEPS4_(
    QV4::Managed *m,
    const QV4::PropertyKey *id,
    const QV4::Value *value,
    QV4::Value *receiver) {
  return QV4::ProxyObject::virtualPut(m, *id, *value, receiver);
}

//  bool QV4::ProxyObject::virtualDeleteProperty(Managed *m, PropertyKey id)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV411ProxyObject21virtualDeletePropertyEPNS_7ManagedENS_11PropertyKeyE(
    QV4::Managed *m,
    const QV4::PropertyKey *id) {
  return QV4::ProxyObject::virtualDeleteProperty(m, *id);
}

//  bool QV4::ProxyObject::virtualHasProperty(const Managed *m, PropertyKey
//      id)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV411ProxyObject18virtualHasPropertyEPKNS_7ManagedENS_11PropertyKeyE(
    const QV4::Managed *m,
    const QV4::PropertyKey *id) {
  return QV4::ProxyObject::virtualHasProperty(m, *id);
}

//  PropertyAttributes QV4::ProxyObject::virtualGetOwnProperty(const Managed
//      *m, PropertyKey id, Property *p)
extern "C" Q_DECL_EXPORT
QV4::PropertyAttributes *ritual_ZN3QV411ProxyObject21virtualGetOwnPropertyEPKNS_7ManagedENS_11PropertyKeyEPNS_8PropertyE(
    const QV4::Managed *m,
    const QV4::PropertyKey *id,
    QV4::Property *p) {
  return new QV4::PropertyAttributes(
      QV4::ProxyObject::virtualGetOwnProperty(
          m,
          *id,
          p));
}

//  bool QV4::ProxyObject::virtualDefineOwnProperty(Managed *m, PropertyKey
//      id, const Property *p, PropertyAttributes attrs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV411ProxyObject24virtualDefineOwnPropertyEPNS_7ManagedENS_11PropertyKeyEPKNS_8PropertyENS_18PropertyAttributesE(
    QV4::Managed *m,
    const QV4::PropertyKey *id,
    const QV4::Property *p,
    const QV4::PropertyAttributes *attrs) {
  return QV4::ProxyObject::virtualDefineOwnProperty(m, *id, p, *attrs);
}

//  bool QV4::ProxyObject::virtualIsExtensible(const Managed *m)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV411ProxyObject19virtualIsExtensibleEPKNS_7ManagedE(
    const QV4::Managed *m) {
  return QV4::ProxyObject::virtualIsExtensible(m);
}

//  bool QV4::ProxyObject::virtualPreventExtensions(Managed *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV411ProxyObject24virtualPreventExtensionsEPNS_7ManagedE(
    QV4::Managed *a0) {
  return QV4::ProxyObject::virtualPreventExtensions(a0);
}

//  Heap::Object *QV4::ProxyObject::virtualGetPrototypeOf(const Managed *a0)
extern "C" Q_DECL_EXPORT
QV4::Heap::Object *ritual_ZN3QV411ProxyObject21virtualGetPrototypeOfEPKNS_7ManagedE(
    const QV4::Managed *a0) {
  return QV4::ProxyObject::virtualGetPrototypeOf(a0);
}

//  bool QV4::ProxyObject::virtualSetPrototypeOf(Managed *a0, const Object
//      *a1)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV411ProxyObject21virtualSetPrototypeOfEPNS_7ManagedEPKNS_6ObjectE(
    QV4::Managed *a0,
    const QV4::Object *a1) {
  return QV4::ProxyObject::virtualSetPrototypeOf(a0, a1);
}
