//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qvariant.h, Qt 6.12.0. Edited by hand on 2026-11-27: the ritual of
//  the destructor the compiler writes for the class, which its cute class
//  calls to remove what Python holds, and which the generator no longer
//  writes for it. Kept as it is when the generator runs again.
#include <QtCore/qglobal.h>
#if QT_DEPRECATED_SINCE(6, 15)
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

#endif  // QT_DEPRECATED_SINCE(6, 15)
