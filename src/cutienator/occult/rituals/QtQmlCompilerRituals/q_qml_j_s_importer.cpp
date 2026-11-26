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
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljscontextualtypes_p.h>
#include <QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljsscope_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmldirparser_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qlist.h>
#include <QtCore/QList>
#include <QtCore/QString>
#include <QtCore/QHash>

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

//  QList<QQmlJS::DiagnosticMessage> QQmlJSImporter::importQmldirs(const
//      QStringList &qmltypesFiles)
extern "C" Q_DECL_EXPORT
QList<QQmlJS::DiagnosticMessage> *ritual_ZN14QQmlJSImporter13importQmldirsERK5QListI7QStringE(
    QQmlJSImporter *self,
    const QList<QString> *qmltypesFiles) {
  return new QList<QQmlJS::DiagnosticMessage>(
      self->importQmldirs(
          *qmltypesFiles));
}

//  QQmlJSScope::Ptr QQmlJSImporter::importFile(const QString &file)
extern "C" Q_DECL_EXPORT
QQmlJSScope::Ptr *ritual_ZN14QQmlJSImporter10importFileERK7QString(
    QQmlJSImporter *self,
    const QString *file) {
  return new QQmlJSScope::Ptr(self->importFile(*file));
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

//  QHash<QString, QQmlJSScope::Ptr> QQmlJSImporter::importedFiles() const
extern "C" Q_DECL_EXPORT
QHash<QString, QQmlJSScope::Ptr> *ritual_ZNK14QQmlJSImporter13importedFilesEv(
    const QQmlJSImporter *self) {
  return new QHash<QString, QQmlJSScope::Ptr>(self->importedFiles());
}

//  ImportedTypes QQmlJSImporter::importModule(const QString &module, quint8
//      precedence, const QString &prefix, QTypeRevision version, QStringList
//      *staticModuleList)
extern "C" Q_DECL_EXPORT
QQmlJSImporter::ImportedTypes *ritual_ZN14QQmlJSImporter12importModuleERK7QStringhS2_13QTypeRevisionP5QListIS0_E(
    QQmlJSImporter *self,
    const QString *module,
    quint8 precedence,
    const QString *prefix,
    const QTypeRevision *version,
    QStringList *staticModuleList) {
  return new QQmlJSImporter::ImportedTypes(
      self->importModule(
          *module,
          precedence,
          *prefix,
          *version,
          staticModuleList));
}

//  ImportedTypes QQmlJSImporter::builtinInternalNames()
extern "C" Q_DECL_EXPORT
QQmlJSImporter::ImportedTypes *ritual_ZN14QQmlJSImporter20builtinInternalNamesEv(
    QQmlJSImporter *self) {
  return new QQmlJSImporter::ImportedTypes(self->builtinInternalNames());
}

//  QList<QQmlJS::DiagnosticMessage> QQmlJSImporter::takeGlobalWarnings()
extern "C" Q_DECL_EXPORT
QList<QQmlJS::DiagnosticMessage> *ritual_ZN14QQmlJSImporter18takeGlobalWarningsEv(
    QQmlJSImporter *self) {
  return new QList<QQmlJS::DiagnosticMessage>(self->takeGlobalWarnings());
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

//  QQmlJSScope::ConstPtr QQmlJSImporter::jsGlobalObject()
extern "C" Q_DECL_EXPORT
QQmlJSScope::ConstPtr *ritual_ZN14QQmlJSImporter14jsGlobalObjectEv(
    QQmlJSImporter *self) {
  return new QQmlJSScope::ConstPtr(self->jsGlobalObject());
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

//  void QQmlJSImporter::setImportVisitor(ImportVisitor visitor)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlJSImporter16setImportVisitorESt8functionIFvPN6QQmlJS3AST4NodeEPS_RKNS_26ImportVisitorPrerequisitesEEE(
    QQmlJSImporter *self,
    const QQmlJSImporter::ImportVisitor *visitor) {
  self->setImportVisitor(*visitor);
}

//  void QQmlJSImporter::setFlags(const QQmlJSImporterFlags &flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlJSImporter8setFlagsERK6QFlagsI18QQmlJSImporterFlagE(
    QQmlJSImporter *self,
    const QQmlJSImporterFlags *flags) {
  self->setFlags(*flags);
}

//  QQmlJSImporterFlags QQmlJSImporter::flags() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QQmlJSImporter5flagsEv(const QQmlJSImporter *self) {
  return static_cast<int>(self->flags().toInt());
}

//  AvailableTypes QQmlJSImporter::builtinImportHelper()
extern "C" Q_DECL_EXPORT
QQmlJSImporter::AvailableTypes *ritual_ZN14QQmlJSImporter19builtinImportHelperEv(
    QQmlJSImporter *self) {
  return new QQmlJSImporter::AvailableTypes(self->builtinImportHelper());
}

//  bool QQmlJSImporter::importHelper(const QString &module, AvailableTypes
//      *types, quint8 precedence, const QString &prefix, QTypeRevision
//      version, bool isDependency, bool isFile)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QQmlJSImporter12importHelperERK7QStringPNS_14AvailableTypesEhS2_13QTypeRevisionbb(
    QQmlJSImporter *self,
    const QString *module,
    QQmlJSImporter::AvailableTypes *types,
    quint8 precedence,
    const QString *prefix,
    const QTypeRevision *version,
    bool isDependency,
    bool isFile) {
  return self->importHelper(
      *module,
      types,
      precedence,
      *prefix,
      *version,
      isDependency,
      isFile);
}

//  void QQmlJSImporter::processImport(const QQmlJS::Import
//      &importDescription, const Import &import, quint8 precedence,
//      AvailableTypes *types)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlJSImporter13processImportERKN6QQmlJS6ImportERKNS_6ImportEhPNS_14AvailableTypesE(
    QQmlJSImporter *self,
    const QQmlJS::Import *importDescription,
    const QQmlJSImporter::Import *import,
    quint8 precedence,
    QQmlJSImporter::AvailableTypes *types) {
  self->processImport(*importDescription, *import, precedence, types);
}

//  void QQmlJSImporter::insertAliases(const QQmlJS::ContextualType &type,
//      QQmlJSImporter::AvailableTypes *types)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlJSImporter13insertAliasesERKN6QQmlJS14ContextualTypeEPNS_14AvailableTypesE(
    const QQmlJS::ContextualType *type,
    QQmlJSImporter::AvailableTypes *types) {
  QQmlJSImporter::insertAliases(*type, types);
}

//  void QQmlJSImporter::insertExport(const QQmlJS::ContextualType &type,
//      const QQmlJS::Export &valExport, const QString &qmlName,
//      QHash<QString, QList<QQmlJSScope::Export>> *seenExports,
//      QQmlJSImporter::AvailableTypes *types) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK14QQmlJSImporter12insertExportERKN6QQmlJS14ContextualTypeERKNS0_6ExportERK7QStringP5QHashIS7_5QListIS4_EEPNS_14AvailableTypesE(
    const QQmlJSImporter *self,
    const QQmlJS::ContextualType *type,
    const QQmlJS::Export *valExport,
    const QString *qmlName,
    QHash<QString, QList<QQmlJSScope::Export>> *seenExports,
    QQmlJSImporter::AvailableTypes *types) {
  self->insertExport(*type, *valExport, *qmlName, seenExports, types);
}

//  QQmlJSScope::Export QQmlJSImporter::resolveConflictingExports(const
//      QQmlJS::Import &importDescription, const QQmlJSExportedScope &val,
//      quint8 precedence, QHash<QString, QList<QQmlJSScope::Export>>
//      *seenExports, QQmlJSImporter::AvailableTypes *types)
extern "C" Q_DECL_EXPORT
QQmlJS::Export *ritual_ZN14QQmlJSImporter25resolveConflictingExportsERKN6QQmlJS6ImportERKNS0_13ExportedScopeI22QDeferredSharedPointerI11QQmlJSScopeEEEhP5QHashI7QString5QListINS0_6ExportEEEPNS_14AvailableTypesE(
    QQmlJSImporter *self,
    const QQmlJS::Import *importDescription,
    const QQmlJSExportedScope *val,
    quint8 precedence,
    QHash<QString, QList<QQmlJSScope::Export>> *seenExports,
    QQmlJSImporter::AvailableTypes *types) {
  return new QQmlJS::Export(
      self->resolveConflictingExports(
          *importDescription,
          *val,
          precedence,
          seenExports,
          types));
}

//  void QQmlJSImporter::insertExportWithConflictingVersion(const
//      QQmlJSExportedScope &val, quint8 precedence, const QString &qmlName,
//      const QQmlJSScope::Export &valExport, const QQmlJSScope::ConstPtr
//      &scope, QHash<QString, QList<QQmlJSScope::Export>> *seenExports,
//      QQmlJSImporter::AvailableTypes *types, SeenVersion seenVersion) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK14QQmlJSImporter34insertExportWithConflictingVersionERKN6QQmlJS13ExportedScopeI22QDeferredSharedPointerI11QQmlJSScopeEEEhRK7QStringRKNS0_6ExportERKS2_IKS3_EP5QHashIS8_5QListISB_EEPNS_14AvailableTypesENS_11SeenVersionE(
    const QQmlJSImporter *self,
    const QQmlJSExportedScope *val,
    quint8 precedence,
    const QString *qmlName,
    const QQmlJS::Export *valExport,
    const QQmlJSScope::ConstPtr *scope,
    QHash<QString, QList<QQmlJSScope::Export>> *seenExports,
    QQmlJSImporter::AvailableTypes *types,
    QQmlJSImporter::SeenVersion seenVersion) {
  self->insertExportWithConflictingVersion(
      *val,
      precedence,
      *qmlName,
      *valExport,
      *scope,
      seenExports,
      types,
      seenVersion);
}

//  SeenVersion QQmlJSImporter::computeSeenVersion(const QQmlJS::Import
//      &importDescription, const QList<QQmlJS::Export> &existingExports,
//      QTypeRevision valExportVersion) const
extern "C" Q_DECL_EXPORT
QQmlJSImporter::SeenVersion ritual_ZNK14QQmlJSImporter18computeSeenVersionERKN6QQmlJS6ImportERK5QListINS0_6ExportEE13QTypeRevision(
    const QQmlJSImporter *self,
    const QQmlJS::Import *importDescription,
    const QList<QQmlJS::Export> *existingExports,
    const QTypeRevision *valExportVersion) {
  return self->computeSeenVersion(
      *importDescription,
      *existingExports,
      *valExportVersion);
}

//  void QQmlJSImporter::insertExports(const QQmlJS::Import
//      &importDescription, const QQmlJSExportedScope &val, const QString
//      &cppName, quint8 precedence, QHash<QString,
//      QList<QQmlJSScope::Export>> *seenExports,
//      QQmlJSImporter::AvailableTypes *types)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlJSImporter13insertExportsERKN6QQmlJS6ImportERKNS0_13ExportedScopeI22QDeferredSharedPointerI11QQmlJSScopeEEERK7QStringhP5QHashISB_5QListINS0_6ExportEEEPNS_14AvailableTypesE(
    QQmlJSImporter *self,
    const QQmlJS::Import *importDescription,
    const QQmlJSExportedScope *val,
    const QString *cppName,
    quint8 precedence,
    QHash<QString, QList<QQmlJSScope::Export>> *seenExports,
    QQmlJSImporter::AvailableTypes *types) {
  self->insertExports(
      *importDescription,
      *val,
      *cppName,
      precedence,
      seenExports,
      types);
}

//  void QQmlJSImporter::importDependencies(const Import &import, quint8
//      precedence, AvailableTypes *types, const QString &prefix,
//      QTypeRevision version, bool isDependency)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlJSImporter18importDependenciesERKNS_6ImportEhPNS_14AvailableTypesERK7QString13QTypeRevisionb(
    QQmlJSImporter *self,
    const QQmlJSImporter::Import *import,
    quint8 precedence,
    QQmlJSImporter::AvailableTypes *types,
    const QString *prefix,
    const QTypeRevision *version,
    bool isDependency) {
  self->importDependencies(
      *import,
      precedence,
      types,
      *prefix,
      *version,
      isDependency);
}

//  QQmlDirParser QQmlJSImporter::createQmldirParserForFile(const QString
//      &filename, Import *import)
extern "C" Q_DECL_EXPORT
QQmlDirParser *ritual_ZN14QQmlJSImporter25createQmldirParserForFileERK7QStringPNS_6ImportE(
    QQmlJSImporter *self,
    const QString *filename,
    QQmlJSImporter::Import *import) {
  return new QQmlDirParser(
      self->createQmldirParserForFile(
          *filename,
          import));
}

//  void QQmlJSImporter::readQmltypes(const QString &filename, Import
//      *result)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlJSImporter12readQmltypesERK7QStringPNS_6ImportE(
    QQmlJSImporter *self,
    const QString *filename,
    QQmlJSImporter::Import *result) {
  self->readQmltypes(*filename, result);
}

//  Import QQmlJSImporter::readQmldir(const QString &dirname)
extern "C" Q_DECL_EXPORT
QQmlJSImporter::Import *ritual_ZN14QQmlJSImporter10readQmldirERK7QString(
    QQmlJSImporter *self,
    const QString *dirname) {
  return new QQmlJSImporter::Import(self->readQmldir(*dirname));
}

//  Import QQmlJSImporter::readDirectory(const QString &directory)
extern "C" Q_DECL_EXPORT
QQmlJSImporter::Import *ritual_ZN14QQmlJSImporter13readDirectoryERK7QString(
    QQmlJSImporter *self,
    const QString *directory) {
  return new QQmlJSImporter::Import(self->readDirectory(*directory));
}

//  QQmlJSScope::Ptr QQmlJSImporter::localFile2QQmlJSScope(const QString
//      &filePath)
extern "C" Q_DECL_EXPORT
QQmlJSScope::Ptr *ritual_ZN14QQmlJSImporter21localFile2QQmlJSScopeERK7QString(
    QQmlJSImporter *self,
    const QString *filePath) {
  return new QQmlJSScope::Ptr(self->localFile2QQmlJSScope(*filePath));
}

//  void QQmlJSImporter::setQualifiedNamesOn(const Import &import)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlJSImporter19setQualifiedNamesOnERKNS_6ImportE(
    const QQmlJSImporter::Import *import) {
  QQmlJSImporter::setQualifiedNamesOn(*import);
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

//  a QList<QQmlJS::DiagnosticMessage> a ritual of QQmlJSImporter gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQmlJSImporter__QList_QQmlJS_DiagnosticMessage(
    QList<QQmlJS::DiagnosticMessage> *self) {
  delete self;
}

//  a QQmlJSScope::Ptr a ritual of QQmlJSImporter gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQmlJSImporter__QQmlJSScope_Ptr(QQmlJSScope::Ptr *self) {
  delete self;
}

//  a QHash<QString, QQmlJSScope::Ptr> a ritual of QQmlJSImporter gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQmlJSImporter__QHash_QString_QQmlJSScope_Ptr(
    QHash<QString, QQmlJSScope::Ptr> *self) {
  delete self;
}

//  a QQmlJSScope::ConstPtr a ritual of QQmlJSImporter gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQmlJSImporter__QQmlJSScope_ConstPtr(
    QQmlJSScope::ConstPtr *self) {
  delete self;
}

//  a QQmlJSImporter::AvailableTypes a ritual of QQmlJSImporter gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQmlJSImporter__QQmlJSImporter_AvailableTypes(
    QQmlJSImporter::AvailableTypes *self) {
  delete self;
}

//  a QQmlJSImporter::Import a ritual of QQmlJSImporter gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQmlJSImporter__QQmlJSImporter_Import(
    QQmlJSImporter::Import *self) {
  delete self;
}
