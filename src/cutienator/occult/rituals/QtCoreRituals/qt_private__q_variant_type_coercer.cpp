//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qvariant.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qvariant.h>
#include <QtCore/qmetatype.h>

//  const void *QtPrivate::QVariantTypeCoercer::convert(const QVariant
//      &value, const QMetaType &type)
extern "C" Q_DECL_EXPORT
const void *ritual_ZN9QtPrivate19QVariantTypeCoercer7convertERK8QVariantRK9QMetaType(
    QtPrivate::QVariantTypeCoercer *self,
    const QVariant *value,
    const QMetaType *type) {
  return self->convert(*value, *type);
}

//  const void *QtPrivate::QVariantTypeCoercer::coerce(const QVariant &value,
//      const QMetaType &type)
extern "C" Q_DECL_EXPORT
const void *ritual_ZN9QtPrivate19QVariantTypeCoercer6coerceERK8QVariantRK9QMetaType(
    QtPrivate::QVariantTypeCoercer *self,
    const QVariant *value,
    const QMetaType *type) {
  return self->coerce(*value, *type);
}

//  QtPrivate::QVariantTypeCoercer::~QVariantTypeCoercer()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtPrivate19QVariantTypeCoercerD1Ev(
    QtPrivate::QVariantTypeCoercer *self) {
  delete self;
}
