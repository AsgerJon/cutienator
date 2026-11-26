//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4scopedvalue_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4scopedvalue_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4propertykey_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QV4::ScopedPropertyKey::ScopedPropertyKey(const Scope &scope)
extern "C" Q_DECL_EXPORT
QV4::ScopedPropertyKey *ritual_ZN3QV417ScopedPropertyKeyC1ERKNS_5ScopeE(
    const QV4::Scope *scope) {
  return new QV4::ScopedPropertyKey(*scope);
}

//  QV4::ScopedPropertyKey::ScopedPropertyKey(const Scope &scope, const
//      PropertyKey &v)
extern "C" Q_DECL_EXPORT
QV4::ScopedPropertyKey *ritual_ZN3QV417ScopedPropertyKeyC1ERKNS_5ScopeERKNS_11PropertyKeyE(
    const QV4::Scope *scope,
    const QV4::PropertyKey *v) {
  return new QV4::ScopedPropertyKey(*scope, *v);
}

//  ScopedPropertyKey &QV4::ScopedPropertyKey::operator=(const PropertyKey
//      &other)
extern "C" Q_DECL_EXPORT
QV4::ScopedPropertyKey *ritual_ZN3QV417ScopedPropertyKeyaSERKNS_11PropertyKeyE(
    QV4::ScopedPropertyKey *self,
    const QV4::PropertyKey *other) {
  return &(self->operator=(*other));
}

//  PropertyKey *QV4::ScopedPropertyKey::operator->()
extern "C" Q_DECL_EXPORT
QV4::PropertyKey *ritual_ZN3QV417ScopedPropertyKeyptEv(
    QV4::ScopedPropertyKey *self) {
  return self->operator->();
}

//  PropertyKey QV4::ScopedPropertyKey::operator PropertyKey() const
extern "C" Q_DECL_EXPORT
QV4::PropertyKey *ritual_ZNK3QV417ScopedPropertyKeycvNS_11PropertyKeyEEv(
    const QV4::ScopedPropertyKey *self) {
  return new QV4::PropertyKey(self->operator QV4::PropertyKey());
}

//  bool QV4::ScopedPropertyKey::operator==(const PropertyKey &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV417ScopedPropertyKeyeqERKNS_11PropertyKeyE(
    const QV4::ScopedPropertyKey *self,
    const QV4::PropertyKey *other) {
  return self->operator==(*other);
}

//  bool QV4::ScopedPropertyKey::operator==(const ScopedPropertyKey &other)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV417ScopedPropertyKeyeqERKS0_(
    const QV4::ScopedPropertyKey *self,
    const QV4::ScopedPropertyKey *other) {
  return self->operator==(*other);
}

//  bool QV4::ScopedPropertyKey::operator!=(const PropertyKey &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV417ScopedPropertyKeyneERKNS_11PropertyKeyE(
    const QV4::ScopedPropertyKey *self,
    const QV4::PropertyKey *other) {
  return self->operator!=(*other);
}

//  bool QV4::ScopedPropertyKey::operator!=(const ScopedPropertyKey &other)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV417ScopedPropertyKeyneERKS0_(
    const QV4::ScopedPropertyKey *self,
    const QV4::ScopedPropertyKey *other) {
  return self->operator!=(*other);
}

//  QV4::ScopedPropertyKey::~ScopedPropertyKey()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV417ScopedPropertyKeyD1Ev(QV4::ScopedPropertyKey *self) {
  delete self;
}
