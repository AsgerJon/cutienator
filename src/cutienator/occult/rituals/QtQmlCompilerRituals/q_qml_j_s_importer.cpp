//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljsimporter_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtQmlCompiler/QtQmlCompiler>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljsimporter_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qtyperevision.h>
#include <QtCore/qlist.h>

//  QQmlJSImporter::QQmlJSImporter(const QStringList &importPaths,
//      QQmlJSResourceFileMapper *mapper, QQmlJSImporterFlags flags)
extern "C" Q_DECL_EXPORT
QQmlJSImporter *ritual_ZN14QQmlJSImporterC1ERK5QListI7QStringEP24QQmlJSResourceFileMapper6QFlagsI18QQmlJSImporterFlagE(
    const QList<QString> *importPaths,
    QQmlJSResourceFileMapper *mapper,
    int flags) {
  return new QQmlJSImporter(
      *importPaths,
      mapper,
      QFlags<QQmlJSImporterFlag>::fromInt(flags));
}

//  const QQmlJSResourceFileMapper *QQmlJSImporter::resourceFileMapper()
//      const
extern "C" Q_DECL_EXPORT
const QQmlJSResourceFileMapper *ritual_ZNK14QQmlJSImporter18resourceFileMapperEv(
    const QQmlJSImporter *self) {
  return self->resourceFileMapper();
}

//  void QQmlJSImporter::setResourceFileMapper(const QQmlJSResourceFileMapper
//      *mapper)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlJSImporter21setResourceFileMapperEPK24QQmlJSResourceFileMapper(
    QQmlJSImporter *self,
    const QQmlJSResourceFileMapper *mapper) {
  self->setResourceFileMapper(mapper);
}

//  QQmlJSResourceFileMapper *QQmlJSImporter::metaDataMapper() const
extern "C" Q_DECL_EXPORT
QQmlJSResourceFileMapper *ritual_ZNK14QQmlJSImporter14metaDataMapperEv(
    const QQmlJSImporter *self) {
  return self->metaDataMapper();
}

//  void QQmlJSImporter::setMetaDataMapper(QQmlJSResourceFileMapper *mapper)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlJSImporter17setMetaDataMapperEP24QQmlJSResourceFileMapper(
    QQmlJSImporter *self,
    QQmlJSResourceFileMapper *mapper) {
  self->setMetaDataMapper(mapper);
}

//  ImportedTypes QQmlJSImporter::importHardCodedBuiltins()
extern "C" Q_DECL_EXPORT
QQmlJSImporter::ImportedTypes *ritual_ZN14QQmlJSImporter23importHardCodedBuiltinsEv(
    QQmlJSImporter *self) {
  return new QQmlJSImporter::ImportedTypes(self->importHardCodedBuiltins());
}

//  ImportedTypes QQmlJSImporter::importDirectory(const QString &directory,
//      quint8 precedence, const QString &prefix)
extern "C" Q_DECL_EXPORT
QQmlJSImporter::ImportedTypes *ritual_ZN14QQmlJSImporter15importDirectoryERK7QStringhS2_(
    QQmlJSImporter *self,
    const QString *directory,
    quint8 precedence,
    const QString *prefix) {
  return new QQmlJSImporter::ImportedTypes(
      self->importDirectory(
          *directory,
          precedence,
          *prefix));
}

//  ImportedTypes QQmlJSImporter::builtinInternalNames()
extern "C" Q_DECL_EXPORT
QQmlJSImporter::ImportedTypes *ritual_ZN14QQmlJSImporter20builtinInternalNamesEv(
    QQmlJSImporter *self) {
  return new QQmlJSImporter::ImportedTypes(self->builtinInternalNames());
}

//  QStringList QQmlJSImporter::importPaths() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK14QQmlJSImporter11importPathsEv(
    const QQmlJSImporter *self) {
  return new QList<QString>(self->importPaths());
}

//  void QQmlJSImporter::setImportPaths(const QStringList &importPaths)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlJSImporter14setImportPathsERK5QListI7QStringE(
    QQmlJSImporter *self,
    const QList<QString> *importPaths) {
  self->setImportPaths(*importPaths);
}

//  void QQmlJSImporter::clearCache()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlJSImporter10clearCacheEv(QQmlJSImporter *self) {
  self->clearCache();
}

//  QString QQmlJSImporter::pathOfModule(const QString &moduleName,
//      QTypeRevision revision) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QQmlJSImporter12pathOfModuleERK7QString13QTypeRevision(
    const QQmlJSImporter *self,
    const QString *moduleName,
    const QTypeRevision *revision) {
  return new QString(self->pathOfModule(*moduleName, *revision));
}

//  void QQmlJSImporter::runImportVisitor(QQmlJS::AST::Node *rootNode, const
//      ImportVisitorPrerequisites &prerequisites)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlJSImporter16runImportVisitorEPN6QQmlJS3AST4NodeERKNS_26ImportVisitorPrerequisitesE(
    QQmlJSImporter *self,
    QQmlJS::AST::Node *rootNode,
    const QQmlJSImporter::ImportVisitorPrerequisites *prerequisites) {
  self->runImportVisitor(rootNode, *prerequisites);
}

//  QQmlJSImporterFlags QQmlJSImporter::flags() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QQmlJSImporter5flagsEv(const QQmlJSImporter *self) {
  return static_cast<int>(self->flags().toInt());
}

//  bool QQmlJSImporter::useOptionalImports() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QQmlJSImporter18useOptionalImportsEv(
    const QQmlJSImporter *self) {
  return self->useOptionalImports();
}

//  bool QQmlJSImporter::preferQmlFilesFromSourceFolder() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QQmlJSImporter30preferQmlFilesFromSourceFolderEv(
    const QQmlJSImporter *self) {
  return self->preferQmlFilesFromSourceFolder();
}

//  QQmlJSImporter::~QQmlJSImporter()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlJSImporterD1Ev(QQmlJSImporter *self) {
  delete self;
}
