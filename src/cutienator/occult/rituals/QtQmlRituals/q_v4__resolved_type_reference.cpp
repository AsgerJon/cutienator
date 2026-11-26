//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4resolvedtypereference_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4resolvedtypereference_p.h>
#include <QtQml/6.12.0/QtQml/private/qqmlpropertycache_p.h>
#include <QtQml/6.12.0/QtQml/private/qqmltype_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qtyperevision.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qv4resolvedtypereference_p.h>
#include <QtQml/private/qqmlengine_p.h>
#include <QtQml/qqmlpropertymap.h>
#include <QtCore/qcryptographichash.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/jsruntime/qv4resolvedtypereference.cpp, line 15, as local:qv4resolvedtypereference.cpp:qtTypeInherits
namespace QV4 {
inline template <typename T>
bool qtTypeInherits(const QMetaObject *mo) {
    while (mo) {
        if (mo == &T::staticMetaObject)
            return true;
        mo = mo->superClass();
    }
    return false;
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4resolvedtypereference.cpp, line 40, as _ZN3QV421ResolvedTypeReference19createPropertyCacheEv
namespace QV4 {
inline QQmlPropertyCache::ConstPtr ResolvedTypeReference::createPropertyCache()
{
    if (!m_typePropertyCache && m_type.isValid()) {
        const QMetaObject *metaObject = m_type.metaObject();
        if (!metaObject) // value type of non-Q_GADGET base with extension
            metaObject = m_type.extensionMetaObject();
        if (metaObject)
            m_typePropertyCache = QQmlMetaType::propertyCache(metaObject, m_version);
    }

    return m_typePropertyCache;
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4resolvedtypereference.cpp, line 53, as _ZN3QV421ResolvedTypeReference9addToHashEP18QCryptographicHashP5QHashIy10QByteArrayE
namespace QV4 {
inline bool ResolvedTypeReference::addToHash(
        QCryptographicHash *hash, QHash<quintptr, QByteArray> *checksums)
{
    // No need to add types from the same document to the hash.
    if (m_isSelfReference)
        return true;

    if (m_compilationUnit) {
        hash->addData({m_compilationUnit->unitData()->md5Checksum,
                        sizeof(m_compilationUnit->unitData()->md5Checksum)});
        return true;
    }

    if (QQmlPropertyCache::ConstPtr propertyCache = createPropertyCache()) {
        bool ok = false;
        hash->addData(propertyCache->checksum(checksums, &ok));
        return ok;
    }

    return false;
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4resolvedtypereference.cpp, line 25, as _ZN3QV421ResolvedTypeReference18doDynamicTypeCheckEv
namespace QV4 {
inline void ResolvedTypeReference::doDynamicTypeCheck()
{
    const QMetaObject *mo = nullptr;
    if (m_typePropertyCache)
        mo = m_typePropertyCache->firstCppMetaObject();
    else if (m_type.isValid())
        mo = m_type.metaObject();
    m_isFullyDynamicType = qtTypeInherits<QQmlPropertyMap>(mo);
}
}  // namespace QV4
//  -----------------------------------------------------------------------

//  QV4::ResolvedTypeReference::ResolvedTypeReference()
extern "C" Q_DECL_EXPORT
QV4::ResolvedTypeReference *ritual_ZN3QV421ResolvedTypeReferenceC1Ev() {
  return new QV4::ResolvedTypeReference();
}

//  QQmlPropertyCache::ConstPtr
//      QV4::ResolvedTypeReference::createPropertyCache()
extern "C" Q_DECL_EXPORT
QQmlPropertyCache::ConstPtr *ritual_ZN3QV421ResolvedTypeReference19createPropertyCacheEv(
    QV4::ResolvedTypeReference *self) {
  return new QQmlPropertyCache::ConstPtr(self->createPropertyCache());
}

//  bool QV4::ResolvedTypeReference::addToHash(QCryptographicHash *hash,
//      QHash<quintptr, QByteArray> *checksums)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV421ResolvedTypeReference9addToHashEP18QCryptographicHashP5QHashIy10QByteArrayE(
    QV4::ResolvedTypeReference *self,
    QCryptographicHash *hash,
    QHash<quintptr, QByteArray> *checksums) {
  return self->addToHash(hash, checksums);
}

//  void QV4::ResolvedTypeReference::doDynamicTypeCheck()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV421ResolvedTypeReference18doDynamicTypeCheckEv(
    QV4::ResolvedTypeReference *self) {
  self->doDynamicTypeCheck();
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

//  QQmlRefPointer<QV4::CompiledData::CompilationUnit>
//      QV4::ResolvedTypeReference::compilationUnit() const
extern "C" Q_DECL_EXPORT
QQmlRefPointer<QV4::CompiledData::CompilationUnit> *ritual_ZNK3QV421ResolvedTypeReference15compilationUnitEv(
    const QV4::ResolvedTypeReference *self) {
  return new QQmlRefPointer<QV4::CompiledData::CompilationUnit>(
      self->compilationUnit());
}

//  void QV4::ResolvedTypeReference::setCompilationUnit(const
//      QQmlRefPointer<QV4::CompiledData::CompilationUnit> &unit)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV421ResolvedTypeReference18setCompilationUnitERK14QQmlRefPointerINS_12CompiledData15CompilationUnitEE(
    QV4::ResolvedTypeReference *self,
    const QQmlRefPointer<QV4::CompiledData::CompilationUnit> *unit) {
  self->setCompilationUnit(*unit);
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

//  a QQmlRefPointer<QV4::CompiledData::CompilationUnit> a ritual of
//      QV4::ResolvedTypeReference gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QV4_ResolvedTypeReference__QQmlRefPointer_QV4_CompiledData_CompilationUnit(
    QQmlRefPointer<QV4::CompiledData::CompilationUnit> *self) {
  delete self;
}
