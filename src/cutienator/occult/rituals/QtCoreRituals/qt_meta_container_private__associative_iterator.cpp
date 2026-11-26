//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qmetaassociation.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qmetaassociation.h>
#include <QtCore/qvariant.h>

//  QtMetaContainerPrivate::AssociativeIterator::AssociativeIterator(QIterato
//      r<QMetaAssociation> &&it)
extern "C" Q_DECL_EXPORT
QtMetaContainerPrivate::AssociativeIterator *ritual_ZN22QtMetaContainerPrivate19AssociativeIteratorC1EO9QIteratorI16QMetaAssociationE(
    QIterator<QMetaAssociation> *it) {
  return new QtMetaContainerPrivate::AssociativeIterator(std::move(*it));
}

//  key_type QtMetaContainerPrivate::AssociativeIterator::key() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK22QtMetaContainerPrivate19AssociativeIterator3keyEv(
    const QtMetaContainerPrivate::AssociativeIterator *self) {
  return new QVariant(self->key());
}

//  reference QtMetaContainerPrivate::AssociativeIterator::value() const
extern "C" Q_DECL_EXPORT
QtMetaContainerPrivate::AssociativeIterator::reference *ritual_ZNK22QtMetaContainerPrivate19AssociativeIterator5valueEv(
    const QtMetaContainerPrivate::AssociativeIterator *self) {
  return new QtMetaContainerPrivate::AssociativeIterator::reference(
      self->value());
}

//  reference QtMetaContainerPrivate::AssociativeIterator::operator*() const
extern "C" Q_DECL_EXPORT
QtMetaContainerPrivate::AssociativeIterator::reference *ritual_ZNK22QtMetaContainerPrivate19AssociativeIteratordeEv(
    const QtMetaContainerPrivate::AssociativeIterator *self) {
  return new QtMetaContainerPrivate::AssociativeIterator::reference(
      self->operator*());
}

//  pointer QtMetaContainerPrivate::AssociativeIterator::operator->() const
extern "C" Q_DECL_EXPORT
QtMetaContainerPrivate::AssociativeIterator::pointer *ritual_ZNK22QtMetaContainerPrivate19AssociativeIteratorptEv(
    const QtMetaContainerPrivate::AssociativeIterator *self) {
  return new QtMetaContainerPrivate::AssociativeIterator::pointer(
      self->operator->());
}

//  QtMetaContainerPrivate::AssociativeIterator::~AssociativeIterator()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QtMetaContainerPrivate19AssociativeIteratorD1Ev(
    QtMetaContainerPrivate::AssociativeIterator *self) {
  delete self;
}

//  a QtMetaContainerPrivate::AssociativeIterator::reference a ritual of
//      QtMetaContainerPrivate::AssociativeIterator gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QtMetaContainerPrivate_AssociativeIterator__QtMetaContainerPrivate_AssociativeIterator_reference(
    QtMetaContainerPrivate::AssociativeIterator::reference *self) {
  delete self;
}

//  a QtMetaContainerPrivate::AssociativeIterator::pointer a ritual of
//      QtMetaContainerPrivate::AssociativeIterator gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QtMetaContainerPrivate_AssociativeIterator__QtMetaContainerPrivate_AssociativeIterator_pointer(
    QtMetaContainerPrivate::AssociativeIterator::pointer *self) {
  delete self;
}
