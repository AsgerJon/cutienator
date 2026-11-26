//  Written by dev_tooling.RitualGenerator from the records of QtQmlCompiler/
//  6.12.0/QtQmlCompiler/private/qqmljstypedescriptionreader_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtQmlCompiler/QtQmlCompiler>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljstypedescriptionreader_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qtyperevision.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmljssourcelocation_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qlist.h>
#include <QtCore/QList>

//  QString QQmlJSTypeDescriptionReader::tr(const char *sourceText, const
//      char *disambiguation, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN27QQmlJSTypeDescriptionReader2trEPKcS1_i(
    const char *sourceText,
    const char *disambiguation,
    int n) {
  return new QString(
      QQmlJSTypeDescriptionReader::tr(
          sourceText,
          disambiguation,
          n));
}

//  QQmlJSTypeDescriptionReader::QQmlJSTypeDescriptionReader(QString
//      fileName, QString data)
extern "C" Q_DECL_EXPORT
QQmlJSTypeDescriptionReader *ritual_ZN27QQmlJSTypeDescriptionReaderC1E7QStringS0_(
    const QString *fileName,
    const QString *data) {
  return new QQmlJSTypeDescriptionReader(*fileName, *data);
}

//  bool QQmlJSTypeDescriptionReader::operator()(QList<QQmlJSExportedScope>
//      *objects, QStringList *dependencies)
extern "C" Q_DECL_EXPORT
bool ritual_ZN27QQmlJSTypeDescriptionReaderclEP5QListIN6QQmlJS13ExportedScopeI22QDeferredSharedPointerI11QQmlJSScopeEEEEPS0_I7QStringE(
    QQmlJSTypeDescriptionReader *self,
    QList<QQmlJSExportedScope> *objects,
    QStringList *dependencies) {
  return self->operator()(objects, dependencies);
}

//  QString QQmlJSTypeDescriptionReader::errorMessage() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK27QQmlJSTypeDescriptionReader12errorMessageEv(
    const QQmlJSTypeDescriptionReader *self) {
  return new QString(self->errorMessage());
}

//  QString QQmlJSTypeDescriptionReader::warningMessage() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK27QQmlJSTypeDescriptionReader14warningMessageEv(
    const QQmlJSTypeDescriptionReader *self) {
  return new QString(self->warningMessage());
}

//  void QQmlJSTypeDescriptionReader::readDocument(QQmlJS::AST::UiProgram
//      *ast)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQmlJSTypeDescriptionReader12readDocumentEPN6QQmlJS3AST9UiProgramE(
    QQmlJSTypeDescriptionReader *self,
    QQmlJS::AST::UiProgram *ast) {
  self->readDocument(ast);
}

//  void
//      QQmlJSTypeDescriptionReader::readModule(QQmlJS::AST::UiObjectDefiniti
//      on *ast)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQmlJSTypeDescriptionReader10readModuleEPN6QQmlJS3AST18UiObjectDefinitionE(
    QQmlJSTypeDescriptionReader *self,
    QQmlJS::AST::UiObjectDefinition *ast) {
  self->readModule(ast);
}

//  void QQmlJSTypeDescriptionReader::readDependencies(QQmlJS::AST::UiScriptB
//      inding *ast)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQmlJSTypeDescriptionReader16readDependenciesEPN6QQmlJS3AST15UiScriptBindingE(
    QQmlJSTypeDescriptionReader *self,
    QQmlJS::AST::UiScriptBinding *ast) {
  self->readDependencies(ast);
}

//  void QQmlJSTypeDescriptionReader::readComponent(QQmlJS::AST::UiObjectDefi
//      nition *ast)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQmlJSTypeDescriptionReader13readComponentEPN6QQmlJS3AST18UiObjectDefinitionE(
    QQmlJSTypeDescriptionReader *self,
    QQmlJS::AST::UiObjectDefinition *ast) {
  self->readComponent(ast);
}

//  void QQmlJSTypeDescriptionReader::readSignalOrMethod(QQmlJS::AST::UiObjec
//      tDefinition *ast, bool isMethod, const QQmlJSScope::Ptr &scope)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQmlJSTypeDescriptionReader18readSignalOrMethodEPN6QQmlJS3AST18UiObjectDefinitionEbRK22QDeferredSharedPointerI11QQmlJSScopeE(
    QQmlJSTypeDescriptionReader *self,
    QQmlJS::AST::UiObjectDefinition *ast,
    bool isMethod,
    const QQmlJSScope::Ptr *scope) {
  self->readSignalOrMethod(ast, isMethod, *scope);
}

//  void
//      QQmlJSTypeDescriptionReader::readProperty(QQmlJS::AST::UiObjectDefini
//      tion *ast, const QQmlJSScope::Ptr &scope)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQmlJSTypeDescriptionReader12readPropertyEPN6QQmlJS3AST18UiObjectDefinitionERK22QDeferredSharedPointerI11QQmlJSScopeE(
    QQmlJSTypeDescriptionReader *self,
    QQmlJS::AST::UiObjectDefinition *ast,
    const QQmlJSScope::Ptr *scope) {
  self->readProperty(ast, *scope);
}

//  void
//      QQmlJSTypeDescriptionReader::readEnum(QQmlJS::AST::UiObjectDefinition
//      *ast, const QQmlJSScope::Ptr &scope)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQmlJSTypeDescriptionReader8readEnumEPN6QQmlJS3AST18UiObjectDefinitionERK22QDeferredSharedPointerI11QQmlJSScopeE(
    QQmlJSTypeDescriptionReader *self,
    QQmlJS::AST::UiObjectDefinition *ast,
    const QQmlJSScope::Ptr *scope) {
  self->readEnum(ast, *scope);
}

//  void QQmlJSTypeDescriptionReader::readParameter(QQmlJS::AST::UiObjectDefi
//      nition *ast, QQmlJSMetaMethod *metaMethod)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQmlJSTypeDescriptionReader13readParameterEPN6QQmlJS3AST18UiObjectDefinitionEP16QQmlJSMetaMethod(
    QQmlJSTypeDescriptionReader *self,
    QQmlJS::AST::UiObjectDefinition *ast,
    QQmlJSMetaMethod *metaMethod) {
  self->readParameter(ast, metaMethod);
}

//  QString QQmlJSTypeDescriptionReader::readStringBinding(QQmlJS::AST::UiScr
//      iptBinding *ast)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN27QQmlJSTypeDescriptionReader17readStringBindingEPN6QQmlJS3AST15UiScriptBindingE(
    QQmlJSTypeDescriptionReader *self,
    QQmlJS::AST::UiScriptBinding *ast) {
  return new QString(self->readStringBinding(ast));
}

//  bool
//      QQmlJSTypeDescriptionReader::readBoolBinding(QQmlJS::AST::UiScriptBin
//      ding *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN27QQmlJSTypeDescriptionReader15readBoolBindingEPN6QQmlJS3AST15UiScriptBindingE(
    QQmlJSTypeDescriptionReader *self,
    QQmlJS::AST::UiScriptBinding *ast) {
  return self->readBoolBinding(ast);
}

//  double QQmlJSTypeDescriptionReader::readNumericBinding(QQmlJS::AST::UiScr
//      iptBinding *ast)
extern "C" Q_DECL_EXPORT
double ritual_ZN27QQmlJSTypeDescriptionReader18readNumericBindingEPN6QQmlJS3AST15UiScriptBindingE(
    QQmlJSTypeDescriptionReader *self,
    QQmlJS::AST::UiScriptBinding *ast) {
  return self->readNumericBinding(ast);
}

//  QTypeRevision QQmlJSTypeDescriptionReader::readNumericVersionBinding(QQml
//      JS::AST::UiScriptBinding *ast)
extern "C" Q_DECL_EXPORT
QTypeRevision *ritual_ZN27QQmlJSTypeDescriptionReader25readNumericVersionBindingEPN6QQmlJS3AST15UiScriptBindingE(
    QQmlJSTypeDescriptionReader *self,
    QQmlJS::AST::UiScriptBinding *ast) {
  return new QTypeRevision(self->readNumericVersionBinding(ast));
}

//  int
//      QQmlJSTypeDescriptionReader::readIntBinding(QQmlJS::AST::UiScriptBind
//      ing *ast)
extern "C" Q_DECL_EXPORT
int ritual_ZN27QQmlJSTypeDescriptionReader14readIntBindingEPN6QQmlJS3AST15UiScriptBindingE(
    QQmlJSTypeDescriptionReader *self,
    QQmlJS::AST::UiScriptBinding *ast) {
  return self->readIntBinding(ast);
}

//  QList<QQmlJSScope::Export>
//      QQmlJSTypeDescriptionReader::readExports(QQmlJS::AST::UiScriptBinding
//      *ast)
extern "C" Q_DECL_EXPORT
QList<QQmlJSScope::Export> *ritual_ZN27QQmlJSTypeDescriptionReader11readExportsEPN6QQmlJS3AST15UiScriptBindingE(
    QQmlJSTypeDescriptionReader *self,
    QQmlJS::AST::UiScriptBinding *ast) {
  return new QList<QQmlJSScope::Export>(self->readExports(ast));
}

//  void
//      QQmlJSTypeDescriptionReader::readAliases(QQmlJS::AST::UiScriptBinding
//      *ast, const QQmlJSScope::Ptr &scope)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQmlJSTypeDescriptionReader11readAliasesEPN6QQmlJS3AST15UiScriptBindingERK22QDeferredSharedPointerI11QQmlJSScopeE(
    QQmlJSTypeDescriptionReader *self,
    QQmlJS::AST::UiScriptBinding *ast,
    const QQmlJSScope::Ptr *scope) {
  self->readAliases(ast, *scope);
}

//  void
//      QQmlJSTypeDescriptionReader::readInterfaces(QQmlJS::AST::UiScriptBind
//      ing *ast, const QQmlJSScope::Ptr &scope)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQmlJSTypeDescriptionReader14readInterfacesEPN6QQmlJS3AST15UiScriptBindingERK22QDeferredSharedPointerI11QQmlJSScopeE(
    QQmlJSTypeDescriptionReader *self,
    QQmlJS::AST::UiScriptBinding *ast,
    const QQmlJSScope::Ptr *scope) {
  self->readInterfaces(ast, *scope);
}

//  void QQmlJSTypeDescriptionReader::checkMetaObjectRevisions(QQmlJS::AST::U
//      iScriptBinding *ast, QList<QQmlJSScope::Export> *exports)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQmlJSTypeDescriptionReader24checkMetaObjectRevisionsEPN6QQmlJS3AST15UiScriptBindingEP5QListINS0_6ExportEE(
    QQmlJSTypeDescriptionReader *self,
    QQmlJS::AST::UiScriptBinding *ast,
    QList<QQmlJSScope::Export> *exports) {
  self->checkMetaObjectRevisions(ast, exports);
}

//  QStringList
//      QQmlJSTypeDescriptionReader::readStringList(QQmlJS::AST::UiScriptBind
//      ing *ast)
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZN27QQmlJSTypeDescriptionReader14readStringListEPN6QQmlJS3AST15UiScriptBindingE(
    QQmlJSTypeDescriptionReader *self,
    QQmlJS::AST::UiScriptBinding *ast) {
  return new QList<QString>(self->readStringList(ast));
}

//  void QQmlJSTypeDescriptionReader::readDeferredNames(QQmlJS::AST::UiScript
//      Binding *ast, const QQmlJSScope::Ptr &scope)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQmlJSTypeDescriptionReader17readDeferredNamesEPN6QQmlJS3AST15UiScriptBindingERK22QDeferredSharedPointerI11QQmlJSScopeE(
    QQmlJSTypeDescriptionReader *self,
    QQmlJS::AST::UiScriptBinding *ast,
    const QQmlJSScope::Ptr *scope) {
  self->readDeferredNames(ast, *scope);
}

//  void QQmlJSTypeDescriptionReader::readImmediateNames(QQmlJS::AST::UiScrip
//      tBinding *ast, const QQmlJSScope::Ptr &scope)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQmlJSTypeDescriptionReader18readImmediateNamesEPN6QQmlJS3AST15UiScriptBindingERK22QDeferredSharedPointerI11QQmlJSScopeE(
    QQmlJSTypeDescriptionReader *self,
    QQmlJS::AST::UiScriptBinding *ast,
    const QQmlJSScope::Ptr *scope) {
  self->readImmediateNames(ast, *scope);
}

//  void
//      QQmlJSTypeDescriptionReader::readEnumValues(QQmlJS::AST::UiScriptBind
//      ing *ast, QQmlJSMetaEnum *metaEnum)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQmlJSTypeDescriptionReader14readEnumValuesEPN6QQmlJS3AST15UiScriptBindingEP14QQmlJSMetaEnum(
    QQmlJSTypeDescriptionReader *self,
    QQmlJS::AST::UiScriptBinding *ast,
    QQmlJSMetaEnum *metaEnum) {
  self->readEnumValues(ast, metaEnum);
}

//  void QQmlJSTypeDescriptionReader::addError(const QQmlJS::SourceLocation
//      &loc, const QString &message)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQmlJSTypeDescriptionReader8addErrorERKN6QQmlJS14SourceLocationERK7QString(
    QQmlJSTypeDescriptionReader *self,
    const QQmlJS::SourceLocation *loc,
    const QString *message) {
  self->addError(*loc, *message);
}

//  void QQmlJSTypeDescriptionReader::addWarning(const QQmlJS::SourceLocation
//      &loc, const QString &message)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQmlJSTypeDescriptionReader10addWarningERKN6QQmlJS14SourceLocationERK7QString(
    QQmlJSTypeDescriptionReader *self,
    const QQmlJS::SourceLocation *loc,
    const QString *message) {
  self->addWarning(*loc, *message);
}

//  QQmlJS::AST::ArrayPattern
//      *QQmlJSTypeDescriptionReader::getArray(QQmlJS::AST::UiScriptBinding
//      *ast)
extern "C" Q_DECL_EXPORT
QQmlJS::AST::ArrayPattern *ritual_ZN27QQmlJSTypeDescriptionReader8getArrayEPN6QQmlJS3AST15UiScriptBindingE(
    QQmlJSTypeDescriptionReader *self,
    QQmlJS::AST::UiScriptBinding *ast) {
  return self->getArray(ast);
}

//  a QList<QQmlJSScope::Export> a ritual of QQmlJSTypeDescriptionReader gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQmlJSTypeDescriptionReader__QList_QQmlJSScope_Export(
    QList<QQmlJSScope::Export> *self) {
  delete self;
}
