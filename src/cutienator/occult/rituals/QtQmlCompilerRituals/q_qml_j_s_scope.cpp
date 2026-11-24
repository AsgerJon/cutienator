//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljsscope_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtQmlCompiler/QtQmlCompiler>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljsscope_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljsmetatypes_p.h>
#include <QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljsannotation_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qanystringview.h>
#include <QtCore/qtyperevision.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmljssourcelocation_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qlist.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>

//  void QQmlJSScope::insertJSIdentifier(const QString &name, const
//      JavaScriptIdentifier &identifier)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQmlJSScope18insertJSIdentifierERK7QStringRKNS_20JavaScriptIdentifierE(
    QQmlJSScope *self,
    const QString *name,
    const QQmlJSScope::JavaScriptIdentifier *identifier) {
  self->insertJSIdentifier(*name, *identifier);
}

//  ScopeType QQmlJSScope::scopeType() const
extern "C" Q_DECL_EXPORT
QQmlJSScope::ScopeType ritual_ZNK11QQmlJSScope9scopeTypeEv(
    const QQmlJSScope *self) {
  return self->scopeType();
}

//  void QQmlJSScope::setScopeType(ScopeType type)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQmlJSScope12setScopeTypeEN6QQmlSA9ScopeTypeE(
    QQmlJSScope *self,
    QQmlJSScope::ScopeType type) {
  self->setScopeType(type);
}

//  void QQmlJSScope::addOwnMethod(const QQmlJSMetaMethod &method)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQmlJSScope12addOwnMethodERK16QQmlJSMetaMethod(
    QQmlJSScope *self,
    const QQmlJSMetaMethod *method) {
  self->addOwnMethod(*method);
}

//  QList<QQmlJSMetaMethod> QQmlJSScope::ownMethods(const QString &name)
//      const
extern "C" Q_DECL_EXPORT
QList<QQmlJSMetaMethod> *ritual_ZNK11QQmlJSScope10ownMethodsERK7QString(
    const QQmlJSScope *self,
    const QString *name) {
  return new QList<QQmlJSMetaMethod>(self->ownMethods(*name));
}

//  bool QQmlJSScope::hasOwnMethod(const QString &name) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QQmlJSScope12hasOwnMethodERK7QString(
    const QQmlJSScope *self,
    const QString *name) {
  return self->hasOwnMethod(*name);
}

//  bool QQmlJSScope::hasMethod(const QString &name) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QQmlJSScope9hasMethodERK7QString(
    const QQmlJSScope *self,
    const QString *name) {
  return self->hasMethod(*name);
}

//  QHash<QString, QQmlJSMetaMethod> QQmlJSScope::methods() const
extern "C" Q_DECL_EXPORT
QHash<QString, QQmlJSMetaMethod> *ritual_ZNK11QQmlJSScope7methodsEv(
    const QQmlJSScope *self) {
  return new QHash<QString, QQmlJSMetaMethod>(self->methods());
}

//  QList<QQmlJSMetaMethod> QQmlJSScope::methods(const QString &name) const
extern "C" Q_DECL_EXPORT
QList<QQmlJSMetaMethod> *ritual_ZNK11QQmlJSScope7methodsERK7QString(
    const QQmlJSScope *self,
    const QString *name) {
  return new QList<QQmlJSMetaMethod>(self->methods(*name));
}

//  QList<QQmlJSMetaMethod> QQmlJSScope::methods(const QString &name,
//      QQmlJSMetaMethodType type) const
extern "C" Q_DECL_EXPORT
QList<QQmlJSMetaMethod> *ritual_ZNK11QQmlJSScope7methodsERK7QStringN6QQmlSA10MethodTypeE(
    const QQmlJSScope *self,
    const QString *name,
    QQmlJSMetaMethodType type) {
  return new QList<QQmlJSMetaMethod>(self->methods(*name, type));
}

//  void QQmlJSScope::addOwnEnumeration(const QQmlJSMetaEnum &enumeration)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQmlJSScope17addOwnEnumerationERK14QQmlJSMetaEnum(
    QQmlJSScope *self,
    const QQmlJSMetaEnum *enumeration) {
  self->addOwnEnumeration(*enumeration);
}

//  QHash<QString, QQmlJSMetaEnum> QQmlJSScope::ownEnumerations() const
extern "C" Q_DECL_EXPORT
QHash<QString, QQmlJSMetaEnum> *ritual_ZNK11QQmlJSScope15ownEnumerationsEv(
    const QQmlJSScope *self) {
  return new QHash<QString, QQmlJSMetaEnum>(self->ownEnumerations());
}

//  QQmlJSMetaEnum QQmlJSScope::ownEnumeration(const QString &name) const
extern "C" Q_DECL_EXPORT
QQmlJSMetaEnum *ritual_ZNK11QQmlJSScope14ownEnumerationERK7QString(
    const QQmlJSScope *self,
    const QString *name) {
  return new QQmlJSMetaEnum(self->ownEnumeration(*name));
}

//  bool QQmlJSScope::hasOwnEnumeration(const QString &name) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QQmlJSScope17hasOwnEnumerationERK7QString(
    const QQmlJSScope *self,
    const QString *name) {
  return self->hasOwnEnumeration(*name);
}

//  bool QQmlJSScope::hasEnumeration(const QString &name) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QQmlJSScope14hasEnumerationERK7QString(
    const QQmlJSScope *self,
    const QString *name) {
  return self->hasEnumeration(*name);
}

//  bool QQmlJSScope::hasEnumerationKey(const QString &name) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QQmlJSScope17hasEnumerationKeyERK7QString(
    const QQmlJSScope *self,
    const QString *name) {
  return self->hasEnumerationKey(*name);
}

//  bool QQmlJSScope::hasOwnEnumerationKey(const QString &name) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QQmlJSScope20hasOwnEnumerationKeyERK7QString(
    const QQmlJSScope *self,
    const QString *name) {
  return self->hasOwnEnumerationKey(*name);
}

//  QQmlJSMetaEnum QQmlJSScope::enumeration(const QString &name) const
extern "C" Q_DECL_EXPORT
QQmlJSMetaEnum *ritual_ZNK11QQmlJSScope11enumerationERK7QString(
    const QQmlJSScope *self,
    const QString *name) {
  return new QQmlJSMetaEnum(self->enumeration(*name));
}

//  QHash<QString, QQmlJSMetaEnum> QQmlJSScope::enumerations() const
extern "C" Q_DECL_EXPORT
QHash<QString, QQmlJSMetaEnum> *ritual_ZNK11QQmlJSScope12enumerationsEv(
    const QQmlJSScope *self) {
  return new QHash<QString, QQmlJSMetaEnum>(self->enumerations());
}

//  void QQmlJSScope::setAnnotations(const QList<QQmlJSAnnotation>
//      &annotations)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQmlJSScope14setAnnotationsERK5QListI16QQmlJSAnnotationE(
    QQmlJSScope *self,
    const QList<QQmlJSAnnotation> *annotations) {
  self->setAnnotations(*annotations);
}

//  const QList<QQmlJSAnnotation> &QQmlJSScope::annotations() const
extern "C" Q_DECL_EXPORT
QList<QQmlJSAnnotation> *ritual_ZNK11QQmlJSScope11annotationsEv(
    const QQmlJSScope *self) {
  return new QList<QQmlJSAnnotation>(self->annotations());
}

//  QString QQmlJSScope::filePath() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QQmlJSScope8filePathEv(const QQmlJSScope *self) {
  return new QString(self->filePath());
}

//  void QQmlJSScope::setFilePath(const QString &file)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQmlJSScope11setFilePathERK7QString(
    QQmlJSScope *self,
    const QString *file) {
  self->setFilePath(*file);
}

//  quint32 QQmlJSScope::lineNumber() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK11QQmlJSScope10lineNumberEv(const QQmlJSScope *self) {
  return self->lineNumber();
}

//  void QQmlJSScope::setLineNumber(quint32 lineNumber)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQmlJSScope13setLineNumberEj(
    QQmlJSScope *self,
    quint32 lineNumber) {
  self->setLineNumber(lineNumber);
}

//  QString QQmlJSScope::resolvedFilePath() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QQmlJSScope16resolvedFilePathEv(
    const QQmlJSScope *self) {
  return new QString(self->resolvedFilePath());
}

//  void QQmlJSScope::setResolvedFilePath(const QString &file)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQmlJSScope19setResolvedFilePathERK7QString(
    QQmlJSScope *self,
    const QString *file) {
  self->setResolvedFilePath(*file);
}

//  quint32 QQmlJSScope::lineNumberInResolvedFile() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK11QQmlJSScope24lineNumberInResolvedFileEv(
    const QQmlJSScope *self) {
  return self->lineNumberInResolvedFile();
}

//  void QQmlJSScope::setLineNumberInResolvedFile(quint32 lineNumber)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQmlJSScope27setLineNumberInResolvedFileEj(
    QQmlJSScope *self,
    quint32 lineNumber) {
  self->setLineNumberInResolvedFile(lineNumber);
}

//  QString QQmlJSScope::internalName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QQmlJSScope12internalNameEv(const QQmlJSScope *self) {
  return new QString(self->internalName());
}

//  void QQmlJSScope::setInternalName(const QString &internalName)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQmlJSScope15setInternalNameERK7QString(
    QQmlJSScope *self,
    const QString *internalName) {
  self->setInternalName(*internalName);
}

//  QString QQmlJSScope::augmentedInternalName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QQmlJSScope21augmentedInternalNameEv(
    const QQmlJSScope *self) {
  return new QString(self->augmentedInternalName());
}

//  QString QQmlJSScope::prettyName(QAnyStringView name)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11QQmlJSScope10prettyNameE14QAnyStringView(
    const QString *name) {
  return new QString(QQmlJSScope::prettyName(QAnyStringView(*name)));
}

//  IsComponentRoot QQmlJSScope::componentRootStatus() const
extern "C" Q_DECL_EXPORT
QQmlJSScope::IsComponentRoot ritual_ZNK11QQmlJSScope19componentRootStatusEv(
    const QQmlJSScope *self) {
  return self->componentRootStatus();
}

//  void QQmlJSScope::setAliases(const QStringList &aliases)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQmlJSScope10setAliasesERK5QListI7QStringE(
    QQmlJSScope *self,
    const QList<QString> *aliases) {
  self->setAliases(*aliases);
}

//  QStringList QQmlJSScope::aliases() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK11QQmlJSScope7aliasesEv(const QQmlJSScope *self) {
  return new QList<QString>(self->aliases());
}

//  void QQmlJSScope::setInterfaceNames(const QStringList &interfaces)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQmlJSScope17setInterfaceNamesERK5QListI7QStringE(
    QQmlJSScope *self,
    const QList<QString> *interfaces) {
  self->setInterfaceNames(*interfaces);
}

//  QStringList QQmlJSScope::interfaceNames() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK11QQmlJSScope14interfaceNamesEv(
    const QQmlJSScope *self) {
  return new QList<QString>(self->interfaceNames());
}

//  bool QQmlJSScope::hasInterface(const QString &name) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QQmlJSScope12hasInterfaceERK7QString(
    const QQmlJSScope *self,
    const QString *name) {
  return self->hasInterface(*name);
}

//  bool QQmlJSScope::hasOwnInterface(const QString &name) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QQmlJSScope15hasOwnInterfaceERK7QString(
    const QQmlJSScope *self,
    const QString *name) {
  return self->hasOwnInterface(*name);
}

//  void QQmlJSScope::setOwnDeferredNames(const QStringList &names)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQmlJSScope19setOwnDeferredNamesERK5QListI7QStringE(
    QQmlJSScope *self,
    const QList<QString> *names) {
  self->setOwnDeferredNames(*names);
}

//  QStringList QQmlJSScope::ownDeferredNames() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK11QQmlJSScope16ownDeferredNamesEv(
    const QQmlJSScope *self) {
  return new QList<QString>(self->ownDeferredNames());
}

//  void QQmlJSScope::setOwnImmediateNames(const QStringList &names)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQmlJSScope20setOwnImmediateNamesERK5QListI7QStringE(
    QQmlJSScope *self,
    const QList<QString> *names) {
  self->setOwnImmediateNames(*names);
}

//  QStringList QQmlJSScope::ownImmediateNames() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK11QQmlJSScope17ownImmediateNamesEv(
    const QQmlJSScope *self) {
  return new QList<QString>(self->ownImmediateNames());
}

//  bool QQmlJSScope::isNameDeferred(const QString &name) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QQmlJSScope14isNameDeferredERK7QString(
    const QQmlJSScope *self,
    const QString *name) {
  return self->isNameDeferred(*name);
}

//  void QQmlJSScope::setBaseTypeName(const QString &baseTypeName)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQmlJSScope15setBaseTypeNameERK7QString(
    QQmlJSScope *self,
    const QString *baseTypeName) {
  self->setBaseTypeName(*baseTypeName);
}

//  QString QQmlJSScope::baseTypeName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QQmlJSScope12baseTypeNameEv(const QQmlJSScope *self) {
  return new QString(self->baseTypeName());
}

//  QTypeRevision QQmlJSScope::baseTypeRevision() const
extern "C" Q_DECL_EXPORT
QTypeRevision *ritual_ZNK11QQmlJSScope16baseTypeRevisionEv(
    const QQmlJSScope *self) {
  return new QTypeRevision(self->baseTypeRevision());
}

//  QString QQmlJSScope::moduleName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QQmlJSScope10moduleNameEv(const QQmlJSScope *self) {
  return new QString(self->moduleName());
}

//  QString QQmlJSScope::ownModuleName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QQmlJSScope13ownModuleNameEv(const QQmlJSScope *self) {
  return new QString(self->ownModuleName());
}

//  void QQmlJSScope::setOwnModuleName(const QString &moduleName)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQmlJSScope16setOwnModuleNameERK7QString(
    QQmlJSScope *self,
    const QString *moduleName) {
  self->setOwnModuleName(*moduleName);
}

//  void QQmlJSScope::clearBaseType()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQmlJSScope13clearBaseTypeEv(QQmlJSScope *self) {
  self->clearBaseType();
}

//  void QQmlJSScope::setBaseTypeError(const QString &baseTypeError)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQmlJSScope16setBaseTypeErrorERK7QString(
    QQmlJSScope *self,
    const QString *baseTypeError) {
  self->setBaseTypeError(*baseTypeError);
}

//  QString QQmlJSScope::baseTypeError() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QQmlJSScope13baseTypeErrorEv(const QQmlJSScope *self) {
  return new QString(self->baseTypeError());
}

//  void QQmlJSScope::addOwnProperty(const QQmlJSMetaProperty &prop)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQmlJSScope14addOwnPropertyERK18QQmlJSMetaProperty(
    QQmlJSScope *self,
    const QQmlJSMetaProperty *prop) {
  self->addOwnProperty(*prop);
}

//  QHash<QString, QQmlJSMetaProperty> QQmlJSScope::ownProperties() const
extern "C" Q_DECL_EXPORT
QHash<QString, QQmlJSMetaProperty> *ritual_ZNK11QQmlJSScope13ownPropertiesEv(
    const QQmlJSScope *self) {
  return new QHash<QString, QQmlJSMetaProperty>(self->ownProperties());
}

//  QQmlJSMetaProperty QQmlJSScope::ownProperty(const QString &name) const
extern "C" Q_DECL_EXPORT
QQmlJSMetaProperty *ritual_ZNK11QQmlJSScope11ownPropertyERK7QString(
    const QQmlJSScope *self,
    const QString *name) {
  return new QQmlJSMetaProperty(self->ownProperty(*name));
}

//  bool QQmlJSScope::hasOwnProperty(const QString &name) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QQmlJSScope14hasOwnPropertyERK7QString(
    const QQmlJSScope *self,
    const QString *name) {
  return self->hasOwnProperty(*name);
}

//  bool QQmlJSScope::hasProperty(const QString &name) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QQmlJSScope11hasPropertyERK7QString(
    const QQmlJSScope *self,
    const QString *name) {
  return self->hasProperty(*name);
}

//  QQmlJSMetaProperty QQmlJSScope::property(const QString &name) const
extern "C" Q_DECL_EXPORT
QQmlJSMetaProperty *ritual_ZNK11QQmlJSScope8propertyERK7QString(
    const QQmlJSScope *self,
    const QString *name) {
  return new QQmlJSMetaProperty(self->property(*name));
}

//  QHash<QString, QQmlJSMetaProperty> QQmlJSScope::properties() const
extern "C" Q_DECL_EXPORT
QHash<QString, QQmlJSMetaProperty> *ritual_ZNK11QQmlJSScope10propertiesEv(
    const QQmlJSScope *self) {
  return new QHash<QString, QQmlJSMetaProperty>(self->properties());
}

//  void QQmlJSScope::setPropertyLocallyRequired(const QString &name, bool
//      isRequired)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQmlJSScope26setPropertyLocallyRequiredERK7QStringb(
    QQmlJSScope *self,
    const QString *name,
    bool isRequired) {
  self->setPropertyLocallyRequired(*name, isRequired);
}

//  bool QQmlJSScope::isPropertyRequired(const QString &name) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QQmlJSScope18isPropertyRequiredERK7QString(
    const QQmlJSScope *self,
    const QString *name) {
  return self->isPropertyRequired(*name);
}

//  bool QQmlJSScope::isPropertyLocallyRequired(const QString &name) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QQmlJSScope25isPropertyLocallyRequiredERK7QString(
    const QQmlJSScope *self,
    const QString *name) {
  return self->isPropertyLocallyRequired(*name);
}

//  void QQmlJSScope::addOwnPropertyBinding(const QQmlJSMetaPropertyBinding
//      &binding, BindingTargetSpecifier specifier)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQmlJSScope21addOwnPropertyBindingERK25QQmlJSMetaPropertyBindingNS_22BindingTargetSpecifierE(
    QQmlJSScope *self,
    const QQmlJSMetaPropertyBinding *binding,
    QQmlJSScope::BindingTargetSpecifier specifier) {
  self->addOwnPropertyBinding(*binding, specifier);
}

//  QList<QQmlJSMetaPropertyBinding>
//      QQmlJSScope::ownPropertyBindingsInQmlIROrder() const
extern "C" Q_DECL_EXPORT
QList<QQmlJSMetaPropertyBinding> *ritual_ZNK11QQmlJSScope31ownPropertyBindingsInQmlIROrderEv(
    const QQmlJSScope *self) {
  return new QList<QQmlJSMetaPropertyBinding>(
      self->ownPropertyBindingsInQmlIROrder());
}

//  bool QQmlJSScope::hasOwnPropertyBindings(const QString &name) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QQmlJSScope22hasOwnPropertyBindingsERK7QString(
    const QQmlJSScope *self,
    const QString *name) {
  return self->hasOwnPropertyBindings(*name);
}

//  bool QQmlJSScope::hasPropertyBindings(const QString &name) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QQmlJSScope19hasPropertyBindingsERK7QString(
    const QQmlJSScope *self,
    const QString *name) {
  return self->hasPropertyBindings(*name);
}

//  QList<QQmlJSMetaPropertyBinding> QQmlJSScope::propertyBindings(const
//      QString &name) const
extern "C" Q_DECL_EXPORT
QList<QQmlJSMetaPropertyBinding> *ritual_ZNK11QQmlJSScope16propertyBindingsERK7QString(
    const QQmlJSScope *self,
    const QString *name) {
  return new QList<QQmlJSMetaPropertyBinding>(self->propertyBindings(*name));
}

//  bool QQmlJSScope::isResolved() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QQmlJSScope10isResolvedEv(const QQmlJSScope *self) {
  return self->isResolved();
}

//  bool QQmlJSScope::isFullyResolved() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QQmlJSScope15isFullyResolvedEv(const QQmlJSScope *self) {
  return self->isFullyResolved();
}

//  QString QQmlJSScope::ownDefaultPropertyName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QQmlJSScope22ownDefaultPropertyNameEv(
    const QQmlJSScope *self) {
  return new QString(self->ownDefaultPropertyName());
}

//  void QQmlJSScope::setOwnDefaultPropertyName(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQmlJSScope25setOwnDefaultPropertyNameERK7QString(
    QQmlJSScope *self,
    const QString *name) {
  self->setOwnDefaultPropertyName(*name);
}

//  QString QQmlJSScope::defaultPropertyName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QQmlJSScope19defaultPropertyNameEv(
    const QQmlJSScope *self) {
  return new QString(self->defaultPropertyName());
}

//  QString QQmlJSScope::ownParentPropertyName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QQmlJSScope21ownParentPropertyNameEv(
    const QQmlJSScope *self) {
  return new QString(self->ownParentPropertyName());
}

//  void QQmlJSScope::setOwnParentPropertyName(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQmlJSScope24setOwnParentPropertyNameERK7QString(
    QQmlJSScope *self,
    const QString *name) {
  self->setOwnParentPropertyName(*name);
}

//  QString QQmlJSScope::parentPropertyName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QQmlJSScope18parentPropertyNameEv(
    const QQmlJSScope *self) {
  return new QString(self->parentPropertyName());
}

//  QString QQmlJSScope::ownAttachedTypeName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QQmlJSScope19ownAttachedTypeNameEv(
    const QQmlJSScope *self) {
  return new QString(self->ownAttachedTypeName());
}

//  void QQmlJSScope::setOwnAttachedTypeName(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQmlJSScope22setOwnAttachedTypeNameERK7QString(
    QQmlJSScope *self,
    const QString *name) {
  self->setOwnAttachedTypeName(*name);
}

//  QString QQmlJSScope::attachedTypeName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QQmlJSScope16attachedTypeNameEv(
    const QQmlJSScope *self) {
  return new QString(self->attachedTypeName());
}

//  QString QQmlJSScope::extensionTypeName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QQmlJSScope17extensionTypeNameEv(
    const QQmlJSScope *self) {
  return new QString(self->extensionTypeName());
}

//  void QQmlJSScope::setExtensionTypeName(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQmlJSScope20setExtensionTypeNameERK7QString(
    QQmlJSScope *self,
    const QString *name) {
  self->setExtensionTypeName(*name);
}

//  AnnotatedScope QQmlJSScope::extensionType() const
extern "C" Q_DECL_EXPORT
QQmlJSScope::AnnotatedScope *ritual_ZNK11QQmlJSScope13extensionTypeEv(
    const QQmlJSScope *self) {
  return new QQmlJSScope::AnnotatedScope(self->extensionType());
}

//  QString QQmlJSScope::elementTypeName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QQmlJSScope15elementTypeNameEv(
    const QQmlJSScope *self) {
  return new QString(self->elementTypeName());
}

//  void QQmlJSScope::setElementTypeName(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQmlJSScope18setElementTypeNameERK7QString(
    QQmlJSScope *self,
    const QString *name) {
  self->setElementTypeName(*name);
}

//  void QQmlJSScope::addOwnRuntimeFunctionIndex(QQmlJSMetaMethod::AbsoluteFu
//      nctionIndex index)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQmlJSScope26addOwnRuntimeFunctionIndexEN16QQmlJSMetaMethod21AbsoluteFunctionIndexE(
    QQmlJSScope *self,
    QQmlJSMetaMethod::AbsoluteFunctionIndex index) {
  self->addOwnRuntimeFunctionIndex(index);
}

//  QQmlJSMetaMethod::AbsoluteFunctionIndex QQmlJSScope::ownRuntimeFunctionIn
//      dex(QQmlJSMetaMethod::RelativeFunctionIndex index) const
extern "C" Q_DECL_EXPORT
QQmlJSMetaMethod::AbsoluteFunctionIndex ritual_ZNK11QQmlJSScope23ownRuntimeFunctionIndexEN16QQmlJSMetaMethod21RelativeFunctionIndexE(
    const QQmlJSScope *self,
    QQmlJSMetaMethod::RelativeFunctionIndex index) {
  return self->ownRuntimeFunctionIndex(index);
}

//  bool QQmlJSScope::isComposite() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QQmlJSScope11isCompositeEv(const QQmlJSScope *self) {
  return self->isComposite();
}

//  void QQmlJSScope::setIsComposite(bool v)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQmlJSScope14setIsCompositeEb(QQmlJSScope *self, bool v) {
  self->setIsComposite(v);
}

//  bool QQmlJSScope::isJavaScriptBuiltin() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QQmlJSScope19isJavaScriptBuiltinEv(
    const QQmlJSScope *self) {
  return self->isJavaScriptBuiltin();
}

//  void QQmlJSScope::setIsJavaScriptBuiltin(bool v)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQmlJSScope22setIsJavaScriptBuiltinEb(
    QQmlJSScope *self,
    bool v) {
  self->setIsJavaScriptBuiltin(v);
}

//  bool QQmlJSScope::isOpaqueType() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QQmlJSScope12isOpaqueTypeEv(const QQmlJSScope *self) {
  return self->isOpaqueType();
}

//  void QQmlJSScope::setIsTypeOpaque(bool v)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQmlJSScope15setIsTypeOpaqueEb(QQmlJSScope *self, bool v) {
  self->setIsTypeOpaque(v);
}

//  bool QQmlJSScope::isScript() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QQmlJSScope8isScriptEv(const QQmlJSScope *self) {
  return self->isScript();
}

//  void QQmlJSScope::setIsScript(bool v)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQmlJSScope11setIsScriptEb(QQmlJSScope *self, bool v) {
  self->setIsScript(v);
}

//  bool QQmlJSScope::hasCustomParser() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QQmlJSScope15hasCustomParserEv(const QQmlJSScope *self) {
  return self->hasCustomParser();
}

//  void QQmlJSScope::setHasCustomParser(bool v)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQmlJSScope18setHasCustomParserEb(
    QQmlJSScope *self,
    bool v) {
  self->setHasCustomParser(v);
}

//  bool QQmlJSScope::isArrayScope() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QQmlJSScope12isArrayScopeEv(const QQmlJSScope *self) {
  return self->isArrayScope();
}

//  void QQmlJSScope::setIsArrayScope(bool v)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQmlJSScope15setIsArrayScopeEb(QQmlJSScope *self, bool v) {
  self->setIsArrayScope(v);
}

//  bool QQmlJSScope::isInlineComponent() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QQmlJSScope17isInlineComponentEv(const QQmlJSScope *self) {
  return self->isInlineComponent();
}

//  void QQmlJSScope::setIsInlineComponent(bool v)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQmlJSScope20setIsInlineComponentEb(
    QQmlJSScope *self,
    bool v) {
  self->setIsInlineComponent(v);
}

//  bool QQmlJSScope::isWrappedInImplicitComponent() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QQmlJSScope28isWrappedInImplicitComponentEv(
    const QQmlJSScope *self) {
  return self->isWrappedInImplicitComponent();
}

//  void QQmlJSScope::setIsWrappedInImplicitComponent(bool v)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQmlJSScope31setIsWrappedInImplicitComponentEb(
    QQmlJSScope *self,
    bool v) {
  self->setIsWrappedInImplicitComponent(v);
}

//  bool QQmlJSScope::isAssignedToUnknownProperty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QQmlJSScope27isAssignedToUnknownPropertyEv(
    const QQmlJSScope *self) {
  return self->isAssignedToUnknownProperty();
}

//  void QQmlJSScope::setAssignedToUnknownProperty(bool v)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQmlJSScope28setAssignedToUnknownPropertyEb(
    QQmlJSScope *self,
    bool v) {
  self->setAssignedToUnknownProperty(v);
}

//  bool QQmlJSScope::extensionIsJavaScript() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QQmlJSScope21extensionIsJavaScriptEv(
    const QQmlJSScope *self) {
  return self->extensionIsJavaScript();
}

//  void QQmlJSScope::setExtensionIsJavaScript(bool v)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQmlJSScope24setExtensionIsJavaScriptEb(
    QQmlJSScope *self,
    bool v) {
  self->setExtensionIsJavaScript(v);
}

//  bool QQmlJSScope::extensionIsNamespace() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QQmlJSScope20extensionIsNamespaceEv(
    const QQmlJSScope *self) {
  return self->extensionIsNamespace();
}

//  void QQmlJSScope::setExtensionIsNamespace(bool v)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQmlJSScope23setExtensionIsNamespaceEb(
    QQmlJSScope *self,
    bool v) {
  self->setExtensionIsNamespace(v);
}

//  bool QQmlJSScope::isListProperty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QQmlJSScope14isListPropertyEv(const QQmlJSScope *self) {
  return self->isListProperty();
}

//  void QQmlJSScope::setIsListProperty(bool v)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQmlJSScope17setIsListPropertyEb(QQmlJSScope *self, bool v) {
  self->setIsListProperty(v);
}

//  bool QQmlJSScope::isSingleton() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QQmlJSScope11isSingletonEv(const QQmlJSScope *self) {
  return self->isSingleton();
}

//  void QQmlJSScope::setIsSingleton(bool v)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQmlJSScope14setIsSingletonEb(QQmlJSScope *self, bool v) {
  self->setIsSingleton(v);
}

//  bool QQmlJSScope::enforcesScopedEnums() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QQmlJSScope19enforcesScopedEnumsEv(
    const QQmlJSScope *self) {
  return self->enforcesScopedEnums();
}

//  void QQmlJSScope::setEnforcesScopedEnumsFlag(bool v)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQmlJSScope26setEnforcesScopedEnumsFlagEb(
    QQmlJSScope *self,
    bool v) {
  self->setEnforcesScopedEnumsFlag(v);
}

//  bool QQmlJSScope::isCreatable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QQmlJSScope11isCreatableEv(const QQmlJSScope *self) {
  return self->isCreatable();
}

//  void QQmlJSScope::setCreatableFlag(bool v)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQmlJSScope16setCreatableFlagEb(QQmlJSScope *self, bool v) {
  self->setCreatableFlag(v);
}

//  bool QQmlJSScope::isStructured() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QQmlJSScope12isStructuredEv(const QQmlJSScope *self) {
  return self->isStructured();
}

//  void QQmlJSScope::setStructuredFlag(bool v)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQmlJSScope17setStructuredFlagEb(QQmlJSScope *self, bool v) {
  self->setStructuredFlag(v);
}

//  bool QQmlJSScope::isFileRootComponent() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QQmlJSScope19isFileRootComponentEv(
    const QQmlJSScope *self) {
  return self->isFileRootComponent();
}

//  void QQmlJSScope::setIsRootFileComponentFlag(bool v)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQmlJSScope26setIsRootFileComponentFlagEb(
    QQmlJSScope *self,
    bool v) {
  self->setIsRootFileComponentFlag(v);
}

//  bool QQmlJSScope::isSelfExtension() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QQmlJSScope15isSelfExtensionEv(const QQmlJSScope *self) {
  return self->isSelfExtension();
}

//  void QQmlJSScope::setIsSelfExtension(bool v)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQmlJSScope18setIsSelfExtensionEb(
    QQmlJSScope *self,
    bool v) {
  self->setIsSelfExtension(v);
}

//  void QQmlJSScope::setAccessSemantics(AccessSemantics semantics)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQmlJSScope18setAccessSemanticsEN6QQmlSA15AccessSemanticsE(
    QQmlJSScope *self,
    QQmlJSScope::AccessSemantics semantics) {
  self->setAccessSemantics(semantics);
}

//  AccessSemantics QQmlJSScope::accessSemantics() const
extern "C" Q_DECL_EXPORT
QQmlJSScope::AccessSemantics ritual_ZNK11QQmlJSScope15accessSemanticsEv(
    const QQmlJSScope *self) {
  return self->accessSemantics();
}

//  bool QQmlJSScope::isReferenceType() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QQmlJSScope15isReferenceTypeEv(const QQmlJSScope *self) {
  return self->isReferenceType();
}

//  bool QQmlJSScope::isValueType() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QQmlJSScope11isValueTypeEv(const QQmlJSScope *self) {
  return self->isValueType();
}

//  void QQmlJSScope::setInlineComponentName(const QString
//      &inlineComponentName)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQmlJSScope22setInlineComponentNameERK7QString(
    QQmlJSScope *self,
    const QString *inlineComponentName) {
  self->setInlineComponentName(*inlineComponentName);
}

//  void QQmlJSScope::setSourceLocation(const QQmlJS::SourceLocation
//      &sourceLocation)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQmlJSScope17setSourceLocationERKN6QQmlJS14SourceLocationE(
    QQmlJSScope *self,
    const QQmlJS::SourceLocation *sourceLocation) {
  self->setSourceLocation(*sourceLocation);
}

//  QQmlJS::SourceLocation QQmlJSScope::sourceLocation() const
extern "C" Q_DECL_EXPORT
QQmlJS::SourceLocation *ritual_ZNK11QQmlJSScope14sourceLocationEv(
    const QQmlJSScope *self) {
  return new QQmlJS::SourceLocation(self->sourceLocation());
}

//  void QQmlJSScope::setIdSourceLocation(const QQmlJS::SourceLocation
//      &sourceLocation)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQmlJSScope19setIdSourceLocationERKN6QQmlJS14SourceLocationE(
    QQmlJSScope *self,
    const QQmlJS::SourceLocation *sourceLocation) {
  self->setIdSourceLocation(*sourceLocation);
}

//  QQmlJS::SourceLocation QQmlJSScope::idSourceLocation() const
extern "C" Q_DECL_EXPORT
QQmlJS::SourceLocation *ritual_ZNK11QQmlJSScope16idSourceLocationEv(
    const QQmlJSScope *self) {
  return new QQmlJS::SourceLocation(self->idSourceLocation());
}

//  bool QQmlJSScope::isInCustomParserParent() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QQmlJSScope22isInCustomParserParentEv(
    const QQmlJSScope *self) {
  return self->isInCustomParserParent();
}

//  qsizetype QQmlJSScope::sizeofQQmlSAElement()
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZN11QQmlJSScope19sizeofQQmlSAElementEv() {
  return QQmlJSScope::sizeofQQmlSAElement();
}

//  QQmlJSScope::QQmlJSScope(const QString &internalName)
extern "C" Q_DECL_EXPORT
QQmlJSScope *ritual_ZN11QQmlJSScopeC1ERK7QString(
    const QString *internalName) {
  return new QQmlJSScope(*internalName);
}

//  QQmlJSScope::QQmlJSScope()
extern "C" Q_DECL_EXPORT
QQmlJSScope *ritual_ZN11QQmlJSScopeC1Ev() {
  return new QQmlJSScope();
}

//  void QQmlJSScope::addOwnPropertyBindingInQmlIROrder(const
//      QQmlJSMetaPropertyBinding &binding, BindingTargetSpecifier specifier)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQmlJSScope33addOwnPropertyBindingInQmlIROrderERK25QQmlJSMetaPropertyBindingNS_22BindingTargetSpecifierE(
    QQmlJSScope *self,
    const QQmlJSMetaPropertyBinding *binding,
    QQmlJSScope::BindingTargetSpecifier specifier) {
  self->addOwnPropertyBindingInQmlIROrder(*binding, specifier);
}

//  bool QQmlJSScope::hasEnforcesScopedEnumsFlag() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QQmlJSScope26hasEnforcesScopedEnumsFlagEv(
    const QQmlJSScope *self) {
  return self->hasEnforcesScopedEnumsFlag();
}

//  bool QQmlJSScope::hasCreatableFlag() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QQmlJSScope16hasCreatableFlagEv(const QQmlJSScope *self) {
  return self->hasCreatableFlag();
}

//  bool QQmlJSScope::hasStructuredFlag() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QQmlJSScope17hasStructuredFlagEv(const QQmlJSScope *self) {
  return self->hasStructuredFlag();
}
