//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4compileddata_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4compileddata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qv4resolvedtypereference_p.h>
#include <QtQml/private/qqmlengine_p.h>
#include <QtQml/qqmlpropertymap.h>
#include <QtCore/qcryptographichash.h>
#include <QtQml/private/qv4compileddata_p.h>
#include <QtQml/private/inlinecomponentutils_p.h>
#include <QtQml/private/qqmlscriptdata_p.h>
#include <QtQml/private/qqmltypenamecache_p.h>
#include <QtQml/private/qv4resolvedtypereference_p.h>
#include <QtQml/qqmlfile.h>
#include <QtCore/qdir.h>
#include <QtCore/qscopeguard.h>
#include <QtCore/qstandardpaths.h>
#include <QtCore/qxpfunctional.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

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

//  from ../qtdeclarative/src/qml/common/qv4compileddata.cpp, line 75, as _ZNK3QV412CompiledData24ResolvedTypeReferenceMap9addToHashEP18QCryptographicHashP5QHashIy10QByteArrayE
namespace QV4::CompiledData {
inline bool ResolvedTypeReferenceMap::addToHash(
        QCryptographicHash *hash, QHash<quintptr, QByteArray> *checksums) const
{
    std::vector<int> keys (size());
    int i = 0;
    for (auto it = constBegin(), end = constEnd(); it != end; ++it) {
        keys[i] = it.key();
        ++i;
    }
    std::sort(keys.begin(), keys.end());
    for (int key: keys) {
        if (!this->operator[](key)->addToHash(hash, checksums))
            return false;
    }

    return true;
}
}  // namespace QV4::CompiledData
//  -----------------------------------------------------------------------

//  bool
//      QV4::CompiledData::ResolvedTypeReferenceMap::addToHash(QCryptographic
//      Hash *hash, QHash<quintptr, QByteArray> *checksums) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV412CompiledData24ResolvedTypeReferenceMap9addToHashEP18QCryptographicHashP5QHashIy10QByteArrayE(
    const QV4::CompiledData::ResolvedTypeReferenceMap *self,
    QCryptographicHash *hash,
    QHash<quintptr, QByteArray> *checksums) {
  return self->addToHash(hash, checksums);
}

//  QV4::CompiledData::ResolvedTypeReferenceMap::~ResolvedTypeReferenceMap()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV412CompiledData24ResolvedTypeReferenceMapD1Ev(
    QV4::CompiledData::ResolvedTypeReferenceMap *self) {
  delete self;
}
