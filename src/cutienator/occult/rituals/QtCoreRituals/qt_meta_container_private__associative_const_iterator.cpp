//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qmetaassociation.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qmetaassociation.h>
#include <QtCore/qvariant.h>

//  key_type QtMetaContainerPrivate::AssociativeConstIterator::key() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK22QtMetaContainerPrivate24AssociativeConstIterator3keyEv(
    const QtMetaContainerPrivate::AssociativeConstIterator *self) {
  return new QVariant(self->key());
}

//  mapped_type QtMetaContainerPrivate::AssociativeConstIterator::value()
//      const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK22QtMetaContainerPrivate24AssociativeConstIterator5valueEv(
    const QtMetaContainerPrivate::AssociativeConstIterator *self) {
  return new QVariant(self->value());
}

//  mapped_type QtMetaContainerPrivate::AssociativeConstIterator::operator*()
//      const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK22QtMetaContainerPrivate24AssociativeConstIteratordeEv(
    const QtMetaContainerPrivate::AssociativeConstIterator *self) {
  return new QVariant(self->operator*());
}

//  QtMetaContainerPrivate::AssociativeConstIterator::~AssociativeConstIterat
//      or()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QtMetaContainerPrivate24AssociativeConstIteratorD1Ev(
    QtMetaContainerPrivate::AssociativeConstIterator *self) {
  delete self;
}
