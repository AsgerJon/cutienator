//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4argumentsobject_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4argumentsobject_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4propertykey_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4global_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4value_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/QString>
#include <QtQml/private/qv4context_p.h>
#include <QtQml/private/qv4object_p.h>
#include <QtQml/private/qv4objectproto_p.h>
#include <QtQml/private/qv4mm_p.h>
#include <QtQml/private/qv4argumentsobject_p.h>
#include <QtQml/private/qv4function_p.h>
#include <QtQml/private/qv4stackframe_p.h>
#include <QtQml/private/qv4symbol_p.h>
#include <QtQml/private/qv4argumentsobject_p.h>
#include <QtQml/private/qv4alloca_p.h>
#include <QtQml/private/qv4arrayobject_p.h>
#include <QtQml/private/qv4function_p.h>
#include <QtQml/private/qv4jscall_p.h>
#include <QtQml/private/qv4scopedvalue_p.h>
#include <QtQml/private/qv4stackframe_p.h>
#include <QtQml/private/qv4string_p.h>
#include <QtQml/private/qv4symbol_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/jsruntime/qv4context.cpp, line 410, as _ZN3QV44Heap11CallContext6setArgEjNS_5ValueE
namespace QV4 {
inline void Heap::CallContext::setArg(uint index, Value v)
{
    locals.set(internalClass->engine, locals.size + index, v);
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4argumentsobject.cpp, line 83, as _ZN3QV415ArgumentsObject24virtualDefineOwnPropertyEPNS_7ManagedENS_11PropertyKeyEPKNS_8PropertyENS_18PropertyAttributesE
namespace QV4 {
inline bool ArgumentsObject::virtualDefineOwnProperty(Managed *m, PropertyKey id, const Property *desc, PropertyAttributes attrs)
{
    ArgumentsObject *args = static_cast<ArgumentsObject *>(m);
    args->fullyCreate();
    if (!id.isArrayIndex())
        return Object::virtualDefineOwnProperty(m, id, desc, attrs);

    uint index = id.asArrayIndex();

    if (!args->isMapped(index))
        return Object::virtualDefineOwnProperty(m, id, desc, attrs);

    Scope scope(args);
    PropertyAttributes cAttrs = attrs;
    ScopedProperty cDesc(scope);
    cDesc->copy(desc, attrs);

    if (attrs.isData() && desc->value.isEmpty() && attrs.hasWritable() && !attrs.isWritable()) {
        cDesc->value = args->context()->args()[index];
        cAttrs.setType(PropertyAttributes::Data);
    }

    bool allowed = Object::virtualDefineOwnProperty(m, id, cDesc, cAttrs);
    if (!allowed)
        return false;

    if (attrs.isAccessor()) {
        args->removeMapping(index);
    } else {
        if (!desc->value.isEmpty())
            args->context()->setArg(index, desc->value);
        if (attrs.hasWritable() && !attrs.isWritable())
            args->removeMapping(index);
    }
    return true;
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4argumentsobject.cpp, line 120, as _ZN3QV415ArgumentsObject10virtualGetEPKNS_7ManagedENS_11PropertyKeyEPKNS_5ValueEPb
namespace QV4 {
inline ReturnedValue ArgumentsObject::virtualGet(const Managed *m, PropertyKey id, const Value *receiver, bool *hasProperty)
{
    if (id.isArrayIndex()) {
        const ArgumentsObject *args = static_cast<const ArgumentsObject *>(m);
        uint index = id.asArrayIndex();
        if (index < args->d()->argCount && !args->d()->fullyCreated) {
            if (hasProperty)
                *hasProperty = true;
            return args->context()->args()[index].asReturnedValue();
        }

        if (args->isMapped(index)) {
            Q_ASSERT(index < static_cast<uint>(args->context()->function->formalParameterCount()));
            if (hasProperty)
                *hasProperty = true;
            return args->context()->args()[index].asReturnedValue();
        }
    }

    return Object::virtualGet(m, id, receiver, hasProperty);
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4argumentsobject.cpp, line 142, as _ZN3QV415ArgumentsObject10virtualPutEPNS_7ManagedENS_11PropertyKeyERKNS_5ValueEPS4_
namespace QV4 {
inline bool ArgumentsObject::virtualPut(Managed *m, PropertyKey id, const Value &value, Value *receiver)
{
    if (id.isArrayIndex()) {
        ArgumentsObject *args = static_cast<ArgumentsObject *>(m);
        uint index = id.asArrayIndex();

        if (args == receiver && index < args->d()->argCount && !args->d()->fullyCreated) {
            args->context()->setArg(index, value);
            return true;
        }

        bool isMapped = (args == receiver && args->isMapped(index));
        if (isMapped)
            args->context()->setArg(index, value);
    }

    return Object::virtualPut(m, id, value, receiver);
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4argumentsobject.cpp, line 161, as _ZN3QV415ArgumentsObject21virtualDeletePropertyEPNS_7ManagedENS_11PropertyKeyE
namespace QV4 {
inline bool ArgumentsObject::virtualDeleteProperty(Managed *m, PropertyKey id)
{
    ArgumentsObject *args = static_cast<ArgumentsObject *>(m);
    args->fullyCreate();
    bool result = Object::virtualDeleteProperty(m, id);
    if (result && id.isArrayIndex())
        args->removeMapping(id.asArrayIndex());
    return result;
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4argumentsobject.cpp, line 171, as _ZN3QV415ArgumentsObject21virtualGetOwnPropertyEPKNS_7ManagedENS_11PropertyKeyEPNS_8PropertyE
namespace QV4 {
inline PropertyAttributes ArgumentsObject::virtualGetOwnProperty(const Managed *m, PropertyKey id, Property *p)
{
    if (!id.isArrayIndex())
        return Object::virtualGetOwnProperty(m, id, p);

    const ArgumentsObject *args = static_cast<const ArgumentsObject *>(m);
    uint index = id.asArrayIndex();
    if (index < args->d()->argCount && !args->d()->fullyCreated) {
        p->value = args->context()->args()[index];
        return Attr_Data;
    }

    PropertyAttributes attrs = Object::virtualGetOwnProperty(m, id, p);
    if (attrs.isEmpty() || !args->isMapped(index))
        return attrs;

    Q_ASSERT(index < static_cast<uint>(args->context()->function->formalParameterCount()));
    if (p)
        p->value = args->context()->args()[index];
    return attrs;
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4argumentsobject.cpp, line 193, as _ZN3QV415ArgumentsObject16virtualGetLengthEPKNS_7ManagedE
namespace QV4 {
inline qint64 ArgumentsObject::virtualGetLength(const Managed *m)
{
    const ArgumentsObject *a = static_cast<const ArgumentsObject *>(m);
    return a->propertyData(Heap::ArgumentsObject::LengthPropertyIndex)->toLength();
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4argumentsobject.cpp, line 199, as _ZN3QV415ArgumentsObject22virtualOwnPropertyKeysEPKNS_6ObjectEPNS_5ValueE
namespace QV4 {
inline OwnPropertyKeyIterator *ArgumentsObject::virtualOwnPropertyKeys(const Object *m, Value *target)
{
    static_cast<ArgumentsObject *>(const_cast<Object *>(m))->fullyCreate();
    return Object::virtualOwnPropertyKeys(m, target);
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4argumentsobject.cpp, line 68, as _ZN3QV415ArgumentsObject11fullyCreateEv
namespace QV4 {
inline void ArgumentsObject::fullyCreate()
{
    if (d()->fullyCreated)
        return;

    Scope scope(engine());

    arrayReserve(d()->argCount);
    arrayPut(0, context()->args(), d()->argCount);
    // Use a sparse array, so that method_getElement() doesn't shortcut
    initSparseArray();

    d()->fullyCreated = true;
}
}  // namespace QV4
//  -----------------------------------------------------------------------

//  void QV4::ArgumentsObject::__dataTest()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV415ArgumentsObject10__dataTestEv(
    QV4::ArgumentsObject *self) {
  self->__dataTest();
}

//  QV4::Heap::ArgumentsObject *QV4::ArgumentsObject::d_unchecked() const
extern "C" Q_DECL_EXPORT
QV4::Heap::ArgumentsObject *ritual_ZNK3QV415ArgumentsObject11d_uncheckedEv(
    const QV4::ArgumentsObject *self) {
  return self->d_unchecked();
}

//  QV4::Heap::ArgumentsObject *QV4::ArgumentsObject::d() const
extern "C" Q_DECL_EXPORT
QV4::Heap::ArgumentsObject *ritual_ZNK3QV415ArgumentsObject1dEv(
    const QV4::ArgumentsObject *self) {
  return self->d();
}

//  Heap::CallContext *QV4::ArgumentsObject::context() const
extern "C" Q_DECL_EXPORT
QV4::Heap::CallContext *ritual_ZNK3QV415ArgumentsObject7contextEv(
    const QV4::ArgumentsObject *self) {
  return self->context();
}

//  bool QV4::ArgumentsObject::fullyCreated() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV415ArgumentsObject12fullyCreatedEv(
    const QV4::ArgumentsObject *self) {
  return self->fullyCreated();
}

//  bool QV4::ArgumentsObject::virtualDefineOwnProperty(Managed *m,
//      PropertyKey id, const Property *desc, PropertyAttributes attrs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV415ArgumentsObject24virtualDefineOwnPropertyEPNS_7ManagedENS_11PropertyKeyEPKNS_8PropertyENS_18PropertyAttributesE(
    QV4::Managed *m,
    const QV4::PropertyKey *id,
    const QV4::Property *desc,
    const QV4::PropertyAttributes *attrs) {
  return QV4::ArgumentsObject::virtualDefineOwnProperty(
      m,
      *id,
      desc,
      *attrs);
}

//  ReturnedValue QV4::ArgumentsObject::virtualGet(const Managed *m,
//      PropertyKey id, const Value *receiver, bool *hasProperty)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV415ArgumentsObject10virtualGetEPKNS_7ManagedENS_11PropertyKeyEPKNS_5ValueEPb(
    const QV4::Managed *m,
    const QV4::PropertyKey *id,
    const QV4::Value *receiver,
    bool *hasProperty) {
  return QV4::ArgumentsObject::virtualGet(m, *id, receiver, hasProperty);
}

//  bool QV4::ArgumentsObject::virtualPut(Managed *m, PropertyKey id, const
//      Value &value, Value *receiver)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV415ArgumentsObject10virtualPutEPNS_7ManagedENS_11PropertyKeyERKNS_5ValueEPS4_(
    QV4::Managed *m,
    const QV4::PropertyKey *id,
    const QV4::Value *value,
    QV4::Value *receiver) {
  return QV4::ArgumentsObject::virtualPut(m, *id, *value, receiver);
}

//  bool QV4::ArgumentsObject::virtualDeleteProperty(Managed *m, PropertyKey
//      id)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV415ArgumentsObject21virtualDeletePropertyEPNS_7ManagedENS_11PropertyKeyE(
    QV4::Managed *m,
    const QV4::PropertyKey *id) {
  return QV4::ArgumentsObject::virtualDeleteProperty(m, *id);
}

//  PropertyAttributes QV4::ArgumentsObject::virtualGetOwnProperty(const
//      Managed *m, PropertyKey id, Property *p)
extern "C" Q_DECL_EXPORT
QV4::PropertyAttributes *ritual_ZN3QV415ArgumentsObject21virtualGetOwnPropertyEPKNS_7ManagedENS_11PropertyKeyEPNS_8PropertyE(
    const QV4::Managed *m,
    const QV4::PropertyKey *id,
    QV4::Property *p) {
  return new QV4::PropertyAttributes(
      QV4::ArgumentsObject::virtualGetOwnProperty(
          m,
          *id,
          p));
}

//  qint64 QV4::ArgumentsObject::virtualGetLength(const Managed *m)
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN3QV415ArgumentsObject16virtualGetLengthEPKNS_7ManagedE(
    const QV4::Managed *m) {
  return QV4::ArgumentsObject::virtualGetLength(m);
}

//  OwnPropertyKeyIterator
//      *QV4::ArgumentsObject::virtualOwnPropertyKeys(const Object *m, Value
//      *target)
extern "C" Q_DECL_EXPORT
QV4::OwnPropertyKeyIterator *ritual_ZN3QV415ArgumentsObject22virtualOwnPropertyKeysEPKNS_6ObjectEPNS_5ValueE(
    const QV4::Object *m,
    QV4::Value *target) {
  return QV4::ArgumentsObject::virtualOwnPropertyKeys(m, target);
}

//  void QV4::ArgumentsObject::fullyCreate()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV415ArgumentsObject11fullyCreateEv(
    QV4::ArgumentsObject *self) {
  self->fullyCreate();
}

//  bool QV4::ArgumentsObject::isMapped(uint arg) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV415ArgumentsObject8isMappedEj(
    const QV4::ArgumentsObject *self,
    uint arg) {
  return self->isMapped(arg);
}

//  void QV4::ArgumentsObject::removeMapping(uint arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV415ArgumentsObject13removeMappingEj(
    QV4::ArgumentsObject *self,
    uint arg) {
  self->removeMapping(arg);
}
