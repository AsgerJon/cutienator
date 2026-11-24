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
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljsscopesbyid_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qlist.h>

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

//  QQmlJSRegisterContent QQmlJSTypeResolver::jsGlobalObjectContent() const
extern "C" Q_DECL_EXPORT
QQmlJSRegisterContent *ritual_ZNK18QQmlJSTypeResolver21jsGlobalObjectContentEv(
    const QQmlJSTypeResolver *self) {
  return new QQmlJSRegisterContent(self->jsGlobalObjectContent());
}

//  bool QQmlJSTypeResolver::isPrefix(const QString &name) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QQmlJSTypeResolver8isPrefixERK7QString(
    const QQmlJSTypeResolver *self,
    const QString *name) {
  return self->isPrefix(*name);
}

//  QStringList QQmlJSTypeResolver::seenModuleQualifiers() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK18QQmlJSTypeResolver20seenModuleQualifiersEv(
    const QQmlJSTypeResolver *self) {
  return new QList<QString>(self->seenModuleQualifiers());
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

//  bool QQmlJSTypeResolver::isPrimitive(QQmlJSRegisterContent type) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QQmlJSTypeResolver11isPrimitiveE21QQmlJSRegisterContent(
    const QQmlJSTypeResolver *self,
    const QQmlJSRegisterContent *type) {
  return self->isPrimitive(*type);
}

//  bool QQmlJSTypeResolver::isNumeric(QQmlJSRegisterContent type) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QQmlJSTypeResolver9isNumericE21QQmlJSRegisterContent(
    const QQmlJSTypeResolver *self,
    const QQmlJSRegisterContent *type) {
  return self->isNumeric(*type);
}

//  bool QQmlJSTypeResolver::isIntegral(QQmlJSRegisterContent type) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QQmlJSTypeResolver10isIntegralE21QQmlJSRegisterContent(
    const QQmlJSTypeResolver *self,
    const QQmlJSRegisterContent *type) {
  return self->isIntegral(*type);
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

//  bool QQmlJSTypeResolver::canConvertFromTo(QQmlJSRegisterContent from,
//      QQmlJSRegisterContent to) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QQmlJSTypeResolver16canConvertFromToE21QQmlJSRegisterContentS0_(
    const QQmlJSTypeResolver *self,
    const QQmlJSRegisterContent *from,
    const QQmlJSRegisterContent *to) {
  return self->canConvertFromTo(*from, *to);
}

//  QQmlJSRegisterContent QQmlJSTypeResolver::original(QQmlJSRegisterContent
//      type) const
extern "C" Q_DECL_EXPORT
QQmlJSRegisterContent *ritual_ZNK18QQmlJSTypeResolver8originalE21QQmlJSRegisterContent(
    const QQmlJSTypeResolver *self,
    const QQmlJSRegisterContent *type) {
  return new QQmlJSRegisterContent(self->original(*type));
}

//  QQmlJSRegisterContent QQmlJSTypeResolver::shadowed(QQmlJSRegisterContent
//      type) const
extern "C" Q_DECL_EXPORT
QQmlJSRegisterContent *ritual_ZNK18QQmlJSTypeResolver8shadowedE21QQmlJSRegisterContent(
    const QQmlJSTypeResolver *self,
    const QQmlJSRegisterContent *type) {
  return new QQmlJSRegisterContent(self->shadowed(*type));
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

//  QQmlJSRegisterContent QQmlJSTypeResolver::lengthProperty(bool isWritable,
//      QQmlJSRegisterContent scope) const
extern "C" Q_DECL_EXPORT
QQmlJSRegisterContent *ritual_ZNK18QQmlJSTypeResolver14lengthPropertyEb21QQmlJSRegisterContent(
    const QQmlJSTypeResolver *self,
    bool isWritable,
    const QQmlJSRegisterContent *scope) {
  return new QQmlJSRegisterContent(self->lengthProperty(isWritable, *scope));
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
