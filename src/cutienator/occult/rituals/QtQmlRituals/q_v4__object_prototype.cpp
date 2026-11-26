//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4objectproto_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4objectproto_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4value_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4global_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void QV4::ObjectPrototype::init(ExecutionEngine *engine, Object *ctor)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV415ObjectPrototype4initEPNS_15ExecutionEngineEPNS_6ObjectE(
    QV4::ObjectPrototype *self,
    QV4::ExecutionEngine *engine,
    QV4::Object *ctor) {
  self->init(engine, ctor);
}

//  ReturnedValue QV4::ObjectPrototype::method_assign(const FunctionObject
//      *a0, const Value *thisObject, const Value *argv, int argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV415ObjectPrototype13method_assignEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::ObjectPrototype::method_assign(a0, thisObject, argv, argc);
}

//  ReturnedValue QV4::ObjectPrototype::method_create(const FunctionObject
//      *a0, const Value *thisObject, const Value *argv, int argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV415ObjectPrototype13method_createEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::ObjectPrototype::method_create(a0, thisObject, argv, argc);
}

//  ReturnedValue QV4::ObjectPrototype::method_defineProperties(const
//      FunctionObject *a0, const Value *thisObject, const Value *argv, int
//      argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV415ObjectPrototype23method_definePropertiesEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::ObjectPrototype::method_defineProperties(
      a0,
      thisObject,
      argv,
      argc);
}

//  ReturnedValue QV4::ObjectPrototype::method_defineProperty(const
//      FunctionObject *a0, const Value *thisObject, const Value *argv, int
//      argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV415ObjectPrototype21method_definePropertyEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::ObjectPrototype::method_defineProperty(
      a0,
      thisObject,
      argv,
      argc);
}

//  ReturnedValue QV4::ObjectPrototype::method_entries(const FunctionObject
//      *a0, const Value *thisObject, const Value *argv, int argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV415ObjectPrototype14method_entriesEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::ObjectPrototype::method_entries(a0, thisObject, argv, argc);
}

//  ReturnedValue QV4::ObjectPrototype::method_freeze(const FunctionObject
//      *a0, const Value *thisObject, const Value *argv, int argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV415ObjectPrototype13method_freezeEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::ObjectPrototype::method_freeze(a0, thisObject, argv, argc);
}

//  ReturnedValue QV4::ObjectPrototype::method_getOwnPropertyDescriptor(const
//      FunctionObject *a0, const Value *thisObject, const Value *argv, int
//      argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV415ObjectPrototype31method_getOwnPropertyDescriptorEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::ObjectPrototype::method_getOwnPropertyDescriptor(
      a0,
      thisObject,
      argv,
      argc);
}

//  ReturnedValue
//      QV4::ObjectPrototype::method_getOwnPropertyDescriptors(const
//      FunctionObject *a0, const Value *thisObject, const Value *argv, int
//      argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV415ObjectPrototype32method_getOwnPropertyDescriptorsEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::ObjectPrototype::method_getOwnPropertyDescriptors(
      a0,
      thisObject,
      argv,
      argc);
}

//  ReturnedValue QV4::ObjectPrototype::method_getOwnPropertyNames(const
//      FunctionObject *a0, const Value *thisObject, const Value *argv, int
//      argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV415ObjectPrototype26method_getOwnPropertyNamesEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::ObjectPrototype::method_getOwnPropertyNames(
      a0,
      thisObject,
      argv,
      argc);
}

//  ReturnedValue QV4::ObjectPrototype::method_getOwnPropertySymbols(const
//      FunctionObject *a0, const Value *thisObject, const Value *argv, int
//      argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV415ObjectPrototype28method_getOwnPropertySymbolsEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::ObjectPrototype::method_getOwnPropertySymbols(
      a0,
      thisObject,
      argv,
      argc);
}

//  ReturnedValue QV4::ObjectPrototype::method_getPrototypeOf(const
//      FunctionObject *a0, const Value *thisObject, const Value *argv, int
//      argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV415ObjectPrototype21method_getPrototypeOfEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::ObjectPrototype::method_getPrototypeOf(
      a0,
      thisObject,
      argv,
      argc);
}

//  ReturnedValue QV4::ObjectPrototype::method_is(const FunctionObject *a0,
//      const Value *thisObject, const Value *argv, int argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV415ObjectPrototype9method_isEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::ObjectPrototype::method_is(a0, thisObject, argv, argc);
}

//  ReturnedValue QV4::ObjectPrototype::method_isExtensible(const
//      FunctionObject *a0, const Value *thisObject, const Value *argv, int
//      argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV415ObjectPrototype19method_isExtensibleEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::ObjectPrototype::method_isExtensible(
      a0,
      thisObject,
      argv,
      argc);
}

//  ReturnedValue QV4::ObjectPrototype::method_isFrozen(const FunctionObject
//      *a0, const Value *thisObject, const Value *argv, int argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV415ObjectPrototype15method_isFrozenEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::ObjectPrototype::method_isFrozen(a0, thisObject, argv, argc);
}

//  ReturnedValue QV4::ObjectPrototype::method_isSealed(const FunctionObject
//      *a0, const Value *thisObject, const Value *argv, int argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV415ObjectPrototype15method_isSealedEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::ObjectPrototype::method_isSealed(a0, thisObject, argv, argc);
}

//  ReturnedValue QV4::ObjectPrototype::method_keys(const FunctionObject *a0,
//      const Value *thisObject, const Value *argv, int argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV415ObjectPrototype11method_keysEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::ObjectPrototype::method_keys(a0, thisObject, argv, argc);
}

//  ReturnedValue QV4::ObjectPrototype::method_preventExtensions(const
//      FunctionObject *a0, const Value *thisObject, const Value *argv, int
//      argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV415ObjectPrototype24method_preventExtensionsEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::ObjectPrototype::method_preventExtensions(
      a0,
      thisObject,
      argv,
      argc);
}

//  ReturnedValue QV4::ObjectPrototype::method_seal(const FunctionObject *a0,
//      const Value *thisObject, const Value *argv, int argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV415ObjectPrototype11method_sealEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::ObjectPrototype::method_seal(a0, thisObject, argv, argc);
}

//  ReturnedValue QV4::ObjectPrototype::method_setPrototypeOf(const
//      FunctionObject *a0, const Value *thisObject, const Value *argv, int
//      argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV415ObjectPrototype21method_setPrototypeOfEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::ObjectPrototype::method_setPrototypeOf(
      a0,
      thisObject,
      argv,
      argc);
}

//  ReturnedValue QV4::ObjectPrototype::method_values(const FunctionObject
//      *a0, const Value *thisObject, const Value *argv, int argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV415ObjectPrototype13method_valuesEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::ObjectPrototype::method_values(a0, thisObject, argv, argc);
}

//  ReturnedValue QV4::ObjectPrototype::method_toString(const FunctionObject
//      *a0, const Value *thisObject, const Value *argv, int argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV415ObjectPrototype15method_toStringEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::ObjectPrototype::method_toString(a0, thisObject, argv, argc);
}

//  ReturnedValue QV4::ObjectPrototype::method_toLocaleString(const
//      FunctionObject *a0, const Value *thisObject, const Value *argv, int
//      argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV415ObjectPrototype21method_toLocaleStringEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::ObjectPrototype::method_toLocaleString(
      a0,
      thisObject,
      argv,
      argc);
}

//  ReturnedValue QV4::ObjectPrototype::method_valueOf(const FunctionObject
//      *a0, const Value *thisObject, const Value *argv, int argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV415ObjectPrototype14method_valueOfEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::ObjectPrototype::method_valueOf(a0, thisObject, argv, argc);
}

//  ReturnedValue QV4::ObjectPrototype::method_hasOwnProperty(const
//      FunctionObject *a0, const Value *thisObject, const Value *argv, int
//      argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV415ObjectPrototype21method_hasOwnPropertyEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::ObjectPrototype::method_hasOwnProperty(
      a0,
      thisObject,
      argv,
      argc);
}

//  ReturnedValue QV4::ObjectPrototype::method_isPrototypeOf(const
//      FunctionObject *a0, const Value *thisObject, const Value *argv, int
//      argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV415ObjectPrototype20method_isPrototypeOfEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::ObjectPrototype::method_isPrototypeOf(
      a0,
      thisObject,
      argv,
      argc);
}

//  ReturnedValue QV4::ObjectPrototype::method_propertyIsEnumerable(const
//      FunctionObject *a0, const Value *thisObject, const Value *argv, int
//      argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV415ObjectPrototype27method_propertyIsEnumerableEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::ObjectPrototype::method_propertyIsEnumerable(
      a0,
      thisObject,
      argv,
      argc);
}

//  ReturnedValue QV4::ObjectPrototype::method_defineGetter(const
//      FunctionObject *a0, const Value *thisObject, const Value *argv, int
//      argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV415ObjectPrototype19method_defineGetterEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::ObjectPrototype::method_defineGetter(
      a0,
      thisObject,
      argv,
      argc);
}

//  ReturnedValue QV4::ObjectPrototype::method_defineSetter(const
//      FunctionObject *a0, const Value *thisObject, const Value *argv, int
//      argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV415ObjectPrototype19method_defineSetterEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::ObjectPrototype::method_defineSetter(
      a0,
      thisObject,
      argv,
      argc);
}

//  ReturnedValue QV4::ObjectPrototype::method_get_proto(const FunctionObject
//      *a0, const Value *thisObject, const Value *argv, int argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV415ObjectPrototype16method_get_protoEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::ObjectPrototype::method_get_proto(a0, thisObject, argv, argc);
}

//  ReturnedValue QV4::ObjectPrototype::method_set_proto(const FunctionObject
//      *a0, const Value *thisObject, const Value *argv, int argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV415ObjectPrototype16method_set_protoEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::ObjectPrototype::method_set_proto(a0, thisObject, argv, argc);
}

//  void QV4::ObjectPrototype::toPropertyDescriptor(ExecutionEngine *engine,
//      const Value &v, Property *desc, PropertyAttributes *attrs)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV415ObjectPrototype20toPropertyDescriptorEPNS_15ExecutionEngineERKNS_5ValueEPNS_8PropertyEPNS_18PropertyAttributesE(
    QV4::ExecutionEngine *engine,
    const QV4::Value *v,
    QV4::Property *desc,
    QV4::PropertyAttributes *attrs) {
  QV4::ObjectPrototype::toPropertyDescriptor(engine, *v, desc, attrs);
}

//  ReturnedValue
//      QV4::ObjectPrototype::fromPropertyDescriptor(ExecutionEngine *engine,
//      const Property *desc, PropertyAttributes attrs)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV415ObjectPrototype22fromPropertyDescriptorEPNS_15ExecutionEngineEPKNS_8PropertyENS_18PropertyAttributesE(
    QV4::ExecutionEngine *engine,
    const QV4::Property *desc,
    const QV4::PropertyAttributes *attrs) {
  return QV4::ObjectPrototype::fromPropertyDescriptor(engine, desc, *attrs);
}

//  Heap::ArrayObject
//      *QV4::ObjectPrototype::getOwnPropertyNames(ExecutionEngine *v4, const
//      Value &o)
extern "C" Q_DECL_EXPORT
QV4::Heap::ArrayObject *ritual_ZN3QV415ObjectPrototype19getOwnPropertyNamesEPNS_15ExecutionEngineERKNS_5ValueE(
    QV4::ExecutionEngine *v4,
    const QV4::Value *o) {
  return QV4::ObjectPrototype::getOwnPropertyNames(v4, *o);
}
