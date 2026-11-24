//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4variantassociationobject_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4variantassociationobject_p.h>
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
