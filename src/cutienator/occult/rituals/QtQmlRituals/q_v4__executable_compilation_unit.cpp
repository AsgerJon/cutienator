//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4executablecompilationunit_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4executablecompilationunit_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlpropertycache_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4identifierhash_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4value_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qlist.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <private/qv4identifierhash_p.h>
#include <private/qv4identifiertable_p.h>
#include <private/qv4string_p.h>
#include <private/qv4identifierhashdata_p.h>
#include <private/qprimefornumbits_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/jsruntime/qv4identifierhash.cpp, line 113, as _ZN3QV414IdentifierHashC1ERKS0_
inline QV4::IdentifierHash::IdentifierHash(const IdentifierHash &other)
{
    d = other.d;
    if (d)
        d->refCount.ref();
}
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

//  IdentifierHash
//      QV4::ExecutableCompilationUnit::namedObjectsPerComponent(int
//      componentObjectIndex)
extern "C" Q_DECL_EXPORT
QV4::IdentifierHash *ritual_ZN3QV425ExecutableCompilationUnit24namedObjectsPerComponentEi(
    QV4::ExecutableCompilationUnit *self,
    int componentObjectIndex) {
  return new QV4::IdentifierHash(
      self->namedObjectsPerComponent(
          componentObjectIndex));
}

//  ResolvedTypeReference *QV4::ExecutableCompilationUnit::resolvedType(int
//      id) const
extern "C" Q_DECL_EXPORT
QV4::ResolvedTypeReference *ritual_ZNK3QV425ExecutableCompilationUnit12resolvedTypeEi(
    const QV4::ExecutableCompilationUnit *self,
    int id) {
  return self->resolvedType(id);
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

//  void QV4::ExecutableCompilationUnit::mark(MarkStack *markStack) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK3QV425ExecutableCompilationUnit4markEPNS_9MarkStackE(
    const QV4::ExecutableCompilationUnit *self,
    QV4::MarkStack *markStack) {
  self->mark(markStack);
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

//  QV4::Function *QV4::ExecutableCompilationUnit::rootFunction()
extern "C" Q_DECL_EXPORT
QV4::Function *ritual_ZN3QV425ExecutableCompilationUnit12rootFunctionEv(
    QV4::ExecutableCompilationUnit *self) {
  return self->rootFunction();
}

//  quint32 QV4::ExecutableCompilationUnit::totalStringCount() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK3QV425ExecutableCompilationUnit16totalStringCountEv(
    const QV4::ExecutableCompilationUnit *self) {
  return self->totalStringCount();
}

//  QUrl QV4::ExecutableCompilationUnit::urlAt(int index) const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK3QV425ExecutableCompilationUnit5urlAtEi(
    const QV4::ExecutableCompilationUnit *self,
    int index) {
  return new QUrl(self->urlAt(index));
}
