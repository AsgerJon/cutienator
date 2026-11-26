//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmltypecompiler_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmltypecompiler_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtQml/qqmlerror.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4compileddata_p.h>
#include <QtQml/6.12.0/QtQml/private/qqmljsdiagnosticmessage_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qurl.h>
#include <QtCore/qstringview.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlcustomparser_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qtyperevision.h>
#include <QtCore/qmetatype.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmltype_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qlist.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
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
#include <QtQml/private/qqmltypecompiler_p.h>
#include <QtQml/private/qqmlobjectcreator_p.h>
#include <QtQml/private/qqmlcustomparser_p.h>
#include <QtQml/private/qqmlvmemetaobject_p.h>
#include <QtQml/private/qqmlcomponent_p.h>
#include <QtQml/private/qqmlpropertyresolver_p.h>
#include <QtQml/private/qqmlcomponentandaliasresolver_p.h>
#include <QtQml/private/qqmlsignalnames_p.h>
#include <QtCore/qtyperevision.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/qml/qqmltypedata.cpp, line 55, as _ZNK12QQmlTypeData7qmlTypeERK7QString
inline QQmlType QQmlTypeData::qmlType(const QString &inlineComponentName) const
{
    if (inlineComponentName.isEmpty())
        return m_qmlType;
    return m_inlineComponentData[inlineComponentName].qmlType;
}

//  from ../qtdeclarative/src/qml/qml/qqmltypecompiler.cpp, line 30, as _ZN16QQmlTypeCompilerC1EP14QQmlTypeLoaderP12QQmlTypeDataPN5QmlIR8DocumentEPN3QV412CompiledData24ResolvedTypeReferenceMapERKSt8functionIF10QByteArrayvEE
inline QQmlTypeCompiler::QQmlTypeCompiler(
        QQmlTypeLoader *typeLoader, QQmlTypeData *typeData, QmlIR::Document *parsedQML,
        QV4::CompiledData::ResolvedTypeReferenceMap *resolvedTypeCache,
        const QV4::CompiledData::DependentTypesHasher &dependencyHasher)
    : resolvedTypes(resolvedTypeCache)
    , loader(typeLoader)
    , dependencyHasher(dependencyHasher)
    , document(parsedQML)
    , typeData(typeData)
{
}

//  from ../qtdeclarative/src/qml/qml/qqmltypecompiler.cpp, line 184, as _ZNK16QQmlTypeCompiler13resolvedIndexEi
inline int QQmlTypeCompiler::resolvedIndex(int index) const
{
    if (index < objectCount())
        return index;
    const auto *p = m_propertyCaches.at(index)->defaultProperty();
    Q_ASSERT(p && p->isComponentWrapper());
    return p->wrappedObjectIndex();
}

//  from ../qtdeclarative/src/qml/qml/qqmltypecompiler.cpp, line 193, as _ZNK16QQmlTypeCompiler26implicitComponentForObjectEi
inline int QQmlTypeCompiler::implicitComponentForObject(int childIndex) const
{
    for (int i = objectCount(), end = m_propertyCaches.count(); i < end; ++i) {
        const auto *p = m_propertyCaches.at(i)->defaultProperty();
        Q_ASSERT(p && p->isComponentWrapper());
        if (p->wrappedObjectIndex() == childIndex)
            return i;
    }
    return -1;
}

//  from ../qtdeclarative/src/qml/qml/qqmltypecompiler.cpp, line 174, as _ZNK16QQmlTypeCompiler8stringAtEi
inline QString QQmlTypeCompiler::stringAt(int idx) const
{
    return document->stringAt(idx);
}

//  from ../qtdeclarative/src/qml/qml/qqmltypecompiler.cpp, line 147, as _ZN16QQmlTypeCompiler11recordErrorERKN3QV412CompiledData8LocationERK7QString
inline void QQmlTypeCompiler::recordError(const QV4::CompiledData::Location &location, const QString &description)
{
    QQmlError error;
    error.setLine(qmlConvertSourceCoordinate<quint32, int>(location.line()));
    error.setColumn(qmlConvertSourceCoordinate<quint32, int>(location.column()));
    error.setDescription(description);
    error.setUrl(url());
    errors << error;
}

//  from ../qtdeclarative/src/qml/qml/qqmltypecompiler.cpp, line 157, as _ZN16QQmlTypeCompiler11recordErrorERKN6QQmlJS17DiagnosticMessageE
inline void QQmlTypeCompiler::recordError(const QQmlJS::DiagnosticMessage &message)
{
    QQmlError error;
    error.setDescription(message.message);
    error.setLine(qmlConvertSourceCoordinate<quint32, int>(message.loc.startLine));
    error.setColumn(qmlConvertSourceCoordinate<quint32, int>(message.loc.startColumn));
    error.setUrl(url());
    errors << error;
}

//  from ../qtdeclarative/src/qml/qml/qqmltypecompiler.cpp, line 167, as _ZN16QQmlTypeCompiler11recordErrorERK9QQmlError
inline void QQmlTypeCompiler::recordError(const QQmlError &e)
{
    QQmlError error = e;
    error.setUrl(url());
    errors << error;
}

//  from ../qtdeclarative/src/qml/qml/qqmltypecompiler.cpp, line 179, as _ZN16QQmlTypeCompiler14registerStringERK7QString
inline int QQmlTypeCompiler::registerString(const QString &str)
{
    return document->jsGenerator.registerString(str);
}

//  from ../qtdeclarative/src/qml/qml/qqmltypecompiler.cpp, line 204, as _ZN16QQmlTypeCompiler16registerConstantEy
inline int QQmlTypeCompiler::registerConstant(QV4::ReturnedValue v)
{
    return document->jsGenerator.registerConstant(v);
}

//  from ../qtdeclarative/src/qml/qml/qqmltypecompiler.cpp, line 209, as _ZNK16QQmlTypeCompiler7qmlUnitEv
inline const QV4::CompiledData::Unit *QQmlTypeCompiler::qmlUnit() const
{
    return document->javaScriptCompilationUnit->unitData();
}

//  from ../qtdeclarative/src/qml/qml/qqmltypecompiler.cpp, line 214, as _ZNK16QQmlTypeCompiler7importsEv
inline const QQmlImports *QQmlTypeCompiler::imports() const
{
    return typeData->imports();
}

//  from ../qtdeclarative/src/qml/qml/qqmltypecompiler.cpp, line 219, as _ZNK16QQmlTypeCompiler10qmlObjectsEv
inline QList<QmlIR::Object *> *QQmlTypeCompiler::qmlObjects() const
{
    return &document->objects;
}

//  from ../qtdeclarative/src/qml/qml/qqmltypecompiler.cpp, line 224, as _ZN16QQmlTypeCompiler14propertyCachesEv
inline QQmlPropertyCacheVector *QQmlTypeCompiler::propertyCaches()
{
    return &m_propertyCaches;
}

//  from ../qtdeclarative/src/qml/qml/qqmltypecompiler.cpp, line 229, as _ZNK16QQmlTypeCompiler14propertyCachesEv
inline const QQmlPropertyCacheVector *QQmlTypeCompiler::propertyCaches() const
{
    return &m_propertyCaches;
}

//  from ../qtdeclarative/src/qml/qml/qqmltypecompiler.cpp, line 234, as _ZN16QQmlTypeCompiler10memoryPoolEv
inline QQmlJS::MemoryPool *QQmlTypeCompiler::memoryPool()
{
    return document->jsParserEngine.pool();
}

//  from ../qtdeclarative/src/qml/qml/qqmltypecompiler.cpp, line 239, as _ZN16QQmlTypeCompiler12newStringRefERK7QString
inline QStringView QQmlTypeCompiler::newStringRef(const QString &string)
{
    return document->jsParserEngine.newStringRef(string);
}

//  from ../qtdeclarative/src/qml/qml/qqmltypecompiler.cpp, line 244, as _ZNK16QQmlTypeCompiler10stringPoolEv
inline const QV4::Compiler::StringTableGenerator *QQmlTypeCompiler::stringPool() const
{
    return &document->jsGenerator.stringTable;
}

//  from ../qtdeclarative/src/qml/qml/qqmltypecompiler.cpp, line 249, as _ZNK16QQmlTypeCompiler15bindingAsStringEPKN5QmlIR6ObjectEi
inline QString QQmlTypeCompiler::bindingAsString(const QmlIR::Object *object, int scriptIndex) const
{
    return object->bindingAsString(document, scriptIndex);
}

//  from ../qtdeclarative/src/qml/qml/qqmltypecompiler.cpp, line 254, as _ZN16QQmlTypeCompiler9addImportERK7QStringS2_13QTypeRevision
inline void QQmlTypeCompiler::addImport(const QString &module, const QString &qualifier, QTypeRevision version)
{
    const quint32 moduleIdx = registerString(module);
    const quint32 qualifierIdx = registerString(qualifier);

    for (int i = 0, count = document->imports.size(); i < count; ++i) {
        const QV4::CompiledData::Import *existingImport = document->imports.at(i);
        if (existingImport->type == QV4::CompiledData::Import::ImportLibrary
            && existingImport->uriIndex == moduleIdx
            && existingImport->qualifierIndex == qualifierIdx)
            return;
    }
    auto pool = memoryPool();
    QV4::CompiledData::Import *import = pool->New<QV4::CompiledData::Import>();
    import->type = QV4::CompiledData::Import::ImportLibrary;
    import->version = version;
    import->uriIndex = moduleIdx;
    import->qualifierIndex = qualifierIdx;
    document->imports.append(import);
}

//  from ../qtdeclarative/src/qml/qml/qqmltypecompiler.cpp, line 275, as _ZNK16QQmlTypeCompiler19qmlTypeForComponentERK7QString
inline QQmlType QQmlTypeCompiler::qmlTypeForComponent(const QString &inlineComponentName) const
{
    return typeData->qmlType(inlineComponentName);
}
//  -----------------------------------------------------------------------

//  QString QQmlTypeCompiler::tr(const char *sourceText, const char
//      *disambiguation, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QQmlTypeCompiler2trEPKcS1_i(
    const char *sourceText,
    const char *disambiguation,
    int n) {
  return new QString(QQmlTypeCompiler::tr(sourceText, disambiguation, n));
}

//  QQmlTypeCompiler::QQmlTypeCompiler(QQmlTypeLoader *typeLoader,
//      QQmlTypeData *typeData, QmlIR::Document *document,
//      QV4::CompiledData::ResolvedTypeReferenceMap *resolvedTypeCache, const
//      QV4::CompiledData::DependentTypesHasher &dependencyHasher)
extern "C" Q_DECL_EXPORT
QQmlTypeCompiler *ritual_ZN16QQmlTypeCompilerC1EP14QQmlTypeLoaderP12QQmlTypeDataPN5QmlIR8DocumentEPN3QV412CompiledData24ResolvedTypeReferenceMapERKSt8functionIF10QByteArrayvEE(
    QQmlTypeLoader *typeLoader,
    QQmlTypeData *typeData,
    QmlIR::Document *document,
    QV4::CompiledData::ResolvedTypeReferenceMap *resolvedTypeCache,
    const QV4::CompiledData::DependentTypesHasher *dependencyHasher) {
  return new QQmlTypeCompiler(
      typeLoader,
      typeData,
      document,
      resolvedTypeCache,
      *dependencyHasher);
}

//  const QmlIR::Object *QQmlTypeCompiler::objectAt(int index) const
extern "C" Q_DECL_EXPORT
const QmlIR::Object *ritual_ZNK16QQmlTypeCompiler8objectAtEi(
    const QQmlTypeCompiler *self,
    int index) {
  return self->objectAt(index);
}

//  QmlIR::Object *QQmlTypeCompiler::objectAt(int index)
extern "C" Q_DECL_EXPORT
QmlIR::Object *ritual_ZN16QQmlTypeCompiler8objectAtEi(
    QQmlTypeCompiler *self,
    int index) {
  return self->objectAt(index);
}

//  int QQmlTypeCompiler::objectCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QQmlTypeCompiler11objectCountEv(
    const QQmlTypeCompiler *self) {
  return self->objectCount();
}

//  int QQmlTypeCompiler::resolvedIndex(int index) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QQmlTypeCompiler13resolvedIndexEi(
    const QQmlTypeCompiler *self,
    int index) {
  return self->resolvedIndex(index);
}

//  int QQmlTypeCompiler::implicitComponentForObject(int childIndex) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QQmlTypeCompiler26implicitComponentForObjectEi(
    const QQmlTypeCompiler *self,
    int childIndex) {
  return self->implicitComponentForObject(childIndex);
}

//  QString QQmlTypeCompiler::stringAt(int idx) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QQmlTypeCompiler8stringAtEi(
    const QQmlTypeCompiler *self,
    int idx) {
  return new QString(self->stringAt(idx));
}

//  QmlIR::PoolList<QmlIR::Function>::Iterator
//      QQmlTypeCompiler::objectFunctionsBegin(const QmlIR::Object *object)
//      const
extern "C" Q_DECL_EXPORT
QmlIR::PoolList<QmlIR::Function>::Iterator *ritual_ZNK16QQmlTypeCompiler20objectFunctionsBeginEPKN5QmlIR6ObjectE(
    const QQmlTypeCompiler *self,
    const QmlIR::Object *object) {
  return new QmlIR::PoolList<QmlIR::Function>::Iterator(
      self->objectFunctionsBegin(
          object));
}

//  QmlIR::PoolList<QmlIR::Function>::Iterator
//      QQmlTypeCompiler::objectFunctionsEnd(const QmlIR::Object *object)
//      const
extern "C" Q_DECL_EXPORT
QmlIR::PoolList<QmlIR::Function>::Iterator *ritual_ZNK16QQmlTypeCompiler18objectFunctionsEndEPKN5QmlIR6ObjectE(
    const QQmlTypeCompiler *self,
    const QmlIR::Object *object) {
  return new QmlIR::PoolList<QmlIR::Function>::Iterator(
      self->objectFunctionsEnd(
          object));
}

//  ListPropertyAssignBehavior QQmlTypeCompiler::listPropertyAssignBehavior()
//      const
extern "C" Q_DECL_EXPORT
QQmlTypeCompiler::ListPropertyAssignBehavior ritual_ZNK16QQmlTypeCompiler26listPropertyAssignBehaviorEv(
    const QQmlTypeCompiler *self) {
  return self->listPropertyAssignBehavior();
}

//  QList<QQmlError> QQmlTypeCompiler::compilationErrors() const
extern "C" Q_DECL_EXPORT
QList<QQmlError> *ritual_ZNK16QQmlTypeCompiler17compilationErrorsEv(
    const QQmlTypeCompiler *self) {
  return new QList<QQmlError>(self->compilationErrors());
}

//  void QQmlTypeCompiler::recordError(const QV4::CompiledData::Location
//      &location, const QString &description)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlTypeCompiler11recordErrorERKN3QV412CompiledData8LocationERK7QString(
    QQmlTypeCompiler *self,
    const QV4::CompiledData::Location *location,
    const QString *description) {
  self->recordError(*location, *description);
}

//  void QQmlTypeCompiler::recordError(const QQmlJS::DiagnosticMessage
//      &message)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlTypeCompiler11recordErrorERKN6QQmlJS17DiagnosticMessageE(
    QQmlTypeCompiler *self,
    const QQmlJS::DiagnosticMessage *message) {
  self->recordError(*message);
}

//  void QQmlTypeCompiler::recordError(const QQmlError &e)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlTypeCompiler11recordErrorERK9QQmlError(
    QQmlTypeCompiler *self,
    const QQmlError *e) {
  self->recordError(*e);
}

//  int QQmlTypeCompiler::registerString(const QString &str)
extern "C" Q_DECL_EXPORT
int ritual_ZN16QQmlTypeCompiler14registerStringERK7QString(
    QQmlTypeCompiler *self,
    const QString *str) {
  return self->registerString(*str);
}

//  int QQmlTypeCompiler::registerConstant(QV4::ReturnedValue v)
extern "C" Q_DECL_EXPORT
int ritual_ZN16QQmlTypeCompiler16registerConstantEy(
    QQmlTypeCompiler *self,
    QV4::ReturnedValue v) {
  return self->registerConstant(v);
}

//  const QV4::CompiledData::Unit *QQmlTypeCompiler::qmlUnit() const
extern "C" Q_DECL_EXPORT
const QV4::CompiledData::Unit *ritual_ZNK16QQmlTypeCompiler7qmlUnitEv(
    const QQmlTypeCompiler *self) {
  return self->qmlUnit();
}

//  QUrl QQmlTypeCompiler::url() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK16QQmlTypeCompiler3urlEv(const QQmlTypeCompiler *self) {
  return new QUrl(self->url());
}

//  QQmlTypeLoader *QQmlTypeCompiler::typeLoader() const
extern "C" Q_DECL_EXPORT
QQmlTypeLoader *ritual_ZNK16QQmlTypeCompiler10typeLoaderEv(
    const QQmlTypeCompiler *self) {
  return self->typeLoader();
}

//  const QQmlImports *QQmlTypeCompiler::imports() const
extern "C" Q_DECL_EXPORT
const QQmlImports *ritual_ZNK16QQmlTypeCompiler7importsEv(
    const QQmlTypeCompiler *self) {
  return self->imports();
}

//  QList<QmlIR::Object *> *QQmlTypeCompiler::qmlObjects() const
extern "C" Q_DECL_EXPORT
QList<QmlIR::Object *> *ritual_ZNK16QQmlTypeCompiler10qmlObjectsEv(
    const QQmlTypeCompiler *self) {
  return self->qmlObjects();
}

//  QQmlPropertyCacheVector *QQmlTypeCompiler::propertyCaches()
extern "C" Q_DECL_EXPORT
QQmlPropertyCacheVector *ritual_ZN16QQmlTypeCompiler14propertyCachesEv(
    QQmlTypeCompiler *self) {
  return self->propertyCaches();
}

//  const QQmlPropertyCacheVector *QQmlTypeCompiler::propertyCaches() const
extern "C" Q_DECL_EXPORT
const QQmlPropertyCacheVector *ritual_ZNK16QQmlTypeCompiler14propertyCachesEv(
    const QQmlTypeCompiler *self) {
  return self->propertyCaches();
}

//  QQmlJS::MemoryPool *QQmlTypeCompiler::memoryPool()
extern "C" Q_DECL_EXPORT
QQmlJS::MemoryPool *ritual_ZN16QQmlTypeCompiler10memoryPoolEv(
    QQmlTypeCompiler *self) {
  return self->memoryPool();
}

//  QStringView QQmlTypeCompiler::newStringRef(const QString &string)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QQmlTypeCompiler12newStringRefERK7QString(
    QQmlTypeCompiler *self,
    const QString *string) {
  return new QString(self->newStringRef(*string).toString());
}

//  const QV4::Compiler::StringTableGenerator *QQmlTypeCompiler::stringPool()
//      const
extern "C" Q_DECL_EXPORT
const QV4::Compiler::StringTableGenerator *ritual_ZNK16QQmlTypeCompiler10stringPoolEv(
    const QQmlTypeCompiler *self) {
  return self->stringPool();
}

//  const QHash<int, QQmlCustomParser *>
//      &QQmlTypeCompiler::customParserCache() const
extern "C" Q_DECL_EXPORT
QHash<int, QQmlCustomParser *> *ritual_ZNK16QQmlTypeCompiler17customParserCacheEv(
    const QQmlTypeCompiler *self) {
  return new QHash<int, QQmlCustomParser *>(self->customParserCache());
}

//  QString QQmlTypeCompiler::bindingAsString(const QmlIR::Object *object,
//      int scriptIndex) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QQmlTypeCompiler15bindingAsStringEPKN5QmlIR6ObjectEi(
    const QQmlTypeCompiler *self,
    const QmlIR::Object *object,
    int scriptIndex) {
  return new QString(self->bindingAsString(object, scriptIndex));
}

//  void QQmlTypeCompiler::addImport(const QString &module, const QString
//      &qualifier, QTypeRevision version)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlTypeCompiler9addImportERK7QStringS2_13QTypeRevision(
    QQmlTypeCompiler *self,
    const QString *module,
    const QString *qualifier,
    const QTypeRevision *version) {
  self->addImport(*module, *qualifier, *version);
}

//  QV4::ResolvedTypeReference *QQmlTypeCompiler::resolvedType(int id) const
extern "C" Q_DECL_EXPORT
QV4::ResolvedTypeReference *ritual_ZNK16QQmlTypeCompiler12resolvedTypeEi(
    const QQmlTypeCompiler *self,
    int id) {
  return self->resolvedType(id);
}

//  QV4::ResolvedTypeReference *QQmlTypeCompiler::resolvedType(QMetaType
//      type) const
extern "C" Q_DECL_EXPORT
QV4::ResolvedTypeReference *ritual_ZNK16QQmlTypeCompiler12resolvedTypeE9QMetaType(
    const QQmlTypeCompiler *self,
    const QMetaType *type) {
  return self->resolvedType(*type);
}

//  QQmlType QQmlTypeCompiler::qmlTypeForComponent(const QString
//      &inlineComponentName) const
extern "C" Q_DECL_EXPORT
QQmlType *ritual_ZNK16QQmlTypeCompiler19qmlTypeForComponentERK7QString(
    const QQmlTypeCompiler *self,
    const QString *inlineComponentName) {
  return new QQmlType(self->qmlTypeForComponent(*inlineComponentName));
}

//  a QmlIR::PoolList<QmlIR::Function>::Iterator a ritual of QQmlTypeCompiler
//      gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQmlTypeCompiler__QmlIR_PoolList_QmlIR_Function_Iterator(
    QmlIR::PoolList<QmlIR::Function>::Iterator *self) {
  delete self;
}

//  a QQmlRefPointer<QV4::CompiledData::CompilationUnit> a ritual of
//      QQmlTypeCompiler gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQmlTypeCompiler__QQmlRefPointer_QV4_CompiledData_CompilationUnit(
    QQmlRefPointer<QV4::CompiledData::CompilationUnit> *self) {
  delete self;
}
