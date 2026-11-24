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
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlpropertycache_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>

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

//  QMetaType QV4::CompiledData::CompilationUnit::metaType() const
extern "C" Q_DECL_EXPORT
QMetaType *ritual_ZNK3QV412CompiledData15CompilationUnit8metaTypeEv(
    const QV4::CompiledData::CompilationUnit *self) {
  return new QMetaType(self->metaType());
}
