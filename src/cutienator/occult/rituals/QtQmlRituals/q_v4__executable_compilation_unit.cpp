//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4executablecompilationunit_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-25: added by hand, instances of templates of
//  the class: 1. Kept as it is when the generator runs again.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4executablecompilationunit_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlpropertycache_p.h>
#include <QtQml/6.12.0/QtQml/private/qqmltype_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4value_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4identifierhash_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qlist.h>
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

//  QString QV4::ExecutableCompilationUnit::finalUrlString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK3QV425ExecutableCompilationUnit14finalUrlStringEv(
    const QV4::ExecutableCompilationUnit *self) {
  return new QString(self->finalUrlString());
}

//  QString QV4::ExecutableCompilationUnit::fileName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK3QV425ExecutableCompilationUnit8fileNameEv(
    const QV4::ExecutableCompilationUnit *self) {
  return new QString(self->fileName());
}

//  QUrl QV4::ExecutableCompilationUnit::url() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK3QV425ExecutableCompilationUnit3urlEv(
    const QV4::ExecutableCompilationUnit *self) {
  return new QUrl(self->url());
}

//  QUrl QV4::ExecutableCompilationUnit::finalUrl() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK3QV425ExecutableCompilationUnit8finalUrlEv(
    const QV4::ExecutableCompilationUnit *self) {
  return new QUrl(self->finalUrl());
}

//  QQmlRefPointer<QQmlTypeNameCache>
//      QV4::ExecutableCompilationUnit::typeNameCache() const
extern "C" Q_DECL_EXPORT
QQmlRefPointer<QQmlTypeNameCache> *ritual_ZNK3QV425ExecutableCompilationUnit13typeNameCacheEv(
    const QV4::ExecutableCompilationUnit *self) {
  return new QQmlRefPointer<QQmlTypeNameCache>(self->typeNameCache());
}

//  QQmlPropertyCacheVector
//      *QV4::ExecutableCompilationUnit::propertyCachesPtr()
extern "C" Q_DECL_EXPORT
QQmlPropertyCacheVector *ritual_ZN3QV425ExecutableCompilationUnit17propertyCachesPtrEv(
    QV4::ExecutableCompilationUnit *self) {
  return self->propertyCachesPtr();
}

//  QQmlPropertyCache::ConstPtr
//      QV4::ExecutableCompilationUnit::rootPropertyCache() const
extern "C" Q_DECL_EXPORT
QQmlPropertyCache::ConstPtr *ritual_ZNK3QV425ExecutableCompilationUnit17rootPropertyCacheEv(
    const QV4::ExecutableCompilationUnit *self) {
  return new QQmlPropertyCache::ConstPtr(self->rootPropertyCache());
}

//  ResolvedTypeReference *QV4::ExecutableCompilationUnit::resolvedType(int
//      id) const
extern "C" Q_DECL_EXPORT
QV4::ResolvedTypeReference *ritual_ZNK3QV425ExecutableCompilationUnit12resolvedTypeEi(
    const QV4::ExecutableCompilationUnit *self,
    int id) {
  return self->resolvedType(id);
}

//  QQmlType QV4::ExecutableCompilationUnit::qmlTypeForComponent(const
//      QString &inlineComponentName) const
extern "C" Q_DECL_EXPORT
QQmlType *ritual_ZNK3QV425ExecutableCompilationUnit19qmlTypeForComponentERK7QString(
    const QV4::ExecutableCompilationUnit *self,
    const QString *inlineComponentName) {
  return new QQmlType(self->qmlTypeForComponent(*inlineComponentName));
}

//  QMetaType QV4::ExecutableCompilationUnit::metaType() const
extern "C" Q_DECL_EXPORT
QMetaType *ritual_ZNK3QV425ExecutableCompilationUnit8metaTypeEv(
    const QV4::ExecutableCompilationUnit *self) {
  return new QMetaType(self->metaType());
}

//  int QV4::ExecutableCompilationUnit::inlineComponentId(const QString
//      &inlineComponentName) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK3QV425ExecutableCompilationUnit17inlineComponentIdERK7QString(
    const QV4::ExecutableCompilationUnit *self,
    const QString *inlineComponentName) {
  return self->inlineComponentId(*inlineComponentName);
}

//  bool QV4::ExecutableCompilationUnit::nativeMethodsAcceptThisObjects()
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV425ExecutableCompilationUnit30nativeMethodsAcceptThisObjectsEv(
    const QV4::ExecutableCompilationUnit *self) {
  return self->nativeMethodsAcceptThisObjects();
}

//  bool QV4::ExecutableCompilationUnit::ignoresFunctionSignature() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV425ExecutableCompilationUnit24ignoresFunctionSignatureEv(
    const QV4::ExecutableCompilationUnit *self) {
  return self->ignoresFunctionSignature();
}

//  bool QV4::ExecutableCompilationUnit::valueTypesAreCopied() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV425ExecutableCompilationUnit19valueTypesAreCopiedEv(
    const QV4::ExecutableCompilationUnit *self) {
  return self->valueTypesAreCopied();
}

//  bool QV4::ExecutableCompilationUnit::valueTypesAreAddressable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV425ExecutableCompilationUnit24valueTypesAreAddressableEv(
    const QV4::ExecutableCompilationUnit *self) {
  return self->valueTypesAreAddressable();
}

//  bool QV4::ExecutableCompilationUnit::valueTypesAreAssertable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV425ExecutableCompilationUnit23valueTypesAreAssertableEv(
    const QV4::ExecutableCompilationUnit *self) {
  return self->valueTypesAreAssertable();
}

//  bool QV4::ExecutableCompilationUnit::componentsAreBound() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV425ExecutableCompilationUnit18componentsAreBoundEv(
    const QV4::ExecutableCompilationUnit *self) {
  return self->componentsAreBound();
}

//  bool QV4::ExecutableCompilationUnit::isESModule() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV425ExecutableCompilationUnit10isESModuleEv(
    const QV4::ExecutableCompilationUnit *self) {
  return self->isESModule();
}

//  int QV4::ExecutableCompilationUnit::objectCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK3QV425ExecutableCompilationUnit11objectCountEv(
    const QV4::ExecutableCompilationUnit *self) {
  return self->objectCount();
}

//  int QV4::ExecutableCompilationUnit::resolvedIndex(int index) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK3QV425ExecutableCompilationUnit13resolvedIndexEi(
    const QV4::ExecutableCompilationUnit *self,
    int index) {
  return self->resolvedIndex(index);
}

//  int QV4::ExecutableCompilationUnit::implicitComponentForObject(int index)
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK3QV425ExecutableCompilationUnit26implicitComponentForObjectEi(
    const QV4::ExecutableCompilationUnit *self,
    int index) {
  return self->implicitComponentForObject(index);
}

//  const CompiledObject *QV4::ExecutableCompilationUnit::objectAt(int index)
//      const
extern "C" Q_DECL_EXPORT
const QV4::ExecutableCompilationUnit::CompiledObject *ritual_ZNK3QV425ExecutableCompilationUnit8objectAtEi(
    const QV4::ExecutableCompilationUnit *self,
    int index) {
  return self->objectAt(index);
}

//  Heap::Object *QV4::ExecutableCompilationUnit::templateObjectAt(int index)
//      const
extern "C" Q_DECL_EXPORT
QV4::Heap::Object *ritual_ZNK3QV425ExecutableCompilationUnit16templateObjectAtEi(
    const QV4::ExecutableCompilationUnit *self,
    int index) {
  return self->templateObjectAt(index);
}

//  Heap::Module *QV4::ExecutableCompilationUnit::instantiate()
extern "C" Q_DECL_EXPORT
QV4::Heap::Module *ritual_ZN3QV425ExecutableCompilationUnit11instantiateEv(
    QV4::ExecutableCompilationUnit *self) {
  return self->instantiate();
}

//  const Value *QV4::ExecutableCompilationUnit::resolveExport(QV4::String
//      *exportName) const
extern "C" Q_DECL_EXPORT
const QV4::Value *ritual_ZNK3QV425ExecutableCompilationUnit13resolveExportEPNS_6StringE(
    const QV4::ExecutableCompilationUnit *self,
    QV4::String *exportName) {
  return self->resolveExport(exportName);
}

//  QStringList QV4::ExecutableCompilationUnit::exportedNames() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK3QV425ExecutableCompilationUnit13exportedNamesEv(
    const QV4::ExecutableCompilationUnit *self) {
  return new QList<QString>(self->exportedNames());
}

//  void QV4::ExecutableCompilationUnit::evaluate()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV425ExecutableCompilationUnit8evaluateEv(
    QV4::ExecutableCompilationUnit *self) {
  self->evaluate();
}

//  void QV4::ExecutableCompilationUnit::evaluateModuleRequests()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV425ExecutableCompilationUnit22evaluateModuleRequestsEv(
    QV4::ExecutableCompilationUnit *self) {
  self->evaluateModuleRequests();
}

//  void QV4::ExecutableCompilationUnit::mark(MarkStack *markStack) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK3QV425ExecutableCompilationUnit4markEPNS_9MarkStackE(
    const QV4::ExecutableCompilationUnit *self,
    QV4::MarkStack *markStack) {
  self->mark(markStack);
}

//  void QV4::ExecutableCompilationUnit::markObjects(MarkStack *markStack)
//      const
extern "C" Q_DECL_EXPORT
void ritual_ZNK3QV425ExecutableCompilationUnit11markObjectsEPNS_9MarkStackE(
    const QV4::ExecutableCompilationUnit *self,
    QV4::MarkStack *markStack) {
  self->markObjects(markStack);
}

//  QString QV4::ExecutableCompilationUnit::bindingValueAsString(const
//      CompiledData::Binding *binding) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK3QV425ExecutableCompilationUnit20bindingValueAsStringEPKNS_12CompiledData7BindingE(
    const QV4::ExecutableCompilationUnit *self,
    const QV4::CompiledData::Binding *binding) {
  return new QString(self->bindingValueAsString(binding));
}

//  double QV4::ExecutableCompilationUnit::bindingValueAsNumber(const
//      CompiledData::Binding *binding) const
extern "C" Q_DECL_EXPORT
double ritual_ZNK3QV425ExecutableCompilationUnit20bindingValueAsNumberEPKNS_12CompiledData7BindingE(
    const QV4::ExecutableCompilationUnit *self,
    const QV4::CompiledData::Binding *binding) {
  return self->bindingValueAsNumber(binding);
}

//  QString QV4::ExecutableCompilationUnit::bindingValueAsScriptString(const
//      CompiledData::Binding *binding) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK3QV425ExecutableCompilationUnit26bindingValueAsScriptStringEPKNS_12CompiledData7BindingE(
    const QV4::ExecutableCompilationUnit *self,
    const QV4::CompiledData::Binding *binding) {
  return new QString(self->bindingValueAsScriptString(binding));
}

//  QString
//      QV4::ExecutableCompilationUnit::translateFrom(TranslationDataIndex
//      index) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK3QV425ExecutableCompilationUnit13translateFromENS0_20TranslationDataIndexE(
    const QV4::ExecutableCompilationUnit *self,
    const QV4::ExecutableCompilationUnit::TranslationDataIndex *index) {
  return new QString(self->translateFrom(*index));
}

//  Heap::Module *QV4::ExecutableCompilationUnit::module() const
extern "C" Q_DECL_EXPORT
QV4::Heap::Module *ritual_ZNK3QV425ExecutableCompilationUnit6moduleEv(
    const QV4::ExecutableCompilationUnit *self) {
  return self->module();
}

//  void QV4::ExecutableCompilationUnit::setModule(Heap::Module *module)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV425ExecutableCompilationUnit9setModuleEPNS_4Heap6ModuleE(
    QV4::ExecutableCompilationUnit *self,
    QV4::Heap::Module *module) {
  self->setModule(module);
}

//  ReturnedValue QV4::ExecutableCompilationUnit::value() const
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZNK3QV425ExecutableCompilationUnit5valueEv(
    const QV4::ExecutableCompilationUnit *self) {
  return self->value();
}

//  void QV4::ExecutableCompilationUnit::setValue(const QV4::Value &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV425ExecutableCompilationUnit8setValueERKNS_5ValueE(
    QV4::ExecutableCompilationUnit *self,
    const QV4::Value *value) {
  self->setValue(*value);
}

//  const CompiledData::Unit *QV4::ExecutableCompilationUnit::unitData()
//      const
extern "C" Q_DECL_EXPORT
const QV4::CompiledData::Unit *ritual_ZNK3QV425ExecutableCompilationUnit8unitDataEv(
    const QV4::ExecutableCompilationUnit *self) {
  return self->unitData();
}

//  QString QV4::ExecutableCompilationUnit::stringAt(uint index) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK3QV425ExecutableCompilationUnit8stringAtEj(
    const QV4::ExecutableCompilationUnit *self,
    uint index) {
  return new QString(self->stringAt(index));
}

//  const QList<QQmlRefPointer<QQmlScriptData>>
//      *QV4::ExecutableCompilationUnit::dependentScriptsPtr() const
extern "C" Q_DECL_EXPORT
const QList<QQmlRefPointer<QQmlScriptData>> *ritual_ZNK3QV425ExecutableCompilationUnit19dependentScriptsPtrEv(
    const QV4::ExecutableCompilationUnit *self) {
  return self->dependentScriptsPtr();
}

//  const CompiledData::BindingPropertyData
//      *QV4::ExecutableCompilationUnit::bindingPropertyDataPerObjectAt(qsize
//      type objectIndex) const
extern "C" Q_DECL_EXPORT
const QV4::CompiledData::BindingPropertyData *ritual_ZNK3QV425ExecutableCompilationUnit30bindingPropertyDataPerObjectAtEx(
    const QV4::ExecutableCompilationUnit *self,
    qsizetype objectIndex) {
  return self->bindingPropertyDataPerObjectAt(objectIndex);
}

//  const QQmlRefPointer<QV4::CompiledData::CompilationUnit>
//      &QV4::ExecutableCompilationUnit::baseCompilationUnit() const
extern "C" Q_DECL_EXPORT
const QQmlRefPointer<QV4::CompiledData::CompilationUnit> *ritual_ZNK3QV425ExecutableCompilationUnit19baseCompilationUnitEv(
    const QV4::ExecutableCompilationUnit *self) {
  return &(self->baseCompilationUnit());
}

//  QV4::Function *QV4::ExecutableCompilationUnit::rootFunction()
extern "C" Q_DECL_EXPORT
QV4::Function *ritual_ZN3QV425ExecutableCompilationUnit12rootFunctionEv(
    QV4::ExecutableCompilationUnit *self) {
  return self->rootFunction();
}

//  void QV4::ExecutableCompilationUnit::populate()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV425ExecutableCompilationUnit8populateEv(
    QV4::ExecutableCompilationUnit *self) {
  self->populate();
}

//  void QV4::ExecutableCompilationUnit::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV425ExecutableCompilationUnit5clearEv(
    QV4::ExecutableCompilationUnit *self) {
  self->clear();
}

//  quint32 QV4::ExecutableCompilationUnit::totalStringCount() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK3QV425ExecutableCompilationUnit16totalStringCountEv(
    const QV4::ExecutableCompilationUnit *self) {
  return self->totalStringCount();
}

//  QV4::ExecutableCompilationUnit::ExecutableCompilationUnit()
extern "C" Q_DECL_EXPORT
QV4::ExecutableCompilationUnit *ritual_ZN3QV425ExecutableCompilationUnitC1Ev() {
  return new QV4::ExecutableCompilationUnit();
}

//  QV4::ExecutableCompilationUnit::ExecutableCompilationUnit(QQmlRefPointer<
//      CompiledData::CompilationUnit> &&compilationUnit)
extern "C" Q_DECL_EXPORT
QV4::ExecutableCompilationUnit *ritual_ZN3QV425ExecutableCompilationUnitC1EO14QQmlRefPointerINS_12CompiledData15CompilationUnitEE(
    QQmlRefPointer<QV4::CompiledData::CompilationUnit> *compilationUnit) {
  return new QV4::ExecutableCompilationUnit(std::move(*compilationUnit));
}

//  QV4::ExecutableCompilationUnit::~ExecutableCompilationUnit()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV425ExecutableCompilationUnitD1Ev(
    QV4::ExecutableCompilationUnit *self) {
  delete self;
}

//  QQmlRefPointer<ExecutableCompilationUnit> QV4::ExecutableCompilationUnit:
//      :create(QQmlRefPointer<CompiledData::CompilationUnit>
//      &&compilationUnit, ExecutionEngine *engine)
extern "C" Q_DECL_EXPORT
QQmlRefPointer<QV4::ExecutableCompilationUnit> *ritual_ZN3QV425ExecutableCompilationUnit6createEO14QQmlRefPointerINS_12CompiledData15CompilationUnitEEPNS_15ExecutionEngineE(
    QQmlRefPointer<QV4::CompiledData::CompilationUnit> *compilationUnit,
    QV4::ExecutionEngine *engine) {
  return new QQmlRefPointer<QV4::ExecutableCompilationUnit>(
      QV4::ExecutableCompilationUnit::create(
          std::move(*compilationUnit),
          engine));
}

//  const Value
//      *QV4::ExecutableCompilationUnit::resolveExportRecursively(QV4::String
//      *exportName, QList<ResolveSetEntry> *resolveSet) const
extern "C" Q_DECL_EXPORT
const QV4::Value *ritual_ZNK3QV425ExecutableCompilationUnit24resolveExportRecursivelyEPNS_6StringEP5QListINS0_15ResolveSetEntryEE(
    const QV4::ExecutableCompilationUnit *self,
    QV4::String *exportName,
    QList<QV4::ExecutableCompilationUnit::ResolveSetEntry> *resolveSet) {
  return self->resolveExportRecursively(exportName, resolveSet);
}

//  QUrl QV4::ExecutableCompilationUnit::urlAt(int index) const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK3QV425ExecutableCompilationUnit5urlAtEi(
    const QV4::ExecutableCompilationUnit *self,
    int index) {
  return new QUrl(self->urlAt(index));
}

//  IdentifierHash
//      QV4::ExecutableCompilationUnit::createNamedObjectsPerComponent(int
//      componentObjectIndex)
extern "C" Q_DECL_EXPORT
QV4::IdentifierHash *ritual_ZN3QV425ExecutableCompilationUnit30createNamedObjectsPerComponentEi(
    QV4::ExecutableCompilationUnit *self,
    int componentObjectIndex) {
  return new QV4::IdentifierHash(
      self->createNamedObjectsPerComponent(
          componentObjectIndex));
}

//  const CompiledData::ExportEntry
//      *QV4::ExecutableCompilationUnit::lookupNameInExportTable(const
//      CompiledData::ExportEntry *firstExportEntry, int tableSize,
//      QV4::String *name) const
extern "C" Q_DECL_EXPORT
const QV4::CompiledData::ExportEntry *ritual_ZNK3QV425ExecutableCompilationUnit23lookupNameInExportTableEPKNS_12CompiledData11ExportEntryEiPNS_6StringE(
    const QV4::ExecutableCompilationUnit *self,
    const QV4::CompiledData::ExportEntry *firstExportEntry,
    int tableSize,
    QV4::String *name) {
  return self->lookupNameInExportTable(firstExportEntry, tableSize, name);
}

//  void
//      QV4::ExecutableCompilationUnit::getExportedNamesRecursively(QStringLi
//      st *names, QList<const ExecutableCompilationUnit *> *exportNameSet,
//      bool includeDefaultExport) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK3QV425ExecutableCompilationUnit27getExportedNamesRecursivelyEP5QListI7QStringEPS1_IPKS0_Eb(
    const QV4::ExecutableCompilationUnit *self,
    QStringList *names,
    QList<const QV4::ExecutableCompilationUnit *> *exportNameSet,
    bool includeDefaultExport) {
  self->getExportedNamesRecursively(
      names,
      exportNameSet,
      includeDefaultExport);
}

//  a QQmlRefPointer<QQmlTypeNameCache> a ritual of
//      QV4::ExecutableCompilationUnit gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QV4_ExecutableCompilationUnit__QQmlRefPointer_QQmlTypeNameCache(
    QQmlRefPointer<QQmlTypeNameCache> *self) {
  delete self;
}

//  a QQmlRefPointer<QV4::ExecutableCompilationUnit> a ritual of
//      QV4::ExecutableCompilationUnit gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QV4_ExecutableCompilationUnit__QQmlRefPointer_QV4_ExecutableCompilationUnit(
    QQmlRefPointer<QV4::ExecutableCompilationUnit> *self) {
  delete self;
}

#include <QtQml/6.12.0/QtQml/private/qv4engine_p.h>

//  QQmlRefPointer<QV4::ExecutableCompilationUnit>
//      QV4::ExecutableCompilationUnit::dependentModule<
//      QV4::ExecutionEngine>(const QUrl &relative) const
extern "C" Q_DECL_EXPORT
QQmlRefPointer<QV4::ExecutableCompilationUnit> *ritual_ZNK3QV425ExecutableCompilationUnit15dependentModuleINS_15ExecutionEngineEEE14QQmlRefPointerIS0_ERK4QUrl(
    const QV4::ExecutableCompilationUnit *self, const QUrl *relative) {
  return new QQmlRefPointer<QV4::ExecutableCompilationUnit>(
      self->dependentModule<QV4::ExecutionEngine>(*relative));
}
