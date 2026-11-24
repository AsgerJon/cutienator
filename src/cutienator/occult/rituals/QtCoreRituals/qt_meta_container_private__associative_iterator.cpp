//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qmetaassociation.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qmetaassociation.h>
#include <QtCore/qvariant.h>

//  key_type QtMetaContainerPrivate::AssociativeIterator::key() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK22QtMetaContainerPrivate19AssociativeIterator3keyEv(
    const QtMetaContainerPrivate::AssociativeIterator *self) {
  return new QVariant(self->key());
}

//  QtMetaContainerPrivate::AssociativeIterator::~AssociativeIterator()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QtMetaContainerPrivate19AssociativeIteratorD1Ev(
    QtMetaContainerPrivate::AssociativeIterator *self) {
  delete self;
}
