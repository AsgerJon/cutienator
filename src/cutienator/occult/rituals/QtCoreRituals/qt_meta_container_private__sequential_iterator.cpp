//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qmetasequence.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qmetasequence.h>

//  QtMetaContainerPrivate::SequentialIterator::SequentialIterator(QIterator<
//      QMetaSequence> &&it)
extern "C" Q_DECL_EXPORT
QtMetaContainerPrivate::SequentialIterator *ritual_ZN22QtMetaContainerPrivate18SequentialIteratorC1EO9QIteratorI13QMetaSequenceE(
    QIterator<QMetaSequence> *it) {
  return new QtMetaContainerPrivate::SequentialIterator(std::move(*it));
}

//  reference QtMetaContainerPrivate::SequentialIterator::operator*() const
extern "C" Q_DECL_EXPORT
QtMetaContainerPrivate::SequentialIterator::reference *ritual_ZNK22QtMetaContainerPrivate18SequentialIteratordeEv(
    const QtMetaContainerPrivate::SequentialIterator *self) {
  return new QtMetaContainerPrivate::SequentialIterator::reference(
      self->operator*());
}

//  pointer QtMetaContainerPrivate::SequentialIterator::operator->() const
extern "C" Q_DECL_EXPORT
QtMetaContainerPrivate::SequentialIterator::pointer *ritual_ZNK22QtMetaContainerPrivate18SequentialIteratorptEv(
    const QtMetaContainerPrivate::SequentialIterator *self) {
  return new QtMetaContainerPrivate::SequentialIterator::pointer(
      self->operator->());
}

//  reference
//      QtMetaContainerPrivate::SequentialIterator::operator[](qsizetype n)
//      const
extern "C" Q_DECL_EXPORT
QtMetaContainerPrivate::SequentialIterator::reference *ritual_ZNK22QtMetaContainerPrivate18SequentialIteratorixEx(
    const QtMetaContainerPrivate::SequentialIterator *self,
    qsizetype n) {
  return new QtMetaContainerPrivate::SequentialIterator::reference(
      self->operator[](
          n));
}

//  QtMetaContainerPrivate::SequentialIterator::~SequentialIterator()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QtMetaContainerPrivate18SequentialIteratorD1Ev(
    QtMetaContainerPrivate::SequentialIterator *self) {
  delete self;
}

//  a QtMetaContainerPrivate::SequentialIterator::reference a ritual of
//      QtMetaContainerPrivate::SequentialIterator gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QtMetaContainerPrivate_SequentialIterator__QtMetaContainerPrivate_SequentialIterator_reference(
    QtMetaContainerPrivate::SequentialIterator::reference *self) {
  delete self;
}

//  a QtMetaContainerPrivate::SequentialIterator::pointer a ritual of
//      QtMetaContainerPrivate::SequentialIterator gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QtMetaContainerPrivate_SequentialIterator__QtMetaContainerPrivate_SequentialIterator_pointer(
    QtMetaContainerPrivate::SequentialIterator::pointer *self) {
  delete self;
}
