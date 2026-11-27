//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qassociativeiterable.h, Qt 6.12.0. Edited by hand on 2026-11-27:
//  the ritual of the destructor the compiler writes for the class, which its
//  cute class calls to remove what Python holds, and which the generator no
//  longer writes for it. Kept as it is when the generator runs again.
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

//  QAssociativeConstIterator::~QAssociativeConstIterator()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QAssociativeConstIteratorD1Ev(
    QAssociativeConstIterator *self) {
  delete self;
}

#endif  // QT_DEPRECATED_SINCE(6, 15)
