//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlmetatypedata_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlmetatypedata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qtyperevision.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlpropertycache_p.h>
#include <QtQml/6.12.0/QtQml/private/qqmltype_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qqmltype_p_p.h"
#include <QtQml/qjsvalue.h>
#include <QtQml/qqmlengine.h>
#include <QtQml/qqmlcontext.h>
#include <QtQml/qqmlcomponent.h>
#include <private/qqmlcustomparser_p.h>
#include <private/qqmldata_p.h>
#include <private/qqmlmetatypedata_p.h>
#include <private/qqmlpropertycache_p.h>
#include <private/qqmltypedata_p.h>
#include "qqmlmetatypedata_p.h"
#include <private/qqmltype_p_p.h>
#include <private/qqmltypemodule_p.h>
#include <private/qqmlpropertycache_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/qml/qqmltype.cpp, line 67, as _ZN15QQmlTypePrivateD1Ev
inline QQmlTypePrivate::~QQmlTypePrivate()
{
    delete enums.fetchAndStoreAcquire(nullptr);
    delete proxyMetaObjects.fetchAndStoreAcquire(nullptr);

    switch (regType) {
    case QQmlType::CppType:
        delete extraData.cppTypeData->customParser;
        delete extraData.cppTypeData;
        break;
    case QQmlType::SingletonType:
    case QQmlType::CompositeSingletonType:
        extraData.singletonTypeData->singletonInstanceInfo.reset();
        delete extraData.singletonTypeData;
        break;
    case QQmlType::CompositeType:
        extraData.compositeTypeData.~QUrl();
        break;
    case QQmlType::InlineComponentType:
        extraData.inlineComponentTypeData.~QUrl();
        break;
    case QQmlType::SequentialContainerType:
        extraData.sequentialContainerTypeData.~QMetaSequence();
        break;
    case QQmlType::JavaScriptType:
        extraData.javaScriptTypeData.~QUrl();
        break;
    default: //Also InterfaceType, because it has no extra data
        break;
    }
}

//  from ../qtdeclarative/src/qml/qml/qqmlmetatypedata.cpp, line 45, as _ZN16QQmlMetaTypeData12VersionedUriC1ERKSt10unique_ptrI14QQmlTypeModuleSt14default_deleteIS2_EE
inline QQmlMetaTypeData::VersionedUri::VersionedUri(const std::unique_ptr<QQmlTypeModule> &module)
    : uri(module->module()), majorVersion(module->majorVersion())
{
}

//  from ../qtdeclarative/src/qml/qml/qqmlmetatypedata.cpp, line 13, as _ZN16QQmlMetaTypeDataC1Ev
inline QQmlMetaTypeData::QQmlMetaTypeData()
{
}

//  from ../qtdeclarative/src/qml/qml/qqmlmetatypedata.cpp, line 17, as _ZN16QQmlMetaTypeDataD1Ev
inline QQmlMetaTypeData::~QQmlMetaTypeData()
{
    clearCompositeTypes();
    propertyCaches.clear();
    // Do this before the attached properties disappear.
    types.clear();
    undeletableTypes.clear();
    qDeleteAll(metaTypeToValueType);
    clearCompositeMetaTypes();
}

//  from ../qtdeclarative/src/qml/qml/qqmlmetatypedata.cpp, line 29, as _ZN16QQmlMetaTypeData12registerTypeEP15QQmlTypePrivate
inline void QQmlMetaTypeData::registerType(QQmlTypePrivate *priv)
{
    for (int i = 0; i < types.size(); ++i) {
        Type &type = types[i];
        if (!type.type.isValid()) {
            type.type = QQmlType(priv);
            priv->index = i;
            priv->release();
            return;
        }
    }
    types.append({QQmlType(priv), {}});
    priv->index = types.size() - 1;
    priv->release();
}

//  from ../qtdeclarative/src/qml/qml/qqmlmetatypedata.cpp, line 50, as _ZN16QQmlMetaTypeData14findTypeModuleERK7QString13QTypeRevision
inline QQmlTypeModule *QQmlMetaTypeData::findTypeModule(const QString &module, QTypeRevision version)
{
    const auto qqtm = std::lower_bound(
                uriToModule.begin(), uriToModule.end(), VersionedUri(module, version),
                std::less<QQmlMetaTypeData::VersionedUri>());
    if (qqtm == uriToModule.end())
        return nullptr;

    QQmlTypeModule *candidate = qqtm->get();
    return (candidate->module() == module && candidate->majorVersion() == version.majorVersion())
            ? candidate
            : nullptr;
}

//  from ../qtdeclarative/src/qml/qml/qqmlmetatypedata.cpp, line 77, as _ZN16QQmlMetaTypeData19registerModuleTypesERK7QString
inline bool QQmlMetaTypeData::registerModuleTypes(const QString &uri)
{
    auto function = moduleTypeRegistrationFunctions.constFind(uri);
    if (function != moduleTypeRegistrationFunctions.constEnd()) {
        (*function)();
        return true;
    }
    return false;
}

//  from ../qtdeclarative/src/qml/qml/qqmlmetatypedata.cpp, line 87, as _ZNK16QQmlMetaTypeData23propertyCacheForVersionEi13QTypeRevision
inline QQmlPropertyCache::ConstPtr QQmlMetaTypeData::propertyCacheForVersion(
        int index, QTypeRevision version) const
{
    return (index < types.size())
            ? types[index].propertyCaches.value(version)
            : QQmlPropertyCache::ConstPtr();
}

//  from ../qtdeclarative/src/qml/qml/qqmlmetatypedata.cpp, line 95, as _ZN16QQmlMetaTypeData26setPropertyCacheForVersionEi13QTypeRevisionRKN17QQmlPropertyCache8ConstPtrE
inline void QQmlMetaTypeData::setPropertyCacheForVersion(int index, QTypeRevision version,
                                                  const QQmlPropertyCache::ConstPtr &cache)
{
    if (index >= types.size())
        types.resize(index + 1);
    types[index].propertyCaches[version] = cache;
}

//  from ../qtdeclarative/src/qml/qml/qqmlmetatypedata.cpp, line 103, as _ZN16QQmlMetaTypeData13propertyCacheEPK11QMetaObject13QTypeRevision
inline QQmlPropertyCache::ConstPtr QQmlMetaTypeData::propertyCache(
        const QMetaObject *metaObject, QTypeRevision version)
{
    if (QQmlPropertyCache::ConstPtr rv = propertyCaches.value(metaObject))
        return rv;

    QQmlPropertyCache::ConstPtr rv;
    if (const QMetaObject *superMeta = metaObject->superClass())
        rv = propertyCache(superMeta, version)->copyAndAppend(metaObject, version);
    else
        rv = QQmlPropertyCache::createStandalone(metaObject);

    const auto *mop = reinterpret_cast<const QMetaObjectPrivate *>(metaObject->d.data);
    if (!(mop->flags & DynamicMetaObject))
        propertyCaches.insert(metaObject, rv);

    return rv;
}

//  from ../qtdeclarative/src/qml/qml/qqmlmetatypedata.cpp, line 122, as _ZN16QQmlMetaTypeData13propertyCacheERK8QQmlType13QTypeRevision
inline QQmlPropertyCache::ConstPtr QQmlMetaTypeData::propertyCache(
        const QQmlType &type, QTypeRevision version)
{
    Q_ASSERT(type.isValid());

    if (auto pc = propertyCacheForVersion(type.index(), version))
        return pc;

    QList<QQmlType> types;

    quint8 maxMinorVersion = 0;

    const QMetaObject *metaObject = type.metaObject();
    Q_ASSERT(metaObject);

    const QTypeRevision combinedVersion = version.hasMajorVersion()
            ? version
            : (version.hasMinorVersion()
               ? QTypeRevision::fromVersion(type.version().majorVersion(),
                                            version.minorVersion())
               : QTypeRevision::fromMajorVersion(type.version().majorVersion()));

    while (metaObject) {
        QQmlType t = QQmlMetaType::qmlType(metaObject, type.module(), combinedVersion);
        if (t.isValid()) {
            maxMinorVersion = qMax(maxMinorVersion, t.version().minorVersion());
            types << t;
        } else {
            types << QQmlType();
        }

        metaObject = metaObject->superClass();
    }

    const QTypeRevision maxVersion = QTypeRevision::fromVersion(combinedVersion.majorVersion(),
                                                                maxMinorVersion);
    if (auto pc = propertyCacheForVersion(type.index(), maxVersion)) {
        setPropertyCacheForVersion(type.index(), maxVersion, pc);
        return pc;
    }

    QQmlPropertyCache::ConstPtr raw = propertyCache(type.metaObject(), combinedVersion);
    QQmlPropertyCache::Ptr copied;

    for (int ii = 0; ii < types.size(); ++ii) {
        const QQmlType &currentType = types.at(ii);
        if (!currentType.isValid())
            continue;

        QTypeRevision rev = currentType.metaObjectRevision();
        int moIndex = types.size() - 1 - ii;

        if (raw->allowedRevision(moIndex) != rev) {
            if (copied.isNull()) {
                copied = raw->copy();
                raw = copied;
            }
            copied->setAllowedRevision(moIndex, rev);
        }
    }

    // Test revision compatibility - the basic rule is:
    //    * Anything that is excluded, cannot overload something that is not excluded *

    // Signals override:
    //    * other signals and methods of the same name.
    //    * properties named on<Signal Name>
    //    * automatic <property name>Changed notify signals

    // Methods override:
    //    * other methods of the same name

    // Properties override:
    //    * other elements of the same name

#if 0
    bool overloadError = false;
    QString overloadName;

    for (QQmlPropertyCache::StringCache::ConstIterator iter = raw->stringCache.begin();
         !overloadError && iter != raw->stringCache.end();
         ++iter) {

        const QQmlPropertyData *d = *iter;
        if (raw->isAllowedInRevision(d))
            continue; // Not excluded - no problems

        // check that a regular "name" overload isn't happening
        const QQmlPropertyData *current = d;
        while (!overloadError && current) {
            current = d->overrideData(current);
            if (current && raw->isAllowedInRevision(current))
                overloadError = true;
        }
    }

    if (overloadError) {
        if (hasCopied) raw->release();

        error.setDescription(QLatin1String("Type ") + type.qmlTypeName() + QLatin1Char(' ') + QString::number(type.majorVersion()) + QLatin1Char('.') + QString::number(minorVersion) + QLatin1String(" contains an illegal property \"") + overloadName + QLatin1String("\".  This is an error in the type's implementation."));
        return 0;
    }
#endif

    setPropertyCacheForVersion(type.index(), version, raw);

    if (version != maxVersion)
        setPropertyCacheForVersion(type.index(), maxVersion, raw);

    return raw;
}

//  from ../qtdeclarative/src/qml/qml/qqmlmetatypedata.cpp, line 255, as _ZN16QQmlMetaTypeData19clearCompositeTypesEv
inline void QQmlMetaTypeData::clearCompositeTypes()
{
    // Unregister all remaining composite types.
    // Avoid deletion recursion (via QQmlTypePrivate dtor) by moving them out of the way first.
    CompositeTypes emptyComposites;
    emptyComposites.swap(compositeTypes);

    // ECMAScript modules can form cycles. Clear the edges first, so that we don't leak memory.
    for (const auto &cu : std::as_const(emptyComposites))
        clearCompositeType(cu);
}

//  from ../qtdeclarative/src/qml/qml/qqmlmetatypedata.cpp, line 267, as _ZN16QQmlMetaTypeData23clearCompositeMetaTypesEv
inline void QQmlMetaTypeData::clearCompositeMetaTypes()
{
    for (const auto &compositeMetaType : std::as_const(compositeMetaTypes)) {
        Q_ASSERT(compositeMetaType.type);
        QMetaType::unregisterMetaType(QMetaType(compositeMetaType.type));
        delete compositeMetaType.type;

        Q_ASSERT(compositeMetaType.listType);
        QMetaType::unregisterMetaType(QMetaType(compositeMetaType.listType));
        delete compositeMetaType.listType;
    }
    compositeMetaTypes.clear();
}
//  -----------------------------------------------------------------------

//  QQmlMetaTypeData::QQmlMetaTypeData()
extern "C" Q_DECL_EXPORT
QQmlMetaTypeData *ritual_ZN16QQmlMetaTypeDataC1Ev() {
  return new QQmlMetaTypeData();
}

//  QQmlMetaTypeData::~QQmlMetaTypeData()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlMetaTypeDataD1Ev(QQmlMetaTypeData *self) {
  delete self;
}

//  void QQmlMetaTypeData::registerType(QQmlTypePrivate *priv)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlMetaTypeData12registerTypeEP15QQmlTypePrivate(
    QQmlMetaTypeData *self,
    QQmlTypePrivate *priv) {
  self->registerType(priv);
}

//  QQmlTypeModule *QQmlMetaTypeData::findTypeModule(const QString &module,
//      QTypeRevision version)
extern "C" Q_DECL_EXPORT
QQmlTypeModule *ritual_ZN16QQmlMetaTypeData14findTypeModuleERK7QString13QTypeRevision(
    QQmlMetaTypeData *self,
    const QString *module,
    const QTypeRevision *version) {
  return self->findTypeModule(*module, *version);
}

//  bool QQmlMetaTypeData::registerModuleTypes(const QString &uri)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QQmlMetaTypeData19registerModuleTypesERK7QString(
    QQmlMetaTypeData *self,
    const QString *uri) {
  return self->registerModuleTypes(*uri);
}

//  QQmlPropertyCache::ConstPtr QQmlMetaTypeData::propertyCacheForVersion(int
//      index, QTypeRevision version) const
extern "C" Q_DECL_EXPORT
QQmlPropertyCache::ConstPtr *ritual_ZNK16QQmlMetaTypeData23propertyCacheForVersionEi13QTypeRevision(
    const QQmlMetaTypeData *self,
    int index,
    const QTypeRevision *version) {
  return new QQmlPropertyCache::ConstPtr(
      self->propertyCacheForVersion(
          index,
          *version));
}

//  void QQmlMetaTypeData::setPropertyCacheForVersion(int index,
//      QTypeRevision version, const QQmlPropertyCache::ConstPtr &cache)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlMetaTypeData26setPropertyCacheForVersionEi13QTypeRevisionRKN17QQmlPropertyCache8ConstPtrE(
    QQmlMetaTypeData *self,
    int index,
    const QTypeRevision *version,
    const QQmlPropertyCache::ConstPtr *cache) {
  self->setPropertyCacheForVersion(index, *version, *cache);
}

//  QQmlPropertyCache::ConstPtr QQmlMetaTypeData::propertyCache(const
//      QMetaObject *metaObject, QTypeRevision version)
extern "C" Q_DECL_EXPORT
QQmlPropertyCache::ConstPtr *ritual_ZN16QQmlMetaTypeData13propertyCacheEPK11QMetaObject13QTypeRevision(
    QQmlMetaTypeData *self,
    const QMetaObject *metaObject,
    const QTypeRevision *version) {
  return new QQmlPropertyCache::ConstPtr(
      self->propertyCache(
          metaObject,
          *version));
}

//  QQmlPropertyCache::ConstPtr QQmlMetaTypeData::propertyCache(const
//      QQmlType &type, QTypeRevision version)
extern "C" Q_DECL_EXPORT
QQmlPropertyCache::ConstPtr *ritual_ZN16QQmlMetaTypeData13propertyCacheERK8QQmlType13QTypeRevision(
    QQmlMetaTypeData *self,
    const QQmlType *type,
    const QTypeRevision *version) {
  return new QQmlPropertyCache::ConstPtr(
      self->propertyCache(
          *type,
          *version));
}

//  void QQmlMetaTypeData::recordTypeRegFailure(const QString &message)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlMetaTypeData20recordTypeRegFailureERK7QString(
    QQmlMetaTypeData *self,
    const QString *message) {
  self->recordTypeRegFailure(*message);
}

//  void QQmlMetaTypeData::clearCompositeTypes()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlMetaTypeData19clearCompositeTypesEv(
    QQmlMetaTypeData *self) {
  self->clearCompositeTypes();
}

//  void QQmlMetaTypeData::clearCompositeMetaTypes()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlMetaTypeData23clearCompositeMetaTypesEv(
    QQmlMetaTypeData *self) {
  self->clearCompositeMetaTypes();
}
