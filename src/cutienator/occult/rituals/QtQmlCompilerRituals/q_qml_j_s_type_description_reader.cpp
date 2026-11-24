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

//  QStringList
//      QQmlJSTypeDescriptionReader::readStringList(QQmlJS::AST::UiScriptBind
//      ing *ast)
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZN27QQmlJSTypeDescriptionReader14readStringListEPN6QQmlJS3AST15UiScriptBindingE(
    QQmlJSTypeDescriptionReader *self,
    QQmlJS::AST::UiScriptBinding *ast) {
  return new QList<QString>(self->readStringList(ast));
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
