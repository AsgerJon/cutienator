//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmldirparser_p.h, Qt 6.12.0. Changes made
//  here are lost.
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
