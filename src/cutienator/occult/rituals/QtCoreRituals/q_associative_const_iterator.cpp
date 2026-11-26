//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qassociativeiterable.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#if QT_DEPRECATED_SINCE(6, 15)
#include <QtCore/qassociativeiterable.h>
#include <QtCore/qvariant.h>

//  QAssociativeConstIterator::QAssociativeConstIterator(QConstIterator<QMeta
//      Association> &&it)
extern "C" Q_DECL_EXPORT
QAssociativeConstIterator *ritual_ZN25QAssociativeConstIteratorC1EO14QConstIteratorI16QMetaAssociationE(
    QConstIterator<QMetaAssociation> *it) {
  return new QAssociativeConstIterator(std::move(*it));
}

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

#endif  // QT_DEPRECATED_SINCE(6, 15)
