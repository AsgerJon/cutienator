//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qmetasequence.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qmetasequence.h>
#include <QtCore/qvariant.h>

//  QtMetaContainerPrivate::SequentialConstIterator::SequentialConstIterator(
//      QConstIterator<QMetaSequence> &&it)
extern "C" Q_DECL_EXPORT
QtMetaContainerPrivate::SequentialConstIterator *ritual_ZN22QtMetaContainerPrivate23SequentialConstIteratorC1EO14QConstIteratorI13QMetaSequenceE(
    QConstIterator<QMetaSequence> *it) {
  return new QtMetaContainerPrivate::SequentialConstIterator(std::move(*it));
}

//  value_type QtMetaContainerPrivate::SequentialConstIterator::operator*()
//      const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK22QtMetaContainerPrivate23SequentialConstIteratordeEv(
    const QtMetaContainerPrivate::SequentialConstIterator *self) {
  return new QVariant(self->operator*());
}

//  pointer QtMetaContainerPrivate::SequentialConstIterator::operator->()
//      const
extern "C" Q_DECL_EXPORT
QtMetaContainerPrivate::SequentialConstIterator::pointer *ritual_ZNK22QtMetaContainerPrivate23SequentialConstIteratorptEv(
    const QtMetaContainerPrivate::SequentialConstIterator *self) {
  return new QtMetaContainerPrivate::SequentialConstIterator::pointer(
      self->operator->());
}

//  value_type
//      QtMetaContainerPrivate::SequentialConstIterator::operator[](qsizetype
//      n) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK22QtMetaContainerPrivate23SequentialConstIteratorixEx(
    const QtMetaContainerPrivate::SequentialConstIterator *self,
    qsizetype n) {
  return new QVariant(self->operator[](n));
}

//  QtMetaContainerPrivate::SequentialConstIterator::~SequentialConstIterator
//      ()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QtMetaContainerPrivate23SequentialConstIteratorD1Ev(
    QtMetaContainerPrivate::SequentialConstIterator *self) {
  delete self;
}

//  a QtMetaContainerPrivate::SequentialConstIterator::pointer a ritual of
//      QtMetaContainerPrivate::SequentialConstIterator gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QtMetaContainerPrivate_SequentialConstIterator__QtMetaContainerPrivate_SequentialConstIterator_pointer(
    QtMetaContainerPrivate::SequentialConstIterator::pointer *self) {
  delete self;
}
