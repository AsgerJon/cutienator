//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qassociativeiterable.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qassociativeiterable.h>
#include <QtCore/qvariant.h>

//  QVariant QAssociativeConstIterator::key() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK25QAssociativeConstIterator3keyEv(
    const QAssociativeConstIterator *self) {
  return new QVariant(self->key());
}

//  QVariant QAssociativeConstIterator::value() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK25QAssociativeConstIterator5valueEv(
    const QAssociativeConstIterator *self) {
  return new QVariant(self->value());
}

//  QVariant QAssociativeConstIterator::operator*() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK25QAssociativeConstIteratordeEv(
    const QAssociativeConstIterator *self) {
  return new QVariant(self->operator*());
}

//  QVariantConstPointer QAssociativeConstIterator::operator->() const
extern "C" Q_DECL_EXPORT
QVariantConstPointer *ritual_ZNK25QAssociativeConstIteratorptEv(
    const QAssociativeConstIterator *self) {
  return new QVariantConstPointer(self->operator->());
}

//  QAssociativeConstIterator::~QAssociativeConstIterator()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QAssociativeConstIteratorD1Ev(
    QAssociativeConstIterator *self) {
  delete self;
}
