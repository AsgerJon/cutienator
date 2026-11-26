//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljstyperesolver_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtQmlCompiler/QtQmlCompiler>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljstyperesolver_p.h>
#include <QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljsregistercontent_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4compileddata_p.h>
#include <QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljsscopesbyid_p.h>
#include <QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljsmetatypes_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qlist.h>
#include <QtCore/QString>
#include <QtCore/QFlags>

//  QQmlJSTypeResolver::QQmlJSTypeResolver(QQmlJSImporter *importer)
extern "C" Q_DECL_EXPORT
QQmlJSTypeResolver *ritual_ZN18QQmlJSTypeResolverC1EP14QQmlJSImporter(
    QQmlJSImporter *importer) {
  return new QQmlJSTypeResolver(importer);
}

//  void QQmlJSTypeResolver::init(QQmlJSImportVisitor *visitor,
//      QQmlJS::AST::Node *program)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlJSTypeResolver4initEP19QQmlJSImportVisitorPN6QQmlJS3AST4NodeE(
    QQmlJSTypeResolver *self,
    QQmlJSImportVisitor *visitor,
    QQmlJS::AST::Node *program) {
  self->init(visitor, program);
}

//  QQmlJSRegisterContentPool *QQmlJSTypeResolver::registerContentPool()
//      const
extern "C" Q_DECL_EXPORT
QQmlJSRegisterContentPool *ritual_ZNK18QQmlJSTypeResolver19registerContentPoolEv(
    const QQmlJSTypeResolver *self) {
  return self->registerContentPool();
}

//  QQmlJSLogger *QQmlJSTypeResolver::logger() const
extern "C" Q_DECL_EXPORT
QQmlJSLogger *ritual_ZNK18QQmlJSTypeResolver6loggerEv(
    const QQmlJSTypeResolver *self) {
  return self->logger();
}

//  void QQmlJSTypeResolver::setParentMode(ParentMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlJSTypeResolver13setParentModeENS_10ParentModeE(
    QQmlJSTypeResolver *self,
    QQmlJSTypeResolver::ParentMode mode) {
  self->setParentMode(mode);
}

//  ParentMode QQmlJSTypeResolver::parentMode() const
extern "C" Q_DECL_EXPORT
QQmlJSTypeResolver::ParentMode ritual_ZNK18QQmlJSTypeResolver10parentModeEv(
    const QQmlJSTypeResolver *self) {
  return self->parentMode();
}

//  void QQmlJSTypeResolver::setCloneMode(CloneMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlJSTypeResolver12setCloneModeENS_9CloneModeE(
    QQmlJSTypeResolver *self,
    QQmlJSTypeResolver::CloneMode mode) {
  self->setCloneMode(mode);
}

//  CloneMode QQmlJSTypeResolver::cloneMode() const
extern "C" Q_DECL_EXPORT
QQmlJSTypeResolver::CloneMode ritual_ZNK18QQmlJSTypeResolver9cloneModeEv(
    const QQmlJSTypeResolver *self) {
  return self->cloneMode();
}

//  QQmlJSScope::ConstPtr QQmlJSTypeResolver::voidType() const
extern "C" Q_DECL_EXPORT
QQmlJSScope::ConstPtr *ritual_ZNK18QQmlJSTypeResolver8voidTypeEv(
    const QQmlJSTypeResolver *self) {
  return new QQmlJSScope::ConstPtr(self->voidType());
}

//  QQmlJSScope::ConstPtr QQmlJSTypeResolver::emptyType() const
extern "C" Q_DECL_EXPORT
QQmlJSScope::ConstPtr *ritual_ZNK18QQmlJSTypeResolver9emptyTypeEv(
    const QQmlJSTypeResolver *self) {
  return new QQmlJSScope::ConstPtr(self->emptyType());
}

//  QQmlJSScope::ConstPtr QQmlJSTypeResolver::nullType() const
extern "C" Q_DECL_EXPORT
QQmlJSScope::ConstPtr *ritual_ZNK18QQmlJSTypeResolver8nullTypeEv(
    const QQmlJSTypeResolver *self) {
  return new QQmlJSScope::ConstPtr(self->nullType());
}

//  QQmlJSScope::ConstPtr QQmlJSTypeResolver::realType() const
extern "C" Q_DECL_EXPORT
QQmlJSScope::ConstPtr *ritual_ZNK18QQmlJSTypeResolver8realTypeEv(
    const QQmlJSTypeResolver *self) {
  return new QQmlJSScope::ConstPtr(self->realType());
}

//  QQmlJSScope::ConstPtr QQmlJSTypeResolver::floatType() const
extern "C" Q_DECL_EXPORT
QQmlJSScope::ConstPtr *ritual_ZNK18QQmlJSTypeResolver9floatTypeEv(
    const QQmlJSTypeResolver *self) {
  return new QQmlJSScope::ConstPtr(self->floatType());
}

//  QQmlJSScope::ConstPtr QQmlJSTypeResolver::int8Type() const
extern "C" Q_DECL_EXPORT
QQmlJSScope::ConstPtr *ritual_ZNK18QQmlJSTypeResolver8int8TypeEv(
    const QQmlJSTypeResolver *self) {
  return new QQmlJSScope::ConstPtr(self->int8Type());
}

//  QQmlJSScope::ConstPtr QQmlJSTypeResolver::uint8Type() const
extern "C" Q_DECL_EXPORT
QQmlJSScope::ConstPtr *ritual_ZNK18QQmlJSTypeResolver9uint8TypeEv(
    const QQmlJSTypeResolver *self) {
  return new QQmlJSScope::ConstPtr(self->uint8Type());
}

//  QQmlJSScope::ConstPtr QQmlJSTypeResolver::int16Type() const
extern "C" Q_DECL_EXPORT
QQmlJSScope::ConstPtr *ritual_ZNK18QQmlJSTypeResolver9int16TypeEv(
    const QQmlJSTypeResolver *self) {
  return new QQmlJSScope::ConstPtr(self->int16Type());
}

//  QQmlJSScope::ConstPtr QQmlJSTypeResolver::uint16Type() const
extern "C" Q_DECL_EXPORT
QQmlJSScope::ConstPtr *ritual_ZNK18QQmlJSTypeResolver10uint16TypeEv(
    const QQmlJSTypeResolver *self) {
  return new QQmlJSScope::ConstPtr(self->uint16Type());
}

//  QQmlJSScope::ConstPtr QQmlJSTypeResolver::int32Type() const
extern "C" Q_DECL_EXPORT
QQmlJSScope::ConstPtr *ritual_ZNK18QQmlJSTypeResolver9int32TypeEv(
    const QQmlJSTypeResolver *self) {
  return new QQmlJSScope::ConstPtr(self->int32Type());
}

//  QQmlJSScope::ConstPtr QQmlJSTypeResolver::uint32Type() const
extern "C" Q_DECL_EXPORT
QQmlJSScope::ConstPtr *ritual_ZNK18QQmlJSTypeResolver10uint32TypeEv(
    const QQmlJSTypeResolver *self) {
  return new QQmlJSScope::ConstPtr(self->uint32Type());
}

//  QQmlJSScope::ConstPtr QQmlJSTypeResolver::int64Type() const
extern "C" Q_DECL_EXPORT
QQmlJSScope::ConstPtr *ritual_ZNK18QQmlJSTypeResolver9int64TypeEv(
    const QQmlJSTypeResolver *self) {
  return new QQmlJSScope::ConstPtr(self->int64Type());
}

//  QQmlJSScope::ConstPtr QQmlJSTypeResolver::uint64Type() const
extern "C" Q_DECL_EXPORT
QQmlJSScope::ConstPtr *ritual_ZNK18QQmlJSTypeResolver10uint64TypeEv(
    const QQmlJSTypeResolver *self) {
  return new QQmlJSScope::ConstPtr(self->uint64Type());
}

//  QQmlJSScope::ConstPtr QQmlJSTypeResolver::sizeType() const
extern "C" Q_DECL_EXPORT
QQmlJSScope::ConstPtr *ritual_ZNK18QQmlJSTypeResolver8sizeTypeEv(
    const QQmlJSTypeResolver *self) {
  return new QQmlJSScope::ConstPtr(self->sizeType());
}

//  QQmlJSScope::ConstPtr QQmlJSTypeResolver::boolType() const
extern "C" Q_DECL_EXPORT
QQmlJSScope::ConstPtr *ritual_ZNK18QQmlJSTypeResolver8boolTypeEv(
    const QQmlJSTypeResolver *self) {
  return new QQmlJSScope::ConstPtr(self->boolType());
}

//  QQmlJSScope::ConstPtr QQmlJSTypeResolver::stringType() const
extern "C" Q_DECL_EXPORT
QQmlJSScope::ConstPtr *ritual_ZNK18QQmlJSTypeResolver10stringTypeEv(
    const QQmlJSTypeResolver *self) {
  return new QQmlJSScope::ConstPtr(self->stringType());
}

//  QQmlJSScope::ConstPtr QQmlJSTypeResolver::stringListType() const
extern "C" Q_DECL_EXPORT
QQmlJSScope::ConstPtr *ritual_ZNK18QQmlJSTypeResolver14stringListTypeEv(
    const QQmlJSTypeResolver *self) {
  return new QQmlJSScope::ConstPtr(self->stringListType());
}

//  QQmlJSScope::ConstPtr QQmlJSTypeResolver::byteArrayType() const
extern "C" Q_DECL_EXPORT
QQmlJSScope::ConstPtr *ritual_ZNK18QQmlJSTypeResolver13byteArrayTypeEv(
    const QQmlJSTypeResolver *self) {
  return new QQmlJSScope::ConstPtr(self->byteArrayType());
}

//  QQmlJSScope::ConstPtr QQmlJSTypeResolver::urlType() const
extern "C" Q_DECL_EXPORT
QQmlJSScope::ConstPtr *ritual_ZNK18QQmlJSTypeResolver7urlTypeEv(
    const QQmlJSTypeResolver *self) {
  return new QQmlJSScope::ConstPtr(self->urlType());
}

//  QQmlJSScope::ConstPtr QQmlJSTypeResolver::dateTimeType() const
extern "C" Q_DECL_EXPORT
QQmlJSScope::ConstPtr *ritual_ZNK18QQmlJSTypeResolver12dateTimeTypeEv(
    const QQmlJSTypeResolver *self) {
  return new QQmlJSScope::ConstPtr(self->dateTimeType());
}

//  QQmlJSScope::ConstPtr QQmlJSTypeResolver::dateType() const
extern "C" Q_DECL_EXPORT
QQmlJSScope::ConstPtr *ritual_ZNK18QQmlJSTypeResolver8dateTypeEv(
    const QQmlJSTypeResolver *self) {
  return new QQmlJSScope::ConstPtr(self->dateType());
}

//  QQmlJSScope::ConstPtr QQmlJSTypeResolver::timeType() const
extern "C" Q_DECL_EXPORT
QQmlJSScope::ConstPtr *ritual_ZNK18QQmlJSTypeResolver8timeTypeEv(
    const QQmlJSTypeResolver *self) {
  return new QQmlJSScope::ConstPtr(self->timeType());
}

//  QQmlJSScope::ConstPtr QQmlJSTypeResolver::regexpType() const
extern "C" Q_DECL_EXPORT
QQmlJSScope::ConstPtr *ritual_ZNK18QQmlJSTypeResolver10regexpTypeEv(
    const QQmlJSTypeResolver *self) {
  return new QQmlJSScope::ConstPtr(self->regexpType());
}

//  QQmlJSScope::ConstPtr QQmlJSTypeResolver::variantListType() const
extern "C" Q_DECL_EXPORT
QQmlJSScope::ConstPtr *ritual_ZNK18QQmlJSTypeResolver15variantListTypeEv(
    const QQmlJSTypeResolver *self) {
  return new QQmlJSScope::ConstPtr(self->variantListType());
}

//  QQmlJSScope::ConstPtr QQmlJSTypeResolver::variantMapType() const
extern "C" Q_DECL_EXPORT
QQmlJSScope::ConstPtr *ritual_ZNK18QQmlJSTypeResolver14variantMapTypeEv(
    const QQmlJSTypeResolver *self) {
  return new QQmlJSScope::ConstPtr(self->variantMapType());
}

//  QQmlJSScope::ConstPtr QQmlJSTypeResolver::varType() const
extern "C" Q_DECL_EXPORT
QQmlJSScope::ConstPtr *ritual_ZNK18QQmlJSTypeResolver7varTypeEv(
    const QQmlJSTypeResolver *self) {
  return new QQmlJSScope::ConstPtr(self->varType());
}

//  QQmlJSScope::ConstPtr QQmlJSTypeResolver::qmlPropertyMapType() const
extern "C" Q_DECL_EXPORT
QQmlJSScope::ConstPtr *ritual_ZNK18QQmlJSTypeResolver18qmlPropertyMapTypeEv(
    const QQmlJSTypeResolver *self) {
  return new QQmlJSScope::ConstPtr(self->qmlPropertyMapType());
}

//  QQmlJSScope::ConstPtr QQmlJSTypeResolver::jsValueType() const
extern "C" Q_DECL_EXPORT
QQmlJSScope::ConstPtr *ritual_ZNK18QQmlJSTypeResolver11jsValueTypeEv(
    const QQmlJSTypeResolver *self) {
  return new QQmlJSScope::ConstPtr(self->jsValueType());
}

//  QQmlJSScope::ConstPtr QQmlJSTypeResolver::jsPrimitiveType() const
extern "C" Q_DECL_EXPORT
QQmlJSScope::ConstPtr *ritual_ZNK18QQmlJSTypeResolver15jsPrimitiveTypeEv(
    const QQmlJSTypeResolver *self) {
  return new QQmlJSScope::ConstPtr(self->jsPrimitiveType());
}

//  QQmlJSScope::ConstPtr QQmlJSTypeResolver::listPropertyType() const
extern "C" Q_DECL_EXPORT
QQmlJSScope::ConstPtr *ritual_ZNK18QQmlJSTypeResolver16listPropertyTypeEv(
    const QQmlJSTypeResolver *self) {
  return new QQmlJSScope::ConstPtr(self->listPropertyType());
}

//  QQmlJSScope::ConstPtr QQmlJSTypeResolver::metaObjectType() const
extern "C" Q_DECL_EXPORT
QQmlJSScope::ConstPtr *ritual_ZNK18QQmlJSTypeResolver14metaObjectTypeEv(
    const QQmlJSTypeResolver *self) {
  return new QQmlJSScope::ConstPtr(self->metaObjectType());
}

//  QQmlJSScope::ConstPtr QQmlJSTypeResolver::functionType() const
extern "C" Q_DECL_EXPORT
QQmlJSScope::ConstPtr *ritual_ZNK18QQmlJSTypeResolver12functionTypeEv(
    const QQmlJSTypeResolver *self) {
  return new QQmlJSScope::ConstPtr(self->functionType());
}

//  QQmlJSScope::ConstPtr QQmlJSTypeResolver::jsGlobalObject() const
extern "C" Q_DECL_EXPORT
QQmlJSScope::ConstPtr *ritual_ZNK18QQmlJSTypeResolver14jsGlobalObjectEv(
    const QQmlJSTypeResolver *self) {
  return new QQmlJSScope::ConstPtr(self->jsGlobalObject());
}

//  QQmlJSScope::ConstPtr QQmlJSTypeResolver::qObjectType() const
extern "C" Q_DECL_EXPORT
QQmlJSScope::ConstPtr *ritual_ZNK18QQmlJSTypeResolver11qObjectTypeEv(
    const QQmlJSTypeResolver *self) {
  return new QQmlJSScope::ConstPtr(self->qObjectType());
}

//  QQmlJSScope::ConstPtr QQmlJSTypeResolver::qObjectListType() const
extern "C" Q_DECL_EXPORT
QQmlJSScope::ConstPtr *ritual_ZNK18QQmlJSTypeResolver15qObjectListTypeEv(
    const QQmlJSTypeResolver *self) {
  return new QQmlJSScope::ConstPtr(self->qObjectListType());
}

//  QQmlJSScope::ConstPtr QQmlJSTypeResolver::arrayPrototype() const
extern "C" Q_DECL_EXPORT
QQmlJSScope::ConstPtr *ritual_ZNK18QQmlJSTypeResolver14arrayPrototypeEv(
    const QQmlJSTypeResolver *self) {
  return new QQmlJSScope::ConstPtr(self->arrayPrototype());
}

//  QQmlJSScope::ConstPtr QQmlJSTypeResolver::forInIteratorPtr() const
extern "C" Q_DECL_EXPORT
QQmlJSScope::ConstPtr *ritual_ZNK18QQmlJSTypeResolver16forInIteratorPtrEv(
    const QQmlJSTypeResolver *self) {
  return new QQmlJSScope::ConstPtr(self->forInIteratorPtr());
}

//  QQmlJSScope::ConstPtr QQmlJSTypeResolver::forOfIteratorPtr() const
extern "C" Q_DECL_EXPORT
QQmlJSScope::ConstPtr *ritual_ZNK18QQmlJSTypeResolver16forOfIteratorPtrEv(
    const QQmlJSTypeResolver *self) {
  return new QQmlJSScope::ConstPtr(self->forOfIteratorPtr());
}

//  QQmlJSScope::ConstPtr QQmlJSTypeResolver::qQmlScriptStringType() const
extern "C" Q_DECL_EXPORT
QQmlJSScope::ConstPtr *ritual_ZNK18QQmlJSTypeResolver20qQmlScriptStringTypeEv(
    const QQmlJSTypeResolver *self) {
  return new QQmlJSScope::ConstPtr(self->qQmlScriptStringType());
}

//  QQmlJSRegisterContent QQmlJSTypeResolver::jsGlobalObjectContent() const
extern "C" Q_DECL_EXPORT
QQmlJSRegisterContent *ritual_ZNK18QQmlJSTypeResolver21jsGlobalObjectContentEv(
    const QQmlJSTypeResolver *self) {
  return new QQmlJSRegisterContent(self->jsGlobalObjectContent());
}

//  QQmlJSScope::ConstPtr QQmlJSTypeResolver::mathObject() const
extern "C" Q_DECL_EXPORT
QQmlJSScope::ConstPtr *ritual_ZNK18QQmlJSTypeResolver10mathObjectEv(
    const QQmlJSTypeResolver *self) {
  return new QQmlJSScope::ConstPtr(self->mathObject());
}

//  QQmlJSScope::ConstPtr QQmlJSTypeResolver::consoleObject() const
extern "C" Q_DECL_EXPORT
QQmlJSScope::ConstPtr *ritual_ZNK18QQmlJSTypeResolver13consoleObjectEv(
    const QQmlJSTypeResolver *self) {
  return new QQmlJSScope::ConstPtr(self->consoleObject());
}

//  QQmlJSScope::ConstPtr QQmlJSTypeResolver::typeForConst(QV4::ReturnedValue
//      rv) const
extern "C" Q_DECL_EXPORT
QQmlJSScope::ConstPtr *ritual_ZNK18QQmlJSTypeResolver12typeForConstEy(
    const QQmlJSTypeResolver *self,
    QV4::ReturnedValue rv) {
  return new QQmlJSScope::ConstPtr(self->typeForConst(rv));
}

//  bool QQmlJSTypeResolver::isPrefix(const QString &name) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QQmlJSTypeResolver8isPrefixERK7QString(
    const QQmlJSTypeResolver *self,
    const QString *name) {
  return self->isPrefix(*name);
}

//  const QHash<QString, QQmlJS::ContextualType>
//      &QQmlJSTypeResolver::importedTypes() const
extern "C" Q_DECL_EXPORT
const QHash<QString, QQmlJS::ContextualType> *ritual_ZNK18QQmlJSTypeResolver13importedTypesEv(
    const QQmlJSTypeResolver *self) {
  return &(self->importedTypes());
}

//  const QMultiHash<QQmlJSScope::ConstPtr, QString>
//      &QQmlJSTypeResolver::importedNames() const
extern "C" Q_DECL_EXPORT
const QMultiHash<QQmlJSScope::ConstPtr, QString> *ritual_ZNK18QQmlJSTypeResolver13importedNamesEv(
    const QQmlJSTypeResolver *self) {
  return &(self->importedNames());
}

//  QQmlJSScope::ConstPtr QQmlJSTypeResolver::typeForName(const QString
//      &name) const
extern "C" Q_DECL_EXPORT
QQmlJSScope::ConstPtr *ritual_ZNK18QQmlJSTypeResolver11typeForNameERK7QString(
    const QQmlJSTypeResolver *self,
    const QString *name) {
  return new QQmlJSScope::ConstPtr(self->typeForName(*name));
}

//  QString QQmlJSTypeResolver::nameForType(const QQmlJSScope::ConstPtr
//      &type) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QQmlJSTypeResolver11nameForTypeERK22QDeferredSharedPointerIK11QQmlJSScopeE(
    const QQmlJSTypeResolver *self,
    const QQmlJSScope::ConstPtr *type) {
  return new QString(self->nameForType(*type));
}

//  QStringList QQmlJSTypeResolver::seenModuleQualifiers() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK18QQmlJSTypeResolver20seenModuleQualifiersEv(
    const QQmlJSTypeResolver *self) {
  return new QList<QString>(self->seenModuleQualifiers());
}

//  QQmlJSScope::ConstPtr QQmlJSTypeResolver::scopeForLocation(const
//      QV4::CompiledData::Location &location) const
extern "C" Q_DECL_EXPORT
QQmlJSScope::ConstPtr *ritual_ZNK18QQmlJSTypeResolver16scopeForLocationERKN3QV412CompiledData8LocationE(
    const QQmlJSTypeResolver *self,
    const QV4::CompiledData::Location *location) {
  return new QQmlJSScope::ConstPtr(self->scopeForLocation(*location));
}

//  QQmlJSScope::ConstPtr QQmlJSTypeResolver::typeFromAST(QQmlJS::AST::Type
//      *type) const
extern "C" Q_DECL_EXPORT
QQmlJSScope::ConstPtr *ritual_ZNK18QQmlJSTypeResolver11typeFromASTEPN6QQmlJS3AST4TypeE(
    const QQmlJSTypeResolver *self,
    QQmlJS::AST::Type *type) {
  return new QQmlJSScope::ConstPtr(self->typeFromAST(type));
}

//  QQmlJSScope::ConstPtr QQmlJSTypeResolver::typeForId(const
//      QQmlJSScope::ConstPtr &scope, const QString &name,
//      QQmlJSScopesByIdOptions options) const
extern "C" Q_DECL_EXPORT
QQmlJSScope::ConstPtr *ritual_ZNK18QQmlJSTypeResolver9typeForIdERK22QDeferredSharedPointerIK11QQmlJSScopeERK7QString6QFlagsI22QQmlJSScopesByIdOptionE(
    const QQmlJSTypeResolver *self,
    const QQmlJSScope::ConstPtr *scope,
    const QString *name,
    int options) {
  return new QQmlJSScope::ConstPtr(
      self->typeForId(
          *scope,
          *name,
          QFlags<QQmlJSScopesByIdOption>::fromInt(options)));
}

//  const QQmlJSScopesById &QQmlJSTypeResolver::objectsById() const
extern "C" Q_DECL_EXPORT
QQmlJSScopesById *ritual_ZNK18QQmlJSTypeResolver11objectsByIdEv(
    const QQmlJSTypeResolver *self) {
  return new QQmlJSScopesById(self->objectsById());
}

//  bool QQmlJSTypeResolver::canCallJSFunctions() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QQmlJSTypeResolver18canCallJSFunctionsEv(
    const QQmlJSTypeResolver *self) {
  return self->canCallJSFunctions();
}

//  bool QQmlJSTypeResolver::canAddressValueTypes() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QQmlJSTypeResolver20canAddressValueTypesEv(
    const QQmlJSTypeResolver *self) {
  return self->canAddressValueTypes();
}

//  QQmlJSScope::ConstPtr QQmlJSTypeResolver::scopedType(const
//      QQmlJSScope::ConstPtr &scope, const QString &name,
//      QQmlJSScopesByIdOptions options) const
extern "C" Q_DECL_EXPORT
QQmlJSScope::ConstPtr *ritual_ZNK18QQmlJSTypeResolver10scopedTypeERK22QDeferredSharedPointerIK11QQmlJSScopeERK7QString6QFlagsI22QQmlJSScopesByIdOptionE(
    const QQmlJSTypeResolver *self,
    const QQmlJSScope::ConstPtr *scope,
    const QString *name,
    int options) {
  return new QQmlJSScope::ConstPtr(
      self->scopedType(
          *scope,
          *name,
          QFlags<QQmlJSScopesByIdOption>::fromInt(options)));
}

//  const QHash<QQmlJS::SourceLocation, QQmlJSMetaSignalHandler>
//      &QQmlJSTypeResolver::signalHandlers() const
extern "C" Q_DECL_EXPORT
const QHash<QQmlJS::SourceLocation, QQmlJSMetaSignalHandler> *ritual_ZNK18QQmlJSTypeResolver14signalHandlersEv(
    const QQmlJSTypeResolver *self) {
  return &(self->signalHandlers());
}

//  bool QQmlJSTypeResolver::isPrimitive(QQmlJSRegisterContent type) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QQmlJSTypeResolver11isPrimitiveE21QQmlJSRegisterContent(
    const QQmlJSTypeResolver *self,
    const QQmlJSRegisterContent *type) {
  return self->isPrimitive(*type);
}

//  bool QQmlJSTypeResolver::isPrimitive(const QQmlJSScope::ConstPtr &type)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QQmlJSTypeResolver11isPrimitiveERK22QDeferredSharedPointerIK11QQmlJSScopeE(
    const QQmlJSTypeResolver *self,
    const QQmlJSScope::ConstPtr *type) {
  return self->isPrimitive(*type);
}

//  bool QQmlJSTypeResolver::isNumeric(QQmlJSRegisterContent type) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QQmlJSTypeResolver9isNumericE21QQmlJSRegisterContent(
    const QQmlJSTypeResolver *self,
    const QQmlJSRegisterContent *type) {
  return self->isNumeric(*type);
}

//  bool QQmlJSTypeResolver::isNumeric(const QQmlJSScope::ConstPtr &type)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QQmlJSTypeResolver9isNumericERK22QDeferredSharedPointerIK11QQmlJSScopeE(
    const QQmlJSTypeResolver *self,
    const QQmlJSScope::ConstPtr *type) {
  return self->isNumeric(*type);
}

//  bool QQmlJSTypeResolver::isIntegral(QQmlJSRegisterContent type) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QQmlJSTypeResolver10isIntegralE21QQmlJSRegisterContent(
    const QQmlJSTypeResolver *self,
    const QQmlJSRegisterContent *type) {
  return self->isIntegral(*type);
}

//  bool QQmlJSTypeResolver::isIntegral(const QQmlJSScope::ConstPtr &type)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QQmlJSTypeResolver10isIntegralERK22QDeferredSharedPointerIK11QQmlJSScopeE(
    const QQmlJSTypeResolver *self,
    const QQmlJSScope::ConstPtr *type) {
  return self->isIntegral(*type);
}

//  bool QQmlJSTypeResolver::isSignedInteger(const QQmlJSScope::ConstPtr
//      &type) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QQmlJSTypeResolver15isSignedIntegerERK22QDeferredSharedPointerIK11QQmlJSScopeE(
    const QQmlJSTypeResolver *self,
    const QQmlJSScope::ConstPtr *type) {
  return self->isSignedInteger(*type);
}

//  bool QQmlJSTypeResolver::isUnsignedInteger(const QQmlJSScope::ConstPtr
//      &type) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QQmlJSTypeResolver17isUnsignedIntegerERK22QDeferredSharedPointerIK11QQmlJSScopeE(
    const QQmlJSTypeResolver *self,
    const QQmlJSScope::ConstPtr *type) {
  return self->isUnsignedInteger(*type);
}

//  bool QQmlJSTypeResolver::isNativeArrayIndex(const QQmlJSScope::ConstPtr
//      &type) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QQmlJSTypeResolver18isNativeArrayIndexERK22QDeferredSharedPointerIK11QQmlJSScopeE(
    const QQmlJSTypeResolver *self,
    const QQmlJSScope::ConstPtr *type) {
  return self->isNativeArrayIndex(*type);
}

//  bool QQmlJSTypeResolver::canHold(const QQmlJSScope::ConstPtr &container,
//      const QQmlJSScope::ConstPtr &contained) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QQmlJSTypeResolver7canHoldERK22QDeferredSharedPointerIK11QQmlJSScopeES5_(
    const QQmlJSTypeResolver *self,
    const QQmlJSScope::ConstPtr *container,
    const QQmlJSScope::ConstPtr *contained) {
  return self->canHold(*container, *contained);
}

//  bool QQmlJSTypeResolver::canHoldUndefined(QQmlJSRegisterContent content)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QQmlJSTypeResolver16canHoldUndefinedE21QQmlJSRegisterContent(
    const QQmlJSTypeResolver *self,
    const QQmlJSRegisterContent *content) {
  return self->canHoldUndefined(*content);
}

//  bool QQmlJSTypeResolver::isOptionalType(QQmlJSRegisterContent content)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QQmlJSTypeResolver14isOptionalTypeE21QQmlJSRegisterContent(
    const QQmlJSTypeResolver *self,
    const QQmlJSRegisterContent *content) {
  return self->isOptionalType(*content);
}

//  bool QQmlJSTypeResolver::canPopulate(const QQmlJSScope::ConstPtr &type,
//      const QQmlJSScope::ConstPtr &argument, bool *isExtension) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QQmlJSTypeResolver11canPopulateERK22QDeferredSharedPointerIK11QQmlJSScopeES5_Pb(
    const QQmlJSTypeResolver *self,
    const QQmlJSScope::ConstPtr *type,
    const QQmlJSScope::ConstPtr *argument,
    bool *isExtension) {
  return self->canPopulate(*type, *argument, isExtension);
}

//  bool QQmlJSTypeResolver::canConvertFromTo(const QQmlJSScope::ConstPtr
//      &from, const QQmlJSScope::ConstPtr &to) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QQmlJSTypeResolver16canConvertFromToERK22QDeferredSharedPointerIK11QQmlJSScopeES5_(
    const QQmlJSTypeResolver *self,
    const QQmlJSScope::ConstPtr *from,
    const QQmlJSScope::ConstPtr *to) {
  return self->canConvertFromTo(*from, *to);
}

//  bool QQmlJSTypeResolver::canConvertFromTo(QQmlJSRegisterContent from,
//      QQmlJSRegisterContent to) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QQmlJSTypeResolver16canConvertFromToE21QQmlJSRegisterContentS0_(
    const QQmlJSTypeResolver *self,
    const QQmlJSRegisterContent *from,
    const QQmlJSRegisterContent *to) {
  return self->canConvertFromTo(*from, *to);
}

//  bool QQmlJSTypeResolver::areEquivalentLists(const QQmlJSScope::ConstPtr
//      &a, const QQmlJSScope::ConstPtr &b) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QQmlJSTypeResolver18areEquivalentListsERK22QDeferredSharedPointerIK11QQmlJSScopeES5_(
    const QQmlJSTypeResolver *self,
    const QQmlJSScope::ConstPtr *a,
    const QQmlJSScope::ConstPtr *b) {
  return self->areEquivalentLists(*a, *b);
}

//  bool QQmlJSTypeResolver::isTriviallyCopyable(const QQmlJSScope::ConstPtr
//      &type) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QQmlJSTypeResolver19isTriviallyCopyableERK22QDeferredSharedPointerIK11QQmlJSScopeE(
    const QQmlJSTypeResolver *self,
    const QQmlJSScope::ConstPtr *type) {
  return self->isTriviallyCopyable(*type);
}

//  bool QQmlJSTypeResolver::inherits(const QQmlJSScope::ConstPtr &derived,
//      const QQmlJSScope::ConstPtr &base) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QQmlJSTypeResolver8inheritsERK22QDeferredSharedPointerIK11QQmlJSScopeES5_(
    const QQmlJSTypeResolver *self,
    const QQmlJSScope::ConstPtr *derived,
    const QQmlJSScope::ConstPtr *base) {
  return self->inherits(*derived, *base);
}

//  QQmlJSScope::ConstPtr QQmlJSTypeResolver::genericType(const
//      QQmlJSScope::ConstPtr &type, ComponentIsGeneric allowComponent) const
extern "C" Q_DECL_EXPORT
QQmlJSScope::ConstPtr *ritual_ZNK18QQmlJSTypeResolver11genericTypeERK22QDeferredSharedPointerIK11QQmlJSScopeENS_18ComponentIsGenericE(
    const QQmlJSTypeResolver *self,
    const QQmlJSScope::ConstPtr *type,
    QQmlJSTypeResolver::ComponentIsGeneric allowComponent) {
  return new QQmlJSScope::ConstPtr(self->genericType(*type, allowComponent));
}

//  QQmlJSScope::ConstPtr QQmlJSTypeResolver::storedType(const
//      QQmlJSScope::ConstPtr &type) const
extern "C" Q_DECL_EXPORT
QQmlJSScope::ConstPtr *ritual_ZNK18QQmlJSTypeResolver10storedTypeERK22QDeferredSharedPointerIK11QQmlJSScopeE(
    const QQmlJSTypeResolver *self,
    const QQmlJSScope::ConstPtr *type) {
  return new QQmlJSScope::ConstPtr(self->storedType(*type));
}

//  QQmlJSRegisterContent QQmlJSTypeResolver::original(QQmlJSRegisterContent
//      type) const
extern "C" Q_DECL_EXPORT
QQmlJSRegisterContent *ritual_ZNK18QQmlJSTypeResolver8originalE21QQmlJSRegisterContent(
    const QQmlJSTypeResolver *self,
    const QQmlJSRegisterContent *type) {
  return new QQmlJSRegisterContent(self->original(*type));
}

//  QQmlJSScope::ConstPtr
//      QQmlJSTypeResolver::originalContainedType(QQmlJSRegisterContent
//      container) const
extern "C" Q_DECL_EXPORT
QQmlJSScope::ConstPtr *ritual_ZNK18QQmlJSTypeResolver21originalContainedTypeE21QQmlJSRegisterContent(
    const QQmlJSTypeResolver *self,
    const QQmlJSRegisterContent *container) {
  return new QQmlJSScope::ConstPtr(self->originalContainedType(*container));
}

//  QQmlJSRegisterContent QQmlJSTypeResolver::shadowed(QQmlJSRegisterContent
//      type) const
extern "C" Q_DECL_EXPORT
QQmlJSRegisterContent *ritual_ZNK18QQmlJSTypeResolver8shadowedE21QQmlJSRegisterContent(
    const QQmlJSTypeResolver *self,
    const QQmlJSRegisterContent *type) {
  return new QQmlJSRegisterContent(self->shadowed(*type));
}

//  QQmlJSScope::ConstPtr QQmlJSTypeResolver::merge(const
//      QQmlJSScope::ConstPtr &a, const QQmlJSScope::ConstPtr &b) const
extern "C" Q_DECL_EXPORT
QQmlJSScope::ConstPtr *ritual_ZNK18QQmlJSTypeResolver5mergeERK22QDeferredSharedPointerIK11QQmlJSScopeES5_(
    const QQmlJSTypeResolver *self,
    const QQmlJSScope::ConstPtr *a,
    const QQmlJSScope::ConstPtr *b) {
  return new QQmlJSScope::ConstPtr(self->merge(*a, *b));
}

//  QQmlJSRegisterContent
//      QQmlJSTypeResolver::extractNonVoidFromOptionalType(QQmlJSRegisterCont
//      ent content) const
extern "C" Q_DECL_EXPORT
QQmlJSRegisterContent *ritual_ZNK18QQmlJSTypeResolver30extractNonVoidFromOptionalTypeE21QQmlJSRegisterContent(
    const QQmlJSTypeResolver *self,
    const QQmlJSRegisterContent *content) {
  return new QQmlJSRegisterContent(
      self->extractNonVoidFromOptionalType(
          *content));
}

//  QQmlJSMetaMethod QQmlJSTypeResolver::selectConstructor(const
//      QQmlJSScope::ConstPtr &type, const QQmlJSScope::ConstPtr &argument,
//      bool *isExtension) const
extern "C" Q_DECL_EXPORT
QQmlJSMetaMethod *ritual_ZNK18QQmlJSTypeResolver17selectConstructorERK22QDeferredSharedPointerIK11QQmlJSScopeES5_Pb(
    const QQmlJSTypeResolver *self,
    const QQmlJSScope::ConstPtr *type,
    const QQmlJSScope::ConstPtr *argument,
    bool *isExtension) {
  return new QQmlJSMetaMethod(
      self->selectConstructor(
          *type,
          *argument,
          isExtension));
}

//  QQmlJSRegisterContent
//      QQmlJSTypeResolver::typeForBinaryOperation(QSOperator::Op oper,
//      QQmlJSRegisterContent left, QQmlJSRegisterContent right) const
extern "C" Q_DECL_EXPORT
QQmlJSRegisterContent *ritual_ZNK18QQmlJSTypeResolver22typeForBinaryOperationEN10QSOperator2OpE21QQmlJSRegisterContentS2_(
    const QQmlJSTypeResolver *self,
    QSOperator::Op oper,
    const QQmlJSRegisterContent *left,
    const QQmlJSRegisterContent *right) {
  return new QQmlJSRegisterContent(
      self->typeForBinaryOperation(
          oper,
          *left,
          *right));
}

//  QQmlJSRegisterContent
//      QQmlJSTypeResolver::typeForArithmeticUnaryOperation(UnaryOperator op,
//      QQmlJSRegisterContent operand) const
extern "C" Q_DECL_EXPORT
QQmlJSRegisterContent *ritual_ZNK18QQmlJSTypeResolver31typeForArithmeticUnaryOperationENS_13UnaryOperatorE21QQmlJSRegisterContent(
    const QQmlJSTypeResolver *self,
    QQmlJSTypeResolver::UnaryOperator op,
    const QQmlJSRegisterContent *operand) {
  return new QQmlJSRegisterContent(
      self->typeForArithmeticUnaryOperation(
          op,
          *operand));
}

//  QQmlJSRegisterContent QQmlJSTypeResolver::merge(QQmlJSRegisterContent a,
//      QQmlJSRegisterContent b) const
extern "C" Q_DECL_EXPORT
QQmlJSRegisterContent *ritual_ZNK18QQmlJSTypeResolver5mergeE21QQmlJSRegisterContentS0_(
    const QQmlJSTypeResolver *self,
    const QQmlJSRegisterContent *a,
    const QQmlJSRegisterContent *b) {
  return new QQmlJSRegisterContent(self->merge(*a, *b));
}

//  void QQmlJSTypeResolver::clearMergeCache() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK18QQmlJSTypeResolver15clearMergeCacheEv(
    const QQmlJSTypeResolver *self) {
  self->clearMergeCache();
}

//  QQmlJSRegisterContent QQmlJSTypeResolver::literalType(const
//      QQmlJSScope::ConstPtr &type) const
extern "C" Q_DECL_EXPORT
QQmlJSRegisterContent *ritual_ZNK18QQmlJSTypeResolver11literalTypeERK22QDeferredSharedPointerIK11QQmlJSScopeE(
    const QQmlJSTypeResolver *self,
    const QQmlJSScope::ConstPtr *type) {
  return new QQmlJSRegisterContent(self->literalType(*type));
}

//  QQmlJSRegisterContent QQmlJSTypeResolver::operationType(const
//      QQmlJSScope::ConstPtr &type) const
extern "C" Q_DECL_EXPORT
QQmlJSRegisterContent *ritual_ZNK18QQmlJSTypeResolver13operationTypeERK22QDeferredSharedPointerIK11QQmlJSScopeE(
    const QQmlJSTypeResolver *self,
    const QQmlJSScope::ConstPtr *type) {
  return new QQmlJSRegisterContent(self->operationType(*type));
}

//  QQmlJSRegisterContent QQmlJSTypeResolver::namedType(const
//      QQmlJSScope::ConstPtr &type) const
extern "C" Q_DECL_EXPORT
QQmlJSRegisterContent *ritual_ZNK18QQmlJSTypeResolver9namedTypeERK22QDeferredSharedPointerIK11QQmlJSScopeE(
    const QQmlJSTypeResolver *self,
    const QQmlJSScope::ConstPtr *type) {
  return new QQmlJSRegisterContent(self->namedType(*type));
}

//  QQmlJSRegisterContent QQmlJSTypeResolver::syntheticType(const
//      QQmlJSScope::ConstPtr &type) const
extern "C" Q_DECL_EXPORT
QQmlJSRegisterContent *ritual_ZNK18QQmlJSTypeResolver13syntheticTypeERK22QDeferredSharedPointerIK11QQmlJSScopeE(
    const QQmlJSTypeResolver *self,
    const QQmlJSScope::ConstPtr *type) {
  return new QQmlJSRegisterContent(self->syntheticType(*type));
}

//  QQmlJSRegisterContent
//      QQmlJSTypeResolver::scopedType(QQmlJSRegisterContent scope, const
//      QString &name, int lookupIndex, QQmlJSScopesByIdOptions options)
//      const
extern "C" Q_DECL_EXPORT
QQmlJSRegisterContent *ritual_ZNK18QQmlJSTypeResolver10scopedTypeE21QQmlJSRegisterContentRK7QStringi6QFlagsI22QQmlJSScopesByIdOptionE(
    const QQmlJSTypeResolver *self,
    const QQmlJSRegisterContent *scope,
    const QString *name,
    int lookupIndex,
    int options) {
  return new QQmlJSRegisterContent(
      self->scopedType(
          *scope,
          *name,
          lookupIndex,
          QFlags<QQmlJSScopesByIdOption>::fromInt(options)));
}

//  QQmlJSRegisterContent
//      QQmlJSTypeResolver::memberType(QQmlJSRegisterContent type, const
//      QString &name, int lookupIndex) const
extern "C" Q_DECL_EXPORT
QQmlJSRegisterContent *ritual_ZNK18QQmlJSTypeResolver10memberTypeE21QQmlJSRegisterContentRK7QStringi(
    const QQmlJSTypeResolver *self,
    const QQmlJSRegisterContent *type,
    const QString *name,
    int lookupIndex) {
  return new QQmlJSRegisterContent(
      self->memberType(
          *type,
          *name,
          lookupIndex));
}

//  QQmlJSRegisterContent
//      QQmlJSTypeResolver::elementType(QQmlJSRegisterContent list) const
extern "C" Q_DECL_EXPORT
QQmlJSRegisterContent *ritual_ZNK18QQmlJSTypeResolver11elementTypeE21QQmlJSRegisterContent(
    const QQmlJSTypeResolver *self,
    const QQmlJSRegisterContent *list) {
  return new QQmlJSRegisterContent(self->elementType(*list));
}

//  QQmlJSRegisterContent QQmlJSTypeResolver::returnType(const
//      QQmlJSMetaMethod &method, const QQmlJSScope::ConstPtr &returnType,
//      QQmlJSRegisterContent scope) const
extern "C" Q_DECL_EXPORT
QQmlJSRegisterContent *ritual_ZNK18QQmlJSTypeResolver10returnTypeERK16QQmlJSMetaMethodRK22QDeferredSharedPointerIK11QQmlJSScopeE21QQmlJSRegisterContent(
    const QQmlJSTypeResolver *self,
    const QQmlJSMetaMethod *method,
    const QQmlJSScope::ConstPtr *returnType,
    const QQmlJSRegisterContent *scope) {
  return new QQmlJSRegisterContent(
      self->returnType(
          *method,
          *returnType,
          *scope));
}

//  QQmlJSRegisterContent QQmlJSTypeResolver::extensionType(const
//      QQmlJSScope::ConstPtr &extension, QQmlJSRegisterContent base) const
extern "C" Q_DECL_EXPORT
QQmlJSRegisterContent *ritual_ZNK18QQmlJSTypeResolver13extensionTypeERK22QDeferredSharedPointerIK11QQmlJSScopeE21QQmlJSRegisterContent(
    const QQmlJSTypeResolver *self,
    const QQmlJSScope::ConstPtr *extension,
    const QQmlJSRegisterContent *base) {
  return new QQmlJSRegisterContent(self->extensionType(*extension, *base));
}

//  QQmlJSRegisterContent QQmlJSTypeResolver::baseType(const
//      QQmlJSScope::ConstPtr &base, QQmlJSRegisterContent derived) const
extern "C" Q_DECL_EXPORT
QQmlJSRegisterContent *ritual_ZNK18QQmlJSTypeResolver8baseTypeERK22QDeferredSharedPointerIK11QQmlJSScopeE21QQmlJSRegisterContent(
    const QQmlJSTypeResolver *self,
    const QQmlJSScope::ConstPtr *base,
    const QQmlJSRegisterContent *derived) {
  return new QQmlJSRegisterContent(self->baseType(*base, *derived));
}

//  QQmlJSRegisterContent QQmlJSTypeResolver::parentScope(const
//      QQmlJSScope::ConstPtr &parent, QQmlJSRegisterContent child) const
extern "C" Q_DECL_EXPORT
QQmlJSRegisterContent *ritual_ZNK18QQmlJSTypeResolver11parentScopeERK22QDeferredSharedPointerIK11QQmlJSScopeE21QQmlJSRegisterContent(
    const QQmlJSTypeResolver *self,
    const QQmlJSScope::ConstPtr *parent,
    const QQmlJSRegisterContent *child) {
  return new QQmlJSRegisterContent(self->parentScope(*parent, *child));
}

//  QQmlJSRegisterContent
//      QQmlJSTypeResolver::iteratorPointer(QQmlJSRegisterContent listType,
//      QQmlJS::AST::ForEachType type, int lookupIndex) const
extern "C" Q_DECL_EXPORT
QQmlJSRegisterContent *ritual_ZNK18QQmlJSTypeResolver15iteratorPointerE21QQmlJSRegisterContentN6QQmlJS3AST11ForEachTypeEi(
    const QQmlJSTypeResolver *self,
    const QQmlJSRegisterContent *listType,
    QQmlJS::AST::ForEachType type,
    int lookupIndex) {
  return new QQmlJSRegisterContent(
      self->iteratorPointer(
          *listType,
          type,
          lookupIndex));
}

//  QQmlJSRegisterContent QQmlJSTypeResolver::convert(QQmlJSRegisterContent
//      from, QQmlJSRegisterContent to) const
extern "C" Q_DECL_EXPORT
QQmlJSRegisterContent *ritual_ZNK18QQmlJSTypeResolver7convertE21QQmlJSRegisterContentS0_(
    const QQmlJSTypeResolver *self,
    const QQmlJSRegisterContent *from,
    const QQmlJSRegisterContent *to) {
  return new QQmlJSRegisterContent(self->convert(*from, *to));
}

//  QQmlJSRegisterContent QQmlJSTypeResolver::convert(QQmlJSRegisterContent
//      from, const QQmlJSScope::ConstPtr &to) const
extern "C" Q_DECL_EXPORT
QQmlJSRegisterContent *ritual_ZNK18QQmlJSTypeResolver7convertE21QQmlJSRegisterContentRK22QDeferredSharedPointerIK11QQmlJSScopeE(
    const QQmlJSTypeResolver *self,
    const QQmlJSRegisterContent *from,
    const QQmlJSScope::ConstPtr *to) {
  return new QQmlJSRegisterContent(self->convert(*from, *to));
}

//  bool QQmlJSTypeResolver::adjustTrackedType(QQmlJSRegisterContent tracked,
//      const QQmlJSScope::ConstPtr &conversion) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QQmlJSTypeResolver17adjustTrackedTypeE21QQmlJSRegisterContentRK22QDeferredSharedPointerIK11QQmlJSScopeE(
    const QQmlJSTypeResolver *self,
    const QQmlJSRegisterContent *tracked,
    const QQmlJSScope::ConstPtr *conversion) {
  return self->adjustTrackedType(*tracked, *conversion);
}

//  bool QQmlJSTypeResolver::adjustTrackedType(QQmlJSRegisterContent tracked,
//      QQmlJSRegisterContent conversion) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QQmlJSTypeResolver17adjustTrackedTypeE21QQmlJSRegisterContentS0_(
    const QQmlJSTypeResolver *self,
    const QQmlJSRegisterContent *tracked,
    const QQmlJSRegisterContent *conversion) {
  return self->adjustTrackedType(*tracked, *conversion);
}

//  bool QQmlJSTypeResolver::adjustTrackedType(QQmlJSRegisterContent tracked,
//      const QList<QQmlJSRegisterContent> &conversions) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QQmlJSTypeResolver17adjustTrackedTypeE21QQmlJSRegisterContentRK5QListIS0_E(
    const QQmlJSTypeResolver *self,
    const QQmlJSRegisterContent *tracked,
    const QList<QQmlJSRegisterContent> *conversions) {
  return self->adjustTrackedType(*tracked, *conversions);
}

//  void QQmlJSTypeResolver::adjustOriginalType(QQmlJSRegisterContent
//      tracked, const QQmlJSScope::ConstPtr &conversion) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK18QQmlJSTypeResolver18adjustOriginalTypeE21QQmlJSRegisterContentRK22QDeferredSharedPointerIK11QQmlJSScopeE(
    const QQmlJSTypeResolver *self,
    const QQmlJSRegisterContent *tracked,
    const QQmlJSScope::ConstPtr *conversion) {
  self->adjustOriginalType(*tracked, *conversion);
}

//  void QQmlJSTypeResolver::generalizeType(QQmlJSRegisterContent type) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK18QQmlJSTypeResolver14generalizeTypeE21QQmlJSRegisterContent(
    const QQmlJSTypeResolver *self,
    const QQmlJSRegisterContent *type) {
  self->generalizeType(*type);
}

//  QQmlJSRegisterContent
//      QQmlJSTypeResolver::memberType(QQmlJSRegisterContent type, const
//      QString &name, int baseLookupIndex, int resultLookupIndex) const
extern "C" Q_DECL_EXPORT
QQmlJSRegisterContent *ritual_ZNK18QQmlJSTypeResolver10memberTypeE21QQmlJSRegisterContentRK7QStringii(
    const QQmlJSTypeResolver *self,
    const QQmlJSRegisterContent *type,
    const QString *name,
    int baseLookupIndex,
    int resultLookupIndex) {
  return new QQmlJSRegisterContent(
      self->memberType(
          *type,
          *name,
          baseLookupIndex,
          resultLookupIndex));
}

//  QQmlJSRegisterContent
//      QQmlJSTypeResolver::memberEnumType(QQmlJSRegisterContent type, const
//      QString &name) const
extern "C" Q_DECL_EXPORT
QQmlJSRegisterContent *ritual_ZNK18QQmlJSTypeResolver14memberEnumTypeE21QQmlJSRegisterContentRK7QString(
    const QQmlJSTypeResolver *self,
    const QQmlJSRegisterContent *type,
    const QString *name) {
  return new QQmlJSRegisterContent(self->memberEnumType(*type, *name));
}

//  bool QQmlJSTypeResolver::checkEnums(QQmlJSRegisterContent scope, const
//      QString &name, QQmlJSRegisterContent *result) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QQmlJSTypeResolver10checkEnumsE21QQmlJSRegisterContentRK7QStringPS0_(
    const QQmlJSTypeResolver *self,
    const QQmlJSRegisterContent *scope,
    const QString *name,
    QQmlJSRegisterContent *result) {
  return self->checkEnums(*scope, *name, result);
}

//  bool QQmlJSTypeResolver::canPrimitivelyConvertFromTo(const
//      QQmlJSScope::ConstPtr &from, const QQmlJSScope::ConstPtr &to) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QQmlJSTypeResolver27canPrimitivelyConvertFromToERK22QDeferredSharedPointerIK11QQmlJSScopeES5_(
    const QQmlJSTypeResolver *self,
    const QQmlJSScope::ConstPtr *from,
    const QQmlJSScope::ConstPtr *to) {
  return self->canPrimitivelyConvertFromTo(*from, *to);
}

//  QQmlJSRegisterContent QQmlJSTypeResolver::lengthProperty(bool isWritable,
//      QQmlJSRegisterContent scope) const
extern "C" Q_DECL_EXPORT
QQmlJSRegisterContent *ritual_ZNK18QQmlJSTypeResolver14lengthPropertyEb21QQmlJSRegisterContent(
    const QQmlJSTypeResolver *self,
    bool isWritable,
    const QQmlJSRegisterContent *scope) {
  return new QQmlJSRegisterContent(self->lengthProperty(isWritable, *scope));
}

//  QQmlJSScope::ConstPtr QQmlJSTypeResolver::containedTypeForName(const
//      QString &name) const
extern "C" Q_DECL_EXPORT
QQmlJSScope::ConstPtr *ritual_ZNK18QQmlJSTypeResolver20containedTypeForNameERK7QString(
    const QQmlJSTypeResolver *self,
    const QString *name) {
  return new QQmlJSScope::ConstPtr(self->containedTypeForName(*name));
}

//  QQmlJSRegisterContent QQmlJSTypeResolver::registerContentForName(const
//      QString &name, QQmlJSRegisterContent scopeType) const
extern "C" Q_DECL_EXPORT
QQmlJSRegisterContent *ritual_ZNK18QQmlJSTypeResolver22registerContentForNameERK7QString21QQmlJSRegisterContent(
    const QQmlJSTypeResolver *self,
    const QString *name,
    const QQmlJSRegisterContent *scopeType) {
  return new QQmlJSRegisterContent(
      self->registerContentForName(
          *name,
          *scopeType));
}

//  QQmlJSScope::ConstPtr QQmlJSTypeResolver::resolveParentProperty(const
//      QString &name, const QQmlJSScope::ConstPtr &base, const
//      QQmlJSScope::ConstPtr &propType) const
extern "C" Q_DECL_EXPORT
QQmlJSScope::ConstPtr *ritual_ZNK18QQmlJSTypeResolver21resolveParentPropertyERK7QStringRK22QDeferredSharedPointerIK11QQmlJSScopeES8_(
    const QQmlJSTypeResolver *self,
    const QString *name,
    const QQmlJSScope::ConstPtr *base,
    const QQmlJSScope::ConstPtr *propType) {
  return new QQmlJSScope::ConstPtr(
      self->resolveParentProperty(
          *name,
          *base,
          *propType));
}

//  a QQmlJSScope::ConstPtr a ritual of QQmlJSTypeResolver gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQmlJSTypeResolver__QQmlJSScope_ConstPtr(
    QQmlJSScope::ConstPtr *self) {
  delete self;
}
