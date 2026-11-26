//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4object_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4object_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4internalclass_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4value_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4propertykey_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4global_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4property_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

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

//  void QV4::Object::setInternalClass(Heap::InternalClass *ic)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV46Object16setInternalClassEPNS_4Heap13InternalClassE(
    QV4::Object *self,
    QV4::Heap::InternalClass *ic) {
  self->setInternalClass(ic);
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

//  void QV4::Object::getProperty(const InternalClassEntry &entry, Property
//      *p) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK3QV46Object11getPropertyERKNS_18InternalClassEntryEPNS_8PropertyE(
    const QV4::Object *self,
    const QV4::InternalClassEntry *entry,
    QV4::Property *p) {
  self->getProperty(*entry, p);
}

//  void QV4::Object::setProperty(const InternalClassEntry &entry, const
//      Property *p)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV46Object11setPropertyERKNS_18InternalClassEntryEPKNS_8PropertyE(
    QV4::Object *self,
    const QV4::InternalClassEntry *entry,
    const QV4::Property *p) {
  self->setProperty(*entry, p);
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

//  PropertyIndex QV4::Object::getValueOrSetter(PropertyKey id,
//      PropertyAttributes *attrs)
extern "C" Q_DECL_EXPORT
QV4::PropertyIndex *ritual_ZN3QV46Object16getValueOrSetterENS_11PropertyKeyEPNS_18PropertyAttributesE(
    QV4::Object *self,
    const QV4::PropertyKey *id,
    QV4::PropertyAttributes *attrs) {
  return new QV4::PropertyIndex(self->getValueOrSetter(*id, attrs));
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

//  ReturnedValue QV4::Object::getValueAccessor(const Value *thisObject,
//      const Value &v, PropertyAttributes attrs)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV46Object16getValueAccessorEPKNS_5ValueERS2_NS_18PropertyAttributesE(
    const QV4::Value *thisObject,
    const QV4::Value *v,
    const QV4::PropertyAttributes *attrs) {
  return QV4::Object::getValueAccessor(thisObject, *v, *attrs);
}

//  bool QV4::Object::putValue(uint memberIndex, PropertyAttributes attrs,
//      const Value &value)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV46Object8putValueEjNS_18PropertyAttributesERKNS_5ValueE(
    QV4::Object *self,
    uint memberIndex,
    const QV4::PropertyAttributes *attrs,
    const QV4::Value *value) {
  return self->putValue(memberIndex, *attrs, *value);
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

//  void QV4::Object::defineDefaultProperty(const QString &name, const Value
//      &value, PropertyAttributes attributes)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV46Object21defineDefaultPropertyERK7QStringRKNS_5ValueENS_18PropertyAttributesE(
    QV4::Object *self,
    const QString *name,
    const QV4::Value *value,
    const QV4::PropertyAttributes *attributes) {
  self->defineDefaultProperty(*name, *value, *attributes);
}

//  void QV4::Object::defineDefaultProperty(const QString &name, VTable::Call
//      code, int argumentCount, PropertyAttributes attributes)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV46Object21defineDefaultPropertyERK7QStringPFyPKNS_14FunctionObjectEPKNS_5ValueES9_iEiNS_18PropertyAttributesE(
    QV4::Object *self,
    const QString *name,
    void *code,
    int argumentCount,
    const QV4::PropertyAttributes *attributes) {
  self->defineDefaultProperty(
      *name,
      reinterpret_cast<QV4::VTable::Call>(code),
      argumentCount,
      *attributes);
}

//  void QV4::Object::defineDefaultProperty(StringOrSymbol *name,
//      VTable::Call code, int argumentCount, PropertyAttributes attributes)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV46Object21defineDefaultPropertyEPNS_14StringOrSymbolEPFyPKNS_14FunctionObjectEPKNS_5ValueES8_iEiNS_18PropertyAttributesE(
    QV4::Object *self,
    QV4::StringOrSymbol *name,
    void *code,
    int argumentCount,
    const QV4::PropertyAttributes *attributes) {
  self->defineDefaultProperty(
      name,
      reinterpret_cast<QV4::VTable::Call>(code),
      argumentCount,
      *attributes);
}

//  void QV4::Object::defineAccessorProperty(const QString &name,
//      VTable::Call getter, VTable::Call setter)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV46Object22defineAccessorPropertyERK7QStringPFyPKNS_14FunctionObjectEPKNS_5ValueES9_iESB_(
    QV4::Object *self,
    const QString *name,
    void *getter,
    void *setter) {
  self->defineAccessorProperty(
      *name,
      reinterpret_cast<QV4::VTable::Call>(getter),
      reinterpret_cast<QV4::VTable::Call>(setter));
}

//  void QV4::Object::defineAccessorProperty(StringOrSymbol *name,
//      VTable::Call getter, VTable::Call setter)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV46Object22defineAccessorPropertyEPNS_14StringOrSymbolEPFyPKNS_14FunctionObjectEPKNS_5ValueES8_iESA_(
    QV4::Object *self,
    QV4::StringOrSymbol *name,
    void *getter,
    void *setter) {
  self->defineAccessorProperty(
      name,
      reinterpret_cast<QV4::VTable::Call>(getter),
      reinterpret_cast<QV4::VTable::Call>(setter));
}

//  void QV4::Object::defineReadonlyProperty(const QString &name, const Value
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV46Object22defineReadonlyPropertyERK7QStringRKNS_5ValueE(
    QV4::Object *self,
    const QString *name,
    const QV4::Value *value) {
  self->defineReadonlyProperty(*name, *value);
}

//  void QV4::Object::defineReadonlyProperty(String *name, const Value
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV46Object22defineReadonlyPropertyEPNS_6StringERKNS_5ValueE(
    QV4::Object *self,
    QV4::String *name,
    const QV4::Value *value) {
  self->defineReadonlyProperty(name, *value);
}

//  void QV4::Object::defineReadonlyConfigurableProperty(const QString &name,
//      const Value &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV46Object34defineReadonlyConfigurablePropertyERK7QStringRKNS_5ValueE(
    QV4::Object *self,
    const QString *name,
    const QV4::Value *value) {
  self->defineReadonlyConfigurableProperty(*name, *value);
}

//  void QV4::Object::defineReadonlyConfigurableProperty(StringOrSymbol
//      *name, const Value &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV46Object34defineReadonlyConfigurablePropertyEPNS_14StringOrSymbolERKNS_5ValueE(
    QV4::Object *self,
    QV4::StringOrSymbol *name,
    const QV4::Value *value) {
  self->defineReadonlyConfigurableProperty(name, *value);
}

//  void QV4::Object::addSymbolSpecies()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV46Object16addSymbolSpeciesEv(QV4::Object *self) {
  self->addSymbolSpecies();
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

//  void QV4::Object::insertMember(StringOrSymbol *s, const Property *p,
//      PropertyAttributes attributes)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV46Object12insertMemberEPNS_14StringOrSymbolEPKNS_8PropertyENS_18PropertyAttributesE(
    QV4::Object *self,
    QV4::StringOrSymbol *s,
    const QV4::Property *p,
    const QV4::PropertyAttributes *attributes) {
  self->insertMember(s, p, *attributes);
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

//  void QV4::Object::setPrototypeUnchecked(const Object *p)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV46Object21setPrototypeUncheckedEPKS0_(
    QV4::Object *self,
    const QV4::Object *p) {
  self->setPrototypeUnchecked(p);
}

//  void QV4::Object::copyArrayData(Object *other)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV46Object13copyArrayDataEPS0_(
    QV4::Object *self,
    QV4::Object *other) {
  self->copyArrayData(other);
}

//  bool QV4::Object::setArrayLength(uint newLen)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV46Object14setArrayLengthEj(QV4::Object *self, uint newLen) {
  return self->setArrayLength(newLen);
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

//  ArrayData::Type QV4::Object::arrayType() const
extern "C" Q_DECL_EXPORT
QV4::ArrayData::Type *ritual_ZNK3QV46Object9arrayTypeEv(
    const QV4::Object *self) {
  return new QV4::ArrayData::Type(self->arrayType());
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

//  void QV4::Object::initSparseArray()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV46Object15initSparseArrayEv(QV4::Object *self) {
  self->initSparseArray();
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

//  bool QV4::Object::isConcatSpreadable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV46Object18isConcatSpreadableEv(const QV4::Object *self) {
  return self->isConcatSpreadable();
}

//  bool QV4::Object::isArray() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV46Object7isArrayEv(const QV4::Object *self) {
  return self->isArray();
}

//  const FunctionObject *QV4::Object::speciesConstructor(Scope &scope, const
//      FunctionObject *defaultConstructor) const
extern "C" Q_DECL_EXPORT
const QV4::FunctionObject *ritual_ZNK3QV46Object18speciesConstructorERNS_5ScopeEPKNS_14FunctionObjectE(
    const QV4::Object *self,
    QV4::Scope *scope,
    const QV4::FunctionObject *defaultConstructor) {
  return self->speciesConstructor(*scope, defaultConstructor);
}

//  bool QV4::Object::setProtoFromNewTarget(const Value *newTarget)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV46Object21setProtoFromNewTargetEPKNS_5ValueE(
    QV4::Object *self,
    const QV4::Value *newTarget) {
  return self->setProtoFromNewTarget(newTarget);
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

//  int QV4::Object::metacall(QMetaObject::Call call, int index, void **a)
extern "C" Q_DECL_EXPORT
int ritual_ZN3QV46Object8metacallEN11QMetaObject4CallEiPPv(
    QV4::Object *self,
    QMetaObject::Call call,
    int index,
    void **a) {
  return self->metacall(call, index, a);
}

//  ReturnedValue QV4::Object::virtualGet(const Managed *m, PropertyKey id,
//      const Value *receiver, bool *hasProperty)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV46Object10virtualGetEPKNS_7ManagedENS_11PropertyKeyEPKNS_5ValueEPb(
    const QV4::Managed *m,
    const QV4::PropertyKey *id,
    const QV4::Value *receiver,
    bool *hasProperty) {
  return QV4::Object::virtualGet(m, *id, receiver, hasProperty);
}

//  bool QV4::Object::virtualPut(Managed *m, PropertyKey id, const Value
//      &value, Value *receiver)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV46Object10virtualPutEPNS_7ManagedENS_11PropertyKeyERKNS_5ValueEPS4_(
    QV4::Managed *m,
    const QV4::PropertyKey *id,
    const QV4::Value *value,
    QV4::Value *receiver) {
  return QV4::Object::virtualPut(m, *id, *value, receiver);
}

//  bool QV4::Object::virtualDeleteProperty(Managed *m, PropertyKey id)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV46Object21virtualDeletePropertyEPNS_7ManagedENS_11PropertyKeyE(
    QV4::Managed *m,
    const QV4::PropertyKey *id) {
  return QV4::Object::virtualDeleteProperty(m, *id);
}

//  bool QV4::Object::virtualHasProperty(const Managed *m, PropertyKey id)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV46Object18virtualHasPropertyEPKNS_7ManagedENS_11PropertyKeyE(
    const QV4::Managed *m,
    const QV4::PropertyKey *id) {
  return QV4::Object::virtualHasProperty(m, *id);
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

//  bool QV4::Object::virtualDefineOwnProperty(Managed *m, PropertyKey id,
//      const Property *p, PropertyAttributes attrs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV46Object24virtualDefineOwnPropertyEPNS_7ManagedENS_11PropertyKeyEPKNS_8PropertyENS_18PropertyAttributesE(
    QV4::Managed *m,
    const QV4::PropertyKey *id,
    const QV4::Property *p,
    const QV4::PropertyAttributes *attrs) {
  return QV4::Object::virtualDefineOwnProperty(m, *id, p, *attrs);
}

//  bool QV4::Object::virtualIsExtensible(const Managed *m)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV46Object19virtualIsExtensibleEPKNS_7ManagedE(
    const QV4::Managed *m) {
  return QV4::Object::virtualIsExtensible(m);
}

//  bool QV4::Object::virtualPreventExtensions(Managed *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV46Object24virtualPreventExtensionsEPNS_7ManagedE(
    QV4::Managed *a0) {
  return QV4::Object::virtualPreventExtensions(a0);
}

//  Heap::Object *QV4::Object::virtualGetPrototypeOf(const Managed *a0)
extern "C" Q_DECL_EXPORT
QV4::Heap::Object *ritual_ZN3QV46Object21virtualGetPrototypeOfEPKNS_7ManagedE(
    const QV4::Managed *a0) {
  return QV4::Object::virtualGetPrototypeOf(a0);
}

//  bool QV4::Object::virtualSetPrototypeOf(Managed *a0, const Object *a1)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV46Object21virtualSetPrototypeOfEPNS_7ManagedEPKS0_(
    QV4::Managed *a0,
    const QV4::Object *a1) {
  return QV4::Object::virtualSetPrototypeOf(a0, a1);
}

//  OwnPropertyKeyIterator *QV4::Object::virtualOwnPropertyKeys(const Object
//      *m, Value *target)
extern "C" Q_DECL_EXPORT
QV4::OwnPropertyKeyIterator *ritual_ZN3QV46Object22virtualOwnPropertyKeysEPKS0_PNS_5ValueE(
    const QV4::Object *m,
    QV4::Value *target) {
  return QV4::Object::virtualOwnPropertyKeys(m, target);
}

//  qint64 QV4::Object::virtualGetLength(const Managed *m)
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN3QV46Object16virtualGetLengthEPKNS_7ManagedE(
    const QV4::Managed *m) {
  return QV4::Object::virtualGetLength(m);
}

//  ReturnedValue QV4::Object::virtualInstanceOf(const Object *typeObject,
//      const Value &var)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV46Object17virtualInstanceOfEPKS0_RKNS_5ValueE(
    const QV4::Object *typeObject,
    const QV4::Value *var) {
  return QV4::Object::virtualInstanceOf(typeObject, *var);
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

//  bool QV4::Object::virtualResolveLookupSetter(Object *object,
//      ExecutionEngine *engine, Lookup *lookup, const Value &value)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV46Object26virtualResolveLookupSetterEPS0_PNS_15ExecutionEngineEPNS_6LookupERKNS_5ValueE(
    QV4::Object *object,
    QV4::ExecutionEngine *engine,
    QV4::Lookup *lookup,
    const QV4::Value *value) {
  return QV4::Object::virtualResolveLookupSetter(
      object,
      engine,
      lookup,
      *value);
}

//  int QV4::Object::virtualMetacall(Object *object, QMetaObject::Call call,
//      int index, void **a)
extern "C" Q_DECL_EXPORT
int ritual_ZN3QV46Object15virtualMetacallEPS0_N11QMetaObject4CallEiPPv(
    QV4::Object *object,
    QMetaObject::Call call,
    int index,
    void **a) {
  return QV4::Object::virtualMetacall(object, call, index, a);
}

//  ReturnedValue QV4::Object::checkedInstanceOf(ExecutionEngine *engine,
//      const FunctionObject *typeObject, const Value &var)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV46Object17checkedInstanceOfEPNS_15ExecutionEngineEPKNS_14FunctionObjectERKNS_5ValueE(
    QV4::ExecutionEngine *engine,
    const QV4::FunctionObject *typeObject,
    const QV4::Value *var) {
  return QV4::Object::checkedInstanceOf(engine, typeObject, *var);
}

//  bool QV4::Object::internalDefineOwnProperty(ExecutionEngine *engine, uint
//      index, const InternalClassEntry *memberEntry, const Property *p,
//      PropertyAttributes attrs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV46Object25internalDefineOwnPropertyEPNS_15ExecutionEngineEjPKNS_18InternalClassEntryEPKNS_8PropertyENS_18PropertyAttributesE(
    QV4::Object *self,
    QV4::ExecutionEngine *engine,
    uint index,
    const QV4::InternalClassEntry *memberEntry,
    const QV4::Property *p,
    const QV4::PropertyAttributes *attrs) {
  return self->internalDefineOwnProperty(
      engine,
      index,
      memberEntry,
      p,
      *attrs);
}

//  ReturnedValue QV4::Object::internalGet(PropertyKey id, const Value
//      *receiver, bool *hasProperty) const
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZNK3QV46Object11internalGetENS_11PropertyKeyEPKNS_5ValueEPb(
    const QV4::Object *self,
    const QV4::PropertyKey *id,
    const QV4::Value *receiver,
    bool *hasProperty) {
  return self->internalGet(*id, receiver, hasProperty);
}

//  bool QV4::Object::internalPut(PropertyKey id, const Value &value, Value
//      *receiver)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV46Object11internalPutENS_11PropertyKeyERKNS_5ValueEPS2_(
    QV4::Object *self,
    const QV4::PropertyKey *id,
    const QV4::Value *value,
    QV4::Value *receiver) {
  return self->internalPut(*id, *value, receiver);
}

//  bool QV4::Object::internalDeleteProperty(PropertyKey id)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV46Object22internalDeletePropertyENS_11PropertyKeyE(
    QV4::Object *self,
    const QV4::PropertyKey *id) {
  return self->internalDeleteProperty(*id);
}

//  a QV4::ArrayData::Type a ritual of QV4::Object gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QV4_Object__QV4_ArrayData_Type(QV4::ArrayData::Type *self) {
  delete self;
}
