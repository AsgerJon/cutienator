//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/qqmlprivate.h, Qt 6.12.0. Changes made here are lost.
#include <QtQml/QtQml>
#include <QtQml/qqmlprivate.h>

//  bool operator==(const Type &lhs, const Type &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QQmlPrivate19AOTLookupValidationeqERKNS0_4TypeES3_(
    const QQmlPrivate::AOTLookupValidation::Type *lhs,
    const QQmlPrivate::AOTLookupValidation::Type *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const Type &lhs, const Type &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QQmlPrivate19AOTLookupValidationneERKNS0_4TypeES3_(
    const QQmlPrivate::AOTLookupValidation::Type *lhs,
    const QQmlPrivate::AOTLookupValidation::Type *rhs) {
  return operator!=(*lhs, *rhs);
}

//  QQmlPrivate::AOTLookupValidation::Type::~Type()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQmlPrivate19AOTLookupValidation4TypeD1Ev(
    QQmlPrivate::AOTLookupValidation::Type *self) {
  delete self;
}
