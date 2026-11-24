//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4resolvedtypereference_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4resolvedtypereference_p.h>
#include <QtQml/6.12.0/QtQml/private/qqmltype_p.h>
#include <QtQml/6.12.0/QtQml/private/qqmlpropertycache_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qtyperevision.h>

//  QV4::ResolvedTypeReference::ResolvedTypeReference()
extern "C" Q_DECL_EXPORT
QV4::ResolvedTypeReference *ritual_ZN3QV421ResolvedTypeReferenceC1Ev() {
  return new QV4::ResolvedTypeReference();
}

//  QQmlType QV4::ResolvedTypeReference::type() const
extern "C" Q_DECL_EXPORT
QQmlType *ritual_ZNK3QV421ResolvedTypeReference4typeEv(
    const QV4::ResolvedTypeReference *self) {
  return new QQmlType(self->type());
}

//  void QV4::ResolvedTypeReference::setType(QQmlType type)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV421ResolvedTypeReference7setTypeE8QQmlType(
    QV4::ResolvedTypeReference *self,
    const QQmlType *type) {
  self->setType(*type);
}

//  QQmlPropertyCache::ConstPtr
//      QV4::ResolvedTypeReference::typePropertyCache() const
extern "C" Q_DECL_EXPORT
QQmlPropertyCache::ConstPtr *ritual_ZNK3QV421ResolvedTypeReference17typePropertyCacheEv(
    const QV4::ResolvedTypeReference *self) {
  return new QQmlPropertyCache::ConstPtr(self->typePropertyCache());
}

//  void QV4::ResolvedTypeReference::setTypePropertyCache(QQmlPropertyCache::
//      ConstPtr cache)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV421ResolvedTypeReference20setTypePropertyCacheEN17QQmlPropertyCache8ConstPtrE(
    QV4::ResolvedTypeReference *self,
    const QQmlPropertyCache::ConstPtr *cache) {
  self->setTypePropertyCache(*cache);
}

//  QTypeRevision QV4::ResolvedTypeReference::version() const
extern "C" Q_DECL_EXPORT
QTypeRevision *ritual_ZNK3QV421ResolvedTypeReference7versionEv(
    const QV4::ResolvedTypeReference *self) {
  return new QTypeRevision(self->version());
}

//  void QV4::ResolvedTypeReference::setVersion(QTypeRevision version)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV421ResolvedTypeReference10setVersionE13QTypeRevision(
    QV4::ResolvedTypeReference *self,
    const QTypeRevision *version) {
  self->setVersion(*version);
}

//  bool QV4::ResolvedTypeReference::isFullyDynamicType() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV421ResolvedTypeReference18isFullyDynamicTypeEv(
    const QV4::ResolvedTypeReference *self) {
  return self->isFullyDynamicType();
}

//  void QV4::ResolvedTypeReference::setFullyDynamicType(bool fullyDynamic)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV421ResolvedTypeReference19setFullyDynamicTypeEb(
    QV4::ResolvedTypeReference *self,
    bool fullyDynamic) {
  self->setFullyDynamicType(fullyDynamic);
}

//  bool QV4::ResolvedTypeReference::isSelfReference() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV421ResolvedTypeReference15isSelfReferenceEv(
    const QV4::ResolvedTypeReference *self) {
  return self->isSelfReference();
}

//  void QV4::ResolvedTypeReference::setIsSelfReference(bool selfReference)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV421ResolvedTypeReference18setIsSelfReferenceEb(
    QV4::ResolvedTypeReference *self,
    bool selfReference) {
  self->setIsSelfReference(selfReference);
}
