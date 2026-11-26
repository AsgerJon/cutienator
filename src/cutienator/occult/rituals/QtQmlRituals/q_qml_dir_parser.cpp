//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmldirparser_p.h, Qt 6.12.0. Edited by hand
//  on 2026-11-25: added by hand, rituals for functions the generator leaves
//  out: 1. Kept as it is when the generator runs again.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmldirparser_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmljsdiagnosticmessage_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qtyperevision.h>
#include <QtCore/qlist.h>
#include <QtCore/QList>
#include <QtCore/QString>
#include <QtCore/QMultiHash>

//  void QQmlDirParser::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQmlDirParser5clearEv(QQmlDirParser *self) {
  self->clear();
}

//  bool QQmlDirParser::parse(const QString &source)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QQmlDirParser5parseERK7QString(
    QQmlDirParser *self,
    const QString *source) {
  return self->parse(*source);
}

//  void QQmlDirParser::disambiguateFileSelectors()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQmlDirParser25disambiguateFileSelectorsEv(
    QQmlDirParser *self) {
  self->disambiguateFileSelectors();
}

//  bool QQmlDirParser::hasError() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QQmlDirParser8hasErrorEv(const QQmlDirParser *self) {
  return self->hasError();
}

//  void QQmlDirParser::setError(const QQmlJS::DiagnosticMessage &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQmlDirParser8setErrorERKN6QQmlJS17DiagnosticMessageE(
    QQmlDirParser *self,
    const QQmlJS::DiagnosticMessage *a0) {
  self->setError(*a0);
}

//  QList<QQmlJS::DiagnosticMessage> QQmlDirParser::errors(const QString
//      &uri) const
extern "C" Q_DECL_EXPORT
QList<QQmlJS::DiagnosticMessage> *ritual_ZNK13QQmlDirParser6errorsERK7QString(
    const QQmlDirParser *self,
    const QString *uri) {
  return new QList<QQmlJS::DiagnosticMessage>(self->errors(*uri));
}

//  bool QQmlDirParser::hasTypeNamespace() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QQmlDirParser16hasTypeNamespaceEv(
    const QQmlDirParser *self) {
  return self->hasTypeNamespace();
}

//  QString QQmlDirParser::typeNamespace() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13QQmlDirParser13typeNamespaceEv(
    const QQmlDirParser *self) {
  return new QString(self->typeNamespace());
}

//  void QQmlDirParser::setTypeNamespace(const QString &s)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQmlDirParser16setTypeNamespaceERK7QString(
    QQmlDirParser *self,
    const QString *s) {
  self->setTypeNamespace(*s);
}

//  void QQmlDirParser::checkNonRelative(const char *item, const QString
//      &typeName, const QString &fileName)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQmlDirParser16checkNonRelativeEPKcRK7QStringS4_(
    const char *item,
    const QString *typeName,
    const QString *fileName) {
  QQmlDirParser::checkNonRelative(item, *typeName, *fileName);
}

//  QMultiHash<QString, Component> QQmlDirParser::components() const
extern "C" Q_DECL_EXPORT
QMultiHash<QString, QQmlDirParser::Component> *ritual_ZNK13QQmlDirParser10componentsEv(
    const QQmlDirParser *self) {
  return new QMultiHash<QString, QQmlDirParser::Component>(
      self->components());
}

//  QList<Import> QQmlDirParser::dependencies() const
extern "C" Q_DECL_EXPORT
QList<QQmlDirParser::Import> *ritual_ZNK13QQmlDirParser12dependenciesEv(
    const QQmlDirParser *self) {
  return new QList<QQmlDirParser::Import>(self->dependencies());
}

//  QList<Import> QQmlDirParser::imports() const
extern "C" Q_DECL_EXPORT
QList<QQmlDirParser::Import> *ritual_ZNK13QQmlDirParser7importsEv(
    const QQmlDirParser *self) {
  return new QList<QQmlDirParser::Import>(self->imports());
}

//  QList<Script> QQmlDirParser::scripts() const
extern "C" Q_DECL_EXPORT
QList<QQmlDirParser::Script> *ritual_ZNK13QQmlDirParser7scriptsEv(
    const QQmlDirParser *self) {
  return new QList<QQmlDirParser::Script>(self->scripts());
}

//  QList<Plugin> QQmlDirParser::plugins() const
extern "C" Q_DECL_EXPORT
QList<QQmlDirParser::Plugin> *ritual_ZNK13QQmlDirParser7pluginsEv(
    const QQmlDirParser *self) {
  return new QList<QQmlDirParser::Plugin>(self->plugins());
}

//  bool QQmlDirParser::designerSupported() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QQmlDirParser17designerSupportedEv(
    const QQmlDirParser *self) {
  return self->designerSupported();
}

//  bool QQmlDirParser::isStaticModule() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QQmlDirParser14isStaticModuleEv(const QQmlDirParser *self) {
  return self->isStaticModule();
}

//  bool QQmlDirParser::isSystemModule() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QQmlDirParser14isSystemModuleEv(const QQmlDirParser *self) {
  return self->isSystemModule();
}

//  QStringList QQmlDirParser::typeInfos() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK13QQmlDirParser9typeInfosEv(
    const QQmlDirParser *self) {
  return new QList<QString>(self->typeInfos());
}

//  QStringList QQmlDirParser::classNames() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK13QQmlDirParser10classNamesEv(
    const QQmlDirParser *self) {
  return new QList<QString>(self->classNames());
}

//  QString QQmlDirParser::preferredPath() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13QQmlDirParser13preferredPathEv(
    const QQmlDirParser *self) {
  return new QString(self->preferredPath());
}

//  QString QQmlDirParser::linkTarget() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13QQmlDirParser10linkTargetEv(const QQmlDirParser *self) {
  return new QString(self->linkTarget());
}

//  void QQmlDirParser::reportError(quint16 line, quint16 column, const
//      QString &message)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQmlDirParser11reportErrorEttRK7QString(
    QQmlDirParser *self,
    quint16 line,
    quint16 column,
    const QString *message) {
  self->reportError(line, column, *message);
}

//  void QQmlDirParser::insertComponentOrScript(const QString &name, const
//      QString &fileName, QTypeRevision version)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQmlDirParser23insertComponentOrScriptERK7QStringS2_13QTypeRevision(
    QQmlDirParser *self,
    const QString *name,
    const QString *fileName,
    const QTypeRevision *version) {
  self->insertComponentOrScript(*name, *fileName, *version);
}

//  QQmlDirParser::~QQmlDirParser()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QQmlDirParserD1Ev(QQmlDirParser *self) {
  delete self;
}

//  a QList<QQmlJS::DiagnosticMessage> a ritual of QQmlDirParser gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQmlDirParser__QList_QQmlJS_DiagnosticMessage(
    QList<QQmlJS::DiagnosticMessage> *self) {
  delete self;
}

//  a QMultiHash<QString, QQmlDirParser::Component> a ritual of QQmlDirParser
//      gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQmlDirParser__QMultiHash_QString_QQmlDirParser_Component(
    QMultiHash<QString, QQmlDirParser::Component> *self) {
  delete self;
}

//  a QList<QQmlDirParser::Import> a ritual of QQmlDirParser gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQmlDirParser__QList_QQmlDirParser_Import(
    QList<QQmlDirParser::Import> *self) {
  delete self;
}

//  a QList<QQmlDirParser::Script> a ritual of QQmlDirParser gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQmlDirParser__QList_QQmlDirParser_Script(
    QList<QQmlDirParser::Script> *self) {
  delete self;
}

//  a QList<QQmlDirParser::Plugin> a ritual of QQmlDirParser gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQmlDirParser__QList_QQmlDirParser_Plugin(
    QList<QQmlDirParser::Plugin> *self) {
  delete self;
}

//  QString QQmlDirParser::scanQuotedWord(const QChar *&ch, quint16
//      lineNumber, quint16 columnNumber)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13QQmlDirParser14scanQuotedWordERPK5QChartt(
    QQmlDirParser *self,
    const QChar **ch,
    quint16 lineNumber,
    quint16 columnNumber) {
  return new QString(
      self->scanQuotedWord(*ch, lineNumber, columnNumber));
}
