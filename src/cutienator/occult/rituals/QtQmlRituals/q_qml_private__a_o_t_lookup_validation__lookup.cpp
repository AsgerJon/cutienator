//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/qqmlprivate.h, Qt 6.12.0. Changes made here are lost.
#include <QtQml/QtQml>
#include <QtQml/qqmlprivate.h>

//  bool operator==(const Lookup &lhs, const Lookup &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QQmlPrivate19AOTLookupValidationeqERKNS0_6LookupES3_(
    const QQmlPrivate::AOTLookupValidation::Lookup *lhs,
    const QQmlPrivate::AOTLookupValidation::Lookup *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const Lookup &lhs, const Lookup &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QQmlPrivate19AOTLookupValidationneERKNS0_6LookupES3_(
    const QQmlPrivate::AOTLookupValidation::Lookup *lhs,
    const QQmlPrivate::AOTLookupValidation::Lookup *rhs) {
  return operator!=(*lhs, *rhs);
}

//  QQmlPrivate::AOTLookupValidation::Lookup::~Lookup()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQmlPrivate19AOTLookupValidation6LookupD1Ev(
    QQmlPrivate::AOTLookupValidation::Lookup *self) {
  delete self;
}
