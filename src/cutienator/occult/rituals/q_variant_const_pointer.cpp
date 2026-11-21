//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qvariant.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qvariant.h>

//  QVariantConstPointer::QVariantConstPointer(QVariant variant)
extern "C" Q_DECL_EXPORT
QVariantConstPointer *ritual_ZN20QVariantConstPointerC1E8QVariant(
    const QVariant *variant) {
  return new QVariantConstPointer(*variant);
}

//  QVariant QVariantConstPointer::operator*() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK20QVariantConstPointerdeEv(
    const QVariantConstPointer *self) {
  return new QVariant(self->operator*());
}

//  const QVariant *QVariantConstPointer::operator->() const
extern "C" Q_DECL_EXPORT
const QVariant *ritual_ZNK20QVariantConstPointerptEv(
    const QVariantConstPointer *self) {
  return self->operator->();
}

//  QVariantConstPointer::~QVariantConstPointer()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QVariantConstPointerD1Ev(QVariantConstPointer *self) {
  delete self;
}
