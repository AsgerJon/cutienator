//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4lookup_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4lookup_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4value_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4propertykey_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  ReturnedValue QV4::Lookup::resolveGetter(ExecutionEngine *engine, const
//      Object *object)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV46Lookup13resolveGetterEPNS_15ExecutionEngineEPKNS_6ObjectE(
    QV4::Lookup *self,
    QV4::ExecutionEngine *engine,
    const QV4::Object *object) {
  return self->resolveGetter(engine, object);
}

//  ReturnedValue QV4::Lookup::resolvePrimitiveGetter(ExecutionEngine
//      *engine, const Value &object)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV46Lookup22resolvePrimitiveGetterEPNS_15ExecutionEngineERKNS_5ValueE(
    QV4::Lookup *self,
    QV4::ExecutionEngine *engine,
    const QV4::Value *object) {
  return self->resolvePrimitiveGetter(engine, *object);
}

//  ReturnedValue QV4::Lookup::resolveGlobalGetter(ExecutionEngine *engine)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV46Lookup19resolveGlobalGetterEPNS_15ExecutionEngineE(
    QV4::Lookup *self,
    QV4::ExecutionEngine *engine) {
  return self->resolveGlobalGetter(engine);
}

//  void QV4::Lookup::resolveProtoGetter(PropertyKey name, const Heap::Object
//      *proto)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV46Lookup18resolveProtoGetterENS_11PropertyKeyEPKNS_4Heap6ObjectE(
    QV4::Lookup *self,
    const QV4::PropertyKey *name,
    const QV4::Heap::Object *proto) {
  self->resolveProtoGetter(*name, proto);
}

//  ReturnedValue QV4::Lookup::getterGeneric(Lookup *lookup, ExecutionEngine
//      *engine, const Value &object)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV46Lookup13getterGenericEPS0_PNS_15ExecutionEngineERKNS_5ValueE(
    QV4::Lookup *lookup,
    QV4::ExecutionEngine *engine,
    const QV4::Value *object) {
  return QV4::Lookup::getterGeneric(lookup, engine, *object);
}

//  ReturnedValue QV4::Lookup::getterTwoClasses(Lookup *lookup,
//      ExecutionEngine *engine, const Value &object)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV46Lookup16getterTwoClassesEPS0_PNS_15ExecutionEngineERKNS_5ValueE(
    QV4::Lookup *lookup,
    QV4::ExecutionEngine *engine,
    const QV4::Value *object) {
  return QV4::Lookup::getterTwoClasses(lookup, engine, *object);
}

//  ReturnedValue QV4::Lookup::getterFallback(Lookup *lookup, ExecutionEngine
//      *engine, const Value &object)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV46Lookup14getterFallbackEPS0_PNS_15ExecutionEngineERKNS_5ValueE(
    QV4::Lookup *lookup,
    QV4::ExecutionEngine *engine,
    const QV4::Value *object) {
  return QV4::Lookup::getterFallback(lookup, engine, *object);
}

//  ReturnedValue QV4::Lookup::getter0MemberData(Lookup *lookup,
//      ExecutionEngine *engine, const Value &object)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV46Lookup17getter0MemberDataEPS0_PNS_15ExecutionEngineERKNS_5ValueE(
    QV4::Lookup *lookup,
    QV4::ExecutionEngine *engine,
    const QV4::Value *object) {
  return QV4::Lookup::getter0MemberData(lookup, engine, *object);
}

//  ReturnedValue QV4::Lookup::getter0Inline(Lookup *lookup, ExecutionEngine
//      *engine, const Value &object)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV46Lookup13getter0InlineEPS0_PNS_15ExecutionEngineERKNS_5ValueE(
    QV4::Lookup *lookup,
    QV4::ExecutionEngine *engine,
    const QV4::Value *object) {
  return QV4::Lookup::getter0Inline(lookup, engine, *object);
}

//  ReturnedValue QV4::Lookup::getterProto(Lookup *lookup, ExecutionEngine
//      *engine, const Value &object)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV46Lookup11getterProtoEPS0_PNS_15ExecutionEngineERKNS_5ValueE(
    QV4::Lookup *lookup,
    QV4::ExecutionEngine *engine,
    const QV4::Value *object) {
  return QV4::Lookup::getterProto(lookup, engine, *object);
}

//  ReturnedValue QV4::Lookup::getter0Inlinegetter0Inline(Lookup *lookup,
//      ExecutionEngine *engine, const Value &object)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV46Lookup26getter0Inlinegetter0InlineEPS0_PNS_15ExecutionEngineERKNS_5ValueE(
    QV4::Lookup *lookup,
    QV4::ExecutionEngine *engine,
    const QV4::Value *object) {
  return QV4::Lookup::getter0Inlinegetter0Inline(lookup, engine, *object);
}

//  ReturnedValue QV4::Lookup::getter0Inlinegetter0MemberData(Lookup *lookup,
//      ExecutionEngine *engine, const Value &object)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV46Lookup30getter0Inlinegetter0MemberDataEPS0_PNS_15ExecutionEngineERKNS_5ValueE(
    QV4::Lookup *lookup,
    QV4::ExecutionEngine *engine,
    const QV4::Value *object) {
  return QV4::Lookup::getter0Inlinegetter0MemberData(
      lookup,
      engine,
      *object);
}

//  ReturnedValue QV4::Lookup::getter0MemberDatagetter0MemberData(Lookup
//      *lookup, ExecutionEngine *engine, const Value &object)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV46Lookup34getter0MemberDatagetter0MemberDataEPS0_PNS_15ExecutionEngineERKNS_5ValueE(
    QV4::Lookup *lookup,
    QV4::ExecutionEngine *engine,
    const QV4::Value *object) {
  return QV4::Lookup::getter0MemberDatagetter0MemberData(
      lookup,
      engine,
      *object);
}

//  ReturnedValue QV4::Lookup::getterProtoTwoClasses(Lookup *lookup,
//      ExecutionEngine *engine, const Value &object)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV46Lookup21getterProtoTwoClassesEPS0_PNS_15ExecutionEngineERKNS_5ValueE(
    QV4::Lookup *lookup,
    QV4::ExecutionEngine *engine,
    const QV4::Value *object) {
  return QV4::Lookup::getterProtoTwoClasses(lookup, engine, *object);
}

//  ReturnedValue QV4::Lookup::getterAccessor(Lookup *lookup, ExecutionEngine
//      *engine, const Value &object)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV46Lookup14getterAccessorEPS0_PNS_15ExecutionEngineERKNS_5ValueE(
    QV4::Lookup *lookup,
    QV4::ExecutionEngine *engine,
    const QV4::Value *object) {
  return QV4::Lookup::getterAccessor(lookup, engine, *object);
}

//  ReturnedValue QV4::Lookup::getterProtoAccessor(Lookup *lookup,
//      ExecutionEngine *engine, const Value &object)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV46Lookup19getterProtoAccessorEPS0_PNS_15ExecutionEngineERKNS_5ValueE(
    QV4::Lookup *lookup,
    QV4::ExecutionEngine *engine,
    const QV4::Value *object) {
  return QV4::Lookup::getterProtoAccessor(lookup, engine, *object);
}

//  ReturnedValue QV4::Lookup::getterProtoAccessorTwoClasses(Lookup *lookup,
//      ExecutionEngine *engine, const Value &object)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV46Lookup29getterProtoAccessorTwoClassesEPS0_PNS_15ExecutionEngineERKNS_5ValueE(
    QV4::Lookup *lookup,
    QV4::ExecutionEngine *engine,
    const QV4::Value *object) {
  return QV4::Lookup::getterProtoAccessorTwoClasses(lookup, engine, *object);
}

//  ReturnedValue QV4::Lookup::getterIndexed(Lookup *lookup, ExecutionEngine
//      *engine, const Value &object)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV46Lookup13getterIndexedEPS0_PNS_15ExecutionEngineERKNS_5ValueE(
    QV4::Lookup *lookup,
    QV4::ExecutionEngine *engine,
    const QV4::Value *object) {
  return QV4::Lookup::getterIndexed(lookup, engine, *object);
}

//  ReturnedValue QV4::Lookup::getterQObject(Lookup *lookup, ExecutionEngine
//      *engine, const Value &object)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV46Lookup13getterQObjectEPS0_PNS_15ExecutionEngineERKNS_5ValueE(
    QV4::Lookup *lookup,
    QV4::ExecutionEngine *engine,
    const QV4::Value *object) {
  return QV4::Lookup::getterQObject(lookup, engine, *object);
}

//  ReturnedValue QV4::Lookup::getterQObjectMethod(Lookup *lookup,
//      ExecutionEngine *engine, const Value &object)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV46Lookup19getterQObjectMethodEPS0_PNS_15ExecutionEngineERKNS_5ValueE(
    QV4::Lookup *lookup,
    QV4::ExecutionEngine *engine,
    const QV4::Value *object) {
  return QV4::Lookup::getterQObjectMethod(lookup, engine, *object);
}

//  ReturnedValue QV4::Lookup::getterFallbackMethod(Lookup *lookup,
//      ExecutionEngine *engine, const Value &object)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV46Lookup20getterFallbackMethodEPS0_PNS_15ExecutionEngineERKNS_5ValueE(
    QV4::Lookup *lookup,
    QV4::ExecutionEngine *engine,
    const QV4::Value *object) {
  return QV4::Lookup::getterFallbackMethod(lookup, engine, *object);
}

//  ReturnedValue QV4::Lookup::getterValueType(Lookup *lookup,
//      ExecutionEngine *engine, const Value &object)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV46Lookup15getterValueTypeEPS0_PNS_15ExecutionEngineERKNS_5ValueE(
    QV4::Lookup *lookup,
    QV4::ExecutionEngine *engine,
    const QV4::Value *object) {
  return QV4::Lookup::getterValueType(lookup, engine, *object);
}

//  ReturnedValue QV4::Lookup::primitiveGetterProto(Lookup *lookup,
//      ExecutionEngine *engine, const Value &object)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV46Lookup20primitiveGetterProtoEPS0_PNS_15ExecutionEngineERKNS_5ValueE(
    QV4::Lookup *lookup,
    QV4::ExecutionEngine *engine,
    const QV4::Value *object) {
  return QV4::Lookup::primitiveGetterProto(lookup, engine, *object);
}

//  ReturnedValue QV4::Lookup::primitiveGetterAccessor(Lookup *lookup,
//      ExecutionEngine *engine, const Value &object)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV46Lookup23primitiveGetterAccessorEPS0_PNS_15ExecutionEngineERKNS_5ValueE(
    QV4::Lookup *lookup,
    QV4::ExecutionEngine *engine,
    const QV4::Value *object) {
  return QV4::Lookup::primitiveGetterAccessor(lookup, engine, *object);
}

//  ReturnedValue QV4::Lookup::stringLengthGetter(Lookup *lookup,
//      ExecutionEngine *engine, const Value &object)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV46Lookup18stringLengthGetterEPS0_PNS_15ExecutionEngineERKNS_5ValueE(
    QV4::Lookup *lookup,
    QV4::ExecutionEngine *engine,
    const QV4::Value *object) {
  return QV4::Lookup::stringLengthGetter(lookup, engine, *object);
}

//  ReturnedValue QV4::Lookup::globalGetterGeneric(Lookup *lookup,
//      ExecutionEngine *engine)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV46Lookup19globalGetterGenericEPS0_PNS_15ExecutionEngineE(
    QV4::Lookup *lookup,
    QV4::ExecutionEngine *engine) {
  return QV4::Lookup::globalGetterGeneric(lookup, engine);
}

//  ReturnedValue QV4::Lookup::globalGetterProto(Lookup *lookup,
//      ExecutionEngine *engine)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV46Lookup17globalGetterProtoEPS0_PNS_15ExecutionEngineE(
    QV4::Lookup *lookup,
    QV4::ExecutionEngine *engine) {
  return QV4::Lookup::globalGetterProto(lookup, engine);
}

//  ReturnedValue QV4::Lookup::globalGetterProtoAccessor(Lookup *lookup,
//      ExecutionEngine *engine)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV46Lookup25globalGetterProtoAccessorEPS0_PNS_15ExecutionEngineE(
    QV4::Lookup *lookup,
    QV4::ExecutionEngine *engine) {
  return QV4::Lookup::globalGetterProtoAccessor(lookup, engine);
}

//  bool QV4::Lookup::resolveSetter(ExecutionEngine *engine, Object *object,
//      const Value &value)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV46Lookup13resolveSetterEPNS_15ExecutionEngineEPNS_6ObjectERKNS_5ValueE(
    QV4::Lookup *self,
    QV4::ExecutionEngine *engine,
    QV4::Object *object,
    const QV4::Value *value) {
  return self->resolveSetter(engine, object, *value);
}

//  bool QV4::Lookup::setterGeneric(Lookup *lookup, ExecutionEngine *engine,
//      Value &object, const Value &value)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV46Lookup13setterGenericEPS0_PNS_15ExecutionEngineERNS_5ValueERKS4_(
    QV4::Lookup *lookup,
    QV4::ExecutionEngine *engine,
    QV4::Value *object,
    const QV4::Value *value) {
  return QV4::Lookup::setterGeneric(lookup, engine, *object, *value);
}

//  bool QV4::Lookup::setterTwoClasses(Lookup *lookup, ExecutionEngine
//      *engine, Value &object, const Value &value)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV46Lookup16setterTwoClassesEPS0_PNS_15ExecutionEngineERNS_5ValueERKS4_(
    QV4::Lookup *lookup,
    QV4::ExecutionEngine *engine,
    QV4::Value *object,
    const QV4::Value *value) {
  return QV4::Lookup::setterTwoClasses(lookup, engine, *object, *value);
}

//  bool QV4::Lookup::setterFallback(Lookup *lookup, ExecutionEngine *engine,
//      Value &object, const Value &value)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV46Lookup14setterFallbackEPS0_PNS_15ExecutionEngineERNS_5ValueERKS4_(
    QV4::Lookup *lookup,
    QV4::ExecutionEngine *engine,
    QV4::Value *object,
    const QV4::Value *value) {
  return QV4::Lookup::setterFallback(lookup, engine, *object, *value);
}

//  bool QV4::Lookup::setter0MemberData(Lookup *lookup, ExecutionEngine
//      *engine, Value &object, const Value &value)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV46Lookup17setter0MemberDataEPS0_PNS_15ExecutionEngineERNS_5ValueERKS4_(
    QV4::Lookup *lookup,
    QV4::ExecutionEngine *engine,
    QV4::Value *object,
    const QV4::Value *value) {
  return QV4::Lookup::setter0MemberData(lookup, engine, *object, *value);
}

//  bool QV4::Lookup::setter0Inline(Lookup *lookup, ExecutionEngine *engine,
//      Value &object, const Value &value)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV46Lookup13setter0InlineEPS0_PNS_15ExecutionEngineERNS_5ValueERKS4_(
    QV4::Lookup *lookup,
    QV4::ExecutionEngine *engine,
    QV4::Value *object,
    const QV4::Value *value) {
  return QV4::Lookup::setter0Inline(lookup, engine, *object, *value);
}

//  bool QV4::Lookup::setter0setter0(Lookup *lookup, ExecutionEngine *engine,
//      Value &object, const Value &value)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV46Lookup14setter0setter0EPS0_PNS_15ExecutionEngineERNS_5ValueERKS4_(
    QV4::Lookup *lookup,
    QV4::ExecutionEngine *engine,
    QV4::Value *object,
    const QV4::Value *value) {
  return QV4::Lookup::setter0setter0(lookup, engine, *object, *value);
}

//  bool QV4::Lookup::setterInsert(Lookup *lookup, ExecutionEngine *engine,
//      Value &object, const Value &value)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV46Lookup12setterInsertEPS0_PNS_15ExecutionEngineERNS_5ValueERKS4_(
    QV4::Lookup *lookup,
    QV4::ExecutionEngine *engine,
    QV4::Value *object,
    const QV4::Value *value) {
  return QV4::Lookup::setterInsert(lookup, engine, *object, *value);
}

//  bool QV4::Lookup::setterQObject(Lookup *lookup, ExecutionEngine *engine,
//      Value &object, const Value &value)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV46Lookup13setterQObjectEPS0_PNS_15ExecutionEngineERNS_5ValueERKS4_(
    QV4::Lookup *lookup,
    QV4::ExecutionEngine *engine,
    QV4::Value *object,
    const QV4::Value *value) {
  return QV4::Lookup::setterQObject(lookup, engine, *object, *value);
}

//  bool QV4::Lookup::arrayLengthSetter(Lookup *lookup, ExecutionEngine
//      *engine, Value &object, const Value &value)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV46Lookup17arrayLengthSetterEPS0_PNS_15ExecutionEngineERNS_5ValueERKS4_(
    QV4::Lookup *lookup,
    QV4::ExecutionEngine *engine,
    QV4::Value *object,
    const QV4::Value *value) {
  return QV4::Lookup::arrayLengthSetter(lookup, engine, *object, *value);
}

//  void QV4::Lookup::markObjects(MarkStack *stack)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV46Lookup11markObjectsEPNS_9MarkStackE(
    QV4::Lookup *self,
    QV4::MarkStack *stack) {
  self->markObjects(stack);
}

//  ReturnedValue QV4::Lookup::contextGetter(ExecutionEngine *engine, Value
//      *base)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV46Lookup13contextGetterEPNS_15ExecutionEngineEPNS_5ValueE(
    QV4::Lookup *self,
    QV4::ExecutionEngine *engine,
    QV4::Value *base) {
  return self->contextGetter(engine, base);
}

//  ReturnedValue QV4::Lookup::doCallGlobal(Call call, Lookup *lookup,
//      ExecutionEngine *engine)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV46Lookup12doCallGlobalENS0_4CallEPS0_PNS_15ExecutionEngineE(
    QV4::Lookup::Call call,
    QV4::Lookup *lookup,
    QV4::ExecutionEngine *engine) {
  return QV4::Lookup::doCallGlobal(call, lookup, engine);
}

//  ReturnedValue QV4::Lookup::globalGetter(ExecutionEngine *engine)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV46Lookup12globalGetterEPNS_15ExecutionEngineE(
    QV4::Lookup *self,
    QV4::ExecutionEngine *engine) {
  return self->globalGetter(engine);
}

//  ReturnedValue QV4::Lookup::getter(ExecutionEngine *engine, const Value
//      &object)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV46Lookup6getterEPNS_15ExecutionEngineERKNS_5ValueE(
    QV4::Lookup *self,
    QV4::ExecutionEngine *engine,
    const QV4::Value *object) {
  return self->getter(engine, *object);
}

//  bool QV4::Lookup::setter(ExecutionEngine *engine, Value &object, const
//      Value &value)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV46Lookup6setterEPNS_15ExecutionEngineERNS_5ValueERKS3_(
    QV4::Lookup *self,
    QV4::ExecutionEngine *engine,
    QV4::Value *object,
    const QV4::Value *value) {
  return self->setter(engine, *object, *value);
}

//  void QV4::Lookup::releasePropertyCache()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV46Lookup20releasePropertyCacheEv(QV4::Lookup *self) {
  self->releasePropertyCache();
}

//  QV4::Lookup::~Lookup()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV46LookupD1Ev(QV4::Lookup *self) {
  delete self;
}
