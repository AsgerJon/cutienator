//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmltype_p_p.h, Qt 6.12.0. Edited by hand on
//  2026-11-25: added by hand, instances of templates of the class: 9. Kept
//  as it is when the generator runs again.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmltype_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qurl.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmltype_p.h>
#include <QtQml/6.12.0/QtQml/private/qqmlpropertycache_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qqmlcomponentandaliasresolver_p.h>
#include <QtQml/private/qqmlengine_p.h>
#include <QtQml/private/qqmlirbuilder_p.h>
#include <QtQml/private/qqmlirloader_p.h>
#include <QtQml/private/qqmlpropertycachecreator_p.h>
#include <QtQml/private/qqmlpropertyvalidator_p.h>
#include <QtQml/private/qqmlscriptblob_p.h>
#include <QtQml/private/qqmlscriptdata_p.h>
#include <QtQml/private/qqmltypecompiler_p.h>
#include <QtQml/private/qqmltypedata_p.h>
#include <QtQml/private/qqmltypeloaderqmldircontent_p.h>
#include <QtCore/qloggingcategory.h>
#include <QtCore/qcryptographichash.h>
#include <memory>
#include <QtQml/private/qqmltype_p_p.h>
#include <QtQml/qjsvalue.h>
#include <QtQml/qqmlengine.h>
#include <QtQml/qqmlcontext.h>
#include <QtQml/qqmlcomponent.h>
#include <QtQml/private/qqmlcustomparser_p.h>
#include <QtQml/private/qqmldata_p.h>
#include <QtQml/private/qqmlmetatypedata_p.h>
#include <QtQml/private/qqmlpropertycache_p.h>
#include <QtQml/private/qqmltypedata_p.h>
#include <QtQml/6.12.0/QtQml/private/qqmltypeloader_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/qml/qqmltype.cpp, line 171, as local:qqmltype.cpp:isPropertyRevisioned
static bool isPropertyRevisioned(const QMetaObject *mo, int index)
{
    return mo->property(index).revision();
}

//  from ../qtdeclarative/src/qml/qml/qqmltypedata.cpp, line 50, as _ZNK12QQmlTypeData15compilationUnitEv
inline QV4::CompiledData::CompilationUnit *QQmlTypeData::compilationUnit() const
{
    return m_compiledData.data();
}

//  from ../qtdeclarative/src/qml/qml/qqmltype.cpp, line 20, as _ZN15QQmlTypePrivateC1EN8QQmlType16RegistrationTypeE
inline QQmlTypePrivate::QQmlTypePrivate(QQmlType::RegistrationType type)
    : regType(type)
{
    switch (type) {
    case QQmlType::CppType:
        extraData.cppTypeData = new QQmlCppTypeData;
        extraData.cppTypeData->allocationSize = 0;
        extraData.cppTypeData->newFunc = nullptr;
        extraData.cppTypeData->createValueTypeFunc = nullptr;
        extraData.cppTypeData->parserStatusCast = -1;
        extraData.cppTypeData->extFunc = nullptr;
        extraData.cppTypeData->extMetaObject = nullptr;
        extraData.cppTypeData->customParser = nullptr;
        extraData.cppTypeData->attachedPropertiesFunc = nullptr;
        extraData.cppTypeData->attachedPropertiesType = nullptr;
        extraData.cppTypeData->propertyValueSourceCast = -1;
        extraData.cppTypeData->propertyValueInterceptorCast = -1;
        extraData.cppTypeData->finalizerCast = -1;
        extraData.cppTypeData->registerEnumClassesUnscoped = true;
        extraData.cppTypeData->registerEnumsFromRelatedTypes = true;
        break;
    case QQmlType::SingletonType:
    case QQmlType::CompositeSingletonType:
        extraData.singletonTypeData = new QQmlSingletonTypeData;
        extraData.singletonTypeData->singletonInstanceInfo = nullptr;
        extraData.singletonTypeData->extFunc = nullptr;
        extraData.singletonTypeData->extMetaObject = nullptr;
        break;
    case QQmlType::InterfaceType:
        extraData.interfaceTypeData = nullptr;
        break;
    case QQmlType::CompositeType:
        new (&extraData.compositeTypeData) QUrl();
        break;
    case QQmlType::InlineComponentType:
        new (&extraData.inlineComponentTypeData) QUrl();
        break;
    case QQmlType::SequentialContainerType:
        new (&extraData.sequentialContainerTypeData) QMetaSequence();
        break;
    case QQmlType::JavaScriptType:
        new (&extraData.javaScriptTypeData) QUrl();
        break;
    default: qFatal("QQmlTypePrivate Internal Error.");
    }
}

//  from ../qtdeclarative/src/qml/qml/qqmltype.cpp, line 176, as _ZNK15QQmlTypePrivate4initEv
inline const QQmlTypePrivate::ProxyMetaObjects *QQmlTypePrivate::init() const
{
    if (const ProxyMetaObjects *result = proxyMetaObjects.loadRelaxed())
        return result;

    ProxyMetaObjects *proxies = new ProxyMetaObjects;
    auto finalize = [this, proxies]() -> const ProxyMetaObjects *{
        const ProxyMetaObjects *concurrentModification;
        if (proxyMetaObjects.testAndSetOrdered(nullptr, proxies, concurrentModification))
            return proxies;

        delete proxies;
        return concurrentModification;
    };

    const QMetaObject *mo = baseMetaObject;
    if (!mo) {
        // version 0 singleton type without metaobject information
        return finalize();
    }

    QList<QQmlProxyMetaObject::ProxyData> metaObjects;

    auto setupExtendedMetaObject = [&](const QMetaObject *extMetaObject,
                                       QObject *(*extFunc)(QObject *)) {
        if (!extMetaObject)
            return;

        // XXX - very inefficient
        QMetaObjectBuilder builder;
        QQmlMetaType::clone(builder, extMetaObject, extMetaObject, extMetaObject,
                            extFunc ? QQmlMetaType::CloneAll : QQmlMetaType::CloneEnumsOnly);
        QMetaObject *mmo = builder.toMetaObject();
        mmo->d.superdata = mo;
        QQmlProxyMetaObject::ProxyData data = { mmo, extFunc, 0, 0 };
        metaObjects << data;
        QQmlMetaType::registerMetaObjectForType(mmo, this);
    };

    if (regType == QQmlType::SingletonType)
        setupExtendedMetaObject(extraData.singletonTypeData->extMetaObject, extraData.singletonTypeData->extFunc);
    else if (regType == QQmlType::CppType)
        setupExtendedMetaObject(extraData.cppTypeData->extMetaObject, extraData.cppTypeData->extFunc);

    metaObjects.append(QQmlMetaType::proxyData(
            mo, baseMetaObject, metaObjects.isEmpty() ? nullptr
                                                      : metaObjects.constLast().metaObject));

    for (int ii = 0; ii < metaObjects.size(); ++ii) {
        metaObjects[ii].propertyOffset =
                metaObjects.at(ii).metaObject->propertyOffset();
        metaObjects[ii].methodOffset =
                metaObjects.at(ii).metaObject->methodOffset();
    }

    bool containsRevisionedAttributes = false;

    // Check for revisioned details
    {
        const QMetaObject *mo = nullptr;
        if (metaObjects.isEmpty())
            mo = baseMetaObject;
        else
            mo = metaObjects.constFirst().metaObject;

        for (int ii = 0; !containsRevisionedAttributes && ii < mo->propertyCount(); ++ii) {
            if (isPropertyRevisioned(mo, ii))
                containsRevisionedAttributes = true;
        }

        for (int ii = 0; !containsRevisionedAttributes && ii < mo->methodCount(); ++ii) {
            if (mo->method(ii).revision() != 0)
                containsRevisionedAttributes = true;
        }
    }

    proxies->data = std::move(metaObjects);
    proxies->containsRevisionedAttributes = containsRevisionedAttributes;

    return finalize();
}

//  from ../qtdeclarative/src/qml/qml/qqmltype.cpp, line 143, as _ZNK15QQmlTypePrivate24resolveCompositeBaseTypeEP14QQmlTypeLoader
inline QQmlType QQmlTypePrivate::resolveCompositeBaseType(QQmlTypeLoader *typeLoader) const
{
    Q_ASSERT(isComposite());
    if (!typeLoader)
        return QQmlType();
    QQmlRefPointer<QQmlTypeData> td(typeLoader->getType(sourceUrl()));
    if (td.isNull() || !td->isComplete())
        return QQmlType();
    QV4::CompiledData::CompilationUnit *compilationUnit = td->compilationUnit();
    if (const auto cache = compilationUnit->rootPropertyCache())
        return QQmlMetaType::qmlType(cache->firstCppMetaObject());
    return QQmlType();
}

//  from ../qtdeclarative/src/qml/qml/qqmltype.cpp, line 157, as _ZNK15QQmlTypePrivate22compositePropertyCacheEP14QQmlTypeLoader
inline QQmlPropertyCache::ConstPtr QQmlTypePrivate::compositePropertyCache(
        QQmlTypeLoader *typeLoader) const
{
    // similar logic to resolveCompositeBaseType
    Q_ASSERT(isComposite());
    if (!typeLoader)
        return nullptr;
    QQmlRefPointer<QQmlTypeData> td(typeLoader->getType(sourceUrl()));
    if (td.isNull() || !td->isComplete())
        return nullptr;
    QV4::CompiledData::CompilationUnit *compilationUnit = td->compilationUnit();
    return compilationUnit->rootPropertyCache();
}

//  from ../qtdeclarative/src/qml/qml/qqmltype.cpp, line 449, as _ZN15QQmlTypePrivate7setNameERK7QStringS2_
inline void QQmlTypePrivate::setName(const QString &uri, const QString &element)
{
    module = uri;
    elementName = element;
    name = uri.isEmpty() ? element : (uri + QLatin1Char('/') + element);
}

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

//  from ../qtdeclarative/src/qml/qml/qqmltype.cpp, line 258, as _ZNK15QQmlTypePrivate9initEnumsEP14QQmlTypeLoader
inline const QQmlTypePrivate::Enums *QQmlTypePrivate::initEnums(QQmlTypeLoader *typeLoader) const
{
    if (const Enums *result = enums.loadRelaxed())
        return result;

    QQmlPropertyCache::ConstPtr cache;
    if (isComposite()) {
        cache = compositePropertyCache(typeLoader);
        if (!cache)
            return nullptr; // Composite type not ready, yet.
    }

    Enums *newEnums = new Enums;

    // beware: It could be a singleton type without metaobject

    if (cache)
        insertEnumsFromPropertyCache(newEnums, cache);

    if (baseMetaObject) {
        // init() can add to the metaObjects list. Therefore, check proxies->data only below
        const ProxyMetaObjects *proxies = init();
        insertEnums(
                newEnums,
                proxies->data.isEmpty() ? baseMetaObject : proxies->data.constFirst().metaObject);
    }

    const Enums *concurrentModification;
    if (enums.testAndSetOrdered(nullptr, newEnums, concurrentModification))
        return newEnums;

    delete newEnums;
    return concurrentModification;
}

//  from ../qtdeclarative/src/qml/qml/qqmltype.cpp, line 293, as _ZNK15QQmlTypePrivate11insertEnumsEPNS_5EnumsEPK11QMetaObject
inline void QQmlTypePrivate::insertEnums(Enums *enums, const QMetaObject *metaObject) const
{
    // Add any enum values defined by 'related' classes
    if (regType != QQmlType::CppType || extraData.cppTypeData->registerEnumsFromRelatedTypes) {
        if (const auto *related = metaObject->d.relatedMetaObjects) {
            while (const QMetaObject *relatedMetaObject = *related) {
                insertEnums(enums, relatedMetaObject);
                ++related;
            }
        }
    }

    QSet<QString> localEnums;
    const QMetaObject *localMetaObject = nullptr;

    // ### TODO (QTBUG-123294): track this at instance creation time
    auto shouldSingletonAlsoRegisterUnscoped = [&](){
        Q_ASSERT(regType == QQmlType::SingletonType);
        if (!baseMetaObject)
            return true;
        int idx = baseMetaObject->indexOfClassInfo("RegisterEnumClassesUnscoped");
        if (idx == -1)
            return true;
        if (qstrcmp(baseMetaObject->classInfo(idx).value(), "false") == 0)
            return false;
        return true;
    };

    // Add any enum values defined by this class, overwriting any inherited values
    for (int ii = 0; ii < metaObject->enumeratorCount(); ++ii) {
        QMetaEnum me = metaObject->enumerator(ii);
        const bool isScoped = me.isScoped();
        QStringHash<int> *e = new QStringHash<int>();

    // We allow enums in sub-classes to overwrite enums from base-classes, such as
    // ListView.Center (from enum PositionMode) overwriting Item.Center (from enum TransformOrigin).
    // This is acceptable because the _use_ of the enum from the QML side requires qualification
    // anyway, i.e. ListView.Center vs. Item.Center.
        // However if a class defines two enums with the same value, then that must produce a warning
        // because it represents a valid conflict.
        if (me.enclosingMetaObject() != localMetaObject) {
            localEnums.clear();
            localMetaObject = me.enclosingMetaObject();
        }
        const bool shouldRegisterUnscoped = !isScoped
                || (regType == QQmlType::CppType && extraData.cppTypeData->registerEnumClassesUnscoped)
                || (regType == QQmlType::SingletonType && shouldSingletonAlsoRegisterUnscoped())
        ;

        for (int jj = 0; jj < me.keyCount(); ++jj) {
            const QString key = QString::fromUtf8(me.key(jj));
            const int value = me.value(jj);
            if (shouldRegisterUnscoped) {
                if (localEnums.contains(key)) {
                    auto existingEntry = enums->enums.find(key);
                    if (existingEntry != enums->enums.end() && existingEntry.value() != value) {
                        qWarning("Previously registered enum will be overwritten due to name clash: %s.%s", metaObject->className(), key.toUtf8().constData());
                        createEnumConflictReport(metaObject, key);
                    }
                } else {
                    localEnums.insert(key);
                }
                enums->enums.insert(key, value);
            }
            e->insert(key, value);
        }

        if (isScoped) {
            enums->scopedEnumIndex.insert(QString::fromUtf8(me.name()), enums->scopedEnums.size());
            enums->scopedEnums << e;
        } else {
            enums->unscopedEnumIndex.insert(QString::fromUtf8(me.name()), enums->unscopedEnums.size());
            enums->unscopedEnums << e;
        }
    }
}

//  from ../qtdeclarative/src/qml/qml/qqmltype.cpp, line 423, as _ZNK15QQmlTypePrivate28insertEnumsFromPropertyCacheEPNS_5EnumsERKN17QQmlPropertyCache8ConstPtrE
inline void QQmlTypePrivate::insertEnumsFromPropertyCache(
        Enums *enums, const QQmlPropertyCache::ConstPtr &cache) const
{
    const QMetaObject *cppMetaObject = cache->firstCppMetaObject();

    for (const QQmlPropertyCache *currentCache = cache.data();
         currentCache && currentCache->metaObject() != cppMetaObject;
         currentCache = currentCache->parent().data()) {

        int count = currentCache->ownEnumCount();
        for (int ii = 0; ii < count; ++ii) {
            QStringHash<int> *scoped = new QStringHash<int>();
            QQmlEnumData *enumData = currentCache->qmlEnum(ii);

            for (int jj = 0; jj < enumData->values.size(); ++jj) {
                const QQmlEnumValue &value = enumData->values.at(jj);
                enums->enums.insert(value.namedValue, value.value);
                scoped->insert(value.namedValue, value.value);
            }
            enums->scopedEnums << scoped;
            enums->scopedEnumIndex.insert(enumData->name, enums->scopedEnums.size()-1);
        }
    }
    insertEnums(enums, cppMetaObject);
}

//  from ../qtdeclarative/src/qml/qml/qqmltype.cpp, line 370, as _ZNK15QQmlTypePrivate36createListOfPossibleConflictingItemsEPK11QMetaObjectR5QListINS_8EnumInfoEES3_I7QStringE
inline void QQmlTypePrivate::createListOfPossibleConflictingItems(const QMetaObject *metaObject, QList<EnumInfo> &enumInfoList, QStringList path) const
{
    path.append(QString::fromUtf8(metaObject->className()));

    if (metaObject->d.relatedMetaObjects) {
        const auto *related = metaObject->d.relatedMetaObjects;
        if (related) {
            while (*related)
                createListOfPossibleConflictingItems(*related++, enumInfoList, path);
        }
    }

    for (int ii = 0; ii < metaObject->enumeratorCount(); ++ii) {
        const auto e = metaObject->enumerator(ii);

        for (int jj = 0; jj < e.keyCount(); ++jj) {
            const QString key = QString::fromUtf8(e.key(jj));

            EnumInfo enumInfo;
            enumInfo.metaObjectName = QString::fromUtf8(metaObject->className());
            enumInfo.enumName = QString::fromUtf8(e.name());
            enumInfo.enumKey = key;
            enumInfo.scoped = e.isScoped();
            enumInfo.path = path;
            enumInfo.metaEnumScope = QString::fromUtf8(e.scope());
            enumInfoList.append(enumInfo);
        }
    }
}

//  from ../qtdeclarative/src/qml/qml/qqmltype.cpp, line 400, as _ZNK15QQmlTypePrivate24createEnumConflictReportEPK11QMetaObjectRK7QString
inline void QQmlTypePrivate::createEnumConflictReport(const QMetaObject *metaObject, const QString &conflictingKey) const
{
    QList<EnumInfo> enumInfoList;

    if (baseMetaObject) // prefer baseMetaObject if available
        metaObject = baseMetaObject;

    if (!metaObject) { // If there is no metaObject at all return early
        qWarning() << "No meta object information available. Skipping conflict analysis.";
        return;
    }

    createListOfPossibleConflictingItems(metaObject, enumInfoList, QStringList());

    qWarning().noquote() << QLatin1String("Possible conflicting items:");
    // find items with conflicting key
    for (const auto &i : std::as_const(enumInfoList)) {
        if (i.enumKey == conflictingKey)
        qWarning().noquote().nospace() << "    " << i.metaObjectName << "." << i.enumName << "." << i.enumKey << " from scope "
                                           << i.metaEnumScope << " injected by " << i.path.join(QLatin1String("->"));
    }
}
//  -----------------------------------------------------------------------

//  QQmlTypePrivate::QQmlTypePrivate(QQmlType::RegistrationType type)
extern "C" Q_DECL_EXPORT
QQmlTypePrivate *ritual_ZN15QQmlTypePrivateC1EN8QQmlType16RegistrationTypeE(
    QQmlType::RegistrationType type) {
  return new QQmlTypePrivate(type);
}

//  const ProxyMetaObjects *QQmlTypePrivate::init() const
extern "C" Q_DECL_EXPORT
const QQmlTypePrivate::ProxyMetaObjects *ritual_ZNK15QQmlTypePrivate4initEv(
    const QQmlTypePrivate *self) {
  return self->init();
}

//  QUrl QQmlTypePrivate::sourceUrl() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK15QQmlTypePrivate9sourceUrlEv(const QQmlTypePrivate *self) {
  return new QUrl(self->sourceUrl());
}

//  const QQmlTypePrivate
//      *QQmlTypePrivate::attachedPropertiesBase(QQmlTypeLoader *typeLoader)
//      const
extern "C" Q_DECL_EXPORT
const QQmlTypePrivate *ritual_ZNK15QQmlTypePrivate22attachedPropertiesBaseEP14QQmlTypeLoader(
    const QQmlTypePrivate *self,
    QQmlTypeLoader *typeLoader) {
  return self->attachedPropertiesBase(typeLoader);
}

//  bool QQmlTypePrivate::isComposite() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QQmlTypePrivate11isCompositeEv(
    const QQmlTypePrivate *self) {
  return self->isComposite();
}

//  bool QQmlTypePrivate::isValueType() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QQmlTypePrivate11isValueTypeEv(
    const QQmlTypePrivate *self) {
  return self->isValueType();
}

//  QQmlType QQmlTypePrivate::resolveCompositeBaseType(QQmlTypeLoader
//      *typeLoader) const
extern "C" Q_DECL_EXPORT
QQmlType *ritual_ZNK15QQmlTypePrivate24resolveCompositeBaseTypeEP14QQmlTypeLoader(
    const QQmlTypePrivate *self,
    QQmlTypeLoader *typeLoader) {
  return new QQmlType(self->resolveCompositeBaseType(typeLoader));
}

//  QQmlPropertyCache::ConstPtr
//      QQmlTypePrivate::compositePropertyCache(QQmlTypeLoader *typeLoader)
//      const
extern "C" Q_DECL_EXPORT
QQmlPropertyCache::ConstPtr *ritual_ZNK15QQmlTypePrivate22compositePropertyCacheEP14QQmlTypeLoader(
    const QQmlTypePrivate *self,
    QQmlTypeLoader *typeLoader) {
  return new QQmlPropertyCache::ConstPtr(
      self->compositePropertyCache(
          typeLoader));
}

//  void QQmlTypePrivate::setName(const QString &uri, const QString &element)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQmlTypePrivate7setNameERK7QStringS2_(
    QQmlTypePrivate *self,
    const QString *uri,
    const QString *element) {
  self->setName(*uri, *element);
}

//  const QMetaObject *QQmlTypePrivate::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QQmlTypePrivate10metaObjectEv(
    const QQmlTypePrivate *self) {
  return self->metaObject();
}

//  const QMetaObject *QQmlTypePrivate::metaObjectForValueType() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QQmlTypePrivate22metaObjectForValueTypeEv(
    const QQmlTypePrivate *self) {
  return self->metaObjectForValueType();
}

//  QQmlType QQmlTypePrivate::visibleQmlTypeByName(const
//      QQmlRefPointer<QV4::CompiledData::CompilationUnit> &unit, const
//      QString &elementName, QQmlTypeLoader *typeLoader)
extern "C" Q_DECL_EXPORT
QQmlType *ritual_ZN15QQmlTypePrivate20visibleQmlTypeByNameERK14QQmlRefPointerIN3QV412CompiledData15CompilationUnitEERK7QStringP14QQmlTypeLoader(
    const QQmlRefPointer<QV4::CompiledData::CompilationUnit> *unit,
    const QString *elementName,
    QQmlTypeLoader *typeLoader) {
  return new QQmlType(
      QQmlTypePrivate::visibleQmlTypeByName(
          *unit,
          *elementName,
          typeLoader));
}

//  QQmlType QQmlTypePrivate::visibleQmlTypeByName(const
//      QV4::ExecutableCompilationUnit *unit, int elementNameId,
//      QQmlTypeLoader *typeLoader)
extern "C" Q_DECL_EXPORT
QQmlType *ritual_ZN15QQmlTypePrivate20visibleQmlTypeByNameEPKN3QV425ExecutableCompilationUnitEiP14QQmlTypeLoader(
    const QV4::ExecutableCompilationUnit *unit,
    int elementNameId,
    QQmlTypeLoader *typeLoader) {
  return new QQmlType(
      QQmlTypePrivate::visibleQmlTypeByName(
          unit,
          elementNameId,
          typeLoader));
}

//  QQmlTypePrivate::~QQmlTypePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQmlTypePrivateD1Ev(QQmlTypePrivate *self) {
  delete self;
}

//  const Enums *QQmlTypePrivate::initEnums(QQmlTypeLoader *typeLoader) const
extern "C" Q_DECL_EXPORT
const QQmlTypePrivate::Enums *ritual_ZNK15QQmlTypePrivate9initEnumsEP14QQmlTypeLoader(
    const QQmlTypePrivate *self,
    QQmlTypeLoader *typeLoader) {
  return self->initEnums(typeLoader);
}

//  void QQmlTypePrivate::insertEnums(Enums *enums, const QMetaObject
//      *metaObject) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK15QQmlTypePrivate11insertEnumsEPNS_5EnumsEPK11QMetaObject(
    const QQmlTypePrivate *self,
    QQmlTypePrivate::Enums *enums,
    const QMetaObject *metaObject) {
  self->insertEnums(enums, metaObject);
}

//  void QQmlTypePrivate::insertEnumsFromPropertyCache(Enums *enums, const
//      QQmlPropertyCache::ConstPtr &cache) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK15QQmlTypePrivate28insertEnumsFromPropertyCacheEPNS_5EnumsERKN17QQmlPropertyCache8ConstPtrE(
    const QQmlTypePrivate *self,
    QQmlTypePrivate::Enums *enums,
    const QQmlPropertyCache::ConstPtr *cache) {
  self->insertEnumsFromPropertyCache(enums, *cache);
}

//  void QQmlTypePrivate::createListOfPossibleConflictingItems(const
//      QMetaObject *metaObject, QList<EnumInfo> &enumInfoList, QStringList
//      path) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK15QQmlTypePrivate36createListOfPossibleConflictingItemsEPK11QMetaObjectR5QListINS_8EnumInfoEES3_I7QStringE(
    const QQmlTypePrivate *self,
    const QMetaObject *metaObject,
    QList<QQmlTypePrivate::EnumInfo> *enumInfoList,
    const QList<QString> *path) {
  self->createListOfPossibleConflictingItems(
      metaObject,
      *enumInfoList,
      *path);
}

//  void QQmlTypePrivate::createEnumConflictReport(const QMetaObject
//      *metaObject, const QString &conflictingKey) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK15QQmlTypePrivate24createEnumConflictReportEPK11QMetaObjectRK7QString(
    const QQmlTypePrivate *self,
    const QMetaObject *metaObject,
    const QString *conflictingKey) {
  self->createEnumConflictReport(metaObject, *conflictingKey);
}

//  static int QQmlTypePrivate::enumValue<QString>(
//      const QQmlRefPointer<const QQmlTypePrivate> &d,
//      QQmlTypeLoader *typeLoader, const QString &name, bool *ok)
extern "C" Q_DECL_EXPORT
int ritual_ZN15QQmlTypePrivate9enumValueI7QStringEEiRK14QQmlRefPointerIKS_EP14QQmlTypeLoaderRKT_Pb(
    const QQmlRefPointer<const QQmlTypePrivate> *d,
    QQmlTypeLoader *typeLoader,
    const QString *name,
    bool *ok) {
  return QQmlTypePrivate::enumValue<QString>(*d, typeLoader, *name, ok);
}

//  static int QQmlTypePrivate::enumIndex<Enums::Scoped, QString>(
//      const QQmlRefPointer<const QQmlTypePrivate> &d,
//      QQmlTypeLoader *typeLoader, const QString &name, bool *ok)
extern "C" Q_DECL_EXPORT
int ritual_ZN15QQmlTypePrivate9enumIndexILNS_5Enums7ScopingE0E7QStringEEiRK14QQmlRefPointerIKS_EP14QQmlTypeLoaderRKT0_Pb(
    const QQmlRefPointer<const QQmlTypePrivate> *d,
    QQmlTypeLoader *typeLoader,
    const QString *name,
    bool *ok) {
  return QQmlTypePrivate::enumIndex<
      QQmlTypePrivate::Enums::Scoped, QString>(
          *d, typeLoader, *name, ok);
}

//  static int QQmlTypePrivate::enumIndex<Enums::Unscoped, QString>(
//      const QQmlRefPointer<const QQmlTypePrivate> &d,
//      QQmlTypeLoader *typeLoader, const QString &name, bool *ok)
extern "C" Q_DECL_EXPORT
int ritual_ZN15QQmlTypePrivate9enumIndexILNS_5Enums7ScopingE1E7QStringEEiRK14QQmlRefPointerIKS_EP14QQmlTypeLoaderRKT0_Pb(
    const QQmlRefPointer<const QQmlTypePrivate> *d,
    QQmlTypeLoader *typeLoader,
    const QString *name,
    bool *ok) {
  return QQmlTypePrivate::enumIndex<
      QQmlTypePrivate::Enums::Unscoped, QString>(
          *d, typeLoader, *name, ok);
}

//  static int QQmlTypePrivate::enumValue<Enums::Scoped, QString>(
//      const QQmlRefPointer<const QQmlTypePrivate> &d,
//      QQmlTypeLoader *typeLoader, int index, const QString &name,
//      bool *ok)
extern "C" Q_DECL_EXPORT
int ritual_ZN15QQmlTypePrivate9enumValueILNS_5Enums7ScopingE0E7QStringEEiRK14QQmlRefPointerIKS_EP14QQmlTypeLoaderiRKT0_Pb(
    const QQmlRefPointer<const QQmlTypePrivate> *d,
    QQmlTypeLoader *typeLoader,
    int index,
    const QString *name,
    bool *ok) {
  return QQmlTypePrivate::enumValue<
      QQmlTypePrivate::Enums::Scoped, QString>(
          *d, typeLoader, index, *name, ok);
}

//  static int QQmlTypePrivate::enumValue<Enums::Unscoped, QString>(
//      const QQmlRefPointer<const QQmlTypePrivate> &d,
//      QQmlTypeLoader *typeLoader, int index, const QString &name,
//      bool *ok)
extern "C" Q_DECL_EXPORT
int ritual_ZN15QQmlTypePrivate9enumValueILNS_5Enums7ScopingE1E7QStringEEiRK14QQmlRefPointerIKS_EP14QQmlTypeLoaderiRKT0_Pb(
    const QQmlRefPointer<const QQmlTypePrivate> *d,
    QQmlTypeLoader *typeLoader,
    int index,
    const QString *name,
    bool *ok) {
  return QQmlTypePrivate::enumValue<
      QQmlTypePrivate::Enums::Unscoped, QString>(
          *d, typeLoader, index, *name, ok);
}

//  static int QQmlTypePrivate::enumValue<Enums::Scoped, QString,
//      QString>(const QQmlRefPointer<const QQmlTypePrivate> &d,
//      QQmlTypeLoader *typeLoader, const QString &scopedEnumName,
//      const QString &name, bool *ok)
extern "C" Q_DECL_EXPORT
int ritual_ZN15QQmlTypePrivate9enumValueILNS_5Enums7ScopingE0E7QStringS3_EEiRK14QQmlRefPointerIKS_EP14QQmlTypeLoaderRKT0_RKT1_Pb(
    const QQmlRefPointer<const QQmlTypePrivate> *d,
    QQmlTypeLoader *typeLoader,
    const QString *scopedEnumName,
    const QString *name,
    bool *ok) {
  return QQmlTypePrivate::enumValue<
      QQmlTypePrivate::Enums::Scoped, QString, QString>(
          *d, typeLoader, *scopedEnumName, *name, ok);
}

//  static int QQmlTypePrivate::enumValue<Enums::Unscoped, QString,
//      QString>(const QQmlRefPointer<const QQmlTypePrivate> &d,
//      QQmlTypeLoader *typeLoader, const QString &scopedEnumName,
//      const QString &name, bool *ok)
extern "C" Q_DECL_EXPORT
int ritual_ZN15QQmlTypePrivate9enumValueILNS_5Enums7ScopingE1E7QStringS3_EEiRK14QQmlRefPointerIKS_EP14QQmlTypeLoaderRKT0_RKT1_Pb(
    const QQmlRefPointer<const QQmlTypePrivate> *d,
    QQmlTypeLoader *typeLoader,
    const QString *scopedEnumName,
    const QString *name,
    bool *ok) {
  return QQmlTypePrivate::enumValue<
      QQmlTypePrivate::Enums::Unscoped, QString, QString>(
          *d, typeLoader, *scopedEnumName, *name, ok);
}

//  static QString QQmlTypePrivate::enumKey<Enums::Scoped>(
//      const QQmlRefPointer<const QQmlTypePrivate> &d,
//      QQmlTypeLoader *typeLoader, int index, int value, bool *ok)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QQmlTypePrivate7enumKeyILNS_5Enums7ScopingE0EEE7QStringRK14QQmlRefPointerIKS_EP14QQmlTypeLoaderiiPb(
    const QQmlRefPointer<const QQmlTypePrivate> *d,
    QQmlTypeLoader *typeLoader,
    int index,
    int value,
    bool *ok) {
  return new QString(QQmlTypePrivate::enumKey<
      QQmlTypePrivate::Enums::Scoped>(
          *d, typeLoader, index, value, ok));
}

//  static QString QQmlTypePrivate::enumKey<Enums::Unscoped>(
//      const QQmlRefPointer<const QQmlTypePrivate> &d,
//      QQmlTypeLoader *typeLoader, int index, int value, bool *ok)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QQmlTypePrivate7enumKeyILNS_5Enums7ScopingE1EEE7QStringRK14QQmlRefPointerIKS_EP14QQmlTypeLoaderiiPb(
    const QQmlRefPointer<const QQmlTypePrivate> *d,
    QQmlTypeLoader *typeLoader,
    int index,
    int value,
    bool *ok) {
  return new QString(QQmlTypePrivate::enumKey<
      QQmlTypePrivate::Enums::Unscoped>(
          *d, typeLoader, index, value, ok));
}
