//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qmetaassociation.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qmetaassociation.h>
#include <QtCore/qvariant.h>

//  QtMetaContainerPrivate::AssociativeConstIterator::AssociativeConstIterato
//      r(QConstIterator<QMetaAssociation> &&it)
extern "C" Q_DECL_EXPORT
QtMetaContainerPrivate::AssociativeConstIterator *ritual_ZN22QtMetaContainerPrivate24AssociativeConstIteratorC1EO14QConstIteratorI16QMetaAssociationE(
    QConstIterator<QMetaAssociation> *it) {
  return new QtMetaContainerPrivate::AssociativeConstIterator(
      std::move(*it));
}

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

//  pointer QtMetaContainerPrivate::AssociativeConstIterator::operator->()
//      const
extern "C" Q_DECL_EXPORT
QtMetaContainerPrivate::AssociativeConstIterator::pointer *ritual_ZNK22QtMetaContainerPrivate24AssociativeConstIteratorptEv(
    const QtMetaContainerPrivate::AssociativeConstIterator *self) {
  return new QtMetaContainerPrivate::AssociativeConstIterator::pointer(
      self->operator->());
}

//  QtMetaContainerPrivate::AssociativeConstIterator::~AssociativeConstIterat
//      or()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QtMetaContainerPrivate24AssociativeConstIteratorD1Ev(
    QtMetaContainerPrivate::AssociativeConstIterator *self) {
  delete self;
}

//  a QtMetaContainerPrivate::AssociativeConstIterator::pointer a ritual of
//      QtMetaContainerPrivate::AssociativeConstIterator gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QtMetaContainerPrivate_AssociativeConstIterator__QtMetaContainerPrivate_AssociativeConstIterator_pointer(
    QtMetaContainerPrivate::AssociativeConstIterator::pointer *self) {
  delete self;
}
