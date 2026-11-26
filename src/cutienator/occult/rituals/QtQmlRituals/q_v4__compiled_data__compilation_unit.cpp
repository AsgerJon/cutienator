//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4compileddata_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4compileddata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtCore/qdatetime.h>
#include <QtCore/qmetatype.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlpropertycache_p.h>
#include <QtQml/6.12.0/QtQml/private/qqmltype_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qlist.h>
#include <QtCore/QUrl>
#include <QtCore/QDateTime>
#include <QtCore/QByteArray>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
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
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/common/qv4compileddata.cpp, line 249, as _ZNK3QV412CompiledData15CompilationUnit12resolvedTypeE9QMetaType
namespace QV4::CompiledData {
inline ResolvedTypeReference *CompilationUnit::resolvedType(QMetaType type) const
{
    for (ResolvedTypeReference *ref : std::as_const(resolvedTypes)) {
        if (ref->type().typeId() == type)
            return ref;
    }
    return nullptr;

}
}  // namespace QV4::CompiledData

//  from ../qtdeclarative/src/qml/common/qv4compileddata.cpp, line 259, as _ZN3QV412CompiledData15CompilationUnit21finalizeCompositeTypeERK8QQmlType
namespace QV4 {
inline void CompiledData::CompilationUnit::finalizeCompositeType(const QQmlType &type)
{
    // Add to type registry of composites
    if (propertyCaches.needsVMEMetaObject(/*root object*/0)) {
        // qmlType is only valid for types that have references to themselves.
        if (type.isValid()) {
            qmlType = type;
        } else {
            qmlType = QQmlMetaType::findCompositeType(
                    url(), this, (unitData()->flags & CompiledData::Unit::IsSingleton)
                            ? QQmlMetaType::Singleton
                            : QQmlMetaType::NonSingleton);
        }

        QQmlMetaType::registerInternalCompositeType(this);
    } else {
        const QV4::CompiledData::Object *obj = objectAt(/*root object*/0);
        auto *typeRef = resolvedTypes.value(obj->inheritedTypeNameIndex);
        Q_ASSERT(typeRef);
        qmlType = typeRef->type();
    }
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/common/qv4compileddata.cpp, line 282, as _ZNK3QV412CompiledData15CompilationUnit14verifyChecksumERKSt8functionIF10QByteArrayvEE
namespace QV4::CompiledData {
inline bool CompilationUnit::verifyChecksum(const DependentTypesHasher &dependencyHasher) const
{
    if (!dependencyHasher) {
        for (size_t i = 0; i < sizeof(data->dependencyMD5Checksum); ++i) {
            if (data->dependencyMD5Checksum[i] != 0)
                return false;
        }
        return true;
    }
    const QByteArray checksum = dependencyHasher();
    return checksum.size() == sizeof(data->dependencyMD5Checksum)
            && memcmp(data->dependencyMD5Checksum, checksum.constData(),
                      sizeof(data->dependencyMD5Checksum)) == 0;
}
}  // namespace QV4::CompiledData

//  from ../qtdeclarative/src/qml/common/qv4compileddata.cpp, line 297, as _ZNK3QV412CompiledData15CompilationUnit19qmlTypeForComponentERK7QString
namespace QV4::CompiledData {
inline QQmlType CompilationUnit::qmlTypeForComponent(const QString &inlineComponentName) const
{
    if (inlineComponentName.isEmpty())
        return qmlType;
    return inlineComponentData[inlineComponentName].qmlType;
}
}  // namespace QV4::CompiledData
//  -----------------------------------------------------------------------

//  QV4::CompiledData::CompilationUnit::CompilationUnit(const Unit *unitData,
//      const QQmlPrivate::AOTCompiledFunction *aotCompiledFunctions,
//      LookupValidationFn validateLookupSignatures, const QString &fileName,
//      const QString &finalUrlString)
extern "C" Q_DECL_EXPORT
QV4::CompiledData::CompilationUnit *ritual_ZN3QV412CompiledData15CompilationUnitC1EPKNS0_4UnitEPKN11QQmlPrivate19AOTCompiledFunctionEPFbP10QQmlEnginePS1_ERK7QStringSG_(
    const QV4::CompiledData::Unit *unitData,
    const QQmlPrivate::AOTCompiledFunction *aotCompiledFunctions,
    void *validateLookupSignatures,
    const QString *fileName,
    const QString *finalUrlString) {
  return new QV4::CompiledData::CompilationUnit(
      unitData,
      aotCompiledFunctions,
      reinterpret_cast<QV4::CompiledData::LookupValidationFn>(validateLookupSignatures),
      *fileName,
      *finalUrlString);
}

//  QV4::CompiledData::CompilationUnit::CompilationUnit(const Unit *unitData,
//      const QString &fileName, const QString &finalUrlString)
extern "C" Q_DECL_EXPORT
QV4::CompiledData::CompilationUnit *ritual_ZN3QV412CompiledData15CompilationUnitC1EPKNS0_4UnitERK7QStringS7_(
    const QV4::CompiledData::Unit *unitData,
    const QString *fileName,
    const QString *finalUrlString) {
  return new QV4::CompiledData::CompilationUnit(
      unitData,
      *fileName,
      *finalUrlString);
}

//  QV4::CompiledData::CompilationUnit::~CompilationUnit()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV412CompiledData15CompilationUnitD1Ev(
    QV4::CompiledData::CompilationUnit *self) {
  delete self;
}

//  const Unit *QV4::CompiledData::CompilationUnit::unitData() const
extern "C" Q_DECL_EXPORT
const QV4::CompiledData::Unit *ritual_ZNK3QV412CompiledData15CompilationUnit8unitDataEv(
    const QV4::CompiledData::CompilationUnit *self) {
  return self->unitData();
}

//  void QV4::CompiledData::CompilationUnit::setUnitData(const Unit
//      *unitData, const QmlUnit *qmlUnit, const QString &fileName, const
//      QString &finalUrlString)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV412CompiledData15CompilationUnit11setUnitDataEPKNS0_4UnitEPKNS0_7QmlUnitERK7QStringSA_(
    QV4::CompiledData::CompilationUnit *self,
    const QV4::CompiledData::Unit *unitData,
    const QV4::CompiledData::QmlUnit *qmlUnit,
    const QString *fileName,
    const QString *finalUrlString) {
  self->setUnitData(unitData, qmlUnit, *fileName, *finalUrlString);
}

//  QString QV4::CompiledData::CompilationUnit::stringAt(uint index) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK3QV412CompiledData15CompilationUnit8stringAtEj(
    const QV4::CompiledData::CompilationUnit *self,
    uint index) {
  return new QString(self->stringAt(index));
}

//  QString QV4::CompiledData::CompilationUnit::fileName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK3QV412CompiledData15CompilationUnit8fileNameEv(
    const QV4::CompiledData::CompilationUnit *self) {
  return new QString(self->fileName());
}

//  QString QV4::CompiledData::CompilationUnit::finalUrlString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK3QV412CompiledData15CompilationUnit14finalUrlStringEv(
    const QV4::CompiledData::CompilationUnit *self) {
  return new QString(self->finalUrlString());
}

//  QString QV4::CompiledData::CompilationUnit::bindingValueAsString(const
//      CompiledData::Binding *binding) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK3QV412CompiledData15CompilationUnit20bindingValueAsStringEPKNS0_7BindingE(
    const QV4::CompiledData::CompilationUnit *self,
    const QV4::CompiledData::Binding *binding) {
  return new QString(self->bindingValueAsString(binding));
}

//  QString
//      QV4::CompiledData::CompilationUnit::bindingValueAsScriptString(const
//      CompiledData::Binding *binding) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK3QV412CompiledData15CompilationUnit26bindingValueAsScriptStringEPKNS0_7BindingE(
    const QV4::CompiledData::CompilationUnit *self,
    const QV4::CompiledData::Binding *binding) {
  return new QString(self->bindingValueAsScriptString(binding));
}

//  double QV4::CompiledData::CompilationUnit::bindingValueAsNumber(const
//      CompiledData::Binding *binding) const
extern "C" Q_DECL_EXPORT
double ritual_ZNK3QV412CompiledData15CompilationUnit20bindingValueAsNumberEPKNS0_7BindingE(
    const QV4::CompiledData::CompilationUnit *self,
    const QV4::CompiledData::Binding *binding) {
  return self->bindingValueAsNumber(binding);
}

//  QString QV4::CompiledData::CompilationUnit::localCacheFilePath(const QUrl
//      &url)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN3QV412CompiledData15CompilationUnit18localCacheFilePathERK4QUrl(
    const QUrl *url) {
  return new QString(
      QV4::CompiledData::CompilationUnit::localCacheFilePath(
          *url));
}

//  bool QV4::CompiledData::CompilationUnit::loadFromDisk(const QUrl &url,
//      const QDateTime &sourceTimeStamp, qxp::function_ref<QByteArray ()
//      const> sourceChecksum, QString *errorString)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV412CompiledData15CompilationUnit12loadFromDiskERK4QUrlRK9QDateTimeN3qxp12function_refIJKF10QByteArrayvEEEEP7QString(
    QV4::CompiledData::CompilationUnit *self,
    const QUrl *url,
    const QDateTime *sourceTimeStamp,
    const qxp::function_ref<QByteArray () const> *sourceChecksum,
    QString *errorString) {
  return self->loadFromDisk(
      *url,
      *sourceTimeStamp,
      *sourceChecksum,
      errorString);
}

//  bool QV4::CompiledData::CompilationUnit::saveToDisk(const QUrl &unitUrl,
//      qxp::function_ref<QByteArray () const> sourceChecksum, QString
//      *errorString) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV412CompiledData15CompilationUnit10saveToDiskERK4QUrlN3qxp12function_refIJKF10QByteArrayvEEEEP7QString(
    const QV4::CompiledData::CompilationUnit *self,
    const QUrl *unitUrl,
    const qxp::function_ref<QByteArray () const> *sourceChecksum,
    QString *errorString) {
  return self->saveToDisk(*unitUrl, *sourceChecksum, errorString);
}

//  int QV4::CompiledData::CompilationUnit::importCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK3QV412CompiledData15CompilationUnit11importCountEv(
    const QV4::CompiledData::CompilationUnit *self) {
  return self->importCount();
}

//  const CompiledData::Import
//      *QV4::CompiledData::CompilationUnit::importAt(int index) const
extern "C" Q_DECL_EXPORT
const QV4::CompiledData::Import *ritual_ZNK3QV412CompiledData15CompilationUnit8importAtEi(
    const QV4::CompiledData::CompilationUnit *self,
    int index) {
  return self->importAt(index);
}

//  QStringList QV4::CompiledData::CompilationUnit::moduleRequests() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK3QV412CompiledData15CompilationUnit14moduleRequestsEv(
    const QV4::CompiledData::CompilationUnit *self) {
  return new QList<QString>(self->moduleRequests());
}

//  QUrl QV4::CompiledData::CompilationUnit::url() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK3QV412CompiledData15CompilationUnit3urlEv(
    const QV4::CompiledData::CompilationUnit *self) {
  return new QUrl(self->url());
}

//  QUrl QV4::CompiledData::CompilationUnit::finalUrl() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK3QV412CompiledData15CompilationUnit8finalUrlEv(
    const QV4::CompiledData::CompilationUnit *self) {
  return new QUrl(self->finalUrl());
}

//  ResolvedTypeReference
//      *QV4::CompiledData::CompilationUnit::resolvedType(int id) const
extern "C" Q_DECL_EXPORT
QV4::ResolvedTypeReference *ritual_ZNK3QV412CompiledData15CompilationUnit12resolvedTypeEi(
    const QV4::CompiledData::CompilationUnit *self,
    int id) {
  return self->resolvedType(id);
}

//  ResolvedTypeReference
//      *QV4::CompiledData::CompilationUnit::resolvedType(QMetaType type)
//      const
extern "C" Q_DECL_EXPORT
QV4::ResolvedTypeReference *ritual_ZNK3QV412CompiledData15CompilationUnit12resolvedTypeE9QMetaType(
    const QV4::CompiledData::CompilationUnit *self,
    const QMetaType *type) {
  return self->resolvedType(*type);
}

//  QQmlPropertyCache::ConstPtr
//      QV4::CompiledData::CompilationUnit::rootPropertyCache() const
extern "C" Q_DECL_EXPORT
QQmlPropertyCache::ConstPtr *ritual_ZNK3QV412CompiledData15CompilationUnit17rootPropertyCacheEv(
    const QV4::CompiledData::CompilationUnit *self) {
  return new QQmlPropertyCache::ConstPtr(self->rootPropertyCache());
}

//  int QV4::CompiledData::CompilationUnit::objectCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK3QV412CompiledData15CompilationUnit11objectCountEv(
    const QV4::CompiledData::CompilationUnit *self) {
  return self->objectCount();
}

//  int QV4::CompiledData::CompilationUnit::resolvedIndex(int index) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK3QV412CompiledData15CompilationUnit13resolvedIndexEi(
    const QV4::CompiledData::CompilationUnit *self,
    int index) {
  return self->resolvedIndex(index);
}

//  const CompiledObject *QV4::CompiledData::CompilationUnit::objectAt(int
//      index) const
extern "C" Q_DECL_EXPORT
const QV4::CompiledData::CompilationUnit::CompiledObject *ritual_ZNK3QV412CompiledData15CompilationUnit8objectAtEi(
    const QV4::CompiledData::CompilationUnit *self,
    int index) {
  return self->objectAt(index);
}

//  int QV4::CompiledData::CompilationUnit::implicitComponentForObject(int
//      index) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK3QV412CompiledData15CompilationUnit26implicitComponentForObjectEi(
    const QV4::CompiledData::CompilationUnit *self,
    int index) {
  return self->implicitComponentForObject(index);
}

//  int QV4::CompiledData::CompilationUnit::inlineComponentId(const QString
//      &inlineComponentName) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK3QV412CompiledData15CompilationUnit17inlineComponentIdERK7QString(
    const QV4::CompiledData::CompilationUnit *self,
    const QString *inlineComponentName) {
  return self->inlineComponentId(*inlineComponentName);
}

//  void QV4::CompiledData::CompilationUnit::finalizeCompositeType(const
//      QQmlType &type)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV412CompiledData15CompilationUnit21finalizeCompositeTypeERK8QQmlType(
    QV4::CompiledData::CompilationUnit *self,
    const QQmlType *type) {
  self->finalizeCompositeType(*type);
}

//  bool QV4::CompiledData::CompilationUnit::verifyChecksum(const
//      CompiledData::DependentTypesHasher &dependencyHasher) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV412CompiledData15CompilationUnit14verifyChecksumERKSt8functionIF10QByteArrayvEE(
    const QV4::CompiledData::CompilationUnit *self,
    const QV4::CompiledData::DependentTypesHasher *dependencyHasher) {
  return self->verifyChecksum(*dependencyHasher);
}

//  ListPropertyAssignBehavior
//      QV4::CompiledData::CompilationUnit::listPropertyAssignBehavior()
//      const
extern "C" Q_DECL_EXPORT
QV4::CompiledData::CompilationUnit::ListPropertyAssignBehavior ritual_ZNK3QV412CompiledData15CompilationUnit26listPropertyAssignBehaviorEv(
    const QV4::CompiledData::CompilationUnit *self) {
  return self->listPropertyAssignBehavior();
}

//  bool QV4::CompiledData::CompilationUnit::ignoresFunctionSignature() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV412CompiledData15CompilationUnit24ignoresFunctionSignatureEv(
    const QV4::CompiledData::CompilationUnit *self) {
  return self->ignoresFunctionSignature();
}

//  bool QV4::CompiledData::CompilationUnit::nativeMethodsAcceptThisObjects()
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV412CompiledData15CompilationUnit30nativeMethodsAcceptThisObjectsEv(
    const QV4::CompiledData::CompilationUnit *self) {
  return self->nativeMethodsAcceptThisObjects();
}

//  bool QV4::CompiledData::CompilationUnit::valueTypesAreCopied() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV412CompiledData15CompilationUnit19valueTypesAreCopiedEv(
    const QV4::CompiledData::CompilationUnit *self) {
  return self->valueTypesAreCopied();
}

//  bool QV4::CompiledData::CompilationUnit::valueTypesAreAddressable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV412CompiledData15CompilationUnit24valueTypesAreAddressableEv(
    const QV4::CompiledData::CompilationUnit *self) {
  return self->valueTypesAreAddressable();
}

//  bool QV4::CompiledData::CompilationUnit::valueTypesAreAssertable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV412CompiledData15CompilationUnit23valueTypesAreAssertableEv(
    const QV4::CompiledData::CompilationUnit *self) {
  return self->valueTypesAreAssertable();
}

//  bool QV4::CompiledData::CompilationUnit::componentsAreBound() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV412CompiledData15CompilationUnit18componentsAreBoundEv(
    const QV4::CompiledData::CompilationUnit *self) {
  return self->componentsAreBound();
}

//  bool QV4::CompiledData::CompilationUnit::isESModule() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV412CompiledData15CompilationUnit10isESModuleEv(
    const QV4::CompiledData::CompilationUnit *self) {
  return self->isESModule();
}

//  bool QV4::CompiledData::CompilationUnit::isSharedLibrary() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV412CompiledData15CompilationUnit15isSharedLibraryEv(
    const QV4::CompiledData::CompilationUnit *self) {
  return self->isSharedLibrary();
}

//  FunctionIterator
//      QV4::CompiledData::CompilationUnit::objectFunctionsBegin(const
//      CompiledObject *object) const
extern "C" Q_DECL_EXPORT
QV4::CompiledData::CompilationUnit::FunctionIterator *ritual_ZNK3QV412CompiledData15CompilationUnit20objectFunctionsBeginEPKNS0_6ObjectE(
    const QV4::CompiledData::CompilationUnit *self,
    const QV4::CompiledData::CompilationUnit::CompiledObject *object) {
  return new QV4::CompiledData::CompilationUnit::FunctionIterator(
      self->objectFunctionsBegin(
          object));
}

//  FunctionIterator
//      QV4::CompiledData::CompilationUnit::objectFunctionsEnd(const
//      CompiledObject *object) const
extern "C" Q_DECL_EXPORT
QV4::CompiledData::CompilationUnit::FunctionIterator *ritual_ZNK3QV412CompiledData15CompilationUnit18objectFunctionsEndEPKNS0_6ObjectE(
    const QV4::CompiledData::CompilationUnit *self,
    const QV4::CompiledData::CompilationUnit::CompiledObject *object) {
  return new QV4::CompiledData::CompilationUnit::FunctionIterator(
      self->objectFunctionsEnd(
          object));
}

//  QQmlType QV4::CompiledData::CompilationUnit::qmlTypeForComponent(const
//      QString &inlineComponentName) const
extern "C" Q_DECL_EXPORT
QQmlType *ritual_ZNK3QV412CompiledData15CompilationUnit19qmlTypeForComponentERK7QString(
    const QV4::CompiledData::CompilationUnit *self,
    const QString *inlineComponentName) {
  return new QQmlType(self->qmlTypeForComponent(*inlineComponentName));
}

//  QMetaType QV4::CompiledData::CompilationUnit::metaType() const
extern "C" Q_DECL_EXPORT
QMetaType *ritual_ZNK3QV412CompiledData15CompilationUnit8metaTypeEv(
    const QV4::CompiledData::CompilationUnit *self) {
  return new QMetaType(self->metaType());
}
