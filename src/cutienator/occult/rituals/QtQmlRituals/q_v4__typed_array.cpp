//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4typedarray_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4typedarray_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4propertykey_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4global_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4value_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  const QV4::VTable *QV4::TypedArray::staticVTable()
extern "C" Q_DECL_EXPORT
const QV4::VTable *ritual_ZN3QV410TypedArray12staticVTableEv() {
  return QV4::TypedArray::staticVTable();
}

//  void QV4::TypedArray::__dataTest()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV410TypedArray10__dataTestEv(QV4::TypedArray *self) {
  self->__dataTest();
}

//  QV4::Heap::TypedArray *QV4::TypedArray::d_unchecked() const
extern "C" Q_DECL_EXPORT
QV4::Heap::TypedArray *ritual_ZNK3QV410TypedArray11d_uncheckedEv(
    const QV4::TypedArray *self) {
  return self->d_unchecked();
}

//  QV4::Heap::TypedArray *QV4::TypedArray::d() const
extern "C" Q_DECL_EXPORT
QV4::Heap::TypedArray *ritual_ZNK3QV410TypedArray1dEv(
    const QV4::TypedArray *self) {
  return self->d();
}

//  Heap::TypedArray *QV4::TypedArray::create(QV4::ExecutionEngine *e,
//      Heap::TypedArray::Type t)
extern "C" Q_DECL_EXPORT
QV4::Heap::TypedArray *ritual_ZN3QV410TypedArray6createEPNS_15ExecutionEngineENS_14TypedArrayTypeE(
    QV4::ExecutionEngine *e,
    QV4::Heap::TypedArray::Type t) {
  return QV4::TypedArray::create(e, t);
}

//  uint QV4::TypedArray::byteOffset() const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK3QV410TypedArray10byteOffsetEv(const QV4::TypedArray *self) {
  return self->byteOffset();
}

//  uint QV4::TypedArray::byteLength() const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK3QV410TypedArray10byteLengthEv(const QV4::TypedArray *self) {
  return self->byteLength();
}

//  int QV4::TypedArray::bytesPerElement() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK3QV410TypedArray15bytesPerElementEv(
    const QV4::TypedArray *self) {
  return self->bytesPerElement();
}

//  uint QV4::TypedArray::length() const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK3QV410TypedArray6lengthEv(const QV4::TypedArray *self) {
  return self->length();
}

//  char *QV4::TypedArray::arrayData()
extern "C" Q_DECL_EXPORT
char *ritual_ZN3QV410TypedArray9arrayDataEv(QV4::TypedArray *self) {
  return self->arrayData();
}

//  const char *QV4::TypedArray::constArrayData() const
extern "C" Q_DECL_EXPORT
const char *ritual_ZNK3QV410TypedArray14constArrayDataEv(
    const QV4::TypedArray *self) {
  return self->constArrayData();
}

//  bool QV4::TypedArray::hasDetachedArrayData() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV410TypedArray20hasDetachedArrayDataEv(
    const QV4::TypedArray *self) {
  return self->hasDetachedArrayData();
}

//  uint QV4::TypedArray::arrayDataLength() const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK3QV410TypedArray15arrayDataLengthEv(
    const QV4::TypedArray *self) {
  return self->arrayDataLength();
}

//  Heap::TypedArray::Type QV4::TypedArray::arrayType() const
extern "C" Q_DECL_EXPORT
QV4::Heap::TypedArray::Type *ritual_ZNK3QV410TypedArray9arrayTypeEv(
    const QV4::TypedArray *self) {
  return new QV4::Heap::TypedArray::Type(self->arrayType());
}

//  ReturnedValue QV4::TypedArray::virtualGet(const Managed *m, PropertyKey
//      id, const Value *receiver, bool *hasProperty)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV410TypedArray10virtualGetEPKNS_7ManagedENS_11PropertyKeyEPKNS_5ValueEPb(
    const QV4::Managed *m,
    const QV4::PropertyKey *id,
    const QV4::Value *receiver,
    bool *hasProperty) {
  return QV4::TypedArray::virtualGet(m, *id, receiver, hasProperty);
}

//  bool QV4::TypedArray::virtualHasProperty(const Managed *m, PropertyKey
//      id)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV410TypedArray18virtualHasPropertyEPKNS_7ManagedENS_11PropertyKeyE(
    const QV4::Managed *m,
    const QV4::PropertyKey *id) {
  return QV4::TypedArray::virtualHasProperty(m, *id);
}

//  PropertyAttributes QV4::TypedArray::virtualGetOwnProperty(const Managed
//      *m, PropertyKey id, Property *p)
extern "C" Q_DECL_EXPORT
QV4::PropertyAttributes *ritual_ZN3QV410TypedArray21virtualGetOwnPropertyEPKNS_7ManagedENS_11PropertyKeyEPNS_8PropertyE(
    const QV4::Managed *m,
    const QV4::PropertyKey *id,
    QV4::Property *p) {
  return new QV4::PropertyAttributes(
      QV4::TypedArray::virtualGetOwnProperty(
          m,
          *id,
          p));
}

//  bool QV4::TypedArray::virtualPut(Managed *m, PropertyKey id, const Value
//      &value, Value *receiver)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV410TypedArray10virtualPutEPNS_7ManagedENS_11PropertyKeyERKNS_5ValueEPS4_(
    QV4::Managed *m,
    const QV4::PropertyKey *id,
    const QV4::Value *value,
    QV4::Value *receiver) {
  return QV4::TypedArray::virtualPut(m, *id, *value, receiver);
}

//  bool QV4::TypedArray::virtualDefineOwnProperty(Managed *m, PropertyKey
//      id, const Property *p, PropertyAttributes attrs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV410TypedArray24virtualDefineOwnPropertyEPNS_7ManagedENS_11PropertyKeyEPKNS_8PropertyENS_18PropertyAttributesE(
    QV4::Managed *m,
    const QV4::PropertyKey *id,
    const QV4::Property *p,
    const QV4::PropertyAttributes *attrs) {
  return QV4::TypedArray::virtualDefineOwnProperty(m, *id, p, *attrs);
}

//  OwnPropertyKeyIterator *QV4::TypedArray::virtualOwnPropertyKeys(const
//      Object *m, Value *target)
extern "C" Q_DECL_EXPORT
QV4::OwnPropertyKeyIterator *ritual_ZN3QV410TypedArray22virtualOwnPropertyKeysEPKNS_6ObjectEPNS_5ValueE(
    const QV4::Object *m,
    QV4::Value *target) {
  return QV4::TypedArray::virtualOwnPropertyKeys(m, target);
}

//  a QV4::Heap::TypedArray::Type a ritual of QV4::TypedArray gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QV4_TypedArray__QV4_Heap_TypedArray_Type(
    QV4::Heap::TypedArray::Type *self) {
  delete self;
}
