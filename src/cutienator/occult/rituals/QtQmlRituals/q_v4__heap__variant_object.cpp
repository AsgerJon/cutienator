//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4variantobject_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4variantobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>

//  const QVariant &QV4::Heap::VariantObject::data() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK3QV44Heap13VariantObject4dataEv(
    const QV4::Heap::VariantObject *self) {
  return new QVariant(self->data());
}

//  void QV4::Heap::VariantObject::addVmePropertyReference()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap13VariantObject23addVmePropertyReferenceEv(
    QV4::Heap::VariantObject *self) {
  self->addVmePropertyReference();
}

//  void QV4::Heap::VariantObject::removeVmePropertyReference()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap13VariantObject26removeVmePropertyReferenceEv(
    QV4::Heap::VariantObject *self) {
  self->removeVmePropertyReference();
}
