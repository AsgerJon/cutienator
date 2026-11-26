//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmltypewrapper_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmltypewrapper_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmltype_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4value_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4propertykey_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4global_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qqmltypewrapper_p.h>
#include <QtQml/private/qjsvalue_p.h>
#include <QtQml/private/qqmlcontext_p.h>
#include <QtQml/private/qqmlengine_p.h>
#include <QtQml/private/qqmlmetaobject_p.h>
#include <QtQml/private/qqmltypedata_p.h>
#include <QtQml/private/qqmlvaluetypewrapper_p.h>
#include <QtQml/private/qv4dateobject_p.h>
#include <QtQml/private/qv4identifiertable_p.h>
#include <QtQml/private/qv4lookup_p.h>
#include <QtQml/private/qv4objectproto_p.h>
#include <QtQml/private/qv4qobjectwrapper_p.h>
#include <QtQml/private/qv4symbol_p.h>
#include <QtQml/private/qv4urlobject_p.h>
#include <QtQml/private/qv4variantobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/qml/qqmltypewrapper.cpp, line 55, as _ZN3QV44Heap15QQmlTypeWrapper7destroyEv
namespace QV4 {
inline void Heap::QQmlTypeWrapper::destroy()
{
    switch (kind()) {
    case Type:
        Q_ASSERT(t.typePrivate);
        QQmlType::derefHandle(t.typePrivate);
        delete[] t.constructors;
        break;
    case Namespace:
        Q_ASSERT(n.typeNamespace);
        n.typeNamespace->release();
        break;
    }

    object.destroy();
    FunctionObject::destroy();
}
}  // namespace QV4
//  -----------------------------------------------------------------------

//  const QV4::VTable *QV4::QQmlTypeWrapper::staticVTable()
extern "C" Q_DECL_EXPORT
const QV4::VTable *ritual_ZN3QV415QQmlTypeWrapper12staticVTableEv() {
  return QV4::QQmlTypeWrapper::staticVTable();
}

//  void QV4::QQmlTypeWrapper::__dataTest()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV415QQmlTypeWrapper10__dataTestEv(
    QV4::QQmlTypeWrapper *self) {
  self->__dataTest();
}

//  QV4::Heap::QQmlTypeWrapper *QV4::QQmlTypeWrapper::d_unchecked() const
extern "C" Q_DECL_EXPORT
QV4::Heap::QQmlTypeWrapper *ritual_ZNK3QV415QQmlTypeWrapper11d_uncheckedEv(
    const QV4::QQmlTypeWrapper *self) {
  return self->d_unchecked();
}

//  QV4::Heap::QQmlTypeWrapper *QV4::QQmlTypeWrapper::d() const
extern "C" Q_DECL_EXPORT
QV4::Heap::QQmlTypeWrapper *ritual_ZNK3QV415QQmlTypeWrapper1dEv(
    const QV4::QQmlTypeWrapper *self) {
  return self->d();
}

//  QV4::Object *QV4::QQmlTypeWrapper::defaultPrototype(QV4::ExecutionEngine
//      *e)
extern "C" Q_DECL_EXPORT
QV4::Object *ritual_ZN3QV415QQmlTypeWrapper16defaultPrototypeEPNS_15ExecutionEngineE(
    QV4::ExecutionEngine *e) {
  return QV4::QQmlTypeWrapper::defaultPrototype(e);
}

//  void QV4::QQmlTypeWrapper::virtualDestroy(QV4::Heap::Base *b)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV415QQmlTypeWrapper14virtualDestroyEPNS_4Heap4BaseE(
    QV4::Heap::Base *b) {
  QV4::QQmlTypeWrapper::virtualDestroy(b);
}

//  bool QV4::QQmlTypeWrapper::isSingleton() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV415QQmlTypeWrapper11isSingletonEv(
    const QV4::QQmlTypeWrapper *self) {
  return self->isSingleton();
}

//  const QMetaObject *QV4::QQmlTypeWrapper::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK3QV415QQmlTypeWrapper10metaObjectEv(
    const QV4::QQmlTypeWrapper *self) {
  return self->metaObject();
}

//  QObject *QV4::QQmlTypeWrapper::object() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK3QV415QQmlTypeWrapper6objectEv(
    const QV4::QQmlTypeWrapper *self) {
  return self->object();
}

//  QObject *QV4::QQmlTypeWrapper::singletonObject() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK3QV415QQmlTypeWrapper15singletonObjectEv(
    const QV4::QQmlTypeWrapper *self) {
  return self->singletonObject();
}

//  QVariant QV4::QQmlTypeWrapper::toVariant() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK3QV415QQmlTypeWrapper9toVariantEv(
    const QV4::QQmlTypeWrapper *self) {
  return new QVariant(self->toVariant());
}

//  void QV4::QQmlTypeWrapper::initProto(ExecutionEngine *v4)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV415QQmlTypeWrapper9initProtoEPNS_15ExecutionEngineE(
    QV4::ExecutionEngine *v4) {
  QV4::QQmlTypeWrapper::initProto(v4);
}

//  ReturnedValue QV4::QQmlTypeWrapper::create(ExecutionEngine *a0, QObject
//      *a1, const QQmlType &a2, Heap::QQmlTypeWrapper::TypeNameMode a3)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV415QQmlTypeWrapper6createEPNS_15ExecutionEngineEP7QObjectRK8QQmlTypeNS_4Heap15QQmlTypeWrapper12TypeNameModeE(
    QV4::ExecutionEngine *a0,
    QObject *a1,
    const QQmlType *a2,
    QV4::Heap::QQmlTypeWrapper::TypeNameMode a3) {
  return QV4::QQmlTypeWrapper::create(a0, a1, *a2, a3);
}

//  ReturnedValue QV4::QQmlTypeWrapper::create(ExecutionEngine *a0, QObject
//      *a1, const QQmlRefPointer<QQmlTypeNameCache> &a2, const QQmlImportRef
//      *a3, Heap::QQmlTypeWrapper::TypeNameMode a4)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV415QQmlTypeWrapper6createEPNS_15ExecutionEngineEP7QObjectRK14QQmlRefPointerI17QQmlTypeNameCacheEPK13QQmlImportRefNS_4Heap15QQmlTypeWrapper12TypeNameModeE(
    QV4::ExecutionEngine *a0,
    QObject *a1,
    const QQmlRefPointer<QQmlTypeNameCache> *a2,
    const QQmlImportRef *a3,
    QV4::Heap::QQmlTypeWrapper::TypeNameMode a4) {
  return QV4::QQmlTypeWrapper::create(a0, a1, *a2, a3, a4);
}

//  ReturnedValue QV4::QQmlTypeWrapper::virtualResolveLookupGetter(const
//      Object *object, ExecutionEngine *engine, Lookup *lookup)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV415QQmlTypeWrapper26virtualResolveLookupGetterEPKNS_6ObjectEPNS_15ExecutionEngineEPNS_6LookupE(
    const QV4::Object *object,
    QV4::ExecutionEngine *engine,
    QV4::Lookup *lookup) {
  return QV4::QQmlTypeWrapper::virtualResolveLookupGetter(
      object,
      engine,
      lookup);
}

//  bool QV4::QQmlTypeWrapper::virtualResolveLookupSetter(Object *object,
//      ExecutionEngine *engine, Lookup *lookup, const Value &value)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV415QQmlTypeWrapper26virtualResolveLookupSetterEPNS_6ObjectEPNS_15ExecutionEngineEPNS_6LookupERKNS_5ValueE(
    QV4::Object *object,
    QV4::ExecutionEngine *engine,
    QV4::Lookup *lookup,
    const QV4::Value *value) {
  return QV4::QQmlTypeWrapper::virtualResolveLookupSetter(
      object,
      engine,
      lookup,
      *value);
}

//  OwnPropertyKeyIterator
//      *QV4::QQmlTypeWrapper::virtualOwnPropertyKeys(const Object *m, Value
//      *target)
extern "C" Q_DECL_EXPORT
QV4::OwnPropertyKeyIterator *ritual_ZN3QV415QQmlTypeWrapper22virtualOwnPropertyKeysEPKNS_6ObjectEPNS_5ValueE(
    const QV4::Object *m,
    QV4::Value *target) {
  return QV4::QQmlTypeWrapper::virtualOwnPropertyKeys(m, target);
}

//  int QV4::QQmlTypeWrapper::virtualMetacall(Object *object,
//      QMetaObject::Call call, int index, void **a)
extern "C" Q_DECL_EXPORT
int ritual_ZN3QV415QQmlTypeWrapper15virtualMetacallEPNS_6ObjectEN11QMetaObject4CallEiPPv(
    QV4::Object *object,
    QMetaObject::Call call,
    int index,
    void **a) {
  return QV4::QQmlTypeWrapper::virtualMetacall(object, call, index, a);
}

//  ReturnedValue QV4::QQmlTypeWrapper::lookupSingletonProperty(Lookup *l,
//      ExecutionEngine *engine, const Value &base)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV415QQmlTypeWrapper23lookupSingletonPropertyEPNS_6LookupEPNS_15ExecutionEngineERKNS_5ValueE(
    QV4::Lookup *l,
    QV4::ExecutionEngine *engine,
    const QV4::Value *base) {
  return QV4::QQmlTypeWrapper::lookupSingletonProperty(l, engine, *base);
}

//  ReturnedValue QV4::QQmlTypeWrapper::lookupSingletonMethod(Lookup *l,
//      ExecutionEngine *engine, const Value &base)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV415QQmlTypeWrapper21lookupSingletonMethodEPNS_6LookupEPNS_15ExecutionEngineERKNS_5ValueE(
    QV4::Lookup *l,
    QV4::ExecutionEngine *engine,
    const QV4::Value *base) {
  return QV4::QQmlTypeWrapper::lookupSingletonMethod(l, engine, *base);
}

//  ReturnedValue QV4::QQmlTypeWrapper::lookupEnumValue(Lookup *l,
//      ExecutionEngine *engine, const Value &base)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV415QQmlTypeWrapper15lookupEnumValueEPNS_6LookupEPNS_15ExecutionEngineERKNS_5ValueE(
    QV4::Lookup *l,
    QV4::ExecutionEngine *engine,
    const QV4::Value *base) {
  return QV4::QQmlTypeWrapper::lookupEnumValue(l, engine, *base);
}

//  ReturnedValue QV4::QQmlTypeWrapper::lookupEnum(Lookup *l, ExecutionEngine
//      *engine, const Value &base)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV415QQmlTypeWrapper10lookupEnumEPNS_6LookupEPNS_15ExecutionEngineERKNS_5ValueE(
    QV4::Lookup *l,
    QV4::ExecutionEngine *engine,
    const QV4::Value *base) {
  return QV4::QQmlTypeWrapper::lookupEnum(l, engine, *base);
}

//  ReturnedValue QV4::QQmlTypeWrapper::virtualGet(const Managed *m,
//      PropertyKey id, const Value *receiver, bool *hasProperty)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV415QQmlTypeWrapper10virtualGetEPKNS_7ManagedENS_11PropertyKeyEPKNS_5ValueEPb(
    const QV4::Managed *m,
    const QV4::PropertyKey *id,
    const QV4::Value *receiver,
    bool *hasProperty) {
  return QV4::QQmlTypeWrapper::virtualGet(m, *id, receiver, hasProperty);
}

//  bool QV4::QQmlTypeWrapper::virtualPut(Managed *m, PropertyKey id, const
//      Value &value, Value *receiver)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV415QQmlTypeWrapper10virtualPutEPNS_7ManagedENS_11PropertyKeyERKNS_5ValueEPS4_(
    QV4::Managed *m,
    const QV4::PropertyKey *id,
    const QV4::Value *value,
    QV4::Value *receiver) {
  return QV4::QQmlTypeWrapper::virtualPut(m, *id, *value, receiver);
}

//  PropertyAttributes QV4::QQmlTypeWrapper::virtualGetOwnProperty(const
//      Managed *m, PropertyKey id, Property *p)
extern "C" Q_DECL_EXPORT
QV4::PropertyAttributes *ritual_ZN3QV415QQmlTypeWrapper21virtualGetOwnPropertyEPKNS_7ManagedENS_11PropertyKeyEPNS_8PropertyE(
    const QV4::Managed *m,
    const QV4::PropertyKey *id,
    QV4::Property *p) {
  return new QV4::PropertyAttributes(
      QV4::QQmlTypeWrapper::virtualGetOwnProperty(
          m,
          *id,
          p));
}

//  bool QV4::QQmlTypeWrapper::virtualIsEqualTo(Managed *that, Managed *o)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV415QQmlTypeWrapper16virtualIsEqualToEPNS_7ManagedES2_(
    QV4::Managed *that,
    QV4::Managed *o) {
  return QV4::QQmlTypeWrapper::virtualIsEqualTo(that, o);
}

//  ReturnedValue QV4::QQmlTypeWrapper::virtualInstanceOf(const Object
//      *typeObject, const Value &var)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV415QQmlTypeWrapper17virtualInstanceOfEPKNS_6ObjectERKNS_5ValueE(
    const QV4::Object *typeObject,
    const QV4::Value *var) {
  return QV4::QQmlTypeWrapper::virtualInstanceOf(typeObject, *var);
}

//  ReturnedValue QV4::QQmlTypeWrapper::method_hasInstance(const
//      FunctionObject *a0, const Value *thisObject, const Value *argv, int
//      argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV415QQmlTypeWrapper18method_hasInstanceEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::QQmlTypeWrapper::method_hasInstance(
      a0,
      thisObject,
      argv,
      argc);
}

//  ReturnedValue QV4::QQmlTypeWrapper::method_toString(const FunctionObject
//      *b, const Value *thisObject, const Value *a2, int a3)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV415QQmlTypeWrapper15method_toStringEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *b,
    const QV4::Value *thisObject,
    const QV4::Value *a2,
    int a3) {
  return QV4::QQmlTypeWrapper::method_toString(b, thisObject, a2, a3);
}
