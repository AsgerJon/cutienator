//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlmetatype_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlmetatype_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qurl.h>
#include <QtCore/qstring.h>
#include <QtQml/qqmlprivate.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmltype_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qtyperevision.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmldirparser_p.h>
#include <QtQml/6.12.0/QtQml/private/qhashedstring_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlpropertycache_p.h>
#include <QtQml/6.12.0/QtQml/private/qqmlmetaobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetaobject.h>
#include <QtCore/qvariant.h>
#include <QtCore/qlist.h>

//  QUrl QQmlMetaType::inlineComponentUrl(const QUrl &baseUrl, const QString
//      &name)
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZN12QQmlMetaType18inlineComponentUrlERK4QUrlRK7QString(
    const QUrl *baseUrl,
    const QString *name) {
  return new QUrl(QQmlMetaType::inlineComponentUrl(*baseUrl, *name));
}

//  bool QQmlMetaType::equalBaseUrls(const QUrl &aUrl, const QUrl &bUrl)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QQmlMetaType13equalBaseUrlsERK4QUrlS2_(
    const QUrl *aUrl,
    const QUrl *bUrl) {
  return QQmlMetaType::equalBaseUrls(*aUrl, *bUrl);
}

//  QUrl QQmlMetaType::normalizedUrl(const QUrl &unNormalizedUrl)
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZN12QQmlMetaType13normalizedUrlERK4QUrl(
    const QUrl *unNormalizedUrl) {
  return new QUrl(QQmlMetaType::normalizedUrl(*unNormalizedUrl));
}

//  QQmlType QQmlMetaType::registerType(const QQmlPrivate::RegisterType
//      &type)
extern "C" Q_DECL_EXPORT
QQmlType *ritual_ZN12QQmlMetaType12registerTypeERKN11QQmlPrivate12RegisterTypeE(
    const QQmlPrivate::RegisterType *type) {
  return new QQmlType(QQmlMetaType::registerType(*type));
}

//  QQmlType QQmlMetaType::registerInterface(const
//      QQmlPrivate::RegisterInterface &type)
extern "C" Q_DECL_EXPORT
QQmlType *ritual_ZN12QQmlMetaType17registerInterfaceERKN11QQmlPrivate17RegisterInterfaceE(
    const QQmlPrivate::RegisterInterface *type) {
  return new QQmlType(QQmlMetaType::registerInterface(*type));
}

//  QQmlType QQmlMetaType::registerCompositeType(const
//      QQmlPrivate::RegisterCompositeType &type)
extern "C" Q_DECL_EXPORT
QQmlType *ritual_ZN12QQmlMetaType21registerCompositeTypeERKN11QQmlPrivate21RegisterCompositeTypeE(
    const QQmlPrivate::RegisterCompositeType *type) {
  return new QQmlType(QQmlMetaType::registerCompositeType(*type));
}

//  QQmlType QQmlMetaType::findOrCreateSpeculativeInlineComponentType(const
//      QUrl &url)
extern "C" Q_DECL_EXPORT
QQmlType *ritual_ZN12QQmlMetaType42findOrCreateSpeculativeInlineComponentTypeERK4QUrl(
    const QUrl *url) {
  return new QQmlType(
      QQmlMetaType::findOrCreateSpeculativeInlineComponentType(
          *url));
}

//  QQmlType QQmlMetaType::findOrCreateSpeculativeInlineComponentType(const
//      QQmlType &outerType, const QString &name)
extern "C" Q_DECL_EXPORT
QQmlType *ritual_ZN12QQmlMetaType42findOrCreateSpeculativeInlineComponentTypeERK8QQmlTypeRK7QString(
    const QQmlType *outerType,
    const QString *name) {
  return new QQmlType(
      QQmlMetaType::findOrCreateSpeculativeInlineComponentType(
          *outerType,
          *name));
}

//  void QQmlMetaType::unregisterType(int type)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQmlMetaType14unregisterTypeEi(int type) {
  QQmlMetaType::unregisterType(type);
}

//  void QQmlMetaType::registerMetaObjectForType(const QMetaObject
//      *metaobject, const QQmlTypePrivate *type)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQmlMetaType25registerMetaObjectForTypeEPK11QMetaObjectPK15QQmlTypePrivate(
    const QMetaObject *metaobject,
    const QQmlTypePrivate *type) {
  QQmlMetaType::registerMetaObjectForType(metaobject, type);
}

//  void QQmlMetaType::registerModule(const char *uri, QTypeRevision version)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQmlMetaType14registerModuleEPKc13QTypeRevision(
    const char *uri,
    const QTypeRevision *version) {
  QQmlMetaType::registerModule(uri, *version);
}

//  bool QQmlMetaType::protectModule(const QString &uri, QTypeRevision
//      version, bool weakProtectAllVersions)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QQmlMetaType13protectModuleERK7QString13QTypeRevisionb(
    const QString *uri,
    const QTypeRevision *version,
    bool weakProtectAllVersions) {
  return QQmlMetaType::protectModule(*uri, *version, weakProtectAllVersions);
}

//  void QQmlMetaType::registerModuleImport(const QString &uri, QTypeRevision
//      version, const QQmlDirParser::Import &import)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQmlMetaType20registerModuleImportERK7QString13QTypeRevisionRKN13QQmlDirParser6ImportE(
    const QString *uri,
    const QTypeRevision *version,
    const QQmlDirParser::Import *import) {
  QQmlMetaType::registerModuleImport(*uri, *version, *import);
}

//  void QQmlMetaType::unregisterModuleImport(const QString &uri,
//      QTypeRevision version, const QQmlDirParser::Import &import)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQmlMetaType22unregisterModuleImportERK7QString13QTypeRevisionRKN13QQmlDirParser6ImportE(
    const QString *uri,
    const QTypeRevision *version,
    const QQmlDirParser::Import *import) {
  QQmlMetaType::unregisterModuleImport(*uri, *version, *import);
}

//  int QQmlMetaType::typeId(const char *uri, QTypeRevision version, const
//      char *qmlName)
extern "C" Q_DECL_EXPORT
int ritual_ZN12QQmlMetaType6typeIdEPKc13QTypeRevisionS1_(
    const char *uri,
    const QTypeRevision *version,
    const char *qmlName) {
  return QQmlMetaType::typeId(uri, *version, qmlName);
}

//  void QQmlMetaType::registerUndeletableType(const QQmlType &dtype)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQmlMetaType23registerUndeletableTypeERK8QQmlType(
    const QQmlType *dtype) {
  QQmlMetaType::registerUndeletableType(*dtype);
}

//  QList<QString> QQmlMetaType::qmlTypeNames()
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZN12QQmlMetaType12qmlTypeNamesEv() {
  return new QList<QString>(QQmlMetaType::qmlTypeNames());
}

//  QList<QQmlType> QQmlMetaType::qmlTypes()
extern "C" Q_DECL_EXPORT
QList<QQmlType> *ritual_ZN12QQmlMetaType8qmlTypesEv() {
  return new QList<QQmlType>(QQmlMetaType::qmlTypes());
}

//  QList<QQmlType> QQmlMetaType::qmlSingletonTypes()
extern "C" Q_DECL_EXPORT
QList<QQmlType> *ritual_ZN12QQmlMetaType17qmlSingletonTypesEv() {
  return new QList<QQmlType>(QQmlMetaType::qmlSingletonTypes());
}

//  QList<QQmlType> QQmlMetaType::qmlAllTypes()
extern "C" Q_DECL_EXPORT
QList<QQmlType> *ritual_ZN12QQmlMetaType11qmlAllTypesEv() {
  return new QList<QQmlType>(QQmlMetaType::qmlAllTypes());
}

//  QQmlType QQmlMetaType::qmlType(const QString &qualifiedName,
//      QTypeRevision version)
extern "C" Q_DECL_EXPORT
QQmlType *ritual_ZN12QQmlMetaType7qmlTypeERK7QString13QTypeRevision(
    const QString *qualifiedName,
    const QTypeRevision *version) {
  return new QQmlType(QQmlMetaType::qmlType(*qualifiedName, *version));
}

//  QQmlType QQmlMetaType::qmlType(const QHashedStringRef &name, const
//      QHashedStringRef &module, QTypeRevision version)
extern "C" Q_DECL_EXPORT
QQmlType *ritual_ZN12QQmlMetaType7qmlTypeERK16QHashedStringRefS2_13QTypeRevision(
    const QHashedStringRef *name,
    const QHashedStringRef *module,
    const QTypeRevision *version) {
  return new QQmlType(QQmlMetaType::qmlType(*name, *module, *version));
}

//  QQmlType QQmlMetaType::qmlType(const QMetaObject *a0)
extern "C" Q_DECL_EXPORT
QQmlType *ritual_ZN12QQmlMetaType7qmlTypeEPK11QMetaObject(
    const QMetaObject *a0) {
  return new QQmlType(QQmlMetaType::qmlType(a0));
}

//  QQmlType QQmlMetaType::qmlType(const QMetaObject *metaObject, const
//      QHashedStringRef &module, QTypeRevision version)
extern "C" Q_DECL_EXPORT
QQmlType *ritual_ZN12QQmlMetaType7qmlTypeEPK11QMetaObjectRK16QHashedStringRef13QTypeRevision(
    const QMetaObject *metaObject,
    const QHashedStringRef *module,
    const QTypeRevision *version) {
  return new QQmlType(QQmlMetaType::qmlType(metaObject, *module, *version));
}

//  QQmlType QQmlMetaType::qmlTypeById(int qmlTypeId)
extern "C" Q_DECL_EXPORT
QQmlType *ritual_ZN12QQmlMetaType11qmlTypeByIdEi(int qmlTypeId) {
  return new QQmlType(QQmlMetaType::qmlTypeById(qmlTypeId));
}

//  QQmlType QQmlMetaType::firstQmlTypeForAttachmentMetaObject(const
//      QMetaObject *attachmentMetaObject)
extern "C" Q_DECL_EXPORT
QQmlType *ritual_ZN12QQmlMetaType35firstQmlTypeForAttachmentMetaObjectEPK11QMetaObject(
    const QMetaObject *attachmentMetaObject) {
  return new QQmlType(
      QQmlMetaType::firstQmlTypeForAttachmentMetaObject(
          attachmentMetaObject));
}

//  QQmlType QQmlMetaType::qmlType(QMetaType metaType)
extern "C" Q_DECL_EXPORT
QQmlType *ritual_ZN12QQmlMetaType7qmlTypeE9QMetaType(
    const QMetaType *metaType) {
  return new QQmlType(QQmlMetaType::qmlType(*metaType));
}

//  QQmlType QQmlMetaType::qmlListType(QMetaType metaType)
extern "C" Q_DECL_EXPORT
QQmlType *ritual_ZN12QQmlMetaType11qmlListTypeE9QMetaType(
    const QMetaType *metaType) {
  return new QQmlType(QQmlMetaType::qmlListType(*metaType));
}

//  QQmlType QQmlMetaType::qmlType(const QUrl &unNormalizedUrl)
extern "C" Q_DECL_EXPORT
QQmlType *ritual_ZN12QQmlMetaType7qmlTypeERK4QUrl(
    const QUrl *unNormalizedUrl) {
  return new QQmlType(QQmlMetaType::qmlType(*unNormalizedUrl));
}

//  QQmlPropertyCache::ConstPtr QQmlMetaType::propertyCache(QObject *object,
//      QTypeRevision version)
extern "C" Q_DECL_EXPORT
QQmlPropertyCache::ConstPtr *ritual_ZN12QQmlMetaType13propertyCacheEP7QObject13QTypeRevision(
    QObject *object,
    const QTypeRevision *version) {
  return new QQmlPropertyCache::ConstPtr(
      QQmlMetaType::propertyCache(
          object,
          *version));
}

//  QQmlPropertyCache::ConstPtr QQmlMetaType::propertyCache(const QMetaObject
//      *metaObject, QTypeRevision version)
extern "C" Q_DECL_EXPORT
QQmlPropertyCache::ConstPtr *ritual_ZN12QQmlMetaType13propertyCacheEPK11QMetaObject13QTypeRevision(
    const QMetaObject *metaObject,
    const QTypeRevision *version) {
  return new QQmlPropertyCache::ConstPtr(
      QQmlMetaType::propertyCache(
          metaObject,
          *version));
}

//  QQmlPropertyCache::ConstPtr QQmlMetaType::propertyCache(const QQmlType
//      &type, QTypeRevision version)
extern "C" Q_DECL_EXPORT
QQmlPropertyCache::ConstPtr *ritual_ZN12QQmlMetaType13propertyCacheERK8QQmlType13QTypeRevision(
    const QQmlType *type,
    const QTypeRevision *version) {
  return new QQmlPropertyCache::ConstPtr(
      QQmlMetaType::propertyCache(
          *type,
          *version));
}

//  QQmlMetaObject QQmlMetaType::rawMetaObjectForType(QMetaType metaType)
extern "C" Q_DECL_EXPORT
QQmlMetaObject *ritual_ZN12QQmlMetaType20rawMetaObjectForTypeE9QMetaType(
    const QMetaType *metaType) {
  return new QQmlMetaObject(QQmlMetaType::rawMetaObjectForType(*metaType));
}

//  QQmlMetaObject QQmlMetaType::metaObjectForType(QMetaType metaType)
extern "C" Q_DECL_EXPORT
QQmlMetaObject *ritual_ZN12QQmlMetaType17metaObjectForTypeE9QMetaType(
    const QMetaType *metaType) {
  return new QQmlMetaObject(QQmlMetaType::metaObjectForType(*metaType));
}

//  QQmlPropertyCache::ConstPtr QQmlMetaType::propertyCacheForType(QMetaType
//      metaType)
extern "C" Q_DECL_EXPORT
QQmlPropertyCache::ConstPtr *ritual_ZN12QQmlMetaType20propertyCacheForTypeE9QMetaType(
    const QMetaType *metaType) {
  return new QQmlPropertyCache::ConstPtr(
      QQmlMetaType::propertyCacheForType(
          *metaType));
}

//  QQmlPropertyCache::ConstPtr
//      QQmlMetaType::rawPropertyCacheForType(QMetaType metaType)
extern "C" Q_DECL_EXPORT
QQmlPropertyCache::ConstPtr *ritual_ZN12QQmlMetaType23rawPropertyCacheForTypeE9QMetaType(
    const QMetaType *metaType) {
  return new QQmlPropertyCache::ConstPtr(
      QQmlMetaType::rawPropertyCacheForType(
          *metaType));
}

//  QQmlPropertyCache::ConstPtr
//      QQmlMetaType::rawPropertyCacheForType(QMetaType metaType,
//      QTypeRevision version)
extern "C" Q_DECL_EXPORT
QQmlPropertyCache::ConstPtr *ritual_ZN12QQmlMetaType23rawPropertyCacheForTypeE9QMetaType13QTypeRevision(
    const QMetaType *metaType,
    const QTypeRevision *version) {
  return new QQmlPropertyCache::ConstPtr(
      QQmlMetaType::rawPropertyCacheForType(
          *metaType,
          *version));
}

//  bool QQmlMetaType::canConvert(QObject *o, QMetaType metaType)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QQmlMetaType10canConvertEP7QObject9QMetaType(
    QObject *o,
    const QMetaType *metaType) {
  return QQmlMetaType::canConvert(o, *metaType);
}

//  bool QQmlMetaType::canConvert(const QQmlPropertyCache::ConstPtr &from,
//      QMetaType metaType)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QQmlMetaType10canConvertERKN17QQmlPropertyCache8ConstPtrE9QMetaType(
    const QQmlPropertyCache::ConstPtr *from,
    const QMetaType *metaType) {
  return QQmlMetaType::canConvert(*from, *metaType);
}

//  void QQmlMetaType::freeUnusedTypesAndCaches()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQmlMetaType24freeUnusedTypesAndCachesEv() {
  QQmlMetaType::freeUnusedTypesAndCaches();
}

//  QMetaProperty QQmlMetaType::defaultProperty(const QMetaObject *a0)
extern "C" Q_DECL_EXPORT
QMetaProperty *ritual_ZN12QQmlMetaType15defaultPropertyEPK11QMetaObject(
    const QMetaObject *a0) {
  return new QMetaProperty(QQmlMetaType::defaultProperty(a0));
}

//  QMetaProperty QQmlMetaType::defaultProperty(QObject *a0)
extern "C" Q_DECL_EXPORT
QMetaProperty *ritual_ZN12QQmlMetaType15defaultPropertyEP7QObject(
    QObject *a0) {
  return new QMetaProperty(QQmlMetaType::defaultProperty(a0));
}

//  QMetaMethod QQmlMetaType::defaultMethod(const QMetaObject *a0)
extern "C" Q_DECL_EXPORT
QMetaMethod *ritual_ZN12QQmlMetaType13defaultMethodEPK11QMetaObject(
    const QMetaObject *a0) {
  return new QMetaMethod(QQmlMetaType::defaultMethod(a0));
}

//  QMetaMethod QQmlMetaType::defaultMethod(QObject *a0)
extern "C" Q_DECL_EXPORT
QMetaMethod *ritual_ZN12QQmlMetaType13defaultMethodEP7QObject(QObject *a0) {
  return new QMetaMethod(QQmlMetaType::defaultMethod(a0));
}

//  QObject *QQmlMetaType::toQObject(const QVariant &a0, bool *ok)
extern "C" Q_DECL_EXPORT
QObject *ritual_ZN12QQmlMetaType9toQObjectERK8QVariantPb(
    const QVariant *a0,
    bool *ok) {
  return QQmlMetaType::toQObject(*a0, ok);
}

//  QMetaType QQmlMetaType::listValueType(QMetaType type)
extern "C" Q_DECL_EXPORT
QMetaType *ritual_ZN12QQmlMetaType13listValueTypeE9QMetaType(
    const QMetaType *type) {
  return new QMetaType(QQmlMetaType::listValueType(*type));
}

//  bool QQmlMetaType::isInterface(QMetaType type)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QQmlMetaType11isInterfaceE9QMetaType(const QMetaType *type) {
  return QQmlMetaType::isInterface(*type);
}

//  const char *QQmlMetaType::interfaceIId(QMetaType type)
extern "C" Q_DECL_EXPORT
const char *ritual_ZN12QQmlMetaType12interfaceIIdE9QMetaType(
    const QMetaType *type) {
  return QQmlMetaType::interfaceIId(*type);
}

//  bool QQmlMetaType::isList(QMetaType type)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QQmlMetaType6isListE9QMetaType(const QMetaType *type) {
  return QQmlMetaType::isList(*type);
}

//  QTypeRevision QQmlMetaType::latestModuleVersion(const QString &uri)
extern "C" Q_DECL_EXPORT
QTypeRevision *ritual_ZN12QQmlMetaType19latestModuleVersionERK7QString(
    const QString *uri) {
  return new QTypeRevision(QQmlMetaType::latestModuleVersion(*uri));
}

//  bool QQmlMetaType::isStronglyLockedModule(const QString &uri,
//      QTypeRevision version)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QQmlMetaType22isStronglyLockedModuleERK7QString13QTypeRevision(
    const QString *uri,
    const QTypeRevision *version) {
  return QQmlMetaType::isStronglyLockedModule(*uri, *version);
}

//  QTypeRevision QQmlMetaType::matchingModuleVersion(const QString &module,
//      QTypeRevision version)
extern "C" Q_DECL_EXPORT
QTypeRevision *ritual_ZN12QQmlMetaType21matchingModuleVersionERK7QString13QTypeRevision(
    const QString *module,
    const QTypeRevision *version) {
  return new QTypeRevision(
      QQmlMetaType::matchingModuleVersion(
          *module,
          *version));
}

//  QQmlTypeModule *QQmlMetaType::typeModule(const QString &uri,
//      QTypeRevision version)
extern "C" Q_DECL_EXPORT
QQmlTypeModule *ritual_ZN12QQmlMetaType10typeModuleERK7QString13QTypeRevision(
    const QString *uri,
    const QTypeRevision *version) {
  return QQmlMetaType::typeModule(*uri, *version);
}

//  QString QQmlMetaType::prettyTypeName(const QObject *object)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN12QQmlMetaType14prettyTypeNameEPK7QObject(
    const QObject *object) {
  return new QString(QQmlMetaType::prettyTypeName(object));
}

//  void QQmlMetaType::registerTypeAlias(int typeId, const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQmlMetaType17registerTypeAliasEiRK7QString(
    int typeId,
    const QString *name) {
  QQmlMetaType::registerTypeAlias(typeId, *name);
}

//  int QQmlMetaType::registerAutoParentFunction(const
//      QQmlPrivate::RegisterAutoParent &autoparent)
extern "C" Q_DECL_EXPORT
int ritual_ZN12QQmlMetaType26registerAutoParentFunctionERKN11QQmlPrivate18RegisterAutoParentE(
    const QQmlPrivate::RegisterAutoParent *autoparent) {
  return QQmlMetaType::registerAutoParentFunction(*autoparent);
}

//  QQmlType QQmlMetaType::registerSequentialContainer(const
//      QQmlPrivate::RegisterSequentialContainer &sequenceRegistration)
extern "C" Q_DECL_EXPORT
QQmlType *ritual_ZN12QQmlMetaType27registerSequentialContainerERKN11QQmlPrivate27RegisterSequentialContainerE(
    const QQmlPrivate::RegisterSequentialContainer *sequenceRegistration) {
  return new QQmlType(
      QQmlMetaType::registerSequentialContainer(
          *sequenceRegistration));
}

//  void QQmlMetaType::unregisterSequentialContainer(int id)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQmlMetaType29unregisterSequentialContainerEi(int id) {
  QQmlMetaType::unregisterSequentialContainer(id);
}

//  int QQmlMetaType::registerUnitCacheHook(const
//      QQmlPrivate::RegisterQmlUnitCacheHook &hookRegistration)
extern "C" Q_DECL_EXPORT
int ritual_ZN12QQmlMetaType21registerUnitCacheHookERKN11QQmlPrivate24RegisterQmlUnitCacheHookE(
    const QQmlPrivate::RegisterQmlUnitCacheHook *hookRegistration) {
  return QQmlMetaType::registerUnitCacheHook(*hookRegistration);
}

//  void QQmlMetaType::clearTypeRegistrations()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQmlMetaType22clearTypeRegistrationsEv() {
  QQmlMetaType::clearTypeRegistrations();
}

//  void QQmlMetaType::qmlRemoveModuleRegistration(const QString &uri)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQmlMetaType27qmlRemoveModuleRegistrationERK7QString(
    const QString *uri) {
  QQmlMetaType::qmlRemoveModuleRegistration(*uri);
}

//  bool QQmlMetaType::qmlRegisterModuleTypes(const QString &uri)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QQmlMetaType22qmlRegisterModuleTypesERK7QString(
    const QString *uri) {
  return QQmlMetaType::qmlRegisterModuleTypes(*uri);
}

//  bool QQmlMetaType::isValueType(QMetaType type)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QQmlMetaType11isValueTypeE9QMetaType(const QMetaType *type) {
  return QQmlMetaType::isValueType(*type);
}

//  QQmlValueType *QQmlMetaType::valueType(QMetaType metaType)
extern "C" Q_DECL_EXPORT
QQmlValueType *ritual_ZN12QQmlMetaType9valueTypeE9QMetaType(
    const QMetaType *metaType) {
  return QQmlMetaType::valueType(*metaType);
}

//  const QMetaObject *QQmlMetaType::metaObjectForValueType(QMetaType type)
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZN12QQmlMetaType22metaObjectForValueTypeE9QMetaType(
    const QMetaType *type) {
  return QQmlMetaType::metaObjectForValueType(*type);
}

//  QQmlPropertyCache::ConstPtr
//      QQmlMetaType::findPropertyCacheInCompositeTypes(QMetaType t)
extern "C" Q_DECL_EXPORT
QQmlPropertyCache::ConstPtr *ritual_ZN12QQmlMetaType33findPropertyCacheInCompositeTypesE9QMetaType(
    const QMetaType *t) {
  return new QQmlPropertyCache::ConstPtr(
      QQmlMetaType::findPropertyCacheInCompositeTypes(
          *t));
}

//  QQmlMetaType::~QQmlMetaType()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQmlMetaTypeD1Ev(QQmlMetaType *self) {
  delete self;
}
