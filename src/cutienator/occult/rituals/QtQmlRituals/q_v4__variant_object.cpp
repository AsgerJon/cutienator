//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4variantobject_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4variantobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  const QV4::VTable *QV4::VariantObject::staticVTable()
extern "C" Q_DECL_EXPORT
const QV4::VTable *ritual_ZN3QV413VariantObject12staticVTableEv() {
  return QV4::VariantObject::staticVTable();
}

//  void QV4::VariantObject::__dataTest()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV413VariantObject10__dataTestEv(QV4::VariantObject *self) {
  self->__dataTest();
}

//  QV4::Heap::VariantObject *QV4::VariantObject::d_unchecked() const
extern "C" Q_DECL_EXPORT
QV4::Heap::VariantObject *ritual_ZNK3QV413VariantObject11d_uncheckedEv(
    const QV4::VariantObject *self) {
  return self->d_unchecked();
}

//  QV4::Heap::VariantObject *QV4::VariantObject::d() const
extern "C" Q_DECL_EXPORT
QV4::Heap::VariantObject *ritual_ZNK3QV413VariantObject1dEv(
    const QV4::VariantObject *self) {
  return self->d();
}

//  QV4::Object *QV4::VariantObject::defaultPrototype(QV4::ExecutionEngine
//      *e)
extern "C" Q_DECL_EXPORT
QV4::Object *ritual_ZN3QV413VariantObject16defaultPrototypeEPNS_15ExecutionEngineE(
    QV4::ExecutionEngine *e) {
  return QV4::VariantObject::defaultPrototype(e);
}

//  void QV4::VariantObject::addVmePropertyReference() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK3QV413VariantObject23addVmePropertyReferenceEv(
    const QV4::VariantObject *self) {
  self->addVmePropertyReference();
}

//  void QV4::VariantObject::removeVmePropertyReference() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK3QV413VariantObject26removeVmePropertyReferenceEv(
    const QV4::VariantObject *self) {
  self->removeVmePropertyReference();
}

//  bool QV4::VariantObject::virtualIsEqualTo(Managed *m, Managed *other)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV413VariantObject16virtualIsEqualToEPNS_7ManagedES2_(
    QV4::Managed *m,
    QV4::Managed *other) {
  return QV4::VariantObject::virtualIsEqualTo(m, other);
}
