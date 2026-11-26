//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4variantassociationobject_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4variantassociationobject_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4propertykey_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4value_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4global_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  const QV4::VTable *QV4::VariantAssociationObject::staticVTable()
extern "C" Q_DECL_EXPORT
const QV4::VTable *ritual_ZN3QV424VariantAssociationObject12staticVTableEv() {
  return QV4::VariantAssociationObject::staticVTable();
}

//  void QV4::VariantAssociationObject::__dataTest()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV424VariantAssociationObject10__dataTestEv(
    QV4::VariantAssociationObject *self) {
  self->__dataTest();
}

//  QV4::Heap::VariantAssociationObject
//      *QV4::VariantAssociationObject::d_unchecked() const
extern "C" Q_DECL_EXPORT
QV4::Heap::VariantAssociationObject *ritual_ZNK3QV424VariantAssociationObject11d_uncheckedEv(
    const QV4::VariantAssociationObject *self) {
  return self->d_unchecked();
}

//  QV4::Heap::VariantAssociationObject *QV4::VariantAssociationObject::d()
//      const
extern "C" Q_DECL_EXPORT
QV4::Heap::VariantAssociationObject *ritual_ZNK3QV424VariantAssociationObject1dEv(
    const QV4::VariantAssociationObject *self) {
  return self->d();
}

//  QV4::Object
//      *QV4::VariantAssociationObject::defaultPrototype(QV4::ExecutionEngine
//      *e)
extern "C" Q_DECL_EXPORT
QV4::Object *ritual_ZN3QV424VariantAssociationObject16defaultPrototypeEPNS_15ExecutionEngineE(
    QV4::ExecutionEngine *e) {
  return QV4::VariantAssociationObject::defaultPrototype(e);
}

//  bool QV4::VariantAssociationObject::virtualPut(Managed *that, PropertyKey
//      id, const QV4::Value &value, Value *receiver)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV424VariantAssociationObject10virtualPutEPNS_7ManagedENS_11PropertyKeyERKNS_5ValueEPS4_(
    QV4::Managed *that,
    const QV4::PropertyKey *id,
    const QV4::Value *value,
    QV4::Value *receiver) {
  return QV4::VariantAssociationObject::virtualPut(
      that,
      *id,
      *value,
      receiver);
}

//  QV4::ReturnedValue QV4::VariantAssociationObject::virtualGet(const
//      QV4::Managed *that, PropertyKey id, const Value *receiver, bool
//      *hasProperty)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV424VariantAssociationObject10virtualGetEPKNS_7ManagedENS_11PropertyKeyEPKNS_5ValueEPb(
    const QV4::Managed *that,
    const QV4::PropertyKey *id,
    const QV4::Value *receiver,
    bool *hasProperty) {
  return QV4::VariantAssociationObject::virtualGet(
      that,
      *id,
      receiver,
      hasProperty);
}

//  bool QV4::VariantAssociationObject::virtualDeleteProperty(QV4::Managed
//      *that, PropertyKey id)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV424VariantAssociationObject21virtualDeletePropertyEPNS_7ManagedENS_11PropertyKeyE(
    QV4::Managed *that,
    const QV4::PropertyKey *id) {
  return QV4::VariantAssociationObject::virtualDeleteProperty(that, *id);
}

//  QV4::OwnPropertyKeyIterator
//      *QV4::VariantAssociationObject::virtualOwnPropertyKeys(const Object
//      *m, Value *target)
extern "C" Q_DECL_EXPORT
QV4::OwnPropertyKeyIterator *ritual_ZN3QV424VariantAssociationObject22virtualOwnPropertyKeysEPKNS_6ObjectEPNS_5ValueE(
    const QV4::Object *m,
    QV4::Value *target) {
  return QV4::VariantAssociationObject::virtualOwnPropertyKeys(m, target);
}

//  PropertyAttributes
//      QV4::VariantAssociationObject::virtualGetOwnProperty(const Managed
//      *m, PropertyKey id, Property *p)
extern "C" Q_DECL_EXPORT
QV4::PropertyAttributes *ritual_ZN3QV424VariantAssociationObject21virtualGetOwnPropertyEPKNS_7ManagedENS_11PropertyKeyEPNS_8PropertyE(
    const QV4::Managed *m,
    const QV4::PropertyKey *id,
    QV4::Property *p) {
  return new QV4::PropertyAttributes(
      QV4::VariantAssociationObject::virtualGetOwnProperty(
          m,
          *id,
          p));
}

//  int QV4::VariantAssociationObject::virtualMetacall(Object *object,
//      QMetaObject::Call call, int index, void **a)
extern "C" Q_DECL_EXPORT
int ritual_ZN3QV424VariantAssociationObject15virtualMetacallEPNS_6ObjectEN11QMetaObject4CallEiPPv(
    QV4::Object *object,
    QMetaObject::Call call,
    int index,
    void **a) {
  return QV4::VariantAssociationObject::virtualMetacall(
      object,
      call,
      index,
      a);
}
