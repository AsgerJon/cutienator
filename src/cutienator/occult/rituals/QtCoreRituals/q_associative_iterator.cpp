//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qassociativeiterable.h, Qt 6.12.0. Edited by hand on 2026-11-27:
//  the ritual of the destructor the compiler writes for the class, which its
//  cute class calls to remove what Python holds, and which the generator no
//  longer writes for it. Kept as it is when the generator runs again.
#include <QtCore/qglobal.h>
#if QT_DEPRECATED_SINCE(6, 15)
#include <QtCore/qassociativeiterable.h>
#include <QtCore/qvariant.h>
#include <QtCore/QAssociativeIterator>

//  QAssociativeIterator::QAssociativeIterator(QIterator<QMetaAssociation>
//      &&it)
extern "C" Q_DECL_EXPORT
QAssociativeIterator *ritual_ZN20QAssociativeIteratorC1EO9QIteratorI16QMetaAssociationE(
    QIterator<QMetaAssociation> *it) {
  return new QAssociativeIterator(std::move(*it));
}

//  QVariant QAssociativeIterator::key() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK20QAssociativeIterator3keyEv(
    const QAssociativeIterator *self) {
  return new QVariant(self->key());
}

//  QVariantRef<QAssociativeIterator> QAssociativeIterator::value() const
extern "C" Q_DECL_EXPORT
QVariantRef<QAssociativeIterator> *ritual_ZNK20QAssociativeIterator5valueEv(
    const QAssociativeIterator *self) {
  return new QVariantRef<QAssociativeIterator>(self->value());
}

//  QVariantRef<QAssociativeIterator> QAssociativeIterator::operator*() const
extern "C" Q_DECL_EXPORT
QVariantRef<QAssociativeIterator> *ritual_ZNK20QAssociativeIteratordeEv(
    const QAssociativeIterator *self) {
  return new QVariantRef<QAssociativeIterator>(self->operator*());
}

//  QVariantPointer<QAssociativeIterator> QAssociativeIterator::operator->()
//      const
extern "C" Q_DECL_EXPORT
QVariantPointer<QAssociativeIterator> *ritual_ZNK20QAssociativeIteratorptEv(
    const QAssociativeIterator *self) {
  return new QVariantPointer<QAssociativeIterator>(self->operator->());
}

//  a QVariantRef<QAssociativeIterator> a ritual of QAssociativeIterator gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QAssociativeIterator__QVariantRef_QAssociativeIterator(
    QVariantRef<QAssociativeIterator> *self) {
  delete self;
}

//  a QVariantPointer<QAssociativeIterator> a ritual of QAssociativeIterator
//      gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QAssociativeIterator__QVariantPointer_QAssociativeIterator(
    QVariantPointer<QAssociativeIterator> *self) {
  delete self;
}

//  QAssociativeIterator::~QAssociativeIterator()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QAssociativeIteratorD1Ev(QAssociativeIterator *self) {
  delete self;
}

#endif  // QT_DEPRECATED_SINCE(6, 15)
