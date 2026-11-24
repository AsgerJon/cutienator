//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4object_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4object_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4value_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4propertykey_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4global_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  const QV4::VTable *QV4::Object::staticVTable()
extern "C" Q_DECL_EXPORT
const QV4::VTable *ritual_ZN3QV46Object12staticVTableEv() {
  return QV4::Object::staticVTable();
}

//  void QV4::Object::__dataTest()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV46Object10__dataTestEv(QV4::Object *self) {
  self->__dataTest();
}

//  QV4::Heap::Object *QV4::Object::d_unchecked() const
extern "C" Q_DECL_EXPORT
QV4::Heap::Object *ritual_ZNK3QV46Object11d_uncheckedEv(
    const QV4::Object *self) {
  return self->d_unchecked();
}

//  QV4::Heap::Object *QV4::Object::d() const
extern "C" Q_DECL_EXPORT
QV4::Heap::Object *ritual_ZNK3QV46Object1dEv(const QV4::Object *self) {
  return self->d();
}

//  Heap::InternalClass *QV4::Object::defaultInternalClass(QV4::EngineBase
//      *e)
extern "C" Q_DECL_EXPORT
QV4::Heap::InternalClass *ritual_ZN3QV46Object20defaultInternalClassEPNS_10EngineBaseE(
    QV4::EngineBase *e) {
  return QV4::Object::defaultInternalClass(e);
}

//  QV4::Object *QV4::Object::defaultPrototype(QV4::ExecutionEngine *e)
extern "C" Q_DECL_EXPORT
QV4::Object *ritual_ZN3QV46Object16defaultPrototypeEPNS_15ExecutionEngineE(
    QV4::ExecutionEngine *e) {
  return QV4::Object::defaultPrototype(e);
}

//  const Value *QV4::Object::propertyData(uint index) const
extern "C" Q_DECL_EXPORT
const QV4::Value *ritual_ZNK3QV46Object12propertyDataEj(
    const QV4::Object *self,
    uint index) {
  return self->propertyData(index);
}

//  Heap::ArrayData *QV4::Object::arrayData() const
extern "C" Q_DECL_EXPORT
QV4::Heap::ArrayData *ritual_ZNK3QV46Object9arrayDataEv(
    const QV4::Object *self) {
  return self->arrayData();
}

//  void QV4::Object::setArrayData(ArrayData *a)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV46Object12setArrayDataEPNS_9ArrayDataE(
    QV4::Object *self,
    QV4::ArrayData *a) {
  self->setArrayData(a);
}

//  void QV4::Object::setProperty(uint index, Value v) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK3QV46Object11setPropertyEjNS_5ValueE(
    const QV4::Object *self,
    uint index,
    const QV4::Value *v) {
  self->setProperty(index, *v);
}

//  void QV4::Object::setProperty(uint index, Heap::Base *b) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK3QV46Object11setPropertyEjPNS_4Heap4BaseE(
    const QV4::Object *self,
    uint index,
    QV4::Heap::Base *b) {
  self->setProperty(index, b);
}

//  void QV4::Object::setProperty(ExecutionEngine *engine, uint index, Value
//      v) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK3QV46Object11setPropertyEPNS_15ExecutionEngineEjNS_5ValueE(
    const QV4::Object *self,
    QV4::ExecutionEngine *engine,
    uint index,
    const QV4::Value *v) {
  self->setProperty(engine, index, *v);
}

//  void QV4::Object::setProperty(ExecutionEngine *engine, uint index,
//      Heap::Base *b) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK3QV46Object11setPropertyEPNS_15ExecutionEngineEjPNS_4Heap4BaseE(
    const QV4::Object *self,
    QV4::ExecutionEngine *engine,
    uint index,
    QV4::Heap::Base *b) {
  self->setProperty(engine, index, b);
}

//  const VTable *QV4::Object::vtable() const
extern "C" Q_DECL_EXPORT
const QV4::VTable *ritual_ZNK3QV46Object6vtableEv(const QV4::Object *self) {
  return self->vtable();
}

//  PropertyAttributes QV4::Object::getOwnProperty(PropertyKey id, Property
//      *p) const
extern "C" Q_DECL_EXPORT
QV4::PropertyAttributes *ritual_ZNK3QV46Object14getOwnPropertyENS_11PropertyKeyEPNS_8PropertyE(
    const QV4::Object *self,
    const QV4::PropertyKey *id,
    QV4::Property *p) {
  return new QV4::PropertyAttributes(self->getOwnProperty(*id, p));
}

//  bool QV4::Object::hasProperty(PropertyKey id) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV46Object11hasPropertyENS_11PropertyKeyE(
    const QV4::Object *self,
    const QV4::PropertyKey *id) {
  return self->hasProperty(*id);
}

//  bool QV4::Object::defineOwnProperty(PropertyKey id, const Property *p,
//      PropertyAttributes attrs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV46Object17defineOwnPropertyENS_11PropertyKeyEPKNS_8PropertyENS_18PropertyAttributesE(
    QV4::Object *self,
    const QV4::PropertyKey *id,
    const QV4::Property *p,
    const QV4::PropertyAttributes *attrs) {
  return self->defineOwnProperty(*id, p, *attrs);
}

//  ReturnedValue QV4::Object::getValue(const Value *thisObject, const Value
//      &v, PropertyAttributes attrs)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV46Object8getValueEPKNS_5ValueERS2_NS_18PropertyAttributesE(
    const QV4::Value *thisObject,
    const QV4::Value *v,
    const QV4::PropertyAttributes *attrs) {
  return QV4::Object::getValue(thisObject, *v, *attrs);
}

//  ReturnedValue QV4::Object::getValue(const Value &v, PropertyAttributes
//      attrs) const
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZNK3QV46Object8getValueERKNS_5ValueENS_18PropertyAttributesE(
    const QV4::Object *self,
    const QV4::Value *v,
    const QV4::PropertyAttributes *attrs) {
  return self->getValue(*v, *attrs);
}

//  ReturnedValue QV4::Object::getValueByIndex(uint propertyIndex) const
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZNK3QV46Object15getValueByIndexEj(
    const QV4::Object *self,
    uint propertyIndex) {
  return self->getValueByIndex(propertyIndex);
}

//  void QV4::Object::defineDefaultProperty(StringOrSymbol *name, const Value
//      &value, PropertyAttributes attributes)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV46Object21defineDefaultPropertyEPNS_14StringOrSymbolERKNS_5ValueENS_18PropertyAttributesE(
    QV4::Object *self,
    QV4::StringOrSymbol *name,
    const QV4::Value *value,
    const QV4::PropertyAttributes *attributes) {
  self->defineDefaultProperty(name, *value, *attributes);
}

//  void QV4::Object::insertMember(StringOrSymbol *s, const Value &v,
//      PropertyAttributes attributes)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV46Object12insertMemberEPNS_14StringOrSymbolERKNS_5ValueENS_18PropertyAttributesE(
    QV4::Object *self,
    QV4::StringOrSymbol *s,
    const QV4::Value *v,
    const QV4::PropertyAttributes *attributes) {
  self->insertMember(s, *v, *attributes);
}

//  bool QV4::Object::isExtensible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV46Object12isExtensibleEv(const QV4::Object *self) {
  return self->isExtensible();
}

//  bool QV4::Object::preventExtensions()
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV46Object17preventExtensionsEv(QV4::Object *self) {
  return self->preventExtensions();
}

//  Heap::Object *QV4::Object::getPrototypeOf() const
extern "C" Q_DECL_EXPORT
QV4::Heap::Object *ritual_ZNK3QV46Object14getPrototypeOfEv(
    const QV4::Object *self) {
  return self->getPrototypeOf();
}

//  bool QV4::Object::setPrototypeOf(const Object *p)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV46Object14setPrototypeOfEPKS0_(
    QV4::Object *self,
    const QV4::Object *p) {
  return self->setPrototypeOf(p);
}

//  void QV4::Object::setArrayLengthUnchecked(uint l)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV46Object23setArrayLengthUncheckedEj(
    QV4::Object *self,
    uint l) {
  self->setArrayLengthUnchecked(l);
}

//  void QV4::Object::arraySet(uint index, const Property *p,
//      PropertyAttributes attributes)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV46Object8arraySetEjPKNS_8PropertyENS_18PropertyAttributesE(
    QV4::Object *self,
    uint index,
    const QV4::Property *p,
    const QV4::PropertyAttributes *attributes) {
  self->arraySet(index, p, *attributes);
}

//  void QV4::Object::arraySet(uint index, const Value &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV46Object8arraySetEjRKNS_5ValueE(
    QV4::Object *self,
    uint index,
    const QV4::Value *value) {
  self->arraySet(index, *value);
}

//  bool QV4::Object::arrayPut(uint index, const Value &value)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV46Object8arrayPutEjRKNS_5ValueE(
    QV4::Object *self,
    uint index,
    const QV4::Value *value) {
  return self->arrayPut(index, *value);
}

//  bool QV4::Object::arrayPut(uint index, const Value *values, uint n)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV46Object8arrayPutEjPKNS_5ValueEj(
    QV4::Object *self,
    uint index,
    const QV4::Value *values,
    uint n) {
  return self->arrayPut(index, values, n);
}

//  void QV4::Object::setArrayAttributes(uint i, PropertyAttributes a)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV46Object18setArrayAttributesEjNS_18PropertyAttributesE(
    QV4::Object *self,
    uint i,
    const QV4::PropertyAttributes *a) {
  self->setArrayAttributes(i, *a);
}

//  void QV4::Object::push_back(const Value &v)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV46Object9push_backERKNS_5ValueE(
    QV4::Object *self,
    const QV4::Value *v) {
  self->push_back(*v);
}

//  void QV4::Object::setArrayType(ArrayData::Type t)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV46Object12setArrayTypeENS_4Heap9ArrayData4TypeE(
    QV4::Object *self,
    QV4::ArrayData::Type t) {
  self->setArrayType(t);
}

//  void QV4::Object::arrayReserve(uint n)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV46Object12arrayReserveEj(QV4::Object *self, uint n) {
  self->arrayReserve(n);
}

//  void QV4::Object::arrayCreate()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV46Object11arrayCreateEv(QV4::Object *self) {
  self->arrayCreate();
}

//  SparseArrayNode *QV4::Object::sparseBegin() const
extern "C" Q_DECL_EXPORT
QV4::SparseArrayNode *ritual_ZNK3QV46Object11sparseBeginEv(
    const QV4::Object *self) {
  return self->sparseBegin();
}

//  SparseArrayNode *QV4::Object::sparseEnd() const
extern "C" Q_DECL_EXPORT
QV4::SparseArrayNode *ritual_ZNK3QV46Object9sparseEndEv(
    const QV4::Object *self) {
  return self->sparseEnd();
}

//  bool QV4::Object::protoHasArray()
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV46Object13protoHasArrayEv(QV4::Object *self) {
  return self->protoHasArray();
}

//  ReturnedValue QV4::Object::get(StringOrSymbol *name, bool *hasProperty,
//      const Value *receiver) const
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZNK3QV46Object3getEPNS_14StringOrSymbolEPbPKNS_5ValueE(
    const QV4::Object *self,
    QV4::StringOrSymbol *name,
    bool *hasProperty,
    const QV4::Value *receiver) {
  return self->get(name, hasProperty, receiver);
}

//  ReturnedValue QV4::Object::get(uint idx, bool *hasProperty, const Value
//      *receiver) const
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZNK3QV46Object3getEjPbPKNS_5ValueE(
    const QV4::Object *self,
    uint idx,
    bool *hasProperty,
    const QV4::Value *receiver) {
  return self->get(idx, hasProperty, receiver);
}

//  ReturnedValue QV4::Object::getIndexed(uint idx, bool *hasProperty) const
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZNK3QV46Object10getIndexedEjPb(
    const QV4::Object *self,
    uint idx,
    bool *hasProperty) {
  return self->getIndexed(idx, hasProperty);
}

//  ReturnedValue QV4::Object::get(PropertyKey id, const Value *receiver,
//      bool *hasProperty) const
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZNK3QV46Object3getENS_11PropertyKeyEPKNS_5ValueEPb(
    const QV4::Object *self,
    const QV4::PropertyKey *id,
    const QV4::Value *receiver,
    bool *hasProperty) {
  return self->get(*id, receiver, hasProperty);
}

//  bool QV4::Object::put(StringOrSymbol *name, const Value &v, Value
//      *receiver)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV46Object3putEPNS_14StringOrSymbolERKNS_5ValueEPS3_(
    QV4::Object *self,
    QV4::StringOrSymbol *name,
    const QV4::Value *v,
    QV4::Value *receiver) {
  return self->put(name, *v, receiver);
}

//  bool QV4::Object::put(uint idx, const Value &v, Value *receiver)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV46Object3putEjRKNS_5ValueEPS1_(
    QV4::Object *self,
    uint idx,
    const QV4::Value *v,
    QV4::Value *receiver) {
  return self->put(idx, *v, receiver);
}

//  bool QV4::Object::putIndexed(uint idx, const Value &v)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV46Object10putIndexedEjRKNS_5ValueE(
    QV4::Object *self,
    uint idx,
    const QV4::Value *v) {
  return self->putIndexed(idx, *v);
}

//  bool QV4::Object::put(PropertyKey id, const Value &v, Value *receiver)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV46Object3putENS_11PropertyKeyERKNS_5ValueEPS2_(
    QV4::Object *self,
    const QV4::PropertyKey *id,
    const QV4::Value *v,
    QV4::Value *receiver) {
  return self->put(*id, *v, receiver);
}

//  bool QV4::Object::setIndexed(uint idx, const Value &v, ThrowOnFailure
//      shouldThrow)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV46Object10setIndexedEjRKNS_5ValueENS0_14ThrowOnFailureE(
    QV4::Object *self,
    uint idx,
    const QV4::Value *v,
    QV4::Object::ThrowOnFailure shouldThrow) {
  return self->setIndexed(idx, *v, shouldThrow);
}

//  bool QV4::Object::set(StringOrSymbol *name, const Value &v,
//      ThrowOnFailure shouldThrow)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV46Object3setEPNS_14StringOrSymbolERKNS_5ValueENS0_14ThrowOnFailureE(
    QV4::Object *self,
    QV4::StringOrSymbol *name,
    const QV4::Value *v,
    QV4::Object::ThrowOnFailure shouldThrow) {
  return self->set(name, *v, shouldThrow);
}

//  bool QV4::Object::deleteProperty(PropertyKey id)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV46Object14deletePropertyENS_11PropertyKeyE(
    QV4::Object *self,
    const QV4::PropertyKey *id) {
  return self->deleteProperty(*id);
}

//  OwnPropertyKeyIterator *QV4::Object::ownPropertyKeys(Value *target) const
extern "C" Q_DECL_EXPORT
QV4::OwnPropertyKeyIterator *ritual_ZNK3QV46Object15ownPropertyKeysEPNS_5ValueE(
    const QV4::Object *self,
    QV4::Value *target) {
  return self->ownPropertyKeys(target);
}

//  qint64 QV4::Object::getLength() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK3QV46Object9getLengthEv(const QV4::Object *self) {
  return self->getLength();
}

//  ReturnedValue QV4::Object::instanceOf(const Value &var) const
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZNK3QV46Object10instanceOfERKNS_5ValueE(
    const QV4::Object *self,
    const QV4::Value *var) {
  return self->instanceOf(*var);
}

//  ReturnedValue QV4::Object::resolveLookupGetter(ExecutionEngine *engine,
//      Lookup *lookup) const
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZNK3QV46Object19resolveLookupGetterEPNS_15ExecutionEngineEPNS_6LookupE(
    const QV4::Object *self,
    QV4::ExecutionEngine *engine,
    QV4::Lookup *lookup) {
  return self->resolveLookupGetter(engine, lookup);
}

//  bool QV4::Object::resolveLookupSetter(ExecutionEngine *engine, Lookup
//      *lookup, const Value &value)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV46Object19resolveLookupSetterEPNS_15ExecutionEngineEPNS_6LookupERKNS_5ValueE(
    QV4::Object *self,
    QV4::ExecutionEngine *engine,
    QV4::Lookup *lookup,
    const QV4::Value *value) {
  return self->resolveLookupSetter(engine, lookup, *value);
}

//  PropertyAttributes QV4::Object::virtualGetOwnProperty(const Managed *m,
//      PropertyKey id, Property *p)
extern "C" Q_DECL_EXPORT
QV4::PropertyAttributes *ritual_ZN3QV46Object21virtualGetOwnPropertyEPKNS_7ManagedENS_11PropertyKeyEPNS_8PropertyE(
    const QV4::Managed *m,
    const QV4::PropertyKey *id,
    QV4::Property *p) {
  return new QV4::PropertyAttributes(
      QV4::Object::virtualGetOwnProperty(
          m,
          *id,
          p));
}

//  ReturnedValue QV4::Object::virtualResolveLookupGetter(const Object
//      *object, ExecutionEngine *engine, Lookup *lookup)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV46Object26virtualResolveLookupGetterEPKS0_PNS_15ExecutionEngineEPNS_6LookupE(
    const QV4::Object *object,
    QV4::ExecutionEngine *engine,
    QV4::Lookup *lookup) {
  return QV4::Object::virtualResolveLookupGetter(object, engine, lookup);
}
